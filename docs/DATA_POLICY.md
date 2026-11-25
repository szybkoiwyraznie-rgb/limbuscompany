# Polityka danych

Plik maszynowy: [`config/polityka_danych.json`](../config/polityka_danych.json)
(`lc-polityka-danych-v1`). Egzekwuje go `tools/check_repository.py` w CI.

## Decyzja (2026-11-25, właściciel)

Tak jak w projektach WWM i SRW: **repozytorium publiczne, żadnych binariów ani
surowych plików gry, ale wyciągnięte teksty, indeksy i tłumaczenia są w
repozytorium.** W polityce: `repozytorium_publiczne: true`,
`tekst_gry_w_git: true`, `katalogi_tekstu_gry: ["wyciag", "czytanki"]`.

## Co gdzie leży

| Dane | Miejsce |
|---|---|
| Kod, testy (dane **wymyślone**), dokumentacja, polityka | Git |
| Wyciąg tekstu (`wyciag/`): jednostki KR/EN/JP z kluczami, mówcami, kontekstem, tokenami; indeksy (sceny, postaci, pliki) | Git |
| Raporty rozpoznania i manifesty (liczby, SHA-256, `buildid`) | Git |
| Czytanki (`czytanki/`) | Git |
| Pakiety dla Tłumacza (`paczki/<nazwa>/`, rozpakowane pliki tekstowe + `paczka.json`) | Git; ZIP do przekazania — Dysk |
| Zwrotki Tłumacza (`zwrotki/`), przekład (`tlumaczenie/`), glosariusz, korekty | Git |
| Surowe pliki lokalizacji (`KR_/EN_/JP_*.json`), katalogi `LimbusCompany_Data/`, `Resources_moved/`, `Localize/` | **poza Git**: `local/` + Dysk |
| ZIP-y zbieracza `LC_DANE_*.zip` | **poza Git**: Dysk (folder „Limbus Company”) + `local/zwroty/` |
| Zbudowane ZIP-y (zbieracz, patch CLS, instalator) | **poza Git**: `dist/` → Dysk (bez GitHub Releases — decyzja 2026-11-25) |
| Binaria Unity, archiwa, pliki wykonywalne, fonty spoza `assets/fonts/` | **nigdy** w Git |

Wyciąg to tekst w formacie projektu, a nie kopia plików gry: patch CLS jest
budowany ze źródłowych JSON-ów z `local/` (albo odtwarzany z wyciągu, jeśli
wyciąg przechowuje pełną strukturę — decyzja przy projektowaniu `lc-wyciag-v1`).

## Limity techniczne

- Pojedynczy plik w Git ≤ 10 MiB (kontrola indeksu). Wyciąg i Czytanki dzielimy
  na części (Czytanki ~2,5 MB, wyciąg według plików/katalogów gry).
- Pliki tekstowe UTF-8, LF (`.gitattributes`), deterministyczne (stała
  kolejność, bez znaczników czasu w treści) — żeby diff po aktualizacji gry
  pokazywał tylko rzeczywiste zmiany.

## Zmiana polityki

Zmiana flag w `config/polityka_danych.json` wymaga decyzji właściciela, wpisu
w [CEL.md](CEL.md) i osobnego commita zawierającego tylko politykę.
`tekst_gry_w_git: false` natychmiast zablokuje w kontroli katalogi
`wyciag/` i `czytanki/`.

## Prywatność właściciela

- Zbieracz zapisuje ścieżki **względne** od `LimbusCompany_Data` i tylko nazwę
  folderu gry; nie zbiera zapisów, logów, poświadczeń.
- W publicznych logach, PR i CI nie podawaj ścieżek z nazwą użytkownika ani ID
  prywatnych plików na Dysku.
