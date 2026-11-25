#!/usr/bin/env python3
"""Build the story index (reading order of StoryData scenes) from the game's own tables.

Inputs:

* ``StaticData/static-data`` (``tools/static_data.py``): the in-game Story
  Theater lists (``storytheater-main`` = Cantos, ``storytheater-other`` =
  Intervallos and side stories, with ``sortingOrder`` and unlock conditions),
  stage→scene links (``story``), battle scripts with mid-battle scenes
  (``battle-story``, ``battle-ab``: ``enter`` → ``others`` → ``exit``) and
  Identity stories (``storytheater-personality``);
* a ``Localize`` snapshot (``tools/localize.py``): ``StageChapterText`` gives the
  official chapter sequence (with in-world dates), ``StoryData`` the list of
  scene files.

Output (default ``wiedza/indeks_fabuly.json``) holds **identifiers only**:
sub-chapter numbers, stage (node) ids, battle ids, scene file stems and stage
phases. Titles and dialogue are resolved later from ``Localize`` by the
readers/packagers, so the index may be committed.

Ordering rules (each one is data-driven; nothing is guessed from text):

1. Intervallos and side stories keep the game's ``sortingOrder``.
2. Each main Canto is inserted before the first of those that, according to
   ``StageChapterText`` or an unlock condition, comes after it.
3. Inside a sub-chapter scenes follow the Story Theater list; stage→scene
   links missing from it (current Canto) are merged by stage id; mid-battle
   scenes go right after the battle's opening scene (or before its closing one).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.localize import Snapshot, load_json
from tools.static_data import StaticData


ROOT = Path(__file__).resolve().parent.parent
FORMAT = "lcb-indeks-fabuly-v1"
DEFAULT_OUT = ROOT / "wiedza" / "indeks_fabuly.json"
GROUPS = {1: "canto", 91: "intervallo", 90: "opowiadanie"}
PHASES = {"Before": "przed", "After": "po", "Inter": "w trakcie", None: None}
BATTLE_PHASE = "walka"


STEM = re.compile(r"^(?P<group>S|E|ES|PC|P|\d+D)(?P<number>\d+)(?P<phase>[A-Z]?)(?P<step>\d*)$")
PHASE_RANK = {"B": 0, "I": 1, "": 1, "A": 2, "C": 3, "X": 4}
GROUP_RANK = {"S": 0, "D": 1, "E": 2, "ES": 3, "PC": 4, "P": 5}


def story_sort_key(stem: str) -> tuple:
    """Naming rule: S < nD < E < ES < PC < P; then number; then phase B < I(n) < A < C < X."""
    match = STEM.match(stem)
    if not match:
        return (9, 0, 9, 0, stem)
    group = match["group"]
    dungeon = group.endswith("D") and group[:-1].isdigit()
    rank = GROUP_RANK["D"] if dungeon else GROUP_RANK[group]
    chapter = int(group[:-1]) if dungeon else 0
    return (rank, chapter * 10**6 + int(match["number"]), PHASE_RANK.get(match["phase"], 5),
            int(match["step"] or 0), stem)


def family(stem: str) -> str | None:
    """Scenes of one family belong to one chapter: S+Canto, nD, E+digit (not X), ES, PC."""
    match = STEM.match(stem)
    if not match or match["phase"] == "X":
        return None
    group, number = match["group"], match["number"]
    if group == "S":
        return "S" + number[:-2] if len(number) > 2 else "S0"
    if group.endswith("D"):
        return group
    if group == "E":
        return "E" + number[0]
    return group if group in ("ES", "PC") else None


def sub_of_node(node: int) -> int | None:
    """Stage id → sub-chapter: ``1CCNN`` → ``1CC``, ``91CCNN``/``90CCNN`` → ``91CC``/``90CC``."""
    text = str(node)
    if len(text) == 5 and text[0] == "1":
        return int(text[:3])
    if len(text) == 6 and text[:2] in ("90", "91"):
        return int(text[:4])
    return None


def chapter_sequence(snapshot: Snapshot) -> list[int]:
    for lang in ("kr", "en", "jp"):
        if "StageChapterText.json" in snapshot.files.get(lang, {}):
            data = load_json(snapshot.read(lang, "StageChapterText.json"))
            seq: list[int] = []
            for row in data.get("dataList", []) if isinstance(data, dict) else []:
                match = re.search(r"_(\d+)$", str(row.get("id", "")))
                if match and int(match[1]) not in seq:
                    seq.append(int(match[1]))
            return seq
    return []


def story_stems(snapshot: Snapshot) -> set[str]:
    stems = set()
    for files in snapshot.files.values():
        for logical in files:
            path = PurePosixPath(logical)
            if len(path.parts) == 2 and path.parts[0] == "StoryData":
                stems.add(path.stem)
    return stems


def _scene(story_id: str, phase: str | None, node: object = None, **extra: object) -> dict:
    scene = {"plik": story_id, "etap": PHASES.get(phase, phase)}
    if isinstance(node, int):
        scene["wezel"] = node
    scene.update({k: v for k, v in extra.items() if v is not None})
    return scene


def collect_chapters(static: StaticData) -> dict[int, dict]:
    chapters: dict[int, dict] = {}
    for folder in ("storytheater-main", "storytheater-other"):
        for row in static.rows(folder):
            sub = row.get("subChapterId")
            if not isinstance(sub, int):
                continue
            chapter = chapters.setdefault(sub, {
                "id": sub,
                "grupa": GROUPS.get(row.get("chapterId"), str(row.get("chapterId"))),
                "sceny": [],
            })
            if "sortingOrder" in row:
                chapter["sortingOrder"] = row["sortingOrder"]
            unlock = row.get("unLockCondition") or {}
            if isinstance(unlock.get("subChapterId"), int):
                chapter["odblokowanie"] = {k: unlock[k] for k in ("subChapterId", "nodeId") if k in unlock}
            for item in sorted(row.get("storyList", []), key=lambda s: s.get("id", 0)):
                if isinstance(item.get("storyId"), str):
                    chapter["sceny"].append(_scene(item["storyId"], item.get("stageDetail"), item.get("nodeId")))
    return chapters


def merge_stage_links(static: StaticData, chapters: dict[int, dict], placed: set[str]) -> int:
    """Add ``story`` stage→scene links that the Story Theater does not list yet."""
    added = 0
    for row in sorted(static.rows("story"), key=lambda r: (r.get("id", 0), str(r.get("storyId")))):
        story_id, node = row.get("storyId"), row.get("id")
        sub = sub_of_node(node) if isinstance(node, int) else None
        if not isinstance(story_id, str) or story_id in placed or sub is None:
            continue
        chapter = chapters.setdefault(sub, {"id": sub, "grupa": GROUPS.get(sub // 100 if sub >= 9000 else 1,
                                                                             "canto"), "sceny": []})
        phase = "After" if re.search(r"A\d*$", story_id) else "Before"
        scenes = chapter["sceny"]
        position = len(scenes)
        for i, scene in enumerate(scenes):
            if isinstance(scene.get("wezel"), int) and scene["wezel"] > node:
                position = i
                break
        scenes.insert(position, _scene(story_id, phase, node, zrodlo="story"))
        placed.add(story_id)
        added += 1
    return added


def merge_battles(static: StaticData, chapters: dict[int, dict], placed: set[str]) -> int:
    """Insert mid-battle scenes (``others``) and missing battle entry/exit scenes."""
    where: dict[str, tuple[int, int]] = {}

    def reindex() -> None:
        where.clear()
        for sub, chapter in chapters.items():
            for i, scene in enumerate(chapter["sceny"]):
                where.setdefault(scene["plik"], (sub, i))

    reindex()
    added = 0
    for folder in ("battle-story", "battle-ab"):
        for row in static.rows(folder):
            story = row.get("story")
            if not isinstance(story, dict):
                continue
            enter = [s for s in story.get("enter", []) if isinstance(s, str)]
            exit_ = [s for s in story.get("exit", []) if isinstance(s, str)]
            others = [o for o in story.get("others", []) if isinstance(o, dict) and isinstance(o.get("storyID"), str)]
            anchor_after = next((where[s] for s in reversed(enter) if s in where), None)
            anchor_before = next((where[s] for s in exit_ if s in where), None)
            battle = row.get("id")
            if anchor_after is None and anchor_before is None:
                sub = sub_of_node(battle) if isinstance(battle, int) else None
                if sub not in chapters:
                    continue
                scenes = chapters[sub]["sceny"]
                position = len(scenes)
                for i, scene in enumerate(scenes):
                    if isinstance(scene.get("wezel"), int) and scene["wezel"] > battle:
                        position = i
                        break
            else:
                sub, index = anchor_after if anchor_after else anchor_before
                position = index + 1 if anchor_after else index
            new: list[dict] = []
            if anchor_after is None:
                new += [_scene(s, "Before", None, bitwa=battle) for s in enter if s not in placed]
            new += [_scene(o["storyID"], BATTLE_PHASE, None, bitwa=battle, faza=o.get("phase"))
                    for o in others if o["storyID"] not in placed]
            if anchor_before is None:
                new += [_scene(s, "After", None, bitwa=battle) for s in exit_ if s not in placed]
            unique: list[dict] = []
            for scene in new:
                if scene["plik"] not in placed:
                    placed.add(scene["plik"])
                    unique.append(scene)
            if unique:
                chapters[sub]["sceny"][position:position] = unique
                added += len(unique)
                reindex()
    return added


def rpg_routes(static: StaticData) -> dict[str, str]:
    """Scene → ending route letter for exploration (RPG) chapters: ``RPGSystem/EndingRouteX``."""
    routes: dict[str, str] = {}

    def walk(node: object, route: str) -> None:
        if isinstance(node, dict):
            if node.get("type") == "Story" and isinstance(node.get("param"), str):
                routes.setdefault(node["param"], route)
            for value in node.values():
                walk(value, route)
        elif isinstance(node, list):
            for value in node:
                walk(value, route)

    for path, doc in static.documents("RPGSystem"):
        match = re.search(r"EndingRoute(\w+)", path.as_posix())
        walk(doc, match[1] if match else "?")
    return routes


def merge_by_name(chapters: dict[int, dict], placed: set[str], stems: set[str], routes: dict[str, str]) -> int:
    """Place leftover scene files next to the closest scene of their family (naming rule)."""
    added = 0
    for stem in sorted(stems - placed, key=story_sort_key):
        fam = family(stem)
        if fam is None:
            continue
        best: tuple | None = None
        first: tuple | None = None
        for sub, chapter in chapters.items():
            for i, scene in enumerate(chapter["sceny"]):
                if family(scene["plik"]) != fam:
                    continue
                key = story_sort_key(scene["plik"])
                if key <= story_sort_key(stem) and (best is None or key > best[0]):
                    best = (key, sub, i + 1)
                if first is None or key < first[0]:
                    first = (key, sub, i)
        target = best or first
        if target is None:
            continue
        _, sub, position = target
        chapters[sub]["sceny"].insert(position, _scene(stem, None, None, zrodlo="regula_nazw",
                                                       trasa=routes.get(stem)))
        placed.add(stem)
        added += 1
    for chapter in chapters.values():
        for scene in chapter["sceny"]:
            if scene["plik"] in routes and "trasa" not in scene:
                scene["trasa"] = routes[scene["plik"]]
    return added


def order_chapters(chapters: dict[int, dict], sequence: list[int]) -> list[int]:
    position = {sub: i for i, sub in enumerate(sequence)}

    def exact(sub: int | None) -> float | None:
        return float(position[sub]) if sub in position else None

    def after_unlock(sub: int | None) -> float | None:
        """Position of an unlock target; an unknown id sits just after the closest lower known one."""
        if sub is None or sub in position:
            return exact(sub)
        known = [s for s in position if s // 100 == sub // 100 and s < sub]
        return position[max(known)] + 0.5 if known else None

    sorted_others = sorted((c for c in chapters.values() if c["grupa"] != "canto" and "sortingOrder" in c),
                           key=lambda c: (c["sortingOrder"], c["id"]))
    order = [c["id"] for c in sorted_others]
    for chapter in sorted((c for c in chapters.values() if c["grupa"] != "canto" and "sortingOrder" not in c),
                          key=lambda c: (exact(c["id"]) or 10**6, c["id"])):
        mine = exact(chapter["id"])
        target = len(order)
        if mine is not None:
            before = [i for i, sub in enumerate(order) if exact(sub) is not None and exact(sub) < mine]
            target = before[-1] + 1 if before else 0
        order.insert(target, chapter["id"])
    start = 0
    for main in sorted(sub for sub, c in chapters.items() if c["grupa"] == "canto"):
        target = len(order)
        for i in range(start, len(order)):
            other = chapters[order[i]]
            unlock = other.get("odblokowanie", {}).get("subChapterId")
            mine = position.get(main)  # a Canto missing from StageChapterText relies on unlocks only
            later_in_sequence = mine is not None and (
                (exact(other["id"]) or -1) > mine or (after_unlock(unlock) or -1) > mine)
            unlocked_by_later_canto = unlock is not None and unlock < 1000 and unlock >= main
            if later_in_sequence or unlocked_by_later_canto:
                target = i
                break
        order.insert(target, main)
        start = target + 1
    return order


def identity_stories(static: StaticData) -> list[dict]:
    out = []
    for row in static.rows("storytheater-personality"):
        for item in row.get("storyList", []):
            stories = [s["storyId"] for s in sorted(item.get("personalityStoryList", []), key=lambda s: s.get("order", 0))
                       if isinstance(s.get("storyId"), str)]
            out.append({k: v for k, v in {
                "postac": row.get("characterId"),
                "identity": item.get("personalityId"),
                "pliki": stories,
                "profil": item.get("profileId") or None,
                "analiza": item.get("analysisId") or None,
            }.items() if v not in (None, [])})
    return sorted(out, key=lambda r: (r.get("postac", 0), r.get("identity", 0)))


def git_head(path: Path) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip() or None


def source_label(path: Path, section: str) -> str | None:
    """Where ``path`` came from: ``index/MANIFEST.json`` for imported data, else the git commit of a mirror."""
    for parent in (path, *path.parents):
        manifest = parent / "MANIFEST.json"
        if manifest.is_file():
            try:
                return json.loads(manifest.read_text(encoding="utf-8")).get(section, {}).get("zrodlo")
            except (OSError, ValueError):
                return None
        if (parent / ".git").exists():
            return git_head(parent)
    return None


def build(static: StaticData, snapshot: Snapshot) -> dict:
    chapters = collect_chapters(static)
    placed: set[str] = set()
    for chapter in chapters.values():
        unique = []
        for scene in chapter["sceny"]:
            if scene["plik"] not in placed:
                placed.add(scene["plik"])
                unique.append(scene)
        chapter["sceny"] = unique
    from_theater = len(placed)
    from_stages = merge_stage_links(static, chapters, placed)
    from_battles = merge_battles(static, chapters, placed)
    stems = story_stems(snapshot)
    from_names = merge_by_name(chapters, placed, stems, rpg_routes(static))
    sequence = chapter_sequence(snapshot)
    order = order_chapters(chapters, sequence)
    identities = identity_stories(static)
    in_identities = {s for row in identities for s in row.get("pliki", [])}
    ordered = []
    for n, sub in enumerate(order, 1):
        chapter = dict(chapters[sub])
        chapter["kolejnosc"] = n
        chapter["w_storydata"] = sum(1 for s in chapter["sceny"] if s["plik"] in stems)
        ordered.append(chapter)
    return {
        "format": FORMAT,
        "zrodla": {"static_data": source_label(static.root, "static_data"),
                   "localize": source_label(snapshot.source, "localize") if snapshot.source.is_dir() else None},
        "liczby": {
            "pliki_storydata": len(stems),
            "sceny_w_indeksie": len(placed),
            "z_teatru": from_theater,
            "z_etapow": from_stages,
            "z_walk": from_battles,
            "z_reguly_nazw": from_names,
            "sceny_bez_pliku": len(placed - stems),
            "historie_identity": len(in_identities),
            "nieprzypisane": len(stems - placed - in_identities),
        },
        "rozdzialy": ordered,
        "identity": identities,
        "nieprzypisane": sorted(stems - placed - in_identities),
    }


def dumps(index: dict) -> str:
    """Indented JSON with each scene on one line (diff-friendly)."""
    text = json.dumps(index, ensure_ascii=False, indent=1)
    text = re.sub(r"\{\n\s+(\"plik\"[^{}\[\]]*?)\n\s+\}", lambda m: "{" + re.sub(r"\n\s+", " ", m[1]) + "}", text)
    text = re.sub(r"\{\n\s+(\"postac\"[^{}]*?)\n\s+\}", lambda m: "{" + re.sub(r"\n\s+", " ", m[1]) + "}", text)
    text = re.sub(r"\[\n\s+(\"[^\"]*\"(?:,\n\s+\"[^\"]*\")*)\n\s+\]", lambda m: "[" + re.sub(r"\n\s+", " ", m[1]) + "]", text)
    return text + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("static_data", type=Path, nargs="?", default=ROOT / "index" / "static-data",
                        help="static-data tables (default: index/static-data)")
    parser.add_argument("snapshot", type=Path, nargs="?", default=ROOT / "index" / "localize",
                        help="Localize: index/localize (default), a collector ZIP or a directory with <lang>/")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    static = StaticData(args.static_data)
    with Snapshot.open(args.snapshot) as snapshot:
        index = build(static, snapshot)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(dumps(index), encoding="utf-8")
    n = index["liczby"]
    print(f"rozdziały: {len(index['rozdzialy'])}, sceny: {n['sceny_w_indeksie']} (teatr {n['z_teatru']}, "
          f"etapy {n['z_etapow']}, walki {n['z_walk']}, reguła nazw {n['z_reguly_nazw']}), historie Identity: {n['historie_identity']}, "
          f"nieprzypisane: {n['nieprzypisane']} z {n['pliki_storydata']}")
    print(f"zapisano {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
