#!/usr/bin/env python3
"""Deploymenty misji (wzór SRW: ``srwy_mission_deployments.md``) — kto jest
przeciwnikiem w każdej misji, jakie ma statystyki, opisy i zdolności.

Jeden plik ``czytanki/plik_META_<LANG>/06_deployment_<LANG>.md``:

* per część etapów (rodziny z tabel ``enemy``/``abnormality-unit`` StaticData,
  poza proceduralnymi Lustrzanymi Lochami): lista etapów (``StageNode``:
  ``Etap X-Y · tytuł``) i pula przeciwników tej części;
* każdy przeciwnik: tabela statystyk (poziom, HP, szybkość, sloty akcji, progi
  oszołomienia, odporności na typy ataku i grzechy), opis, umiejętności
  (grzech/typ/moc bazowa/moc monety/monety/cele) i pasywki; Anomalie dodatkowo
  łączą jednostkę z częściami (per część HP/odporności);
* walki z Anomaliami o znanych falach (``battle-ab`` → ``waveList``) pod etapem.

Liczby pochodzą z ``index/static-data`` (``enemy``, ``abnormality-unit``,
``abnormality-part``, ``skill``, ``battle-ab``), nazwy i opisy z ``Localize``
(``Enemies*``, ``Skills_Enemy*``/``Skills_Abnormality*``, ``Passives_*``).
Wersja PL korzysta z pakietu ``Lang/Polski`` (fallback EN wbudowany per wpis).
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

# Rodziny proceduralne (Lustrzane Lochy i pochodne) — poza zakresem misji.
EXCLUDED = ("mirrordungeon", "schema-craft", "shadowenemy")

STORY_PART = re.compile(r"^a1c(\d+)p(\d+)$")

L = {
    "pl": {
        "title": "Deploymenty misji (przeciwnicy)",
        "intro": ("Przeciwnicy każdej misji: pula wrogów części etapów (tabele ``enemy`` i"
                  " ``abnormality-unit`` z StaticData), statystyki, opisy, umiejętności i"
                  " pasywki; fale walk z Anomaliami z tabel ``battle-ab``. Nazwy części"
                  " (np. ``a1c5p1``) to identyfikatory danych gry."),
        "reader": ("**Uwaga dla czytelnika:** liczby z tabel StaticData (wartości bazowe);"
                   " teksty w wersji polskiej — wpisy bez przekładu pozostają w oryginale"
                   " (angielskim)."),
        "scope": "Zakres i zasady odczytu",
        "stages": "Etapy",
        "skills": "Umiejętności",
        "skill": "Umiejętność",
        "passives": "Pasywki",
        "parts": "Części (anatomia)",
        "waves": "Walki z Anomaliami — znane fale",
        "wave": "Fala {n}",
        "untranslated": "Wpisów bez przekładu (fallback EN): {n}.",
        "params": "Parametr",
        "value": "Wartość",
    },
    "en": {
        "title": "Mission deployments (enemies)",
        "intro": ("Every mission's enemies: the enemy pool of each stage part (`enemy` and"
                  " `abnormality-unit` StaticData tables) with stats, descriptions, skills"
                  " and passives; known Abnormality battle waves from `battle-ab`. Part"
                  " names (e.g. `a1c5p1`) are the game's data identifiers."),
        "reader": ("**Reader's note:** numbers from the StaticData tables (base values);"
                   " texts follow the reading edition's language."),
        "scope": "Scope and reading notes",
        "stages": "Stages",
        "skills": "Skills",
        "skill": "Skill",
        "passives": "Passives",
        "parts": "Parts (anatomy)",
        "waves": "Abnormality battles — known waves",
        "wave": "Wave {n}",
        "untranslated": "Entries without a translation (EN fallback): {n}.",
        "params": "Parameter",
        "value": "Value",
    },
}

RESIST_MAP = {2.0: "Fatal", 1.5: "Weak", 0.75: "Endured", 0.5: "Ineff.", 0.25: "Ineff.", 0.0: "Immune"}


def _t(lang: str) -> dict[str, str]:
    return L.get(lang, L["en"])


def _family_of(stem: str, prefix: str) -> str:
    """``enemy-a1c5p1`` → ``a1c5p1``; ``enemy91-4`` → ``91-4``; ``enemy`` → ``common``."""
    leaf = stem[len(prefix):]
    if leaf.startswith("-"):
        leaf = leaf[1:]
    return leaf or "common"


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


def _ordered(families: dict[str, dict]) -> list[str]:
    def key(fam: str):
        match = STORY_PART.match(fam)
        if match:
            return (0, int(match.group(1)), int(match.group(2)), fam)
        if fam == "common":
            return (-1, 0, 0, fam)
        return (1, 0, 0, fam)

    return sorted(families, key=key)


def _part_sort_key(fam: str) -> tuple:
    match = STORY_PART.match(fam)
    if match:
        return (0, int(match.group(1)), int(match.group(2)), fam)
    if fam == "common":
        return (-1, 0, 0, fam)
    return (1, 0, 0, fam)


class Renderer:
    """Etykiety grzechów/ataków z Localize + renderery statystyk."""

    def __init__(self, texts: Texts, lang: str) -> None:
        self.texts = texts
        self.lang = lang
        self.lbl = _t(lang)
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
                note = RESIST_MAP.get(float(value), "")
                parts.append(f"{label} ×{number(value)}" + (f" ({note})" if note else ""))
        return "; ".join(parts) or "wszystkie ×1 (Normal)"

    def stats_table(self, row: dict, part: bool = False) -> list[str]:
        hp = row.get("hp", {}) or {}
        out = [f"| {self.lbl['params']} | {self.lbl['value']} |", "|---|---|"]
        out.append(f"| Poziom | {number(row.get('level', '—'))} |")
        out.append(f"| HP | {number(hp.get('defaultStat', '—'))} (+{number(hp.get('incrementByLevel', '—'))} za poziom) |")
        speeds = " / ".join(f"{a}–{b}" for a, b in zip(row.get("minSpeedList", []) or [],
                                                       row.get("maxSpeedList", []) or []))
        if speeds:
            out.append(f"| Szybkość | {speeds} |")
        if not part:
            starts = row.get("startActionSlotNumList")
            if starts:
                out.append(f"| Sloty akcji | start: {'/'.join(str(s) for s in starts)}"
                           f" · maks. {number(row.get('maxActionSlotNum', '—'))} |")
            else:
                out.append(f"| Sloty akcji | start: {number(row.get('startActionSlotNum', '—'))}"
                           f" · maks. {number(row.get('maxActionSlotNum', '—'))} |")
        stagger = " / ".join(f"{v}%" for v in (row.get("breakSection", {}) or {}).get("sectionList", []))
        if stagger:
            out.append(f"| Progi oszołomienia | {stagger} |")
        out.append(f"| Odporności | {self.resists(row.get('resistInfo', {}) or {})} |")
        return out


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
                   skills_loc: dict[int, list], skills_static: dict[int, dict],
                   lbl: dict[str, str]) -> None:
    shown = 0
    for entry in ids_numbers:
        sid = entry.get("skillId")
        if sid is None or int(sid) <= 0:
            continue
        number_of = entry.get("number", 1)
        levels = skills_loc.get(int(sid), []) or []
        name = one_line(to_markdown(levels[-1].get("name"))) if levels else f"umiejętność {sid}"
        count_note = f" (×{number_of})" if number_of and number_of != 1 else ""
        out += [f"#### {lbl['skill']}: {name}{count_note} — id {sid}", ""]
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
        out += [f"*Brak danych o umiejętnościach.*", ""]


def _render_passives(out: list[str], renderer: Renderer, passive_ids: list,
                     passives_loc: dict[int, dict], lbl: dict[str, str]) -> None:
    lines = []
    for pid in passive_ids or []:
        row = passives_loc.get(int(pid))
        if not row:
            continue
        name = one_line(to_markdown(row.get("name")))
        desc = renderer.kw(row.get("desc"))
        lines.append(f"- **{name or pid}** — {desc}" if desc else f"- **{name or pid}**")
    if lines:
        out += [f"**{lbl['passives']}:**", ""]
        out += lines
        out.append("")


def _stage_list(texts: Texts, fam: str) -> tuple[str, list[str]]:
    """Nagłówek zakresu etapów + lista ``Etap X-Y · tytuł``."""
    name = f"StageNode-{fam}.json"
    if name not in texts.snapshot.files[texts.lang]:
        return "", []
    rows = texts.table(name)
    entries = []
    for row in sorted(rows, key=lambda r: int(r.get("id", 0) or 0)):
        label = stage_label(int(row.get("id", 0) or 0))
        title = one_line(to_markdown(row.get("title")))
        entries.append(f"{label or row.get('id')}" + (f" · {title}" if title else ""))
    if not entries:
        return "", []
    first, last = entries[0], entries[-1]
    first_label = first.split(" · ")[0]
    last_label = last.split(" · ")[0]
    return f"{first_label} … {last_label}", entries


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
    lbl = _t(lang)
    static = StaticData(ROOT / "index" / "static-data")
    renderer = Renderer(texts, lang)
    families = _families(static)
    skills_static = _skill_static(static)
    enemies_loc, skills_loc, passives_loc = _enemy_text_maps(texts)

    out = [
        f"# {GAME} — {lbl['title']}",
        "",
        lbl["reader"],
        "",
        lbl["intro"],
        "",
        f"## {lbl['scope']}",
        "",
        "- **HP** = wartość bazowa (+ przyrost za każdy poziom wroga); **szybkość** = zakres"
        " inicjatywy na ulepszenia 1–4; **sloty akcji** = liczba żetonów na początek i maksimum.",
        "- **Progi oszołomienia** = odsetek HP łamiący kolejne sekcje stabilności.",
        "- **Odporności** = mnożniki obrażeń; przy braku wpisu mnożnik wynosi ×1 (Normal);"
        " skróty: Fatal ×2, Weak ×1,5, Endured ×0,75, Ineff. ×0,5, Immune ×0.",
        "- Nazwa części etapów (np. `a1c5p1`) to identyfikator danych gry; pula wroga jest"
        " wspólna dla etapów tej części — dokładne fale zwykłych etapów nie są częścią"
        " danych StaticData (znane fale walk z Anomaliami pochodzą z tabel `battle-ab`).",
        f"- {lbl['untranslated'].format(n=_count_untranslated(texts, lang, enemies_loc))}",
        "",
    ]

    total = 0
    for fam in _ordered(families):
        scope, stages = _stage_list(texts, fam)
        heading = f"Część `{fam}`" if fam != "common" else "Zestaw wspólny (`enemy.json`)"
        if scope:
            heading += f" — Etapy {scope}"
        out += [f"## {heading}", ""]
        if stages:
            out += [f"**{lbl['stages']}:** " + " · ".join(stages), ""]

        enemy_rel = f"enemy/enemy-{fam}.json" if fam != "common" else "enemy/enemy.json"
        # zwykli wrogowie części
        for row in sorted(_rows_file(static, enemy_rel), key=lambda r: int(r.get("id", 0) or 0)):
            eid = int(row.get("id", 0) or 0)
            loc = enemies_loc.get(eid, {})
            name = one_line(to_markdown(loc.get("name"))) or f"wrogowie id {eid}"
            out += [f"### {name} — id {eid}", ""]
            out += renderer.stats_table(row)
            out.append("")
            desc = renderer.kw(loc.get("desc"))
            if desc:
                out += [f"*Opis:* {desc}", ""]
            _render_skills(out, renderer, row.get("attributeList", []) or [],
                           skills_loc, skills_static, lbl)
            _render_passives(out, renderer, (row.get("passiveSet", {}) or {}).get("passiveIdList"),
                             passives_loc, lbl)
            total += 1

        # anomalie części
        if families[fam].get("abnormality"):
            unit_rel = f"abnormality-unit/abnormality-unit-{fam}.json" if fam != "common" else \
                "abnormality-unit/abnormality-unit.json"
            part_rel = f"abnormality-part/abnormality-part-{fam}.json" if fam != "common" else \
                "abnormality-part/abnormality-part.json"
            parts_static = {int(r["id"]): r for r in _rows_file(static, part_rel) if "id" in r}
            for row in sorted(_rows_file(static, unit_rel), key=lambda r: int(r.get("id", 0) or 0)):
                uid = int(row.get("id", 0) or 0)
                loc = enemies_loc.get(uid, {})
                name = one_line(to_markdown(loc.get("name"))) or f"anomalia id {uid}"
                klass = row.get("classType")
                sin_label = renderer.sin(row.get("attributeType"))
                meta = " · ".join(x for x in [f"klasa {klass}" if klass else "",
                                              f"grzech {sin_label}" if sin_label else ""] if x)
                out += [f"### {name} — id {uid}" + (f" ({meta})" if meta else ""), ""]
                out += renderer.stats_table(row)
                out.append("")
                desc = renderer.kw(loc.get("desc"))
                if desc:
                    out += [f"*Opis:* {desc}", ""]
                raw_parts = row.get("abnormalityPartList", []) or []
                part_ids = [int(p if isinstance(p, (int, float)) else p.get("id", 0) or 0) for p in raw_parts]
                if part_ids:
                    out += [f"**{lbl['parts']}:**", ""]
                    for pid in part_ids:
                        prow = parts_static.get(pid, {})
                        ploc = enemies_loc.get(pid, {})
                        pname = one_line(to_markdown(ploc.get("name"))) or f"część id {pid}"
                        out += [f"#### {pname} — id {pid}", ""]
                        if prow:
                            out += renderer.stats_table(prow, part=True)
                            out.append("")
                        pdesc = renderer.kw(ploc.get("desc"))
                        if pdesc:
                            out += [f"*Opis:* {pdesc}", ""]
                _render_skills(out, renderer, row.get("attributeList", []) or [],
                               skills_loc, skills_static, lbl)
                _render_passives(out, renderer, (row.get("passiveSet", {}) or {}).get("passiveIdList"),
                                 passives_loc, lbl)
                total += 1

    # znane fale walk z Anomaliami (battle-ab → waveList)
    waves: dict[int, list[dict]] = {}
    for row in static.rows("battle-ab"):
        sid = row.get("id")
        if row.get("waveList") and sid:
            waves.setdefault(int(sid), []).extend(row["waveList"])
    if waves:
        out += [f"## {lbl['waves']}", ""]
        for sid in sorted(waves):
            label = stage_label(sid) or str(sid)
            out += [f"### Etap {label}", ""]
            for wi, wave in enumerate(waves[sid], 1):
                units = []
                for bucket, tag in (("unitList", ""), ("subUnitList", " (wsparcie)")):
                    for unit in wave.get(bucket, []) or []:
                        uid = int(unit.get("unitID", 0) or 0)
                        loc = enemies_loc.get(uid, {})
                        uname = one_line(to_markdown(loc.get("name"))) or f"jednostka {uid}"
                        level = unit.get("unitLevel")
                        units.append(f"{uname} ×{unit.get('unitCount', 1)}"
                                     + (f" (poz. {level})" if level is not None else "") + tag)
                out += [f"- **{lbl['wave'].format(n=wi)}:** " + ("; ".join(units) or "—")]
            out.append("")

    return "\n".join(out).rstrip() + "\n", total


def main(argv: list[str] | None = None) -> int:
    import argparse

    from tools.localize import Snapshot as _Snapshot
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
    with _Snapshot.open(args.snapshot) as snapshot:
        text, count = build_deployments_file(Texts(snapshot, args.lang), args.lang)
        (args.out / f"06_deployment_{suffix}.md").write_text(align_markdown_tables(text), encoding="utf-8")
    print(f"zapisano 06_deployment_{suffix}.md ({count} jednostek) do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
