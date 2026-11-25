#!/usr/bin/env python3
"""Sprawdź ZIP zwrócony przez zbieracz (format ``lc-zbior-v1``) bez rozpakowania.

Wypisuje wyłącznie liczby. Uruchamiaj na archiwum w ignorowanym ``local/``.
Sumy SHA-256 dowodzą zgodności z raportem dołączonym do archiwum, a nie
pochodzenia ani kompletności danych. Archiwum i dane gry pozostają prywatne.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile


FORMAT = "lc-zbior-v1"
MAX_ARCHIVE_BYTES = 200 * 1024 * 1024
MAX_EXPANDED_BYTES = 1024 * 1024 * 1024
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_REPORT_BYTES = 32 * 1024 * 1024
MAX_MEMBERS = 50_000
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ALLOWED_SUFFIXES = frozenset({".json", ".txt", ".csv", ".tsv", ".xml", ".yaml", ".yml", ".md"})
LOCALIZE_PREFIX = "pliki/Assets/Resources_moved/Localize/"
LANG_CONFIG = "pliki/Lang/config.json"
# Dane pomocnicze od zbieracza 1.1.0 (kolejność scen, statystyki, tła scen).
EXTRA_PREFIXES = {
    "StaticData": "pliki/Assets/Resources_moved/StaticData/",
    "Story": "pliki/Assets/Resources_moved/Story/",
}
FIXED_MEMBERS = frozenset({"RAPORT.json", "RAPORT.txt", "INWENTARZ.jsonl"})


class InvalidReturn(ValueError):
    """Wadliwe lub niespójne archiwum (komunikat bez prywatnych ścieżek)."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidReturn(message)


def _unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON field in report")
        result[key] = value
    return result


def safe_member(name: str) -> bool:
    if not name or name.startswith("/") or "\\" in name or "\0" in name:
        return False
    parts = PurePosixPath(name).parts
    return all(part not in ("", ".", "..") for part in parts) and ":" not in parts[0]


def is_localize(name: str) -> bool:
    # Windows nie rozróżnia wielkości liter; porównuj prefiks bez niej.
    return name.casefold().startswith(LOCALIZE_PREFIX.casefold())


def extra_area(name: str) -> str | None:
    for area, prefix in EXTRA_PREFIXES.items():
        if name.casefold().startswith(prefix.casefold()):
            return area
    return None


def payload_allowed(name: str) -> bool:
    if name.casefold() == LANG_CONFIG.casefold():
        return True
    if not is_localize(name) and extra_area(name) is None:
        return False
    return PurePosixPath(name).suffix.lower() in ALLOWED_SUFFIXES


def validate(path: Path) -> dict[str, object]:
    require(path.stat().st_size <= MAX_ARCHIVE_BYTES, "archive is larger than the intake limit")
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        require(0 < len(infos) <= MAX_MEMBERS, "unexpected number of archive members")
        names = [info.filename for info in infos]
        require(len(names) == len(set(names)), "duplicate archive member")
        expanded = 0
        for info in infos:
            require(safe_member(info.filename), "unsafe member name")
            require(not info.is_dir(), "directory entries are not expected")
            require(info.file_size <= MAX_MEMBER_BYTES, "member larger than the limit")
            expanded += info.file_size
            require(info.filename in FIXED_MEMBERS or payload_allowed(info.filename),
                    "member outside the collector format")
        require(expanded <= MAX_EXPANDED_BYTES, "expanded size exceeds the limit")
        require("RAPORT.json" in names and "RAPORT.txt" in names, "missing report")
        report_info = archive.getinfo("RAPORT.json")
        require(report_info.file_size <= MAX_REPORT_BYTES, "report too large")
        try:
            report = json.loads(archive.read("RAPORT.json").decode("utf-8-sig"), object_pairs_hook=_unique)
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise InvalidReturn("report is not valid UTF-8 JSON") from exc
        require(isinstance(report, dict) and report.get("format") == FORMAT, "unknown report format")
        for key in ("tryb", "zbior_id", "czesc", "czesci", "gra", "pliki", "problemy",
                    "pominiete", "stan_zbioru", "inwentarz", "wszystkie_czesci"):
            require(key in report, f"report field missing: {key}")
        require(report["tryb"] in ("pelny", "aktualizacja"), "unknown mode")
        require(report["stan_zbioru"] in ("kompletny", "niepelny"), "unknown collection state")
        part, parts = report["czesc"], report["czesci"]
        require(isinstance(part, int) and isinstance(parts, int) and 1 <= part <= parts, "bad part numbers")
        require(isinstance(report["wszystkie_czesci"], list) and len(report["wszystkie_czesci"]) == parts,
                "part summary does not match part count")
        inventory_here = bool(report["inwentarz"].get("w_tej_czesci"))
        require(inventory_here == ("INWENTARZ.jsonl" in names), "inventory presence mismatch")

        records = report["pliki"]
        require(isinstance(records, list), "file list must be a list")
        listed: dict[str, dict[str, object]] = {}
        for record in records:
            require(isinstance(record, dict), "file record must be an object")
            member = record.get("czlon")
            require(isinstance(member, str) and member not in listed, "duplicate or missing member in report")
            require(member == "pliki/" + str(record.get("sciezka")), "member does not match source path")
            require(isinstance(record.get("rozmiar"), int), "file size missing")
            require(isinstance(record.get("sha256"), str) and SHA256.match(record["sha256"]), "bad SHA-256")
            listed[member] = record
        payload = {name for name in names if name.startswith("pliki/")}
        require(payload == set(listed), "archive payload does not match the report")

        languages: dict[str, int] = {}
        extras: dict[str, int] = {}
        payload_bytes = 0
        for member in sorted(payload):
            data = archive.read(member)  # odczyt sprawdza też CRC
            record = listed[member]
            require(len(data) == record["rozmiar"], "size mismatch")
            require(hashlib.sha256(data).hexdigest() == record["sha256"], "SHA-256 mismatch")
            payload_bytes += len(data)
            if is_localize(member):
                rest = member[len(LOCALIZE_PREFIX):].split("/", 1)
                language = rest[0] if len(rest) == 2 else "(korzen)"
                languages[language] = languages.get(language, 0) + 1
            elif (area := extra_area(member)) is not None:
                extras[area] = extras.get(area, 0) + 1

        inventory_rows = 0
        if inventory_here:
            for line in archive.read("INWENTARZ.jsonl").decode("utf-8").splitlines():
                row = json.loads(line)
                require(isinstance(row.get("p"), str) and isinstance(row.get("s"), int), "bad inventory row")
                inventory_rows += 1
            require(inventory_rows == report["inwentarz"].get("wierszy"), "inventory row count mismatch")

    return {
        "validation": "passed",
        "format": FORMAT,
        "tryb": report["tryb"],
        "czesc": part,
        "czesci": parts,
        "buildid": report["gra"].get("buildid"),
        "stan_zbioru": report["stan_zbioru"],
        "plikow": len(listed),
        "bajtow": payload_bytes,
        "plikow_wg_jezyka": dict(sorted(languages.items())),
        "plikow_pomocniczych": dict(sorted(extras.items())),
        "lang_config": any(m.casefold() == LANG_CONFIG.casefold() for m in payload),
        "inwentarz_wierszy": inventory_rows,
        "pominietych": len(report["pominiete"]),
        "problemow": len(report["problemy"]),
        "usunietych": len(report.get("stan", {}).get("usuniete", [])),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archiwa", nargs="+", type=Path)
    args = parser.parse_args()
    code = 0
    for path in args.archiwa:
        try:
            result = validate(path)
        except (OSError, zipfile.BadZipFile, InvalidReturn) as exc:
            print(json.dumps({"validation": "failed", "reason": str(exc)}, ensure_ascii=False))
            code = 1
            continue
        print(json.dumps(result, ensure_ascii=False))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
