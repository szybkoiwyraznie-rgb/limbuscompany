#!/usr/bin/env python3
"""E-027: aplikuje 133 tłumaczenia PL Notatek Dantego do magazynu ``tlumaczenie/``.

Źródła: ``local/pipeline/tr_dante/notes_pairs_{a,b,c}.json`` (mapa id → PL).
KR/EN źródła liści: ``index/localize/kr/KR_StoryTheaterDanteNoteDetail*.json``
oraz ``index/localize/en/EN_StoryTheaterDanteNoteDetail*.json``.
Idempotentny: wpisy AI nadpisują AI, ludzkie zostają nietknięte (``set_leaf``).
Klucz logical store zawsze z rozszerzeniem ``.json``.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from tools.import_zwrotki import ORIGIN_AI, TranslationStore  # noqa: E402

EN_DIR = ROOT / "index" / "localize" / "en"
KR_DIR = ROOT / "index" / "localize" / "kr"
PAIRS_DIR = ROOT / "local" / "pipeline" / "tr_dante"

# id → plik logical (wg klucza dataList w pliku _N)
LOGICAL_BY_ID: dict[int, str] = {}
_STEM = "StoryTheaterDanteNoteDetail"
_RANGES = [
    (_STEM, [12]),
    (f"{_STEM}_2", [25, 26, 27, 30, 33, 37]),
    (f"{_STEM}_3", list(range(45, 59))),
    (f"{_STEM}_4", list(range(67, 77))),
    (f"{_STEM}_5", list(range(77, 92))),
    (f"{_STEM}_6", list(range(92, 115))),
    (f"{_STEM}_7", list(range(115, 122))),
    (f"{_STEM}_8", list(range(122, 131))),
    (f"{_STEM}_9", list(range(131, 138))),
    (f"{_STEM}_10", list(range(138, 148))),
    (f"{_STEM}_11", list(range(148, 164))),
    (f"{_STEM}_12", list(range(164, 172))),
    (f"{_STEM}_13", list(range(172, 179))),
]
for stem, ids in _RANGES:
    for i in ids:
        LOGICAL_BY_ID[i] = f"{stem}.json"


def load_rows(path: Path) -> dict[int, dict]:
    d = json.loads(path.read_text(encoding="utf-8-sig"))
    return {int(str(x["id"]).split("_")[-1]): x for x in (d.get("dataList") or [])}


def source_maps() -> dict[str, dict[int, dict[int, dict]]]:
    """logical → {id → {0: kr_row, 1: en_row}}"""
    out: dict[str, dict[int, dict[int, dict]]] = {}
    for logical in sorted(set(LOGICAL_BY_ID.values())):
        kr = load_rows(KR_DIR / f"KR_{logical[:-5]}.json")
        en = load_rows(EN_DIR / f"EN_{logical[:-5]}.json")
        m: dict[int, dict[int, dict]] = {}
        for i in LOGICAL_BY_ID:
            if i in kr or i in en:
                slot = m.setdefault(i, {})
                if i in kr:
                    slot[0] = kr[i]
                if i in en:
                    slot[1] = en[i]
        out[logical] = m
    return out


def main() -> int:
    pairs: dict[str, str] = {}
    for name in ("notes_pairs_a.json", "notes_pairs_b.json", "notes_pairs_c.json"):
        pairs.update(json.loads((PAIRS_DIR / name).read_text(encoding="utf-8")))

    maps = source_maps()
    store = TranslationStore.load(ROOT / "tlumaczenie")
    written = skipped_human = missing = 0
    for sid_s, pl in sorted(pairs.items(), key=lambda kv: int(kv[0])):
        sid = int(sid_s)
        logical = LOGICAL_BY_ID[sid]
        slot = maps[logical].get(sid)
        if not slot or not slot.get(1):
            missing += 1
            print(f"BRAK EN/KR: {logical} id={sid}")
            continue
        kr_row = slot.get(0, {})
        en_row = slot[1]
        kr_desc = kr_row.get("desc") or ""
        en_desc = en_row.get("desc") or ""
        res = store.set_leaf(
            logical, f"dataList[id=DanteNoteDetail_{sid}].desc", pl, kr_desc, en_desc, origin=ORIGIN_AI
        )
        if res == "skipped_human":
            skipped_human += 1
        else:
            written += 1
    store.save_atomic(json.loads((ROOT / "index" / "MANIFEST.json").read_text(encoding="utf-8-sig")))
    print(
        f"par: {len(pairs)} | zapisanych: {written} | pominięte (human): {skipped_human} | brak źródła: {missing}"
    )
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
