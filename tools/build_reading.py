#!/usr/bin/env python3
"""Build the story Czytanki (readable story editions) from the story index and Localize.

One Markdown file per chapter in reading order (``wiedza/indeks_fabuly.json``),
SRW/OE layout:

* ``# Limbus Company — Canto I: The Outcast`` + in-world date, place and the
  chapter epigraph from the Story Theater;
* ``### Etap 1-1 · <stage title>`` with the stage place and description,
  phase notes (before / during / after battle, exploration);
* ``#### <place>`` whenever a scene changes location;
* dialogue as ``**Speaker:** line`` (epithet shown on first appearance in a
  scene), narration as plain paragraphs, no identifiers in the visible text
  (scene file names are kept in HTML comments for traceability).

Output: ``czytanki/fabula_<LANG>/`` (Markdown, versioned in Git like the
source texts in ``index/``).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import unicodedata
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.lcb_text import Texts, one_line, stage_label, to_markdown
from tools.localize import Snapshot


ROOT = Path(__file__).resolve().parent.parent
GAME = "Limbus Company"
PHASE_TEXT = {
    "przed": "Przed walką",
    "po": "Po walce",
    "w trakcie": "W trakcie etapu",
    "walka": "W trakcie walki",
}
LANG_NAMES = {"en": "angielskiej", "kr": "koreańskiej", "jp": "japońskiej", "pl": "polskiej"}
SPEAKER_OVERRIDES = {"Me": "Ja"}


def _is_dante(model: object, teller: object) -> bool:
    return (isinstance(model, str) and "단테" in model) or teller in ("Dante", "단테", "Me", "나", "Ja")


def _format_speaker(name: str, title: str | None) -> str:
    if title:
        epithet = f"({title})" if not title.strip("*") else f"(*{title}*)"
        return f"{name} {epithet}:" if not name.strip("*") else f"**{name}** {epithet}:"
    return f"{name}:" if not name.strip("*") else f"**{name}:**"


def slug(text: str) -> str:
    """ASCII file-name part (portable on Windows/zip/Drive); empty for non-Latin titles."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return text[:40] or "rozdzial"


class Chapters:
    """Chapter titles and stage titles from Localize."""

    def __init__(self, texts: Texts) -> None:
        self.texts = texts
        self.chapter_rows: dict[int, dict] = {}
        for row in texts.family("StageChapterText"):
            match = re.search(r"_(\d+)$", str(row.get("id", "")))
            if match:
                self.chapter_rows.setdefault(int(match[1]), row)
        self.theater = {**texts.by_id("StoryTheaterMain"), **texts.by_id("StoryTheaterOther")}
        self.nodes = texts.by_id("StageNode")

    def heading(self, chapter: dict) -> tuple[str, list[str]]:
        sub = chapter["id"]
        row = self.chapter_rows.get(sub, {})
        number = one_line(to_markdown(row.get("chapter")))
        title = one_line(to_markdown(row.get("chaptertitle")))
        if not title:
            for key in (f"CHAPTER_{sub}", f"EventTitleText_{sub}"):
                if key in self.theater:
                    title = one_line(to_markdown(self.theater[key].get("title")))
                    break
        if not number:
            number = {"canto": "Canto", "intervallo": "Intervallo", "opowiadanie": "Opowiadanie"}.get(
                chapter.get("grupa"), "Rozdział")
            if chapter.get("grupa") == "canto" and sub == 100:
                number = "Prolog"
        name = f"{number}: {title}" if title else number
        details = []
        meta = [one_line(to_markdown(row.get(k))) for k in ("timeline", "company", "area")]
        meta = [m for m in meta if m]
        if meta:
            if row.get("timeline"):
                meta[0] = f"rok {meta[0]}"
            details.append("*" + " · ".join(meta) + "*")
        epigraph = self.theater.get(f"CHAPTER_{sub}", {}).get("desc")
        if epigraph:
            details.append("\n".join("> " + line if line.strip() else ">"
                                     for line in to_markdown(epigraph).splitlines()))
        return name, details

    def stage(self, node: int) -> tuple[str | None, str | None, str | None]:
        row = self.nodes.get(str(node), {})
        title = row.get("title") or self.theater.get(f"STORY_{node}", {}).get("title")
        return (one_line(to_markdown(title)) or None, one_line(to_markdown(row.get("place"))) or None,
                to_markdown(row.get("desc")) or None)


def render_scene(lines: list[dict], texts: Texts, out: list[str], place_state: dict) -> int:
    models = texts.models
    keywords = texts.keywords
    introduced: set[tuple[str, str]] = set()
    written = 0
    for row in lines:
        if row.get("id") == -1:
            continue
        place = one_line(to_markdown(row.get("place")))
        if place and place != place_state.get("place"):
            if out and out[-1] != "":
                out.append("")
            out += [f"#### {place}", ""]
            place_state["place"] = place
        model = row.get("model")
        teller = row.get("teller")
        content = to_markdown(
            row.get("content"),
            keywords,
            strip_ticking=True,
            dante=_is_dante(model, teller),
        )
        if not content:
            continue
        content = re.sub(r"\n+", " ", content)
        if model or teller:
            name = one_line(to_markdown(teller)) if teller else ""
            if not name and isinstance(model, str):
                name = one_line(to_markdown(models.get(model, {}).get("name"))) or model
            name = SPEAKER_OVERRIDES.get(name, name)
            title = one_line(to_markdown(row.get("title")))
            title = SPEAKER_OVERRIDES.get(title, title)
            shown_title: str | None = None
            if title and title != name and (name, title) not in introduced:
                introduced.add((name, title))
                shown_title = title
            out.append(f"{_format_speaker(name, shown_title)} {content}")
        else:
            out.append(content)
        written += 1
    if out and out[-1] != "":
        out.append("")
    return written


def build_chapter(chapter: dict, texts: Texts, chapters: Chapters, lang: str,
                  en_texts: Texts | None = None) -> tuple[str, str, dict]:
    name, details = chapters.heading(chapter)
    out = [f"# {GAME} — {name}", ""]
    for detail in details:
        out += [detail, ""]
    missing = [s["plik"] for s in chapter["sceny"] if texts.story(s["plik"]) is None]
    note = (f"> **Uwaga dla czytelnika:** tekst w wersji {LANG_NAMES.get(lang, lang)}; kolejność scen według "
            "Teatru Opowieści i tabel etapów gry (`wiedza/indeks_fabuly.json`).")
    if en_texts is not None:
        note += " Sceny bez przekładu pozostają w oryginale (angielskim)."
    if any(s.get("trasa") for s in chapter["sceny"]):
        note += " Rozdział ma rozgałęzienia (trasy A/B/C); sceny tras podano w kolejności plików."
    if missing:
        note += f" Brak tekstu {len(missing)} scen w tej wersji danych."
    fallback = 0
    if en_texts is not None:
        for scene in chapter["sceny"]:
            lines = texts.story(scene["plik"])
            if lines is not None and lines == en_texts.story(scene["plik"]):
                fallback += 1
        if fallback:
            note += f" {fallback} scen(y) w tej Czytance to jeszcze wersja angielska."
    out += [note, "", "## Sceny fabularne", ""]
    stats = {"sceny": 0, "kwestie": 0}
    current_stage = object()
    place_state: dict = {}
    for scene in chapter["sceny"]:
        lines = texts.story(scene["plik"])
        if lines is None:
            continue
        node = scene.get("wezel")
        if node is None and isinstance(scene.get("bitwa"), int) and stage_label(scene["bitwa"]):
            node = scene["bitwa"]
        if node != current_stage:
            current_stage = node
            place_state.clear()
            if node is not None:
                title, place, desc = chapters.stage(node)
                label = stage_label(node) or str(node)
                out += [f"### Etap {label}" + (f" · {title}" if title else ""), ""]
                if place:
                    out += [f"*Miejsce: {place}*", ""]
                if desc:
                    out += ["\n".join("> " + l if l.strip() else ">" for l in desc.splitlines()), ""]
            elif re.match(r"^\d+D", scene["plik"]):
                out += ["### Eksploracja", ""]
            else:
                out += ["### Scena", ""]
        phase = PHASE_TEXT.get(scene.get("etap"))
        if scene.get("trasa"):
            phase = f"{phase} · trasa {scene['trasa']}" if phase else f"Trasa {scene['trasa']}"
        out += [f"<!-- {scene['plik']} -->", ""]
        if phase:
            out += [f"*— {phase} —*", ""]
        stats["kwestie"] += render_scene(lines, texts, out, place_state)
        stats["sceny"] += 1
    return name, "\n".join(out).rstrip() + "\n", stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "index" / "localize",
                        help="Localize: index/localize (default), a collector ZIP or a directory with <lang>/")
    parser.add_argument("--index", type=Path, default=ROOT / "wiedza" / "indeks_fabuly.json")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--out", type=Path, help="default: czytanki/fabula_<LANG>")
    parser.add_argument("--only", action="append", type=int, help="sub-chapter id(s) to build, e.g. 101")
    args = parser.parse_args(argv)
    index = json.loads(args.index.read_text(encoding="utf-8"))
    args.out = args.out or ROOT / "czytanki" / f"fabula_{args.lang.upper()}"
    args.out.mkdir(parents=True, exist_ok=True)
    toc = [f"# {GAME} — Czytanki: spis rozdziałów", "",
           f"Wersja językowa: {args.lang}. Kolejność: `{args.index.name}`.", "",
           "| # | Rozdział | Sceny | Kwestie | Plik |", "|---|---|---|---|---|"]
    with Snapshot.open(args.snapshot) as snapshot:
        texts = Texts(snapshot, args.lang)
        chapters = Chapters(texts)
        # File names come from the English titles, so every language has the same names.
        naming = Chapters(Texts(snapshot, "en")) if args.lang != "en" and "en" in snapshot.languages else chapters
        # PL: scenes without a translation keep their English original (fallback).
        en_texts = Texts(snapshot, "en") if args.lang == "pl" and "en" in snapshot.languages else None
        for chapter in index["rozdzialy"]:
            if args.only and chapter["id"] not in args.only:
                continue
            name, text, stats = build_chapter(chapter, texts, chapters, args.lang, en_texts)
            file_name = f"{chapter['kolejnosc']:02d}_{slug(naming.heading(chapter)[0])}_{args.lang.upper()}.md"
            (args.out / file_name).write_text(text, encoding="utf-8")
            toc.append(f"| {chapter['kolejnosc']} | {name} | {stats['sceny']} | {stats['kwestie']} | "
                       f"[{file_name}]({file_name}) |")
    (args.out / f"00_spis_{args.lang.upper()}.md").write_text("\n".join(toc) + "\n", encoding="utf-8")
    print(f"zapisano {len(toc) - 6} rozdziałów do {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
