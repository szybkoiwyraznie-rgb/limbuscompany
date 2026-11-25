# Czytanki

Materiały **do czytania przez właściciela jako gracza** — fabuła i lore
Limbus Company w wygodnej formie, niezależnie od postępu przekładu. Wzorzec:
czytanki WWM i SRW Y (HTML/DOCX, kolejność gry, mówcy, jawne luki).

## Planowane serie

| Seria | Źródło | Zawartość |
|---|---|---|
| **Fabuła** | `StoryData` | Prolog, Canto, Intervallo, wydarzenia — sceny w kolejności, z mówcą i miejscem |
| **Sinnerzy i Identity** | pliki postaci/osobowości, kwestie głosowe | dla każdej Identity: opis, historia (jeśli jest), kwestie |
| **E.G.O** | pliki E.G.O | opisy, kwestie, powiązane Abnormality |
| **Miasto (lore)** | opisy przedmiotów, słowa kluczowe, teksty interfejsu | słowniczek pojęć: Skrzydła, Dystrykty, Palce… |

Każda Czytanka ma wersję **EN** (od razu po pierwszym wyciągu) i później
**PL** (z przyjętego przekładu, z angielskim tam, gdzie przekładu brak —
oznaczonym).

## Zasady

- Budowane **tylko z `index/` i `tlumaczenie/`** (planowany
  `tools/czytanki.py`), z manifestem buildu.
- Kolejność opiera się na danych gry (identyfikatory scen, nazwy plików,
  ewentualne tabele kolejności). Niepewność kolejności = jawna uwaga w
  dokumencie, nie zgadywanie.
- Format i układ ustala właściciel (O-04). **Po akceptacji układ jest
  zamrożony** (lekcja SRW Y).
- Czytanki z tekstem gry są prywatne: trafiają na Dysk właściciela, nie do Git
  (w Git — generator i ewentualnie mały przykład na danych wymyślonych).

## Kolejność fabuły (stan wiedzy)

Plik **[`wiedza/kolejnosc_fabuly.json`](../wiedza/kolejnosc_fabuly.json)**
zawiera 34 strony (rozdziały) w kolejności czytania i przypisane do nich pliki
StoryData. Są tam tylko nazwy plików i liczby, bez tekstu gry. Powstał
narzędziem `tools/story_order.py`: unikalne linie `content` z plików EN
dopasowano do stron fanowskiej biblioteki
[retcons/limbus-storylogs](https://github.com/retcons/limbus-storylogs),
ułożonych w kolejności jej spisu (E-004).

- Przypisano **728 z 922** plików StoryData (lustro LLC, 2026-08-06).
  Nieprzypisane: 173 pliki `P1SSNN` (12 serii po ~14 plików; najpewniej
  historie Sinnerów, których biblioteka nie zawiera), `E000X`–`E003X`, kilka
  `S…`/`3D…` i `ProjectGS`.
- **Reguła nazw** (hipoteza sprawdzona na danych): wewnątrz rozdziału
  `S` < `nD` < `E` < `ES` < `PC` < `P`, potem numer, potem faza
  `B` < `I`, `I1`, `I2`… < `A` (prawdopodobnie *before* / *in* / *after*
  względem walki lub etapu); `X` = samodzielne opowiadanie. Zgodność z kolejnością biblioteki:
  **685 z 694** sąsiednich par. Wyjątki dotyczą głównie scen przeplatanych
  (np. `S643B` przed `S641I`) i plików `ES` w Intervallo 8.5.
- Znaczenie nazw: `S0xx` = Prolog; `SNxx` + `ND…` = Canto N (sceny i
  lochy/eksploracja); `ENxx` = Intervallo N.5 (6.5 i 9.5 mają po dwie
  części: `E615`/`E616`, `E914`/`E915`); `E0NNX` = opowiadania i Noce
  Walpurgii; `E701`–`E717` i `E718`–`E728` = dwa wydarzenia po Canto 7;
  `ES…` = część Intervallo 8.5; `PC01`–`PC14` = wydarzenie
  współpracy (Arknights).
- Biblioteka kończy się na Intervallo 9.5. **Nowsze rozdziały** trzeba
  ułożyć regułą nazw i sprawdzić na paczce właściciela.

| # | Rozdział | Pliki | Od … do |
|---|---|---|---|
| 1 | Prolog | 7 | `S001B` … `S004A` |
| 2 | Canto 1 | 30 | `S101B` … `1D306A` |
| 3 | Canto 2 | 26 | `S201B` … `2D306A` |
| 4 | Canto 3 | 34 | `S301B` … `3D309A` |
| 5 | Intervallo 3.5 | 11 | `E301B` … `E306A` |
| 6 | Opowiadanie: dantes_notes | 3 | `E010X` … `E030X` |
| 7 | Canto 4 | 57 | `S401B` … `4D305A` |
| 8 | Intervallo 4.5 | 10 | `E401B` … `E407A` |
| 9 | Opowiadanie: past_the_backdoor | 2 | `E041X` … `E042X` |
| 10 | Canto 5 | 70 | `S501B` … `5D304A` |
| 11 | Opowiadanie: notable_change | 1 | `E050X` … `E050X` |
| 12 | Intervallo 5.5 (miracle) | 13 | `E501B` … `E509B` |
| 13 | Opowiadanie: walpurgis2 | 2 | `E051X` … `E052X` |
| 14 | Opowiadanie: back2bus | 1 | `E053X` … `E053X` |
| 15 | Intervallo 5.5 (ycgd) | 15 | `E510B` … `E519A` |
| 16 | Opowiadanie: risklevel | 1 | `E054X` … `E054X` |
| 17 | Canto 6 | 63 | `S601B` … `S648A` |
| 18 | Opowiadanie: walpurgis3 | 2 | `E061X` … `E062X` |
| 19 | Intervallo 6.5 (timekilling) | 19 | `E601B` … `E615A` |
| 20 | Opowiadanie: familiarsiren | 1 | `E063X` … `E063X` |
| 21 | Intervallo 6.5 (warp) | 15 | `E616B` … `E627B` |
| 22 | Opowiadanie: walpurgis4 | 2 | `E064X` … `E065X` |
| 23 | Canto 7 | 66 | `S701B` … `7D112A` |
| 24 | Opowiadanie: walpurgis5 | 2 | `E070X` … `E071X` |
| 25 | Opowiadanie: checkup | 23 | `E701B` … `E717A` |
| 26 | Opowiadanie: nocturnalsweeping | 19 | `E718B` … `E728B` |
| 27 | Canto 8 | 68 | `S801B` … `S833A` |
| 28 | Opowiadanie: walpurgis6 | 3 | `E080X` … `E082X` |
| 29 | Intervallo 8.5 | 47 | `E801B` … `E812B` |
| 30 | Opowiadanie: arknights | 19 | `PC01B` … `PC14A` |
| 31 | Canto 9 | 59 | `S901B` … `S951B` |
| 32 | Opowiadanie: walpurgis8 | 2 | `E090X` … `E091X` |
| 33 | Intervallo 9.5 | 17 | `E901B` … `E914B` |
| 34 | Intervallo 9.5 (2) | 18 | `E915B` … `E927B` |

## Otwarte pytania

- Gdzie są tytuły rozdziałów i scen: pole `title` w StoryData (14 350 tekstów
  EN) czy pliki `StoryTheater*`/`ChapterBannerConfig`?
- Gdzie są historie Identity (osobny plik? tekst w opisach `Personalities`?).
- Zakres plików „fabularnych” poza StoryData. Punkt wyjścia: lista 13 wzorców
  z paczki dwujęzycznej SunZheee ([PRIOR_ART.md](PRIOR_ART.md)) —
  `AbnormalityGuides*`, `StoryTheater*`, Dante's Notes, `Egos*`,
  `Personalities*`.
