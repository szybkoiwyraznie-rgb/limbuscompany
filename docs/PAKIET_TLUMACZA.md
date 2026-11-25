# Pakiet dla Tłumacza (`lc-paczka-v1`) — wzór SRW

**Decyzja właściciela (2026-11-25): Pakiet jest wzorowany na SRW** (pakiet SRW Y
`template-v8`, który ma ten sam układ co pakiet SRW OE). Sceny (Canto) i inne
elementy fabularne mają mieć **jak najwięcej kontekstu**: mówców, miejsca i
miejsce w chronologii.
**Źródło przekładu: koreański.** EN jest obok jako odniesienie.
**Status: specyfikacja.** Liczby i nazwy pól uzupełnimy po pierwszym
rozpoznaniu danych. Źródła kontekstu opisuje sekcja 4.

## 1. Zawartość archiwum (jak w SRW)

```text
LC_PAKIET_<nazwa>_v<N>.zip
├── README.md      instrukcja po polsku: element, zasady, tokeny, limity, odpowiedzi
│                  na pytania Tłumacza (numerowane sekcje), „co się zmieniło w wersji N”
├── sceny.zip      fabuła: spis-rozdzialow.md + spis-scen.md + pliki scen
│                  (canto-00.md, canto-01_a.md, …, intervallo-*.md, wydarzenie-*.md)
└── widoki.zip     nazwy i teksty spoza scen, pogrupowane tematycznie (sekcja 3)
```

- Tłumacz pracuje **tylko w plikach `.md`** i wpisuje polski tekst po `PL:`.
  Nie musi znać JSON-ów ani żadnych narzędzi.
- Plik dzielimy na części `_a`, `_b`, … powyżej ok. 8000 linii, tak jak w SRW.
- Kopia rozpakowanego pakietu i jego manifest importu leżą w repozytorium w
  `paczki/<nazwa>/v<N>/`. ZIP trafia na Dysk do folderu „Limbus Company”, z
  rozmiarem, SHA-256 i ponownym pobraniem dla sprawdzenia bajtów.
- Pakiet jest deterministyczny: z tych samych danych powstają te same bajty.
  Pliki mają kodowanie UTF-8; LF i CRLF są akceptowane przy imporcie.

## 2. Element (układ SRW)

```text
14. [Kwestia — 그레고르 (Gregor)] <tekst KR>
   tokeny: zachowaj dokładnie: <color=#f8c200> </color>
   EN: <tekst EN>
   PL:
```

- **Pierwsza linia** zawiera numer, etykietę i tekst źródłowy KR. Etykiety:
  - `[Kwestia — mówca]` i `[Narracja]`;
  - `[Miejsce]`: podpis miejsca na ekranie (pole `place`);
  - `[Mówca — wyświetlane imię]` / `[Tytuł mówcy]`: pola `teller`/`title`;
  - `[Nazwa umiejętności]`, `[Opis monety]`, `[Status]`, `[Interfejs]` itd.

  Tekst wielowierszowy ma kolejne linie **wcięte trzema spacjami**, tak samo w
  KR i EN.
- **Mówca** pochodzi z danych gry: `model` → `ScenarioModelCodes`, a jeśli
  scena nadpisuje imię, to z `teller`. Podajemy imię KR i angielskie w
  nawiasie, jak w SRW Y. Gdy mówcy nie da się ustalić, piszemy `???` z numerem
  grupy, nigdy imię zgadnięte z treści.
- `tokeny:` wylicza wszystkie znaczniki i zmienne, które mają zostać bez zmian
  (`tools/lc_tokeny.py`, reguły w [METODA.md](METODA.md), punkt 4). Ich kolejność
  może się zmienić zgodnie z gramatyką, liczba nie.
- `limit:` dodajemy **tylko tam, gdzie jest zmierzony**: pola interfejsu i
  nazwy, liczone z najdłuższego tekstu, który gra pokazuje w tym samym polu (jak
  w SRW). Okno dialogowe Limbusa przewija tekst; limit dla kwestii pojawi się
  dopiero wtedy, gdy test w grze pokaże taką potrzebę **[?]**.
- `PL:` wypełnia się **w jednej linii**. Podział wiersza `\n` wpisuje się tylko
  wtedy, gdy wymienia go `tokeny:`.
- `(powtórzenie elementu N — nie wpisuj tu nic)` oznacza ten sam tekst KR w tym
  samym pliku. Przekład dziedziczy się automatycznie.
- `EN: (brak wersji angielskiej w grze)` oznacza, że tłumaczymy z samego KR.
- **Klucze nie są widoczne w pliku**, jak w SRW. Powiązanie element → jednostka
  (klucz `zakres/plik#id~n#ścieżka`, [METODA.md](METODA.md), punkt 2) jest w
  manifeście `paczki/<nazwa>/v<N>/manifest.json`. Numeracja elementów nie zmienia
  się między wersjami pakietu; nowe wersje tylko dopisują linie informacyjne.

## 3. Pliki

### `sceny.zip` — fabuła z pełnym kontekstem

**`spis-rozdzialow.md`** pokazuje cały przebieg fabuły, jak `spis-misji.md`
w SRW Y:

- część (Inferno, …), a w niej Canto z numerem, tytułem KR/EN, firmą,
  dystryktem i datą z osi czasu;
- etapy w kolejności gry, z tytułem etapu, liczbą scen i liczbą linii;
- na końcu Intervallo, wydarzenia i opowieści osobowości, w podziale na grupy.

**`spis-scen.md`** zawiera wszystkie sceny w kolejności chronologicznej. Przy
każdej: numer porządkowy, plik sceny (`S101B`), Canto i etap, „przed walką /
po walce”, mówcy, liczba linii i plik `.md`.

**Nagłówek każdej sceny:**

```text
## Scena 12/920 — S107B
- chronologia: Canto I „<tytuł KR> / <tytuł EN>”, scena 7 z 24 w Canto
  (poprzednia: S106B, następna: S107A)
- część: Inferno · firma: <KR / EN> · dystrykt: <KR / EN> · oś czasu: 984-01
- etap: 1-7 „<tytuł etapu KR / EN>” — przed walką
- opis etapu (z gry): KR: … / EN: …
- miejsce: <podpis miejsca KR / EN>; tło sceny: <identyfikator tła>
- uczestnicy:
  - 그레고르 — Gregor
  - 유리 — Yuri (tytuł: <KR / EN>)
```

- Opis etapu (`StageNode*.desc`) i opis Canto (`StoryTheaterMain.desc`) to
  krótkie streszczenia pisane przez grę. Dla Tłumacza są tym, czym w SRW
  „bible”, i biorą się z danych, a nie z naszych domysłów.
- Gdy w trakcie sceny zmienia się miejsce lub tło, przed elementem pojawia się
  linia informacyjna `— miejsce: … —`. Nie jest to element do tłumaczenia.
- Wszystko, czego nie da się ustalić z danych, jest wpisane wprost, np.
  `etap: brak wpisu w danych`. Niczego nie dopisujemy „na oko”.

### `widoki.zip` — teksty spoza scen

Ostateczny podział ustalimy po rozpoznaniu. Wstępnie:

| Plik | Zawartość | Kontekst przy elemencie |
|---|---|---|
| `00_postacie_i_mowcy.md` | `ScenarioModelCodes` (imiona, przydomki), nazwy Grzeszników | ile kwestii ma postać, w których Canto mówi |
| `01_osobowosci.md` | Osobowości (ID): nazwa, tytuł, umiejętności, opisy monet, pasywki, kwestie | blok na ID: Grzesznik, ranga, sezon; przy umiejętności: numer, poziom Uptie, grzech i typ ataku |
| `02_ego.md` | E.G.O: nazwy, umiejętności, pasywki, kwestie | jak wyżej |
| `03_statusy_i_slowa_kluczowe.md` | `BattleKeywords`, `Bufs`, `SkillTag` | **nazwa statusu ma jedną pisownię**, bo działa jako link w opisach ([METODA.md](METODA.md), punkt 4) |
| `04_etapy_i_rozdzialy.md` | `StageChapterText`, `StagePartText`, `StageNode*`, `StoryTheater*` | Canto i etap, do którego należy tekst |
| `05_interfejs.md` | `MainUIText`, `BattleUIText` i inne pliki UI | limit pola |
| `06_wrogowie_i_anomalie.md` | `Enemies*`, `AbnormalityGuides*`, `AbEvents*` | Canto lub wydarzenie |
| `07_lustro_kolej_wydarzenia.md` | Mirror Dungeon, Refraction Railway, wydarzenia | nazwa trybu lub wydarzenia |
| `08_dialogi_bitewne.md` | `BattleSpeechBubbleDlg*`, `PersonalityVoiceDlg/`, `BattleAnnouncerDlg/` | mówca (osobowość lub komentator) i sytuacja (pole lub identyfikator) |

## 4. Skąd kontekst (dane gry)

| Kontekst | Źródło | Pewność |
|---|---|---|
| Kolejność scen w Canto, etap, przed/po walce | `StaticData/static-data/storytheater-main/*.json` (`storyList`: `storyId`, `nodeId`, `stageDetail` Before/After) | **[1]**: format z publicznej kopii danych z 2023 r.; potwierdzimy na zbiorze z zbieracza 1.1.0 |
| Część, Canto, firma, dystrykt, oś czasu | `Localize`: `StagePartText`, `StageChapterText` (`chapter`, `chaptertitle`, `company`, `area`, `timeline`) | [P] |
| Tytuł i opis etapu | `Localize`: `StageNode<część>-<canto>.json` (`id` = węzeł, `title`, `place`, `desc`) | [P] |
| Opis Canto | `Localize`: `StoryTheaterMain` (`CHAPTER_<n>`: `title`, `desc`) | [P] |
| Mówca | `StoryData` `model` → `ScenarioModelCodes-AutoCreated` (`name`, `nickName`); nadpisanie: `teller`/`title` | [P] |
| Miejsce i tło, postacie na ekranie | `StoryData.place`; `Story/Effect/<scena>.json` (`bg`, `characterlist`) | [1] (dane z 2023 r.) |
| Segmenty lochów w Canto | `DungeonNode*`, `DungeonArea*` (`stageList`: `title`, `desc`) | [P] |

## 5. Zwrotka i import (jak w SRW)

- Tłumacz odsyła te same pliki `.md`, w całości albo partiami, np. po jednym
  pliku Canto. Dozwolony jest ZIP z płaskimi plikami `.md`.
- Import porównuje **cały plik poza wartościami `PL:`** z manifestem: numery,
  kolejność, KR/EN, etykiety, tokeny i powtórzenia. Każda niezgodność kończy się
  odmową i raportem z numerem pliku i linii, bez cytowania treści.
- Kontrole elementu: dokładnie jedna linia `PL:`; tokeny zgadzają się jako
  multizbiór; brak Hangula; brak niewidocznych znaków sterujących. Puste `PL:`
  jest pomijane, więc można importować nieukończone pliki.
- Wynik trafia do `tlumaczenie/<obszar>.jsonl` (`{"klucz", "pl", "zrodlo_hash",
  "pakiet", "element"}`) w Git. Korekty techniczne agentów są w
  `tlumaczenie/KOREKTY.json`.
- Patch zawiera 100% zaakceptowanych pozycji. Pozostałe, a także przekłady
  nieaktualne po zmianie tekstu KR, pokazują w grze tekst **EN** ([CEL.md](CEL.md)).

## 6. Kolejność pakietów (propozycja)

1. **Pilot**: wybrane teksty interfejsu i Prolog. Test formatu, polskich znaków
   w domyślnym foncie i linków słów kluczowych w grze.
2. Statusy, słowa kluczowe, imiona i nazwy, czyli glosariusz.
3. Fabuła według `spis-rozdzialow.md`: Canto po Canto. Równolegle Czytanki PL.
4. Osobowości i E.G.O: umiejętności, pasywki, opisy, kwestie.
5. Wydarzenia, Mirror Dungeon i Refraction Railway, dialogi bitewne, reszta.
