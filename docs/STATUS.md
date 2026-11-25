# Status

Stan na **2026-11-25**.

## Gdzie jesteśmy

**Kompletny pakiet dla tłumacza obejmujący 100% tekstów gry (`plik_dla_tlumacza_v2.zip`:
`sceny.zip` + `widoki.zip`, Steam build `26652290`, E-008) zbudowany,
zweryfikowany i wgrany na Dysk właściciela.**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł pełny przebieg na instalacji
  właściciela (`LCB_DANE_20261125_190908_2e6403.zip`, build Steam **`26652290`**,
  7320 plików, 0 błędów — E-007).
- Decyzje z 2026-11-25: źródło przekładu **KR** potwierdzone (D-05), pliki gry i
  **teksty gry w repozytorium jako JSON/MD, binaria nigdy** (D-06), pakiet i
  Czytanki w układzie SRW (D-07), **pełny pakiet 100% gry naraz** (D-08, zamyka
  O-02); czcionki — najpierw domyślna czcionka gry (O-03).
- **Teksty gry w repozytorium** (E-006, E-007): `index/localize/{kr,en}` bajt w
  bajt z instalacji Steam właściciela (build `26652290`: 2449 `kr`, 2406 `en`;
  2459 plików logicznych łącznie); `index/static-data/` z OpenLethe;
  [INDEX_FORMAT.md](INDEX_FORMAT.md). Czytanki i pliki ID w `czytanki/`.
- **Kompletny pakiet dla tłumacza na Dysku (`plik_dla_tlumacza_v2.zip`, E-008):**
  11 449 704 B (~10,9 MiB), SHA-256 `9bb4dcad…a5006`:
  - `sceny.zip` — 1001 scen fabularnych w kolejności czytania (63 010 elementów,
    **60 362** unikalne kwestie do przetłumaczenia + **1533** pozycje w
    `mowcy-i-miejsca.md`),
  - `widoki.zip` — 1458 plików źródłowych poza `StoryData/` (**103 871** liści
    JSON, **100%** pokrycia zweryfikowane bramką), pogrupowanych z pełnym
    kontekstem w 104 pliki `.md` (93 069 elementów, **68 148** unikalnych do
    przetłumaczenia),
  - łącznie **156 079** elementów (**130 043** unikalnych napisów do przekładu).
- **Próbki na Dysku:** `LCB_PROBKI_2026-11-25_v2.zip` (36 Czytanek EN, Prolog +
  Canto I po koreańsku, 12 plików ID — po 4 poprawkach układu Czytanki).

## Następny krok

1. **Właściciel:** przekazać `plik_dla_tlumacza_v2.zip` tłumaczowi; przy okazji
   potwierdzić O-01 (nazwa języka w `Lang/`, np. `Polski`) oraz O-04 (układ
   Czytanek po poprawkach).
2. **Agent:** przygotować `tools/import_zwrotki.py` oraz `tools/build_lang.py` i
   paczkę testową `Lang/` z polskimi znakami w domyślnej czcionce dla buildu
   Steam `26652290` (O-03).

## Otwarte decyzje

O-01, O-03 i O-04 w [DECYZJE.md](DECYZJE.md) (O-02, O-05, O-06 i O-07 zamknięte).
