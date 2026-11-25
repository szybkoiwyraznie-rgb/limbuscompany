# Pakiet dla Tłumacza — projekt

Stan: **projekt** (przed pierwszym wyciągiem). Wzorce: pakiety WWM
(`sceny.zip` + `widoki.zip` + README) i SRW Y (format elementu, limity,
tokeny, podział plików). Narzędzia `tools/bundle.py` (budowa) i
`tools/import_zwrotki.py` (import) powstaną po ustaleniu formatu `Localize`.

## Obieg

```text
Localize/kr (źródło) + en (odniesienie) + jp (prywatne, ZIP od zbieracza)
      │ tools/extract.py                    wyciąg + manifest buildu
      ▼
index/ (Git)                                teksty źródłowe, adresy, sceny
      │ tools/bundle.py --zakres …          tylko z index/
      ▼
LCB_PAKIET_<nr>_<build>.zip → Dysk właściciela → tłumacz
      │ zwrotka: te same pliki .md z wypełnionym PL:
      ▼ tools/import_zwrotki.py              kontrola źródła, tokenów, kompletności
tlumaczenie/ (Git)                          adres + SHA źródła → przekład
      │ tools/build_lang.py
      ▼
dist/LCB_PL_<build>.zip (folder Lang/<Nazwa>/)

po aktualizacji gry: nowy ZIP zbieracza → nowy index/ → audyt różnic
                     → pakiet uzupełniający (tylko nowe i zmienione teksty)
```

## Zawartość pakietu

```
LCB_PAKIET_001_<build>/
├── README.md              instrukcja dla tłumacza (format, tokeny, limity, pytania)
├── sceny/                 fabuła w kolejności, jeden plik na rozdział/część
│   ├── 00_spis-scen.md
│   ├── 1D101-1D105.md
│   └── …
├── widoki/                teksty nie-fabularne, pogrupowane tematycznie
│   ├── 01_interfejs.md
│   ├── 02_umiejetnosci.md
│   ├── 03_slowa_kluczowe.md   (statusy, efekty, tagi — tłumaczone raz, spójnie)
│   ├── 04_postacie_identity_ego.md
│   └── …
├── slowniczek.md          KR | oficjalne EN | PL — ustalone terminy (rośnie z każdym pakietem)
└── MANIFEST.json          build, SHA-256 index/, numer → adres + SHA tekstu EN
```

Pliki dłuższe niż ~8000 linii dzielone na `_a`/`_b` (lekcja SRW Y).

## Format elementu (do potwierdzenia z właścicielem i tłumaczem)

```text
## Scena 1D101A · miejsce: <place> · tytuł: <title>

14. [Dialog - 단테 / Dante]
   KR: <oryginał koreański — TO tłumaczymy>
   EN: <oficjalny angielski — odniesienie>
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   PL:
```

Źródłem jest koreański, angielski jest odniesieniem ([DECYZJE.md](DECYZJE.md)
D-05). Jeśli tłumacz nie czyta po koreańsku, pakiet buduje się z
`--zrodlo en` i kolejność linii się odwraca (EN jako źródło, KR do wglądu).
Teksty, które istnieją tylko w jednym języku, są oznaczone jawnie, np.
`[tylko EN]`.

- Tłumacz wypełnia **jedną linię** po `PL:`; łamanie i ewentualne `\n` to
  zadanie narzędzi (chyba że inspekcja pokaże, że `\n` w źródle ma znaczenie —
  wtedy token).
- `tokeny:` — znaczniki i zmienne wykryte w tekście EN (kolory, linki do słów
  kluczowych, zmienne liczbowe); import odrzuca element, jeśli zbiór tokenów
  w `PL:` różni się od EN.
- `limit:` — dodawany tylko tam, gdzie test w grze pokaże realne ograniczenie
  (przyciski, nazwy umiejętności); fabuła prawdopodobnie bez limitu.
- Mówca (`teller`) i miejsce (`place`) z danych sceny; brak mówcy = narracja.
  Mówców **nie zgadujemy**.
- Numer elementu jest lokalny w pliku; tożsamość niesie `MANIFEST.json`
  (ścieżka logiczna + adres + SHA-256 tekstu źródłowego KR oraz EN). Import
  sprawdza, że linie `KR:` i `EN:` w zwrotce nie zostały zmienione.
- `tokeny:` pochodzą z tekstu KR; jeśli zbiór znaczników w EN jest inny,
  element ma uwagę `różnica znaczników KR/EN` (do decyzji, nie błąd).
- `limit:` szacujemy względem EN i testu w grze, nie względem liczby znaków
  koreańskich (koreański jest dużo zwięźlejszy).

## Import zwrotki — bramki

1. `MANIFEST.json` pakietu pasuje do aktualnego `index/` (build/SHA) —
   inaczej odmowa albo jawny tryb „przenieś na nowy build” z raportem.
2. Każdy element: niezmienione `KR:` i `EN:`, poprawne tokeny, niepusty `PL:` (pusty =
   brak, raportowany).
3. Zapis atomowy do `tlumaczenie/` i raport importu w `zwrotki/<nr>/`
   (liczby przyjętych, pustych, odrzuconych i powód).
4. Poprawki techniczne agenta (np. naprawa tokenu za zgodą właściciela) idą do
   rejestru poprawek, nigdy cicho.

## Kolejność pakietów (propozycja, decyzja O-02)

1. **Pakiet 000 — próbny**: ~50–200 tekstów interfejsu (menu, przyciski,
   „Clear all caches”). Cel: sprawdzić cały obieg i czcionki w grze.
2. **Pakiet 001**: słowa kluczowe i statusy (`Bufs`, `BattleKeywords`,
   `SkillTag`) — fundament spójności terminologii.
3. **Pakiety fabularne**: Prolog + Canto I, dalej po kolei.
4. Równolegle: Identity/E.G.O (umiejętności, opisy, kwestie głosowe).
