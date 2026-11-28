#!/usr/bin/env python3
"""Deterministic 3-Wave batch planner and renderer for provisional AI UI/meta translation.

Follows project rule D-11 (modeled after ``wherewindsmeet``):
- Provisional AI translations (``"origin": "ai"``) cover ONLY UI, technical, and
  meta/stats strings so the game is comfortably playable before the human
  Translator finishes all views.
- Narrative prose, dialogues, character/announcer voice lines, song lyrics,
  Observation Logs, Dante's Note lore details, Abnormality/Dungeon event stories,
  Sinner dossier bios, and Canto X RPG dialogues/narrations are strictly EXCLUDED
  and reserved exclusively for the human Translator.
- Untranslated developer Korean strings in EN (``KR == EN`` containing Hangul)
  are excluded until Project Moon localizes them to English.
- Each batch ``P01..PNN`` (~450-600 unique ``PL:`` slots) renders as a single,
  self-contained Translator-format Markdown file ready for ``zwrotki/ai/`` and
  ``python3 tools/import_zwrotki.py --ai``.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
from pathlib import Path, PurePosixPath
import re
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.audit_update import _prefill_view_md
from tools.import_zwrotki import (
    HANGUL_RE,
    LocalizeReference,
    TranslationStore,
    is_ai_entry,
    parse_index_manifest,
    sha256_text,
)
from tools.localize import Snapshot, field_name
from tools.package_views import (
    Corpus,
    PendingItem,
    SectionBlock,
    ViewGlossary,
    ascii_slug,
    build_view_model,
    encode_view_text,
    render_section_lines,
)
from tools.static_data import StaticData


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "paczki_ai" / "MANIFEST.json"
DEFAULT_RENDER_OUT = ROOT / "local" / "paczki_ai"
DEFAULT_ZWROTKI_AI = ROOT / "zwrotki" / "ai"
TARGET_BATCH_TODO = 560
MIN_TAIL_MERGE = 160

# Strictly excluded narrative, dialogue, voiceover, and lyric files (reserved for human Translator)
EXCLUDED_LOGICAL_PREFIXES: tuple[str, ...] = (
    "StoryData/",
    "Story-",
    "PersonalityVoiceDlg/",
    "EGOVoiceDig/",
    "EGOvoiceDlg/",
    "BattleAnnouncerDlg/",
    "BgmLyrics/",
    "BattleSpeechBubbleDlg",
    "AbnormalityGuides",
    "StoryTheaterDanteNoteDetail",
    "AbEvents",
    "AbDlg",
    "ActionEvents",
    "RPGSystem/rpg-loc-dialogue",
    "RPGSystem/rpg-loc-narration",
)

EXCLUDED_REASON_LABELS: tuple[tuple[tuple[str, ...], str], ...] = (
    (("PersonalityVoiceDlg/",), "kwestie głosowe Tożsamości Grzeszników"),
    (("EGOVoiceDig/", "EGOvoiceDlg/"), "kwestie głosowe przebudzenia i korozji E.G.O"),
    (("BattleAnnouncerDlg/",), "kwestie komentatorów walki"),
    (("BgmLyrics/",), "teksty piosenek (Mili / motywy bossów)"),
    (("BattleSpeechBubbleDlg",), "dymki dialogowe postaci w walce"),
    (("AbnormalityGuides",), "dzienniki obserwacji Anomalii (prozatorskie)"),
    (("StoryTheaterDanteNoteDetail", "Story-"), "wpisy fabularno-lore w Notatkach Dantego i cytaty kulminacyjne"),
    (("AbEvents", "AbDlg", "ActionEvents"), "zdarzenia, wybory i dialogi Anomalii / Lochów"),
    (
        ("RPGSystem/rpg-loc-dialogue", "RPGSystem/rpg-loc-narration"),
        "dialogi i narracja trybu RPG Canto X",
    ),
)

SINNER_SLUGS: dict[int, tuple[str, str]] = {
    1: ("yi_sang", "Yi Sang"),
    2: ("faust", "Faust"),
    3: ("don_quixote", "Don Quixote"),
    4: ("ryoshu", "Ryōshū"),
    5: ("meursault", "Meursault"),
    6: ("hong_lu", "Hong Lu"),
    7: ("heathcliff", "Heathcliff"),
    8: ("ishmael", "Ishmael"),
    9: ("rodion", "Rodion"),
    10: ("sinclair", "Sinclair"),
    11: ("outis", "Outis"),
    12: ("gregor", "Gregor"),
}


@dataclass(frozen=True)
class CategorySpec:
    key: str
    wave: int
    order: int
    slug: str
    title: str
    description: str


CATEGORIES: dict[str, CategorySpec] = {
    c.key: c
    for c in (
        CategorySpec(
            "1A",
            1,
            10,
            "fundament_bojowy",
            "Fundament bojowy — grzechy, odporności, tagi, Panika i interfejs walki",
            "Słownik bazowy mechaniki walki (AttributeText, ResistText, SkillTag, MentalCondition, PanicInfo, BattleUIText, UnitKeyword). Tłumaczony jako pierwszy — ustala terminologię dla wszystkich kolejnych paczek.",
        ),
        CategorySpec(
            "1B",
            1,
            20,
            "interfejs_i_ustawienia",
            "Interfejs główny, ustawienia, okna dialogowe i formacja",
            " Menu główne (Window), ustawienia gry (w tym kr_settings-ui-donttranslate.json), komunikaty systemowe, skróty klawiszowe, profil gracza, filtry i ekran drużyny.",
        ),
        CategorySpec(
            "1C",
            1,
            30,
            "tryby_etapy_lochy_teatr",
            "Tryby gry, nazwy etapów, Lustrzane Lochy, Kolej i Teatr (UI)",
            "Nazwy rozdziałów i węzłów mapy, warunki etapów, interfejs Lustrzanych Lochów i Kolei Załamania oraz nagłówki/tytuły Teatru i Notatek Dantego (bez prozatorskich opisów lore).",
        ),
        CategorySpec(
            "1D",
            1,
            40,
            "samouczki_i_wskazowki",
            "Samouczki systemowe i wskazówki ekranu ładowania",
            "Instrukcje obsługi interfejsu i walki (TutorialDesc, TutorialMainUIText, TutorialMirrorDungeon, BattleHint, ekrany wskazówek).",
        ),
        CategorySpec(
            "2A",
            2,
            50,
            "slowa_kluczowe_i_statusy",
            "Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords)",
            "Wszystkie wzmocnienia, osłabienia, żetony mechanik i słowniczki podpowiedzi na kartach umiejętności.",
        ),
        CategorySpec(
            "2B",
            2,
            60,
            "przedmioty_sklep_wydarzenia",
            "Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń",
            "Opisy walut, biletów i skrzynek, sklep, banery Gacha, misje Przepustki Bitewnej oraz interfejs wydarzeń sezonowych.",
        ),
        CategorySpec(
            "2C",
            2,
            70,
            "modele_i_rpg_ui",
            "Tabela modeli postaci oraz interfejs, zadania i przedmioty RPG Canto X",
            "Nazwy i przydomki modeli (ScenarioModelCodes-AutoCreated), mówcy RPG (rpg_speaker) oraz UI, dziennik zadań, przedmioty, lokacje i statystyki trybu RPG Canto X (bez dialogów i narracji).",
        ),
        CategorySpec(
            "3A",
            3,
            80,
            "grzesznicy_tozsamosci",
            "Grzesznicy — Tożsamości, umiejętności i pasywki (01 Yi Sang – 12 Gregor)",
            "Nazwy Tożsamości, warunki pozyskania, nazwy i opisy umiejętności oraz umiejętności pasywnych wszystkich 12 Grzeszników (pogrupowane per Grzesznik).",
        ),
        CategorySpec(
            "3B",
            3,
            90,
            "ego_i_dary_ego",
            "Karty E.G.O, umiejętności/pasywki E.G.O oraz Dary E.G.O",
            "Karty E.G.O Grzeszników, ich umiejętności przebudzenia/korozji, pasywki oraz pełny katalog Darów E.G.O z Lustrzanych Lochów.",
        ),
        CategorySpec(
            "3C",
            3,
            100,
            "przeciwnicy_i_anomalie",
            "Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille)",
            "Nazwy wrogów i części Anomalii oraz techniczne opisy ich umiejętności i pasywek bojowych (bez dzienników obserwacji i zdarzeń tekstowych).",
        ),
    )
}


def excluded_reason(logical_file: str, addr: str, kr_raw: str, en_raw: str) -> str | None:
    """Return exclusion reason if ``(logical_file, addr)`` is outside D-11 AI scope."""
    for prefixes, label in EXCLUDED_REASON_LABELS:
        if logical_file.startswith(prefixes):
            return label
    if logical_file.startswith(EXCLUDED_LOGICAL_PREFIXES):
        return "wyłączone pliki narracyjne/głosowe"
    if logical_file == "IntroduceCharacter.json" and field_name(addr) == "description":
        return "literackie biogramy Grzeszników (IntroduceCharacter.description)"
    if en_raw and HANGUL_RE.search(en_raw) and kr_raw.strip() == en_raw.strip():
        return "nieprzetłumaczony tekst roboczy KR w EN (dev-Korean)"
    return None


def classify_logical_file(logical_file: str, domain_base: str = "") -> tuple[str, str, str]:
    """Map an in-scope logical file (and its view domain) to ``(cat_key, sub_slug, sub_title)``."""
    name = PurePosixPath(logical_file).name

    # Sinner-specific grouping preserved from package_views domain 02_tozsamosc_XX_*
    if domain_base.startswith("02_tozsamosc_"):
        parts = domain_base.split("_", 3)
        if len(parts) >= 4 and parts[2].isdigit():
            s_no = int(parts[2])
            if s_no in SINNER_SLUGS:
                s_slug, s_name = SINNER_SLUGS[s_no]
                return "3A", f"{s_no:02d}_{s_slug}", f"Grzesznik {s_no:02d} — {s_name}"
        return "3A", "13_wspolne", "Grzesznicy — Tożsamości i pasywki wspólne"

    if logical_file.startswith("RPGSystem/") or logical_file == "ScenarioModelCodes-AutoCreated.json":
        return "2C", "modele_i_rpg_ui", CATEGORIES["2C"].title

    # Wave 1A: Combat foundation
    if name.startswith((
        "AttributeText",
        "ResistText",
        "SkillTag",
        "SuccessRate",
        "MentalCondition",
        "PanicInfo",
        "BattleUIText",
        "UnitKeyword",
    )):
        return "1A", "fundament_bojowy", CATEGORIES["1A"].title

    # Wave 2A: Keywords & Buffs
    if name.startswith(("BattleKeywords", "Bufs")):
        return "2A", "slowa_kluczowe_i_statusy", CATEGORIES["2A"].title

    # Wave 3B: E.G.O & E.G.O Gifts
    if (
        domain_base.startswith("03_")
        or name.startswith(("Egos", "Skills_Ego", "Passive_Ego", "EGOgift", "MirrorDungeonEgoGift"))
    ):
        if name.startswith(("EGOgift", "MirrorDungeonEgoGift")) or "dary_ego" in domain_base:
            return "3B", "dary_ego", "Dary E.G.O (Lustrzane Lochy i fabularne)"
        return "3B", "karty_ego", "Karty E.G.O, umiejętności i pasywki"

    # Wave 3C: Enemies, Abnormalities combat stats, Assist units
    if (
        domain_base.startswith("04_")
        or name.startswith((
            "Enemies",
            "Enemy",
            "Assist",
            "Skills_Enemy",
            "Skills_Abnormality",
            "Skills_Assist",
            "Passives_Enemy",
            "Passives_Abnormality",
            "Passives_Assist",
            "AbnormalityParts",
        ))
    ):
        return "3C", "przeciwnicy_i_anomalie", CATEGORIES["3C"].title

    # Wave 3A fallback (Characters / Personalities / Skills / Passives outside 02_tozsamosc_*)
    if name.startswith((
        "Characters",
        "IntroduceCharacter",
        "Personalities",
        "Personality_Get_Condition",
        "Skills",
        "Passives",
    )):
        return "3A", "00_ogolne", "Grzesznicy — profile i tabele wspólne"

    # Wave 1D: Tutorials & Hints
    if name.startswith(("Tutorial", "BattleHint", "TipContent", "BattleTip")):
        return "1D", "samouczki_i_wskazowki", CATEGORIES["1D"].title

    # Wave 1C: Modes, Stages, Dungeons, Railway, Theater UI
    if (
        domain_base.startswith("07_")
        or name.startswith((
            "Stage",
            "SubChapter",
            "Dungeon",
            "MirrorDungeonUI",
            "MirrorDungeonAbName",
            "MirrorDungeonNode",
            "RailwayDungeon",
            "HellsChickenDungeon",
            "Walpurgisnacht",
            "StoryTheater",
            "MirrorWorld",
        ))
    ):
        return "1C", "tryby_etapy_lochy_teatr", CATEGORIES["1C"].title

    # Wave 1B: Settings & Main UI
    if name.startswith((
        "kr_settings-ui",
        "MainUIText",
        "PopupDesc",
        "ShortCutKey",
        "LoadingCGSubTitle",
        "UpperSkillInfoUI",
        "FormationUIText",
        "UserInfo",
        "Filter",
        "UnlockCode",
        "UpgradeCharacterUI",
        "LoginUIText",
        "Account",
        "Network",
        "Steam",
    )):
        return "1B", "interfejs_i_ustawienia", CATEGORIES["1B"].title

    # Wave 2B: Items, Shop, Battle Pass, Events, Catch-all UI tables
    return "2B", "przedmioty_sklep_wydarzenia", CATEGORIES["2B"].title


@dataclass
class PlannedEntry:
    kind: str  # "section_item" | "view_glossary"
    cat_key: str
    sub_slug: str
    sub_title: str
    section_heading: str
    context_lines: list[str]
    item: PendingItem | None = None
    glossary_kind: str = ""
    glossary_label: str = ""
    logical_file: str = ""
    addrs: list[str] = field(default_factory=list)
    src_raw: str = ""
    ref_raw: str = ""


def _unique_key(entry: PlannedEntry) -> tuple[str, str, str]:
    src_enc = encode_view_text(entry.src_raw)
    ref_enc = encode_view_text(entry.ref_raw)
    if entry.kind == "view_glossary":
        return ("gl", entry.glossary_kind, f"{src_enc}\t{ref_enc}")
    return ("tx", src_enc, ref_enc)


def collect_plan_data(
    corpus: Corpus,
    domains: list[tuple[str, str, str, list[SectionBlock]]],
    mc_blocks: list[SectionBlock],
) -> tuple[list[PlannedEntry], dict[str, int], dict[str, set[str]]]:
    """Collect all in-scope AI items and exact exclusion statistics from the view model."""
    excluded_slot_counts: dict[str, int] = {}
    excluded_files_by_reason: dict[str, set[str]] = {}
    in_scope_entries: list[PlannedEntry] = []

    # 1. View glossary: rpg_speaker (in scope -> 2C), abdlg_teller (excluded -> AbDlg)
    gl_labels = dict(ViewGlossary.KINDS)
    for (kind, src_enc, ref_enc), meta in sorted(
        corpus.glossary.entries.items(),
        key=lambda kv: (kv[0][0], kv[0][2].lower(), kv[0][1]),
    ):
        lf = meta["first_file"]
        first_addr = meta["first_addr"]
        kr_raw = corpus.leaves_src.get(lf, {}).get(first_addr, "")
        en_raw = corpus.leaves_ref.get(lf, {}).get(first_addr, "")
        label = gl_labels.get(kind, kind)
        reason = excluded_reason(lf, first_addr, kr_raw, en_raw)
        if reason or kind == "abdlg_teller":
            r = reason or "zdarzenia, wybory i dialogi Anomalii / Lochów"
            excluded_slot_counts[r] = excluded_slot_counts.get(r, 0) + 1
            excluded_files_by_reason.setdefault(r, set()).add(lf)
            continue
        in_scope_entries.append(
            PlannedEntry(
                kind="view_glossary",
                cat_key="2C",
                sub_slug="modele_i_rpg_ui",
                sub_title=CATEGORIES["2C"].title,
                section_heading=f"## {label}",
                context_lines=[
                    "- Słownik mówców trybu RPG Canto X — przetłumacz raz na parę (KR, EN); gra podstawia nazwę mówcy automatycznie.",
                ],
                glossary_kind=kind,
                glossary_label=label,
                logical_file=lf,
                addrs=[first_addr],
                src_raw=kr_raw,
                ref_raw=en_raw,
            )
        )

    # 2. ScenarioModelCodes-AutoCreated.json (from mc_blocks -> 2C)
    for block in mc_blocks:
        for it in block.items:
            reason = excluded_reason(it.logical_file, it.addrs[0], it.src_raw, it.ref_raw)
            if reason:
                excluded_slot_counts[reason] = excluded_slot_counts.get(reason, 0) + 1
                excluded_files_by_reason.setdefault(reason, set()).add(it.logical_file)
                continue
            in_scope_entries.append(
                PlannedEntry(
                    kind="section_item",
                    cat_key="2C",
                    sub_slug="modele_i_rpg_ui",
                    sub_title=CATEGORIES["2C"].title,
                    section_heading=block.heading,
                    context_lines=list(block.context_lines),
                    item=it,
                    logical_file=it.logical_file,
                    addrs=list(it.addrs),
                    src_raw=it.src_raw,
                    ref_raw=it.ref_raw,
                )
            )

    # 3. All domain sections
    for domain_base, _domain_title, _domain_intro, blocks in domains:
        for block in blocks:
            for it in block.items:
                reason = excluded_reason(it.logical_file, it.addrs[0], it.src_raw, it.ref_raw)
                if reason:
                    excluded_slot_counts[reason] = excluded_slot_counts.get(reason, 0) + 1
                    excluded_files_by_reason.setdefault(reason, set()).add(it.logical_file)
                    continue
                cat_key, sub_slug, sub_title = classify_logical_file(
                    it.logical_file, domain_base=domain_base
                )
                in_scope_entries.append(
                    PlannedEntry(
                        kind="section_item",
                        cat_key=cat_key,
                        sub_slug=sub_slug,
                        sub_title=sub_title,
                        section_heading=block.heading,
                        context_lines=list(block.context_lines),
                        item=it,
                        logical_file=it.logical_file,
                        addrs=list(it.addrs),
                        src_raw=it.src_raw,
                        ref_raw=it.ref_raw,
                    )
                )

    return in_scope_entries, excluded_slot_counts, excluded_files_by_reason


def partition_into_batches(
    entries: list[PlannedEntry],
    target_todo: int = TARGET_BATCH_TODO,
) -> list[dict]:
    """Deterministically partition PlannedEntries into coherent ~500-600-slot batches."""
    groups: dict[tuple[int, str, str], list[PlannedEntry]] = {}
    group_titles: dict[tuple[int, str, str], str] = {}
    for e in entries:
        spec = CATEGORIES[e.cat_key]
        gkey = (spec.order, e.cat_key, e.sub_slug)
        groups.setdefault(gkey, []).append(e)
        group_titles[gkey] = e.sub_title

    raw_chunks: list[tuple[str, str, str, list[PlannedEntry]]] = []
    for gkey in sorted(groups):
        _order, cat_key, sub_slug = gkey
        sub_title = group_titles[gkey]
        bucket = groups[gkey]

        sub_chunks: list[list[PlannedEntry]] = []
        cur: list[PlannedEntry] = []
        seen_keys: set[tuple[str, str, str]] = set()
        for e in bucket:
            ukey = _unique_key(e)
            adds_todo = 0 if ukey in seen_keys else 1
            if cur and (len(seen_keys) + adds_todo > target_todo):
                sub_chunks.append(cur)
                cur = []
                seen_keys = set()
            cur.append(e)
            seen_keys.add(ukey)
        if cur:
            if sub_chunks:
                tail_unique = {_unique_key(x) for x in cur}
                prev_unique = {_unique_key(x) for x in sub_chunks[-1]}
                if len(tail_unique) < MIN_TAIL_MERGE and len(prev_unique | tail_unique) <= (
                    target_todo + MIN_TAIL_MERGE
                ):
                    sub_chunks[-1].extend(cur)
                else:
                    sub_chunks.append(cur)
            else:
                sub_chunks.append(cur)

        for idx, ch in enumerate(sub_chunks, 1):
            part_slug = (
                f"{cat_key.lower()}_{sub_slug}"
                if len(sub_chunks) == 1
                else f"{cat_key.lower()}_{sub_slug}_cz{idx:02d}"
            )
            part_title = (
                sub_title
                if len(sub_chunks) == 1
                else f"{sub_title} (część {idx}/{len(sub_chunks)})"
            )
            raw_chunks.append((cat_key, part_slug, part_title, ch))

    batches: list[dict] = []
    file_to_batches: dict[str, list[str]] = {}
    for b_idx, (cat_key, part_slug, part_title, ch) in enumerate(raw_chunks, 1):
        batch_id = f"P{b_idx:02d}"
        spec = CATEGORIES[cat_key]
        unique_todo = len({_unique_key(x) for x in ch})
        lfiles = sorted({x.logical_file for x in ch})
        for lf in lfiles:
            file_to_batches.setdefault(lf, []).append(batch_id)
        addr_count = sum(len(x.addrs) for x in ch)
        batches.append(
            {
                "id": batch_id,
                "wave": spec.wave,
                "category": cat_key,
                "category_title": spec.title,
                "slug": f"{batch_id}_{part_slug}",
                "zwrotka_path": f"zwrotki/ai/{batch_id}_{part_slug}.md",
                "title": part_title,
                "elements": len(ch),
                "unique_slots": unique_todo,
                "leaf_addresses": addr_count,
                "logical_files_count": len(lfiles),
                "logical_files": lfiles,
                "_entries": ch,
            }
        )

    for b in batches:
        shared = sorted(
            lf for lf in b["logical_files"] if len(file_to_batches.get(lf, [])) > 1
        )
        b["shared_logical_files"] = shared

    return batches


def compute_batch_status(
    batches: list[dict],
    store: TranslationStore,
    corpus: Corpus,
) -> dict:
    """Compute exact human / AI / pending unique-slot counts per batch and per wave."""
    wave_Rollup: dict[int, dict[str, int]] = {
        1: {"batches": 0, "unique_slots": 0, "human": 0, "ai": 0, "pending": 0},
        2: {"batches": 0, "unique_slots": 0, "human": 0, "ai": 0, "pending": 0},
        3: {"batches": 0, "unique_slots": 0, "human": 0, "ai": 0, "pending": 0},
    }
    batch_rows: list[dict] = []

    for b in batches:
        seen: set[tuple[str, str, str]] = set()
        human_cnt = 0
        ai_cnt = 0
        pending_cnt = 0
        for e in b["_entries"]:
            ukey = _unique_key(e)
            if ukey in seen:
                continue
            seen.add(ukey)
            first_addr = e.addrs[0]
            kr_raw = corpus.leaves_src.get(e.logical_file, {}).get(first_addr, "")
            if e.kind == "view_glossary":
                gkey = f"{encode_view_text(e.src_raw)}\t{encode_view_text(e.ref_raw)}"
                hit = store.view_glossary.get(e.glossary_kind, {}).get(gkey)
            else:
                hit = store.files.get(e.logical_file, {}).get(first_addr)

            valid = False
            if hit:
                exp_sha = hit.get("kr_sha256")
                if not (exp_sha and kr_raw and sha256_text(kr_raw) != exp_sha):
                    valid = True
            if not valid:
                pending_cnt += 1
            elif is_ai_entry(hit):
                ai_cnt += 1
            else:
                human_cnt += 1

        w = b["wave"]
        wave_Rollup[w]["batches"] += 1
        wave_Rollup[w]["unique_slots"] += len(seen)
        wave_Rollup[w]["human"] += human_cnt
        wave_Rollup[w]["ai"] += ai_cnt
        wave_Rollup[w]["pending"] += pending_cnt

        done = human_cnt + ai_cnt
        pct = round(100.0 * done / len(seen), 2) if seen else 100.0
        batch_rows.append(
            {
                "id": b["id"],
                "wave": w,
                "category": b["category"],
                "slug": b["slug"],
                "zwrotka_path": b["zwrotka_path"],
                "title": b["title"],
                "elements": b["elements"],
                "unique_slots": len(seen),
                "human_done": human_cnt,
                "ai_done": ai_cnt,
                "pending": pending_cnt,
                "percent_done": pct,
                "logical_files_count": b["logical_files_count"],
                "shared_logical_files_count": len(b["shared_logical_files"]),
                "logical_files": b["logical_files"],
            }
        )

    totals = {
        "batches": len(batch_rows),
        "unique_slots": sum(r["unique_slots"] for r in batch_rows),
        "human_done": sum(r["human_done"] for r in batch_rows),
        "ai_done": sum(r["ai_done"] for r in batch_rows),
        "pending": sum(r["pending"] for r in batch_rows),
    }
    return {"totals": totals, "waves": wave_Rollup, "batches": batch_rows}


def render_batch_markdown(
    batch: dict,
    corpus: Corpus,
    store: TranslationStore | None = None,
    ref: LocalizeReference | None = None,
) -> str:
    """Render one self-contained Markdown file compatible with ``import_zwrotki.py --ai``."""
    entries: list[PlannedEntry] = batch["_entries"]
    lines: list[str] = [
        f"# Paczka AI {batch['id']} (Fala {batch['wave']} · {batch['category']}) — {batch['title']}",
        "",
        "Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).",
        "Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.",
        f"Po wypełnieniu zapisz plik jako `{batch['zwrotka_path']}` i zaimportuj poleceniem:",
        f"`python3 tools/import_zwrotki.py --ai {batch['zwrotka_path']}`.",
        "",
        "- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.",
        "- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).",
        "",
    ]

    next_seq = 1
    seen_text_key_to_seq: dict[tuple[str, str], int] = {}
    seen_gl_key_to_seq: dict[tuple[str, str, str], int] = {}

    # Group consecutive entries by section_heading to keep clean ## headers
    grouped_sections: list[tuple[str, list[str], list[PlannedEntry]]] = []
    for e in entries:
        if grouped_sections and grouped_sections[-1][0] == e.section_heading:
            grouped_sections[-1][2].append(e)
        else:
            grouped_sections.append((e.section_heading, e.context_lines, [e]))

    for heading, ctx_lines, sec_entries in grouped_sections:
        clean_heading = heading if heading.startswith("## ") else f"## {heading}"
        gl_entries = [x for x in sec_entries if x.kind == "view_glossary"]
        item_entries = [x.item for x in sec_entries if x.kind == "section_item" and x.item is not None]

        if gl_entries:
            lines.append(clean_heading)
            for cl in ctx_lines:
                lines.append(cl if cl.startswith("- ") else f"- {cl}")
            lines.append("")
            for ge in gl_entries:
                seq = next_seq
                next_seq += 1
                src_enc = encode_view_text(ge.src_raw)
                ref_enc = encode_view_text(ge.ref_raw)
                head = src_enc or f"{ref_enc} (tylko EN)"
                gkey_tup = (ge.glossary_kind, src_enc, ref_enc)
                lines.append(f"{seq}. {head}")
                lines.append(f"   źródło: {ge.logical_file} :: {ge.addrs[0]}")
                lines.append(f"   słownik: {ge.glossary_kind}")
                if gkey_tup in seen_gl_key_to_seq:
                    lines.append(
                        f"   (powtórzenie elementu {seen_gl_key_to_seq[gkey_tup]} — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)"
                    )
                else:
                    seen_gl_key_to_seq[gkey_tup] = seq
                    lines.append(f"   EN: {ref_enc or '(brak wersji angielskiej)'}")
                    lines.append("   PL:")
            lines.append("")

        if item_entries:
            sec_block = SectionBlock(
                heading=clean_heading,
                context_lines=ctx_lines,
                items=item_entries,
            )
            sec_lines, next_seq, _, _ = render_section_lines(
                corpus,
                sec_block,
                seen=seen_text_key_to_seq,
                next_seq=next_seq,
            )
            lines.extend(sec_lines)

    md_text = "\n".join(lines).rstrip() + "\n"
    if store is not None and ref is not None:
        md_text, _, _ = _prefill_view_md(md_text, store, ref, entry_filter="all")
    return md_text


def build_manifest_payload(
    index_manifest: dict,
    status_data: dict,
    excluded_counts: dict[str, int],
    excluded_files: dict[str, set[str]],
) -> dict:
    buildid, zrodlo, kr_sha, en_sha = parse_index_manifest(index_manifest)
    excluded_summary = [
        {
            "reason": reason,
            "logical_files": len(excluded_files.get(reason, set())),
            "elements_skipped": count,
        }
        for reason, count in sorted(excluded_counts.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    return {
        "format_version": 1,
        "policy": "D-11 (AI-tymczasowe wyłącznie dla UI, opisów technicznych i meta/statystyk; pełny priorytet tłumacza)",
        "steam_buildid": None if buildid == "unknown" else buildid,
        "zrodlo_localize": zrodlo,
        "localize_kr_sha256": kr_sha,
        "localize_en_sha256": en_sha,
        "target_unique_slots_per_batch": TARGET_BATCH_TODO,
        "zwrotki_dir": "zwrotki/ai",
        "import_command_template": "python3 tools/import_zwrotki.py --ai zwrotki/ai/<PLIK>.md",
        "excluded_scope": {
            "story_scenes": "100% StoryData/*.json (czytanki/sceny/ i mowcy-i-miejsca.md — wyłącznie tłumacz)",
            "view_exclusions": excluded_summary,
            "total_view_elements_excluded": sum(excluded_counts.values()),
        },
        "summary": status_data["totals"],
        "waves": {str(k): v for k, v in status_data["waves"].items()},
        "categories": [
            {
                "key": spec.key,
                "wave": spec.wave,
                "slug": spec.slug,
                "title": spec.title,
                "description": spec.description,
            }
            for spec in sorted(CATEGORIES.values(), key=lambda s: s.order)
        ],
        "batches": status_data["batches"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--localize", type=Path, default=ROOT / "index" / "localize")
    parser.add_argument("--static-data", type=Path, default=ROOT / "index" / "static-data")
    parser.add_argument("--story-index", type=Path, default=ROOT / "wiedza" / "indeks_fabuly.json")
    parser.add_argument("--index-manifest", type=Path, default=ROOT / "index" / "MANIFEST.json")
    parser.add_argument("--tlumaczenie", type=Path, default=ROOT / "tlumaczenie")
    parser.add_argument("--manifest-out", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="zapisz deterministyczny manifest paczek do paczki_ai/MANIFEST.json",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="wypisz podsumowanie postępu fal i paczek (tłumacz vs AI vs pozostałe)",
    )
    parser.add_argument(
        "--render",
        nargs="*",
        metavar="BATCH_ID",
        help="wygeneruj gotowe pliki .md dla wskazanych paczek (np. P01 P02)",
    )
    parser.add_argument(
        "--wave",
        type=int,
        choices=(1, 2, 3),
        help="wygeneruj wszystkie paczki z wybranej fali (1, 2 lub 3)",
    )
    parser.add_argument(
        "--render-all",
        action="store_true",
        help="wygeneruj pliki .md wszystkich paczek do katalogu --out",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_RENDER_OUT,
        help="katalog wyjściowy wyrenderowanych paczek roboczych (domyślnie: local/paczki_ai)",
    )
    args = parser.parse_args(argv)

    static = StaticData(args.static_data) if args.static_data.is_dir() else None
    store = TranslationStore.load(args.tlumaczenie)
    story_index = json.loads(args.story_index.read_text(encoding="utf-8"))
    index_manifest = (
        json.loads(args.index_manifest.read_text(encoding="utf-8"))
        if args.index_manifest.is_file()
        else {}
    )

    with Snapshot.open(args.localize) as snapshot:
        corpus, domains, mc_blocks, _ = build_view_model(snapshot, static=static)
        entries, excluded_counts, excluded_files = collect_plan_data(corpus, domains, mc_blocks)
        batches = partition_into_batches(entries, target_todo=TARGET_BATCH_TODO)
        status_data = compute_batch_status(batches, store, corpus)

        if args.write_manifest:
            payload = build_manifest_payload(
                index_manifest=index_manifest,
                status_data=status_data,
                excluded_counts=excluded_counts,
                excluded_files=excluded_files,
            )
            args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
            args.manifest_out.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            print(f"Zapisano manifest paczek AI: {args.manifest_out} ({len(batches)} paczek)")

        wanted_ids: set[str] = set()
        if args.render is not None:
            wanted_ids.update(x.upper() for x in args.render)
        if args.wave is not None:
            wanted_ids.update(b["id"] for b in batches if b["wave"] == args.wave)
        if args.render_all:
            wanted_ids.update(b["id"] for b in batches)

        if wanted_ids:
            ref = LocalizeReference(snapshot, story_index)
            batch_by_id = {b["id"]: b for b in batches}
            unknown = sorted(wanted_ids - set(batch_by_id))
            if unknown:
                raise SystemExit(f"Nieznane identyfikatory paczek: {', '.join(unknown)}")
            args.out.mkdir(parents=True, exist_ok=True)
            for bid in sorted(wanted_ids):
                b = batch_by_id[bid]
                md = render_batch_markdown(b, corpus, store=store, ref=ref)
                dest = args.out / f"{b['slug']}.md"
                dest.write_text(md, encoding="utf-8")
            print(f"Wyrenderowano {len(wanted_ids)} paczek .md do: {args.out}")

        if args.status or (not args.write_manifest and not wanted_ids):
            buildid, _, _, _ = parse_index_manifest(index_manifest)
            tot = status_data["totals"]
            print(
                f"Plan paczek AI (build {buildid}): "
                f"{tot['batches']} paczek, {tot['unique_slots']} unikalnych slotów PL "
                f"(tłumacz: {tot['human_done']}, AI: {tot['ai_done']}, do zrobienia: {tot['pending']})"
            )
            for w in (1, 2, 3):
                wr = status_data["waves"][w]
                print(
                    f"  Fala {w}: {wr['batches']:2d} paczek | slotów: {wr['unique_slots']:5d} "
                    f"| tłumacz: {wr['human']:4d} | AI: {wr['ai']:5d} | pozostało: {wr['pending']:5d}"
                )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
