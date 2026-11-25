#!/usr/bin/env python3
"""Tokeny formatowania w tekstach Limbus Company: rozpoznawanie, spis i kontrola.

Reguły pochodzą z analizy publicznych projektów tłumaczeń (docs/PRIOR_ART.md,
docs/METODA.md), zaimplementowane tu od nowa:

* **Lista nazw tagów jest zamknięta.** Gra używa nawiasów ostrych także jako
  cudzysłowu w dialogach (np. myśli, komunikaty radiowe), więc ``<[^>]+>`` nie
  może być traktowane jak tag. Tylko nazwy z ``STRICT_TAGS``/``SOFT_TAGS`` są
  tagami; nowe nazwy dopisujemy po rozpoznaniu danych, nie ogólnym wzorcem.
* **Tagi „twarde”** (kolor, styl, wyróżnienie, noparse) oraz **wypełniacze**
  ``{0}``/``{amount}`` i **ciągi „zaszumionego” tekstu** (``#&#(!@&$``) muszą
  wystąpić w przekładzie tyle samo razy co w źródle.
* **Tagi układu** (``<i>``, ``<b>``, ``<size>``...) — przekład ich nie gubi i nie
  dodaje (wyjątki tylko jawne, ``DOZWOLONE_DODATKOWE``).
* **Słowa kluczowe w nawiasach kwadratowych** (``[Sinking]``) są
  identyfikatorami tylko w tekstach mechaniki (umiejętności, pasywki, statusy);
  w fabule ``[Activating]`` to opis dźwięku i podlega tłumaczeniu.
* ``\\n`` w JSON to celowy podział wiersza — zmiana liczby to ostrzeżenie.

Moduł nie wypisuje treści — zwraca liczby i nazwy tokenów.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
import re


STRICT_TAGS = ("color", "style", "mark", "noparse")
SOFT_TAGS = ("i", "b", "u", "s", "size", "voffset", "width", "ruby", "link", "font",
             "sprite", "align", "line-height", "cspace", "material", "nobr")
DOZWOLONE_DODATKOWE: tuple[str, ...] = ()


def _tag_pattern(names: tuple[str, ...]) -> str:
    # <name>, </name>, <name=...>, </name=...> (zniekształcone zamknięcie występuje
    # w grze), <name attr=...> — wariant ze spacją wymaga "=", inaczej zdanie w
    # nawiasach zaczynające się od takiego słowa byłoby uznane za tag.
    alternatives = "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True))
    return r"</?(?:" + alternatives + r")(?:=[^<>]*|\s+[A-Za-z-]+\s*=[^<>]*)?>"


STRICT_TAG_RE = re.compile(_tag_pattern(STRICT_TAGS), re.IGNORECASE)
SOFT_TAG_RE = re.compile(_tag_pattern(SOFT_TAGS), re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\{[A-Za-z0-9_]*(?::[A-Za-z0-9.]+)?\}")
GARBLED_RE = re.compile(r"[#@$%&*!()^~]*[#@$&*^][#@$%&*!()^~]{3,}")
KEYWORD_ID_RE = re.compile(r"\[[A-Za-z][A-Za-z0-9_]*\]")
ANY_ANGLE_RE = re.compile(r"</?([A-Za-z][A-Za-z-]*)(?:=[^<>]*|\s[^<>]*)?>")
NEWLINE = "\n"


def _norm_tag(tag: str) -> str:
    """Postać do porównania: nazwa + atrybut, bez wielkości liter w nazwie."""
    match = re.match(r"(</?)([A-Za-z-]+)(.*)>", tag, re.DOTALL)
    if not match:
        return tag
    return match.group(1) + match.group(2).lower() + match.group(3) + ">"


def strict_tokens(text: str, *, keyword_ids: bool = False) -> Counter:
    tokens: Counter = Counter()
    tokens.update(_norm_tag(t) for t in STRICT_TAG_RE.findall(text))
    tokens.update(PLACEHOLDER_RE.findall(text))
    tokens.update(GARBLED_RE.findall(STRICT_TAG_RE.sub(" ", text)))
    if keyword_ids:
        tokens.update(KEYWORD_ID_RE.findall(text))
    return tokens


def soft_tokens(text: str) -> Counter:
    return Counter(_norm_tag(t) for t in SOFT_TAG_RE.findall(text))


@dataclass
class WynikKontroli:
    brakujace: Counter = field(default_factory=Counter)   # twarde: w źródle, brak w przekładzie
    nadmiarowe: Counter = field(default_factory=Counter)  # twarde: dodane w przekładzie
    uklad_brak: Counter = field(default_factory=Counter)
    uklad_dodane: Counter = field(default_factory=Counter)
    rozne_nowe_linie: bool = False

    @property
    def blad(self) -> bool:
        return bool(self.brakujace or self.nadmiarowe or self.uklad_brak or self.uklad_dodane)


def sprawdz(zrodlo: str, przeklad: str, *, keyword_ids: bool = False) -> WynikKontroli:
    """Porównaj tokeny źródła (np. KR) i przekładu (PL). Bez treści w wyniku."""
    a, b = strict_tokens(zrodlo, keyword_ids=keyword_ids), strict_tokens(przeklad, keyword_ids=keyword_ids)
    sa, sb = soft_tokens(zrodlo), soft_tokens(przeklad)
    dodane = sb - sa
    for tag in DOZWOLONE_DODATKOWE:
        dodane.pop(tag, None)
    return WynikKontroli(
        brakujace=a - b,
        nadmiarowe=b - a,
        uklad_brak=sa - sb,
        uklad_dodane=dodane,
        rozne_nowe_linie=zrodlo.count(NEWLINE) != przeklad.count(NEWLINE),
    )


def lista_tokenow(tekst: str, *, keyword_ids: bool = False) -> list[str]:
    """Tokeny do wiersza ``tokeny:`` w Pakiecie (kolejność wystąpienia, bez powtórzeń)."""
    found: list[tuple[int, str]] = []
    regexes = [STRICT_TAG_RE, SOFT_TAG_RE, PLACEHOLDER_RE]
    if keyword_ids:
        regexes.append(KEYWORD_ID_RE)
    for rx in regexes:
        found.extend((m.start(), m.group(0)) for m in rx.finditer(tekst))
    stripped = STRICT_TAG_RE.sub(lambda m: " " * len(m.group(0)), tekst)
    found.extend((m.start(), m.group(0)) for m in GARBLED_RE.finditer(stripped))
    out: list[str] = []
    for _, token in sorted(found):
        if token not in out:
            out.append(token)
    if NEWLINE in tekst:
        out.append("\\n")
    return out


class Spis:
    """Zlicza tagi i tokeny w całym zbiorze — do sprawdzenia, czy listy są pełne."""

    def __init__(self) -> None:
        self.znane: Counter = Counter()
        self.nieznane_nazwy: Counter = Counter()
        self.wypelniacze: Counter = Counter()
        self.slowa_kluczowe_id = 0
        self.zaszumione = 0
        self.nowe_linie = 0

    def dodaj(self, tekst: str) -> None:
        known = {n.lower() for n in STRICT_TAGS + SOFT_TAGS}
        for match in ANY_ANGLE_RE.finditer(tekst):
            name = match.group(1).lower()
            if name in known:
                self.znane[name] += 1
            elif match.group(0).startswith("</") or "=" in match.group(0):
                # Zamknięcie albo atrybut przy nieznanej nazwie: kandydat na tag.
                self.nieznane_nazwy[name] += 1
        self.wypelniacze.update(PLACEHOLDER_RE.findall(tekst))
        self.slowa_kluczowe_id += len(KEYWORD_ID_RE.findall(tekst))
        self.zaszumione += len(GARBLED_RE.findall(STRICT_TAG_RE.sub(" ", tekst)))
        self.nowe_linie += tekst.count(NEWLINE)

    def jako_dict(self) -> dict[str, object]:
        return {
            "tagi_znane": dict(sorted(self.znane.items())),
            "kandydaci_na_nowe_tagi": dict(sorted(self.nieznane_nazwy.items())),
            "wypelniacze": dict(sorted(self.wypelniacze.items())),
            "slowa_kluczowe_w_nawiasach": self.slowa_kluczowe_id,
            "zaszumione_ciagi": self.zaszumione,
            "nowe_linie": self.nowe_linie,
        }
