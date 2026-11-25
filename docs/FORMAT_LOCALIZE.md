# Format plików `Localize` (źródło tekstów gry)

Stan wiedzy: **przed pierwszą paczką od zbieracza**. Poniższe opiera się na
ogłoszeniu Project Moon i na układzie publicznych paczek Custom Language
([PRIOR_ART.md](PRIOR_ART.md)); każdą pozycję trzeba potwierdzić na plikach
właściciela i zapisać wynik w [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md).

## Położenie i nazwy — fakt (oficjalne)

```
LimbusCompany_Data/Assets/Resources_moved/Localize/
├── en/  EN_MainUIText.json, EN_Skills.json, …, StoryData/…
├── kr/  KR_…
└── jp/  JP_…
```

Nazwy plików mają prefiks języka; w `Lang/<nazwa>/` prefiks jest usuwany.

## Struktura JSON — obserwacja z publicznych paczek (hipoteza dla `Localize`)

Korzeń: `{"dataList": [ … ]}`, elementy z polem `id`. Przykładowe schematy
elementów (nazwy kluczy, bez treści):

| Plik / grupa | Klucze elementu |
|---|---|
| `StoryData/*.json` | `id`, `place`, `content`, `model`, `teller`, `title` |
| `Skills*.json` | `id`, `levelList[{level, name, desc}]` |
| `MainUIText.json` | `id`, `content` |
| `PersonalityVoiceDlg/*.json` | `id`, `desc`, `dlg` |

Podfoldery widziane w paczce `Lang/`: `BattleAnnouncerDlg`, `BgmLyrics`,
`EGOVoiceDig`, `PersonalityVoiceDlg`, `RPGSystem`, `StoryData` (~1000 plików).
Prefiksy nazw w `StoryData`: `1D`–`8D`, `E`, `ES`, `P`, `PC`, `S`, plus
pojedyncze `SDUMMY`, `ProjectGS`. Znaczenie prefiksów (rozdział/Canto,
wydarzenia, Intervallo…) — **niewiadoma**, do ustalenia z danymi i treścią.

Spodziewany rozmiar `Localize/en`: ~35–40 MB, ~2400 plików JSON.

## Model adresowania w narzędziach (`tools/localize.py`)

Wspólny czytnik, używany przez inspekcję i przyszły wyciąg:

- **Ścieżka logiczna** = ścieżka pod folderem języka, z prefiksem
  `EN_`/`KR_`/`JP_` usuniętym **tylko z nazwy pliku**
  (`en/StoryData/EN_1D101A.json` → `StoryData/1D101A.json`). Dwie ścieżki
  dające tę samą logiczną to błąd.
- **Adres tekstu** w pliku: klucze słownika jako `.klucz`; elementy listy z
  prostym `id` jako `[id=X]` (powtórzenie: `[id=X#2]`); pozostałe jako `[#i]`.
  Przykład: `.dataList[id=3].levelList[#0].desc`. Adres jest stabilny między
  językami, jeśli zgadzają się `id` — dzięki temu parujemy `en`↔`kr`↔`jp`.
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
projektujemy `index/`.

## Do ustalenia po pierwszej paczce

1. Pełna lista plików i podfolderów; które mają `dataList`, a które inny układ.
2. Które pola są tekstem do tłumaczenia, a które identyfikatorami / nazwami
   modeli / kluczami (np. `model`, `place` w StoryData — tekst czy klucz?).
3. Znaczniki w tekście: kolory, `<link>`/słowa kluczowe, zmienne, `\n` — lista
   tokenów do zachowania ([PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md)).
4. Kolejność scen: czy `id` w StoryData i nazwy plików wystarczą do odtworzenia
   kolejności fabuły ([CZYTANKI.md](CZYTANKI.md)).
5. **Parowanie `kr`↔`en` (kluczowe przy D-05):** pliki i adresy obecne tylko
   w jednym języku; czy `id` się zgadzają; czy znaczniki w tekście są te same.
   Gdy `kr` ma teksty, których nie ma w `en` (albo odwrotnie), trzeba ustalić,
   który zestaw wyznacza strukturę paczki `Lang/`.
6. Kodowanie i normalizacja koreańskiego (BOM, NFC/NFD, znaki specjalne).
7. Słowa kluczowe (`Bufs`, `BattleKeywords`, `SkillTag`): czy w `Lang/` muszą
   być kompletne (wg poradnika podglądu — `Localize/en` jest dla nich
   fallbackiem).
