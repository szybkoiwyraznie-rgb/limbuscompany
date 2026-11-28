# FALA 4 — RESUME (2026-11-25, po P84-REDO)

## Stan
- HEAD: P84-REDO (PRIORYTET-1 = `7a8632c`; parts_16 @ `774c480`; P88b `6926ee4`; P88 `d545b8e`).
- parts_1..16 DONE (96/96 każdy, assert set-equality OK). parts_16 = seq 1521–1627+1629+1631+1632, typo-pass DONE.
- PRIORYTET-1: nazwy przeciwników/skilli (1568 liści, 32 ledgery Enemies*/Skills_Enemy*) + piosenka BgmLyrics_Pv (22 seq) — ZAPISANE, testy 76/76. Skrypt: `local/pipeline/fala4_names_apply.py`.
- P84-REDO: redo decyzji P84 „Nazwy 1:1 (EN)" wg zasady usera — 310 liści w 36 plikach (Refraction/mirror enemies + „It Shall …" + „… Gossypium" + Master-portret + passives „Additionally"), testy 76/76. Skrypt: `local/pipeline/fala4_p84_apply.py` (mapa 197 EN→PL = single source of truth). Lekcja 31 w LESSONS.md = zasada universalna.

## ZASADA NAZW (universalna, user 2026-11-25 — lekcja 31)
KR = fonetyczny zapis nazwy obcej → Latin 1:1 (Kromer, Baba Yaga, Clover, Boss, Hongyu).
KR = konkretny wyraz → PL (불한당=Chuligan, 굴절된=Załamany, 목화=Bawełna, 인어=Syrena).
Kanon rodzin z `local/krmap.json` + przetłumaczonych plików. Szczegóły: SŁOWNIK bloki PRIORYTET-1 + P84-REDO.

## WZNOWIENIE tłumaczenia sekwencyjnego (fala 4, WSTRZYMANA)
- tl_input_17.txt wiersz 0 = seq 1633 (AbnoGuides#AbnormalityGuides_Refraction4.json).
- c17: Refraction4–6, exme, AbDlg_* per-Grzesznik (1668–1742). Czytać per-seq pythonem, paczki ~6 wierszy, print-cap [:19500].
- Procedura: czytaj → parts_N.json (96/96) → assert set-equality vs tl_input_N → typo-pass → commit+push bezzwłocznie → fala4_apply --fams <Fam> --dry-run → apply → testy → commit.
- Fam miedzy chunkami weryfikować nagłówkiem fam#plik.

## OPEN (do decyzji/zadania usera)
- ~5900 pozostałych stubów .name (kategorie spoza P84: base-1:1 innych partii — Dulcinea, Candle, Bloodbag, mermaid-base, Fanghunt base itd. + descs Core/Enemy Unit/Enemy Boss) — redo wg zasady przy kolejnych przebiegach.
- Harmonizacja E.G.O ID ↔ wrogów (Rozkwitłe E.G.O::Spicebush/Kamelia; Nadzorca Farmy).
- Ujednolicenia z SŁOWNIKU P84-REDO ('Marząca'→'Śniąca Elektryczna Owca'; 'Biuro Fanghunt'→'Biuro Łowców Kłów'; 'Sakiewka'→'Worek Krwi'; base 'Dulcinea'→'Dulcynea').
- Fala 4: pozostałe famy — AbnoGuides 308/231 (c15–17), EGOvoice 375/367, Announcer 1979/1978, PersonVoice 4742/4683, BgmLyrics 506/484 (Pv done), StoryTheater 134/134, RPGSystem 6880/6742, UI 65/0.

## Flagi
- (stare) FL1–FL5, canon-check „Prescript"→„Z-zlecenie", „barry-kate" transkreacja seq 1400.
- LEN: lim = ceil10(max(40, longest(KR,EN)*1.25+5)) dla .name; formy >lim wymagają skrótów (konwencje: Tingtangczyk, adjektyw-first „Ze Wspomnień", „Ożywiony Strażnik K Corp." bez „Punktu Kontrolnego").
- Ledger `pl` = literal `\n`; scope.json kr/en = realne `\n`; set_leaf wymaga logical name Z `.json`.
- Restart sandboxa czyści gitignored `local/` — skrypty/parts commitować bezzwłocznie po apply (parts i skrypty pipeline są w local/ — po apply natychmiast commit tlumaczenie/; local/ odtwarzalny z historii sesji).
