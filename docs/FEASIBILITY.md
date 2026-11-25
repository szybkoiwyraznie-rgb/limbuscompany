# Wykonalność — oficjalny Custom Language

## Fakty (źródło: ogłoszenie Project Moon na Steam, 2025-03-31)

[„Custom Language Translation Support”](https://store.steampowered.com/news/app/1973530/view/533220039674824263):

- Mechanizm działa od wersji gry **1.73.0** (Steam, Windows). Wersji mobilnych
  nie dotyczy.
- Teksty źródłowe są w
  `LimbusCompany_Data/Assets/Resources_moved/Localize/{kr,en,jp}` — pliki
  JSON z prefiksem języka w nazwie (np. `EN_MainUIText.json`).
- Własny język: folder `LimbusCompany_Data/Lang/<Nazwa>/` o strukturze
  identycznej jak źródło, **nazwy bez prefiksu** (`MainUIText.json`),
  czcionki w podfolderze `Font/`, a w `Lang/config.json` wartość równa nazwie
  folderu.
- Sugerowany test: zmienić tekst przycisku „Clear all caches” i sprawdzić w
  grze. Przy dwóch i więcej językach pojawia się przycisk „Select Custom
  Language”.

## Obserwacje społeczności (do potwierdzenia u nas)

Z poradników PT-BR/RU/FR i paczek fanowskich ([PRIOR_ART.md](PRIOR_ART.md)):

- Mechanizm nie niesie ryzyka bana (w przeciwieństwie do modów w pamięci).
- Jedna czcionka na „slot”: `Context` (tekst) i `Title` (nagłówki).
- Część tekstów jest **nieprzetłumaczalna z założenia** (np. w grafikach,
  część nazw własnych w obrazach, niektóre efekty).
- Brakujący plik/klucz w `Lang/` → gra pokazuje tekst domyślny (prawdopodobnie
  angielski) — **hipoteza**, do sprawdzenia testem w grze.
- Polskie znaki: istniejąca polska paczka używa mapy `replacement_map.json`
  (znaki → kody z prywatnego obszaru Unicode). Sugeruje to, że generator
  atlasu czcionki w grze nie obejmuje wszystkich znaków bez zabiegów —
  **hipoteza**, szczegóły w [LANG_FORMAT.md](LANG_FORMAT.md).

## Ryzyka

| Ryzyko | Skutek | Środek zaradczy |
|---|---|---|
| Cotygodniowe aktualizacje (czwartki) zmieniają/dodają pliki | paczka nieaktualna, braki | zbieracz co tydzień, audyt różnic, pakiety uzupełniające |
| Gra dociąga dane po starcie (poza Steam) | `buildid` nie zmienia się mimo nowych tekstów | SHA-256 plików w raporcie, nie tylko build |
| Ogromny wolumen fabuły (~1000 plików StoryData) | długi czas przekładu | priorytety (O-02), przyrostowe pakiety |
| Czcionki i polskie znaki | „krzaki” lub kwadraty w grze | wczesny test w grze z małą paczką |
| Znaczniki w tekście (kolory, linki do słów kluczowych) | zepsute opisy | walidacja tokenów przy imporcie |
| Klucze tylko w `kr`/`jp`, brak w `en` | luki w źródle | inspekcja parowania języków |

## Wniosek

Projekt jest **wykonalny bez modyfikowania gry**. Najbliższe niewiadome
rozstrzyga pierwsza paczka od zbieracza (struktura i wolumen) oraz pierwszy test
w grze (czcionki, fallback).
