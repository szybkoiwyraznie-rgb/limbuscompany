#!/usr/bin/env python3
"""Reconstruct the reading order of StoryData files from a fan story library.

Inputs:

* a Localize snapshot (collector ZIP or a directory with ``<lang>/StoryData``),
* a checkout of a story-reading site laid out like ``retcons/limbus-storylogs``
  (``index.html`` linking ``chapters/**.html`` in reading order; each page
  shows the dialogue lines as HTML text).

Method: every StoryData ``content`` line longer than ``MIN_CHARS`` characters
(after stripping tags/punctuation and lowercasing) that occurs in exactly one
StoryData file becomes a fingerprint. Each page is scanned in order and its
text runs are matched against the fingerprints; the sequence of distinct files
hit is the page's reading order. A file hit on several pages is assigned to the
page with the most matched lines.

The output (default ``wiedza/kolejnosc_fabuly.json``) contains **only file
stems, page names and counts** - never game text - so it may be committed.
It also reports how often the in-page order agrees with ``story_sort_key``.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import html
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.localize import Snapshot, load_json


ROOT = Path(__file__).resolve().parent.parent
FORMAT = "lcb-kolejnosc-fabuly-v1"
DEFAULT_OUT = ROOT / "wiedza" / "kolejnosc_fabuly.json"
MIN_CHARS = 25
TAG = re.compile(r"<[^>]+>")
NON_WORD = re.compile(r"\W+", re.UNICODE)
PAGE_LINK = re.compile(r'href="(chapters/[^"]+\.html)"')
TEXT_RUN = re.compile(r">([^<>]{20,})<")
STEM = re.compile(r"^(?P<group>S|E|ES|PC|P|\d+D)(?P<number>\d+)(?P<phase>[A-Z]?)(?P<step>\d*)$")
PHASE_RANK = {"B": 0, "I": 1, "": 1, "A": 2, "X": 3}
GROUP_RANK = {"S": 0, "D": 1, "E": 2, "ES": 3, "PC": 4, "P": 5}


def normalize(text: str) -> str:
    return NON_WORD.sub(" ", TAG.sub("", text)).strip().lower()


def story_sort_key(stem: str) -> tuple:
    """Hypothetical in-chapter order: S < nD < E < ES < PC < P, number, B < I(n) < A.

    Unknown stems sort last by name. Measured agreement is reported, not assumed.
    """
    match = STEM.match(stem)
    if not match:
        return (9, 0, 9, 0, stem)
    group = match["group"]
    rank = GROUP_RANK["D"] if group.endswith("D") and group[:-1].isdigit() else GROUP_RANK[group]
    chapter = int(group[:-1]) if rank == GROUP_RANK["D"] else 0
    return (rank, chapter * 10**6 + int(match["number"]), PHASE_RANK.get(match["phase"], 4),
            int(match["step"] or 0), stem)


def label(page: str) -> str:
    stem = PurePosixPath(page).stem
    if stem == "prologue":
        return "Prolog"
    match = re.fullmatch(r"chapter(\d+)", stem)
    if match:
        return f"Canto {match[1]}"
    match = re.fullmatch(r"chapter(\d+\.5)(?:_(.+))?", stem)
    if match:
        return f"Intervallo {match[1]}" + (f" ({match[2]})" if match[2] else "")
    return f"Opowiadanie: {stem}"


def fingerprints(snapshot: Snapshot, lang: str) -> tuple[dict[str, str], list[str]]:
    seen: dict[str, set[str]] = defaultdict(set)
    stems = []
    for logical in sorted(snapshot.files.get(lang, {})):
        path = PurePosixPath(logical)
        if path.parts[0] != "StoryData" or len(path.parts) != 2:
            continue
        stems.append(path.stem)
        data = load_json(snapshot.read(lang, logical))
        items = data.get("dataList", []) if isinstance(data, dict) else []
        for item in items:
            if isinstance(item, dict) and isinstance(item.get("content"), str):
                text = normalize(item["content"])
                if len(text) > MIN_CHARS:
                    seen[text].add(path.stem)
    unique = {text: next(iter(files)) for text, files in seen.items() if len(files) == 1}
    return unique, stems


def page_sequence(page_html: str, unique: dict[str, str]) -> list[list]:
    sequence: list[list] = []
    for run in TEXT_RUN.findall(page_html):
        stem = unique.get(normalize(html.unescape(run)))
        if stem is None:
            continue
        if sequence and sequence[-1][0] == stem:
            sequence[-1][1] += 1
        else:
            sequence.append([stem, 1])
    return sequence


def git_head(path: Path) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"], capture_output=True,
                             text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip() or None


def build(snapshot: Snapshot, library: Path, lang: str = "en") -> dict:
    unique, stems = fingerprints(snapshot, lang)
    pages = PAGE_LINK.findall((library / "index.html").read_text(encoding="utf-8"))
    pages = list(dict.fromkeys(pages))
    raw = {page: page_sequence((library / page).read_text(encoding="utf-8"), unique) for page in pages}

    totals: dict[str, Counter] = defaultdict(Counter)
    for page, sequence in raw.items():
        for stem, lines in sequence:
            totals[stem][page] += lines
    home = {stem: max(counter.items(), key=lambda kv: (kv[1], -pages.index(kv[0])))[0]
            for stem, counter in totals.items()}

    chapters, agree, pairs = [], 0, 0
    for page in pages:
        ordered: list[str] = []
        for stem, _ in raw[page]:
            if home[stem] == page and stem not in ordered:
                ordered.append(stem)
        for before, after in zip(ordered, ordered[1:]):
            pairs += 1
            agree += story_sort_key(before) <= story_sort_key(after)
        chapters.append({
            "strona": page,
            "etykieta": label(page),
            "pliki": [[stem, totals[stem][page]] for stem in ordered],
        })
    placed = set(home)
    return {
        "format": FORMAT,
        "jezyk_dopasowania": lang,
        "migawka_commit": git_head(snapshot.source) if snapshot.source.is_dir() else None,
        "zrodlo_kolejnosci": {"repozytorium": "retcons/limbus-storylogs", "commit": git_head(library)},
        "metoda": (f"unikalne linie content > {MIN_CHARS} znaków (bez tagów, małe litery) dopasowane do "
                   "tekstu stron w kolejności index.html; plik przypisany do strony z największą liczbą "
                   "dopasowanych linii; liczba przy pliku = dopasowane linie"),
        "zgodnosc_z_regula": {"zgodne_pary": agree, "pary": pairs,
                              "regula": "S < nD < E < ES < PC < P; numer; B < I(n) < A < X"},
        "pliki_storydata": len(stems),
        "przypisane": len(placed),
        "rozdzialy": chapters,
        "nieprzypisane": sorted(set(stems) - placed, key=story_sort_key),
    }


def dumps(result: dict) -> str:
    """Indented JSON with each ``[stem, lines]`` pair kept on one line (diff-friendly)."""
    text = json.dumps(result, ensure_ascii=False, indent=1)
    return re.sub(r'\[\s+("[^"]*"),\s+(\d+)\s+\]', r"[\1, \2]", text) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", type=Path, help="collector ZIP or directory with <lang>/StoryData")
    parser.add_argument("library", type=Path, help="checkout of a story library (index.html + chapters/)")
    parser.add_argument("--lang", default="en", help="language of the library text (default: en)")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    with Snapshot.open(args.snapshot) as snapshot:
        if args.lang not in snapshot.files:
            parser.error(f"language {args.lang!r} not in snapshot: {snapshot.languages}")
        result = build(snapshot, args.library, args.lang)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(dumps(result), encoding="utf-8")
    z = result["zgodnosc_z_regula"]
    print(f"StoryData: {result['pliki_storydata']}, przypisane: {result['przypisane']}, "
          f"strony: {len(result['rozdzialy'])}, nieprzypisane: {len(result['nieprzypisane'])}, "
          f"zgodność z regułą: {z['zgodne_pary']}/{z['pary']}")
    print(f"zapisano {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
