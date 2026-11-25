# Dziennik eksperymentów

Każdy wpis: data, rodzaj (**fakt ze źródła / test syntetyczny / test na
kopii plików / test w grze**), wejście (build, SHA-256), metoda, wynik z
liczbami, ograniczenia. Bez tekstów gry i prywatnych ścieżek. Najnowsze na dole.

## E-001 · 2026-11-25 · rozpoznanie źródeł (fakt ze źródła)

- Oficjalne ogłoszenie Custom Language (Steam, 2025-03-31): położenie
  `Localize/{kr,en,jp}`, struktura `Lang/<Nazwa>/`, prefiksy usuwane, `Font/`,
  `config.json`. Szczegóły: [FEASIBILITY.md](FEASIBILITY.md).
- Publiczna paczka FR (`Eden-Office/LimbusCompanyBusFR`, commit `fcefec1`):
  2423 pliki JSON, ~34 MB, korzeń `{"dataList": […]}`; StoryData 999 plików.
- Polska paczka fanowska (`Echodial/…`, commit `12a3ebe`): 1980 plików,
  `lang` = `Polish`, `Font/replacement_map.json`. Tylko analiza techniczna.
- Dysk właściciela: wyszukiwanie nazw zawierających „Limbus” — 0 plików.
- Ograniczenie: to układ paczek fanowskich, nie oryginalnego `Localize`;
  struktura źródła do potwierdzenia na pierwszej paczce.

## E-002 · 2026-11-25 · zbieracz na Windows CI (test syntetyczny)

- Wejście: sztuczna instalacja z wymyślonymi plikami (`tests/synthetic_localize.py`),
  ścieżki z polskimi znakami, spacjami i nawiasami; Windows PowerShell 5.1 na
  `windows-latest`, Python 3.11 i 3.12.
- Pierwszy przebieg (commit `a989822`): 5/5 testów integracyjnych **nie
  przeszło** — `Get-FileHash` „nie jest rozpoznany” (cmdlet z modułu
  skryptowego `Microsoft.PowerShell.Utility.psm1`; PSModulePath na runnerze
  wskazuje moduły PowerShell 7). Ten sam problem może wystąpić u gracza.
- Poprawka (commit `dd45626`): SHA-256 przez .NET
  (`System.Security.Cryptography.SHA256`); test zakazujący cmdletów z modułów
  skryptowych. Wynik: wszystkie 4 zadania CI (Ubuntu/Windows × 3.11/3.12) zielone,
  w tym: pełne zbieranie tylko do odczytu, BAT z przeciągniętym folderem,
  brak języka → kod 2 i stan `partial`, wykrycie gry przez bibliotekę Steam
  i `appmanifest_1973530.acf`, kolejne uruchomienia bez nadpisania.
- Ograniczenie: nie uruchomiono na prawdziwej grze ani u właściciela.

## E-003 · 2026-11-25 · dostarczenie zestawu przez Dysk (test na kopii)

- `python tools/build_collector_kit.py` → `LCB_ZBIERZ_DANE.zip`, 29 652 B,
  SHA-256 `f12f73d4d4d5496ecca9518cff7b1589ff6a25319443402f299d8b7a4426656c`,
  członkowie: `CZYTAJ_TO.txt`, `URUCHOM.bat`, `zbierz.ps1`.
- Utworzono folder Dysku „Limbus Company” i wgrano zestaw konektorem; Dysk
  zwraca ten sam rozmiar i `sha256Checksum` — bajty nienaruszone. (W WWM
  konektor odrzucał ZIP z `.ps1`; tutaj nie.)
- Ograniczenie: nie sprawdzono, czy Windows/przeglądarka u właściciela nie
  zablokuje pobranego ZIP-a; BAT i tak zdejmuje znacznik pobrania z `*.ps1`.

## E-004 · 2026-11-25 · przegląd projektów społeczności i lustro oryginału (test na kopii plików)

- **Wejście:** publiczne repozytoria GitHub (lista i licencje w
  [PRIOR_ART.md](PRIOR_ART.md)); lustro oryginalnych plików
  `LocalizeLimbusCompany/LocalizeLimbusCompany` commit `231a8bc` (foldery
  `EN/ KR/ JP/`, ostatnia zmiana `KR/` 2026-08-06); biblioteka fabuły
  `retcons/limbus-storylogs` commit `c530489`. Wszystko lokalnie, wyniki
  pośrednie w ignorowanym `local/survey/`. Build Steam lustra **nieznany**.
- **Inspekcja** (`tools/inspect_localize.py`, 2,6 s): 2090/2074/2116 plików
  en/kr/jp, 0 błędów parsowania, 214 110 / 213 387 / 214 929 tekstów;
  2059 ścieżek wspólnych dla trzech języków; adresy `en`↔`kr`: 213 359
  wspólnych, 123 tylko `en`, 28 tylko `kr`. Pełna tabela:
  [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md).
- **Znaczniki** (skrypt jednorazowy, lista nazw znaczników TMP): 22 603 / 18 452
  znaczników en/kr, 52 415 / 50 483 słów kluczowych `[…]` (963 różne),
  3050 / 3027 zmiennych `{n}`. Zbiory tokenów KR = EN w 22 921 tekstach,
  różne w 3474 (~13%). Ogólny wzorzec `<…>` dawał fałszywe trafienia w 3190
  tekstach dialogów — odrzucony.
- **Adresowanie:** przy kluczu tylko `id` 31 778 z 229 413 niepustych tekstów
  EN (13,9%) miało adres pozycyjny `[#i]`; po dodaniu `key`/`level`/`abilityID`
  (`c1ac5e0`) — 19 177 (8,4%). Reszta to głównie monety umiejętności.
- **Kolejność fabuły** (`tools/story_order.py` → `wiedza/kolejnosc_fabuly.json`):
  34 strony, 728 z 922 plików StoryData przypisane; reguła nazw
  `S < nD < E…; numer; B < I < A` zgodna dla 685 z 694 sąsiednich par.
- **Czcionki** (`fontTools`, pliki z publicznych paczek): Mikodacs i
  Pretendard z paczek PL (`Echodial`), IT (`louzhee`), FR (`Eden-Office`) i
  RCR — wszystkie mają 18/18 polskich liter; licencja w pliku: SIL OFL 1.1
  (Mikodacs: gluk, Reserved Font Name „Mikodacs”). `replacement_map.json`
  paczki PL: 5 czcionek × 203 znaki, w tym 66 cyrylicy i **0 polskich liter**.
- **Świeżość luster:** TW `story-data` i `x1bViolet/Limbus-Localization-Files`
  — ostatni commit 2026-11-19; lustro LLC — 2026-08-06 (nieaktualne,
  niepełne: 2090 plików EN wobec 2406 w TW).
- **Ograniczenia:** to nie są pliki właściciela ani bieżący build; liczby
  służą do projektu narzędzi, nie jako fakty o wersji gry. Wynik czcionek nie
  mówi, czy gra poprawnie wyrenderuje polskie znaki — to rozstrzygnie test w
  grze.

## E-005 · 2026-11-25 · źródła kontekstu: chronologia, etapy, mówcy, statystyki (test na kopii plików)

- **Wejście (lokalnie, D-06):** lustro TW `LimbusTraditionalMandarin/story-data`
  commit `f218bbec` (2026-11-19; `kr/ en/ jp/`, 1002 pliki StoryData) oraz
  `StaticData/static-data` z `LEAGUE-OF-NINE/OpenLethe` commit `8f24cba`
  (dane 2026-11-12; ~2340 plików JSON, część z BOM, jeden z przecinkiem przed
  `]`). Build Steam **nieznany**.
- **Chronologia:** `storytheater-main` (Canto: rozdział → lista scen w
  kolejności menu gry, węzeł etapu, `Before`/`After`/`Inter`) i
  `storytheater-other` (Intervalla i opowiadania z `sortingOrder` i warunkiem
  odblokowania). Do tego `StageChapterText` (Localize: kolejność rozdziałów z
  datą w świecie gry), `story` (etap → scena bieżącego Canto), `battle-story`
  i `battle-ab` (sceny w trakcie walki: `enter` → `others` → `exit`),
  `RPGSystem/EndingRoute*` (trasy Canto X), `storytheater-personality`
  (historie Identity).
- **Wynik** (`tools/story_index.py` → `wiedza/indeks_fabuly.json`): 36
  rozdziałów, 808 scen (667 z Teatru, 5 z etapów, 82 z walk, 54 z reguły nazw),
  184 historie Identity, 11 bez miejsca (`E000X`–`E003X`, `RPG1`,
  `S9991B`/`S9992B`). **Kolejność 34 rozdziałów wspólnych ze storylogs (E-004)
  identyczna**; doszły Canto X i 10. Noc Walpurgii. Canto VII nie ma wpisu w
  `StageChapterText` — ustawione wyłącznie z warunków odblokowania (przed
  opowiadaniem odblokowywanym przez Canto VII), zgodnie ze storylogs.
- **Kontekst sceny:** wiersz StoryData = `content` + opcjonalnie `model`
  (koreański klucz postaci → `ScenarioModelCodes`: imię), `teller` (imię
  wyświetlane, np. „???”), `title` (**epitet mówcy**, nie tytuł sceny),
  `place` (zmiana miejsca; 147 razy liczba zamiast tekstu — pomijane). Tytuły,
  miejsca i opisy etapów: `StageNode*`; motta rozdziałów:
  `StoryTheaterMain`. EN↔KR: wiersze parują się po `id` (1 plik z różnicą:
  `P10511`).
- **Statystyki Identity:** `personality` (HP + przyrost, szybkość per
  ulepszenie, poziom obrony, odporności, progi Stagger, grzech, słowa
  kluczowe), `skill` (moc bazowa, moc i liczba monet, grzech, typ ataku per
  ulepszenie — kolejne ulepszenia nadpisują tylko zmienione pola),
  `personality-passive` + `passive` (pasywki i wymagania). Opisy z Localize
  (`Skills_personality-NN`, `Passives`, `Bufs`/`SkillTag`/`BattleKeywords`
  dla `[Słów]`, `IntroduceCharacter`, `PersonalityVoiceDlg`).
- **Prototypy** (testy syntetyczne `tests/test_story_tools.py`):
  `tools/build_reading.py` (36 Czytanek EN, Prolog + Canto I KR),
  `tools/build_profiles.py` (12 plików ID), `tools/build_package.py`
  (`plik_dla_tlumacza_v1.zip`: 1001 scen, 63 010 elementów, 60 362 do
  przetłumaczenia, 1529 napisów słownika, limit kwestii 340 = 99,9. centyl
  długości EN; 4 897 791 B, SHA-256 `1a0b02f1…1c39`). Próbki na Dysku
  właściciela (folder „Limbus Company”): `LCB_PROBKI_2026-11-25.zip`
  (2 083 386 B, `edd13310…89df`) i `plik_dla_tlumacza_v1.zip`.
- **Ograniczenia:** dane z luster, nie z paczki właściciela; w Canto X
  kolejność scen tras wynika z numeracji plików; limit 340 to miara z
  danych, nie test w grze; nazwy przynależności (`MOLAR`) bez tłumaczenia w
  danych — pokazywane jako klucz.

## E-006 · 2026-11-25 · teksty gry w repozytorium: `index/` i `czytanki/`

- **Powód:** korekta właściciela — teksty gry mają być w repozytorium jako
  JSON/MD (jak w WWM i SRW), binaria nigdy. Wcześniejsze D-06 i raport E-005
  mówiły błędnie „bez tekstu gry w repo” (lekcja 29).
- **Narzędzie:** `tools/import_data.py` kopiuje pliki JSON bajt w bajt do
  `index/localize/<lang>/` i `index/static-data/<tabela>/`, zapisuje
  `index/MANIFEST.json` (źródło, liczby, SHA-256). Generatory domyślnie
  czytają `index/`; Czytanki i pliki ID trafiają do `czytanki/`.
- **Liczby:** `localize/kr` 2449 plików / 24 594 177 B (SHA-256 katalogu
  `7762f110…77bb`), `localize/en` 2406 / 25 492 917 B (`1958134f…91ea`) z
  lustra TW @ `f218bbec`; `static-data` 12 tabel, 1153 pliki / 21 620 590 B z
  OpenLethe @ `8f24cba5`. Największy plik < 5 MB. `czytanki/`: 2 × 37 plików
  fabuły (spis + 36 rozdziałów) i 2 × 12 plików ID.
- **Zmiana w indeksie fabuły:** 1001 plików StoryData zamiast 1002 —
  `S1002A` istnieje w lustrze tylko po japońsku (bez KR/EN), a JP nie jest
  kopiowany. Reszta indeksu bez zmian; `zrodla` podaje teraz opis z manifestu
  zamiast commitu katalogu.
- **Kontrola:** `diff -r` lustra z `index/localize/kr` — identyczne;
  ponowny import daje ten sam manifest; `.gitattributes` wyłącza konwersję
  końców wierszy w `index/localize` i `index/static-data` (28 plików z BOM
  zostaje nietkniętych).
