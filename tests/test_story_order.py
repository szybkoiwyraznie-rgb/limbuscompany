"""Story reading-order reconstruction on invented StoryData and an invented story library."""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools import story_order
from tools.localize import Snapshot


def _story(*lines: str) -> str:
    return json.dumps({"dataList": [{"id": str(i), "content": text} for i, text in enumerate(lines)]})


class StoryOrderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        story = root / "snap" / "en" / "StoryData"
        story.mkdir(parents=True)
        files = {
            "S101B": ("Synthetic opening line about the bus and the city", "Short"),
            "S101A": ("Synthetic closing line of the first invented scene",),
            "1D101A": ("Synthetic dungeon line number one for testing order",),
            "E101X": ("Synthetic side story line that appears on two pages",
                      "Another synthetic side story line for weighting"),
            "P10102": ("Synthetic personal story line never shown on any page",),
            "SHARED": ("Synthetic line duplicated in two files is no fingerprint",),
        }
        for stem, lines in files.items():
            (story / f"EN_{stem}.json").write_text(_story(*lines), encoding="utf-8")
        (story / "EN_SHARED2.json").write_text(_story(files["SHARED"][0]), encoding="utf-8")

        library = root / "library"
        (library / "chapters" / "minis").mkdir(parents=True)
        (library / "index.html").write_text(
            '<a href="chapters/chapter1.html"></a><a href="chapters/minis/side.html"></a>'
            '<a href="chapters/chapter1.html"></a>', encoding="utf-8")

        def page(*runs: str) -> str:
            return "".join(f"<p>{run}</p>" for run in runs)

        (library / "chapters" / "chapter1.html").write_text(page(
            "Synthetic opening line about the bus and the city!",
            "Synthetic closing line of the first invented scene",
            "Synthetic dungeon line number one for testing order",
            "Synthetic side story line that appears on two pages",
            "Synthetic line duplicated in two files is no fingerprint",
        ), encoding="utf-8")
        (library / "chapters" / "minis" / "side.html").write_text(page(
            "Synthetic side story line that appears on two pages",
            "Another synthetic side story line for weighting",
        ), encoding="utf-8")
        self.snapshot = Snapshot.open(root / "snap")
        self.library = library

    def tearDown(self) -> None:
        self.snapshot.close()
        self.tmp.cleanup()

    def test_order_assignment_and_unplaced_files(self) -> None:
        result = story_order.build(self.snapshot, self.library)
        chapters = {c["strona"]: c for c in result["rozdzialy"]}
        self.assertEqual(list(chapters), ["chapters/chapter1.html", "chapters/minis/side.html"])
        self.assertEqual([s for s, _ in chapters["chapters/chapter1.html"]["pliki"]], ["S101B", "S101A", "1D101A"])
        # E101X matched once on chapter1 and twice on the side page: it belongs to the side page.
        self.assertEqual(chapters["chapters/minis/side.html"]["pliki"], [["E101X", 2]])
        self.assertEqual(chapters["chapters/chapter1.html"]["etykieta"], "Canto 1")
        self.assertEqual(chapters["chapters/minis/side.html"]["etykieta"], "Opowiadanie: side")
        self.assertEqual(result["nieprzypisane"], ["P10102", "SHARED", "SHARED2"])
        self.assertEqual(result["pliki_storydata"], 7)
        self.assertEqual(result["przypisane"], 4)

    def test_output_holds_no_game_text(self) -> None:
        text = story_order.dumps(story_order.build(self.snapshot, self.library))
        self.assertNotIn("Synthetic", text)
        self.assertIn('["S101B", 1]', text)
        json.loads(text)

    def test_sort_key_rule(self) -> None:
        stems = ["E101A", "S102B", "1D101A", "S101A", "S101I2", "S101B", "S101I", "PC01B", "ES01B", "P10102"]
        self.assertEqual(sorted(stems, key=story_order.story_sort_key),
                         ["S101B", "S101I", "S101I2", "S101A", "S102B", "1D101A", "E101A", "ES01B", "PC01B", "P10102"])

    def test_cli_writes_report(self) -> None:
        out = Path(self.tmp.name) / "out" / "order.json"
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            code = story_order.main([str(self.snapshot.source), str(self.library), "--out", str(out)])
        self.assertIn("przypisane: 4", stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out.read_text(encoding="utf-8"))["format"], story_order.FORMAT)


if __name__ == "__main__":
    unittest.main()
