"""Kontrola indeksu Git na tymczasowych, syntetycznych repozytoriach."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools import check_repository as cr


def policy(allowed: bool = False, public: bool = True) -> str:
    return json.dumps(
        {
            "format": "lc-polityka-danych-v1",
            "repozytorium_publiczne": public,
            "tekst_gry_w_git": allowed,
            "katalogi_tekstu_gry": ["wyciag", "czytanki"],
            "uzasadnienie": "test",
        }
    )


class CheckRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="lc-check-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.git("init", "-q")
        self.write("config/polityka_danych.json", policy())
        self.write("README.md", "# test\n")

    def git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.repo, check=True, capture_output=True)

    def write(self, relative: str, text: str | bytes) -> None:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            path.write_bytes(text)
        else:
            path.write_text(text, encoding="utf-8")
        self.git("add", "-f", relative)  # celowo omijamy .gitignore — kontrola ma to złapać

    def violations(self) -> tuple[str, ...]:
        return cr.scan_index(self.repo).violations

    def test_clean_index_passes(self):
        self.write("docs/STATUS.md", "stan\n")
        self.write("tlumaczenie/pl_0.jsonl", '{"k": "x"}\n')
        self.assertEqual(self.violations(), ())

    def test_raw_localization_file_is_blocked_anywhere(self):
        self.write("notatki/EN_MainUIText.json", "{}")
        self.assertTrue(any("raw game localization" in v for v in self.violations()))

    def test_game_directories_are_blocked(self):
        self.write("LimbusCompany_Data/Lang/config.json", "{}")
        self.write("x/Resources_moved/Localize/en/StoryData/S1.json", "{}")
        self.write("notatki/static-data/personality/personality-01.json", "{}")
        self.write("x/StaticData/a.json", "{}")
        found = self.violations()
        self.assertEqual(sum("protected directory" in v for v in found), 4)

    def test_game_text_directory_requires_policy_flag(self):
        self.write("wyciag/teksty_0.jsonl", "{}\n")
        self.assertTrue(any("game-text directory" in v for v in self.violations()))

    def test_game_text_allowed_in_public_repository_when_flag_is_set(self):
        self.write("config/polityka_danych.json", policy(allowed=True, public=True))
        self.write("wyciag/teksty_0.jsonl", "{}\n")
        self.write("czytanki/README.md", "# x\n")
        self.assertEqual(self.violations(), ())

    def test_raw_localization_files_blocked_even_when_text_allowed(self):
        self.write("config/polityka_danych.json", policy(allowed=True, public=True))
        self.write("wyciag/KR_MainUIText.json", "{}")
        self.assertTrue(any("raw game localization" in v for v in self.violations()))

    def test_binary_archives_secrets_and_fonts(self):
        self.write("dist/x.txt", "x")
        self.write("a.zip", b"PK")
        self.write("data.bundle", b"x")
        self.write(".env", "TOKEN=1")
        self.write("Font/Context/font.ttf", b"x")
        self.write("assets/fonts/Wolna/font.ttf", b"x")
        found = self.violations()
        self.assertTrue(any("'dist'" in v for v in found))
        self.assertTrue(any(".zip" in v for v in found))
        self.assertTrue(any(".bundle" in v for v in found))
        self.assertTrue(any("environment file" in v for v in found))
        self.assertEqual(sum("fonts are allowed only" in v for v in found), 1)

    def test_size_limit_uses_index_blob(self):
        self.write("duzy.txt", "x" * 2048)
        found = cr.scan_index(self.repo, max_file_bytes=1024).violations
        self.assertTrue(any("limit is 1024 B" in v for v in found))

    def test_missing_policy_is_an_error(self):
        self.git("rm", "-q", "--cached", "config/polityka_danych.json")
        with self.assertRaises(RuntimeError):
            cr.scan_index(self.repo)

    def test_real_repository_policy_matches_owner_decision(self):
        data = json.loads((cr.ROOT / "config" / "polityka_danych.json").read_text("utf-8"))
        # Decyzja właściciela 2026-11-25: publiczne repo, wyciąg i Czytanki w Git.
        self.assertTrue(data["repozytorium_publiczne"])
        self.assertTrue(data["tekst_gry_w_git"])
        self.assertEqual(sorted(data["katalogi_tekstu_gry"]), ["czytanki", "wyciag"])


if __name__ == "__main__":
    unittest.main()
