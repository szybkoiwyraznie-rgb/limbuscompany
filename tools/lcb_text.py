#!/usr/bin/env python3
"""Shared helpers for reading Limbus Company ``Localize`` tables in one language.

``Texts`` wraps a ``Snapshot`` (collector ZIP or directory with ``<lang>/``
files) and exposes ``dataList`` tables by logical name (``StageNode1-1.json``),
merged families (``StageNode*``), story scenes and speaker names.
``to_markdown`` turns game markup (TextMeshPro tags, ``[Keyword]`` tokens)
into readable Markdown for the Czytanki and profiles.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import PurePosixPath
import re

from tools.localize import Snapshot, load_json


class Texts:
    """Localize tables of one language of a snapshot."""

    def __init__(self, snapshot: Snapshot, lang: str) -> None:
        if lang not in snapshot.files:
            raise KeyError(f"snapshot has no language {lang!r} (has: {', '.join(snapshot.languages)})")
        self.snapshot = snapshot
        self.lang = lang
        self._cache: dict[str, list[dict]] = {}

    def names(self) -> list[str]:
        return sorted(self.snapshot.files[self.lang])

    def table(self, logical: str) -> list[dict]:
        if logical not in self._cache:
            rows: list[dict] = []
            if logical in self.snapshot.files[self.lang]:
                data = load_json(self.snapshot.read(self.lang, logical))
                payload = data.get("dataList", []) if isinstance(data, dict) else data
                rows = [row for row in payload or [] if isinstance(row, dict)]
            self._cache[logical] = rows
        return self._cache[logical]

    def family(self, prefix: str) -> list[dict]:
        """Rows of every top-level table whose name starts with ``prefix`` (name order)."""
        rows: list[dict] = []
        for name in self.names():
            if "/" not in name and name.startswith(prefix):
                rows.extend(self.table(name))
        return rows

    def by_id(self, prefix: str, exact: bool = False) -> dict[str, dict]:
        rows = self.table(prefix) if exact else self.family(prefix)
        return {str(row.get("id")): row for row in rows if "id" in row}

    def story(self, stem: str) -> list[dict] | None:
        logical = str(PurePosixPath("StoryData") / f"{stem}.json")
        if logical not in self.snapshot.files[self.lang]:
            return None
        return self.table(logical)

    @property
    def models(self) -> dict[str, dict]:
        """Scenario model code (Korean key) → ``{name, nickName}``."""
        return self.by_id("ScenarioModelCodes")

    @property
    def keywords(self) -> dict[str, str]:
        """``[Keyword]`` token → display name (skill tags, statuses, battle keywords)."""
        if "_keywords" not in self.__dict__:
            names: dict[str, str] = {}
            for prefix in ("BattleKeywords", "Bufs", "SkillTag"):
                for key, row in self.by_id(prefix).items():
                    if isinstance(row.get("name"), str) and row["name"].strip():
                        names[key] = row["name"].strip()
            self.__dict__["_keywords"] = names
        return self.__dict__["_keywords"]


RUBY = re.compile(r"<ruby=\"?([^>\"]*)\"?>(.*?)</ruby>", re.S)
TAG_NAMES = ("i", "b", "u", "s", "color", "size", "sprite", "link", "style", "font", "mark", "align",
             "noparse", "voffset", "line-height", "cspace", "material", "sup", "sub", "nobr", "br")
TAG = re.compile(r"</?(?:" + "|".join(re.escape(t) for t in TAG_NAMES) + r")(?:[= ][^<>]*)?>", re.I)
KEYWORD = re.compile(r"\[([A-Za-z][A-Za-z0-9_]*)\]")


def to_markdown(text: object, keywords: dict[str, str] | None = None) -> str:
    """Game markup → Markdown: italics/bold kept, colours/sizes dropped, ruby as ``base (reading)``,
    ``[Keyword]`` resolved to its display name, other ``<…>`` (e.g. Dante's ticking) shown literally."""
    if not isinstance(text, str):
        return ""
    out = RUBY.sub(lambda m: f"{m[2]} ({m[1]})" if m[1] else m[2], text)

    def tag(match: re.Match) -> str:
        raw = match[0].lower()
        if raw in ("<i>", "</i>"):
            return "*"
        if raw in ("<b>", "</b>"):
            return "**"
        if raw.startswith("<br"):
            return "\n"
        return ""

    out = TAG.sub(tag, out)
    if keywords:
        def keyword(match: re.Match) -> str:
            name = keywords.get(match[1])
            if name is None:
                return match[0]
            return name if name.startswith("[") else f"[{name}]"

        out = KEYWORD.sub(keyword, out)
    out = out.replace("\\n", "\n")
    out = out.replace("<", "\\<")
    return out.strip()


def one_line(text: str) -> str:
    return re.sub(r"\s*\n\s*", " ", text).strip()


@lru_cache(maxsize=None)
def stage_label(node: int) -> str | None:
    """``1CCNN`` → ``C-N``; ``91CCNN`` / ``90CCNN`` → ``N`` (number inside the chapter)."""
    text = str(node)
    if len(text) == 5 and text[0] == "1":
        return f"{int(text[1:3])}-{int(text[3:])}"
    if len(text) == 6 and text[:2] in ("90", "91"):
        return str(int(text[4:]))
    return None
