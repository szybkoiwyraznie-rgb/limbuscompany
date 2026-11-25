# Wcześniejsze prace (prior art)

Zasada: z cudzych projektów bierzemy **wiedzę o formacie, problemach i
sposobach pracy**, nigdy ich tekstu przekładu (także z polskiego tłumaczenia).
Kodu na GPL nie kopiujemy (nasze narzędzia mają zostać proste i bez licencji
copyleft); kod MIT można by zaadaptować z atrybucją, ale na razie nie było
potrzeby. Testy używają wyłącznie danych wymyślonych.

Przegląd GitHuba zrobiono **2026-11-25**: 12 zapytań wyszukiwania, drzewa
plików ~25 repozytoriów, częściowe klony 14 z nich. Liczby z lustra
oryginalnych plików: [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md), E-004.

## Najważniejsze wnioski

1. **Oryginalne pliki `Localize` (KR/EN/JP) są publicznie dostępne w kilku
   lustrach** aktualizowanych co tydzień. Formatem możemy się więc zająć,
   zanim przyjdzie paczka ze zbieracza. Paczka właściciela pozostaje jednak
   źródłem prawdy (build Steam, hashe, pewność wersji). Czy korzystamy z luster
   w pracy, rozstrzyga **O-07** w [DECYZJE.md](DECYZJE.md).
2. **Nikt nie publikuje gotowego „indeksu” w naszym sensie** (wyciąg z
   adresami, kolejnością i kontekstem). Największe zespoły (LLC, TW) pracują na
   [ParaTranz](https://paratranz.cn): jeden plik JSON gry odpowiada tam
   jednemu plikowi projektu, a klucz tekstu to `id`/`key`/pozycja. Ich
   „indeks” to stan projektu ParaTranz, nie pliki w repozytorium.
3. **Sposób aktualizacji jest wszędzie ten sam:** porównanie nowego
   `Localize` ze starym → nowe/zmienione/usunięte → scalenie przekładów **po
   identyfikatorze, a nie po pozycji** (TW `processor.py` nazywa problem
   „file shift”). To potwierdza nasz `audit_update.py` i naturalne
   identyfikatory w adresach (`tools/localize.py`, od commita `c1ac5e0`).
4. **Brak tekstu w paczce `Lang/` daje „Unknown”, a według kazhu233 nawet
   zawieszenie gry.** Paczka musi więc mieć każdy plik i każdy element źródła
   (nieprzetłumaczone z tekstem zastępczym). To już jest zasadą w
   [LANG_FORMAT.md](LANG_FORMAT.md).
5. **Polskie znaki nie potrzebują sztuczek.** Czcionki używane przez
   społeczność (Mikodacs — autor gluk, OFL; Pretendard — OFL) mają w
   wersjach z paczek PL/IT/FR komplet `ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ` (sprawdzone
   `fontTools`, E-004). `Font/replacement_map.json` w istniejącej paczce PL
   mapuje **cyrylicę** na PUA (203 znaki, 0 polskich). Wygląda na skopiowany z
   rosyjskiej paczki i z polszczyzną nie ma związku.
6. **Kolejność fabuły da się odtworzyć**: strony `retcons/limbus-storylogs`
   ułożone w kolejności czytania dopasowaliśmy do nazw plików StoryData
   (`tools/story_order.py` → `wiedza/kolejnosc_fabuly.json`, bez tekstu gry).
   Szczegóły: [CZYTANKI.md](CZYTANKI.md).

## Lustra oryginalnych plików gry

Żadne z luster nie ma licencji; tekst należy do Project Moon. Do analizy
lokalnej (w ignorowanym `local/`) nadają się wszystkie; do Git nie trafia
z nich nic poza liczbami, nazwami plików i pól.

| Lustro | Zawartość | Świeżość (2026-11-25) | Uwagi |
|---|---|---|---|
| [LimbusTraditionalMandarin/story-data](https://github.com/LimbusTraditionalMandarin/story-data) | `kr/` 2449, `en/` 2406, `jp/` 2464 plików; nazwy z prefiksem `KR_`… jak w grze | commit co aktualizację (ostatni 2026-11-19) | **najlepszy kandydat**: pełny `Localize`, historia commitów = historia wersji gry; z tej historii TW liczy różnice (`update-kor.yml`) |
| [x1bViolet/Limbus-Localization-Files](https://github.com/x1bViolet/Limbus-Localization-Files) | gałęzie `English`, `Korean`, `Japanese`; ~2406 JSON | 2026-11-19 | układ bez prefiksów |
| [LocalizeLimbusCompany/LocalizeLimbusCompany](https://github.com/LocalizeLimbusCompany/LocalizeLimbusCompany) `EN/ KR/ JP/` | ~2090/2074/2116 plików | **nieaktualne**: `KR/` zmienione ostatnio 2026-08-06 | na nim zrobiono inspekcję E-004 |
| [LEAGUE-OF-NINE/OpenLethe](https://github.com/LEAGUE-OF-NINE/OpenLethe) `src/OpenLethe.Resources/StaticData/static-data` | **StaticData** gry (~2340 JSON `{"list": […]}`, część z BOM, jeden z przecinkiem na końcu): Teatr Opowieści, etapy, walki, Identity, umiejętności, pasywki, E.G.O | commit danych 2026-11-12 (repo 2026-11-20) | **struktura i liczby** (E-005): kolejność scen, statystyki do plików ID. Repozytorium serwera prywatnego — używamy wyłącznie danych, lokalnie (D-06) |
| [monthofjune/limbus_data](https://github.com/monthofjune/limbus_data) | przetworzone JSON Identity/umiejętności | 2026-07 | zapasowe źródło statystyk |
| flaglow/LimbusStaticData, SyxP/ObiterDicta.jl | StaticData | **nieaktualne** (2025-01 / 2024) | nie używać |

## Projekty tłumaczeń i narzędzia

| Projekt | Licencja | Co z niego bierzemy (wiedza) |
|---|---|---|
| [LocalizeLimbusCompany](https://github.com/LocalizeLimbusCompany/LocalizeLimbusCompany) (LLC, zh-CN, ~1200★) | CC BY-NC-SA 4.0 | przekład na ParaTranz (projekt 6860), oficjalnie uznany przez Project Moon; [LLC_Release](https://github.com/LocalizeLimbusCompany/LLC_Release): codzienna akcja pobiera artefakt ParaTranz i składa wydanie; `RemoteLocalizeFileList.json` (lista plików według kategorii), `NickName.json` (imiona i kolory postaci) |
| [LocalizeLimbusCompany/PRTS](https://github.com/LocalizeLimbusCompany/PRTS) | MIT | własny klon ParaTranz (serwer + baza): ciężka infrastruktura, nie dla nas |
| [LimbusTraditionalMandarin/storyline](https://github.com/LimbusTraditionalMandarin/storyline) (+ `storyline-template`) | GPL-3 | Python (`uv`), CLI `ptsd`: `update-kor.yml` porównuje `kr/` między commitami lustra (A/M/D, zmiana nazwy = D+A) i wysyła zmiany na ParaTranz z EN/JP jako kontekstem; `processor.py` przywraca przekład po `id`/`key`, potem po tekście oryginału; pomija pola `id`, `model`, `key` i oryginały złożone z samych znaczników. **Najbliższy naszemu przepływowi KR→PL** |
| [EnderDremurr/rainbus-toolbox](https://github.com/EnderDremurr/rainbus-toolbox) (RU) | GPL-3 | ~70 typowanych schematów plików (`Models/LimbusSerialization`; StoryData = `model/teller/title/place/content`); scalanie nowej wersji po `id` ze szczególnym przypadkiem `levelList`; spacja między znacznikami (`>\s+<`) psuje wyświetlanie |
| [kimght/LimbusLocalizationManager](https://github.com/kimght/LimbusLocalizationManager) | GPL-3 | instalator wielu tłumaczeń (Tauri/Rust): rejestr `data/localizations.toml` (repo, format, czcionki z MD5); szuka folderu z `StoryData` w ZIP-ie wydania; instaluje do `LimbusCompany_Data/Lang/<id>`. Społecznościowy instalator — **niepotrzebny** (paczkę instaluje się rozpakowaniem folderu); najwyżej opcjonalny kanał, gdyby właściciel chciał udostępnić przekład innym |
| [kazhu233/Limbus-Company-Translation-Merge](https://github.com/kazhu233/Limbus-Company-Translation-Merge) | brak | uzupełnia brakujące `id` z oryginału po aktualizacji gry, „żeby nie było Unknown i zawieszeń” |
| [SunZheee/LimbusCompany-Bilingual-zh-CN](https://github.com/SunZheee/LimbusCompany-Bilingual-zh-CN) | brak (tekst CC BY-NC-SA) | paczka dwujęzyczna EN+ZH: `StoryFields.json` = 13 wzorców plików fabularnych (StoryData, AbnormalityGuides, StoryTheater*, DanteNote*, Egos, Personalities…) i pola wykluczone (`id`, `codeName`, `abilityID`, `model`, `fileName`, `level`); skrypty PowerShell scal/zweryfikuj. **Wzór dla Czytanek dwujęzycznych** |
| [x1bViolet/Limbus-Localization-UI](https://github.com/x1bViolet/Limbus-Localization-UI) | MIT | edytor z podglądem dla `Skills`, `Passives`, `EGOgift`, `Bufs`/`BattleKeywords`, `AbnormalityGuides`; własny parser znaczników TMP i słów kluczowych; dokumentacja na GitBook. Może się przydać tłumaczowi do podglądu opisów umiejętności |
| [i-ribas/DesconversorCLT](https://github.com/i-ribas/DesconversorCLT) (PT-BR) | MIT | pobiera przekład z API ParaTranz i składa paczkę |
| [retcons/limbus-storylogs](https://github.com/retcons/limbus-storylogs) | brak | strony fabuły (34) w kolejności czytania; z nich odtworzyliśmy kolejność plików |
| [Echodial/Limbus-Company-PL-Tlumaczenie](https://github.com/Echodial/Limbus-Company-PL-Tlumaczenie) | brak | istniejące fanowskie tłumaczenie PL (folder `Polish`, ~1980 plików; Selva Obscura, Canto I, część Identity) — **tylko technika, zero tekstu**; nasza nazwa języka musi się różnić (O-01) |
| [Eden-Office/LimbusCompanyBusFR](https://github.com/Eden-Office/LimbusCompanyBusFR) | brak | pełny układ paczki `Lang/fr` (~2423 JSON) |
| Inne paczki `Lang/` (IT `louzhee`, TH `stlinx`, RU Crescent/MTL/Divine, ES Dreams-Office, RCR) | różne / brak | `config.json`: `lang` + `titleFont`/`contextFont` (nazwa czcionki albo pusty ciąg), `samplingPointSize` 78, `padding` 2–8; TH ma tylko `lang`; w RU MTL paczka = sama zawartość folderu języka |
| jinglejingle3344/LCB-translation-randomizer | — | usuwanie prefiksów `EN_`/`KR_`/`JP_` przy kopiowaniu do `Lang/` |
| [Ogłoszenie Project Moon, 2025-03-31](https://store.steampowered.com/news/app/1973530/view/533220039674824263) | — | oficjalny mechanizm Custom Language ([FEASIBILITY.md](FEASIBILITY.md)) |
| Poradniki PT-BR / RU / FR, gitbook „Limbus Custom Language” | — | brak ryzyka bana; jedna czcionka na slot; część tekstów nieprzetłumaczalna; `Bufs`/`BattleKeywords`/`SkillTag` z fallbackiem do `Localize/en` (do sprawdzenia) |

Nie pobierano (do ewentualnego sprawdzenia): narzędzia iOS, mapery ID,
konwertery JSON→CSV, talia Anki.

## Co przejmujemy, a czego nie

| Przejmujemy (jako wiedzę lub wzorzec) | Nie przejmujemy |
|---|---|
| porównanie wersji po commitach lustra i scalanie po `id`/`key` (TW) | ParaTranz/PRTS: przy jednym tłumaczu i pakietach Markdown to zbędna infrastruktura (opcja na przyszłość, gdyby zespół urósł) |
| lista pól niebędących tekstem (`model`, `id`, `key`, `level`, kody kolorów, ikony) | tekst przekładów innych zespołów (także jako „podpowiedzi” dla tłumacza) |
| zakres plików fabularnych dla Czytanek (SunZheee) | kod GPL (rainbus, TW, kimght) |
| kolejność stron fabuły (storylogs) jako dane wejściowe, zweryfikowane regułą nazw | |
| czcionki OFL, które już mają polskie znaki (decyzja O-03) | |
| Teatr Opowieści i tabele etapów/walk ze StaticData jako źródło chronologii (E-005) | kopie tabel StaticData w repozytorium (OpenLethe bez licencji) |

Projekty właściciela, z których przejęliśmy sposób pracy: WWM i SRW
([LESSONS.md](../LESSONS.md)).
