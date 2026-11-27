# Status

Stan na **2026-11-27**.

## Gdzie jesteśmy

**Druga produkcyjna polska paczka językowa `LCB_PL_Polski_26917622_v2.zip`
(`7 566 960` B, build Steam `26917622`) jest zbudowana z repozytorium i wgrana na
Dysk Google (E-016): zawiera pełny przekład Tłumacza z `LC_PL1.zip` + `LC_PL2.zip`
(`7 147` adresów: Prolog, Canto I–III, Intervallo I „Hell's Chicken”, opowiadanie
Notatek Dantego, 36 historii Tożsamości Sezonu 1, widoki rozdziałów/etapów i
interfejsu głównego, `197` mówców/tytułów/miejsc) oraz tymczasowy przekład AI
(`42 662` adresów; wpisy Tłumacza nadpisują AI). Razem `57 071 / 193 309` =
`29,52%` liści w całej grze z bezpiecznym fallbackiem EN dla reszty.**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows,
  `64/64` testów zielonych).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł przebieg bazowy (`26652290`, E-007)
  oraz przebieg po czwartkowej aktualizacji (`LCB_DANE_20261126_094359_ef145d.zip`,
  build Steam **`26917622`**, 7368 plików, 0 błędów — E-013).
- Wszystkie decyzje projektowe zamknięte (`D-01` … `D-12`, brak otwartych `O-*`):
  źródło przekładu **KR** (D-05), teksty gry w repozytorium jako JSON/MD bez
  binariów (D-06), układ Czytanek zaakceptowany i zamrożony (D-07), kompletny
  pakiet 100% gry naraz (D-08), nazwa języka **`Polski`** i 5-kluczowy
  `Lang/config.json` (D-09), niemodyfikowane czcionki SIL OFL 1.1 w
  `assets/fonts/` potwierdzone w grze (D-10, zamyka O-03), architektura
  tymczasowego przekładu UI/technikaliów/meta przez agenty (`AI-tymczasowe`,
  `"origin": "ai"`) z pełnym priorytetem Tłumacza (D-11) oraz polityka
  **wszystko poza binariami gry w Gicie; zakaz `/tmp` i katalogów
  gitignored dla artefaktów pracy** (D-12).
- **Teksty gry i Czytanki w repozytorium** (E-006, E-007, E-013):
  `index/localize/{kr,en}` na aktualnym buildzie Steam **`26917622`** (`2 464`
  `kr`, `2 421` `en`); `index/static-data/` z OpenLethe (`8f24cba5`, dane z
  `2026-11-12` — do odświeżenia, gdy OpenLethe opublikuje tabele dla `10117` i
  `11217`); Czytanki i pliki ID w `czytanki/`.
- **Pakiety dla tłumacza na Dysku:**
  - pakiet bazowy (`26652290`, E-008): `plik_dla_tlumacza_v2.zip` (`11 449 704` B,
    SHA-256 `9bb4dcad…a5006` — **156 079** elementów / **130 043** unikalnych
    napisów);
  - **pakiet przyrostowy z aktualizacji `2026-11-26` (`26652290` → `26917622`,
    E-013): `pakiet_przyrostowy_26652290_do_26917622.zip`** (`155 363` B,
    SHA-256 `c20f006a1e7cb38a7a21b1b5f5f2307b784d5476527df72f4a0df9ba1953b3df`
    — wyłącznie nowości i poprawki z łatki: `2` nowe historie Tożsamości
    `P10117` Yi Sang i `P11217` Gregor, `3` nowe wpisy słownika mówców oraz `17`
    plików widoków, łącznie **1 733** unikalne puste pola `PL:`).
- **Stan przekładu (`tlumaczenie/`) i paczka do gry na Dysku (E-014, E-016):**
  - zaimportowano pierwszą zwrotkę `LC_PL1.zip` (`19` plików Markdown, `0`
    błędów, `0` ostrzeżeń) i drugą `LC_PL2.zip` (`24` plików, `6 802`
    przetłumaczonych, **`696` wpisów AI nadpisanych przez Tłumacza**, `1`
    ostrzeżenie: zmiana źródła `chapter_n_9128` na tytuł Canto X — element
    pominięty do pakietu przyrostowego): łącznie **`7 147` adresów Tłumacza**
    i `42 662` adresów AI (`49 809` plików-wyników w `tlumaczenie/pliki/`),
    `197` wpisów w `tlumaczenie/slowniki.json`;
  - treść MD zwrotek Tłumacza jest w repo (`zwrotki/tlumacz/LC_PL1/`, `LC_PL2/`,
    `D-12`);
  - zbudowano i wgrano na Dysk produkcyjne paczki **`LCB_PL_Polski_26917622_v1.zip`**
    (`7 491 054` B, `12 099 / 193 308` = `6,26%` liści) i
    **`LCB_PL_Polski_26917622_v2.zip`** (`7 566 960` B, SHA-256
    `4af4f29c01b47981933c721159b8fe567ad8eb04c48492dccb0955f8cc2501b8`,
    `2 422` plików JSON, `1 130` zmodyfikowanych, **`57 071 / 193 309` =
    `29,52%` liści po polsku**).
- **Importer zwrotek, generator `Lang/Polski/` i audyt aktualizacji (E-009 … E-014):**
  - `tools/import_zwrotki.py` waliduje zgodność źródeł, znaczniki TMP, zmienne
    `{0}`, słowa kluczowe `[Keyword]`, styl `DEN` w `BgmLyrics/*` i znaczniki
    skryptu `//…` w `StoryData/*`, ostrzega przed niezamierzonym Hangulem w
    `PL:`, dziedziczy powtórzenia, obsługuje `--allow-older-package` i zapisuje
    `tlumaczenie/` atomowo;
  - `tools/build_lang.py` buduje deterministyczne archiwum `Lang/Polski/` (pełny
    5-kluczowy `config.json` + czcionki OFL z `assets/fonts/` + pliki JSON z
    fallbackiem EN i rzutowaniem słownika mówców/tytułów) — działanie
    potwierdzone w grze (`E-012`);
  - `tools/audit_update.py` porównuje buildy (`--old` lub czysto z Git
    `--old-rev`), wykrywa zmienione oryginały `KR` w `tlumaczenie/` i buduje
    pakiety uzupełniające (`--delta-scope files`) oraz ścisłe pakiety
    przyrostowe (`--delta-scope items`), pomijając wpisy `"origin": "ai"` przy
    wypełnianiu pól `PL:` dla Tłumacza;
  - **Przygotowanie techniczne pod `AI-tymczasowe` (`D-11`, `E-015`):**
    `tools/prepare_ai_batches.py`, `paczki_ai/MANIFEST.json`,
    `paczki_ai/SLOWNIK_TERMINOW.md` oraz `docs/PLAN_TLUMACZENIA_AI.md` dzielą
    cały zakres UI, opisów technicznych i kart meta/statystyk na **`87`
    bezkolizyjnych paczek (`P01`–`P87`) w 3 falach (`47 376` unikalnych slotów
    `PL:`, w tym `72` już przetłumaczone przez Tłumacza i `47 304` do wykonania)**,
    z pełnym wyłączeniem całej fabuły, dialogów, głosów, piosenek, dzienników
    obserwacji i narracji RPG. **Oczekuje na sygnał właściciela przed startem
    tłumaczenia.**

## Następny krok

1. **Właściciel:**
   - dać sygnał do rozpoczęcia tłumaczenia `AI-tymczasowe` (np. od **Fali 1**:
     `P01`–`P14` — rdzeń UI, ustawienia, tryby, samouczki i słownik bazowy walki,
     lub równolegle na kilku sesjach Arena według `docs/PLAN_TLUMACZENIA_AI.md`),
   - przetestować w grze paczkę `LCB_PL_Polski_26917622_v2.zip` z Dysku Google i
     przekazywać kolejne zwrotki Tłumacza.
2. **Agenci (po sygnale właściciela):** realizować paczki `P01`–`P87` według
   `paczki_ai/SLOWNIK_TERMINOW.md` → `zwrotki/ai/PXX_*.md` →
   `import_zwrotki.py --ai`, integrować zwrotki Tłumacza (zawsze nadpisujące
   wpisy AI), budować kolejne wersje `LCB_PL_Polski_<build>_vN.zip` oraz — gdy
   `OpenLethe` opublikuje zaktualizowane `StaticData` — dograć je przez
   `tools/import_data.py`.

## Otwarte decyzje

Brak — wszystkie `O-01` … `O-07` zamknięte w [DECYZJE.md](DECYZJE.md).
