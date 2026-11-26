#!/usr/bin/env python3
"""Audit Localize differences between two Limbus Company builds and emit delta packages.

Compares an older ``Localize`` snapshot (``index/localize`` or an earlier
``LCB_DANE_*.zip``) against a newer snapshot (a fresh ``LCB_DANE_*.zip`` or
updated ``index/localize``) using stable identifier-based JSON addresses from
``tools/localize.py``:

* counts added, removed, modified, and unchanged logical files and translatable
  leaves in ``kr`` (translation source) and ``en`` (reference);
* checks existing Polish translations in ``tlumaczenie/`` to report preserved
  entries, stale entries (``kr`` text changed since translation), and orphaned
  addresses (file or row removed in the new build);
* optionally emits a deterministic supplementary translator package
  (``--delta-out``) containing ``AUDYT_AKTUALIZACJI.md`` plus filtered
  ``sceny.zip`` and ``widoki.zip`` covering 100% of new, changed, and stale
  items (including any brand-new ``StoryData/*.json`` scenes not yet listed in
  ``wiedza/indeks_fabuly.json``), while pre-filling unchanged ``PL:`` lines in
  impacted files as Polish context.

Stdout and JSON reports contain aggregate counts, build IDs, logical paths, and
structural addresses only — never game prose (``docs/DATA_POLICY.md``).
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_package import Story, build, pack_zip_bytes, write_zip
from tools.import_zwrotki import (
    LocalizeReference,
    PL_LINE_RE,
    SCENE_HEADING_RE,
    SOURCE_LINE_RE,
    STORY_REPEAT_RE,
    TranslationStore,
    VIEW_REPEAT_RE,
    parse_index_manifest,
    sha256_text,
    split_item_head,
)
from tools.localize import Snapshot, field_name, iter_strings, load_json
from tools.package_views import NON_TRANSLATABLE_FIELDS, build_views, encode_view_text
from tools.static_data import StaticData


ROOT = Path(__file__).resolve().parent.parent
SCENE_PLIK_RE = re.compile(r"^- Plik: `([^`\s]+)\.json`\s*$")


@dataclass
class LangDiff:
    added_files: list[str]
    removed_files: list[str]
    modified_files: list[str]
    unchanged_files: int
    added_leaves: int
    removed_leaves: int
    changed_leaves: int
    unchanged_leaves: int

    def to_dict(self) -> dict[str, object]:
        return {
            "files": {
                "added": len(self.added_files),
                "removed": len(self.removed_files),
                "modified": len(self.modified_files),
                "unchanged": self.unchanged_files,
            },
            "translatable_leaves": {
                "added": self.added_leaves,
                "removed": self.removed_leaves,
                "changed": self.changed_leaves,
                "unchanged": self.unchanged_leaves,
            },
            "added_file_paths": self.added_files,
            "removed_file_paths": self.removed_files,
            "modified_file_paths": self.modified_files,
        }


def detect_buildid(source: Path) -> str:
    """Read Steam ``buildid`` from a collector ZIP (``RAPORT.json``) or ``MANIFEST.json``."""
    if source.is_file():
        try:
            with zipfile.ZipFile(source) as zf:
                if "RAPORT.json" in zf.namelist():
                    rep = json.loads(zf.read("RAPORT.json").decode("utf-8-sig"))
                    steam = ((rep.get("game") or {}).get("steam") or {}) if isinstance(rep, dict) else {}
                    bid = str(steam.get("buildid") or "")
                    if bid:
                        return bid
        except (OSError, zipfile.BadZipFile, UnicodeError, json.JSONDecodeError):
            pass
        return "unknown"

    for candidate in (source / "MANIFEST.json", source.parent / "MANIFEST.json"):
        if candidate.is_file():
            try:
                meta = json.loads(candidate.read_text(encoding="utf-8"))
                bid, _, _, _ = parse_index_manifest(meta)
                if bid and bid != "unknown":
                    return bid
            except (OSError, UnicodeError, json.JSONDecodeError):
                pass
    return "unknown"


def _translatable_leaves(snapshot: Snapshot, lang: str, logical_file: str) -> dict[str, str]:
    if logical_file not in snapshot.files.get(lang, {}):
        return {}
    doc = load_json(snapshot.read(lang, logical_file))
    out: dict[str, str] = {}
    for addr, val in iter_strings(doc):
        if field_name(addr) in NON_TRANSLATABLE_FIELDS:
            continue
        if not val.strip():
            continue
        out[addr] = val
    return out


def _diff_language(old_snap: Snapshot, new_snap: Snapshot, lang: str) -> tuple[LangDiff, dict[str, set[str]]]:
    old_set = set(old_snap.files.get(lang, {}))
    new_set = set(new_snap.files.get(lang, {}))

    added_files = sorted(new_set - old_set)
    removed_files = sorted(old_set - new_set)
    common_files = sorted(old_set & new_set)

    modified_files: list[str] = []
    unchanged_files = 0
    added_leaves = 0
    removed_leaves = 0
    changed_leaves = 0
    unchanged_leaves = 0
    impacted_addrs: dict[str, set[str]] = {}

    for lf in added_files:
        new_leaves = _translatable_leaves(new_snap, lang, lf)
        added_leaves += len(new_leaves)
        if new_leaves:
            impacted_addrs[lf] = set(new_leaves)

    for lf in removed_files:
        old_leaves = _translatable_leaves(old_snap, lang, lf)
        removed_leaves += len(old_leaves)

    for lf in common_files:
        old_raw = old_snap.read(lang, lf)
        new_raw = new_snap.read(lang, lf)
        if old_raw == new_raw:
            unchanged_files += 1
            unchanged_leaves += len(_translatable_leaves(new_snap, lang, lf))
            continue

        old_leaves = _translatable_leaves(old_snap, lang, lf)
        new_leaves = _translatable_leaves(new_snap, lang, lf)
        old_keys = set(old_leaves)
        new_keys = set(new_leaves)

        f_added = new_keys - old_keys
        f_removed = old_keys - new_keys
        f_changed = {k for k in (old_keys & new_keys) if old_leaves[k] != new_leaves[k]}
        f_unchanged = len(old_keys & new_keys) - len(f_changed)

        added_leaves += len(f_added)
        removed_leaves += len(f_removed)
        changed_leaves += len(f_changed)
        unchanged_leaves += f_unchanged

        if f_added or f_removed or f_changed:
            modified_files.append(lf)
            if f_added or f_changed:
                impacted_addrs[lf] = f_added | f_changed
        else:
            unchanged_files += 1

    return (
        LangDiff(
            added_files=added_files,
            removed_files=removed_files,
            modified_files=modified_files,
            unchanged_files=unchanged_files,
            added_leaves=added_leaves,
            removed_leaves=removed_leaves,
            changed_leaves=changed_leaves,
            unchanged_leaves=unchanged_leaves,
        ),
        impacted_addrs,
    )


def audit_snapshots(
    old_source: Path,
    new_source: Path,
    tlumaczenie_dir: Path = ROOT / "tlumaczenie",
) -> tuple[dict[str, object], set[str], set[str]]:
    """Compare ``old_source`` and ``new_source`` and return ``(report, impacted_story, impacted_views)``."""
    old_build = detect_buildid(old_source)
    new_build = detect_buildid(new_source)
    store = TranslationStore.load(tlumaczenie_dir)

    with Snapshot.open(old_source) as old_snap, Snapshot.open(new_source) as new_snap:
        kr_diff, kr_impacted = _diff_language(old_snap, new_snap, "kr")
        en_diff, en_impacted = _diff_language(old_snap, new_snap, "en")

        impacted_all = set(kr_impacted) | set(en_impacted)

        preserved = 0
        stale_entries: list[str] = []
        orphaned_entries: list[str] = []

        new_kr_files = set(new_snap.files.get("kr", {}))
        new_en_files = set(new_snap.files.get("en", {}))
        new_union_files = new_kr_files | new_en_files

        kr_leaf_cache: dict[str, dict[str, str]] = {}
        en_leaf_cache: dict[str, dict[str, str]] = {}

        def _all_leaves(lang: str, lf: str, cache: dict[str, dict[str, str]]) -> dict[str, str]:
            if lf not in cache:
                if lf in new_snap.files.get(lang, {}):
                    cache[lf] = dict(iter_strings(load_json(new_snap.read(lang, lf))))
                else:
                    cache[lf] = {}
            return cache[lf]

        for lf in sorted(store.files):
            entries = store.files[lf]
            if lf not in new_union_files:
                for addr in sorted(entries):
                    orphaned_entries.append(f"{lf} :: {addr}")
                continue
            kr_map = _all_leaves("kr", lf, kr_leaf_cache)
            en_map = _all_leaves("en", lf, en_leaf_cache)
            for addr in sorted(entries):
                if addr not in kr_map and addr not in en_map:
                    orphaned_entries.append(f"{lf} :: {addr}")
                    continue
                entry = entries[addr]
                expected_sha = entry.get("kr_sha256")
                cur_kr = kr_map.get(addr, "")
                if expected_sha and cur_kr and sha256_text(cur_kr) != expected_sha:
                    stale_entries.append(f"{lf} :: {addr}")
                    impacted_all.add(lf)
                else:
                    preserved += 1

    impacted_story = {f for f in impacted_all if f.startswith("StoryData/")}
    impacted_views = {f for f in impacted_all if not f.startswith("StoryData/")}

    report: dict[str, object] = {
        "old_buildid": old_build,
        "new_buildid": new_build,
        "kr": kr_diff.to_dict(),
        "en": en_diff.to_dict(),
        "impacted_logical_files": {
            "total": len(impacted_all),
            "story_scenes": len(impacted_story),
            "view_files": len(impacted_views),
            "story_paths": sorted(impacted_story),
            "view_paths": sorted(impacted_views),
        },
        "translations": {
            "preserved": preserved,
            "stale_kr_changed": len(stale_entries),
            "orphaned_removed": len(orphaned_entries),
            "stale_addresses": stale_entries,
            "orphaned_addresses": orphaned_entries,
        },
    }
    return report, impacted_story, impacted_views


def _encode_story_pl(pl_raw: str, kr_raw: str, en_raw: str) -> str:
    if "\n" in pl_raw and ("\n" in kr_raw or "\n" in en_raw):
        return pl_raw.replace("\n", " / ")
    return pl_raw.replace("\n", "\\n")


def _prefill_story_md(
    md_text: str,
    store: TranslationStore,
    ref: LocalizeReference,
) -> tuple[str, int, int]:
    """Pre-fill valid existing ``PL:`` lines in a story chapter Markdown file.

    Returns ``(updated_md, prefilled_count, remaining_blank_count)``.
    """
    lines = md_text.splitlines()
    out: list[str] = []
    current_stem = ""
    current_seq: int | None = None
    is_repeat = False
    prefilled = 0
    remaining = 0

    for line in lines:
        m_scene = SCENE_HEADING_RE.match(line)
        if m_scene:
            current_stem = m_scene[1]
            current_seq = None
            is_repeat = False
            out.append(line)
            continue

        head = split_item_head(line)
        if head is not None:
            current_seq = head[0]
            is_repeat = False
            out.append(line)
            continue

        if STORY_REPEAT_RE.match(line):
            is_repeat = True
            out.append(line)
            continue

        if PL_LINE_RE.match(line) and line.strip() == "PL:":
            if is_repeat:
                out.append(line)
                continue
            filled = False
            if current_stem and current_seq is not None:
                logical = f"StoryData/{current_stem}.json"
                pair_info = ref.story_pairs(current_stem).get(current_seq)
                if pair_info is not None:
                    addr, kr_raw, en_raw = pair_info
                    entry = store.files.get(logical, {}).get(addr)
                    if entry:
                        exp_sha = entry.get("kr_sha256")
                        if not (exp_sha and kr_raw and sha256_text(kr_raw) != exp_sha):
                            out.append(f"   PL: {_encode_story_pl(entry['pl'], kr_raw, en_raw)}")
                            prefilled += 1
                            filled = True
            if not filled:
                remaining += 1
                out.append(line)
            current_seq = None
            continue

        out.append(line)

    return "\n".join(out) + "\n", prefilled, remaining


def _prefill_view_md(
    md_text: str,
    store: TranslationStore,
    ref: LocalizeReference,
) -> tuple[str, int, int]:
    """Pre-fill valid existing ``PL:`` lines in a view Markdown file."""
    lines = md_text.splitlines()
    out: list[str] = []
    cur_file = ""
    cur_primary_addr = ""
    is_repeat = False
    in_item = False
    prefilled = 0
    remaining = 0

    for line in lines:
        if split_item_head(line) is not None:
            cur_file = ""
            cur_primary_addr = ""
            is_repeat = False
            in_item = True
            out.append(line)
            continue

        if VIEW_REPEAT_RE.match(line):
            is_repeat = True
            out.append(line)
            continue

        m_src = SOURCE_LINE_RE.match(line)
        if m_src:
            cur_file = m_src[1].strip()
            cur_primary_addr = m_src[2].split(" (+", 1)[0].strip()
            out.append(line)
            continue

        if in_item and PL_LINE_RE.match(line) and line.strip() == "PL:":
            in_item = False
            if is_repeat:
                out.append(line)
                continue
            filled = False
            if cur_file and cur_primary_addr:
                entry = store.files.get(cur_file, {}).get(cur_primary_addr)
                if entry:
                    kr_raw = ref.leaves("kr", cur_file).get(cur_primary_addr, "")
                    exp_sha = entry.get("kr_sha256")
                    if not (exp_sha and kr_raw and sha256_text(kr_raw) != exp_sha):
                        out.append(f"   PL: {encode_view_text(entry['pl'])}")
                        prefilled += 1
                        filled = True
            if not filled:
                remaining += 1
                out.append(line)
            continue

        out.append(line)

    return "\n".join(out) + "\n", prefilled, remaining


def _format_audit_markdown(report: dict[str, object], delta_stats: dict[str, int]) -> str:
    old_b = report["old_buildid"]
    new_b = report["new_buildid"]
    kr = report["kr"]
    en = report["en"]
    tr = report["translations"]
    imp = report["impacted_logical_files"]
    assert isinstance(kr, dict) and isinstance(en, dict) and isinstance(tr, dict) and isinstance(imp, dict)
    kr_f, kr_l = kr["files"], kr["translatable_leaves"]
    en_f, en_l = en["files"], en["translatable_leaves"]
    assert isinstance(kr_f, dict) and isinstance(kr_l, dict)
    assert isinstance(en_f, dict) and isinstance(en_l, dict)

    lines = [
        f"# Audyt aktualizacji Limbus Company (`{old_b}` → `{new_b}`)",
        "",
        "Ten pakiet uzupełniający zawiera **wyłącznie pliki dotknięte aktualizacją gry**.",
        "Wiersze przetłumaczone wcześniej, których tekst koreański (`KR`) nie uległ zmianie,",
        "mają już wstępnie wypełnione `PL:` jako kontekst — tłumacz uzupełnia tylko puste pola `PL:`.",
        "",
        "## Zmiany w danych gry (`Localize`)",
        "",
        "| Język | Nowe pliki | Zmienione pliki | Usunięte pliki | Nowe napisy | Zmienione napisy | Usunięte napisy |",
        "|---|---:|---:|---:|---:|---:|---:|",
        f"| `kr` (źródło) | {kr_f['added']} | {kr_f['modified']} | {kr_f['removed']} | {kr_l['added']} | {kr_l['changed']} | {kr_l['removed']} |",
        f"| `en` (odniesienie) | {en_f['added']} | {en_f['modified']} | {en_f['removed']} | {en_l['added']} | {en_l['changed']} | {en_l['removed']} |",
        "",
        "## Wpływ na dotychczasowe polskie tłumaczenie (`tlumaczenie/`)",
        "",
        f"- Zachowane aktualne wpisy PL: **{tr['preserved']}**",
        f"- Wpisy wymagające rewizji (zmienił się oryginał `KR`): **{tr['stale_kr_changed']}**",
        f"- Osierocone adresy (usunięte w nowym buildzie): **{tr['orphaned_removed']}**",
        "",
        "## Zawartość pakietu uzupełniającego",
        "",
        f"- Dotknięte sceny fabularne (`StoryData/*.json`): **{imp['story_scenes']}** "
        f"(plików `.md` w `sceny.zip`: **{delta_stats['story_md_files']}**)",
        f"- Dotknięte pliki widoków/UI/umiejętności: **{imp['view_files']}** "
        f"(plików `.md` w `widoki.zip`: **{delta_stats['view_md_files']}**)",
        f"- Puste pola `PL:` do przetłumaczenia w tym pakiecie: **{delta_stats['blank_pl_items']}**",
        f"- Wstępnie wypełnione pola `PL:` (kontekst z wcześniejszych zwrotek): **{delta_stats['prefilled_pl_items']}**",
        "",
    ]
    return "\n".join(lines)


def build_delta_package(
    new_source: Path,
    report: dict[str, object],
    impacted_story: set[str],
    impacted_views: set[str],
    delta_out_dir: Path,
    story_index_path: Path = ROOT / "wiedza" / "indeks_fabuly.json",
    static_data_path: Path = ROOT / "index" / "static-data",
    tlumaczenie_dir: Path = ROOT / "tlumaczenie",
) -> dict[str, object]:
    """Emit ``pakiet_uzupelniajacy_<old>_do_<new>.zip`` covering 100% of impacted files."""
    base_index = json.loads(story_index_path.read_text(encoding="utf-8"))
    known_stems: set[str] = set()
    for ch in base_index.get("rozdzialy", []):
        known_stems.update(s["plik"] for s in ch.get("sceny", []))
    for row in base_index.get("identity", []):
        known_stems.update(row.get("pliki", []))
    known_stems.update(base_index.get("nieprzypisane", []))

    store = TranslationStore.load(tlumaczenie_dir)
    static = StaticData(static_data_path) if static_data_path and static_data_path.exists() else None

    with Snapshot.open(new_source) as new_snap:
        # Ensure brand-new StoryData/*.json files not yet in indeks_fabuly.json are never dropped
        extra_stems = sorted(
            PurePosixPath(lf).stem
            for lf in new_snap.files.get("kr", {})
            if lf.startswith("StoryData/") and PurePosixPath(lf).stem not in known_stems
        )
        effective_index = {
            **base_index,
            "nieprzypisane": list(base_index.get("nieprzypisane", [])) + extra_stems,
        }

        ref = LocalizeReference(new_snap, effective_index)
        full_scenes, _ = build(effective_index, Story(new_snap))
        full_views, _ = build_views(new_snap, static)

        impacted_stems = {PurePosixPath(lf).stem for lf in impacted_story}

        filtered_scenes: dict[str, str] = {}
        prefilled_total = 0
        blank_total = 0
        story_content_mds = 0

        for md_name, md_body in full_scenes.items():
            if md_name in ("spis-rozdzialow.md", "spis-scen.md"):
                filtered_scenes[md_name] = md_body
                continue
            if md_name == "mowcy-i-miejsca.md":
                if impacted_stems:
                    filtered_scenes[md_name] = md_body
                continue
            stems_in_md = {
                m[1]
                for line in md_body.splitlines()
                if (m := SCENE_HEADING_RE.match(line)) is not None
            } | {
                m[1]
                for line in md_body.splitlines()
                if (m := SCENE_PLIK_RE.match(line)) is not None
            }
            if stems_in_md & impacted_stems:
                updated_md, pre, rem = _prefill_story_md(md_body, store, ref)
                filtered_scenes[md_name] = updated_md
                prefilled_total += pre
                blank_total += rem
                story_content_mds += 1

        filtered_views: dict[str, str] = {}
        view_content_mds = 0
        for md_name, md_body in full_views.items():
            if md_name == "spis-widokow.md":
                filtered_views[md_name] = md_body
                continue
            if md_name == "mowcy-rpg-i-anomalii.md":
                if any(
                    lf.startswith("RPGSystem/") or PurePosixPath(lf).name.startswith("AbDlg")
                    for lf in impacted_views
                ):
                    filtered_views[md_name] = md_body
                continue
            files_in_md = {
                m[1].strip()
                for line in md_body.splitlines()
                if (m := SOURCE_LINE_RE.match(line)) is not None
            }
            if files_in_md & impacted_views:
                updated_md, pre, rem = _prefill_view_md(md_body, store, ref)
                filtered_views[md_name] = updated_md
                prefilled_total += pre
                blank_total += rem
                view_content_mds += 1

    delta_stats = {
        "story_md_files": story_content_mds,
        "view_md_files": view_content_mds,
        "prefilled_pl_items": prefilled_total,
        "blank_pl_items": blank_total,
        "unindexed_new_story_stems": len(extra_stems),
    }

    old_b = str(report["old_buildid"])
    new_b = str(report["new_buildid"])
    audit_md = _format_audit_markdown(report, delta_stats)
    manifest_obj = {
        "format_version": 1,
        "mode": "delta",
        "old_buildid": old_b,
        "new_buildid": new_b,
        "delta_stats": delta_stats,
        "audit": report,
    }

    payload: dict[str, bytes] = {
        "AUDYT_AKTUALIZACJI.md": audit_md.encode("utf-8"),
        "MANIFEST.json": (json.dumps(manifest_obj, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "sceny.zip": pack_zip_bytes(filtered_scenes),
        "widoki.zip": pack_zip_bytes(filtered_views),
    }
    delta_out_dir.mkdir(parents=True, exist_ok=True)
    out_zip = delta_out_dir / f"pakiet_uzupelniajacy_{old_b}_do_{new_b}.zip"
    write_zip(out_zip, payload)
    raw = out_zip.read_bytes()
    return {
        "zip_path": str(out_zip),
        "zip_bytes": len(raw),
        "zip_sha256": hashlib.sha256(raw).hexdigest(),
        **delta_stats,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--old", type=Path, required=True, help="starszy snapshot Localize (katalog lub ZIP zbieracza)")
    parser.add_argument(
        "--new",
        type=Path,
        default=ROOT / "index" / "localize",
        help="nowszy snapshot Localize (domyślnie: index/localize lub nowy ZIP zbieracza)",
    )
    parser.add_argument("--tlumaczenie", type=Path, default=ROOT / "tlumaczenie")
    parser.add_argument("--index", type=Path, default=ROOT / "wiedza" / "indeks_fabuly.json")
    parser.add_argument("--static-data", type=Path, default=ROOT / "index" / "static-data")
    parser.add_argument("--out-report", type=Path, help="opcjonalna ścieżka zapisu raportu JSON")
    parser.add_argument("--delta-out", type=Path, help="opcjonalny katalog wyjściowy dla pakietu uzupełniającego")
    args = parser.parse_args(argv)

    report, impacted_story, impacted_views = audit_snapshots(
        old_source=args.old,
        new_source=args.new,
        tlumaczenie_dir=args.tlumaczenie,
    )

    if args.delta_out is not None:
        delta_info = build_delta_package(
            new_source=args.new,
            report=report,
            impacted_story=impacted_story,
            impacted_views=impacted_views,
            delta_out_dir=args.delta_out,
            story_index_path=args.index,
            static_data_path=args.static_data,
            tlumaczenie_dir=args.tlumaczenie,
        )
        report["delta_package"] = delta_info

    if args.out_report is not None:
        args.out_report.parent.mkdir(parents=True, exist_ok=True)
        args.out_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Compact prose-free summary on stdout
    summary = {
        "old_buildid": report["old_buildid"],
        "new_buildid": report["new_buildid"],
        "kr_files": report["kr"]["files"],  # type: ignore[index]
        "kr_leaves": report["kr"]["translatable_leaves"],  # type: ignore[index]
        "en_files": report["en"]["files"],  # type: ignore[index]
        "en_leaves": report["en"]["translatable_leaves"],  # type: ignore[index]
        "impacted_story_scenes": report["impacted_logical_files"]["story_scenes"],  # type: ignore[index]
        "impacted_view_files": report["impacted_logical_files"]["view_files"],  # type: ignore[index]
        "translations": {
            k: report["translations"][k]  # type: ignore[index]
            for k in ("preserved", "stale_kr_changed", "orphaned_removed")
        },
    }
    if "delta_package" in report:
        summary["delta_package"] = report["delta_package"]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
