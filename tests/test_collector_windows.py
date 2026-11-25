"""Run the *built* BAT and PowerShell collector on a synthetic Windows install.

These integration tests are intentionally defined only on Windows (GitHub
Actions windows-latest, Windows PowerShell 5.1). Linux runs the
platform-independent builder, encoding and intake tests instead.
No game, credentials or external dependencies are used.
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
from zipfile import ZipFile

from tests.synthetic_localize import localize_files
from tools.build_collector_kit import build_bytes
from tools.inspect_localize import inspect
from tools.validate_collector_return import validate


if os.name == "nt":
    class WindowsCollectorIntegrationTests(unittest.TestCase):
        def setUp(self):
            self.tmp = tempfile.TemporaryDirectory(prefix="lcb-fixture-")
            self.addCleanup(self.tmp.cleanup)
            self.root = Path(self.tmp.name)
            self.kit = self.root / "Zestaw z polskimi znakami żółć"
            self.kit.mkdir()
            with ZipFile(io.BytesIO(build_bytes())) as archive:
                archive.extractall(self.kit)  # our own three known member names
            self.ps = Path(os.environ["SystemRoot"]) / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe"
            self.library = self.root / "Biblioteka [gry] żółć"
            self.game = self.library / "steamapps" / "common" / "Limbus Company"
            self.out = self.root / "Wyniki żółć"
            self.out.mkdir()
            base = "LimbusCompany_Data/Assets/Resources_moved/"
            for member, data in localize_files().items():
                self.write(base + member, data)
            self.write(base + "Localize/en/readme_not_json.txt", b"not copied")
            self.write(base + "Localize/fonts_synthetic/x.json", b"{}")  # other dir: listed, not copied
            self.write("LimbusCompany_Data/Lang/config.json", b'{"lang": "Synthetic"}')
            self.write("LimbusCompany_Data/Lang/Synthetic/MainUIText.json", b'{"dataList": []}')
            self.write("LimbusCompany_Data/app.info", b"Project Moon\nLimbusCompany")
            self.write("LimbusCompany_Data/StreamingAssets/synthetic.bundle", b"not copied")
            self.write("LimbusCompany.exe", b"MZ not copied")
            acf = '"AppState"\n{\n\t"appid"\t\t"1973530"\n\t"installdir"\t\t"Limbus Company"\n\t"buildid"\t\t"12345678"\n\t"LastUpdated"\t\t"1764000000"\n}\n'
            (self.library / "steamapps" / "appmanifest_1973530.acf").write_text(acf, encoding="utf-8")
            self.original = self.game_files()

        def write(self, relative: str, data: bytes):
            path = self.game / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        def game_files(self):
            return {
                p.relative_to(self.game).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.game.rglob("*") if p.is_file()
            }

        def run_ps(self, *args: str):
            return subprocess.run(
                [str(self.ps), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                 "-File", str(self.kit / "zbierz.ps1"), *map(str, args)],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300, check=False,
            )

        def detail(self, result):
            text = result.stdout.decode("utf-8", errors="replace")
            errors = [line.strip() for line in text.splitlines() if "BLAD:" in line]
            return (errors[0] if errors else repr(text))[:900]

        def single_zip(self):
            paths = list(self.out.glob("LCB_DANE_*.zip"))
            self.assertEqual(len(paths), 1, paths)
            return paths[0]

        def test_collects_localize_lang_config_and_inventory_read_only(self):
            result = self.run_ps("-GameRoot", self.game, "-OutputDirectory", self.out, "-NonInteractive")
            self.assertEqual(result.returncode, 0, self.detail(result))
            path = self.single_zip()
            summary = validate(path)
            self.assertEqual(summary["status"], "complete")
            self.assertEqual(summary["steam_buildid"], "12345678")
            self.assertEqual(summary["localize_files_by_language"], {"en": 5, "jp": 4, "kr": 4})
            self.assertEqual(summary["files_by_kind"], {"localize": 13, "lang_config": 1, "app_info": 1})
            with ZipFile(path) as archive:
                names = archive.namelist()
                report = json.loads(archive.read("RAPORT.json").decode("utf-8-sig"))
                inventory = archive.read("INWENTARZ.jsonl").decode("utf-8")
            self.assertTrue(all("\\" not in n for n in names))
            self.assertNotIn("LimbusCompany.exe", " ".join(names))
            self.assertNotIn("Lang/Synthetic/MainUIText.json", names)
            self.assertIn("LimbusCompany_Data/StreamingAssets/synthetic.bundle", inventory)
            self.assertEqual(report["game"]["root_name"], "Limbus Company")
            self.assertNotIn(str(self.root), json.dumps(report, ensure_ascii=False))
            self.assertEqual([f["name"] for f in report["lang"]["folders"]], ["Synthetic"])
            self.assertIn("fonts_synthetic", [d["name"] for d in report["localize"]["directories"]])
            self.assertTrue(any(s["reason"] == "not_json" for s in report["skipped"]))
            self.assertEqual(self.game_files(), self.original)
            self.assertEqual(list(self.out.glob(".LCB_ZBIERANIE_*")), [])
            # The private investigation tool reads the real return directly.
            self.assertEqual(inspect(path)["pairing"]["only_in"]["en"], 1)

        def test_steam_library_detection_and_dragged_inner_folder(self):
            result = self.run_ps("-SteamRoot", self.library, "-OutputDirectory", self.out, "-NonInteractive")
            self.assertEqual(result.returncode, 0, self.detail(result))
            self.assertEqual(validate(self.single_zip())["steam_buildid"], "12345678")
            self.single_zip().unlink()
            inner = self.game / "LimbusCompany_Data" / "Assets"
            result = self.run_ps("-GameRoot", inner, "-OutputDirectory", self.out, "-NonInteractive")
            self.assertEqual(result.returncode, 0, self.detail(result))

        def test_delivered_batch_runs_with_dragged_folder_and_spaces(self):
            bat = self.kit / "URUCHOM.bat"
            command = f'"{bat}" "{self.game}" -OutputDirectory "{self.out}" -NonInteractive'
            result = subprocess.run(command, shell=True, input=b"\r\n", stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, timeout=300, check=False)
            self.assertEqual(result.returncode, 0, self.detail(result))
            self.assertEqual(validate(self.single_zip())["validation"], "passed")

        def test_missing_language_gives_partial_zip(self):
            result = self.run_ps("-GameRoot", self.game, "-OutputDirectory", self.out, "-NonInteractive",
                                 "-Jezyki", "en,kr,jp,xx")
            self.assertEqual(result.returncode, 2, self.detail(result))
            path = self.single_zip()
            self.assertEqual(validate(path)["status"], "partial")

        def test_output_inside_game_is_refused_before_writing(self):
            target = self.game / "LimbusCompany_Data"
            result = self.run_ps("-GameRoot", self.game, "-OutputDirectory", target, "-NonInteractive")
            self.assertEqual(result.returncode, 1)
            self.assertEqual(self.game_files(), self.original)

        def test_not_a_game_folder_is_refused(self):
            result = self.run_ps("-GameRoot", self.out, "-OutputDirectory", self.out, "-NonInteractive")
            self.assertEqual(result.returncode, 1)
            self.assertEqual(list(self.out.glob("*.zip")), [])

        def test_repeated_runs_create_new_zip_without_overwriting(self):
            for _ in range(2):
                result = self.run_ps("-GameRoot", self.game, "-OutputDirectory", self.out, "-NonInteractive")
                self.assertEqual(result.returncode, 0, self.detail(result))
            self.assertEqual(len(list(self.out.glob("LCB_DANE_*.zip"))), 2)


if __name__ == "__main__":
    unittest.main()
