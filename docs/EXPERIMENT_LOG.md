# Dziennik eksperymentów

Najnowszy wpis na górze. Szablon:

```
## RRRR-MM-DD — krótki tytuł
- Cel:
- Wejście: (plik, buildid, SHA-256 — bez prywatnych ścieżek i ID z Dysku)
- Metoda: (polecenie / narzędzie i wersja)
- Wynik: (liczby)
- Rodzaj dowodu: test syntetyczny / test na kopii plików / test w grze
- Ograniczenia:
- Następny krok:
```

## 2026-11-25 — przegląd innych projektów tłumaczeń Limbus

- Cel: przejąć sprawdzone metody i indeksy zamiast projektować od zera
  (decyzja właściciela).
- Wejście: 14 publicznych repozytoriów GitHub (lista i licencje w
  [PRIOR_ART.md](PRIOR_ART.md)); płytkie klony 10 z nich + drzewa plików.
- Metoda: `gh search repos`, `gh api …/git/trees`, odczyt README, konfiguracji,
  skryptów budowania/kontroli i wytycznych (LLC Wiki); bez kopiowania kodu
  ani tekstów do repozytorium.
- Wynik: [METODA.md](METODA.md) — 10 punktów; `tools/lc_tokeny.py` (8 testów);
  spis tokenów w raporcie rozpoznania.
- Rodzaj dowodu: analiza cudzych publicznych materiałów + testy syntetyczne.
- Ograniczenia: reguły tagów zweryfikowane przez autorów AutoLocalization na
  parach EN–zh, nie na naszych danych; licencje części repozytoriów nieokreślone
  (tylko reguły, kod własny).
- Następny krok: indeksy (postacie, słowa kluczowe) i specyfikacja
  `lc-wyciag-v1` na pierwszym zbiorze właściciela.

## 2026-11-25 — rozpoznanie publiczne formatu CLS (bez danych właściciela)

- Cel: ustalić format paczki CLS i strukturę plików przed pierwszym zbiorem.
- Wejście: komunikaty Steam (CLS 2025-03-31, v1.74.0), publiczne repozytorium
  paczki FR (Eden-Office/LimbusCompanyBusFR, klon bez blobów, lista plików +
  3 próbki: scena `StoryData`, plik umiejętności, `config.json`), dokumentacja
  narzędzi społeczności.
- Metoda: `git ls-tree` z `GIT_NO_LAZY_FETCH=1`, odczyt próbek; bez kopiowania
  treści do repozytorium.
- Wynik: ~2429 plików w paczce FR; katalogi i schematy opisane w
  [CLS_FORMAT.md](CLS_FORMAT.md) (oznaczone [P]).
- Rodzaj dowodu: analiza publicznych plików (nie dane właściciela, nie test w grze).
- Ograniczenia: paczka FR może nie odpowiadać aktualnej wersji gry; nazwy
  plików bez prefiksów (to już format `Lang/`, nie `Localize`).
- Następny krok: pierwszy zbiór od właściciela i `rozpoznanie_localize.py`.

## 2026-11-25 — zbieracz 1.0.0: testy syntetyczne

- Cel: sprawdzić zestaw zbieracza przed wysłaniem właścicielowi.
- Wejście: wymyślone drzewo `Localize` (`tests/syntetyczne.py`).
- Metoda: `python3 tools/run_tests.py` (Linux, lokalnie); CI `windows-latest`
  uruchamia `tests/test_collector_windows.py` z prawdziwym PowerShell 5.1.
- Wynik: Linux — wszystkie testy OK; Windows (CI) — 4/4 testy integracyjne OK po
  poprawce: Windows PowerShell 5.1 zgłaszał „Argument types do not match” przy
  `@(… | Sort-Object)` w zagnieżdżonym literale `[ordered]@{}` — raport składany
  teraz ze zwykłych zmiennych (wniosek w LESSONS.md).
- Dostawa: `LC_ZBIERZ_DANE.zip`, 28 200 B, SHA-256
  `2138f49adf00394e766db96d1ec3c222996277c026d17a1ead27c668d0b3ee7f`, Dysk →
  pobranie z powrotem → `cmp` identyczne.
- Rodzaj dowodu: test syntetyczny.
- Ograniczenia: brak testu na prawdziwej instalacji (rejestr Steam,
  `libraryfolders.vdf` testowane tylko pośrednio).
- Następny krok: uruchomienie u właściciela.
