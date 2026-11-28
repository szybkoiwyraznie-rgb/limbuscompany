"""Synthetic tests for ``tools/audit_update.py`` (build diff, stale PL detection, delta package).

Every string and number in this file is invented; no game prose is used.
"""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from tools import audit_update, import_zwrotki, story_index
from tools.localize import Snapshot
from tools.static_data import StaticData


def _write_json(path: Path, doc: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class AuditUpdateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

        sd = self.root / "static-data"
        self.sd = sd
        _write_json(sd / "storytheater-main" / "main.json", {"list": [
            {"chapterId": 1, "subChapterId": 100, "storyList": [
                {"id": 1, "storyId": "S001B", "nodeId": 10001, "stageDetail": "Before"},
            ]},
            {"chapterId": 2, "subChapterId": 200, "storyList": [
                {"id": 1, "storyId": "S101B", "nodeId": 20001, "stageDetail": "Before"},
            ]},
        ]})
        for empty_tbl in ("skill", "personality", "personality-passive", "passive"):
            _write_json(sd / empty_tbl / "t.json", {"list": []})

        # Build OLD snapshot (directory with MANIFEST.json in parent)
        old_root = self.root / "old_index"
        self.old_snap = old_root / "localize"
        _write_json(old_root / "MANIFEST.json", {"localize": {"buildid": "100100"}})

        for lang in ("kr", "en"):
            p = f"{lang.upper()}_"
            base = self.old_snap / lang
            _write_json(base / "StoryData" / f"{p}S001B.json", {"dataList": [
                {"id": 0, "teller": "Guide", "content": "Unchanged line kr" if lang == "kr" else "Unchanged line en"},
                {"id": 1, "teller": "Guide", "content": "Old line kr" if lang == "kr" else "Old line en"},
            ]})
            _write_json(base / "StoryData" / f"{p}S101B.json", {"dataList": [
                {"id": 0, "teller": "Scout", "content": "Untouched chapter kr" if lang == "kr" else "Untouched chapter en"},
            ]})
            _write_json(base / f"{p}MainUIText.json", {"dataList": [
                {"id": "btn_keep", "content": "Keep kr" if lang == "kr" else "Keep en"},
                {"id": "btn_edit", "content": "Before kr" if lang == "kr" else "Before en"},
                {"id": "btn_drop", "content": "Drop kr" if lang == "kr" else "Drop en"},
            ]})
            _write_json(base / f"{p}ObsoleteUI.json", {"dataList": [
                {"id": "obs_1", "content": "Gone kr" if lang == "kr" else "Gone en"},
            ]})
            _write_json(base / f"{p}StageChapterText.json", {"dataList": [
                {"id": "chapter_a_100", "chapter": "Ch1", "chaptertitle": "First"},
                {"id": "chapter_b_200", "chapter": "Ch2", "chaptertitle": "Second"},
            ]})
            _write_json(base / f"{p}StageNode1-1.json", {"dataList": []})
            _write_json(base / f"{p}StoryTheaterMain.json", {"dataList": []})
            _write_json(base / f"{p}ScenarioModelCodes-AutoCreated.json", {"dataList": []})
            _write_json(base / f"{p}Characters.json", {"dataList": []})

        with Snapshot.open(self.old_snap) as s:
            idx = story_index.build(StaticData(sd), s)
        self.story_index_path = self.root / "indeks_fabuly.json"
        _write_json(self.story_index_path, idx)

        # Seed existing Polish translations in tlumaczenie/ for build 100100
        self.tlum_dir = self.root / "tlumaczenie"
        _write_json(self.tlum_dir / "MANIFEST.json", {"steam_buildid": "100100"})
        _write_json(self.tlum_dir / "pliki" / "StoryData" / "S001B.json", {
            "entries": {
                "dataList[id=0].content": {
                    "pl": "Niezmieniona kwestia PL",
                    "kr_sha256": import_zwrotki.sha256_text("Unchanged line kr"),
                },
                "dataList[id=1].content": {
                    "pl": "Stara kwestia PL",
                    "kr_sha256": import_zwrotki.sha256_text("Old line kr"),
                },
            }
        })
        _write_json(self.tlum_dir / "pliki" / "MainUIText.json", {
            "entries": {
                "dataList[id=btn_keep].content": {
                    "pl": "Zachowaj PL",
                    "kr_sha256": import_zwrotki.sha256_text("Keep kr"),
                },
                "dataList[id=btn_edit].content": {
                    "pl": "Stary przycisk PL",
                    "kr_sha256": import_zwrotki.sha256_text("Before kr"),
                },
                "dataList[id=btn_drop].content": {
                    "pl": "Usunięty przycisk PL",
                    "kr_sha256": import_zwrotki.sha256_text("Drop kr"),
                },
            }
        })
        _write_json(self.tlum_dir / "pliki" / "ObsoleteUI.json", {
            "entries": {
                "dataList[id=obs_1].content": {
                    "pl": "Stary plik PL",
                    "kr_sha256": import_zwrotki.sha256_text("Gone kr"),
                },
            }
        })

        # Build NEW snapshot as a collector-style ZIP archive (build 100200)
        self.new_zip = self.root / "LCB_DANE_new.zip"
        new_members: dict[str, object] = {
            "RAPORT.json": {"game": {"steam": {"buildid": "100200"}}},
        }
        for lang in ("kr", "en"):
            p = f"{lang.upper()}_"
            pref = f"Localize/{lang}"
            new_members[f"{pref}/StoryData/{p}S001B.json"] = {"dataList": [
                {"id": 0, "teller": "Guide", "content": "Unchanged line kr" if lang == "kr" else "Unchanged line en"},
                {"id": 1, "teller": "Guide", "content": "Revised line kr" if lang == "kr" else "Revised line en"},
                {"id": 2, "teller": "Guide", "content": "Added line kr" if lang == "kr" else "Added line en"},
            ]}
            new_members[f"{pref}/StoryData/{p}S101B.json"] = {"dataList": [
                {"id": 0, "teller": "Scout", "content": "Untouched chapter kr" if lang == "kr" else "Untouched chapter en"},
            ]}
            # Brand-new unindexed StoryData scene S999B!
            new_members[f"{pref}/StoryData/{p}S999B.json"] = {"dataList": [
                {"id": 0, "teller": "Newcomer", "content": "Brand new scene kr" if lang == "kr" else "Brand new scene en"},
            ]}
            new_members[f"{pref}/{p}MainUIText.json"] = {"dataList": [
                {"id": "btn_keep", "content": "Keep kr" if lang == "kr" else "Keep en"},
                {"id": "btn_edit", "content": "After kr" if lang == "kr" else "After en"},
                {"id": "btn_new", "content": "Added btn kr" if lang == "kr" else "Added btn en"},
            ]}
            new_members[f"{pref}/{p}StageChapterText.json"] = {"dataList": [
                {"id": "chapter_a_100", "chapter": "Ch1", "chaptertitle": "First"},
                {"id": "chapter_b_200", "chapter": "Ch2", "chaptertitle": "Second"},
            ]}
            new_members[f"{pref}/{p}StageNode1-1.json"] = {"dataList": []}
            new_members[f"{pref}/{p}StoryTheaterMain.json"] = {"dataList": []}
            new_members[f"{pref}/{p}ScenarioModelCodes-AutoCreated.json"] = {"dataList": []}
            new_members[f"{pref}/{p}Characters.json"] = {"dataList": []}

        with zipfile.ZipFile(self.new_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for m_name, obj in sorted(new_members.items()):
                zf.writestr(m_name, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_audit_counts_stale_detection_and_delta_roundtrip(self) -> None:
        delta_dir = self.root / "delta"
        report_json = self.root / "audit.json"
        stdout_buf = io.StringIO()
        with contextlib.redirect_stdout(stdout_buf):
            rc = audit_update.main([
                "--old", str(self.old_snap),
                "--new", str(self.new_zip),
                "--tlumaczenie", str(self.tlum_dir),
                "--index", str(self.story_index_path),
                "--static-data", str(self.sd),
                "--out-report", str(report_json),
                "--delta-out", str(delta_dir),
            ])
        self.assertEqual(rc, 0)
        stdout_txt = stdout_buf.getvalue()
        # Ensure stdout and JSON report contain zero invented prose
        for prose in ("Unchanged line", "Revised line", "Untouched chapter", "Brand new scene", "Zachowaj PL"):
            self.assertNotIn(prose, stdout_txt)
            self.assertNotIn(prose, report_json.read_text(encoding="utf-8"))

        rep = json.loads(report_json.read_text(encoding="utf-8"))
        self.assertEqual(rep["old_buildid"], "100100")
        self.assertEqual(rep["new_buildid"], "100200")
        self.assertEqual(rep["kr"]["files"]["added"], 1)      # S999B.json
        self.assertEqual(rep["kr"]["files"]["removed"], 1)    # ObsoleteUI.json
        self.assertEqual(rep["kr"]["files"]["modified"], 2)   # S001B.json, MainUIText.json

        # Translation impact: 2 preserved, 2 stale (S001B id=1 + btn_edit), 2 orphaned (btn_drop + ObsoleteUI)
        self.assertEqual(rep["translations"]["preserved"], 2)
        self.assertEqual(rep["translations"]["stale_kr_changed"], 2)
        self.assertEqual(rep["translations"]["orphaned_removed"], 2)

        delta_zip = delta_dir / "pakiet_uzupelniajacy_100100_do_100200.zip"
        self.assertTrue(delta_zip.is_file())

        with zipfile.ZipFile(delta_zip) as dz:
            sceny_raw = dz.read("sceny.zip")
            widoki_raw = dz.read("widoki.zip")
            self.assertIn("AUDYT_AKTUALIZACJI.md", dz.namelist())

        with zipfile.ZipFile(io.BytesIO(sceny_raw)) as sz:
            sceny_mds = {n: sz.read(n).decode("utf-8") for n in sz.namelist()}
        with zipfile.ZipFile(io.BytesIO(widoki_raw)) as wz:
            widoki_mds = {n: wz.read(n).decode("utf-8") for n in wz.namelist()}

        # Untouched chapter 2 (S101B) must NOT be emitted in delta sceny.zip!
        self.assertFalse(any(n.startswith("02_") for n in sceny_mds))
        # Impacted chapter 1 (S001B) AND unindexed new scene S999B (pozostale.md) MUST be emitted!
        ch1_name = next(n for n in sceny_mds if n.startswith("01_"))
        self.assertIn("pozostale.md", sceny_mds)
        self.assertIn("S999B", sceny_mds["pozostale.md"])

        # In chapter 1, unchanged line 0 is pre-filled with PL, while revised line 1 & added line 2 stay blank!
        self.assertIn("   PL: Niezmieniona kwestia PL", sceny_mds[ch1_name])
        self.assertNotIn("Stara kwestia PL", sceny_mds[ch1_name])

        # In widoki, btn_keep is pre-filled, while stale btn_edit and added btn_new stay blank!
        ui_name = next(n for n in widoki_mds if n.startswith("08_interfejs"))
        self.assertIn("   PL: Zachowaj PL", widoki_mds[ui_name])
        self.assertNotIn("Stary przycisk PL", widoki_mds[ui_name])

        # Round-trip: fill the remaining blank PL lines in delta and import into tlumaczenie against new_zip!
        return_dir = self.root / "delta_zwrotka"
        return_dir.mkdir()
        (return_dir / ch1_name).write_text(
            sceny_mds[ch1_name]
            .replace("   EN: Revised line en\n   PL:", "   EN: Revised line en\n   PL: Poprawiona kwestia PL")
            .replace("   EN: Added line en\n   PL:", "   EN: Added line en\n   PL: Dodana kwestia PL"),
            encoding="utf-8",
        )
        (return_dir / "pozostale.md").write_text(
            sceny_mds["pozostale.md"].replace(
                "   EN: Brand new scene en\n   PL:",
                "   EN: Brand new scene en\n   PL: Nowa scena PL",
            ),
            encoding="utf-8",
        )
        (return_dir / ui_name).write_text(
            widoki_mds[ui_name]
            .replace("   EN: After en\n   PL:", "   EN: After en\n   PL: Po zmianie PL")
            .replace("   EN: Added btn en\n   PL:", "   EN: Added btn en\n   PL: Nowy przycisk PL"),
            encoding="utf-8",
        )
        # Also include AUDYT_AKTUALIZACJI.md to verify import_zwrotki skips it cleanly
        with zipfile.ZipFile(delta_zip) as dz:
            (return_dir / "AUDYT_AKTUALIZACJI.md").write_bytes(dz.read("AUDYT_AKTUALIZACJI.md"))

        new_manifest = self.root / "NEW_MANIFEST.json"
        _write_json(new_manifest, {"localize": {"buildid": "100200"}})
        # Append S999B to story index for import validation
        idx_new = json.loads(self.story_index_path.read_text(encoding="utf-8"))
        idx_new["nieprzypisane"] = list(idx_new.get("nieprzypisane", [])) + ["S999B"]
        idx_new_path = self.root / "indeks_fabuly_new.json"
        _write_json(idx_new_path, idx_new)

        imp_rep = import_zwrotki.import_returns(
            inputs=[return_dir],
            localize_path=self.new_zip,
            story_index_path=idx_new_path,
            index_manifest_path=new_manifest,
            tlumaczenie_dir=self.tlum_dir,
        )
        self.assertEqual(imp_rep.errors, [])
        store_after = import_zwrotki.TranslationStore.load(self.tlum_dir)
        self.assertEqual(store_after.files["StoryData/S001B.json"]["dataList[id=1].content"]["pl"], "Poprawiona kwestia PL")
        self.assertEqual(store_after.files["StoryData/S001B.json"]["dataList[id=2].content"]["pl"], "Dodana kwestia PL")
        self.assertEqual(store_after.files["StoryData/S999B.json"]["dataList[id=0].content"]["pl"], "Nowa scena PL")
        self.assertEqual(store_after.files["MainUIText.json"]["dataList[id=btn_edit].content"]["pl"], "Po zmianie PL")
        self.assertEqual(store_after.files["MainUIText.json"]["dataList[id=btn_new].content"]["pl"], "Nowy przycisk PL")

    def test_incremental_items_scope_excludes_unchanged_items_and_groups_new_identity(self) -> None:
        # Build a patch ZIP adding a brand-new Sinner 01 Identity 10199 (story + card + skill + passive + voice)
        # and modifying one item in MainUIText while leaving btn_keep untouched (with empty tlumaczenie/).
        patch_zip = self.root / "LCB_DANE_patch.zip"
        members: dict[str, object] = {
            "RAPORT.json": {"game": {"steam": {"buildid": "100300"}}},
        }
        for lang in ("kr", "en"):
            p = f"{lang.upper()}_"
            pref = f"Localize/{lang}"
            members[f"{pref}/StoryData/{p}S001B.json"] = {"dataList": [
                {"id": 0, "teller": "Guide", "content": "Unchanged line kr" if lang == "kr" else "Unchanged line en"},
                {"id": 1, "teller": "Guide", "content": "Old line kr" if lang == "kr" else "Old line en"},
            ]}
            members[f"{pref}/StoryData/{p}S101B.json"] = {"dataList": [
                {"id": 0, "teller": "Scout", "content": "Untouched chapter kr" if lang == "kr" else "Untouched chapter en"},
            ]}
            members[f"{pref}/StoryData/{p}P10199.json"] = {"dataList": [
                {"id": 0, "teller": "FreshSpeakerKr" if lang == "kr" else "FreshSpeakerEn",
                 "content": "Identity story kr" if lang == "kr" else "Identity story en"},
            ]}
            members[f"{pref}/{p}MainUIText.json"] = {"dataList": [
                {"id": "btn_keep", "content": "Keep kr" if lang == "kr" else "Keep en"},
                {"id": "btn_edit", "content": "Before kr" if lang == "kr" else "Edited EN only"},
                {"id": "btn_drop", "content": "Drop kr" if lang == "kr" else "Drop en"},
                {"id": "btn_added", "content": "Added kr" if lang == "kr" else "Added en"},
            ]}
            members[f"{pref}/{p}ObsoleteUI.json"] = {"dataList": [
                {"id": "obs_1", "content": "Gone kr" if lang == "kr" else "Gone en"},
            ]}
            members[f"{pref}/{p}Personalities.json"] = {"dataList": [
                {"id": 10199, "title": "Invented Title", "name": "Hero", "desc": "Invented desc"},
            ]}
            members[f"{pref}/{p}Skills_personality-01.json"] = {"dataList": [
                {"id": 1019901, "levelList": [{"level": 1, "name": "Invented Skill", "desc": "Skill desc"}]},
            ]}
            members[f"{pref}/{p}Passives.json"] = {"dataList": [
                {"id": 1019901, "name": "Invented Passive", "desc": "Passive desc"},
            ]}
            members[f"{pref}/PersonalityVoiceDlg/{p}Voice_Hero_10199.json"] = {"dataList": [
                {"id": "v1", "desc": "Cue", "dlg": "Voice line"},
            ]}
            members[f"{pref}/{p}StageChapterText.json"] = {"dataList": [
                {"id": "chapter_a_100", "chapter": "Ch1", "chaptertitle": "First"},
                {"id": "chapter_b_200", "chapter": "Ch2", "chaptertitle": "Second"},
            ]}
            members[f"{pref}/{p}StageNode1-1.json"] = {"dataList": []}
            members[f"{pref}/{p}StoryTheaterMain.json"] = {"dataList": []}
            members[f"{pref}/{p}ScenarioModelCodes-AutoCreated.json"] = {"dataList": []}
            members[f"{pref}/{p}Characters.json"] = {"dataList": [{"id": 1, "name": "Hero"}]}

        with zipfile.ZipFile(patch_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for m_name, obj in sorted(members.items()):
                zf.writestr(m_name, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

        empty_tlum = self.root / "empty_tlum"
        delta_dir = self.root / "delta_items"
        with contextlib.redirect_stdout(io.StringIO()):
            rc = audit_update.main([
                "--old", str(self.old_snap),
                "--new", str(patch_zip),
                "--tlumaczenie", str(empty_tlum),
                "--index", str(self.story_index_path),
                "--static-data", str(self.sd),
                "--delta-out", str(delta_dir),
                "--delta-scope", "items",
            ])
        self.assertEqual(rc, 0)

        inc_zip = delta_dir / "pakiet_przyrostowy_100100_do_100300.zip"
        self.assertTrue(inc_zip.is_file())
        with zipfile.ZipFile(inc_zip) as dz:
            self.assertIn("README.md", dz.namelist())
            sceny_raw = dz.read("sceny.zip")
            widoki_raw = dz.read("widoki.zip")

        with zipfile.ZipFile(io.BytesIO(sceny_raw)) as sz:
            sceny_mds = {n: sz.read(n).decode("utf-8") for n in sz.namelist()}
        with zipfile.ZipFile(io.BytesIO(widoki_raw)) as wz:
            widoki_mds = {n: wz.read(n).decode("utf-8") for n in wz.namelist()}

        # P10199 must be placed in identity-01.md (not pozostale.md), and untouched S001B/S101B omitted!
        self.assertIn("identity-01.md", sceny_mds)
        self.assertNotIn("pozostale.md", sceny_mds)
        self.assertFalse(any(n.startswith("01_") or n.startswith("02_") for n in sceny_mds))
        # Story glossary contains ONLY FreshSpeakerKr, NOT Guide or Scout!
        self.assertIn("FreshSpeakerKr", sceny_mds["mowcy-i-miejsca.md"])
        self.assertNotIn("Guide", sceny_mds["mowcy-i-miejsca.md"])
        self.assertNotIn("Scout", sceny_mds["mowcy-i-miejsca.md"])

        # In widoki, MainUIText has ONLY btn_edit (EN changed) and btn_added (new) — NOT untouched btn_keep/btn_drop!
        ui_md = widoki_mds[next(n for n in widoki_mds if n.startswith("08_interfejs"))]
        self.assertIn("btn_edit", ui_md)
        self.assertIn("btn_added", ui_md)
        self.assertNotIn("btn_keep", ui_md)
        self.assertNotIn("btn_drop", ui_md)

        # Card + skill + passive + voice for 10199 are grouped together in Sinner 01 file, not spilled into 13_wspolne!
        id01_md = widoki_mds[next(n for n in widoki_mds if n.startswith("02_tozsamosc_01"))]
        self.assertIn("Passives.json :: dataList[id=1019901].name", id01_md)
        self.assertFalse(any("13_wspolne" in n for n in widoki_mds))

        # Verify strict import_returns compatibility on the rebuilt story_index + patch_zip!
        with Snapshot.open(patch_zip) as ps:
            idx_100300 = story_index.build(StaticData(self.sd), ps)
        idx_100300_path = self.root / "indeks_100300.json"
        _write_json(idx_100300_path, idx_100300)
        man_100300 = self.root / "MAN_100300.json"
        _write_json(man_100300, {"localize": {"buildid": "100300"}})

        # Also test cross-build --allow-older-package: import incremental translation first, then an older 100100 return!
        zwrotka_inc = self.root / "zwrotka_inc"
        zwrotka_inc.mkdir()
        (zwrotka_inc / "ui.md").write_text(
            ui_md.replace("   EN: Edited EN only\n   PL:", "   EN: Edited EN only\n   PL: Nowy przekład po erracie EN"),
            encoding="utf-8",
        )
        rep_inc = import_zwrotki.import_returns(
            inputs=[inc_zip, zwrotka_inc],
            localize_path=patch_zip,
            story_index_path=idx_100300_path,
            index_manifest_path=man_100300,
            tlumaczenie_dir=empty_tlum,
        )
        self.assertEqual(rep_inc.errors, [])
        self.assertEqual(rep_inc.warnings, [])

        # Older 100100 package file has old EN ("Before en") on btn_edit and valid unchanged btn_keep
        older_ui_md = (
            "# Interfejs\n\n## Interfejs\n\n"
            "1. [Tekst] Keep kr\n"
            "   źródło: MainUIText.json :: dataList[id=btn_keep].content\n"
            "   limit: do 40 znaków\n"
            "   EN: Keep en\n"
            "   PL: Zachowany ze starego pakietu\n"
            "2. [Tekst] Before kr\n"
            "   źródło: MainUIText.json :: dataList[id=btn_edit].content\n"
            "   limit: do 40 znaków\n"
            "   EN: Before en\n"
            "   PL: Starszy przekład przed erratą EN\n"
        )
        older_md_path = self.root / "older_ui.md"
        older_md_path.write_text(older_ui_md, encoding="utf-8")

        # Strict mode rejects the older EN line:
        rep_strict = import_zwrotki.import_returns(
            inputs=[older_md_path],
            localize_path=patch_zip,
            story_index_path=idx_100300_path,
            index_manifest_path=man_100300,
            tlumaczenie_dir=empty_tlum,
        )
        self.assertEqual(len(rep_strict.errors), 1)

        # --allow-older-package accepts btn_keep, warns on btn_edit, and preserves the newer delta translation!
        rep_compat = import_zwrotki.import_returns(
            inputs=[older_md_path],
            localize_path=patch_zip,
            story_index_path=idx_100300_path,
            index_manifest_path=man_100300,
            tlumaczenie_dir=empty_tlum,
            allow_older_package=True,
        )
        self.assertEqual(rep_compat.errors, [])
        self.assertEqual(len(rep_compat.warnings), 1)
        final_store = import_zwrotki.TranslationStore.load(empty_tlum)
        self.assertEqual(
            final_store.files["MainUIText.json"]["dataList[id=btn_keep].content"]["pl"],
            "Zachowany ze starego pakietu",
        )
        self.assertEqual(
            final_store.files["MainUIText.json"]["dataList[id=btn_edit].content"]["pl"],
            "Nowy przekład po erracie EN",
        )


if __name__ == "__main__":
    unittest.main()
