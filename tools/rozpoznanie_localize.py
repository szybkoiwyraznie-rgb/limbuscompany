#!/usr/bin/env python3
"""Rozpoznanie struktury plików lokalizacji — bez wypisywania tekstów gry.

Wejście: części ZIP zbieracza (``LC_DANE_*.zip``, walidowane przed odczytem)
albo katalog (folder gry, ``LimbusCompany_Data`` lub ``Localize``).
Wynik: raport JSON (``lc-rozpoznanie-v1``) z liczbami, nazwami plików i
wzorcami pól oraz opcjonalne podsumowanie Markdown. Raport nie zawiera treści
napisów (do jej przetwarzania służy wyciąg). Po przeglądzie raport może trafić
do Git (np. ``wyciag/rozpoznanie/``), zob. docs/DATA_POLICY.md.

Przykład::

    python tools/rozpoznanie_localize.py local/LC_DANE_x.zip --wyj dist/rozpoznanie.json --md dist/rozpoznanie.md
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import lc_localize as lc  # noqa: E402
from tools.validate_collector_return import validate  # noqa: E402


FORMAT = "lc-rozpoznanie-v1"


def analizuj(zbior: lc.ZbiorLokalizacji) -> dict[str, object]:
    jezyki = sorted(zbior.pliki)
    wszystkie_nazwy = sorted({n for pliki in zbior.pliki.values() for n in pliki})
    raport_jezykow: dict[str, dict[str, int]] = {}
    pola_razem: dict[str, Counter] = defaultdict(Counter)
    katalogi: Counter = Counter()
    wzorce: Counter = Counter()
    pliki_raport = []
    bledne: Counter = Counter()

    for jezyk in jezyki:
        pliki = zbior.pliki[jezyk]
        raport_jezykow[jezyk] = {
            "plikow": len(pliki),
            "bajtow": sum(len(p.dane) for p in pliki.values()),
        }

    for nazwa in wszystkie_nazwy:
        katalogi[lc.katalog_gorny(nazwa)] += 1
        wzorce[f"{lc.katalog_gorny(nazwa)}/{lc.wzorzec_nazwy(nazwa)}"] += 1
        obecne = [j for j in jezyki if nazwa in zbior.pliki[j]]
        wpis: dict[str, object] = {"nazwa": nazwa, "jezyki": obecne}
        ids_wg_jezyka: dict[str, list[str] | None] = {}
        for jezyk in obecne:
            try:
                obiekt = lc.wczytaj_json(zbior.pliki[jezyk][nazwa].dane)
            except (UnicodeError, json.JSONDecodeError):
                bledne[jezyk] += 1
                wpis.setdefault("bledny_json", []).append(jezyk)
                continue
            ids_wg_jezyka[jezyk] = lc.identyfikatory(obiekt)
            pola = Counter()
            niepuste = 0
            znaki = 0
            hangul = 0
            for wzorzec, wartosc in lc.liscie_tekstowe(obiekt):
                pola[wzorzec] += 1
                if wartosc.strip():
                    niepuste += 1
                    znaki += len(wartosc)
                    hangul += lc.ma_hangul(wartosc)
            wpis.setdefault("napisy", {})[jezyk] = {
                "pol": sum(pola.values()),
                "niepustych": niepuste,
                "znakow": znaki,
                "z_hangul": hangul,
            }
            if jezyk == "en" or "pola" not in wpis:
                wpis["pola"] = dict(sorted(pola.items()))
                lista = lc.rekordy(obiekt)
                wpis["rekordow"] = len(lista) if lista is not None else None
                wpis["uklad"] = "dataList" if lista is not None else type(obiekt).__name__
        ids = {j: v for j, v in ids_wg_jezyka.items() if v is not None}
        if ids:
            pierwszy = next(iter(ids.values()))
            wpis["duplikaty_id"] = len(pierwszy) - len(set(pierwszy))
            wpis["id_zgodne_miedzy_jezykami"] = all(set(v) == set(pierwszy) for v in ids.values())
        for wzorzec, liczba in wpis.get("pola", {}).items():
            pola_razem[wzorzec]["plikow"] += 1
            pola_razem[wzorzec]["wystapien"] += liczba
        pliki_raport.append(wpis)

    wspolne = [p for p in pliki_raport if len(p["jezyki"]) == len(jezyki)]
    tylko = {
        j: sorted(p["nazwa"] for p in pliki_raport if p["jezyki"] == [j])
        for j in jezyki
    }
    niezgodne_id = sorted(
        p["nazwa"] for p in pliki_raport if p.get("id_zgodne_miedzy_jezykami") is False
    )
    return {
        "format": FORMAT,
        "jezyki": raport_jezykow,
        "plikow_logicznych": len(wszystkie_nazwy),
        "parzystosc": {
            "we_wszystkich_jezykach": len(wspolne),
            "tylko_w_jednym": tylko,
            "niezgodne_id": niezgodne_id,
        },
        "bledny_json": dict(bledne),
        "pliki_poza_jezykami": sorted(zbior.inne),
        "katalogi": dict(sorted(katalogi.items())),
        "rodziny_nazw": dict(sorted(wzorce.items(), key=lambda kv: (-kv[1], kv[0]))),
        "pola": {k: dict(v) for k, v in sorted(pola_razem.items(), key=lambda kv: (-kv[1]["wystapien"], kv[0]))},
        "pliki": pliki_raport,
    }


def podsumowanie_md(raport: dict[str, object], opis: dict[str, object]) -> str:
    linie = ["# Rozpoznanie plików lokalizacji", ""]
    for klucz, wartosc in opis.items():
        linie.append(f"- {klucz}: `{wartosc}`")
    linie += ["", "| język | plików | bajtów |", "|---|---:|---:|"]
    for jezyk, dane in raport["jezyki"].items():
        linie.append(f"| {jezyk} | {dane['plikow']} | {dane['bajtow']} |")
    par = raport["parzystosc"]
    linie += [
        "",
        f"Plików logicznych: **{raport['plikow_logicznych']}**, we wszystkich językach: "
        f"**{par['we_wszystkich_jezykach']}**, z niezgodnymi `id`: **{len(par['niezgodne_id'])}**.",
        "",
        "| katalog | plików |",
        "|---|---:|",
    ]
    for katalog, liczba in raport["katalogi"].items():
        linie.append(f"| {katalog} | {liczba} |")
    linie += ["", "## Najczęstsze pola z napisami (wzorce)", "", "| pole | plików | wystąpień |", "|---|---:|---:|"]
    for pole, dane in list(raport["pola"].items())[:40]:
        linie.append(f"| `{pole}` | {dane['plikow']} | {dane['wystapien']} |")
    linie += ["", "## Rodziny nazw plików (top 40)", "", "| wzorzec | plików |", "|---|---:|"]
    for wzorzec, liczba in list(raport["rodziny_nazw"].items())[:40]:
        linie.append(f"| `{wzorzec}` | {liczba} |")
    return "\n".join(linie) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("wejscie", nargs="+", type=Path, help="części ZIP zbieracza albo jeden katalog")
    parser.add_argument("--wyj", type=Path, required=True, help="raport JSON (np. dist/rozpoznanie.json)")
    parser.add_argument("--md", type=Path, help="opcjonalne podsumowanie Markdown")
    args = parser.parse_args()

    opis: dict[str, object] = {}
    if len(args.wejscie) == 1 and args.wejscie[0].is_dir():
        zbior = lc.z_katalogu(args.wejscie[0])
        opis["wejscie"] = "katalog"
    else:
        wyniki = [validate(p) for p in args.wejscie]
        buildy = sorted({str(w["buildid"]) for w in wyniki})
        opis.update({"wejscie": "zip", "czesci": len(wyniki), "buildid": ", ".join(buildy),
                     "tryb": ", ".join(sorted({str(w["tryb"]) for w in wyniki}))})
        zbior = lc.z_archiwow(args.wejscie)
    raport = analizuj(zbior)
    raport["wejscie"] = opis
    args.wyj.parent.mkdir(parents=True, exist_ok=True)
    args.wyj.write_text(json.dumps(raport, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if args.md:
        args.md.parent.mkdir(parents=True, exist_ok=True)
        args.md.write_text(podsumowanie_md(raport, opis), encoding="utf-8")
    print(json.dumps({
        "jezyki": raport["jezyki"],
        "plikow_logicznych": raport["plikow_logicznych"],
        "we_wszystkich_jezykach": raport["parzystosc"]["we_wszystkich_jezykach"],
        "niezgodne_id": len(raport["parzystosc"]["niezgodne_id"]),
        "bledny_json": raport["bledny_json"],
        "katalogi": raport["katalogi"],
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
