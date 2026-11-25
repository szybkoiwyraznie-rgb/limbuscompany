"""Walidator zwrotu zbieracza na wymyślonych archiwach."""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tests import syntetyczne as syn
from tools.validate_collector_return import InvalidReturn, validate


class CollectorReturnTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="lc-return-")
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)

    def save(self, data: bytes) -> Path:
        path = self.dir / f"LC_DANE_{len(list(self.dir.iterdir()))}.zip"
        path.write_bytes(data)
        return path

    def test_valid_return_reports_only_aggregates(self):
        result = validate(self.save(syn.zwrot_zbieracza(syn.drzewo_localize())))
        self.assertEqual(result["validation"], "passed")
        self.assertEqual(result["buildid"], "123456")
        self.assertEqual(result["plikow_wg_jezyka"], {"en": 5, "jp": 3, "kr": 4})
        self.assertTrue(result["lang_config"])
        self.assertEqual(result["inwentarz_wierszy"], result["plikow"])
        self.assertNotIn("Lorem", repr(result))

    def test_hash_mismatch_is_rejected(self):
        with self.assertRaises(InvalidReturn):
            validate(self.save(syn.zwrot_zbieracza(syn.drzewo_localize(), psuj="sha")))

    def test_unexpected_payload_is_rejected(self):
        with self.assertRaises(InvalidReturn):
            validate(self.save(syn.zwrot_zbieracza(syn.drzewo_localize(), psuj="nadmiarowy")))

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(InvalidReturn):
            validate(self.save(syn.zwrot_zbieracza(syn.drzewo_localize(), psuj="traversal")))


if __name__ == "__main__":
    unittest.main()
