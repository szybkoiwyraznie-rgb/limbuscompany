# Status

Stan na **2026-11-25**.

## Gdzie jesteśmy

**Cała infrastruktura techniczna projektu (Etapy 0–6) jest ukończona, a droga
end-to-end została potwierdzona w grze (`v.1.119.1`, build Steam `26652290`,
E-012): paczka `Lang/Polski/` z niemodyfikowanymi czcionkami SIL OFL 1.1
(`Pretendard-Regular.ttf` + `Mikodacs.otf`) uruchamia grę po polsku i czysto
wyświetla komplet 18/18 polskich znaków (`ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ`). Kompletny
pakiet `plik_dla_tlumacza_v2.zip` (100% gry) czeka na Dysku na pierwszą zwrotkę
od tłumacza.**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows,
  `60/60` testów zielonych).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` przeszedł pełny przebieg na instalacji
  właściciela (`LCB_DANE_20261125_190908_2e6403.zip`, build Steam **`26652290`**,
  7320 plików, 0 błędów — E-007).
- Wszystkie decyzje projektowe zamknięte (`D-01` … `D-10`, brak otwartych `O-*`):
  źródło przekładu **KR** (D-05), teksty gry w repozytorium jako JSON/MD bez
  binariów (D-06), układ Czytanek zaakceptowany i zamrożony (D-07), kompletny
  pakiet 100% gry naraz (D-08), nazwa języka **`Polski`** i 5-kluczowy
  `Lang/config.json` (D-09), niemodyfikowane czcionki SIL OFL 1.1 w
  `assets/fonts/` potwierdzone w grze (D-10, zamyka O-03).
- **Teksty gry i Czytanki w repozytorium** (E-006, E-007): `index/localize/{kr,en}`
  bajt w bajt z instalacji Steam właściciela (build `26652290`: 2449 `kr`,
  2406 `en`); `index/static-data/` z OpenLethe; Czytanki i pliki ID w `czytanki/`.
- **Kompletny pakiet dla tłumacza na Dysku (`plik_dla_tlumacza_v2.zip`, E-008):**
  11 449 704 B (~10,9 MiB), SHA-256 `9bb4dcad…a5006` (`sceny.zip` + `widoki.zip`,
  łącznie **156 079** elementów i **130 043** unikalnych napisów do przekładu).
- **Importer zwrotek, generator `Lang/Polski/` i audyt aktualizacji (E-009 … E-012):**
  - `tools/import_zwrotki.py` waliduje zgodność źródeł, znaczniki TMP, zmienne
    `{0}`, słowa kluczowe `[Keyword]` i styl `DEN` w `BgmLyrics/*`, dziedziczy
    powtórzenia i zapisuje `tlumaczenie/` atomowo;
  - `tools/build_lang.py` buduje deterministyczne archiwum `Lang/Polski/` (pełny
    5-kluczowy `config.json` + czcionki OFL z `assets/fonts/` + 2406 plików JSON
    z fallbackiem EN) — działanie potwierdzone w grze (`E-012`);
  - `tools/audit_update.py` porównuje buildy po aktualizacjach gry, wykrywa
    zmienione oryginały `KR` w `tlumaczenie/` i generuje pakiety uzupełniające
    (`--delta-out`).

## Następny krok

1. **Właściciel:** przekazać `plik_dla_tlumacza_v2.zip` z Dysku tłumaczowi i po
   otrzymaniu pierwszej partii plików `.md` wrzucić zwrotkę do folderu `Limbus
   Company` na Dysku (na czas normalnego grania przed pierwszą zwrotką można
   przełączyć `Select Custom Language` z powrotem na domyślny język lub usunąć
   testowy folder `LimbusCompany_Data\Lang`, aby zniknęły znaczniki `[PL: …]`).
2. **Agent:** zaimportować pierwszą zwrotkę (`tools/import_zwrotki.py`),
   zbudować pierwszą paczkę produkcyjną `LCB_PL_Polski_<build>.zip`
   (`tools/build_lang.py`) i wgrać na Dysk; po cotygodniowej aktualizacji gry
   przeprowadzić obieg `import_data.py` + `audit_update.py --delta-out`.

## Otwarte decyzje

Brak — wszystkie `O-01` … `O-07` zamknięte w [DECYZJE.md](DECYZJE.md).
