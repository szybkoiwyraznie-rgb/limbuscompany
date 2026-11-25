# Status

Stan na **2026-11-25**.

## Gdzie jesteśmy

**Etap 0 — fundamenty gotowe; czekamy na pierwszą paczkę od zbieracza.**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` gotowy; na Windows CI przechodzi testy
  integracyjne z prawdziwym PowerShell 5.1 na sztucznej instalacji
  ([EXPERIMENT_LOG.md](EXPERIMENT_LOG.md), E-002). **Nie był jeszcze uruchomiony
  na prawdziwej grze.**
- Walidator zwrotki i inspekcja korpusu gotowe (testy syntetyczne).
- Na Dysku właściciela brak plików Limbus (wyszukiwanie 2026-11-25: 0 wyników).

## Następny krok

1. **Właściciel:** pobrać repozytorium (Code → Download ZIP), uruchomić
   `collector/URUCHOM.bat`, wgrać `LCB_DANE_*.zip` na Dysk (folder
   „Limbus Company”). Instrukcja: `collector/CZYTAJ_TO.txt`.
2. **Agent:** walidacja + inspekcja, wpis E-003, uzupełnienie
   [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md) faktami, pytanie O-06 (publiczne
   repo a `index/`), projekt `index/` i `tools/extract.py`.
3. Potem: pakiet próbny 000 (UI) + paczka testowa „Clear all caches” z
   polskimi znakami → pierwszy test w grze ([ROADMAP.md](ROADMAP.md)).

## Otwarte decyzje

O-01…O-06 w [DECYZJE.md](DECYZJE.md).
