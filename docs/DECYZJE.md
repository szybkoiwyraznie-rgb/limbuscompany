# Decyzje

Każda decyzja ma numer, datę, uzasadnienie i ewentualne warunki rewizji.
Decyzji podjętych **nie** przedstawiamy właścicielowi ponownie, chyba że
zmieniły się fakty (wtedy nowy wpis odwołuje stary).

## Podjęte

### D-01 · 2026-11-25 · Pliki gry dostarcza zbieracz, nie ręczny upload katalogu

Pliki tekstowe Limbus Company są małe (spodziewane ~35–40 MB dla jednego
języka), więc dało się je wrzucić ręcznie na Dysk, jak w SRW OE. Wybrano jednak
zbieracz (wzorzec WWM), bo:

- właściciel nie musi szukać folderu gry ani wiedzieć, które pliki są potrzebne;
- zbieracz odczytuje **build Steam** (`appmanifest_1973530.acf`) — bez tego nie
  da się powiązać tekstu z wersją gry ani wykryć aktualizacji;
- kopie są weryfikowane SHA-256, a inwentarz (`INWENTARZ.jsonl`) pokazuje, co
  jeszcze jest w instalacji, bez przesyłania tego;
- ten sam `URUCHOM.bat` służy co tydzień po aktualizacji gry (nowy ZIP, stary
  zostaje).

Ręczny upload folderu `Localize` na Dysk pozostaje **awaryjnym wyjściem**, gdy
zbieracz nie działa. Wtedy agent zapisuje w `EXPERIMENT_LOG.md`, że brak buildu
i hashy źródłowych.

### D-02 · 2026-11-25 · Wyciąg tekstów jest wersjonowany w `index/`

Jak w WWM i SRW: teksty potrzebne do budowania pakietów, paczki `Lang/` i
Czytanek są w Git (z manifestem źródła). Pozwala to budować bez
dostępu do Dysku i robić diffy między wersjami gry. Szczegóły i granice:
[DATA_POLICY.md](DATA_POLICY.md). Wykonanie (E-006): pliki JSON gry bajt w
bajt, bez normalizacji — [INDEX_FORMAT.md](INDEX_FORMAT.md).

### D-03 · 2026-11-25 · ~~Przekład z angielskiego~~ — ZASTĄPIONA przez D-05

Angielski jest językiem, z którego pracuje tłumacz. Oryginał koreański (`kr`) i
japoński (`jp`) zbieramy, bo pomagają rozstrzygać niejasności (płeć, ton, gry
słów); Pakiety mogą je dołączać jako informację, nie jako tekst do przekładu.
Rewizja, jeśli tłumacz zna koreański i woli pracować z oryginału.

### D-04 · 2026-11-25 · Tylko oficjalny Custom Language

Żadnych modyfikacji bundli Unity, pliku wykonywalnego ani loaderów modów.
Uzasadnienie: oficjalne wsparcie od wersji 1.73.0, brak ryzyka bana zgłaszany
przez społeczność, odinstalowanie przez usunięcie folderu. Teksty, których ten
mechanizm nie obejmuje (np. wpisane w grafiki), są poza zakresem i trafiają do
listy ograniczeń. [FEASIBILITY.md](FEASIBILITY.md).

### D-05 · 2026-11-25 · Przekład z koreańskiego; angielski jako odniesienie

Kierunek wskazany przez właściciela: Limbus Company jest napisane po
koreańsku, a angielski to już przekład. Tłumaczenie z angielskiego byłoby
„pochodną pochodnej”: przenosiłoby jego skróty, wybory i błędy. Dlatego:

- **Źródłem jest `kr`.** To z niego tłumacz robi przekład. Import sprawdza, że
  linia `KR:` w zwrotce się nie zmieniła; klucz przekładu to SHA-256 tekstu
  koreańskiego.
- **`en` to odniesienie (benchmark):** widoczne przy każdym elemencie. Pomaga
  przy ustalonej terminologii znanej graczom (słowa kluczowe, nazwy statusów),
  przy szacowaniu długości tekstu w interfejsie (polski jest bliższy długością
  angielskiemu niż zwięzłemu koreańskiemu) i jako druga opinia przy
  niejasnościach.
- **`jp`:** opcjonalnie do wglądu (również przekład z koreańskiego).
- **Tokeny i znaczniki** bierzemy z `kr` i porównujemy z `en`; różnice trafiają
  do raportu (mogą oznaczać różnice w lokalizacji, a nie błąd).
- **Słowniczek** ma kolumny KR | oficjalne EN | PL. Nazwy własne
  (Sinnerzy, Miasto) w transkrypcji ustala właściciel z tłumaczem;
  domyślnie oficjalna pisownia angielska, bo tę znają gracze.
- Paczka `Lang/` i fallback dla nieprzetłumaczonych tekstów: bez zmian (tekst
  angielski, który gracz w Polsce zrozumie), z wpisem w raporcie pokrycia.

**Potwierdzone 2026-11-25:** tłumacz czyta po koreańsku (O-05 = tak). Pakiet
fabularny ma koreański w linii elementu i `EN:` jako odniesienie
([PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md)).

### D-06 · 2026-11-25 · Teksty gry w repozytorium (JSON/MD), binaria nigdy

Odpowiedzi właściciela na O-07 i O-06 (poprawka tego samego dnia — pierwsza
wersja tej decyzji błędnie trzymała teksty poza repo):

- Wolno pracować na plikach gry i publicznych lustrach (TW `story-data`,
  OpenLethe `StaticData`, także binaria) w piaskownicy — swobodnie.
- **Teksty gry są w repozytorium** jako JSON/MD, jak w WWM i SRW:
  `index/localize/{kr,en}` (pliki Localize bajt w bajt), `index/static-data/`
  (potrzebne tabele) z `index/MANIFEST.json`, wygenerowane `czytanki/`.
  Opis: [INDEX_FORMAT.md](INDEX_FORMAT.md), zasady: [DATA_POLICY.md](DATA_POLICY.md).
- **Binaria gry nigdy nie trafiają do repozytorium** (bundle, `*.assets`,
  pliki wykonywalne, archiwa, czcionki gry); pilnuje tego `.gitignore` i
  `tools/check_repository.py`.
- Repozytorium zostaje publiczne.
- Źródło jest zapisane w manifeście. Obecnie są to lustra o nieznanym buildzie
  Steam; po paczce zbieracza właściciela (`LCB_DANE_*.zip`) podmieniamy
  `index/` jednym poleceniem (`tools/import_data.py`), a `git diff` pokaże
  różnice. OpenLethe nie ma pliku licencji — w manifeście jest to zaznaczone.

### D-07 · 2026-11-25 · Pakiet i Czytanki w układzie SRW, z maksimum kontekstu

Polecenie właściciela:

- **Pakiet dla tłumacza** wzorowany na SRW Y: README + `sceny.zip`, element
  `N. [Dialog - mówca] źródło` / `limit:` / `tokeny:` / `EN:` / `PL:`, nagłówek
  sceny z kontekstem (rozdział, etap, miejsce, moment walki, sąsiednie sceny,
  uczestnicy), spisy rozdziałów i scen, mówcy/miejsca tłumaczone raz.
- **Czytanka** w „ludzkim” układzie: dokładna chronologia, nazwy Canto i etapów
  we właściwych miejscach, mówcy jak w SRW (`**Imię:** tekst`), bez
  identyfikatorów w tekście. Poprawki właściciela z 2026-11-25 po lekturze
  próbki: pojedynczy `\n` między kwestiami w scenie (bez pustych linii między
  wierszami dialogu), kwestie Dantego bez nawiasów `<…>` / `\<…>`, `"Me"` →
  `"Ja"`, ciągi `■…` (cenzura / zaniki pamięci z gry) → `***`.
- **Plik ID** (profile Identity): co naprawdę jest w danej Identity —
  statystyki, umiejętności, pasywki, opisy i kwestie w czytelnej formie.

Szczegóły: [PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md), [CZYTANKI.md](CZYTANKI.md).

### D-08 · 2026-11-25 · Jeden kompletny pakiet dla tłumacza obejmujący 100% gry

Polecenie właściciela (zamyka O-02): pakiet dla tłumacza zawiera **wszystkie
teksty gry do przetłumaczenia** naraz, nie tylko fabułę — tj. `sceny.zip` (całe
`StoryData/`) oraz `widoki.zip` (wszystkie pozostałe 1458 plików `Localize`:
słownik bojowy, karty i kwestie Tożsamości połączone ze statystykami per
Grzesznik, E.G.O i Dary E.G.O, Anomalie, wydarzenia i wrogowie, komentatorzy,
piosenki, tryb RPG z Canto X, Notatki Dantego, Teatr, Lochy, UI, samouczki,
wydarzenia sezonowe i sklep) z maksymalnym zachowaniem kontekstu z danych gry.
Tłumacz sam wybiera kolejność i tempo pracy, odsyłając dowolne partie plików
`.md` (zalecany start w `README.md`: słownik bojowy i słowniki mówców).

### D-09 · 2026-11-25 · Nazwa języka `Polski` i konfiguracja `Lang/config.json`

Polecenie właściciela (zamyka O-01) oraz uściślenie po pierwszym teście w grze
(`E-010`, `v.1.119.1`):

- Nazwa katalogu i wartość klucza `"lang"` w `LimbusCompany_Data/Lang/config.json`
  to **`Polski`** (`LimbusCompany_Data/Lang/Polski/`).
- Nazwa składa się wyłącznie ze znaków ASCII (brak ryzyka problemów ze
  ścieżkami w Windows/Unity) i nie koliduje z cudzą paczką `Polish`.
- Archiwum wynikowe (`tools/build_lang.py`) dostarcza pełny 5-kluczowy plik
  `LimbusCompany_Data/Lang/config.json` (`"lang": "Polski"`, `"titleFont": ""`,
  `"contextFont": ""`, `"samplingPointSize": 78`, `"padding": 5`).
- Pierwszy test w grze (`E-010`) potwierdził, że przycisk **`Select Custom
  Language`** na ekranie startowym (lewy dolny róg, obok `Clear all caches`)
  pojawia się już przy jednym zainstalowanym języku i potwierdza poprawne
  wykrycie katalogu `Lang/Polski/`. Jeśli przy pierwszej instalacji gra otworzy
  się po angielsku, jednorazowe kliknięcie `Select Custom Language` → `Polski`
  i restart gry aktywuje język na stałe dla wszystkich kolejnych uruchomień.

### D-10 · 2026-11-25 · Niemodyfikowane czcionki SIL OFL 1.1 (`Pretendard-Regular.ttf` + `Mikodacs.otf`) w `assets/fonts/`

Trzy kolejne testy w grze (`v.1.119.1`, build Steam `26652290` — `E-010`,
`E-011`, `E-012`) rozstrzygnęły i zamknęły **O-03**:

- W Limbus Company `v.1.119.1` własny język w `LimbusCompany_Data/Lang/Polski/`
  **wymaga** obecności niepustych plików `.ttf`/`.otf` w podkatalogach
  `Font/Context/` oraz `Font/Title/` — bez nich gra pomija paczkę językową nawet
  po wybraniu `Polski` w `Select Custom Language` (`E-011`).
- W `assets/fonts/` wersjonujemy w 100% **niemodyfikowane** pliki na licencji
  **SIL Open Font License 1.1** odpowiadające krojom samej gry:
  `Context/Pretendard-Regular.ttf` (`orioncactus/pretendard` v1.309) oraz
  `Title/Mikodacs.otf` (v0.28 polskiego projektanta Grzegorza Luka,
  `glukfonts.pl`). Brak modyfikacji gwarantuje pełną zgodność z zastrzeżonymi
  nazwami `Pretendard` i `Mikodacs` (pkt 3 SIL OFL 1.1).
- Test w grze (`E-012`) na `LCB_TEST_DROGI_Polski_26652290_v3.zip` potwierdził
  natychmiastowe uruchomienie gry w języku `Polski` i czyste renderowanie
  kompletu **18/18 polskich znaków diakrytycznych** (`ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ`) bez
  kwadratów ani artefaktów.

### D-11 · 2026-11-26 · Tymczasowy przekład UI, technikaliów i kart meta przez agenty (`AI-tymczasowe`, `"origin": "ai"`) z pełnym priorytetem Tłumacza

Polecenie właściciela (przeniesione z `szybkoiwyraznie-rgb/wherewindsmeet`):

- Aby gra była szybko i wygodnie grywalna po polsku jeszcze przed ukończeniem
  wszystkich działów `widoki.zip` przez ludzkiego Tłumacza, agenty Arena (ten
  oraz równoległe sesje) mogą tworzyć **tymczasowy przekład `AI-tymczasowe`**
  wyłącznie dla **interfejsu (UI), ustawień, samouczków, opisów technicznych
  mechanik/statusów oraz kart meta/statystyk** (Tożsamości, umiejętności,
  pasywki, E.G.O, Dary E.G.O, statystyki/skille wrogów, UI/zadania/przedmioty
  trybu RPG).
- **Ściśle wyłączone z `AI-tymczasowe` (100% zarezerwowane dla Tłumacza):**
  cały `StoryData/*` (`sceny.zip`), kwestie głosowe (`PersonalityVoiceDlg/*`,
  `EGOVoiceDig/*`, `BattleAnnouncerDlg/*`), piosenki (`BgmLyrics/*`), dymki
  bojowe (`BattleSpeechBubbleDlg*`), dzienniki obserwacji (`AbnormalityGuides*`),
  opisy lore w Notatkach Dantego (`StoryTheaterDanteNoteDetail*`, `Story-*`),
  biogramy Grzeszników (`IntroduceCharacter.description`), zdarzenia i dialogi
  Anomalii/Lochów (`AbEvents*`, `AbDlg*`, `ActionEvents*`) oraz dialogi i
  narracja RPG Canto X (`rpg-loc-dialogue*`, `rpg-loc-narration*`).
- **Oznaczenie pochodzenia i reguły priorytetu:**
  - każdy wpis AI w `tlumaczenie/pliki/*.json` i `tlumaczenie/slowniki.json`
    nosi jawne pole `"origin": "ai"` (`tools/import_zwrotki.py --ai`), a zwrotki
    źródłowe agentów są wersjonowane w `zwrotki/ai/PXX_<slug>.md`;
  - import `--ai` nigdy nie nadpisuje wpisu Tłumacza (`skipped_human_existing`),
    natomiast zwrotka Tłumacza zawsze nadpisuje wpis AI (`replaced_ai`) i usuwa
    znacznik `"origin": "ai"`;
  - paczka do gry (`tools/build_lang.py`) domyślnie włącza wpisy Tłumacza oraz
    `AI-tymczasowe` (z rozbiciem `human_leaves` / `ai_leaves` w `MANIFEST.json`
    i opcją `--no-ai`);
  - pakiety robocze i przyrostowe dla Tłumacza (`tools/build_package.py
    --wypelnij-pl`, `tools/audit_update.py --delta-out`) **pomijają wpisy
    `"origin": "ai"`**, zostawiając Tłumaczowi puste pola `PL:` (osobny pakiet
    kontrolny samych wpisów AI buduje flaga `--tylko-ai`).
- **Bramka startowa:** po przygotowaniu technicznym i podziale na `87` paczek
  (`paczki_ai/MANIFEST.json`, `docs/PLAN_TLUMACZENIA_AI.md`) agenty czekają na
  wyraźny sygnał właściciela przed rozpoczęciem tłumaczenia.

### D-12 · 2026-11-25 · Wszystkie artefakty pracy w Gicie; poza Gitem tylko binaria gry

Decyzja właściciela po utracie artefaktów paczki P59 (`/tmp` znika razem z
piaskownicą, a ignorowane `local/` nie przechodzi przez odtworzenie sesji —
oba mechanizmy skasowały pliki pracy):

- **Jedyne pliki, których nie wolno trzymać w Git, to binarne pliki gry**
  (bundle Unity, `*.assets`, pliki wykonywalne, czcionki gry, archiwa, zapisy,
  zrzuty) oraz dane prywatne — jak w D-06 i [DATA_POLICY.md](DATA_POLICY.md).
- **Wszystko inne** — rendery paczek, wyciągi AI (`parsed`/`work`/`krmatch`/
  `fresh`), pliki `merged`/`filled`, skrypty builderów, `krmap`, indeksy,
  teksty, bazy — trafia do commitowanego drzewa (katalog `local/` przestaje
  być ignorowany) i jest zapisywana w checkpointach.
- **Zakaz pracy w `/tmp`** dla czegokolwiek, co ma przetrwać turę; narzędzia
  i pipeline AI zapisują pośrednie artefakty wyłącznie pod ścieżkami w repo.
- Surowe ZIP-y od właściciela nadal żyją w ignorowanym `google_drive/`.

## Otwarte (decyduje właściciel; agent przygotowuje opcje)

Brak otwartych decyzji — wszystkie `O-01` … `O-07` zostały rozstrzygnięte.

| Nr | Pytanie | Kiedy potrzebne | Uwagi |
|---|---|---|---|
| ~~O-01~~ | ~~Nazwa języka w `config.json` / folderu (`Polski`? `PL`?)~~ | — | **zamknięte 2026-11-25: `Polski`** → D-09 |
| ~~O-02~~ | ~~Kolejność prac / zakres pierwszego pakietu~~ | — | **zamknięte 2026-11-25: od razu cała gra (`sceny.zip` + `widoki.zip`, 100% tekstów z kontekstem)** → D-08 |
| ~~O-03~~ | ~~Czcionki i wyświetlanie polskich znaków w `Lang/Polski/`~~ | — | **zamknięte 2026-11-25: wymagane `Font/{Context,Title}` z niemodyfikowanymi czcionkami SIL OFL 1.1 (`Pretendard-Regular.ttf` + `Mikodacs.otf`); działanie i 18/18 polskich liter potwierdzone w grze (`E-012`)** → D-10 |
| ~~O-04~~ | ~~Akceptacja układu Czytanek (próbki w Markdown; ewentualnie HTML/DOCX)~~ | — | **zamknięte 2026-11-25: układ zaakceptowany i zamrożony; ewentualne usterki zgłaszane na bieżąco w trakcie czytania** → D-07 |
| ~~O-05~~ | ~~Czy tłumacz czyta po koreańsku~~ | — | **zamknięte 2026-11-25: tak** → D-05 potwierdzona |
| ~~O-06~~ | ~~Czy teksty gry mają być w repozytorium (publicznym)~~ | — | **zamknięte 2026-11-25: tak, jako JSON/MD; binaria nigdy** → D-06 |
| ~~O-07~~ | ~~Czy wolno pracować na publicznych lustrach~~ | — | **zamknięte 2026-11-25: tak** → D-06 |
