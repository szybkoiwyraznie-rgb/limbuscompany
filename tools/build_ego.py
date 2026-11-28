#!/usr/bin/env python3
"""Build readable E.G.O profiles ("plik E.G.O") for each Sinner.

Joins the game's numeric tables (``StaticData``: ``skill/ego-skill-*`` with
``skillType`` ``EGO_AWAKEN``/``EGO_EROSION``, ``passive/passive-ego``) with
``Localize`` texts (card names and subtitles from ``Egos``, skill texts from
``Skills_Ego``, passives from ``Passive_Ego``, E.G.O voice lines from
``EGOVoiceDig``) into one Markdown file per Sinner, in the layout of the
Identity profile files (``tools/build_profiles.py``):

* ``Zakres i zasady odczytu`` (what the numbers mean, what is not shown);
* a catalog table of the Sinner's E.G.O cards;
* per card: the subtitle, the Awakening skill with power per Uptie and its
  coin texts, the Erosion skill when the card has one, the passive with its
  awakening requirement, and the card's voice lines.

Output: ``czytanki/plik_EGO_<LANG>/`` (Markdown, versioned in Git like the
source texts in ``index/``).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_profiles import coin_text, merged_levels, number, season, signed
from tools.lcb_text import Texts, one_line, to_markdown
from tools.md_table_align import align_markdown_tables
from tools.localize import Snapshot
from tools.static_data import StaticData


ROOT = Path(__file__).resolve().parent.parent
GAME = "Limbus Company"
REQUIRE_LABELS = {
    "CheckAwakenLevel2": "przebudzenie E.G.O na poziomie 2",
    "CheckAwakenLevel3": "przebudzenie E.G.O na poziomie 3",
    "CheckAwakenLevel4": "przebudzenie E.G.O na poziomie 4",
    "CheckAwakenLevelBetween_2_4": "przebudzenie E.G.O na poziomie 2–4",
    "CheckErosionLevel1": "erozja E.G.O na poziomie 1",
}


def require_text(code: str) -> str:
    return REQUIRE_LABELS.get(code, code)


class Library:
    def __init__(self, static: StaticData, texts: Texts) -> None:
        self.static, self.texts = static, texts
        self.cards = {row["id"]: row for row in texts.by_id("Egos").values() if "id" in row}
        self.skill_texts = texts.by_id("Skills_Ego")
        self.passive_texts = texts.by_id("Passive_Ego")
        ego_ids = {str(k) for k in self.skill_texts}
        self.skills = {row["id"]: row for row in static.rows("skill") if str(row.get("id")) in ego_ids}
        self.characters = texts.by_id("Characters")
        self.sins = {k: one_line(to_markdown(v.get("name"))) for k, v in texts.by_id("AttributeText").items()}
        self.ui = {k: one_line(to_markdown(v.get("content"))) for k, v in texts.by_id("BattleUIText").items()}
        # E.G.O voice lines: EGOVoiceDig/Voice_EGO_<Name>_<char>.json, ids like
        # battle_awaken_<card>_1 / battle_erosion_<card>_1.
        self.voices: dict[int, list[dict]] = {}
        for logical in texts.names():
            match = re.match(r"EGOVoiceDig/Voice_EGO_\w+_(\d+)\.json$", logical)
            if match:
                self.voices.setdefault(int(match[1]), []).extend(texts.table(logical))
        for group in self.voices.values():
            group.sort(key=lambda row: str(row.get("id", "")))

    def kw(self, text: object) -> str:
        return to_markdown(text, self.texts.keywords)

    def sin(self, key: object) -> str:
        return self.sins.get(str(key), str(key).title() if key else "—")

    def attack(self, key: object) -> str:
        return self.ui.get(str(key), "") or str(key).title()

    def card_ids(self, character: int) -> list[int]:
        """E.G.O card ids of one Sinner; ``20101`` → digits ``20|01|01`` → Sinner 1, ``21201`` → Sinner 12."""
        ids = []
        for card_id in self.cards:
            digits = str(card_id)
            if len(digits) == 5 and digits.startswith("2") and int(digits[1:3]) == character:
                ids.append(card_id)
        return sorted(ids)

    def ego_section(self, skill_id: int, label: str, out: list[str]) -> None:
        data = self.skills.get(skill_id, {})
        texts = self.skill_texts.get(str(skill_id), {})
        levels = texts.get("levelList", []) or []
        name = one_line(to_markdown(levels[0].get("name"))) if levels else str(skill_id)
        out += [f"#### {label}: {name}", ""]
        rows = merged_levels(data.get("skillData", []) or [])
        if rows:
            out += ["| Ulepszenie | Grzech | Typ | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |",
                    "|---:|---|---|---:|---:|---:|---:|---:|"]
            previous = None
            for level, state in rows:
                cells = (self.sin(state.get("attributeType")), self.attack(state.get("atkType")),
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

    def card(self, card_id: int, out: list[str]) -> None:
        card = self.cards[card_id]
        name = one_line(to_markdown(card.get("name"))) or str(card_id)
        subtitle = one_line(to_markdown(card.get("desc")))
        out += [f"### {name}", ""]
        if subtitle:
            out += [f"*{subtitle}*", ""]
        skill_ids = sorted(sid for sid in self.skills if str(sid).startswith(str(card_id)))
        for sid in skill_ids:
            label = {"11": "Przebudzenie", "21": "Erozja"}.get(str(sid)[-2:], "Wariant")
            self.ego_section(sid, label, out)
        passive = self.passive_texts.get(str(card_id), {})
        if passive.get("desc"):
            requires = [require_text(code) for code in self.skills.get(skill_ids[0], {}).get("requireIDList", []) or []]
            out += [f"#### Pasywka: {one_line(to_markdown(passive.get('name'))) or card_id}", ""]
            if requires:
                out += [f"*Wymagania: {'; '.join(requires)}*", ""]
            out += [self.kw(passive.get("desc")).replace("\n", "  \n"), ""]

    def voice_section(self, character: int, out: list[str]) -> None:
        lines = self.voices.get(character, [])
        if not lines:
            return
        out += ["## Kwestie E.G.O", ""]
        for line in lines:
            dlg = to_markdown(line.get("dlg")).replace("\n", " ")
            if dlg:
                out.append(f"- **{one_line(to_markdown(line.get('desc'))) or '—'}:** {dlg}")
        out.append("")

    def sinner_file(self, character: int, lang: str) -> tuple[str, str]:
        name = one_line(to_markdown(self.characters.get(str(character), {}).get("name"))) or f"Grzesznik {character}"
        ids = self.card_ids(character)
        out = [f"# {GAME} — {name}: E.G.O", "",
               "*Profil postaci: dane liczbowe z tabel gry, opisy z plików lokalizacji.*", "",
               "## Zakres i zasady odczytu", "",
               f"- Teksty w wersji `{lang}`"
               + ("; wpisy bez przekładu pozostają w oryginale (angielskim)" if lang == "pl" else "")
               + "; liczby z `StaticData` (wartości bazowe, bez bonusów Klas Mirroringu).",
               "- **Przebudzenie** = zwykłe użycie karty E.G.O, **Erozja** = forma po przekroczeniu progu SP "
               "(jeżeli karta ją ma).",
               "- **Ulepszenie** = Uptie E.G.O (1/3/4); tabela pokazuje tylko wiersze, w których coś się zmienia.",
               "- **Odporności/progi** karty nie są tu pokazywane — karta E.G.O dzieli statystyki z Identity.",
               "- Elementy bez opisu w danych są oznaczone „—”, nie zgadywane.", ""]
        if ids:
            out += ["## Katalog E.G.O", "",
                    "| Karta | Podtytuł |", "|---|---|"]
            for card_id in ids:
                card = self.cards[card_id]
                title = one_line(to_markdown(card.get("name"))) or str(card_id)
                subtitle = one_line(to_markdown(card.get("desc"))) or "—"
                out.append(f"| {title} | {subtitle} |")
            out += ["", "## Karty", ""]
            for card_id in ids:
                self.card(card_id, out)
        self.voice_section(character, out)
        text = "\n".join(out).rstrip() + "\n"
        # Gra dopisuje adnotacje po tokenach („[Motyl](Żyjącego)”); łamiemy
        # sąsiedztwo „](”, by markdown nie czytał tego jako linku.
        return name, text.replace("](", "] (")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("static_data", type=Path, nargs="?", default=ROOT / "index" / "static-data",
                        help="static-data tables (default: index/static-data)")
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "index" / "localize",
                        help="Localize: index/localize (default), a collector ZIP or a directory with <lang>/")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--out", type=Path, help="default: czytanki/plik_EGO_<LANG>")
    parser.add_argument("--only", action="append", type=int, help="character id(s), e.g. 1 = Yi Sang")
    args = parser.parse_args(argv)
    static = StaticData(args.static_data)
    args.out = args.out or ROOT / "czytanki" / f"plik_EGO_{args.lang.upper()}"
    args.out.mkdir(parents=True, exist_ok=True)
    with Snapshot.open(args.snapshot) as snapshot:
        library = Library(static, Texts(snapshot, args.lang))
        characters = sorted({int(str(card_id)[1:3]) for card_id in library.cards})
        written = 0
        for character in characters:
            if args.only and character not in args.only:
                continue
            name, text = library.sinner_file(character, args.lang)
            ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
            file_name = f"ego_{character:02d}_{re.sub(r'[^A-Za-z0-9]+', '_', ascii_name).strip('_')}_{args.lang.upper()}.md"
            (args.out / file_name).write_text(align_markdown_tables(text), encoding="utf-8")
            written += 1
    print(f"zapisano {written} plików do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
