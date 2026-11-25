# Format paczki `Lang/` (wynik projektu)

Docelowa instalacja u gracza:

```
LimbusCompany_Data/Lang/
├── config.json            ← {"lang": "Polski", "titleFont": "", "contextFont": "", "samplingPointSize": 78, "padding": 5}
└── Polski/                ← nazwa ustalona w D-09 (zamyka O-01)
    ├── Font/              ← WYMAGANE przez grę od 1.74.0 (potwierdzone w v.1.119.1, E-011)
    │   ├── Context/Pretendard-Regular.ttf
    │   └── Title/Mikodacs.otf
    ├── LoginUIText.json   ← ta sama ścieżka logiczna co w Localize/en, bez prefiksu EN_
    ├── MainUIText.json
    ├── …
    └── StoryData/…
```

## `config.json` i aktywacja języka w grze

Pełny schemat używany przez grę i narzędzia społeczności (`v.1.119.1`):

```json
{
  "lang": "Polski",
  "titleFont": "",
  "contextFont": "",
  "samplingPointSize": 78,
  "padding": 5
}
```

- `lang` — nazwa podkatalogu w `LimbusCompany_Data/Lang/`.
- `titleFont`, `contextFont` — puste ciągi `""` (nawet gdy używany jest katalog
  `Font/Title/` i `Font/Context/`, gra sama skanuje oba podkatalogi; wpisanie
  tam ścieżki względnej zdublowałoby podkatalog).
- `samplingPointSize` (`78`) i `padding` (`5`) — parametry dynamicznego atlasu
  SDF czcionki w Unity TextMeshPro; przy ich pominięciu deserializacja w C#
  podstawia `0`, a nasz pierwszy test w grze (`E-010`, `v.1.119.1`) pokazał, że
  3-kluczowy `config.json` nie aktywuje języka przy pierwszym uruchomieniu.
- **Aktywacja przy pierwszej instalacji (`v.1.119.1`, E-010):** po wykryciu
  choćby jednego podkatalogu w `LimbusCompany_Data/Lang/` gra wyświetla na
  ekranie tytułowym (lewy dolny róg, obok `Clear all caches`) przycisk
  **`Select Custom Language`** (`custom_localize_button` w `LoginUIText.json`).
  Jeśli pierwsze uruchomienie po rozpakowaniu otworzy się po angielsku,
  jednorazowy wybór `Select Custom Language` → `Polski` i ponowne uruchomienie
  gry (`custom_localize_desc`: *„Restart the game to apply the language change”*)
  zapisuje wybór — od tej pory każde kolejne uruchomienie startuje od razu po
  polsku.

## Czcionki i polskie znaki (`assets/fonts/`, E-011)

- **Wynik testu w grze bez folderu `Font/` (`v.1.119.1`, E-011):** nawet po
  wcześniejszym wybraniu `Polski` na liście `Select Custom Language` i restarcie
  gry paczka bez `Font/Context/` i `Font/Title/` **nie ładuje się w ogóle**
  (ekran tytułowy i lobby pozostają w 100% po angielsku). Porównanie z
  działającymi paczkami dla `v.1.119.1` (m.in. `Limbus-RU-Full`: identyczne
  `2406/2406` ścieżek JSON z naszym `index/localize/en`) oraz walidatorami
  instalatorów (`LimbusLLmTranslate`, `llc-rs`) potwierdziło, że silnik wymaga
  obecności plików `.ttf`/`.otf` w `Font/Context/` i `Font/Title/`.
- **Dołączone czcionki (`assets/fonts/`, licencja SIL OFL 1.1):** w 100%
  **niemodyfikowane** pliki z oficjalnych źródeł odpowiadające krojom samej gry:
  - `Font/Context/Pretendard-Regular.ttf` (`orioncactus/pretendard` v1.309,
    `2 725 828` B, SHA-256 `6d0af525…a324`, `14 336` znaków, `18/18` polskich
    liter + `8/8` znaków polskiej typografii);
  - `Font/Title/Mikodacs.otf` (Grzegorz Luk `gluk`, `glukfonts.pl`, v0.28,
    `110 228` B, SHA-256 `d685ef7f…8d30`, `18/18` polskich liter + `8/8`
    znaków polskiej typografii — polski autor zawarł komplet polskich znaków w
    oryginale, dzięki czemu nie trzeba modyfikować pliku i zastrzeżona nazwa
    `Mikodacs` jest w pełni zgodna z SIL OFL 1.1).
- W `Font/Context/` i `Font/Title/` umieszczamy **wyłącznie** pliki `.ttf`/`.otf`
  (przy `titleFont: ""` i `contextFont: ""` gra wybiera pierwszy plik z każdego
  katalogu), a pełne teksty licencji (`OFL-Pretendard.txt`, `OFL-Mikodacs.txt`)
  trafiają do archiwum w katalogu `LICENCJE_CZCIONEK/` (poza `LimbusCompany_Data/`).
- `Font/replacement_map.json` z istniejącej paczki fanowskiej przenosi
  cyrylicę do PUA i polskich znaków nie dotyczy — nie jest nam potrzebny.

## Zasady budowania (`tools/build_lang.py`)

- Wejście: `index/` (struktura i teksty źródłowe danego buildu) +
  `tlumaczenie/` (przyjęte przekłady z `tools/import_zwrotki.py`) +
  `assets/fonts/` (wymagane czcionki OFL w `Title/` i `Context/` — brak czcionki
  przerywa budowanie z błędem). **Nigdy** `local/`.
- Dla każdego pliku z `Localize/en` (oraz każdego przetłumaczonego pliku
  obecnego wyłącznie w `Localize/kr`) powstaje plik o tej samej ścieżce
  logicznej i **tej samej strukturze JSON**; podmieniane są tylko pola tekstowe
  z przekładem (wraz ze słownikami mówców i miejsc). Teksty bez przekładu:
  zostaje angielski oryginał i wpis w raporcie pokrycia (nie usuwamy kluczy).
  Brak elementu daje w grze „Unknown”, a według społeczności nawet zawieszenie
  (E-004).
- Walidacja: każdy wygenerowany JSON jest ponownie parsowany, zbiór adresów
  musi być identyczny ze zbiorem adresów źródła, a tokeny/znaczniki TMP,
  zmienne `{0}` i słowa kluczowe `[Keyword]` muszą przejść bramkę.
- Wynik produkcyjny: `dist/LCB_PL_Polski_<build>.zip` z układem
  `LimbusCompany_Data/Lang/config.json` (pełny schemat 5 kluczy) +
  `LimbusCompany_Data/Lang/Polski/…`, `INSTRUKCJA.txt` oraz `MANIFEST.json`
  (build Steam, SHA-256 źródeł, pokrycie i ostrzeżenia wersji).
- Wynik diagnostyczny (`python3 tools/build_lang.py --probe`):
  `dist/LCB_TEST_DROGI_Polski_<build>.zip` — nie zapisuje nic do `tlumaczenie/`
  ani nie tłumaczy tekstów gry, lecz dopisuje znacznik `ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ` do
  4 punktów kontrolnych (`LoginUIText.json :: switch_allcacheclear`,
  `MainUIText.json :: mainui_main_button1/2`, `StoryData/S001B.json :: id=0`,
  `Skills.json :: id=1010101`).

## Test w grze (właściciel)

1. Pierwszy test „drogi”: paczka z jednym zmienionym tekstem — przycisk
   „Clear all caches” — oraz z polskimi znakami w nim.
2. Zgłoszenie: czy język się pojawia, czy znaki są poprawne, zrzut ekranu.
3. Wynik trafia do `EXPERIMENT_LOG.md` jako *test w grze*.
