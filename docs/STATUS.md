# Status

Stan na **2026-11-25**.

## Gdzie jesteśmy

**Etap 0 gotowy; Czytanki, plik ID i pakiet fabularny działają jako prototypy
na publicznych lustrach (E-005). Czekamy na paczkę ze zbieracza i uwagi do
układu.**

- Repozytorium urządzone według wzorców WWM/SRW: zasady (`AGENTS.md`),
  środowisko, lekcje, decyzje, polityka danych, workflow, CI (Ubuntu + Windows).
- Zbieracz `LCB_ZBIERZ_DANE 1.0.0` gotowy (testy na Windows CI, E-002); **nie
  był jeszcze uruchomiony na prawdziwej grze**. Zestaw na Dysku (folder
  „Limbus Company”).
- Decyzje z 2026-11-25: źródło przekładu **KR** potwierdzone (D-05), pliki gry i
  lustra tylko poza repo (D-06), pakiet i Czytanki w układzie SRW (D-07);
  czcionki — najpierw domyślna czcionka gry (O-03).
- **Kolejność fabuły z danych gry** (Teatr Opowieści, etapy, walki):
  `wiedza/indeks_fabuly.json` — 36 rozdziałów, 808 scen + 184 historie
  Identity; 34 rozdziały zgodne ze storylogs co do kolejności.
- **Próbki na Dysku:** `LCB_PROBKI_2026-11-25.zip` (36 Czytanek EN, Prolog +
  Canto I po koreańsku, 12 plików ID) i `plik_dla_tlumacza_v1.zip` (1001 scen,
  60 362 elementy do przetłumaczenia).

## Następny krok

1. **Właściciel:** przejrzeć próbki (układ Czytanki, pliku ID, pakietu) i
   zgłosić uwagi — po akceptacji układ zamrażamy (O-04). Pakiet można już dać
   tłumaczowi do oceny formy.
2. **Właściciel:** uruchomić zbieracz (`LCB_ZBIERZ_DANE.zip` z Dysku →
   `URUCHOM.bat`) i wgrać `LCB_DANE_*.zip` — wtedy budujemy pakiety z Twojego
   buildu zamiast z lustra.
3. **Agent:** `widoki.zip` (interfejs, słowa kluczowe, umiejętności pogrupowane
   po Identity), import zwrotki, paczka testowa `Lang/` z polskimi znakami w
   domyślnej czcionce.

## Otwarte decyzje

O-01…O-04 i O-06 w [DECYZJE.md](DECYZJE.md) (O-05 i O-07 zamknięte).
