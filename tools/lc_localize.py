#!/usr/bin/env python3
"""Odczyt plików lokalizacji Limbus Company (``Localize/<jezyk>/...``) — wspólny moduł.

Wiedza o formacie jest opisana w docs/CLS_FORMAT.md. Ten moduł robi tylko to,
co jest potwierdzone publicznie (komunikat Project Moon z 2025-03-31 i
publiczne paczki CLS): pliki JSON w folderach ``kr``/``en``/``jp`` z prefiksem
``KR_``/``EN_``/``JP_`` w nazwie, który w paczce CLS się usuwa. Wszystko inne
(znaczenie pól, mówcy, kolejność scen) jest hipotezą do sprawdzenia na danych.

Moduł nie wypisuje tekstów gry; zwraca struktury do dalszego przetwarzania.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path, PurePosixPath
import re
from typing import Iterable, Iterator
import zipfile


JEZYKI = ("kr", "en", "jp")
PREFIKSY = {"kr": "KR_", "en": "EN_", "jp": "JP_"}
KATALOG_LOCALIZE = "Assets/Resources_moved/Localize"
CZLON_LOCALIZE = "pliki/" + KATALOG_LOCALIZE + "/"
KORZEN = "(korzen)"
_HANGUL = re.compile(r"[\uac00-\ud7a3\u1100-\u11ff\u3130-\u318f]")
_CYFRY = re.compile(r"\d+")


@dataclass
class PlikLokalizacji:
    """Jeden plik w jednym języku."""

    jezyk: str
    sciezka: str          # względna w folderze języka, np. "StoryData/EN_S1.json"
    nazwa_logiczna: str   # bez prefiksu języka, np. "StoryData/S1.json"
    dane: bytes


@dataclass
class ZbiorLokalizacji:
    """Pliki wszystkich języków: jezyk → nazwa logiczna → plik."""

    pliki: dict[str, dict[str, PlikLokalizacji]] = field(default_factory=dict)
    inne: list[str] = field(default_factory=list)  # pliki poza folderami języków

    def dodaj(self, plik: PlikLokalizacji) -> None:
        jezyk = self.pliki.setdefault(plik.jezyk, {})
        if plik.nazwa_logiczna in jezyk:
            raise ValueError(f"duplicate logical file in {plik.jezyk}: {plik.nazwa_logiczna}")
        jezyk[plik.nazwa_logiczna] = plik


def nazwa_logiczna(jezyk: str, sciezka: str) -> str:
    """Usuń prefiks języka z nazwy pliku (wymóg CLS); katalogi zostają."""
    czesci = PurePosixPath(sciezka).parts
    nazwa = czesci[-1]
    prefiks = PREFIKSY.get(jezyk.casefold())
    if prefiks and nazwa.upper().startswith(prefiks):
        nazwa = nazwa[len(prefiks):]
    return str(PurePosixPath(*czesci[:-1], nazwa)) if len(czesci) > 1 else nazwa


def katalog_gorny(nazwa: str) -> str:
    czesci = PurePosixPath(nazwa).parts
    return czesci[0] if len(czesci) > 1 else KORZEN


def wzorzec_nazwy(nazwa: str) -> str:
    """``StoryData/S101B.json`` → ``S{n}B.json`` (do grupowania rodzin plików)."""
    return _CYFRY.sub("{n}", PurePosixPath(nazwa).name)


def _dodaj_wzgledny(zbior: ZbiorLokalizacji, wzgledna: str, dane: bytes) -> None:
    czesci = PurePosixPath(wzgledna).parts
    if len(czesci) < 2:
        zbior.inne.append(wzgledna)
        return
    jezyk, reszta = czesci[0], str(PurePosixPath(*czesci[1:]))
    zbior.dodaj(PlikLokalizacji(jezyk, reszta, nazwa_logiczna(jezyk, reszta), dane))


def z_katalogu(sciezka: Path) -> ZbiorLokalizacji:
    """Przyjmij katalog gry, ``LimbusCompany_Data`` albo sam ``Localize``."""
    kandydaci = [
        sciezka / "LimbusCompany_Data" / KATALOG_LOCALIZE,
        sciezka / KATALOG_LOCALIZE,
        sciezka,
    ]
    korzen = next((k for k in kandydaci if k.is_dir() and any(
        (k / j).is_dir() for j in JEZYKI)), None)
    if korzen is None:
        raise ValueError("no Localize directory with kr/en/jp found")
    zbior = ZbiorLokalizacji()
    for plik in sorted(p for p in korzen.rglob("*") if p.is_file()):
        _dodaj_wzgledny(zbior, plik.relative_to(korzen).as_posix(), plik.read_bytes())
    return zbior


def z_archiwow(archiwa: Iterable[Path]) -> ZbiorLokalizacji:
    """Złóż zbiór z jednej lub kilku części ZIP zbieracza (już zwalidowanych)."""
    zbior = ZbiorLokalizacji()
    for archiwum in archiwa:
        with zipfile.ZipFile(archiwum) as zf:
            for info in zf.infolist():
                if info.filename.casefold().startswith(CZLON_LOCALIZE.casefold()) and not info.is_dir():
                    wzgledna = info.filename[len(CZLON_LOCALIZE):]
                    _dodaj_wzgledny(zbior, wzgledna, zf.read(info))
    return zbior


def wczytaj_json(dane: bytes) -> object:
    return json.loads(dane.decode("utf-8-sig"))


def liscie_tekstowe(obiekt: object, sciezka: str = "") -> Iterator[tuple[str, str]]:
    """Zwróć (wzorzec_pola, wartość) dla każdego napisu; indeksy list jako ``[]``."""
    if isinstance(obiekt, dict):
        for klucz, wartosc in obiekt.items():
            yield from liscie_tekstowe(wartosc, f"{sciezka}.{klucz}" if sciezka else str(klucz))
    elif isinstance(obiekt, list):
        for element in obiekt:
            yield from liscie_tekstowe(element, f"{sciezka}[]")
    elif isinstance(obiekt, str):
        yield sciezka, obiekt


def rekordy(obiekt: object) -> list[object] | None:
    """Lista ``dataList`` (jeśli plik ma taki układ)."""
    if isinstance(obiekt, dict) and isinstance(obiekt.get("dataList"), list):
        return obiekt["dataList"]
    return None


def identyfikatory(obiekt: object) -> list[str] | None:
    lista = rekordy(obiekt)
    if lista is None:
        return None
    return [str(r.get("id")) for r in lista if isinstance(r, dict) and "id" in r]


def ma_hangul(tekst: str) -> bool:
    return bool(_HANGUL.search(tekst))
