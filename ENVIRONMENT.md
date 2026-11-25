# Środowisko projektu

## Wymagania

- Git w `PATH`; GitHub CLI (`gh`) do obsługi PR.
- Python 3.11 lub 3.12. Narzędzia i testy używają **wyłącznie biblioteki
  standardowej** — bez `pip install`, bez plików gry, bez Dysku i sekretów.
- Właściciel (Windows) nie instaluje Pythona: dostaje ZIP z BAT + Windows
  PowerShell 5.1 ([docs/COLLECTOR.md](docs/COLLECTOR.md)).

Sandbox Arena (Linux) nie ma PowerShella. Skrypty `.ps1` są wykonywane w CI na
`windows-latest` na **sztucznej instalacji gry**
(`tests/test_collector_windows.py`). Wynik konkretnego commita sprawdzaj w
GitHub Actions (`gh run list`, `gh run view`).

## Kontrole z katalogu repozytorium

```sh
python --version
git status --short --branch
python tools/check_repository.py   # sprawdza pliki W INDEKSIE — najpierw git add
python tools/run_tests.py          # błąd także przy 0 testach lub pominięciach
git diff --check
```

W Windows zamiast `python` można użyć `py -3.11`.

## Katalogi i wejścia

- `local/` — prywatne wejścia (ZIP-y zbieracza, rozpakowane `Localize`,
  zwrotki przed importem). Ignorowany, regularnie czyszczony, **nie jest
  kopią zapasową**.
- `build/`, `dist/`, `artifacts/` — wyniki (ZIP zbieracza, raporty, pakiety).
- Narzędzia przyjmują ścieżki wejścia jawnie (`--wejscie`), nigdy nie szukają
  plików gry same.

Budowa zestawu zbieracza i rozpoznanie zwrotu:

```sh
python tools/build_collector_kit.py --output dist/LC_ZBIERZ_DANE.zip
python tools/validate_collector_return.py local/LC_DANE_....zip
python tools/rozpoznanie_localize.py local/LC_DANE_....zip --wyj dist/rozpoznanie.json
```

## Windows i końce wierszy

Dokumenty i kod: LF. Pliki `.bat`, `.cmd`, `.ps1` mają w `.gitattributes`
`-text` — Git zachowuje zapisane bajty. Źródła w `collector/`: **BAT = ASCII +
CRLF**, **PS1 = UTF-8 z BOM + CRLF** (PowerShell 5.1 bez BOM psuje polskie
znaki). Builder sprawdza te bajty i odmawia budowy, zamiast je „naprawiać”.
