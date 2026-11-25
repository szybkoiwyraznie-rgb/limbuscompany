# Prior art — co już istnieje i czego się nauczyliśmy

Analizujemy **formaty i narzędzia**. Nie kopiujemy cudzych przekładów (także
polskiego) ani zasobów.

## Oficjalne

- **CLS** (Project Moon, 2025-03-31, v1.73.0; fonty v1.74.0) — [CLS_FORMAT.md](CLS_FORMAT.md).
- **Zasady twórczości fanowskiej** — komunikat 2025-09-26
  (<https://store.steampowered.com/news/app/1973530/view/525355229451911687>):
  zapowiedź aktualizacji wytycznych; jako naruszenia wymieniono m.in.
  modyfikację klienta, udostępnianie zasobów, prywatne serwery, trenowanie AI
  i wykorzystanie występów aktorów głosowych przez AI. Zgłoszenia miały ruszyć
  od 2025-10-13; według społeczności aktualizacja się opóźniła i obowiązują
  stare zasady. Tłumaczenia przez CLS są przez społeczność uznawane za
  dozwolone. **Do ponownego sprawdzenia przed publicznym wydaniem.**

## Polskie tłumaczenie fanowskie (istniejące)

- Tumblr **@st0nek** (<https://www.tumblr.com/st0nek>) z @pati-patter i
  @strix-and-stones — „nieoficjalne polskie tłumaczenie”: fabuła (m.in.
  Selva Obscura, Canto I), karty ID, umiejętności.
- Poradnik Steam „(Nieoficjalne) Polskie Tłumaczenie Limbus Company”
  (wrzesień 2026, sekcja poradników gry na Steam).
- Wniosek: istnieje równoległa inicjatywa. Decyzja właściciela, czy ją
  ignorować, czy nawiązać kontakt ([CEL.md](CEL.md), pyt. 3). Nie kopiujemy
  jej tekstu; można porównać zakres i podejście (np. font, nazewnictwo).

## Inne społeczności (format CLS)

| Projekt | Wnioski |
|---|---|
| FR — Eden-Office/LimbusCompanyBusFR (GitHub) | Pełna struktura `Lang/fr/` (~2430 plików), `config.json`, katalogi `StoryData`, `PersonalityVoiceDlg`, `RPGSystem`, `BattleAnnouncerDlg`, `BgmLyrics`, `EGOVoiceDig`, `Font/`. Źródło liczb w CLS_FORMAT. |
| PT-BR — CLT District | Launcher/instalator; FAQ z ograniczeniami CLS (jeden font, teksty na sprite'ach, tylko PC). |
| ES — Dreams-Office | Paczka CLS, aktualizowana po każdej łatce. |
| RU — Crescent-Corporation; kimght/LimbusCompanyRuMTL | Ręczny przekład vs. maszynowy (MTL) — przykład, jak społeczność odróżnia oba. |
| zh-CN — LLC_zh-CN („都市零协会”) | Największa paczka; konwencje: `model` bez tłumaczenia, imiona przez `ScenarioModelCodes-AutoCreated.json`. |
| WhenThe1 (dialogi bitewne) | Pliki `BattleSpeechBubbleDlg*`. |

## Narzędzia społeczności (pomysły do przejęcia)

- **Cynanchum0109/AutoLocalization** — automatyczne łączenie zmian po
  aktualizacjach; potwierdza: `model` = identyfikator zasobu, duplikaty `id`
  (`-1` dla dźwięków), potrzeba kluczy z numerem wystąpienia (`#-1~2`).
- **Noplch0/limbus-ai-localization** — **biała lista tłumaczonych pól**
  (`translatable_keys.json`): tłumaczone są tylko pola z listy, reszta JSON
  bez zmian. Przejmujemy ideę (bez części AI).
- **Ian1254/LCPatch-Localization-Builder** — budowanie paczki z różnic.

## Własne projekty właściciela (źródło sposobu pracy)

| Z projektu | Przejmujemy | Nie przejmujemy |
|---|---|---|
| `wherewindsmeet` (WWM) | AGENTS/ENVIRONMENT/LESSONS/STATUS/EXPERIMENT_LOG; zbieracz BAT+PS1 z testem w CI na Windows; builder z kontrolą kodowania; walidator zwrotu bez rozpakowywania; kontrola indeksu Git; Pakiet `wwm-paczka-v1` (klucz SHA-256, tokeny, import tylko klucz/PL); Czytanki w częściach | silnik, formaty plików, klucze i patcher WWM; skala 200 GB |
| `mtgcrawler` (SRW OE/Y/Z) | wiele tytułów w jednym repo → u nas jeden; dane na Dysku jak SRW OE; agenci robią tylko korekty techniczne (`CORRECTIONS.json`); patch = 100% zwrotki | binarne patchowanie, formaty Switch/PC SRW |

## Do sprawdzenia (gdy będzie potrzebne)

- Jak inne paczki rozwiązują font z polskimi/łacińskimi znakami
  diakrytycznymi (FR/ES mają podobne potrzeby) i jakie wartości
  `samplingPointSize`/`padding` stosują.
- Jak PT-BR i ES radzą sobie z cotygodniowymi aktualizacjami (diff, narzędzia).
