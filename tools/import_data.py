#!/usr/bin/env python3
"""Copy game text files (JSON) into ``index/`` — the versioned source of every build.

``index/localize/<lang>/``  Localize files exactly as the game ships them
                           (``KR_…``/``EN_…`` names, BOM kept, bytes unchanged);
``index/static-data/<table>/``  the StaticData tables the tools read (story
                           theater, stages, battles, Identities, skills, passives);
``index/MANIFEST.json``     where the files came from, counts and SHA-256.

Only JSON is copied — never bundles, executables or other binaries (D-06).
Re-running replaces the copied languages/tables completely, so ``git diff``
shows exactly what changed between two versions of the game.

Sources: a collector ZIP (``LCB_DANE_*.zip``), a directory with ``<lang>/``
(e.g. a public mirror) and a ``static-data`` directory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
import zipfile

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "index"
STATIC_TABLES = ("storytheater-main", "storytheater-other", "storytheater-personality", "storytheater-mirrorworld",
                 "story", "battle-story", "battle-ab", "RPGSystem", "personality", "skill", "personality-passive",
                 "passive", "enemy", "abnormality-unit", "abnormality-part")


def _localize_members(source: Path, lang: str) -> list[tuple[str, bytes]]:
    """``(relative path inside the language folder, bytes)`` for every JSON of ``lang``."""
    out: list[tuple[str, bytes]] = []
    if source.is_file():
        with zipfile.ZipFile(source) as archive:
            for info in archive.infolist():
                parts = PurePosixPath(info.filename).parts
                if info.is_dir() or len(parts) < 3 or parts[0] != "Localize" or parts[1].lower() != lang:
                    continue
                if parts[-1].lower().endswith(".json"):
                    out.append(("/".join(parts[2:]), archive.read(info)))
    else:
        base = source / "Localize" if (source / "Localize").is_dir() else source
        folder = next((p for p in base.iterdir() if p.is_dir() and p.name.lower() == lang), None)
        if folder is None:
            raise FileNotFoundError(f"no {lang}/ in {base}")
        for path in sorted(folder.rglob("*.json")):
            out.append((path.relative_to(folder).as_posix(), path.read_bytes()))
    return sorted(out)


def _replace(target: Path, files: list[tuple[str, bytes]]) -> dict:
    if target.exists():
        shutil.rmtree(target)
    digest = hashlib.sha256()
    total = 0
    for relative, data in files:
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        digest.update(relative.encode("utf-8") + b"\0" + hashlib.sha256(data).digest())
        total += len(data)
    return {"pliki": len(files), "bajty": total, "sha256": digest.hexdigest()}


def import_localize(source: Path, langs: list[str], out: Path) -> dict[str, dict]:
    return {lang: _replace(out / "localize" / lang, _localize_members(source, lang)) for lang in langs}


def import_static(source: Path, out: Path, tables: tuple[str, ...] = STATIC_TABLES) -> dict[str, dict]:
    base = source
    for candidate in (source, source / "static-data", source / "StaticData" / "static-data"):
        if (candidate / "personality").is_dir() or (candidate / "storytheater-main").is_dir():
            base = candidate
            break
    result = {}
    for table in tables:
        folder = base / table
        if not folder.is_dir():
            continue
        files = [(p.relative_to(folder).as_posix(), p.read_bytes()) for p in sorted(folder.rglob("*.json"))]
        result[table] = _replace(out / "static-data" / table, files)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--localize", type=Path, help="collector ZIP or directory with <lang>/")
    parser.add_argument("--langs", nargs="+", default=["kr", "en"])
    parser.add_argument("--localize-source", default="", help="description, e.g. 'TW story-data f218bbec'")
    parser.add_argument("--static-data", type=Path, help="static-data directory")
    parser.add_argument("--static-source", default="", help="description of the StaticData source")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    if not args.localize and not args.static_data:
        parser.error("nothing to import: pass --localize and/or --static-data")
    manifest_path = args.out / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    manifest["format"] = "lcb-index-v1"
    if args.localize:
        manifest["localize"] = {"zrodlo": args.localize_source or args.localize.name,
                                "jezyki": import_localize(args.localize, args.langs, args.out)}
    if args.static_data:
        manifest["static_data"] = {"zrodlo": args.static_source or args.static_data.name,
                                   "tabele": import_static(args.static_data, args.out)}
    args.out.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in manifest.items() if k != "format"}, ensure_ascii=False)[:2000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
