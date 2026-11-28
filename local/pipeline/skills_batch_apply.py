#!/usr/bin/env python3
"""Aplikuje partię tłumaczeń nazw/opisów skilli wroga i anomalii do magazynu.

Źródła: ``local/pipeline/tr_skills/skills_pairs.json`` (mapa ``KR||EN`` → PL;
``null`` = celowy 1:1, np. morse/kod/onomatopeje/łacina), plus reguły specjalne
dla tagów ``[...]`` i placeholderów dev. Idempotentny: wpisy AI nadpisują AI,
ludzkie zostają nietknięte (``set_leaf``).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.import_zwrotki import ORIGIN_AI, TranslationStore  # noqa: E402

EN_DIR = ROOT / "index" / "localize" / "en"
KR_DIR = ROOT / "index" / "localize" / "kr"
PL_DIR = ROOT / "local" / "cz_snapshot" / "pl"

SPECIAL_DESC = {
    "사용하지 않는 스킬": "NIEUŻYWANA UMIEJĘTNOŚĆ",
}


def load_rows(path: Path) -> list[dict]:
    d = json.loads(path.read_text(encoding="utf-8-sig"))
    return d.get("dataList") or []


def src_map(logical: str) -> dict[int, dict[object, list]]:
    out: dict[int, dict[object, list]] = {}
    en_f = EN_DIR / f"EN_{logical}.json"
    kr_f = KR_DIR / f"KR_{logical}.json"
    for x in load_rows(en_f):
        for lv in x.get("levelList") or []:
            slot = out.setdefault(int(x["id"]), {}).setdefault(lv.get("level"), [None, None])
            slot[1] = lv
    if kr_f.exists():
        for x in load_rows(kr_f):
            for lv in x.get("levelList") or []:
                slot = out.setdefault(int(x["id"]), {}).setdefault(lv.get("level"), [None, None])
                slot[0] = lv
    return out


def worklist() -> list[tuple[str, int, object, str, str, str]]:
    """(logical, id, level, field, kr, en) wszystkich liści EN==PL do naprawy."""
    rows: list[tuple[str, int, object, str, str, str]] = []
    for plf in sorted(PL_DIR.glob("Skills_*.json")):
        if not (plf.name.startswith("Skills_Enemy") or plf.name.startswith("Skills_Abnormality")
                or plf.name.startswith("Skills_Tutorial")):
            continue
        stem = plf.stem  # do plików indeksu
        logical = plf.name  # klucz store = nazwa pliku z .json
        if not (EN_DIR / f"EN_{stem}.json").exists():
            continue
        src = src_map(stem)
        for x in load_rows(plf):
            e = src.get(int(x["id"]), {})
            for lv in x.get("levelList") or []:
                kr_lv, en_lv = e.get(lv.get("level"), (None, None))
                if not en_lv:
                    continue
                if lv.get("name") and lv["name"] == en_lv.get("name"):
                    rows.append((logical, int(x["id"]), lv.get("level"), "name",
                                 kr_lv.get("name") or "", lv["name"]))
                if lv.get("desc") and (lv["desc"] or "") == (en_lv.get("desc") or ""):
                    rows.append((logical, int(x["id"]), lv.get("level"), "desc",
                                 kr_lv.get("desc") or "", lv["desc"]))
    return rows


def main() -> int:
    pairs = json.loads((ROOT / "local/pipeline/tr_skills/skills_pairs.json").read_text(encoding="utf-8"))
    pairs.update(json.loads((ROOT / "local/pipeline/tr_skills/zasied_kr_map.json").read_text(encoding="utf-8")))
    pairs.update(json.loads((ROOT / "local/pipeline/tr_skills/overrides.json").read_text(encoding="utf-8")))
    store = TranslationStore.load(ROOT / "tlumaczenie")
    rows = worklist()
    written = skipped_human = onetoone = 0
    seen: set[tuple] = set()
    for logical, sid, level, field, kr, en in rows:
        key = (logical, sid, level, field)
        if key in seen:
            continue
        seen.add(key)
        addr = f"dataList[id={sid}].levelList[level={level}].{field}"
        if kr in SPECIAL_DESC:
            pl = SPECIAL_DESC[kr]
        else:
            mapped = pairs.get(f"{kr}||{en}")
            pl = en if mapped is None else mapped  # None = celowy 1:1
            if mapped is None:
                onetoone += 1
        res = store.set_leaf(logical, addr, pl, kr, en, origin=ORIGIN_AI)
        if res == "skipped_human":
            skipped_human += 1
        else:
            written += 1
    store.save_atomic(json.loads((ROOT / "index" / "MANIFEST.json").read_text(encoding="utf-8-sig")))
    print(f"wpisów w pracy: {len(seen)} | zapisanych: {written} | 1:1: {onetoone} | pominięte (human): {skipped_human}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
