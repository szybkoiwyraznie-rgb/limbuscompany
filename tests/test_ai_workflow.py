"""Synthetic end-to-end tests for D-11 provisional AI workflow (``origin: ai``).

Tests cover:
1. ``import_zwrotki --ai`` provenance tagging, human-priority protection, and
   clean human overwrite of AI entries.
2. ``build_lang`` inclusion of AI entries by default vs exclusion under ``--no-ai``,
   plus ``human_leaves`` / ``ai_leaves`` accounting.
3. ``build_package --wypelnij-pl`` (skips AI entries for human Translator) vs
   ``--tylko-ai`` (AI verification pack), and ``audit_update`` incremental package
   exclusion of AI prefill.
4. ``prepare_ai_batches`` scope filtering (UI/meta included; voices, lyrics,
   dialogues, Observation Logs, Dante Note details, Sinner bios, and dev-KR excluded)
   and round-trip batch render -> fill -> ``import_zwrotki --ai``.
"""

from __future__ import annotations

import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from tools import (
    audit_update,
    build_lang,
    build_package,
    import_zwrotki,
    prepare_ai_batches,
    story_index,
)
from tools.localize import load_json


def _write_json(path: Path, doc: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _fill_pl_by_en(md_text: str, mapping: dict[str, str]) -> str:
    out: list[str] = []
    last_en = ""
    for line in md_text.splitlines():
        if line.startswith("   EN:"):
            last_en = line[len("   EN:") :].strip()
        if line.strip() == "PL:" and line.startswith("   PL:") and last_en in mapping:
            out.append(f"   PL: {mapping[last_en]}")
        else:
            out.append(line)
    return "\n".join(out) + "\n"


class AiWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

        self.fonts = self.root / "fonts"
        (self.fonts / "Title").mkdir(parents=True)
        (self.fonts / "Context").mkdir(parents=True)
        (self.fonts / "Title" / "SyntheticTitle.otf").write_bytes(b"OTTO-SYNTH")
        (self.fonts / "Context" / "SyntheticContext.ttf").write_bytes(b"\x00\x01\x00\x00SYNTH")
        (self.fonts / "OFL_LICENSE.txt").write_text("SIL OFL 1.1 test\n", encoding="utf-8")

        sd = self.root / "static-data"
        self.sd = sd
        _write_json(
            sd / "storytheater-main" / "main.json",
            {
                "list": [
                    {
                        "chapterId": 1,
                        "subChapterId": 100,
                        "storyList": [
                            {"id": 1, "storyId": "S001B", "nodeId": 10001, "stageDetail": "Before"}
                        ],
                    }
                ]
            },
        )
        for sub in ("skill", "personality", "personality-passive", "passive"):
            _write_json(sd / sub / "empty.json", {"list": []})

        self.snap = self.root / "localize"
        self._populate_localize(self.snap)

        self.index_manifest = self.root / "MANIFEST.json"
        _write_json(
            self.index_manifest,
            {
                "steam_buildid": "990001",
                "zrodlo_localize": "synthetic-test",
                "localize": {"kr_sha256": "aa" * 32, "en_sha256": "bb" * 32},
            },
        )
        from tools.localize import Snapshot
        from tools.static_data import StaticData

        self.story_idx = self.root / "indeks_fabuly.json"
        with Snapshot.open(self.snap) as s:
            idx_payload = story_index.build(StaticData(self.sd), s)
        _write_json(self.story_idx, idx_payload)
        self.tlum_dir = self.root / "tlumaczenie"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _populate_localize(self, snap: Path, extra_ui_row: bool = False) -> None:
        for lang in ("kr", "en"):
            p = f"{lang.upper()}_"
            base = snap / lang
            _write_json(
                base / "StoryData" / f"{p}S001B.json",
                {
                    "dataList": [
                        {
                            "id": 1,
                            "model": "모델A",
                            "teller": "가이드" if lang == "kr" else "Guide",
                            "title": "안내역" if lang == "kr" else "Mentor",
                            "content": "길 안내 문장" if lang == "kr" else "Story path line",
                        }
                    ]
                },
            )
            ui_rows = [
                {"id": "btn_confirm", "content": "확인" if lang == "kr" else "Confirm"},
                {"id": "btn_cancel", "content": "취소" if lang == "kr" else "Cancel"},
            ]
            if extra_ui_row:
                ui_rows.append({"id": "btn_apply", "content": "적용" if lang == "kr" else "Apply"})
            _write_json(base / f"{p}MainUIText.json", {"dataList": ui_rows})
            _write_json(
                base / f"{p}kr_settings-ui-donttranslate.json",
                {"dataList": [{"id": "opt_audio", "content": "오디오" if lang == "kr" else "Audio"}]},
            )
            _write_json(
                base / f"{p}SkillTag.json",
                {"dataList": [{"id": "OnSucceedAttack", "name": "[적중시]" if lang == "kr" else "[On Hit]"}]},
            )
            _write_json(
                base / f"{p}LimtochessUI.json",
                {
                    "dataList": [
                        {"id": "dev_untranslated", "content": "임시 프로토타입"},
                        {"id": "ready_label", "content": "준비" if lang == "kr" else "Ready"},
                    ]
                },
            )
            _write_json(
                base / f"{p}IntroduceCharacter.json",
                {
                    "dataList": [
                        {
                            "id": "이상",
                            "name": "이상" if lang == "kr" else "Yi Sang",
                            "description": "긴 문학 소개글" if lang == "kr" else "Long literary bio",
                        }
                    ]
                },
            )
            # Excluded narrative / voice / lyric files
            _write_json(
                base / "PersonalityVoiceDlg" / f"{p}Voice_10101.json",
                {"dataList": [{"id": "v1", "dlg": "음성 대사" if lang == "kr" else "Voice line"}]},
            )
            _write_json(
                base / "EGOVoiceDig" / f"{p}Voice_EGO_YiSang_1.json",
                {"dataList": [{"id": "ev1", "dlg": "에고 대사" if lang == "kr" else "EGO voice line"}]},
            )
            _write_json(
                base / "BgmLyrics" / f"{p}Lyrics_Boss.json",
                {"dataList": [{"id": 1, "content": "노래 가사" if lang == "kr" else "Song lyric"}]},
            )
            _write_json(
                base / f"{p}AbEvents.json",
                {"dataList": [{"id": 10, "eventDesc": "이벤트 서술" if lang == "kr" else "Event prose"}]},
            )
            _write_json(
                base / "RPGSystem" / f"{p}rpg-loc-ui.json",
                {"dataList": [{"id": "rpg_inv", "text": "가방" if lang == "kr" else "Inventory"}]},
            )
            _write_json(
                base / "RPGSystem" / f"{p}rpg-loc-dialogue.json",
                {
                    "dataList": [
                        {
                            "id": "dlg_1",
                            "speaker": "주민" if lang == "kr" else "Villager",
                            "text": "마을 대화" if lang == "kr" else "Town dialogue",
                        }
                    ]
                },
            )

    def test_scope_filtering_and_ai_priority_pipeline(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            self._run_pipeline_assertions()

    def _run_pipeline_assertions(self) -> None:
        # 1. Verify prepare_ai_batches scope rules & manifest writing
        manifest_path = self.root / "paczki_ai" / "MANIFEST.json"
        render_dir = self.root / "rendered_ai"
        rc = prepare_ai_batches.main(
            [
                "--localize",
                str(self.snap),
                "--static-data",
                str(self.sd),
                "--story-index",
                str(self.story_idx),
                "--index-manifest",
                str(self.index_manifest),
                "--tlumaczenie",
                str(self.tlum_dir),
                "--manifest-out",
                str(manifest_path),
                "--write-manifest",
                "--render-all",
                "--out",
                str(render_dir),
            ]
        )
        self.assertEqual(rc, 0)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        included_files = {lf for b in manifest["batches"] for lf in b["logical_files"]}

        self.assertIn("MainUIText.json", included_files)
        self.assertIn("kr_settings-ui-donttranslate.json", included_files)
        self.assertIn("SkillTag.json", included_files)
        self.assertIn("RPGSystem/rpg-loc-ui.json", included_files)
        self.assertIn("IntroduceCharacter.json", included_files)  # .name in scope, .description excluded

        self.assertNotIn("PersonalityVoiceDlg/Voice_10101.json", included_files)
        self.assertNotIn("EGOVoiceDig/Voice_EGO_YiSang_1.json", included_files)
        self.assertNotIn("BgmLyrics/Lyrics_Boss.json", included_files)
        self.assertNotIn("AbEvents.json", included_files)
        self.assertNotIn("RPGSystem/rpg-loc-dialogue.json", included_files)

        all_rendered_txt = "\n".join(
            p.read_text(encoding="utf-8") for p in sorted(render_dir.glob("*.md"))
        )
        self.assertNotIn("Long literary bio", all_rendered_txt)
        self.assertNotIn("임시 프로토타입", all_rendered_txt)
        self.assertIn("EN: Confirm", all_rendered_txt)
        self.assertIn("EN: Audio", all_rendered_txt)
        self.assertIn("EN: Inventory", all_rendered_txt)

        # 2. First import a HUMAN translation for "Confirm" ("Potwierdź (Tłumacz)")
        pkg_dir = self.root / "pkg_base"
        build_package.main(
            [
                str(self.snap),
                "--index",
                str(self.story_idx),
                "--static-data",
                str(self.sd),
                "--version",
                "1",
                "--out",
                str(pkg_dir),
            ]
        )
        with zipfile.ZipFile(pkg_dir / "plik_dla_tlumacza_v1.zip") as zf:
            with zipfile.ZipFile(zf.open("widoki.zip")) as wzf:
                ui_md_name = next(n for n in wzf.namelist() if "interfejs" in n)
                ui_md = wzf.read(ui_md_name).decode("utf-8")

        human_md = self.root / "human_return.md"
        human_md.write_text(
            _fill_pl_by_en(ui_md, {"Confirm": "Potwierdź (Tłumacz)"}),
            encoding="utf-8",
        )
        rep_human = import_zwrotki.import_returns(
            inputs=[human_md],
            localize_path=self.snap,
            story_index_path=self.story_idx,
            index_manifest_path=self.index_manifest,
            tlumaczenie_dir=self.tlum_dir,
        )
        self.assertEqual(rep_human.errors, [])
        self.assertEqual(rep_human.addresses_updated, 1)

        # 3. Import AI translations attempting to overwrite "Confirm" + translating "Cancel" & "Audio"
        ai_dir = self.root / "zwrotki_ai"
        ai_dir.mkdir()
        for p in sorted(render_dir.glob("*.md")):
            filled = _fill_pl_by_en(
                p.read_text(encoding="utf-8"),
                {
                    "Confirm": "Zatwierdź (AI — nie wolno nadpisać!)",
                    "Cancel": "Anuluj (AI)",
                    "Audio": "Dźwięk (AI)",
                    "[On Hit]": "[Przy Trafieniu]",
                },
            )
            (ai_dir / p.name).write_text(filled, encoding="utf-8")

        rep_ai = import_zwrotki.import_returns(
            inputs=[ai_dir],
            localize_path=self.snap,
            story_index_path=self.story_idx,
            index_manifest_path=self.index_manifest,
            tlumaczenie_dir=self.tlum_dir,
            origin=import_zwrotki.ORIGIN_AI,
        )
        self.assertEqual(rep_ai.errors, [])
        self.assertEqual(rep_ai.skipped_human_existing, 1)

        store = import_zwrotki.TranslationStore.load(self.tlum_dir)
        confirm_entry = store.get_leaf("MainUIText.json", "dataList[id=btn_confirm].content")
        cancel_entry = store.get_leaf("MainUIText.json", "dataList[id=btn_cancel].content")
        self.assertEqual(confirm_entry["pl"], "Potwierdź (Tłumacz)")
        self.assertNotIn("origin", confirm_entry)
        self.assertEqual(cancel_entry["pl"], "Anuluj (AI)")
        self.assertEqual(cancel_entry.get("origin"), "ai")

        tlum_manifest = json.loads((self.tlum_dir / "MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(tlum_manifest["human_addresses"], 1)
        self.assertEqual(tlum_manifest["ai_addresses"], 3)

        # 4. build_lang default includes AI; --no-ai excludes AI
        zip_with_ai = self.root / "dist" / "with_ai.zip"
        sum_with_ai = build_lang.build_lang_pack(
            localize_path=self.snap,
            index_manifest_path=self.index_manifest,
            tlumaczenie_dir=self.tlum_dir,
            fonts_dir=self.fonts,
            out_zip=zip_with_ai,
            include_ai=True,
        )
        self.assertEqual(sum_with_ai.human_leaves, 1)
        self.assertEqual(sum_with_ai.ai_leaves, 3)
        self.assertEqual(sum_with_ai.translated_leaves, 4)

        zip_no_ai = self.root / "dist" / "no_ai.zip"
        sum_no_ai = build_lang.build_lang_pack(
            localize_path=self.snap,
            index_manifest_path=self.index_manifest,
            tlumaczenie_dir=self.tlum_dir,
            fonts_dir=self.fonts,
            out_zip=zip_no_ai,
            include_ai=False,
        )
        self.assertEqual(sum_no_ai.human_leaves, 1)
        self.assertEqual(sum_no_ai.ai_leaves, 0)
        self.assertEqual(sum_no_ai.translated_leaves, 1)
        with zipfile.ZipFile(zip_no_ai) as zf:
            doc_no_ai = load_json(zf.read("LimbusCompany_Data/Lang/Polski/MainUIText.json"))
            by_id = {r["id"]: r["content"] for r in doc_no_ai["dataList"]}
            self.assertEqual(by_id["btn_confirm"], "Potwierdź (Tłumacz)")
            self.assertEqual(by_id["btn_cancel"], "Cancel")  # AI skipped -> EN fallback!

        # 5. build_package --wypelnij-pl omits AI entries (leaves Cancel blank for Translator!)
        pkg_pref_dir = self.root / "pkg_prefilled"
        build_package.main(
            [
                str(self.snap),
                "--index",
                str(self.story_idx),
                "--static-data",
                str(self.sd),
                "--tlumaczenie",
                str(self.tlum_dir),
                "--wypelnij-pl",
                "--version",
                "2",
                "--out",
                str(pkg_pref_dir),
            ]
        )
        with zipfile.ZipFile(pkg_pref_dir / "plik_dla_tlumacza_v2.zip") as zf:
            with zipfile.ZipFile(zf.open("widoki.zip")) as wzf:
                pref_ui = wzf.read(ui_md_name).decode("utf-8")
        self.assertIn("   PL: Potwierdź (Tłumacz)", pref_ui)
        self.assertNotIn("Anuluj (AI)", pref_ui)
        self.assertNotIn("Dźwięk (AI)", pref_ui)

        # 6. build_package --tylko-ai includes ONLY AI entries
        pkg_ai_dir = self.root / "pkg_only_ai"
        build_package.main(
            [
                str(self.snap),
                "--index",
                str(self.story_idx),
                "--static-data",
                str(self.sd),
                "--tlumaczenie",
                str(self.tlum_dir),
                "--tylko-ai",
                "--version",
                "1",
                "--out",
                str(pkg_ai_dir),
            ]
        )
        with zipfile.ZipFile(pkg_ai_dir / "paczka_ai_weryfikacja_v1.zip") as zf:
            with zipfile.ZipFile(zf.open("widoki.zip")) as wzf:
                ai_ver_ui = wzf.read(ui_md_name).decode("utf-8")
        self.assertIn("   PL: Anuluj (AI)", ai_ver_ui)
        self.assertNotIn("Potwierdź (Tłumacz)", ai_ver_ui)

        # 7. audit_update incremental package (--delta-scope files) prefills human, skips AI!
        snap_v2 = self.root / "localize_v2"
        self._populate_localize(snap_v2, extra_ui_row=True)
        manifest_v2 = self.root / "MANIFEST_v2.json"
        _write_json(
            manifest_v2,
            {
                "steam_buildid": "990002",
                "zrodlo_localize": "synthetic-test-v2",
                "localize": {"kr_sha256": "cc" * 32, "en_sha256": "dd" * 32},
            },
        )
        inc_dir = self.root / "delta_out"
        audit_update.main(
            [
                "--old",
                str(self.snap),
                "--new",
                str(snap_v2),
                "--tlumaczenie",
                str(self.tlum_dir),
                "--index",
                str(self.story_idx),
                "--static-data",
                str(self.sd),
                "--delta-scope",
                "files",
                "--delta-out",
                str(inc_dir),
                "--delta-zip-name",
                "pakiet_przyrostowy.zip",
            ]
        )
        inc_zip = inc_dir / "pakiet_przyrostowy.zip"
        with zipfile.ZipFile(inc_zip) as zf:
            with zipfile.ZipFile(zf.open("widoki.zip")) as wzf:
                inc_ui_name = next(n for n in wzf.namelist() if "interfejs" in n)
                inc_ui = wzf.read(inc_ui_name).decode("utf-8")
        self.assertIn("   PL: Potwierdź (Tłumacz)", inc_ui)
        self.assertNotIn("Anuluj (AI)", inc_ui)

        # 8. Human Translator later returns "Cancel" -> overwrites AI cleanly and drops origin="ai"
        human_md_2 = self.root / "human_return_2.md"
        human_md_2.write_text(
            _fill_pl_by_en(ui_md, {"Cancel": "Anuluj (Tłumacz)"}),
            encoding="utf-8",
        )
        rep_human_2 = import_zwrotki.import_returns(
            inputs=[human_md_2],
            localize_path=self.snap,
            story_index_path=self.story_idx,
            index_manifest_path=self.index_manifest,
            tlumaczenie_dir=self.tlum_dir,
        )
        self.assertEqual(rep_human_2.errors, [])
        self.assertEqual(rep_human_2.replaced_ai, 1)

        store_after = import_zwrotki.TranslationStore.load(self.tlum_dir)
        cancel_after = store_after.get_leaf("MainUIText.json", "dataList[id=btn_cancel].content")
        self.assertEqual(cancel_after["pl"], "Anuluj (Tłumacz)")
        self.assertNotIn("origin", cancel_after)


if __name__ == "__main__":
    unittest.main()
