#!/usr/bin/env python3
"""Build an official Limbus Company Custom Language archive (``LimbusCompany_Data/Lang/``).

Reads strictly from versioned repository inputs (``index/localize``,
``index/MANIFEST.json``, ``tlumaczenie/``, and ``assets/fonts/``) — never from
``local/`` — and produces a deterministic ``.zip`` ready to unpack into the
game directory:

* ``LimbusCompany_Data/Lang/config.json`` with the full 5-key schema
  (``"lang": "<Nazwa>"``, ``"titleFont": ""``, ``"contextFont": ""``,
  ``"samplingPointSize": 78``, ``"padding": 5``; default language ``Polski``
  per decision D-09 / O-01);
* ``LimbusCompany_Data/Lang/<Nazwa>/Font/Context/`` and ``Font/Title/``
  populated with unmodified SIL OFL 1.1 ``.ttf``/``.otf`` fonts from
  ``assets/fonts/`` (required by Limbus Company ``v.1.119.1`` to load a Custom
  Language; font license texts are included under ``LICENCJE_CZCIONEK/``);
* ``LimbusCompany_Data/Lang/<Nazwa>/...`` mirroring 100% of ``Localize/en``
  (with ``EN_`` file prefixes stripped) plus any translated ``kr``-only files,
  keeping untouched English strings as safe fallback so missing keys never
  produce ``"Unknown"`` or crashes;
* ``--probe`` builds a non-translation diagnostic archive
  (``LCB_TEST_DROGI_<Nazwa>_<build>.zip``) appending the 18 Polish diacritics
  ``ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ`` to ``Clear all caches`` and 3 UI/story/skill
  checkpoints to test boot & Polish glyph rendering in-game (O-03).

Specification: docs/LANG_FORMAT.md, docs/FEASIBILITY.md, docs/DECYZJE.md.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_package import clean
from tools.import_zwrotki import (
    TranslationStore,
    is_ai_entry,
    parse_index_manifest,
    sha256_text,
    validate_tokens,
)
from tools.lcb_text import Texts
from tools.localize import (
    Snapshot,
    field_name,
    iter_strings,
    list_row_steps,
    load_json,
    transform_strings,
)
from tools.package_views import NON_TRANSLATABLE_FIELDS, encode_view_text


ROOT = Path(__file__).resolve().parent.parent
ZIP_TIME = (2026, 1, 1, 0, 0, 0)
DEFAULT_LANG_NAME = "Polski"
DEFAULT_SAMPLING_POINT_SIZE = 78
DEFAULT_PADDING = 5
PL_LOWER = "ąćęłńóśźż"
PL_UPPER = "ĄĆĘŁŃÓŚŹŻ"
PL_ALL = f"{PL_LOWER} {PL_UPPER}"

SAFE_LANG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")

# Strictly diagnostic, non-translation glyph probes for Etap 3 / O-03 in-game test
PROBE_TARGETS: tuple[tuple[str, str, str, str], ...] = (
    (
        "LoginUIText.json",
        "dataList[id=switch_allcacheclear].content",
        "suffix",
        f" [PL: {PL_ALL}]",
    ),
    (
        "MainUIText.json",
        "dataList[id=mainui_main_button1].content",
        "suffix",
        f" [{PL_LOWER}]",
    ),
    (
        "MainUIText.json",
        "dataList[id=mainui_main_button2].content",
        "suffix",
        f" [{PL_UPPER}]",
    ),
    (
        "StoryData/S001B.json",
        "dataList[id=0].content",
        "prefix",
        f"[TEST PL: {PL_ALL}] ",
    ),
    (
        "Skills.json",
        "dataList[id=1010101].levelList[level=1].name",
        "suffix",
        f" [{PL_LOWER}]",
    ),
    (
        "Skills.json",
        "dataList[id=1010101].levelList[level=2].name",
        "suffix",
        f" [{PL_LOWER}]",
    ),
    (
        "Skills.json",
        "dataList[id=1010101].levelList[level=4].name",
        "suffix",
        f" [{PL_LOWER}]",
    ),
    (
        "Skills.json",
        "dataList[id=1010101].levelList[level=1].coinlist[#0].coindescs[#0].desc",
        "suffix",
        f" [PL: {PL_ALL}]",
    ),
    (
        "Skills.json",
        "dataList[id=1010101].levelList[level=2].coinlist[#0].coindescs[#0].desc",
        "suffix",
        f" [PL: {PL_ALL}]",
    ),
    (
        "Skills.json",
        "dataList[id=1010101].levelList[level=4].coinlist[#0].coindescs[#0].desc",
        "suffix",
        f" [PL: {PL_ALL}]",
    ),
)


@dataclass
class BuildSummary:
    out_zip: Path
    zip_bytes: int
    zip_sha256: str
    lang_name: str
    steam_buildid: str
    probe: bool
    files_written: int
    files_modified: int
    total_translatable: int
    translated_leaves: int
    human_leaves: int
    ai_leaves: int
    fallback_leaves: int
    probe_leaves_applied: int
    stale_source_warnings: list[str] = field(default_factory=list)
    build_warnings: list[str] = field(default_factory=list)


FONT_EXTENSIONS = {".ttf", ".otf"}


def _discover_fonts(
    fonts_dir: Path | None,
    require_fonts: bool = True,
) -> tuple[str, str, dict[str, bytes], dict[str, bytes]]:
    """Discover Title/Context ``.ttf``/``.otf`` fonts and license files under ``assets/fonts/``.

    Limbus Company (``v.1.119.1``) requires font files inside
    ``Lang/<lang>/Font/Title/`` and ``Lang/<lang>/Font/Context/`` to load a
    Custom Language; when ``titleFont`` and ``contextFont`` in ``Lang/config.json``
    are empty strings ``""``, the game loads the first font file in each folder.
    Only ``.ttf`` / ``.otf`` files are placed inside ``Font/{Title,Context}/``,
    while license texts go to ``LICENCJE_CZCIONEK/`` at the archive root.
    """
    bundled_fonts: dict[str, bytes] = {}
    bundled_licenses: dict[str, bytes] = {}
    bundled_title = ""
    bundled_context = ""

    if fonts_dir is not None and fonts_dir.is_dir():
        for slot in ("Title", "Context"):
            slot_dir = fonts_dir / slot
            if not slot_dir.is_dir():
                continue
            for f in sorted(slot_dir.iterdir()):
                if not f.is_file() or f.suffix.lower() not in FONT_EXTENSIONS:
                    continue
                raw = f.read_bytes()
                if not raw:
                    continue
                rel = f"Font/{slot}/{f.name}"
                bundled_fonts[rel] = raw
                if slot == "Title" and not bundled_title:
                    bundled_title = rel
                elif slot == "Context" and not bundled_context:
                    bundled_context = rel
        seen_lic: set[str] = set()
        for lic in sorted(fonts_dir.glob("*LICENSE*")) + sorted(fonts_dir.glob("*OFL*")):
            if lic.is_file() and lic.name not in seen_lic:
                seen_lic.add(lic.name)
                bundled_licenses[f"LICENCJE_CZCIONEK/{lic.name}"] = lic.read_bytes()

    if require_fonts and (not bundled_title or not bundled_context):
        missing = [
            slot
            for slot, val in (("Font/Title", bundled_title), ("Font/Context", bundled_context))
            if not val
        ]
        raise ValueError(
            f"brak wymaganych czcionek .ttf/.otf ({', '.join(missing)}) w {fonts_dir}: "
            "Limbus Company v.1.119.1 wymaga plików czcionek w Font/Title/ i Font/Context/"
        )

    return bundled_title, bundled_context, bundled_fonts, bundled_licenses


def _build_instructions(
    lang_name: str,
    buildid: str,
    probe: bool,
    translated_leaves: int,
    human_leaves: int,
    ai_leaves: int,
    total_translatable: int,
    bundled_title: str,
    bundled_context: str,
    warnings: list[str],
) -> bytes:
    pct = (100.0 * translated_leaves / total_translatable) if total_translatable else 0.0
    lines = [
        f"Limbus Company — polska paczka językowa ({lang_name})",
        "=" * 60,
        f"Build Steam: {buildid}",
    ]
    if bundled_title or bundled_context:
        lines.append(
            f"Czcionki (SIL OFL 1.1, LICENCJE_CZCIONEK/): {bundled_context or '-'}, {bundled_title or '-'}"
        )
    if probe:
        lines += [
            "TRYB: PACZKA DIAGNOSTYCZNA (test uruchomienia i polskich znaków O-03)",
            "",
            "Ta paczka NIE zawiera jeszcze tłumaczenia fabuły — dopisuje wyłącznie",
            f"znacznik testowy z 18 polskimi literami ({PL_ALL})",
            "do 4 miejsc w grze, aby sprawdzić w praktyce:",
            f"  1) aktywację języka '{lang_name}' w oficjalnym mechanizmie Lang/,",
            "  2) poprawne wyświetlanie wszystkich 18 polskich znaków w tytułach i tekście.",
            "",
            "GDZIE SPOJRZEĆ PO URUCHOMIENIU GRY (wystarczy 30 sekund):",
            "  1. Ekran startowy (lewy dolny róg, przed wejściem do lobby):",
            f"     przycisk 'Clear all caches [PL: {PL_ALL}]'",
            "  2. Dolny pasek w głównym oknie (Window / Lobby):",
            f"     przyciski 'Sinners [{PL_LOWER}]' oraz 'Theater [{PL_UPPER}]'",
            "  3. Theater -> Prologue (Selva Oscura) -> pierwsza scena przed walką (0-1):",
            "     pierwsza kwestia Wilka zaczyna się od '[TEST PL: ...]'",
            "  4. Sinners -> Yi Sang -> LCB Sinner -> 1. umiejętność 'Deflect':",
            "     nazwa i opis monety mają dopisane polskie znaki.",
        ]
    else:
        lines += [
            f"Pokrycie przekładu: {translated_leaves} / {total_translatable} ({pct:.2f}%)",
        ]
        if ai_leaves:
            lines.append(
                f"  w tym przekład tłumacza: {human_leaves}, tymczasowy przekład UI/meta (AI): {ai_leaves}"
            )
        lines.append("(napisy jeszcze nieprzetłumaczone zachowują bezpiecznie tekst angielski).")

    if warnings:
        lines += ["", "UWAGI WERSJI:"] + [f"  - {w}" for w in warnings]

    lines += [
        "",
        "INSTALACJA (Steam, Windows):",
        "  1. Przy wyłączonej grze w Steam kliknij prawym przyciskiem na",
        "     'Limbus Company' -> 'Zarządzaj' -> 'Przeglądaj pliki lokalne'.",
        "  2. Rozpakuj folder 'LimbusCompany_Data' z tego archiwum wprost do",
        "     otwartego katalogu gry (obok pliku LimbusCompany.exe; jeśli system",
        "     zapyta o zastąpienie wcześniejszego pliku Lang\\config.json, potwierdź).",
        "     Powstaną ścieżki:",
        "       LimbusCompany_Data\\Lang\\config.json",
        f"       LimbusCompany_Data\\Lang\\{lang_name}\\Font\\Context\\...",
        f"       LimbusCompany_Data\\Lang\\{lang_name}\\Font\\Title\\...",
        f"       LimbusCompany_Data\\Lang\\{lang_name}\\*.json",
        "     Żaden oryginalny plik gry poza katalogiem Lang\\ nie jest dotykany.",
        f"  3. Uruchom grę — powinna od razu wystartować w języku '{lang_name}'.",
        "     Gdyby nadal wyświetlała angielski, na ekranie startowym kliknij",
        f"     'Select Custom Language' -> wybierz '{lang_name}' -> zamknij i uruchom",
        "     grę ponownie.",
        "",
        "ODINSTALOWANIE / WYŁĄCZENIE:",
        "  Usuń folder 'LimbusCompany_Data\\Lang' (lub przełącz w 'Select Custom Language').",
        "",
    ]
    return "\r\n".join(lines).encode("utf-8")


def _write_deterministic_zip(path: Path, members: dict[str, bytes]) -> tuple[int, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for name in sorted(members):
            info = zipfile.ZipInfo(filename=name, date_time=ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, members[name])
    raw = path.read_bytes()
    return len(raw), hashlib.sha256(raw).hexdigest()


def build_lang_pack(
    localize_path: Path = ROOT / "index" / "localize",
    index_manifest_path: Path = ROOT / "index" / "MANIFEST.json",
    tlumaczenie_dir: Path = ROOT / "tlumaczenie",
    fonts_dir: Path | None = ROOT / "assets" / "fonts",
    lang_name: str = DEFAULT_LANG_NAME,
    out_zip: Path | None = None,
    unpacked_dir: Path | None = None,
    probe: bool = False,
    require_fonts: bool = True,
    include_ai: bool = True,
) -> BuildSummary:
    """Build the ``LimbusCompany_Data/Lang/`` archive and validate every JSON file."""
    if not SAFE_LANG_RE.match(lang_name):
        raise ValueError(
            f"nieprawidłowa nazwa języka {lang_name!r}: użyj liter ASCII, cyfr, '-' lub '_'"
        )
    resolved_loc = localize_path.resolve()
    if "local" in {p.lower() for p in resolved_loc.relative_to(ROOT).parts} if resolved_loc.is_relative_to(ROOT) else False:
        raise ValueError("budowanie paczki Lang/ z katalogu local/ jest zabronione (AGENTS.md)")

    index_manifest = (
        json.loads(index_manifest_path.read_text(encoding="utf-8"))
        if index_manifest_path.is_file()
        else {}
    )
    buildid, zrodlo_loc, cur_kr_sha, cur_en_sha = parse_index_manifest(index_manifest)

    store = TranslationStore.load(tlumaczenie_dir)
    build_warnings: list[str] = []
    tlum_manifest_path = tlumaczenie_dir / "MANIFEST.json"
    if tlum_manifest_path.is_file():
        tlum_meta = json.loads(tlum_manifest_path.read_text(encoding="utf-8"))
        tlum_build = str(tlum_meta.get("steam_buildid") or "")
        if tlum_build and buildid != "unknown" and tlum_build != buildid:
            build_warnings.append(
                f"zwrotki zaimportowano dla buildu {tlum_build}, a obecne źródło index/ ma build {buildid}"
            )

    if out_zip is None:
        prefix = "LCB_TEST_DROGI" if probe else "LCB_PL"
        out_zip = ROOT / "dist" / f"{prefix}_{lang_name}_{buildid}.zip"

    probe_lookup: dict[str, list[tuple[str, str, str]]] = {}
    if probe:
        for p_file, p_addr, p_mode, p_text in PROBE_TARGETS:
            probe_lookup.setdefault(p_file, []).append((p_addr, p_mode, p_text))

    bundled_title, bundled_context, font_members, license_members = _discover_fonts(
        fonts_dir, require_fonts=require_fonts
    )

    zip_members: dict[str, bytes] = {}
    lang_prefix = f"LimbusCompany_Data/Lang/{lang_name}"

    config_obj = {
        "lang": lang_name,
        "titleFont": "",
        "contextFont": "",
        "samplingPointSize": DEFAULT_SAMPLING_POINT_SIZE,
        "padding": DEFAULT_PADDING,
    }
    zip_members["LimbusCompany_Data/Lang/config.json"] = (
        json.dumps(config_obj, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")

    for rel_font, font_bytes in font_members.items():
        zip_members[f"{lang_prefix}/{rel_font}"] = font_bytes
    for rel_lic, lic_bytes in license_members.items():
        zip_members[rel_lic] = lic_bytes

    stale_warnings: list[str] = []
    files_written = 0
    files_modified = 0
    total_translatable = 0
    translated_leaves = 0
    human_leaves = 0
    ai_leaves = 0
    fallback_leaves = 0
    probe_leaves_applied = 0

    def _allowed(entry: dict | None) -> bool:
        return bool(entry) and (include_ai or not is_ai_entry(entry))

    with Snapshot.open(localize_path) as snapshot:
        src_texts = Texts(snapshot, "kr") if "kr" in snapshot.files else None
        ref_texts = Texts(snapshot, "en")
        known_kw_ids = (
            (set(src_texts.keywords) if src_texts else set())
            | set(ref_texts.keywords)
            | {"ATTRIBUTES"}
        )

        en_set = set(snapshot.files.get("en", {}))
        kr_set = set(snapshot.files.get("kr", {}))
        translated_kr_only = {
            f
            for f in (kr_set - en_set)
            if any(_allowed(e) for e in store.files.get(f, {}).values())
        }
        target_files = sorted(en_set | translated_kr_only)

        # Precompute lookup maps for glossaries
        story_gl = store.story_glossary
        view_gl = store.view_glossary

        for logical_file in target_files:
            base_lang = "en" if logical_file in en_set else "kr"
            base_doc = load_json(snapshot.read(base_lang, logical_file))
            kr_doc = (
                load_json(snapshot.read("kr", logical_file))
                if logical_file in kr_set
                else {}
            )
            base_leaves = dict(iter_strings(base_doc))
            kr_leaves = dict(iter_strings(kr_doc)) if kr_doc else {}

            updates: dict[str, str] = {}
            ai_addrs_in_file: set[str] = set()
            file_entries = store.files.get(logical_file, {})

            def _apply_entry(addr: str, entry: dict) -> None:
                updates[addr] = entry["pl"]
                if is_ai_entry(entry):
                    ai_addrs_in_file.add(addr)

            # 1. Direct address translations from tlumaczenie/pliki/
            for addr, entry in file_entries.items():
                if addr not in base_leaves or not _allowed(entry):
                    continue
                kr_val = kr_leaves.get(addr, "")
                expected_kr_sha = entry.get("kr_sha256")
                if expected_kr_sha and kr_val and sha256_text(kr_val) != expected_kr_sha:
                    stale_warnings.append(f"{logical_file} :: {addr}")
                _apply_entry(addr, entry)

            # 2. Story glossary application (teller, title, place) across StoryData/*.json
            if logical_file.startswith("StoryData/") and any(story_gl.get(k) for k in ("teller", "title", "place")):
                base_rows = base_doc.get("dataList", []) if isinstance(base_doc, dict) else []
                kr_row_by_step = {
                    step: row
                    for step, row in list_row_steps(
                        kr_doc.get("dataList", []) if isinstance(kr_doc, dict) else []
                    )
                    if isinstance(row, dict)
                }
                for step, row in list_row_steps(base_rows):
                    if not isinstance(row, dict) or row.get("id") == -1:
                        continue
                    kr_row = kr_row_by_step.get(step, {})
                    for g_field in ("teller", "title", "place"):
                        f_addr = f"dataList{step}.{g_field}"
                        if f_addr in updates or f_addr not in base_leaves:
                            continue
                        en_f = clean(row.get(g_field))
                        kr_f = clean(kr_row.get(g_field))
                        g_key = kr_f or (f"{en_f} (tylko EN)" if en_f else "")
                        g_hit = story_gl.get(g_field, {}).get(g_key)
                        if _allowed(g_hit):
                            _apply_entry(f_addr, g_hit)

            # 3. Story model/title glossary fallback on ScenarioModelCodes-AutoCreated.json
            if logical_file == "ScenarioModelCodes-AutoCreated.json" and any(
                story_gl.get(k) for k in ("model", "teller", "title")
            ):
                for addr, base_val in base_leaves.items():
                    if addr in updates or not base_val.strip():
                        continue
                    fname = field_name(addr)
                    kr_v = clean(kr_leaves.get(addr, ""))
                    en_v = clean(base_val)
                    g_key = kr_v or (f"{en_v} (tylko EN)" if en_v else "")
                    if fname == "name":
                        m_hit = story_gl.get("model", {}).get(g_key)
                        t_hit = story_gl.get("teller", {}).get(g_key)
                        g_hit = m_hit if _allowed(m_hit) else (t_hit if _allowed(t_hit) else None)
                        if g_hit and g_hit.get("en_sha256") == sha256_text(en_v):
                            _apply_entry(addr, g_hit)
                    elif fname == "nickName" and story_gl.get("title"):
                        g_hit = story_gl["title"].get(g_key)
                        if _allowed(g_hit) and g_hit.get("en_sha256") == sha256_text(en_v):
                            _apply_entry(addr, g_hit)

            # 4. View speaker glossaries (RPGSystem/*.speaker, AbDlg*.teller)
            if logical_file.startswith("RPGSystem/") and view_gl.get("rpg_speaker"):
                for addr, base_val in base_leaves.items():
                    if addr in updates or field_name(addr) != "speaker":
                        continue
                    g_key = f"{encode_view_text(kr_leaves.get(addr, ''))}\t{encode_view_text(base_val)}"
                    g_hit = view_gl["rpg_speaker"].get(g_key)
                    if _allowed(g_hit):
                        _apply_entry(addr, g_hit)
            elif PurePosixPath(logical_file).name.startswith("AbDlg") and view_gl.get("abdlg_teller"):
                for addr, base_val in base_leaves.items():
                    if addr in updates or field_name(addr) != "teller":
                        continue
                    g_key = f"{encode_view_text(kr_leaves.get(addr, ''))}\t{encode_view_text(base_val)}"
                    g_hit = view_gl["abdlg_teller"].get(g_key)
                    if _allowed(g_hit):
                        _apply_entry(addr, g_hit)

            # Validate translated updates against source tokens before applying probe
            for addr, pl_val in updates.items():
                kr_val = kr_leaves.get(addr, "")
                en_val = base_leaves.get(addr, "") if base_lang == "en" else ""
                tok_errs = validate_tokens(pl_val, kr_val, en_val, known_kw_ids, logical_file)
                if tok_errs:
                    raise ValueError(
                        f"błąd walidacji tokenów w {logical_file} :: {addr}: {'; '.join(tok_errs)}"
                    )

            translated_addrs_in_file = set(updates)

            # 5. Optional Etap 3 diagnostic glyph probe (--probe)
            if logical_file in probe_lookup:
                for p_addr, p_mode, p_text in probe_lookup[logical_file]:
                    if p_addr in base_leaves:
                        current = updates.get(p_addr, base_leaves[p_addr])
                        updates[p_addr] = (
                            f"{p_text}{current}" if p_mode == "prefix" else f"{current}{p_text}"
                        )
                        probe_leaves_applied += 1

            # Coverage accounting on translatable leaves
            for addr, base_val in base_leaves.items():
                if field_name(addr) in NON_TRANSLATABLE_FIELDS:
                    continue
                kr_val = kr_leaves.get(addr, "")
                if not base_val.strip() and not kr_val.strip():
                    continue
                total_translatable += 1
                if addr in translated_addrs_in_file:
                    translated_leaves += 1
                    if addr in ai_addrs_in_file:
                        ai_leaves += 1
                    else:
                        human_leaves += 1
                else:
                    fallback_leaves += 1

            if updates:
                out_doc, applied = transform_strings(base_doc, updates)
                if applied != set(updates):
                    missing_apply = sorted(set(updates) - applied)
                    raise RuntimeError(
                        f"nie udało się podmienić adresów w {logical_file}: {missing_apply}"
                    )
                files_modified += 1
            else:
                out_doc = base_doc

            serialized = (json.dumps(out_doc, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

            # Strict post-build structural & JSON parse verification
            reparsed = json.loads(serialized.decode("utf-8"))
            out_addr_set = {a for a, _ in iter_strings(reparsed)}
            if out_addr_set != set(base_leaves):
                raise RuntimeError(
                    f"niezgodność struktury adresów po zbudowaniu {logical_file}"
                )

            zip_members[f"{lang_prefix}/{logical_file}"] = serialized
            files_written += 1

    if stale_warnings:
        build_warnings.append(
            f"{len(stale_warnings)} przetłumaczonych wpisów ma zmieniony tekst źródłowy KR względem momentu tłumaczenia"
        )

    zip_members["INSTRUKCJA.txt"] = _build_instructions(
        lang_name=lang_name,
        buildid=buildid,
        probe=probe,
        translated_leaves=translated_leaves,
        human_leaves=human_leaves,
        ai_leaves=ai_leaves,
        total_translatable=total_translatable,
        bundled_title=bundled_title,
        bundled_context=bundled_context,
        warnings=build_warnings,
    )

    manifest_payload = {
        "format_version": 1,
        "lang": lang_name,
        "probe": probe,
        "include_ai": include_ai,
        "steam_buildid": buildid,
        "zrodlo_localize": zrodlo_loc,
        "localize_kr_sha256": cur_kr_sha,
        "localize_en_sha256": cur_en_sha,
        "fonts": {
            "titleFont": "",
            "contextFont": "",
            "samplingPointSize": DEFAULT_SAMPLING_POINT_SIZE,
            "padding": DEFAULT_PADDING,
            "bundled_title_font": bundled_title,
            "bundled_context_font": bundled_context,
            "uses_default_game_font": not (bundled_title or bundled_context),
        },
        "files_written": files_written,
        "files_modified": files_modified,
        "coverage": {
            "total_translatable_leaves": total_translatable,
            "translated_leaves": translated_leaves,
            "human_leaves": human_leaves,
            "ai_leaves": ai_leaves,
            "fallback_en_leaves": fallback_leaves,
            "percent": round((100.0 * translated_leaves / total_translatable), 4)
            if total_translatable
            else 0.0,
        },
        "probe_leaves_applied": probe_leaves_applied,
        "stale_source_count": len(stale_warnings),
        "stale_source_sample": stale_warnings[:25],
        "warnings": build_warnings,
    }
    zip_members["MANIFEST.json"] = (
        json.dumps(manifest_payload, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")

    if unpacked_dir is not None:
        unpacked_dir.mkdir(parents=True, exist_ok=True)
        for member_path, payload in zip_members.items():
            dest = unpacked_dir / member_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(payload)

    zip_bytes, zip_sha = _write_deterministic_zip(out_zip, zip_members)
    return BuildSummary(
        out_zip=out_zip,
        zip_bytes=zip_bytes,
        zip_sha256=zip_sha,
        lang_name=lang_name,
        steam_buildid=buildid,
        probe=probe,
        files_written=files_written,
        files_modified=files_modified,
        total_translatable=total_translatable,
        translated_leaves=translated_leaves,
        human_leaves=human_leaves,
        ai_leaves=ai_leaves,
        fallback_leaves=fallback_leaves,
        probe_leaves_applied=probe_leaves_applied,
        stale_source_warnings=stale_warnings,
        build_warnings=build_warnings,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--localize", type=Path, default=ROOT / "index" / "localize")
    parser.add_argument("--index-manifest", type=Path, default=ROOT / "index" / "MANIFEST.json")
    parser.add_argument("--tlumaczenie", type=Path, default=ROOT / "tlumaczenie")
    parser.add_argument(
        "--fonts",
        type=Path,
        default=ROOT / "assets" / "fonts",
        help="katalog czcionek OFL (domyślnie: assets/fonts)",
    )
    parser.add_argument(
        "--allow-missing-fonts",
        action="store_true",
        help="pozwól zbudować paczkę bez Font/Title i Font/Context (tylko diagnostycznie)",
    )
    parser.add_argument("--lang-name", default=DEFAULT_LANG_NAME, help="nazwa folderu i języka w config.json (domyślnie: Polski)")
    parser.add_argument("--out", type=Path, help="ścieżka wynikowego archiwum .zip (domyślnie w dist/)")
    parser.add_argument("--unpack-to", type=Path, help="opcjonalny katalog do rozpakowania struktury")
    parser.add_argument(
        "--probe",
        action="store_true",
        help="zbuduj paczkę diagnostyczną Etapu 3 (test uruchomienia i 18 polskich znaków O-03)",
    )
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="pomiń tymczasowe wpisy AI ('origin': 'ai') — zbuduj paczkę wyłącznie z przekładu tłumacza",
    )
    args = parser.parse_args(argv)

    summary = build_lang_pack(
        localize_path=args.localize,
        index_manifest_path=args.index_manifest,
        tlumaczenie_dir=args.tlumaczenie,
        fonts_dir=args.fonts,
        lang_name=args.lang_name,
        out_zip=args.out,
        unpacked_dir=args.unpack_to,
        probe=args.probe,
        require_fonts=not args.allow_missing_fonts,
        include_ai=not args.no_ai,
    )
    mode_txt = "DIAGNOSTYCZNA (--probe)" if summary.probe else "PRODUKCYJNA"
    print(
        f"Zbudowano paczkę {mode_txt} '{summary.lang_name}' (build {summary.steam_buildid}): "
        f"{summary.out_zip} ({summary.zip_bytes} B, SHA-256 {summary.zip_sha256})"
    )
    print(
        f"Plików JSON: {summary.files_written} (zmodyfikowanych: {summary.files_modified}), "
        f"przetłumaczonych liści: {summary.translated_leaves}/{summary.total_translatable}, "
        f"znaczników diagnostycznych: {summary.probe_leaves_applied}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
