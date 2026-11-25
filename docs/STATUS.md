# Status

Stan na **2026-11-25**.

## Gdzie jesteśmy

**Zbieracz sprawdzony na prawdziwej instalacji właściciela (Steam build
`26652290`, E-007); `index/localize/` podmieniony na pliki gry; Czytanki
poprawione według uwag (O-04).**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł pełny przebieg na instalacji
  właściciela (`LCB_DANE_20261125_190908_2e6403.zip`, build Steam **`26652290`**,
  7320 plików, 0 błędów — E-007).
- Decyzje z 2026-11-25: źródło przekładu **KR** potwierdzone (D-05), pliki gry i
  **teksty gry w repozytorium jako JSON/MD, binaria nigdy** (D-06), pakiet i
  Czytanki w układzie SRW (D-07);
  czcionki — najpierw domyślna czcionka gry (O-03).
- **Teksty gry w repozytorium** (E-006, E-007): `index/localize/{kr,en}` bajt w
  bajt z instalacji Steam właściciela (build `26652290`: 2449 `kr`, 2406 `en`;
  treść identyczna z wcześniejszym lustrem TW, zachowane oryginalne CRLF + BOM);
  tabele `index/static-data/` z OpenLethe; [INDEX_FORMAT.md](INDEX_FORMAT.md).
  Czytanki i pliki ID w `czytanki/`.
- **Kolejność fabuły z danych gry** (Teatr Opowieści, etapy, walki):
  `wiedza/indeks_fabuly.json` — 36 rozdziałów, 807 scen + 184 historie
  Identity; 34 rozdziały zgodne ze storylogs co do kolejności.
- **Próbki na Dysku:** `LCB_PROBKI_2026-11-25_v2.zip` (36 Czytanek EN, Prolog +
  Canto I po koreańsku, 12 plików ID — po poprawkach układu Czytanki: pojedynczy
  `\n` między kwestiami, `■…` → `***`, `"Me"` → `"Ja"`, kwestie Dantego bez
  `\<…>`) i `plik_dla_tlumacza_v1.zip` (1001 scen, 60 362 elementy do
  przetłumaczenia).

## Następny krok

1. **Właściciel:** potwierdzić poprawiony układ Czytanek (`LCB_PROBKI_2026-11-25_v2.zip`
   — po akceptacji zamrażamy O-04) oraz decyzje O-01 (nazwa języka w `Lang/`) i
   O-02 (kolejność prac: interfejs vs fabuła).
2. **Agent:** `widoki.zip` (interfejs, słowa kluczowe, umiejętności pogrupowane
   po Identity), import zwrotki, paczka testowa `Lang/` z polskimi znakami w
   domyślnej czcionce dla buildu Steam `26652290`.

## Otwarte decyzje

O-01…O-04 w [DECYZJE.md](DECYZJE.md) (O-05, O-06 i O-07 zamknięte).
