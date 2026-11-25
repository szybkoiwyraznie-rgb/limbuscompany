#!/usr/bin/env python3
"""First-look investigation of a Limbus Company Localize snapshot.

Reads a validated collector return ZIP (or a directory with Localize/<lang>/)
and writes a *private* JSON report (default: local/inspekcja/<name>.json)
describing the corpus shape: files per language, JSON layouts, string fields,
cross-language pairing, id problems, StoryData naming groups and volume
estimates. Standard output carries aggregate counts only, never game text.

The report is a research aid for docs/FORMAT_LOCALIZE.md, not an extractor:
it decides nothing about which fields are translatable.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path, PurePosixPath
import re
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.localize import Snapshot, field_name, iter_strings, load_json


ROOT = Path(__file__).resolve().parent.parent
WORD = re.compile(r"\w+", re.UNICODE)
STORY_DIR = "StoryData"
DUPLICATE_ID = re.compile(r"\[\w+=[^\]]*#\d+\]")


def shape(value: object) -> str:
    if isinstance(value, dict):
        keys = sorted(value)
        return "object:" + ",".join(keys[:6]) + (",…" if len(keys) > 6 else "")
    return type(value).__name__


def group_of(logical: str) -> str:
    parts = PurePosixPath(logical).parts
    return parts[0] if len(parts) > 1 else "(główny)"


def story_group(logical: str) -> str:
    """Coarse naming group of a StoryData file, e.g. ``1D101A`` -> ``<cyfra>D``."""
    stem = PurePosixPath(logical).stem
    match = re.match(r"^(\d+)([A-Za-z]+)", stem)
    if match:
        return "<cyfra>" + match.group(2)[:1].upper()
    match = re.match(r"^([A-Za-z]+)", stem)
    return (match.group(1)[:2] if match else "?") + "…"


def inspect(source: Path, samples: int = 0) -> dict[str, object]:
    with Snapshot.open(source) as snap:
        languages = snap.languages
        all_paths = sorted(set().union(*(snap.files[lang] for lang in languages))) if languages else []
        per_lang: dict[str, dict[str, object]] = {}
        addresses: dict[str, dict[str, set[str]]] = {lang: {} for lang in languages}
        fields: dict[str, Counter[str]] = {lang: Counter() for lang in languages}
        groups: dict[str, Counter[str]] = {}
        story_fields: Counter[str] = Counter()
        story_groups: Counter[str] = Counter()
        sample_rows: list[dict[str, str]] = []
        for lang in languages:
            stats = {
                "files": 0, "bytes": 0, "parse_errors": 0, "bom_files": 0,
                "string_leaves": 0, "empty_strings": 0, "chars": 0, "words": 0,
                "duplicate_ids": 0, "top_level": Counter(),
            }
            for logical in sorted(snap.files[lang]):
                data = snap.read(lang, logical)
                stats["files"] += 1
                stats["bytes"] += len(data)
                stats["bom_files"] += int(data.startswith(b"\xef\xbb\xbf"))
                groups.setdefault(group_of(logical), Counter())[lang] += 1
                try:
                    obj = load_json(data)
                except (UnicodeError, json.JSONDecodeError):
                    stats["parse_errors"] += 1
                    continue
                stats["top_level"][shape(obj)] += 1
                found: set[str] = set()
                for address, text in iter_strings(obj):
                    name = field_name(address)
                    if name == "id":
                        continue
                    if DUPLICATE_ID.search(address):
                        stats["duplicate_ids"] += 1
                    found.add(address)
                    stats["string_leaves"] += 1
                    stats["empty_strings"] += int(not text.strip())
                    stats["chars"] += len(text)
                    stats["words"] += len(WORD.findall(text))
                    fields[lang][name] += 1
                    if lang == "en" and logical.startswith(STORY_DIR + "/"):
                        story_fields[name] += 1
                    if samples and lang == "en" and len(sample_rows) < samples and text.strip():
                        sample_rows.append({"file": logical, "address": address, "text": text[:200]})
                addresses[lang][logical] = found
                if lang == "en" and logical.startswith(STORY_DIR + "/"):
                    story_groups[story_group(logical)] += 1
            stats["top_level"] = dict(stats["top_level"].most_common())
            per_lang[lang] = stats

        pairing = {
            "logical_files": len(all_paths),
            "in_all_languages": sum(all(p in snap.files[l] for l in languages) for p in all_paths),
            "only_in": {
                lang: sum(p in snap.files[lang] and all(p not in snap.files[o] for o in languages if o != lang) for p in all_paths)
                for lang in languages
            },
            "missing_in": {lang: sum(p not in snap.files[lang] for p in all_paths) for lang in languages},
        }
        alignment: dict[str, dict[str, int]] = {}
        if "en" in addresses:
            for other in languages:
                if other == "en":
                    continue
                only_en = only_other = shared = 0
                for logical, found in addresses["en"].items():
                    theirs = addresses[other].get(logical)
                    if theirs is None:
                        continue
                    shared += len(found & theirs)
                    only_en += len(found - theirs)
                    only_other += len(theirs - found)
                alignment[f"en~{other}"] = {"shared": shared, "only_en": only_en, f"only_{other}": only_other}

        report: dict[str, object] = {
            "format": "lcb-inspekcja-v1",
            "languages": languages,
            "per_language": per_lang,
            "pairing": pairing,
            "address_alignment": alignment,
            "groups": {g: dict(c) for g, c in sorted(groups.items())},
            "string_fields": {lang: dict(c.most_common(80)) for lang, c in fields.items()},
            "story": {
                "directory": STORY_DIR,
                "files_en": sum(story_groups.values()),
                "naming_groups_en": dict(story_groups.most_common()),
                "fields_en": dict(story_fields.most_common()),
            },
        }
        if samples:
            report["samples_en"] = sample_rows
        return report


def summary(report: dict[str, object]) -> dict[str, object]:
    per = report["per_language"]  # type: ignore[index]
    return {
        "languages": report["languages"],
        "files": {lang: per[lang]["files"] for lang in per},  # type: ignore[index]
        "parse_errors": {lang: per[lang]["parse_errors"] for lang in per},  # type: ignore[index]
        "string_leaves": {lang: per[lang]["string_leaves"] for lang in per},  # type: ignore[index]
        "words": {lang: per[lang]["words"] for lang in per},  # type: ignore[index]
        "pairing": report["pairing"],
        "groups": len(report["groups"]),  # type: ignore[arg-type]
        "story_files_en": report["story"]["files_en"],  # type: ignore[index]
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", type=Path, help="collector ZIP or directory with Localize/")
    parser.add_argument("--out", type=Path, help="private report path (default under local/inspekcja/)")
    parser.add_argument("--probki", type=int, default=0, help="add N English text samples to the private report")
    args = parser.parse_args(argv)
    out = args.out or ROOT / "local" / "inspekcja" / (args.source.stem + ".json")
    report = inspect(args.source, samples=args.probki)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary(report), ensure_ascii=False, indent=2))
    print(f"Pełny (prywatny) raport: {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
