#!/usr/bin/env python3
"""Build the translator package (story part) in the SRW layout.

``plik_dla_tlumacza_vN.zip``::

    README.md        instructions (Polish)
    sceny.zip        spis-rozdzialow.md, spis-scen.md, mowcy-i-miejsca.md,
                     NN_<chapter>[_a].md  (scenes in reading order), identity-NN.md,
                     pozostale.md

Every scene starts with a context header (chapter, stage title and place,
battle phase, previous/next scene, speakers, locations); every line is one
element::

    14. [Dialog - 카론 (Charon)] 베르.
       miejsce: 메피스토펠레스 내부 — Aboard Mephistopheles
       limit: do 340 znaków
       EN: Verg.
       PL:

Speaker names, epithets and locations are separate strings in the game data;
they are translated once in ``mowcy-i-miejsca.md`` and only shown as context in
the scenes. Repeated lines in one file are marked ``(powtórzenie elementu N)``.

Sources: the story index (``wiedza/indeks_fabuly.json``) and a Localize
snapshot with ``kr`` (source) and ``en`` (reference), by default ``index/localize``.
The ZIP goes to ``local/pakiet/`` and the owner's Drive (ZIPs are not versioned).
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_reading import Chapters, PHASE_TEXT, slug
from tools.lcb_text import Texts, one_line, stage_label
from tools.localize import Snapshot


ROOT = Path(__file__).resolve().parent.parent
LINES_PER_FILE = 8000
SCENE_LIMIT_QUANTILE = 0.999
TOKEN = re.compile(r"<[^<>]+>|\{\d+\}")
TMP_TAG = re.compile(r"</?(?:i|b|u|s|color|size|sprite|link|style|font|mark|align|ruby|noparse|br)(?:[= ][^<>]*)?>",
                     re.I)
ZIP_TIME = (2026, 1, 1, 0, 0, 0)


def visible_length(text: str) -> int:
    return len(TMP_TAG.sub("", text))


def tokens(text: str) -> list[str]:
    found = []
    for token in TMP_TAG.findall(text) + re.findall(r"\{\d+\}", text):
        if token not in found:
            found.append(token)
    return found


def clean(text: object) -> str:
    """One line as the translator sees it: game line breaks become `` / ``."""
    if not isinstance(text, str):
        return ""
    return re.sub(r"\s*(?:\\n|\n)\s*", " / ", text.strip())


def by_id(rows: list[dict] | None) -> dict:
    return {row.get("id"): row for row in rows or [] if isinstance(row, dict) and "id" in row}


class Story:
    """KR and EN texts of the snapshot plus derived context."""

    def __init__(self, snapshot: Snapshot, source: str = "kr", reference: str = "en") -> None:
        self.src = Texts(snapshot, source)
        self.ref = Texts(snapshot, reference)
        self.chapters_src = Chapters(self.src)
        self.chapters_ref = Chapters(self.ref)
        self.models_src = self.src.models
        self.models_ref = self.ref.models
        self.limit = self._scene_limit()

    def _scene_limit(self) -> int:
        lengths = []
        for logical in self.ref.names():
            if logical.startswith("StoryData/"):
                lengths += [visible_length(r["content"]) for r in self.ref.table(logical)
                            if isinstance(r.get("content"), str)]
        if not lengths:
            return 300
        lengths.sort()
        value = lengths[min(len(lengths) - 1, int(len(lengths) * SCENE_LIMIT_QUANTILE))]
        return int(-(-value // 10) * 10)

    def pair(self, stem: str) -> list[tuple[int, dict, dict]]:
        src_rows = self.src.story(stem) or []
        ref_rows = by_id(self.ref.story(stem))
        out = []
        for row in src_rows:
            if row.get("id") == -1:
                continue
            out.append((len(out) + 1, row, ref_rows.get(row.get("id"), {})))
        return out

    def speaker(self, src: dict, ref: dict) -> tuple[str, str] | None:
        if not (src.get("model") or src.get("teller") or ref.get("teller")):
            return None
        model = src.get("model") if isinstance(src.get("model"), str) else ""
        name_src = clean(src.get("teller")) or clean(self.models_src.get(model, {}).get("name")) or model
        name_ref = clean(ref.get("teller")) or clean(self.models_ref.get(model, {}).get("name"))
        return name_src, name_ref


def text_block(prefix: str, text: str) -> list[str]:
    return [prefix + text]


class Glossary:
    """Speaker names, epithets and places: translated once, used everywhere."""

    KINDS = (("teller", "Imię mówcy"), ("model", "Imię postaci (tabela modeli)"),
             ("title", "Tytuł mówcy"), ("place", "Miejsce"))

    def __init__(self) -> None:
        self.items: dict[tuple[str, str], dict] = {}

    def add(self, kind: str, src: str, ref: str, where: str) -> None:
        if not src:
            return
        item = self.items.setdefault((kind, src), {"ref": ref, "count": 0, "first": where})
        item["count"] += 1
        if not item["ref"] and ref:
            item["ref"] = ref

    def render(self) -> str:
        lines = ["# Mówcy, tytuły i miejsca — Limbus Company", "",
                 "Te napisy gra trzyma osobno od kwestii. Tłumaczysz je **raz tutaj**; w plikach scen są "
                 "pokazane tylko jako kontekst.", ""]
        for kind, label in self.KINDS:
            entries = sorted(((src, item) for (k, src), item in self.items.items() if k == kind),
                             key=lambda e: (-e[1]["count"], e[0]))
            if not entries:
                continue
            limit = max(max(len(item["ref"]), len(src)) for src, item in entries)
            lines += [f"## {label}", "", f"Limit pola: do {limit} znaków (najdłuższy napis tego rodzaju w grze).", ""]
            for number, (src, item) in enumerate(entries, 1):
                lines += [f"{number}. [{label}] {src}",
                          f"   występuje: {item['count']}×, pierwszy raz: {item['first']}",
                          f"   limit: do {limit} znaków",
                          f"   EN: {item['ref'] or '(brak w wersji angielskiej)'}",
                          "   PL:"]
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"


def scene_block(story: Story, scene: dict, seq: int, total: int, chapter_name: tuple[str, str],
                position: tuple[int, int], neighbours: tuple[str | None, str | None],
                seen: dict, glossary: Glossary) -> list[str]:
    stem = scene["plik"]
    pairs = story.pair(stem)
    where = f"{chapter_name[0]} ({stem})"
    lines = [f"## Scena {seq}/{total} — {stem}"]
    lines.append(f"- rozdział: {chapter_name[0]}" + (f" — {chapter_name[1]}" if chapter_name[1] else ""))
    lines.append(f"- miejsce w rozdziale: scena {position[0]}/{position[1]}")
    node = scene.get("wezel")
    if node is None and isinstance(scene.get("bitwa"), int) and stage_label(scene["bitwa"]):
        node = scene["bitwa"]
    if node is not None:
        t_src, p_src, _ = story.chapters_src.stage(node)
        t_ref, p_ref, d_ref = story.chapters_ref.stage(node)
        lines.append(f"- etap: {stage_label(node) or node} · {t_src or '—'}" + (f" — {t_ref}" if t_ref else ""))
        if p_src or p_ref:
            lines.append(f"- miejsce etapu: {p_src or '—'}" + (f" — {p_ref}" if p_ref else ""))
        if d_ref:
            lines.append(f"- opis etapu (EN): {one_line(d_ref)}")
    elif re.match(r"^\d+D", stem):
        lines.append("- etap: eksploracja (loch)")
    moment = PHASE_TEXT.get(scene.get("etap"))
    if moment:
        lines.append(f"- moment: {moment.lower()}")
    if scene.get("trasa"):
        lines.append(f"- trasa: {scene['trasa']} (rozdział z rozgałęzieniami)")
    lines.append(f"- poprzednia scena: {neighbours[0] or '—'}; następna: {neighbours[1] or '—'}")
    speakers: dict[str, str] = {}
    places: dict[str, str] = {}
    for _, src, ref in pairs:
        who = story.speaker(src, ref)
        if who:
            speakers.setdefault(who[0], who[1])
        if isinstance(src.get("place"), str) and src["place"].strip():
            places.setdefault(clean(src["place"]), clean(ref.get("place")))
    if speakers:
        lines.append("- uczestnicy:")
        lines += [f"  - {s}" + (f" — {r}" if r and r != s else "") for s, r in speakers.items()]
    if places:
        lines.append("- miejsca:")
        lines += [f"  - {s}" + (f" — {r}" if r else "") for s, r in places.items()]
    lines.append("")
    for index, src, ref in pairs:
        text = clean(src.get("content"))
        if not text:
            continue
        who = story.speaker(src, ref)
        label = f"Dialog - {who[0]}" + (f" ({who[1]})" if who[1] and who[1] != who[0] else "") if who else "Narracja"
        lines.append(f"{index}. [{label}] {text}")
        if isinstance(src.get("place"), str) and src["place"].strip():
            lines.append(f"   miejsce: {clean(src['place'])}" + (f" — {clean(ref.get('place'))}"
                                                                    if ref.get("place") else ""))
            glossary.add("place", clean(src["place"]), clean(ref.get("place")), where)
        if isinstance(src.get("title"), str) and src["title"].strip():
            lines.append(f"   tytuł mówcy: {clean(src['title'])}" + (f" — {clean(ref.get('title'))}"
                                                                        if ref.get("title") else ""))
            glossary.add("title", clean(src["title"]), clean(ref.get("title")), where)
        if isinstance(src.get("teller"), str) and src["teller"].strip():
            glossary.add("teller", clean(src["teller"]), clean(ref.get("teller")), where)
        elif isinstance(src.get("model"), str) and who:
            glossary.add("model", who[0], who[1], where)
        english = clean(ref.get("content"))
        lines.append(f"   limit: do {max(story.limit, visible_length(english))} znaków")
        found = tokens(text)
        if found:
            lines.append("   tokeny: zachowaj dokładnie: " + ", ".join(found))
        key = (text, english)
        if key in seen:
            lines.append(f"   (powtórzenie elementu {seen[key]} — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)")
            continue
        seen[key] = f"{index} sceny {stem}"
        lines.append(f"   EN: {english or '(brak wersji angielskiej)'}")
        lines.append("   PL:")
    lines += ["", "_koniec sceny_", ""]
    return lines


def chapter_files(base: str, title: str, blocks: list[list[str]], limit_note: str) -> dict[str, str]:
    chunks: list[list[list[str]]] = []
    current: list[list[str]] = []
    count = 0
    for block in blocks:
        if current and count + len(block) > LINES_PER_FILE:
            chunks.append(current)
            current, count = [], 0
        current.append(block)
        count += len(block)
    if current:
        chunks.append(current)
    files = {}
    for number, chunk in enumerate(chunks):
        suffix = "" if len(chunks) == 1 else f"_{chr(ord('a') + number)}"
        head = [f"# {title}{' (część ' + chr(ord('a') + number) + ')' if suffix else ''} — Limbus Company", "",
                limit_note, ""]
        files[f"{base}{suffix}.md"] = "\n".join(head + [line for block in chunk for line in block]).rstrip() + "\n"
    return files


def build(index: dict, story: Story) -> tuple[dict[str, str], dict]:
    groups: list[tuple[str, str, tuple[str, str], list[dict]]] = []
    for chapter in index["rozdzialy"]:
        name_src, _ = story.chapters_src.heading(chapter)
        name_ref, _ = story.chapters_ref.heading(chapter)
        scenes = [s for s in chapter["sceny"] if story.src.story(s["plik"]) is not None]
        groups.append((f"{chapter['kolejnosc']:02d}_{slug(name_ref)}", name_ref, (name_ref, name_src), scenes))
    by_character: dict[int, list[dict]] = collections.defaultdict(list)
    for row in index.get("identity", []):
        for stem in row.get("pliki", []):
            if story.src.story(stem) is not None:
                by_character[row.get("postac", 0)].append({"plik": stem, "etap": None, "identity": row.get("identity")})
    characters = by_character and {str(k): one_line(v.get("name", "")) for k, v in story.ref.by_id("Characters").items()}
    for character, scenes in sorted(by_character.items()):
        name = characters.get(str(character)) or f"postać {character}"
        groups.append((f"identity-{character:02d}", f"Historie Identity: {name}", (f"Historie Identity: {name}", ""),
                       scenes))
    rest = [{"plik": stem, "etap": None} for stem in index.get("nieprzypisane", []) if story.src.story(stem) is not None]
    if rest:
        groups.append(("pozostale", "Sceny bez miejsca w kolejności", ("Sceny bez miejsca w kolejności", ""), rest))

    flat = [s["plik"] for *_, scenes in groups for s in scenes]
    total = len(flat)
    glossary = Glossary()
    files: dict[str, str] = {}
    toc_scenes = ["# Spis scen — Limbus Company", "", f"Scen: {total}. Numer w nagłówku sceny (`## Scena 12/{total}`) "
                  "to pozycja w kolejności czytania.", "",
                  "| # | rozdział | scena | etap | moment | plik | kwestii |", "|---|---|---|---|---|---|---|"]
    toc_chapters = ["# Spis rozdziałów — Limbus Company", "",
                    "Kolejność rozdziałów i scen pochodzi z danych gry (Teatr Opowieści, tabele etapów i walk).", "",
                    "| # | rozdział | KR | scen | kwestii | plik |", "|---|---|---|---|---|---|"]
    limit_note = (f"Każda kwestia ma `limit:` — liczba polskich znaków (domyślnie {story.limit}: tyle mieści "
                  "99,9% angielskich kwestii; okno gry samo łamie linie). Tekst wpisujesz w jednej linii po `PL:`.")
    seq = 0
    counts = {"sceny": 0, "elementy": 0, "do_tlumaczenia": 0}
    for number, (base, title, names, scenes) in enumerate(groups, 1):
        blocks = []
        seen: dict = {}
        group_lines = 0
        for i, scene in enumerate(scenes):
            seq += 1
            prev_stem = flat[seq - 2] if seq > 1 else None
            next_stem = flat[seq] if seq < total else None
            block = scene_block(story, scene, seq, total, names, (i + 1, len(scenes)), (prev_stem, next_stem),
                                seen, glossary)
            elements = sum(1 for line in block if re.match(r"^\d+\. \[", line))
            todo = sum(1 for line in block if line == "   PL:")
            counts["elementy"] += elements
            counts["do_tlumaczenia"] += todo
            group_lines += elements
            node = scene.get("wezel") or (scene.get("bitwa") if isinstance(scene.get("bitwa"), int) else None)
            toc_scenes.append(f"| {seq} | {title} | {i + 1}/{len(scenes)} | {stage_label(node) if node else '—'} | "
                              f"{(PHASE_TEXT.get(scene.get('etap')) or '—').lower()} | {base} | {elements} |")
            blocks.append(block)
        counts["sceny"] += len(scenes)
        produced = chapter_files(base, title, blocks, limit_note)
        files.update(produced)
        toc_chapters.append(f"| {number} | {names[0]} | {names[1] or '—'} | {len(scenes)} | {group_lines} | "
                            + ", ".join(sorted(produced)) + " |")
    files["spis-scen.md"] = "\n".join(toc_scenes) + "\n"
    files["spis-rozdzialow.md"] = "\n".join(toc_chapters) + "\n"
    files["mowcy-i-miejsca.md"] = glossary.render()
    counts["napisy_slownika"] = len(glossary.items)
    counts["limit_kwestii"] = story.limit
    return files, counts


def readme(version: int, counts: dict) -> str:
    return f"""# Limbus Company — pakiet dla tłumacza (koreański → polski), wersja {version}

## 0. W skrócie

- W środku: `sceny.zip` — {counts['sceny']} scen fabuły w **kolejności czytania**, {counts['elementy']} elementów,
  z czego {counts['do_tlumaczenia']} do przetłumaczenia (reszta to powtórzenia).
- Źródłem jest **koreański**; `EN:` to oficjalna wersja angielska jako odniesienie.
- Polski tekst wpisujesz w jednej linii po `PL:`. Nic więcej w pliku nie zmieniasz.

## 1. Jak wygląda jeden element

```text
14. [Dialog - 카론 (Charon)] 베르.
   miejsce: 메피스토펠레스 내부 — Aboard Mephistopheles
   limit: do {counts['limit_kwestii']} znaków
   EN: Verg.
   PL: Werg.
```

- `[Dialog - mówca]` — kto mówi (koreańska nazwa z gry i angielska w nawiasie); `[Narracja]` — narrator
  (najczęściej Dante; jego myśli i opis).
- `miejsce:` / `tytuł mówcy:` — tylko kontekst; te napisy tłumaczysz raz, w `mowcy-i-miejsca.md`.
- `tokeny:` — znaczniki gry (`<i>`, `<color=…>`, `<ruby=…>`); muszą zostać w tekście, w tej samej kolejności.
- `(powtórzenie elementu N…)` — ta sama kwestia była już wcześniej w tym pliku; nic nie wpisujesz.

## 2. Nagłówek sceny — kontekst

Każda scena zaczyna się od `## Scena N/{counts['sceny']} — <plik>` i listy: rozdział, miejsce w rozdziale,
etap (numer, tytuł, miejsce i opis z gry), moment (przed walką / w trakcie walki / po walce / eksploracja),
poprzednia i następna scena, uczestnicy i miejsca. `spis-rozdzialow.md` i `spis-scen.md` pokazują całość.

## 3. Zasady

- Kwestie Dantego w nawiasach `<…>` to tykanie zegara, które rozumieją tylko Grzesznicy — nawiasy zostają.
- Imiona i nazwy własne: według słowniczka projektu; w razie wątpliwości zostaw jak w EN i dopisz `[?]`.
- Limit to liczba znaków, którą da się policzyć; gra sama łamie linie.

## 4. Co odesłać

Te same pliki `.md` z wypełnionymi `PL:` (całe lub część) — spakowane w zip, nazwy plików bez zmian.
"""


def write_zip(path: Path, files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[name])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "index" / "localize",
                        help="Localize: index/localize (default), a collector ZIP or a directory with <lang>/")
    parser.add_argument("--index", type=Path, default=ROOT / "wiedza" / "indeks_fabuly.json")
    parser.add_argument("--version", type=int, default=1)
    parser.add_argument("--out", type=Path, default=ROOT / "local" / "pakiet")
    parser.add_argument("--only", action="append", type=int, help="sub-chapter id(s) (sample package)")
    args = parser.parse_args(argv)
    index = json.loads(args.index.read_text(encoding="utf-8"))
    if args.only:
        index = {**index, "rozdzialy": [c for c in index["rozdzialy"] if c["id"] in args.only],
                 "identity": [], "nieprzypisane": []}
    with Snapshot.open(args.snapshot) as snapshot:
        files, counts = build(index, Story(snapshot))
    scenes = io.BytesIO()
    with zipfile.ZipFile(scenes, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[name].encode("utf-8"))
    args.out.mkdir(parents=True, exist_ok=True)
    target = args.out / f"plik_dla_tlumacza_v{args.version}.zip"
    write_zip(target, {"README.md": readme(args.version, counts).encode("utf-8"), "sceny.zip": scenes.getvalue()})
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(json.dumps({**counts, "plik": str(target), "bajty": target.stat().st_size, "sha256": digest},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
