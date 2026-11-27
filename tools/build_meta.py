#!/usr/bin/env python3
"""Build the "meta" Czytanka (``plik META``) — elements outside the three main
Czytanka groups (fabula / plik ID / plik E.G.O):

* in-mission tutorial texts (``TutorialRenewalDesc`` grouped by the stage that
  shows them, ``TutorialRenewalMainUIDesc`` stage ``10108`` → Etap 1-8);
* UI tutorials shown outside missions (EXP dungeons, lobby, Mirror Dungeon,
  Identity/E.G.O info tour);
* in-battle hints (``BattleHint``, ``BattleHint_NormalBattle``,
  ``BattleHint_AbnorBattle``) and tutorial pop-ups (``TutorialPopUpDesc``);
* Dante's Notes (``StoryTheaterDanteNote*`` keywords + ``*Detail*`` first-person
  wiki entries);
* the patch-download splash screens (``FileDownloadDesc``);
* the twelve Sinner introductions (``IntroduceCharacter`` descriptions with
  names from ``Characters``).

Output: ``czytanki/plik_META_<LANG>/`` (Markdown, versioned in Git like the
other Czytanki series). Stage titles come from ``StageNode`` (``10001`` →
Etap 0-1 via ``lcb_text.stage_label``).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.lcb_text import Texts, stage_label, to_markdown
from tools.localize import Snapshot
from tools.md_table_align import align_markdown_tables


ROOT = Path(__file__).resolve().parent.parent
GAME = "Limbus Company"

TOUR_NAMES = {
    "tuto_exp_mining": "Lochy Wydobywcze (PD)",
    "tuto_lobby_at_start": "Lobby — kontynuacja opowieści",
    "tuto_mirror_dungeon": "Lustrzane Lochy",
    "tuto_personality_ego_info": "Tożsamości i E.G.O — przegląd informacji",
}
RENEWAL_ID = re.compile(r"^tuto_(\d+)_(\d+)_(\d+)_(\d+)$")
MAINUI_STAGE_ID = re.compile(r"^tuto_(\d+)_(\d+)$")
HINT_FILES = [
    ("BattleHint.json", "Ogólne"),
    ("BattleHint_NormalBattle.json", "Zwykłe walki"),
    ("BattleHint_AbnorBattle.json", "Walki z Anomaliami"),
]

# Minimal reader-facing labels; the series is produced for Polish, English
# labels keep EN/KR builds readable.
L = {
    "pl": {
        "meta": "Elementy spoza głównej fabuły (tutorial, encyklopedia, akta)",
        "reader": ("**Uwaga dla czytelnika:** tekst w wersji polskiej; układ sekcji odzwierciedla"
                   " kolejność z danych gry (`index/` + przekład w `tlumaczenie/`)."),
        "missions": "Teksty pokazywane w misjach",
        "place": "Miejsce",
        "ui_in_stage": "*(opisy interfejsu pokazywane w tym etapie)*",
        "tours": "Poradniki poza misjami",
        "hints": "Wskazówki w walce",
        "popups": "Okna pop-up tutoriali",
        "fallback": "Wpisy bez przekładu pozostają w oryginale (angielskim).",
        "notes_kw": "Hasła (glosariusz świata)",
        "notes_kw_set": "Hasła — zestaw {n}",
        "notes_detail": "Zapiski Dantego (pełne wpisy)",
        "notes_detail_set": "Zapiski — zestaw {n}",
        "splashes": "Splashe pobierania patcha",
        "sinners": "Akta Grzeszników (introdukcje)",
        "sinner": "Grzesznik #{n} — {name}",
        "spis": "„Plik META” — spis serii",
        "file": "Plik",
        "content": "Zawartość",
        "items": "Wpisów",
    },
    "en": {
        "meta": "Elements outside the main story (tutorial, encyclopedia, dossiers)",
        "reader": ("**Reader's note:** section layout mirrors the game's data order (`index/` sources"
                   " + the translation store in `tlumaczenie/`)."),
        "missions": "Texts shown during missions",
        "place": "Place",
        "ui_in_stage": "*(interface descriptions shown in this stage)*",
        "tours": "Tutorials outside missions",
        "hints": "In-battle hints",
        "popups": "Tutorial pop-up windows",
        "fallback": "Entries without a translation remain in the original (English).",
        "notes_kw": "Keywords (world glossary)",
        "notes_kw_set": "Keywords — set {n}",
        "notes_detail": "Dante's Notes (full entries)",
        "notes_detail_set": "Notes — set {n}",
        "splashes": "Patch-download splash screens",
        "sinners": "Sinner dossiers (introductions)",
        "sinner": "Sinner #{n} — {name}",
        "spis": "\"META file\" — series contents",
        "file": "File",
        "content": "Contents",
        "items": "Entries",
    },
}


def _t(texts: Texts, lang: str) -> dict[str, str]:
    return L.get(lang, L["en"])


def _para(text: str) -> str:
    """One readable paragraph: hard line breaks inside, markup already gone."""
    return text.replace("\n", "  \n").strip()


def _quote(text: str) -> str:
    lines = [ln.strip() for ln in text.split("\n")]
    return "\n".join(f"> {ln}".rstrip() for ln in lines)


def _set_files(texts: Texts, stem: str, exclude: str | None = None) -> list[tuple[int, str]]:
    """Logical file names ``<stem>[.json|_<N>.json]`` in numeric order; base = set 1."""
    names = []
    for name in texts.names():
        if "/" in name or not name.startswith(stem):
            continue
        leaf = name[:-5]  # strip .json
        if exclude and leaf.startswith(exclude):
            continue
        suffix = leaf[len(stem):]
        match = re.fullmatch(r"_(\d+)", suffix)
        if suffix and not match:
            continue
        names.append((int(match.group(1)) if match else 1, name))
    return sorted(set(names))


def _rows(texts: Texts, name: str) -> list[dict]:
    return texts.table(name) if name in texts.snapshot.files[texts.lang] else []


# ---------------------------------------------------------------- file 01


def _mission_groups(texts: Texts) -> dict[int, dict[str, list[tuple[str, str]]]]:
    """Stage node → ``{"stage": [(id, content)], "ui": [(id, content)]}``."""
    nodes: dict[int, dict[str, list[tuple[str, str]]]] = {}
    for row in _rows(texts, "TutorialRenewalDesc.json"):
        match = RENEWAL_ID.match(str(row.get("id", "")))
        if not match:
            continue
        chapter, stage = int(match.group(1)), int(match.group(2))
        node = 10000 + chapter * 100 + stage
        nodes.setdefault(node, {"stage": [], "ui": []})["stage"].append(
            (str(row.get("id")), to_markdown(row.get("content"), texts.keywords)))
    for row in _rows(texts, "TutorialRenewalMainUIDesc.json"):
        match = MAINUI_STAGE_ID.match(str(row.get("id", "")))
        if not match:
            continue
        num = match.group(1)
        if len(num) == 5 and num[0] == "1":
            node = int(num)
            nodes.setdefault(node, {"stage": [], "ui": []})["ui"].append(
                (str(row.get("id")), to_markdown(row.get("content"), texts.keywords)))
    return nodes


def build_mission_file(texts: Texts, lang: str) -> tuple[str, int]:
    lbl = _t(texts, lang)
    out = [
        f"# {GAME} — Teksty z misji (tutorial bojowy)",
        "",
        f"{lbl['reader']}",
        "",
        "Teksty tutoriali bojowych pokazywane w trakcie etapów fabularnych"
        " (`TutorialRenewalDesc`, `TutorialRenewalMainUIDesc`), wskazówki w walce"
        " (`BattleHint*`) oraz okna pop-up tutoriali (`TutorialPopUpDesc`)."
        " Nagłówki etapów pochodzą z tabel `StageNode`.",
        "",
        f"## {lbl['missions']}",
        "",
    ]
    stages = texts.by_id("StageNode")
    groups = _mission_groups(texts)
    for node in sorted(groups):
        data = groups[node]
        stage = stages.get(str(node), {})
        title = to_markdown(stage.get("title"))
        heading = f"Etap {stage_label(node)}"
        if title:
            heading += f" · {title}"
        out += [f"### {heading}", ""]
        place = to_markdown(stage.get("place"))
        if place:
            out += [f"*{lbl['place']}: {place}*", ""]
        for _, content in sorted(data["stage"]):
            if content:
                out += [_para(content), ""]
        if data["ui"]:
            out += [lbl["ui_in_stage"], ""]
            for _, content in sorted(data["ui"]):
                if content:
                    out += [_para(content), ""]
    if not groups:
        out = out[: out.index(f"## {lbl['missions']}") + 1]
    out += [f"## {lbl['tours']}", ""]
    tours: dict[str, list[str]] = {}
    for row in _rows(texts, "TutorialRenewalMainUIDesc.json"):
        match = re.match(r"^tuto_([a-z_]+?)_(\d+)$", str(row.get("id", "")))
        if not match:
            continue
        content = to_markdown(row.get("content"), texts.keywords)
        if content:
            tours.setdefault(match.group(1), []).append(content)
    for stem, items in sorted(tours.items()):
        out += [f"### {TOUR_NAMES.get(f'tuto_{stem}', stem)}", ""]
        out += [_para(c) for c in items]
        out.append("")
    out += [f"## {lbl['hints']}", ""]
    for name, title in HINT_FILES:
        rows = _rows(texts, name)
        if not rows:
            continue
        out += [f"### {title}", ""]
        for row in sorted(rows, key=lambda r: str(r.get("id", ""))):
            content = to_markdown(row.get("content"), texts.keywords)
            if content:
                out += [_para(content), ""]
    popups: dict[str, dict[str, list[str]]] = {}
    for row in _rows(texts, "TutorialPopUpDesc.json"):
        key = str(row.get("id", ""))
        match = re.match(r"^(.*?)_(title|\d+)$", key)
        if not match:
            continue
        content = to_markdown(row.get("content"), texts.keywords)
        if not content:
            continue
        popups.setdefault(match.group(1), {"title": [], "items": []})
        popups[match.group(1)]["title" if match.group(2) == "title" else "items"].append(content)
    if popups:
        out += [f"## {lbl['popups']}", ""]
        for stem in sorted(popups):
            group = popups[stem]
            title = group["title"][0] if group["title"] else stem
            out += [f"### {title}", ""]
            for item in sorted(group["items"]):
                out += [_para(item), ""]
    count = (sum(len(g["stage"]) + len(g["ui"]) for g in groups.values())
             + sum(len(v) for v in tours.values())
             + sum(len(_rows(texts, name)) for name, _ in HINT_FILES)
             + sum(len(g["items"]) for g in popups.values()))
    return "\n".join(out).rstrip() + "\n", count


# ---------------------------------------------------------------- file 02


def build_notes_file(texts: Texts, lang: str) -> tuple[str, int]:
    lbl = _t(texts, lang)
    out = [
        f"# {GAME} — Notatki Dantego (encyklopedia świata)",
        "",
        lbl["reader"],
        "",
        "Hasła odsyłaczowe encyklopedii Dantego (`StoryTheaterDanteNote*`) oraz"
        " pełne wpisy w pierwszoosobowym stylu zapisków (`StoryTheaterDanteNoteDetail*`)."
        f" {lbl['fallback']}",
        "",
        f"## {lbl['notes_kw']}",
        "",
    ]
    kw_total = 0
    for n, name in _set_files(texts, "StoryTheaterDanteNote", exclude="StoryTheaterDanteNoteDetail"):
        out += [f"### {lbl['notes_kw_set'].format(n=n)}", ""]
        count = 0
        for row in sorted(texts.table(name), key=lambda r: str(r.get("id", ""))):
            word = to_markdown(row.get("content"), texts.keywords)
            if word:
                out.append(f"- **{word}**")
                count += 1
        kw_total += count
        out.append("")
    out += [f"## {lbl['notes_detail']}", ""]
    entry_total = 0
    for n, name in _set_files(texts, "StoryTheaterDanteNoteDetail"):
        out += [f"### {lbl['notes_detail_set'].format(n=n)}", ""]
        for row in sorted(texts.table(name), key=lambda r: int(re.sub(r"\D", "", str(r.get("id", ""))) or 0)):
            content = to_markdown(row.get("desc"), texts.keywords)
            if content:
                out += [_quote(content), ""]
                entry_total += 1
    if not kw_total and not entry_total:
        return "", 0
    return "\n".join(out).rstrip() + "\n", kw_total + entry_total


# ---------------------------------------------------------------- file 03


def build_splash_file(texts: Texts, lang: str) -> tuple[str, int]:
    lbl = _t(texts, lang)
    out = [
        f"# {GAME} — Splashe pobierania patcha",
        "",
        lbl["reader"],
        "",
        "Teksty z lore Miasta pokazywane podczas pobierania patcha"
        " (`FileDownloadDesc`: tytuł + opis każdego ekranu).",
        "",
        f"## {lbl['splashes']}",
        "",
    ]
    groups: dict[str, dict[str, str]] = {}
    for row in _rows(texts, "FileDownloadDesc.json"):
        match = re.match(r"^(FileDownload_Desc_\d+)", str(row.get("id", "")))
        if not match:
            continue
        groups.setdefault(match.group(1), {})
        for field in ("title", "desc"):
            content = to_markdown(row.get(field), texts.keywords)
            if content:
                groups[match.group(1)].setdefault(field, content)
    total = 0
    for stem in sorted(groups):
        data = groups[stem]
        title = data.get("title", stem)
        out += [f"### {title}", ""]
        if data.get("desc"):
            out += [_quote(data["desc"]), ""]
        total += 1
    if not total:
        return "", 0
    return "\n".join(out).rstrip() + "\n", total


# ---------------------------------------------------------------- file 04


def build_sinner_file(texts: Texts, lang: str) -> tuple[str, int]:
    lbl = _t(texts, lang)
    out = [
        f"# {GAME} — Akta Grzeszników (introdukcje)",
        "",
        lbl["reader"],
        "",
        "Krótkie akta osobowe każdego Grzesznika widoczne w profilu więźnia"
        " (`IntroduceCharacter`: opisy akt; imiona z `Characters`). Kolejność ="
        " kolejność Grzeszników w autobusie (#1–#12).",
        "",
        f"## {lbl['sinners']}",
        "",
    ]
    characters = texts.by_id("Characters")
    rows = _rows(texts, "IntroduceCharacter.json")
    total = 0
    for idx, row in enumerate(rows, 1):
        hangul = str(row.get("id", ""))
        name_row = characters.get(str(idx), {})
        name = to_markdown(name_row.get("name"), texts.keywords)
        bio = to_markdown(row.get("description"), texts.keywords)
        if not bio:
            continue
        out += [f"### {lbl['sinner'].format(n=idx, name=name or hangul)}", ""]
        out += [_quote(bio), ""]
        total += 1
    if not total:
        return "", 0
    return "\n".join(out).rstrip() + "\n", total


# ---------------------------------------------------------------- spis


def build_index_file(files: dict[str, tuple[str, int]], lang: str) -> str:
    lbl = _t(texts=None, lang=lang)
    out = [
        f"# {GAME} — {lbl['spis']}",
        "",
        "Czwarta seria Czytanek: elementy spoza trzech głównych grup"
        " (fabuła / plik ID / plik E.G.O) — teksty tutoriali z misji, Notatki"
        " Dantego, splashe pobierania patcha i akta Grzeszników.",
        "",
        "Poza zakresem serii (osobne grupy albo teksty interfejsu bez treści"
        " fabularnej): `TutorialMainUIText` (przechadzki po interfejsie),"
        " `TutorialMirrorDungeon` (tutorial Lustrzanych Lochów), starsze zestawy"
        " `TutorialDesc*` (poprzednia wersja tutoriali).",
        "",
        f"| {lbl['file']} | {lbl['content']} | {lbl['items']} |",
        "|---|---|---:|",
    ]
    for name, (title, count) in sorted(files.items()):
        out.append(f"| `{name}` | {title} | {count} |")
    out.append("")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "index" / "localize",
                        help="Localize: index/localize (default) or a directory with <lang>/")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--out", type=Path, help="default: czytanki/plik_META_<LANG>")
    args = parser.parse_args(argv)
    args.out = args.out or ROOT / "czytanki" / f"plik_META_{args.lang.upper()}"
    args.out.mkdir(parents=True, exist_ok=True)
    suffix = args.lang.upper()
    written: dict[str, tuple[str, int]] = {}
    with Snapshot.open(args.snapshot) as snapshot:
        texts = Texts(snapshot, args.lang)
        pieces = [
            (f"01_teksty_z_misji_{suffix}.md", "Teksty z misji (tutorial bojowy)", build_mission_file),
            (f"02_notatki_dantego_{suffix}.md", "Notatki Dantego (encyklopedia świata)", build_notes_file),
            (f"03_splashe_pobierania_{suffix}.md", "Splashe pobierania patcha", build_splash_file),
            (f"04_akta_grzesznikow_{suffix}.md", "Akta Grzeszników (introdukcje)", build_sinner_file),
        ]
        for file_name, title, builder in pieces:
            text, count = builder(texts, args.lang)
            if not text:
                continue
            (args.out / file_name).write_text(align_markdown_tables(text), encoding="utf-8")
            written[file_name] = (title, count)
        (args.out / f"00_spis_META_{suffix}.md").write_text(
            align_markdown_tables(build_index_file(written, args.lang)), encoding="utf-8")
    print(f"zapisano {len(written) + 1} plików do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
