#!/usr/bin/env python3
"""Validate a Limbus Company collector return ZIP without extracting it.

Prints aggregate counts only (no game text, no paths beyond fixed names).
Run it on an archive kept in ignored local/ or google_drive/. Hashes prove
consistency with the accompanying RAPORT.json, not origin or completeness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile


FORMAT = "lcb-zbieracz-v1"
MAX_ARCHIVE_BYTES = 200 * 1024 * 1024
MAX_EXPANDED_BYTES = 1024 * 1024 * 1024
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_MEMBERS = 50_000
MAX_INVENTORY_ROWS = 250_000
REPORT_MEMBERS = ("RAPORT.json", "RAPORT.txt", "INWENTARZ.jsonl")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
LOCALIZE_MEMBER = re.compile(r"^Localize/[A-Za-z]{2,8}/(?:[^/]+/)*[^/]+\.json$")
KINDS = {"localize", "lang_config", "app_info"}
STATUSES = {"complete", "partial"}


class InvalidReturn(ValueError):
    """A malformed or inconsistent collector return (no private data in message)."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidReturn(message)


def unique_dict(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON field")
        result[key] = value
    return result


def decode_json(data: bytes) -> object:
    try:
        return json.loads(data.decode("utf-8-sig"), object_pairs_hook=unique_dict)
    except (UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise InvalidReturn("invalid JSON or UTF-8") from exc


def safe_member(name: str) -> bool:
    if not name or "\\" in name or ":" in name or "\x00" in name or name.startswith("/"):
        return False
    return all(part not in ("", ".", "..") for part in name.split("/"))


def nonnegative_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def kind_matches(kind: str, path: str) -> bool:
    if kind == "localize":
        return bool(LOCALIZE_MEMBER.match(path))
    if kind == "lang_config":
        return path == "Lang/config.json"
    return path == "app.info"


def validate(path: Path) -> dict[str, object]:
    require(path.is_file(), "archive is not a file")
    require(path.stat().st_size <= MAX_ARCHIVE_BYTES, "archive exceeds intake limit")
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile as exc:
        raise InvalidReturn("not a ZIP archive") from exc
    with archive:
        infos = archive.infolist()
        require(len(infos) <= MAX_MEMBERS, "too many members")
        names = [info.filename for info in infos]
        require(len(set(names)) == len(names), "duplicate member names")
        expanded = 0
        for info in infos:
            require(safe_member(info.filename) and not info.is_dir(), "unsafe member name")
            require(info.file_size <= MAX_MEMBER_BYTES, "member exceeds size limit")
            require(info.flag_bits & 0x1 == 0, "encrypted member")
            expanded += info.file_size
        require(expanded <= MAX_EXPANDED_BYTES, "expanded size exceeds limit")
        for required in REPORT_MEMBERS:
            require(required in names, f"missing {required}")

        report = decode_json(archive.read("RAPORT.json"))
        require(isinstance(report, dict), "report is not an object")
        require(report.get("format") == FORMAT, "unknown report format")
        require(report.get("status") in STATUSES, "unknown status")
        files = report.get("files")
        require(isinstance(files, list), "files is not a list")

        declared: dict[str, dict[str, object]] = {}
        by_kind = {kind: 0 for kind in KINDS}
        languages: dict[str, int] = {}
        payload = 0
        for item in files:
            require(isinstance(item, dict), "file entry is not an object")
            member = item.get("path")
            kind = item.get("kind")
            require(isinstance(member, str) and safe_member(member), "unsafe declared path")
            require(member not in declared, "duplicate declared path")
            require(kind in KINDS and kind_matches(str(kind), member), "unexpected kind or path")
            require(nonnegative_int(item.get("size")), "invalid size")
            require(isinstance(item.get("sha256"), str) and SHA256.match(str(item["sha256"])), "invalid sha256")
            require(member in names, "declared file missing from archive")
            info = archive.getinfo(member)
            require(info.file_size == item["size"], "size mismatch")
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            require(digest.hexdigest() == item["sha256"], "sha256 mismatch")
            declared[member] = item
            by_kind[str(kind)] += 1
            payload += int(item["size"])
            if kind == "localize":
                lang = PurePosixPath(member).parts[1].lower()
                languages[lang] = languages.get(lang, 0) + 1

        extra = set(names) - set(declared) - set(REPORT_MEMBERS)
        require(not extra, "archive contains undeclared members")

        inventory = report.get("inventory")
        require(isinstance(inventory, dict) and nonnegative_int(inventory.get("entries")), "invalid inventory block")
        rows = 0
        with archive.open("INWENTARZ.jsonl") as handle:
            for raw in handle:
                if not raw.strip():
                    continue
                row = decode_json(raw)
                require(isinstance(row, dict) and set(row) == {"p", "s", "t"}, "invalid inventory row")
                require(isinstance(row["p"], str) and safe_member(row["p"]), "unsafe inventory path")
                require(nonnegative_int(row["s"]), "invalid inventory size")
                rows += 1
                require(rows <= MAX_INVENTORY_ROWS, "inventory too long")
        require(rows == inventory["entries"], "inventory count mismatch")

        problems = report.get("problems")
        skipped = report.get("skipped")
        require(isinstance(problems, list) and isinstance(skipped, list), "invalid problems/skipped")
        steam = (report.get("game") or {}).get("steam") or {}
        buildid = steam.get("buildid") if isinstance(steam, dict) else ""
        return {
            "validation": "passed",
            "format": FORMAT,
            "status": report["status"],
            "tool_version": report.get("tool_version"),
            "steam_buildid": buildid or None,
            "files": len(declared),
            "files_by_kind": by_kind,
            "localize_files_by_language": dict(sorted(languages.items())),
            "payload_bytes": payload,
            "inventory_rows": rows,
            "problems": len(problems),
            "skipped": len(skipped),
            "archive_bytes": path.stat().st_size,
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("archive", type=Path)
    args = parser.parse_args(argv)
    try:
        summary = validate(args.archive)
    except InvalidReturn as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
