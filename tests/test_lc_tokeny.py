"""Tokeny formatowania na wymyślonych napisach."""
from __future__ import annotations

import unittest

from tools import lc_tokeny as tk


class TokenTests(unittest.TestCase):
    def test_angle_bracket_quotes_are_not_tags(self):
        text = "<Hej...> <color=#f8c200>raz</color> <Mark, proszę>"
        self.assertEqual(tk.strict_tokens(text), {"<color=#f8c200>": 1, "</color>": 1})
        self.assertEqual(tk.soft_tokens(text), {})

    def test_attribute_with_space_requires_equals(self):
        self.assertEqual(tk.strict_tokens("<mark color=#ff000040>x</mark>"),
                         {"<mark color=#ff000040>": 1, "</mark>": 1})
        self.assertEqual(tk.strict_tokens("<mark it down>"), {})

    def test_malformed_closing_tag_is_kept_as_token(self):
        self.assertEqual(tk.strict_tokens("<color=#fff>a</color=#fff>")["</color=#fff>"], 1)

    def test_placeholders_and_garbled_sequences(self):
        tokens = tk.strict_tokens("{0} i {amount} oraz {0:F1} #&#(!@&$")
        self.assertEqual(tokens["{0}"], 1)
        self.assertEqual(tokens["{amount}"], 1)
        self.assertEqual(tokens["{0:F1}"], 1)
        self.assertEqual(tokens["#&#(!@&$"], 1)

    def test_keyword_ids_only_when_requested(self):
        self.assertEqual(tk.strict_tokens("Nałóż 2 [Sinking]"), {})
        self.assertEqual(tk.strict_tokens("Nałóż 2 [Sinking]", keyword_ids=True), {"[Sinking]": 1})

    def test_check_detects_lost_added_and_layout_changes(self):
        ok = tk.sprawdz("<i>가나</i> {0}", "<i>ab</i> {0}")
        self.assertFalse(ok.blad)
        lost = tk.sprawdz("<color=#a>가</color> {0}", "<color=#a>a</color>")
        self.assertEqual(lost.brakujace, {"{0}": 1})
        added = tk.sprawdz("가", "<b>a</b>")
        self.assertEqual(added.uklad_dodane, {"<b>": 1, "</b>": 1})
        self.assertTrue(tk.sprawdz("가\n나", "ab").rozne_nowe_linie)

    def test_token_list_for_packages(self):
        self.assertEqual(tk.lista_tokenow("<color=#f8c200>{0}</color> [Burn]\nx", keyword_ids=True),
                         ["<color=#f8c200>", "{0}", "</color>", "[Burn]", "\\n"])

    def test_inventory_reports_names_and_candidates(self):
        spis = tk.Spis()
        spis.dodaj("<color=#fff>a</color> <Hej> <glow=1>b</glow> {0}\n")
        result = spis.jako_dict()
        self.assertEqual(result["tagi_znane"], {"color": 2})
        self.assertEqual(result["kandydaci_na_nowe_tagi"], {"glow": 2})
        self.assertEqual(result["wypelniacze"], {"{0}": 1})
        self.assertEqual(result["nowe_linie"], 1)


if __name__ == "__main__":
    unittest.main()
