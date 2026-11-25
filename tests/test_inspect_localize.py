from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tests.synthetic_localize import localize_files, write_collector_zip
from tools.inspect_localize import inspect, story_group, summary
from tools.localize import Snapshot, field_name, iter_strings, logical_path, strip_prefix


class LocalizeHelpersTests(unittest.TestCase):
    def test_prefix_is_stripped_from_file_name_only(self):
        self.assertEqual(strip_prefix("EN_MainUIText.json"), "MainUIText.json")
        self.assertEqual(strip_prefix("KR_Skills.json"), "Skills.json")
        self.assertEqual(strip_prefix("MainUIText.json"), "MainUIText.json")
        self.assertEqual(logical_path("StoryData/JP_1D101A.json"), "StoryData/1D101A.json")
        self.assertEqual(logical_path("EN_Dir/EN_File.json"), "EN_Dir/File.json")

    def test_addresses_use_ids_and_mark_repeats(self):
        doc = {"dataList": [
            {"id": 7, "levelList": [{"level": 1, "desc": "a"}, {"level": 2, "desc": "b"}]},
            {"id": "x", "content": "c"},
            {"id": "x", "content": "d"},
            {"content": "e"},
        ]}
        found = dict(iter_strings(doc))
        self.assertEqual(found["dataList[id=7].levelList[level=1].desc"], "a")
        self.assertEqual(found["dataList[id=x].content"], "c")
        self.assertEqual(found["dataList[id=x#2].content"], "d")
        self.assertEqual(found["dataList[#3].content"], "e")
        self.assertEqual(field_name("dataList[id=7].levelList[level=2].desc"), "desc")

    def test_natural_identifiers_keep_addresses_stable_when_rows_are_inserted(self):
        before = {"list": [
            {"abilityID": 11, "simpleDesc": "p"},
            {"key": "AskToMove", "text": "q"},
            {"level": 3, "coinlist": [{"coindescs": [{"desc": "r"}]}]},
        ]}
        after = {"list": [{"abilityID": 10, "simpleDesc": "new"}] + before["list"]}
        old, new = dict(iter_strings(before)), dict(iter_strings(after))
        for address in ("list[abilityID=11].simpleDesc", "list[key=AskToMove].text",
                        "list[level=3].coinlist[#0].coindescs[#0].desc"):
            with self.subTest(address=address):
                self.assertEqual(old[address], new[address])
        # "id" wins over the other identifiers when an item has several.
        self.assertIn("x[id=5].name", dict(iter_strings({"x": [{"id": 5, "level": 1, "name": "n"}]})))

    def test_snapshot_reads_zip_and_directory_identically(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = write_collector_zip(root / "r.zip")
            for member, data in localize_files().items():
                target = root / "dir" / member
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            with Snapshot.open(archive) as a, Snapshot.open(root / "dir") as b:
                self.assertEqual(a.languages, ["en", "kr", "jp"])
                self.assertEqual({k: sorted(v) for k, v in a.files.items()},
                                 {k: sorted(v) for k, v in b.files.items()})
                self.assertEqual(a.read("kr", "Skills.json"), b.read("kr", "Skills.json"))


class InspectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="lcb-inspect-")
        self.addCleanup(self.tmp.cleanup)
        self.zip = write_collector_zip(Path(self.tmp.name) / "LCB_DANE_test.zip")

    def test_report_measures_pairing_fields_and_story_groups(self):
        report = inspect(self.zip)
        self.assertEqual(report["languages"], ["en", "kr", "jp"])
        self.assertEqual(report["pairing"]["logical_files"], 5)
        self.assertEqual(report["pairing"]["in_all_languages"], 4)
        self.assertEqual(report["pairing"]["only_in"]["en"], 1)
        self.assertEqual(report["per_language"]["kr"]["bom_files"], 4)
        self.assertEqual(report["per_language"]["en"]["duplicate_ids"], 1)
        self.assertEqual(report["per_language"]["en"]["empty_strings"], 1)
        self.assertEqual(report["story"]["files_en"], 2)
        self.assertEqual(report["story"]["naming_groups_en"], {"<cyfra>D": 1, "S…": 1})
        self.assertIn("teller", report["story"]["fields_en"])
        self.assertIn("en~kr", report["address_alignment"])
        self.assertNotIn("samples_en", report)

    def test_stdout_summary_contains_no_text(self):
        text = json.dumps(summary(inspect(self.zip)), ensure_ascii=False)
        self.assertNotIn("Synthetic", text)

    def test_samples_only_on_request(self):
        report = inspect(self.zip, samples=3)
        self.assertEqual(len(report["samples_en"]), 3)

    def test_story_group_naming(self):
        self.assertEqual(story_group("StoryData/1D101A.json"), "<cyfra>D")
        self.assertEqual(story_group("StoryData/E3S01A.json"), "E…")
        self.assertEqual(story_group("StoryData/PC0101.json"), "PC…")


if __name__ == "__main__":
    unittest.main()
