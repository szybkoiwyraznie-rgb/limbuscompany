# Status

Stan na **2026-11-26**.

## Gdzie jesteśmy

**Cała infrastruktura techniczna projektu (Etapy 0–6) jest ukończona i
sprawdzona na żywej czwartkowej aktualizacji gry (`26652290` → `26917622`,
E-013): paczka `Lang/Polski/` z niemodyfikowanymi czcionkami SIL OFL 1.1
(`Pretendard-Regular.ttf` + `Mikodacs.otf`) działa w grze (`18/18` polskich
znaków, E-012), `index/localize` jest na aktualnym buildzie `26917622`, a na
Dysku obok pełnego pakietu bazowego (`plik_dla_tlumacza_v2.zip`) czeka gotowy
pakiet przyrostowy `pakiet_przyrostowy_26652290_do_26917622.zip` (`1 733`
unikalne pozycje z dzisiejszej łatki).**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows,
  `61/61` testów zielonych).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł przebieg bazowy (`26652290`, E-007)
  oraz przebieg po czwartkowej aktualizacji (`LCB_DANE_20261126_094359_ef145d.zip`,
  build Steam **`26917622`**, 7368 plików, 0 błędów — E-013).
- Wszystkie decyzje projektowe zamknięte (`D-01` … `D-10`, brak otwartych `O-*`):
  źródło przekładu **KR** (D-05), teksty gry w repozytorium jako JSON/MD bez
  binariów (D-06), układ Czytanek zaakceptowany i zamrożony (D-07), kompletny
  pakiet 100% gry naraz (D-08), nazwa języka **`Polski`** i 5-kluczowy
  `Lang/config.json` (D-09), niemodyfikowane czcionki SIL OFL 1.1 w
  `assets/fonts/` potwierdzone w grze (D-10, zamyka O-03).
- **Teksty gry i Czytanki w repozytorium** (E-006, E-007, E-013):
  `index/localize/{kr,en}` na aktualnym buildzie Steam **`26917622`** (`2 464`
  `kr`, `2 421` `en`); `index/static-data/` z OpenLethe (`8f24cba5`, dane z
  `2026-11-12` — do odświeżenia, gdy OpenLethe opublikuje tabele dla `10117` i
  `11217`); Czytanki i pliki ID w `czytanki/`.
- **Pakiety dla tłumacza na Dysku:**
  - pakiet bazowy (`26652290`, E-008): `plik_dla_tlumacza_v2.zip` (`11 449 704` B,
    SHA-256 `9bb4dcad…a5006` — **156 079** elementów / **130 043** unikalnych
    napisów);
  - **pakiet przyrostowy z aktualizacji `2026-11-26` (`26652290` → `26917622`,
    E-013): `pakiet_przyrostowy_26652290_do_26917622.zip`** (`155 363` B,
    SHA-256 `c20f006a1e7cb38a7a21b1b5f5f2307b784d5476527df72f4a0df9ba1953b3df`
    — wyłącznie nowości i poprawki z łatki: `2` nowe historie Tożsamości
    `P10117` Yi Sang i `P11217` Gregor, `3` nowe wpisy słownika mówców oraz `17`
    plików widoków, łącznie **1 733** unikalne puste pola `PL:`).
- **Importer zwrotek, generator `Lang/Polski/` i audyt aktualizacji (E-009 … E-013):**
  - `tools/import_zwrotki.py` waliduje zgodność źródeł, znaczniki TMP, zmienne
    `{0}`, słowa kluczowe `[Keyword]` i styl `DEN` w `BgmLyrics/*`, dziedziczy
    powtórzenia, obsługuje bezstratny import zwrotek ze starszego pakietu po
    aktualizacji gry (`--allow-older-package`) i zapisuje `tlumaczenie/` atomowo;
  - `tools/build_lang.py` buduje deterministyczne archiwum `Lang/Polski/` (pełny
    5-kluczowy `config.json` + czcionki OFL z `assets/fonts/` + pliki JSON z
    fallbackiem EN) — działanie potwierdzone w grze (`E-012`);
  - `tools/audit_update.py` porównuje buildy (`--old` lub czysto z Git
    `--old-rev`), wykrywa zmienione oryginały `KR` w `tlumaczenie/` i buduje
    pakiety uzupełniające (`--delta-scope files`) oraz ścisłe pakiety
    przyrostowe (`--delta-scope items`).

## Następny krok

1. **Właściciel:** przekazać tłumaczowi pakiet bazowy `plik_dla_tlumacza_v2.zip`
   wraz z dzisiejszym pakietem przyrostowym
   `pakiet_przyrostowy_26652290_do_26917622.zip` z folderu `Limbus Company` na
   Dysku, a po otrzymaniu zwrotki wrzucić ją do tego samego folderu.
2. **Agent:** zaimportować zwrotki (`tools/import_zwrotki.py`, z flagą
   `--allow-older-package` dla plików z `v2`), zbudować paczkę produkcyjną
   `LCB_PL_Polski_26917622.zip` (`tools/build_lang.py`) i wgrać na Dysk; gdy
   `OpenLethe` opublikuje zaktualizowane `StaticData`, dograć je przez
   `tools/import_data.py` i odświeżyć `czytanki/plik_ID_*`.

## Otwarte decyzje

Brak — wszystkie `O-01` … `O-07` zamknięte w [DECYZJE.md](DECYZJE.md).
