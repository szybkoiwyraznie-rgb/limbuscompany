# Pakiet dla Tłumacza

Stan: **część fabularna działa** (`tools/build_package.py`, prototyp na
publicznym lustrze — E-005). Układ jest taki sam jak w SRW Y
(`plik_dla_tlumacza_vN.zip`: README + `sceny.zip`, element
`N. [Dialog - mówca] źródło` / `limit:` / `tokeny:` / `EN:` / `PL:`), a nagłówek
sceny podaje cały kontekst, jaki dają dane gry: rozdział, etap, miejsce,
moment walki, sąsiednie sceny i uczestników. Decyzja: [DECYZJE.md](DECYZJE.md) D-07.
Część nie-fabularna (`widoki.zip`: interfejs, umiejętności, słowa kluczowe) i
import zwrotki są jeszcze **planowane**.

## Obieg

```text
index/localize/kr (źródło) + en (odniesienie) — w Git; z lustra, potem z ZIP-a zbieracza
index/static-data (struktura: Teatr Opowieści, etapy, walki) — w Git
      │ tools/story_index.py                 kolejność scen (identyfikatory)
      ▼
wiedza/indeks_fabuly.json (Git)
      │ tools/build_package.py               teksty z Localize + kontekst
      ▼
plik_dla_tlumacza_vN.zip → Dysk właściciela → tłumacz
      │ zwrotka: te same pliki .md z wypełnionym PL:
      ▼ tools/import_zwrotki.py (planowane)   kontrola źródła, tokenów, kompletności
tlumaczenie/ (Git)                           adres + SHA źródła → przekład
      │ tools/build_lang.py (planowane)
      ▼
dist/LCB_PL_<build>.zip (folder Lang/<Nazwa>/)
```

## Zawartość

```text
plik_dla_tlumacza_v1.zip
├── README.md            instrukcja (polski): element, nagłówek sceny, zasady, co odesłać
└── sceny.zip
    ├── spis-rozdzialow.md   36 rozdziałów w kolejności czytania (EN i KR nazwa, scen, kwestii, pliki)
    ├── spis-scen.md         każda scena: numer w kolejności, rozdział, etap, moment, plik
    ├── mowcy-i-miejsca.md   imiona mówców, tytuły (epitety) i miejsca — tłumaczone RAZ
    ├── 01_prologue_selva_oscura.md … 36_….md   rozdziały (Canto, Intervallo, opowiadania)
    ├── identity-01.md … identity-12.md         historie Identity, po jednym pliku na Grzesznika
    └── pozostale.md         sceny bez miejsca w kolejności (jawnie)
```

Pliki powyżej 8000 linii dzielą się na `_a`, `_b`, … (lekcja SRW Y). Paczka
jest deterministyczna: te same dane → bajt w bajt ten sam ZIP.

Pomiar na lustrze (TW `story-data` f218bbec + OpenLethe StaticData 8f24cba):
**1001 scen, 63 010 elementów, 60 362 do przetłumaczenia** (reszta to
powtórzenia), 1529 napisów w `mowcy-i-miejsca.md`, ZIP 4,9 MB.

## Nagłówek sceny

```text
## Scena 8/1001 — S101B
- rozdział: Canto I: The Outcast — 1장: 속하지 못하는
- miejsce w rozdziale: scena 1/32
- etap: 1-1 · 부릉부릉 — Vroom-vroom
- miejsce etapu: 메피스토펠레스 안 — Mephistopheles
- opis etapu (EN): The ride is awkward and intimidating. …
- moment: przed walką
- poprzednia scena: S004A; następna: S102B
- uczestnicy:
  - 카론 — Charon
  - 베르길리우스 — Vergilius
- miejsca:
  - 메피스토펠레스 내부 — Aboard Mephistopheles
```

| Pole | Skąd |
|---|---|
| numer sceny, poprzednia/następna | `wiedza/indeks_fabuly.json` (kolejność z danych gry) |
| rozdział | `StageChapterText` (EN + KR), dla opowiadań `StoryTheaterOther` |
| etap: numer, tytuł, miejsce, opis | `StageNode*` (węzeł sceny z Teatru Opowieści lub walki) |
| moment | `stageDetail` Teatru (`Before`/`After`/`Inter`), sceny w trakcie walki z `battle-story`/`battle-ab` |
| trasa A/B/C | rozdziały z eksploracją (Canto X): `RPGSystem/EndingRoute*` |
| uczestnicy, miejsca | wiersze sceny: `model` → `ScenarioModelCodes`, `teller`, `place` |

## Element

```text
1. [Dialog - 카론 (Charon)] 베르.
   miejsce: 메피스토펠레스 내부 — Aboard Mephistopheles
   limit: do 340 znaków
   EN: Verg.
   PL:
```

- Linia elementu ma **źródło koreańskie** (D-05); `EN:` to oficjalny angielski
  jako odniesienie. Import sprawdza, że obie linie się nie zmieniły.
- `[Dialog - mówca (EN)]` albo `[Narracja]` (brak mówcy w danych = narracja;
  mówców nie zgadujemy).
- `miejsce:` (zmiana lokacji) i `tytuł mówcy:` (epitet nad imieniem) są tylko
  kontekstem: te napisy gra trzyma w osobnych polach i tłumaczy się je raz, w
  `mowcy-i-miejsca.md` (z liczbą wystąpień i pierwszym wystąpieniem).
- `limit:` — liczba polskich znaków: 340 (tyle mieści 99,9% angielskich kwestii
  w grze; okno samo łamie linie), a dla dłuższych kwestii długość EN. Pola
  słownika mają limit = najdłuższy napis tego rodzaju w grze.
- `tokeny:` — znaczniki TextMeshPro z tekstu KR (`<i>`, `<color=…>`,
  `<ruby=…>`, `{0}`); muszą zostać w `PL:`. Nawiasy `<…>` Dantego (tykanie)
  to tekst, nie znacznik.
- `(powtórzenie elementu N sceny X — …)` — ta sama para KR/EN była wcześniej w
  pliku; przekład dziedziczy się sam.
- Numer elementu = pozycja wiersza w pliku sceny (bez nagłówka), więc nie
  zmienia się przy przebudowie pakietu.

## Import zwrotki — bramki (planowane `tools/import_zwrotki.py`)

1. Wersja pakietu i build danych pasują do aktualnych — inaczej odmowa albo
   jawny tryb „przenieś na nowy build” z raportem.
2. Każdy element: niezmieniona linia źródła i `EN:`, poprawne tokeny, niepusty
   `PL:` (pusty = brak, raportowany).
3. Zapis atomowy do `tlumaczenie/` i raport importu w `zwrotki/<nr>/`.
4. Poprawki techniczne agenta idą do rejestru poprawek, nigdy cicho.

## Kolejność pakietów (propozycja, decyzja O-02)

1. **Pakiet 000 — próbny**: ~50–200 tekstów interfejsu + paczka testowa w grze
   (polskie znaki w domyślnej czcionce).
2. **Pakiet 001**: słowa kluczowe i statusy (`Bufs`, `BattleKeywords`,
   `SkillTag`) — fundament terminologii.
3. **Pakiety fabularne**: Prolog + Canto I (`--only 100 --only 101`), dalej po
   kolei; całość jest już w `sceny.zip`, więc tłumacz może pracować dowolnym
   tempem.
4. Równolegle: Identity/E.G.O (umiejętności, opisy, kwestie głosowe) — jako
   `widoki.zip` pogrupowany po Grzeszniku i Identity, z kontekstem z profili
   ([CZYTANKI.md](CZYTANKI.md)).

## Odtworzenie

```text
python3 tools/story_index.py                       # domyślnie index/static-data + index/localize
python3 tools/build_package.py --version 1          # → local/pakiet/plik_dla_tlumacza_v1.zip
python3 tools/build_package.py --only 100 --only 101    # próbka: Prolog + Canto I
# inne źródło: python3 tools/build_package.py <Localize lub ZIP zbieracza> …
```
