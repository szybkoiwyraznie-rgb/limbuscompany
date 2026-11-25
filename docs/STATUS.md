# Status

Stan na **2026-11-25**.

## Gdzie jesteśmy

**Pełny rurociąg lokalizacji (`build_package.py` → `import_zwrotki.py` →
`build_lang.py`) jest gotowy i przetestowany; drugi test w grze (`v.1.119.1`,
E-011) wyjaśnił przyczynę nieładowania paczek `v1`/`v2` (silnik wymaga plików
`.ttf`/`.otf` w `Lang/Polski/Font/Context/` i `Font/Title/`), do `assets/fonts/`
dodano niemodyfikowane czcionki SIL OFL 1.1 samej gry (`Pretendard-Regular.ttf`
+ `Mikodacs.otf`, `18/18` polskich liter), a na Dysku właściciela czeka
kompletna paczka diagnostyczna `LCB_TEST_DROGI_Polski_26652290_v3.zip` oraz
`plik_dla_tlumacza_v2.zip` (100% gry, E-008).**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł pełny przebieg na instalacji
  właściciela (`LCB_DANE_20261125_190908_2e6403.zip`, build Steam **`26652290`**,
  7320 plików, 0 błędów — E-007).
- Zamknięte decyzje (D-01 … D-09): źródło przekładu **KR** (D-05), teksty gry
  w repozytorium jako JSON/MD bez binariów (D-06), układ Czytanek zaakceptowany
  i zamrożony (D-07, zamyka O-04), kompletny pakiet 100% gry naraz (D-08,
  zamyka O-02), nazwa języka **`Polski`** i automatyczny start gry w tym języku
  przez `Lang/config.json` (D-09, zamyka O-01).
- **Teksty gry w repozytorium** (E-006, E-007): `index/localize/{kr,en}` bajt w
  bajt z instalacji Steam właściciela (build `26652290`: 2449 `kr`, 2406 `en`;
  2459 plików logicznych łącznie); `index/static-data/` z OpenLethe;
  [INDEX_FORMAT.md](INDEX_FORMAT.md). Czytanki i pliki ID w `czytanki/`.
- **Kompletny pakiet dla tłumacza na Dysku (`plik_dla_tlumacza_v2.zip`, E-008):**
  11 449 704 B (~10,9 MiB), SHA-256 `9bb4dcad…a5006` (`sceny.zip` + `widoki.zip`,
  łącznie **156 079** elementów i **130 043** unikalnych napisów do przekładu).
- **Importer zwrotek i generator `Lang/Polski/` (E-009):**
  - `tools/import_zwrotki.py` waliduje zgodność źródeł, znaczniki TMP (w tym
    odróżnienie kwestii Dantego `<I …>` od kursywy `<i>` oraz odczytów
    `<ruby=…>`), zmienne `{0}`, słowa kluczowe `[Keyword]` i styl `DEN` w
    `BgmLyrics/*`, automatycznie dziedziczy powtórzenia i zapisuje `tlumaczenie/`
    atomowo (sprawdzone na wszystkich `157 612` pozycjach pakietu: 0 błędów);
  - `tools/build_lang.py` buduje deterministyczne archiwum
    `LimbusCompany_Data/Lang/config.json` (pełny schemat 5 kluczy: `"lang":
    "Polski"`, `titleFont`, `contextFont`, `samplingPointSize: 78`, `padding: 5`)
    + wymagane przez grę czcionki SIL OFL 1.1 z `assets/fonts/`
    (`Font/Context/Pretendard-Regular.ttf`, `Font/Title/Mikodacs.otf`, licencje
    w `LICENCJE_CZCIONEK/`) + pełne drzewo 2406 plików `Localize/en` (fallback
    EN chroniący przed `"Unknown"`).
- **Paczka diagnostyczna na Dysku (`LCB_TEST_DROGI_Polski_26652290_v3.zip`, E-011):**
  7 430 569 B (~7,1 MiB), SHA-256 `fe359fcd…1ff1` — uzupełniona o obowiązkowe
  katalogi `Font/Context/` i `Font/Title/`; czeka na sprawdzenie w grze
  (`v.1.119.1`), aby zamknąć `O-03`.

## Następny krok

1. **Właściciel:** rozpakować `LimbusCompany_Data` z
   `LCB_TEST_DROGI_Polski_26652290_v3.zip` do katalogu gry (nadpisując
   wcześniejszy `Lang/config.json`), uruchomić grę i sprawdzić polskie znaki na
   `Clear all caches [PL: ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ]` oraz w lobby (`Sinners
   [ąćęłńóśźż]`, `Theater [ĄĆĘŁŃÓŚŹŻ]`) — zamknięcie **O-03**; przekazać
   `plik_dla_tlumacza_v2.zip` tłumaczowi.
2. **Agent:** po zgłoszeniu wyniku testu z gry zapisać potwierdzenie w
   `EXPERIMENT_LOG.md`, zamknąć O-03 i przygotować `tools/audit_update.py` pod
   cotygodniowe aktualizacje gry.

## Otwarte decyzje

Tylko **O-03** (ostateczne potwierdzenie wyświetlania polskich znaków w grze na
paczce `v3`) w [DECYZJE.md](DECYZJE.md) — O-01, O-02, O-04, O-05, O-06 i O-07
zamknięte.
