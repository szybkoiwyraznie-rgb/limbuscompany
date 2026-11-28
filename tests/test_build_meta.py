"""Tests for tools/build_meta.py (the "plik META" Czytanka series).

Uses an invented Localize snapshot in the game's layout; every string is
made up (``Synthetic …``) so no game text leaks into the test suite.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.build_meta import build_index_file, build_mission_file, build_notes_file, build_sinner_file, build_splash_file
from tools.lcb_text import Texts
from tools.localize import Snapshot
from tools.static_data import StaticData


def _doc(rows: list[dict]) -> bytes:
    return json.dumps({"dataList": rows}, ensure_ascii=False).encode("utf-8")


def _fixture() -> dict[str, bytes]:
    files = {
        "StageNode1-0.json": _doc([
            {"id": "10001", "title": "Synthetic stage zero", "desc": "Synthetic desc", "place": "Synthetic place"},
        ]),
        "StageNode1-1.json": _doc([
            {"id": "10102", "title": "Synthetic stage twelve", "desc": "", "place": "Synthetic place 2"},
            {"id": "10108", "title": "Synthetic stage eight", "desc": "", "place": ""},
        ]),
        "TutorialRenewalDesc.json": _doc([
            {"id": "tuto_00_01_01_01", "content": "Synthetic mission text <color=#f8c200>marked</color> one."},
            {"id": "tuto_00_01_01_02", "content": "Synthetic mission text two\\nsecond line"},
            {"id": "tuto_01_02_01_01", "content": "Synthetic mission text for 1-2"},
        ]),
        "TutorialRenewalMainUIDesc.json": _doc([
            {"id": "tuto_10108_01", "content": "Synthetic interface text in stage 1-8"},
            {"id": "tuto_exp_mining_01", "content": "Synthetic tour text"},
        ]),
        "BattleHint.json": _doc([{"id": "1", "content": "Synthetic generic hint"}]),
        "BattleHint_NormalBattle.json": _doc([{"id": "1", "content": "Synthetic normal hint"}]),
        "TutorialPopUpDesc.json": _doc([
            {"id": "tutorial_syn_title", "content": "Synthetic popup title"},
            {"id": "tutorial_syn_1", "content": "Synthetic popup body"},
        ]),
        "StoryTheaterDanteNote.json": _doc([
            {"id": "City", "content": "Synthetic City"},
            {"id": "Limbuscompany", "content": "Synthetic Limbus"},
        ]),
        "StoryTheaterDanteNoteDetail.json": _doc([
            {"id": "DanteNoteDetail_1", "title": "", "desc": "- Synthetic note line one\\n- Synthetic note line two"},
            {"id": "DanteNoteDetail_2", "title": "", "desc": "Synthetic plain paragraph"},
        ]),
        "FileDownloadDesc.json": _doc([
            {"id": "FileDownload_Desc_01", "title": "Synthetic splash title"},
            {"id": "FileDownload_Desc_01", "desc": "Synthetic splash body"},
        ]),
        "IntroduceCharacter.json": _doc([
            {"id": "이상", "name": "Yi Sang", "description": "Synthetic bio one\\nsentence two", "sentence": ""},
            {"id": "파우스트", "name": "Faust", "description": "Synthetic bio two", "sentence": ""},
        ]),
        "Characters.json": _doc([
            {"id": "1", "name": "Synthetic Name One"},
            {"id": "2", "name": "Synthetic Name Two"},
        ]),
    }
    return {f"Localize/en/EN_{name}": data for name, data in files.items()}


class BuildMetaTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        for name, data in _fixture().items():
            path = base / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.snapshot = Snapshot.open(base)
        self.texts = Texts(self.snapshot, "en")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _synthetic_static(self) -> Path:
        """Minimal StaticData tree for the notes file (marker dir + dante tables)."""
        base = Path(self._tmp.name) / "static-data"
        (base / "storytheater-main").mkdir(parents=True, exist_ok=True)
        tree = {"list": [{"mainCategory": {"id": 1, "name": "City"}, "middleCategoryList": [
            {"middleCategory": {"id": 101, "name": "Limbuscompany", "danteNoteDetailId": [1, 2]}},
        ]}]}
        detail = {"list": [
            {"id": 1, "openOrder": 1, "titleOrder": 1, "days": "984.4.20"},
            {"id": 2, "openOrder": 2, "titleOrder": 2, "days": "984.4.21"},
        ]}
        (base / "storytheater-dantenote").mkdir(parents=True, exist_ok=True)
        (base / "storytheater-dantenote" / "storytheater-dantenote-1.json").write_text(
            json.dumps(tree, ensure_ascii=False), encoding="utf-8")
        (base / "storytheater-dantenote-detail").mkdir(parents=True, exist_ok=True)
        (base / "storytheater-dantenote-detail" / "storytheater-dantenote-detail-1.json").write_text(
            json.dumps(detail, ensure_ascii=False), encoding="utf-8")
        return base

    def test_missions_grouped_by_stage_with_markup_stripped(self) -> None:
        text, count = build_mission_file(self.texts, "en")
        self.assertIn("### Etap 0-1 · Synthetic stage zero", text)
        self.assertIn("*Place: Synthetic place*", text)
        self.assertIn("### Etap 1-2 · Synthetic stage twelve", text)
        self.assertIn("### Etap 1-8 · Synthetic stage eight", text)
        # 1-8 has only interface texts: they come after the ui note.
        ui_idx = text.index("*(interface descriptions shown in this stage)*")
        self.assertLess(text.index("### Etap 1-8"), ui_idx)
        self.assertIn("Synthetic interface text in stage 1-8", text[ui_idx:])
        self.assertIn("### Lochy Wydobywcze (PD)", text)
        self.assertIn("### Ogólne", text)
        self.assertIn("### Zwykłe walki", text)
        self.assertIn("### Synthetic popup title", text)
        self.assertIn("Synthetic popup body", text)
        self.assertNotIn("<color", text)
        self.assertEqual(count, 3 + 1 + 1 + 1 + 1 + 1)

    def test_mission_line_breaks_kept_as_hard_breaks(self) -> None:
        text, _ = build_mission_file(self.texts, "en")
        self.assertIn("Synthetic mission text two  \nsecond line", text)

    def test_notes_keywords_and_details(self) -> None:
        static = StaticData(self._synthetic_static())
        text, count = build_notes_file(self.texts, "en", static=static)
        self.assertIn("- **Synthetic City**", text)
        self.assertIn("- **Synthetic Limbus**", text)
        self.assertIn("## Synthetic Limbus", text)
        self.assertIn("### Zapiski #1 - 984.4.20", text)
        self.assertIn("### Zapiski #2 - 984.4.21", text)
        # source bullets stay bullets, plain lines become paragraphs
        self.assertIn("- Synthetic note line one\n\n- Synthetic note line two", text)
        self.assertNotIn("> - Synthetic note line one", text)
        self.assertEqual(count, 4)

    def test_splash_title_desc_pairs(self) -> None:
        text, count = build_splash_file(self.texts, "en")
        self.assertIn("### Synthetic splash title", text)
        self.assertIn("> Synthetic splash body", text)
        self.assertEqual(count, 1)

    def test_sinner_dossier_order_and_names(self) -> None:
        text, count = build_sinner_file(self.texts, "en")
        self.assertIn("### Sinner #1 — Synthetic Name One", text)
        self.assertIn("### Sinner #2 — Synthetic Name Two", text)
        self.assertIn("> Synthetic bio one\n> sentence two", text)
        self.assertEqual(count, 2)

    def test_index_table_lists_files_with_counts(self) -> None:
        table = build_index_file({"01_x_EN.md": ("Title", 7)}, "en")
        self.assertIn("| `01_x_EN.md` | Title | 7 |", table)
        self.assertIn("7 |", table)

    def test_empty_sources_produce_no_files(self) -> None:
        with tempfile.TemporaryDirectory() as empty:
            base = Path(empty) / "en"
            base.mkdir()
            (base / "EN_MainUIText.json").write_bytes(_doc([{"id": "x", "content": "Window"}]))
            with Snapshot.open(Path(empty)) as snap:
                texts = Texts(snap, "en")
            self.assertEqual(build_notes_file(texts, "en"), ("", 0))
            self.assertEqual(build_splash_file(texts, "en"), ("", 0))
            self.assertEqual(build_sinner_file(texts, "en"), ("", 0))


if __name__ == "__main__":
    unittest.main()
