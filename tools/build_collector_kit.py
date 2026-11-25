#!/usr/bin/env python3
"""Build the Windows read-only collector kit; no game data is included.

The resulting ZIP is reproducible and belongs in an ignored directory
(artifacts/ by default). The owner only unpacks it and runs URUCHOM.bat;
Python is used solely by the project to produce and test the kit.
Pattern: wherewindsmeet tools/build_collector_kit.py.
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
KIT_NAME = "LCB_ZBIERZ_DANE.zip"
STAMP = (2026, 11, 25, 0, 0, 0)
MEMBERS = ("CZYTAJ_TO.txt", "URUCHOM.bat", "zbierz.ps1")


def windows_lines(data: bytes, *, bom: bool, ascii_only: bool = False) -> bytes:
    """Validate the checked-in PS/BAT bytes instead of silently repairing them."""
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


def readme_bytes() -> bytes:
    text = (COLLECTOR / "CZYTAJ_TO.txt").read_text(encoding="utf-8")
    # A BOM makes Polish characters reliable in the classic Windows Notepad.
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n")
    return text.encode("utf-8-sig")


def kit_files() -> dict[str, bytes]:
    return {
        "CZYTAJ_TO.txt": readme_bytes(),
        "URUCHOM.bat": windows_lines((COLLECTOR / "URUCHOM.bat").read_bytes(), bom=False, ascii_only=True),
        # PowerShell 5.1 reads a BOM-less script as the ANSI code page; keep it
        # ASCII as well so the bytes are unambiguous in any locale.
        "zbierz.ps1": windows_lines((COLLECTOR / "zbierz.ps1").read_bytes(), bom=True, ascii_only=True),
    }


def build_bytes() -> bytes:
    files = kit_files()
    if tuple(files) != MEMBERS:
        raise ValueError("unexpected kit members")
    buffer = io.BytesIO()
    # The kit is tiny; storing rather than deflating avoids zlib-version drift.
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in files.items():
            info = zipfile.ZipInfo(name, date_time=STAMP)
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def build(output: Path) -> dict[str, object]:
    data = build_bytes()
    # Independently read back the complete archive before delivering it.
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None or archive.namelist() != list(MEMBERS):
            raise ValueError("kit archive did not pass read-back")
        expected = kit_files()
        if any(archive.read(name) != expected[name] for name in MEMBERS):
            raise ValueError("kit archive content mismatch")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)
    return {
        "file": str(output),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "members": list(MEMBERS),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, default=ROOT / "artifacts" / KIT_NAME)
    args = parser.parse_args(argv)
    print(json.dumps(build(args.output), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
