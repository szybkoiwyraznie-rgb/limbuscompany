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

- Gra wymaga po jednej czcionce na slot (`Context`, `Title`).
- Istniejąca polska paczka fanowska zawiera `Font/replacement_map.json`
  mapujący znaki na kody z prywatnego obszaru Unicode (PUA). Możliwe przyczyny:
  czcionka gry/atlas nie obejmuje `ą ć ę ł ń ó ś ź ż`, albo trzeba było
  podmienić glify w zmodyfikowanej czcionce. **Hipoteza do sprawdzenia** —
  pierwszy test w grze: wolna czcionka z pełnym zestawem polskich znaków
  (np. z rodziny Noto/Source/Pretendard na OFL) bez żadnej mapy.
- W repo trzymamy tylko czcionki z licencją pozwalającą na redystrybucję, w
  `assets/fonts/` z plikiem licencji.

## Zasady budowania (planowany `tools/build_lang.py`)

- Wejście: `index/` (struktura i teksty źródłowe danego buildu) +
  `tlumaczenie/` (przyjęte przekłady) + `assets/fonts/`. **Nigdy** `local/`.
- Dla każdego pliku z `Localize/en` powstaje plik o tej samej ścieżce logicznej
  i **tej samej strukturze JSON**; podmieniane są tylko pola tekstowe z
  przekładem. Teksty bez przekładu: zostaje angielski oryginał i wpis w
  raporcie pokrycia (nie usuwamy kluczy).
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
