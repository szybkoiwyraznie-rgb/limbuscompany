#!/usr/bin/env python3
"""Fala 4 — merge (pool + parts) i bezpośredni import liści do tlumaczenie/.

Użycie:
  python3 local/pipeline/fala4_apply.py --fams SpeechBubbles,AbnoGuides
  python3 local/pipeline/fala4_apply.py --fams all
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.import_zwrotki import (
    TranslationStore, validate_tokens, has_unexpected_hangul, decode_view_text,
)
from tools.lcb_text import Texts
from tools.localize import Snapshot, field_name
from tools.package_views import NON_TRANSLATABLE_FIELDS, compute_limit, encode_view_text, visible_len

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "local" / "fala4"

NOISE = {"999999", "TabExplain", "TabExpalin"}


def toks(t: str) -> set[str]:
    import re
    return {x for x in re.findall(r"\[([^\]]+)\]", t) if x not in NOISE and not x.isdigit()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fams", default="all")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    fams = None if args.fams == "all" else set(args.fams.split(","))
    scope = json.loads((OUT / "scope.json").read_text(encoding="utf-8"))
    pool = json.loads((OUT / "pool.json").read_text(encoding="utf-8"))

    values: dict[str, str] = dict(pool)
    parts = {}
    for f in sorted(OUT.glob("parts_*.json")):
        parts.update(json.loads(f.read_text(encoding="utf-8")))
    values.update(parts)

    snap = Snapshot.open(ROOT / "index" / "localize")
    store = TranslationStore.load(ROOT / "tlumaczenie")
    known_kw = set(Texts(snap, "kr").keywords) | set(Texts(snap, "en").keywords) | {"ATTRIBUTES"}

    todo = [r for r in scope if fams is None or r["fam"] in fams]
    missing = [r["seq"] for r in todo if str(r["seq"]) not in values]
    if missing:
        print(f"BRAK tłumaczeń dla {len(missing)} seq (pierwsze 10): {missing[:10]}")
        return 1

    errors = []
    warn = []
    imported = collections.Counter()
    leaf_count = 0
    token_report = collections.Counter()
    for rec in todo:
        seq = str(rec["seq"])
        pl = values[seq]
        kr, en = rec["kr"], rec["en"]
        for lf, addr in rec["addrs"]:
            if field_name(addr) in NON_TRANSLATABLE_FIELDS:
                errors.append(f"{seq} {lf} {addr}: pole nietłumaczalne")
                continue
            lim = compute_limit(field_name(addr), encode_view_text(kr), encode_view_text(en))
            pl_raw = pl.replace("\n", "\\n")
            if visible_len(pl_raw) > lim:
                errors.append(f"{seq} {lf} {addr}: LEN {visible_len(pl_raw)} > {lim}")
                continue
            errs = validate_tokens(pl_raw, kr, en, known_kw, lf)
            if errs:
                errors.append(f"{seq} {lf} {addr}: {errs}")
                continue
            if has_unexpected_hangul(pl_raw, kr, en, lf):
                errors.append(f"{seq} {lf} {addr}: Hangul w PL")
                continue
            miss = toks(kr) - toks(pl)
            if miss:
                token_report[f"{seq} {sorted(miss)}"] += 1
            if not args.dry_run:
                store.set_leaf(lf, addr, pl, kr, en, "ai")
            imported[rec["fam"]] += 1
            leaf_count += 1

    print(f"liści do importu: {leaf_count} | par: {len(todo)}")
    for fam, n in imported.most_common():
        print(f"  {fam:20s} {n:6d}")
    if token_report:
        print(f"TOKEN MISS (do triage): {len(token_report)}")
        for k in list(token_report)[:20]:
            print(f"  {k}")
    if errors:
        print(f"BŁĘDY: {len(errors)} (pierwsze 10)")
        for e in errors[:10]:
            print(f"  {e}")
    if errors:
        return 1
    if args.dry_run:
        print("DRY-RUN OK — bez zapisu")
        return 0
    manifest = json.loads((ROOT / "tlumaczenie" / "MANIFEST.json").read_text(encoding="utf-8"))
    store.save_atomic(manifest)
    print("ZAPISANO tlumaczenie/ (atomic)")
    snap.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
