# Format plików `Localize` (źródło tekstów gry)

Stan wiedzy: **przed pierwszą paczką od zbieracza, ale po inspekcji
publicznego lustra oryginalnych plików** (E-004 w
[EXPERIMENT_LOG.md](EXPERIMENT_LOG.md); lustra opisane w
[PRIOR_ART.md](PRIOR_ART.md)). Liczby z lustra to obserwacje; na plikach
właściciela (ze znanym buildem Steam) trzeba je potwierdzić.

## Położenie i nazwy — fakt (oficjalne)

```
LimbusCompany_Data/Assets/Resources_moved/Localize/
├── en/  EN_MainUIText.json, EN_Skills.json, …, StoryData/…
├── kr/  KR_…
└── jp/  JP_…
```

Nazwy plików mają prefiks języka; w `Lang/<nazwa>/` prefiks jest usuwany.

## Struktura JSON — obserwacja na lustrze oryginału (E-004)

Liczby z inspekcji lustra LLC (`EN/ KR/ JP/`, stan 2026-08-06). To lustro
ma ~2090 plików EN wobec 2406 w pełnym lustrze TW, więc jest niepełne. Na
plikach właściciela trzeba je potwierdzić (E-005).

| | en | kr | jp |
|---|---|---|---|
| pliki JSON | 2090 | 2074 | 2116 |
| błędy parsowania | 0 | 0 | 0 |
| pliki z BOM | 10 | 9 | 10 |
| korzeń `{"dataList": […]}` / pusty `{}` | 2071 / 19 | 2058 / 16 | 2097 / 19 |
| teksty (liście-napisy) / puste | 214 110 / 6 589 | 213 387 / 6 333 | 214 929 / 6 586 |
| znaki | 10,8 mln | 5,4 mln | 5,1 mln |
| powtórzone identyfikatory | 38 | 37 | 50 |

- Podfoldery (en/kr/jp): `StoryData` 922/919/924, `PersonalityVoiceDlg`
  186, `BattleAnnouncerDlg` 59, `BgmLyrics` 15, `EGOVoiceDig` 14; reszta
  (~890) w katalogu głównym.
- Parowanie: 2059 ścieżek logicznych jest we wszystkich trzech językach; w
  `kr` brakuje 44 plików obecnych gdzie indziej, w `en` 28. Adresy tekstów
  `en`↔`kr`: 213 359 wspólnych, 123 tylko w `en`, 28 tylko w `kr`.
  **Strukturę paczki `Lang/` trzeba więc wyznaczać z sumy, a nie z jednego
  języka**; różnice trafiają do raportu.
- Najczęstsze pola z tekstem (en): `content` 68 660, `model` 43 834, `desc`
  36 936, `name` 16 631, `title` 14 350, `teller` 9 282, `dlg` 7 677.

Schematy elementów (nazwy kluczy, bez treści):

| Plik / grupa | Klucze elementu |
|---|---|
| `StoryData/*.json` | `id`, `content`, `model`, `teller`, `title`, `place` |
| `Skills*.json` | `id`, `levelList[{level, name, desc, coinlist[{coindescs[…]}]}]` |
| `MainUIText.json` | `id`, `content` |
| `PersonalityVoiceDlg/*.json` | `id`, `desc`, `dlg` |

### Pola, które nie są tekstem do przekładu

Na podstawie danych i list z TW/rainbus/SunZheee: `id`, `key`, `level`,
`abilityID`, `model` (nazwa modelu postaci w StoryData — klucz, nie imię;
imię to `teller`), `codeName`, `fileName`, `colorCode`, `outlineColorCode`,
`mainTextColor`, `imgStr`, `iconId`/`iconID` oraz klucze `debugNodeId `
(ze spacją na końcu). Ostateczną listę ustali paczka właściciela (E-005); teksty gry leżą w `index/localize/` ([INDEX_FORMAT.md](INDEX_FORMAT.md)).

### Znaczniki w tekście (en / kr)

| Rodzaj | en | kr | Uwagi |
|---|---|---|---|
| znaczniki TMP `<…>` | 22 603 | 18 452 | najczęstsze: `style` 8175, `color` 5337, `i` 1832, `u` 1311, `b` 972, `mark` 862, `link` 462, `size` 362, `sprite` 213, `noparse` 118, `ruby` 80, `s` 66 |
| słowa kluczowe `[Nazwa]` | 52 415 | 50 483 | 963 różne; najczęstsze `[OnSucceedAttack]`, `[Laceration]`, `[WhenUse]`, `[Burst]`… |
| zmienne `{0}`… | 3 050 | 3 027 | nazwane `{…}`: 64 |
| `\n` | 43 522 | 42 591 | |

- W dialogach jest też **tekst w nawiasach ostrych, który nie jest
  znacznikiem** (3190 tekstów EN). Wykrywanie tokenów musi używać listy nazw
  znaczników TMP, a nie ogólnego wzorca `<…>`.
- **Zbiory tokenów KR i EN są równe w 22 921 tekstach, a różne w 3 474
  (~13%):** słowa kluczowe 2098, znaczniki 1230, zmienne 66; w polach `desc`
  1862, `content` 1150, `name` 170. Lokalizacja EN dodaje i usuwa
  formatowanie. Bramka tokenów przy D-05 porównuje więc przekład z **KR**, a
  różnicę KR↔EN pokazuje tłumaczowi jako informację, nie jako błąd.

### StoryData: nazwy plików

Grupy nazw (en): `S…` 344, `E…` 202, `P…` 173, `<n>D…` 148, `ES…` 35,
`PC…` 19, `ProjectGS` 1. Znaczenie i kolejność ustaliliśmy dopasowaniem do
biblioteki fabuły — [CZYTANKI.md](CZYTANKI.md).

## Model adresowania w narzędziach (`tools/localize.py`)

Wspólny czytnik, używany przez inspekcję i przyszły wyciąg:

- **Ścieżka logiczna** = ścieżka pod folderem języka, z prefiksem
  `EN_`/`KR_`/`JP_` usuniętym **tylko z nazwy pliku**
  (`en/StoryData/EN_1D101A.json` → `StoryData/1D101A.json`). Dwie ścieżki
  dające tę samą logiczną to błąd.
- **Adres tekstu** w pliku: klucze słownika jako `.klucz`. Elementy listy z
  identyfikatorem naturalnym (pierwsze z pól `id`, `key`, `level`,
  `abilityID`, czyli `IDENTIFIER_FIELDS`) jako `[pole=X]`, a powtórzenie
  jako `[id=X#2]`. Pozostałe jako `[#i]`. Przykład:
  `.dataList[id=3].levelList[level=1].desc`. Adres jest stabilny między
  językami i wersjami gry, jeśli zgadzają się identyfikatory. Wstawienie
  elementu w środek listy nie przesuwa pozostałych adresów. Na lustrze
  (E-004) adresów pozycyjnych `[#i]` jest 8,4% (przy samym `id` było 13,9%).
  Zostały głównie monety umiejętności (`coinlist`/`coindescs`), które
  naprawdę są porządkowe.
- Pliki czytane jako `utf-8-sig` (pliki `kr` mogą mieć BOM).

## Inspekcja (`tools/inspect_localize.py`)

```sh
python tools/inspect_localize.py google_drive/LCB_DANE_....zip [--out PLIK] [--probki N]
```

Raport `lcb-inspekcja-v1` (prywatny, domyślnie `local/inspekcja/<nazwa>.json`):

| Klucz | Zawartość |
|---|---|
| `per_language` | pliki, bajty, błędy parsowania, pliki z BOM, liczba tekstów, puste, znaki, słowa, powtórzone `id`, typy korzenia |
| `pairing` | ile ścieżek logicznych jest we wszystkich językach, tylko w jednym, brakujących |
| `address_alignment` | zgodność adresów tekstów `en`↔`kr`, `en`↔`jp` |
| `groups` | liczby plików według katalogu/rodzaju |
| `string_fields` | najczęstsze nazwy pól z tekstem (np. `content`, `desc`, `name`) |
| `story` | pliki StoryData, grupy prefiksów nazw, pola |
| `samples` | tylko z `--probki N`: fragmenty tekstu — **prywatne** |

Na standardowe wyjście trafiają tylko liczby. Inspekcja niczego nie
rozstrzyga — na jej podstawie uzupełniamy ten dokument (fakty z liczbami) i
sprawdzamy `index/` ([INDEX_FORMAT.md](INDEX_FORMAT.md)).

## Do potwierdzenia na paczce właściciela (E-005)

1. Liczby z tabeli powyżej dla bieżącego buildu; pliki obecne tylko w jednym
   języku (lustro LLC jest niepełne).
2. Ostateczna lista pól tekstowych i wykluczonych (wyciąg). `place` w
   StoryData wygląda na tekst wyświetlany (miejsce sceny), ale wymaga
   potwierdzenia.
3. Kodowanie i normalizacja koreańskiego (BOM, NFC/NFD, znaki specjalne).
4. Słowa kluczowe (`Bufs`, `BattleKeywords`, `SkillTag`): czy w `Lang/` muszą
   być kompletne (według poradnika podglądu `Localize/en` jest dla nich
   fallbackiem). Według kazhu233 brak elementu daje „Unknown”, a nawet
   zawieszenie gry, więc paczka i tak zawiera wszystko.
5. Znaczenie grup `P1SSNN` w StoryData (12 serii po ~14 plików, `SS` = 01–12;
   prawdopodobnie historie Sinnerów, nieobecne w bibliotece fabuły).
