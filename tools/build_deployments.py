#!/usr/bin/env python3
"""Deploymenty misji (wzór SRW: ``srwy_mission_deployments.md``) — kto jest
przeciwnikiem w każdej misji, jakie ma statystyki, opisy i zdolności.

Jeden plik ``czytanki/plik_META_<LANG>/06_deployment_<LANG>.md`` o układzie:

1. **Etapy i ich przeciwnicy** — per część etapów (rodziny z tabel
   ``battle-story``/``battle-ab`` i tabel wrogów) lista etapów (``StageNode``:
   ``Etap X-Y · tytuł``) z dokładnymi falami przeciwników (``waveList``:
   battle-story = walka fabularna, battle-ab = walki z Anomaliami);
2. **Szczegóły przeciwników** — per część pula wrogów (``enemy``/``abnormality-unit``)
   z tabelami statystyk (poziom, HP, szybkość, sloty akcji, progi oszołomienia,
   odporności), opisem, umiejętnościami (grzech/typ/moc/monety/cele) i pasywkami;
   Anomalie łączą jednostkę z częściami (per część HP/odporności).

Liczby pochodzą z ``index/static-data`` (``enemy``, ``abnormality-unit``,
``abnormality-part``, ``skill``, ``battle-story``, ``battle-ab``), nazwy i opisy
z ``Localize`` (``Enemies*``, ``Skills_Enemy*``/``Skills_Abnormality*``,
``Passives_*``). Wersja PL korzysta z pakietu ``Lang/Polski`` (fallback EN
wbudowany per wpis).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path, PurePosixPath

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_profiles import DEFENSE, coin_text, merged_levels, number, signed
from tools.lcb_text import Texts, one_line, stage_label, to_markdown
from tools.localize import Snapshot
from tools.static_data import StaticData, load_lenient

ROOT = Path(__file__).resolve().parent.parent
GAME = "Limbus Company"

# Rodziny proceduralne (Lustrzane Lochy i pochodne) — poza zakresem misji.
EXCLUDED = ("mirrordungeon", "schema-craft", "shadowenemy")

STORY_PART = re.compile(r"^a1c(\d+)p(\d+)$")


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


FAM_LABELS = {
    "tutorialRenewal": "Prolog (tutorial)",
    "common": "Zestaw wspólny (`enemy.json`)",
}


NUM_PART = re.compile(r"^(\d+)-(\d+)$")


def _fam_label(fam: str) -> str:
    if fam in FAM_LABELS:
        return FAM_LABELS[fam]
    match = STORY_PART.match(fam)
    if match:
        return f"Canto {int(match.group(1))} · część {int(match.group(2))} (`{fam}`)"
    match = NUM_PART.match(fam)
    if match and 1 <= int(match.group(1)) <= 9:
        return f"Canto {int(match.group(2))} (`{fam}`)"
    return f"Część `{fam}`"


def _part_sort_key(fam: str) -> tuple:
    """Kolejność gry: Prolog, Canto I–IX (część po części), potem reszta."""
    if fam == "tutorialRenewal":
        return (0, 0, 0, fam)
    match = STORY_PART.match(fam)
    if match:
        return (1, int(match.group(1)), int(match.group(2)), fam)
    match = NUM_PART.match(fam)
    if match and 1 <= int(match.group(1)) <= 9:
        return (1, int(match.group(2)), -0.5, fam)
    if match and int(match.group(1)) == 91:
        return (1, int(match.group(2)), 0.5, fam)
    if fam == "common":
        return (2, 0, 0, fam)
    return (3, 0, 0, fam)


def _families(static: StaticData) -> dict[str, dict]:
    """family → ``{"enemy": bool, "abnormality": bool}`` (poza wykluczonymi)."""
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


def _all_waves(static: StaticData, stage_fam: dict[int, str]) -> dict[int, dict]:
    """stage_id → ``{"waves": [...], "source": "battle-story|battle-ab", "fam": …}``.

    Walka fabularna (``battle-story``) wygrywa z wpisem z ``battle-ab`` (osobne,
    powtarzalne walki z Anomaliami — inne fale dla tej samej walki).
    """
    out: dict[int, dict] = {}
    for folder, source in (("battle-story", "battle-story"), ("battle-ab", "battle-ab")):
        for path in static.files(folder):
            fam = _family_of(path.stem, "storybattle" if source == "battle-story" else "abbattle")
            if source == "battle-story" and path.stem == "stage_Tutorial":
                fam = "tutorialRenewal"
            for row in _rows_file(static, f"{folder}/{path.name}"):
                sid = row.get("id")
                if not row.get("waveList") or sid is None:
                    continue
                rec = {"waves": row["waveList"], "source": source,
                       "fam": stage_fam.get(int(sid), fam)}
                if source == "battle-story" or sid not in out:
                    out[int(sid)] = rec
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

    def stats_table(self, row: dict, part: bool = False) -> list[str]:
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


def _unit2nameid(static: StaticData) -> dict[int, int]:
    """unit id → ``nameID`` (id wpisu lokalizacji z nazwą; pola ``nameID`` tabel)."""
    out: dict[int, int] = {}
    for folder in ("enemy", "abnormality-unit"):
        for path in static.files(folder):
            for row in _rows_file(static, f"{folder}/{path.name}"):
                nid = row.get("nameID")
                uid = row.get("id")
                if nid and uid:
                    out[int(uid)] = int(nid)
    return out


def _loc_row(enemies_loc: dict[int, dict], unit2nameid: dict[int, int], uid: int) -> dict:
    row = enemies_loc.get(uid, {})
    nid = unit2nameid.get(uid)
    if nid and not (row.get("name") or row.get("desc")):
        row = enemies_loc.get(nid, row)
    return row


def _unit_name(enemies_loc: dict[int, dict], unit2nameid: dict[int, int], uid: int) -> str:
    row = _loc_row(enemies_loc, unit2nameid, uid)
    return one_line(to_markdown(row.get("name"))) or f"jednostka {uid}"


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


def _enemy_text_maps(texts: Texts) -> tuple[dict[int, dict], dict[int, list], dict[int, dict]]:
    """Globalne mapy id → (name, desc) / id → levelList / id → (name, desc) pasywek."""
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


def _render_skills(out: list[str], renderer: Renderer, ids_numbers: list[dict],
                   skills_loc: dict[int, list], skills_static: dict[int, dict]) -> None:
    shown = 0
    for entry in ids_numbers:
        sid = entry.get("skillId")
        if sid is None or int(sid) <= 0:
            continue
        number_of = entry.get("number", 1)
        levels = skills_loc.get(int(sid), []) or []
        name = one_line(to_markdown(levels[-1].get("name"))) if levels else f"umiejętność {sid}"
        count_note = f" (×{number_of})" if number_of and number_of != 1 else ""
        out += [f"#### Umiejętność: {name}{count_note} — id {sid}", ""]
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
        out += ["*Brak danych o umiejętnościach.*", ""]


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


def _count_untranslated(texts: Texts, lang: str, enemies: dict[int, dict]) -> int:
    if lang != "pl":
        return 0
    with Snapshot.open(ROOT / "index" / "localize") as snap:
        en = Texts(snap, "en")
        en_rows = {}
        for row in en.family("Enemies"):
            try:
                en_rows[int(row["id"])] = row
            except (KeyError, TypeError, ValueError):
                continue
    miss = 0
    for eid, row in enemies.items():
        src = en_rows.get(eid, {})
        if row.get("name") == src.get("name") and row.get("name"):
            miss += 1
        if (row.get("desc") or "") == (src.get("desc") or "") and row.get("desc"):
            miss += 1
    return miss


def build_deployments_file(texts: Texts, lang: str) -> tuple[str, int]:
    static = StaticData(ROOT / "index" / "static-data")
    renderer = Renderer(texts, lang)
    families = _families(static)
    skills_static = _skill_static(static)
    enemies_loc, skills_loc, passives_loc = _enemy_text_maps(texts)
    unit2nameid = _unit2nameid(static)
    stage_fam = _stage_fam_map(texts)
    waves = _all_waves(static, stage_fam)
    fam_of_stage: dict[int, str] = {sid: rec["fam"] for sid, rec in waves.items()}
    for fam, flags in families.items():
        flags.setdefault("waves", False)
    for rec in waves.values():
        families.setdefault(rec["fam"], {})["waves"] = True
    order = sorted(families, key=_part_sort_key)

    total_units = 0
    total_stages = 0
    unnamed = 0

    out = [
        f"# {GAME} — Deploymenty misji (przeciwnicy)",
        "",
        "**Uwaga dla czytelnika:** liczby z tabel StaticData (wartości bazowe); teksty w wersji polskiej"
        " — wpisy bez przekładu pozostają w oryginale (angielskim).",
        "",
        "**Jak czytać ten plik** — plik ma dwie duże sekcje:",
        "",
        "1. **Etapy i ich przeciwnicy** — każdy etap misji (kolejność gry: Prolog, Canto I–IX,"
        " reszta) z dokładną listą przeciwników w kolejnych falach. **To tu szukasz"
        " „kto jest przeciwnikiem w misji X-Y”** — np. przeciwnicy etapu 0-1 są"
        " w podpunkcie „Etap 0-1” sekcji „Prolog (tutorial)”. Nazwę konkretnej"
        " jednostki (liczba po przeciwniku to liczba sztuk; „poz.” = poziom;"
        " „(wsparcie)” = jednostka towarzysząca) wyszukaj (Ctrl+F) w sekcji 2.",
        "2. **Szczegóły przeciwników** — karta każdej jednostki: tabela statystyk"
        " (poziom, HP z przyrostem za poziom, szybkość, sloty akcji, progi"
        " oszołomienia, odporności), opis, umiejętności (tabela: poz. = poziom"
        " umiejętności, moc bazowa i moc monety za każdą wyrzuconą reszkę/orła,"
        " monety = liczba monet) i pasywki. Anomalie mają dodatkowo rozpisane"
        " części (osobne HP i odporności per część).",
        "",
        "Fale etapów fabularnych pochodzą z tabel `battle-story`; tam, gdzie gra"
        " przewiduje osobne walki z Anomaliami (tabele `battle-ab`), użyto ich jako"
        " uzupełnienia dla etapów bez walki fabularnej. Pula wroga części etapów"
        " (nazwa w nawiasie, np. `a1c5p1`) to identyfikator danych gry; dokładny"
        " podział zwykłych etapów na fale nie zawsze jest w danych StaticData —"
        " wtedy podany jest poziom i pula, nie kolejność tur.",
        "Zapis **„jednostka NNNNN”** = jednostka celowo bez nazwy w danych"
        " lokalizacji gry (np. bestie Prologu — Lion/Wolf/Panther); identyfikator"
        " pozwala odnaleźć jej kartę w sekcji 2, o ile dane statystyk istnieją.",
        "",
        f"Wpisów bez przekładu (fallback EN): {_count_untranslated(texts, lang, enemies_loc)}.",
        "",
    ]

    # ---------------------------------------------- 1. Etapy i ich przeciwnicy
    out += ["## 1. Etapy i ich przeciwnicy", ""]
    for fam in order:
        if not families[fam].get("waves"):
            continue
        stage_rows = _stage_rows(texts, fam)
        stage_ids = [int(r.get("id", 0) or 0) for r in stage_rows]
        wave_ids = [sid for sid in stage_ids if sid in waves]
        if not wave_ids:
            wave_ids = sorted(sid for sid, rec in fam_of_stage.items() if rec == fam)
        if not wave_ids:
            continue
        total_stages += len(wave_ids)
        out += [f"### {_fam_label(fam)}", ""]
        stage_by_id = {int(r.get("id", 0) or 0): r for r in stage_rows}
        for sid in sorted(wave_ids):
            row = stage_by_id.get(sid)
            label = stage_label(sid)
            heading = f"Etap {label or sid}"
            if row:
                title = one_line(to_markdown(row.get("title")))
                if title:
                    heading += f" · {title}"
            out += [f"#### {heading}", ""]
            for wi, wave in enumerate(waves[sid]["waves"], 1):
                line = _wave_line(enemies_loc, unit2nameid, wave)
                unnamed += line.count("jednostka ")
                out += [f"- **Fala {wi}:** {line}"]
            out.append("")
        out.append("")

    # ---------------------------------------------- 2. Szczegóły przeciwników
    out += ["## 2. Szczegóły przeciwników", ""]
    for fam in order:
        enemy_rel = f"enemy/enemy-{fam}.json" if fam != "common" else "enemy/enemy.json"
        enemy_rows = sorted(_rows_file(static, enemy_rel), key=lambda r: int(r.get("id", 0) or 0))
        unit_rel = f"abnormality-unit/abnormality-unit-{fam}.json" if fam != "common" else \
            "abnormality-unit/abnormality-unit.json"
        part_rel = f"abnormality-part/abnormality-part-{fam}.json" if fam != "common" else \
            "abnormality-part/abnormality-part.json"
        unit_rows = sorted(_rows_file(static, unit_rel), key=lambda r: int(r.get("id", 0) or 0))
        if not enemy_rows and not unit_rows:
            continue
        out += [f"### {_fam_label(fam)}", ""]
        for row in enemy_rows:
            eid = int(row.get("id", 0) or 0)
            loc = _loc_row(enemies_loc, unit2nameid, eid)
            name = one_line(to_markdown(loc.get("name"))) or f"wrogowie id {eid}"
            out += [f"#### {name} — id {eid}", ""]
            out += renderer.stats_table(row)
            out.append("")
            desc = renderer.kw(loc.get("desc"))
            if desc:
                out += [f"*Opis:* {desc}", ""]
            _render_skills(out, renderer, row.get("attributeList", []) or [],
                           skills_loc, skills_static)
            _render_passives(out, renderer, (row.get("passiveSet", {}) or {}).get("passiveIdList"),
                             passives_loc)
            total_units += 1
        if unit_rows:
            parts_static = {int(r["id"]): r for r in _rows_file(static, part_rel) if "id" in r}
            for row in unit_rows:
                uid = int(row.get("id", 0) or 0)
                loc = _loc_row(enemies_loc, unit2nameid, uid)
                name = one_line(to_markdown(loc.get("name"))) or f"anomalia id {uid}"
                klass = row.get("classType")
                sin_label = renderer.sin(row.get("attributeType"))
                meta = " · ".join(x for x in [f"klasa {klass}" if klass else "",
                                              f"grzech {sin_label}" if sin_label else ""] if x)
                out += [f"#### {name} — id {uid}" + (f" ({meta})" if meta else ""), ""]
                out += renderer.stats_table(row)
                out.append("")
                desc = renderer.kw(loc.get("desc"))
                if desc:
                    out += [f"*Opis:* {desc}", ""]
                raw_parts = row.get("abnormalityPartList", []) or []
                part_ids = [int(p if isinstance(p, (int, float)) else p.get("id", 0) or 0) for p in raw_parts]
                if part_ids:
                    out += ["**Części (anatomia):**", ""]
                    for pid in part_ids:
                        prow = parts_static.get(pid, {})
                        ploc = _loc_row(enemies_loc, unit2nameid, pid)
                        pname = one_line(to_markdown(ploc.get("name"))) or f"część id {pid}"
                        out += [f"##### {pname} — id {pid}", ""]
                        if prow:
                            out += renderer.stats_table(prow, part=True)
                            out.append("")
                        pdesc = renderer.kw(ploc.get("desc"))
                        if pdesc:
                            out += [f"*Opis:* {pdesc}", ""]
                _render_skills(out, renderer, row.get("attributeList", []) or [],
                               skills_loc, skills_static)
                _render_passives(out, renderer, (row.get("passiveSet", {}) or {}).get("passiveIdList"),
                                 passives_loc)
                total_units += 1

    print(f"stages z falami: {total_stages} | jednostek: {total_units} | bez nazwy: {unnamed}")
    return "\n".join(out).rstrip() + "\n", total_units


def main(argv: list[str] | None = None) -> int:
    import argparse

    from tools.md_table_align import align_markdown_tables

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "local" / "cz_snapshot",
                        help="Localize snapshot: katalog z <lang>/ (default local/cz_snapshot)")
    parser.add_argument("--lang", default="pl")
    parser.add_argument("--out", type=Path, help="default: czytanki/plik_META_<LANG>")
    args = parser.parse_args(argv)
    args.out = args.out or ROOT / "czytanki" / f"plik_META_{args.lang.upper()}"
    args.out.mkdir(parents=True, exist_ok=True)
    suffix = args.lang.upper()
    with Snapshot.open(args.snapshot) as snapshot:
        text, count = build_deployments_file(Texts(snapshot, args.lang), args.lang)
        (args.out / f"06_deployment_{suffix}.md").write_text(align_markdown_tables(text), encoding="utf-8")
    print(f"zapisano 06_deployment_{suffix}.md ({count} jednostek) do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
