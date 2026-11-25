# Format paczki `Lang/` (wynik projektu)

Docelowa instalacja u gracza:

```
LimbusCompany_Data/Lang/
├── config.json            ← wskazuje aktywny język
└── <Nazwa>/               ← nazwa = O-01 w DECYZJE.md
    ├── MainUIText.json    ← ta sama ścieżka logiczna co w Localize/en, bez prefiksu
    ├── …
    ├── StoryData/…
    └── Font/
        ├── Context/<czcionka>.ttf|otf
        └── Title/<czcionka>.ttf|otf
```

## `config.json` — obserwacja z publicznych paczek

Klucze: `lang` (= nazwa folderu), `titleFont`, `contextFont`,
`samplingPointSize` (np. 78), `padding` (np. 5–8). Dokładne znaczenie
`samplingPointSize`/`padding` (generowanie atlasu SDF czcionki w grze) —
**hipoteza**, ustalimy testem w grze. Zbieracz kopiuje istniejący
`Lang/config.json` właściciela, jeśli jest, i spisuje nazwy innych folderów
w `Lang/`.

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

## Zasady budowania (planowany `tools/build_lang.py`)

- Wejście: `index/` (struktura i teksty źródłowe danego buildu) +
  `tlumaczenie/` (przyjęte przekłady) + `assets/fonts/`. **Nigdy** `local/`.
- Dla każdego pliku z `Localize/en` powstaje plik o tej samej ścieżce logicznej
  i **tej samej strukturze JSON**; podmieniane są tylko pola tekstowe z
  przekładem. Teksty bez przekładu: zostaje angielski oryginał i wpis w
  raporcie pokrycia (nie usuwamy kluczy). Brak elementu daje w grze
  „Unknown”, a według społeczności nawet zawieszenie (E-004).
- Walidacja: każdy JSON się parsuje, zbiór adresów = zbiór adresów źródła,
  tokeny/znaczniki zachowane, brak znaków spoza zestawu czcionki.
- Wynik: `dist/LCB_PL_<build>_<data>.zip` z folderem `<Nazwa>/`, przykładowym
  `config.json`, instrukcją instalacji i `MANIFEST.json` (build Steam, SHA-256
  źródeł i zwrotek, pokrycie).
- Paczka zbudowana dla innego buildu/hashy niż bieżące źródło → ostrzeżenie w
  raporcie i w instrukcji.

## Test w grze (właściciel)

1. Pierwszy test „drogi”: paczka z jednym zmienionym tekstem — przycisk
   „Clear all caches” — oraz z polskimi znakami w nim.
2. Zgłoszenie: czy język się pojawia, czy znaki są poprawne, zrzut ekranu.
3. Wynik trafia do `EXPERIMENT_LOG.md` jako *test w grze*.
