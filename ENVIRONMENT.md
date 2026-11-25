# Środowisko projektu

## Wymagania obecnego etapu

- Git dostępny w `PATH`.
- Python 3.11 lub 3.12. Obecne narzędzia i testy używają **wyłącznie
  biblioteki standardowej** — nie trzeba niczego instalować `pip`-em ani mieć
  plików gry.
- GitHub CLI (`gh`) do obsługi PR (nie jest potrzebne do testów).
- Właściciel uruchamia [zbieracz Windows](docs/COLLECTOR.md) bez Pythona —
  wystarczy Windows PowerShell 5.1 (część Windows 10/11).

## Kontrole z katalogu repozytorium

```sh
python --version
git status --short --branch
python tools/check_repository.py
python tools/run_tests.py
git diff --check
```

W Windows można zamiast `python` użyć `py -3.11`. `check_repository.py`
sprawdza pliki **w indeksie Git** — nowe pliki trzeba najpierw dodać
(`git add`), aby je skontrolował. `run_tests.py` zwraca błąd także wtedy, gdy
nie uruchomiono żadnego testu albo któryś pominięto.

Testy integracyjne zbieracza (`tests/test_collector_windows.py`) są
definiowane **tylko w Windows** i uruchamiają prawdziwy `powershell.exe` 5.1
na sztucznej instalacji gry. Lokalnie w Linuksie działają testy buildera,
bajtów skryptów, walidatora i inspekcji. Pełną macierz (Ubuntu i Windows ×
Python 3.11/3.12) wykonuje GitHub Actions (`.github/workflows/ci.yml`);
wynik każdego commita sprawdzaj osobno.

## Narzędzia

| Narzędzie | Do czego | Wejście → wynik |
|---|---|---|
| `tools/build_collector_kit.py` | buduje zestaw zbieracza dla właściciela | `collector/` → `artifacts/LCB_ZBIERZ_DANE.zip` |
| `tools/validate_collector_return.py` | sprawdza ZIP od właściciela bez rozpakowania | `LCB_DANE_*.zip` → podsumowanie liczbowe |
| `tools/inspect_localize.py` | pierwsze rozpoznanie korpusu | ZIP lub katalog `Localize/` → prywatny raport `local/inspekcja/*.json` |
| `tools/localize.py` | wspólne czytniki (prefiksy, adresy tekstów) | biblioteka |
| `tools/import_data.py` | kopiuje teksty gry (JSON) do repo | ZIP zbieracza / lustro + StaticData → `index/` + `MANIFEST.json` |
| `tools/story_index.py`, `tools/build_reading.py`, `tools/build_profiles.py`, `tools/build_package.py` | indeks fabuły, Czytanki, plik ID, pakiet | `index/` → `wiedza/`, `czytanki/`, `local/pakiet/*.zip` |
| `tools/check_repository.py`, `tools/run_tests.py` | kontrole repozytorium | — |

Przykład pracy z paczką od właściciela:

```sh
mkdir -p google_drive
# pobierz LCB_DANE_....zip z Dysku do google_drive/ (ignorowane przez Git)
python tools/validate_collector_return.py google_drive/LCB_DANE_....zip
python tools/inspect_localize.py google_drive/LCB_DANE_....zip
```

## Katalogi i wejścia

| Katalog | W Git? | Zawartość |
|---|---|---|
| `collector/` | tak | źródła zbieracza Windows (CRLF; `.ps1` z UTF-8 BOM, ASCII) |
| `tools/`, `tests/` | tak | narzędzia i testy na danych wymyślonych |
| `docs/` | tak | stan, decyzje, formaty, workflow, dziennik |
| `index/` | tak | teksty gry jako JSON: Localize `kr`/`en` bajt w bajt + tabele StaticData, `MANIFEST.json` ([INDEX_FORMAT.md](docs/INDEX_FORMAT.md)) |
| `czytanki/` | tak | wygenerowane Czytanki i pliki ID (Markdown) |
| `wiedza/` | tak | indeks i kolejność fabuły (identyfikatory) |
| `tlumaczenie/` *(planowany)* | tak | magazyn przyjętych przekładów |
| `zwrotki/` *(planowany)* | tak | rejestr zwrotek tłumacza (manifesty, raporty importu) |
| `assets/fonts/` *(planowany)* | tak | wyłącznie czcionki na wolnej licencji + plik licencji |
| `local/`, `google_drive/` | **nie** | prywatne kopie od właściciela, raporty inspekcji |
| `build/`, `dist/`, `artifacts/` | **nie** | wyniki budowania (ZIP-y) |

**Budowanie czyta wyłącznie repozytorium.** Pakiety dla Tłumacza, paczka
`Lang/`, Czytanki i audyt aktualizacji biorą dane z `index/`,
`tlumaczenie/` i `zwrotki/` — nie z `local/`, nie z `google_drive/` i nie z
Dysku. Pliki od właściciela służą tylko do zbudowania lub odświeżenia `index/`.

## Windows i końce wierszy

Dokumenty i kod są wersjonowane z LF. Pliki `.bat`, `.cmd` i `.ps1` mają w
`.gitattributes` ustawione `-text` — Git zachowuje ich bajty także w „Download
ZIP” z GitHuba. Źródła `collector/` mają CRLF, `.ps1` ma UTF-8 BOM i zawiera
tylko ASCII, `.bat` jest ASCII. Builder i testy sprawdzają te bajty i
odrzucają odstępstwa zamiast je cicho naprawiać.
