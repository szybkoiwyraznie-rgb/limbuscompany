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
- Wynik: Linux — wszystkie testy OK; Windows — patrz checki PR #2.
- Rodzaj dowodu: test syntetyczny.
- Ograniczenia: brak testu na prawdziwej instalacji (rejestr Steam,
  `libraryfolders.vdf` testowane tylko pośrednio).
- Następny krok: uruchomienie u właściciela.
