#!/usr/bin/env python3
"""Audit Localize differences between two Limbus Company builds and emit delta packages.

Compares an older ``Localize`` snapshot (``index/localize``, a git revision via
``--old-rev``, or an earlier ``LCB_DANE_*.zip``) against a newer snapshot (an
updated ``index/localize`` or a fresh ``LCB_DANE_*.zip``) using stable
identifier-based JSON addresses from ``tools/localize.py``:

* counts added, removed, modified, and unchanged logical files and translatable
  leaves in ``kr`` (translation source) and ``en`` (reference);
* checks existing Polish translations in ``tlumaczenie/`` to report preserved
  entries, stale entries (``kr`` text changed since translation), and orphaned
  addresses (file or row removed in the new build);
* optionally emits a deterministic delta translator package (``--delta-out``) in
  one of two scopes (``--delta-scope``):
  - ``files`` (default): context-preserving file mode
    (``pakiet_uzupelniajacy_<old>_do_<new>.zip``) containing all impacted files
    with valid existing ``PL:`` lines pre-filled;
  - ``items``: strict incremental mode
    (``pakiet_przyrostowy_<old>_do_<new>.zip``) containing **only** new,
    modified, or stale story scenes, story glossary entries, and view items —
    so updates after ``plik_dla_tlumacza_v2.zip`` never re-send unchanged game
    text.

Stdout and JSON reports contain aggregate counts, build IDs, logical paths, and
structural addresses only — never game prose (``docs/DATA_POLICY.md``).
"""
from __future__ import annotations

import argparse
import contextlib
from dataclasses import dataclass
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
from typing import Iterator
import zipfile

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_package import Glossary, Story, build, pack_zip_bytes, write_zip
from tools.import_zwrotki import (
    GLOSSARY_KIND_RE,
    LocalizeReference,
    PL_LINE_RE,
    SCENE_HEADING_RE,
    SECTION_H2_RE,
    SOURCE_LINE_RE,
    STORY_GLOSSARY_KINDS,
    STORY_REPEAT_RE,
    TranslationStore,
    VIEW_REPEAT_RE,
    is_ai_entry,
    parse_index_manifest,
    sha256_text,
    split_item_head,
)
from tools.localize import Snapshot, field_name, iter_strings, load_json
from tools.package_views import NON_TRANSLATABLE_FIELDS, build_views, encode_view_text
from tools.static_data import StaticData
from tools.story_index import IDENTITY_STEM_RE


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


@contextlib.contextmanager
def checkout_git_localize(rev: str, repo_root: Path = ROOT) -> Iterator[Path]:
    """Extract ``index/localize`` and ``index/MANIFEST.json`` from ``rev`` into a temp directory."""
    raw = subprocess.check_output(
        ["git", "-C", str(repo_root), "archive", "--format=zip", rev, "index/localize", "index/MANIFEST.json"]
    )
    with tempfile.TemporaryDirectory(prefix="lcb_old_rev_") as tmp_dir:
        tmp_path = Path(tmp_dir)
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            zf.extractall(tmp_path)
        yield tmp_path / "index" / "localize"


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


def detect_manifest_hashes(source: Path) -> tuple[str | None, str | None]:
    for candidate in (source / "MANIFEST.json", source.parent / "MANIFEST.json"):
        if candidate.is_file():
            try:
                meta = json.loads(candidate.read_text(encoding="utf-8"))
                _, _, kr_sha, en_sha = parse_index_manifest(meta)
                return kr_sha, en_sha
            except (OSError, UnicodeError, json.JSONDecodeError):
                pass
    return None, None


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
    report, impacted_story, impacted_views, _ = _audit_snapshots_detailed(old_source, new_source, tlumaczenie_dir)
    return report, impacted_story, impacted_views


def _audit_snapshots_detailed(
    old_source: Path,
    new_source: Path,
    tlumaczenie_dir: Path = ROOT / "tlumaczenie",
) -> tuple[dict[str, object], set[str], set[str], set[tuple[str, str]]]:
    old_build = detect_buildid(old_source)
    new_build = detect_buildid(new_source)
    store = TranslationStore.load(tlumaczenie_dir)

    impacted_view_addrs: set[tuple[str, str]] = set()

    with Snapshot.open(old_source) as old_snap, Snapshot.open(new_source) as new_snap:
        kr_diff, kr_impacted = _diff_language(old_snap, new_snap, "kr")
        en_diff, en_impacted = _diff_language(old_snap, new_snap, "en")

        impacted_all = set(kr_impacted) | set(en_impacted)
        for imp_map in (kr_impacted, en_impacted):
            for lf, addrs in imp_map.items():
                if not lf.startswith("StoryData/"):
                    for a in addrs:
                        impacted_view_addrs.add((lf, a))

        preserved = 0
        preserved_human = 0
        preserved_ai = 0
        stale_entries: list[str] = []
        stale_ai_entries: list[str] = []
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
                ai_flag = is_ai_entry(entry)
                expected_sha = entry.get("kr_sha256")
                cur_kr = kr_map.get(addr, "")
                if expected_sha and cur_kr and sha256_text(cur_kr) != expected_sha:
                    if ai_flag:
                        stale_ai_entries.append(f"{lf} :: {addr}")
                    else:
                        stale_entries.append(f"{lf} :: {addr}")
                        impacted_all.add(lf)
                        if not lf.startswith("StoryData/"):
                            impacted_view_addrs.add((lf, addr))
                else:
                    preserved += 1
                    if ai_flag:
                        preserved_ai += 1
                    else:
                        preserved_human += 1

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
            "view_leaf_addresses": len(impacted_view_addrs),
            "story_paths": sorted(impacted_story),
            "view_paths": sorted(impacted_views),
        },
        "translations": {
            "preserved": preserved,
            "preserved_human": preserved_human,
            "preserved_ai": preserved_ai,
            "stale_kr_changed": len(stale_entries),
            "stale_ai_kr_changed": len(stale_ai_entries),
            "orphaned_removed": len(orphaned_entries),
            "stale_addresses": stale_entries,
            "stale_ai_addresses": stale_ai_entries,
            "orphaned_addresses": orphaned_entries,
        },
    }
    return report, impacted_story, impacted_views, impacted_view_addrs


def _encode_story_pl(pl_raw: str, kr_raw: str, en_raw: str) -> str:
    if "\n" in pl_raw and ("\n" in kr_raw or "\n" in en_raw):
        return pl_raw.replace("\n", " / ")
    return pl_raw.replace("\n", "\\n")


def _entry_matches_filter(entry: dict | None, entry_filter: str) -> bool:
    if not entry:
        return False
    if entry_filter == "human":
        return not is_ai_entry(entry)
    if entry_filter == "ai":
        return is_ai_entry(entry)
    if entry_filter == "all":
        return True
    raise ValueError(f"nieznany filtr wpisów: {entry_filter!r}")


def _prefill_story_glossary_md(
    md_text: str,
    store: TranslationStore,
    entry_filter: str = "human",
) -> tuple[str, int, int]:
    """Pre-fill valid existing ``PL:`` lines in ``mowcy-i-miejsca.md``."""
    lines = md_text.splitlines()
    out: list[str] = []
    current_kind: str | None = None
    current_key: str | None = None
    prefilled = 0
    remaining = 0

    for line in lines:
        h2 = SECTION_H2_RE.match(line)
        if h2:
            current_kind = STORY_GLOSSARY_KINDS.get(h2[1])
            current_key = None
            out.append(line)
            continue
        head = split_item_head(line)
        if head is not None:
            current_key = head[2]
            out.append(line)
            continue
        if PL_LINE_RE.match(line) and line.strip() == "PL:":
            filled = False
            if current_kind and current_key is not None:
                entry = store.story_glossary.get(current_kind, {}).get(current_key)
                if _entry_matches_filter(entry, entry_filter):
                    exp_sha = entry.get("kr_sha256")
                    if not (exp_sha and sha256_text(current_key) != exp_sha):
                        out.append(f"   PL: {entry['pl']}")
                        prefilled += 1
                        filled = True
            if not filled:
                remaining += 1
                out.append(line)
            current_key = None
            continue
        out.append(line)

    return "\n".join(out) + "\n", prefilled, remaining


def _prefill_story_md(
    md_text: str,
    store: TranslationStore,
    ref: LocalizeReference,
    entry_filter: str = "human",
) -> tuple[str, int, int]:
    """Pre-fill valid existing ``PL:`` lines in a story chapter Markdown file.

    By default (``entry_filter='human'``), provisional AI entries
    (``"origin": "ai"``) are skipped so the human Translator receives clean
    ``PL:`` blanks.
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
                    if _entry_matches_filter(entry, entry_filter):
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
    entry_filter: str = "human",
) -> tuple[str, int, int]:
    """Pre-fill valid existing ``PL:`` lines in a view Markdown file.

    By default (``entry_filter='human'``), provisional AI entries
    (``"origin": "ai"``) are skipped so the human Translator receives clean
    ``PL:`` blanks.
    """
    lines = md_text.splitlines()
    out: list[str] = []
    cur_file = ""
    cur_primary_addr = ""
    cur_glossary_kind = ""
    is_repeat = False
    in_item = False
    prefilled = 0
    remaining = 0

    for line in lines:
        if split_item_head(line) is not None:
            cur_file = ""
            cur_primary_addr = ""
            cur_glossary_kind = ""
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
            cur_primary_addr = m_src[2].split(" ; ", 1)[0].split(" (+", 1)[0].strip()
            out.append(line)
            continue

        m_gl = GLOSSARY_KIND_RE.match(line)
        if m_gl:
            cur_glossary_kind = m_gl[1].strip()
            out.append(line)
            continue

        if in_item and PL_LINE_RE.match(line) and line.strip() == "PL:":
            in_item = False
            if is_repeat:
                out.append(line)
                continue
            filled = False
            if cur_file and cur_primary_addr:
                kr_raw = ref.leaves("kr", cur_file).get(cur_primary_addr, "")
                en_raw = ref.leaves("en", cur_file).get(cur_primary_addr, "")
                if cur_glossary_kind:
                    gkey = f"{encode_view_text(kr_raw)}\t{encode_view_text(en_raw)}"
                    entry = store.view_glossary.get(cur_glossary_kind, {}).get(gkey)
                else:
                    entry = store.files.get(cur_file, {}).get(cur_primary_addr)
                if _entry_matches_filter(entry, entry_filter):
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


def prefill_bundles(
    scene_files: dict[str, str],
    view_files: dict[str, str] | None,
    localize_path: Path,
    story_index_path: Path,
    tlumaczenie_dir: Path,
    entry_filter: str = "human",
) -> tuple[dict[str, str], dict[str, str] | None, dict[str, int]]:
    """Pre-fill ``PL:`` lines across ``sceny.zip`` and ``widoki.zip`` file maps.

    With ``entry_filter='human'`` (default), provisional AI entries
    (``"origin": "ai"``) are skipped so the human Translator sees blank ``PL:``
    lines everywhere they have not personally translated yet.
    With ``entry_filter='ai'``, only ``"origin": "ai"`` entries are filled and
    files without AI items are omitted (AI verification package).
    """
    store = TranslationStore.load(tlumaczenie_dir)
    base_index = json.loads(story_index_path.read_text(encoding="utf-8"))
    out_scenes: dict[str, str] = {}
    out_views: dict[str, str] | None = {} if view_files is not None else None
    stats = {
        "sceny_wypelnione_pl": 0,
        "sceny_pozostale_pl": 0,
        "slownik_wypelnione_pl": 0,
        "slownik_pozostale_pl": 0,
        "widoki_wypelnione_pl": 0,
        "widoki_pozostale_pl": 0,
    }

    with Snapshot.open(localize_path) as snap:
        aug_index, _ = _augment_story_index(base_index, snap)
        ref = LocalizeReference(snap, aug_index)

        for name, txt in scene_files.items():
            if name.startswith("sceny/") and name.endswith(".md"):
                new_txt, pref, rem = _prefill_story_md(
                    txt, store, ref, entry_filter=entry_filter
                )
                if entry_filter == "ai" and pref == 0:
                    continue
                stats["sceny_wypelnione_pl"] += pref
                stats["sceny_pozostale_pl"] += rem
                out_scenes[name] = new_txt
            elif name == "mowcy-i-miejsca.md":
                new_txt, pref, rem = _prefill_story_glossary_md(
                    txt, store, entry_filter=entry_filter
                )
                if entry_filter == "ai" and pref == 0:
                    continue
                stats["slownik_wypelnione_pl"] += pref
                stats["slownik_pozostale_pl"] += rem
                out_scenes[name] = new_txt
            else:
                out_scenes[name] = txt

        if view_files is not None and out_views is not None:
            for name, txt in view_files.items():
                if name.endswith(".md") and name != "spis-widokow.md":
                    new_txt, pref, rem = _prefill_view_md(
                        txt, store, ref, entry_filter=entry_filter
                    )
                    if entry_filter == "ai" and pref == 0:
                        continue
                    stats["widoki_wypelnione_pl"] += pref
                    stats["widoki_pozostale_pl"] += rem
                    out_views[name] = new_txt
                else:
                    out_views[name] = txt

    stats["lacznie_wypelnione_pl"] = (
        stats["sceny_wypelnione_pl"]
        + stats["slownik_wypelnione_pl"]
        + stats["widoki_wypelnione_pl"]
    )
    stats["lacznie_pozostale_pl"] = (
        stats["sceny_pozostale_pl"]
        + stats["slownik_pozostale_pl"]
        + stats["widoki_pozostale_pl"]
    )
    return out_scenes, out_views, stats


def _augment_story_index(base_index: dict, snap: Snapshot) -> tuple[dict, list[str]]:
    """Place any brand-new ``StoryData/*.json`` stems into ``identity`` (by P1xxNN rule) or ``nieprzypisane``."""
    known_stems: set[str] = set()
    for ch in base_index.get("rozdzialy", []):
        known_stems.update(s["plik"] for s in ch.get("sceny", []))
    for row in base_index.get("identity", []):
        known_stems.update(row.get("pliki", []))
    known_stems.update(base_index.get("nieprzypisane", []))

    extra_stems = sorted(
        PurePosixPath(lf).stem
        for lf in snap.files.get("kr", {})
        if lf.startswith("StoryData/") and PurePosixPath(lf).stem not in known_stems
    )
    if not extra_stems:
        return base_index, []

    identities = [dict(r, pliki=list(r.get("pliki", []))) for r in base_index.get("identity", [])]
    by_pid = {r["identity"]: r for r in identities if isinstance(r.get("identity"), int)}
    rest = list(base_index.get("nieprzypisane", []))

    for stem in extra_stems:
        m = IDENTITY_STEM_RE.fullmatch(stem)
        if m:
            cid = int(m[1]) - 100
            pid = int(m[1] + m[2])
            if pid in by_pid:
                by_pid[pid].setdefault("pliki", []).append(stem)
            else:
                entry = {"postac": cid, "identity": pid, "pliki": [stem], "zrodlo": "regula_nazw"}
                identities.append(entry)
                by_pid[pid] = entry
        else:
            rest.append(stem)

    identities.sort(key=lambda r: (r.get("postac", 0), r.get("identity", 0)))
    return {**base_index, "identity": identities, "nieprzypisane": rest}, extra_stems


def _render_delta_story_glossary(
    full_glossary_md: str,
    delta_keys: set[tuple[str, str]],
) -> tuple[str, int]:
    """Filter ``mowcy-i-miejsca.md`` to ``delta_keys`` while keeping full-game field limits."""
    if not delta_keys:
        return "", 0

    label_to_kind = {lbl: k for k, lbl in Glossary.KINDS}
    lines = full_glossary_md.splitlines()
    out_header = [
        "# Mówcy, tytuły i miejsca — pakiet przyrostowy — Limbus Company",
        "",
        "Wyłącznie **nowe lub zmienione** imiona mówców, tytuły i nazwy miejsc dodane w tej aktualizacji gry.",
        "Tłumaczysz je **raz tutaj**; w plikach scen są pokazane tylko jako kontekst.",
        "",
    ]
    sections: list[str] = []
    total_kept = 0
    cur_kind: str | None = None
    cur_h2 = ""
    cur_limit_line = ""
    sec_items: list[list[str]] = []

    def flush_section() -> None:
        nonlocal total_kept
        if cur_h2 and sec_items:
            sections.extend([cur_h2, ""])
            if cur_limit_line:
                sections.extend([cur_limit_line, ""])
            for idx, item_lines in enumerate(sec_items, 1):
                rewritten = re.sub(r"^\d+\.", f"{idx}.", item_lines[0], count=1)
                sections.append(rewritten)
                sections.extend(item_lines[1:])
                total_kept += 1
            sections.append("")

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            flush_section()
            cur_h2 = line
            cur_kind = label_to_kind.get(line[3:].strip())
            cur_limit_line = ""
            sec_items = []
            i += 1
            continue
        if line.startswith("Limit pola:"):
            cur_limit_line = line
            i += 1
            continue
        parsed = split_item_head(line)
        if parsed is not None and cur_kind is not None:
            _, _, src_key = parsed
            block = [line]
            i += 1
            while i < len(lines) and lines[i].startswith("   "):
                block.append(lines[i])
                i += 1
            if (cur_kind, src_key) in delta_keys:
                sec_items.append(block)
            continue
        i += 1
    flush_section()

    if total_kept == 0:
        return "", 0
    return "\n".join(out_header + sections).rstrip() + "\n", total_kept


def _format_audit_markdown(
    report: dict[str, object],
    delta_stats: dict[str, int],
    delta_scope: str = "files",
) -> str:
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

    scope_desc = (
        "Ten **pakiet przyrostowy** zawiera **wyłącznie nowe i zmienione pozycje** względem poprzedniego wydania "
        "(bez powtarzania niezmienionych tekstów z wcześniejszego pakietu bazowego)."
        if delta_scope == "items"
        else "Ten pakiet uzupełniający zawiera **wyłącznie pliki dotknięte aktualizacją gry**. "
        "Wiersze przetłumaczone wcześniej, których tekst koreański (`KR`) nie uległ zmianie, "
        "mają już wstępnie wypełnione `PL:` jako kontekst — tłumacz uzupełnia tylko puste pola `PL:`."
    )

    lines = [
        f"# Audyt aktualizacji Limbus Company (`{old_b}` → `{new_b}`)",
        "",
        scope_desc,
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
        "## Zawartość pakietu",
        "",
        f"- Tryb pakietu: **`{delta_scope}`**",
        f"- Dotknięte sceny fabularne (`StoryData/*.json`): **{imp['story_scenes']}** "
        f"(plików `.md` w `sceny.zip`: **{delta_stats['story_md_files']}**, nowych wpisów słownika mówców: **{delta_stats.get('story_glossary_items', 0)}**)",
        f"- Dotknięte pliki widoków/UI/umiejętności: **{imp['view_files']}** "
        f"(dotkniętych adresów JSON: **{imp.get('view_leaf_addresses', 0)}**, plików `.md` w `widoki.zip`: **{delta_stats['view_md_files']}**)",
        f"- Puste pola `PL:` do przetłumaczenia w tym pakiecie: **{delta_stats['blank_pl_items']}**",
        f"- Wstępnie wypełnione pola `PL:` (kontekst z wcześniejszych zwrotek): **{delta_stats['prefilled_pl_items']}**",
        "",
    ]
    return "\n".join(lines)


def _format_incremental_readme(report: dict[str, object], delta_stats: dict[str, int]) -> str:
    old_b = report["old_buildid"]
    new_b = report["new_buildid"]
    imp = report["impacted_logical_files"]
    assert isinstance(imp, dict)
    return "\n".join([
        f"# Pakiet przyrostowy dla Tłumacza — Limbus Company (`{old_b}` → `{new_b}`)",
        "",
        "Ten pakiet zawiera **wyłącznie nowości i poprawki tekstowe** wprowadzone w aktualizacji gry",
        f"ze Steam `buildid` **`{old_b}`** do **`{new_b}`**.",
        "",
        "- **Nie zastępuje** on pełnego pakietu bazowego (`plik_dla_tlumacza_v2.zip`), lecz go **uzupełnia**:",
        "  niezmienione sceny, karty, słowa kluczowe i napisy UI z poprzedniej wersji nie są tu powtórzone.",
        "- Sposób pracy jest **identyczny** jak w pakiecie bazowym:",
        "  1. Rozpakuj `sceny.zip` i/lub `widoki.zip`.",
        "  2. Wpisuj polski przekład wyłącznie w liniach `   PL: ` (w jednej linii; łamanie wiersza zapisuj jako `\\n`).",
        "  3. Zostaw puste elementy oznaczone jako `(powtórzenie elementu …)` — tłumaczenie odziedziczy się automatycznie.",
        "  4. Zachowaj bez zmian tagi techniczne wskazane w `tokeny:` (`[Sinking]`, `<style=\"highlight\">`, `{0}` itp.).",
        "  5. Odeślij przetłumaczone pliki `.md` lub spakowany `.zip`.",
        "",
        "## Co znajduje się w środku",
        "",
        f"- `sceny.zip` — **{imp['story_scenes']}** nowych/zmienionych scen fabularnych "
        f"(`{delta_stats['story_md_files']}` plików `.md`) + **{delta_stats.get('story_glossary_items', 0)}** nowych wpisów w `mowcy-i-miejsca.md`.",
        f"- `widoki.zip` — elementy z **{imp['view_files']}** nowych/zmienionych plików niefabularnych "
        f"(`{delta_stats['view_md_files']}` plików `.md` + `spis-widokow.md`).",
        f"- Łącznie pustych pól `PL:` do przetłumaczenia w całej paczce przyrostowej: **{delta_stats['blank_pl_items']}**.",
        "- `AUDYT_AKTUALIZACJI.md` — szczegółowe zestawienie liczbowe zmian między wersjami.",
        "- `MANIFEST.json` — metadane wersji i sumy kontrolne do automatycznego importu zwrotki.",
        "",
    ])


def build_delta_package(
    new_source: Path,
    report: dict[str, object],
    impacted_story: set[str],
    impacted_views: set[str],
    delta_out_dir: Path,
    story_index_path: Path = ROOT / "wiedza" / "indeks_fabuly.json",
    static_data_path: Path = ROOT / "index" / "static-data",
    tlumaczenie_dir: Path = ROOT / "tlumaczenie",
    old_source: Path | None = None,
    impacted_view_addrs: set[tuple[str, str]] | None = None,
    delta_scope: str = "files",
    zip_name: str | None = None,
) -> dict[str, object]:
    """Emit delta translator ZIP in ``files`` or ``items`` scope."""
    if delta_scope not in {"files", "items"}:
        raise ValueError(f"unsupported delta_scope: {delta_scope!r}")

    base_index = json.loads(story_index_path.read_text(encoding="utf-8"))
    store = TranslationStore.load(tlumaczenie_dir)
    static = StaticData(static_data_path) if static_data_path and static_data_path.exists() else None

    with Snapshot.open(new_source) as new_snap:
        effective_index, extra_stems = _augment_story_index(base_index, new_snap)
        ref = LocalizeReference(new_snap, effective_index)
        impacted_stems = {PurePosixPath(lf).stem for lf in impacted_story}

        prefilled_total = 0
        blank_total = 0
        story_content_mds = 0
        story_glossary_items = 0
        filtered_scenes: dict[str, str] = {}

        if delta_scope == "items":
            delta_index = {
                **effective_index,
                "rozdzialy": [
                    {**ch, "sceny": [s for s in ch.get("sceny", []) if s["plik"] in impacted_stems]}
                    for ch in effective_index.get("rozdzialy", [])
                    if any(s["plik"] in impacted_stems for s in ch.get("sceny", []))
                ],
                "identity": [
                    {**row, "pliki": [s for s in row.get("pliki", []) if s in impacted_stems]}
                    for row in effective_index.get("identity", [])
                    if any(s in impacted_stems for s in row.get("pliki", []))
                ],
                "nieprzypisane": [
                    s for s in effective_index.get("nieprzypisane", []) if s in impacted_stems
                ],
            }
            delta_scenes_raw, _ = build(delta_index, Story(new_snap))
            full_scenes_for_gl, _ = build(effective_index, Story(new_snap))

            delta_gl_keys: set[tuple[str, str]] = set()
            if old_source is not None:
                with Snapshot.open(old_source) as old_snap:
                    old_eff_index, _ = _augment_story_index(base_index, old_snap)
                    old_ref = LocalizeReference(old_snap, old_eff_index)
                    old_gl = old_ref.story_glossary_expected
                new_gl = ref.story_glossary_expected
                for k, v in new_gl.items():
                    if k not in old_gl or old_gl[k] != v:
                        delta_gl_keys.add(k)
            else:
                delta_gl_keys = set(ref.story_glossary_expected)

            for kind, entries in store.story_glossary.items():
                for sk, meta in entries.items():
                    if (kind, sk) in ref.story_glossary_expected:
                        if meta.get("kr_sha256") and meta["kr_sha256"] != sha256_text(sk):
                            delta_gl_keys.add((kind, sk))

            gl_md, story_glossary_items = _render_delta_story_glossary(
                full_scenes_for_gl.get("mowcy-i-miejsca.md", ""),
                delta_gl_keys,
            )

            for md_name, md_body in delta_scenes_raw.items():
                if md_name in ("spis-rozdzialow.md", "spis-scen.md"):
                    filtered_scenes[md_name] = md_body
                    continue
                if md_name == "mowcy-i-miejsca.md":
                    if gl_md:
                        filtered_scenes[md_name] = gl_md
                        blank_total += story_glossary_items
                    continue
                updated_md, pre, rem = _prefill_story_md(md_body, store, ref)
                filtered_scenes[md_name] = updated_md
                prefilled_total += pre
                blank_total += rem
                story_content_mds += 1

            eff_addrs = impacted_view_addrs if impacted_view_addrs is not None else set()
            delta_views_raw, _ = build_views(new_snap, static, include_addrs=eff_addrs)
            filtered_views: dict[str, str] = {}
            view_content_mds = 0
            for md_name, md_body in delta_views_raw.items():
                if md_name == "spis-widokow.md":
                    filtered_views[md_name] = md_body
                    continue
                updated_md, pre, rem = _prefill_view_md(md_body, store, ref)
                filtered_views[md_name] = updated_md
                prefilled_total += pre
                blank_total += rem
                view_content_mds += 1
        else:
            full_scenes, _ = build(effective_index, Story(new_snap))
            full_views, _ = build_views(new_snap, static)

            for md_name, md_body in full_scenes.items():
                if md_name in ("spis-rozdzialow.md", "spis-scen.md"):
                    filtered_scenes[md_name] = md_body
                    continue
                if md_name == "mowcy-i-miejsca.md":
                    if impacted_stems:
                        filtered_scenes[md_name] = md_body
                        story_glossary_items = sum(1 for ln in md_body.splitlines() if ln.strip() == "PL:")
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

            filtered_views = {}
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
        "story_glossary_items": story_glossary_items,
        "view_md_files": view_content_mds,
        "prefilled_pl_items": prefilled_total,
        "blank_pl_items": blank_total,
        "unindexed_new_story_stems": len(extra_stems),
    }

    old_b = str(report["old_buildid"])
    new_b = str(report["new_buildid"])
    kr_sha, en_sha = detect_manifest_hashes(new_source)
    audit_md = _format_audit_markdown(report, delta_stats, delta_scope=delta_scope)
    manifest_obj = {
        "format_version": 1,
        "mode": "delta",
        "delta_scope": delta_scope,
        "old_buildid": old_b,
        "new_buildid": new_b,
        "localize_kr_sha256": kr_sha,
        "localize_en_sha256": en_sha,
        "delta_stats": delta_stats,
        "audit": report,
    }

    payload: dict[str, bytes] = {
        "AUDYT_AKTUALIZACJI.md": audit_md.encode("utf-8"),
        "MANIFEST.json": (json.dumps(manifest_obj, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "sceny.zip": pack_zip_bytes(filtered_scenes),
        "widoki.zip": pack_zip_bytes(filtered_views),
    }
    if delta_scope == "items":
        payload["README.md"] = _format_incremental_readme(report, delta_stats).encode("utf-8")

    delta_out_dir.mkdir(parents=True, exist_ok=True)
    default_name = (
        f"pakiet_przyrostowy_{old_b}_do_{new_b}.zip"
        if delta_scope == "items"
        else f"pakiet_uzupelniajacy_{old_b}_do_{new_b}.zip"
    )
    out_zip = delta_out_dir / (zip_name or default_name)
    write_zip(out_zip, payload)
    raw = out_zip.read_bytes()
    return {
        "zip_path": str(out_zip),
        "zip_bytes": len(raw),
        "zip_sha256": hashlib.sha256(raw).hexdigest(),
        "delta_scope": delta_scope,
        **delta_stats,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    old_group = parser.add_mutually_exclusive_group(required=True)
    old_group.add_argument("--old", type=Path, help="starszy snapshot Localize (katalog lub ZIP zbieracza)")
    old_group.add_argument(
        "--old-rev",
        type=str,
        help="rewizja Git z wcześniejszym index/localize oraz index/MANIFEST.json (budowa czysto z repozytorium)",
    )
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
    parser.add_argument("--delta-out", type=Path, help="opcjonalny katalog wyjściowy dla pakietu uzupełniającego/przyrostowego")
    parser.add_argument(
        "--delta-scope",
        choices=("files", "items"),
        default="files",
        help="zakres pakietu: 'files' = pełne dotknięte pliki z kontekstem PL, 'items' = wyłącznie nowe/zmienione elementy",
    )
    parser.add_argument("--delta-zip-name", type=str, help="opcjonalna nazwa pliku .zip w katalogu --delta-out")
    args = parser.parse_args(argv)

    with contextlib.ExitStack() as stack:
        old_path = (
            stack.enter_context(checkout_git_localize(args.old_rev))
            if args.old_rev
            else args.old
        )
        assert old_path is not None

        report, impacted_story, impacted_views, impacted_view_addrs = _audit_snapshots_detailed(
            old_source=old_path,
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
                old_source=old_path,
                impacted_view_addrs=impacted_view_addrs,
                delta_scope=args.delta_scope,
                zip_name=args.delta_zip_name,
            )
            report["delta_package"] = delta_info

    if args.out_report is not None:
        args.out_report.parent.mkdir(parents=True, exist_ok=True)
        args.out_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    summary = {
        "old_buildid": report["old_buildid"],
        "new_buildid": report["new_buildid"],
        "kr_files": report["kr"]["files"],  # type: ignore[index]
        "kr_leaves": report["kr"]["translatable_leaves"],  # type: ignore[index]
        "en_files": report["en"]["files"],  # type: ignore[index]
        "en_leaves": report["en"]["translatable_leaves"],  # type: ignore[index]
        "impacted_story_scenes": report["impacted_logical_files"]["story_scenes"],  # type: ignore[index]
        "impacted_view_files": report["impacted_logical_files"]["view_files"],  # type: ignore[index]
        "impacted_view_leaf_addresses": report["impacted_logical_files"]["view_leaf_addresses"],  # type: ignore[index]
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
