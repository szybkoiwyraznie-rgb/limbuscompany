# Czytanki

Materiały **do czytania przez właściciela jako gracza** — fabuła i lore
Limbus Company w „ludzkim” układzie, niezależnie od postępu przekładu. Wzorzec:
czytanki SRW (OE/Y: `srwy_episode_NN_PL.md`, `srwy_mission_deployments.md`).
Decyzja o układzie: [DECYZJE.md](DECYZJE.md) D-07.

## Serie

| Seria | Narzędzie | Zawartość | Stan |
|---|---|---|---|
| **Fabuła** | `tools/build_reading.py` | jeden plik na rozdział (Prolog, Canto, Intervallo, opowiadania) w kolejności gry | **prototyp** (36 rozdziałów EN/KR z lustra) |
| **Plik ID (Identity)** | `tools/build_profiles.py` | jeden plik na Grzesznika: akta, katalog Identity, profile z liczbami, umiejętnościami, pasywkami i kwestiami | **prototyp** (12 plików EN z lustra) |
| **E.G.O** | planowane (to samo narzędzie) | opisy, statystyki, kwestie, powiązane Abnormality | planowane |
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
**Charon:** Verg.                                         ← mówca jak w SRW
**Dongrang** (*K Corp. Dept. of Food Resource Development*): …   ← epitet przy pierwszym wystąpieniu w scenie
The chatter was what finally got me to open my eyes.      ← narracja: zwykły akapit
**Dante:** \<Hey...>                                     ← tykanie Dantego zostaje w nawiasach
```

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

## Zasady

- Kolejność opiera się na danych gry ([`wiedza/indeks_fabuly.json`](../wiedza/indeks_fabuly.json)).
  Niepewność = jawna uwaga w dokumencie, nie zgadywanie.
- Układ zaakceptowany przez właściciela jest **zamrożony** (lekcja SRW Y);
  bieżący jest propozycją do akceptacji (O-04).
- Czytanki z tekstem gry są prywatne: `local/` albo Dysk właściciela, nie Git
  (w Git — generatory i testy na danych wymyślonych).

## Kolejność fabuły

Plik **[`wiedza/indeks_fabuly.json`](../wiedza/indeks_fabuly.json)** (narzędzie
`tools/story_index.py`) zawiera rozdziały w kolejności czytania i sceny w
każdym z nich — **tylko identyfikatory** (numery rozdziałów, węzłów etapów,
walk, nazwy plików scen i moment), bez tekstu gry. Źródła, w kolejności
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
