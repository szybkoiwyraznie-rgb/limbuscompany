"""Story index, Czytanka, Identity profile and translator package on invented data.

Every string and number here is made up; only the table layout follows the
game (StaticData ``{"list": [...]}``, Localize ``{"dataList": [...]}``).
"""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from tools import build_package, build_profiles, build_reading, package_views, story_index
from tools.lcb_text import Texts, to_markdown
from tools.localize import Snapshot
from tools.static_data import StaticData


def _write(path: Path, doc: object, bom: bool = False, raw: str | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (raw if raw is not None else json.dumps(doc, ensure_ascii=False)).encode("utf-8")
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + data)


def _scene(lang: str, stem: str, place: bool = False) -> dict:
    rows = [{"id": -1, "content": f"Episode {stem}"},
            {"id": 0, "model": "모델", "content": f"<i>Line</i> {lang} {stem} one"},
            {"id": 1, "content": f"Narration {lang} {stem} ■■■"},
            {"id": 2, "teller": f"Teller {lang}", "title": f"Epithet {lang}", "content": f"<Tick {lang}>"},
            {"id": 3, "teller": "Me", "title": "■■■", "content": "<Ghaagh…! ■■■■■■>"},
            {"id": 4, "teller": "Dante", "title": "Me", "content": "<Second tick>"}]
    if place:
        rows[1]["place"] = f"Place {lang}"
    return {"dataList": rows}


class StoryToolsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        sd = root / "static-data"
        self.sd = sd
        _write(sd / "storytheater-main" / "a.json", {"list": [
            {"chapterId": 1, "subChapterId": 101, "storyList": [
                {"id": 2, "storyId": "S102B", "nodeId": 10102, "stageDetail": "Before"},
                {"id": 1, "storyId": "S101B", "nodeId": 10101, "stageDetail": "Before"},
            ]},
            {"chapterId": 1, "subChapterId": 102, "storyList": [
                {"id": 1, "storyId": "S201B", "nodeId": 10201, "stageDetail": "Before"}]},
        ]}, bom=True)
        _write(sd / "storytheater-other" / "b.json", {"list": [
            {"chapterId": 91, "subChapterId": 9101, "sortingOrder": 1, "storyList": [
                {"id": 1, "storyId": "E101B", "nodeId": 910101, "stageDetail": "Before"}]},
            {"chapterId": 90, "subChapterId": 9001, "sortingOrder": 2,
             "unLockCondition": {"chapterId": 1, "subChapterId": 102}, "storyList": [
                 {"id": 1, "storyId": "E001X"}]},
        ]})
        _write(sd / "story" / "story.json", {"list": [{"id": 10103, "storyId": "S103A"}]})
        _write(sd / "battle-story" / "c.json", {"list": [
            {"id": 10101, "story": {"enter": ["S101B"], "others": [{"phase": "X", "storyID": "S101I"}]}}]})
        # a shipped table with a trailing comma, as in the real data
        _write(sd / "skill" / "s.json", None, raw='{"list": [{"id": 1000101, "skillData": ['
               '{"gaksungLevel": 1, "attributeType": "CRIMSON", "atkType": "SLASH", "defType": "ATTACK",'
               ' "targetNum": 1, "skillLevelCorrection": 0, "defaultValue": 4,'
               ' "coinList": [{"operatorType": "ADD", "scale": 2}, {"operatorType": "ADD", "scale": 2},]},'
               '{"gaksungLevel": 3, "defaultValue": 5}]}]}')
        _write(sd / "personality" / "p.json", {"list": [
            {"id": 10001, "characterId": 1, "rank": 2, "season": 9104, "hp": {"defaultStat": 70, "incrementByLevel": 2.5},
             "defCorrection": -1, "minSpeedList": [2, 3], "maxSpeedList": [5, 6], "uniqueAttribute": "CRIMSON",
             "breakSection": {"sectionList": [60, 30]},
             "resistInfo": {"atkResistList": [{"type": "SLASH", "value": 0.5}, {"type": "HIT", "value": 2}]},
             "attributeList": [{"skillId": 1000101, "number": 3}], "skillKeywordList": ["Burn"],
             "associationList": ["SYNTH"]}]})
        _write(sd / "personality-passive" / "pp.json", {"list": [
            {"personalityID": 10001, "battlePassiveList": [{"level": 2, "passiveIDList": [1000101]}]}]})
        _write(sd / "passive" / "passive.json", {"list": [
            {"id": 1000101, "attributeResonanceCondition": [{"type": "CRIMSON", "value": 3}]}]})
        _write(sd / "storytheater-personality" / "x.json", {"list": [
            {"characterId": 1, "storyList": [{"personalityId": 10001, "personalityStoryList": [
                {"storyId": "P10001", "order": 1}]}]}]})

        snap = root / "snap"
        self.snap = snap
        for lang in ("en", "kr"):
            p = lang.upper() + "_"
            base = snap / lang
            for stem in ("S101B", "S101I", "S102B", "S103A", "S201B", "E101B", "E001X", "P10001", "S199B"):
                _write(base / "StoryData" / f"{p}{stem}.json", _scene(lang, stem, place=stem == "S101B"))
            _write(base / f"{p}StageChapterText.json", {"dataList": [
                {"id": "chapter_a_101", "chapter": f"Canto I {lang}", "chaptertitle": f"Title {lang}", "timeline": "984-01"},
                {"id": "chapter_a_9101", "chapter": f"Intervallo {lang}", "chaptertitle": f"Inter {lang}"},
                {"id": "chapter_a_102", "chapter": f"Canto II {lang}", "chaptertitle": f"Second {lang}"}]})
            _write(base / f"{p}StageNode1-1.json", {"dataList": [
                {"id": "10101", "title": f"Stage {lang}", "place": f"Stage place {lang}", "desc": f"Stage desc {lang}"}]})
            _write(base / f"{p}StoryTheaterMain.json", {"dataList": [{"id": "CHAPTER_101", "desc": "Epigraph"}]})
            _write(base / f"{p}ScenarioModelCodes-AutoCreated.json", {"dataList": [{"id": "모델", "name": f"Model {lang}"}]})
            _write(base / f"{p}Personalities.json", {"dataList": [
                {"id": 10001, "title": f"Synthetic\\nOffice {lang}", "name": f"Hero {lang}", "desc": "Invented"}]})
            _write(base / f"{p}Characters.json", {"dataList": [{"id": 1, "name": f"Hero {lang}"}]})
            _write(base / f"{p}Skills_personality-01.json", {"dataList": [{"id": 1000101, "levelList": [
                {"level": 1, "name": f"Cut {lang}", "desc": "[WhenUse] Inflict 1 [Burn]",
                 "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 1 [Burn]"}]}]}]}]})
            _write(base / f"{p}Passives.json", {"dataList": [{"id": 1000101, "name": f"Calm {lang}", "desc": "Invented"}]})
            _write(base / f"{p}AttributeText.json", {"dataList": [{"id": "CRIMSON", "name": "Wrath"}]})
            _write(base / f"{p}SkillTag.json", {"dataList": [{"id": "WhenUse", "name": "[On Use]"},
                                                             {"id": "OnSucceedAttack", "name": "[On Hit]"}]})
            _write(base / f"{p}Bufs.json", {"dataList": [{"id": "Burn", "name": "Burn"}]})
            _write(base / "PersonalityVoiceDlg" / f"{p}Voice_Hero_10001.json", {"dataList": [
                {"id": "get", "desc": "Acquisition", "dlg": "Invented voice line"}]})
        self.static = StaticData(sd)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _index(self) -> dict:
        with Snapshot.open(self.snap) as snapshot:
            return story_index.build(self.static, snapshot)

    def test_index_order_and_sources(self) -> None:
        index = self._index()
        self.assertEqual([c["id"] for c in index["rozdzialy"]], [101, 9101, 102, 9001])
        canto = index["rozdzialy"][0]["sceny"]
        self.assertEqual([s["plik"] for s in canto], ["S101B", "S101I", "S102B", "S103A", "S199B"])
        self.assertEqual(canto[1]["etap"], "walka")
        self.assertEqual(canto[3]["zrodlo"], "story")
        self.assertEqual(canto[4]["zrodlo"], "regula_nazw")
        self.assertEqual(index["identity"][0]["pliki"], ["P10001"])
        self.assertEqual(index["nieprzypisane"], [])
        text = story_index.dumps(index)
        self.assertIn('{"plik": "S101B", "etap": "przed", "wezel": 10101}', text)
        self.assertEqual(json.loads(text), index)

    def test_reading_layout(self) -> None:
        index = self._index()
        with Snapshot.open(self.snap) as snapshot:
            texts = Texts(snapshot, "en")
            name, text, stats = build_reading.build_chapter(index["rozdzialy"][0], texts,
                                                            build_reading.Chapters(texts), "en")
        self.assertEqual(name, "Canto I en: Title en")
        self.assertTrue(text.startswith("# Limbus Company — Canto I en: Title en\n"))
        self.assertIn("### Etap 1-1 · Stage en", text)
        self.assertIn("*Miejsce: Stage place en*", text)
        self.assertIn("#### Place en", text)
        self.assertIn(
            "**Model en:** *Line* en S101B one\n"
            "Narration en S101B ***\n"
            "**Teller en** (*Epithet en*): Tick en\n"
            "**Ja** (***): Ghaagh…! ***\n"
            "**Dante** (*Ja*): Second tick\n\n"
            "<!-- S101I -->",
            text,
        )
        self.assertNotIn("■", text)
        self.assertNotIn("**Me", text)
        self.assertNotIn("(*Me*)", text)
        self.assertNotIn("\\<", text)
        self.assertIn("*— W trakcie walki —*", text)
        self.assertEqual(stats["sceny"], 5)

    def test_profile(self) -> None:
        with Snapshot.open(self.snap) as snapshot:
            library = build_profiles.Library(self.static, Texts(snapshot, "en"))
            name, text = library.sinner_file(1, "en")
        self.assertEqual(name, "Hero en")
        self.assertIn("### 00 Synthetic Office en — Hero en", text)
        self.assertIn("| Szybkość (ulepszenia 1–4) | 2–5 / 3–6 |", text)
        self.assertIn("Slash ×0,5 (Endured)", text)
        self.assertIn("| Sezon | wydarzenie 9104 |", text)
        self.assertIn("| 1 | Wrath | Slash | 4 | +2 | 2 | +0 | 1 |", text)
        self.assertIn("| 3 | Wrath | Slash | 5 | +2 | 2 | +0 | 1 |", text)
        self.assertIn("[On Use] Inflict 1 [Burn]", text)
        self.assertIn("Moneta 2: [On Hit] Gain 1 [Burn]", text)
        self.assertIn("*od ulepszenia 2; rezonans 3× Wrath*", text)
        self.assertIn("- **Acquisition:** Invented voice line", text)

    def test_package(self) -> None:
        index = self._index()
        with Snapshot.open(self.snap) as snapshot:
            files, counts = build_package.build(index, build_package.Story(snapshot))
        self.assertIn("spis-scen.md", files)
        chapter = next(text for name, text in files.items() if name.startswith("01_"))
        self.assertIn("## Scena 1/", chapter)
        self.assertIn("- etap: 1-1 · Stage kr — Stage en", chapter)
        self.assertIn("- moment: przed walką", chapter)
        self.assertIn("1. [Dialog - Model kr (Model en)] <i>Line</i> kr S101B one", chapter)
        self.assertIn("   tokeny: zachowaj dokładnie: <i>, </i>", chapter)
        self.assertIn("   EN: <i>Line</i> en S101B one", chapter)
        self.assertIn("   miejsce: Place kr — Place en", chapter)
        glossary = files["mowcy-i-miejsca.md"]
        self.assertIn("[Imię mówcy] Teller kr", glossary)
        self.assertIn("[Tytuł mówcy] Epithet kr", glossary)
        self.assertTrue(any(name.startswith("identity-01") for name in files))
        self.assertEqual(counts["sceny"], 9)

    def test_package_zip_is_deterministic(self) -> None:
        out = Path(self.tmp.name) / "out"
        index_path = Path(self.tmp.name) / "index.json"
        index_path.write_text(story_index.dumps(self._index()), encoding="utf-8")
        digests = []
        for _ in range(2):
            with contextlib.redirect_stdout(io.StringIO()):
                build_package.main([
                    str(self.snap),
                    "--index", str(index_path),
                    "--static-data", str(self.sd),
                    "--out", str(out),
                ])
            data = (out / "plik_dla_tlumacza_v1.zip").read_bytes()
            digests.append(data)
        self.assertEqual(digests[0], digests[1])
        with zipfile.ZipFile(out / "plik_dla_tlumacza_v1.zip") as archive:
            self.assertEqual(sorted(archive.namelist()), ["README.md", "sceny.zip", "widoki.zip"])

        out_story = Path(self.tmp.name) / "out_story"
        with contextlib.redirect_stdout(io.StringIO()):
            build_package.main([str(self.snap), "--index", str(index_path), "--no-views", "--out", str(out_story)])
        with zipfile.ZipFile(out_story / "plik_dla_tlumacza_v1.zip") as archive:
            self.assertEqual(sorted(archive.namelist()), ["README.md", "sceny.zip"])

    def test_views_context_uptie_dedup_lyrics_and_en_only_coverage(self) -> None:
        # Add Uptie 1-3 skill progression, BgmLyrics (DKR vs DEN), RPGSystem speakers, and an EN-only file
        _write(self.snap / "kr" / "KR_Skills_personality-01.json", {"dataList": [{"id": 1000101, "levelList": [
            {"level": 1, "name": "Cut kr", "desc": "[WhenUse] Inflict 1 [Burn]",
             "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 1 [Burn]"}]}]},
            {"level": 2, "name": "Cut kr", "desc": "[WhenUse] Inflict 1 [Burn]",
             "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 1 [Burn]"}]}]},
            {"level": 3, "name": "Cut kr", "desc": "[WhenUse] Inflict 2 [Burn]",
             "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 2 [Burn]"}]}]},
        ]}]})
        _write(self.snap / "en" / "EN_Skills_personality-01.json", {"dataList": [{"id": 1000101, "levelList": [
            {"level": 1, "name": "Cut en", "desc": "[WhenUse] Inflict 1 [Burn]",
             "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 1 [Burn]"}]}]},
            {"level": 2, "name": "Cut en", "desc": "[WhenUse] Inflict 1 [Burn]",
             "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 1 [Burn]"}]}]},
            {"level": 3, "name": "Cut en", "desc": "[WhenUse] Inflict 2 [Burn]",
             "coinlist": [{}, {"coindescs": [{"desc": "[OnSucceedAttack] Gain 2 [Burn]"}]}]},
        ]}]})
        _write(self.snap / "kr" / "BgmLyrics" / "KR_BgmLyrics_Test.json", {"dataList": [
            {"id": 0, "content": "<style=\"DKR_CP9_1\">노래 가사"},
        ]})
        _write(self.snap / "en" / "BgmLyrics" / "EN_BgmLyrics_Test.json", {"dataList": [
            {"id": 0, "content": "<style=\"DEN_CP9_1\">Song lyric"},
        ]})
        _write(self.snap / "kr" / "RPGSystem" / "KR_rpg-loc-dialogue-floor-1-a.json", {"dataList": [
            {"key": "D1", "texts": [
                {"index": 0, "speaker": "단테", "text": "<첫 번째 대사>"},
                {"index": 1, "speaker": "단테", "text": "<두 번째 대사>"},
            ]},
        ]})
        _write(self.snap / "en" / "RPGSystem" / "EN_rpg-loc-dialogue-floor-1-a.json", {"dataList": [
            {"key": "D1", "texts": [
                {"index": 0, "speaker": "Dante", "text": "<First line>"},
                {"index": 1, "speaker": "Dante", "text": "<Second line>"},
            ]},
        ]})
        _write(self.snap / "en" / "EN_UserBanner-a1c8p1.json", {"dataList": [
            {"id": 99, "name": "English Only Banner", "desc": "Obtained in test"},
        ]})

        with Snapshot.open(self.snap) as snapshot:
            files, stats = package_views.build_views(snapshot, self.static)

        self.assertIn("spis-widokow.md", files)
        self.assertIn("mowcy-rpg-i-anomalii.md", files)
        self.assertNotIn("09_pozostale_widoki.md", files)
        self.assertGreater(stats["widoki_liscie_json"], 0)

        sinner_md = files["02_tozsamosc_01_Yi_Sang.md"]
        self.assertIn("## [00] Synthetic Office en — Hero en", sinner_md)
        self.assertIn("parametry karty: rzadkość `00`", sinner_md)
        self.assertIn("Umiejętność 1 (×3) (ulepszenia 1–3) — nazwa] Cut kr", sinner_md)
        self.assertIn(
            "źródło: Skills_personality-01.json :: dataList[id=1000101].levelList[level=1].desc ; dataList[id=1000101].levelList[level=2].desc",
            sinner_md,
        )
        self.assertIn("znaczenie tagów: [WhenUse] = [On Use] / [On Use]; [Burn] = Burn / Burn", sinner_md)
        self.assertIn("Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath)", sinner_md)
        self.assertIn("Kwestia głosowa [get] (Acquisition)", sinner_md)

        lyrics_md = files["05_muzyka_i_piosenki.md"]
        self.assertIn('tokeny: zachowaj dokładnie: <style="DEN_CP9_1">', lyrics_md)
        self.assertIn("czcionka: użyj stylu łacińskiego z EN", lyrics_md)

        rpg_md = files["06_tryb_rpg_canto10.md"]
        self.assertIn("[Dialog RPG [D1] — 단테 (Dante)] <첫 번째 대사>", rpg_md)
        self.assertIn("[Mówca w trybie RPG (Canto X)] 단테", files["mowcy-rpg-i-anomalii.md"])
        self.assertIn("występuje: 2×", files["mowcy-rpg-i-anomalii.md"])

        shop_md = files["08_przedmioty_sklep_i_profil.md"]
        self.assertIn("tylko EN w danych gry] English Only Banner", shop_md)

    def test_views_coverage_gate_verifies_all_translatable_leaves(self) -> None:
        with Snapshot.open(self.snap) as snapshot:
            corpus = package_views.Corpus(snapshot, self.static)
            total = sum(len(v) for v in corpus.translatable.values())
            self.assertGreater(total, 0)
            _, stats = package_views.build_views(snapshot, self.static)
            self.assertEqual(stats["widoki_liscie_json"], total)

    def test_markup(self) -> None:
        self.assertEqual(to_markdown("<ruby=cannon>pao</ruby> <color=#fff>x</color> <b>y</b>"), "pao (cannon) x **y**")
        self.assertEqual(to_markdown("[Burn][TabExplain]", {"Burn": "Burn", "TabExplain": ""}), "[Burn]")
        self.assertEqual(to_markdown("<Hey>"), "\\<Hey>")
        self.assertEqual(to_markdown("<Ghaagh…!>", strip_ticking=True), "Ghaagh…!")
        self.assertEqual(to_markdown("<i><Are these photos?></i>", strip_ticking=True), "*Are these photos?*")
        self.assertEqual(to_markdown("engraving the ■■■■■■ and ■■■"), "engraving the *** and ***")


if __name__ == "__main__":
    unittest.main()
