# Status

Najnowszy wpis na górze. Każdy wpis: data, co jest gotowe, co sprawdzono (jak),
czego **nie** sprawdzono, następny krok.

## Najnowsze — 2026-11-25: fundamenty repozytorium i zbieracz 1.0.0

**Gotowe (w PR #2, gałąź sesji):**

- Zasady pracy: `AGENTS.md`, `ENVIRONMENT.md`, `LESSONS.md`, dokumenty w `docs/`.
- Polityka danych `config/polityka_danych.json` + kontrola indeksu
  `tools/check_repository.py` (blokuje surowe pliki `KR_/EN_/JP_*.json`,
  katalogi gry, binaria Unity, archiwa, fonty poza `assets/fonts/`, katalogi
  tekstu gry przy `tekst_gry_w_git: false`).
- Zbieracz Windows `collector/` (BAT + PowerShell 5.1), tryby `pelny` i
  `aktualizacja`, budowany przez `tools/build_collector_kit.py` do
  `dist/LC_ZBIERZ_DANE.zip`.
- `tools/validate_collector_return.py` (format `lc-zbior-v1`),
  `tools/lc_localize.py` + `tools/rozpoznanie_localize.py` (raport struktury
  bez treści).
- CI: Ubuntu i Windows × Python 3.11/3.12; na Windows test integracyjny
  zbieracza na sztucznej instalacji gry (`tests/test_collector_windows.py`).

**Sprawdzone:** testy syntetyczne (Linux lokalnie; Windows w CI — wynik w PR).
**Niesprawdzone:** zbieracz na prawdziwej instalacji właściciela; prawdziwa
struktura `Localize` w aktualnej wersji gry (znana tylko z publicznych paczek
CLS, [CLS_FORMAT.md](CLS_FORMAT.md)).

**Następny krok:**

1. Właściciel uruchamia `LC_ZBIERZ_DANE.zip` → `URUCHOM.bat` i wgrywa
   `LC_DANE_*.zip` do folderu Dysku „Limbus Company”.
2. Agent: walidacja (`validate_collector_return.py`), rozpoznanie
   (`rozpoznanie_localize.py`), wpis w `EXPERIMENT_LOG.md`, uzupełnienie
   `CLS_FORMAT.md` o fakty z prawdziwych danych.
3. Odpowiedzi na otwarte pytania z [CEL.md](CEL.md) → projekt wyciągu
   (`lc-wyciag-v1`) i pierwszego Pakietu dla Tłumacza (pilot: UI + jeden
   rozdział fabuły).
