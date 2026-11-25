"""tools/import_data.py on made-up files: bytes kept, manifest, replace semantics."""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from tools import import_data


BOM_JSON = b'\xef\xbb\xbf{"dataList": [{"id": 1, "content": "Synthetic"}]}\r\n'


class ImportDataTests(unittest.TestCase):
    def test_directory_and_zip_sources_copy_bytes_exactly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            mirror = root / "mirror"
            (mirror / "kr" / "StoryData").mkdir(parents=True)
            (mirror / "kr" / "StoryData" / "KR_S101B.json").write_bytes(BOM_JSON)
            (mirror / "kr" / "readme.txt").write_text("not json", encoding="utf-8")
            (mirror / "zh").mkdir()
            (mirror / "zh" / "x.json").write_bytes(b"{}")
            out = root / "index"
            result = import_data.import_localize(mirror, ["kr"], out)
            copied = out / "localize" / "kr" / "StoryData" / "KR_S101B.json"
            self.assertEqual(copied.read_bytes(), BOM_JSON)
            self.assertEqual(result["kr"]["pliki"], 1)
            self.assertFalse((out / "localize" / "zh").exists())
            self.assertFalse((out / "localize" / "kr" / "readme.txt").exists())

            archive = root / "LCB_DANE_test.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("Localize/kr/StoryData/KR_S101B.json", BOM_JSON)
                zf.writestr("manifest.json", "{}")
            out2 = root / "index2"
            result2 = import_data.import_localize(archive, ["kr"], out2)
            self.assertEqual(result2["kr"]["sha256"], result["kr"]["sha256"])

    def test_reimport_replaces_language_and_writes_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "src" / "en").mkdir(parents=True)
            (root / "src" / "en" / "EN_A.json").write_bytes(b"{}")
            (root / "src" / "en" / "EN_B.json").write_bytes(b"{}")
            static = root / "static-data" / "personality"
            static.mkdir(parents=True)
            (static / "p.json").write_bytes(b'{"list": []}')
            out = root / "index"
            args = ["--localize", str(root / "src"), "--langs", "en", "--static-data", str(root / "static-data"),
                    "--out", str(out), "--localize-source", "synthetic"]
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(import_data.main(args), 0)
            (root / "src" / "en" / "EN_B.json").unlink()
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(import_data.main(args), 0)
            self.assertEqual(sorted(p.name for p in (out / "localize" / "en").iterdir()), ["EN_A.json"])
            manifest = json.loads((out / "MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["format"], "lcb-index-v1")
            self.assertEqual(manifest["localize"]["zrodlo"], "synthetic")
            self.assertEqual(manifest["static_data"]["tabele"]["personality"]["pliki"], 1)


if __name__ == "__main__":
    unittest.main()
