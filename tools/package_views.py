#!/usr/bin/env python3
"""Build ``widoki.zip`` — all non-StoryData game texts with rich context.

Covers 100% of translatable string leaves outside ``StoryData/`` across both
``kr`` (source) and ``en`` (reference) in a ``Localize`` snapshot, joined with
``index/static-data/`` (Identity stats, skills, coins, passives, chapters) so
related texts appear together in human-readable context:

* ``mowcy-rpg-i-anomalii.md`` — speaker glossary for Canto X RPG dialogues,
  Abnormality check lines, and ``ScenarioModelCodes``;
* ``01_slownik_bojowy*.md`` — ``SkillTag``, attributes, battle keywords, buffs,
  sanity & panic;
* ``02_tozsamosc_01_Yi_Sang*.md`` … ``12_Gregor*.md`` — per-Sinner dossier,
  Identities (with StaticData parameters), Uptie 1–4 skills & coins, passives,
  voice lines, and Abnormality check dialogues;
* ``03_ego_postaci*.md``, ``03_dary_ego*.md`` — character E.G.O (cards,
  Awakening/Corrosion skills, passives, voice lines) and E.G.O Gifts;
* ``04_anomalie_*.md``, ``04_wydarzenia_*.md``, ``04_wrogowie_*.md`` —
  Abnormality guides, choice events + result logs, interactive events, combat
  assists, enemies, boss speech bubbles, enemy skills & passives;
* ``05_komentatorzy*.md``, ``05_muzyka_i_piosenki*.md`` — battle announcers
  (joined with cue types) and BGM titles + song lyrics;
* ``06_tryb_rpg_canto10*.md`` — Canto X RPG quests, items, NPCs, locations,
  narrations, dialogues, and choices grouped by floor;
* ``07_notatki_dantego_i_teatr*.md``, ``07_rozdzialy_*.md``, ``07_loch_*.md`` —
  Dante's Notes (paired topic + detail), Story Theater, chapters/stages,
  Dante's abilities, Mirror Dungeon, Refraction Railway, Boss Raid;
* ``08_interfejs_*.md``, ``08_samouczki_*.md``, ``08_wydarzenia_*.md``,
  ``08_przedmioty_sklep_i_profil*.md`` — UI, settings, tutorials, seasonal
  events, items, shop, banners, tickets;
* ``09_pozostale_widoki*.md`` — automatic catch-all for any future tables,
  followed by a strict 100% leaf-coverage check.
"""
from __future__ import annotations

import collections
from dataclasses import dataclass, field
from pathlib import PurePosixPath
import re
import unicodedata

from tools.build_profiles import DEFENSE, RANK, coin_text, merged_levels, number, resist_label, season, signed
from tools.lcb_text import KEYWORD, TAG, Texts, one_line, to_markdown
from tools.localize import Snapshot, field_name, iter_strings, load_json
from tools.static_data import StaticData


LINES_PER_FILE = 8000
TMP_TAG = re.compile(
    r"</?(?:(?:i|b|u|s|br|sup|sub|nobr|noparse)|(?:color|size|sprite|link|style|font|mark|align|ruby|voffset|line-height|cspace|material)(?:[= ][^<>]*)?)>",
    re.I,
)
PLACEHOLDER = re.compile(r"\{\d+\}|%[ds]")
DKR_STYLE = re.compile(r'<style="?(?:DKR|dkr)[^">]*"?>')
DEN_STYLE = re.compile(r'<style="?(?:DEN|den)[^">]*"?>')

NON_TRANSLATABLE_FIELDS = frozenset({
    "id",
    "key",
    "level",
    "abilityID",
    "model",
    "fileName",
    "undefined",
    "codeName",
    "usage",
    "imgStr",
    "debugNodeId",
    "debugNodeID",
    "debugNodeId ",
    "debugNodeID ",
    "colorCode",
    "outlineColorCode",
    "mainTextColor",
    "mainTextGlowColor",
    "iconId",
    "iconID",
    "keywords",
    "timeline",
    "chapterNumber",
    "songWriter",
})

SHORT_FIELDS = frozenset({
    "name",
    "title",
    "nameWithTitle",
    "displayName",
    "shortName",
    "longName",
    "abName",
    "abnormalityName",
    "panicName",
    "specialName",
    "skinItemTitle",
    "chapter",
    "chaptertitle",
    "parttitle",
    "company",
    "area",
    "place",
    "nickName",
    "teacher",
})

FIELD_LABELS = {
    "name": "nazwa",
    "title": "tytuł",
    "nameWithTitle": "nazwa z tytułem",
    "displayName": "nazwa wyświetlana",
    "shortName": "nazwa skrócona",
    "longName": "pełna nazwa",
    "desc": "opis",
    "description": "opis",
    "rawDesc": "opis bazowy",
    "subDesc": "podopis",
    "simpleDesc": "opis skrócony",
    "summary": "podsumowanie",
    "flavor": "tekst klimatyczny",
    "content": "tekst",
    "text": "tekst",
    "dlg": "kwestia",
    "dialog": "kwestia",
    "story": "wpis obserwacji",
    "clue": "wskazówka",
    "abName": "źródło (Anomalia)",
    "abnormalityName": "nazwa Anomalii",
    "prevDesc": "wstęp",
    "eventDesc": "opis wydarzenia",
    "behaveDesc": "pytanie / działanie",
    "successDesc": "wynik — sukces",
    "failureDesc": "wynik — porażka",
    "message": "opcja wyboru",
    "messageDesc": "podpowiedź efektu",
    "result": "rezultat wyboru",
    "panicName": "nazwa Paniki",
    "lowMoraleDescription": "efekt niskiego morale",
    "panicDescription": "efekt Paniki",
    "add": "warunek wzrostu poczytalności",
    "min": "warunek spadku poczytalności",
    "statText": "statystyki przedmiotu",
    "openCondition": "warunek odblokowania",
    "openConditionNumber": "wymagany etap",
    "relatedChapterText": "powiązany rozdział",
    "askLevelUp": "komunikat limitu poziomu",
    "company": "korporacja",
    "area": "dzielnica / obszar",
    "chapter": "numer rozdziału",
    "chaptertitle": "tytuł rozdziału",
    "parttitle": "tytuł części",
    "place": "miejsce",
    "nickName": "przydomek / oznaczenie",
    "teacher": "prowadzący",
    "variation": "wariant opisu 1",
    "variation2": "wariant opisu 2",
    "specialName": "nazwa specjalna",
    "skinItemTitle": "nazwa projekcji wyglądu",
    "skinItemDesc": "opis projekcji wyglądu",
}

SINNER_SLUGS = {
    1: "Yi_Sang",
    2: "Faust",
    3: "Don_Quixote",
    4: "Ryoshu",
    5: "Meursault",
    6: "Hong_Lu",
    7: "Heathcliff",
    8: "Ishmael",
    9: "Rodion",
    10: "Sinclair",
    11: "Outis",
    12: "Gregor",
}

ABDLG_SINNER = {
    "YiSang": 1,
    "Faust": 2,
    "DonQuixote": 3,
    "Ryoshu": 4,
    "Meursault": 5,
    "HongLu": 6,
    "Heathcliff": 7,
    "Ishmael": 8,
    "Rodion": 9,
    "Sinclair": 10,
    "Outis": 11,
    "Gregor": 12,
}


def encode_view_text(value: object) -> str:
    """Single-line representation preserving explicit ``\\n`` line breaks."""
    if not isinstance(value, str):
        return ""
    norm = value.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not norm:
        return ""
    return norm.replace("\n", "\\n")


def visible_len(raw: str) -> int:
    clean = TMP_TAG.sub("", raw.replace("\\n", "\n"))
    return len(clean)


def compute_limit(fn: str, src_enc: str, ref_enc: str) -> int:
    base = 40 if fn in SHORT_FIELDS else 120
    longest = max(visible_len(src_enc), visible_len(ref_enc))
    padded = int(longest * 1.25) + 5 if longest else base
    rounded = int(-(-max(base, padded) // 10) * 10)
    return rounded


def ascii_slug(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    out = re.sub(r"[^A-Za-z0-9]+", "_", norm).strip("_").lower()
    return out or "sekcja"


@dataclass
class PendingItem:
    label: str
    logical_file: str
    addrs: list[str]
    field: str
    src_raw: str
    ref_raw: str
    extra_notes: list[str] = field(default_factory=list)


@dataclass
class SectionBlock:
    heading: str
    context_lines: list[str] = field(default_factory=list)
    items: list[PendingItem] = field(default_factory=list)


class ViewGlossary:
    """Deduplicated speaker/model glossary for non-StoryData tables."""

    KINDS = (
        ("rpg_speaker", "Mówca w trybie RPG (Canto X)"),
        ("abdlg_teller", "Mówca w testach Anomalii (AbDlg)"),
    )

    def __init__(self) -> None:
        self.entries: dict[tuple[str, str, str], dict] = {}

    def record(self, kind: str, src_raw: str, ref_raw: str, logical_file: str, addr: str) -> None:
        src = encode_view_text(src_raw)
        ref = encode_view_text(ref_raw)
        if not src and not ref:
            return
        entry = self.entries.setdefault(
            (kind, src, ref),
            {"count": 0, "first_file": logical_file, "first_addr": addr, "sources": set()},
        )
        entry["count"] += 1
        entry["sources"].add((logical_file, addr))


class Corpus:
    """Indexed non-StoryData Localize tables across ``kr`` and ``en``."""

    def __init__(self, snapshot: Snapshot, static: StaticData | None = None,
                 source: str = "kr", reference: str = "en") -> None:
        self.snapshot = snapshot
        self.static = static
        self.src_lang = source
        self.ref_lang = reference
        self.src_texts = Texts(snapshot, source)
        self.ref_texts = Texts(snapshot, reference)
        self.kw_src = self.src_texts.keywords
        self.kw_ref = self.ref_texts.keywords
        self.known_kw_ids = (set(self.kw_src) | set(self.kw_ref) | {"ATTRIBUTES"})

        src_set = set(snapshot.files.get(source, {}))
        ref_set = set(snapshot.files.get(reference, {}))
        self.logical_files = sorted(
            f for f in (src_set | ref_set) if not f.startswith("StoryData/")
        )

        self.docs_src: dict[str, object] = {}
        self.docs_ref: dict[str, object] = {}
        self.leaves_src: dict[str, dict[str, str]] = {}
        self.leaves_ref: dict[str, dict[str, str]] = {}
        self.translatable: dict[str, list[str]] = {}
        self.consumed: set[tuple[str, str]] = set()
        self.glossary = ViewGlossary()

        for f in self.logical_files:
            ds = load_json(snapshot.read(source, f)) if f in src_set else {}
            dr = load_json(snapshot.read(reference, f)) if f in ref_set else {}
            self.docs_src[f] = ds
            self.docs_ref[f] = dr
            ls = dict(iter_strings(ds))
            lr = dict(iter_strings(dr))
            self.leaves_src[f] = ls
            self.leaves_ref[f] = lr
            # Preserve source document order first, then any EN-only tail addresses
            ordered: list[str] = []
            seen_addr: set[str] = set()
            for a in list(ls.keys()) + list(lr.keys()):
                if a in seen_addr:
                    continue
                seen_addr.add(a)
                if field_name(a) in NON_TRANSLATABLE_FIELDS:
                    continue
                if ls.get(a, "").strip() or lr.get(a, "").strip():
                    ordered.append(a)
            self.translatable[f] = ordered

    def get_pair(self, logical_file: str, addr: str) -> tuple[str, str]:
        return (
            self.leaves_src.get(logical_file, {}).get(addr, ""),
            self.leaves_ref.get(logical_file, {}).get(addr, ""),
        )

    def claim(self, logical_file: str, addr: str) -> tuple[str, str] | None:
        if addr not in self.leaves_src.get(logical_file, {}) and addr not in self.leaves_ref.get(logical_file, {}):
            return None
        if field_name(addr) in NON_TRANSLATABLE_FIELDS:
            return None
        vs, vr = self.get_pair(logical_file, addr)
        if not vs.strip() and not vr.strip():
            return None
        if (logical_file, addr) in self.consumed:
            return None
        self.consumed.add((logical_file, addr))
        return vs, vr

    def rows_by_key(self, logical_file: str, key_field: str = "id") -> tuple[list[tuple[object, dict, dict]], list[str]]:
        """Pair dataList rows between KR and EN preserving order (including EN-only rows)."""
        ds = self.docs_src.get(logical_file, {})
        dr = self.docs_ref.get(logical_file, {})
        rs = ds.get("dataList", []) if isinstance(ds, dict) else []
        rr = dr.get("dataList", []) if isinstance(dr, dict) else []
        ref_map: dict[object, dict] = {}
        for idx, r in enumerate(rr or []):
            if isinstance(r, dict):
                k = r.get(key_field, f"#{idx}")
                ref_map[k] = r
        paired: list[tuple[object, dict, dict]] = []
        seen_keys: set[object] = set()
        for idx, r in enumerate(rs or []):
            if not isinstance(r, dict):
                continue
            k = r.get(key_field, f"#{idx}")
            seen_keys.add(k)
            paired.append((k, r, ref_map.get(k, {})))
        for idx, r in enumerate(rr or []):
            if not isinstance(r, dict):
                continue
            k = r.get(key_field, f"#{idx}")
            if k not in seen_keys:
                seen_keys.add(k)
                paired.append((k, {}, r))
        return paired, self.translatable.get(logical_file, [])

    def row_prefix(self, logical_file: str, row_idx: int, row: dict, key_field: str = "id") -> str:
        if key_field in row and isinstance(row[key_field], (int, str)):
            return f"dataList[{key_field}={row[key_field]}]"
        return f"dataList[#{row_idx}]"

    def claim_prefix(self, logical_file: str, addr_prefix: str) -> list[tuple[str, str, str]]:
        """Claim all unclaimed translatable leaves in ``logical_file`` starting with ``addr_prefix``."""
        out: list[tuple[str, str, str]] = []
        dot = addr_prefix + "."
        brk = addr_prefix + "["
        for addr in self.translatable.get(logical_file, []):
            if addr == addr_prefix or addr.startswith(dot) or addr.startswith(brk):
                pair = self.claim(logical_file, addr)
                if pair is not None:
                    out.append((addr, pair[0], pair[1]))
        return out

    def claim_file(self, logical_file: str) -> list[tuple[str, str, str]]:
        out: list[tuple[str, str, str]] = []
        for addr in self.translatable.get(logical_file, []):
            pair = self.claim(logical_file, addr)
            if pair is not None:
                out.append((addr, pair[0], pair[1]))
        return out

    def tokens_and_hints(self, src_raw: str, ref_raw: str, logical_file: str = "") -> tuple[list[str], list[str]]:
        """Extract TMP/placeholder/[Keyword] tokens and human-readable tag explanations."""
        toks: list[str] = []
        notes: list[str] = []
        is_lyrics = logical_file.startswith("BgmLyrics/")
        # In BgmLyrics, KR uses DKR font style while EN uses DEN (Latin) font style
        if is_lyrics and DKR_STYLE.search(src_raw) and DEN_STYLE.search(ref_raw):
            for t in DEN_STYLE.findall(ref_raw):
                if t not in toks:
                    toks.append(t)
            for t in TMP_TAG.findall(src_raw):
                if not DKR_STYLE.fullmatch(t) and t not in toks:
                    toks.append(t)
            notes.append("czcionka: użyj stylu łacińskiego z EN (<style=\"DEN_…\"> lub <style=\"den…\">), nie koreańskiego DKR")
        else:
            for t in TMP_TAG.findall(src_raw or ref_raw):
                if t not in toks:
                    toks.append(t)
        for p in PLACEHOLDER.findall(src_raw) + PLACEHOLDER.findall(ref_raw):
            if p not in toks:
                toks.append(p)
        if "\n" in src_raw or "\n" in ref_raw:
            toks.append("\\n")

        kw_hints: list[str] = []
        seen_kw: set[str] = set()
        for kw in KEYWORD.findall(src_raw) + KEYWORD.findall(ref_raw):
            if kw in self.known_kw_ids and kw not in seen_kw:
                seen_kw.add(kw)
                bracket = f"[{kw}]"
                if bracket not in toks:
                    toks.append(bracket)
                ks = self.kw_src.get(kw, "")
                kr_or_en = self.kw_ref.get(kw, "")
                if ks or kr_or_en:
                    kw_hints.append(f"[{kw}] = {ks or '—'} / {kr_or_en or '—'}")
        if kw_hints:
            notes.append("znaczenie tagów: " + "; ".join(kw_hints[:8]) + (" …" if len(kw_hints) > 8 else ""))
        return toks, notes


def human_addr_label(addr: str, default_prefix: str = "") -> str:
    """Turn a JSON address into a concise Polish field label."""
    fn = field_name(addr)
    base = FIELD_LABELS.get(fn, fn)
    parts: list[str] = []
    if default_prefix:
        parts.append(default_prefix)
    lvl = re.search(r"levelList\[level=(\d+)\]", addr)
    if lvl:
        parts.append(f"ulepszenie {lvl[1]}")
    coin = re.search(r"coinlist\[#(\d+)\]", addr)
    cd = re.search(r"coindescs\[#(\d+)\]", addr)
    if coin:
        c_num = int(coin[1]) + 1
        if cd:
            parts.append(f"moneta {c_num}, efekt {int(cd[1]) + 1}")
        else:
            parts.append(f"moneta {c_num}")
    sl = re.search(r"storyList\[level=(\d+)\]", addr)
    if sl:
        parts.append(f"poziom obserwacji {sl[1]}")
    opt = re.search(r"options\[#(\d+)\]", addr)
    if opt:
        parts.append(f"opcja {int(opt[1]) + 1}")
    res = re.search(r"result\[#(\d+)\]", addr)
    if res and fn == "result":
        parts.append(f"wariant {int(res[1]) + 1}")
    sd = re.search(r"(successDesc|failureDesc)\[#(\d+)\]", addr)
    if sd:
        parts.append(f"wariant {int(sd[2]) + 1}")
    step = re.search(r"steps\[#(\d+)\]", addr)
    if step:
        parts.append(f"krok {int(step[1]) + 1}")
    gd = re.match(r"goalDescription(\d+)$", fn)
    if gd:
        base = f"cel zadania {gd[1]}"
    parts.append(base)
    return " — ".join(parts)


def make_skill_items(
    corpus: Corpus,
    logical_file: str,
    skill_id: object,
    prefix_label: str,
) -> list[PendingItem]:
    """Claim a skill row and merge identical texts across Uptie levels 1–4."""
    addr_prefix = f"dataList[id={skill_id}]"
    claimed = corpus.claim_prefix(logical_file, addr_prefix)
    if not claimed:
        return []
    # Group leaves that only differ by levelList[level=N] when (src_enc, ref_enc) are identical
    grouped: list[dict] = []
    index_by_sig: dict[tuple[str, str, str], int] = {}
    for addr, vs, vr in claimed:
        src_enc = encode_view_text(vs)
        ref_enc = encode_view_text(vr)
        lvl_match = re.search(r"levelList\[level=(\d+)\]", addr)
        if lvl_match:
            norm_addr = re.sub(r"levelList\[level=\d+\]", "levelList[level=*]", addr, count=1)
            sig = (norm_addr, src_enc, ref_enc)
            if sig in index_by_sig:
                entry = grouped[index_by_sig[sig]]
                entry["addrs"].append(addr)
                entry["levels"].append(lvl_match[1])
                continue
            index_by_sig[sig] = len(grouped)
            grouped.append({
                "norm_addr": norm_addr,
                "addrs": [addr],
                "levels": [lvl_match[1]],
                "field": field_name(addr),
                "vs": vs,
                "vr": vr,
            })
        else:
            grouped.append({
                "norm_addr": addr,
                "addrs": [addr],
                "levels": [],
                "field": field_name(addr),
                "vs": vs,
                "vr": vr,
            })

    items: list[PendingItem] = []
    for g in grouped:
        first_addr = g["addrs"][0]
        if g["levels"]:
            lvls = g["levels"]
            lvl_txt = (f"ulepszenie {lvls[0]}" if len(lvls) == 1
                       else f"ulepszenia {lvls[0]}–{lvls[-1]}" if [int(x) for x in lvls] == list(range(int(lvls[0]), int(lvls[-1]) + 1))
                       else "ulepszenia " + ",".join(lvls))
            stripped = re.sub(r"\.levelList\[level=\d+\]", "", first_addr)
            label = human_addr_label(stripped, f"{prefix_label} ({lvl_txt})")
        else:
            label = human_addr_label(first_addr, prefix_label)
        items.append(PendingItem(
            label=label,
            logical_file=logical_file,
            addrs=g["addrs"],
            field=g["field"],
            src_raw=g["vs"],
            ref_raw=g["vr"],
        ))
    return items


def append_generic_file_sections(
    corpus: Corpus,
    logical_files: list[str],
    section_prefix: str = "",
) -> list[SectionBlock]:
    """Claim remaining rows from ``logical_files`` preserving row grouping & context."""
    blocks: list[SectionBlock] = []
    for f in logical_files:
        unclaimed = [a for a in corpus.translatable.get(f, []) if (f, a) not in corpus.consumed]
        if not unclaimed:
            continue
        ds = corpus.docs_src.get(f, {})
        dr = corpus.docs_ref.get(f, {})
        key_field = "key" if (
            isinstance(ds, dict) and ds.get("dataList") and isinstance(ds["dataList"][0], dict) and "key" in ds["dataList"][0]
        ) or (
            isinstance(dr, dict) and dr.get("dataList") and isinstance(dr["dataList"][0], dict) and "key" in dr["dataList"][0]
        ) else "id"
        paired_rows, _ = corpus.rows_by_key(f, key_field=key_field)
        items: list[PendingItem] = []
        ctx: list[str] = [f"- plik gry: `{f}`"]
        if paired_rows:
            for idx, (rk, rs, rr) in enumerate(paired_rows):
                row_sample = rs or rr
                rpref = corpus.row_prefix(f, idx, row_sample, key_field=key_field)
                claimed = corpus.claim_prefix(f, rpref)
                if not claimed:
                    continue
                row_head = str(rk)
                code = rs.get("codeName") or rr.get("codeName")
                sw = rs.get("songWriter") or rr.get("songWriter")
                extra_tag = f" · kod {code}" if code else (f" · wykonawca: {sw}" if sw else "")
                for addr, vs, vr in claimed:
                    fn = field_name(addr)
                    if f.startswith("RPGSystem/") and fn == "speaker":
                        corpus.glossary.record("rpg_speaker", vs, vr, f, addr)
                        continue
                    if f.startswith("AbDlg") and fn == "teller":
                        corpus.glossary.record("abdlg_teller", vs, vr, f, addr)
                        continue
                    lbl_prefix = f"{section_prefix} [{row_head}{extra_tag}]".strip()
                    notes: list[str] = []
                    if f.startswith("AbDlg"):
                        teller_s = one_line(rs.get("teller", ""))
                        teller_r = one_line(rr.get("teller", ""))
                        usage = rs.get("usage") or rr.get("usage")
                        if teller_s or teller_r:
                            lbl_prefix = f"Test Anomalii — {teller_s or teller_r}" + (
                                f" ({teller_r})" if teller_s and teller_r and teller_s != teller_r else ""
                            )
                        if usage:
                            notes.append(f"warunek użycia w grze: {usage}")
                    items.append(PendingItem(
                        label=human_addr_label(addr, lbl_prefix),
                        logical_file=f,
                        addrs=[addr],
                        field=fn,
                        src_raw=vs,
                        ref_raw=vr,
                        extra_notes=notes,
                    ))
        # Also catch any top-level / non-dataList leaves in this file
        for addr, vs, vr in corpus.claim_file(f):
            fn = field_name(addr)
            items.append(PendingItem(
                label=human_addr_label(addr, section_prefix or f[:-5]),
                logical_file=f,
                addrs=[addr],
                field=fn,
                src_raw=vs,
                ref_raw=vr,
            ))
        if items:
            title = f"{section_prefix}: {f[:-5]}" if section_prefix else f[:-5]
            blocks.append(SectionBlock(heading=f"## {title}", context_lines=ctx, items=items))
    return blocks


def render_section_lines(
    corpus: Corpus,
    block: SectionBlock,
    seen: dict[tuple[str, str], int],
    next_seq: int,
) -> tuple[list[str], int, int, int]:
    """Render one ``SectionBlock`` to Markdown lines, updating per-file ``seen``."""
    lines: list[str] = [block.heading]
    if block.context_lines:
        lines.extend(block.context_lines)
    lines.append("")
    elements = 0
    todo = 0
    for item in block.items:
        src_enc = encode_view_text(item.src_raw)
        ref_enc = encode_view_text(item.ref_raw)
        if not src_enc and not ref_enc:
            continue
        seq = next_seq
        next_seq += 1
        elements += 1
        if src_enc:
            head_text = src_enc
            head_label = item.label
        else:
            head_text = ref_enc
            head_label = f"{item.label} — tylko EN w danych gry"
        lines.append(f"{seq}. [{head_label}] {head_text}")
        joined_addrs = " ; ".join(item.addrs)
        lines.append(f"   źródło: {item.logical_file} :: {joined_addrs}")
        for note in item.extra_notes:
            lines.append(f"   kontekst: {note}")
        dedup_key = (src_enc, ref_enc)
        if dedup_key in seen:
            lines.append(
                f"   (powtórzenie elementu {seen[dedup_key]} — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)"
            )
            continue
        seen[dedup_key] = seq
        todo += 1
        lim = compute_limit(item.field, src_enc, ref_enc)
        lines.append(f"   limit: do {lim} znaków")
        toks, tok_notes = corpus.tokens_and_hints(item.src_raw, item.ref_raw, item.logical_file)
        if toks:
            lines.append("   tokeny: zachowaj dokładnie: " + ", ".join(toks))
        for tn in tok_notes:
            lines.append(f"   {tn}")
        lines.append(f"   EN: {ref_enc or '(brak wersji angielskiej)'}")
        lines.append("   PL:")
    lines.append("")
    return lines, next_seq, elements, todo


def chunk_domain_files(
    corpus: Corpus,
    base: str,
    title: str,
    intro: str,
    blocks: list[SectionBlock],
) -> tuple[dict[str, str], int, int]:
    """Split a domain's ``SectionBlock`` list into ``<= LINES_PER_FILE`` Markdown files."""
    non_empty = [b for b in blocks if b.items]
    if not non_empty:
        return {}, 0, 0

    # Further split oversized single SectionBlocks (> 500 items) into sub-blocks so every file stays <= LINES_PER_FILE
    normalized: list[SectionBlock] = []
    max_items_per_block = 700
    for b in non_empty:
        if len(b.items) <= max_items_per_block:
            normalized.append(b)
        else:
            parts = -(-len(b.items) // max_items_per_block)
            for idx in range(parts):
                sub = b.items[idx * max_items_per_block:(idx + 1) * max_items_per_block]
                normalized.append(SectionBlock(
                    heading=f"{b.heading} (część {idx + 1}/{parts})",
                    context_lines=b.context_lines,
                    items=sub,
                ))

    # First estimate chunk boundaries, then render each chunk cleanly with fresh per-file numbering 1..K & dedup!
    chunks: list[list[SectionBlock]] = []
    cur: list[SectionBlock] = []
    est_lines = 0
    for b in normalized:
        b_est = len(b.context_lines) + 4 + len(b.items) * 7
        if cur and est_lines + b_est > LINES_PER_FILE:
            chunks.append(cur)
            cur = []
            est_lines = 0
        cur.append(b)
        est_lines += b_est
    if cur:
        chunks.append(cur)

    files: dict[str, str] = {}
    total_elements = 0
    total_todo = 0
    note = (
        "Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\\n` oznacza łamanie linii w oknie gry — "
        "zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`."
    )
    for idx, chunk in enumerate(chunks):
        if len(chunks) == 1:
            suffix = ""
            part_label = ""
        elif len(chunks) <= 26:
            letter = chr(ord("a") + idx)
            suffix = f"_{letter}"
            part_label = f" (część {letter})"
        else:
            suffix = f"_{idx + 1:02d}"
            part_label = f" (część {idx + 1})"
        head = [
            f"# {title}{part_label} — Limbus Company",
            "",
            intro,
            "",
            note,
            "",
        ]
        seen: dict[tuple[str, str], int] = {}
        seq = 1
        body: list[str] = []
        for b in chunk:
            b_lines, seq, el, td = render_section_lines(corpus, b, seen, seq)
            total_elements += el
            total_todo += td
            body.extend(b_lines)
        files[f"{base}{suffix}.md"] = "\n".join(head + body).rstrip() + "\n"
    return files, total_elements, total_todo


def _find_skill_location(corpus: Corpus, skill_files: list[str]) -> dict[str, str]:
    """Map skill ``str(id)`` -> logical file (preferring the first file with non-empty text)."""
    mapping: dict[str, str] = {}
    for f in skill_files:
        for rk, _, _ in corpus.rows_by_key(f)[0]:
            key = str(rk)
            if key not in mapping and corpus.translatable.get(f):
                mapping[key] = f
    return mapping


def build_combat_dictionary(corpus: Corpus) -> list[SectionBlock]:
    """01 — SkillTag, attributes, BattleKeywords, Bufs, sanity & panic."""
    blocks: list[SectionBlock] = []

    # 1. SkillTag
    if "SkillTag.json" in corpus.docs_src or "SkillTag.json" in corpus.docs_ref:
        items: list[PendingItem] = []
        for rk, rs, rr in corpus.rows_by_key("SkillTag.json")[0]:
            for addr, vs, vr in corpus.claim_prefix("SkillTag.json", f"dataList[id={rk}]"):
                items.append(PendingItem(
                    label=f"Tag umiejętności [{rk}] — {FIELD_LABELS.get(field_name(addr), field_name(addr))}",
                    logical_file="SkillTag.json",
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                    extra_notes=[f"w opisach umiejętności zapisywany jako `[{rk}]` — gra podstawia tu ten napis"],
                ))
        if items:
            blocks.append(SectionBlock(
                heading="## Tagi warunków umiejętności (SkillTag)",
                context_lines=[
                    "- Te etykiety (np. `[On Use]`, `[Heads Hit]`) gra wstawia automatycznie w miejsce tagów `[WhenUse]`, `[OnSucceedAttackHead]` w opisach umiejętności.",
                ],
                items=items,
            ))

    # 2. Attributes, resistances, keyword dictionaries, unit keywords
    core_files = [
        f for f in corpus.logical_files
        if f in {"AttributeText.json", "ResistText.json", "KeywordDictionary.json", "SynergyKeyword.json"}
        or f.startswith("UnitKeyword")
    ]
    blocks.extend(append_generic_file_sections(corpus, core_files, "Pojęcia bazowe i cechy jednostek"))

    # 3. BattleKeywords* + Bufs* + BuffAbilities
    kw_files = [f for f in corpus.logical_files if f.startswith("BattleKeywords")]
    for f in kw_files:
        items = []
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(f)[0]):
            rpref = corpus.row_prefix(f, idx, rs or rr)
            for addr, vs, vr in corpus.claim_prefix(f, rpref):
                items.append(PendingItem(
                    label=human_addr_label(addr, f"Słowo kluczowe [{rk}]"),
                    logical_file=f,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                    extra_notes=[f"identyfikator tagu w tekstach: `[{rk}]`"] if field_name(addr) == "name" else [],
                ))
        if items:
            blocks.append(SectionBlock(
                heading=f"## Słowa kluczowe bitwy — {f[:-5]}",
                context_lines=[f"- plik gry: `{f}` (opisy wyświetlane w dymkach pomocy podczas walki)"],
                items=items,
            ))

    buf_files = [f for f in corpus.logical_files if f.startswith("Bufs") or f == "BuffAbilities.json"]
    for f in buf_files:
        items = []
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(f)[0]):
            rpref = corpus.row_prefix(f, idx, rs or rr)
            for addr, vs, vr in corpus.claim_prefix(f, rpref):
                items.append(PendingItem(
                    label=human_addr_label(addr, f"Status [{rk}]"),
                    logical_file=f,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                    extra_notes=[f"identyfikator statusu w tekstach: `[{rk}]`"] if field_name(addr) == "name" else [],
                ))
        if items:
            blocks.append(SectionBlock(
                heading=f"## Statusy i efekty bojowe — {f[:-5]}",
                context_lines=[f"- plik gry: `{f}`"],
                items=items,
            ))

    # 4. MentalCondition* + PanicInfo*
    sanity_files = [
        f for f in corpus.logical_files
        if f.startswith("MentalCondition") or f.startswith("PanicInfo")
    ]
    blocks.extend(append_generic_file_sections(corpus, sanity_files, "Poczytalność i Panika"))
    return blocks


def build_sinners_and_identities(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """02 — Per-Sinner Identity cards + skills + passives + voice lines + AbDlg."""
    static = corpus.static
    sd_pers = {r["id"]: r for r in (static.rows("personality") if static else []) if "id" in r}
    sd_skills = {r["id"]: r for r in (static.rows("skill") if static else []) if "id" in r}
    sd_psets = {r.get("personalityID"): r for r in (static.rows("personality-passive") if static else [])}
    sd_prules = {r["id"]: r for r in (static.rows("passive") if static else []) if "id" in r}

    sins_en = {k: one_line(to_markdown(v.get("name"))) for k, v in corpus.ref_texts.by_id("AttributeText").items()}
    chars_kr = corpus.src_texts.by_id("Characters")
    chars_en = corpus.ref_texts.by_id("Characters")

    # Map Korean character name -> characterId (1..12)
    kr_name_to_cid: dict[str, int] = {}
    for cid in range(1, 13):
        kn = one_line(chars_kr.get(str(cid), {}).get("name", ""))
        if kn:
            kr_name_to_cid[kn] = cid

    pers_files = [f for f in corpus.logical_files if f.startswith("Personalities")]
    skill_pers_files = [
        f for f in corpus.logical_files
        if f.startswith("Skills_personality") or f == "Skills.json"
    ]
    passive_player_files = [
        f for f in corpus.logical_files
        if re.match(r"^Passives(?:-[A-Za-z0-9-]+)?\.json$", f) or re.match(r"^Passive-[A-Za-z0-9-]+\.json$", f)
    ]
    voice_files = [f for f in corpus.logical_files if f.startswith("PersonalityVoiceDlg/")]

    skill_loc = _find_skill_location(corpus, skill_pers_files)
    passive_loc = _find_skill_location(corpus, passive_player_files)

    voice_by_pid: dict[int, list[str]] = collections.defaultdict(list)
    for vf in voice_files:
        m = re.search(r"_(\d{5,6})\.json$", vf)
        if m:
            voice_by_pid[int(m[1])].append(vf)

    # Collect all Personality rows across Personalities*.json and assign to Sinner 1..12
    identities_by_cid: dict[int, list[tuple[str, int, dict, dict]]] = collections.defaultdict(list)
    for pf in pers_files:
        for rk, rs, rr in corpus.rows_by_key(pf)[0]:
            if not isinstance(rk, int):
                continue
            pid = rk
            cid = sd_pers.get(pid, {}).get("characterId")
            if not isinstance(cid, int):
                kn = one_line(rs.get("name", ""))
                cid = kr_name_to_cid.get(kn, 0)
            if not cid and 10100 <= pid <= 11299:
                cid = (pid // 100) % 100
            identities_by_cid[cid if 1 <= cid <= 12 else 0].append((pf, pid, rs, rr))

    def passive_req(passive_id: int) -> str:
        rule = sd_prules.get(passive_id, {})
        parts = []
        for fld, lbl in (("attributeStockCondition", "posiadane"), ("attributeResonanceCondition", "rezonans")):
            for cond in rule.get(fld, []) or []:
                parts.append(f"{lbl} {cond.get('value')}× {sins_en.get(str(cond.get('type')), cond.get('type'))}")
        return ", ".join(parts)

    def skill_stat_note(skill_id: int) -> str:
        sdata = sd_skills.get(skill_id, {})
        rows = merged_levels(sdata.get("skillData", []) or [])
        if not rows:
            return ""
        _, st = rows[-1]
        sin_name = sins_en.get(str(st.get("attributeType")), str(st.get("attributeType") or "—"))
        kind = DEFENSE.get(st.get("defType")) if st.get("defType") != "ATTACK" else str(st.get("atkType") or "—").title()
        coins = st.get("coinList", []) or []
        return (
            f"grzech: {sin_name} · typ: {kind} · moc bazowa: {number(st.get('defaultValue', '—'))} · "
            f"monety: {len(coins)} ({coin_text(coins)})"
        )

    domains: list[tuple[str, str, str, list[SectionBlock]]] = []
    # Map IntroduceCharacter rows by characterId / order
    intro_rows = corpus.rows_by_key("IntroduceCharacter.json")[0] if (
        "IntroduceCharacter.json" in corpus.docs_src or "IntroduceCharacter.json" in corpus.docs_ref
    ) else []
    intro_by_cid: dict[int, tuple[int, object, dict, dict]] = {}
    for idx, (rk, rs, rr) in enumerate(intro_rows):
        kn = one_line(rs.get("name", ""))
        cid = kr_name_to_cid.get(kn) or (rk if isinstance(rk, int) and 1 <= rk <= 12 else 0)
        if cid:
            intro_by_cid[cid] = (idx, rk, rs, rr)

    all_cids = sorted(cid for cid in set(identities_by_cid) | set(range(1, 13)) if 1 <= cid <= 12)
    for cid in all_cids:
        en_char = one_line(chars_en.get(str(cid), {}).get("name", "")) or SINNER_SLUGS.get(cid, f"Postac_{cid}")
        kr_char = one_line(chars_kr.get(str(cid), {}).get("name", ""))
        slug_name = SINNER_SLUGS.get(cid, ascii_slug(en_char))
        sinner_blocks: list[SectionBlock] = []

        # Dossier section (Characters.json + IntroduceCharacter.json)
        dossier_items: list[PendingItem] = []
        for addr, vs, vr in corpus.claim_prefix("Characters.json", f"dataList[id={cid}]"):
            dossier_items.append(PendingItem(
                label=human_addr_label(addr, "Grzesznik"),
                logical_file="Characters.json",
                addrs=[addr],
                field=field_name(addr),
                src_raw=vs,
                ref_raw=vr,
            ))
        if cid in intro_by_cid:
            i_idx, i_rk, i_rs, i_rr = intro_by_cid[cid]
            ipref = corpus.row_prefix("IntroduceCharacter.json", i_idx, i_rs or i_rr)
            for addr, vs, vr in corpus.claim_prefix("IntroduceCharacter.json", ipref):
                dossier_items.append(PendingItem(
                    label=human_addr_label(addr, "Akta więźnia"),
                    logical_file="IntroduceCharacter.json",
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                ))
        if dossier_items:
            sinner_blocks.append(SectionBlock(
                heading=f"## Grzesznik #{cid:02d}: {en_char}" + (f" ({kr_char})" if kr_char else ""),
                context_lines=["- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia."],
                items=dossier_items,
            ))

        # Each Identity card of this Sinner
        for pf, pid, rs, rr in sorted(identities_by_cid.get(cid, []), key=lambda x: (x[1], x[0])):
            id_items: list[PendingItem] = []
            p_row = sd_pers.get(pid, {})
            title_en = one_line(to_markdown(rr.get("title", ""))) or one_line(to_markdown(rs.get("title", ""))) or str(pid)
            title_kr = one_line(to_markdown(rs.get("title", "")))
            rank_str = RANK.get(p_row.get("rank"), "?")
            ctx = [f"- ID Tożsamości: `{pid}` (plik: `{pf}`)"]
            if p_row:
                hp = p_row.get("hp", {}) or {}
                speeds = " / ".join(f"{a}–{b}" for a, b in zip(p_row.get("minSpeedList", []), p_row.get("maxSpeedList", [])))
                resist = ", ".join(
                    f"{r.get('type', '').title()} {resist_label(r.get('value'))}"
                    for r in (p_row.get("resistInfo", {}) or {}).get("atkResistList", [])
                )
                kws = ", ".join(corpus.kw_ref.get(k, k) for k in p_row.get("skillKeywordList", []) or []) or "—"
                ctx.append(
                    f"- parametry karty: rzadkość `{rank_str}` · sezon: {season(p_row.get('season'))} · "
                    f"HP bazowe: {number(hp.get('defaultStat', '—'))} · szybkość: {speeds or '—'}"
                )
                ctx.append(f"- odporności: {resist or '—'} · słowa kluczowe: {kws}")

            # 1) Card strings
            for addr, vs, vr in corpus.claim_prefix(pf, f"dataList[id={pid}]"):
                id_items.append(PendingItem(
                    label=human_addr_label(addr, "Karta Tożsamości"),
                    logical_file=pf,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                ))

            # 2) Skills from StaticData attributeList + defenseSkillIDList (or ID prefix fallback pid*100 + 1..9)
            skill_entries: list[tuple[int, str]] = []
            if p_row:
                for s_i, attr in enumerate(p_row.get("attributeList", []) or [], 1):
                    sid = attr.get("skillId")
                    if isinstance(sid, int):
                        skill_entries.append((sid, f"Umiejętność {s_i} (×{attr.get('number')})"))
                for sid in p_row.get("defenseSkillIDList", []) or []:
                    if isinstance(sid, int):
                        skill_entries.append((sid, "Obrona"))
            # Fallback: any skill in Skills_personality-{cid:02d}.json starting with str(pid)
            sp_file = f"Skills_personality-{cid:02d}.json"
            if sp_file in corpus.docs_src or sp_file in corpus.docs_ref:
                known_sids = {s for s, _ in skill_entries}
                for rk, _, _ in corpus.rows_by_key(sp_file)[0]:
                    if isinstance(rk, int) and str(rk).startswith(str(pid)) and rk not in known_sids:
                        skill_entries.append((rk, f"Umiejętność powiązana {rk}"))

            for sid, slabel in skill_entries:
                sf = skill_loc.get(str(sid))
                if not sf:
                    continue
                s_items = make_skill_items(corpus, sf, sid, slabel)
                stat_note = skill_stat_note(sid)
                if s_items and stat_note:
                    s_items[0].extra_notes.insert(0, stat_note)
                id_items.extend(s_items)

            # 3) Passives from StaticData personality-passive (or ID prefix fallback)
            pset = sd_psets.get(pid, {})
            passive_entries: list[tuple[int, str]] = []
            for pfld, plbl in (("battlePassiveList", "Pasywka bojowa"), ("supporterPassiveList", "Pasywka wsparcia")):
                for entry in pset.get(pfld, []) or []:
                    for pas_id in entry.get("passiveIDList", []) or []:
                        if isinstance(pas_id, int):
                            req = passive_req(pas_id)
                            meta = f"od ulepszenia {entry.get('level')}" + (f", {req}" if req else "")
                            passive_entries.append((pas_id, f"{plbl} ({meta})"))
            known_pas = {pas_id for pas_id, _ in passive_entries}
            pid_str = str(pid)
            for pas_key in sorted(passive_loc):
                if pas_key.isdigit() and len(pas_key) == len(pid_str) + 2 and pas_key.startswith(pid_str):
                    pas_id = int(pas_key)
                    if pas_id not in known_pas:
                        kind_lbl = "Pasywka wsparcia" if pas_key.endswith("21") else "Pasywka bojowa"
                        passive_entries.append((pas_id, f"{kind_lbl} [{pas_id}]"))
                        known_pas.add(pas_id)
            for pas_id, plbl in passive_entries:
                pfile = passive_loc.get(str(pas_id))
                if not pfile:
                    continue
                for addr, vs, vr in corpus.claim_prefix(pfile, f"dataList[id={pas_id}]"):
                    id_items.append(PendingItem(
                        label=human_addr_label(addr, plbl),
                        logical_file=pfile,
                        addrs=[addr],
                        field=field_name(addr),
                        src_raw=vs,
                        ref_raw=vr,
                    ))

            # 4) Voice lines of this Identity
            for vf in voice_by_pid.get(pid, []):
                for idx, (vrk, vrs, vrr) in enumerate(corpus.rows_by_key(vf)[0]):
                    vpref = corpus.row_prefix(vf, idx, vrs or vrr)
                    cue_en = one_line(vrr.get("desc", "")) or one_line(vrs.get("desc", ""))
                    for addr, vs, vr in corpus.claim_prefix(vf, vpref):
                        fn = field_name(addr)
                        lbl = (
                            f"Kwestia głosowa [{vrk}] — sytuacja"
                            if fn == "desc"
                            else f"Kwestia głosowa [{vrk}] ({cue_en or 'wypowiedź'})"
                        )
                        id_items.append(PendingItem(
                            label=lbl,
                            logical_file=vf,
                            addrs=[addr],
                            field=fn,
                            src_raw=vs,
                            ref_raw=vr,
                        ))

            if id_items:
                head_kr = f" — {title_kr}" if title_kr and title_kr != title_en else ""
                sinner_blocks.append(SectionBlock(
                    heading=f"## [{rank_str}] {title_en} — {en_char}{head_kr}",
                    context_lines=ctx,
                    items=id_items,
                ))

        # Also claim any remaining skills in Skills_personality-{cid:02d}.json or voice files for this Sinner
        sp_file = f"Skills_personality-{cid:02d}.json"
        if sp_file in corpus.logical_files:
            extra_skill_items: list[PendingItem] = []
            for rk, _, _ in corpus.rows_by_key(sp_file)[0]:
                extra_skill_items.extend(make_skill_items(corpus, sp_file, rk, f"Umiejętność [{rk}]"))
            if extra_skill_items:
                sinner_blocks.append(SectionBlock(
                    heading=f"## Dodatkowe umiejętności Tożsamości — {en_char} ({sp_file[:-5]})",
                    context_lines=[f"- plik gry: `{sp_file}` (warianty / przemiany umiejętności tego Grzesznika)"],
                    items=extra_skill_items,
                ))

        # AbDlg_<Sinner>.json
        for ab_slug, ab_cid in ABDLG_SINNER.items():
            if ab_cid == cid:
                ab_file = f"AbDlg_{ab_slug}.json"
                if ab_file in corpus.logical_files:
                    sinner_blocks.extend(append_generic_file_sections(
                        corpus, [ab_file], f"Kwestie testów Anomalii — {en_char}"
                    ))

        if sinner_blocks:
            domains.append((
                f"02_tozsamosc_{cid:02d}_{slug_name}",
                f"Grzesznik #{cid:02d}: {en_char} — Tożsamości, umiejętności, pasywki i głos",
                f"Kompletny zestaw kart Tożsamości postaci **{en_char}** ({kr_char}) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.",
                sinner_blocks,
            ))

    # Remaining player Identity / skill / passive / voice tables not tied to a single 1..12 Sinner
    rem_blocks: list[SectionBlock] = []
    for pf, pid, rs, rr in identities_by_cid.get(0, []):
        rem_items = [
            PendingItem(
                label=human_addr_label(addr, f"Tożsamość [{pid}]"),
                logical_file=pf,
                addrs=[addr],
                field=field_name(addr),
                src_raw=vs,
                ref_raw=vr,
            )
            for addr, vs, vr in corpus.claim_prefix(pf, f"dataList[id={pid}]")
        ]
        if rem_items:
            rem_blocks.append(SectionBlock(
                heading=f"## Tożsamość specjalna [{pid}] ({pf[:-5]})",
                context_lines=[f"- plik gry: `{pf}`"],
                items=rem_items,
            ))
    misc_pers = [
        f for f in corpus.logical_files
        if f in {"IntroduceCharacter.json", "Characters.json"}
        or (f.startswith("Personality") and not f.startswith("PersonalityVoiceDlg/"))
        or f in pers_files
        or f in skill_pers_files
        or f in passive_player_files
        or f in voice_files
        or f.startswith("AbDlg")
    ]
    for f in misc_pers:
        if f.startswith("Skills"):
            s_items: list[PendingItem] = []
            for rk, _, _ in corpus.rows_by_key(f)[0]:
                s_items.extend(make_skill_items(corpus, f, rk, f"Umiejętność [{rk}]"))
            if s_items:
                rem_blocks.append(SectionBlock(
                    heading=f"## Pozostałe umiejętności graczy — {f[:-5]}",
                    context_lines=[f"- plik gry: `{f}`"],
                    items=s_items,
                ))
        else:
            rem_blocks.extend(append_generic_file_sections(corpus, [f], "Tożsamości i pasywki (wspólne / dodatkowe)"))
    if rem_blocks:
        domains.append((
            "02_tozsamosc_13_wspolne_i_dodatkowe",
            "Tożsamości, umiejętności i pasywki — wpisy wspólne oraz wydarzeniowe",
            "Pozostałe karty, umiejętności przemian, pasywki oraz kwestie głosowe nieprzypisane bezpośrednio do pojedynczej karty w StaticData.",
            rem_blocks,
        ))
    return domains


def build_ego_and_gifts(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """03 — Character E.G.O (cards + Awakening/Corrosion skills + passives + voices) and E.G.O Gifts."""
    chars_en = corpus.ref_texts.by_id("Characters")
    chars_kr = corpus.src_texts.by_id("Characters")
    ego_ui_files = [
        f for f in corpus.logical_files
        if (f.startswith("EGO") and not f.startswith("EGOgift") and not f.startswith("EGOVoiceDig/"))
    ]
    ego_card_files = [f for f in corpus.logical_files if f.startswith("Egos")]
    ego_skill_files = [f for f in corpus.logical_files if f.startswith("Skills_Ego")]
    ego_passive_files = [f for f in corpus.logical_files if f.startswith("Passive_Ego")]
    ego_voice_files = [f for f in corpus.logical_files if f.startswith("EGOVoiceDig/")]

    ego_blocks: list[SectionBlock] = []
    if ego_ui_files:
        ego_blocks.extend(append_generic_file_sections(corpus, ego_ui_files, "Interfejs i warunki E.G.O"))

    # Index E.G.O cards, skills, passives, and voices by base 5-digit ego_id (2XXYY)
    cards_by_ego: dict[int, list[tuple[str, object, dict, dict]]] = collections.defaultdict(list)
    for f in ego_card_files:
        for rk, rs, rr in corpus.rows_by_key(f)[0]:
            if isinstance(rk, int):
                base_id = rk // 10 if rk >= 200000 else rk
                cards_by_ego[base_id].append((f, rk, rs, rr))

    skills_by_ego: dict[int, list[tuple[str, int]]] = collections.defaultdict(list)
    for f in ego_skill_files:
        for rk, _, _ in corpus.rows_by_key(f)[0]:
            if isinstance(rk, int) and rk >= 2000000:
                skills_by_ego[rk // 100].append((f, rk))

    passives_by_ego: dict[int, list[tuple[str, int]]] = collections.defaultdict(list)
    for f in ego_passive_files:
        for rk, _, _ in corpus.rows_by_key(f)[0]:
            if isinstance(rk, int) and rk >= 2000000:
                passives_by_ego[rk // 100].append((f, rk))

    voices_by_ego: dict[int, list[tuple[str, int, object, dict, dict]]] = collections.defaultdict(list)
    for vf in ego_voice_files:
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(vf)[0]):
            m = re.search(r"_(2\d{4})_", str(rk))
            if m:
                voices_by_ego[int(m[1])].append((vf, idx, rk, rs, rr))

    all_ego_ids = sorted(set(cards_by_ego) | set(skills_by_ego) | set(passives_by_ego) | set(voices_by_ego))
    by_sinner: dict[int, list[int]] = collections.defaultdict(list)
    for eid in all_ego_ids:
        cid = (eid // 100) % 100 if 20100 <= eid <= 21299 else 0
        by_sinner[cid if 1 <= cid <= 12 else 0].append(eid)

    for cid in sorted(k for k in by_sinner if k > 0) + ([0] if 0 in by_sinner else []):
        en_char = one_line(chars_en.get(str(cid), {}).get("name", "")) if cid else "Pozostałe / wspólne"
        kr_char = one_line(chars_kr.get(str(cid), {}).get("name", "")) if cid else ""
        for eid in by_sinner[cid]:
            items: list[PendingItem] = []
            ego_name_en = str(eid)
            ego_name_kr = ""
            for cf, crk, crs, crr in cards_by_ego.get(eid, []):
                ego_name_en = one_line(crr.get("name", "")) or one_line(crs.get("name", "")) or ego_name_en
                ego_name_kr = one_line(crs.get("name", "")) or ego_name_kr
                for addr, vs, vr in corpus.claim_prefix(cf, f"dataList[id={crk}]"):
                    items.append(PendingItem(
                        label=human_addr_label(addr, "Karta E.G.O"),
                        logical_file=cf,
                        addrs=[addr],
                        field=field_name(addr),
                        src_raw=vs,
                        ref_raw=vr,
                    ))
            for sf, srk in skills_by_ego.get(eid, []):
                mode = "Przebudzenie (Awakening)" if (srk % 100) // 10 == 1 else "Korozja (Corrosion)" if (srk % 100) // 10 == 2 else f"Umiejętność {srk}"
                items.extend(make_skill_items(corpus, sf, srk, f"E.G.O — {mode}"))
            for pf, prk in passives_by_ego.get(eid, []):
                for addr, vs, vr in corpus.claim_prefix(pf, f"dataList[id={prk}]"):
                    items.append(PendingItem(
                        label=human_addr_label(addr, "Pasywka E.G.O"),
                        logical_file=pf,
                        addrs=[addr],
                        field=field_name(addr),
                        src_raw=vs,
                        ref_raw=vr,
                    ))
            for vf, vidx, vrk, vrs, vrr in voices_by_ego.get(eid, []):
                vpref = corpus.row_prefix(vf, vidx, vrs or vrr)
                cue = one_line(vrr.get("desc", "")) or one_line(vrs.get("desc", ""))
                for addr, vs, vr in corpus.claim_prefix(vf, vpref):
                    fn = field_name(addr)
                    lbl = f"Głos E.G.O [{vrk}] — sytuacja" if fn == "desc" else f"Głos E.G.O [{vrk}] ({cue or 'kwestia'})"
                    items.append(PendingItem(
                        label=lbl,
                        logical_file=vf,
                        addrs=[addr],
                        field=fn,
                        src_raw=vs,
                        ref_raw=vr,
                    ))
            if items:
                ego_blocks.append(SectionBlock(
                    heading=f"## E.G.O [{eid}] {ego_name_en}" + (f" ({ego_name_kr})" if ego_name_kr else "") + f" — {en_char}",
                    context_lines=[
                        f"- postać: {en_char}" + (f" ({kr_char})" if kr_char else "") + f" · ID E.G.O: `{eid}`",
                    ],
                    items=items,
                ))

    # Any remaining E.G.O skills, passives, or voice lines (e.g. Common_998, Enemy_999, special IDs)
    for f in ego_skill_files:
        rem_s: list[PendingItem] = []
        for rk, _, _ in corpus.rows_by_key(f)[0]:
            rem_s.extend(make_skill_items(corpus, f, rk, f"Umiejętność E.G.O [{rk}]"))
        if rem_s:
            ego_blocks.append(SectionBlock(
                heading=f"## Dodatkowe umiejętności E.G.O — {f[:-5]}",
                context_lines=[f"- plik gry: `{f}`"],
                items=rem_s,
            ))
    ego_blocks.extend(append_generic_file_sections(
        corpus, ego_card_files + ego_passive_files + ego_voice_files, "E.G.O (dodatkowe)"
    ))

    # E.G.O Gifts
    gift_files = [
        f for f in corpus.logical_files
        if f in {"EgoGiftCategory.json", "MirrorDungeonEgoGiftLockedDesc.json"} or f.startswith("EGOgift")
    ]
    gift_blocks = append_generic_file_sections(corpus, gift_files, "Dar E.G.O")

    out: list[tuple[str, str, str, list[SectionBlock]]] = []
    if ego_blocks:
        out.append((
            "03_ego_postaci",
            "E.G.O Grzeszników — karty, Przebudzenie, Korozja, pasywki i kwestie",
            "Każde E.G.O zgrupowane razem: nazwa i opis ekwipunku, umiejętność Przebudzenia (Awakening), umiejętność Korozji (Corrosion), pasywka oraz kwestie głosowe.",
            ego_blocks,
        ))
    if gift_blocks:
        out.append((
            "03_dary_ego",
            "Dary E.G.O (E.G.O Gifts) — Lochy Fabularne i Lochy Lustra",
            "Nazwy, pełne opisy i skrócone opisy wszystkich Darów E.G.O oraz kategorii i warunków ich odblokowania.",
            gift_blocks,
        ))
    return out


def _extract_mode_suffix(filename: str) -> str:
    stem = PurePosixPath(filename).stem
    m = re.search(r"[-_](a1c\d+p?\d*|Refraction\w*|Mirror\w*|mr\d+\w*|walpu\d+|BossRaid|tkt(?:-re)?|mowe(?:-re)?|ycgd|twth|cultivation|pilgrimage|exme|fools|sweep|hidden|x1p1c1|night-clean-up-re|\d+-\d+(?:-hard)?)$", stem, re.I)
    return m[1].lower() if m else "podstawowe"


def build_abnormalities_events_and_enemies(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """04 — Abnormality guides, AbEvents + ResultLogs, ActionEvents, Assists, Enemies + enemy skills/passives."""
    out: list[tuple[str, str, str, list[SectionBlock]]] = []

    # 4a. AbnormalityGuides
    guide_files = [f for f in corpus.logical_files if f.startswith("AbnormalityGuides")]
    guide_blocks: list[SectionBlock] = []
    for f in guide_files:
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(f)[0]):
            rpref = corpus.row_prefix(f, idx, rs or rr)
            claimed = corpus.claim_prefix(f, rpref)
            if not claimed:
                continue
            code = rs.get("codeName") or rr.get("codeName") or "—"
            name_en = one_line(rr.get("name", "")) or one_line(rs.get("name", "")) or str(rk)
            name_kr = one_line(rs.get("name", ""))
            items = [
                PendingItem(
                    label=human_addr_label(addr, f"Przewodnik Anomalii [{rk}]"),
                    logical_file=f,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                )
                for addr, vs, vr in claimed
            ]
            guide_blocks.append(SectionBlock(
                heading=f"## Anomalia {code}: {name_en}" + (f" ({name_kr})" if name_kr and name_kr != name_en else ""),
                context_lines=[f"- kod klasyfikacji: `{code}` · ID wpisu: `{rk}` · plik: `{f}`"],
                items=items,
            ))
    if guide_blocks:
        out.append((
            "04_anomalie_przewodnik",
            "Przewodnik po Anomaliach i dziennik obserwacji (AbnormalityGuides)",
            "Wpisy encyklopedyczne Anomalii i części bossów: nazwa, wskazówka bojowa oraz kolejne poziomy obserwacji.",
            guide_blocks,
        ))

    # 4b. ChoiceEvent* + AbEvents* + AbEventsResultLog*
    choice_meta = [f for f in corpus.logical_files if f.startswith("ChoiceEvent")]
    ab_event_files = [f for f in corpus.logical_files if f.startswith("AbEvents") and not f.startswith("AbEventsResultLog")]
    ab_log_files = [f for f in corpus.logical_files if f.startswith("AbEventsResultLog")]

    # Index AbEventsResultLog rows by leading numeric event id prefix (e.g. "810001_...")
    logs_by_ev: dict[str, list[tuple[str, int, object, dict, dict]]] = collections.defaultdict(list)
    for lf in ab_log_files:
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(lf)[0]):
            m = re.match(r"^(\d+)_", str(rk))
            if m:
                logs_by_ev[m[1]].append((lf, idx, rk, rs, rr))

    ab_blocks = append_generic_file_sections(corpus, choice_meta, "Mechanika wydarzeń wyboru")
    for ef in ab_event_files:
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(ef)[0]):
            rpref = corpus.row_prefix(ef, idx, rs or rr)
            claimed = corpus.claim_prefix(ef, rpref)
            items = [
                PendingItem(
                    label=human_addr_label(addr, f"Wydarzenie Anomalii [{rk}]"),
                    logical_file=ef,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                )
                for addr, vs, vr in claimed
            ]
            for lf, lidx, lrk, lrs, lrr in logs_by_ev.get(str(rk), []):
                lpref = corpus.row_prefix(lf, lidx, lrs or lrr)
                for addr, vs, vr in corpus.claim_prefix(lf, lpref):
                    items.append(PendingItem(
                        label=human_addr_label(addr, f"Dziennik wyniku [{lrk}]"),
                        logical_file=lf,
                        addrs=[addr],
                        field=field_name(addr),
                        src_raw=vs,
                        ref_raw=vr,
                    ))
            if items:
                title_en = one_line(rr.get("title", "")) or one_line(rs.get("title", "")) or str(rk)
                ab_blocks.append(SectionBlock(
                    heading=f"## Spotkanie z Anomalią [{rk}]: {title_en} ({ef[:-5]})",
                    context_lines=[f"- plik wydarzenia: `{ef}` (wraz z komunikatami wyniku `AbEventsResultLog`)"],
                    items=items,
                ))
    ab_blocks.extend(append_generic_file_sections(corpus, ab_log_files, "Pozostałe komunikaty wyników (AbEventsResultLog)"))
    if ab_blocks:
        out.append((
            "04_wydarzenia_anomalii",
            "Wydarzenia spotkań z Anomaliami i komunikaty wyników (AbEvents)",
            "Opisy spotkań z Anomaliami w lochach, pytania testowe, opisy sukcesu i porażki oraz komunikaty efektów.",
            ab_blocks,
        ))

    # 4c. ActionEvents*
    act_files = [f for f in corpus.logical_files if f.startswith("ActionEvents")]
    act_blocks: list[SectionBlock] = []
    for af in act_files:
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(af)[0]):
            rpref = corpus.row_prefix(af, idx, rs or rr)
            claimed = corpus.claim_prefix(af, rpref)
            if not claimed:
                continue
            name_en = one_line(rr.get("name", "")) or one_line(rs.get("name", "")) or str(rk)
            items = [
                PendingItem(
                    label=human_addr_label(addr, f"Wydarzenie [{rk}]"),
                    logical_file=af,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                )
                for addr, vs, vr in claimed
            ]
            act_blocks.append(SectionBlock(
                heading=f"## Wydarzenie interaktywne [{rk}]: {name_en} ({af[:-5]})",
                context_lines=[f"- plik gry: `{af}` — opis sceny oraz opcje wyboru gracza wraz z ich rezultatami"],
                items=items,
            ))
    if act_blocks:
        out.append((
            "04_wydarzenia_interaktywne",
            "Wydarzenia interaktywne i wybory w lochach (ActionEvents)",
            "Sceny wyboru w Lochach Fabularnych i Lochach Lustra: opis sytuacji, opcje gracza, podpowiedzi skutków i rezultaty.",
            act_blocks,
        ))

    # 4d. Assists (NPC allies)
    assist_files = [
        f for f in corpus.logical_files
        if f.startswith("Assist") or f.startswith("Skills_Assist") or f.startswith("Passives_Assist")
    ]
    assist_blocks: list[SectionBlock] = []
    for f in assist_files:
        if f.startswith("Skills_Assist"):
            s_items: list[PendingItem] = []
            for rk, _, _ in corpus.rows_by_key(f)[0]:
                s_items.extend(make_skill_items(corpus, f, rk, f"Umiejętność sojusznika [{rk}]"))
            if s_items:
                assist_blocks.append(SectionBlock(
                    heading=f"## Umiejętności jednostek wsparcia — {f[:-5]}",
                    context_lines=[f"- plik gry: `{f}`"],
                    items=s_items,
                ))
        else:
            assist_blocks.extend(append_generic_file_sections(corpus, [f], "Jednostka wsparcia"))
    if assist_blocks:
        out.append((
            "04_jednostki_wsparcia",
            "Sojusznicze jednostki wsparcia w bitwach (Assist)",
            "Postacie niezależne walczące po stronie gracza wraz z ich umiejętnościami i pasywkami.",
            assist_blocks,
        ))

    # 4e. Enemies + BattleSpeechBubbleDlg + Enemy/Abnormality Skills & Passives grouped by chapter/mode suffix
    combat_enemy_files = [
        f for f in corpus.logical_files
        if f.startswith("Enemies")
        or f.startswith("BattleSpeechBubbleDlg")
        or f.startswith("Skills_Abnormality")
        or f.startswith("Skills_Enemy")
        or f in {"Skills_Tutorial.json", "Skills_fools.json"}
        or f.startswith("Passives_Abnormality")
        or f.startswith("Passives_Enemy")
        or f in {"Passives_check4.json", "Passives_fools.json"}
    ]
    by_mode: dict[str, list[str]] = collections.defaultdict(list)
    for f in combat_enemy_files:
        by_mode[_extract_mode_suffix(f)].append(f)

    enemy_blocks: list[SectionBlock] = []
    for mode_key in sorted(by_mode):
        # Order within each chapter/mode: Enemies -> SpeechBubbles -> Skills -> Passives
        ordered_files = sorted(
            by_mode[mode_key],
            key=lambda x: (
                0 if x.startswith("Enemies") else
                1 if x.startswith("BattleSpeechBubbleDlg") else
                2 if x.startswith("Skills") else 3,
                x,
            ),
        )
        for f in ordered_files:
            if f.startswith("Skills"):
                s_items = []
                for rk, _, _ in corpus.rows_by_key(f)[0]:
                    s_items.extend(make_skill_items(corpus, f, rk, f"Umiejętność wroga [{rk}]"))
                if s_items:
                    enemy_blocks.append(SectionBlock(
                        heading=f"## [{mode_key}] Umiejętności wrogów / Anomalii — {f[:-5]}",
                        context_lines=[f"- grupa rozdziału/trybu: `{mode_key}` · plik: `{f}`"],
                        items=s_items,
                    ))
            elif f.startswith("BattleSpeechBubbleDlg"):
                enemy_blocks.extend(append_generic_file_sections(corpus, [f], f"[{mode_key}] Dymek bojowy"))
            elif f.startswith("Enemies"):
                enemy_blocks.extend(append_generic_file_sections(corpus, [f], f"[{mode_key}] Wróg / część"))
            else:
                enemy_blocks.extend(append_generic_file_sections(corpus, [f], f"[{mode_key}] Pasywka wroga"))
    if enemy_blocks:
        out.append((
            "04_wrogowie_dymki_i_umiejetnosci",
            "Wrogowie, dymki bojowe oraz umiejętności i pasywki przeciwników",
            "Zgrupowane według rozdziału / Kolei Refrakcji / Walpurgisnacht: nazwy przeciwników i ich części, kwestie w dymkach podczas walki, umiejętności oraz pasywki.",
            enemy_blocks,
        ))
    return out


def build_announcers_and_music(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """05 — Battle announcers + voice lines, and Lobby BGM + song lyrics."""
    out: list[tuple[str, str, str, list[SectionBlock]]] = []

    ann_meta = [f for f in ("AnnouncerTicketUIPopup.json", "AnnouncerVoiceType.json") if f in corpus.logical_files]
    ann_name_files = [
        f for f in corpus.logical_files
        if f.startswith("Announcer") and f not in {"AnnouncerTicketUIPopup.json", "AnnouncerVoiceType.json"}
    ]
    ann_dlg_files = [f for f in corpus.logical_files if f.startswith("BattleAnnouncerDlg/")]

    ann_blocks = append_generic_file_sections(corpus, ann_meta, "System komentatorów")

    dlg_by_id: dict[str, list[str]] = collections.defaultdict(list)
    for df in ann_dlg_files:
        m = re.search(r"_(\d+)\.json$", df)
        if m:
            dlg_by_id[m[1]].append(df)

    # Pair Announcer rows with their BattleAnnouncerDlg files
    ann_names_en: dict[str, str] = {}
    ann_names_kr: dict[str, str] = {}
    name_items_by_id: dict[str, list[PendingItem]] = collections.defaultdict(list)
    for af in ann_name_files:
        for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(af)[0]):
            aid = str(rk)
            if one_line(rr.get("name", "")):
                ann_names_en[aid] = one_line(rr["name"])
            if one_line(rs.get("name", "")):
                ann_names_kr[aid] = one_line(rs["name"])
            rpref = corpus.row_prefix(af, idx, rs or rr)
            for addr, vs, vr in corpus.claim_prefix(af, rpref):
                name_items_by_id[aid].append(PendingItem(
                    label=human_addr_label(addr, f"Komentator [{aid}]"),
                    logical_file=af,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                ))

    all_ann_ids = sorted(set(name_items_by_id) | set(dlg_by_id), key=lambda x: (int(x) if x.isdigit() else 999999, x))
    for aid in all_ann_ids:
        items = list(name_items_by_id.get(aid, []))
        a_en = ann_names_en.get(aid, f"ID {aid}")
        a_kr = ann_names_kr.get(aid, "")
        for df in dlg_by_id.get(aid, []):
            for idx, (rk, rs, rr) in enumerate(corpus.rows_by_key(df)[0]):
                rpref = corpus.row_prefix(df, idx, rs or rr)
                for addr, vs, vr in corpus.claim_prefix(df, rpref):
                    items.append(PendingItem(
                        label=f"Kwestia komentatora ({a_en}) [{rk}]",
                        logical_file=df,
                        addrs=[addr],
                        field=field_name(addr),
                        src_raw=vs,
                        ref_raw=vr,
                    ))
        if items:
            ann_blocks.append(SectionBlock(
                heading=f"## Komentator bitwy [{aid}]: {a_en}" + (f" ({a_kr})" if a_kr and a_kr != a_en else ""),
                context_lines=[f"- ID komentatora: `{aid}`" + (f" · pliki kwestii: {', '.join(dlg_by_id.get(aid, []))}" if dlg_by_id.get(aid) else "")],
                items=items,
            ))
    ann_blocks.extend(append_generic_file_sections(corpus, ann_dlg_files, "Komentator (dodatkowe)"))
    if ann_blocks:
        out.append((
            "05_komentatorzy_bitwy",
            "Komentatorzy bitwy (Battle Announcers) — nazwy i kwestie głosowe",
            "Typy komunikatów oraz pełne zestawy wypowiedzi poszczególnych komentatorów bitwy.",
            ann_blocks,
        ))

    # Music & Lyrics
    music_files = [
        f for f in corpus.logical_files
        if f == "LobbyBGMUI.json" or f.startswith("LobbyBGM") or f.startswith("BgmLyrics/")
    ]
    music_blocks = append_generic_file_sections(corpus, music_files, "Muzyka i tekst utworu")
    if music_blocks:
        out.append((
            "05_muzyka_i_piosenki",
            "Muzyka w lobby oraz napisy do utworów wokalnych (BgmLyrics)",
            "Tytuły ścieżek dźwiękowych oraz zsynchronizowane wers po wersie napisy do piosenek bossów i napisów końcowych (uwaga: w BgmLyrics zachowaj łaciński styl `<style=\"DEN_…\">` z wersji EN).",
            music_blocks,
        ))
    return out


def build_rpg_canto10(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """06 — Canto X RPG exploration mode grouped by floor."""
    rpg_files = [
        f for f in corpus.logical_files
        if f.startswith("RPGSystem/") or f == "RPGSuicideBoxUI.json"
    ]
    if not rpg_files:
        return []

    def floor_group(fname: str) -> str:
        m = re.search(r"(floor-b?\d+|common|theater)", fname)
        return m[1] if m else "inne"

    by_floor: dict[str, list[str]] = collections.defaultdict(list)
    for f in rpg_files:
        by_floor[floor_group(f)].append(f)

    blocks: list[SectionBlock] = []
    for fl in sorted(by_floor):
        for f in sorted(by_floor[fl]):
            if not f.startswith("RPGSystem/"):
                blocks.extend(append_generic_file_sections(corpus, [f], "Interfejs RPG"))
                continue
            paired_rows, _ = corpus.rows_by_key(f, key_field="key")
            items: list[PendingItem] = []
            for idx, (rk, rs, rr) in enumerate(paired_rows):
                row_sample = rs or rr
                rpref = corpus.row_prefix(f, idx, row_sample, key_field="key")
                # Build per-subindex speaker lookup for RPG dialogue files
                speakers_s = {
                    t.get("index", i): one_line(t.get("speaker", ""))
                    for i, t in enumerate(rs.get("texts", []) or []) if isinstance(t, dict)
                }
                speakers_r = {
                    t.get("index", i): one_line(t.get("speaker", ""))
                    for i, t in enumerate(rr.get("texts", []) or []) if isinstance(t, dict)
                }
                for addr, vs, vr in corpus.claim_prefix(f, rpref):
                    fn = field_name(addr)
                    if fn == "speaker":
                        corpus.glossary.record("rpg_speaker", vs, vr, f, addr)
                        continue
                    tm = re.search(r"texts\[#(\d+)\]", addr)
                    sp_label = ""
                    if tm:
                        t_idx = int(tm[1])
                        # Match by list position
                        ts_list = rs.get("texts", []) if isinstance(rs, dict) else []
                        tr_list = rr.get("texts", []) if isinstance(rr, dict) else []
                        sp_s = one_line(ts_list[t_idx].get("speaker", "")) if t_idx < len(ts_list) and isinstance(ts_list[t_idx], dict) else speakers_s.get(t_idx, "")
                        sp_r = one_line(tr_list[t_idx].get("speaker", "")) if t_idx < len(tr_list) and isinstance(tr_list[t_idx], dict) else speakers_r.get(t_idx, "")
                        if sp_s or sp_r:
                            sp_label = f"Dialog RPG [{rk}] — {sp_s or sp_r}" + (
                                f" ({sp_r})" if sp_s and sp_r and sp_s != sp_r else ""
                            )
                    label = sp_label if sp_label and fn == "text" else human_addr_label(addr, f"RPG [{rk}]")
                    items.append(PendingItem(
                        label=label,
                        logical_file=f,
                        addrs=[addr],
                        field=fn,
                        src_raw=vs,
                        ref_raw=vr,
                    ))
            for addr, vs, vr in corpus.claim_file(f):
                items.append(PendingItem(
                    label=human_addr_label(addr, f"RPG ({f})"),
                    logical_file=f,
                    addrs=[addr],
                    field=field_name(addr),
                    src_raw=vs,
                    ref_raw=vr,
                ))
            if items:
                blocks.append(SectionBlock(
                    heading=f"## Tryb RPG [{fl}] — {PurePosixPath(f).stem}",
                    context_lines=[f"- obszar/warstwa: `{fl}` · plik gry: `{f}` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)"],
                    items=items,
                ))
    return [(
        "06_tryb_rpg_canto10",
        "Tryb eksploracji RPG (Canto X) — zadania, przedmioty, postacie, narracja i dialogi",
        "Wszystkie teksty trybu RPG z Canto X pogrupowane po piętrach (`common`, `theater`, `floor-1`…`floor-6`, `floor-b1`…`floor-b3`). Mówcy są pokazani w etykietach kwestii i tłumaczeni raz w `mowcy-rpg-i-anomalii.md`.",
        blocks,
    )]


def build_theater_stages_and_dungeons(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """07 — Dante's Notes + Story Theater, Chapters/Stages/DanteAbility, Mirror & Railway Dungeons."""
    out: list[tuple[str, str, str, list[SectionBlock]]] = []

    # 7a. Dante's Notes (pair keyword list + detail entries) & Story Theater
    note_files = [f for f in corpus.logical_files if f.startswith("StoryTheaterDanteNote") and not f.startswith("StoryTheaterDanteNoteDetail")]
    detail_files = [f for f in corpus.logical_files if f.startswith("StoryTheaterDanteNoteDetail")]
    theater_other = [
        f for f in corpus.logical_files
        if (f.startswith("StoryTheater") and f not in note_files and f not in detail_files)
        or f in {"StoryUIText.json", "StoryVoiceSettingUI.json", "Story.json"}
        or f.startswith("Story-")
    ]
    t_blocks = append_generic_file_sections(corpus, note_files, "Notatki Dantego — hasło")
    t_blocks.extend(append_generic_file_sections(corpus, detail_files, "Notatki Dantego — treść wpisu"))
    t_blocks.extend(append_generic_file_sections(corpus, theater_other, "Teatr Opowieści"))
    if t_blocks:
        out.append((
            "07_notatki_dantego_i_teatr",
            "Notatki Dantego (encyklopedia świata) oraz Teatr Opowieści",
            "Hasła i pełne wpisy encyklopedyczne Dantego o świecie Miasta, Korporacjach i Grzesznikach oraz opisy rozdziałów i opowiadań w Teatrze Opowieści.",
            t_blocks,
        ))

    # 7b. Chapters, StageNodes, DungeonNodes, DanteAbility, Ch8 text effects
    stage_files = [
        f for f in corpus.logical_files
        if f == "StagePartText.json"
        or f.startswith("StageChapterText")
        or f.startswith("StageNode")
        or f in {"StageContinueText.json", "StageStatisticUIText.json"}
        or f.startswith("DungeonName")
        or f.startswith("DungeonArea")
        or f.startswith("DungeonNode")
        or f.startswith("DanteAbility")
        or f.startswith("Ch")
    ]
    stage_blocks = append_generic_file_sections(corpus, stage_files, "Rozdziały, etapy i zdolności Dantego")
    if stage_blocks:
        out.append((
            "07_rozdzialy_etapy_i_zdolnosci_dantego",
            "Rozdziały, węzły etapów, lochy fabularne, zdolności Dantego i efekty tekstowe",
            "Tytuły części i rozdziałów, nazwy i opisy wszystkich węzłów na mapie etapów, lochów fabularnych, zdolności Złotej Gałęzi (Durante) oraz napisy specjalne w walkach fabularnych.",
            stage_blocks,
        ))

    # 7c. Mirror Dungeon, Refraction Railway, Thread/EXP Dungeon, Boss Raid
    dungeon_files = [
        f for f in corpus.logical_files
        if f.startswith("MirrorDungeon")
        or f.startswith("DungeonStartBuffs")
        or f in {"ThreadDungeon.json", "RewardDungeonUI.json", "HellsChickenDungeonNode.json"}
        or f.startswith("StoryDungeonUI")
        or f.startswith("RailwayDungeon")
        or f.startswith("BossRaidUI")
    ]
    d_blocks = append_generic_file_sections(corpus, dungeon_files, "Tryby lochów i Kolei Refrakcji")
    if d_blocks:
        out.append((
            "07_loch_lustra_kolej_i_rajdy",
            "Loch Lustra (Mirror Dungeon), Kolej Refrakcji (Refraction Railway) i pozostałe tryby",
            "Motywy pięter, wzmocnienia startowe, stacje Kolei Refrakcji, interfejs Lochu Lustra, Ekstrakcji Nici i ekspedycji.",
            d_blocks,
        ))
    return out


def build_ui_tutorials_events_and_shop(corpus: Corpus) -> list[tuple[str, str, str, list[SectionBlock]]]:
    """08 — Main UI/settings, tutorials/hints, seasonal events/pass, items/shop/banners/tickets."""
    out: list[tuple[str, str, str, list[SectionBlock]]] = []

    ui_files = [
        f for f in corpus.logical_files
        if f.startswith("MainUIText")
        or f == "BattleUIText.json"
        or f.startswith("UI")
        or f.startswith("Formation")
        or f in {
            "LoginUIText.json",
            "kr_settings-ui-donttranslate.json",
            "Filter.json",
            "UpgradeCharacterUI.json",
            "SkinUI.json",
            "SelectLoadingCgUi.json",
            "SelectDUI.json",
            "TooltipUIText.json",
            "ShotcutKeyManual.json",
            "FileDownloadDesc.json",
            "IntegrateAccountUI.json",
            "ErrorCodeMsg.json",
            "UserAgreements.json",
            "ReturnPolicy.json",
            "FAQ.json",
            "AssociationName.json",
        }
        or f.startswith("Limbus")
    ]
    ui_blocks = append_generic_file_sections(corpus, ui_files, "Interfejs i ustawienia")
    if ui_blocks:
        out.append((
            "08_interfejs_glowny_i_ustawienia",
            "Interfejs główny, bitwa, formacja, ustawienia, komunikaty i skróty",
            "Przyciski, okna dialogowe, menu ustawień, filtry formacji, komunikaty błędów, regulaminy i FAQ.",
            ui_blocks,
        ))

    tut_files = [
        f for f in corpus.logical_files
        if f.startswith("Tutorial")
        or f.startswith("BattleHint")
        or f.startswith("BattleResultHint")
        or f == "SuccessRate.json"
    ]
    tut_blocks = append_generic_file_sections(corpus, tut_files, "Samouczek i wskazówki")
    if tut_blocks:
        out.append((
            "08_samouczki_i_wskazowki",
            "Samouczki (Tutorials), wskazówki na ekranie ładowania i podpowiedzi po porażce",
            "Instrukcje mechanik walki i Lochu Lustra oraz wskazówki taktyczne wyświetlane graczowi.",
            tut_blocks,
        ))

    ev_files = [
        f for f in corpus.logical_files
        if f.startswith("SeasonTitle")
        or f.startswith("BattlePass")
        or f.startswith("Walpu")
        or f.startswith("Event")
        or f.startswith("Fools")
        or f in {
            "DawnOfGreenEventText.json",
            "HellsChicken.json",
            "CultivationEvent.json",
            "NightCleanUpEvent.json",
            "RecordMemoryEvent.json",
            "TwiningThreadsEvent.json",
            "PilgrimageUIText.json",
        }
        or f.startswith("ProjectGS")
        or f.startswith("DailyLoginEvent")
        or f.startswith("Attendance")
        or f.startswith("Limtochess")
        or f.startswith("SchemaCraft")
    ]
    ev_blocks = append_generic_file_sections(corpus, ev_files, "Wydarzenia i Przepustka")
    if ev_blocks:
        out.append((
            "08_wydarzenia_sezonowe_i_przepustka",
            "Sezony, Przepustka Limbus (Battle Pass), Noc Walpurgii i wydarzenia specjalne",
            "Teksty wydarzeń sezonowych, misji Nocy Walpurgii, wydarzeń Intervallo, trybów specjalnych oraz nagród logowania.",
            ev_blocks,
        ))

    shop_files = [
        f for f in corpus.logical_files
        if f.startswith("Items")
        or f.startswith("Shop")
        or f.startswith("IAP")
        or f == "CouponUIText.json"
        or f.startswith("Gacha")
        or f in {"MissionUIText.json", "Quest.json", "IntroductionPreset.json"}
        or f.startswith("reward")
        or f.startswith("UserInfo")
        or f.startswith("UnlockCode")
        or f.startswith("UserBanner")
        or f.startswith("UserTicket")
    ]
    shop_blocks = append_generic_file_sections(corpus, shop_files, "Przedmioty, sklep i profil gracza")
    if shop_blocks:
        out.append((
            "08_przedmioty_sklep_i_profil",
            "Przedmioty, sklep, Ekstrakcja (Gacha), warunki odblokowania, sztandary i wizytówki",
            "Opisy przedmiotów i walut, sklep i pakiety, banery Ekstrakcji, szablony wizytówki gracza, sztandary oraz bilety ozdobne.",
            shop_blocks,
        ))
    return out


def _filter_blocks_by_addrs(
    blocks: list[SectionBlock],
    include_addrs: set[tuple[str, str]],
) -> list[SectionBlock]:
    filtered: list[SectionBlock] = []
    for b in blocks:
        kept = [it for it in b.items if any((it.logical_file, a) in include_addrs for a in it.addrs)]
        if kept:
            filtered.append(SectionBlock(heading=b.heading, context_lines=list(b.context_lines), items=kept))
    return filtered


def render_view_glossary(
    corpus: Corpus,
    mc_blocks: list[SectionBlock],
    include_addrs: set[tuple[str, str]] | None = None,
) -> tuple[str, int, int]:
    """Render ``mowcy-rpg-i-anomalii.md`` + ``ScenarioModelCodes-AutoCreated.json``."""
    lines = [
        "# Mówcy trybu RPG, testów Anomalii oraz tabela modeli — Limbus Company",
        "",
        "Te napisy występują wielokrotnie jako etykiety mówców w trybie RPG (Canto X), w testach Anomalii (`AbDlg`) "
        "oraz w globalnej tabeli modeli postaci (`ScenarioModelCodes-AutoCreated.json`). Tłumaczysz je **raz tutaj**.",
        "",
    ]
    seen: dict[tuple[str, str], int] = {}
    seq = 1
    elements = 0
    todo = 0

    for kind, label in ViewGlossary.KINDS:
        entries = sorted(
            (
                (src, ref, meta)
                for (k, src, ref), meta in corpus.glossary.entries.items()
                if k == kind and (include_addrs is None or bool(meta.get("sources", set()) & include_addrs))
            ),
            key=lambda e: (-e[2]["count"], e[0], e[1]),
        )
        if not entries:
            continue
        lines += [f"## {label}", ""]
        for src, ref, meta in entries:
            elements += 1
            cur = seq
            seq += 1
            head = src or f"{ref} (tylko EN)"
            lines.append(f"{cur}. [{label}] {head}")
            lines.append(f"   słownik: {kind}")
            lines.append(f"   źródło: {meta['first_file']} :: {meta['first_addr']}")
            lines.append(f"   występuje: {meta['count']}×")
            key = (src, ref)
            if key in seen:
                lines.append(
                    f"   (powtórzenie elementu {seen[key]} — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)"
                )
                continue
            seen[key] = cur
            todo += 1
            lines.append(f"   limit: do {compute_limit('name', src, ref)} znaków")
            lines.append(f"   EN: {ref or '(brak wersji angielskiej)'}")
            lines.append("   PL:")
        lines.append("")

    eff_mc_blocks = _filter_blocks_by_addrs(mc_blocks, include_addrs) if include_addrs is not None else mc_blocks
    for b in eff_mc_blocks:
        b_lines, seq, el, td = render_section_lines(corpus, b, seen, seq)
        elements += el
        todo += td
        lines.extend(b_lines)

    if elements == 0:
        return "", 0, 0
    return "\n".join(lines).rstrip() + "\n", elements, todo


def build_views(
    snapshot: Snapshot,
    static: StaticData | None = None,
    source: str = "kr",
    reference: str = "en",
    include_addrs: set[tuple[str, str]] | None = None,
) -> tuple[dict[str, str], dict]:
    """Build ``widoki.zip`` Markdown files (full or filtered to ``include_addrs``)."""
    corpus = Corpus(snapshot, static=static, source=source, reference=reference)

    domains: list[tuple[str, str, str, list[SectionBlock]]] = []

    combat_blocks = build_combat_dictionary(corpus)
    if combat_blocks:
        domains.append((
            "01_slownik_bojowy",
            "Słownik bojowy — tagi umiejętności, grzechy, słowa kluczowe, statusy i Panika",
            "Fundament terminologii bojowej Limbus Company: przetłumacz ten dział w pierwszej kolejności, aby zachować spójność nazw statusów i tagów w umiejętnościach oraz Darach E.G.O.",
            combat_blocks,
        ))

    domains.extend(build_sinners_and_identities(corpus))
    domains.extend(build_ego_and_gifts(corpus))
    domains.extend(build_abnormalities_events_and_enemies(corpus))
    domains.extend(build_announcers_and_music(corpus))
    domains.extend(build_rpg_canto10(corpus))
    domains.extend(build_theater_stages_and_dungeons(corpus))
    domains.extend(build_ui_tutorials_events_and_shop(corpus))

    mc_blocks: list[SectionBlock] = []
    if "ScenarioModelCodes-AutoCreated.json" in corpus.logical_files:
        mc_blocks = append_generic_file_sections(
            corpus, ["ScenarioModelCodes-AutoCreated.json"], "Tabela modeli postaci"
        )
        for b in mc_blocks:
            b.context_lines.append(
                "- Uwaga: imiona używane w scenach fabularnych pokrywają się częściowo z `sceny.zip/mowcy-i-miejsca.md`; zachowaj identyczną pisownię imion i przydomków."
            )

    # Automatic catch-all for any remaining translatable leaves in any file
    remaining_files = [
        f for f in corpus.logical_files
        if any((f, a) not in corpus.consumed for a in corpus.translatable.get(f, []))
    ]
    if remaining_files:
        catchall_blocks = append_generic_file_sections(corpus, remaining_files, "Pozostałe tabele gry")
        if catchall_blocks:
            domains.append((
                "09_pozostale_widoki",
                "Pozostałe tabele lokalizacji gry",
                "Dodatkowe wpisy lokalizacyjne nieprzypisane do wcześniejszych działów tematycznych.",
                catchall_blocks,
            ))

    # Strict 100% coverage gate on the full snapshot!
    missing: list[tuple[str, str]] = []
    total_leaves = 0
    for f in corpus.logical_files:
        addrs = corpus.translatable.get(f, [])
        total_leaves += len(addrs)
        for a in addrs:
            if (f, a) not in corpus.consumed:
                missing.append((f, a))
    if missing:
        sample = ", ".join(f"{f}::{a}" for f, a in missing[:10])
        raise RuntimeError(f"widoki.zip coverage gate failed: {len(missing)} unconsumed leaves (e.g. {sample})")

    glossary_md, gl_elements, gl_todo = render_view_glossary(corpus, mc_blocks, include_addrs=include_addrs)
    if include_addrs is not None:
        domains = [
            (base, title, intro, _filter_blocks_by_addrs(blocks, include_addrs))
            for base, title, intro, blocks in domains
        ]
        touched_files = {lf for lf, _ in include_addrs}
        toc_header = (
            f"Tryb przyrostowy — dotkniętych plików poza `StoryData/`: **{len(touched_files)}** · "
            f"Dotkniętych pól tekstowych: **{len(include_addrs)}**."
        )
    else:
        toc_header = (
            f"Plików źródłowych poza `StoryData/`: **{len(corpus.logical_files)}** · "
            f"Wszystkich niepustych pól tekstowych w grze: **{total_leaves}** (pokrycie: **100%**)."
        )

    files: dict[str, str] = {}
    toc = [
        "# Spis widoków i działów niefabularnych — Limbus Company",
        "",
        toc_header,
        "",
        "| # | dział | elementów | do tłumaczenia | pliki `.md` |",
        "|---|---|---|---|---|",
    ]

    total_elements = 0
    total_todo = 0
    row_no = 0
    if glossary_md:
        row_no += 1
        files["mowcy-rpg-i-anomalii.md"] = glossary_md
        total_elements += gl_elements
        total_todo += gl_todo
        toc.append(
            f"| {row_no} | Mówcy RPG, testów Anomalii i tabela modeli | {gl_elements} | {gl_todo} | mowcy-rpg-i-anomalii.md |"
        )

    for base, title, intro, blocks in domains:
        produced, el, td = chunk_domain_files(corpus, base, title, intro, blocks)
        if not produced:
            continue
        row_no += 1
        files.update(produced)
        total_elements += el
        total_todo += td
        toc.append(f"| {row_no} | {title} | {el} | {td} | {', '.join(sorted(produced))} |")

    files["spis-widokow.md"] = "\n".join(toc) + "\n"
    stats = {
        "widoki_pliki_gry": len({lf for lf, _ in include_addrs}) if include_addrs is not None else len(corpus.logical_files),
        "widoki_liscie_json": len(include_addrs) if include_addrs is not None else total_leaves,
        "widoki_pliki_md": len(files),
        "widoki_elementy": total_elements,
        "widoki_do_tlumaczenia": total_todo,
    }
    return files, stats
