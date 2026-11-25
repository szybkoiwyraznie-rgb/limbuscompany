from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tests.synthetic_localize import write_collector_zip
from tools.validate_collector_return import InvalidReturn, validate


class CollectorReturnTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="lcb-return-")
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)

    def test_valid_synthetic_return_passes_with_aggregate_summary(self):
        path = write_collector_zip(self.dir / "LCB_DANE_test.zip")
        summary = validate(path)
        self.assertEqual(summary["validation"], "passed")
        self.assertEqual(summary["steam_buildid"], "12345678")
        self.assertEqual(summary["files_by_kind"]["lang_config"], 1)
        self.assertEqual(summary["localize_files_by_language"], {"en": 5, "jp": 4, "kr": 4})
        self.assertEqual(summary["inventory_rows"], 2)

    def test_hash_mismatch_is_rejected(self):
        path = write_collector_zip(self.dir / "bad.zip", tamper="sha")
        with self.assertRaisesRegex(InvalidReturn, "sha256"):
            validate(path)

    def test_inventory_count_mismatch_is_rejected(self):
        path = write_collector_zip(self.dir / "bad.zip", tamper="count")
        with self.assertRaisesRegex(InvalidReturn, "inventory count"):
            validate(path)

    def test_undeclared_or_unsafe_members_are_rejected(self):
        for extra in ({"Localize/en/EN_Extra.json": b"{}"}, {"../escape.json": b"{}"}, {"LimbusCompany.exe": b"MZ"}):
            with self.subTest(extra=list(extra)):
                path = write_collector_zip(self.dir / "bad.zip", extra=extra)
                with self.assertRaises(InvalidReturn):
                    validate(path)

    def test_not_a_zip_is_rejected(self):
        path = self.dir / "x.zip"
        path.write_bytes(b"not a zip")
        with self.assertRaises(InvalidReturn):
            validate(path)


if __name__ == "__main__":
    unittest.main()
