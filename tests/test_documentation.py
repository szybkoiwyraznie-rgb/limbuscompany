from __future__ import annotations

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
GUIDES = (
    "README.md",
    "AGENTS.md",
    "ENVIRONMENT.md",
    "LESSONS.md",
    "docs/CEL.md",
    "docs/DECYZJE.md",
    "docs/STATUS.md",
    "docs/WORKFLOW.md",
    "docs/FEASIBILITY.md",
    "docs/COLLECTOR.md",
    "docs/DATA_POLICY.md",
    "docs/FORMAT_LOCALIZE.md",
    "docs/INDEX_FORMAT.md",
    "docs/LANG_FORMAT.md",
    "docs/PAKIET_TLUMACZA.md",
    "docs/PLAN_TLUMACZENIA_AI.md",
    "docs/CZYTANKI.md",
    "docs/EXPERIMENT_LOG.md",
    "docs/PRIOR_ART.md",
    "docs/ROADMAP.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/research.md",
)
INLINE_LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")


def markdown_files() -> list[Path]:
    skip = {".git", "local", "google_drive", "build", "dist", "artifacts", "node_modules"}
    return sorted(
        p for p in ROOT.rglob("*.md") if not skip.intersection(p.relative_to(ROOT).parts)
    )


class DocumentationTests(unittest.TestCase):
    def test_guides_exist_and_are_utf8(self):
        for name in GUIDES:
            with self.subTest(name=name):
                text = (ROOT / name).read_text(encoding="utf-8")
                self.assertTrue(text.strip(), name)

    def test_every_docs_page_is_listed_as_a_guide(self):
        listed = set(GUIDES)
        for path in sorted((ROOT / "docs").glob("*.md")):
            with self.subTest(path=path.name):
                self.assertIn(path.relative_to(ROOT).as_posix(), listed)

    def test_internal_markdown_links_resolve_inside_repository(self):
        for source in markdown_files():
            name = source.relative_to(ROOT).as_posix()
            for link in INLINE_LINK.findall(source.read_text(encoding="utf-8")):
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                with self.subTest(source=name, link=link):
                    target = (source.parent / unquote(parsed.path)).resolve()
                    self.assertTrue(target.is_relative_to(ROOT), link)
                    self.assertTrue(target.exists(), f"{name}: missing {link}")

    def test_current_tools_table_names_existing_or_planned_tools(self):
        workflow = (ROOT / "docs/WORKFLOW.md").read_text(encoding="utf-8")
        for row in workflow.splitlines():
            for tool in re.findall(r"`(tools/[\w/]+\.py)`", row):
                with self.subTest(tool=tool):
                    exists = (ROOT / tool).exists()
                    self.assertTrue(exists or "planowane" in row, f"{tool} missing but not marked planowane")
                    if exists:
                        self.assertNotIn("planowane", row.lower(), f"{tool} exists but marked planowane")

    def test_referenced_docs_in_code_exist(self):
        for path in sorted(list((ROOT / "tools").glob("*.py")) + list((ROOT / "tests").glob("*.py"))):
            for ref in re.findall(r"\bdocs/[A-Z_]+\.md\b", path.read_text(encoding="utf-8")):
                with self.subTest(source=path.name, ref=ref):
                    self.assertTrue((ROOT / ref).exists(), ref)


if __name__ == "__main__":
    unittest.main()
