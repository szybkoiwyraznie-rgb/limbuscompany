# Plan tymczasowego tłumaczenia UI, technikaliów i kart meta (`AI-tymczasowe`, `D-11`)

Dokument opisuje architekturę techniczną oraz podział materiału na paczki robocze przygotowane dla agentów Arena zgodnie z decyzją **`D-11`** (wzorowaną na repozytorium `wherewindsmeet`).

> **Bramka startowa:** Repozytorium, narzędzia i podział na 87 paczek są gotowe technicznie. Agenty **nie rozpoczynają tłumaczenia** do momentu wyraźnego sygnału właściciela projektu.

---

## 1. Zasady nadrzędne (`D-11`)

1. **Zakres `AI-tymczasowe` (`"origin": "ai"`):** wyłącznie elementy interfejsu (UI), ustawień, samouczków, opisów technicznych mechanik/statusów oraz kart meta/statystyk (Tożsamości, umiejętności, pasywki, E.G.O, Dary E.G.O, statystyki/skille wrogów, UI/zadania/przedmioty RPG).
2. **Zakres ściśle wyłączony (100% zarezerwowany dla ludzkiego Tłumacza):**
   - wszystkie sceny fabularne i historie Tożsamości (`StoryData/*.json` → `sceny.zip`: Prolog, Canto I–IX, Intervallo, Walpurgis),
   - kwestie głosowe Tożsamości (`PersonalityVoiceDlg/*` — `199` plików, `9 504` el.) i E.G.O (`EGOVoiceDig/*` — `14` plików, `405` el.),
   - kwestie komentatorów walki (`BattleAnnouncerDlg/*` — `68` plików, `1 982` el.),
   - teksty piosenek (`BgmLyrics/*` — `17` plików, `662` el.),
   - dymki dialogowe postaci w walce (`BattleSpeechBubbleDlg*` — `12` plików, `2 471` el.),
   - prozatorskie dzienniki obserwacji Anomalii (`AbnormalityGuides*` — `24` plików, `783` el.),
   - prozatorskie wpisy lore w Notatkach Dantego i cytaty kulminacyjne (`StoryTheaterDanteNoteDetail*`, `Story-*` — `14` plików, `178` el.),
   - literackie biogramy Grzeszników (`IntroduceCharacter.json :: *.description` — `12` el.),
   - zdarzenia tekstowe, wybory i dialogi Anomalii/Lochów (`AbEvents*`, `AbDlg*`, `ActionEvents*` — `99` plików, `4 421` el.),
   - dialogi i narracja trybu RPG Canto X (`RPGSystem/rpg-loc-dialogue*`, `RPGSystem/rpg-loc-narration*` — `53` plików, `8 440` el.),
   - nieprzetłumaczone przez Project Moon robocze napisy koreańskie w plikach EN (`KR == EN` z Hangulem — `293` el.).
3. **Pełny priorytet ludzkiego Tłumacza:**
   - wpisy AI są zapisywane w `tlumaczenie/pliki/*.json` i `tlumaczenie/slowniki.json` z jawnym polem `"origin": "ai"`,
   - `import_zwrotki.py --ai` **nigdy nie nadpisuje** istniejących wpisów Tłumacza (`skipped_human_existing`),
   - standardowy import zwrotki Tłumacza (`import_zwrotki.py` bez `--ai`) **zawsze nadpisuje** wpis AI (`replaced_ai`) i usuwa znacznik `"origin": "ai"`,
   - paczki robocze generowane dla Tłumacza (`build_package.py --wypelnij-pl` oraz pakiety przyrostowe `audit_update.py --delta-out`) **pomijają wpisy `"origin": "ai"`**, zostawiając Tłumaczowi czyste puste pola `PL:` wszędzie tam, gdzie jeszcze sam nie tłumaczył,
   - grywalna paczka językowa (`build_lang.py`) **domyślnie uwzględnia** zarówno wpisy Tłumacza, jak i tymczasowe wpisy AI (z dokładnym rozbiciem `human_leaves` i `ai_leaves` w `MANIFEST.json` i `INSTRUKCJA.txt`; flaga `--no-ai` pozwala zbudować paczkę wyłącznie z przekładu Tłumacza).

---

## 2. Podział na 3 Fale i 87 paczek (`paczki_ai/MANIFEST.json`, build `26917622`)

| Fala | Kategorie | Zakres paczek | Liczba paczek | Unikalne sloty `PL:` | Już przetłumaczone (Tłumacz) | Do przetłumaczenia (`AI`) |
|---|---|---|---:|---:|---:|---:|
| **Fala 1** | `1A`–`1D` | Fundament bojowy, interfejs główny i ustawienia, tryby/etapy/Lochy/Teatr UI, samouczki i wskazówki | **14** (`P01`–`P14`) | `7 291` | `72` | **`7 219`** |
| **Fala 2** | `2A`–`2C` | Słowa kluczowe i statusy walki (`BattleKeywords`/`Bufs`), przedmioty/sklep/Przepustka/wydarzenia UI, modele i RPG Canto X UI/zadania | **28** (`P15`–`P42`) | `14 994` | `0` | **`14 994`** |
| **Fala 3** | `3A`–`3C` | 12 Grzeszników (Tożsamości, skille, pasywki — 1 paczka na Grzesznika + wspólne), E.G.O i Dary E.G.O, wrogowie/Anomalie/bossowie | **45** (`P43`–`P87`) | `25 091` | `0` | **`25 091`** |
| **Razem** | `1A`–`3C` | **Całość UI, technikaliów i kart meta/statystyk** | **87** (`P01`–`P87`) | **`47 376`** | **`72`** | **`47 304`** |

### Szczegółowy rozkład kategorii

1. **Fala 1 — natychmiastowa czytelność menu, ustawień, trybów i samouczków (`P01`–`P14`):**
   - `1A` (`P01`–`P02`, `849` slotów): grzechy, odporności, tagi `[On Hit]`/`[Clash Win]`, Panika, interfejs bitwy i cechy jednostek (`UnitKeyword`). **Paczka `P01` musi powstać jako pierwsza** — zamraża nazewnictwo bojowe dla Fal 2–3.
   - `1B` (`P03`–`P04`, `868` slotów): menu główne (`MainUIText`), pełne ustawienia gry (`kr_settings-ui-donttranslate.json`), komunikaty okienkowe (`PopupDesc`), skróty klawiszowe, profil, filtry i ekran formacji.
   - `1C` (`P05`–`P10`, `3 470` slotów, w tym `72` Tłumacza): nazwy rozdziałów, etapów i węzłów mapy, warunki etapów, Lustrzane Lochy UI, Kolej Załamania oraz nagłówki/tytuły Teatru i Notatek Dantego.
   - `1D` (`P11`–`P14`, `2 104` slotów): samouczki systemowe (`TutorialDesc*`, `TutorialMainUIText`, `TutorialMirrorDungeon`) i wskazówki ekranu ładowania (`BattleHint*`).
2. **Fala 2 — słownik statusów bojowych, ekonomia/wydarzenia i UI trybu RPG (`P15`–`P42`):**
   - `2A` (`P15`–`P29`, `8 279` slotów): pełny katalog `BattleKeywords*` i `Bufs*` (wszystkie statusy, buffy, debuffy i żetony mechanik).
   - `2B` (`P30`–`P38`, `4 777` slotów): przedmioty, waluty, sklep, banery ekstrakcji, Przepustka Bitewna, misje oraz interfejs wydarzeń sezonowych.
   - `2C` (`P39`–`P42`, `1 938` slotów): tabela modeli (`ScenarioModelCodes-AutoCreated.json`), mówcy RPG (`rpg_speaker`) oraz UI, zadania, przedmioty, lokacje i statystyki trybu RPG Canto X.
3. **Fala 3 — karty Grzeszników, E.G.O / Dary E.G.O oraz przeciwnicy (`P43`–`P87`):**
   - `3A` (`P43`–`P55`, `7 629` slotów): komplet Tożsamości, umiejętności i pasywek każdego Grzesznika w osobnej, spójnej paczce (`P43` Yi Sang, `P44` Faust, `P45` Don Quixote, `P46` Ryōshū, `P47` Meursault, `P48` Hong Lu, `P49` Heathcliff, `P50` Ishmael, `P51` Rodion, `P52` Sinclair, `P53` Outis, `P54` Gregor) + `P55` tabele wspólne.
   - `3B` (`P56`–`P65`, `5 370` slotów): Dary E.G.O (`P56`–`P60`) oraz karty, umiejętności i pasywki E.G.O (`P61`–`P65`).
   - `3C` (`P66`–`P87`, `12 092` slotów): nazwy, części, umiejętności i pasywki przeciwników, Anomalii, bossów i jednostek wsparcia.

---

## 3. Protokół pracy wieloagentowej (brak konfliktów Git)

1. **Sprawdzenie aktualnego stanu fal i paczek:**
   ```bash
   python3 tools/prepare_ai_batches.py --status
   ```
2. **Wygenerowanie roboczego pliku `.md` dla przydzielonej paczki (np. `P01`):**
   ```bash
   python3 tools/prepare_ai_batches.py --render P01 --out local/paczki_ai
   ```
3. **Przekład zgodnie z `paczki_ai/SLOWNIK_TERMINOW.md` i zapis gotowej zwrotki w `zwrotki/ai/`:**
   - Każda paczka ma unikalną ścieżkę docelową `zwrotki/ai/PXX_<slug>.md` zapisaną w `paczki_ai/MANIFEST.json`.
   - Jeżeli kilka agentów Arena pracuje równolegle na osobnych gałęziach/sesjach, każdy zapisuje wyłącznie własne pliki `zwrotki/ai/PXX_*.md` — brak kolizji nazw plików.
4. **Walidacja tokenów i atomowy import do `tlumaczenie/` z oznaczeniem `"origin": "ai"`:**
   ```bash
   python3 tools/import_zwrotki.py --ai zwrotki/ai/P01_1a_fundament_bojowy_cz01.md
   ```
   (lub zbiorczo po scaleniu wielu zwrotek: `python3 tools/import_zwrotki.py --ai zwrotki/ai/`).
5. **Zbudowanie grywalnej paczki językowej / pakietów dla Tłumacza:**
   - Grywalna paczka `Lang/Polski/` (Tłumacz + AI): `python3 tools/build_lang.py`
   - Paczka wyłącznie z przekładu Tłumacza (bez AI): `python3 tools/build_lang.py --no-ai`
   - Pełny pakiet roboczy dla Tłumacza (wpisy AI są automatycznie pomijane, pola `PL:` pozostają puste): `python3 tools/build_package.py --wypelnij-pl --version <N>`
   - Pakiet weryfikacyjny wyłącznie z wpisami AI: `python3 tools/build_package.py --tylko-ai --version <N>`
