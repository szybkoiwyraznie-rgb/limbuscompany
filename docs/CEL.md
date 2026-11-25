# Cel projektu

## Co ma powstać

1. **Polska wersja językowa Limbus Company** jako oficjalny *Custom Language*:
   folder `LimbusCompany_Data/Lang/<nazwa>/` z plikami JSON o strukturze
   identycznej jak `Localize/en`, czcionkami w `Font/` i wpisem w
   `Lang/config.json`. Instalacja to skopiowanie folderu i wybór języka w grze;
   odinstalowanie to usunięcie folderu ([FEASIBILITY.md](FEASIBILITY.md),
   [LANG_FORMAT.md](LANG_FORMAT.md)).
2. **Pakiety dla Tłumacza** — materiały, z których zewnętrzny tłumacz pracuje
   bez znajomości plików gry: sceny w kolejności fabuły, z mówcą, miejscem i
   kontekstem; teksty interfejsu i mechaniki pogrupowane tematycznie; limity,
   znaczniki do zachowania i słowniczek ([PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md)).
3. **Czytanki** — do czytania przez właściciela jako gracza: fabuła (Canto,
   Intervallo, wydarzenia) w kolejności, profile i historie Sinnerów/Identity,
   E.G.O, lore Miasta. Najpierw z tekstu angielskiego, później z polskiego
   ([CZYTANKI.md](CZYTANKI.md)).

## Kryteria odbioru

- **Tłumaczenie:** 100% tekstów, mówców i granic scen w zakresie danego pakietu
  wraca od tłumacza i przechodzi import (zachowane identyfikatory, znaczniki
  i struktura). Braki są jawnie raportowane, nigdy nie są cicho uzupełniane
  tekstem angielskim bez wpisu w raporcie.
- **Paczka `Lang/`:** zbudowana wyłącznie z repozytorium, z manifestem (build
  Steam, SHA-256 źródeł i zwrotek), każdy plik JSON parsuje się, struktura
  odpowiada `Localize/en` tego samego buildu, polskie znaki wyświetlają się
  (test w grze właściciela).
- **Aktualizacje:** po aktualizacji gry audyt różnic wskazuje nowe, zmienione i
  usunięte teksty; tłumacz dostaje pakiet uzupełniający tylko z nimi.
- **Czytanki:** kolejność oparta na danych gry (identyfikatory rozdziałów i
  scen), luki i niepewności wypisane jawnie.

## Rozstrzygnięte — nie pytać ponownie

| Kwestia | Decyzja | Źródło |
|---|---|---|
| Kto tłumaczy | zewnętrzny tłumacz z Pakietów; agenci tylko technika | właściciel, 2026-11-25 |
| Mechanizm instalacji | wyłącznie oficjalny Custom Language (`Lang/`) | [FEASIBILITY.md](FEASIBILITY.md) |
| Dostarczanie plików gry | zbieracz `URUCHOM.bat` → ZIP → Dysk Google | [DECYZJE.md](DECYZJE.md) D-01 |
| Teksty w Git | tak, znormalizowany wyciąg w `index/` | [DATA_POLICY.md](DATA_POLICY.md) |
| Język źródłowy przekładu | angielski (`en`), `kr`/`jp` jako pomoc kontekstowa | [DECYZJE.md](DECYZJE.md) D-03 |
| Cudze tłumaczenia (także PL) | tylko wiedza techniczna, zero tekstu | [PRIOR_ART.md](PRIOR_ART.md) |

Otwarte decyzje właściciela są w [DECYZJE.md](DECYZJE.md) (sekcja „Otwarte”).
