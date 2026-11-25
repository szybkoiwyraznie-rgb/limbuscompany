"""Uruchom *zbudowany* zbieracz (PowerShell 5.1) na sztucznej instalacji gry.

Testy są wykrywane wyłącznie w Windows (CI: windows-latest). Linux sprawdza
builder, kodowanie i walidator. Bez gry, poświadczeń i zależności zewnętrznych.
"""
from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

from tests import syntetyczne as syn
from tools.build_collector_kit import build_bytes
from tools.validate_collector_return import validate


if os.name == "nt":
    class WindowsCollectorIntegrationTests(unittest.TestCase):
        def setUp(self):
            self.tmp = tempfile.TemporaryDirectory(prefix="lc-fixture-")
            self.addCleanup(self.tmp.cleanup)
            self.root = Path(self.tmp.name)
            self.kit = self.root / "Zestaw żółć"
            self.kit.mkdir()
            with zipfile.ZipFile(io.BytesIO(build_bytes())) as archive:
                archive.extractall(self.kit)
            self.ps = Path(os.environ["SystemRoot"]) / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe"
            self.game = self.root / "Biblioteka [gry] żółć" / "steamapps" / "common" / "Limbus Company"
            self.data = self.game / "LimbusCompany_Data"
            self.localize = self.data / "Assets" / "Resources_moved" / "Localize"
            syn.zapisz_drzewo(self.localize, syn.drzewo_localize())
            self.write("Lang/config.json", b'{"lang": "inne"}')
            self.write("Lang/inne/MainUIText.json", b'{"dataList": []}')
            self.write("Assets/Resources_moved/Localize/en/obraz.png", b"\x89PNG")
            for relative, data in syn.drzewo_pomocnicze().items():
                self.write(relative, data)
            self.write("Assets/Resources_moved/StaticData/static-data/blob.bytes", b"\x00\x01")
            self.write("Managed/fake.dll", b"MZ")
            self.write("output_log.log", b"fake log")
            (self.game.parent.parent / "appmanifest_1973530.acf").write_text(
                '"AppState"\n{\n\t"appid"\t\t"1973530"\n\t"buildid"\t\t"7654321"\n\t"installdir"\t\t"Limbus Company"\n}\n',
                encoding="utf-8",
            )
            self.out = self.root / "Wyniki żółć"
            self.out.mkdir()
            self.state = self.root / "Stan"
            self.before = self.snapshot()

        def write(self, relative: str, data: bytes) -> None:
            path = self.data / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        def snapshot(self):
            return {p.relative_to(self.game).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in self.game.rglob("*") if p.is_file()}

        def run_ps(self, *args: str):
            return subprocess.run(
                [str(self.ps), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                 "-File", str(self.kit / "zbierz.ps1"), str(self.game), "-OutputDirectory", str(self.out),
                 "-KatalogStanu", str(self.state), "-NonInteractive", *args],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300, check=False,
            )

        def detail(self, result) -> str:
            text = result.stdout.decode("utf-8", errors="replace")
            errors = [line.strip() for line in text.splitlines() if "BLAD:" in line]
            return (errors[0] if errors else repr(text))[:700]

        def zips(self):
            return sorted(self.out.glob("LC_DANE_*.zip"))

        def test_full_collection_is_valid_and_read_only(self):
            result = self.run_ps("-Tryb", "pelny")
            self.assertEqual(result.returncode, 0, self.detail(result))
            self.assertEqual(self.snapshot(), self.before, "game files must not change")
            paths = self.zips()
            self.assertEqual(len(paths), 1, paths)
            verified = validate(paths[0])
            self.assertEqual(verified["buildid"], "7654321")
            self.assertEqual(verified["plikow_wg_jezyka"], {"en": 5, "jp": 3, "kr": 4})
            self.assertTrue(verified["lang_config"])
            self.assertEqual(verified["plikow_pomocniczych"], {"StaticData": 2, "Story": 1})
            self.assertEqual(verified["pominietych"], 2)  # obraz.png, blob.bytes
            with zipfile.ZipFile(paths[0]) as archive:
                names = archive.namelist()
                report = json.loads(archive.read("RAPORT.json").decode("utf-8-sig"))
                inventory = archive.read("INWENTARZ.jsonl").decode("utf-8")
            self.assertFalse(any("fake.dll" in n or ".log" in n or "Lang/inne" in n for n in names))
            self.assertIn("Managed/fake.dll", inventory)  # tylko nazwa w spisie
            self.assertNotIn(str(self.root), inventory)
            self.assertEqual(report["lang"]["podfoldery"], ["inne"])
            self.assertEqual(report["zbieracz"], "LC_ZBIERZ_DANE 1.1.0")
            self.assertEqual(report["dodatkowe"]["Assets/Resources_moved/StaticData"],
                             {"istnieje": True, "plikow": 2})
            self.assertTrue((self.state / "stan_wyslanych.json").is_file())

        def test_update_mode_sends_only_changes(self):
            first = self.run_ps("-Tryb", "pelny")
            self.assertEqual(first.returncode, 0, self.detail(first))
            for path in self.zips():
                path.unlink()
            same = self.run_ps("-Tryb", "aktualizacja")
            self.assertEqual(same.returncode, 0, self.detail(same))
            self.assertEqual(self.zips(), [], "no ZIP when nothing changed")
            (self.localize / "en" / "EN_MainUIText.json").write_bytes(b'{"dataList": [{"id": "a", "content": "Nowe"}]}')
            (self.localize / "en" / "EN_OnlyEnglish.json").unlink()
            (self.localize / "kr" / "KR_New.json").write_bytes(b'{"dataList": []}')
            changed = self.run_ps("-Tryb", "aktualizacja")
            self.assertEqual(changed.returncode, 0, self.detail(changed))
            paths = self.zips()
            self.assertEqual(len(paths), 1, paths)
            verified = validate(paths[0])
            self.assertEqual(verified["tryb"], "aktualizacja")
            self.assertEqual(verified["plikow"], 2)
            self.assertEqual(verified["usunietych"], 1)

        def test_parts_are_split_by_uncompressed_budget(self):
            result = self.run_ps("-Tryb", "pelny", "-LimitCzesciBajtow", "600", "-BezStanu")
            self.assertEqual(result.returncode, 0, self.detail(result))
            paths = self.zips()
            self.assertGreater(len(paths), 1)
            total = 0
            for path in paths:
                verified = validate(path)
                self.assertEqual(verified["czesci"], len(paths))
                total += verified["plikow"]
            self.assertEqual(total, 16)
            self.assertFalse((self.state / "stan_wyslanych.json").exists())

        def test_missing_game_folder_is_an_error(self):
            result = subprocess.run(
                [str(self.ps), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                 "-File", str(self.kit / "zbierz.ps1"), str(self.root), "-OutputDirectory", str(self.out),
                 "-NonInteractive"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("BLAD:", result.stdout.decode("utf-8", errors="replace"))
            self.assertEqual(self.zips(), [])
