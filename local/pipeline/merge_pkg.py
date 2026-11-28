# -*- coding: utf-8 -*-
"""Generyczny merge dla paczek AI-tymczasowych (D-12: wszystko w repo).

Użycie: python3 local/pipeline/merge_pkg.py <dir_praca> <glob_parts>
  <dir_praca>  np. local/praca_ai/P60  (parsed.json + krmatch.json)
  <glob_parts> np. 'local/p60_parts/parts_*.json'  ({seq: pl})

Wynik: <dir_praca>/merged.json + pełny raport walidacji LEN/TAG/NUM/TOK/NL.
"""
import glob as _glob
import json
import re
import sys

TMP_TAG = re.compile(
    r"</?(?:(?:i|b|u|s|br|sup|sub|nobr|noparse)|(?:color|size|sprite|link|style|font|mark|align|ruby|voffset|line-height|cspace|material)(?:[= ][^<>]*)?)>",
    re.I,
)
strip_prefix = re.compile(r"^— [^\]]*\]\s?")
sc = lambda s: re.sub(r"<[^>]+>", "", s)

NUM_WORDS = {
    1: ("jeden", "jedną", "jednym", "jednej", "jedno"),
    2: ("dwa", "dwie", "dwóch", "dwoma", "dwie"),
    3: ("trzy", "trzech", "trzema"),
}


def visible_len(s):
    return len(TMP_TAG.sub("", s.replace("\\n", "\n")))


def main():
    praca, parts_glob = sys.argv[1], sys.argv[2]
    D = json.load(open(praca + "/parsed.json"))
    KEYP = json.load(open(praca + "/krmatch.json"))

    parts = []
    for fn in sorted(_glob.glob(parts_glob)):
        m = json.load(open(fn))
        parts.extend((int(k), v) for k, v in m.items())

    seen = {}
    for seq, pl in parts:
        pl = pl.replace("\n", "\\n")
        if seq in seen and seen[seq] != pl:
            print("DUP CONFLICT", seq, repr(seen[seq])[:40], repr(pl)[:40])
            sys.exit(1)
        seen[seq] = pl
    # krmatch tylko dla seqów bez przekładu fresh (parts mają pierwszeństwo)
    for s in KEYP:
        if int(s) in seen:
            continue
        pl = re.sub(r"^— [^\]]*\]\s?", "", KEYP[s]).replace("\n", "\\n")
        seen[int(s)] = pl

    nonrepeat = {int(s) for s, e in D.items() if e.get("en")}
    dropped = sorted(set(seen) - nonrepeat)
    seen = {k: v for k, v in seen.items() if k in nonrepeat}
    missing = sorted(nonrepeat - set(seen))
    phantom = sorted(set(seen) - nonrepeat)
    print("non-repeat:", len(nonrepeat), "| merged:", len(seen), "| dropped:", len(dropped))
    if missing:
        print("missing:", missing)
    if phantom:
        print("phantom:", phantom)

    bad_len, bad_hangul, bad_tags, bad_num, bad_tok, bad_nl = [], [], [], [], [], []
    for seq, pl in sorted(seen.items()):
        e = D.get(str(seq))
        if not e or not e.get("en"):
            continue
        kr = strip_prefix.sub("", e["kr"])
        lim = e.get("lim") or 120
        v = visible_len(pl)
        if v > lim:
            bad_len.append((seq, lim, v, pl[:60]))
        if re.search(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]", pl):
            bad_hangul.append(seq)
        krtags = set(re.findall(r"\[([A-Za-z_0-9]+)\]", kr))
        pltags = set(re.findall(r"\[([A-Za-z_0-9]+)\]", pl))
        if krtags - pltags:
            bad_tags.append((seq, sorted(krtags - pltags)))
        kd = set(int(x) for x in re.findall(r"\d+", sc(kr)))
        pd = set(int(x) for x in re.findall(r"\d+", sc(pl)))
        miss_num = kd - pd
        real = []
        for n in miss_num:
            words = NUM_WORDS.get(n)
            if words and any(w in pl.lower() for w in words):
                continue
            real.append(n)
        if real:
            bad_num.append((seq, sorted(real), kr[:60]))
        krt = set(re.findall(r"\{\d+\}", kr))
        plt = set(re.findall(r"\{\d+\}", pl))
        if krt != plt:
            bad_tok.append((seq, sorted(krt), sorted(plt)))
        if "\\n" in e["kr"] and "\\n" not in pl:
            bad_nl.append(seq)

    print("LEN over:", len(bad_len))
    for x in bad_len:
        print("  LEN", x[0], "lim", x[1], "vis", x[2], repr(x[3]))
    print("HANGUL:", bad_hangul)
    print("MISSING TAGS:", len(bad_tags))
    for x in bad_tags[:30]:
        print("  TAG", x[0], x[1])
    print("NUM:", len(bad_num))
    for x in bad_num[:20]:
        print("  NUM", x[0], x[1], "|", x[2])
    print("TOK:", bad_tok)
    print("NL KR-has but PL-not:", bad_nl)

    json.dump({str(k): v for k, v in sorted(seen.items())}, open(praca + "/merged.json", "w"))
    print("OK ->", praca + "/merged.json")


if __name__ == "__main__":
    main()
