#!/usr/bin/env python3
"""Import translator return Markdown files (``zwrotka``) into ``tlumaczenie/``.

Accepts any combination of ``.md`` files, directories, or ``.zip`` archives
(including nested ``sceny.zip`` / ``widoki.zip``) produced from
``tools/build_package.py`` and validates every item against ``index/localize``
before atomically updating ``tlumaczenie/``:

* source (``kr``) and reference (``en``) lines must match ``index/localize``;
* structural tokens — placeholders (``{0}``, ``%d``, ``%s``), engine keywords
  (``[Sinking]``, ``[WhenUse]``, ...), TextMeshPro tags (``<i>``, ``<color=…>``,
  ``<sprite …>``, ``<link=…>``, ``<font=…>``, ``<ruby=…>``), and Latin
  ``<style="DEN_…">`` in ``BgmLyrics/*`` — must be preserved and balanced;
* file-local ``(powtórzenie elementu N …)`` in ``widoki`` and cross-scene
  ``(powtórzenie elementu N sceny STEM …)`` in ``sceny`` inherit translations
  automatically (even across partial batches);
* any gate violation aborts with exit code ``2`` without modifying
  ``tlumaczenie/``.

Specification: docs/PAKIET_TLUMACZA.md, docs/WORKFLOW.md, docs/LANG_FORMAT.md.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import zipfile

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_package import Glossary, Story, TMP_TAG, clean
from tools.lcb_text import KEYWORD, Texts
from tools.localize import Snapshot, iter_strings, list_row_steps, load_json
from tools.package_views import (
    DEN_STYLE,
    DKR_STYLE,
    PLACEHOLDER,
    ViewGlossary,
    encode_view_text,
    visible_len,
)


ROOT = Path(__file__).resolve().parent.parent
SKIP_MARKDOWN = frozenset({
    "readme.md",
    "audyt_aktualizacji.md",
    "spis-scen.md",
    "spis-rozdzialow.md",
    "spis-widokow.md",
})

STORY_GLOSSARY_KINDS = {label: kind for kind, label in Glossary.KINDS}
SCENE_HEADING_RE = re.compile(r"^## Scena \d+/\d+ — (\S+)\s*$")
SECTION_H2_RE = re.compile(r"^## (.+?)\s*$")
ITEM_START_RE = re.compile(r"^(\d+)\. \[")
LIMIT_RE = re.compile(r"^   limit: do (\d+) znaków\s*$")


def split_item_head(line: str) -> tuple[int, str, str] | None:
    """Parse ``<seq>. [<balanced label>] <text>`` without greedy bracket collision."""
    m = ITEM_START_RE.match(line)
    if not m:
        return None
    seq = int(m[1])
    depth = 1
    pos = m.end()
    while pos < len(line) and depth > 0:
        ch = line[pos]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        pos += 1
    if depth != 0 or pos >= len(line) or line[pos] != " ":
        return None
    return seq, line[m.end() : pos - 1], line[pos + 1 :]
STORY_REPEAT_RE = re.compile(
    r"^   \(powtórzenie elementu (\d+) sceny (\S+) — nie wpisuj tu nic, tłumaczenie dziedziczy się samo\)\s*$"
)
VIEW_REPEAT_RE = re.compile(
    r"^   \(powtórzenie elementu (\d+) — nie wpisuj tu nic, tłumaczenie dziedziczy się samo\)\s*$"
)
SOURCE_LINE_RE = re.compile(r"^   źródło: (.+?) :: (.+?)\s*$")
GLOSSARY_KIND_RE = re.compile(r"^   słownik: (\S+)\s*$")
EN_LINE_RE = re.compile(r"^   EN:(?: (.*))?$")
PL_LINE_RE = re.compile(r"^   PL:(?: (.*))?$")

VOID_TMP_TAGS = frozenset({"br", "sprite"})
TAG_NAME_RE = re.compile(r"^<(/?)([a-zA-Z-]+)")
HANGUL_RE = re.compile(r"[\uac00-\ud7a3\u3131-\u318e]")


def is_story_script_comment(kr_raw: str, en_raw: str, logical_file: str = "") -> bool:
    """Return True for scenario-script ``//…`` markers left verbatim by official EN."""
    stripped = kr_raw.strip()
    return (
        logical_file.startswith("StoryData/")
        and stripped.startswith("//")
        and stripped == en_raw.strip()
    )


def has_unexpected_hangul(
    pl_raw: str, kr_raw: str, en_raw: str, logical_file: str = ""
) -> bool:
    """Return True when ``pl_raw`` keeps Hangul absent from ``en_raw`` (outside ``//`` comments)."""
    if not HANGUL_RE.search(pl_raw):
        return False
    if is_story_script_comment(kr_raw, en_raw, logical_file):
        return False
    if HANGUL_RE.search(en_raw):
        return False
    return True


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def parse_index_manifest(manifest: dict) -> tuple[str, str | None, str | None, str | None]:
    """Extract ``(steam_buildid, zrodlo, kr_sha256, en_sha256)`` from ``index/MANIFEST.json``."""
    loc = manifest.get("localize", {}) if isinstance(manifest, dict) else {}
    zrodlo = loc.get("zrodlo") if isinstance(loc.get("zrodlo"), str) else None
    buildid = str(loc.get("buildid") or "")
    if not buildid and zrodlo:
        match = re.search(r"build\s+Steam\s+(\d+)", zrodlo, flags=re.I)
        if match:
            buildid = match[1]
    langs = loc.get("jezyki") or loc.get("languages") or {}
    kr_sha = (langs.get("kr") or {}).get("sha256")
    en_sha = (langs.get("en") or {}).get("sha256")
    return (buildid or "unknown"), zrodlo, kr_sha, en_sha


def decode_view_text(encoded: str) -> str:
    return encoded.replace("\\n", "\n")


def decode_story_text(pl_line: str, kr_raw: str, en_raw: str) -> str:
    text = pl_line.replace("\\n", "\n")
    if ("\n" in kr_raw or "\n" in en_raw) and " / " in text:
        text = re.sub(r"\s+/\s+", "\n", text)
    return text


def _tag_parts(tag: str) -> tuple[bool, str]:
    match = TAG_NAME_RE.match(tag)
    if not match:
        return False, ""
    return bool(match[1]), match[2].lower()


def _net_tag_counts(raw: str) -> tuple[dict[str, int], list[str]]:
    """Return ``(net_open_minus_close_by_tag, balance_errors_if_zero_net)``."""
    counts: dict[str, int] = {}
    stack: list[str] = []
    order_errors: list[str] = []
    for tok in TMP_TAG.findall(raw):
        is_close, name = _tag_parts(tok)
        if not name or name in VOID_TMP_TAGS:
            continue
        if not is_close:
            counts[name] = counts.get(name, 0) + 1
            stack.append(name)
        else:
            counts[name] = counts.get(name, 0) - 1
            if stack and stack[-1] == name:
                stack.pop()
            elif name in stack:
                order_errors.append(f"nieprawidłowe zagnieżdżenie znacznika </{name}>")
                idx = len(stack) - 1 - stack[::-1].index(name)
                stack.pop(idx)
            else:
                order_errors.append(f"zamknięcie </{name}> bez otwarcia")
    counts = {k: v for k, v in counts.items() if v != 0}
    return counts, order_errors


def validate_tokens(
    pl_raw: str,
    kr_raw: str,
    en_raw: str,
    known_kw_ids: set[str],
    logical_file: str = "",
) -> list[str]:
    """Return a list of structural token/markup errors in ``pl_raw`` (empty = valid)."""
    errors: list[str] = []

    # 1. Placeholders ({0}, %d, %s)
    ph_kr = set(PLACEHOLDER.findall(kr_raw))
    ph_en = set(PLACEHOLDER.findall(en_raw))
    ph_pl = set(PLACEHOLDER.findall(pl_raw))
    allowed_ph = ph_kr | ph_en
    required_ph = (ph_kr & ph_en) if (kr_raw and en_raw) else (ph_kr or ph_en)
    missing_ph = sorted(required_ph - ph_pl)
    extra_ph = sorted(ph_pl - allowed_ph)
    if missing_ph:
        errors.append("brak zmiennych z oryginału: " + ", ".join(missing_ph))
    if extra_ph:
        errors.append("nieznane zmienne spoza oryginału: " + ", ".join(extra_ph))

    # 2. Engine [Keyword] IDs
    kw_kr = {k for k in KEYWORD.findall(kr_raw) if k in known_kw_ids}
    kw_en = {k for k in KEYWORD.findall(en_raw) if k in known_kw_ids}
    kw_pl = {k for k in KEYWORD.findall(pl_raw) if k in known_kw_ids}
    required_kw = (kw_kr & kw_en) if (kr_raw and en_raw) else (kw_kr or kw_en)
    missing_kw = sorted(required_kw - kw_pl)
    if missing_kw:
        errors.append("brak tagów słów kluczowych: " + ", ".join(f"[{k}]" for k in missing_kw))

    # 3. BgmLyrics Latin font style check
    is_lyrics_dkr = (
        logical_file.startswith("BgmLyrics/")
        and bool(DKR_STYLE.search(kr_raw))
        and bool(DEN_STYLE.search(en_raw))
    )
    if is_lyrics_dkr:
        if DKR_STYLE.search(pl_raw):
            errors.append("użyto koreańskiego stylu czcionki DKR zamiast łacińskiego DEN z EN")
        for req_den in DEN_STYLE.findall(en_raw):
            if req_den not in pl_raw:
                errors.append(f"brak wymaganego stylu czcionki z EN: {req_den}")

    # 4. TMP tag balance and structural attribute tags
    net_kr, _ = _net_tag_counts(kr_raw)
    net_en, _ = _net_tag_counts(en_raw)
    net_pl, order_errs = _net_tag_counts(pl_raw)
    valid_nets = [net_kr] + ([net_en] if en_raw else [])
    if net_pl not in valid_nets:
        errors.append(f"niezbalansowane znaczniki TMP w PL ({net_pl}; oczekiwano {net_kr})")
    elif net_pl == {} and order_errs:
        errors.extend(order_errs)

    # Check non-empty <ruby=...> and matching count when source uses ruby
    ruby_kr = re.findall(r"<ruby=([^<>]*)>", kr_raw, flags=re.I)
    ruby_en = re.findall(r"<ruby=([^<>]*)>", en_raw, flags=re.I)
    ruby_pl = re.findall(r"<ruby=([^<>]*)>", pl_raw, flags=re.I)
    if any(not r.strip() for r in ruby_pl):
        errors.append("pusty odczyt w znaczniku <ruby=>")
    expected_ruby_counts = {len(ruby_kr)} | ({len(ruby_en)} if en_raw else set())
    if (ruby_kr or ruby_en) and len(ruby_pl) not in expected_ruby_counts:
        errors.append(f"liczba znaczników <ruby=…> ({len(ruby_pl)}) niezgodna ze źródłem ({sorted(expected_ruby_counts)})")

    # Preserve exact <sprite ...>, <link=...>, <font=...> tags
    for attr_kind in ("sprite", "link", "font"):
        pat = re.compile(rf"<{attr_kind}[= ][^<>]*>", re.I)
        req_kr = set(pat.findall(kr_raw))
        req_en = set(pat.findall(en_raw))
        req_tags = (req_kr & req_en) if (kr_raw and en_raw) else (req_kr or req_en)
        present_pl = set(pat.findall(pl_raw))
        for req in sorted(req_tags - present_pl):
            errors.append(f"brak wymaganego znacznika {req}")

    # 5. Scenario-script '//…' directives in StoryData (e.g. '//효과연출1' in 3D309I2)
    if is_story_script_comment(kr_raw, en_raw, logical_file):
        if pl_raw.strip() != kr_raw.strip():
            errors.append(
                f"znacznik skryptu scenariusza {kr_raw.strip()!r} musi pozostać bez zmian (albo puste PL:)"
            )

    return errors


@dataclass
class ImportWarningItem:
    source_md: str
    item_no: int
    detail: str


@dataclass
class ImportReport:
    files_read: int = 0
    items_seen: int = 0
    translated_items: int = 0
    inherited_repeats: int = 0
    untranslated_items: int = 0
    addresses_updated: int = 0
    story_glossary_updated: int = 0
    view_glossary_updated: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[ImportWarningItem] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "status": "failed" if self.errors else "passed",
            "files_read": self.files_read,
            "items_seen": self.items_seen,
            "translated_items": self.translated_items,
            "inherited_repeats": self.inherited_repeats,
            "untranslated_items": self.untranslated_items,
            "addresses_updated": self.addresses_updated,
            "story_glossary_updated": self.story_glossary_updated,
            "view_glossary_updated": self.view_glossary_updated,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "errors": self.errors,
            "warnings": [
                {"file": w.source_md, "item": w.item_no, "detail": w.detail}
                for w in self.warnings
            ],
        }


def collect_markdown_inputs(paths: list[Path]) -> list[tuple[str, str]]:
    """Read Markdown files from paths (files, directories, or nested ZIPs)."""
    collected: list[tuple[str, str]] = []

    def _read_zip_bytes(label_prefix: str, data: bytes) -> None:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            for info in sorted(zf.infolist(), key=lambda i: i.filename):
                if info.is_dir():
                    continue
                inner_name = PurePosixPath(info.filename).as_posix()
                base_lower = PurePosixPath(inner_name).name.lower()
                full_label = f"{label_prefix}!/{inner_name}" if label_prefix else inner_name
                payload = zf.read(info.filename)
                if base_lower.endswith(".zip"):
                    _read_zip_bytes(full_label, payload)
                elif base_lower.endswith(".md") and base_lower not in SKIP_MARKDOWN:
                    collected.append((full_label, payload.decode("utf-8-sig")))

    for path in paths:
        if not path.exists():
            raise FileNotFoundError(str(path))
        if path.is_file():
            lower = path.name.lower()
            if lower.endswith(".zip"):
                _read_zip_bytes(path.name, path.read_bytes())
            elif lower.endswith(".md"):
                if lower not in SKIP_MARKDOWN:
                    collected.append((path.name, path.read_text(encoding="utf-8-sig")))
            else:
                raise ValueError(f"nieobsługiwany plik wejściowy: {path}")
        elif path.is_dir():
            for child in sorted(path.rglob("*")):
                if not child.is_file():
                    continue
                rel = child.relative_to(path).as_posix()
                lower = child.name.lower()
                if lower.endswith(".zip"):
                    _read_zip_bytes(rel, child.read_bytes())
                elif lower.endswith(".md") and lower not in SKIP_MARKDOWN:
                    collected.append((rel, child.read_text(encoding="utf-8-sig")))
    return collected


class LocalizeReference:
    """Fast lookup index over ``index/localize`` for validating translator returns."""

    def __init__(self, snapshot: Snapshot, index_data: dict) -> None:
        self.snapshot = snapshot
        self.src_files = set(snapshot.files.get("kr", {}))
        self.ref_files = set(snapshot.files.get("en", {}))
        src_texts = Texts(snapshot, "kr")
        ref_texts = Texts(snapshot, "en")
        self.known_kw_ids = set(src_texts.keywords) | set(ref_texts.keywords) | {"ATTRIBUTES"}

        self._leaves_kr: dict[str, dict[str, str]] = {}
        self._leaves_en: dict[str, dict[str, str]] = {}
        self._story_map: dict[str, dict[int, tuple[str, str, str]]] = {}

        # Build expected story glossary keys using the exact build_package.py rules
        story = Story(snapshot)
        glossary = Glossary()
        stems: list[str] = []
        for ch in index_data.get("rozdzialy", []):
            stems.extend(s["plik"] for s in ch.get("sceny", []) if story.src.story(s["plik"]) is not None)
        for row in index_data.get("identity", []):
            stems.extend(s for s in row.get("pliki", []) if story.src.story(s) is not None)
        stems.extend(s for s in index_data.get("nieprzypisane", []) if story.src.story(s) is not None)

        for stem in stems:
            pairs = story.pair(stem)
            for _, src_row, ref_row in pairs:
                pl_s, pl_r = clean(src_row.get("place")), clean(ref_row.get("place"))
                ti_s, ti_r = clean(src_row.get("title")), clean(ref_row.get("title"))
                te_s, te_r = clean(src_row.get("teller")), clean(ref_row.get("teller"))
                text = clean(src_row.get("content"))
                if not text:
                    if pl_s or pl_r:
                        glossary.add("place", pl_s, pl_r, stem)
                    if ti_s or ti_r:
                        glossary.add("title", ti_s, ti_r, stem)
                    if te_s or te_r:
                        glossary.add("teller", te_s, te_r, stem)
                    continue
                who = story.speaker(src_row, ref_row)
                if pl_s or pl_r:
                    glossary.add("place", pl_s, pl_r, stem)
                if ti_s or ti_r:
                    glossary.add("title", ti_s, ti_r, stem)
                if te_s or te_r:
                    glossary.add("teller", te_s, te_r, stem)
                elif isinstance(src_row.get("model"), str) and who:
                    glossary.add("model", who[0], who[1], stem)
        self.story_glossary_expected: dict[tuple[str, str], str] = {
            (kind, key_src): item["ref"]
            for (kind, key_src), item in glossary.items.items()
        }

    def leaves(self, lang: str, logical_file: str) -> dict[str, str]:
        cache = self._leaves_kr if lang == "kr" else self._leaves_en
        if logical_file not in cache:
            files = self.src_files if lang == "kr" else self.ref_files
            if logical_file in files:
                doc = load_json(self.snapshot.read(lang, logical_file))
                cache[logical_file] = dict(iter_strings(doc))
            else:
                cache[logical_file] = {}
        return cache[logical_file]

    def story_pairs(self, stem: str) -> dict[int, tuple[str, str, str]]:
        """Map 1-based Story.pair index -> ``(address, kr_raw, en_raw)``."""
        if stem in self._story_map:
            return self._story_map[stem]
        logical = f"StoryData/{stem}.json"
        if logical not in self.src_files:
            self._story_map[stem] = {}
            return {}
        kr_doc = load_json(self.snapshot.read("kr", logical))
        en_leaves = self.leaves("en", logical)
        kr_rows = kr_doc.get("dataList", []) if isinstance(kr_doc, dict) else []
        mapping: dict[int, tuple[str, str, str]] = {}
        pair_idx = 0
        for step, row in list_row_steps(kr_rows):
            if not isinstance(row, dict) or row.get("id") == -1:
                continue
            pair_idx += 1
            addr = f"dataList{step}.content"
            kr_val = row.get("content", "") if isinstance(row.get("content"), str) else ""
            en_val = en_leaves.get(addr, "")
            mapping[pair_idx] = (addr, kr_val, en_val)
        self._story_map[stem] = mapping
        return mapping


class TranslationStore:
    """In-memory representation of ``tlumaczenie/`` with atomic directory save."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.files: dict[str, dict[str, dict[str, str]]] = {}
        self.story_glossary: dict[str, dict[str, dict[str, str]]] = {
            kind: {} for kind, _ in Glossary.KINDS
        }
        self.view_glossary: dict[str, dict[str, dict[str, str]]] = {
            kind: {} for kind, _ in ViewGlossary.KINDS
        }
        self.story_repeats: dict[str, str] = {}

    @classmethod
    def load(cls, root: Path) -> "TranslationStore":
        store = cls(root)
        if not root.is_dir():
            return store
        slowniki_path = root / "slowniki.json"
        if slowniki_path.is_file():
            data = json.loads(slowniki_path.read_text(encoding="utf-8"))
            for kind, entries in data.get("story", {}).items():
                store.story_glossary.setdefault(kind, {}).update(entries)
            for kind, entries in data.get("views", {}).items():
                store.view_glossary.setdefault(kind, {}).update(entries)
        repeats_path = root / "powtorzenia.json"
        if repeats_path.is_file():
            store.story_repeats.update(json.loads(repeats_path.read_text(encoding="utf-8")))
        pliki_dir = root / "pliki"
        if pliki_dir.is_dir():
            for child in sorted(pliki_dir.rglob("*.json")):
                logical = child.relative_to(pliki_dir).as_posix()
                payload = json.loads(child.read_text(encoding="utf-8"))
                entries = payload.get("entries", {})
                if entries:
                    store.files[logical] = dict(entries)
        return store

    def set_leaf(self, logical_file: str, addr: str, pl: str, kr_raw: str, en_raw: str) -> None:
        bucket = self.files.setdefault(logical_file, {})
        bucket[addr] = {
            "pl": pl,
            "kr_sha256": sha256_text(kr_raw),
            "en_sha256": sha256_text(en_raw),
        }

    def get_leaf(self, logical_file: str, addr: str) -> dict[str, str] | None:
        return self.files.get(logical_file, {}).get(addr)

    def propagate_story_repeats(self, ref: LocalizeReference) -> int:
        propagated = 0
        for target_key, primary_key in sorted(self.story_repeats.items()):
            p_file, p_addr = primary_key.split("::", 1)
            t_file, t_addr = target_key.split("::", 1)
            primary_entry = self.get_leaf(p_file, p_addr)
            if primary_entry is None:
                continue
            kr_raw = ref.leaves("kr", t_file).get(t_addr, "")
            en_raw = ref.leaves("en", t_file).get(t_addr, "")
            existing = self.get_leaf(t_file, t_addr)
            if existing is None or existing.get("pl") != primary_entry["pl"]:
                self.set_leaf(t_file, t_addr, primary_entry["pl"], kr_raw, en_raw)
                propagated += 1
        return propagated

    def save_atomic(self, index_manifest: dict) -> None:
        parent = self.root.parent
        parent.mkdir(parents=True, exist_ok=True)
        staging = parent / f".{self.root.name}.tmp.{os.getpid()}"
        backup = parent / f".{self.root.name}.bak.{os.getpid()}"
        if staging.exists():
            shutil.rmtree(staging)
        if backup.exists():
            shutil.rmtree(backup)

        try:
            staging.mkdir(parents=True)
            pliki_dir = staging / "pliki"
            total_leaves = 0
            for logical_file in sorted(self.files):
                entries = self.files[logical_file]
                if not entries:
                    continue
                ordered = {k: entries[k] for k in sorted(entries)}
                total_leaves += len(ordered)
                out_path = pliki_dir / logical_file
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(
                    json.dumps({"entries": ordered}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )

            slowniki_payload = {
                "story": {
                    k: {sk: self.story_glossary[k][sk] for sk in sorted(self.story_glossary[k])}
                    for k in sorted(self.story_glossary)
                    if self.story_glossary[k]
                },
                "views": {
                    k: {sk: self.view_glossary[k][sk] for sk in sorted(self.view_glossary[k])}
                    for k in sorted(self.view_glossary)
                    if self.view_glossary[k]
                },
            }
            (staging / "slowniki.json").write_text(
                json.dumps(slowniki_payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            if self.story_repeats:
                ordered_repeats = {k: self.story_repeats[k] for k in sorted(self.story_repeats)}
                (staging / "powtorzenia.json").write_text(
                    json.dumps(ordered_repeats, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )

            buildid, zrodlo, kr_sha, en_sha = parse_index_manifest(index_manifest)
            manifest = {
                "format_version": 1,
                "steam_buildid": None if buildid == "unknown" else buildid,
                "zrodlo_localize": zrodlo,
                "localize_kr_sha256": kr_sha,
                "localize_en_sha256": en_sha,
                "translated_files": sum(1 for v in self.files.values() if v),
                "translated_addresses": total_leaves,
                "story_glossary_entries": sum(len(v) for v in self.story_glossary.values()),
                "view_glossary_entries": sum(len(v) for v in self.view_glossary.values()),
                "story_repeat_links": len(self.story_repeats),
            }
            (staging / "MANIFEST.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            if self.root.exists():
                self.root.rename(backup)
            staging.rename(self.root)
            if backup.exists():
                shutil.rmtree(backup)
        except Exception:
            if staging.exists():
                shutil.rmtree(staging)
            if backup.exists() and not self.root.exists():
                backup.rename(self.root)
            raise


def _parse_story_glossary_file(
    source_name: str,
    text: str,
    ref: LocalizeReference,
    store: TranslationStore,
    report: ImportReport,
    allow_older_package: bool = False,
) -> None:
    current_kind: str | None = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        h2 = SECTION_H2_RE.match(line)
        if h2:
            current_kind = STORY_GLOSSARY_KINDS.get(h2[1])
            i += 1
            continue
        parsed_head = split_item_head(line)
        if parsed_head is None:
            i += 1
            continue
        item_no, _, src_key = parsed_head
        report.items_seen += 1
        i += 1
        en_line: str | None = None
        pl_line: str | None = None
        limit_val: int | None = None
        while i < len(lines) and lines[i].startswith("   "):
            sub = lines[i]
            lm = LIMIT_RE.match(sub)
            em = EN_LINE_RE.match(sub)
            pm = PL_LINE_RE.match(sub)
            if lm:
                limit_val = int(lm[1])
            elif em:
                en_line = (em[1] or "").strip()
            elif pm:
                pl_line = (pm[1] or "").strip()
            i += 1

        if current_kind is None:
            report.errors.append(f"{source_name}: element {item_no} poza znaną sekcją słownika")
            continue
        if pl_line is None:
            report.errors.append(f"{source_name}: element {item_no} nie ma linii PL:")
            continue
        if (current_kind, src_key) not in ref.story_glossary_expected:
            if allow_older_package:
                if pl_line:
                    report.warnings.append(
                        ImportWarningItem(
                            source_name,
                            item_no,
                            f"pominięto nieaktualny wpis słownika ({current_kind}: {src_key!r}) ze starszego pakietu",
                        )
                    )
                else:
                    report.untranslated_items += 1
                continue
            report.errors.append(
                f"{source_name}: element {item_no} ({current_kind}: {src_key!r}) nie występuje w bieżącym index/localize"
            )
            continue
        expected_ref = ref.story_glossary_expected[(current_kind, src_key)]
        expected_en_line = expected_ref or "(brak w wersji angielskiej)"
        en_mismatch = en_line not in {expected_en_line, "(brak w wersji angielskiej)"}
        if en_mismatch and not allow_older_package:
            report.errors.append(
                f"{source_name}: element {item_no} ma zmienioną linię EN ({en_line!r} != {expected_en_line!r})"
            )
            continue
        if not pl_line:
            report.untranslated_items += 1
            continue
        if en_mismatch and allow_older_package:
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    item_no,
                    f"zmieniła się referencja EN w nowszym buildzie ({en_line!r} -> {expected_en_line!r})",
                )
            )
            existing_gl = store.story_glossary.get(current_kind, {}).get(src_key)
            if existing_gl and existing_gl.get("en_sha256") == sha256_text(expected_ref):
                continue

        tok_errs = validate_tokens(pl_line, src_key, expected_ref, ref.known_kw_ids)
        if tok_errs:
            for err in tok_errs:
                report.errors.append(f"{source_name}: element {item_no}: {err}")
            continue
        if limit_val and visible_len(pl_line) > limit_val:
            report.warnings.append(
                ImportWarningItem(source_name, item_no, f"przekroczono limit {limit_val} znaków ({visible_len(pl_line)})")
            )
        if has_unexpected_hangul(pl_line, src_key, expected_ref):
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    item_no,
                    "pozostały znaki koreańskie (Hangul) w PL mimo ich braku w EN",
                )
            )
        store.story_glossary.setdefault(current_kind, {})[src_key] = {
            "pl": pl_line,
            "kr_sha256": sha256_text(src_key),
            "en_sha256": sha256_text(expected_ref),
        }
        report.translated_items += 1
        report.story_glossary_updated += 1


def _parse_story_scenes_file(
    source_name: str,
    text: str,
    ref: LocalizeReference,
    store: TranslationStore,
    report: ImportReport,
    allow_older_package: bool = False,
) -> None:
    current_stem: str | None = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        sh = SCENE_HEADING_RE.match(line)
        if sh:
            current_stem = sh[1]
            if not ref.story_pairs(current_stem):
                report.errors.append(f"{source_name}: nieznana scena {current_stem!r}")
            i += 1
            continue
        parsed_head = split_item_head(line)
        if parsed_head is None:
            i += 1
            continue
        pair_idx, _, kr_head = parsed_head
        report.items_seen += 1
        i += 1

        en_line: str | None = None
        pl_line: str | None = None
        limit_val: int | None = None
        repeat_ref: tuple[str, int] | None = None
        unexpected_pl_on_repeat = False

        while i < len(lines) and lines[i].startswith("   "):
            sub = lines[i]
            lm = LIMIT_RE.match(sub)
            rm = STORY_REPEAT_RE.match(sub)
            em = EN_LINE_RE.match(sub)
            pm = PL_LINE_RE.match(sub)
            if lm:
                limit_val = int(lm[1])
            elif rm:
                repeat_ref = (rm[2], int(rm[1]))
            elif em:
                en_line = (em[1] or "").strip()
            elif pm:
                val = (pm[1] or "").strip()
                if repeat_ref is not None and val:
                    unexpected_pl_on_repeat = True
                pl_line = val
            i += 1

        if current_stem is None:
            report.errors.append(f"{source_name}: element {pair_idx} poza nagłówkiem sceny")
            continue
        scene_map = ref.story_pairs(current_stem)
        if pair_idx not in scene_map:
            if allow_older_package:
                if pl_line:
                    report.warnings.append(
                        ImportWarningItem(
                            source_name,
                            pair_idx,
                            f"pominięto usunięty element nr {pair_idx} sceny {current_stem} ze starszego pakietu",
                        )
                    )
                else:
                    report.untranslated_items += 1
                continue
            report.errors.append(f"{source_name}: scena {current_stem} nie ma elementu nr {pair_idx}")
            continue
        addr, kr_raw, en_raw = scene_map[pair_idx]
        expected_kr_clean = clean(kr_raw)
        if kr_head != expected_kr_clean:
            if allow_older_package:
                if repeat_ref is None and pl_line is None:
                    report.errors.append(f"{source_name}: scena {current_stem} el. {pair_idx} nie ma linii PL:")
                    continue
                if pl_line:
                    report.warnings.append(
                        ImportWarningItem(
                            source_name,
                            pair_idx,
                            f"scena {current_stem}: zmienił się oryginał KR w nowszym buildzie — element pominięty, użyj pakietu przyrostowego",
                        )
                    )
                else:
                    report.untranslated_items += 1
                continue
            report.errors.append(
                f"{source_name}: scena {current_stem} el. {pair_idx} ma zmieniony tekst KR ({kr_head!r} != {expected_kr_clean!r})"
            )
            continue

        logical_file = f"StoryData/{current_stem}.json"
        if repeat_ref is not None:
            if unexpected_pl_on_repeat:
                report.errors.append(
                    f"{source_name}: scena {current_stem} el. {pair_idx} jest powtórzeniem — wpisz przekład w elemencie pierwotnym"
                )
                continue
            ref_stem, ref_idx = repeat_ref
            ref_map = ref.story_pairs(ref_stem)
            if ref_idx not in ref_map:
                report.errors.append(
                    f"{source_name}: scena {current_stem} el. {pair_idx} wskazuje nieistniejące powtórzenie {ref_stem}:{ref_idx}"
                )
                continue
            ref_addr, _, _ = ref_map[ref_idx]
            store.story_repeats[f"{logical_file}::{addr}"] = f"StoryData/{ref_stem}.json::{ref_addr}"
            continue

        if pl_line is None:
            report.errors.append(f"{source_name}: scena {current_stem} el. {pair_idx} nie ma linii PL:")
            continue

        expected_en_line = clean(en_raw) or "(brak wersji angielskiej)"
        allowed_en_lines = {expected_en_line}
        if "[#" in addr:
            allowed_en_lines.add("(brak wersji angielskiej)")
        dup_id_match = re.match(r"^dataList\[id=([^#\]]+)(?:#\d+)?\]\.content$", addr)
        if dup_id_match:
            base_id = dup_id_match[1]
            en_file_leaves = ref.leaves("en", logical_file)
            if f"dataList[id={base_id}#2].content" in en_file_leaves:
                for k_addr, k_val in en_file_leaves.items():
                    if k_addr.startswith(f"dataList[id={base_id}") and k_addr.endswith("].content"):
                        allowed_en_lines.add(clean(k_val) or "(brak wersji angielskiej)")
        en_mismatch = en_line not in allowed_en_lines
        if en_mismatch and not allow_older_package:
            report.errors.append(
                f"{source_name}: scena {current_stem} el. {pair_idx} ma zmienioną linię EN ({en_line!r} != {expected_en_line!r})"
            )
            continue
        if not pl_line:
            report.untranslated_items += 1
            continue
        if en_mismatch and allow_older_package:
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    pair_idx,
                    f"scena {current_stem}: zmieniła się referencja EN w nowszym buildzie",
                )
            )
            existing_leaf = store.get_leaf(logical_file, addr)
            if existing_leaf and existing_leaf.get("en_sha256") == sha256_text(en_raw):
                continue

        pl_decoded = decode_story_text(pl_line, kr_raw, en_raw)
        tok_errs = validate_tokens(pl_decoded, kr_raw, en_raw, ref.known_kw_ids, logical_file)
        if tok_errs:
            for err in tok_errs:
                report.errors.append(f"{source_name}: scena {current_stem} el. {pair_idx}: {err}")
            continue
        if limit_val and visible_len(pl_line) > limit_val:
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    pair_idx,
                    f"scena {current_stem}: przekroczono limit {limit_val} znaków ({visible_len(pl_line)})",
                )
            )
        if has_unexpected_hangul(pl_decoded, kr_raw, en_raw, logical_file):
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    pair_idx,
                    f"scena {current_stem}: pozostały znaki koreańskie (Hangul) w PL mimo ich braku w EN",
                )
            )
        store.set_leaf(logical_file, addr, pl_decoded, kr_raw, en_raw)
        report.translated_items += 1
        report.addresses_updated += 1


def _parse_views_file(
    source_name: str,
    text: str,
    ref: LocalizeReference,
    store: TranslationStore,
    report: ImportReport,
    allow_older_package: bool = False,
) -> None:
    lines = text.splitlines()
    parsed_items: list[dict] = []
    i = 0
    while i < len(lines):
        parsed_head = split_item_head(lines[i])
        if parsed_head is None:
            i += 1
            continue
        seq, _, head_text = parsed_head
        report.items_seen += 1
        i += 1

        logical_file: str | None = None
        addrs: list[str] = []
        glossary_kind: str | None = None
        limit_val: int | None = None
        repeat_of: int | None = None
        en_line: str | None = None
        pl_line: str | None = None
        unexpected_pl_on_repeat = False

        while i < len(lines) and lines[i].startswith("   "):
            sub = lines[i]
            sm = SOURCE_LINE_RE.match(sub)
            gm = GLOSSARY_KIND_RE.match(sub)
            lm = LIMIT_RE.match(sub)
            rm = VIEW_REPEAT_RE.match(sub)
            em = EN_LINE_RE.match(sub)
            pm = PL_LINE_RE.match(sub)
            if sm:
                logical_file = sm[1].strip()
                addrs = [a.strip() for a in sm[2].split(" ; ") if a.strip()]
            elif gm:
                glossary_kind = gm[1].strip()
            elif lm:
                limit_val = int(lm[1])
            elif rm:
                repeat_of = int(rm[1])
            elif em:
                en_line = (em[1] or "").strip()
            elif pm:
                val = (pm[1] or "").strip()
                if repeat_of is not None and val:
                    unexpected_pl_on_repeat = True
                pl_line = val
            i += 1

        parsed_items.append({
            "seq": seq,
            "head_text": head_text,
            "logical_file": logical_file,
            "addrs": addrs,
            "glossary_kind": glossary_kind,
            "limit_val": limit_val,
            "repeat_of": repeat_of,
            "en_line": en_line,
            "pl_line": pl_line,
            "unexpected_pl_on_repeat": unexpected_pl_on_repeat,
        })

    resolved_pl_by_seq: dict[int, str] = {}
    for item in parsed_items:
        seq = item["seq"]
        logical_file = item["logical_file"]
        addrs = item["addrs"]
        if not logical_file or not addrs:
            report.errors.append(f"{source_name}: element {seq} nie ma poprawnej linii źródło:")
            continue

        if item["repeat_of"] is not None:
            if item["unexpected_pl_on_repeat"]:
                report.errors.append(
                    f"{source_name}: element {seq} jest powtórzeniem elementu {item['repeat_of']} — nie wpisuj w nim PL:"
                )
                continue
        elif item["pl_line"] is None:
            report.errors.append(f"{source_name}: element {seq} nie ma linii PL:")
            continue

        kr_leaves = ref.leaves("kr", logical_file)
        en_leaves = ref.leaves("en", logical_file)
        missing_addrs = [a for a in addrs if a not in kr_leaves and a not in en_leaves]
        if missing_addrs:
            if allow_older_package:
                present_addrs = [a for a in addrs if a in kr_leaves or a in en_leaves]
                if not present_addrs:
                    if item["repeat_of"] is None and item["pl_line"]:
                        resolved_pl_by_seq[seq] = item["pl_line"]
                        report.warnings.append(
                            ImportWarningItem(
                                source_name,
                                seq,
                                f"pominięto usunięty adres w {logical_file}: {missing_addrs[0]}",
                            )
                        )
                    elif item["repeat_of"] is None:
                        report.untranslated_items += 1
                    continue
                addrs = present_addrs
            else:
                report.errors.append(
                    f"{source_name}: element {seq} wskazuje nieistniejący adres w {logical_file}: {missing_addrs[0]}"
                )
                continue

        first_addr = addrs[0]
        kr_raw = kr_leaves.get(first_addr, "")
        en_raw = en_leaves.get(first_addr, "")
        src_enc = encode_view_text(kr_raw)
        ref_enc = encode_view_text(en_raw)

        if item["glossary_kind"]:
            expected_head = src_enc or f"{ref_enc} (tylko EN)"
        else:
            expected_head = src_enc if src_enc else ref_enc
        if item["head_text"] != expected_head:
            if allow_older_package:
                if item["repeat_of"] is None and item["pl_line"]:
                    resolved_pl_by_seq[seq] = item["pl_line"]
                    report.warnings.append(
                        ImportWarningItem(
                            source_name,
                            seq,
                            f"{logical_file}: zmienił się tekst źródłowy w nowszym buildzie — element pominięty, użyj pakietu przyrostowego",
                        )
                    )
                elif item["repeat_of"] is None:
                    report.untranslated_items += 1
                continue
            report.errors.append(
                f"{source_name}: element {seq} ma zmieniony tekst źródłowy ({item['head_text']!r} != {expected_head!r})"
            )
            continue

        en_mismatch = False
        if item["repeat_of"] is not None:
            primary_seq = item["repeat_of"]
            if primary_seq not in resolved_pl_by_seq:
                continue
            pl_encoded = resolved_pl_by_seq[primary_seq]
            is_repeat = True
        else:
            expected_en_line = ref_enc or "(brak wersji angielskiej)"
            en_mismatch = item["en_line"] != expected_en_line
            if en_mismatch and not allow_older_package:
                report.errors.append(
                    f"{source_name}: element {seq} ma zmienioną linię EN ({item['en_line']!r} != {expected_en_line!r})"
                )
                continue
            if not item["pl_line"]:
                report.untranslated_items += 1
                continue
            pl_encoded = item["pl_line"]
            resolved_pl_by_seq[seq] = pl_encoded
            is_repeat = False
            if en_mismatch and allow_older_package:
                report.warnings.append(
                    ImportWarningItem(
                        source_name,
                        seq,
                        f"{logical_file}: zmieniła się referencja EN w nowszym buildzie",
                    )
                )

        pl_decoded = decode_view_text(pl_encoded)
        tok_errs = validate_tokens(pl_decoded, kr_raw, en_raw, ref.known_kw_ids, logical_file)
        if tok_errs:
            for err in tok_errs:
                report.errors.append(f"{source_name}: element {seq}: {err}")
            continue

        if not is_repeat and item["limit_val"] and visible_len(pl_encoded) > item["limit_val"]:
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    seq,
                    f"przekroczono limit {item['limit_val']} znaków ({visible_len(pl_encoded)})",
                )
            )
        if not is_repeat and has_unexpected_hangul(pl_decoded, kr_raw, en_raw, logical_file):
            report.warnings.append(
                ImportWarningItem(
                    source_name,
                    seq,
                    f"{logical_file}: pozostały znaki koreańskie (Hangul) w PL mimo ich braku w EN",
                )
            )

        if item["glossary_kind"]:
            gkind = item["glossary_kind"]
            gkey = f"{src_enc}\t{ref_enc}"
            if en_mismatch and allow_older_package:
                existing_vg = store.view_glossary.get(gkind, {}).get(gkey)
                if existing_vg and existing_vg.get("en_sha256") == sha256_text(en_raw):
                    continue
            store.view_glossary.setdefault(gkind, {})[gkey] = {
                "src": src_enc,
                "ref": ref_enc,
                "pl": pl_decoded,
                "kr_sha256": sha256_text(kr_raw),
                "en_sha256": sha256_text(en_raw),
            }
            if is_repeat:
                report.inherited_repeats += 1
            else:
                report.translated_items += 1
            report.view_glossary_updated += 1
        else:
            wrote_any = False
            for addr in addrs:
                a_kr = kr_leaves.get(addr, "")
                a_en = en_leaves.get(addr, "")
                if allow_older_package and en_mismatch:
                    existing_leaf = store.get_leaf(logical_file, addr)
                    if existing_leaf and existing_leaf.get("en_sha256") == sha256_text(a_en):
                        continue
                store.set_leaf(logical_file, addr, pl_decoded, a_kr, a_en)
                report.addresses_updated += 1
                wrote_any = True
            if wrote_any:
                if is_repeat:
                    report.inherited_repeats += 1
                else:
                    report.translated_items += 1


def import_returns(
    inputs: list[Path],
    localize_path: Path = ROOT / "index" / "localize",
    story_index_path: Path = ROOT / "wiedza" / "indeks_fabuly.json",
    index_manifest_path: Path = ROOT / "index" / "MANIFEST.json",
    tlumaczenie_dir: Path = ROOT / "tlumaczenie",
    allow_older_package: bool = False,
) -> ImportReport:
    """Validate and atomically import translator Markdown returns into ``tlumaczenie_dir``."""
    markdown_files = collect_markdown_inputs(inputs)
    if not markdown_files:
        raise ValueError("nie znaleziono żadnych plików .md do zaimportowania")

    index_data = json.loads(story_index_path.read_text(encoding="utf-8"))
    index_manifest = (
        json.loads(index_manifest_path.read_text(encoding="utf-8"))
        if index_manifest_path.is_file()
        else {}
    )
    report = ImportReport(files_read=len(markdown_files))
    store = TranslationStore.load(tlumaczenie_dir)

    with Snapshot.open(localize_path) as snapshot:
        ref = LocalizeReference(snapshot, index_data)
        for source_name, content in markdown_files:
            base_name = PurePosixPath(source_name).name.lower()
            if base_name == "mowcy-i-miejsca.md" or content.startswith("# Mówcy, tytuły i miejsca"):
                _parse_story_glossary_file(source_name, content, ref, store, report, allow_older_package=allow_older_package)
            elif SCENE_HEADING_RE.search(content) or "\n## Scena " in content:
                _parse_story_scenes_file(source_name, content, ref, store, report, allow_older_package=allow_older_package)
            elif "   źródło: " in content or "   słownik: " in content:
                _parse_views_file(source_name, content, ref, store, report, allow_older_package=allow_older_package)
            else:
                report.errors.append(f"{source_name}: nierozpoznany układ pliku zwrotki")

        if not report.errors:
            propagated = store.propagate_story_repeats(ref)
            report.inherited_repeats += propagated
            report.addresses_updated += propagated
            store.save_atomic(index_manifest)

    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inputs", nargs="+", type=Path, help="plik(i) .md, katalog lub archiwum .zip ze zwrotką")
    parser.add_argument("--localize", type=Path, default=ROOT / "index" / "localize")
    parser.add_argument("--story-index", type=Path, default=ROOT / "wiedza" / "indeks_fabuly.json")
    parser.add_argument("--index-manifest", type=Path, default=ROOT / "index" / "MANIFEST.json")
    parser.add_argument("--out", type=Path, default=ROOT / "tlumaczenie", help="katalog docelowy (domyślnie: tlumaczenie/)")
    parser.add_argument("--report", type=Path, help="opcjonalna ścieżka raportu JSON")
    parser.add_argument(
        "--allow-older-package",
        action="store_true",
        help="przyjmij zwrotkę ze starszego pakietu po aktualizacji gry (pomiń zmienione KR z ostrzeżeniem, zachowaj niezmienione KR)",
    )
    args = parser.parse_args(argv)

    report = import_returns(
        inputs=args.inputs,
        localize_path=args.localize,
        story_index_path=args.story_index,
        index_manifest_path=args.index_manifest,
        tlumaczenie_dir=args.out,
        allow_older_package=args.allow_older_package,
    )
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report.to_dict(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    if report.errors:
        print(
            f"BŁĄD IMPORTU: {len(report.errors)} błędów w {report.files_read} plikach — katalog {args.out} pozostał nietknięty.",
            file=sys.stderr,
        )
        for err in report.errors[:25]:
            print(f"  - {err}", file=sys.stderr)
        return 2

    print(
        f"Zaimportowano zwrotkę ({report.files_read} plików): "
        f"przetłumaczono {report.translated_items}, odziedziczono powtórzeń {report.inherited_repeats}, "
        f"zaktualizowano adresów {report.addresses_updated}, bez przekładu {report.untranslated_items}, "
        f"ostrzeżeń {len(report.warnings)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
