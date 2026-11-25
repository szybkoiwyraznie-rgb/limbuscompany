#!/usr/bin/env python3
"""Read-only access to a Limbus Company ``StaticData/static-data`` tree.

StaticData holds the game's structural tables (story theater lists, stages,
battles, Identities, skills). It contains numbers and identifiers, not
localized text; the text lives in ``Localize`` (``tools/localize.py``).

Each table folder contains one or more JSON files (sometimes one level deeper,
``folder/name/name.json``). Most files are ``{"list": [...]}``; a few use a
different top-level key. ``rows`` merges all list-like payloads of a folder in
file-name order.
"""
from __future__ import annotations

import json
from pathlib import Path
import re

if __package__ in (None, ""):
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.localize import load_json

TRAILING_COMMA = re.compile(r",(\s*[}\]])")


def load_lenient(data: bytes) -> object:
    """JSON as the game reads it: a few shipped files have trailing commas."""
    try:
        return load_json(data)
    except json.JSONDecodeError:
        return json.loads(TRAILING_COMMA.sub(r"\1", data.decode("utf-8-sig")))


class StaticData:
    """A ``static-data`` directory (the folder holding ``personality/``, ``skill/``…)."""

    def __init__(self, root: Path) -> None:
        root = Path(root)
        for candidate in (root, root / "static-data", root / "StaticData" / "static-data"):
            if (candidate / "personality").is_dir() or (candidate / "storytheater-main").is_dir():
                self.root = candidate
                break
        else:
            raise FileNotFoundError(f"no static-data tables under {root}")
        self.skipped: list[str] = []

    def files(self, folder: str) -> list[Path]:
        base = self.root / folder
        if not base.is_dir():
            return []
        return sorted(base.rglob("*.json"), key=lambda p: p.relative_to(base).as_posix())

    def documents(self, folder: str) -> list[tuple[Path, object]]:
        out = []
        for path in self.files(folder):
            try:
                out.append((path, load_lenient(path.read_bytes())))
            except json.JSONDecodeError as error:
                self.skipped.append(f"{path.relative_to(self.root).as_posix()}: {error}")
        return out

    def rows(self, folder: str, key: str | None = None) -> list[dict]:
        """All dict rows of ``folder``; ``key`` picks the list (default: ``list`` or the only list)."""
        out: list[dict] = []
        for _, doc in self.documents(folder):
            if isinstance(doc, list):
                payload = doc
            elif isinstance(doc, dict):
                if key is not None:
                    payload = doc.get(key, [])
                elif isinstance(doc.get("list"), list):
                    payload = doc["list"]
                else:
                    lists = [v for v in doc.values() if isinstance(v, list)]
                    payload = lists[0] if len(lists) == 1 else []
            else:
                payload = []
            out.extend(row for row in payload if isinstance(row, dict))
        return out
