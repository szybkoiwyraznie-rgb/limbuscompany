# Zbieracz danych (ZBIERACZ) — `LC_ZBIERZ_DANE`

Wzór: zbieracz z projektu WWM (BAT + PowerShell 5.1, test w CI na Windows),
uproszczony do plików tekstowych Limbus Company i rozszerzony o tryb
aktualizacji.

## Dla właściciela (skrót)

1. Pobierz `LC_ZBIERZ_DANE.zip` z Dysku (folder „Limbus Company”), rozpakuj
   poza folderem gry.
2. Zamknij grę. Pierwszy raz: `URUCHOM.bat`. Po aktualizacji gry:
   `URUCHOM_AKTUALIZACJE.bat`.
3. Wgraj `LC_DANE_*.zip` z Pulpitu do folderu „Limbus Company” na Dysku.

Pełna instrukcja dla właściciela: [`collector/CZYTAJ_TO.txt`](../collector/CZYTAJ_TO.txt)
(trafia do ZIP-a).

## Budowanie

```bash
python3 tools/build_collector_kit.py --output dist/LC_ZBIERZ_DANE.zip
```

ZIP jest powtarzalny (stała data, bez kompresji). Builder **sprawdza**, a nie
naprawia kodowanie: `zbierz.ps1` musi mieć UTF-8 z BOM i CRLF (PowerShell 5.1
bez BOM czyta pliki jako ANSI), pliki `.bat` — czyste ASCII i CRLF. Po edycji
narzędziem zapisującym LF przekonwertuj plik i uruchom testy.
`.gitattributes` oznacza `*.bat`/`*.ps1` jako `-text` (bajty bez zmian w Git).

## Co robi `zbierz.ps1`

1. Odmawia pracy, gdy działa proces `LimbusCompany`.
2. Znajduje grę: parametr/przeciągnięty folder → rejestr Steam
   (`SteamPath`, `InstallPath`) → `libraryfolders.vdf` → `appmanifest_1973530.acf`
   (`installdir`, `buildid`) → okno wyboru folderu. Kilka instalacji → pyta o numer.
   Odrzuca `LimbusCompany_Data` będący linkiem.
3. Tworzy spis nazw/rozmiarów/dat plików całego `LimbusCompany_Data`
   (`INWENTARZ.jsonl`, ≤250 000 wierszy, bez treści) — pozwala zobaczyć zmiany
   układu gry bez wysyłania assetów.
4. Kopiuje pliki z `Assets/Resources_moved/Localize` o rozszerzeniach
   json/txt/csv/tsv/xml/yaml/yml/md do 64 MiB (inne → `pominiete`) oraz
   `Lang/config.json` (≤64 KiB). Z `Lang/` zapisuje tylko nazwy podfolderów —
   nie kopiuje cudzych paczek tłumaczeń.
5. Liczy SHA-256 każdego pliku; przy pakowaniu liczy ponownie i oznacza pliki
   zmienione w trakcie (`problemy`, stan `niepelny`, kod 2).
6. Tryb `aktualizacja`: porównuje z plikiem stanu
   `%LOCALAPPDATA%\LC_ZBIERACZ_STAN\stan_wyslanych.json` (`lc-zbieracz-stan-v1`,
   ścieżka względna → SHA-256), pakuje tylko nowe/zmienione pliki, zapisuje
   listę usuniętych; jeśli nic się nie zmieniło — kończy bez ZIP-a (kod 0).
   Stan jest zapisywany po każdym udanym przebiegu (także `pelny`), chyba że
   `-BezStanu`.
7. Dzieli wynik na części według rozmiaru przed kompresją
   (`-LimitCzesciBajtow`, domyślnie 300 MiB); `INWENTARZ.jsonl` w części 1.
8. Zapisuje `LC_DANE_<yyyyMMdd-HHmmss>_<8 hex>[_czescN].zip` przez plik
   `.partial` i zmianę nazwy; wypisuje rozmiar i SHA-256, ostrzega powyżej 95 MiB.

Kody wyjścia: `0` OK (lub brak zmian), `2` ZIP powstał, ale zbiór niepełny,
`1` błąd (komunikat `BLAD: …`).

Parametry (dla testów i zaawansowanych): `-GameRoot` (pozycyjny),
`-OutputDirectory`, `-SteamRoot`, `-Tryb pelny|aktualizacja`, `-KatalogStanu`,
`-LimitCzesciBajtow`, `-BezStanu`, `-NonInteractive`.

## Format zwrotu `lc-zbior-v1`

| Członek ZIP | Opis |
|---|---|
| `RAPORT.json` | `format`, `zbieracz`, `tryb`, `zbior_id`, `utworzono_utc`, `czesc`/`czesci`, `gra{appid,buildid,folder_gry}`, `localize{istnieje,jezyki}`, `lang{istnieje,podfoldery,config_json}`, `stan{uzyty,plikow_w_stanie,niezmienione,usuniete[]}`, `inwentarz{w_tej_czesci,wierszy,ograniczony}`, `wszystkie_czesci[]`, `pliki[{sciezka,czlon,rozmiar,sha256}]`, `pominiete[]`, `problemy[]`, `stan_zbioru` |
| `RAPORT.txt` | to samo w skrócie, dla człowieka (CRLF) |
| `INWENTARZ.jsonl` | `{"p": ścieżka względna, "s": rozmiar, "m": data UTC}` — tylko część 1 |
| `pliki/<ścieżka względna od LimbusCompany_Data>` | kopie plików |

## Przyjęcie zwrotu (agent)

```bash
mkdir -p local/zwroty/<data>
# pobierz z Dysku do local/zwroty/<data>/ (nie do repo!)
python3 tools/validate_collector_return.py local/zwroty/<data>/LC_DANE_*.zip
python3 tools/rozpoznanie_localize.py local/zwroty/<data>/LC_DANE_*.zip \
    --wyj dist/rozpoznanie.json --md dist/rozpoznanie.md
```

Walidator otwiera ZIP bez rozpakowywania, sprawdza nazwy członków (biała lista,
brak `..`), limity rozmiarów, zgodność z raportem (rozmiar, SHA-256), duplikaty
kluczy JSON i spis; wypisuje tylko liczby. Wynik zapisz w `EXPERIMENT_LOG.md`
(SHA-256 ZIP-a, `buildid`, liczby plików na język, problemy).

## Testy

- `tests/test_collector_kit.py` — powtarzalność, kodowanie, brak operacji
  zapisu poza wynikiem i stanem, brak sieci.
- `tests/test_collector_return.py` — walidator na wymyślonych ZIP-ach (w tym
  zły SHA, niedozwolony plik, `../`).
- `tests/test_collector_windows.py` (tylko Windows/CI) — zbudowany zestaw na
  sztucznej instalacji z polskimi znakami w ścieżkach: tryb pełny, aktualizacja
  (brak zmian → brak ZIP-a; zmiana/nowy/usunięty plik), podział na części, brak
  gry; drzewo gry niezmienione (SHA-256 przed i po).

## Zmiany zbieracza

Podnieś wersję w `$script:Version`, zaktualizuj ten plik i `CZYTAJ_TO.txt`,
zbuduj ZIP, sprawdź CI na Windows, a dopiero potem wgraj na Dysk (z SHA-256 i
pobraniem z powrotem). Dysk raz zablokował ZIP zbieracza (WWM) — awaryjnie:
pobranie repozytorium z GitHub (`archive/refs/heads/main.zip`) i uruchomienie
`collector/URUCHOM.bat` z katalogu `collector/`.
