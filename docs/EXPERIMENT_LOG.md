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

---

### E-014 · 2026-11-26 · Integracja pierwszej zwrotki tłumacza (`LC_PL1.zip`) i budowa pierwszej produkcyjnej paczki polskiej `LCB_PL_Polski_26917622_v1.zip`

- **Rodzaj dowodu:** **test na rzeczywistej zwrotce tłumacza i danych gry właściciela (`26917622`)** + **test syntetyczny** (`63/63`).
- **Wejście (`LC_PL1.zip`):** `1 692 944` B, SHA-256
  `ae9a4d7ada782d11d190875fba228e70d7ac53fffc9dbf7384fef247807ccb1f` — `19`
  plików Markdown z `plik_dla_tlumacza_v2.zip`:
  - kompletny **Prolog** (`01_prologue_selva_oscura.md`: `395/395`),
    **Canto I** (`02_canto_i_the_outcast.md`: `1 185/1 185`),
    **Canto II** (`03_canto_ii_the_unloving.md`: `1 242/1 242`) oraz
    **Canto III** (`04_canto_iii_the_unconfronting_a.md`: `1 553/1 553` +
    `04_canto_iii_the_unconfronting_b.md`: `107/107`);
  - **36 historii Tożsamości Sezonu 1** w `identity-01.md` … `identity-12.md`
    (`P10102` … `P11204`, łącznie `788` wypełnionych pól `PL:`);
  - słownik `mowcy-i-miejsca.md` (`169` wpisów: `78` `teller`, `37` `title`,
    `38` `place`, `16` `model`);
  - `widoki/07_notatki_dantego_i_teatr.md` (`113` wpisów: karty Teatru
    `StoryTheaterMain.json`, tytuły 36 historii lustrzanych
    `StoryTheaterMirrorWorldStoryTitle.json` + `StoryTheaterPersonality.json`
    oraz Notatki Dantego `StoryTheaterDanteNote*.json` / `StoryTheaterDanteNoteDetail*.json`).
- **Analiza korpusu dla pytania technicznego tłumacza (`//효과연출1`, `//효과연출2`):**
  - przeskanowano wszystkie `1 003` pliki `StoryData/*.json` (`id != -1`) w całym
    korpusie `index/localize/{kr,en}`: wiersze `StoryData/3D309I2.json` `id=56`
    (`"//효과연출1"`) i `id=61` (`"//효과연출2"`) są **jedynymi dwoma wierszami w
    całych `sceny/`** (`id != -1`), w których oficjalne `EN` (podobnie jak łatki
    społeczności `RU` i `FR`) pozostawia tekst koreański / prefiks `//`;
  - są to wewnętrzne znaczniki inscenizacji/VFX w scenie z Demianem i Kromer,
    którym scenarzysta omyłkowo nie nadał `id: -1` (w pozostałych scenach
    Canto III komentarze `//효과음` i `//CG` mają `id: -1`);
  - uzupełniono `tools/import_zwrotki.py` o bramkę chroniącą znaczniki `//…` w
    `StoryData/*` przed przypadkową zmianą treści oraz o ostrzeżenie przy
    niezamierzonych znakach Hangul w `PL:` (gdy `EN` ich nie zawiera), a w
    `tools/build_lang.py` dopięto rzutowanie `ScenarioModelCodes-AutoCreated.json`
    `nickName` ← `story_glossary["title"]` (z weryfikacją `en_sha256`, bez
    fałszywych dopasowań na zamazanych ciągach `■■■`).
- **Wynik importu (`tlumaczenie/`) i budowy paczki produkcyjnej (`dist/LCB_PL_Polski_26917622_v1.zip`):**
  - ścisły `tools/import_zwrotki.py` na buildzie `26917622`: **`0` błędów, `0`
    ostrzeżeń**; `5 552` przetłumaczonych pozycji + `176` odziedziczonych
    powtórzeń → `149` plików w `tlumaczenie/pliki/` (`5 559` adresów) + `169`
    wpisów w `tlumaczenie/slowniki.json` + `379` powiązań w `powtorzenia.json`;
  - deterministyczna paczka produkcyjna **`LCB_PL_Polski_26917622_v1.zip`**:
    `7 491 054` B, SHA-256
    `b335c53abf082a201a15dc4dfbc9f7710df84ee5d559f9f24bdd2ab7e4169e82`
    (`2 421` zweryfikowanych plików JSON, w tym **`469` zmodyfikowanych** i
    **`12 099 / 193 308` (`6,26%`)** przetłumaczonych liści w całej grze przy
    `0` zdezaktualizowanych źródłach i bezpiecznym fallbacku `EN` dla reszty) —
    wgrana na Dysk Google właściciela ze zgodną sumą kontrolną.

## E-015 · 2026-11-26 · Architektura `AI-tymczasowe` (`"origin": "ai"`) i deterministyczny podział 87 paczek UI/meta (`D-11`)

- **Rodzaj:** implementacja i audyt zakresu (testy syntetyczne + klasyfikacja pełnego korpusu buildu Steam `26917622`; bez tłumaczenia do sygnału właściciela).
- **Cel:** przenieść z projektu `wherewindsmeet` architekturę tymczasowego przekładu UI/technikaliów/meta przez agenty Arena (`AI-tymczasowe`) tak, aby:
  1. wpisy agentów i wpisy ludzkiego Tłumacza współistniały w `tlumaczenie/` z jawnym pochodzeniem i pełnym priorytetem Tłumacza,
  2. paczka do gry (`build_lang.py`) zawierała wpisy Tłumacza + AI, natomiast pakiety robocze i przyrostowe dla Tłumacza (`build_package.py --wypelnij-pl`, `audit_update.py --delta-out`) pomijały wpisy AI,
  3. cały materiał UI, techniczny i meta/statystyk został podzielony na bezkolizyjne paczki gotowe do równoległej pracy agentów.
- **Wyniki i liczby (build `26917622`):**
  - **Pochodzenie i bramki (`tools/import_zwrotki.py`, `tools/build_lang.py`, `tools/build_package.py`, `tools/audit_update.py`):**
    - flaga `--ai` oznacza wpisy polem `"origin": "ai"` w `tlumaczenie/pliki/*.json` i `tlumaczenie/slowniki.json`, zliczając osobno `human_addresses` (`5 559`) i `ai_addresses` (`0`) w `tlumaczenie/MANIFEST.json`;
    - import `--ai` nigdy nie nadpisuje wpisów Tłumacza (`skipped_human_existing`), a import zwrotki Tłumacza zawsze zastępuje wpisy AI (`replaced_ai`) i usuwa klucz `"origin"`;
    - `build_lang.py` raportuje osobno `human_leaves` i `ai_leaves` oraz udostępnia `--no-ai`; `build_package.py` obsługuje `--wypelnij-pl` (pomija `"origin": "ai"`) oraz `--tylko-ai` (pakiet weryfikacyjny samych wpisów AI).
  - **Audyt zakresu i podział na 3 Fale (`tools/prepare_ai_batches.py`, `paczki_ai/MANIFEST.json`):**
    - wyłączono `100%` fabuły (`StoryData/*.json`) oraz wszystkie pliki prozatorskie, dialogowe, głosowe i muzyczne poza `StoryData/` (`28 747` elementów w widokach, w tym m.in. `PersonalityVoiceDlg/*`, `EGOVoiceDig/*`, `BattleAnnouncerDlg/*`, `BgmLyrics/*`, `BattleSpeechBubbleDlg*`, `AbnormalityGuides*`, `StoryTheaterDanteNoteDetail*`, `IntroduceCharacter.description`, `AbEvents*`/`AbDlg*`/`ActionEvents*`, `rpg-loc-dialogue*`/`rpg-loc-narration*`, a także `293` nieprzetłumaczone robocze napisy KR w EN);
    - zakwalifikowano **`47 376` unikalnych slotów `PL:`** UI/technikaliów/meta (`72` już przetłumaczone przez człowieka w `LC_PL1.zip`, **`47 304` do wykonania**) i podzielono je deterministycznie na **`87` paczek (`P01`–`P87`)**:
      - **Fala 1 (`P01`–`P14`, `14` paczek, `7 219` pozostałych slotów):** fundament bojowy (`1A`), interfejs główny i ustawienia z `kr_settings-ui-donttranslate.json` (`1B`), tryby/etapy/Lochy/Teatr UI (`1C`), samouczki i wskazówki (`1D`);
      - **Fala 2 (`P15`–`P42`, `28` paczek, `14 994` slotów):** `BattleKeywords*` i `Bufs*` (`2A`), przedmioty/sklep/Przepustka/wydarzenia UI (`2B`), modele postaci + UI/zadania/przedmioty RPG Canto X (`2C`);
      - **Fala 3 (`P43`–`P87`, `45` paczek, `25 091` slotów):** komplet kart każdego z 12 Grzeszników po 1 paczce na postać + wspólne (`3A`), Dary E.G.O i karty/skille E.G.O (`3B`), statystyki i umiejętności wrogów/Anomalii/wsparcia (`3C`).
  - **Słownik terminów (`paczki_ai/SLOWNIK_TERMINOW.md`):** utrwalono kanoniczne terminy i odmianę imion 12 Grzeszników z `LC_PL1.zip` oraz konwencje bojowe dla Fal 1–3.

### E-016 · 2026-11-27 · Integracja drugiej zwrotki tłumacza (`LC_PL2.zip`) — priorytet Tłumacza nad AI (`replaced_ai: 696`) — i produkcyjna paczka `LCB_PL_Polski_26917622_v2.zip`

- **Rodzaj dowodu:** **test na rzeczywistej zwrotce tłumacza** (`1` błąd ścisłej bramki rozstrzygnięty `--allow-older-package` z `1` ostrzeżeniem) + pełne testy (`64/64`).
- **Wejście (`LC_PL2.zip`):** `1 968 062` B, SHA-256
  `b2f41e61d69b40a78f3f8a3ed143f9d993686f6f824d800d00f36a5beb6fed05` — `24`
  plików Markdown (nowość względem `LC_PL1`: **Intervallo I „Hell's Chicken”**,
  opowiadanie Notatek Dantego, widoki „Rozdziały, etapy i zdolności Dantego”
  a+b oraz „Interfejs główny i ustawienia” a). Zgodnie z polityką `D-12`
  treść MD obu zwrotek jest teraz w repozytorium:
  `zwrotki/tlumacz/LC_PL1/` i `zwrotki/tlumacz/LC_PL2/` (+ `import_report.json`).
- **Bramka zmienionego źródła (element `1110`):** ścisły import odrzucił
  `07_rozdzialy_etapy_i_zdolnosci_dantego_a.md` element `1110`:
  `StageChapterText.json :: dataList[id=chapter_n_9128].chaptertitle` — w danych
  gry wiersz rozdziału `chapter_n_9128` (korporacja N사/N Corp., `14구`, 10장)
  został podmieniony z tytułu dziesiątej Walpurgii (`제 10 회 발푸르기스의 밤` /
  `The 10th Walpurgis Night`) na tytuł **Canto X** (`바라보아지는` /
  `The Gaze Bearing`). PL Tłumacza „Dziesiąta Noc Walpurgii” przestał pasować do
  źródła — element **pominięty z ostrzeżeniem** (`--allow-older-package`),
  wróci w pakiecie przyrostowym dla Tłumacza z nowym źródłem.
- **Wynik importu (`tlumaczenie/`):** `24` plików, `22 989` elementów:
  **przetłumaczono `6 802`**, odziedziczono powtórzeń `402`, zaktualizowano
  adresów `7 007`, **nadpisano wpisów AI (`replaced_ai`): `696`**,
  `skipped_human_existing: 0`, słownik mówców/miejsc: `197` pozycji,
  `1` ostrzeżenie, `0` błędów. `tlumaczenie/MANIFEST.json`:
  `human_addresses` `5 559` → **`7 147`**, `ai_addresses` `43 358` → **`42 662`**
  (suma `49 809` adresów), `story_glossary_entries` `169` → `197`.
  Nowe pliki wynikowe: `StoryData/E01xx–E3xx` (Intervallo I), `EGOgift_StoryDungeon*`,
  `StoryTheaterDanteNoteDetail_4`, `MainUIText`, `StageNode*`/`DungeonNode*`/`DungeonArea1-*`,
  `FileDownloadDesc` i in. (łącznie `42` plików zmienionych/nowych).
  *Dopełnienie sesyjne:* 3 pliki wynikowe importu AI z P59
  (`EGOgift_MirrorDungeon_2/6/7.json`, `296` adresów `origin: "ai"`) dodane do
  Git poza kolejnością checkpointa.
- **Wynik budowy paczki produkcyjnej (`dist/LCB_PL_Polski_26917622_v2.zip`):**
  `7 566 960` B, SHA-256
  `4af4f29c01b47981933c721159b8fe567ad8eb04c48492dccb0955f8cc2501b8`
  (`2 422` plików JSON, w tym **`1 130` zmodyfikowanych**,
  **`57 071 / 193 309` = `29,52%`** przetłumaczonych liści w całej grze —
  Tłumacz + AI, `0` zdezaktualizowanych źródeł, fallback EN dla reszty) —
  wgrana na Dysk Google właściciela ze zgodną sumą kontrolną.



### E-017 · 2026-11-27 · Paczka produkcyjna v3 (`LCB_PL_Polski_26917622_v3.zip` — AI do P64) i Czytanki PL (fallback EN)

- **Paczka produkcyjna (`dist/LCB_PL_Polski_26917622_v3.zip`):**
  `7 574 690` B, SHA-256
  `af7087402f9c8c3ae46e166e99622bdb76a3543a6dc35a06c66e9a9b3eaf21a0` —
  `2 422` plików JSON (`1 161` zmodyfikowanych), **`62 476 / 193 309` = `32,32%`**
  przetłumaczonych liści (v2: 29,52%) — Tłumacz (LC_PL1+LC_PL2) + AI (P01–P64),
  `0` znaczników diagnostycznych, fallback EN dla reszty.
- **Nowa seria Czytanek E.G.O (`tools/build_ego.py` → `czytanki/plik_EGO_PL`, 12 plików):**
  łączy `StaticData` (`skill/ego-skill-*` z `skillType` `EGO_AWAKEN`/`EGO_EROSION`,
  `passive/passive-ego` wymagania) z `Localize` (`Egos`/`Skills_Ego`/`Passive_Ego`,
  głosy `EGOVoiceDig`). Układ plików ID (E-00x): katalog kart, per karta
  Przebudzenie/Erozja/wariant sezonowy z tabelą per Uptie i opisami monet,
  pasywka z wymaganiami, kwestie E.G.O. Identyfikator Grzesznika = cyfry 2–3
  id karty (`20101` → 1, `21201` → 12); warianty sezonowe (np. `2010112`
  z `ego-skill-a1c9p3`) etykietowane „Wariant”. Gra dopisuje adnotacje po
  tokenach („[Motyl]” z dopiskiem „Żyjącego”) — generator łamie sąsiedztwo
  nawiasu kwadratowego z okrągłym (znaki `]` i `(` obok siebie),
  by checker dokumentacji nie czytał tego jako linku.
- **Czytanki PL (fallback EN):** `czytanki/fabula_PL` (36 rozdziałów),
  `czytanki/plik_ID_PL`, `czytanki/plik_EGO_PL` — wejście: produkcyjna
  `Lang/Polski` (fallback EN wbudowany per wpis) jako katalog snapshotu
  `pl/` + `en/` dla nazw plików i detekcji nieprzetłumaczonych scen.
  Czytanka fabularna liczy sceny bez przekładu (porównanie tabel PL↔EN,
  np. Canto X: 57/65 scen w oryginale); `tools/build_reading.py` dostaje
  wersję „polską” w nocie, `tools/build_profiles.py` — dopisek o fallbacku.
  Snapshot `local/cz_snapshot/` i `local/lang_pl_v3/` regenerowalne,
  zignorowane w `.gitignore` (test polityki zaktualizowany razem, 65/65).
- **Dostawa na Dysk Google (folder kanału):** paczka produkcyjna
  `LCB_PL_Polski_26917622_v3.zip` (`1C8LtGyPaKaJ_BdK5bJ7CkAGZWDmrJtGt`,
  `7 574 690` B) oraz Czytanki PL `LCB_Czytanki_PL_2026-11-27.zip`
  (`1RVUhsYgyv2Hs6hwqliS8JwAZOXzusKzs`, `2 115 411` B, 61 plików MD:
  fabula_PL + plik_ID_PL + plik_EGO_PL).

### E-018 · 2026-11-27 · Formatowanie Czytanek: tabele wyrównane w pionie (konwencja mtgcrawler) i usunięcie technicznych znaczników scen (uwagi właściciela)

Właściciel zgłosił dwie uwagi do wydania Czytanek: (1) tabele mają być
składane jak w wydaniach SRW (repo `mtgcrawler`) — kolumny `|` wyrównane
w pionie w edytorze o stałej szerokości znaków, kolumny liczbowe
prawostronnie przez `---:` — a nie jako gołe wiersze `|---|---|`;
(2) z Czytanek fabuły mają zniknąć czysto techniczne znaczniki scen
(`<!-- S001B -->`).

- **`tools/md_table_align.py` (nowy, port z `srw-oe-translation/tools/`):**
  formatter tabel Markdown „monospace-exact” — wyrównanie kolumn w pionie
  (nagłówek/separator/wiersze), budżet szerokości linii 216 komórek,
  długa ostatnia kolumna zawijana z wcięciem kontynuacji, `<br>` nigdy
  nie trafia do czystego tekstu, CJK (`unicodedata.east_asian_width`)
  liczone jako 2 komórki; CLI do poprawki plików w miejscu. Genery
  (`build_reading.py`, `build_profiles.py`, `build_ego.py`) wywołują
  `align_markdown_tables` przed zapisem; separatory liczbowe
  (`---:`) ustawione dla `#`/`Sceny`/`Kwestie` (spis), `Ulepszenie`/
  moce/monety/cele (tabele skilli), `Rzadkość`/`Sezon` (katalog Identity).
- **Znaczniki scen:** `build_reading.py` nie emituje `<!-- SXXX -->`;
  rolę separatora scen przejmuje czysta linia przerwy (granice wyznaczają
  nagłówki etapów i dopiski faz). Z wydania usunięto 2408 znaczników.
  Test `test_reading_layout` kotwiczy zakaz `<!--` (test zaktualizowany
  razem ze zmianą układu).
- **Regeneracja:** wszystkie 7 serii zbudowane z generatorów
  (EN/KR z `index/`, PL ze snapshotu `local/cz_snapshot`); 159 plików,
  diff zawiera wyłącznie usunięte znaczniki i przeformatowane tabele
  (0 niezamierzonych zmian), ponowne przejście alignera = operacja
  tożsamościowa (159/159). Testy: 69/69 (nowe 4 w
  `tests/test_md_table_align.py`, port z mtgcrawler + idempotencja).
- **Dostawa:** paczka `LCB_Czytanki_PL_2026-11-27.zip` odświeżona na
  Dysku Google (`1Fz9csdM4jhg1TAOIUNastxaP_yKAqrdh`, `2 125 507` B,
  61 plików MD; wcześniejsza wersja `1RVUhsYgyv2Hs6hwqliS8JwAZOXzusKzs`
  z E-017 przeniesiona do kosza).

### E-019 · 2026-11-27 · Integracja trzeciej zwrotki tłumacza (`LC_PL3.zip`) — akta Grzeszników (#1–#12)

- **Wejście (`LC_PL3.zip`):** `2 871 898` B, SHA-256
  `cd1ae6b6b8e733497b3bf2fafc3681808a2411cff9ddfce336a3d97ec81f2b69` — `36`
  plików Markdown: `24` plików identycznych z `LC_PL2` (porównanie bajtowe)
  plus `12` **nowych** widoków `02_tozsamosc_01..12_<Grzesznik>_a.md`
  (karty Tożsamości Grzeszników #1–#12 z aktami więźnia). Do integracji
  wzięto wyłącznie deltę (`12` plików → `zwrotki/tlumacz/LC_PL3/PL/widoki/`,
  polityka `D-12`, wraz z `import_report.json`).
- **Wynik importu (`tlumaczenie/`, tryb Tłumacza, bez `--ai`):** `12` plików,
  `12 954` elementów: **przetłumaczono `12`**, odziedziczono powtórzeń `0`,
  zaktualizowano adresów `12`, bez przekładu `8 398` (karty Tożsamości
  pozostają niezapełnione w zwrotce — do osobnej dostawy), `replaced_ai: 0`,
  `skipped_human_existing: 0`, `0` ostrzeżeń, `0` błędów. Nowe wpisy PL =
  **akta (bio) wszystkich 12 Grzeszników** (`IntroduceCharacter.json ::
  dataList[id=<한글>].description`); `tlumaczenie/MANIFEST.json`:
  `human_addresses` `7 147` → **`7 159`**, `translated_addresses`
  `58 750` → **`58 762`**.

### E-020 · 2026-11-27 · Czwarta seria Czytanek „plik META" (`tools/build_meta.py` → `czytanki/plik_META_PL`) i paczka produkcyjna v4 (`LCB_PL_Polski_26917622_v4.zip`)

- **Zakres serii (prośba właściciela: elementy spoza trzech dotychczasowych
  grup):** (1) teksty tutoriali bojowych z misji — `TutorialRenewalDesc`
  (`198` tekstów) pogrupowane po etapach (`Etap 0-1 · Pantera, Lew i Wilk` …
  `Etap 2-12`; dekodowanie `tuto_<CH>_<ST>_*` → węzeł `StageNode`
  `10000+CH·100+ST`, `stage_label`) plus fragment `TutorialRenewalMainUIDesc`
  (`tuto_10108` = Etap 1-8); (2) Notatki Dantego — `100` haseł
  (`StoryTheaterDanteNote*`) i `177` pełnych wpisów „Zapiski"
  (`StoryTheaterDanteNoteDetail*`; `44` PL, `133` w oryginale EN — wpisane bez
  przekładu, jak konwencja fabuły); (3) splashe pobierania patcha
  (`FileDownloadDesc`, `9` ekranów Miasto/Gniazda/Skrzydła/…); (4) akta
  Grzeszników #1–#12 (`IntroduceCharacter` + imiona z `Characters`) z
  tłumaczeń E-019. Dodatkowo w pliku 01: poradniki poza misjami
  (`tuto_exp_mining`, `tuto_lobby_at_start`, `tuto_mirror_dungeon`,
  `tuto_personality_ego_info`), wskazówki w walce (`BattleHint*`, `46`) i
  pop-upy tutoriali (`TutorialPopUpDesc`). Poza zakresem (odnotowane w spisie):
  `TutorialMainUIText` (1 474 tekstów interfejsu), `TutorialMirrorDungeon`
  (575), starsze `TutorialDesc*` (167) — poprzednia wersja tutoriali,
  nadpisana przez zestawy Renewal.
- **Narzędzia:** `tools/build_meta.py` (5 plików + spis z tabelą liczbową
  `| ---: |`, wyrównanie `align_markdown_tables`, nagłówki etapów z `StageNode`
  i `stage_label`, źródła w nagłówkach; PL/EN etykiety) oraz
  `tests/test_build_meta.py` (`7` testów na syntetycznym snapshocie:
  grupowanie po misjach, łączenie `10108` z etapem 1-8, usuwanie markupu
  `<color>`, twarde łamania linii, pary title/desc, kolejność Grzeszników,
  puste źródła → brak pliku). Testy: **76/76**.
- **Seria PL:** `5` plików (`00_spis` + 4 grupy, `450` wpisów razem:
  `252` misje/hints/pop-upy, `277` Notatki, `9` splashe, `12` akta).
  Przebudowane serie istniejące: `plik_ID_PL` (12 plików — akta Grzeszników
  po polsku zamiast fallbacku EN, po E-019), `fabula_PL`/`plik_EGO_PL`
  bez zmian.
- **Paczka produkcyjna (`dist/LCB_PL_Polski_26917622_v4.zip`):**
  `7 581 096` B, SHA-256
  `b770b5058a8f07d02aa596070e9599fc92ea376cf4e5fe74edffaf373b43d508` —
  `2 422` plików JSON (`1 211` zmodyfikowanych), **`66 024 / 193 309` =
  `34,16%`** przetłumaczonych liści (v3: 32,32%) — Tłumacz
  (LC_PL1+LC_PL2+LC_PL3) + AI (P01–P68), `0` znaczników diagnostycznych.
- **Dostawa na Dysk Google (folder kanału):** paczka
  `LCB_PL_Polski_26917622_v4.zip` (`1oAwOD_r6cKf-GjXx7Fh5mbdbgUqPPABr`,
  `7 581 096` B) oraz Czytanki `LCB_Czytanki_PL_2026-11-27_v2.zip`
  (`1-6eX0Uy6U_tGT4C8vHAknZyRjshifjaC`, `2 205 379` B, `65` plików MD;
  SHA-256 `463a0a4740d2db86aa3240d73fc99f22f81795999acb15b3e8e781cc03daae10`).
  Poprzednie wersje przeniesione do kosza: paczka v3
  (`1C8LtGyPaKaJ_BdK5bJ7CkAGZWDmrJtGt`) i Czytanki z E-018
  (`1Fz9csdM4jhg1TAOIUNastxaP_yKAqrdh`).

## E-021 · 2026-11-28 · Patch v5, deploymenty misji i piosenki w Czytankach (fakt z pomiaru)

- **Zadania właściciela:** (1) nowy patch PL z magazynu tłumaczenia → Dysk;
  (2) nowe pliki w dziale `plik_META_PL` — piosenki + deployment misji
  (przeciwnicy ze statystykami); (3) nowe Czytanki → Dysk.
- **Nowe tabele StaticData (import_data.py, `STATIC_TABLES` +3):** `enemy`
  (42 pliki), `abnormality-unit` (68), `abnormality-part` (67) — lustro
  `LEAGUE-OF-NINE/OpenLethe` @ `8f24cba5` (ten sam commit co reszta indeksu;
  nowszy commit danych `281f0bf9` tylko dodaje pliki — nie mieszać).
  `index/MANIFEST.json` bez zmiany `zrodlo`, 3 nowe tabele z SHA-256.
- **PRIORYTET-1 + P84-REDO w paczce:** nazwy wrogów/skilli (1878 liści) i
  piosenka Prologu (`BgmLyrics_Pv`) weszły do patcha v5.
- **`tools/build_deployments.py` (nowy):** plik `06_deployment_<LANG>.md` —
  per część etapów (70 rodzin z tabel `enemy`/`abnormality-unit`, poza
  `mirrordungeon*`/`schema-craft`/`shadowenemy`): lista etapów (`StageNode`)
  i pula przeciwników; **406 jednostek** (wrogowie + Anomalie z częściami),
  **5134 sekcji** (statystyki/umiejętności/pasywki), **172 etapów** ze znanymi
  falami (`battle-ab` → `waveList`). Statystyki: poziom, HP (+/poziom),
  szybkość, sloty akcji, progi oszołomienia, odporności (atak ×2/×1,5/… i 9
  typów obrażeń), umiejętności (grzech/typ/moc bazowa/moc monety/monety/cele —
  sin z `AttributeText`, typy z `BattleUIText`, konwencje renderu z
  `build_profiles`), pasywki z opisami; PL z fallbackiem EN (liczba bez
  przekładu podana w „Zakresie"). Odporność ×1 pomijana (notacja „wszystkie ×1").
- **`tools/build_meta.py`:** dołożone pliki `05_piosenki_<LANG>.md`
  (17 piosenek `BgmLyrics`, **662 wierszy**; Pv przetłumaczona, pozostałe EN z
  adnotacją) i `06_deployment` (wrapper na `build_deployments_file`); spis serii
  (7 plików) aktualizowany automatycznie. Lekcja przy okazji: `edit_file`
  zapisuje teksty literalnie — sekwencje `"\n"` w nowych stringach sprawdzić
  w zbudowanym pliku (`cat -A`), zanim odda się wydanie.
- **Czytanki PL przebudowane** z `local/cz_snapshot` (paczka v5 rozpakowana →
  `Lang/Polski`): `fabula_PL` 37, `plik_ID_PL` 12, `plik_EGO_PL` 12,
  `plik_META_PL` 7 — razem **68 plików MD**.
- **Patch v5 (`dist/LCB_PL_Polski_26917622.zip`):** `7 607 934` B, SHA-256
  `b658c6d3f6d94e92e52b051429e7c56dbcbd1304382be56502edb45f0a601f57`,
  `2 422` plików JSON (`1 420` zmodyfikowanych), **`85 391 / 193 309` =
  `44,17%`** przetłumaczonych liści (v4: 34,16%), `0` znaczników diagnostycznych.
- **Dostawa na Dysk Google (folder kanału):** paczka
  `LCB_PL_Polski_26917622_v5.zip` (`1y6cvYlnA_peim__XTGh28R-KSs-qUEkn`) i
  Czytanki `LCB_Czytanki_PL_2026-11-28_v3.zip`
  (`1AcF5S8ttUPWih0qSZx6L1497Iu9d2FbV`, `2 444 164` B, SHA-256
  `b1dd9e6a8feec01ac53acd73da010ca695f81d23ac77af07eb4d99ce7e9a106f`).
  Poprzednie wersje przeniesione do kosza (odzyskiwalne): paczka v4
  (`1oAwOD_r6cKf-GjXx7Fh5mbdbgUqPPABr`) i Czytanki v2
  (`1-6eX0Uy6U_tGT4C8vHAknZyRjshifjaC`).
- **Testy:** `76/76` po importach i przebudowach. `docs/CZYTANKI.md`
  (seria META: 7 plików + opisy 05/06) i `docs/STATUS.md` (odnośnik do v5)
  zaktualizowane.

- **Poprawka tej samej sesji (reagując na trudność z nawigacją pliku
  `06_deployment`):** generator przepisany na układ dwusekcyjny. Sekcja
  **„1. Etapy i ich przeciwnicy”** (na początku pliku): **482 etapy** w
  kolejności gry z dokładnymi falami — źródło `battle-story` (457 stage'ów
  z `waveList`, w tym `stage_Tutorial` = Prolog 0-1…0-4), uzupełniająco
  `battle-ab` (172; 85 kolizji z battle-story — walka fabularna wygrywa).
  Sekcja „2. Szczegóły przeciwników” bez zmian (1044 jednostek). Famy z
  plików `StageNode*` rozplątane: `StageNode1-N` = **Canto N** (nie „część
  Canto 1”), `StageNode1-0` = Prolog, `StageNode91-N` = Intervallo 910N;
  chronologia: Canto N → 91-N → Canto N+1. Nazwy jednostek: pole `nameID`
  (787 wrogów/anomalii + 321 enemy rows) → wpis lokalizacji o tym id
  (np. 1131 → 90185 „Heishou Pack - Mao: Featherstriker”); bez nazwy zostało
  6 jednostek (bestie Prologu 99001–99003 Lion/Wolf/Panther — tytuł etapu
  „Pantera, Lew i Wilk” to potwierdza — i 3 podobne). Instrukcja obsługi
  pliku w jego nagłówku („Jak czytać ten plik”). Testy 76/76.
