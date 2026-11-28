# FALA 4 — RESUME (2026-11-25, po PRIORYTET-1)

## Stan
- HEAD: PRIORYTET-1 (parts_16 @ 774c480; P88b 6926ee4; P88 d545b8e).
- parts_1..16 DONE (96/96 każdy, assert set-equality OK). parts_16 = seq 1521–1627+1629+1631+1632, typo-pass DONE.
- PRIORYTET-1: nazwy przeciwników/skilli (1568 liści, 32 ledgery Enemies*/Skills_Enemy*) + piosenka BgmLyrics_Pv (22 seq) — ZAPISANE w tlumaczenie/, testy 76/76. Skrypt: local/pipeline/fala4_names_apply.py. Mapa: base_todos.json (346) + IDX_PL w skrypcie + krmap reuse (base_krmap_hits.json).

## WZNOWIENIE tłumaczenia sekwencyjnego
- tl_input_17.txt wiersz 0 = seq 1633 (AbnoGuides#AbnormalityGuides_Refraction4.json: portrety/kamerdyner — „Uhm… Whassit…").
- c17: Refraction4–6, exme, AbDlg_* per-Grzesznik (1668–1742). Czytać per-seq pythonem, paczki ~6 wierszy, print-cap [:19500].
- Procedura: czytaj → parts_N.json (96/96) → assert set-equality vs tl_input_N → typo-pass → commit+push bezzwłocznie → fala4_apply --fams <Fam> --dry-run → apply → testy → commit.
- Fam miedzy chunkami weryfikować nagłówkiem fam#plik.

## OPEN (do zgłoszenia userowi)
- „Refracted …" names (TE/Refraction ledgers) — prefix wg zasady usera (fonetyka/znaczenie) — do tłumaczenia w następnym kroku.
- Harmonizacja E.G.O ID ↔ wrogów (Spicebush/Kamelia, Farmwatch/Nadzorca Farmy).
- Per-chapter unikalne stuby nazw spoza base-346 (z 1343 unikalnych).

## Flagi
- (stare) FL1–FL5, canon-check „Prescript"→„Z-zlecenie", „barry-kate" transkreacja seq 1400.
- LEN: przy nazwach limit = max(40, longest_src*1.25+5) zaokrąglone do 10 — krótkie EN nazwy → lim 40! Skróty stosowane: „Ożywiony Strażnik K Corp." (bez Punktu Kontrolnego), Tingtangczyk-demony, adjektyw-first Ze Wspomnień.
