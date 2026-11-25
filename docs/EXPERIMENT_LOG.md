# Dziennik eksperymentów

Każdy wpis: data, rodzaj (**fakt ze źródła / test syntetyczny / test na
kopii plików / test w grze**), wejście (build, SHA-256), metoda, wynik z
liczbami, ograniczenia. Bez tekstów gry i prywatnych ścieżek. Najnowsze na dole.

## E-001 · 2026-11-25 · rozpoznanie źródeł (fakt ze źródła)

- Oficjalne ogłoszenie Custom Language (Steam, 2025-03-31): położenie
  `Localize/{kr,en,jp}`, struktura `Lang/<Nazwa>/`, prefiksy usuwane, `Font/`,
  `config.json`. Szczegóły: [FEASIBILITY.md](FEASIBILITY.md).
- Publiczna paczka FR (`Eden-Office/LimbusCompanyBusFR`, commit `fcefec1`):
  2423 pliki JSON, ~34 MB, korzeń `{"dataList": […]}`; StoryData 999 plików.
- Polska paczka fanowska (`Echodial/…`, commit `12a3ebe`): 1980 plików,
  `lang` = `Polish`, `Font/replacement_map.json`. Tylko analiza techniczna.
- Dysk właściciela: wyszukiwanie nazw zawierających „Limbus” — 0 plików.
- Ograniczenie: to układ paczek fanowskich, nie oryginalnego `Localize`;
  struktura źródła do potwierdzenia na pierwszej paczce.

## E-002 · 2026-11-25 · zbieracz na Windows CI (test syntetyczny)

- Wejście: sztuczna instalacja z wymyślonymi plikami (`tests/synthetic_localize.py`),
  ścieżki z polskimi znakami, spacjami i nawiasami; Windows PowerShell 5.1 na
  `windows-latest`, Python 3.11 i 3.12.
- Pierwszy przebieg (commit `a989822`): 5/5 testów integracyjnych **nie
  przeszło** — `Get-FileHash` „nie jest rozpoznany” (cmdlet z modułu
  skryptowego `Microsoft.PowerShell.Utility.psm1`; PSModulePath na runnerze
  wskazuje moduły PowerShell 7). Ten sam problem może wystąpić u gracza.
- Poprawka (commit `dd45626`): SHA-256 przez .NET
  (`System.Security.Cryptography.SHA256`); test zakazujący cmdletów z modułów
  skryptowych. Wynik: wszystkie 4 zadania CI (Ubuntu/Windows × 3.11/3.12) zielone,
  w tym: pełne zbieranie tylko do odczytu, BAT z przeciągniętym folderem,
  brak języka → kod 2 i stan `partial`, wykrycie gry przez bibliotekę Steam
  i `appmanifest_1973530.acf`, kolejne uruchomienia bez nadpisania.
- Ograniczenie: nie uruchomiono na prawdziwej grze ani u właściciela.

## E-003 · 2026-11-25 · dostarczenie zestawu przez Dysk (test na kopii)

- `python tools/build_collector_kit.py` → `LCB_ZBIERZ_DANE.zip`, 29 652 B,
  SHA-256 `f12f73d4d4d5496ecca9518cff7b1589ff6a25319443402f299d8b7a4426656c`,
  członkowie: `CZYTAJ_TO.txt`, `URUCHOM.bat`, `zbierz.ps1`.
- Utworzono folder Dysku „Limbus Company” i wgrano zestaw konektorem; Dysk
  zwraca ten sam rozmiar i `sha256Checksum` — bajty nienaruszone. (W WWM
  konektor odrzucał ZIP z `.ps1`; tutaj nie.)
- Ograniczenie: nie sprawdzono, czy Windows/przeglądarka u właściciela nie
  zablokuje pobranego ZIP-a; BAT i tak zdejmuje znacznik pobrania z `*.ps1`.
