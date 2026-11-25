"""Moduł lc_localize i narzędzie rozpoznania na wymyślonym drzewie Localize."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests import syntetyczne as syn
from tools import lc_localize as lc
from tools.rozpoznanie_localize import analizuj


ROOT = Path(__file__).resolve().parent.parent


class LocalizeModuleTests(unittest.TestCase):
    def test_logical_names_strip_language_prefix_only_from_filename(self):
        self.assertEqual(lc.nazwa_logiczna("en", "EN_MainUIText.json"), "MainUIText.json")
        self.assertEqual(lc.nazwa_logiczna("kr", "StoryData/KR_S101B.json"), "StoryData/S101B.json")
        self.assertEqual(lc.nazwa_logiczna("jp", "JPN_folder/X.json"), "JPN_folder/X.json")
        self.assertEqual(lc.wzorzec_nazwy("StoryData/S101B.json"), "S{n}B.json")

    def test_text_leaves_use_list_patterns(self):
        obj = {"dataList": [{"id": 1, "levelList": [{"name": "a", "coinlist": [{"desc": "b"}]}]}]}
        self.assertEqual(
            list(lc.liscie_tekstowe(obj)),
            [("dataList[].levelList[].name", "a"), ("dataList[].levelList[].coinlist[].desc", "b")],
        )

    def test_directory_input_accepts_game_root_data_or_localize(self):
        with tempfile.TemporaryDirectory() as tmp:
            game = Path(tmp) / "Limbus Company"
            localize = game / "LimbusCompany_Data" / lc.KATALOG_LOCALIZE
            syn.zapisz_drzewo(localize, syn.drzewo_localize())
            for start in (game, game / "LimbusCompany_Data", localize):
                zbior = lc.z_katalogu(start)
                self.assertEqual(sorted(zbior.pliki), ["en", "jp", "kr"])

    def test_duplicate_logical_file_is_an_error(self):
        zbior = lc.ZbiorLokalizacji()
        zbior.dodaj(lc.PlikLokalizacji("en", "EN_A.json", "A.json", b"{}"))
        with self.assertRaises(ValueError):
            zbior.dodaj(lc.PlikLokalizacji("en", "A.json", "A.json", b"{}"))


class RozpoznanieTests(unittest.TestCase):
    def setUp(self):
        zbior = lc.ZbiorLokalizacji()
        for wzgledna, dane in syn.drzewo_localize().items():
            lc._dodaj_wzgledny(zbior, wzgledna, dane)
        self.raport = analizuj(zbior)
        self.pliki = {p["nazwa"]: p for p in self.raport["pliki"]}

    def test_parity_and_id_checks(self):
        par = self.raport["parzystosc"]
        self.assertEqual(self.raport["plikow_logicznych"], 5)
        self.assertEqual(par["we_wszystkich_jezykach"], 3)
        self.assertEqual(par["tylko_w_jednym"]["en"], ["OnlyEnglish.json"])
        self.assertEqual(par["niezgodne_id"], ["MainUIText.json"])
        self.assertEqual(self.raport["bledny_json"], {"kr": 1})

    def test_story_structure_and_duplicate_ids(self):
        story = self.pliki["StoryData/S101B.json"]
        self.assertEqual(story["rekordow"], 4)
        self.assertEqual(story["duplikaty_id"], 1)
        self.assertEqual(story["pola"]["dataList[].content"], 4)
        self.assertEqual(story["napisy"]["en"]["niepustych"], 5)
        self.assertEqual(story["napisy"]["kr"]["z_hangul"], 5)
        self.assertEqual(self.raport["katalogi"], {"(korzen)": 4, "StoryData": 1})
        self.assertIn("StoryData/S{n}B.json", self.raport["rodziny_nazw"])

    def test_report_contains_no_text_values(self):
        dump = json.dumps(self.raport, ensure_ascii=False)
        for fragment in ("Lorem", "가나다", "あいう", "cios", "moneta"):
            self.assertNotIn(fragment, dump)

    def test_cli_on_collector_zip_writes_json_and_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "LC_DANE_x.zip"
            archive.write_bytes(syn.zwrot_zbieracza(syn.drzewo_localize()))
            out, md = Path(tmp) / "r.json", Path(tmp) / "r.md"
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools" / "rozpoznanie_localize.py"), str(archive),
                 "--wyj", str(out), "--md", str(md)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            raport = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(raport["wejscie"]["buildid"], "123456")
            self.assertIn("| en | 5 |", md.read_text(encoding="utf-8"))
            self.assertNotIn("Lorem", result.stdout + out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
