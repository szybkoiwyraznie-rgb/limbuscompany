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
  dozwolone. Wydań na GitHub nie robimy (patch idzie na Dysk), ale zasady warto
  sprawdzić ponownie, gdy zostaną zaktualizowane.

## Polskie tłumaczenie fanowskie (istniejące)

- Tumblr **@st0nek** (<https://www.tumblr.com/st0nek>) z @pati-patter i
  @strix-and-stones — „nieoficjalne polskie tłumaczenie”: fabuła (m.in.
  Selva Obscura, Canto I), karty ID, umiejętności.
- Poradnik Steam „(Nieoficjalne) Polskie Tłumaczenie Limbus Company”
  (wrzesień 2026, sekcja poradników gry na Steam).
- **Decyzja właściciela (2026-11-25): ignorujemy.** Projekt jest niezależny —
  bez kontaktu, bez porównywania i bez korzystania z jego tekstu.

## Inne projekty tłumaczeń Limbus Company (przegląd 2026-11-25)

Właściciel zdecydował (2026-11-25), że przejmujemy ich metody i indeksy. Co
dokładnie przejmujemy i jak dostosowujemy do źródła KR:
**[METODA.md](METODA.md)**. Kodu z repozytoriów bez licencji nie kopiujemy,
tylko implementujemy reguły od nowa. Tekstów przekładów nie kopiujemy z żadnego
repozytorium.

| Projekt (GitHub) | Licencja | Co z niego bierzemy |
|---|---|---|
| `LocalizeLimbusCompany/LocalizeLimbusCompany` (zh-CN, „都市零协会”, ~1200★) | własna (CC BY-NC-SA 4.0 w README) | Skala i rodziny plików (pełne drzewa `KR/EN/JP` w repo). Praca w Paratranz, synchronizacja `LLC_Release`, instalator `LLC_MOD_Toolbox`. |
| `LocalizeLimbusCompany/LLC_Wiki` | MIT | Wytyczne: wypełniacze `{0}` przestawiane według gramatyki; nazwa statusu + spacja = automatyczny link do `BattleKeywords`; stałe formuły opisów umiejętności; archiwum decyzji o nazwach; karty stylu wypowiedzi postaci. Wzór dla `tlumaczenie/` (glosariusz, styl). |
| `Cynanchum0109/AutoLocalization` | brak | Schemat kluczy `zakres/plik#id~n#ścieżka`, biała lista pól, zamknięta lista tagów, reguły nawiasów, stany jednostek, pamięć tłumaczeniowa, kontrole `check.py`. Instalator BAT+PS1 podobny do naszego zbieracza. |
| `Crescent-Corporation/LimbusCompanyBusRUS` (RU) | brak | Budowanie z **zapasem EN** dla brakujących plików i wpisów; StoryData łączone według kolejności, reszta według `id`; reguły fontu per pole; skrót słów kluczowych (nie przejmujemy). |
| `kazhu233/Limbus-Company-Translation-Merge` | brak | Potwierdzenie: po aktualizacji brakujące pliki lub wpisy dają „Unknown” albo zawieszenie, więc patch musi być kompletny. |
| `Ian1254/LCPatch-Localization-Builder` | brak | Mówcy z `ScenarioModelCodes-AutoCreated.json` według `model`; `merge-report.json` + `checksums.sha256`; odrzucanie niebezpiecznych ścieżek i złego JSON. |
| `Noplch0/limbus-ai-localization` | brak | Biała lista pól (`translatable_keys.json`); własny folder w `Lang/`; wykrywanie Steam z `libraryfolders.vdf`. |
| `HKStudio011/trans-limbus` (VI) | brak | Kontrola wyrównania rekordów i `id` względem EN/KR oraz liczby `[]<>{}` i `\n`; kodowanie zapisu jak w źródle; własne fonty w `Font/`. |
| `kermond369-nsis/Limbus-glyph-zero-pack` | MIT | Fail-fast pokrycia znaków przez font (`safe_charset`); deterministyczny ZIP + SHA-256. |
| `Eden-Office/LimbusCompanyBusFR` (FR) | brak | Pełna struktura `Lang/fr/` (~2430 plików), `config.json` (`samplingPointSize` 78, `padding` 8), własne `.ttf` w `Font/`. Źródło liczb w CLS_FORMAT. |
| `Dreams-Office/LimbusCompanySpanishTranslationTeam` (ES) | MIT | Paczka CLS aktualizowana po łatkach; tłumaczone sprite'y opisane osobno. |
| `PGGB/limbus-company-data` (kopia folderu gry z 2023 r.) | brak | Tylko **format** danych pomocniczych: `StaticData/static-data/*` (kolejność scen w `storytheater-main`, statystyki ID/umiejętności), `Story/Effect/*` (tła scen), `Localize/RemoteLocalizeFileList.json`. Stąd zbieracz 1.1.0. Treści nie używamy. |
| PT-BR — CLT District, Uniao | — | FAQ ograniczeń CLS: jeden font, teksty na sprite'ach, tylko PC. |
| `kimght/LimbusLocalizationManager` | GPL-3.0 | Katalog 14 tłumaczeń społeczności (`data/localizations.toml`). Instalatora nie przejmujemy. |
| `x1bViolet/Limbus-Localization-UI` | MIT | Edytor z podglądem `Skills`/`Passives`/`EGOgift`/`Bufs`/`BattleKeywords`: wskazówka, które pliki mają bogate formatowanie. |
| `EnderDremurr/rainbus-toolbox` | GPL-3.0 | Tylko informacyjnie. |
| kimght/LimbusCompanyRuMTL, WhenThe1 | — | Rozróżnienie przekład ręczny / maszynowy; `BattleSpeechBubbleDlg*`. |

## Własne projekty właściciela (źródło sposobu pracy)

| Z projektu | Przejmujemy | Nie przejmujemy |
|---|---|---|
| `wherewindsmeet` (WWM) | AGENTS/ENVIRONMENT/LESSONS/STATUS/EXPERIMENT_LOG; zbieracz BAT+PS1 z testem w CI na Windows; builder z kontrolą kodowania; walidator zwrotu bez rozpakowywania; kontrola indeksu Git; Pakiet `wwm-paczka-v1` (klucz SHA-256, tokeny, import tylko klucz/PL); Czytanki w częściach | silnik, formaty plików, klucze i patcher WWM; skala 200 GB |
| `mtgcrawler` (SRW OE/Y/Z) | wiele tytułów w jednym repo → u nas jeden; dane na Dysku jak SRW OE; agenci robią tylko korekty techniczne (`CORRECTIONS.json`); patch = 100% zwrotki | binarne patchowanie, formaty Switch/PC SRW |

## Do sprawdzenia (gdy będzie potrzebne)

- Font: test w grze z wartościami z paczki FR (`samplingPointSize` 78,
  `padding` 8) — [METODA.md](METODA.md), punkt 9.
- Czy automatyczne linki słów kluczowych (nazwa + spacja) działają w CLS dla
  polskich nazw — test pilotażowy.
