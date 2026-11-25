#!/usr/bin/env python3
"""Build readable Identity profiles ("plik ID") for each Sinner.

Joins the game's numeric tables (``StaticData``: Identity stats, skills,
passives) with ``Localize`` texts (names, skill and passive descriptions,
keyword names, the Sinner's file from ``IntroduceCharacter``, Identity voice
lines) into one Markdown file per Sinner, in the layout of the SRW profile
files:

* ``Zakres i zasady odczytu`` (what the numbers mean, what is not shown);
* a catalog table of the Sinner's Identities;
* per Identity: a parameter table (rarity, season, HP, speed per Uptie,
  defense level, resistances, Stagger thresholds, keywords), skills with power
  per Uptie and their texts, passives with requirements, voice lines.

The output contains game text, so it goes to ``local/`` or the owner's Drive,
never to Git.
"""
from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import re
import sys
import unicodedata

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.lcb_text import Texts, one_line, to_markdown
from tools.localize import Snapshot
from tools.static_data import StaticData


ROOT = Path(__file__).resolve().parent.parent
GAME = "Limbus Company"
RANK = {1: "0", 2: "00", 3: "000"}
RESIST = [(2.0, "Fatal"), (1.5, "Weak"), (1.0, "Normal"), (0.5, "Endured"), (0.25, "Ineff."), (0.0, "Immune")]
DEFENSE = {"GUARD": "obrona: blok", "EVADE": "obrona: unik", "COUNTER": "obrona: kontra"}
ATTACK_UI = {"SLASH": "slash", "PENETRATE": "penetrate", "HIT": "hit"}
ATTACK_FALLBACK = {"SLASH": "Slash", "PENETRATE": "Pierce", "HIT": "Blunt"}


def number(value: object) -> str:
    if isinstance(value, float):
        return f"{value:g}".replace(".", ",")
    return str(value)


def signed(value: object) -> str:
    if not isinstance(value, (int, float)):
        return "—"
    return ("+" if value >= 0 else "−") + number(abs(value))


def season(value: object) -> str:
    """Season number; ids above 1000 are events (e.g. 9104 = the Intervallo II event)."""
    if isinstance(value, int) and value >= 1000:
        return f"wydarzenie {value}"
    return "—" if value is None else str(value)


def resist_label(value: object) -> str:
    if not isinstance(value, (int, float)):
        return "—"
    label = next((name for threshold, name in RESIST if value >= threshold), "?")
    return f"×{number(float(value))} ({label})"


def merged_levels(entries: list[dict], key: str = "gaksungLevel") -> list[tuple[int, dict]]:
    """Cumulative per-level data: later entries override only the fields they list."""
    state: dict = {}
    out = []
    for entry in sorted(entries, key=lambda e: e.get(key, 0)):
        state = {**state, **{k: v for k, v in entry.items() if k != key}}
        out.append((entry.get(key, 0), dict(state)))
    return out


def coin_text(coins: list[dict]) -> str:
    if not coins:
        return "—"
    parts = []
    for coin in coins:
        op, scale = coin.get("operatorType", "ADD"), coin.get("scale")
        parts.append({"ADD": signed(scale), "SUB": signed(-scale) if isinstance(scale, (int, float)) else "—"}
                     .get(op, f"{op} {number(scale)}"))
    return parts[0] if len(set(parts)) == 1 else " / ".join(parts)


class Library:
    def __init__(self, static: StaticData, texts: Texts) -> None:
        self.static, self.texts = static, texts
        self.personalities = {row["id"]: row for row in static.rows("personality") if "id" in row}
        self.skills = {row["id"]: row for row in static.rows("skill") if "id" in row}
        self.passive_sets = {row.get("personalityID"): row for row in static.rows("personality-passive")}
        self.passive_rules = {row["id"]: row for row in static.rows("passive") if "id" in row}
        self.names = texts.by_id("Personalities")
        self.skill_texts = texts.by_id("Skills")
        self.passive_texts = texts.by_id("Passives")
        self.characters = texts.by_id("Characters")
        self.intro = {one_line(to_markdown(r.get("name"))): r for r in texts.table("IntroduceCharacter.json")}
        self.sins = {k: one_line(to_markdown(v.get("name"))) for k, v in texts.by_id("AttributeText").items()}
        self.ui = {k: one_line(to_markdown(v.get("content"))) for k, v in texts.by_id("BattleUIText").items()}
        self.voices: dict[int, list[dict]] = {}
        for logical in texts.names():
            path = PurePosixPath(logical)
            if path.parts[0] == "PersonalityVoiceDlg":
                match = re.search(r"_(\d{5})$", path.stem)
                if match:
                    self.voices.setdefault(int(match[1]), []).extend(texts.table(logical))

    def kw(self, text: object) -> str:
        return to_markdown(text, self.texts.keywords)

    def sin(self, key: object) -> str:
        return self.sins.get(str(key), str(key).title() if key else "—")

    def attack(self, key: object) -> str:
        return self.ui.get(ATTACK_UI.get(str(key), ""), "") or ATTACK_FALLBACK.get(str(key), str(key).title())

    def identity_name(self, pid: int) -> tuple[str, str]:
        row = self.names.get(str(pid), {})
        return one_line(to_markdown(row.get("title"))) or str(pid), one_line(to_markdown(row.get("name")))

    def requirement(self, passive_id: int) -> str:
        rule = self.passive_rules.get(passive_id, {})
        parts = []
        for field, label in (("attributeStockCondition", "posiadane"), ("attributeResonanceCondition", "rezonans")):
            for cond in rule.get(field, []) or []:
                parts.append(f"{label} {cond.get('value')}× {self.sin(cond.get('type'))}")
        return ", ".join(parts)

    def skill_section(self, skill_id: int, label: str, out: list[str]) -> None:
        data = self.skills.get(skill_id, {})
        texts = self.skill_texts.get(str(skill_id), {})
        levels = texts.get("levelList", []) or []
        name = one_line(to_markdown(levels[-1].get("name"))) if levels else str(skill_id)
        out += [f"#### {label}: {name}", ""]
        rows = merged_levels(data.get("skillData", []) or [])
        if rows:
            out += ["| Ulepszenie | Grzech | Typ | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |",
                    "|---|---|---|---|---|---|---|---|"]
            previous = None
            for level, state in rows:
                kind = DEFENSE.get(state.get("defType")) if state.get("defType") != "ATTACK" else None
                cells = (self.sin(state.get("attributeType")), kind or self.attack(state.get("atkType")),
                         number(state.get("defaultValue", "—")), coin_text(state.get("coinList", [])),
                         str(len(state.get("coinList", []) or [])), signed(state.get("skillLevelCorrection")),
                         str(state.get("targetNum", "—")))
                if cells != previous:
                    out.append(f"| {level} | " + " | ".join(cells) + " |")
                previous = cells
            out.append("")
        for level in levels:
            lines = []
            desc = self.kw(level.get("desc"))
            if desc:
                lines.append(desc.replace("\n", "  \n"))
            for i, coin in enumerate(level.get("coinlist", []) or [], 1):
                for cd in coin.get("coindescs", []) or []:
                    text = self.kw(cd.get("desc"))
                    if text:
                        lines.append(f"Moneta {i}: {text}".replace("\n", "  \n"))
            if lines:
                prefix = f"*Od ulepszenia {level.get('level')}:* " if len(levels) > 1 else ""
                out += [prefix + "  \n".join(lines), ""]

    def profile(self, pid: int, out: list[str]) -> None:
        row = self.personalities[pid]
        title, name = self.identity_name(pid)
        out += [f"### {RANK.get(row.get('rank'), '?')} {title} — {name}", ""]
        desc = one_line(self.kw(self.names.get(str(pid), {}).get("desc")))
        if desc:
            out += [f"> {desc}", ""]
        hp = row.get("hp", {}) or {}
        speeds = " / ".join(f"{a}–{b}" for a, b in zip(row.get("minSpeedList", []), row.get("maxSpeedList", [])))
        resist = ", ".join(f"{self.attack(r.get('type'))} {resist_label(r.get('value'))}"
                           for r in (row.get("resistInfo", {}) or {}).get("atkResistList", []))
        stagger = " / ".join(f"{v}%" for v in (row.get("breakSection", {}) or {}).get("sectionList", []))
        params = [
            ("Rzadkość", RANK.get(row.get("rank"), str(row.get("rank")))),
            ("Sezon", season(row.get("season"))),
            ("HP", f"{number(hp.get('defaultStat', '—'))} (+{number(hp.get('incrementByLevel', '—'))} za poziom)"),
            ("Szybkość (ulepszenia 1–4)", speeds or "—"),
            ("Poziom obrony", f"poziom {signed(row.get('defCorrection'))}"),
            ("Odporności", resist or "—"),
            ("Progi Stagger (HP)", stagger or "—"),
            ("Grzech wyróżniony", self.sin(row.get("uniqueAttribute"))),
            ("Przynależność", ", ".join(str(a).title() for a in row.get("associationList", [])) or "—"),
            ("Słowa kluczowe", ", ".join(self.texts.keywords.get(k, k) for k in row.get("skillKeywordList", []))
             or "—"),
            ("Data aktualizacji", str(row.get("updatedDate", "—"))),
        ]
        out += ["| Parametr | Wartość bazowa |", "|---|---|"] + [f"| {k} | {v} |" for k, v in params] + [""]
        for i, attr in enumerate(row.get("attributeList", []) or [], 1):
            self.skill_section(attr.get("skillId"), f"Umiejętność {i} (×{attr.get('number')})", out)
        for skill_id in row.get("defenseSkillIDList", []) or []:
            self.skill_section(skill_id, "Obrona", out)
        passives = self.passive_sets.get(pid, {})
        for field, label in (("battlePassiveList", "Pasywka bojowa"), ("supporterPassiveList", "Pasywka wsparcia")):
            for entry in passives.get(field, []) or []:
                for passive_id in entry.get("passiveIDList", []) or []:
                    text = self.passive_texts.get(str(passive_id), {})
                    req = self.requirement(passive_id)
                    head = f"#### {label}: {one_line(to_markdown(text.get('name'))) or passive_id}"
                    meta = [f"od ulepszenia {entry.get('level')}"] + ([req] if req else [])
                    out += [head, "", f"*{'; '.join(meta)}*", "", self.kw(text.get("desc")).replace("\n", "  \n"), ""]
        voices = self.voices.get(pid, [])
        if voices:
            out += ["#### Kwestie", ""]
            for line in voices:
                dlg = to_markdown(line.get("dlg")).replace("\n", " ")
                if dlg:
                    out += [f"- **{one_line(to_markdown(line.get('desc')))}:** {dlg}"]
            out.append("")

    def sinner_file(self, character: int, lang: str) -> tuple[str, str]:
        name = one_line(to_markdown(self.characters.get(str(character), {}).get("name"))) or f"Postać {character}"
        ids = sorted(pid for pid, row in self.personalities.items() if row.get("characterId") == character)
        out = [f"# {GAME} — {name}: Identity", "",
               "*Profil postaci: dane liczbowe z tabel gry, opisy z plików lokalizacji.*", "",
               "## Zakres i zasady odczytu", "",
               f"- Teksty w wersji `{lang}`; liczby z `StaticData` (wartości bazowe, bez E.G.O i bonusów).",
               "- **Ulepszenie** = Uptie (gaksung) 1–4; tabela umiejętności pokazuje tylko wiersze, w których "
               "coś się zmienia. Moc ataku = moc bazowa + moc monety za każdą wyrzuconą reszkę/orła wg reguł gry.",
               "- **Poziom ataku/obrony** to korekta względem poziomu postaci.",
               "- **Odporności**: mnożnik obrażeń danego typu (×2 = Fatal, ×0,5 = Endured).",
               "- Elementy bez opisu w danych są oznaczone „—”, nie zgadywane.", ""]
        intro = self.intro.get(name, {})
        if intro.get("description"):
            out += ["## Akta więźnia", "", "\n".join("> " + l if l.strip() else ">"
                                                     for l in to_markdown(intro["description"]).splitlines()), ""]
        out += ["## Katalog Identity", "", "| Rzadkość | Identity | Sezon | Grzech wyróżniony | Słowa kluczowe |",
                "|---|---|---|---|---|"]
        for pid in ids:
            row = self.personalities[pid]
            title, _ = self.identity_name(pid)
            out.append(f"| {RANK.get(row.get('rank'), '?')} | {title} | {season(row.get('season'))} | "
                       f"{self.sin(row.get('uniqueAttribute'))} | "
                       f"{', '.join(self.texts.keywords.get(k, k) for k in row.get('skillKeywordList', [])) or '—'} |")
        out += ["", "## Profile", ""]
        for pid in ids:
            self.profile(pid, out)
        return name, "\n".join(out).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("static_data", type=Path)
    parser.add_argument("snapshot", type=Path, help="collector ZIP or directory with <lang>/ Localize files")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--out", type=Path, default=ROOT / "local" / "profile")
    parser.add_argument("--only", action="append", type=int, help="character id(s), e.g. 1 = Yi Sang")
    args = parser.parse_args(argv)
    static = StaticData(args.static_data)
    args.out.mkdir(parents=True, exist_ok=True)
    with Snapshot.open(args.snapshot) as snapshot:
        library = Library(static, Texts(snapshot, args.lang))
        characters = sorted({row.get("characterId") for row in library.personalities.values()
                             if isinstance(row.get("characterId"), int)})
        written = 0
        for character in characters:
            if args.only and character not in args.only:
                continue
            name, text = library.sinner_file(character, args.lang)
            ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
            file_name = f"identity_{character:02d}_{re.sub(r'[^A-Za-z0-9]+', '_', ascii_name).strip('_')}_{args.lang.upper()}.md"
            (args.out / file_name).write_text(text, encoding="utf-8")
            written += 1
    print(f"zapisano {written} plików do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
