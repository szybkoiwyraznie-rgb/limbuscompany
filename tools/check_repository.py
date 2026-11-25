#!/usr/bin/env python3
"""Sprawdź indeks Git pod kątem plików gry, prywatnych artefaktów i dużych plików.

To zabezpieczenie pomocnicze, nie skaner treści ani sekretów. Rozmiary są
czytane z obiektów w indeksie (a nie z drzewa roboczego), więc lokalna edycja
nie ukryje dodanego pliku. Dodatkowo:

* kopie surowych plików lokalizacji gry (``KR_*.json``, ``EN_*.json``,
  ``JP_*.json``, ścieżki ``Resources_moved/Localize`` i ``LimbusCompany_Data``)
  są zawsze odrzucane;
* katalogi z tekstem gry (``config/polityka_danych.json`` →
  ``katalogi_tekstu_gry``) są odrzucane, dopóki właściciel nie przestawi flagi
  ``tekst_gry_w_git`` (wymaga prywatnego repozytorium, zob. docs/DATA_POLICY.md).
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
POLICY = PurePosixPath("config/polityka_danych.json")
MAX_FILE_BYTES = 10 * 1024 * 1024

# Celowo odpowiada ochronnym częściom .gitignore. Recenzent i tak musi obejrzeć
# każdy plik w indeksie: jego treść może być prywatna pod dowolną nazwą.
BLOCKED_DIRECTORIES = frozenset(
    {
        "local", "google_drive", "build", "dist", "out", "artifacts", "downloads",
        ".venv", "venv", ".direnv", "__pycache__", ".pytest_cache", ".mypy_cache",
        ".ruff_cache", ".cache", "coverage", "node_modules",
        "limbuscompany_data", "resources_moved", "localize",
    }
)
BLOCKED_SUFFIXES = frozenset(
    {
        ".pem", ".key", ".p12", ".pfx", ".bundle", ".assetbundle", ".assets",
        ".ress", ".resource", ".unity3d", ".bin", ".dat", ".exe", ".dll", ".so",
        ".dylib", ".iso", ".img", ".sav", ".save", ".dmp", ".bak", ".zip", ".7z",
        ".rar", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".zst", ".log", ".pyc",
        ".pyo", ".pyd",
    }
)
FONT_SUFFIXES = frozenset({".ttf", ".otf"})
FONT_DIRECTORY = ("assets", "fonts")
BLOCKED_FILENAMES = frozenset({".coverage", ".ds_store", "thumbs.db"})
# Nazwy surowych plików lokalizacji gry: KR_/EN_/JP_ + nazwa + .json.
RAW_LOCALIZE_NAME = re.compile(r"^(kr|en|jp)_[a-z0-9].*\.json$", re.IGNORECASE)


@dataclass(frozen=True)
class IndexEntry:
    path: str
    mode: str
    oid: str
    stage: int


@dataclass(frozen=True)
class Policy:
    game_text_allowed: bool
    game_text_directories: frozenset[str]


@dataclass(frozen=True)
class ScanResult:
    entries: int
    violations: tuple[str, ...]


def _git(repo: Path, *args: str, input_data: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=repo, input=input_data, capture_output=True, check=False
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def read_index(repo: Path) -> list[IndexEntry]:
    raw = _git(repo, "ls-files", "--stage", "-z")
    entries = []
    for item in raw.split(b"\0"):
        if not item:
            continue
        header, raw_path = item.split(b"\t", 1)
        mode, oid, stage = header.split(b" ")
        entries.append(
            IndexEntry(
                path=os.fsdecode(raw_path),
                mode=mode.decode("ascii"),
                oid=oid.decode("ascii"),
                stage=int(stage),
            )
        )
    return entries


def blob_sizes(repo: Path, entries: list[IndexEntry]) -> dict[str, int]:
    oids = sorted({entry.oid for entry in entries if entry.mode != "160000"})
    if not oids:
        return {}
    raw = _git(
        repo,
        "cat-file",
        "--batch-check=%(objectname) %(objecttype) %(objectsize)",
        input_data=("\n".join(oids) + "\n").encode("ascii"),
    )
    lines = raw.decode("ascii").splitlines()
    if len(lines) != len(oids):
        raise RuntimeError("git cat-file returned an incomplete index size report")
    sizes = {}
    for requested, line in zip(oids, lines):
        parts = line.split()
        if len(parts) != 3 or parts[0] != requested or parts[1] != "blob":
            raise RuntimeError(f"index object is missing or not a blob: {line}")
        sizes[requested] = int(parts[2])
    return sizes


def read_policy(repo: Path, entries: list[IndexEntry]) -> Policy:
    """Czytaj politykę z indeksu (to, co trafi do commita), nie z dysku."""
    entry = next((e for e in entries if e.path == str(POLICY) and e.stage == 0), None)
    if entry is None:
        raise RuntimeError(f"{POLICY} is not in the Git index")
    data = json.loads(_git(repo, "cat-file", "blob", entry.oid).decode("utf-8"))
    if data.get("format") != "lc-polityka-danych-v1":
        raise RuntimeError(f"{POLICY}: unknown format")
    allowed = data.get("tekst_gry_w_git")
    directories = data.get("katalogi_tekstu_gry")
    if not isinstance(allowed, bool) or not isinstance(directories, list):
        raise RuntimeError(f"{POLICY}: invalid fields")
    if allowed and data.get("repozytorium_publiczne") is not False:
        raise RuntimeError(
            f"{POLICY}: game text in Git requires 'repozytorium_publiczne': false"
        )
    return Policy(
        game_text_allowed=allowed,
        game_text_directories=frozenset(str(d).casefold() for d in directories),
    )


def entry_violations(
    entry: IndexEntry,
    size: int | None,
    policy: Policy,
    max_file_bytes: int = MAX_FILE_BYTES,
) -> list[str]:
    shown = ascii(entry.path)
    parts = PurePosixPath(entry.path).parts
    folded = [part.casefold() for part in parts]
    name = folded[-1]
    violations = []
    blocked_dirs = [part for part in folded[:-1] if part in BLOCKED_DIRECTORIES]
    if blocked_dirs:
        violations.append(f"{shown}: protected directory {ascii(blocked_dirs[0])}")
    if folded and folded[0] in policy.game_text_directories and not policy.game_text_allowed:
        violations.append(
            f"{shown}: game-text directory {ascii(folded[0])} is blocked by {POLICY}"
        )
    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        violations.append(f"{shown}: environment file may contain secrets")
    elif name in BLOCKED_FILENAMES:
        violations.append(f"{shown}: local-only filename")
    if RAW_LOCALIZE_NAME.match(name):
        violations.append(f"{shown}: looks like a raw game localization file")
    suffix = PurePosixPath(name).suffix
    if suffix in BLOCKED_SUFFIXES:
        violations.append(f"{shown}: protected extension {suffix}")
    if suffix in FONT_SUFFIXES and tuple(folded[:2]) != FONT_DIRECTORY:
        violations.append(f"{shown}: fonts are allowed only under assets/fonts/ with a license")
    if entry.mode == "160000":
        violations.append(f"{shown}: submodule requires an explicit policy review")
    if entry.stage != 0:
        violations.append(f"{shown}: unresolved Git index conflict (stage {entry.stage})")
    if size is not None and size > max_file_bytes:
        violations.append(f"{shown}: staged blob is {size} B, limit is {max_file_bytes} B")
    return violations


def scan_index(repo: Path, max_file_bytes: int = MAX_FILE_BYTES) -> ScanResult:
    entries = read_index(repo)
    policy = read_policy(repo, entries)
    sizes = blob_sizes(repo, entries)
    violations = []
    for entry in entries:
        violations.extend(
            entry_violations(entry, sizes.get(entry.oid), policy, max_file_bytes)
        )
    return ScanResult(entries=len(entries), violations=tuple(violations))


def main() -> int:
    try:
        result = scan_index(ROOT)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Repository check failed to run: {exc}", file=sys.stderr)
        return 2
    if result.violations:
        print("Repository check failed (inspect the Git index):", file=sys.stderr)
        for violation in result.violations:
            print(f"  - {violation}", file=sys.stderr)
        return 1
    print(f"Repository check OK: {result.entries} index entries, limit {MAX_FILE_BYTES} B/file.")
    print("This is not a content or secrets scan; review the staged diff manually.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
