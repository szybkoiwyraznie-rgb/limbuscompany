# Format paczki `Lang/` (wynik projektu)

Docelowa instalacja u gracza:

```
LimbusCompany_Data/Lang/
├── config.json            ← {"lang": "Polski", "titleFont": "", "contextFont": "", "samplingPointSize": 78, "padding": 5}
└── Polski/                ← nazwa ustalona w D-09 (zamyka O-01)
    ├── LoginUIText.json   ← ta sama ścieżka logiczna co w Localize/en, bez prefiksu EN_
    ├── MainUIText.json
    ├── …
    ├── StoryData/…
    └── Font/              ← tylko jeśli O-03 wykaże potrzebę zewnętrznych czcionek OFL
        ├── Context/<czcionka>.ttf|otf
        └── Title/<czcionka>.ttf|otf
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

## Czcionki i polskie znaki

**Plan: najpierw domyślna czcionka gry** (uwaga właściciela, 2026-11-25:
domyślna czcionka najpewniej ma polskie znaki, więc zewnętrzne czcionki mogą
być zbędne).

- Za tym przemawiają dane z publicznych paczek: w `config.json` pola
  `titleFont`/`contextFont` bywają **pustym ciągiem**, a paczka TH ma tylko
  `lang` (E-004, [PRIOR_ART.md](PRIOR_ART.md)) — mechanizm najpewniej działa
  bez własnych czcionek.
- **Pierwszy test w grze:** paczka bez folderu `Font/`, `config.json` z pustymi
  `titleFont`/`contextFont`, kilka tekstów z `ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ` w różnych
  miejscach (menu, kwestia fabularna, nazwa umiejętności). Jeśli wszystko się
  wyświetla — zostajemy przy domyślnej czcionce i O-03 się zamyka.
- **Tylko awaryjnie** (gdyby brakowało znaków albo gra wymagała pliku):
  czcionki OFL z kompletem polskich liter, sprawdzone w E-004 — Pretendard
  (tekst) i Mikodacs (tytuły; zmodyfikowana kopia nie może nosić tej nazwy),
  pobrane od autorów, w `assets/fonts/` z licencją.
- `Font/replacement_map.json` z istniejącej paczki fanowskiej przenosi
  cyrylicę do PUA i polskich znaków nie dotyczy — nie jest nam potrzebny.

## Zasady budowania (`tools/build_lang.py`)

- Wejście: `index/` (struktura i teksty źródłowe danego buildu) +
  `tlumaczenie/` (przyjęte przekłady z `tools/import_zwrotki.py`) + opcjonalnie
  `assets/fonts/`. **Nigdy** `local/`.
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
