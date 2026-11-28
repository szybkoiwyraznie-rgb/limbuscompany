#!/usr/bin/env python3
"""Generic validator for AI batch translations: TOK / LEN(lim) / NUM / HANGUL.

Usage: python3 tools/validate_batch.py <parsed.json> <allp.json>
parsed.json: {seq: {kr, lim, ...}} as produced by tools/ai_batch_dump.py dump --json
allp.json:   {seq(str): PL}
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.import_zwrotki import visible_len

HANGUL = re.compile(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]")

NUM_WORDS = ["jeden", "jedna", "jedno", "jednej", "jednym", "jedną", "jedenast",
             "dwa", "dwie", "dwóch", "dwoma", "drugi", "drugiej", "drugim", "druga",
             "trzy", "trzech", "trzema", "trzeci", "trzeciej", "trzecim", "trzecia",
             "raz"]


def strip_prefix(s: str) -> str:
    m = re.match(r"^— [^\]]*\]\s?", s)
    return s[m.end():] if m else s


def main() -> int:
    parsed = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    allp = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    issues = []
    for seq in sorted(parsed, key=int):
        e = parsed[seq]
        if e.get("repeat") is not None:
            continue
        kr = strip_prefix(e["kr"])
        pl = allp.get(seq)
        if pl is None:
            issues.append((seq, "MISSING", "", ""))
            continue
        lim = e.get("lim")
        tok_kr = sorted(set(re.findall(r"\{(\d+)\}", kr)))
        tok_pl = sorted(set(re.findall(r"\{(\d+)\}", pl)))
        if tok_kr != tok_pl:
            issues.append((seq, "TOK", "kr=" + ",".join(tok_kr), "pl=" + ",".join(tok_pl)))
        if "\\n" in kr and "\\n" not in pl:
            issues.append((seq, "NL", "kr has \\n", "pl lacks \\n"))
        if lim is not None:
            L = visible_len(pl)
            if L > lim:
                issues.append((seq, "LEN", f"vis={L}", f"lim={lim}"))
        src = re.sub(r"<color=[^>]*>|</color>|<mark[^>]*>|</mark>", " ", kr)
        miss = []
        for n in sorted(set(re.findall(r"\d+", src))):
            if n in pl:
                continue
            if n in ("1", "2", "3") and any(w in pl.lower() for w in NUM_WORDS):
                continue
            miss.append(n)
        if miss:
            issues.append((seq, "NUM", ",".join(miss), ""))
        m = HANGUL.search(pl)
        if m:
            issues.append((seq, "HANGUL", m.group(), ""))
    print("issues:", len(issues))
    for seq, typ, a, b in issues:
        print(f"[{typ}] {seq}: {a} | {b}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
