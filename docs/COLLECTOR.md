# Zbieracz danych (`LCB_ZBIERZ_DANE`)

Zestaw dla właściciela, uruchamiany na jego Windows. **Tylko odczyt**: nie
zmienia gry, nie wysyła niczego przez sieć, nie wymaga Pythona ani
administratora. Wzorzec: zbieracz WWM ([LESSONS.md](../LESSONS.md), lekcje 14–17).

| Plik | Rola |
|---|---|
| `collector/URUCHOM.bat` | uruchamia `zbierz.ps1` w Windows PowerShell 5.1 z `-ExecutionPolicy Bypass` (tylko ten proces), zdejmuje znacznik „pobrane z internetu”, tłumaczy kody wyjścia |
| `collector/zbierz.ps1` | właściwy zbieracz, wersja `1.0.0`, raport `lcb-zbieracz-v1` |
| `collector/CZYTAJ_TO.txt` | instrukcja po polsku dla właściciela |
| `tools/build_collector_kit.py` | buduje powtarzalny `artifacts/LCB_ZBIERZ_DANE.zip` |
| `tools/validate_collector_return.py` | sprawdza ZIP zwrotny bez rozpakowywania |

## Jak właściciel dostaje zestaw

Najprościej: z Dysku, folder **„Limbus Company” → `LCB_ZBIERZ_DANE.zip`**.
Agent buduje go `python tools/build_collector_kit.py` i wgrywa konektorem Dysku;
2026-11-25 wgranie się udało, a SHA-256 na Dysku zgadzał się z buildem
(E-003). Po zmianie zbieracza agent wgrywa nową wersję i podaje jej SHA-256.

Zapasowo: na GitHubie **Code → Download ZIP** i `collector/URUCHOM.bat`;
`.gitattributes` gwarantuje właściwe bajty (CRLF, BOM) także w takim ZIP-ie.

## Co robi

1. Znajduje grę: argument / przeciągnięty folder (dowolny folder w głąb do
   poziomu `LimbusCompany_Data` jest akceptowany) → Steam z rejestru →
   `libraryfolders.vdf` → `appmanifest_1973530.acf` → okno wyboru folderu →
   wpisanie ścieżki. Przy kilku instalacjach pyta o numer.
2. Odmawia pracy, gdy: gra jest uruchomiona; któryś folder nadrzędny gry jest
   dowiązaniem (reparse point); folder wynikowy leży wewnątrz gry.
3. Odczytuje z manifestu Steam: `buildid`, `LastUpdated`, `installdir`.
4. Kopiuje z weryfikacją SHA-256 (przed i po kopii):
   - `LimbusCompany_Data/Assets/Resources_moved/Localize/<en|kr|jp>/**/*.json`
     → `Localize/<język>/…` (języki parametrem `-Jezyki`);
   - `LimbusCompany_Data/Lang/config.json` (≤ 64 KiB), jeśli istnieje;
   - `LimbusCompany_Data/app.info` (≤ 4 KiB), jeśli istnieje.
5. Spisuje bez kopiowania: podfoldery `Lang/` (nazwa, liczba plików, bajty),
   inne katalogi obok `Localize/<język>` oraz `INWENTARZ.jsonl` —
   `{"p": ścieżka względna, "s": rozmiar, "t": data UTC}` dla plików pod
   `LimbusCompany_Data` (do 250 000 wierszy).
6. Pisze `RAPORT.json` (bez BOM) i `RAPORT.txt` (z BOM), pakuje wszystko do
   `LCB_DANE_<data>_<6 hex>.zip` na Pulpicie (ścieżki z `/`), usuwa folder
   tymczasowy `.LCB_ZBIERANIE_*`.

Kody wyjścia: **0** komplet, **2** niepełny (np. brak języka, pominięcia —
ZIP i tak powstaje, raport mówi czego brakuje), **1** błąd (bez ZIP-a).

Pełna ścieżka gry nie trafia do raportu — tylko nazwa ostatniego folderu.

## Parametry (dla testów i agentów)

| Parametr | Domyślnie | Uwagi |
|---|---|---|
| `GameRoot` (pozycyjny) | — | przeciągnięcie folderu na BAT |
| `OutputDirectory` | Pulpit | musi leżeć poza grą |
| `SteamRoot` | z rejestru | testy wskazują sztuczną bibliotekę |
| `Jezyki` | `en,kr,jp` | lista po przecinkach (`-File` podaje jeden napis) |
| `PayloadLimitBytes` | 900 MiB | po przekroczeniu pliki są pomijane → stan `partial` |
| `ArchiveWarnBytes` | 95 MiB | ostrzeżenie o limicie pobierania z Dysku |
| `NonInteractive` | wyłączony | brak pytań; niejednoznaczność = błąd |

## Po otrzymaniu ZIP-a (agent)

```sh
python tools/validate_collector_return.py google_drive/LCB_DANE_....zip
python tools/inspect_localize.py google_drive/LCB_DANE_....zip
```

Walidator sprawdza bez rozpakowania: bezpieczne nazwy członków, brak plików
wykonywalnych i niezadeklarowanych, zgodność SHA-256 i rozmiarów z
`RAPORT.json`, liczbę wierszy inwentarza. Wypisuje tylko liczby (stan, build,
pliki według rodzaju i języka). Inspekcja zapisuje **prywatny** raport do
`local/inspekcja/` ([FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md)). Wynik obu
zapisz w [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md) (bez tekstów gry).

## Testy

- `tests/test_collector_kit.py` (wszędzie): powtarzalność ZIP-a, bajty
  skryptów (CRLF, BOM, ASCII), BAT, zakaz zapisu do gry, zakaz sieci, zakaz
  cmdletów z modułów skryptowych PowerShell.
- `tests/test_collector_windows.py` (tylko Windows CI): prawdziwy
  `powershell.exe` 5.1 na sztucznej instalacji z polskimi znakami, spacjami i
  nawiasami w ścieżkach — pełne zbieranie i tylko odczyt, przeciągnięcie
  folderu przez BAT, brak języka → kod 2, wykrycie przez bibliotekę Steam,
  kolejne uruchomienia bez nadpisywania.
- `tests/test_collector_return.py`: walidator na sztucznych ZIP-ach.

## Zmiana zakresu

Gdy potrzeba więcej plików (np. czcionek gry do analizy, innych katalogów z
inwentarza): nowa wersja zbieracza (podnieś `ToolVersion`), rozszerz testy
Windows, opisz zakres w `CZYTAJ_TO.txt` i tutaj. Nie proś właściciela o ręczne
kopiowanie.
