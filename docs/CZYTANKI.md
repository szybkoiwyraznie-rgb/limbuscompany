# Czytanki

Materiały **do czytania przez właściciela jako gracza** — fabuła i lore
Limbus Company w „ludzkim” układzie, niezależnie od postępu przekładu. Wzorzec:
czytanki SRW (OE/Y: `srwy_episode_NN_PL.md`, `srwy_mission_deployments.md`).
Decyzja o układzie: [DECYZJE.md](DECYZJE.md) D-07.

## Serie

| Seria | Narzędzie | Zawartość | Stan |
|---|---|---|---|
| **Fabuła** | `tools/build_reading.py` | jeden plik na rozdział (Prolog, Canto, Intervallo, opowiadania) w kolejności gry | **prototyp** — [`czytanki/fabula_EN`](../czytanki/fabula_EN/00_spis_EN.md), [`czytanki/fabula_KR`](../czytanki/fabula_KR/00_spis_KR.md) (po 36 rozdziałów), [`czytanki/fabula_PL`](../czytanki/fabula_PL/00_spis_PL.md) (PL + fallback EN) |
| **Plik ID (Identity)** | `tools/build_profiles.py` | jeden plik na Grzesznika: akta, katalog Identity, profile z liczbami, umiejętnościami, pasywkami i kwestiami | **prototyp** — `czytanki/plik_ID_EN`, `czytanki/plik_ID_KR`, `czytanki/plik_ID_PL` (PL + fallback EN) |
| **E.G.O** | `tools/build_ego.py` | jeden plik na Grzesznika: karty E.G.O (Przebudzenie/Erozja/warianty sezonowe, statystyki per Uptie, opisy monet), pasywki z wymaganiami, kwestie E.G.O | **prototyp** — `czytanki/plik_EGO_PL` (PL + fallback EN, 12 plików) |
| **Miasto (lore)** | planowane | słowniczek pojęć: Skrzydła, Dystrykty, Palce… | planowane |

Każda Czytanka ma wersję **EN** lub **KR** od razu, a później **PL** (z
przyjętego przekładu; tam, gdzie przekładu brak — tekst EN, oznaczony).

## Układ Czytanki fabularnej

```text
# Limbus Company — Canto I: The Outcast
*rok 984-01 · D Corp. · District 4*                      ← StageChapterText
> I was given the role of Manager. …                      ← motto z Teatru Opowieści
> **Uwaga dla czytelnika:** wersja językowa, źródło kolejności, luki
## Sceny fabularne
### Etap 1-1 · Vroom-vroom                                ← StageNode: numer i tytuł etapu
*Miejsce: Mephistopheles*
> The ride is awkward and intimidating. …                 ← opis etapu z gry
*— Przed walką —*                                         ← moment: przed / w trakcie walki / po walce
#### Aboard Mephistopheles                               ← zmiana miejsca w scenie (place)
**Charon:** Verg.                                         ← mówca jak w SRW (pojedynczy \n między kwestiami)
**Dongrang** (*K Corp. Dept. of Food Resource Development*): …   ← epitet przy pierwszym wystąpieniu w scenie
The chatter was what finally got me to open my eyes.      ← narracja: zwykły wiersz w scenie
**Dante:** Hey...                                        ← kwestie Dantego bez nawiasów <…>
```

- **Pojedynczy znak nowej linii (`\n`)** między kolejnymi kwestiami i narracją
  w obrębie sceny/miejsca (jak w czytankach WWM/SRW); pusta linia oddziela
  dopiero zmianę miejsca, moment walki i kolejną scenę.
- **Kwestie Dantego bez `<` i `>`** — w grze nawiasy ostre oznaczają tykanie
  zegara, w Czytance są zdejmowane (w pakiecie dla tłumacza i w `Lang/` zostają).
- **Mówca i epitet `"Me"` → `"Ja"`** w prologu przed poznaniem imienia Dantego.
- **Cenzura / luki w pamięci (`■…`) → `***`** — ciągi czarnych kwadratów z
  plików gry zastępowane są w Czytance i plikach ID zapisem `***`.
- **Bez identyfikatorów w tekście**; nazwa pliku sceny jest tylko w
  niewidocznym komentarzu HTML (do sprawdzania).
- Sceny eksploracji (lochy `nD…`) mają nagłówek „Eksploracja”; rozdziały z
  rozgałęzieniami (Canto X) — oznaczenie trasy A/B/C.
- `00_spis_EN.md` — spis rozdziałów z liczbą scen i kwestii.

## Układ pliku ID (profile Identity)

```text
# Limbus Company — Yi Sang: Identity
## Zakres i zasady odczytu        ← co znaczą liczby, czego nie ma (E.G.O, bonusy)
## Akta więźnia                   ← IntroduceCharacter
## Katalog Identity               ← tabela: rzadkość, Identity, sezon, grzech, słowa kluczowe
## Profile
### 00 Molar Office Fixer — Yi Sang
| Parametr | Wartość bazowa |     ← rzadkość, sezon, HP (+za poziom), szybkość per ulepszenie,
                                    poziom obrony, odporności (×0,5 Endured…), progi Stagger,
                                    grzech wyróżniony, przynależność, słowa kluczowe
#### Umiejętność 1 (×3): Stay Calm
| Ulepszenie | Grzech | Typ | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
*Od ulepszenia 2:* opis ze słowami kluczowymi ([Tremor], [On Use]) i opisy monet
#### Obrona: Guard
#### Pasywka bojowa / wsparcia   ← od którego ulepszenia, wymaganie (posiadane / rezonans N× grzech)
#### Kwestie                      ← PersonalityVoiceDlg: sytuacja + kwestia
```

Liczby pochodzą z tabel `StaticData` (lustro OpenLethe, tylko lokalnie — D-06),
opisy z `Localize`. Kolejne ulepszenia nadpisują tylko zmienione pola, więc
narzędzie składa je kumulatywnie i pokazuje tylko wiersze, w których coś się
zmienia.

## Układ pliku E.G.O

```text
# Limbus Company — Yi Sang: E.G.O
## Zakres i zasady odczytu        ← co znaczą liczby, czego nie ma
## Katalog E.G.O                  ← tabela: karta, podtytuł („Podstawowe/Wyłączny…”)
## Karty
### 4. Płomyk Zapałki
*Wyłączny Sprzęt E.G.O Yi Sanga*                          ← podtytuł z tabeli `Egos`
#### Przebudzenie: 4. Płomyk Zapałki                      ← `skillType` = EGO_AWAKEN
| Ulepszenie | Grzech | Typ | Moc bazowa | Moc monety | … |  ← Uptie 1/3/4, zmienne wiersze
*Od ulepszenia N:* opis + opisy monet
#### Erozja: …                                            ← `skillType` = EGO_EROSION, gdy karta ją ma
#### Wariant: …                                           ← sezonowe warianty danych (np. a1c9p3)
#### Pasywka: <nazwa>
*Wymagania: przebudzenie E.G.O na poziomie 2*             ← `passive-ego` requireIDList
opis pasywki
## Kwestie E.G.O                  ← EGOVoiceDig: sytuacja + kwestia (per Grzesznik)
```

## Wersja PL (fallback EN)

Wersje `*_PL` Czytanek łączą przekład z oryginałem: tam, gdzie przekładu
jeszcze nie ma (wpis AI-tymczasowe lub Tłumacza), tekst pozostaje
**angielski**. Czytanka fabularna mówi to wprost w „Uwadze dla czytelnika”
(liczba scen jeszcze nieprzetłumaczonych), a pliki ID i E.G.O — w „Zakresie
i zasadach odczytu”. Dane PL budowane są z produkcyjnej paczki
`Lang/Polski` (fallback EN jest w niej wbudowany per wpis); wiersz
`Uwaga` przy scenach bez przekładu pochodzi z porównania z tabelami EN.

## Zasady

- Kolejność opiera się na danych gry ([`wiedza/indeks_fabuly.json`](../wiedza/indeks_fabuly.json)).
  Niepewność = jawna uwaga w dokumencie, nie zgadywanie.
- Układ zaakceptowany przez właściciela jest **zamrożony** (lekcja SRW Y);
  bieżący jest propozycją do akceptacji (O-04).
- Czytanki są częścią projektu i leżą w repozytorium: `czytanki/fabula_EN`,
  `czytanki/fabula_KR` (fabuła) i `czytanki/plik_ID_EN`, `czytanki/plik_ID_KR`
  (pliki ID), zbudowane z `index/` ([INDEX_FORMAT.md](INDEX_FORMAT.md)). Po zmianie `index/` lub
  generatorów budujemy je od nowa i commitujemy razem.
- **Formatowanie tabel (konwencja mtgcrawler, zaakceptowana przez właściciela):**
  wszystkie tabele Markdown w Czytankach są składane przez
  `tools/md_table_align.py` (genery wywołują `align_markdown_tables` przed
  zapisem) — kolumny `|` wyrównane w pionie dla edytora o stałej szerokości
  znaków, budżet szerokości linii 216 komórek, długa ostatnia kolumna
  zawijana z 2-spacjowym wcięciem kontynuacji, kolumny liczbowe/indeksowe
  (`#`, `Slot`, `Ulepszenie`, `Rzadkość`, `Sezon`, liczniki, moce) prawostronnie
  przez `---:`, tekstowe lewostronnie. Weryfikacja: ponowne przejście
  alignera na plikach jest operacją tożsamościową.
- **Bez czysto technicznych znaczników:** identyfikatory scen (`<!-- S001B -->`)
  nie trafiają do tekstu Czytanki — granice scen wyznaczają nagłówki etapów
  i dopiski faz (`*— Przed walką —*`); test `test_reading_layout` kotwiczy
  zakaz `<!--` w wydaniu.

## Kolejność fabuły

Plik **[`wiedza/indeks_fabuly.json`](../wiedza/indeks_fabuly.json)** (narzędzie
`tools/story_index.py`) zawiera rozdziały w kolejności czytania i sceny w
każdym z nich jako identyfikatory (numery rozdziałów, węzłów etapów, walk,
nazwy plików scen i moment); teksty dokłada generator z `index/`. Źródła, w kolejności
ważności (E-005):

1. **Teatr Opowieści** gry (`storytheater-main`, `storytheater-other`): lista
   scen każdego rozdziału w kolejności z menu gry, z węzłem etapu i momentem
   (`Before`/`After`/`Inter`); opowiadania i Intervalla mają `sortingOrder` i
   warunek odblokowania.
2. `StageChapterText` (Localize): oficjalna kolejność rozdziałów z datami w
   świecie gry; Canto wstawiamy przed pierwszym Intervallem/opowiadaniem, które
   według tej listy lub warunku odblokowania jest po nim.
3. Powiązania etap → scena (`story`) dla bieżącego Canto, którego Teatr jeszcze
   nie wymienia.
4. Sceny w trakcie walk (`battle-story`, `battle-ab`: `enter` → `others` →
   `exit`) — wstawiane za sceną otwierającą walkę.
5. Reguła nazw (z E-004) dla reszty scen tej samej rodziny (np. trasy Canto X z
   `RPGSystem/EndingRoute*`).

Wynik na lustrze (1002 pliki StoryData): **808 scen w 36 rozdziałach**
(667 z Teatru, 5 z etapów, 82 z walk, 54 z reguły nazw), **184 historie
Identity** (osobno, po Grzeszniku) i **11 bez miejsca** (`E000X`–`E003X` —
samouczki, `RPG1`, `S9991B`/`S9992B`). Kolejność 34 rozdziałów wspólnych z
fanowską biblioteką storylogs (E-004) jest **identyczna**; doszły Canto X i
10. Noc Walpurgii. Wcześniejszy heurystyczny plik
[`wiedza/kolejnosc_fabuly.json`](../wiedza/kolejnosc_fabuly.json) zostaje jako
niezależne sprawdzenie.

Ograniczenie: w Canto X (eksploracja z trzema trasami) kolejność scen tras
wynika z numeracji plików, nie z przejścia gry; Czytanka mówi to wprost.

| # | Rozdział (id) | Grupa | Scen | Od … do |
|---|---|---|---|---|
| 1 | Prologue (100) | canto | 7 | `S001B` … `S004A` |
| 2 | Canto I (101) | canto | 32 | `S101B` … `1D306A` |
| 3 | Canto II (102) | canto | 30 | `S201B` … `2D306A` |
| 4 | Canto III (103) | canto | 36 | `S301B` … `3D309A` |
| 5 | Intervallo I (9103) | intervallo | 11 | `E301B` … `E306A` |
| 6 | Opowiadanie (9010) | opowiadanie | 3 | `E010X` … `E030X` |
| 7 | Canto IV (104) | canto | 57 | `S401B` … `4D305A` |
| 8 | Intervallo II (9104) | intervallo | 10 | `E401B` … `E407A` |
| 9 | Opowiadanie (9011) | opowiadanie | 2 | `E041X` … `E042X` |
| 10 | Canto V (105) | canto | 70 | `S501B` … `5D304A` |
| 11 | Opowiadanie (9012) | opowiadanie | 1 | `E050X` … `E050X` |
| 12 | Intervallo III (9105) | intervallo | 13 | `E501B` … `E509B` |
| 13 | Opowiadanie (9013) | opowiadanie | 2 | `E051X` … `E052X` |
| 14 | Opowiadanie (9014) | opowiadanie | 1 | `E053X` … `E053X` |
| 15 | Intervallo III (9107) | intervallo | 15 | `E510B` … `E519A` |
| 16 | Opowiadanie (9015) | opowiadanie | 1 | `E054X` … `E054X` |
| 17 | Canto VI (106) | canto | 64 | `S601B` … `S648A` |
| 18 | Opowiadanie (9016) | opowiadanie | 2 | `E061X` … `E062X` |
| 19 | Intervallo IV (9109) | intervallo | 19 | `E601B` … `E615A` |
| 20 | Opowiadanie (9017) | opowiadanie | 1 | `E063X` … `E063X` |
| 21 | Intervallo IV (9110) | intervallo | 15 | `E616B` … `E627B` |
| 22 | Opowiadanie (9018) | opowiadanie | 2 | `E064X` … `E065X` |
| 23 | Canto VII (107) | canto | 66 | `S701B` … `7D112A` |
| 24 | Opowiadanie (9019) | opowiadanie | 2 | `E070X` … `E071X` |
| 25 | Intervallo V (9114) | intervallo | 23 | `E701B` … `E717A` |
| 26 | Intervallo V (9116) | intervallo | 19 | `E718B` … `E728B` |
| 27 | Canto VIII (108) | canto | 68 | `S801B` … `S833A` |
| 28 | Opowiadanie (9020) | opowiadanie | 3 | `E080X` … `E082X` |
| 29 | Intervallo VI (9119) | intervallo | 47 | `E801B` … `E812B` |
| 30 | 8.5-EX (9120) | intervallo | 19 | `PC01B` … `PC14B` |
| 31 | Canto IX (109) | canto | 60 | `S901B` … `S951B` |
| 32 | Opowiadanie (9021) | opowiadanie | 2 | `E090X` … `E091X` |
| 33 | Intervallo VII (9125) | intervallo | 17 | `E901B` … `E914B` |
| 34 | Intervallo VII (9127) | intervallo | 18 | `E915B` … `E927B` |
| 35 | Canto X (110) | canto | 65 | `S1000B` … `S1043C` |
| 36 | Opowiadanie (9022) | opowiadanie | 5 | `E100X` … `E103X` |

## Odpowiedzi i otwarte pytania

- ~~Gdzie są tytuły rozdziałów i scen?~~ **Rozwiązane (E-005):** rozdziały w
  `StageChapterText` i `StoryTheaterMain/Other`; etapy w `StageNode*`; pole
  `title` w StoryData to **epitet mówcy** (np. „K Corp. Dept. of Food Resource
  Development” nad imieniem Dongranga), nie tytuł sceny.
- ~~Gdzie są historie Identity?~~ **Rozwiązane:** pliki `P1SSNN` w StoryData,
  przypisanie do Identity w `storytheater-personality` (StaticData).
- Zakres plików „fabularnych” poza StoryData: Dante's Notes
  (`storytheater-dantenote`), `AbnormalityGuides*`, `Egos*`, opisy E.G.O —
  do kolejnej serii.
- Jak Czytanka ma pokazywać trasy Canto X (osobne pliki na trasę czy jeden
  plik z oznaczeniami) — do decyzji właściciela po lekturze próbki.

## „Plik META” — elementy spoza trzech głównych grup (E-020)

Czwarta seria (`tools/build_meta.py` → `czytanki/plik_META_PL`, 6 plików)
zbiera teksty spoza fabuły, kart Tożsamości i kart E.G.O:

* `01_teksty_z_misji_PL` — teksty tutoriali bojowych pogrupowane po etapach
  (`Etap 0-1 · …` z tytułami z `StageNode`; źródła `TutorialRenewalDesc`
  i `TutorialRenewalMainUIDesc` [fragment `tuto_10108`]), poradniki poza
  misjami (Lochy Wydobywcze, lobby, Lustrzane Lochy, przegląd Tożsamości
  i E.G.O), wskazówki w walce (`BattleHint*`) i okna pop-up tutoriali
  (`TutorialPopUpDesc`);
* `02_notatki_dantego_PL` — hasła glosariusza świata (`StoryTheaterDanteNote*`)
  i pełne pierwszoosobowe wpisy („Zapiski”, `StoryTheaterDanteNoteDetail*`);
  wpisy bez przekładu pozostają w oryginale;
* `03_splashe_pobierania_PL` — ekrany z lore Miasta podczas pobierania
  patcha (`FileDownloadDesc`);
* `04_akta_grzesznikow_PL` — akta osobowe Grzeszników #1–#12
  (`IntroduceCharacter`; imiona z `Characters`);
* `05_piosenki_PL` — słowa piosenek z tabel `BgmLyrics` (piosenka Prologu
  `BgmLyrics_Pv`, motywy bossów, utwory z napisów końcowych); tytuły =
  identyfikatory plików gry, wiersze w kolejności tabeli;
Poza zakresem: `TutorialMainUIText` (przechadzki po interfejsie),
`TutorialMirrorDungeon`, starsze zestawy `TutorialDesc*` (poprzednia wersja
tutoriali).

## „Deploymenty” — przeciwnicy etapów (E-021)

Piąta seria (`tools/build_deployments.py` → `czytanki/deployment_PL`,
31 plików + spis; wzór SRW `srwy_mission_deployments.md`) — dla **każdego
etapu** lista fal przeciwników i pełne karty tych jednostek (dane celowo się
powtarzają między etapami):

* pliki grupują etapy według kolejności fabuły, jak seria `fabula_PL`
  (Prolog → Canto I–X → Intervallo → Noce Walpurgii → inne wydarzenia →
  zestaw wspólny); tytuły części zgodne ze spisem `fabula_PL`;
* fale: `battle-story` (walka fabularna; id wiersza = id misji, w rozdziale 1
  wiersze są przesunięte o +1 — mapowanie kotwicami skryptów
  `TutorialRenewal_C_N` z E-025; etapy czysto fabularne jak 1-1 nie mają
  wiersza i nie renderują się wcale), uzupełniająco `battle-ab` — jego id NIE
  są id misji (podrozdział + porządkowy numer spotkania): pliki wydarzeń
  przypisywane po id etapu jak dotąd, rozdziały główne tylko zakotwiczone
  skryptem (Loch D-02 = etap 1-11 jako „Spotkanie N”), reszta → sekcja
  „Spotkania z Anomalią — Canto N” na końcu pliku rozdziału (E-025);
* karty bez technicznych identyfikatorów (E-023): nagłówki „Nazwa” zamiast
  „Nazwa — id NNN”; statystyki (poziom, HP z przyrostem, szybkość, sloty
  akcji, progi oszołomienia, poczytalność z progami Niskiego
  Morale/Paniki, typ paniki wg `PanicInfo`, odporności), efekty Niskiego
  Morale i Paniki, opis, umiejętności (grzech/typ/moc bazowa/moc
  monety/monety/cele per poziom; nazwy PL po E-022, także z
  `Skills_Tutorial`; „(bez nazwy)” gdy danych brak), pasywki wymieniane
  tylko gdy istnieją (bez pustych sekcji); Anomalie z częściami
  (per część HP/odporności/opis/umiejętności);
* pule jednostek: tabele StaticData `enemy` i `abnormality-unit` poza
  proceduralnymi Lustrzanymi Lochami (`mirrordungeon*`, `schema-craft`,
  `shadowenemy`); jednostki nieoczekujące w żadnym etapie lądują w puli na
  końcu pliku swojej części; nieużywane jednostki `enemy.json` → plik
  `31_zestaw_wspolny_PL`;
* nazwy jednostek mapowane przez pole `nameID` (787 wrogów/anomalii +
  321 wierszy enemy); „jednostka NNNNN” = celowo nienazwane w danych
  (np. bestie Prologu 0-1: Panther/Lion/Wolf);
* mapowanie części na etapy z plików `StageNode*` (`StageNode1-N` = Canto N,
  `StageNode1-0` = Prolog, `StageNode91-N` = id 91NNxx); etykiety
  walpurgijskich/wydarzeniowych części zweryfikowane tytułami StageNode
  i spisem fabuły (tkt = Czas zabijania czasu, mowe = Warp Express,
  ycgd = Poświęcić ciało, twth = Splatanie nici, exme = Pamięć
  doświadczeń, 91-14/91-24 = Okresowe badania LCB).

## Odtworzenie

```sh
python tools/story_index.py                       # index/ → wiedza/indeks_fabuly.json
python tools/build_reading.py --lang en           # → czytanki/fabula_EN/
python tools/build_reading.py --lang kr           # → czytanki/fabula_KR/
python tools/build_profiles.py --lang en          # → czytanki/plik_ID_EN/
python tools/build_profiles.py --lang kr          # → czytanki/plik_ID_KR/
python tools/build_meta.py --lang en              # → czytanki/plik_META_EN/
python tools/build_meta.py --lang kr              # → czytanki/plik_META_KR/
```

Domyślnym wejściem jest `index/` ([INDEX_FORMAT.md](INDEX_FORMAT.md)); można
podać inny katalog lub ZIP zbieracza jako argument.

Wersje PL buduje się ze snapshotu `Lang/Polski` (paczka produkcyjna,
fallback EN wbudowany per wpis) podanego jako katalog z podkatalogami
`pl/`, `en/`, `kr/`:

```sh
# 1) rozpakuj paczkę produkcyjną do podkatalogu pl/ snapshotu:
python tools/build_lang.py --unpack-to local/lang_pl_v3
#    (LimbusCompany_Data/Lang/Polski → local/cz_snapshot/pl)
# 2) uzupełnij brakujące tabele kopiami z index/localize/en (fallback EN),
#    zachowując podkatalogi (np. EGOVoiceDig/);
# 3) zbuduj wszystkie trzy serie PL:
python tools/build_reading.py  local/cz_snapshot --lang pl   # → czytanki/fabula_PL/
python tools/build_profiles.py index/static-data local/cz_snapshot --lang pl  # → czytanki/plik_ID_PL/
python tools/build_ego.py      index/static-data local/cz_snapshot --lang pl  # → czytanki/plik_EGO_PL/
python tools/build_meta.py     local/cz_snapshot --lang pl   # → czytanki/plik_META_PL/ + deployment_PL/
```

Snapshot (`local/cz_snapshot/`) i rozpakowana paczka
(`local/lang_pl_v3/`) są w pełni regenerowalne i nie trafiają do Git
(zignorowane w `.gitignore`).
