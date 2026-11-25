# Status

Najnowszy wpis na górze. Każdy wpis: data, co jest gotowe, co sprawdzono (jak),
czego **nie** sprawdzono, następny krok.

## Najnowsze — 2026-11-25: fundamenty repozytorium i zbieracz 1.0.0

**Gotowe (w PR #2, gałąź sesji):**

- Zasady pracy: `AGENTS.md`, `ENVIRONMENT.md`, `LESSONS.md`, dokumenty w `docs/`.
- Polityka danych `config/polityka_danych.json` + kontrola indeksu
  `tools/check_repository.py` (blokuje surowe pliki `KR_/EN_/JP_*.json`,
  katalogi gry, binaria Unity, archiwa, fonty poza `assets/fonts/`). Wyciąg,
  indeksy, Czytanki i tłumaczenia mogą być w Git (decyzja 2026-11-25).
- Zbieracz Windows `collector/` (BAT + PowerShell 5.1), tryby `pelny` i
  `aktualizacja`, budowany przez `tools/build_collector_kit.py` do
  `dist/LC_ZBIERZ_DANE.zip`.
- `tools/validate_collector_return.py` (format `lc-zbior-v1`),
  `tools/lc_localize.py` + `tools/rozpoznanie_localize.py` (raport struktury
  bez treści).
- CI: Ubuntu i Windows × Python 3.11/3.12; na Windows test integracyjny
  zbieracza na sztucznej instalacji gry (`tests/test_collector_windows.py`).

**Sprawdzone:** testy syntetyczne — Linux lokalnie i w CI; Windows w CI
(`windows-latest`, PowerShell 5.1, Python 3.11/3.12): zbieracz na sztucznej
instalacji — tryb pełny, aktualizacja, części, brak gry — zielone.
**Dostarczone:** `LC_ZBIERZ_DANE.zip` (28 200 B, SHA-256
`2138f49adf00394e766db96d1ec3c222996277c026d17a1ead27c668d0b3ee7f`) w folderze
Dysku „Limbus Company”; pobrany z powrotem — bajty identyczne.
**Niesprawdzone:** zbieracz na prawdziwej instalacji właściciela; prawdziwa
struktura `Localize` w aktualnej wersji gry (znana tylko z publicznych paczek
CLS, [CLS_FORMAT.md](CLS_FORMAT.md)).

**Następny krok:**

1. Właściciel uruchamia `LC_ZBIERZ_DANE.zip` → `URUCHOM.bat` i wgrywa
   `LC_DANE_*.zip` do folderu Dysku „Limbus Company”.
2. Agent: walidacja (`validate_collector_return.py`), rozpoznanie
   (`rozpoznanie_localize.py`), wpis w `EXPERIMENT_LOG.md`, uzupełnienie
   `CLS_FORMAT.md` o fakty z prawdziwych danych.
3. Projekt wyciągu `lc-wyciag-v1` (źródło KR, EN/JP obok) do `wyciag/` w
   Git, Czytanki źródłowe, pierwszy Pakiet dla Tłumacza (pilot: UI + jeden
   rozdział fabuły). Decyzje z 2026-11-25 są w [CEL.md](CEL.md).
