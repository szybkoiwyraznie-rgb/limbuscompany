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

## E-007 · 2026-11-25 · pierwsza paczka ze zbieracza właściciela: Steam build `26652290` (fakt ze źródła)

- **Wejście:** `LCB_DANE_20261125_190908_2e6403.zip` (19 086 393 B,
  SHA-256 `169c774e771dcb58f5bcd0fb2a57b230d179b2921a959aab285a49d403036f90`),
  zebrany narzędziem `LCB_ZBIERZ_DANE 1.0.0` na instalacji właściciela.
  `status = complete`, `problems = 0`, `skipped = 0`, build Steam
  **`26652290`**, `app.info` = `ProjectMoon` / `LimbusCompany`.
- **Walidacja** (`tools/validate_collector_return.py`): `passed`; 7320 plików
  zadeklarowanych i zgodnych po SHA-256 (`Localize`: 2449 `kr`, 2406 `en`,
  2464 `jp`; 1 × `app.info`; 0 × `Lang/config.json` — brak zainstalowanej
  paczki językowej), 78 813 543 B ładunku. `INWENTARZ.jsonl`: 9136 wpisów
  (7322 w `LimbusCompany_Data/Assets`, 1746 w `StreamingAssets` — banki FMOD
  `.bank` i konfiguracja usług; w katalogu instalacji Steam nie ma luźnych
  plików `StaticData`).
- **Import** (`tools/import_data.py` → `index/localize/`):
  `kr` — 2449 plików / 25 222 309 B (SHA-256 katalogu `7adf1c18…f832`);
  `en` — 2406 plików / 26 225 485 B (`12c225b0…892b`).
- **Porównanie z lustrem TW (`f218bbec`):** `git diff --ignore-space-at-eol`
  na całym `index/localize/` daje **0 różnic** — liczba plików, nazwy i cała
  treść JSON w `kr` i `en` są w 100% identyczne z buildem Steam `26652290`;
  różnica rozmiaru bajtowego (+628 132 B w `kr`, +732 568 B w `en`) wynika
  wyłącznie z zachowania oryginalnych końców linii CRLF z gry (lustro Git
  miało LF). Przebudowa `wiedza/indeks_fabuly.json` aktualizuje metadane
  źródła; wygenerowane `czytanki/` nie zmieniają ani jednego znaku.
- **Ograniczenia:** `StaticData` pochodzi nadal z lustra OpenLethe (`8f24cba5`),
  ponieważ gra nie trzyma `StaticData` jako luźnych JSON-ów w katalogu Steam.

## E-008 · 2026-11-25 · kompletny pakiet dla tłumacza 100% gry (`sceny.zip` + `widoki.zip`, build `26652290`) (fakt z pomiaru)

- **Cel:** rozszerzyć `tools/build_package.py` (z nowym modułem
  `tools/package_views.py`) tak, aby pakiet dla tłumacza obejmował **100%
  tekstów do lokalizacji** w całym `index/localize/{kr,en}` (zarówno `StoryData/`,
  jak i wszystkie 1458 pozostałych plików logicznych), z maksymalnym kontekstem
  z `index/static-data/`.
- **Rozpoznanie pól niefabularnych (1458 plików logicznych: 1401 wspólnych,
  47 tylko w `kr`, 10 tylko w `en`):**
  - łącznie **103 871** niepustych liści tekstowych podlegających lokalizacji
    (`103 476` w obu językach, `299` tylko w `kr`, `96` tylko w `en` — m.in.
    sztandary i bilety z sezonów 5–6 oraz 3 przydomki w `ScenarioModelCodes`);
  - pola nietłumaczone (identyfikatory, kolory hex, assety, kody klasyfikacji
    Anomalii `codeName`, warunki techniczne `usage`, wykonawcy `songWriter`,
    daty `timeline`, puste `undefined = "-"`): potwierdzono **0 różnic** między
    `kr` a `en` w całym korpusie;
  - w `BgmLyrics/*` (6 plików z tagami stylu) `kr` używa arkusza czcionki
    `<style="DKR_…">` / `<style="dkr…">`, natomiast `en` łacińskiego
    `<style="DEN_…">` / `<style="den…">` — narzędzie podaje w `tokeny:` styl
    łaciński z `en` wraz z jawną uwagą dla tłumacza.
- **Grupowanie kontekstowe i deduplikacja:**
  - złączenie identycznych napisów pomiędzy poziomami ulepszeń 1–4 tej samej
    umiejętności (`Skills*`) redukuje 28 832 liści do 21 354 elementów (−7478
    duplikatów ulepszeń) przy zachowaniu pełnej listy adresów JSON w `źródło:`;
  - powtarzalne pola mówców poza `StoryData/` (`RPGSystem/*.speaker`: 5989
    wystąpień → 106 unikalnych mówców; `AbDlg_*.teller`: 169 wystąpień → 23
    unikalnych mówców) trafiają do `mowcy-rpg-i-anomalii.md`, a w dialogach są
    wyświetlane jako etykieta mówcy;
  - uzupełniono również 80 liści tylko-EN (`title`, `teller`, `place`) w
    `StoryData/` w słowniku `mowcy-i-miejsca.md` (1533 pozycje zamiast 1529).
- **Wynik (`plik_dla_tlumacza_v2.zip`):** 11 449 704 B, SHA-256
  `9bb4dcad41ffebf64e3fb6547c894b4d17a4608a27afc2901f38d851551a5006`
  (deterministyczny bit w bit w dwóch niezależnych przebiegach):
  - `sceny.zip`: 68 plików `.md` (max 7998 linii), 1001 scen, 63 010 elementów,
    60 362 do przetłumaczenia + 1533 pozycje słownika mówców/miejsc;
  - `widoki.zip`: 104 pliki `.md` (max 6340 linii, 0 plików w awaryjnym dziale
    `09_pozostale`), 93 069 elementów, 68 148 unikalnych do przetłumaczenia;
  - niezależny audyt round-trip adresów `źródło:` + `słownik:` potwierdza
    pokrycie `103 871 / 103 871` liści JSON (`missing = 0`, `duplicates = 0`).

## E-009 · 2026-11-25 · `import_zwrotki.py`, `build_lang.py` i paczka diagnostyczna `Polski` dla buildu `26652290` (test syntetyczny + test na kopii plików)

- **Cel:** domknąć techniczny rurociąg od zwrotki tłumacza do gotowego archiwum
  `LimbusCompany_Data/Lang/` (D-09: `lang = Polski`, O-01 zamknięte; O-04
  zamknięte) oraz zbudować deterministyczną paczkę diagnostyczną Etapu 3 pod
  test w grze (O-03).
- **Ustalenia podczas walidacji na pełnym korpusie (`157 612` pozycji pakietu):**
  - doprecyzowano wyrażenie regularne znaczników TMP (`TMP_TAG`), aby
    jednoliterowe znaczniki (`<i>`, `<b>`, `<u>`, `<s>`) nie przyjmowały spacji
    po nazwie — eliminuje to fałszywe trafienia na kwestiach Dantego w nawiasach
    `<I …>` (w tym po polsku `<I wtedy…>`);
  - w `<ruby=…>…</ruby>` (np. `StoryData/S830B.json`) odczyt wewnątrz atrybutu
    podlega tłumaczeniu — bramka sprawdza zbalansowanie i niepusty odczyt zamiast
    wymuszać koreański tekst atrybutu;
  - w 27 plikach `StoryData/` (690 wierszy bez pola `id`, m.in. `S202A` oraz 8
    historii Identity `P10210`–`P11110`) oraz 2 plikach ze zduplikowanym `id`
    (`S737B`, `P10916`) poprawiono parowanie `Story.pair()` na `list_row_steps`,
    zachowując w `import_zwrotki.py` pełną zgodność wsteczną z
    `plik_dla_tlumacza_v2.zip` (przebieg kontrolny na archiwum `v2`:
    `169` plików `.md`, `157 612` pozycji, `0` błędów).
- **Wynik (`LCB_TEST_DROGI_Polski_26652290.zip`):**
  - `python3 tools/build_lang.py --probe` → 6 204 533 B, SHA-256
    `b897db11f3c2e2bc57da8e81e0c488397750413d7f1e1b8adcd20ed82bbff292`
    (identyczny bit w bit w dwóch przebiegach);
  - zawartość: `LimbusCompany_Data/Lang/config.json` (`{"lang": "Polski",
    "titleFont": "", "contextFont": ""}`), `2406` plików JSON w
    `LimbusCompany_Data/Lang/Polski/` (`191 140` liści tekstowych z fallbackiem
    EN, `100%` zgodności zbiorów adresów ze źródłem `Localize/en`), `4` pliki ze
    znacznikiem diagnostycznym `ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ` (`10` liści:
    `LoginUIText.json :: switch_allcacheclear`, `MainUIText.json ::
    mainui_main_button1/2`, `StoryData/S001B.json :: id=0`, `Skills.json ::
    id=1010101`), `INSTRUKCJA.txt` oraz `MANIFEST.json`;
  - archiwum wgrano na Dysk właściciela (suma SHA-256 potwierdzona po stronie
    Dysku).
- **Ograniczenia:** to jest wynik testów syntetycznych i walidacji na kopii
  plików gry z buildu `26652290` — rzeczywiste uruchomienie gry po polsku oraz
  poprawność wyświetlania 18 polskich znaków w domyślnej czcionce wymagają
  potwierdzenia przez właściciela w grze (*test w grze*, O-03).

---

### E-010 · 2026-11-25 · Pierwszy test w grze paczki diagnostycznej (`v.1.119.1`) i korekta `Lang/config.json`

- **Rodzaj dowodu:** **test w grze** (dwa zrzuty ekranu od właściciela z wersji
  `v.1.119.1`, build Steam `26652290`) + analiza formatu + **test syntetyczny**
  i **walidacja na kopii plików** dla poprawionej paczki `v2`.
- **Obserwacja z gry (`LCB_TEST_DROGI_Polski_26652290.zip`, v1):**
  - na ekranie tytułowym (`v.1.119.1`, lewy dolny róg) obok przycisku
    `Clear all caches` pojawił się przycisk **`Select Custom Language`**
    (`custom_localize_button` w `LoginUIText.json`), nieobecny w czystej
    instalacji — potwierdza to w 100%, że katalog
    `LimbusCompany_Data/Lang/Polski/` został rozpakowany we właściwe miejsce i
    wykryty przez grę (obala też wcześniejsze założenie, że przycisk pojawia się
    dopiero przy ≥2 językach);
  - mimo obecności 3-kluczowego `LimbusCompany_Data/Lang/config.json`
    (`{"lang": "Polski", "titleFont": "", "contextFont": ""}`) gra przy
    pierwszym uruchomieniu wyświetliła czysto angielskie napisy (`Clear all
    caches`, w lobby `Window` / `Sinners` / `Drive` / `Theater` / `Extract` /
    `Dispense`) bez znaczników `[PL: ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ]`.
- **Diagnoza techniczna:**
  1. W pełnym schemacie `LimbusCompany_Data/Lang/config.json` używanym przez
     grę i aktywne paczki dla `v.1.119.1` (`Limbus-RU-Full`, `LimbusCompanyBusFR`,
     `LocalizeLimbusIT`, `LLC_MOD_Toolbox`, `LLC-update-tool`) występują **5
     kluczy**: `lang`, `titleFont`, `contextFont`, `samplingPointSize` (`78`)
     oraz `padding` (`5`). Pominięcie `samplingPointSize` i `padding` daje w
     deserializacji C# wartość `0` dla parametrów atlasu SDF czcionki TMP.
  2. Zgodnie z oficjalnym komunikatem gry (`LoginUIText.json ::
     custom_localize_desc`: *„※ Restart the game to apply the language change.”*)
     oraz instrukcjami instalacji dla `v.1.119.1`, przy pierwszej instalacji
     wybór języka przyciskiem **`Select Custom Language` → `Polski`** na ekranie
     tytułowym i restart gry aktywuje język na stałe dla kolejnych uruchomień.
  3. Przy okazji wykryto i naprawiono w `_discover_fonts()` (`tools/build_lang.py`)
     wpisywanie ścieżki `Font/Title/<plik>` do `titleFont`/`contextFont` w
     `config.json` — w Limbus Company pola te pozostają pustymi ciągami `""`,
     gdyż silnik sam skanuje `Lang/<lang>/Font/Title/` i `Font/Context/`.
- **Wprowadzone poprawki i wynik walidacji (`v2`):**
  - zaktualizowano `tools/build_lang.py` (pełny 5-kluczowy `Lang/config.json` z
    `samplingPointSize: 78`, `padding: 5`, obsługa slotów `Font/Title` i
    `Font/Context`, poprawiona `INSTRUKCJA.txt` wskazująca lewy dolny róg oraz
    jednorazowy wybór `Select Custom Language` → `Polski` + restart);
  - dodano test syntetyczny `test_optional_font_slots_keep_five_key_config`
    (`58/58` testów zielonych);
  - zbudowano i wgrano na Dysk właściciela `LCB_TEST_DROGI_Polski_26652290_v2.zip`
    (`6 204 710` B, SHA-256 `e63b43c536b75db3d2ee0da1c56d5784922ed4a7a4b97e08bb536013c6537673`,
    suma SHA-256 potwierdzona po stronie Dysku).
- **Ograniczenia:** wykrycie folderu `Lang/Polski/` przez grę jest już
  potwierdzone *testem w grze*, natomiast sprawdzenie wszystkich 18 polskich
  liter (`ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ`) w domyślnej czcionce (zamknięcie O-03) wymaga
  wybrania `Select Custom Language` → `Polski` i restartu gry przez właściciela.

---

### E-011 · 2026-11-25 · Drugi test w grze (`v.1.119.1`): wymagalność `Font/{Context,Title}` i dołączenie niemodyfikowanych czcionek SIL OFL 1.1 (`v3`)

- **Rodzaj dowodu:** **test w grze** (dwa kolejne zrzuty ekranu od właściciela z
  `v.1.119.1`, build Steam `26652290`: ekran tytułowy i lobby po wcześniejszym
  wybraniu `Polski` w `Select Custom Language`) + porównanie 1:1 z aktywnymi
  paczkami `v.1.119.1` + weryfikacja tablic OpenType `cmap` + **test
  syntetyczny** (`59/59`).
- **Obserwacja z gry:**
  - właściciel zgłosił *„Bez zmian. Polski wybrałem wcześniej.”* — mimo że sama
    gra zapisała już wybór `Polski` w `LimbusCompany_Data/Lang/config.json`, przy
    kolejnym uruchomieniu zarówno ekran tytułowy (`Clear all caches`, `Select
    Custom Language`), jak i lobby (`Window`, `Sinners`, `Drive`, `Theater`,
    `Extract`, `Dispense`) pozostały w 100% po angielsku.
- **Diagnoza przyczyny źródłowej (100% pewności):**
  1. Porównanie drzewa naszego `index/localize/en` z działającą na `Ver. 1.119.1`
     paczką `Slavuck/Limbus-RU-Full` wykazało **2406 / 2406 identycznych ścieżek
     plików JSON** (`0` brakujących, `0` nadmiarowych), identyczne kodowanie
     UTF-8 bez BOM oraz identyczny 5-kluczowy `config.json` (`titleFont: ""`,
     `contextFont: ""`, `samplingPointSize: 78`, `padding: 5`).
  2. Sprawdzenie 13 niezależnych paczek Custom Language (`LocalizeLimbusCompany`,
     `LimbusTraditionalMandarin`, `Limbus-RU-Full`, `LimbusCompanyRuMTL`,
     `LimbusCompanyBusRUS`, `Divine-Company`, `RCR`, `LimbusCompanyBusFR`,
     `LocalizeLimbusIT`, `Uniao_LimbusCompanyPT-BR`, `CLT-District_Limbus-Brasil`,
     `LocalizeLimbusTH`, `Echodial`), oficjalnych ogłoszeń Project Moon z
     `2025-03-31` i `2025-04-16` (`1.74.0`) oraz walidatorów instalatorów
     (`KIDJourney/LimbusLLmTranslate`, `lightsing/llc-rs`) wykazało **jedyną
     różnicę**: `LimbusCompany_Data/Lang/<lang>/Font/Context/` (z niepustym
     plikiem `.ttf`/`.otf`) oraz `Font/Title/`. Bez tych katalogów i czcionek
     `CustomLanguageManager` w `v.1.119.1` przerywa inicjalizację własnego
     języka (przypadek rezerwowy przewidziany w [LANG_FORMAT.md](LANG_FORMAT.md):
     *„gdyby brakowało znaków albo gra wymagała pliku”*).
- **Dobór i weryfikacja czcionek (`assets/fonts/`, SIL Open Font License 1.1):**
  - `assets/fonts/Context/Pretendard-Regular.ttf` — oficjalny, w 100%
    niemodyfikowany plik z `orioncactus/pretendard` v1.309 (`2 725 828` B,
    SHA-256 `6d0af5258997aec7354a6e340fc2325ba321c410ca48b3af858c8c3d6e92a324`,
    `14 336` punktów kodowych w `cmap`, `18/18` polskich liter i `8/8` znaków
    polskiej typografii `„”«»–—…•`);
  - `assets/fonts/Title/Mikodacs.otf` — oryginalny, w 100% niemodyfikowany plik
    polskiego projektanta Grzegorza Luka (`gluk`, `glukfonts.pl`), v0.28
    (`110 228` B, SHA-256 `d685ef7fb3b0c88a8c830fb664079d30bacfb5a5dbb0d58d6170f732391b8d30`,
    `910` punktów kodowych w `cmap`, `18/18` polskich liter i `8/8` znaków
    polskiej typografii; brak jakichkolwiek modyfikacji zachowuje pełną zgodność
    z zastrzeżoną nazwą `Mikodacs` w SIL OFL 1.1);
  - pełne teksty licencji (`OFL-Pretendard.txt`, `OFL-Mikodacs.txt`) zapisano w
    `assets/fonts/` oraz w katalogu `LICENCJE_CZCIONEK/` każdego budowanego
    archiwum `.zip`, natomiast do `LimbusCompany_Data/Lang/<lang>/Font/{Context,Title}/`
    trafiają wyłącznie pliki `.ttf`/`.otf`.
- **Zmiany w generatorze i wynik budowy (`v3`):**
  - `tools/build_lang.py` domyślnie czyta `assets/fonts/` i wymaga niepustych
    czcionek `.ttf`/`.otf` w `Font/Title/` i `Font/Context/` (błąd zatrzymuje
    budowę); test `test_repository_ofl_fonts_cover_all_polish_glyphs` sprawdza
    tablice `cmap` obu czcionek w CI (`59/59` testów zielonych);
  - zbudowano i wgrano na Dysk właściciela `LCB_TEST_DROGI_Polski_26652290_v3.zip`
    (`7 430 569` B, SHA-256 `fe359fcd6a6898983a0c7accba8847ba2df7ef836b1c68e5638f0ead3ffb1ff1`).
- **Ograniczenia:** wymóg obecności `Font/{Context,Title}` został potwierdzony
  *testem w grze*, a pokrycie `18/18` polskich znaków zweryfikowano na tablicach
  `cmap`; ostateczne zamknięcie O-03 nastąpi po potwierdzeniu przez właściciela
  uruchomienia i wyglądu znaków w grze na paczce `v3`.

---

### E-012 · 2026-11-25 · Trzeci test w grze (`v.1.119.1`): pełne potwierdzenie end-to-end i 18/18 polskich znaków (`O-03` → `D-10`) + narzędzie aktualizacji `audit_update.py`

- **Rodzaj dowodu:** **test w grze** (zrzut ekranu od właściciela z wersji
  `v.1.119.1`, build Steam `26652290`, po rozpakowaniu
  `LCB_TEST_DROGI_Polski_26652290_v3.zip` z komentarzem *„i teraz działa”*) +
  **test syntetyczny** dla `tools/audit_update.py` (`60/60`).
- **Wynik w grze:**
  - gra wystartowała od razu w wybranym wcześniej języku `Polski` bez żadnych
    dodatkowych czynności;
  - przycisk na ekranie tytułowym wyświetlił napis
    **`Clear all caches [PL: ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ]`** w kroju `Mikodacs`
    Grzegorza Luka — wszystkie **18/18 polskich znaków diakrytycznych** (małych
    i wielkich, w tym ogonki `ą ę Ą Ę`, kreski `ć ń ó ś ź Ć Ń Ó Ś Ź`, `ł Ł` i
    kropka `ż Ż`) wyrenderowało się ostro, bez kwadratów i artefaktów SDF;
  - **obserwacja praktyczna dotycząca limitów długości w UI:** sztucznie
    wydłużony do `42` znaków napis diagnostyczny wyszedł poziomo poza stałą
    ramkę przycisku `switch_allcacheclear` (oryginał EN ma `16` znaków, brak
    auto-zmniejszania czcionki na tym przycisku), co potwierdza w praktyce
    zasadność podawanych w pakiecie limitów długości znaków `limit:` na polach
    interfejsu.
- **Domknięcie Etapu 6 (`tools/audit_update.py`):**
  - dodano `tools/audit_update.py` porównujący dwa snapshoty `Localize` (katalog
    `index/localize` lub archiwum `LCB_DANE_*.zip` ze zbieracza) po stabilnych
    identyfikatorach JSON, raportujący dodane/zmienione/usunięte pliki i liście
    w `kr` i `en`, sprawdzający wpływ łatki na wpisy w `tlumaczenie/`
    (`preserved`, `stale_kr_changed`, `orphaned_removed`) oraz budujący
    deterministyczny pakiet uzupełniający `--delta-out` (z zachowaniem nowych,
    jeszcze nieindeksowanych scen `StoryData/*.json` w `pozostale.md` i
    wstępnym wypełnieniem niezmienionych linii `PL:` jako kontekstu).

---

### E-013 · 2026-11-26 · Czwartkowa aktualizacja gry (`26652290` → `26917622`): import `index/localize` i deterministyczny pakiet przyrostowy (`pakiet_przyrostowy_26652290_do_26917622.zip`)

- **Rodzaj dowodu:** **test na kopii plików z gry właściciela** + **test syntetyczny** (`61/61`).
- **Wejście:** `LCB_DANE_20261126_094359_ef145d.zip` (`19 234 825` B, SHA-256
  `28f53cdbd6bd8b144ff48a5dd84ecd76bbcea5e90bdbf44db24069f005badfa8`; walidacja
  `tools/validate_collector_return.py`: `status = complete`, `problems = 0`,
  `skipped = 0`, `buildid = 26917622`; pliki `Localize`: `2 464` `kr`, `2 421`
  `en`, `2 481` `jp`; zebrany `Lang/config.json` potwierdza aktywny profil
  `{"lang": "Polski", "titleFont": "", "contextFont": "", "samplingPointSize": 78, "padding": 5}`).
- **Audyt różnic między buildem `26652290` a `26917622` (`tools/audit_update.py`):**
  - `kr` (źródło): **+15** nowych plików (`0` usuniętych), **27** zmienionych
    (`2 422` bez zmian); liście tekstowe: **+2 169** nowych, **5** zmienionych,
    **0** usuniętych (`191 140` bez zmian);
  - `en` (odniesienie): **+15** nowych plików (`0` usuniętych), **32** zmienione
    (`2 374` bez zmian); liście tekstowe: **+2 169** nowych, **36** zmienionych,
    **1** usunięty przy podziale identyfikatora w `BattleSpeechBubbleDlg.json`
    (`190 808` bez zmian);
  - zawartość merytoryczna łatki:
    1. **2 nowe Tożsamości 000 + historie + umiejętności + pasywki + kwestie:**
       *Haute Couture:: Le Noir B3F Drying Room* Yi Sang (`10117`, `StoryData/P10117.json`
       — `219` kwestii, `Voice_Yisang_Contem_10117.json`, `Skills_personality-01.json`,
       `Passives.json` `1011701..1011721`) oraz *Haute Couture:: Le Rouge B2F
       Skein Nest* Gregor (`11217`, `StoryData/P11217.json` — `165` kwestii,
       `Voice_Gregor_Contem_11217.json`, `Skills_personality-12.json`,
       `Passives.json` `1121701..1121721`, rozszerzenie `RougeFamilySinclair.desc`);
    2. **nowy komentator bitwy:** `BattleAnnouncerDlg/Announcer_Overseer_60.json`
       (`32` kwestie) + `Announcer.json`;
    3. **nowy tryb wydarzeniowy (`Limtochess` / `SchemaCraft` / `Synergy`):**
       `LimtochessUI.json` (`1 023` pola `kr` / `1 022` `en`),
       `SchemaCraftChoice.json` (`59`), `TutorialMainUIText.json` (`+119`),
       `BattleKeywords-schema.json` (`15`), `Bufs-schema.json` (`15`),
       `BattleKeywords_Synergy.json` (`2`), `Bufs_Synergy.json` (`2`),
       `Enemies-schema.json` (`1`), `PanicInfo-schema.json` (`3`),
       `Passives_Enemy-schema.json` (`30`), `Skills_Enemy-schema.json` (`92`),
       `Passive_Ego.json` (`+6`), `SynergyKeyword.json` (`+1`);
    4. **poprawki i erraty w istniejących plikach:** `5` zmian `KR`
       (`ActionEvents-walpu10.json` ×2, `EGOgift_walpu10.json` `9296.desc`,
       `BattleKeywords.json` `RougeFamilySinclair.desc`, `StageChapterText.json`
       `chapter_n_9128.chaptertitle`) oraz `36` poprawek sformułowań `EN`
       (m.in. `Skills_personality-09.json`, `Skills_Ego_Personality-06.json`,
       `BattleKeywords_Mirror3.json`, `Bufs_Mirror3.json`, `Skills_Enemy-a1c9116.json`).
- **Ulepszenia potoku aktualizacji i wynik budowy pakietu przyrostowego:**
  - `tools/story_index.py` i `tools/package_views.py` uzupełniono o regułę
    prefiksu dla nowych historii `P1xxNN` oraz pasywek `1xxNNyy`, dzięki czemu
    nowe Tożsamości trafiają od razu pod właściwego Grzesznika (`identity-01.md`,
    `identity-12.md`, `02_tozsamosc_01_Yi_Sang.md`, `02_tozsamosc_12_Gregor.md`),
    zanim zewnętrzne lustro `OpenLethe` opublikuje zaktualizowane `StaticData`;
  - `tools/audit_update.py` rozszerzono o `--old-rev <git-rev>` (budowa pakietu
    przyrostowego czysto z historii Git bez polegania na `local/` ani Dysku) oraz
    tryb `--delta-scope items`, emitujący wyłącznie nowe i zmienione sceny,
    wpisy słownika mówców oraz pojedyncze pozycje widoków;
  - `tools/import_zwrotki.py` uzupełniono o jawną flagę `--allow-older-package`
    do bezstratnego przyjmowania zwrotek z wcześniejszego pakietu bazowego
    (`26652290`) po przesunięciu `index/localize` na nowszy build (`169` plików /
    `157 612` pozycji z `26652290` przechodzi suchy przebieg bez błędów);
  - zaimportowano build `26917622` do `index/localize` (`kr` SHA-256
    `54c9f37d…fae6e2`, `en` SHA-256 `d10485fb…ee9c10`), odświeżono
    `wiedza/indeks_fabuly.json` (`186` historii Identity, `0` nowych
    nieprzypisanych) i `czytanki/`, a następnie zbudowano z repozytorium i
    wgrano na Dysk właściciela deterministyczny pakiet przyrostowy
    **`pakiet_przyrostowy_26652290_do_26917622.zip`** (`155 363` B, SHA-256
    `c20f006a1e7cb38a7a21b1b5f5f2307b784d5476527df72f4a0df9ba1953b3df`:
    `2` pliki scen + `3` nowe wpisy słownika mówców + `17` plików widoków =
    łącznie **`1 733`** unikalne puste pola `PL:` do przetłumaczenia; suchy
    przebieg ścisłego `import_zwrotki.py`: `0` błędów, `0` ostrzeżeń).
- **Ograniczenia:** tabele `StaticData` w `index/static-data/` pochodzą nadal z
  `LEAGUE-OF-NINE/OpenLethe` (`8f24cba5`, dane z `2026-11-12`), więc karty `10117`
  i `11217` pojawią się w liczbowych profilach `czytanki/plik_ID_*` po
  opublikowaniu nowego zrzutu `StaticData` w OpenLethe (w pakiecie dla tłumacza
  są już kompletne w 100% z `Localize`).




