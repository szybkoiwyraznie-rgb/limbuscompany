#!/usr/bin/env python3
"""Build the complete translator package (story + views) in the SRW layout.

``plik_dla_tlumacza_vN.zip``::

    README.md        instructions (Polish)
    sceny.zip        spis-rozdzialow.md, spis-scen.md, mowcy-i-miejsca.md,
                     NN_<chapter>[_a].md  (scenes in reading order), identity-NN.md,
                     pozostale.md
    widoki.zip       spis-widokow.md, mowcy-rpg-i-anomalii.md,
                     01_slownik_bojowy*.md, 02_tozsamosc_NN_<Sinner>*.md,
                     03_ego_postaci*.md, 03_dary_ego*.md, 04_anomalie_*.md,
                     04_wydarzenia_*.md, 04_wrogowie_*.md, 05_komentatorzy*.md,
                     05_muzyka_i_piosenki.md, 06_tryb_rpg_canto10*.md,
                     07_notatki_dantego_*.md, 07_rozdzialy_*.md, 07_loch_*.md,
                     08_interfejs_*.md, 08_samouczki_*.md, 08_wydarzenia_*.md,
                     08_przedmioty_sklep_i_profil*.md

Every scene in ``sceny.zip`` starts with a context header (chapter, stage title
and place, battle phase, previous/next scene, speakers, locations); every view
section in ``widoki.zip`` groups related game entities (Sinner Identities with
StaticData stats, skills, coins, passives, voice lines; E.G.O; Abnormalities;
RPG floors; UI) and records the exact ``Localize`` JSON leaf address on
``źródło:`` for lossless import.

Sources: ``wiedza/indeks_fabuly.json``, ``index/static-data/`` and a ``Localize``
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
from tools.package_views import build_views
from tools.static_data import StaticData


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
        return name_src or name_ref, name_ref


def text_block(prefix: str, text: str) -> list[str]:
    return [prefix + text]


class Glossary:
    """Speaker names, epithets and places: translated once, used everywhere."""

    KINDS = (("teller", "Imię mówcy"), ("model", "Imię postaci (tabela modeli)"),
             ("title", "Tytuł mówcy"), ("place", "Miejsce"))

    def __init__(self) -> None:
        self.items: dict[tuple[str, str], dict] = {}

    def add(self, kind: str, src: str, ref: str, where: str) -> None:
        key_src = src or (f"{ref} (tylko EN)" if ref else "")
        if not key_src:
            return
        item = self.items.setdefault((kind, key_src), {"ref": ref, "count": 0, "first": where})
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
        pl_s, pl_r = clean(src.get("place")), clean(ref.get("place"))
        if pl_s or pl_r:
            places.setdefault(pl_s or pl_r, pl_r)
    if speakers:
        lines.append("- uczestnicy:")
        lines += [f"  - {s}" + (f" — {r}" if r and r != s else "") for s, r in speakers.items()]
    if places:
        lines.append("- miejsca:")
        lines += [f"  - {s}" + (f" — {r}" if r and r != s else "") for s, r in places.items()]
    lines.append("")
    for index, src, ref in pairs:
        pl_s, pl_r = clean(src.get("place")), clean(ref.get("place"))
        ti_s, ti_r = clean(src.get("title")), clean(ref.get("title"))
        te_s, te_r = clean(src.get("teller")), clean(ref.get("teller"))
        text = clean(src.get("content"))
        if not text:
            if pl_s or pl_r:
                glossary.add("place", pl_s, pl_r, where)
            if ti_s or ti_r:
                glossary.add("title", ti_s, ti_r, where)
            if te_s or te_r:
                glossary.add("teller", te_s, te_r, where)
            continue
        who = story.speaker(src, ref)
        label = f"Dialog - {who[0]}" + (f" ({who[1]})" if who[1] and who[1] != who[0] else "") if who else "Narracja"
        lines.append(f"{index}. [{label}] {text}")
        if pl_s or pl_r:
            lines.append(f"   miejsce: {pl_s or '—'}" + (f" — {pl_r}" if pl_r else ""))
            glossary.add("place", pl_s, pl_r, where)
        if ti_s or ti_r:
            lines.append(f"   tytuł mówcy: {ti_s or '—'}" + (f" — {ti_r}" if ti_r else ""))
            glossary.add("title", ti_s, ti_r, where)
        if te_s or te_r:
            glossary.add("teller", te_s, te_r, where)
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
    has_views = "widoki_elementy" in counts
    views_bullet = ""
    if has_views:
        views_bullet = (
            f"\n- `widoki.zip` — **100% pozostałych tekstów gry** ({counts['widoki_pliki_gry']} plików źródłowych, "
            f"{counts['widoki_liscie_json']} niepustych pól w grze → {counts['widoki_elementy']} elementów w "
            f"{counts['widoki_pliki_md']} plikach `.md`, z czego **{counts['widoki_do_tlumaczenia']}** unikalnych do przetłumaczenia): "
            "słownik bojowy, karty i kwestie Tożsamości połączone dla każdego Grzesznika, E.G.O i Dary E.G.O, "
            "Anomalie, wydarzenia i wrogowie, komentatorzy bitwy, teksty piosenek, tryb RPG z Canto X, "
            "Notatki Dantego, Teatr, Lochy, interfejs, samouczki, wydarzenia sezonowe i sklep."
        )
    views_section = ""
    if has_views:
        views_section = """
## 2. Widoki, postacie, umiejętności i interfejs (`widoki.zip`)

Zacznij od `spis-widokow.md` (pełna tabela działów) oraz od słowników terminologii:
1. `01_slownik_bojowy_*.md` — tagi umiejętności (`[On Hit]`, `[On Use]`), grzechy, słowa kluczowe bitwy i statusy (`Burn`, `Bleed`, `Tremor`, `Sinking`…).
2. `mowcy-rpg-i-anomalii.md` (oraz `mowcy-i-miejsca.md` w `sceny.zip`) — imiona mówców i tabela modeli postaci, tłumaczone raz.

Przykład elementu umiejętności w `widoki.zip`:

```text
7. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 공격 위력 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2010111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Reduction]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttackHead] Inflict 2 [Reduction]
   PL: [OnSucceedAttackHead] Nałóż 2 [Reduction]
```

Najważniejsze zasady w `widoki.zip`:
- **Nie tłumacz angielskich identyfikatorów w nawiasach kwadratowych** wypisanych w `tokeny:` (np. `[OnSucceedAttackHead]`, `[Combustion]`, `[Vibration]`, `[Reduction]`). Gra sama podstawia w ich miejsce polskie nazwy z `01_slownik_bojowy_*.md`; linia `znaczenie tagów:` podpowiada Ci, jaki to status, żeby dobrać poprawną odmianę zdania.
- **`\\n` w `widoki.zip`** oznacza celowe przejście do nowej linii na karcie lub w opisie — zostaw `\\n` w jednej linii po `PL:`.
- **Symbole `{0}`, `{1}`** to podstawiane przez grę liczby lub imiona — muszą zostać w `PL:`.
- **Piosenki (`05_muzyka_i_piosenki.md`)**: koreański oryginał używa stylu czcionki `<style="DKR_…">`, natomiast w języku polskim należy użyć łacińskiego stylu z linii `EN:` (`<style="DEN_…">` lub `<style="den…">`), wskazanego w `tokeny:`.
- Nie zmieniaj linii `źródło:` — po niej narzędzie importujące bezbłędnie trafia we właściwe pole pliku JSON gry (także dla połączonych poziomów ulepszeń 1–4).
"""

    return f"""# Limbus Company — kompletny pakiet dla tłumacza (koreański → polski), wersja {version}

## 0. W skrócie

- `sceny.zip` — **{counts['sceny']} scen fabuły w kolejności czytania**, {counts['elementy']} elementów,
  z czego **{counts['do_tlumaczenia']}** do przetłumaczenia (oraz **{counts['napisy_slownika']}** pozycji w `mowcy-i-miejsca.md`).{views_bullet}
- Źródłem jest **koreański**; `EN:` to oficjalna wersja angielska jako odniesienie.
- Polski tekst wpisujesz zawsze w **jednej linii** po `PL:`. Nic innego w pliku nie zmieniasz.

## 1. Sceny fabularne (`sceny.zip`)

```text
14. [Dialog - 카론 (Charon)] 베르.
   miejsce: 메피스토펠레스 내부 — Aboard Mephistopheles
   limit: do {counts['limit_kwestii']} znaków
   EN: Verg.
   PL: Werg.
```

- Każda scena zaczyna się od `## Scena N/{counts['sceny']} — <plik>` i pełnej metryki kontekstowej: rozdział, miejsce w rozdziale, etap, moment (przed walką / w trakcie walki / po walce / eksploracja), sąsiednie sceny, uczestnicy i miejsca (`spis-rozdzialow.md`, `spis-scen.md`).
- `[Dialog - mówca]` — kto mówi; `[Narracja]` — narrator (najczęściej Dante).
- `miejsce:` / `tytuł mówcy:` — kontekst w scenie; same napisy tłumaczysz raz w `mowcy-i-miejsca.md`.
- W `sceny.zip` ukośnik ` / ` oznacza łamanie linii w dymku; okno dialogowe gry samo zawija wiersze.
- `(powtórzenie elementu N…)` — ta sama kwestia była już wcześniej w tym pliku; nic nie wpisujesz.
{views_section}
## 3. Zasady wspólne

- Kwestie Dantego w nawiasach `<…>` to tykanie zegara, które słyszą tylko Grzesznicy — nawiasy `<…>` zostają w `PL:`.
- Znaczniki formatowania TextMeshPro (`<i>`, `</i>`, `<color=…>`, `</color>`, `<ruby=…>`) muszą zostać w tekście.
- Imiona i nazwy własne: według słowniczka projektu; w razie wątpliwości zostaw jak w EN i dopisz `[?]`.

## 4. Co odesłać

Te same pliki `.md` z wypełnionymi polami `PL:` (możesz odsyłać partiami — dowolny podzbiór plików z `sceny.zip` i/lub `widoki.zip`), spakowane w ZIP bez zmiany nazw plików.
"""


def pack_zip_bytes(files: dict[str, str]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[name].encode("utf-8"))
    return buf.getvalue()


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
    parser.add_argument("--static-data", type=Path, default=ROOT / "index" / "static-data",
                        help="StaticData directory for Identity/skill/passive context (default: index/static-data)")
    parser.add_argument("--version", type=int, default=1)
    parser.add_argument("--out", type=Path, default=ROOT / "local" / "pakiet")
    parser.add_argument("--only", action="append", type=int, help="sub-chapter id(s) (story-only sample package)")
    parser.add_argument("--no-views", action="store_true", help="omit widoki.zip (build story scenes only)")
    args = parser.parse_args(argv)

    index = json.loads(args.index.read_text(encoding="utf-8"))
    include_views = not args.no_views and not args.only
    if args.only:
        index = {**index, "rozdzialy": [c for c in index["rozdzialy"] if c["id"] in args.only],
                 "identity": [], "nieprzypisane": []}

    static = StaticData(args.static_data) if include_views and args.static_data and args.static_data.exists() else None
    with Snapshot.open(args.snapshot) as snapshot:
        scene_files, counts = build(index, Story(snapshot))
        payload: dict[str, bytes] = {"sceny.zip": pack_zip_bytes(scene_files)}
        if include_views:
            view_files, view_stats = build_views(snapshot, static)
            payload["widoki.zip"] = pack_zip_bytes(view_files)
            counts.update(view_stats)
            counts["lacznie_elementy"] = counts["elementy"] + counts["widoki_elementy"]
            counts["lacznie_do_tlumaczenia"] = (
                counts["do_tlumaczenia"] + counts["napisy_slownika"] + counts["widoki_do_tlumaczenia"]
            )

    payload["README.md"] = readme(args.version, counts).encode("utf-8")
    args.out.mkdir(parents=True, exist_ok=True)
    target = args.out / f"plik_dla_tlumacza_v{args.version}.zip"
    write_zip(target, payload)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(json.dumps({**counts, "plik": str(target), "bajty": target.stat().st_size, "sha256": digest},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
