from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.check_repository import (
    MAX_FILE_BYTES,
    IndexEntry,
    entry_violations,
    scan_index,
)


ROOT = Path(__file__).resolve().parent.parent


def entry(path: str, *, mode: str = "100644", stage: int = 0) -> IndexEntry:
    return IndexEntry(path=path, mode=mode, oid="synthetic", stage=stage)


class PathPolicyTests(unittest.TestCase):
    def test_private_directories_are_blocked_at_any_depth_case_insensitively(self):
        for path in (
            "local/entries.jsonl",
            "data/LOCAL/source.txt",
            "build/kit.txt",
            "foo/google_drive/report.txt",
            "node_modules/package/readme.md",
            "LimbusCompany_Data/Assets/Resources_moved/Localize/en/EN_MainUIText.json",
            "kopia/limbuscompany_data/Lang/config.json",
        ):
            with self.subTest(path=path):
                self.assertTrue(entry_violations(entry(path), 1))

    def test_unity_binaries_archives_and_secrets_are_blocked_even_if_forced(self):
        for path in (
            "game/sharedassets0.assets",
            "game/sharedassets0.assets.resS",
            "game/data.unity3d",
            "game/LimbusCompany.exe",
            "game/GameAssembly.dll",
            "game/globalgamemanagers",
            "il2cpp/global-metadata.dat",
            "output/result.zip",
            "credentials/private.key",
            ".env",
            "config/.env.local",
        ):
            with self.subTest(path=path):
                self.assertTrue(entry_violations(entry(path), 1))

    def test_fonts_only_in_dedicated_directory(self):
        self.assertEqual(entry_violations(entry("assets/fonts/NotoSans-Regular.ttf"), 1), [])
        for path in ("Font/Context/ContextFont.ttf", "pakiet/Font/Title/TitleFont.otf"):
            with self.subTest(path=path):
                self.assertTrue(entry_violations(entry(path), 1))

    def test_text_and_safe_example_names_are_not_blanket_blocked(self):
        for path in (
            "README.md",
            "docs/STATUS.md",
            "index/teksty_0.jsonl",
            "tlumaczenie/pl_0.jsonl",
            "tests/fixtures/sample.txt",
            "collector/zbierz.ps1",
            ".env.example",
            "config/.env.example",
        ):
            with self.subTest(path=path):
                self.assertEqual(entry_violations(entry(path), 1), [])

    def test_size_limit_is_exact_and_applies_to_index_blob(self):
        self.assertEqual(entry_violations(entry("data/a.jsonl"), MAX_FILE_BYTES), [])
        issues = entry_violations(entry("data/a.jsonl"), MAX_FILE_BYTES + 1)
        self.assertTrue(any("staged blob" in issue for issue in issues))

    def test_unresolved_conflict_and_unreviewed_submodule_are_blocked(self):
        self.assertTrue(entry_violations(entry("notes.md", stage=2), 1))
        self.assertTrue(entry_violations(entry("vendor/source", mode="160000"), None))


class RealIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="lcb-policy-test-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git("init", "--quiet")

    def git(self, *args: str):
        return subprocess.run(["git", *args], cwd=self.repo, check=True, capture_output=True)

    def put(self, name: str, content: bytes):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def test_large_staged_blob_is_not_hidden_by_smaller_working_tree_file(self):
        self.put("data/sample.txt", b"01234567890")
        self.git("add", "--", "data/sample.txt")
        self.put("data/sample.txt", b"x")
        result = scan_index(self.repo, max_file_bytes=10)
        self.assertEqual(result.entries, 1)
        self.assertTrue(any("staged blob is 11 B" in issue for issue in result.violations))

    def test_unstaged_growth_does_not_change_what_is_in_the_index(self):
        self.put("data/sample.txt", b"x")
        self.git("add", "--", "data/sample.txt")
        self.put("data/sample.txt", b"x" * 20)
        result = scan_index(self.repo, max_file_bytes=10)
        self.assertEqual(result.violations, ())

    def test_force_added_ignored_game_file_is_still_rejected(self):
        self.put(".gitignore", b"local/\n*.assets\n")
        self.put("local/sharedassets0.assets", b"synthetic fixture, not game data")
        self.git("add", "--", ".gitignore")
        self.git("add", "-f", "--", "local/sharedassets0.assets")
        result = scan_index(self.repo)
        self.assertTrue(any("local/sharedassets0.assets" in issue for issue in result.violations))

    def test_unicode_and_spaces_in_tracked_paths_are_supported(self):
        self.put("data/źródło próbne.txt", b"synthetic")
        self.git("add", "--", "data/źródło próbne.txt")
        result = scan_index(self.repo)
        self.assertEqual(result.entries, 1)
        self.assertEqual(result.violations, ())


class RepositoryConfigurationTests(unittest.TestCase):
    def ignored(self, paths: list[str]) -> set[str]:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-z", "--stdin"],
            cwd=ROOT,
            input=("\0".join(paths) + "\0").encode("utf-8"),
            capture_output=True,
            check=False,
        )
        self.assertIn(result.returncode, (0, 1), result.stderr)
        return {p for p in result.stdout.decode("utf-8").split("\0") if p}

    def test_gitignore_blocks_typical_private_files_but_allows_text_sources(self):
        ignored = {
            "google_drive/LCB_DANE.zip",
            "artifacts/LCB_ZBIERZ_DANE.zip",
            "LimbusCompany_Data/Lang/config.json",
            ".env",
            "game/LimbusCompany.exe",
            "game/GameAssembly.dll",
            "game/sharedassets0.assets",
            "game/archive.zip",
            "node_modules/module/index.js",
        }
        allowed = {
            "README.md",
            "index/teksty_0.jsonl",
            "tlumaczenie/pl_0.jsonl",
            "tests/fixtures/example.txt",
            "collector/URUCHOM.bat",
            ".env.example",
            # D-12 (2026-11-25): artefakty pracy agentów w `local/` są commitowane.
            "local/source.jsonl",
            "nested/local/source.txt",
        }
        found = self.ignored(sorted(ignored | allowed))
        self.assertEqual(found, ignored)

    def test_windows_scripts_keep_their_bytes(self):
        result = subprocess.run(
            ["git", "check-attr", "text", "--", "collector/URUCHOM.bat", "collector/zbierz.ps1"],
            cwd=ROOT, capture_output=True, check=True,
        )
        lines = result.stdout.decode("utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        for line in lines:
            self.assertTrue(line.endswith("text: unset"), line)


if __name__ == "__main__":
    unittest.main()
