#!/usr/bin/env python3
"""Fala 4 — buduje zakres pozostałych tekstów z widoki.zip poza fabułą.

Zakres: wszystkie liście KR poza ``StoryData/`` (fabuła scenes.zip + historie
IDs zostają dla Tłumacza), minus pola nietłumaczalne, minus już przetłumaczone.
Duplikaty (KR, EN) łączą się w jedną pozycję seq; mirror-pool z ``tlumaczenie/pliki``
automatycznie sugeruje PL dla par już przetłumaczonych gdziekolwiek indziej.

Wyjście: ``local/fala4/scope.json`` (pozycje seq), ``local/fala4/pool.json``
(auto-akceptowane PL z poola), ``local/fala4/tl_input_N.txt`` (rowsze bez poola).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.import_zwrotki import TranslationStore, validate_tokens, has_unexpected_hangul
from tools.lcb_text import Texts
from tools.localize import Snapshot, iter_strings, load_json, field_name
from tools.package_views import NON_TRANSLATABLE_FIELDS, compute_limit, encode_view_text, visible_len

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "local" / "fala4"

FAM_PRIORITY = [
    "SpeechBubbles", "AbnoGuides", "AbEvents", "Announcer", "EGOvoice",
    "PersonVoice", "BgmLyrics", "StoryTheater-lore", "UI-widoki", "RPGSystem",
]


def fam(lf: str) -> str:
    if lf.startswith("RPGSystem/"):
        return "RPGSystem"
    if lf.startswith("BattleAnnouncerDlg"):
        return "Announcer"
    if lf.startswith("PersonalityVoiceDlg"):
        return "PersonVoice"
    if lf.startswith(("EGOVoiceDig", "EGOvoiceDlg")):
        return "EGOvoice"
    if lf.startswith("BgmLyrics"):
        return "BgmLyrics"
    if lf.startswith("BattleSpeechBubbleDlg"):
        return "SpeechBubbles"
    if lf.startswith("AbnormalityGuides"):
        return "AbnoGuides"
    if lf.startswith(("AbEvents", "AbDlg", "ActionEvents")):
        return "AbEvents"
    if lf.startswith(("StoryTheaterDanteNoteDetail", "Story-")):
        return "StoryTheater-lore"
    return "UI-widoki"


def build_pool() -> dict[str, str]:
    store = TranslationStore.load(ROOT / "tlumaczenie")
    pool_en: dict[str, str] = {}
    pool_kr: dict[str, str] = {}
    for lf, bucket in store.files.items():
        for entry in bucket.values():
            pl = (entry.get("pl") or "").strip()
            if not pl:
                continue
            en = entry.get("en_sha256")
            kr = entry.get("kr_sha256")
            if en and en not in pool_en:
                pool_en[en] = pl
            if kr and kr not in pool_kr:
                pool_kr[kr] = pl
    return pool_en, pool_kr


def main() -> int:
    import hashlib

    def sha(t: str) -> str:
        return hashlib.sha256(t.encode("utf-8")).hexdigest()

    snap = Snapshot.open(ROOT / "index" / "localize")
    kr_files = sorted(snap.files["kr"])
    en_files = set(snap.files.get("en", {}))
    store = TranslationStore.load(ROOT / "tlumaczenie")
    known_kw = set(Texts(snap, "kr").keywords) | set(Texts(snap, "en").keywords) | {"ATTRIBUTES"}

    pool_en, pool_kr = build_pool()

    fam_rank = {f: i for i, f in enumerate(FAM_PRIORITY)}
    pairs: dict[tuple[str, str], dict] = {}
    leaves = 0
    for lf in kr_files:
        if lf.startswith("StoryData/"):
            continue
        ls = dict(iter_strings(load_json(snap.read("kr", lf))))
        lr = dict(iter_strings(load_json(snap.read("en", lf)))) if lf in en_files else {}
        bucket = store.files.get(lf, {})
        for addr, kr in ls.items():
            if field_name(addr) in NON_TRANSLATABLE_FIELDS:
                continue
            en = lr.get(addr, "")
            if not (kr.strip() or en.strip()):
                continue
            entry = bucket.get(addr)
            if entry and (entry.get("pl") or "").strip():
                continue
            if en and kr.strip() == en.strip() and any(0xAC00 <= ord(c) <= 0xD7A3 for c in en):
                continue  # dev-placeholder: nieprzetłumaczony tekst roboczy KR w EN
            leaves += 1
            lim = compute_limit(field_name(addr), encode_view_text(kr), encode_view_text(en))
            key = (kr, en)
            item = pairs.setdefault(key, {"addrs": [], "lim": lim, "fam": fam(lf), "file": lf})
            item["addrs"].append([lf, addr])
            item["lim"] = min(item["lim"], lim)
            if fam_rank[fam(lf)] < fam_rank[item["fam"]]:
                item["fam"] = fam(lf)

    ordered = sorted(
        pairs.items(),
        key=lambda kv: (fam_rank[kv[1]["fam"]], kv[1]["file"], kv[1]["addrs"][0][1]),
    )
    scope = []
    pool_out = {}
    for seq, ((kr, en), item) in enumerate(ordered, 1):
        rec = {
            "seq": seq,
            "kr": kr,
            "en": en,
            "fam": item["fam"],
            "file": item["file"],
            "lim": item["lim"],
            "addrs": item["addrs"],
        }
        scope.append(rec)
        cand = None
        if en and sha(en) in pool_en:
            cand = pool_en[sha(en)]
        elif kr and sha(kr) in pool_kr:
            cand = pool_kr[sha(kr)]
        if cand is None:
            continue
        pl = cand.replace("\n", "\\n")
        ok = (
            visible_len(pl) <= rec["lim"]
            and not has_unexpected_hangul(pl, kr, en, rec["addrs"][0][0])
            and not validate_tokens(pl, kr, en, known_kw, rec["addrs"][0][0])
        )
        if ok:
            pool_out[str(seq)] = cand

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "scope.json").write_text(json.dumps(scope, ensure_ascii=False), encoding="utf-8")
    (OUT / "pool.json").write_text(json.dumps(pool_out, ensure_ascii=False, indent=0), encoding="utf-8")

    free = [r for r in scope if str(r["seq"]) not in pool_out]
    CHUNK = 96
    n = 0
    pos = 0
    while pos < len(free):
        n += 1
        chunk = free[pos:pos + CHUNK]
        lines = []
        for r in chunk:
            kr = encode_view_text(r["kr"])
            en = encode_view_text(r["en"])
            key = f"{r['fam']}#{PurePosixPath(r['file']).name}"
            lines.append(f"{r['seq']}||{key}] {kr}|{en}")
        (OUT / f"tl_input_{n}.txt").write_text("\n".join(lines), encoding="utf-8")
        pos += len(chunk)

    stats = {}
    for r in scope:
        stats.setdefault(r["fam"], [0, 0])
        stats[r["fam"]][0] += 1
        if str(r["seq"]) not in pool_out:
            stats[r["fam"]][1] += 1
    print(f"liście w zakresie: {leaves} | unikalne pary: {len(scope)} | pool-auto: {len(pool_out)} | do ręcznego: {len(free)}")
    print(f"chunki tl_input: {n} (po 96)")
    for f in FAM_PRIORITY:
        if f in stats:
            print(f"  {f:20s} par: {stats[f][0]:6d} | do ręcznego: {stats[f][1]:6d}")
    snap.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
