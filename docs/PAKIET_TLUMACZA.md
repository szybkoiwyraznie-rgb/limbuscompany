# Pakiet dla Tłumacza

Stan: **kompletny pakiet całej gry działa** (`tools/build_package.py` +
`tools/package_views.py`, zbudowany z `index/localize` z buildu Steam `26652290`
oraz `index/static-data` — E-008). Układ odpowiada wzorcowi SRW Y
(`plik_dla_tlumacza_vN.zip`: `README.md` + `sceny.zip` + `widoki.zip`), obejmując
**100% tekstów do lokalizacji** w grze z maksymalnym zachowaniem kontekstu
fabularnego i mechanicznego. Decyzje: [DECYZJE.md](DECYZJE.md) D-05, D-07, D-08.
Import zwrotki (`tools/import_zwrotki.py`) i budowa paczki `Lang/`
(`tools/build_lang.py`) są następne w kolejce.

## Obieg

```text
index/localize/kr (źródło) + en (odniesienie) — w Git (build Steam 26652290)
index/static-data (struktura: Teatr Opowieści, etapy, walki, Identity, skille, pasywki) — w Git
      │ tools/story_index.py                 kolejność scen (identyfikatory)
      ▼
wiedza/indeks_fabuly.json (Git)
      │ tools/build_package.py (+ tools/package_views.py)
      ▼
plik_dla_tlumacza_vN.zip → Dysk właściciela → tłumacz
      │ zwrotka: te same pliki .md z wypełnionym PL: (w całości lub partiami)
      ▼ tools/import_zwrotki.py (planowane)   kontrola źródła, tokenów, kompletności
tlumaczenie/ (Git)                           adres + SHA źródła → przekład
      │ tools/build_lang.py (planowane)
      ▼
dist/LCB_PL_<build>.zip (folder Lang/<Nazwa>/)
```

## Zawartość

```text
plik_dla_tlumacza_v2.zip
├── README.md            instrukcja (polski): układ sceny i widoku, tagi, zasady, co odesłać
├── sceny.zip            100% fabuły (1001 plików StoryData/ w 68 plikach .md)
│   ├── spis-rozdzialow.md   36 rozdziałów w kolejności czytania (EN i KR nazwa, scen, kwestii, pliki)
│   ├── spis-scen.md         każda scena: numer w kolejności, rozdział, etap, moment, plik
│   ├── mowcy-i-miejsca.md   imiona mówców, tytuły (epitety) i miejsca — tłumaczone RAZ (1533 pozycje)
│   ├── 01_prologue_selva_oscura.md … 36_….md   rozdziały (Canto, Intervallo, opowiadania)
│   ├── identity-01.md … identity-12.md         historie Identity, po jednym pliku na Grzesznika
│   └── pozostale.md         sceny bez miejsca w kolejności (jawnie)
└── widoki.zip           100% pozostałych tekstów gry (1458 plików źródłowych w 104 plikach .md)
    ├── spis-widokow.md                     pełna tabela 32 działów tematycznych i plików .md
    ├── mowcy-rpg-i-anomalii.md             mówcy trybu RPG (Canto X), testów Anomalii i tabela modeli
    ├── 01_slownik_bojowy_a.md … _j.md      SkillTag, grzechy, BattleKeywords, Bufs, poczytalność i Panika
    ├── 02_tozsamosc_01_Yi_Sang_*.md … 12_* karty Tożsamości połączone ze statystykami, skillami 1–4, pasywkami, głosem i AbDlg
    ├── 02_tozsamosc_13_wspolne_i_dodatkowe.md   wpisy wspólne i wydarzeniowe Tożsamości
    ├── 03_ego_postaci_a.md … _d.md         każde E.G.O: karta + Przebudzenie + Korozja + pasywka + głos
    ├── 03_dary_ego_a.md … _d.md            wszystkie Dary E.G.O (pełne i skrócone opisy, kategorie)
    ├── 04_anomalie_przewodnik.md           encyklopedia Anomalii i poziomy obserwacji (z kodami klasyfikacji)
    ├── 04_wydarzenia_anomalii_*.md         spotkania z Anomaliami połączone z komunikatami wyników (AbEventsResultLog)
    ├── 04_wydarzenia_interaktywne_*.md     wydarzenia wyboru (ActionEvents: opis + opcje + podpowiedzi + rezultaty)
    ├── 04_jednostki_wsparcia.md            sojusznicy NPC (Assist) wraz z umiejętnościami i pasywkami
    ├── 04_wrogowie_dymki_i_umiejetnosci_*.md    przeciwnicy, dymki bojowe, umiejętności i pasywki pogrupowane po rozdziale/trybie
    ├── 05_komentatorzy_bitwy_*.md          komentatorzy bitwy połączeni z ich kwestiami głosowymi
    ├── 05_muzyka_i_piosenki.md             ścieżki BGM w lobby (z wykonawcami) i napisy piosenek (BgmLyrics)
    ├── 06_tryb_rpg_canto10_a.md … _l.md    zadania, przedmioty, NPC, lokacje, narracja i dialogi RPG z Canto X (po piętrach)
    ├── 07_notatki_dantego_i_teatr.md       Notatki Dantego (hasła + wpisy) i Teatr Opowieści
    ├── 07_rozdzialy_etapy_i_zdolnosci_dantego_*.md   rozdziały, węzły mapy, zdolności Durante i efekty tekstowe
    ├── 07_loch_lustra_kolej_i_rajdy_*.md   Loch Lustra, Kolej Refrakcji, Ekstrakcja Nici i rajdy
    ├── 08_interfejs_glowny_i_ustawienia_*.md    główne UI, bitwa, formacja, menu ustawień, skróty, błędy i FAQ
    ├── 08_samouczki_i_wskazowki_*.md       samouczki i podpowiedzi taktyczne
    ├── 08_wydarzenia_sezonowe_i_przepustka.md   Przepustka Limbus, Noc Walpurgii i wydarzenia Intervallo
    └── 08_przedmioty_sklep_i_profil_*.md   przedmioty, sklep, Ekstrakcja (Gacha), sztandary i bilety profilu
```

Pliki powyżej 8000 linii dzielą się automatycznie na `_a`, `_b`, … (lekcja SRW Y;
maksymalny rozmiar pliku w `v2`: 7998 linii w `sceny.zip`, 6340 linii w
`widoki.zip`). Paczka jest w 100% deterministyczna: te same dane → bajt w bajt
ten sam ZIP.

Pomiar na buildzie Steam `26652290` (`plik_dla_tlumacza_v2.zip`, E-008):
- **`sceny.zip`:** 1001 scen, 63 010 elementów, **60 362** do przetłumaczenia +
  **1533** pozycje w `mowcy-i-miejsca.md`.
- **`widoki.zip`:** 1458 plików źródłowych, **103 871** niepustych liści JSON
  (pokrycie **100,00%** weryfikowane automatyczną bramką), **93 069** elementów
  po złączeniu identycznych poziomów ulepszeń 1–4 i mówców, z czego **68 148**
  unikalnych do przetłumaczenia.
- **Razem cała gra:** **156 079** elementów, **130 043** unikalne napisy do
  przetłumaczenia, rozmiar ZIP **11 449 704 B (~10,9 MiB)**.

## Kontekst i format elementów

### 1. Element w `sceny.zip`

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

1. [Dialog - 카론 (Charon)] 베르.
   miejsce: 메피스토펠레스 내부 — Aboard Mephistopheles
   limit: do 340 znaków
   EN: Verg.
   PL:
```

### 2. Element w `widoki.zip`

```text
## [0] LCB Sinner — Yi Sang — LCB 수감자
- ID Tożsamości: `10101` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 72 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Sinking

7. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 공격 위력 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2010111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Reduction]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttackHead] Inflict 2 [Reduction]
   PL:
```

- `źródło: <plik_logiczny> :: <adres_json> [; <adres_json_2> …]` wskazuje
  dokładny liść w tabeli `Localize` (a przy identycznych tekstach na kolejnych
  poziomach ulepszeń 1–4 umiejętności łączy te adresy w jeden element, oszczędzając
  7478 duplikatów bez utraty adresacji).
- Identyfikatory tagów w nawiasach kwadratowych (`[OnSucceedAttackHead]`,
  `[Combustion]`, `[Vibration]`, …) pozostają nietłumaczone w kodzie, a linia
  `znaczenie tagów:` wyświetla ich nazwę KR/EN ze słownika bojowego, aby ułatwić
  odmianę fleksyjną po polsku.
- W `05_muzyka_i_piosenki.md` (`BgmLyrics/*`) narzędzie wykrywa koreańskie style
  czcionki `<style="DKR_…">` i podaje w `tokeny:` odpowiadający im łaciński styl
  `<style="DEN_…">` z wersji angielskiej.
- Wpisy obecne w danych gry wyłącznie po angielsku (96 liści w 10 plikach, np.
  sztandary i bilety sezonowe) są jawnie oznaczone `tylko EN w danych gry`, dzięki
  czemu żaden widoczny w grze napis nie zostaje pominięty.

## Import zwrotki — bramki (planowane `tools/import_zwrotki.py`)

1. Wersja pakietu i build danych pasują do aktualnych — inaczej odmowa albo
   jawny tryb „przenieś na nowy build” z raportem.
2. Każdy element: niezmieniona linia źródła, `źródło:` i `EN:`, poprawne tokeny,
   niepusty `PL:` (pusty = brak, raportowany; tłumacz może odsyłać dowolne podzbiory
   plików `.md`).
3. Zapis atomowy do `tlumaczenie/` i raport importu w `zwrotki/<nr>/`.
4. Poprawki techniczne agenta idą do rejestru poprawek, nigdy cicho.

## Odtworzenie

```text
python3 tools/story_index.py                        # indeks kolejności fabuły
python3 tools/build_package.py --version 2          # pełny pakiet: README.md + sceny.zip + widoki.zip
python3 tools/build_package.py --only 100 --only 101    # próbka fabularna: Prolog + Canto I
python3 tools/build_package.py --no-views           # tylko sceny.zip (bez widoki.zip)
```
