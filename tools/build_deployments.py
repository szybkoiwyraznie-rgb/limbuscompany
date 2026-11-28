#!/usr/bin/env python3
"""Deploymenty misji (wzór SRW: ``srwy_mission_deployments.md``) — seria plików
``czytanki/deployment_<LANG>/``: dla **każdego etapu** lista fal przeciwników
oraz pełne karty tych przeciwników (statystyki, opis, umiejętności z mocami
monet, pasywki; Anomalie z częściami). Dane celowo się powtarzają między
etapami — czytanie bez przeszukiwania plików.

Pliki grupują etapy według kolejności fabuły (Prolog → Canto I–X → Intervallo
→ Noce Walpurgii → pozostałe wydarzenia), jak seria ``fabula_<LANG>``. Pule
jednostek części etapów pochodzą z tabel ``enemy``/``abnormality-unit`` (poza
proceduralnymi Lustrzanymi Lochami); fale z tabel ``battle-story`` (walka
fabularna) i uzupełniająco ``battle-ab`` (walki z Anomaliami). Nazwy i opisy z
``Localize`` (mapowanie przez pole ``nameID``); wersja PL z fallbackiem EN.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path, PurePosixPath

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_profiles import DEFENSE, coin_text, merged_levels, number
from tools.lcb_text import Texts, one_line, stage_label, to_markdown
from tools.localize import Snapshot
from tools.md_table_align import align_markdown_tables
from tools.static_data import StaticData, load_lenient

ROOT = Path(__file__).resolve().parent.parent
GAME = "Limbus Company"

# Rodziny proceduralne (Lustrzane Lochy i pochodne) — poza zakresem misji.
EXCLUDED = ("mirrordungeon", "schema-craft", "shadowenemy")

STORY_PART = re.compile(r"^a1c(\d+)p(\d+)$")
NUM_PART = re.compile(r"^(\d+)-(\d+)$")
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
         8: "VIII", 9: "IX", 10: "X"}

# Grupy plików serii (kolejność fabuły wg spisu Czytanki/fabula; tytuły z
# fabula_PL/00_spis_PL.md i tytułów StageNode). ``fams`` = klucze rodzin fal
# (StageNode* / storybattle* / abbattle*).
GROUPS: list[tuple[str, str, tuple[str, ...]]] = [
    ("01_prolog_PL.md", "Prolog", ("tutorialRenewal",)),
    ("02_canto_i_PL.md", "Canto I: Nieprzynależny", ("1-1",)),
    ("03_canto_ii_PL.md", "Canto II: Niekochająca", ("1-2",)),
    ("04_canto_iii_PL.md", "Canto III: Unikający", ("1-3",)),
    ("05_intervallo_i_hells_chicken_PL.md", "Intervallo I: Hell's Chicken", ("91-3",)),
    ("06_canto_iv_PL.md", "Canto IV: Niezmienny", ("1-4",)),
    ("07_intervallo_ii_morze_PL.md", "Intervallo II: M.O.R.Z.E.", ("91-4",)),
    ("08_canto_v_PL.md", "Canto V: Uznana za zło",
     ("a1c5p1", "a1c5p2", "a1c5p3")),
    ("09_intervallo_iii_miracle_in_district_20_PL.md",
     "Intervallo III: Cud w Dystrykcie 20", ("91-5",)),
    ("10_walpurgis_2nd_night_PL.md", "2. Noc Walpurgii", ("91-6",)),
    ("11_intervallo_iii_yield_my_flesh_PL.md",
     "Intervallo III: Poświęcić ciało, by zmiażdżyć kości", ("91-7",)),
    ("12_canto_vi_PL.md", "Canto VI: Rozdarty", ("a1c6p1", "a1c6p2", "a1c6p3")),
    ("13_walpurgis_3rd_night_PL.md", "3. Noc Walpurgii", ("91-8", "wp3")),
    ("14_intervallo_iv_timekilling_time_PL.md",
     "Intervallo IV: Czas zabijania czasu", ("91-9", "tkt-re")),
    ("15_intervallo_iv_murder_on_the_warp_express_PL.md",
     "Intervallo IV: Morderstwo w Warp Expressie", ("91-10", "mowe", "mowe-re")),
    ("16_walpurgis_4th_night_PL.md", "4. Noc Walpurgii", ("91-11", "wp4")),
    ("17_canto_vii_PL.md", "Canto VII: Koniec Snu",
     ("a1c7p1", "a1c7p2", "a1c7p3")),
    ("18_walpurgis_5th_night_PL.md", "5. Noc Walpurgii", ("91-13", "wp5")),
    ("19_intervallo_v_lcb_regular_check_up_PL.md",
     "Intervallo V: Okresowe badania LCB", ("91-14", "91-24")),
    ("20_intervallo_v_nocturnal_sweeping_PL.md",
     "Intervallo V: Nocne zamiatanie", ("night-cleanup-re",)),
    ("21_canto_viii_PL.md", "Canto VIII: Skazany na patrzenie",
     ("a1c8p1", "a1c8p2", "a1c8p3")),
    ("22_walpurgis_6th_night_PL.md", "6. Noc Walpurgii", ("91-17", "wp6")),
    ("23_intervallo_vi_spring_cultivation_PL.md",
     "Intervallo VI: Wiosenne szlify", ("91-19",)),
    ("24_8_5_ex_pilgrimage_of_compassion_PL.md",
     "8.5-EX: Pielgrzymka dobrej woli", ("91-20", "91-21")),
    ("25_canto_ix_PL.md", "Canto IX: Nierozerwana",
     ("a1c9p1", "a1c9p2", "a1c9p3")),
    ("26_walpurgis_8th_night_PL.md", "8. Noc Walpurgii", ("91-23", "wp8")),
    ("27_intervallo_vii_twining_threads_PL.md",
     "Intervallo VII: Splatanie nici", ("91-25",)),
    ("28_intervallo_vii_mnestic_experience_PL.md",
     "Intervallo VII: Pamięć doświadczeń", ("91-27",)),
    ("29_canto_x_PL.md", "Canto X: Obserwowany",
     ("a1c10p1", "a1c10p2", "a1c10p3")),
    ("30_walpurgis_10th_night_PL.md", "10. Noc Walpurgii", ("91-29", "wp10")),
]
MISC_SLUG = "31_inne_wydarzenia_PL.md"
MISC_TITLE = "Inne wydarzenia i pozostałe części"
COMMON_SLUG = "99_zestaw_wspolny_PL.md"
COMMON_TITLE = "Zestaw wspólny (`enemy.json`) — jednostki bez przypisanego etapu"

FAM_LABELS = {
    "tutorialRenewal": "Prolog",
    "common": "Zestaw wspólny (`enemy.json`)",
    "91-16": "Wydarzenie: Nowy Rok (`91-16`)",
}


def _rows_file(static: StaticData, rel: str) -> list[dict]:
    """Wiersze jednego pliku tabeli StaticData (puste pliki → [])."""
    path = static.root / rel
    if not path.is_file():
        return []
    doc = load_lenient(path.read_bytes())
    if isinstance(doc, list):
        payload = doc
    elif isinstance(doc, dict):
        payload = doc.get("list", [])
    else:
        payload = []
    return [row for row in payload if isinstance(row, dict)]


def _family_of(stem: str, prefix: str) -> str:
    """``enemy-a1c5p1`` → ``a1c5p1``; ``enemy91-4`` → ``91-4``; ``enemy`` → ``common``."""
    leaf = stem[len(prefix):]
    if leaf.startswith("-"):
        leaf = leaf[1:]
    return leaf or "common"


def _fam_label(fam: str) -> str:
    if fam in FAM_LABELS:
        return FAM_LABELS[fam]
    match = STORY_PART.match(fam)
    if match:
        canto = int(match.group(1))
        return f"Canto {ROMAN.get(canto, canto)} · część {int(match.group(2))} (`{fam}`)"
    return f"Część `{fam}`"


# ----------------------------------------------------------------- dane wej.
def _families(static: StaticData) -> dict[str, dict]:
    """family → flagi (``enemy``/``abnormality``), poza wykluczonymi."""
    out: dict[str, dict] = {}
    for path in static.files("enemy"):
        fam = _family_of(path.stem, "enemy")
        if any(x in fam for x in EXCLUDED):
            continue
        out.setdefault(fam, {})["enemy"] = True
    for path in static.files("abnormality-unit"):
        fam = _family_of(path.stem, "abnormality-unit")
        if any(x in fam for x in EXCLUDED):
            continue
        out.setdefault(fam, {})["abnormality"] = True
    return out


def _stage_rows(texts: Texts, fam: str) -> list[dict]:
    if fam == "tutorialRenewal":
        name = "StageNode1-0.json"
    elif fam[0].isdigit():
        name = f"StageNode{fam}.json"
    else:
        name = f"StageNode-{fam}.json"
    if name not in texts.snapshot.files[texts.lang]:
        return []
    return texts.table(name)


def _stage_fam_map(texts: Texts) -> dict[int, str]:
    """stage id → część etapów wg plików ``StageNode*`` ('1-0' → Prolog)."""
    out: dict[int, str] = {}
    for name in texts.names():
        stem = PurePosixPath(name).stem
        if "/" in name or not stem.startswith("StageNode"):
            continue
        leaf = stem[len("StageNode"):]
        if leaf.startswith("-"):
            leaf = leaf[1:]
        fam = "tutorialRenewal" if leaf == "1-0" else leaf
        for row in texts.table(name):
            sid = int(row.get("id", 0) or 0)
            if sid:
                out.setdefault(sid, fam)
    return out


def _all_waves(static: StaticData, stage_fam: dict[int, str]) -> dict[int, dict]:
    """stage_id → ``{"waves": [...], "fam": …}``; walka fabularna wygrywa."""
    out: dict[int, dict] = {}
    for folder, prefix in (("battle-story", "storybattle"), ("battle-ab", "abbattle")):
        for path in static.files(folder):
            fam = _family_of(path.stem, prefix)
            if folder == "battle-story" and path.stem == "stage_Tutorial":
                fam = "tutorialRenewal"
            for row in _rows_file(static, f"{folder}/{path.name}"):
                sid = row.get("id")
                if not row.get("waveList") or sid is None:
                    continue
                rec = {"waves": row["waveList"], "fam": stage_fam.get(int(sid), fam)}
                if folder == "battle-story" or int(sid) not in out:
                    out[int(sid)] = rec
    return out


def _uid2static(static: StaticData) -> dict[int, tuple[str, dict]]:
    """unit id → (rodzaj, wiersz statystyk) z tabel enemy/abnormality-unit/part."""
    out: dict[int, tuple[str, dict]] = {}
    for folder, kind in (("enemy", "wrogowie"), ("abnormality-unit", "anomalia"),
                         ("abnormality-part", "część")):
        for path in static.files(folder):
            for row in _rows_file(static, f"{folder}/{path.name}"):
                uid = row.get("id")
                if uid is not None:
                    out.setdefault(int(uid), (kind, row))
    return out


def _unit2nameid(static: StaticData) -> dict[int, int]:
    """unit id → ``nameID`` (id wpisu lokalizacji z nazwą)."""
    out: dict[int, int] = {}
    for folder in ("enemy", "abnormality-unit", "abnormality-part"):
        for path in static.files(folder):
            for row in _rows_file(static, f"{folder}/{path.name}"):
                nid = row.get("nameID")
                uid = row.get("id")
                if nid and uid:
                    out[int(uid)] = int(nid)
    return out


# ----------------------------------------------------------------- lokalizacja
def _loc_row(enemies_loc: dict[int, dict], unit2nameid: dict[int, int], uid: int) -> dict:
    row = enemies_loc.get(uid, {})
    nid = unit2nameid.get(uid)
    if nid and not (row.get("name") or row.get("desc")):
        row = enemies_loc.get(nid, row)
    return row


def _unit_name(enemies_loc: dict[int, dict], unit2nameid: dict[int, int], uid: int) -> str:
    row = _loc_row(enemies_loc, unit2nameid, uid)
    return one_line(to_markdown(row.get("name"))) or f"jednostka {uid}"


def _enemy_text_maps(texts: Texts) -> tuple[dict[int, dict], dict[int, list], dict[int, dict]]:
    """id → (name, desc) wrogów / id → levelList skilli / id → pasywki."""
    enemies: dict[int, dict] = {}
    for row in texts.family("Enemies"):
        try:
            enemies[int(row["id"])] = row
        except (KeyError, TypeError, ValueError):
            continue
    skills: dict[int, list] = {}
    for table in ("Skills_Enemy", "Skills_Abnormality"):
        for row in texts.family(table):
            try:
                skills[int(row["id"])] = row.get("levelList", []) or []
            except (KeyError, TypeError, ValueError):
                continue
    passives: dict[int, dict] = {}
    for table in ("Passives_Enemy", "Passives_Abnormality"):
        for row in texts.family(table):
            try:
                passives[int(row["id"])] = row
            except (KeyError, TypeError, ValueError):
                continue
    return enemies, skills, passives


# ----------------------------------------------------------------- renderery
class Renderer:
    """Etykiety grzechów/ataków z Localize + renderery statystyk."""

    def __init__(self, texts: Texts, lang: str) -> None:
        self.texts = texts
        self.lang = lang
        self.sins = {k: one_line(to_markdown(v.get("name"))) for k, v in texts.by_id("AttributeText").items()}
        ui = {k: one_line(to_markdown(v.get("content"))) for k, v in texts.by_id("BattleUIText").items()}
        self.attacks = {code: ui.get(key) or code.title() for code, key in
                        (("SLASH", "slash"), ("PENETRATE", "penetrate"), ("HIT", "hit"))}

    def sin(self, key: object) -> str:
        return self.sins.get(str(key), str(key).title() if key else "—")

    def attack(self, key: object) -> str:
        return self.attacks.get(str(key), str(key).title() if key else "—")

    def kw(self, text: object) -> str:
        return to_markdown(text, self.texts.keywords)

    def resists(self, resist_info: dict) -> str:
        parts = []
        for entry in (resist_info or {}).get("atkResistList", []):
            value = entry.get("value")
            if value != 1:
                parts.append(f"{self.attack(entry.get('type'))} ×{number(value)}")
        for entry in (resist_info or {}).get("attributeResistList", []):
            value = entry.get("value")
            if value != 1:
                label = self.sin(entry.get("type"))
                note = {2.0: "Fatal", 1.5: "Weak", 0.75: "Endured", 0.5: "Ineff.", 0.25: "Ineff.",
                        0.0: "Immune"}.get(float(value), "")
                parts.append(f"{label} ×{number(value)}" + (f" ({note})" if note else ""))
        return "; ".join(parts) or "wszystkie ×1 (Normal)"

    def stats_table(self, row: dict) -> list[str]:
        hp = row.get("hp", {}) or {}
        out = ["| Parametr | Wartość |", "|---|---|"]
        out.append(f"| Poziom | {number(row.get('level', '—'))} |")
        out.append(f"| HP | {number(hp.get('defaultStat', '—'))} (+{number(hp.get('incrementByLevel', '—'))} za poziom) |")
        speeds = " / ".join(f"{a}–{b}" for a, b in zip(row.get("minSpeedList", []) or [],
                                                       row.get("maxSpeedList", []) or []))
        if speeds:
            out.append(f"| Szybkość | {speeds} |")
        starts = row.get("startActionSlotNumList") or row.get("startActionSlotNum")
        if starts:
            if isinstance(starts, list):
                out.append(f"| Sloty akcji | start: {'/'.join(str(s) for s in starts)}"
                           f" · maks. {number(row.get('maxActionSlotNum', '—'))} |")
            else:
                out.append(f"| Sloty akcji | start: {number(starts)}"
                           f" · maks. {number(row.get('maxActionSlotNum', '—'))} |")
        stagger = " / ".join(f"{v}%" for v in (row.get("breakSection", {}) or {}).get("sectionList", []))
        if stagger:
            out.append(f"| Progi oszołomienia | {stagger} |")
        out.append(f"| Odporności | {self.resists(row.get('resistInfo', {}) or {})} |")
        return out


def _wave_line(enemies_loc: dict[int, dict], unit2nameid: dict[int, int], wave: dict) -> str:
    units = []
    for bucket, tag in (("unitList", ""), ("subUnitList", " (wsparcie)")):
        for unit in wave.get(bucket, []) or []:
            uid = int(unit.get("unitID", 0) or 0)
            name = _unit_name(enemies_loc, unit2nameid, uid)
            count = unit.get("unitCount", 1)
            level = unit.get("unitLevel")
            units.append(f"{name} ×{count}" + (f" (poz. {level})" if level is not None else "") + tag)
    return "; ".join(units) or "—"


def _skill_static(static: StaticData) -> dict[int, dict]:
    return {row["id"]: row for row in static.rows("skill") if "id" in row}


def _render_skills(out: list[str], renderer: Renderer, ids_numbers: list[dict],
                   skills_loc: dict[int, list], skills_static: dict[int, dict],
                   heading: str = "#####") -> None:
    shown = 0
    for entry in ids_numbers:
        sid = entry.get("skillId")
        if sid is None or int(sid) <= 0:
            continue
        number_of = entry.get("number", 1)
        levels = skills_loc.get(int(sid), []) or []
        name = one_line(to_markdown(levels[-1].get("name"))) if levels else f"umiejętność {sid}"
        count_note = f" (×{number_of})" if number_of and number_of != 1 else ""
        out += [f"{heading} Umiejętność: {name}{count_note} — id {sid}", ""]
        data = skills_static.get(int(sid), {})
        entries = data.get("skillData", []) or []
        rows = merged_levels(entries, "gaksungLevel") if any("gaksungLevel" in e for e in entries) else \
            [(1, entries[0])] if entries else []
        if rows:
            out += ["| Poz. | Grzech | Typ | Moc bazowa | Moc monety | Monety | Cele |",
                    "|---:|---|---|---:|---:|---:|---:|"]
            for level, state in rows:
                kind = DEFENSE.get(state.get("defType")) if state.get("defType") != "ATTACK" else None
                cells = (renderer.sin(state.get("attributeType")),
                         kind or renderer.attack(state.get("atkType")),
                         number(state.get("defaultValue", "—")),
                         coin_text(state.get("coinList", [])),
                         str(len(state.get("coinList", []) or [])),
                         str(state.get("targetNum", "—")))
                out.append(f"| {level} | " + " | ".join(cells) + " |")
            out.append("")
        shown += 1
    if not shown:
        out += [f"{heading} Umiejętności", "", "*Brak danych o umiejętnościach.*", ""]


def _render_passives(out: list[str], renderer: Renderer, passive_ids: list,
                     passives_loc: dict[int, dict]) -> None:
    lines = []
    for pid in passive_ids or []:
        row = passives_loc.get(int(pid))
        if not row:
            continue
        name = one_line(to_markdown(row.get("name")))
        desc = renderer.kw(row.get("desc"))
        lines.append(f"- **{name or pid}** — {desc}" if desc else f"- **{name or pid}**")
    if lines:
        out += ["**Pasywki:**", ""]
        out += lines
        out.append("")


class Context:
    """Wspólne mapy dla całej serii."""

    def __init__(self, texts: Texts, lang: str) -> None:
        self.texts = texts
        self.lang = lang
        self.static = StaticData(ROOT / "index" / "static-data")
        self.renderer = Renderer(texts, lang)
        self.enemies_loc, self.skills_loc, self.passives_loc = _enemy_text_maps(texts)
        self.skills_static = _skill_static(self.static)
        self.unit2nameid = _unit2nameid(self.static)
        self.uid2static = _uid2static(self.static)
        self.stage_fam = _stage_fam_map(texts)
        self.waves = _all_waves(self.static, self.stage_fam)
        self.families = _families(self.static)
        for rec in self.waves.values():
            self.families.setdefault(rec["fam"], {}).setdefault("waves", True)
        self.used_uids: set[int] = set()
        for rec in self.waves.values():
            for wave in rec["waves"]:
                for bucket in ("unitList", "subUnitList"):
                    for unit in wave.get(bucket) or []:
                        uid = int(unit.get("unitID", 0) or 0)
                        if uid:
                            self.used_uids.add(uid)
        self.unit2fam: dict[int, str] = {}
        for fam, flags in self.families.items():
            for rel, kind in self._fam_tables(fam):
                for row in self._rows(rel):
                    self.unit2fam.setdefault(int(row["id"]), fam)

    def _fam_tables(self, fam: str) -> list[tuple[str, str]]:
        if fam == "common":
            return [("enemy/enemy.json", "enemy"), ("abnormality-unit/abnormality-unit.json", "unit")]
        out = [(f"enemy/enemy-{fam}.json", "enemy"),
               (f"abnormality-unit/abnormality-unit-{fam}.json", "unit")]
        return out

    def _rows(self, rel: str) -> list[dict]:
        return [r for r in _rows_file(self.static, rel) if r.get("id") is not None]

    def name(self, uid: int) -> str:
        return _unit_name(self.enemies_loc, self.unit2nameid, uid)

    def card(self, out: list[str], uid: int, occ: dict, heading: str = "####") -> None:
        """Karta jednostki: wystąpienia, statystyki, opis, umiejętności, pasywki."""
        kind, row = self.uid2static.get(uid, ("", {}))
        name = self.name(uid)
        counts = occ["count"]
        levels = sorted(occ["levels"])
        tags = ""
        if occ.get("support"):
            tags += " · też jako wsparcie"
        lvl_note = "poz. " + ", ".join(str(x) for x in levels) if levels else "poz. —"
        out += [f"{heading} {name} — id {uid}", ""]
        out += [f"*Wystąpienia: ×{counts} ({lvl_note}){tags}.*", ""]
        if not row:
            out += ["*Brak danych statystyk w StaticData.*", ""]
            return
        out += self.renderer.stats_table(row)
        out.append("")
        desc = self.renderer.kw(_loc_row(self.enemies_loc, self.unit2nameid, uid).get("desc"))
        if desc:
            out += [f"*Opis:* {desc}", ""]
        raw_parts = row.get("abnormalityPartList", []) or []
        part_ids = [int(p if isinstance(p, (int, float)) else p.get("id", 0) or 0) for p in raw_parts]
        if part_ids:
            out += ["**Części (anatomia):**", ""]
            for pid in part_ids:
                _, prow = self.uid2static.get(pid, ("część", {}))
                ploc = _loc_row(self.enemies_loc, self.unit2nameid, pid)
                pname = one_line(to_markdown(ploc.get("name"))) or f"część id {pid}"
                out += [f"{heading}# {pname} — id {pid}", ""]
                if prow:
                    out += self.renderer.stats_table(prow)
                    out.append("")
                pdesc = self.renderer.kw(ploc.get("desc"))
                if pdesc:
                    out += [f"*Opis:* {pdesc}", ""]
        _render_skills(out, self.renderer, row.get("attributeList", []) or [],
                       self.skills_loc, self.skills_static, heading=f"{heading}#")
        _render_passives(out, self.renderer, (row.get("passiveSet", {}) or {}).get("passiveIdList"),
                         self.passives_loc)


def _occurrences(ctx: Context, waves: list[dict]) -> dict[int, dict]:
    """uid → {count, levels, support} w kolejności pierwszego wystąpienia."""
    out: dict[int, dict] = {}

    def add(uid: int, count: int, level, support: bool) -> None:
        if uid <= 0:
            return
        rec = out.setdefault(uid, {"count": 0, "levels": set(), "support": False})
        rec["count"] += count
        if level is not None:
            rec["levels"].add(int(level))
        rec["support"] = rec["support"] or support

    for wave in waves:
        for unit in wave.get("unitList") or []:
            add(int(unit.get("unitID", 0) or 0), int(unit.get("unitCount", 1) or 1),
                unit.get("unitLevel"), False)
        for unit in wave.get("subUnitList") or []:
            add(int(unit.get("unitID", 0) or 0), int(unit.get("unitCount", 1) or 1),
                unit.get("unitLevel"), True)
    return out


def _stage_block(ctx: Context, out: list[str], sid: int) -> None:
    rec = ctx.waves[sid]
    stage_row = next((r for r in _stage_rows(ctx.texts, rec["fam"])
                      if int(r.get("id", 0) or 0) == sid), None)
    label = stage_label(sid)
    heading = f"### Etap {label or sid}"
    if stage_row:
        title = one_line(to_markdown(stage_row.get("title")))
        if title:
            heading += f" · {title}"
    out += [heading, ""]
    for wi, wave in enumerate(rec["waves"], 1):
        line = _wave_line(ctx.enemies_loc, ctx.unit2nameid, wave)
        out += [f"- **Fala {wi}:** {line}"]
    out.append("")
    for uid, occ in _occurrences(ctx, rec["waves"]).items():
        ctx.card(out, uid, occ)


def _fam_section(ctx: Context, out: list[str], fam: str) -> tuple[int, int]:
    """Blok jednej rodziny: etapy + pula bez przypisania. → (etapy, karty)."""
    stage_rows = _stage_rows(ctx.texts, fam)
    stage_ids = [int(r.get("id", 0) or 0) for r in stage_rows]
    wave_ids = [sid for sid in stage_ids if sid in ctx.waves]
    wave_ids += sorted(sid for sid, rec in ctx.waves.items()
                       if rec["fam"] == fam and sid not in wave_ids)
    cards = 0
    pool = [int(row["id"]) for rel, _ in ctx._fam_tables(fam)
            for row in ctx._rows(rel) if int(row["id"]) not in ctx.used_uids]
    if not wave_ids and not pool:
        return 0, 0
    out += [f"## Część: {_fam_label(fam)}", ""]
    for sid in sorted(wave_ids):
        _stage_block(ctx, out, sid)
        cards += len(_occurrences(ctx, ctx.waves[sid]["waves"]))
    # pula części: jednostki tej rodziny, które nie występują w żadnym etapie
    if pool:
        out += [f"## Pula {_fam_label(fam)} — jednostki bez przypisanego etapu", ""]
        for uid in sorted(pool):
            ctx.card(out, uid, {"count": 0, "levels": set(), "support": False})
            cards += 1
    return len(wave_ids), cards


INTRO = ("Dla każdego etapu: fale przeciwników, a pod nimi pełne karty"
         " (statystyki, opis, umiejętności z mocami monet, pasywki; Anomalie z"
         " częściami). Dane celowo powtarzają się między etapami. „poz.” ="
         " poziom jednostki w etapie; „(wsparcie)” = jednostka towarzysząca;"
         " „×N” = liczba sztuk. Wartości bazowe z StaticData.")


def _slug_numbered(n: int, slug: str) -> str:
    """``01_prolog_PL.md`` z licznikiem porządkowym zamiast wbudowanego numeru."""
    return f"{n:02d}_{slug.split('_', 1)[1]}"


def build_deployments_series(texts: Texts, lang: str, out_dir: Path) -> list[dict]:
    """Buduje serię deploymentów i zapisuje ją do ``out_dir`` (bez spisu)."""
    ctx = Context(texts, lang)
    grouped = {fam for _, _, fams in GROUPS for fam in fams}
    misc_fams = [fam for fam, flags in ctx.families.items()
                 if fam != "common" and fam not in grouped]
    summary: list[dict] = []
    ordinal = 0

    def write_file(body_slug: str, title: str, out: list[str],
                   stages: int, cards: int) -> None:
        nonlocal ordinal
        ordinal += 1
        out_dir.mkdir(parents=True, exist_ok=True)
        name = _slug_numbered(ordinal, body_slug)
        (out_dir / name).write_text(
            align_markdown_tables("\n".join(out).rstrip() + "\n"), encoding="utf-8")
        summary.append({"name": name, "title": title, "stages": stages, "cards": cards})

    for slug, title, fams in GROUPS:
        out = [f"# {GAME} — {title} — deploymenty misji", "", INTRO, ""]
        stages = cards = 0
        any_content = False
        for fam in fams:
            if fam not in ctx.families and not any(
                    rec["fam"] == fam for rec in ctx.waves.values()):
                continue
            s, c = _fam_section(ctx, out, fam)
            stages += s
            cards += c
            any_content = any_content or bool(s or c)
        if not any_content:
            continue
        write_file(slug, title, out, stages, cards)
    if misc_fams:
        out = [f"# {GAME} — {MISC_TITLE} — deploymenty misji", "", INTRO, ""]
        stages = cards = 0
        for fam in misc_fams:
            s, c = _fam_section(ctx, out, fam)
            stages += s
            cards += c
        write_file(MISC_SLUG, MISC_TITLE, out, stages, cards)
    # zestaw wspólny: jednostki `enemy.json` bez przypisanego etapu
    pool = [int(row["id"]) for row in ctx._rows("enemy/enemy.json")
            if int(row["id"]) not in ctx.used_uids]
    if pool:
        out = [f"# {GAME} — {COMMON_TITLE}", "", INTRO, ""]
        out += ["## Pula: zestaw wspólny (`enemy.json`)", ""]
        for uid in sorted(pool):
            ctx.card(out, uid, {"count": 0, "levels": set(), "support": False})
        write_file(COMMON_SLUG, COMMON_TITLE, out, 0, len(pool))
    return summary


def build_deployments_index(summary: list[dict], lang: str) -> str:
    suffix = lang.upper()
    out = [f"# {GAME} — Deploymenty misji — spis serii", "",
           "Dla każdego etapu: fale przeciwników i pełne karty jednostek"
           " (statystyki, opis, umiejętności, pasywki). Kolejność jak seria"
           " fabuły.", "",
           f"| Plik | Część | Etapy | Karty jednostek |", "|---|---|---:|---:|"]
    for rec in summary:
        out.append(f"| `{rec['name']}` | {rec['title']} | {rec['stages']} | {rec['cards']} |")
    out.append("")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    from tools.md_table_align import align_markdown_tables

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "local" / "cz_snapshot",
                        help="Localize snapshot: katalog z <lang>/ (default local/cz_snapshot)")
    parser.add_argument("--lang", default="pl")
    parser.add_argument("--out", type=Path, help="default: czytanki/deployment_<LANG>")
    args = parser.parse_args(argv)
    args.out = args.out or ROOT / "czytanki" / f"deployment_{args.lang.upper()}"
    args.out.mkdir(parents=True, exist_ok=True)
    suffix = args.lang.upper()
    with Snapshot.open(args.snapshot) as snapshot:
        summary = build_deployments_series(Texts(snapshot, args.lang), args.lang, args.out)
        (args.out / f"00_spis_DEPLOYMENT_{suffix}.md").write_text(
            align_markdown_tables(build_deployments_index(summary, args.lang)), encoding="utf-8")
    print(f"zapisano {len(summary) + 1} plików do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
