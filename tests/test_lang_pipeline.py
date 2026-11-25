"""End-to-end synthetic tests for ``tools/import_zwrotki.py`` and ``tools/build_lang.py``.

Every string and number in this file is invented; no game prose is used.
"""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import struct
import tempfile
import unittest
import zipfile

from tools import build_lang, build_package, import_zwrotki, story_index
from tools.localize import Snapshot, iter_strings, load_json
from tools.static_data import StaticData


def _write_json(path: Path, doc: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _fill_pl_lines(md_text: str, mapping: dict[str, str]) -> str:
    """Fill ``   PL:`` lines according to ``EN:`` value in a generated package Markdown file."""
    out: list[str] = []
    last_en = ""
    for line in md_text.splitlines():
        if line.startswith("   EN:"):
            last_en = line[len("   EN:"):].strip()
        if line == "   PL:" and last_en in mapping:
            out.append(f"   PL: {mapping[last_en]}")
        else:
            out.append(line)
    return "\n".join(out) + "\n"


class LangPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        sd = self.root / "static-data"
        self.sd = sd
        _write_json(sd / "storytheater-main" / "main.json", {"list": [
            {"chapterId": 1, "subChapterId": 100, "storyList": [
                {"id": 1, "storyId": "S001B", "nodeId": 10001, "stageDetail": "Before"},
                {"id": 2, "storyId": "S002B", "nodeId": 10002, "stageDetail": "Before"},
            ]},
        ]})
        _write_json(sd / "skill" / "s.json", {"list": [
            {"id": 1010101, "skillData": [
                {"gaksungLevel": 1, "attributeType": "CRIMSON", "atkType": "SLASH", "defType": "ATTACK",
                 "targetNum": 1, "skillLevelCorrection": 0, "defaultValue": 4,
                 "coinList": [{"operatorType": "ADD", "scale": 2}]},
                {"gaksungLevel": 4, "defaultValue": 5},
            ]}
        ]})
        _write_json(sd / "personality" / "p.json", {"list": [
            {"id": 10101, "characterId": 1, "rank": 1, "season": 1,
             "hp": {"defaultStat": 66, "incrementByLevel": 2.2},
             "defCorrection": 0, "minSpeedList": [4], "maxSpeedList": [7],
             "uniqueAttribute": "CRIMSON", "breakSection": {"sectionList": [70]},
             "resistInfo": {"atkResistList": [{"type": "SLASH", "value": 1.0}]},
             "attributeList": [{"skillId": 1010101, "number": 3}],
             "skillKeywordList": ["Sinking"], "associationList": ["SYNTH"]}
        ]})
        _write_json(sd / "personality-passive" / "pp.json", {"list": []})
        _write_json(sd / "passive" / "pa.json", {"list": []})

        snap = self.root / "localize"
        self.snap = snap
        for lang in ("kr", "en"):
            p = f"{lang.upper()}_"
            base = snap / lang
            _write_json(base / "StoryData" / f"{p}S001B.json", {"dataList": [
                {"id": -1, "content": "Header"},
                {"id": 0, "place": f"Forest {lang}", "model": "모델A", "teller": f"Scout {lang}",
                 "title": f"Rank {lang}", "content": f"<i>Hello</i> {{0}} {lang}" if lang == "en" else "<i>안녕</i> {0} kr"},
                {"id": 1, "teller": "Dante", "content": "<I think therefore I am>" if lang == "en" else "<나는 생각한다>"},
                {"id": 2, "content": "<ruby=Alpha Reading>Base</ruby>" if lang == "en" else "<ruby=알파>Base</ruby>"},
                {"id": 3, "content": "Line one\nLine two" if lang == "en" else "첫 줄\n둘째 줄"},
            ]})
            # S002B repeats line 0 from S001B in the same chapter to test cross-scene repeat inheritance
            _write_json(base / "StoryData" / f"{p}S002B.json", {"dataList": [
                {"id": 0, "teller": f"Scout {lang}", "content": f"<i>Hello</i> {{0}} {lang}" if lang == "en" else "<i>안녕</i> {0} kr"},
                {"id": 1, "content": f"Second scene unique {lang}"},
            ]})
            _write_json(base / f"{p}LoginUIText.json", {"dataList": [
                {"id": "switch_allcacheclear", "content": "Clear all caches" if lang == "en" else "캐시 전체 삭제"},
                {"id": "custom_localize_button", "content": "Select Custom Language" if lang == "en" else "커스텀 언어 선택"},
            ]})
            _write_json(base / f"{p}MainUIText.json", {"dataList": [
                {"id": "mainui_main_button1", "content": "Sinners" if lang == "en" else "수감자"},
                {"id": "mainui_main_button2", "content": "Theater" if lang == "en" else "극장"},
                {"id": "dup_btn_a", "content": "Confirm" if lang == "en" else "확인"},
                {"id": "dup_btn_b", "content": "Confirm" if lang == "en" else "확인"},
            ]})
            _write_json(base / f"{p}StageChapterText.json", {"dataList": [
                {"id": "chapter_p_100", "chapter": "Prologue", "chaptertitle": f"Woods {lang}"}
            ]})
            _write_json(base / f"{p}StageNode1-1.json", {"dataList": [
                {"id": "10001", "title": f"Node {lang}", "place": f"Clearing {lang}", "desc": f"Desc {lang}"}
            ]})
            _write_json(base / f"{p}StoryTheaterMain.json", {"dataList": [{"id": "CHAPTER_100", "desc": "Motto"}]})
            _write_json(base / f"{p}ScenarioModelCodes-AutoCreated.json", {"dataList": [
                {"id": "모델A", "name": f"Agent {lang}"}
            ]})
            _write_json(base / f"{p}Characters.json", {"dataList": [{"id": 1, "name": "Hero"}]})
            _write_json(base / f"{p}Personalities.json", {"dataList": [
                {"id": 10101, "title": f"Synth {lang}", "name": "Hero", "desc": "Bio"}
            ]})
            _write_json(base / f"{p}AttributeText.json", {"dataList": [{"id": "CRIMSON", "name": "Wrath"}]})
            _write_json(base / f"{p}SkillTag.json", {"dataList": [
                {"id": "OnSucceedAttackHead", "name": "[Heads Hit]"}
            ]})
            _write_json(base / f"{p}Bufs.json", {"dataList": [{"id": "Sinking", "name": "Sinking"}]})
            _write_json(base / f"{p}Skills.json", {"dataList": [
                {"id": 1010101, "levelList": [
                    {"level": 1, "name": "Deflect" if lang == "en" else "쳐내기", "desc": "",
                     "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttackHead] Inflict 1 [Sinking]"}]}]},
                    {"level": 2, "name": "Deflect" if lang == "en" else "쳐내기", "desc": "",
                     "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttackHead] Inflict 2 [Sinking]"}]}]},
                    {"level": 4, "name": "Deflect" if lang == "en" else "쳐내기", "desc": "",
                     "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttackHead] Inflict 2 [Sinking]"}]}]},
                ]}
            ]})
            _write_json(base / "RPGSystem" / f"{p}RPGDialog.json", {"dataList": [
                {"key": "d1", "texts": [{"speaker": f"Keeper {lang}", "text": f"Welcome {lang}"}]},
                {"key": "d2", "texts": [{"speaker": f"Keeper {lang}", "text": f"Farewell {lang}"}]},
            ]})
            _write_json(base / f"{p}AbDlg_Hero.json", {"dataList": [
                {"id": 1, "teller": f"HeroTeller {lang}", "dlg": f"Check pass {lang}", "usage": "(8001, VERY_HIGH)"},
            ]})
            _write_json(base / "BgmLyrics" / f"{p}BgmLyrics_1.json", {"dataList": [
                {"id": 0, "content": '<style="DEN_1">Synthetic lyric</style>' if lang == "en" else '<style="DKR_1">합성 가사</style>'}
            ]})

        # Also add a KR-only file to verify KR-only translation emission
        _write_json(snap / "kr" / "KR_ExtraKrOnly.json", {"dataList": [
            {"id": "k1", "content": "전용 텍스트"}
        ]})

        self.static = StaticData(sd)
        with Snapshot.open(snap) as s:
            idx = story_index.build(self.static, s)
        self.story_index_path = self.root / "indeks_fabuly.json"
        _write_json(self.story_index_path, idx)

        self.manifest_path = self.root / "MANIFEST.json"
        _write_json(self.manifest_path, {
            "localize": {
                "buildid": "999001",
                "languages": {
                    "kr": {"sha256": "aaa111"},
                    "en": {"sha256": "bbb222"},
                },
            }
        })

        pkg_dir = self.root / "pakiet"
        with contextlib.redirect_stdout(io.StringIO()):
            build_package.main([
                str(snap),
                "--index", str(self.story_index_path),
                "--static-data", str(sd),
                "--out", str(pkg_dir),
            ])
        self.pkg_zip = pkg_dir / "plik_dla_tlumacza_v1.zip"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _extract_pkg(self) -> tuple[dict[str, str], dict[str, str]]:
        with zipfile.ZipFile(self.pkg_zip) as outer:
            sceny_bytes = outer.read("sceny.zip")
            widoki_bytes = outer.read("widoki.zip")
        with zipfile.ZipFile(io.BytesIO(sceny_bytes)) as sz:
            sceny = {n: sz.read(n).decode("utf-8") for n in sz.namelist()}
        with zipfile.ZipFile(io.BytesIO(widoki_bytes)) as wz:
            widoki = {n: wz.read(n).decode("utf-8") for n in wz.namelist()}
        return sceny, widoki

    def test_end_to_end_import_and_build_lang(self) -> None:
        sceny, widoki = self._extract_pkg()
        return_dir = self.root / "zwrotka"
        return_dir.mkdir()

        # Fill story scenes (including Dante <I ...> in Polish, <ruby=...>, newline ' / ', and cross-scene repeat)
        prologue_name = next(n for n in sceny if n.startswith("01_"))
        filled_prologue = _fill_pl_lines(sceny[prologue_name], {
            "<i>Hello</i> {0} en": "<i>Witaj</i> {0} przybyszu",
            "<I think therefore I am>": "<I wtedy pomyślałem, że istnieję>",
            "<ruby=Alpha Reading>Base</ruby>": "<ruby=Polski Odczyt>Baza</ruby>",
            "Line one / Line two": "Pierwsza linia / Druga linia",
            "Second scene unique en": "Unikalna kwestia drugiej sceny",
        })
        (return_dir / prologue_name).write_text(filled_prologue, encoding="utf-8")

        # Fill story glossary (teller, title, place)
        filled_story_gl = _fill_pl_lines(sceny["mowcy-i-miejsca.md"], {
            "Scout en": "Zwiadowca",
            "Rank en": "Stopień",
            "Forest en": "Las Mroku",
        })
        (return_dir / "mowcy-i-miejsca.md").write_text(filled_story_gl, encoding="utf-8")

        # Fill view glossary (rpg_speaker, abdlg_teller + ScenarioModelCodes)
        filled_view_gl = _fill_pl_lines(widoki["mowcy-rpg-i-anomalii.md"], {
            "Keeper en": "Strażnik",
            "HeroTeller en": "Opowiadacz",
            "Agent en": "Agent Modelu",
        })
        (return_dir / "mowcy-rpg-i-anomalii.md").write_text(filled_view_gl, encoding="utf-8")

        # Fill UI + Skill (merged Uptie 1/2/4!) + BgmLyrics + KR-only item
        for name, md in widoki.items():
            if name in ("spis-widokow.md", "mowcy-rpg-i-anomalii.md"):
                continue
            updated = _fill_pl_lines(md, {
                "Clear all caches": "Wyczyść pamięć podręczną",
                "Confirm": "Potwierdź",
                "Deflect": "Odbicie",
                "[OnSucceedAttackHead] Inflict 2 [Sinking]": "[OnSucceedAttackHead] Nakłada 2 [Sinking]",
                '<style="DEN_1">Synthetic lyric</style>': '<style="DEN_1">Polski wers piosenki</style>',
                "(brak wersji angielskiej)": "Tylko w KR po polsku",
            })
            if "PL: " in updated:
                (return_dir / name).write_text(updated, encoding="utf-8")

        tlum_dir = self.root / "tlumaczenie"
        report = import_zwrotki.import_returns(
            inputs=[return_dir],
            localize_path=self.snap,
            story_index_path=self.story_index_path,
            index_manifest_path=self.manifest_path,
            tlumaczenie_dir=tlum_dir,
        )
        self.assertEqual(report.errors, [])
        self.assertGreater(report.translated_items, 0)
        self.assertGreater(report.inherited_repeats, 0)

        out_zip = self.root / "dist" / "LCB_PL_Polski_999001.zip"
        summary = build_lang.build_lang_pack(
            localize_path=self.snap,
            index_manifest_path=self.manifest_path,
            tlumaczenie_dir=tlum_dir,
            lang_name="Polski",
            out_zip=out_zip,
        )
        self.assertEqual(summary.lang_name, "Polski")
        self.assertEqual(summary.steam_buildid, "999001")
        self.assertTrue(out_zip.is_file())

        # Deterministic rebuild check
        out_zip_2 = self.root / "dist" / "LCB_PL_Polski_999001_b.zip"
        summary_2 = build_lang.build_lang_pack(
            localize_path=self.snap,
            index_manifest_path=self.manifest_path,
            tlumaczenie_dir=tlum_dir,
            lang_name="Polski",
            out_zip=out_zip_2,
        )
        self.assertEqual(summary.zip_sha256, summary_2.zip_sha256)

        with zipfile.ZipFile(out_zip) as zf:
            cfg = json.loads(zf.read("LimbusCompany_Data/Lang/config.json").decode("utf-8"))
            self.assertEqual(
                cfg,
                {
                    "lang": "Polski",
                    "titleFont": "",
                    "contextFont": "",
                    "samplingPointSize": 78,
                    "padding": 5,
                },
            )

            # Story S001B checks: content, Dante <I ...>, ruby, newline, glossary teller/title/place
            s1 = load_json(zf.read("LimbusCompany_Data/Lang/Polski/StoryData/S001B.json"))
            rows1 = {r["id"]: r for r in s1["dataList"]}
            self.assertEqual(rows1[0]["content"], "<i>Witaj</i> {0} przybyszu")
            self.assertEqual(rows1[0]["teller"], "Zwiadowca")
            self.assertEqual(rows1[0]["title"], "Stopień")
            self.assertEqual(rows1[0]["place"], "Las Mroku")
            self.assertEqual(rows1[1]["content"], "<I wtedy pomyślałem, że istnieję>")
            self.assertEqual(rows1[2]["content"], "<ruby=Polski Odczyt>Baza</ruby>")
            self.assertEqual(rows1[3]["content"], "Pierwsza linia\nDruga linia")

            # Story S002B inherited repeat from S001B!
            s2 = load_json(zf.read("LimbusCompany_Data/Lang/Polski/StoryData/S002B.json"))
            rows2 = {r["id"]: r for r in s2["dataList"]}
            self.assertEqual(rows2[0]["content"], "<i>Witaj</i> {0} przybyszu")
            self.assertEqual(rows2[0]["teller"], "Zwiadowca")

            # UI file-local repeat inheritance (dup_btn_a -> dup_btn_b) + English fallback on untranslated
            mui = load_json(zf.read("LimbusCompany_Data/Lang/Polski/MainUIText.json"))
            mui_by_id = {r["id"]: r["content"] for r in mui["dataList"]}
            self.assertEqual(mui_by_id["dup_btn_a"], "Potwierdź")
            self.assertEqual(mui_by_id["dup_btn_b"], "Potwierdź")
            self.assertEqual(mui_by_id["mainui_main_button1"], "Sinners")

            # Merged Uptie levels 1/2/4 all received "Odbicie", and levels 2 & 4 received coin desc
            skills = load_json(zf.read("LimbusCompany_Data/Lang/Polski/Skills.json"))
            lvls = {lv["level"]: lv for lv in skills["dataList"][0]["levelList"]}
            for lv_no in (1, 2, 4):
                self.assertEqual(lvls[lv_no]["name"], "Odbicie")
            self.assertEqual(
                lvls[2]["coinlist"][0]["coindescs"][0]["desc"],
                "[OnSucceedAttackHead] Nakłada 2 [Sinking]",
            )
            self.assertEqual(
                lvls[4]["coinlist"][0]["coindescs"][0]["desc"],
                "[OnSucceedAttackHead] Nakłada 2 [Sinking]",
            )

            # RPG speaker and AbDlg teller glossaries applied across rows
            rpg = load_json(zf.read("LimbusCompany_Data/Lang/Polski/RPGSystem/RPGDialog.json"))
            self.assertTrue(all(r["texts"][0]["speaker"] == "Strażnik" for r in rpg["dataList"]))
            abdlg = load_json(zf.read("LimbusCompany_Data/Lang/Polski/AbDlg_Hero.json"))
            self.assertEqual(abdlg["dataList"][0]["teller"], "Opowiadacz")

            # Translated KR-only file included cleanly
            kr_only = load_json(zf.read("LimbusCompany_Data/Lang/Polski/ExtraKrOnly.json"))
            self.assertEqual(kr_only["dataList"][0]["content"], "Tylko w KR po polsku")

    def test_gate_rejects_broken_tokens_and_preserves_existing_store(self) -> None:
        sceny, widoki = self._extract_pkg()
        tlum_dir = self.root / "tlumaczenie"

        # First valid import
        good_md = self.root / "good.md"
        prologue_name = next(n for n in sceny if n.startswith("01_"))
        good_md.write_text(
            _fill_pl_lines(sceny[prologue_name], {"<i>Hello</i> {0} en": "<i>Cześć</i> {0}"}),
            encoding="utf-8",
        )
        rep_ok = import_zwrotki.import_returns(
            inputs=[good_md],
            localize_path=self.snap,
            story_index_path=self.story_index_path,
            index_manifest_path=self.manifest_path,
            tlumaczenie_dir=tlum_dir,
        )
        self.assertEqual(rep_ok.errors, [])
        before_s1 = (tlum_dir / "pliki" / "StoryData" / "S001B.json").read_text(encoding="utf-8")

        # Now try importing a broken batch: missing {0}, unbalanced <i>, translated [Sinking], and DKR in lyrics
        bad_dir = self.root / "bad_zwrotka"
        bad_dir.mkdir()
        (bad_dir / prologue_name).write_text(
            _fill_pl_lines(sceny[prologue_name], {"<i>Hello</i> {0} en": "<i>Brak zmiennej i zamknięcia"}),
            encoding="utf-8",
        )
        for name, md in widoki.items():
            if name == "spis-widokow.md":
                continue
            broken = _fill_pl_lines(md, {
                "[OnSucceedAttackHead] Inflict 2 [Sinking]": "[OnSucceedAttackHead] Nakłada 2 [Tonięcie]",
                '<style="DEN_1">Synthetic lyric</style>': '<style="DKR_1">Zły styl czcionki</style>',
            })
            if "PL: " in broken:
                (bad_dir / name).write_text(broken, encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            exit_code = import_zwrotki.main([
                str(bad_dir),
                "--localize", str(self.snap),
                "--story-index", str(self.story_index_path),
                "--index-manifest", str(self.manifest_path),
                "--out", str(tlum_dir),
            ])
        self.assertEqual(exit_code, 2)
        # Verify atomic rollback: existing tlumaczenie/ file is byte-for-byte untouched
        after_s1 = (tlum_dir / "pliki" / "StoryData" / "S001B.json").read_text(encoding="utf-8")
        self.assertEqual(before_s1, after_s1)

    def test_probe_pack_injects_polish_diacritics_without_touching_tlumaczenie(self) -> None:
        tlum_dir = self.root / "empty_tlumaczenie"
        probe_zip = self.root / "dist" / "LCB_TEST_DROGI_Polski_999001.zip"
        summary = build_lang.build_lang_pack(
            localize_path=self.snap,
            index_manifest_path=self.manifest_path,
            tlumaczenie_dir=tlum_dir,
            lang_name="Polski",
            out_zip=probe_zip,
            probe=True,
        )
        self.assertFalse(tlum_dir.exists())
        self.assertTrue(summary.probe)
        self.assertEqual(summary.translated_leaves, 0)
        self.assertEqual(summary.probe_leaves_applied, 10)

        with zipfile.ZipFile(probe_zip) as zf:
            cfg = json.loads(zf.read("LimbusCompany_Data/Lang/config.json").decode("utf-8"))
            self.assertEqual(
                cfg,
                {
                    "lang": "Polski",
                    "titleFont": "",
                    "contextFont": "",
                    "samplingPointSize": 78,
                    "padding": 5,
                },
            )

            login = load_json(zf.read("LimbusCompany_Data/Lang/Polski/LoginUIText.json"))
            login_map = {r["id"]: r["content"] for r in login["dataList"]}
            self.assertIn("ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ", login_map["switch_allcacheclear"])
            self.assertTrue(login_map["switch_allcacheclear"].startswith("Clear all caches"))

            # Structural address parity check across every generated JSON in Lang/Polski/
            with Snapshot.open(self.snap) as s:
                for logical in s.files["en"]:
                    src_addrs = {a for a, _ in iter_strings(load_json(s.read("en", logical)))}
                    out_addrs = {
                        a for a, _ in iter_strings(
                            load_json(zf.read(f"LimbusCompany_Data/Lang/Polski/{logical}"))
                        )
                    }
                    self.assertEqual(src_addrs, out_addrs, logical)

    def test_font_slots_filter_non_fonts_and_enforce_required_directories(self) -> None:
        fonts_dir = self.root / "fonts"
        (fonts_dir / "Title").mkdir(parents=True)
        (fonts_dir / "Context").mkdir(parents=True)
        (fonts_dir / "Title" / "SyntheticTitle.otf").write_bytes(b"SYNTH_TITLE")
        (fonts_dir / "Title" / "00_notes.txt").write_text("must not enter Font/Title\n", encoding="utf-8")
        (fonts_dir / "Context" / "SyntheticContext.ttf").write_bytes(b"SYNTH_CONTEXT")
        (fonts_dir / "Context" / "README.md").write_text("must not enter Font/Context\n", encoding="utf-8")
        (fonts_dir / "OFL-LICENSE.txt").write_text("Synthetic OFL\n", encoding="utf-8")

        out_zip = self.root / "dist" / "LCB_PL_Polski_fonts.zip"
        build_lang.build_lang_pack(
            localize_path=self.snap,
            index_manifest_path=self.manifest_path,
            tlumaczenie_dir=self.root / "empty_tlum",
            fonts_dir=fonts_dir,
            lang_name="Polski",
            out_zip=out_zip,
        )
        with zipfile.ZipFile(out_zip) as zf:
            names = set(zf.namelist())
            cfg = json.loads(zf.read("LimbusCompany_Data/Lang/config.json").decode("utf-8"))
            self.assertEqual(
                cfg,
                {
                    "lang": "Polski",
                    "titleFont": "",
                    "contextFont": "",
                    "samplingPointSize": 78,
                    "padding": 5,
                },
            )
            self.assertEqual(
                zf.read("LimbusCompany_Data/Lang/Polski/Font/Title/SyntheticTitle.otf"),
                b"SYNTH_TITLE",
            )
            self.assertEqual(
                zf.read("LimbusCompany_Data/Lang/Polski/Font/Context/SyntheticContext.ttf"),
                b"SYNTH_CONTEXT",
            )
            self.assertNotIn("LimbusCompany_Data/Lang/Polski/Font/Title/00_notes.txt", names)
            self.assertNotIn("LimbusCompany_Data/Lang/Polski/Font/Context/README.md", names)
            self.assertIn("LICENCJE_CZCIONEK/OFL-LICENSE.txt", names)
            self.assertNotIn("LimbusCompany_Data/Lang/Polski/Font/OFL-LICENSE.txt", names)
            manifest = json.loads(zf.read("MANIFEST.json").decode("utf-8"))
            self.assertFalse(manifest["fonts"]["uses_default_game_font"])
            self.assertEqual(manifest["fonts"]["bundled_title_font"], "Font/Title/SyntheticTitle.otf")
            self.assertEqual(manifest["fonts"]["bundled_context_font"], "Font/Context/SyntheticContext.ttf")

        # Missing Font/Title or Font/Context must fail fast unless require_fonts=False
        empty_fonts = self.root / "empty_fonts"
        empty_fonts.mkdir()
        with self.assertRaises(ValueError):
            build_lang.build_lang_pack(
                localize_path=self.snap,
                index_manifest_path=self.manifest_path,
                tlumaczenie_dir=self.root / "empty_tlum",
                fonts_dir=empty_fonts,
                lang_name="Polski",
                out_zip=self.root / "dist" / "should_fail.zip",
            )

    def test_repository_ofl_fonts_cover_all_polish_glyphs(self) -> None:
        repo_fonts = build_lang.ROOT / "assets" / "fonts"
        title_fonts = [
            p for p in (repo_fonts / "Title").iterdir()
            if p.is_file() and p.suffix.lower() in {".ttf", ".otf"}
        ]
        context_fonts = [
            p for p in (repo_fonts / "Context").iterdir()
            if p.is_file() and p.suffix.lower() in {".ttf", ".otf"}
        ]
        self.assertGreaterEqual(len(title_fonts), 1)
        self.assertGreaterEqual(len(context_fonts), 1)
        self.assertTrue((repo_fonts / "OFL-Mikodacs.txt").is_file())
        self.assertTrue((repo_fonts / "OFL-Pretendard.txt").is_file())

        required = set("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ„”«»–—…•")
        for font_path in title_fonts + context_fonts:
            data = font_path.read_bytes()
            _, num_tables = struct.unpack_from(">4sH", data, 0)
            tables = {
                struct.unpack_from(">4sIII", data, 12 + i * 16)[0].decode("latin1"): struct.unpack_from(
                    ">4sIII", data, 12 + i * 16
                )[2]
                for i in range(num_tables)
            }
            cmap_off = tables["cmap"]
            _, num_sub = struct.unpack_from(">HH", data, cmap_off)
            cps: set[int] = set()
            for i in range(num_sub):
                _, _, sub_off = struct.unpack_from(">HHI", data, cmap_off + 4 + i * 8)
                p = cmap_off + sub_off
                fmt = struct.unpack_from(">H", data, p)[0]
                if fmt == 4:
                    seg_count = struct.unpack_from(">H", data, p + 6)[0] // 2
                    end_count = struct.unpack_from(f">{seg_count}H", data, p + 14)
                    start_count = struct.unpack_from(f">{seg_count}H", data, p + 16 + seg_count * 2)
                    id_delta = struct.unpack_from(f">{seg_count}h", data, p + 16 + seg_count * 4)
                    iro_pos = p + 16 + seg_count * 6
                    iro = struct.unpack_from(f">{seg_count}H", data, iro_pos)
                    for s in range(seg_count):
                        if start_count[s] == 0xFFFF:
                            continue
                        for c in range(start_count[s], end_count[s] + 1):
                            if iro[s] == 0:
                                gid = (c + id_delta[s]) & 0xFFFF
                            else:
                                roff = iro_pos + s * 2 + iro[s] + (c - start_count[s]) * 2
                                gid = struct.unpack_from(">H", data, roff)[0]
                                if gid != 0:
                                    gid = (gid + id_delta[s]) & 0xFFFF
                            if gid != 0:
                                cps.add(c)
                elif fmt == 12:
                    n_groups = struct.unpack_from(">I", data, p + 12)[0]
                    for g in range(n_groups):
                        sc, ec, sg = struct.unpack_from(">III", data, p + 16 + g * 12)
                        if sg != 0:
                            cps.update(range(sc, ec + 1))
            missing = sorted(ch for ch in required if ord(ch) not in cps)
            self.assertEqual(missing, [], f"{font_path.name} missing Polish glyphs: {missing}")


if __name__ == "__main__":
    unittest.main()
