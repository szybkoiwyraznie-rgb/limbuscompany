# Status

Stan na **2026-11-26**.

## Gdzie jesteśmy

**Pierwsza produkcyjna polska paczka językowa `LCB_PL_Polski_26917622_v1.zip`
(`7 491 054` B, build Steam `26917622`) jest zbudowana z repozytorium i wgrana na
Dysk Google (E-014): obejmuje 100% Prologu oraz Canto I–III (`105` scen), `36`
historii Tożsamości Sezonu 1, `169` mówców/tytułów/miejsc oraz wczesne Notatki
Dantego i karty Teatru (`12 099 / 193 308` = `6,26%` liści w całej grze z
bezpiecznym fallbackiem EN dla nieprzetłumaczonych jeszcze części).**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows,
  `63/63` testów zielonych).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł przebieg bazowy (`26652290`, E-007)
  oraz przebieg po czwartkowej aktualizacji (`LCB_DANE_20261126_094359_ef145d.zip`,
  build Steam **`26917622`**, 7368 plików, 0 błędów — E-013).
- Wszystkie decyzje projektowe zamknięte (`D-01` … `D-10`, brak otwartych `O-*`):
  źródło przekładu **KR** (D-05), teksty gry w repozytorium jako JSON/MD bez
  binariów (D-06), układ Czytanek zaakceptowany i zamrożony (D-07), kompletny
  pakiet 100% gry naraz (D-08), nazwa języka **`Polski`** i 5-kluczowy
  `Lang/config.json` (D-09), niemodyfikowane czcionki SIL OFL 1.1 w
  `assets/fonts/` potwierdzone w grze (D-10, zamyka O-03).
- **Teksty gry i Czytanki w repozytorium** (E-006, E-007, E-013):
  `index/localize/{kr,en}` na aktualnym buildzie Steam **`26917622`** (`2 464`
  `kr`, `2 421` `en`); `index/static-data/` z OpenLethe (`8f24cba5`, dane z
  `2026-11-12` — do odświeżenia, gdy OpenLethe opublikuje tabele dla `10117` i
  `11217`); Czytanki i pliki ID w `czytanki/`.
- **Pakiety dla tłumacza na Dysku:**
  - pakiet bazowy (`26652290`, E-008): `plik_dla_tlumacza_v2.zip` (`11 449 704` B,
    SHA-256 `9bb4dcad…a5006` — **156 079** elementów / **130 043** unikalnych
    napisów);
  - **pakiet przyrostowy z aktualizacji `2026-11-26` (`26652290` → `26917622`,
    E-013): `pakiet_przyrostowy_26652290_do_26917622.zip`** (`155 363` B,
    SHA-256 `c20f006a1e7cb38a7a21b1b5f5f2307b784d5476527df72f4a0df9ba1953b3df`
    — wyłącznie nowości i poprawki z łatki: `2` nowe historie Tożsamości
    `P10117` Yi Sang i `P11217` Gregor, `3` nowe wpisy słownika mówców oraz `17`
    plików widoków, łącznie **1 733** unikalne puste pola `PL:`).
- **Stan przekładu (`tlumaczenie/`) i paczka do gry na Dysku (E-014):**
  - zaimportowano pierwszą zwrotkę `LC_PL1.zip` (`19` plików Markdown, `0`
    błędów, `0` ostrzeżeń): `149` plików w `tlumaczenie/pliki/` (`5 559`
    adresów), `169` wpisów w `tlumaczenie/slowniki.json`, `379` powiązań w
    `tlumaczenie/powtorzenia.json`;
  - zbudowano i wgrano na Dysk produkcyjną paczkę
    **`LCB_PL_Polski_26917622_v1.zip`** (`7 491 054` B, SHA-256
    `b335c53abf082a201a15dc4dfbc9f7710df84ee5d559f9f24bdd2ab7e4169e82` —
    `2 421` plików JSON, `469` zmodyfikowanych, `12 099 / 193 308` = `6,26%`
    liści po polsku).
- **Importer zwrotek, generator `Lang/Polski/` i audyt aktualizacji (E-009 … E-014):**
  - `tools/import_zwrotki.py` waliduje zgodność źródeł, znaczniki TMP, zmienne
    `{0}`, słowa kluczowe `[Keyword]`, styl `DEN` w `BgmLyrics/*` i znaczniki
    skryptu `//…` w `StoryData/*`, ostrzega przed niezamierzonym Hangulem w
    `PL:`, dziedziczy powtórzenia, obsługuje `--allow-older-package` i zapisuje
    `tlumaczenie/` atomowo;
  - `tools/build_lang.py` buduje deterministyczne archiwum `Lang/Polski/` (pełny
    5-kluczowy `config.json` + czcionki OFL z `assets/fonts/` + pliki JSON z
    fallbackiem EN i rzutowaniem słownika mówców/tytułów) — działanie
    potwierdzone w grze (`E-012`);
  - `tools/audit_update.py` porównuje buildy (`--old` lub czysto z Git
    `--old-rev`), wykrywa zmienione oryginały `KR` w `tlumaczenie/` i buduje
    pakiety uzupełniające (`--delta-scope files`) oraz ścisłe pakiety
    przyrostowe (`--delta-scope items`).

## Następny krok

1. **Właściciel:** pobrać z folderu `Limbus Company` na Dysku paczkę
   `LCB_PL_Polski_26917622_v1.zip`, rozpakować `LimbusCompany_Data` do katalogu
   gry i przetestować polską wersję (Prolog + Canto I–III + 36 historii
   Identity + Notatki Dantego / Teatr); kolejne części zwrotki wrzucać do tego
   samego folderu.
2. **Agent:** integrować kolejne zwrotki tłumacza (`tools/import_zwrotki.py` z
   `--allow-older-package`, gdy dotyczą plików dotkniętych aktualizacją) i
   publikować kolejne wersje `LCB_PL_Polski_<build>_vN.zip`; gdy `OpenLethe`
   opublikuje zaktualizowane `StaticData`, dograć je przez `tools/import_data.py`.

## Otwarte decyzje

Brak — wszystkie `O-01` … `O-07` zamknięte w [DECYZJE.md](DECYZJE.md).
