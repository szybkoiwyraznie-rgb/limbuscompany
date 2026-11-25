from __future__ import annotations

import hashlib
import io
from pathlib import Path
import re
import tempfile
import unittest
import zipfile

from tools.build_collector_kit import COLLECTOR, MEMBERS, build, build_bytes, windows_lines


class CollectorKitTests(unittest.TestCase):
    def test_kit_is_reproducible_and_has_exact_members(self):
        first, second = build_bytes(), build_bytes()
        self.assertEqual(first, second)
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertEqual(archive.namelist(), list(MEMBERS))
            readme = archive.read("CZYTAJ_TO.txt")
            self.assertTrue(readme.startswith(b"\xef\xbb\xbf"))
            self.assertNotIn(b"\n", readme.replace(b"\r\n", b""))

    def test_build_writes_file_and_reports_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = build(Path(tmp) / "kit.zip")
            data = Path(result["file"]).read_bytes()
            self.assertEqual(result["sha256"], hashlib.sha256(data).hexdigest())

    def test_checked_in_scripts_have_windows_bytes(self):
        windows_lines((COLLECTOR / "URUCHOM.bat").read_bytes(), bom=False, ascii_only=True)
        windows_lines((COLLECTOR / "zbierz.ps1").read_bytes(), bom=True, ascii_only=True)

    def test_line_ending_validation_rejects_lf(self):
        with self.assertRaises(ValueError):
            windows_lines(b"echo\n", bom=False)
        with self.assertRaises(ValueError):
            windows_lines(b"\xef\xbb\xbfecho\r\n", bom=False)

    def test_batch_uses_process_scoped_bypass_and_reports_exit_codes(self):
        bat = (COLLECTOR / "URUCHOM.bat").read_text(encoding="ascii")
        self.assertIn("-ExecutionPolicy Bypass -File", bat)
        self.assertIn("Unblock-File", bat)
        self.assertIn('if "%RESULT%"=="2" goto partial', bat)
        self.assertNotIn("Set-ExecutionPolicy", bat)

    def test_powershell_is_read_only_towards_the_game(self):
        ps = (COLLECTOR / "zbierz.ps1").read_text(encoding="utf-8-sig")
        # The only writes go to the work directory / output ZIP outside the game.
        self.assertIn("Folder wynikowy jest wewnatrz folderu gry", ps)
        forbidden = re.search(r"(?i)(?<![A-Za-z])(Set-Content|Out-File|Move-Item|Rename-Item|Copy-Item)", ps)
        self.assertIsNone(forbidden, forbidden and forbidden.group(0))
        for call in re.findall(r"Remove-Item[^\r\n]*", ps):
            self.assertIn("$", call)
            self.assertTrue("$target" in call or "$script:Work" in call, call)
        network = re.search(r"(?i)Invoke-WebRequest|Invoke-RestMethod|Net\.WebClient|Start-BitsTransfer", ps)
        self.assertIsNone(network, network and network.group(0))
        self.assertIn("'1973530'", ps)
        self.assertIn("Resources_moved\\Localize", ps)

    def test_powershell_avoids_script_module_cmdlets(self):
        # In Windows PowerShell 5.1 these live in .psm1 script modules and are
        # unavailable when PSModulePath points at PowerShell 7 modules (seen on
        # Windows CI with Get-FileHash). Use .NET instead.
        ps = (COLLECTOR / "zbierz.ps1").read_text(encoding="utf-8-sig")
        fragile = re.search(
            r"(?i)(?<![A-Za-z-])(Get-FileHash|Format-Hex|New-Guid|Import-PowerShellDataFile"
            r"|Compress-Archive|Expand-Archive|New-TemporaryFile)(?![A-Za-z-])",
            ps,
        )
        self.assertIsNone(fragile, fragile and fragile.group(0))
        self.assertIn("SHA256]::Create()", ps)


if __name__ == "__main__":
    unittest.main()
