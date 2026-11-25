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

## 2026-11-25 — szacunek objętości tekstu do przekładu

- Cel: odpowiedzieć właścicielowi, ile jest tekstu (stan fabuły do Canto IX
  i Intervallo VII).
- Wejście: publiczna kopia `Localize` KR/EN w
  `LocalizeLimbusCompany/LocalizeLimbusCompany`, commit `231a8bc` z 2026-08-06.
  Skrypt jednorazowy działał w `/tmp`, a wyniki zapisano tylko tutaj.
- Metoda: liczone są wartości KR z Hangulem, bez pól `id` i `model` i bez
  tagów; EN brany z tej samej ścieżki. Powtórzenia KR liczone raz.
- Wynik: wartości unikalne, słowa EN i strony po 1800 znaków EN.
  - Fabuła główna: 330 tys. słów, ok. 1000 stron.
  - Wydarzenia i Intervallo: 220 tys. słów, ok. 680 stron.
  - Opowieści osobowości: 187 tys. słów, ok. 580 stron.
  - ID, E.G.O, umiejętności, statusy i wrogowie: 341 tys. słów, ok. 1040 stron.
  - Kwestie głosowe: 133 tys. słów, ok. 410 stron.
  - Lochy: 106 tys. słów, ok. 330 stron.
  - Interfejs: 101 tys. słów, ok. 330 stron.
  - **Razem: ok. 1,42 mln słów, ok. 3,5 mln znaków KR, ok. 4400 stron.**
- Wynik w liniach (pozycje KR z Hangulem):
  - Razem 152 678 pozycji, w tym około 97 tys. unikalnych.
  - Kwestie w scenach (`StoryData`, pole `content`): 56 502.
    - Fabuła główna: 27 144 (Prolog 393; Canto I–IX: 1183, 1237, 1710,
      2493, 3578, 3101, 3647, 5312, 4490, licząc z lochami fabularnymi).
    - Wydarzenia i Intervallo: 16 641.
    - Opowieści osobowości: 12 717.
  - ID, E.G.O, umiejętności i wrogowie: 44 550 pozycji, w tym 21 329 unikalnych.
  - Głosy: 13 261 pozycji, w tym 7974 unikalne.
  - Lochy: 7129 pozycji, w tym 4982 unikalne.
  - Interfejs: 11 065 pozycji, w tym 7601 unikalnych.
- Rodzaj dowodu: szacunek z publicznej kopii.
- Ograniczenia: kopia jest z sierpnia 2026, więc treści dodane później
  doliczy pomiar na zbiorze właściciela. Kategorie przypisano po nazwach
  plików.

## 2026-11-25 — format danych pomocniczych (chronologia, statystyki) i zbieracz 1.1.0

- Cel: ustalić, skąd wziąć dokładną chronologię scen i statystyki ID dla
  Czytanek i nagłówków Pakietu (wymagania właściciela).
- Wejście: publiczne repozytoria `LocalizeLimbusCompany/LocalizeLimbusCompany`
  (drzewo i kilka plików EN: `StageChapterText`, `StagePartText`,
  `StoryTheaterMain`, `StageNode1-1`, `DungeonNode1-1`, `Personalities`,
  `Skills`, `ScenarioModelCodes`, jedna scena) i `PGGB/limbus-company-data`
  (kopia folderu gry z 2023 r.: `storytheater-main-100/101`, `personality-01`,
  `personality-skill-01`, `storybattle1-1`, `Story/Effect/1D101A`).
- Metoda: `gh api` (drzewa, pojedyncze pliki do `/tmp`), odczyt schematów;
  nic z treści nie trafiło do repozytorium.
- Wynik: chronologia = `storytheater-main` (`storyList`: scena, węzeł,
  Before/After); Canto/etapy = `StageChapterText`/`StageNode*`; statystyki =
  `personality`/`personality-skill`; tła = `Story/Effect`. Zbieracz 1.1.0
  zbiera `StaticData` i `Story`; walidator i testy (w tym Windows) rozszerzone.
- Rodzaj dowodu: analiza publicznych kopii + testy syntetyczne.
- Ograniczenia: dane pomocnicze znane z kopii z 2023 r.; bieżący układ
  potwierdzi pierwszy zbiór (raport `dodatkowe` + `INWENTARZ.jsonl`).
- Następny krok: zbiór od właściciela zestawem 1.1.0.

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
