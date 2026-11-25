"""Invented Localize snapshots for tests: the layout mimics the game, the text does not.

Every string here is made up ("Synthetic …"); no game text is used. The file
and field names follow the publicly documented layout (Steam notice of
2025-03-31 and public custom-language repositories, see docs/PRIOR_ART.md).
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import zipfile


def _story(lang: str, n: int) -> dict:
    return {
        "dataList": [
            {"id": "0", "place": f"Synthetic place {lang}", "content": f"Synthetic narration {lang} {n}"},
            {"id": "1", "teller": f"Speaker {lang}", "title": f"Title {lang}", "model": "synthetic_model",
             "content": f"Synthetic line {lang} {n} one"},
            {"id": "2", "teller": f"Speaker {lang}", "content": f"Synthetic line {lang} {n} two"},
        ]
    }


def localize_files(languages: tuple[str, ...] = ("en", "kr", "jp")) -> dict[str, bytes]:
    """Return ``{"Localize/<lang>/<PREFIX>_<name>.json": bytes}``."""
    files: dict[str, bytes] = {}
    for lang in languages:
        prefix = lang.upper() + "_"
        docs = {
            "MainUIText.json": {"dataList": [
                {"id": "synthetic_button0", "content": f"Window {lang}"},
                {"id": "synthetic_button1", "content": ""},
            ]},
            "Skills.json": {"dataList": [
                {"id": 100, "levelList": [
                    {"level": 1, "name": f"Skill {lang}", "desc": f"Synthetic description {lang}"},
                    {"level": 2, "name": f"Skill {lang} II", "desc": f"Synthetic description {lang} II"},
                ]},
            ]},
            "StoryData/1D101A.json": _story(lang, 1),
            "StoryData/S101A.json": _story(lang, 2),
        }
        if lang == "en":
            docs["OnlyEnglish.json"] = {"dataList": [{"id": "x", "content": "Synthetic only en"}]}
            # A repeated id, as can happen in real tables.
            docs["MainUIText.json"]["dataList"].append({"id": "synthetic_button0", "content": "Again"})
        for name, doc in docs.items():
            folder, _, leaf = name.rpartition("/")
            member = f"Localize/{lang}/" + (folder + "/" if folder else "") + prefix + leaf
            data = json.dumps(doc, ensure_ascii=False, indent=2).encode("utf-8")
            if lang == "kr":
                data = b"\xef\xbb\xbf" + data  # some files may carry a BOM
            files[member] = data
    return files


def collector_zip(*, tamper: str | None = None, extra: dict[str, bytes] | None = None) -> bytes:
    """Build a return ZIP in the ``lcb-zbieracz-v1`` layout from invented files."""
    payload = localize_files()
    payload["Lang/config.json"] = json.dumps({"lang": "Synthetic", "titleFont": "", "contextFont": ""}).encode()
    entries = []
    for path, data in payload.items():
        kind = "localize" if path.startswith("Localize/") else "lang_config"
        entries.append({"path": path, "kind": kind, "size": len(data),
                        "sha256": hashlib.sha256(data).hexdigest(), "mtime_utc": "2026-11-20T00:00:00Z"})
    inventory = [
        {"p": "LimbusCompany_Data/app.info", "s": 20, "t": "2026-11-20T00:00:00Z"},
        {"p": "LimbusCompany_Data/StreamingAssets/synthetic.bundle", "s": 1234, "t": "2026-11-20T00:00:00Z"},
    ]
    report = {
        "format": "lcb-zbieracz-v1", "tool_version": "1.0.0", "created_utc": "2026-11-25T00:00:00Z",
        "status": "complete",
        "game": {"root_name": "Limbus Company", "steam": {"app_id": "1973530", "buildid": "12345678"}},
        "inventory": {"file": "INWENTARZ.jsonl", "entries": len(inventory), "limited": False},
        "files": entries, "skipped": [], "problems": [],
    }
    if tamper == "sha":
        entries[0]["sha256"] = "0" * 64
    if tamper == "count":
        report["inventory"]["entries"] = 99
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("RAPORT.json", json.dumps(report, indent=2))
        archive.writestr("RAPORT.txt", "synthetic")
        archive.writestr("INWENTARZ.jsonl", "".join(json.dumps(r) + "\n" for r in inventory))
        for path, data in payload.items():
            archive.writestr(path, data)
        for path, data in (extra or {}).items():
            archive.writestr(path, data)
    return buffer.getvalue()


def write_collector_zip(target: Path, **kwargs) -> Path:
    target.write_bytes(collector_zip(**kwargs))
    return target
