# Metoda i indeksy przejęte z innych projektów

Decyzja właściciela (2026-11-25): **nie wymyślamy od nowa** — przejmujemy
metody i indeksy sprawdzone w innych projektach tłumaczeń Limbus Company i
dostosowujemy je do naszego przypadku (źródło **KR**, przekład zewnętrznego
Tłumacza, zapas **EN**, dostawa na Dysk). Przegląd projektów i ich licencje:
[PRIOR_ART.md](PRIOR_ART.md).

Zasada: przejmujemy **reguły, schematy i układ danych**, a kod piszemy od
nowa. Nie kopiujemy kodu z repozytoriów bez licencji ani tekstów przekładów.

Oznaczenia: **[P]** potwierdzone w co najmniej dwóch niezależnych projektach,
**[1]** tylko w jednym projekcie, **[?]** do sprawdzenia na danych właściciela.

## 1. Skala (punkt odniesienia)

- LLC zh-CN (2024-04): **71 127** pól, 899 plików, ~1040 terminów w
  glosariuszu. Drzewo `KR/` w ich repozytorium (2026): ~900 plików głównych +
  `StoryData` ~920, `PersonalityVoiceDlg` 186, `BattleAnnouncerDlg` 59,
  `BgmLyrics` 15, `EGOVoiceDig` 14; największy plik KR to `Skills.json`,
  ~290 KB; żaden nie przekracza 1 MB **[1]**.
- Wniosek: tekst KR mieści się w Git bez problemu (setki plików poniżej 1 MB),
  a pakiety dla Tłumacza trzeba dzielić na obszary, nie ze względu na rozmiar.
- Rodziny plików (z drzewa LLC, nazwy bez prefiksu): `Skills*` 121,
  `Passives*` 77, `EGOgift*` 28, `StageNode*`, `DungeonNode*`,
  `ActionEvents*`, `AbEvents*`, `Enemies*`, `Bufs*`, `BattleKeywords*`,
  `PanicInfo*`, `AbnormalityGuides*`, `UnitKeyword*`, `MirrorDungeonUI*`,
  `RailwayDungeon*`, `StoryTheaterDanteNote*`, `Walpu*EventText`, `IAPProduct*`.
  Sufiksy `-aNcNpN` i `-walpuN` dotyczą sezonów, wydarzeń i Walpurgisnacht.
  Nasze `rozpoznanie_localize.py` raportuje to samo (`rodziny_nazw`).

## 2. Klucz jednostki — schemat AutoLocalization

Format **[1]** (Cynanchum0109/AutoLocalization):

```
<zakres>/<plik_logiczny>#<id>[~<n>]#<ścieżka_pola>
```

- `zakres`: `StoryData`, `PersonalityVoiceDlg`, inny podkatalog albo `_root`
  dla plików w korzeniu `Localize`.
- `plik_logiczny`: nazwa bez prefiksu języka (`MainUIText.json`) — tak samo
  jak w `Lang/<nazwa>/` w CLS.
- `id`: pole `id` rekordu z `dataList`. Gdy rekord nie ma `id`, używamy pola
  `key`, a w ostateczności pozycji `@<indeks>`.
- `~<n>`: numer wystąpienia przy **powtórzonym `id`** (od `~2`). Takie
  powtórzenia potwierdzają trzy projekty, np. `-1` dla wpisów dźwiękowych
  w StoryData **[P]**.
- `ścieżka_pola`: ścieżka zagnieżdżona, np.
  `levelList[0].coinlist[2].coindescs[4].desc`.

U nas dodatkowo, jak w WWM:

- **`klucz`** w Pakiecie to pierwsze 16 znaków hex z SHA-256 pełnego
  klucza tekstowego. Jest krótki, stały i nie zdradza treści.
- **`zrodlo_hash`** to 16 znaków hex z SHA-256 tekstu **KR**. Gdy po
  aktualizacji gry zmieni się tekst KR, przekład dostaje stan `nieaktualne`
  (`stale`).

## 3. Które pola tłumaczymy — biała lista

Tłumaczymy tylko pola z białej listy, a reszta JSON przechodzi bez zmian.
Ideę stosują dwa projekty **[P]** (Noplch0 `translatable_keys.json`,
AutoLocalization `TRANSLATABLE_FIELDS`).

- **Lista startowa** (z AutoLocalization): `content`, `dlg`, `title`,
  `teller`, `place`, `desc`, `name`, `nickName`, `summary`, `flavor`, `text`,
  `displayName`, `description`, `speaker`, `statText`,
  `goalDescription1`–`goalDescription6`.
- **Nigdy nie tłumaczymy:** `id`, `model`, `d`, `level`, `voicefile`/`voiceFile`,
  `personalityid`, `usage`. `model` jest identyfikatorem zasobu, nie
  imieniem **[P]**.
- **Dostosowanie do KR:** AutoLocalization pomija pole, w którym po usunięciu
  tokenów nie ma słowa łacińskiego (ich źródłem jest EN). U nas pole idzie do
  Tłumacza, gdy **tekst KR zawiera Hangul**. Pozostałe pola z białej listy
  (liczby, `???`, nazwy pisane alfabetem łacińskim) zostają jak w pliku
  zapasowym EN.
- Listę weryfikujemy na danych: raport `rozpoznanie_localize.py` wypisuje wszystkie
  wzorce pól z liczbami wystąpień i liczbą pól z Hangulem. Wynikowa lista
  będzie w `config/pola_tlumaczone.json`, wersjonowana w Git **[?]**.

## 4. Tokeny i nawiasy — reguły do pilnowania

Moduł: [`tools/lc_tokeny.py`](../tools/lc_tokeny.py) (z testami). Regułę
zamkniętej listy tagów sprawdzono w AutoLocalization na 91 584 oficjalnych
parach EN–zh (0,021% fałszywych alarmów) **[1]**.

| Rodzaj | Przykłady | Reguła |
|---|---|---|
| Tagi „twarde” | `<color=#…>`, `</color>`, `<style=…>`, `<mark …>`, `<noparse>` | Ta sama liczba każdego tagu w PL co w KR. |
| Wypełniacze | `{0}`…`{6}`, `{0:F1}`, `{amount}`, `{stack}`, `{target}`… | Ta sama liczba. Kolejność może się zmienić zgodnie z gramatyką **[P]** (LLC Wiki). |
| Zaszumiony tekst | `#&#(!@&$` | Bez zmian, ta sama liczba. |
| Tagi układu | `<i>`, `<b>`, `<u>`, `<s>`, `<size>`, `<voffset>`, `<width>`, `<ruby>`, `<link>`, `<font>`, `<sprite>`, `<align>`… | Przekład ich nie gubi i nie dodaje. |
| Nawiasy ostre bez nazwy tagu | myśli, komunikaty radiowe, terminy w `<…>` | **To nie są tagi.** Tłumaczymy wnętrze, a nawiasy zostają **[P]**. |
| `[Słowo]` w mechanice | `[Sinking]`, `[DarkFlame]` w `desc`/`summary`/`flavor` umiejętności, pasywek i statusów | Identyfikator słowa kluczowego: **bez zmian** **[P]**. |
| `[…]` w fabule i w polach `name` | opis dźwięku, nazwa z nawiasami | Tłumaczymy. |
| `\n` | podział wiersza | Liczba powinna się zgadzać (ostrzeżenie, nie błąd). Dosłowny tekst `\n` jest zakazany. |

- **Tagi rozpoznajemy po zamkniętej liście nazw.** Ogólny wzorzec `<[^>]+>`
  jest zakazany, bo gra używa `<…>` jako cudzysłowu. Nowe nazwy tagów dopisujemy
  dopiero po rozpoznaniu. Raport `rozpoznanie` ma sekcję
  `tokeny.kandydaci_na_nowe_tagi`: nieznane nazwy z zamknięciem albo atrybutem.
- Gra ma też zniekształcone tagi, np. `</color=#x>` jako zamknięcie. Traktujemy je
  jako tokeny do zachowania 1:1 **[1]**.
- **Automatyczne linki słów kluczowych** (LLC Wiki, „技能类文本翻译”) **[1]**:
  w opisach umiejętności status zapisuje się jako `[Id]` albo jako
  **`nazwa` + spacja**. Nazwa ze spacją po niej łączy się z wpisem w
  `BattleKeywords.json` i dostaje kolor, podkreślenie i okienko podpowiedzi.
  Spacji nie wolno usunąć, nawet na końcu zdania. Konsekwencje dla nas:
  1. Polska nazwa statusu w opisach musi być **identyczna** z przekładem w
     `BattleKeywords`/`Bufs`. To wymóg techniczny, nie tylko kwestia stylu.
     Kontrola sprawdzi to na podstawie indeksu słów kluczowych (punkt 7).
  2. Polska odmiana nazwy statusu przez przypadki zrywa link. Tłumacz musi
     przyjąć konstrukcje z nazwą w formie nieodmiennej. Decyzja należy do
     Tłumacza. My dostarczamy listę i kontrolę.
  3. **[?]** Sprawdzić w grze, czy mechanizm działa w CLS dla polskiego
     tekstu. Przetestujemy to na pakiecie pilotażowym.

## 5. Budowa patcha — zapas EN, pełny komplet plików

Decyzja właściciela: pozycje bez przekładu pokazują **angielski** tekst.

- Wzór: RU Crescent-Corporation (`scripts/build.py`) **[P]**. Brakujące pliki
  i wpisy uzupełniają z EN. kazhu233 opisuje, co się dzieje bez tego: po
  aktualizacji gry brakujące pliki lub wpisy w `Lang/` dają napisy „Unknown”
  albo zawieszenia.
- U nas:
  1. Bazą każdego pliku jest **EN** z bieżącego zbioru, czyli pełna struktura JSON.
  2. W polach z białej listy wstawiamy PL według klucza. Klucze liczone są na
     KR, więc wymagamy zgodności rekordów KR↔EN (te same `id` i wystąpienia).
     Raport `parzystosc.niezgodne_id` z rozpoznania wskazuje wyjątki.
     - StoryData: RU łączy według kolejności rekordów, a pozostałe pliki według `id`.
     - U nas: według `id~n`, a przy niezgodności liczby rekordów KR/EN dany plik
       zostaje w całości EN i trafia do raportu.
  3. Przekład ma stan `nieaktualne`, gdy hash KR się zmienił. Wtedy w patchu zostaje EN.
     Lepiej pokazać aktualny angielski tekst niż przestarzały polski.
  4. Patch zawiera **wszystkie** pliki logiczne z EN, także te bez żadnego
     przekładu. Po aktualizacji gry budujemy patch ponownie z nowego zbioru.
- Kodowanie: odczyt z usunięciem BOM. Zapis w UTF-8 z takim BOM i takimi końcami
  wierszy jak w pliku źródłowym; projekty zapisują różnie (RU `utf-8-sig`,
  HKStudio011: „jak źródło”) **[?]**. Wcięcia 2 spacje.
- Mówcy: pusty `teller`/`title` w StoryData uzupełnia się z
  `ScenarioModelCodes-AutoCreated.json` według `model` (Ian1254) **[1]**.
  Najpierw tłumaczymy samą tabelę. Czy gra sama sięga do niej przy pustym
  `teller`, czy trzeba wpisać imię do sceny, sprawdzimy w teście w grze **[?]**.
  W Czytankach i Pakiecie nagłówek `[Kwestia — mówca]` zawsze pochodzi z tej
  tabeli.
- Pakiet do wgrania na Dysk: **deterministyczny ZIP**, ze stałymi znacznikami
  czasu i stałą kolejnością (glyph-zero-pack, Ian1254) **[P]**. Do tego
  `RAPORT.json` (liczby: przetłumaczone, zapas EN, nieaktualne), `SUMY.sha256`
  i sprawdzenie pobrania z Dysku.
  **Bez wydań na GitHub** (decyzja właściciela).

## 6. Cykl po aktualizacji gry

Wzór: AutoLocalization `scan.py` → `batch_*` → `apply` → `check.py`,
dostosowany do Pakietów:

1. Właściciel uruchamia `URUCHOM_AKTUALIZACJE.bat`. Do Dysku trafiają tylko
   zmienione pliki i lista usuniętych.
2. Agent przelicza jednostki i porównuje je ze stanem w `wyciag/`. Stany:
   - `do_tlumaczenia`, czyli nowe;
   - `nieaktualne`, czyli zmieniony tekst KR;
   - `przetlumaczone`;
   - `pominiete`, czyli brak Hangul albo pole techniczne;
   - `usuniete`.

   Raport zmian ma postać `wyciag/zmiany/<buildid>.md` (liczby i klucze).
3. **Pamięć tłumaczeniowa:** gdy nowa jednostka ma tekst KR identyczny z już
   przetłumaczoną, przekład jest proponowany automatycznie z oznaczeniem
   `z_pamieci`. Tłumacz widzi go w Pakiecie do potwierdzenia.
4. Pakiet przyrostowy zawiera tylko `do_tlumaczenia` i `nieaktualne`. Import
   odrzuca cały plik zwrotki, gdy są w nim błędy tokenów, tak jak
   `batch_merge` w AutoLocalization; Tłumacz dostaje raport z numerami pozycji.
5. Budujemy patch, sumy i ZIP, wgrywamy go na Dysk i zapisujemy wpis w
   `STATUS`/`EXPERIMENT_LOG`.

## 7. Indeksy do zbudowania z danych (dla Tłumacza i Czytanek)

Każdy indeks podaje KR i EN, a po przekładzie także PL. Indeksy trafiają do
`wyciag/indeksy/`.

| Indeks | Źródło w danych | Po co |
|---|---|---|
| Postacie i mówcy | `ScenarioModelCodes-AutoCreated.json` (`model` → `teller`/`title`) | Nagłówki scen, glosariusz imion, Czytanki. |
| Słowa kluczowe i statusy | `BattleKeywords*.json`, `Bufs*.json` | Jedna polska nazwa na status (automatyczne linki, p. 4); kolory buff/debuff. |
| Rozdziały i sceny (chronologia) | `StaticData/static-data/storytheater-main/*` (`storyList`: scena, etap, Before/After) + `StageChapterText`, `StagePartText`, `StageNode*`, `DungeonNode*` | Dokładna kolejność fabuły w Czytankach i Pakietach ([CZYTANKI.md](CZYTANKI.md), sekcja 3). |
| Statystyki ID i E.G.O | `StaticData/static-data/{personality,skill,passive,ego}/*` (HP, szybkość, obrona, odporności, moc i monety) | Karty ID w Czytankach; kontekst umiejętności w Pakiecie. |
| Tła i postacie na scenie | `Story/Effect/<scena>.json` (`bg`, `characterlist`) | Zmiany miejsca w nagłówkach scen. |
| Osobowości i E.G.O | `Personalities*`, `Skills*`, `Passives*`, `EGO*`, `PersonalityVoiceDlg/` | Pakiety „osobowość + jej kwestie” razem. |
| Lista plików gry | odpowiednik `RemoteLocalizeFileList.json` (HKStudio011) **[?]** | Kontrola kompletności patcha. |

## 8. Kontrole jakości

Kontrole za AutoLocalization `check.py` i HKStudio011, w raporcie podajemy
klucze i liczby, bez cytowania treści:

- tokeny i nawiasy zgodnie z punktem 4: błąd blokuje import;
- **Hangul w PL**: błąd, bo to pozostałość źródła;
- **PL identyczne z EN** w polu, w którym KR ma Hangul: ostrzeżenie, bo to
  zapewne nieprzetłumaczona kopia;
- **ten sam tekst KR przetłumaczony na kilka sposobów**: informacja dla Tłumacza;
- **stosunek długości PL/KR** poza typowym zakresem dla danego pola:
  ostrzeżenie, zwłaszcza w UI (miejsce na ekranie);
- **nazwy słów kluczowych** w opisach zgodne z indeksem statusów (punkt 4);
- **pokrycie fontu**: każdy znak PL występuje w wybranym foncie. Fail-fast jak
  `safe_charset` w glyph-zero-pack **[1]**.

## 9. Font

**Decyzja (2026-11-25): najpierw domyślny font gry** ([CEL.md](CEL.md)).
Pilot w grze pokaże, czy domyślne fonty mają polskie znaki we wszystkich
miejscach: dialog, UI, tytuły. Własny font tylko przy brakach. Poniżej punkt
wyjścia na taki wypadek:

- Pakiet FR (Eden-Office) ma w `Lang/fr/Font/{Context,Title}/` własne pliki
  `.ttf`. Jego `config.json` ma `"titleFont": ""`, `"contextFont": ""`,
  `"samplingPointSize": 78`, `"padding": 8`. To punkt wyjścia do testu **[1]**.
- Wietnamski (HKStudio011) też ma własne fonty w `Font/Context` i `Font/Title`.
  zh-CN rozprowadza `ChineseFont.ttf`, około 24 MB.
- Gdyby był potrzebny: font z licencją pozwalającą na redystrybucję (np. OFL)
  i z polskimi znakami. Licencja trafia do `assets/fonts/`, a pokrycie sprawdza
  kontrola z punktu 8.

## 10. Czego świadomie nie przejmujemy

- Paratranz i chmurowej synchronizacji (LLC, RU): u nas jest jeden zewnętrzny
  Tłumacz i Pakiety w plikach, jak w WWM/SRW.
- Modyfikacji klienta (wczesne BepInEx LLC): tylko CLS.
- Skrótu `[KeywordId:*tekst*](#kolor)` z RU: źródło KR ma już pełne tagi.
  Możemy wrócić do tego pomysłu, jeśli Tłumacz poprosi o uproszczony zapis.
- Instalatora z listą wielu tłumaczeń (kimght/LimbusLocalizationManager):
  u nas jest ZIP na Dysku. Ewentualny prosty instalator BAT powstanie w fazie 2.
