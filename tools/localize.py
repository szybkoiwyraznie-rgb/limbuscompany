#!/usr/bin/env python3
"""Shared readers for Limbus Company Localize snapshots (no game data inside).

A snapshot is either a collector return ZIP (``Localize/<lang>/...``) or a
directory containing ``Localize/<lang>/...`` (or the language folders
directly). File names carry a language prefix (``EN_``, ``KR_``, ``JP_``) that
the game's custom-language loader expects to be removed; the *logical path*
used everywhere in this project is the path below the language folder with
that prefix stripped, e.g. ``StoryData/1D101A.json``.

Text addresses are built from ``id`` fields instead of list positions so that
an inserted entry does not shift every later address after a game update.
"""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
import json
from pathlib import Path, PurePosixPath
import re
import zipfile


PREFIX = re.compile(r"^(?:EN|KR|JP)_")
KNOWN_LANGUAGES = ("en", "kr", "jp")


def strip_prefix(name: str) -> str:
    """Remove the official language prefix from a file name (not from folders)."""
    return PREFIX.sub("", name, count=1)


def logical_path(relative: str) -> str:
    parts = PurePosixPath(relative).parts
    if not parts:
        raise ValueError("empty path")
    return "/".join((*parts[:-1], strip_prefix(parts[-1])))


def load_json(data: bytes) -> object:
    return json.loads(data.decode("utf-8-sig"))


def _id_label(value: object) -> str | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, str)):
        return str(value)
    return None


IDENTIFIER_FIELDS = ("id", "key", "level", "abilityID")


def _identifier(item: dict) -> tuple[str, str] | None:
    for name in IDENTIFIER_FIELDS:
        label = _id_label(item.get(name))
        if label is not None:
            return name, label
    return None


def list_row_steps(items: list) -> list[tuple[str, object]]:
    """Return ``(step, item)`` pairs using the exact addressing rules of ``iter_strings``."""
    seen: dict[str, int] = {}
    out: list[tuple[str, object]] = []
    for index, item in enumerate(items):
        ident = _identifier(item) if isinstance(item, dict) else None
        if ident is None:
            step = f"[#{index}]"
        else:
            label = f"{ident[0]}={ident[1]}"
            seen[label] = seen.get(label, 0) + 1
            step = f"[{label}]" if seen[label] == 1 else f"[{label}#{seen[label]}]"
        out.append((step, item))
    return out


def iter_strings(node: object, path: str = "") -> Iterator[tuple[str, str]]:
    """Yield ``(address, text)`` for every string leaf of a JSON value.

    Dict members become ``.key``; list items that are objects with a scalar
    identifier become ``[field=X]`` using the first of ``IDENTIFIER_FIELDS``
    present (``id``, then ``key``, ``level``, ``abilityID``; repeats get
    ``#2``, ``#3``...), other items ``[#i]``. Positional ``[#i]`` addresses
    shift when the game inserts rows (seen by other translation teams), so
    they are the last resort. ``id`` values themselves are yielded too, under ``.id``; callers
    decide which fields are translatable.
    """
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for key, value in node.items():
            yield from iter_strings(value, f"{path}.{key}" if path else str(key))
    elif isinstance(node, list):
        for step, item in list_row_steps(node):
            yield from iter_strings(item, path + step)


def transform_strings(
    node: object,
    updates: dict[str, str],
    path: str = "",
) -> tuple[object, set[str]]:
    """Return a copy of ``node`` with string leaves at ``updates`` replaced, plus matched addresses."""
    if isinstance(node, str):
        if path in updates:
            return updates[path], {path}
        return node, set()
    if isinstance(node, dict):
        out_dict: dict = {}
        applied: set[str] = set()
        for key, value in node.items():
            child_path = f"{path}.{key}" if path else str(key)
            if key in IDENTIFIER_FIELDS and child_path in updates:
                raise ValueError(f"cannot overwrite identifier field {child_path}")
            new_val, child_applied = transform_strings(value, updates, child_path)
            out_dict[key] = new_val
            applied |= child_applied
        return out_dict, applied
    if isinstance(node, list):
        out_list: list = []
        applied = set()
        for step, item in list_row_steps(node):
            new_item, item_applied = transform_strings(item, updates, path + step)
            out_list.append(new_item)
            applied |= item_applied
        return out_list, applied
    return node, set()


def field_name(address: str) -> str:
    """Last object key of an address (``dataList[id=3].content`` -> ``content``)."""
    tail = address.rsplit(".", 1)[-1]
    return tail.split("[", 1)[0]


@dataclass
class Snapshot:
    """Read-only view of Localize files grouped by language and logical path."""

    source: Path
    files: dict[str, dict[str, str]] = field(default_factory=dict)
    _zip: zipfile.ZipFile | None = None

    @classmethod
    def open(cls, source: Path) -> "Snapshot":
        snapshot = cls(source=source)
        if source.is_file():
            snapshot._zip = zipfile.ZipFile(source)
            names = [i.filename for i in snapshot._zip.infolist() if not i.is_dir()]
            snapshot._index(names, base="Localize/")
        elif source.is_dir():
            base = source / "Localize" if (source / "Localize").is_dir() else source
            names = [p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file()]
            snapshot._index(names, base="", root=base)
        else:
            raise FileNotFoundError(str(source))
        return snapshot

    def _index(self, names: list[str], base: str, root: Path | None = None) -> None:
        self._root = root
        for name in sorted(names):
            if base and not name.startswith(base):
                continue
            relative = name[len(base):]
            parts = relative.split("/")
            if len(parts) < 2 or not relative.lower().endswith(".json"):
                continue
            lang = parts[0].lower()
            logical = logical_path("/".join(parts[1:]))
            bucket = self.files.setdefault(lang, {})
            if logical in bucket:
                raise ValueError(f"two files map to one logical path in {lang}")
            bucket[logical] = name

    @property
    def languages(self) -> list[str]:
        known = [lang for lang in KNOWN_LANGUAGES if lang in self.files]
        return known + sorted(set(self.files) - set(known))

    def read(self, lang: str, logical: str) -> bytes:
        name = self.files[lang][logical]
        if self._zip is not None:
            return self._zip.read(name)
        assert self._root is not None
        return (self._root / name).read_bytes()

    def close(self) -> None:
        if self._zip is not None:
            self._zip.close()

    def __enter__(self) -> "Snapshot":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
