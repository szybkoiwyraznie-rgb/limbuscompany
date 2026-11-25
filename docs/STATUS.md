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
- Na Dysku właściciela utworzono folder „Limbus Company” z zestawem
  `LCB_ZBIERZ_DANE.zip` (1.0.0, SHA-256 `f12f73d4…656c`).

## Następny krok

1. **Właściciel:** z Dysku (folder „Limbus Company”) pobrać
   `LCB_ZBIERZ_DANE.zip`, rozpakować poza grą, uruchomić `URUCHOM.bat`,
   wgrać powstały `LCB_DANE_*.zip` do tego samego folderu. Instrukcja:
   `CZYTAJ_TO.txt` w zestawie.
2. **Właściciel (równolegle):** potwierdzić, czy tłumacz czyta po koreańsku
   (O-05). Od tego zależy, czy źródłem pakietów będzie `kr` (D-05), czy `en`.
3. **Agent:** walidacja + inspekcja (szczególnie parowanie `kr`↔`en`), wpis E-004, uzupełnienie
   [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md) faktami, pytanie O-06 (publiczne
   repo a `index/`), projekt `index/` i `tools/extract.py`.
4. Potem: pakiet próbny 000 (UI) + paczka testowa „Clear all caches” z
   polskimi znakami → pierwszy test w grze ([ROADMAP.md](ROADMAP.md)).

## Otwarte decyzje

O-01…O-06 w [DECYZJE.md](DECYZJE.md).
