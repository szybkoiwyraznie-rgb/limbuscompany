#!/usr/bin/env python3
"""Zbuduj zestaw zbieracza dla Windows (tylko odczyt gry); bez danych gry.

Wynikowy ZIP jest powtarzalny (stałe znaczniki czasu, bez kompresji) i trafia do
ignorowanego katalogu (np. ``dist/``). Właściciel tylko go rozpakowuje i
uruchamia ``URUCHOM.bat`` albo ``URUCHOM_AKTUALIZACJE.bat``; Python służy
wyłącznie projektowi do zbudowania i przetestowania zestawu.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parent.parent
COLLECTOR = ROOT / "collector"
STAMP = (2026, 11, 25, 0, 0, 0)
MEMBERS = ("CZYTAJ_TO.txt", "URUCHOM.bat", "URUCHOM_AKTUALIZACJE.bat", "zbierz.ps1")


def windows_lines(data: bytes, *, bom: bool, ascii_only: bool = False) -> bytes:
    """Sprawdź zapisane bajty skryptu Windows zamiast je po cichu naprawiać."""
    has_bom = data.startswith(b"\xef\xbb\xbf")
    if has_bom != bom:
        raise ValueError("unexpected BOM state in Windows script")
    content = data[3:] if has_bom else data
    content.decode("ascii" if ascii_only else "utf-8")
    if not content.endswith(b"\r\n") or b"\n" in content.replace(b"\r\n", b""):
        raise ValueError("Windows script must use CRLF throughout")
    if b"\r" in content.replace(b"\r\n", b""):
        raise ValueError("Windows script has a stray carriage return")
    return data


def kit_files(collector: Path = COLLECTOR) -> dict[str, bytes]:
    readme = (collector / "CZYTAJ_TO.txt").read_text(encoding="utf-8")
    # BOM, żeby klasyczny Notatnik pokazał polskie znaki.
    readme_windows = (
        readme.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n").encode("utf-8-sig")
    )
    return {
        "CZYTAJ_TO.txt": readme_windows,
        "URUCHOM.bat": windows_lines((collector / "URUCHOM.bat").read_bytes(), bom=False, ascii_only=True),
        "URUCHOM_AKTUALIZACJE.bat": windows_lines(
            (collector / "URUCHOM_AKTUALIZACJE.bat").read_bytes(), bom=False, ascii_only=True
        ),
        "zbierz.ps1": windows_lines((collector / "zbierz.ps1").read_bytes(), bom=True),
    }


def build_bytes(collector: Path = COLLECTOR) -> bytes:
    files = kit_files(collector)
    if tuple(files) != MEMBERS:
        raise ValueError("unexpected kit members")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in files.items():
            info = zipfile.ZipInfo(name, date_time=STAMP)
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def build(output: Path) -> dict[str, object]:
    data = build_bytes()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None or archive.namelist() != list(MEMBERS):
            raise ValueError("kit archive did not pass read-back")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)
    if output.read_bytes() != data:
        raise ValueError("written kit differs from the built bytes")
    return {
        "plik": output.name,
        "rozmiar": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "czlonki": list(MEMBERS),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "LC_ZBIERZ_DANE.zip")
    args = parser.parse_args()
    print(json.dumps(build(args.output), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
