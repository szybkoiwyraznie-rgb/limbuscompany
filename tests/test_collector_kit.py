"""Builder zestawu zbieracza i kodowanie skryptów Windows (Linux i Windows)."""
from __future__ import annotations

import io
from pathlib import Path
import re
import shutil
import tempfile
import unittest
import zipfile

from tools import build_collector_kit as kit


class CollectorKitTests(unittest.TestCase):
    def test_kit_is_reproducible_and_has_expected_members(self):
        first, second = kit.build_bytes(), kit.build_bytes()
        self.assertEqual(first, second)
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertEqual(archive.namelist(), list(kit.MEMBERS))
            self.assertIsNone(archive.testzip())
            readme = archive.read("CZYTAJ_TO.txt")
            self.assertTrue(readme.startswith(b"\xef\xbb\xbf"))
            self.assertIn("Limbus Company".encode(), readme)

    def test_script_encodings_are_checked_not_repaired(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "collector"
            shutil.copytree(kit.COLLECTOR, copy)
            kit.build_bytes(copy)  # oryginalne bajty są poprawne
            ps1 = copy / "zbierz.ps1"
            ps1.write_bytes(ps1.read_bytes()[3:])  # bez BOM
            with self.assertRaises(ValueError):
                kit.build_bytes(copy)
            shutil.copy(kit.COLLECTOR / "zbierz.ps1", ps1)
            bat = copy / "URUCHOM.bat"
            bat.write_bytes(bat.read_bytes().replace(b"\r\n", b"\n"))
            with self.assertRaises(ValueError):
                kit.build_bytes(copy)

    def test_build_writes_and_reads_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = kit.build(Path(tmp) / "out" / "LC_ZBIERZ_DANE.zip")
            self.assertEqual(result["czlonki"], list(kit.MEMBERS))
            self.assertRegex(result["sha256"], r"^[0-9a-f]{64}$")

    def test_powershell_is_read_only_towards_the_game(self):
        text = (kit.COLLECTOR / "zbierz.ps1").read_bytes().decode("utf-8-sig")
        # Zapis wyłącznie do katalogu wynikowego i pliku stanu; żadnych operacji
        # usuwania/zmiany w grze ani połączeń sieciowych.
        for forbidden in ("Remove-Item", "Invoke-WebRequest", "Invoke-RestMethod", "Net.WebClient",
                          "Set-Content", "Start-Process", "Set-ExecutionPolicy", "Out-File"):
            self.assertNotIn(forbidden, text)
        writes = re.findall(r"\[IO\.File\]::(Write\w+|Open)\(([^,)]+)", text)
        self.assertEqual(sorted(target.strip() for _, target in writes), ["$temp", "$tmp"])
        self.assertIn("'1973530'", text)
        self.assertIn("Assets/Resources_moved/Localize", text)

    def test_bat_files_call_the_right_modes(self):
        self.assertIn(b"-Tryb pelny", (kit.COLLECTOR / "URUCHOM.bat").read_bytes())
        self.assertIn(b"-Tryb aktualizacja", (kit.COLLECTOR / "URUCHOM_AKTUALIZACJE.bat").read_bytes())


if __name__ == "__main__":
    unittest.main()
