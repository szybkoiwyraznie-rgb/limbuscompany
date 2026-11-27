# Paczka AI P43 (Fala 3 · 3A) — Grzesznik 01 — Yi Sang

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P43_3a_01_yi_sang.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P43_3a_01_yi_sang.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #01: Yi Sang (이상)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 이상
   źródło: Characters.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang
2. [Akta więźnia — nazwa] 이상
   źródło: IntroduceCharacter.json :: dataList[id=이상].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Yi Sang — LCB 수감자
- ID Tożsamości: `10101` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 72 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Sinking

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10101].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10101].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10101].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 이상의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10101].desc
   limit: do 120 znaków
   EN: Yi Sang’s 1st Identity
   PL: Pierwsza Tożsamość Yi Sanga
7. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 쳐내기
   źródło: Skills.json :: dataList[id=1010101].levelList[level=1].name ; dataList[id=1010101].levelList[level=2].name ; dataList[id=1010101].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Deflect
   PL: Odbicie
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1010101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 1 Zatonięcia
9. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 2 Zatonięcia
10. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 Zatonięcia
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 밀어 찌르기
   źródło: Skills.json :: dataList[id=1010102].levelList[level=1].name ; dataList[id=1010102].levelList[level=2].name ; dataList[id=1010102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: End-stop Stab
   PL: Pchnięcie z Odepchnięciem
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttackHead] Nakłada +1 Licznika Zatonięcia
13. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여. 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada 1 Zatonięcia i +1 Licznika Zatonięcia
14. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여. 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada 2 Zatonięcia i +1 Licznika Zatonięcia
15. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연격
   źródło: Skills.json :: dataList[id=1010103].levelList[level=3].name ; dataList[id=1010103].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 6 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Enjamb
   PL: Przerzutnia
16. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력이 0미만이면 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target’s SP is below 0, inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] Jeżeli Poczytalność celu spadnie poniżej 0, nakłada w następnej turze 1 Wrażliwości
17. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 Zatonięcia
19. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력이 0미만이면 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target has less than 0 SP, inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] Jeżeli cel ma mniej niż 0 Poczytalności, nakłada w następnej turze 1 Wrażliwości
20. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1010104].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL: Garda
21. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Gloom) — nazwa] 정보전달
   źródło: Passives.json :: dataList[id=1010101].name
   limit: do 40 znaków
   EN: Information Relay
   PL: Przekaz Informacji
22. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Gloom) — opis] 조작 패널에서 자신의 뒤에 있는 아군 2명에게 피해량 증가 1 부여
   źródło: Passives.json :: dataList[id=1010101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Apply 1 [AttackDmgUp] to 2 allies placed after this unit on the Dashboard
   PL: Na panelu sterowania nakłada 1 Wzrostu Obrażeń na 2 sojuszników ustawionych za tą jednostką
23. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 정보중화
   źródło: Passives.json :: dataList[id=1010121].name
   limit: do 40 znaków
   EN: Information Neutralization
   PL: Neutralizacja Informacji
24. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 10 회복
   źródło: Passives.json :: dataList[id=1010121].desc
   limit: do 120 znaków
   EN: Turn End: If 1 ally that has the lowest SP lost SP this turn, heal 10 SP for the said ally
   PL: Sojusznik z najniższą Poczytalnością: jeżeli w tej turze stracił Poczytalność, na koniec tury odzyskuje 10 Poczytalności

## [00] Seven Assoc. South Section 6 — Yi Sang — 남부 세븐 협회 6과
- ID Tożsamości: `10102` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 5–6 / 5–7 / 5–8 / 5–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

25. [Karta Tożsamości — tytuł] 남부 세븐 협회\n6과
   źródło: Personalities.json :: dataList[id=10102].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 6
   PL: Południowe Stowarzyszenie Seven\nSekcja 6
26. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10102].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10102].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Karta Tożsamości — opis] 이상의 두번째 인격
   źródło: Personalities.json :: dataList[id=10102].desc
   limit: do 120 znaków
   EN: Yi Sang’s 2nd Identity
   PL: Druga Tożsamość Yi Sanga
29. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 플레쉬
   źródło: Skills.json :: dataList[id=1010201].levelList[level=1].name ; dataList[id=1010201].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Flèche
   PL: Flèche
30. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1010201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 1 Rozdarcia
31. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1010201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 2 Rozdarcia
32. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 리포스트
   źródło: Skills.json :: dataList[id=1010203].levelList[level=1].name ; dataList[id=1010203].levelList[level=2].name ; dataList[id=1010203].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Riposte
   PL: Riposta
33. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WinDuel] 다음 턴에 마비 3 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=1].desc ; dataList[id=1010203].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Paralysis]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Paralysis] = 마비 / Paralyze
   EN: [WinDuel] Inflict 3 [Paralysis] next turn
   PL: [WinDuel] Nakłada w następnej turze 3 Paraliżu
34. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Wrażliwości
35. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WinDuel] 다음 턴에 마비 3 부여\n[WinDuel] 파열 횟수 1 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Paralysis], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Paralysis] = 마비 / Paralyze; [Burst] = 파열 / Rupture
   EN: [WinDuel] Inflict 3 [Paralysis] next turn\n[WinDuel] Inflict +1 [Burst] Count
   PL: [WinDuel] Nakłada w następnej turze 3 Paraliżu\n[WinDuel] Nakłada +1 Licznika Rozdarcia
36. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 Rozdarcia
37. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 물리네
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].name ; dataList[id=1010202].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Moulinet
   PL: Moulinet
38. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Final Coin inflicts +1 more Stack of its effect
   PL: [OnSucceedAttack] Ostatnia moneta nadaje o 1 więcej stosów swojego efektu
39. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 관통 취약 1 부여
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1010202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Wrażliwości na Kłucie
41. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Final Coin inflicts +1 more Stack of its effects
   PL: [OnSucceedAttack] Ostatnia moneta nadaje o 1 więcej stosów swoich efektów
42. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1010202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1010204].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 9 · monety: 1 (+3)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Glut.) — nazwa] 관찰
   źródło: Passives.json :: dataList[id=1010201].name
   limit: do 40 znaków
   EN: Acute Studies
   PL: Obserwacja
46. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Glut.) — opis] 합 진행 시 대상의 합 위력 -2
   źródło: Passives.json :: dataList[id=1010201].desc
   limit: do 120 znaków
   EN: In a Clash, the opponent has Clash Power -2
   PL: Podczas Starcia Moc Starcia celu -2
47. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 분석
   źródło: Passives.json :: dataList[id=1010221].name
   limit: do 40 znaków
   EN: Observational Eye
   PL: Analiza
48. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 최대 체력이 가장 높은 아군 1명 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1010221].desc
   limit: do 120 znaków
   EN: 1 ally that has the highest max HP gains Clash Power +1 in a Clash
   PL: 1 sojusznik z najwyższym Maks. HP zyskuje podczas Starcia Moc Starcia +1

## [000] Blade Lineage Salsu — Yi Sang — 검계 살수
- ID Tożsamości: `10103` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

49. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=10103].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL: Ród Ostrza\nSalsu
50. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10103].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10103].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Karta Tożsamości — opis] 이상의 세번째 인격
   źródło: Personalities.json :: dataList[id=10103].desc
   limit: do 120 znaków
   EN: Yi Sang’s 3rd Identity
   PL: Trzecia Tożsamość Yi Sanga
53. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 격세
   źródło: Skills.json :: dataList[id=1010301].levelList[level=1].name ; dataList[id=1010301].levelList[level=2].name ; dataList[id=1010301].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Striker’s Stance
   PL: Postawa Uderzeniowa
54. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1010301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 1 Oddechu
55. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1010301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 3 Oddechu
56. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 호흡 횟수 2 얻음
   źródło: Skills.json :: dataList[id=1010301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zyskuje +2 Licznika Oddechu
57. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 두의틀기
   źródło: Skills.json :: dataList[id=1010302].levelList[level=1].name ; dataList[id=1010302].levelList[level=2].name ; dataList[id=1010302].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Heel Turn
   PL: Zwrot o Obcasie
58. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +1 [Breath] Count next turn
   PL: [WinDuel] Zyskuje +1 Licznika Oddechu w następnej turze
59. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 다음 턴에 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1010302].levelList[level=2].desc ; dataList[id=1010302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +2 [Breath] Count next turn
   PL: [WinDuel] Zyskuje +2 Licznika Oddechu w następnej turze
60. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 이면찬자
   źródło: Skills.json :: dataList[id=1010303].levelList[level=3].name ; dataList[id=1010303].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 8 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Flank Thrust
   PL: Pchnięcie z Boku
61. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1010303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1010303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 2 Oddechu
62. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills.json :: dataList[id=1010303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +50% damage on Critical Hit
   PL: Zadaje +50% obrażeń Krytycznych
63. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1010303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL: [WhenUse] Zyskuje 2 Oddechu
64. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +70%
   źródło: Skills.json :: dataList[id=1010303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +70% damage on Critical Hit
   PL: Zadaje +70% obrażeń Krytycznych
65. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1010304].levelList[level=1].name ; dataList[id=1010304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 10 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Counter
   PL: Kontra
66. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +70%
   źródło: Skills.json :: dataList[id=1010304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 냉정
   źródło: Passives.json :: dataList[id=1010301].name
   limit: do 40 znaków
   EN: Poised
   PL: Opanowanie
68. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 합 승리 시 호흡 횟수 1 증가
   źródło: Passives.json :: dataList[id=1010301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On Clash Win, gain +1 [Breath] Count
   PL: Po wygranej Starciu zyskuje +1 Licznika Oddechu
69. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 사사
   źródło: Passives.json :: dataList[id=1010321].name
   limit: do 40 znaków
   EN: Bestow
   PL: Darowanie
70. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 정신력이 가장 높은 아군 1명 스킬의 효과로 얻는 호흡 횟수 +1
   źródło: Passives.json :: dataList[id=1010321].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: 1 ally that has the highest SP gains +1 more [Breath] Count from Skill effects
   PL: 1 sojusznik z najwyższą Poczytalnością zyskuje o 1 więcej Licznika Oddechu z efektów Umiejętności

## [000] Effloresced E.G.O::Spicebush — Yi Sang — 개화 E.G.O:: 동백
- ID Tożsamości: `10104` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Sinking

71. [Karta Tożsamości — tytuł] 개화 E.G.O::\n동백
   źródło: Personalities.json :: dataList[id=10104].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Effloresced E.G.O::Spicebush
   PL: Rozkwitłe E.G.O::\nSpicebush
72. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10104].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10104].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Karta Tożsamości — opis] 이상의 네번째 인격
   źródło: Personalities.json :: dataList[id=10104].desc
   limit: do 120 znaków
   EN: Yi Sang’s 4th Identity
   PL: Czwarta Tożsamość Yi Sanga
75. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 움트는 봉우리
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].name ; dataList[id=1010401].levelList[level=2].name ; dataList[id=1010401].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Sprouting Bud
   PL: Kiełkujący Pąk
76. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 진동 횟수 2를 얻음
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL: [WhenUse] Zyskuje +2 Licznika Wstrząsu
77. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze +1 Licznika Zatonięcia
78. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 진동 횟수 3을 얻음
   źródło: Skills.json :: dataList[id=1010401].levelList[level=2].desc ; dataList[id=1010401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL: [WhenUse] Zyskuje +3 Licznika Wstrząsu
80. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze +1 Licznika Zatonięcia
81. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 횟수 2 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze +2 Licznika Zatonięcia
83. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 찰나의 꽃바람
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].name ; dataList[id=1010402].levelList[level=2].name ; dataList[id=1010402].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Moment's Floral Breeze
   PL: Ulotny Wiatr Kwiatów
84. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [StartBattle] 자신의 진동 횟수를 6 소모하여 공격 가중치 3 스킬로 변경
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].desc ; dataList[id=1010402].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 6 [Vibration] Count on self to turn this into an AoE skill with 3 Atk Weight
   PL: [StartBattle] Zużywa 6 Licznika Wstrząsu, by zamienić tę Umiejętność w atak obszarowy o wadze ataku 3
85. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 2 Zatonięcia
86. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 Zatonięcia
89. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1010402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 자신의 진동 횟수를 6 소모하여 공격 가중치 3 스킬로 변경\n메인 타겟의 침잠 횟수가 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1010402].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Vibration], [Sinking]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [StartBattle] Consume 6 [Vibration] Count on self to turn this into an AoE skill with 3 Atk Weight\nIf main target has 6+ [Sinking] Count, Coin Power +1
   PL: [StartBattle] Zużywa 6 Licznika Wstrząsu, by zamienić tę Umiejętność w atak obszarowy o wadze ataku 3\nJeżeli główny cel ma 6+ Licznika Zatonięcia, Moc Monet +1
92. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 피를 머금은 향기
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].name ; dataList[id=1010403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 6 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Bloodsteeped Scent
   PL: Zapach Nasiąknięty Krwią
93. [Umiejętność 3 (×1) (ulepszenia 1,4) — opis] [DefeatDuel] 정신력 20 감소\n[WhenUse] 진동 횟수 6을 얻음
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].desc ; dataList[id=1010403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [WhenUse], [Vibration]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [DefeatDuel] Lose 20 SP\n[WhenUse] Gain +6 [Vibration] Count
   PL: [DefeatDuel] Traci 20 Poczytalności\n[WhenUse] Zyskuje +6 Licznika Wstrząsu
94. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika Zatonięcia
95. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 6 이상이면, 침잠쇄도
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1010403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [SinkingSurge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [SinkingSurge] = 침잠쇄도 / Sinking Deluge
   EN: [OnSucceedAttack] If target has 6+ [Sinking], cause [SinkingSurge]
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Sinking], wywołuje Potop Zatonięcia
97. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수가 10 이상이면, 피해량의 30%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has 10+ [Vibration] Count, deal 30% of damage dealt as bonus damage
   PL: [OnSucceedAttack] Jeżeli ta jednostka ma 10+ Licznika Wstrząsu, zadaje dodatkowe obrażenia równe 30% zadanych obrażeń
98. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수가 10 이상이면, 피해량의 40%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1010403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has 10+ [Vibration] Count, deal 40% of damage dealt as bonus damage
   PL: [OnSucceedAttack] Jeżeli ta jednostka ma 10+ Licznika Wstrząsu, zadaje dodatkowe obrażenia równe 40% zadanych obrażeń
99. [Obrona (ulepszenie 1) — nazwa] 흩날리는 잔향
   źródło: Skills.json :: dataList[id=1010404].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Scattering Aroma
   PL: Rozwiewany Aromat
100. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1010404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Sinking]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedEvade] Inflict 1 [Sinking]
   PL: [OnSucceedEvade] Nakłada 1 Zatonięcia
101. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Sloth) — nazwa] 만개
   źródło: Passives.json :: dataList[id=1010401].name
   limit: do 40 znaków
   EN: Full Bloom
   PL: Pełen Rozkwit
102. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Sloth) — opis] 2명 이상을 공격할 때 피해량 +30%
   źródło: Passives.json :: dataList[id=1010401].desc
   limit: do 120 znaków
   EN: When attacking 2 or more targets at once, deal +30% damage
   PL: Przy atakowaniu 2 lub więcej celów naraz zadaje +30% obrażeń
103. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 알싸한 봄바람
   źródło: Passives.json :: dataList[id=1010421].name
   limit: do 40 znaków
   EN: Pungent Spring Breeze
   PL: Ostry Wiosenny Wiatr
104. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 정신력이 가장 낮은 아군 1명이 2명 이상을 공격할 때 피해량 +10%
   źródło: Passives.json :: dataList[id=1010421].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest SP deals +10% damage when attacking 2 or more targets at once
   PL: 1 sojusznik z najniższą Poczytalnością zadaje +10% obrażeń przy atakowaniu 2 lub więcej celów naraz

## [00] Molar Office Fixer — Yi Sang — 어금니 사무소 해결사
- ID Tożsamości: `10105` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 73 · szybkość: 3–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

105. [Karta Tożsamości — tytuł] 어금니 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10105].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molar Office\nFixer
   PL: Biuro Trzonowca\nFixer
106. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10105].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10105].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Karta Tożsamości — opis] 이상의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10105].desc
   limit: do 120 znaków
   EN: Yi Sang's 5th Identity
   PL: Piąta Tożsamość Yi Sanga
109. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 침착하게
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=1].name ; dataList[id=1010501].levelList[level=2].name ; dataList[id=1010501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Stay Calm
   PL: Zachowaj Spokój
110. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 자신의 진동 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +3 [Vibration] Count
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje +3 Licznika Wstrząsu
111. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttackHead] Nakłada +2 Licznika Wstrząsu
112. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +4 [Vibration] Count\n[WhenUse] Gain +2 [Vibration] Count
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje +4 Licznika Wstrząsu\n[WhenUse] Zyskuje +2 Licznika Wstrząsu
113. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Wstrząsu
114. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 진동 횟수 2 증가\n자신의 진동 횟수가 5 이상일 때 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +4 [Vibration] Count\n[WhenUse] Gain +2 [Vibration] Count\nAt 5+ [Vibration] Count, gain Coin Power +1
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje +4 Licznika Wstrząsu\n[WhenUse] Zyskuje +2 Licznika Wstrząsu\nPrzy 5+ Licznika Wstrząsu Moc Monet +1
115. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도박수
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=1].name ; dataList[id=1010502].levelList[level=2].name ; dataList[id=1010502].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Gamble
   PL: Zakład
116. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬이 버려지면 자신의 진동 횟수 3 증가\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +3 [Vibration] Count\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje +3 Licznika Wstrząsu\n[WhenUse] Odrzuca 1 Umiejętność najniższej Rangi ze wszystkich swoich slotów
117. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수가 5 이상일 때, 진동 폭발. 대상의 진동 횟수 2 감소
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] At 5+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 2
   PL: [OnSucceedAttack] Przy 5+ Licznika Wstrząsu wywołuje Wybuch Wstrząsu; następnie zmniejsza Licznik Wstrząsu celu o 2
118. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=2].desc ; dataList[id=1010502].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +4 [Vibration] Count\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje +4 Licznika Wstrząsu\n[WhenUse] Odrzuca 1 Umiejętność najniższej Rangi ze wszystkich swoich slotów
119. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수가 5 이상일 때, 진동 폭발. 대상의 진동 횟수 2 감소
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1010502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Wstrząsu
122. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 어금니 갈기
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].name ; dataList[id=1010503].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Grinding the Molars
   PL: Mielenie Trzonowców
123. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림.\n[WhenUse] 자신의 진동 횟수 10을 소모하여 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +1
   PL: [WhenUse] Odrzuca 1 Umiejętność najniższej Rangi ze wszystkich swoich slotów.\n[WhenUse] Zużywa 10 Licznika Wstrząsu, by zyskać Moc Monet +1
124. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1010503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] Nakłada 4 Wstrząsu
125. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 스킬 사용 시 진동 횟수를 소모했으면, 진동 폭발
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1010503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If the Skill consumed [Vibration] Count, trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Jeżeli Umiejętność zużyła Licznik Wstrząsu, wywołuje Wybuch Wstrząsu
126. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 방어 레벨 감소 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttackHead] Nakłada 2 Spadku Poziomu Obrony
127. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 스킬 사용 시 진동 횟수를 소모했으면, 진동 폭발
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1010503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림.\n[WhenUse] 자신의 진동 횟수 10을 소모하여 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL: [WhenUse] Odrzuca 1 Umiejętność najniższej Rangi ze wszystkich swoich slotów.\n[WhenUse] Zużywa 10 Licznika Wstrząsu, by zyskać Moc Monet +2
129. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttack] Nakłada 2 Spadku Poziomu Obrony
130. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-01.json :: dataList[id=1010504].levelList[level=1].name ; dataList[id=1010504].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+5)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010504].levelList[level=1].desc ; dataList[id=1010504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL: [WhenUse] Odrzuca 1 Umiejętność najniższej Rangi ze wszystkich swoich slotów
132. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 이럴 때 일수록...
   źródło: Passives.json :: dataList[id=1010501].name
   limit: do 40 znaków
   EN: In Times Like These...
   PL: W Takich Chwilach...
133. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] 적에게 진동 폭발 시 입히는 흐트러짐 손상 4 당 [DefenseDown] 1 부여 (턴마다 적 1명당 최대 5)
   źródło: Passives.json :: dataList[id=1010501].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [VibrationExplosion]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Upon triggering [VibrationExplosion] on an enemy, inflict 1 [DefenseDown] for every 4 Stagger Threshold raised (max 5 [DefenseDown] per enemy per turn)
   PL: Przy wywołaniu Wybuchu Wstrząsu na wrogu nakłada 1 [DefenseDown] za każde 4 podniesienia Progu Oszołomienia (maks. 5 [DefenseDown] na wroga na turę)
134. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 벌려진 일 수습
   źródło: Passives.json :: dataList[id=1010521].name
   limit: do 40 znaków
   EN: Cleaning Up the Mess
   PL: Naprawianie Szkód
135. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 최대 체력이 가장 낮은 아군 1명이 적에게 진동 폭발 시 입히는 흐트러짐 손상 4 당 다음 턴에 [DefenseDown] 1 부여 (턴마다 적 1명당 최대 3)
   źródło: Passives.json :: dataList[id=1010521].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [VibrationExplosion]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: 1 ally that has the lowest max HP: For every 4 Stagger Threshold raised by triggering [VibrationExplosion] on an enemy, inflict 1 [DefenseDown] next turn (max 3 [DefenseDown] per enemy per turn)
   PL: 1 sojusznik z najniższym Maks. HP: za każde 4 podniesienia Progu Oszołomienia zadane wywołaniem Wybuchu Wstrząsu na wrogu, nakłada w następnej turze 1 [DefenseDown] (maks. 3 [DefenseDown] na wroga na turę)

## [000] W Corp. L3 Cleanup Agent — Yi Sang — W사 3등급 정리 요원
- ID Tożsamości: `10106` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

136. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10106].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Agent
   PL: W Corp. L3\nAgent Oczyszczania
137. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10106].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10106].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Karta Tożsamości — opis] 이상의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10106].desc
   limit: do 120 znaków
   EN: Yi Sang's 6th Identity
   PL: Szósta Tożsamość Yi Sanga
140. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 차원 긋기
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=1].name ; dataList[id=1010601].levelList[level=2].name ; dataList[id=1010601].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Dimensional Slit
   PL: Nacięcie Wymiaru
141. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=1].desc ; dataList[id=1010601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL: [WhenUse] Zyskuje +2 Licznika Ładowania
142. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika Ładowania
143. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가\n충전 횟수가 10 이상이면, 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count\nAt 10+ [Charge] Count, Coin Power +2
   PL: [WhenUse] Zyskuje +2 Licznika Ładowania\nPrzy 10+ Licznika Ładowania Moc Monet +2
145. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
146. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].name ; dataList[id=1010602].levelList[level=2].name ; dataList[id=1010602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Energy Cycle
   PL: Obieg Energii
147. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 5 증가
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +5 [Charge] Count
   PL: [WhenUse] Zyskuje +5 Licznika Ładowania
148. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Spętania
149. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
150. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 6 증가\n충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +6 [Charge] Count\nAt 10+ [Charge] Count, Coin Power +1
   PL: [WhenUse] Zyskuje +6 Licznika Ładowania\nPrzy 10+ Licznika Ładowania Moc Monet +1
151. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spętania
152. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수가 10 이상이면, 파열 3 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 10+ [Charge] Count, inflict 3 [Burst]
   PL: [OnSucceedAttack] Przy 10+ Licznika Ładowania nakłada 3 Rozdarcia
153. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 7 증가\n충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +7 [Charge] Count\nAt 10+ [Charge] Count, Coin Power +1
   PL: [WhenUse] Zyskuje +7 Licznika Ładowania\nPrzy 10+ Licznika Ładowania Moc Monet +1
154. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수가 10 이상이면,  파열 3 부여, 파열 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 10+ [Charge] Count, inflict 3 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] Przy 10+ Licznika Ładowania nakłada 3 Rozdarcia i +2 Licznika Rozdarcia
155. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 차원의 틈
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].name ; dataList[id=1010603].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Dimensional Rift
   PL: Szczelina Wymiaru
156. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 충전 횟수가 15 미만이면, 충전 횟수를 10 소모하여 코인 위력 +1\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At less than 15 [Charge] Count, consume 10 [Charge] Count to gain Coin Power +1\n[WhenUse] Consume 15 [Charge] Count to gain Coin Power +2
   PL: [WhenUse] Przy mniej niż 15 Licznika Ładowania zużywa 10 Licznika Ładowania, by zyskać Moc Monet +1\n[WhenUse] Zużywa 15 Licznika Ładowania, by zyskać Moc Monet +2
157. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1010603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1010603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 소모한 충전 횟수 5 당 파열 2 부여 (최대 6)
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 2 [Burst] for every 5 [Charge] Count consumed by the Skill (max 6)
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia za każde 5 Licznika Ładowania zużytego przez Umiejętność (maks. 6)
160. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 스킬 사용시 충전 횟수를 15 소모하였으면, 차원 균열 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1010603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] If the Skill consumed 15 [Charge] Count upon use, inflict 2 [DimensionRift]
   PL: [OnSucceedAttack] Jeżeli Umiejętność zużyła przy użyciu 15 Licznika Ładowania, nakłada 2 Pęknięcia Wymiaru
161. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [EnemyKill] 충전 역장 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [ChargeForceField]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [EnemyKill] Gain 3 [ChargeForceField]
   PL: [EnemyKill] Zyskuje 3 Bariery Ładunku
162. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 충전 횟수가 15 미만이면, 충전 횟수를 10 소모하여 코인 위력 +1\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +2\n[BeforeAttack] 충전 횟수를 15 소모했다면, 파열 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BeforeAttack], [Charge], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [WhenUse] At less than 15 [Charge] Count, consume 10 [Charge] Count to gain Coin Power +1\n[WhenUse] Consume 15 [Charge] Count to gain Coin Power +2\n[BeforeAttack] If 15 [Charge] Count has been consumed, inflict +3 [Burst] Count
   PL: [WhenUse] Przy mniej niż 15 Licznika Ładowania zużywa 10 Licznika Ładowania, by zyskać Moc Monet +1\n[WhenUse] Zużywa 15 Licznika Ładowania, by zyskać Moc Monet +2\n[BeforeAttack] Jeżeli zużyto 15 Licznika Ładowania, nakłada +3 Licznika Rozdarcia
163. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 소모한 충전 횟수 5 당 파열 3 부여 (최대 9)
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 3 [Burst] for every 5 [Charge] Count consumed by the Skill (max 9)
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia za każde 5 Licznika Ładowania zużytego przez Umiejętność (maks. 9)
164. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [EnemyKill] 충전 역장 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [ChargeForceField]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [EnemyKill] Gain 5 [ChargeForceField]
   PL: [EnemyKill] Zyskuje 5 Bariery Ładunku
165. [Obrona (ulepszenia 1,4) — nazwa] 텅 빈 차원
   źródło: Skills_personality-01.json :: dataList[id=1010604].levelList[level=1].name ; dataList[id=1010604].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Hollow Dimension
   PL: Pusty Wymiar
166. [Obrona (ulepszenie 1) — opis] 충전 횟수 5당 기본 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1010604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Base Power +1 for every 5 [Charge] Count (max 2)
   PL: Moc Bazowa +1 za każde 5 Licznika Ładowania (maks. 2)
167. [Obrona (ulepszenie 4) — opis] 충전 횟수 5당 기본 위력 +1 (최대 2)\n[OnSucceedEvade] 다음 턴에 처음으로 스킬로 부여하는 파열 +1 (턴 당 최대 증가량 : 3)
   źródło: Skills_personality-01.json :: dataList[id=1010604].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Charge], [Burst]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: Base Power +1 for every 5 [Charge] Count (max 2)\n[OnSucceedEvade] Next turn, when inflicting [Burst] with a Skill for the first time, inflict +1 more [Burst] (max +3 per turn)
   PL: Moc Bazowa +1 za każde 5 Licznika Ładowania (maks. 2)\n[OnSucceedEvade] W następnej turze, gdy Umiejętność po raz pierwszy nadaje Rozdarcie, nadaje o 1 więcej Rozdarcia (maks. +3 na turę)
168. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 비워낸 생각
   źródło: Passives.json :: dataList[id=1010601].name
   limit: do 40 znaków
   EN: Emptied Thought
   PL: Opróżniona Myśl
169. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] - 턴 종료 시 자신의 충전 횟수 5 당 다음 턴에 신속 1을 얻음. (최대 2)\n- 자신이 스킬로 충전 횟수를 소모할 때, 현재 체력 비율이 가장 낮은 아군 1명에게 충전 역장 3 부여
   źródło: Passives.json :: dataList[id=1010601].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Charge], [ChargeForceField]
   znaczenie tagów: [Agility] = 신속 / Haste; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: - Turn End: Gain 1 [Agility] next turn for every 5 [Charge] Count on self (max 2)\n- If this unit's Skill consumed [Charge] Count, apply 3 [ChargeForceField] on 1 ally that has the lowest current HP percentage
   PL: - Na koniec tury zyskuje 1 Pośpiechu w następnej turze za każde 5 Licznika Ładowania na tej jednostce (maks. 2)\n- Gdy Umiejętność tej jednostki zużywa Licznik Ładowania, nakłada 3 Bariery Ładunku na 1 sojusznika o najniższym obecnym procentowym HP
170. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 비워낸 생각
   źródło: Passives.json :: dataList[id=1010611].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] - 턴 종료 시 자신의 충전 횟수 5 당 다음 턴에 신속 1을 얻음. (최대 3)\n- 자신이 스킬로 충전 횟수를 소모할 때, 현재 체력 비율이 가장 낮은 아군 1명에게 충전 역장 3 부여
   źródło: Passives.json :: dataList[id=1010611].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Charge], [ChargeForceField]
   znaczenie tagów: [Agility] = 신속 / Haste; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: - Turn End: Gain 1 [Agility] next turn for every 5 [Charge] Count on self (max 3)\n- If this unit's Skill consumed [Charge] Count, apply 3 [ChargeForceField] on 1 ally that has the lowest current HP percentage
   PL: - Na koniec tury zyskuje 1 Pośpiechu w następnej turze za każde 5 Licznika Ładowania na tej jednostce (maks. 3)\n- Gdy Umiejętność tej jednostki zużywa Licznik Ładowania, nakłada 3 Bariery Ładunku na 1 sojusznika o najniższym obecnym procentowym HP
172. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 정리 시범 교육
   źródło: Passives.json :: dataList[id=1010621].name
   limit: do 40 znaków
   EN: Cleanup Demonstration
   PL: Szkolenie z Oczyszczania
173. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 충전 횟수가 가장 높은 아군 1명이 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 있는 대상에게 가하는 피해량이 대상의 파열 에 비례하여 증가 (파열 1 당 1.5%. 최대 15%)
   źródło: Passives.json :: dataList[id=1010621].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the highest [Charge] Count deals more damage against targets that have <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> based on Rupture on target (+1.5% per Rupture, max +15% damage)
   PL: 1 sojusznik z najwyższym Licznikiem Ładowania zadaje więcej obrażeń celom z <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarciem</link></u></color>, proporcjonalnie do ich Rozdarcia (+1,5% za każde Rozdarcie, maks. +15% obrażeń)

## [00] The Pequod First Mate — Yi Sang — 피쿼드호 일등 항해사
- ID Tożsamości: `10107` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 69 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed, Poise

174. [Karta Tożsamości — tytuł] 피쿼드호\n일등 항해사
   źródło: Personalities.json :: dataList[id=10107].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pequod\nFirst Mate
   PL: Pequod\nPierwszy Oficer
175. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10107].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10107].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Karta Tożsamości — opis] 이상의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10107].desc
   limit: do 120 znaków
   EN: Yi Sang's 7th Identity
   PL: Siódma Tożsamość Yi Sanga
178. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 후벼파기
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=1].name ; dataList[id=1010701].levelList[level=2].name ; dataList[id=1010701].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Impale
   PL: Przebicie na Wylot
179. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=1].desc ; dataList[id=1010701].levelList[level=2].desc ; dataList[id=1010701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zyskuje +2 Licznika Oddechu
180. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
181. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1010701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
183. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 쑤시고 쑤시기
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].name ; dataList[id=1010702].levelList[level=2].name ; dataList[id=1010702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Relentless Stabbing
   PL: Niesłabnące Kłucie
185. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n자신의 호흡 이 5 이상이면, 합 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].desc ; dataList[id=1010702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count\nAt 5+ [Breath], Clash Power +2
   PL: [WhenUse] Zyskuje +2 Licznika Oddechu\nPrzy 5+ Oddechu Moc Starcia +2
186. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010702].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 2 Oddechu
187. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
188. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 이 코인 재사용 (최대 1회)
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin (1 time max)
   PL: [CriticalOnSucceedAttack] Używa tej monety ponownie (maks. 1 raz)
189. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n자신의 호흡 이 5 이상이면, 합 위력 +3
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count\nAt 5+ [Breath], Clash Power +3
   PL: [WhenUse] Zyskuje +2 Licznika Oddechu\nPrzy 5+ Oddechu Moc Starcia +3
190. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 Oddechu
191. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 이 코인 재사용 (최대 3회)
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin (3 times max)
   PL: [CriticalOnSucceedAttack] Używa tej monety ponownie (maks. 3 razy)
192. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 급습
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].name ; dataList[id=1010703].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Ambush
   PL: Zasadzka
193. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 호흡 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]
   PL: [WhenUse] Zyskuje 5 Oddechu
194. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +2 [Breath] Count
   PL: [OnSucceedAttackHead] Zyskuje +2 Licznika Oddechu
195. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1010703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] Nakłada 4 Krwawienia
196. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 횟수 4 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +4 [Laceration] Count
   PL: [CriticalOnSucceedAttack] Nakłada +4 Licznika Krwawienia
197. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 호흡 5 얻음\n자신의 호흡 이 7 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]\nAt 7+ [Breath], Coin Power +1
   PL: [WhenUse] Zyskuje 5 Oddechu\nPrzy 7+ Oddechu Moc Monet +1
198. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika Oddechu
199. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 횟수 6 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +6 [Laceration] Count
   PL: [CriticalOnSucceedAttack] Nakłada +6 Licznika Krwawienia
200. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-01.json :: dataList[id=1010704].levelList[level=1].name ; dataList[id=1010704].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
201. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 일등 항해사의 작살
   źródło: Passives.json :: dataList[id=1010701].name
   limit: do 40 znaków
   EN: The First Mate's Harpoon
   PL: Harpun Pierwszego Oficera
202. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 크리티컬 적중 시 스킬로 부여하는 출혈 위력 +2 (턴 당 최대 6회)
   źródło: Passives.json :: dataList[id=1010701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Crit, this unit inflicts +2 more [Laceration] Potency using its Skills (6 times per turn)
   PL: Przy trafieniu krytycznym Umiejętności nadają o 2 więcej Mocy Krwawienia (6 razy na turę)
203. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 일등 항해사의 노련함
   źródło: Passives.json :: dataList[id=1010721].name
   limit: do 40 znaków
   EN: The First Mate's Acumen
   PL: Sprawność Pierwszego Oficera
204. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] [Breath]을 가장 많이 보유한 아군 1명이 크리티컬 적중 시 스킬로 부여하는 출혈 위력 +2 (턴 당 최대 6회)
   źródło: Passives.json :: dataList[id=1010721].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Breath], [Laceration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: On Crit, 1 ally that has the highest [Breath] inflicts +2 more [Laceration] Potency using its Skills (6 times per turn)
   PL: Przy trafieniu krytycznym 1 sojusznik z najwyższym [Breath] nadaje o 2 więcej Mocy Krwawienia Umiejętnościami (6 razy na turę)

## [00] Dieci Assoc. South Section 4 — Yi Sang — 남부 디에치 협회 4과
- ID Tożsamości: `10108` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

205. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과
   źródło: Personalities.json :: dataList[id=10108].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Dieci\nSekcja 4
206. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10108].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10108].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Karta Tożsamości — opis] 이상의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10108].desc
   limit: do 120 znaków
   EN: Yi Sang's 8th Identity
   PL: Ósma Tożsamość Yi Sanga
209. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 지식 소모
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].name ; dataList[id=1010801].levelList[level=2].name ; dataList[id=1010801].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Expend Knowledge
   PL: Wydatkowanie Wiedzy
210. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 2%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]
   EN: Gain ([KnowledgeExplored] x 2% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 2% Maks. HP)\n[WhenUse] Odrzuca 1 Umiejętność najwyższej Rangi ze wszystkich swoich slotów
211. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttackHead] Lower user’s Stagger Threshold by [KnowledgeExplored]
   PL: [OnSucceedAttackHead] Odzyskuje [KnowledgeExplored] Ogłuszenia
212. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 3%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]
   EN: Gain ([KnowledgeExplored] x 3% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 3% Maks. HP)\n[WhenUse] Odrzuca 1 Umiejętność najwyższej Rangi ze wszystkich swoich slotów
214. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by [KnowledgeExplored]
   PL: [OnSucceedAttack] Odzyskuje [KnowledgeExplored] Ogłuszenia
215. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 3%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Sinking]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: Gain ([KnowledgeExplored] x 3% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] If target has 5+ [Sinking], Coin Power +1
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 3% Maks. HP)\n[WhenUse] Odrzuca 1 Umiejętność najwyższej Rangi ze wszystkich swoich slotów\n[WhenUse] Jeżeli cel ma 5+ [Sinking], Moc Monet +1
217. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 잠궈닫기
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].name ; dataList[id=1010802].levelList[level=2].name ; dataList[id=1010802].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Seal Shut
   PL: Zaryglowanie
218. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 4%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]
   EN: Gain ([KnowledgeExplored] x 4% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 4% Maks. HP)\n[WhenUse] Odrzuca 1 Umiejętność najwyższej Rangi ze wszystkich swoich slotów
219. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010802].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict [Sinking] equal to [KnowledgeExplored]
   PL: [OnSucceedAttackHead] Nakłada [Sinking] równe [KnowledgeExplored]
220. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1010802].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 5%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 5% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 5% Maks. HP)\n[WhenUse] Odrzuca 1 Umiejętność najwyższej Rangi ze wszystkich swoich slotów\n[WhenUse] W następnej turze ten slot zyskuje 3 Prowokacji
222. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 6%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Sinking], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 6% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] If target has 5+ [Sinking], Coin Power +1\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 6% Maks. HP)\n[WhenUse] Odrzuca 1 Umiejętność najwyższej Rangi ze wszystkich swoich slotów\n[WhenUse] Jeżeli cel ma 5+ [Sinking], Moc Monet +1\n[WhenUse] W następnej turze ten slot zyskuje 3 Prowokacji
223. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to [KnowledgeExplored]
   PL: [OnSucceedAttack] Nakłada [Sinking] równe [KnowledgeExplored]
224. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 지식의 가호
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=3].name ; dataList[id=1010803].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Grace of Knowledge
   PL: Łaska Wiedzy
226. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 9%)만큼 보호막을 얻음\n[WhenUse] 다음 턴에 이 슬롯이 도발치 8 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 9% of max HP) Shield if this Skill is Discarded\n[WhenUse] Gain +8 [Aggro] to this Skill Slot next turn
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 9% Maks. HP)\n[WhenUse] W następnej turze ten slot zyskuje 8 Prowokacji
227. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
228. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 12%)만큼 보호막을 얻음\n[WhenUse] 다음 턴에 이 슬롯이 도발치 10 얻음\n[WhenUse] 자신의 체력이 50% 미만이면 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 12% of max HP) Shield if this Skill is Discarded\n[WhenUse] Gain +10 [Aggro] to this Skill Slot next turn\n[WhenUse] At less than 50% HP, Coin Power +1
   PL: Jeżeli ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] × 12% Maks. HP)\n[WhenUse] W następnej turze ten slot zyskuje 10 Prowokacji\n[WhenUse] Przy HP poniżej 50% Moc Monet +1
229. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
230. [Obrona (ulepszenia 1,4) — nazwa] 탐구 몰입
   źródło: Skills_personality-01.json :: dataList[id=1010804].levelList[level=1].name ; dataList[id=1010804].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Fixated Study
   PL: Obsesyjne Badanie
231. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010804].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] Losowo odrzuca 2 swoje Umiejętności w kolejności od najniższej Rangi\n[WhenUse] W następnej turze ten slot zyskuje 3 Prowokacji
232. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010804].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] Gain +5 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] Losowo odrzuca 2 swoje Umiejętności w kolejności od najniższej Rangi\n[WhenUse] W następnej turze ten slot zyskuje 5 Prowokacji
233. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 가라앉는 지식
   źródło: Passives.json :: dataList[id=1010801].name
   limit: do 40 znaków
   EN: Sinking Knowledge
   PL: Grząska Wiedza
234. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] 피격 시 공격자에게 침잠 1 부여 (최대 4회)
   źródło: Passives.json :: dataList[id=1010801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When hit, inflict 1 [Sinking] on the attacker (max 4 times)
   PL: Przy otrzymaniu trafienia nakłada 1 Zatonięcia na atakującego (maks. 4 razy)
235. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — nazwa] 가라앉는 지식
   źródło: Passives.json :: dataList[id=1010811].name
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — opis] 피격 시 공격자에게 침잠 1 부여. 보호막이 있는 동안 피격 시 침잠 1 추가 부여 (최대 4회)
   źródło: Passives.json :: dataList[id=1010811].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When hit, inflict 1 [Sinking] on the attacker. When hit while Shielded, inflict 1 additional [Sinking] on the attacker (max 4 times)
   PL: Przy otrzymaniu trafienia nakłada 1 Zatonięcia na atakującego. Podczas posiadania Tarczy nakłada przy trafieniu dodatkowe 1 Zatonięcia (maks. 4 razy)
237. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — nazwa] 반복 지식
   źródło: Passives.json :: dataList[id=1010821].name
   limit: do 40 znaków
   EN: Reviewed Knowledge
   PL: Powtórzona Wiedza
238. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — opis] 속도가 가장 빠른 아군 1명이 스킬을 버릴 때, 해당 캐릭터 최대 체력의 (3 x 버린 스킬의 등급) % 만큼 보호막을 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1010821].desc
   limit: do 170 znaków
   EN: When 1 ally with the fastest Speed Discards a Skill, gain (3 x Discarded Skill rank)% of the max HP as Shield (once per turn)
   PL: Gdy 1 sojusznik z najwyższą Szybkością odrzuca Umiejętność, zyskuje Tarczę równą (3 × Ranga odrzuconej Umiejętności)% Maks. HP (raz na turę)
239. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Sloth) — nazwa] 반복 지식
   źródło: Passives.json :: dataList[id=1010831].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Sloth) — opis] 속도가 가장 빠른 아군 1명이 스킬을 버릴 때, 해당 캐릭터 최대 체력의 (5 x 버린 스킬의 등급) % 만큼 보호막을 얻음 (턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1010831].desc
   limit: do 170 znaków
   EN: When 1 ally with the fastest Speed Discards a Skill, gain (5 x Discarded Skill rank)% of the max HP as Shield (2 times per turn)
   PL: Gdy 1 sojusznik z najwyższą Szybkością odrzuca Umiejętność, zyskuje Tarczę równą (5 × Ranga odrzuconej Umiejętności)% Maks. HP (2 razy na turę)

## [000] The Ring Pointillist Student — Yi Sang — 약지 점묘파 스튜던트
- ID Tożsamości: `10109` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

241. [Karta Tożsamości — tytuł] 약지 점묘파\n스튜던트
   źródło: Personalities.json :: dataList[id=10109].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Ring Pointillist\nStudent
   PL: Pointilliści Serdecznego\nStudent
242. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10109].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10109].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Karta Tożsamości — opis] 이상의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10109].desc
   limit: do 120 znaków
   EN: Yi Sang's 9th Identity
   PL: Dziewiąta Tożsamość Yi Sanga
245. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 덧칠
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=1].name ; dataList[id=1010901].levelList[level=2].name ; dataList[id=1010901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 2 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Paint Over
   PL: Przemalowanie
246. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttackHead] Wybiera 1 losowy efekt spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] i nakłada +2 jego Licznika
247. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL: [OnSucceedAttackHead] Nakłada 2 [Laceration]
248. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1010901].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
249. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Clash Power +1
   PL: Jeżeli cel ma 6+ [Laceration], Moc Starcia +1
250. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 혈점묘화
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].name ; dataList[id=1010902].levelList[level=2].name ; dataList[id=1010902].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Sanguine Pointillism
   PL: Krwawy Pointillizm
251. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 20% 확률로 코인 1회 재사용. 대상이 보유한 부정적인 효과 1개당 재사용 확률 +20%
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010902].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] 20% chance to Reuse Coin once. +20% more chance to Reuse Coin for every type of negative effect on target
   PL: [OnSucceedAttack] 20% szans na 1 ponowne użycie monety. +20% szans za każdy 1 rodzaj negatywnego efektu na celu
252. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1010902].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1010902].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
253. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] Wybiera 1 losowy efekt spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] i nakłada +2 jego Licznika
254. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=2].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=1010902].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] Wybiera 1 losowy efekt spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] i nakłada +3 jego Licznika
256. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Laceration] 3 당 합 위력 +1 (최대 2)\n대상의 [Laceration] 횟수 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Clash Power +1 for every 3 [Laceration] on target (max 2)\nCoin Power +1 for every 3 [Laceration] Count on target (max 2)
   PL: Moc Starcia +1 za każde 3 [Laceration] na celu (maks. 2)\nMoc Monet +1 za każde 3 Licznika [Laceration] na celu (maks. 2)
257. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 40% 확률로 코인 재사용. 대상이 보유한 부정적인 효과 1개당 재사용 확률 +20%. (스킬당 최대 2회 재사용 가능)
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] 40% chance to Reuse Coin. +20% more chance to Reuse Coin for every type of negative effect on target (2 times max per Skill)
   PL: [OnSucceedAttack] 40% szans na ponowne użycie monety. +20% szans za każdy 1 rodzaj negatywnego efektu na celu (maks. 2 ponowne użycia na Umiejętność)
258. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 핏방울 채색
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].name ; dataList[id=1010903].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Hematic Coloring
   PL: Krwawe Barwienie
259. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가. 대상이 보유한 부정적인 효과가 4개 이상이면, 추가 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count. If target has 4+ types of negative effects, inflict +2 additional [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]. Jeżeli cel ma 4+ rodzaje negatywnych efektów, nakłada dodatkowe +2
261. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1010903].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여. 대상이 보유한 부정적인 효과가 4개 이상이면, 추가 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]. If target has 4+ types of negative effects, inflict 2 additional [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]. Jeżeli cel ma 4+ rodzaje negatywnych efektów, nakłada dodatkowe 2
263. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 위력 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1010903].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 Potency of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] Wybiera 1 losowy efekt spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] i nakłada 2 jego Mocy
264. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +15% (최대 75%)
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +15% damage for every type of negative effect on target (max 75%)
   PL: Zadaje +15% obrażeń za każdy rodzaj negatywnego efektu na celu (maks. 75%)
265. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [EndSkill] 대상이 흐트러졌거나 사망했으면, 부정적인 효과를 가장 적게 보유한 적 1명에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [EndSkill] If target is Staggered or Defeated, inflict 2 Potency of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking], on 1 enemy that has the fewest types of negative effects
   PL: [EndSkill] Jeżeli cel został Oszołomiony lub zginął, nakłada 2 Mocy losowego statusu spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] na 1 wroga z najmniejszą liczbą rodzajów negatywnych efektów
266. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Laceration] 3 당 합 위력 +1 (최대 2)\n대상의 [Laceration] 횟수 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가. 대상이 보유한 부정적인 효과가 3개 이상이면, 추가 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count. If target has 3+ types of negative effects, inflict +2 additional [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]. Jeżeli cel ma 3+ rodzaje negatywnych efektów, nakłada dodatkowe +2
268. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여. 대상이 보유한 부정적인 효과가 3개 이상이면, 추가 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]. If target has 3+ types of negative effects, inflict 2 additional [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]. Jeżeli cel ma 3+ rodzaje negatywnych efektów, nakłada dodatkowe 2
269. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +25% (최대 125%)
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +25% damage for every type of negative effect on target (max 125%)
   PL: Zadaje +25% obrażeń za każdy rodzaj negatywnego efektu na celu (maks. 125%)
270. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [EndSkill] 대상이 흐트러졌거나 사망했으면, 부정적인 효과를 가장 적게 보유한 적 2명에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [EndSkill] If target is Staggered or Defeated, inflict 2 Potency of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking], on 2 enemies that have the fewest types of negative effects
   PL: [EndSkill] Jeżeli cel został Oszołomiony lub zginął, wybiera 1 losowy efekt spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] i nakłada 2 jego Mocy na 2 wrogów z najmniejszą liczbą rodzajów negatywnych efektów
271. [Obrona (ulepszenia 1,4) — nazwa] 붓 털기
   źródło: Skills_personality-01.json :: dataList[id=1010904].levelList[level=1].name ; dataList[id=1010904].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Beat the Brush
   PL: Otrząsanie Pędzla
272. [Obrona (ulepszenie 1) — opis] 대상의 [Laceration]이 6 이상이면, 기본 위력 +5
   źródło: Skills_personality-01.json :: dataList[id=1010904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Base Power +5
   PL: Jeżeli cel ma 6+ [Laceration], Moc Bazowa +5
273. [Obrona (ulepszenie 4) — opis] 대상의 [Laceration] 1당 기본 위력 +1 (최대 10)
   źródło: Skills_personality-01.json :: dataList[id=1010904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Base Power +1 for every 1 [Laceration] on target (max 10)
   PL: Moc Bazowa +1 za każde 1 [Laceration] na celu (maks. 10)
274. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈점묘파
   źródło: Passives.json :: dataList[id=1010902].name
   limit: do 40 znaków
   EN: Sanguine Pointillist
   PL: Krwawy Pointillista
275. [Pasywka bojowa (od ulepszenia 1) — opis] 이 인격은 [Laceration]을 부여하는 인격으로만 취급됨. 랜덤으로 [Combustion], [Laceration], [Vibration], [Burst], [Sinking]을 부여하는 스킬이 이 효과로 인해서 해당 키워드를 부여하는 스킬로 취급되지 않음.
   źródło: Passives.json :: dataList[id=1010902].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Combustion], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: This Identity only counts as an "Identity that inflicts [Laceration]". This Identity's Skills that randomly inflict [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] do not count as Skills that inflict each respective Keyword
   PL: Ta Tożsamość liczy się wyłącznie jako „Tożsamość nakładająca [Laceration]”. Jej Umiejętności, które losowo nakładają [Combustion], [Laceration], [Vibration], [Burst] i [Sinking], nie są traktowane przez ten efekt jako Umiejętności nakładające poszczególne Keywords.
276. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 과제평가
   źródło: Passives.json :: dataList[id=1010901].name
   limit: do 40 znaków
   EN: Assignment Evaluation
   PL: Ocena Zadania
277. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 적중시 대상에게 [Laceration]이 6 이상 있으면 정신력 2 회복.\n대상이 보유한 부정적인 효과 1개당 정신력 1 추가 회복.(최대 3)\n이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [AttackUp] 1 얻음.\n(턴 당 패시브 최대 발동 횟수 : 4회)
   źródło: Passives.json :: dataList[id=1010901].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Hit, if the target has 6+ [Laceration], heal 2 SP\nHeal 1 additional SP for every type of negative effect on the target (max 3)\nIf this unit's SP is at max, gain 1 [AttackUp] next turn when this unit heals SP with this effect\n(This Passive activates 4 times max per turn)
   PL: Przy trafieniu jeżeli cel ma 6+ [Laceration], odzyskuje 2 Poczytalności\n+1 dodatkowej Poczytalności za każdy rodzaj negatywnego efektu na celu (maks. 3)\nJeżeli przy odzyskiwaniu Poczytalności tym efektem ma jej Maks., zyskuje w następnej turze 1 [AttackUp]\n(Ten pasyw aktywuje maks. 4 razy na turę)
278. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — podsumowanie] 적중시 조건에 따라 정신력 회복. 정신력이 최대면, 다음 턴에 [AttackUp] 1 얻음
   źródło: Passives.json :: dataList[id=1010901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Conditional SP Heal On Hit. At max SP, gain 1 [AttackUp] next turn
   PL: Przy trafieniu odzyskuje Poczytalność warunkowo. Przy Maks. Poczytalności zyskuje w następnej turze 1 [AttackUp]
279. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — nazwa] 과제평가
   źródło: Passives.json :: dataList[id=1010911].name
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — opis] 적중시 대상에게 [Laceration]이 <style="highlight">4</style> 이상 있으면 정신력 2 회복.\n대상이 보유한 부정적인 효과 1개당 정신력 1 추가 회복.(최대 3)\n이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [AttackUp] <style="highlight">2</style> 얻음.\n(턴 당 패시브 최대 발동 횟수 : 4회)
   źródło: Passives.json :: dataList[id=1010911].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Hit, if target has <style="highlight">4</style>+ [Laceration], heal 2 SP\nHeal 1 additional SP for every type of negative effect on the target (max 3)\nIf this unit's SP is at max, gain <style="highlight">2</style> [AttackUp] next turn when this unit heals SP with this effect\n(This Passive activates 4 times max per turn)
   PL: Przy trafieniu jeżeli cel ma <style="highlight">4</style>+ [Laceration], odzyskuje 2 Poczytalności\n+1 dodatkowej Poczytalności za każdy rodzaj negatywnego efektu na celu (maks. 3)\nJeżeli przy odzyskiwaniu Poczytalności tym efektem ma jej Maks., zyskuje w następnej turze <style="highlight">2</style> [AttackUp]\n(Ten pasyw aktywuje maks. 4 razy na turę)
281. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 적중시 조건에 따라 정신력 회복. 정신력이 최대면, 다음 턴에 [AttackUp] 2 얻음
   źródło: Passives.json :: dataList[id=1010911].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Conditional SP Heal On Hit. At max SP, gain 2 [AttackUp] next turn
   PL: Przy trafieniu odzyskuje Poczytalność warunkowo. Przy Maks. Poczytalności zyskuje w następnej turze 2 [AttackUp]
282. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 미학견습
   źródło: Passives.json :: dataList[id=1010921].name
   limit: do 40 znaków
   EN: Practices on Aesthetics
   PL: Praktyki Estetyczne
283. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 정신력이 가장 낮은 아군이 공격 적중 시 대상이 보유한 부정적인 효과 1개당 정신력 2 회복.(최대 6)\n(턴 당 패시브 최대 발동 횟수 : 2회)
   źródło: Passives.json :: dataList[id=1010921].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally that has the lowest SP heals 2 SP On Hit for every type of negative effect on the target (max 6)\n(This Passive activates 2 times max per turn)
   PL: Sojusznik z najniższą Poczytalnością odzyskuje przy trafieniu 2 Poczytalności za każdy rodzaj negatywnego efektu na celu (maks. 6)\n(Ten pasyw aktywuje maks. 2 razy na turę)
284. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — podsumowanie] 적중시 대상이 보유한 부정적인 효과 수에 비례하여 정신력 회복
   źródło: Passives.json :: dataList[id=1010921].summary
   limit: do 120 znaków
   EN: On Hit, heal SP based on the number of negative effect types on the target
   PL: Przy trafieniu odzyskuje Poczytalność proporcjonalnie do liczby rodzajów negatywnych efektów na celu
285. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — nazwa] 미학견습
   źródło: Passives.json :: dataList[id=1010931].name
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — opis] 정신력이 가장 낮은 아군이 공격 적중 시 대상이 보유한 부정적인 효과 1개당 정신력 2 회복.(최대 6)\n<style="highlight">대상에게 [Laceration]이 있으면 추가 3 회복.</style>\n(턴 당 패시브 최대 발동 횟수 : 2회)
   źródło: Passives.json :: dataList[id=1010931].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally that has the lowest SP heals 2 SP On Hit for every type of negative effect on the target (max 6)\n<style="highlight">If the target has [Laceration], heal 3 additional SP</style>\n(This Passive activates 2 times max per turn)
   PL: Sojusznik z najniższą Poczytalnością odzyskuje przy trafieniu 2 Poczytalności za każdy rodzaj negatywnego efektu na celu (maks. 6)\n<style="highlight">Jeżeli cel ma [Laceration], odzyskuje dodatkowe 3 Poczytalności.</style>\n(Ten pasyw aktywuje maks. 2 razy na turę)
287. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 적중시 대상이 보유한 부정적인 효과 수에 비례하여 정신력 회복
   źródło: Passives.json :: dataList[id=1010931].summary
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [000] Lobotomy E.G.O:: Solemn Lament — Yi Sang — 로보토미 E.G.O:: 엄숙한 애도
- ID Tożsamości: `10110` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9104 · HP bazowe: 66 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Sinking

288. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n엄숙한 애도
   źródło: Personalities.json :: dataList[id=10110].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nSolemn Lament
   PL: Lobotomy E.G.O::\nUroczysty Lament
289. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10110].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10110].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Karta Tożsamości — opis] 이상의 열번째 인격
   źródło: Personalities.json :: dataList[id=10110].desc
   limit: do 120 znaków
   EN: Yi Sang's 10th Identity
   PL: Dziesiąta Tożsamość Yi Sanga
292. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 떠난이에게 축하를
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].name ; dataList[id=1011001].levelList[level=2].name ; dataList[id=1011001].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Celebration for the Departed
   PL: Uczta dla Odchodzących
293. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend 1 [BulletLament]
   PL: Zużywa 1 [BulletLament]
294. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011001].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011001].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletLament], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict [SinkingWhite] equal to [BulletLament] spent
   PL: [OnSucceedAttack] Nakłada [SinkingWhite] równe zużytym [BulletLament]
295. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011001].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Sinking]과 모든 [SinkingWhite]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [SinkingWhite], [WinDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If the sum of the target's [Sinking] and both [SinkingWhite] is 6 or higher, Coin Power +1\n[WinDuel] Inflict +2 [Sinking] Count
   PL: Jeżeli suma [Sinking] celu i wszystkich [SinkingWhite] wynosi 6 lub więcej, Moc Monet +1\n[WinDuel] Nakłada +2 Licznika [Sinking]
298. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">보유한 [BulletLament]가 10 이상이면, 합 위력 +1</style>\n대상의 [Sinking]과 모든 [SinkingWhite]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletLament], [Sinking], [SinkingWhite], [WinDuel]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">At 10+ [BulletLament], Clash Power +1</style>\nIf the sum of the target's [Sinking] and both [SinkingWhite] is 6 or higher, Coin Power +1\n[WinDuel] Inflict +2 [Sinking] Count
   PL: <style="highlight">Przy 10+ [BulletLament] Moc Starcia +1</style>\nJeżeli suma [Sinking] celu i wszystkich [SinkingWhite] wynosi 6 lub więcej, Moc Monet +1\n[WinDuel] Nakłada +2 Licznika [Sinking]
299. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 남은자에게 엄숙한 애도를
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].name ; dataList[id=1011002].levelList[level=2].name ; dataList[id=1011002].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Solemn Lament for the Living
   PL: Uroczysty Lament dla Żywych
300. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [BulletLament] 5 소모
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend 5 [BulletLament]
   PL: Zużywa 5 [BulletLament]
301. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011002].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011002].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011002].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Sinking]과 모든 [SinkingWhite]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [Sinking] 횟수 1 증가\n[EndSkill] 최대 공명 수만큼 [BulletLament]를 얻음 (최대 6)\n- 해당 공명이 완전 공명이면, (최대 공명 수 x 2)만큼 얻음 (최대 12)
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [SinkingWhite], [WinDuel], [EndSkill], [BulletLament]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: If the sum of the target's [Sinking] and both [SinkingWhite] is 6 or higher, Coin Power +1\n[WinDuel] Inflict +1 [Sinking] Count\n[EndSkill] Gain (highest Reson.) of [BulletLament] (max 6)\n- If the said Reson. was an A-Reson., gain (highest Reson. x 2) of [BulletLament] (max 12)
   PL: Jeżeli suma [Sinking] celu i wszystkich [SinkingWhite] wynosi 6 lub więcej, Moc Monet +1\n[WinDuel] Nakłada +1 Licznika [Sinking]\n[EndSkill] Zyskuje [BulletLament] równe najwyższemu Rezonansowi (maks. 6)\n- Jeżeli był to Pełny Rezonans, zyskuje (najwyższy Rezonans × 2) [BulletLament] (maks. 12)
305. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 보유한 [BulletLament]가 10 이상이면, 합 위력 +1\n대상의 [Sinking]과 모든 [SinkingWhite]의 <style="highlight">합 6 당, 코인 위력 +1(최대 2)</style>\n[WinDuel] [Sinking] 횟수 1 증가\n[EndSkill] 최대 공명 수만큼 [BulletLament]를 얻음 (최대 6)\n- 해당 공명이 완전 공명이면, (최대 공명 수 x 2)만큼 얻음 (최대 12)\n<style="highlight"> - 해당 공명이 완전 공명 4 이상이면, 대신 [ReloadLament]</style>
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletLament], [Sinking], [SinkingWhite], [WinDuel], [EndSkill], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [ReloadLament] = 재장전 / Reload
   EN: At 10+ [BulletLament], Clash Power +1\n<style="highlight">Coin Power +1 for every 6 value</style> of the sum of the target's [Sinking] and both [SinkingWhite] <style="highlight">(max 2)</style>\n[WinDuel] Inflict +1 [Sinking] Count\n[EndSkill] Gain (highest Reson.) of [BulletLament] (max 6)\n- If the said Reson. was an A-Reson., gain (highest Reson. x 2) of [BulletLament] (max 12)\n<style="highlight"> - If the said Reson. was at 4+ A-Reson., [ReloadLament] instead</style>
   PL: Przy 10+ [BulletLament] Moc Starcia +1\nMoc Monet +1 za każdą 6 wartości<style="highlight"> sumy [Sinking] celu i wszystkich [SinkingWhite] (maks. 2)</style>\n[WinDuel] Nakłada +1 Licznika [Sinking]\n[EndSkill] Zyskuje [BulletLament] równe najwyższemu Rezonansowi (maks. 6)\n- Jeżeli był to Pełny Rezonans, zyskuje (najwyższy Rezonans × 2) [BulletLament] (maks. 12)\n<style="highlight"> - Jeżeli był to Pełny Rezonans 4 lub większy, zamiast tego [ReloadLament]</style>
306. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 이상으로 장례는 이상이오
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].name ; dataList[id=1011003].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Goodbye Now, a Sorrow in You
   PL: Żegnaj więc — w Tobie zostaje smutek
307. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 보유한 [BulletLament] 10마다, 기본 위력 +1 (최대 2)\n[WinDuel] [Sinking] 횟수 3 증가\n[EndSkill] [ReloadLament]
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [BulletLament], [WinDuel], [Sinking], [EndSkill], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [ReloadLament] = 재장전 / Reload
   EN: Base Power +1 for every 10 value of [BulletLament] (max 2)\n[WinDuel] Inflict +3 [Sinking] Count\n[EndSkill] [ReloadLament]
   PL: Moc Bazowa +1 za każde 10 wartości [BulletLament] (maks. 2)\n[WinDuel] Nakłada +3 Licznika [Sinking]\n[EndSkill] [ReloadLament]
308. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011003].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [BulletLament] 6 소모
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend 6 [BulletLament]
   PL: Zużywa 6 [BulletLament]
311. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1011003].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 보유한 [BulletLament] 전부 소모
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend all of [BulletLament] on self
   PL: Zużywa wszystkie posiadane [BulletLament]
313. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1011003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 스킬에서 소모한 [BulletLament] 1당 피해량 +2%
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletLament]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: [OnSucceedAttack] Deal +2% damage for every value of [BulletLament] spent by this Skill
   PL: [OnSucceedAttack] Zadaje +2% obrażeń za każde 1 zużyte przez tę Umiejętność [BulletLament]
315. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 모든 [SinkingWhite]만큼 우울 피해\n- 산나비와 죽은나비의 합으로 계산
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict Gloom damage equal to "All" [SinkingWhite] on target\n- "All" = the sum of both The Living and The Departed on target
   PL: [OnSucceedAttack] Zadaje obrażenia Posępnością równe "wszystkim" [SinkingWhite] na celu\n- "Wszystkie" = suma Żywych i Zmarłych Motyli na celu
316. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 보유한 [BulletLament] <style="highlight">5</style> 마다 기본 위력 +1 <style="highlight">(최대 4)</style>\n대상의 [Sinking]과 모든 [SinkingWhite]의 합 6당, 코인 위력 +1 (최대 2)\n[WinDuel] [Sinking] 횟수 3 증가\n[EndSkill] [ReloadLament]
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletLament], [Sinking], [SinkingWhite], [WinDuel], [EndSkill], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [ReloadLament] = 재장전 / Reload
   EN: Base Power +1 for every <style="highlight">5</style> value of [BulletLament] <style="highlight">(max 4)</style>\nCoin Power +1 for every 6 value of the sum of the target's [Sinking] and both [SinkingWhite] (max 2)\n[WinDuel] Inflict +3 [Sinking] Count\n[EndSkill] [ReloadLament]
   PL: Moc Bazowa +1 za każdą wartość <style="highlight">5</style> [BulletLament] <style="highlight">(maks. 4)</style>\nMoc Monet +1 za każdą 6 wartości sumy [Sinking] celu i wszystkich [SinkingWhite] (maks. 2)\n[WinDuel] Nakłada +3 Licznika [Sinking]\n[EndSkill] [ReloadLament]
317. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 스킬에서 소모한 [BulletLament] 1당 피해량 +4%
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletLament]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: [OnSucceedAttack] Deal +4% damage for every value of [BulletLament] spent by this Skill
   PL: [OnSucceedAttack] Zadaje +4% obrażeń za każde 1 zużyte przez tę Umiejętność [BulletLament]
318. [Obrona (ulepszenia 1,4) — nazwa] 관에서나비가날아오리라
   źródło: Skills_personality-01.json :: dataList[id=1011004].levelList[level=1].name ; dataList[id=1011004].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 50 znaków
   EN: FromTheCoffinAButterflyTakesFlight
   PL: ZTrumnyWzleciMotyl
319. [Obrona (ulepszenie 1) — opis] [StartBattle] [ReloadLament] (턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [ReloadLament]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ReloadLament] = 재장전 / Reload
   EN: [StartBattle] [ReloadLament] (once per turn)
   PL: [StartBattle] [ReloadLament] (raz na turę)
320. [Obrona (ulepszenie 4) — opis] [StartBattle] [ReloadLament] (턴 당 1회)\n[StartBattle] 최대 체력의 (지정한 대상의 모든 [SinkingWhite])% 만큼 보호막을 얻음. (턴 당 최대 20%)
   źródło: Skills_personality-01.json :: dataList[id=1011004].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ReloadLament], [SinkingWhite]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ReloadLament] = 재장전 / Reload; [SinkingWhite] = 나비 / Butterfly
   EN: [StartBattle] [ReloadLament] (once per turn)\n[StartBattle] Gain Shield equal to (the sum of both [SinkingWhite] on the selected target)% HP (max 20% per turn)
   PL: [StartBattle] [ReloadLament] (raz na turę)\n[StartBattle] Zyskuje Tarczę równą (suma wszystkich [SinkingWhite] wybranego celu)% HP (maks. 20% na turę)
321. [Pasywka bojowa (od ulepszenia 1) — nazwa] 죽어가는나비를본다.
   źródło: Passives.json :: dataList[id=1011002].name
   limit: do 40 znaków
   EN: ISeeTheDyingButterfly.
   PL: WidzęUmarającegoMotyla.
322. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 시작 시 [BulletLament]를 각각 10씩 보유함.\n\n [BulletLament]를 소모할 때, 해당 효과의 산나비(위력)와 죽은나비(횟수)를 무작위로 소모.\n\n[SinkingWhite]를 부여할 때, 해당 코인에서 소모한 [BulletLament]에 따라 부여.\n- 산나비를 소모했으면, 소모한 값만큼 산나비를 부여.\n- 죽은나비를 소모했으면, 소모한 값만큼 죽은나비를 부여.\n\n스킬 사용 중 [BulletLament]가 부족하면, 다음 코인을 모두 취소하고 [ReloadLament]\n\n[ReloadLament]을 하거나 [BulletLament]를 얻을 때, 현재 정신력에 따라 얻는 나비가 정해짐.\n- 정신력이 0 이상이면, 30% 확률로 산나비를, 70% 확률로 죽은나비를 얻음.\n- 정신력이 0 미만이면, 70% 확률로 산나비를, 30% 확률로 죽은나비를 얻음.\n- 확률은 각 탄환마다 개별적으로 적용됨.
   źródło: Passives.json :: dataList[id=1011002].desc
   limit: do 1110 znaków
   tokeny: zachowaj dokładnie: \n, [BulletLament], [SinkingWhite], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [SinkingWhite] = 나비 / Butterfly; [ReloadLament] = 재장전 / Reload
   EN: Begin encounters with 10 of each of [BulletLament]\n\nWhen spending [BulletLament], select randomly between The Living(Potency) and The Departed(Count) for each [BulletLament] value\n\nWhen inflicting [SinkingWhite], inflict the same amount of The Living and The Departed as they were consumed. Example below:\n- If this unit spent X Living, inflict X Living\n- If this unit spent Y Departed, inflict Y Departed\n\nIf this unit runs out of [BulletLament] midway through Skill use, cancel all subsequent Coins and [ReloadLament]\n\nWhen [ReloadLament]ing, or when gaining [BulletLament], gain either The Living or The Departed based on this unit's current SP\n- At 0 or higher SP: 30% chance to gain The Living; 70% chance to gain The Departed\n- At less than 0 SP: 70% chance to gain The Living; 30% chance to gain The Departed\n- The probabilities are calculated separately for each ammo spent
   PL: Rozpoczyna spotkania z 10 każdego z [BulletLament]\n\nZużywając [BulletLament], losowo wybiera między Żywymi Motylami (Moc) a Zmarłymi Motylami (Licznik) dla każdej wartości [BulletLament]\n\nNakładając [SinkingWhite], nakłada tyle Żywych i Zmarłych Motyli, ile zużyto. Przykład:\n- Jeżeli ta jednostka zużyła X Żywych, nakłada X Żywych\n- Jeżeli zużyła Y Zmarłych, nakłada Y Zmarłych\n\nJeżeli tej jednostce skończą się [BulletLament] w trakcie użycia Umiejętności, anuluje wszystkie następne monety i wykonuje [ReloadLament]\n\nWykonując [ReloadLament] lub zyskując [BulletLament], otrzymuje Żywe albo Zmarłe Motyle w zależności od obecnej Poczytalności\n- Przy 0 lub wyższej Poczytalności: 30% szans na Żywe Motyle; 70% szans na Zmarłe Motyle\n- Przy Poczytalności poniżej 0: 70% szans na Żywe Motyle; 30% szans na Zmarłe Motyle\n- Prawdopodobieństwa liczone są osobno dla każdej zużytej amunicji
323. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 스킬 사용 중 탄환이 부족하면 재장전
   źródło: Passives.json :: dataList[id=1011002].summary
   limit: do 120 znaków
   EN: Reloads if this unit runs out of Ammo midway through Skill use
   PL: Przeładowuje, jeżeli skończy się amunicja w trakcie użycia Umiejętności
324. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 쏘아라.쏘으리로다.
   źródło: Passives.json :: dataList[id=1011001].name
   limit: do 40 znaków
   EN: Fire.IShallFire.
   PL: Strzelaj.StrzelaćBędę.
325. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] [BulletLament]를 얻으면, 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1011001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament], [Agility]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Agility] = 신속 / Haste
   EN: When this unit gains [BulletLament], gain 2 [Agility] next turn (once per turn)
   PL: Gdy ta jednostka zyska [BulletLament], zyskuje 2 [Agility] w następnej turze (raz na turę)
326. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — podsumowanie] 탄환을 얻으면, 다음 턴에 신속을 얻음
   źródło: Passives.json :: dataList[id=1011001].summary
   limit: do 120 znaków
   EN: When this unit gains Ammo, gain Agility next turn
   PL: Gdy ta jednostka zdobędzie amunicję, zyskuje Pośpiech w następnej turze
327. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — nazwa] 쏘아라.쏘으리로다.
   źródło: Passives.json :: dataList[id=1011011].name
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — opis] 공격 종료시 자신의 스킬에 의해 대상이 사망했으면, [ReloadLament]\n[BulletLament]를 얻으면, 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1011011].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [ReloadLament], [BulletLament], [Agility]
   znaczenie tagów: [ReloadLament] = 재장전 / Reload; [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Agility] = 신속 / Haste
   EN: Attack End: If this unit killed the target with its Skill, [ReloadLament]\nWhen this unit gains [BulletLament], gain 2 [Agility] next turn (once per turn)
   PL: Na koniec ataku, jeżeli Umiejętność tej jednostki zabiła cel, wykonuje [ReloadLament]\nGdy ta jednostka zyska [BulletLament], zyskuje 2 [Agility] w następnej turze (raz na turę)
329. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — podsumowanie] 탄환을 얻으면, 다음 턴에 신속을 얻음. 대상 처치시, 재장전
   źródło: Passives.json :: dataList[id=1011011].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: When this unit gains Ammo, gain [Agility] next turn. On Kill, Reload
   PL: Gdy ta jednostka zdobędzie amunicję, zyskuje Pośpiech w następnej turze. Przy zabiciu celu przeładowuje
330. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Gloom) — nazwa] 구원의 손
   źródło: Passives.json :: dataList[id=1011021].name
   limit: do 40 znaków
   EN: Hand of Salvation
   PL: Ręka Zbawienia
331. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Gloom) — opis] 아군의 스킬 적중 시 대상의 [Sinking]을 2 소모하여 [SinkingWhite] 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1011021].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking], [SinkingWhite]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly
   EN: When an ally hits with a Skill, consume 2 [Sinking] on the target to inflict them with 1 [SinkingWhite] (3 times per turn)
   PL: Gdy sojusznik trafi Umiejętnością, zużywa 2 [Sinking] celu, by nałożyć na niego 1 [SinkingWhite] (3 razy na turę)
332. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Gloom) — podsumowanie] 대상의 침잠을 나비로 전환
   źródło: Passives.json :: dataList[id=1011021].summary
   limit: do 120 znaków
   EN: Convert target's Sinking into Butterfly
   PL: Zamienia Zatonięcie celu na Motyla

## [00] LCE E.G.O:: Lantern — Yi Sang — LCE E.G.O:: 초롱
- ID Tożsamości: `10111` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 5 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Rupture

333. [Karta Tożsamości — tytuł] LCE E.G.O::\n초롱
   źródło: Personalities.json :: dataList[id=10111].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCE E.G.O::\nLantern
   PL: LCE E.G.O::\nLatarnia
334. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10111].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10111].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Karta Tożsamości — opis] 이상의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10111].desc
   limit: do 120 znaków
   EN: Yi Sang's 11th Identity
   PL: Jedenasta Tożsamość Yi Sanga
337. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] E.G.O는 제식 장비라 할지라도,
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].name ; dataList[id=1011101].levelList[level=2].name ; dataList[id=1011101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 100 znaków
   EN: Though it must be prefaced that E.G.O gears are standardized equipment,
   PL: Choć trzeba zaznaczyć, że ekwipunek E.G.O jest standaryzowany,
338. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Aggro] 2 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst]을 부여하지 않음.
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +2 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] with its effects
   PL: [WhenUse] Zyskuje +2 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada [Burst] swoimi efektami
339. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
340. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011101].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
341. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [StartBattle] 자신을 타겟팅 한 스킬의 수만큼 합 패배 시 최종 위력이 증가 (최대 2)\n[WhenUse] 다음 턴에 [Aggro] 3 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst]을 부여하지 않음.\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=2].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] On Clash Lose, gain Final Power equal to the number of Skills targeting this unit (max 2)\n[WhenUse] Gain +3 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] with its effects\n[DefeatDuel] [Burst] Potency inflicted by this Skill +1
   PL: [StartBattle] Przy przegranej Starciu zyskuje Moc Końcową równą liczbie Umiejętności celujących w tę jednostkę (maks. 2)\n[WhenUse] Zyskuje +3 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada [Burst] swoimi efektami\n[DefeatDuel] [Burst] nadawany przez tę Umiejętność +1
344. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [StartBattle] 자신을 타겟팅 한 스킬의 수만큼 합 패배 시 최종 위력이 증가 (최대 3)\n[WhenUse] 다음 턴에 [Aggro] 3 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst]을 부여하지 않음.\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] On Clash Lose, gain Final Power equal to the number of Skills targeting this unit (max 3)\n[WhenUse] Gain +3 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] with its effects\n[DefeatDuel] [Burst] Potency inflicted by this Skill +2
   PL: [StartBattle] Przy przegranej Starciu zyskuje Moc Końcową równą liczbie Umiejętności celujących w tę jednostkę (maks. 3)\n[WhenUse] Zyskuje +3 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada [Burst] swoimi efektami\n[DefeatDuel] [Burst] nadawany przez tę Umiejętność +2
345. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 로보토미때의 E.G.O보다 환상체와의 감응 정도에 따라
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].name ; dataList[id=1011102].levelList[level=2].name ; dataList[id=1011102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 8 · monety: 1 (+6)
   limit: do 140 znaków
   EN: when juxtaposed with E.G.O gear from L Corp., depending on the degree of attunement to the Abnormality,
   PL: w porównaniu z ekwipunkiem E.G.O z czasów L Corp., zależnie od stopnia dostrojenia do Abnormalności,
346. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Aggro] 2 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않음.
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +2 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects
   PL: [WhenUse] Zyskuje +2 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Licznika [Burst] swoimi efektami
347. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
349. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [StartBattle] 자신을 타겟팅 한 스킬의 수 만큼 합 패배 시 최종 위력이 증가 (최대 3)\n[WhenUse] 다음 턴에 [Aggro] 3 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않음.\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 횟수 +1
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=2].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] On Clash Lose, gain Final Power equal to the number of Skills targeting this unit (max 3)\n[WhenUse] Gain +3 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects\n[DefeatDuel] [Burst] Count inflicted by this Skill +1
   PL: [StartBattle] Przy przegranej Starciu zyskuje Moc Końcową równą liczbie Umiejętności celujących w tę jednostkę (maks. 3)\n[WhenUse] Zyskuje +3 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Licznika [Burst] swoimi efektami\n[DefeatDuel] Licznik [Burst] nadawany przez tę Umiejętność +1
350. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Burst]
351. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] <style="highlight">(자신을 타겟팅 한 스킬의 수 X 2) 만큼 합 패배 시 최종 위력이 증가 (최대 6)</style>\n[WhenUse] 다음 턴에 [Aggro] 4 얻음\n[WhenUse] 대상의 [Burst] 위력이 15, 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않음\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 횟수 +2
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] <style="highlight">On Clash Lose, gain (# of Skills targeting this unit x 2) Final Power (max 6)</style>\n[WhenUse] Gain +4 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects\n[DefeatDuel] [Burst] Count inflicted by this Skill +2
   PL: [StartBattle] <style="highlight">Przy przegranej Starciu zyskuje (# Umiejętności celujących w tę jednostkę × 2) Moc Końcowej (maks. 6)</style>\n[WhenUse] Zyskuje +4 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Licznika [Burst] swoimi efektami\n[DefeatDuel] Licznik [Burst] nadawany przez tę Umiejętność +2
352. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 본체의 특징을 더 유연하게 활용 가능하오
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].name ; dataList[id=1011103].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 16 · monety: 3 (−5)
   limit: do 100 znaków
   EN: the idiosyncrasies of the source may be utilized with greater flexibility
   PL: cechy źródła można wykorzystać z większą swobodą
353. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 잃은 체력 1%당 피해량 0.5% 증가\n[StartBattle] 자신을 타겟팅 한 스킬의 수 만큼 기본 위력 +1 (최대 2)\n[WhenUse] [GlowingLantern] 2 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 6 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력과 횟수를 부여하지 않고, 기본 위력 +1\n[EndSkill] 정신력 30 회복
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [GlowingLantern], [Aggro], [Burst], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +0.5% damage for every 1% missing HP on self\n[StartBattle] Base Power +1 for every Skill that targets this unit (max 2)\n[WhenUse] Gain 2 [GlowingLantern] (once per turn)\n[WhenUse] Gain +6 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency or Count with its effects; instead, gain Base Power +1\n[EndSkill] Heal 30 SP
   PL: Zadaje +0,5% obrażeń za każde 1% brakującego HP tej jednostki\n[StartBattle] Moc Bazowa +1 za każdą Umiejętność celującą w tę jednostkę (maks. 2)\n[WhenUse] Zyskuje 2 [GlowingLantern] (raz na turę)\n[WhenUse] Zyskuje +6 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Mocy ani Licznika [Burst] swoimi efektami; zamiast tego zyskuje Moc Bazową +1\n[EndSkill] Odzyskuje 30 Poczytalności
354. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]
356. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 잃은 체력 1%당 피해량 0.8% 증가\n[StartBattle] 자신을 타겟팅 한 스킬의 수 만큼 기본 위력 +1 (최대 3)\n[WhenUse] [GlowingLantern] 3 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 8 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력과 횟수를 부여하지 않고, 기본 위력 +1\n[EndSkill] 정신력 30 회복
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [GlowingLantern], [Aggro], [Burst], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +0.8% damage for every 1% missing HP on self\n[StartBattle] Base Power +1 for every Skill that targets this unit (max 3)\n[WhenUse] Gain 3 [GlowingLantern] (once per turn)\n[WhenUse] Gain +8 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency or Count with its effects; instead, gain Base Power +1\n[EndSkill] Heal 30 SP
   PL: Zadaje +0,8% obrażeń za każde 1% brakującego HP tej jednostki\n[StartBattle] Moc Bazowa +1 za każdą Umiejętność celującą w tę jednostkę (maks. 3)\n[WhenUse] Zyskuje 3 [GlowingLantern] (raz na turę)\n[WhenUse] Zyskuje +8 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Mocy ani Licznika [Burst] swoimi efektami; zamiast tego zyskuje Moc Bazową +1\n[EndSkill] Odzyskuje 30 Poczytalności
359. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Burst]
360. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [Binding]
361. [Obrona (ulepszenia 1,4) — nazwa] 다만 그 감응과 동기화 정도에 따라 잡아먹힐 수 있소
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=1].name ; dataList[id=1011104].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 10 · monety: 1 (+5)
   limit: do 160 znaków
   EN: Yet, the degree to which that attunement and synchronization are achieved may resultantly allow the user to be devoured
   PL: Jednakże stopień osiągniętego dostrojenia i synchronizacji może sprawić, że użytkownik zostanie pożarty
362. [Obrona (ulepszenie 1) — opis] [StartBattle] [GlowingLantern] 2 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 6 얻음\n[WhenUse] 대상의 [Burst] 위력이 15, 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않고, 기본 위력 +3
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [GlowingLantern], [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [StartBattle] Gain 2 [GlowingLantern] (once per turn)\n[WhenUse] Gain +6 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects; instead, gain Base Power +3
   PL: [StartBattle] Zyskuje 2 [GlowingLantern] (raz na turę)\n[WhenUse] Zyskuje +6 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ Mocy [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Licznika [Burst] swoimi efektami; zamiast tego zyskuje Moc Bazową +3
363. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Obrona (ulepszenie 4) — opis] [StartBattle] [GlowingLantern] 3 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 8 얻음\n[WhenUse] 대상의 [Burst] 위력이 15, 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않고, 기본 위력 +3
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [GlowingLantern], [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [StartBattle] Gain 3 [GlowingLantern] (once per turn)\n[WhenUse] Gain +8 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects; instead, gain Base Power +3
   PL: [StartBattle] Zyskuje 3 [GlowingLantern] (raz na turę)\n[WhenUse] Zyskuje +8 [Aggro] w następnej turze\n[WhenUse] Jeżeli cel ma 15+ Mocy [Burst] i 3+ Licznika [Burst], ta Umiejętność nie nakłada Licznika [Burst] swoimi efektami; zamiast tego zyskuje Moc Bazową +3
365. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 외형 또한 이전 L사의 E.G.O에 비해, 환상체와 가깝게 추출할 수 있소
   źródło: Passives.json :: dataList[id=1011101].name
   limit: do 160 znaków
   EN: This is reflected in their appearance, more closely resembling the source Abnormality than E.G.O of the former L Corp. do
   PL: Zewnętrzna postać również może być wyekstrahowana bliżej Abnormalności niż w przypadku dawnego E.G.O L Corp.
366. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 사망 시 자신을 가장 마지막으로 공격한 대상에게 [Burst] 4, [Burst] 횟수 2를 부여하고, 가장 부족한 속성의 E.G.O 자원 4종을 2개씩 얻음.\n- 공격자가 없거나 아군에게 사망한 경우, 현재 [Burst] 횟수가 가장 적은 적에게 [Burst] 4, [Burst] 횟수 2 부여
   źródło: Passives.json :: dataList[id=1011101].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: On death, inflict 4 [Burst] and +2 [Burst] Count against the target that attacked this unit last; then, gain 2 E.G.O resources for 4 least-owned Affinities\n- If no one attacked this unit, or if an ally killed this unit, inflict 4 [Burst] and +2 [Burst] Count against the enemy that has the least [Burst] Count
   PL: Po śmierci nakłada 4 [Burst] i +2 Licznika [Burst] na cel, który zaatakował tę jednostkę ostatni; następnie zyskuje po 2 zasobów E.G.O dla 4 Afinności o najmniejszym posiadaniu\n- Jeżeli nikt nie zaatakował tej jednostki lub zabił ją sojusznik, nakłada 4 [Burst] i +2 Licznika [Burst] na wroga z najmniejszym Licznikiem [Burst]
367. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — nazwa] 외형 또한 이전 L사의 E.G.O에 비해, 환상체와 가깝게 추출할 수 있소
   źródło: Passives.json :: dataList[id=1011111].name
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — opis] 사망 시 자신을 가장 마지막으로 공격한 대상에게 [Burst] <style="highlight">5</style>, [Burst] 횟수 <style="highlight">3</style>을 부여하고, 가장 부족한 속성의 E.G.O 자원 4종을 2개씩 얻음.\n- 공격자가 없거나 아군에게 사망한 경우, 현재 [Burst] 횟수가 가장 적은 적에게 [Burst] 5, [Burst] 횟수 3 부여\n- 자신이 [GlowingLantern] 상태인 경우, 이 효과로 부여하는 [Burst] 위력이 2배로 적용됨.
   źródło: Passives.json :: dataList[id=1011111].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [GlowingLantern]
   znaczenie tagów: [Burst] = 파열 / Rupture; [GlowingLantern] = 미끼 요정 / Fairy Lure
   EN: On death, inflict <style="highlight">5</style> [Burst] and +<style="highlight">3</style> [Burst] Count against the target that attacked this unit last; then, gain 2 E.G.O resources for 4 least-owned Affinities\n- If no one attacked this unit, or if an ally killed this unit, inflict 5 [Burst] and +3 [Burst] Count against the enemy that has the least [Burst] Count\n- If this unit is in a [GlowingLantern] state, inflict double the [Burst] Potency with this effect
   PL: Po śmierci nakłada <style="highlight">5</style> [Burst] i +<style="highlight">3</style> Licznika [Burst] na cel, który zaatakował tę jednostkę ostatni; następnie zyskuje po 2 zasobów E.G.O dla 4 Afinności o najmniejszym posiadaniu\n- Jeżeli nikt nie zaatakował tej jednostki lub zabił ją sojusznik, nakłada 5 [Burst] i +3 Licznika [Burst] na wroga z najmniejszym Licznikiem [Burst]\n- Jeżeli ta jednostka jest w stanie [GlowingLantern], ten efekt nakłada podwójną Moc [Burst]
369. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] E.G.O가 붕괴될 때 거름과 같이 분해되오
   źródło: Passives.json :: dataList[id=1011121].name
   limit: do 80 znaków
   EN: E.G.O disintegration is not unlike decomposition of compost
   PL: Rozpad E.G.O nie różni się od rozkładu kompostu
370. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 현재 체력이 가장 낮은 아군 1명이 사망 시 가장 부족한 속성의 E.G.O 자원 2종을 2개씩 얻음.
   źródło: Passives.json :: dataList[id=1011121].desc
   limit: do 140 znaków
   EN: When 1 ally that has the lowest current HP is killed, gain 2 E.G.O resources for 2 least-owned Affinities
   PL: Po śmierci 1 sojusznika z najniższym obecnym HP zyskuje po 2 zasobów E.G.O dla 2 Afinności o najmniejszym posiadaniu

## [000] Liu Assoc. South Section 3 — Yi Sang — 남부 리우 협회 3과
- ID Tożsamości: `10112` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Burn

371. [Karta Tożsamości — tytuł] 남부 리우 협회\n3과
   źródło: Personalities.json :: dataList[id=10112].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 3
   PL: Południowe Stowarzyszenie Liu\nSekcja 3
372. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10112].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10112].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Karta Tożsamości — opis] 이상의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10112].desc
   limit: do 120 znaków
   EN: Yi Sang's 12th Identity
   PL: Dwunasta Tożsamość Yi Sanga
375. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 염참
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].name ; dataList[id=1011201].levelList[level=2].name ; dataList[id=1011201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flame Hew
   PL: Cios Płomienia
376. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 대상의 [Combustion] 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL: Jeżeli cel ma 6+ [Combustion], Moc Monet +1
377. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]
   PL: [OnSucceedAttackHead] Nakłada 1 [Combustion]
378. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion] <style="highlight">3</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has <style="highlight">3</style>+ [Combustion], Coin Power +1
   PL: Jeżeli cel ma <style="highlight">3</style>+ [Combustion], Moc Monet +1
380. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
381. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion] <style="highlight">3 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n<style="highlight">대상의 [Combustion] 10 당, 피해량 +10% (최대 30%)</style>
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: <style="highlight">Coin Power +1 for every 3 [Combustion] on target (max 2)</style>\n<style="highlight">Deal +10% damage for every 10 [Combustion] on target (max 30%)</style>
   PL: <style="highlight">Moc Monet +1 za każde 3 [Combustion] na celu (maks. 2)</style>\n<style="highlight">Zadaje +10% obrażeń za każde 10 [Combustion] na celu (maks. 30%)</style>
383. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정면돌파
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].name ; dataList[id=1011202].levelList[level=2].name ; dataList[id=1011202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Frontal Assault
   PL: Szturm od Frontu
386. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 대상의 [Combustion] 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]
388. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, [Combustion] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict +2 [Combustion] Count on target
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], nakłada na cel +2 Licznika [Combustion]
390. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 대상의 [Combustion] 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=2].desc ; dataList[id=1011202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 6 [Combustion] on target (max 2)
   PL: Moc Monet +1 za każde 6 [Combustion] na celu (maks. 2)
391. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 대상의 [Combustion]당, 피해량 +2.5% (최대 30%)
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +2.5% damage for every [Combustion] on target (max 30%)
   PL: Zadaje +2,5% obrażeń za każde [Combustion] na celu (maks. 30%)
392. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, [Combustion] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1011202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict +2 [Combustion] Count on target<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], nakłada na cel +2 Licznika [Combustion]<style="highlight"></style>
393. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상의 [Combustion]당, 피해량 +<style="highlight">5</style>% (최대  <style="highlight">60</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +<style="highlight">5</style>% damage for every [Combustion] on target (max <style="highlight">60</style>%)
   PL: Zadaje +<style="highlight">5</style>% obrażeń za każde [Combustion] na celu (maks. <style="highlight">60</style>%)
394. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 검의 흐름
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].name ; dataList[id=1011203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Flow of the Sword
   PL: Przepływ Miecza
395. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion] 6 이상이면, 코인 위력 +1\n대상의 [Combustion] 6 당, 피해량 +10% (최대 30%)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 1명 정신력 10 회복\n- 공격 대상을 처치했거나 공격 대상의 [Combustion]이 10 이상이면, 인원 1명 추가
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If target has 6+ [Combustion], Coin Power +1\nDeal +10% damage for every 6 [Combustion] on target (max 30%)\n[EndSkill] Heal 10 SP for 1 other ally that has the lowest SP\n- If this attack killed the target, or if target had 10+ [Combustion], heal 1 more ally
   PL: Jeżeli cel ma 6+ [Combustion], Moc Monet +1\nZadaje +10% obrażeń za każde 6 [Combustion] na celu (maks. 30%)\n[EndSkill] Odzyskuje 10 Poczytalności dla 1 innego sojusznika z najniższą Poczytalnością\n- Jeżeli ten atak zabił cel lub cel miał 10+ [Combustion], odzyskuje 1 sojusznik więcej
396. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 대상의 [Combustion]당, 피해량 +2% (최대 60%)
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +2% damage for every [Combustion] on target (max 60%)
   PL: Zadaje +2% obrażeń za każde [Combustion] na celu (maks. 60%)
400. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌 (최대 30). 대상의 [Combustion] 횟수 2 감소
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1011203].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Deal Wrath damage equal to [Combustion] Potency on target (max 30). Reduce target's [Combustion] Count by 2
   PL: [OnSucceedAttack] Zadaje obrażenia Gniewem równe Mocy [Combustion] na celu (maks. 30). Zmniejsza Licznik [Combustion] celu o 2
401. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion] 6 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n대상의 [Combustion] 6 당, 피해량 +10% (최대 30%)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 1명 정신력 <style="highlight">15</style> 회복\n- 공격 대상을 처치했거나 공격 대상의 [Combustion]이 10 이상이면, 인원 1명 추가
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">Coin Power +1 for every 6 [Combustion] on target (max 2)</style>\nDeal +10% damage for every 6 [Combustion] on target (max 30%)\n[EndSkill] Heal <style="highlight">15</style> SP for 1 other ally that has the lowest SP\n- If this attack killed the target, or if target had 10+ [Combustion], heal 1 more ally
   PL: <style="highlight">Moc Monet +1 za każde 6 [Combustion] na celu (maks. 2)</style>\nZadaje +10% obrażeń za każde 6 [Combustion] na celu (maks. 30%)\n[EndSkill] Odzyskuje <style="highlight">15</style> Poczytalności dla 1 innego sojusznika z najniższą Poczytalnością\n- Jeżeli ten atak zabił cel lub cel miał 10+ [Combustion], odzyskuje 1 sojusznik więcej
402. [Obrona (ulepszenia 1,4) — nazwa] 염반
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].name ; dataList[id=1011204].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Flame Counter
   PL: Kontra Płomienia
403. [Obrona (ulepszenie 1) — opis] [BeforeHit] 대상의 [Combustion]만큼 보호막을 얻음 (최대 10, 턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeHit], [Combustion]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]; [Combustion] = 화상 / Burn
   EN: [BeforeHit] Gain Shield equal to [Combustion] on target (max 10, once per turn)
   PL: [BeforeHit] Zyskuje Tarczę równą [Combustion] na celu (maks. 10, raz na turę)
404. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여\n- 자신에게 보호막이 있으면, [Combustion] 1 추가 부여
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]\n- If this unit has Shield, inflict 1 additional [Combustion]
   PL: [OnSucceedAttackHead] Nakłada 1 [Combustion]\n- Jeżeli ta jednostka ma Tarczę, nakłada dodatkowe 1 [Combustion]
405. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여\n- 자신에게 보호막이 있으면, [Combustion] 1 추가 부여
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Obrona (ulepszenie 4) — opis] [BeforeHit] 대상의 [Combustion]만큼 보호막을 얻음 (최대 15, 턴 당 1회)\n[WhenUse] 대상의 [Combustion]이 10 이상이면, 피해량 +10%
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeHit], [Combustion], [WhenUse]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]; [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeHit] Gain Shield equal to [Combustion] on target (max 15, once per turn)\n[WhenUse] If target has 10+ [Combustion], deal +10% damage
   PL: [BeforeHit] Zyskuje Tarczę równą [Combustion] na celu (maks. 15, raz na turę)\n[WhenUse] Jeżeli cel ma 10+ [Combustion], zadaje +10% obrażeń
407. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — nazwa] 내면의 열혈
   źródło: Passives.json :: dataList[id=1011201].name
   limit: do 40 znaków
   EN: Inner Ardor
   PL: Wewnętrzna Żarliwość
408. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — opis] 턴 종료 시 현재 정신력이 가장 낮은 아군 1명의 정신력을 5 + (최대 공명 수)만큼 회복시킴. (최대 10) (자신 또는 패닉, E.G.O 침식 상태인 아군 제외)\n- 회복 대상이 [Combustion] 위력이나 횟수를 부여하는 기본 스킬을 보유하고 있으면, 정신력 5 추가 회복
   źródło: Passives.json :: dataList[id=1011201].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn End: Heal 1 ally that has the lowest SP by (5 + highest Reson.) (max 10) (excludes: self and Panicked or E.G.O Corroded allies)\n- If the said ally has Base Skills that inflict [Combustion] Potency or Count, heal 5 additional SP to them
   PL: Na koniec tury 1 sojusznik z najniższą Poczytalnością (poza tą jednostką oraz sojuszników w Panice lub Korozji E.G.O) odzyskuje (5 + najwyższy Rezonans) Poczytalności (maks. 10)\n- Jeżeli odzyskujący posiada Umiejętności bazowe nakładające Moc lub Licznik [Combustion], odzyskuje dodatkowe 5 Poczytalności
409. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — nazwa] 내면의 열혈
   źródło: Passives.json :: dataList[id=1011211].name
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — opis] 턴 종료 시 현재 정신력이 가장 낮은 아군 1명의 정신력을 5 + (최대 공명 수)만큼 회복시킴. (최대 10) (자신 또는 패닉, E.G.O 침식 상태인 아군 제외)\n- 회복 대상이 [Combustion] 위력이나 횟수를 부여하는 기본 스킬을 보유하고 있으면, 정신력 5 추가 회복\n- 분노 공명 4 이상이면, 회복 대상 1명 추가
   źródło: Passives.json :: dataList[id=1011211].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn End: Heal 1 ally that has the lowest SP by (5 + highest Reson.) (max 10) (excludes: self and Panicked or E.G.O Corroded allies)\n- If the said ally has Base Skills that inflict [Combustion] Potency or Count, heal 5 additional SP to them\n- At 4+ Wrath Reson., heal 1 additional ally
   PL: Na koniec tury 1 sojusznik z najniższą Poczytalnością (poza tą jednostką oraz sojuszników w Panice lub Korozji E.G.O) odzyskuje (5 + najwyższy Rezonans) Poczytalności (maks. 10)\n- Jeżeli odzyskujący posiada Umiejętności bazowe nakładające Moc lub Licznik [Combustion], odzyskuje dodatkowe 5 Poczytalności\n- Przy 4+ Rezonansie Gniewu odzyskuje 1 sojusznik więcej
411. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 리우 방진
   źródło: Passives.json :: dataList[id=1011221].name
   limit: do 40 znaków
   EN: Liu Defensive Square
   PL: Kwadrat Obrony Liu
412. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 정신력이 가장 낮은 아군 2명이 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 5 회복
   źródło: Passives.json :: dataList[id=1011221].desc
   limit: do 120 znaków
   EN: For 2 allies that have the lowest SP: If they lost SP this turn, heal 5 SP at Turn End
   PL: 2 sojuszników z najniższą Poczytalnością, którzy w tej turze ją stracili, odzyskuje na koniec tury 5 Poczytalności
413. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — nazwa] 리우 방진
   źródło: Passives.json :: dataList[id=1011231].name
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — opis] 정신력이 가장 낮은 아군 2명이 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 5 회복\n- 회복 대상이 [Combustion] 위력이나 횟수를 부여하는 기본 스킬을 보유하고 있으면, 대신 5 - 10 회복
   źródło: Passives.json :: dataList[id=1011231].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: For 2 allies that have the lowest SP: If they lost SP this turn, heal 5 SP at Turn End\n- If the said allies have Base Skills that inflict [Combustion] Potency or Count, heal 5~10 SP instead
   PL: 2 sojuszników z najniższą Poczytalnością, którzy w tej turze ją stracili, odzyskuje na koniec tury 5 Poczytalności\n- Jeżeli odzyskujący posiadają Umiejętności bazowe nakładające Moc lub Licznik [Combustion], odzyskują zamiast tego 5~10 Poczytalności

## [000] N Corp. E.G.O:: Fell Bullet — Yi Sang — N사 E.G.O:: 흉탄
- ID Tożsamości: `10113` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Poise

415. [Karta Tożsamości — tytuł] N사 E.G.O::\n흉탄
   źródło: Personalities.json :: dataList[id=10113].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp. E.G.O::\nFell Bullet
   PL: E.G.O Korp. N::\nMroczny Pocisk
416. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10113].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10113].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Karta Tożsamości — opis] 이상의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10113].desc
   limit: do 120 znaków
   EN: Yi Sang's 13th Identity
   PL: Trzynasta Tożsamość Yi Sanga
419. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 헛점 파악
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=1].name ; dataList[id=1011301].levelList[level=2].name ; dataList[id=1011301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: See Through Defenses
   PL: Dostrzeżenie Słabości
420. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 [BoseProjektil]당 피해량 +7% (최대 49%)\n[WhenUse] [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [BoseProjektil], [WhenUse]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]
   EN: Deal +7% damage for every [BoseProjektil] on self (max 49%)\n[WhenUse] Gain 1 [BoseProjektil]
   PL: Zadaje +7% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 49%)\n[WhenUse] Zyskuje 1 [BoseProjektil]
421. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
422. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 [BoseProjektil]당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)\n<style="highlight">[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 이상이면, 기본 위력 +1</style>\n[WhenUse] <style="highlight">자신의 [Breath] 횟수 1 증가,</style> [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BoseProjektil], [WhenUse], [Breath]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Deal +<style="highlight">10</style>% damage for every [BoseProjektil] on self (max <style="highlight">70</style>%)\n<style="highlight">[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] At 3+ [Breath] Count, Base Power +1 </style>\n[WhenUse] Gain <style="highlight">+1 [Breath] Count and</style> 1 [BoseProjektil]
   PL: Zadaje +<style="highlight">10</style>% obrażeń za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">70</style>%)\n<style="highlight">[WhenUse] Przy 5+ [Breath] Moc Monet +1\n[WhenUse] Przy 3+ Licznika [Breath] Moc Bazowa +1</style>\n[WhenUse] Zyskuje <style="highlight">+1 Licznika [Breath] i</style> 1 [BoseProjektil]
423. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]<style="highlight"></style>
424. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttackHead] [Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttackHead], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttackHead] Inflict +1 [Laceration] Count</style>
   PL: <style="highlight">[CriticalOnSucceedAttackHead] Nakłada +1 Licznika [Laceration]</style>
425. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttackHead] [BoseProjektil] 1 얻음</style>
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttackHead], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: <style="highlight">[CriticalOnSucceedAttackHead] Gain 1 [BoseProjektil]</style>
   PL: <style="highlight">[CriticalOnSucceedAttackHead] Zyskuje 1 [BoseProjektil]</style>
426. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 [BoseProjektil]당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">105</style>%)\n[WhenUse] 자신의 [Breath] 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 <style="highlight">당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가, [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BoseProjektil], [WhenUse], [Breath]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Deal +<style="highlight">15</style>% damage for every [BoseProjektil] on self (max <style="highlight">105</style>%)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] <style="highlight">Base Power +1 for every 3 [Breath] Count on self (max 2)</style>\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count and 1 [BoseProjektil]
   PL: Zadaje +<style="highlight">15</style>% obrażeń za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">105</style>%)\n[WhenUse] Moc Monet +1 za każde 5 [Breath] na tej jednostce <style="highlight">(maks. 2)</style>\n[WhenUse] Moc Bazowa +1 za każde 3 Licznika [Breath] na tej jednostce <style="highlight">(maks. 2)</style>\n[WhenUse] Zyskuje +<style="highlight">2</style> Licznika [Breath] i 1 [BoseProjektil]
427. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack]</style> [Laceration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttack]</style> Inflict +1 [Laceration] Count
   PL: <style="highlight">[CriticalOnSucceedAttack]</style> Nakłada +1 Licznika [Laceration]
428. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttack]</style> [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: <style="highlight">[CriticalOnSucceedAttack]</style> Gain 1 [BoseProjektil]
   PL: <style="highlight">[CriticalOnSucceedAttack]</style> Zyskuje 1 [BoseProjektil]
429. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 꿰뚫으리라
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].name ; dataList[id=1011302].levelList[level=2].name ; dataList[id=1011302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Punch Through
   PL: Przeszyję na Wylot
430. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [BoseProjektil]당 피해량 +10% (최대 70%)\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BoseProjektil], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +10% damage for every [BoseProjektil] on self (max 70%)\n[WhenUse] Gain 2 [Breath]
   PL: [WhenUse] Zadaje +10% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 70%)\n[WhenUse] Zyskuje 2 [Breath]
431. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]
432. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [OnSucceedAttack] Gain 1 [BoseProjektil]
   PL: [OnSucceedAttack] Zyskuje 1 [BoseProjektil]
435. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] [BoseProjektil] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [CriticalOnSucceedAttack] Gain 2 [BoseProjektil]
   PL: [CriticalOnSucceedAttack] Zyskuje 2 [BoseProjektil]
436. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [BoseProjektil]당 피해량 +10% (최대 70%)\n<style="highlight">[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BoseProjektil], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +10% damage for every [BoseProjektil] on self (max 70%)\n<style="highlight">[WhenUse] At 5+ [Breath], Coin Power +1</style>\n[WhenUse] Gain 2 [Breath]
   PL: [WhenUse] Zadaje +10% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 70%)\n<style="highlight">[WhenUse] Przy 5+ [Breath] Moc Monet +1</style>\n[WhenUse] Zyskuje 2 [Breath]
437. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]<style="highlight"></style>
438. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttackHead] [Laceration] 2 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttackHead], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttackHead] Inflict 2 [Laceration]</style>
   PL: <style="highlight">[CriticalOnSucceedAttackHead] Nakłada 2 [Laceration]</style>
439. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
440. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BoseProjektil] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [OnSucceedAttack] Gain 1 [BoseProjektil]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 1 [BoseProjektil]<style="highlight"></style>
442. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 4 — opis] <style="highlight">[CriticalOnSucceedAttack] [Laceration] 1 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [Laceration]</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Nakłada 1 [Laceration]</style>
443. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 5 — opis] [CriticalOnSucceedAttack] [BoseProjektil] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#4].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [CriticalOnSucceedAttack] Gain 2 [BoseProjektil]<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zyskuje 2 [BoseProjektil]<style="highlight"></style>
444. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [BoseProjektil]당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">105</style>%)\n[WhenUse] 자신의 [Breath] 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BoseProjektil], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +<style="highlight">15</style>% damage for every [BoseProjektil] on self (max <style="highlight">105</style>%)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] Gain 2 [Breath]
   PL: [WhenUse] Zadaje +<style="highlight">15</style>% obrażeń za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">105</style>%)\n[WhenUse] Moc Monet +1 za każde 5 [Breath] na tej jednostce <style="highlight">(maks. 2)</style>\n[WhenUse] Zyskuje 2 [Breath]
445. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack]</style> [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttack]</style> Inflict 2 [Laceration]<style="highlight"></style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Nakłada 2 [Laceration]</style><style="highlight"></style>
446. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL: [CriticalOnSucceedAttack] Nakłada <style="highlight">2</style> [Laceration]
447. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대상 조정 사격
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].name ; dataList[id=1011303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: Target Readjustment Fire
   PL: Strzał z Korektą Celu
448. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 체력이 가장 낮은 대상 우선 공격\n- 자신의 [BoseProjektil]이 7이면, 메인 타겟을 아군 우선 지정\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모\n- 전부 소모했고 아군이 사망했으면, 자신의 정신력 20 회복
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Targets the unit that has the lowest HP\n- At 7 [BoseProjektil], primarily targets among allies as the main target\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] At 3+ [Breath] Count, Base Power +1\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all\n- If this unit lost all [BoseProjektil], and if an ally is killed, heal 20 SP on self
   PL: [StartBattle] Celuje w jednostkę z najniższym HP\n- Przy 7 [BoseProjektil] głównym celem są przede wszystkim sojusznicy\n[StartBattle] Waga ataku +1 za każde 3 [BoseProjektil] na tej jednostce (maks. 2)\n[WhenUse] Przy 5+ [Breath] Moc Monet +1\n[WhenUse] Przy 3+ Licznika [Breath] Moc Bazowa +1\n[WhenUse] Zyskuje 1 [Breath] za każde [BoseProjektil] na tej jednostce (maks. 7)\n[EndSkill] Traci ([BoseProjektil] na tej jednostce × 2) Poczytalności (maks. 14)\n[EndSkill] Jeżeli ma 7 [BoseProjektil] na początku walki, zużywa je wszystkie\n- Jeżeli zużyła wszystkie [BoseProjektil] i sojusznik zginął, odzyskuje 20 Poczytalności
449. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target
   PL: Ta moneta zadaje obrażenia tylko głównemu celowi
451. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] 메인 타겟이 아군이면, 아래 효과가 적용됨\n- 이 공격에 한해 관통 속성 내성을 취약으로 변경함
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If the main target is an ally, activate the following effects:\n- The main target's Pierce Resistance becomes Fatal against this attack
   PL: Jeżeli głównym celem jest sojusznik, aktywują się następujące efekty:\n- Odporność głównego celu na Kłucie staje się Fatal dla tego ataku
452. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] - 자신의 [BoseProjektil]당 피해량 +5% (최대 35%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - Deal +5% damage for every [BoseProjektil] on self (max 35%)
   PL: - Zadaje +5% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 35%)
453. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 5 — opis] - 자신의 [Breath]당 크리티컬 피해량 +2% (최대 40%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: - +2% Damage on Critical Hit for every [Breath] on self (max 40%)
   PL: - +2% obrażeń Krytycznych za każdy [Breath] na tej jednostce (maks. 40%)
454. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the sub-targets
   PL: Ta moneta zadaje obrażenia tylko celom drugorzędnym
456. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] - 메인 타겟이 적이였을 경우, 메인 타겟에게 피해를 입힘
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: - However, if the main target was an enemy, deal damage against the main target
   PL: - Jeżeli jednak głównym celem był wróg, zadaje mu obrażenia
457. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 4 — opis] - 첫번째 코인에서 아군을 처치하지 못했으면, 서브 타겟 중 무작위 1명이 피해를 입음
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If the first Coin failed to kill an ally, 1 random sub-target takes damage
   PL: - Jeżeli pierwsza moneta nie zabiła sojusznika, obrażenia otrzymuje 1 losowy cel drugorzędny
458. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 5 — opis] 자신의 [BoseProjektil]당, 피해량 +15% (최대 105%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +15% damage for every [BoseProjektil] on self (max 105%)
   PL: Zadaje +15% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 105%)
459. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 6 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 자신의 [BoseProjektil]당 피해량 +30% (최대 210%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#5].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - If the first Coin killed an ally, deal +30% damage for every [BoseProjektil] on self instead (max 210%)
   PL: - Jeżeli pierwsza moneta zabiła sojusznika, zamiast tego zadaje +30% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 210%)
460. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 7 — opis] [Breath] 위력당, 크리티컬 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +2.5% Damage on Critical Hit for every [Breath] Potency (max 25%)
   PL: +2,5% obrażeń Krytycznych za każdą Moc [Breath] (maks. 25%)
461. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 8 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +7% (최대 49%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +7% Damage on Critical Hit for every [BoseProjektil] on self (max 49%)
   PL: +7% obrażeń Krytycznych za każde [BoseProjektil] na tej jednostce (maks. 49%)
462. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 9 — opis] 첫번째 코인으로 메인 타겟에게 가한 피해 비율(최대 체력 기준)만큼 피해량이 증가 (최대 100%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#8].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#8].desc
   limit: do 120 znaków
   EN: Deal +(HP percentage the first Coin removed from the main target)% damage (max 100%)
   PL: Zadaje +(procent Maks. HP zadany pierwszą monetą głównemu celowi)% obrażeń (maks. 100%)
463. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 10 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#9].desc
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 11 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: - If the first Coin killed an ally, inflict 3 [Laceration] and +1 [Laceration] Count instead
   PL: - Jeżeli pierwsza moneta zabiła sojusznika, zamiast tego nakłada 3 [Laceration] i +1 Licznika [Laceration]
465. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 체력이 가장 낮은 대상 우선 공격\n- 자신의 [BoseProjektil]이 7이면, 메인 타겟을 아군 우선 지정\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 <style="highlight">당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모\n- 전부 소모했고 아군이 사망했으면, 자신의 정신력 20 회복
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Targets the unit that has the lowest HP\n- At 7 [BoseProjektil], primarily targets among allies as the main target\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] <style="highlight">Base Power +1 for every 3 [Breath] Count on self (max 2)</style>\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all\n- If this unit lost all [BoseProjektil], and if an ally is killed, heal 20 SP on self
   PL: [StartBattle] Celuje w jednostkę z najniższym HP\n- Przy 7 [BoseProjektil] głównym celem są przede wszystkim sojusznicy\n[StartBattle] Waga ataku +1 za każde 3 [BoseProjektil] na tej jednostce (maks. 2)\n[WhenUse] <style="highlight">Moc Monet +1 za każde 5 [Breath] na tej jednostce (maks. 2)</style>\n[WhenUse] <style="highlight">Moc Bazowa +1 za każde 3 Licznika [Breath] na tej jednostce (maks. 2)</style>\n[WhenUse] Zyskuje 1 [Breath] za każde [BoseProjektil] na tej jednostce (maks. 7)\n[EndSkill] Traci ([BoseProjektil] na tej jednostce × 2) Poczytalności (maks. 14)\n[EndSkill] Jeżeli ma 7 [BoseProjektil] na początku walki, zużywa je wszystkie\n- Jeżeli zużyła wszystkie [BoseProjektil] i sojusznik zginął, odzyskuje 20 Poczytalności
466. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] - 자신의 [BoseProjektil]당 피해량 +7% (최대 49%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - Deal +7% damage for every [BoseProjektil] on self (max 49%)
   PL: - Zadaje +7% obrażeń za każde [BoseProjektil] na tej jednostce (maks. 49%)
467. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 5 — opis] - 자신의 [Breath]당 크리티컬 피해량 +3% (최대 60%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: - +3% Damage on Critical Hit for every [Breath] on self (max 60%)
   PL: - +3% obrażeń Krytycznych za każdy [Breath] na tej jednostce (maks. 60%)
468. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 5 — opis] 자신의 [BoseProjektil]당, 피해량 +<style="highlight">20</style>% (최대 <style="highlight">140</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +<style="highlight">20</style>% damage for every [BoseProjektil] on self (max <style="highlight">140</style>%)
   PL: Zadaje +<style="highlight">20</style>% obrażeń za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">140</style>%)
469. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 6 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 자신의 [BoseProjektil]당 피해량 +<style="highlight">40</style>% (최대 <style="highlight">280</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#5].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - If the first Coin killed an ally, deal +<style="highlight">40</style>% damage for every [BoseProjektil] on self instead (max <style="highlight">280</style>%)
   PL: - Jeżeli pierwsza moneta zabiła sojusznika, zamiast tego zadaje +<style="highlight">40</style>% obrażeń za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">280</style>%)
470. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 7 — opis] [Breath] 위력당, 크리티컬 피해량 +<style="highlight">5</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +<style="highlight">5</style>% Damage on Critical Hit for every [Breath] Potency (max <style="highlight">50</style>%)
   PL: +<style="highlight">5</style>% obrażeń Krytycznych za każdą Moc [Breath] (maks. <style="highlight">50</style>%)
471. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 8 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +<style="highlight">10</style>% Damage on Critical Hit for every [BoseProjektil] on self (max <style="highlight">70</style>%)
   PL: +<style="highlight">10</style>% obrażeń Krytycznych za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">70</style>%)
472. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 10 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#9].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Laceration]
473. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 11 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 [Laceration] <style="highlight">5</style> 부여, [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: - If the first Coin killed an ally, inflict <style="highlight">5</style> [Laceration] and +<style="highlight">2</style> [Laceration] Count instead
   PL: - Jeżeli pierwsza moneta zabiła sojusznika, zamiast tego nakłada <style="highlight">5</style> [Laceration] i +<style="highlight">2</style> Licznika [Laceration]
474. [Obrona (ulepszenia 1,4) — nazwa] 전방 지원
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].name ; dataList[id=1011304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Front Line Support
   PL: Wsparcie Pierwszej Linii
475. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath] 2 당, 코인 위력 +1 (최대 2)\n[WhenUse] [BoseProjektil] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [BoseProjektil]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [DuelCounter]\n[WhenUse] Coin Power +1 for every 2 [Breath] on self (max 2)\n[WhenUse] Gain 2 [BoseProjektil]
   PL: [DuelCounter]\n[WhenUse] Moc Monet +1 za każde 2 [Breath] na tej jednostce (maks. 2)\n[WhenUse] Zyskuje 2 [BoseProjektil]
476. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Obrona (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011304].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika [Breath]
478. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath] 2 당, 코인 위력 +1 (최대 3)\n[WhenUse] [BoseProjektil] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [BoseProjektil]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [DuelCounter]\n[WhenUse] Coin Power +1 for every 2 [Breath] on self (max 3)\n[WhenUse] Gain 2 [BoseProjektil]
   PL: [DuelCounter]\n[WhenUse] Moc Monet +1 za każde 2 [Breath] na tej jednostce (maks. 3)\n[WhenUse] Zyskuje 2 [BoseProjektil]
479. [Pasywka bojowa (od ulepszenia 1) — nazwa] 휘발된 추억
   źródło: Passives.json :: dataList[id=1011302].name
   limit: do 40 znaków
   EN: Volatilized Memory
   PL: Odparowane Wspomnienie
480. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 종료 시 자신의 [BoseProjektil]을 전부 제거하고 다음 턴에 제거한 수치만큼 [BoseProjektil]을 얻음
   źródło: Passives.json :: dataList[id=1011302].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Turn End: Lose all [BoseProjektil] on self. Next turn, gain [BoseProjektil] equal to the amount lost
   PL: Na koniec tury usuwa całe swoje [BoseProjektil]; w następnej turze zyskuje tyle [BoseProjektil], ile usunięto
481. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Pride) — nazwa] 흉탄
   źródło: Passives.json :: dataList[id=1011301].name
   limit: do 40 znaków
   EN: Fell Bullet
   PL: Mroczny Pocisk
482. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Pride) — opis] 전투 중 자신의 공격으로 아군을 사망시켰으면, 다음 턴동안 [FellBulletPersonality]을 얻음 (자신의 E.G.O 침식 및 아군 공격 포함)\n자신의 E.G.O 흉탄을 사용하여, [BoseProjektil]이 소모되면, 턴 종료 시 소모한만큼 다음 턴에 [BoseProjektil]을 얻음
   źródło: Passives.json :: dataList[id=1011301].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [FellBulletPersonality], [BoseProjektil]
   znaczenie tagów: [FellBulletPersonality] = 흉탄 / Fell Bullet; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: If this unit killed an allied unit using its attack, gain [FellBulletPersonality] for the next turn (including using this unit's 'E.G.O Corrosion' and attacks against allies)\nIf this unit uses its E.G.O 'Fell Bullet' and consumes [BoseProjektil]: Next turn, gain [BoseProjektil] equal to the amount of it consumed by the end of the last turn
   PL: Jeżeli podczas walki ta jednostka zabiła atakiem sojusznika, zyskuje [FellBulletPersonality] na następną turę (w tym Korozję E.G.O tej jednostki i ataki na sojuszników)\nGdy ta jednostka używa swojego E.G.O „Mroczny Pocisk” i zużywa [BoseProjektil]: w następnej turze zyskuje [BoseProjektil] równe ilości zużytej do końca ostatniej tury
483. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Pride) — nazwa] 대상 지정
   źródło: Passives.json :: dataList[id=1011321].name
   limit: do 40 znaków
   EN: Designate Target
   PL: Wskazanie Celu
484. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Pride) — opis] 속도가 가장 느린 아군이 아군을 공격했다면 공격 종료 시, 다음 턴에 [AttackDmgUp]를 1 얻음 (턴 당 최대 2)\n- 이 때, 아군이 사망했으면, 위 효과를 대신하여 이번 전투 동안 [AttackDmgUp]를 1 얻음 (스테이지 및 인격당 최대 2)\n- 위 효과들로 얻는 [AttackDmgUp]는 최대 2까지만 얻어짐.
   źródło: Passives.json :: dataList[id=1011321].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: When the ally with the slowest Speed attacked an ally, Attack End: Gain 1 [AttackDmgUp] next turn (2 times per turn)\n- If the attacked ally is killed by this attack, gain 1 [AttackDmgUp] for the whole Encounter instead (max 2 per Stage per Identity)\n- Can gain only up to 2 [AttackDmgUp] from the above effect
   PL: Gdy sojusznik z najniższą Szybkością zaatakował sojusznika, na koniec ataku zyskuje 1 [AttackDmgUp] w następnej turze (2 razy na turę)\n- Jeżeli zaatakowany sojusznik zginął od tego ataku, zamiast tego zyskuje 1 [AttackDmgUp] na całe spotkanie (maks. 2 na etap na Tożsamość)\n- Efekty te mogą dać łącznie maks. 2 [AttackDmgUp]

## [000] Heishou Pack - Wu Branch Adept — Yi Sang — 흑수 - 오 필두
- ID Tożsamości: `10114` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Rupture, Tremor

485. [Karta Tożsamości — tytuł] 흑수 - 오 필두
   źródło: Personalities.json :: dataList[id=10114].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heishou Pack -\nWu Branch Adept
   PL: Adept Watahy Heishou -\nGałąź Wu
486. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10114].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10114].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Karta Tożsamości — opis] 이상의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10114].desc
   limit: do 120 znaków
   EN: Yi Sang's 14th Identity
   PL: Czternasta Tożsamość Yi Sanga
489. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 베어 무너뜨리리
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=1].name ; dataList[id=1011401].levelList[level=2].name ; dataList[id=1011401].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cut Down and Trample
   PL: Ścieć i Zdepcz
490. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Vibration]의 합이 5 이상이면, 코인 위력 + 1
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 5+ ([Burst] + [Vibration]), Coin Power +1
   PL: [WhenUse] Jeżeli suma [Burst] i [Vibration] celu wynosi 5 lub więcej, Moc Monet +1
491. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
493. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">자신의 속도가 대상보다 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합이 5 이상이면, 코인 위력 + 1
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor
   EN: <style="highlight">If this unit's Speed is faster than the target's, Coin Power +1</style>\n[WhenUse] If target has 5+ ([Burst] + [Vibration]), Coin Power +1
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Monet +1</style>\n[WhenUse] Jeżeli suma [Burst] i [Vibration] celu wynosi 5 lub więcej, Moc Monet +1
494. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Burst] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada +1 Licznika [Burst]</style>
495. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]<style="highlight"></style>
496. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높으면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합이 5 이상이면, 코인 위력 + 1\n<style="highlight">[WinDuel] 다음 턴에 [Binding] 1 부여 (턴 당 2회)</style>
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Vibration], [WinDuel], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [Binding] = 속박 / Bind
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] If target has 5+ ([Burst] + [Vibration]), Coin Power +1\n<style="highlight">[WinDuel] Inflict 1 [Binding] next turn (2 times per turn)</style>
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Monet +1\n[WhenUse] Jeżeli suma [Burst] i [Vibration] celu wynosi 5 lub więcej, Moc Monet +1\n<style="highlight">[WinDuel] Nakłada w następnej turze 1 [Binding] (2 razy na turę)</style>
497. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
498. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
499. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Vibration]
500. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 월도격 [月刀擊]
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=1].name ; dataList[id=1011402].levelList[level=2].name ; dataList[id=1011402].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Crescent Blade Strike [月刀擊]
   PL: Cięcie Woldo [月刀擊]
501. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)\n[WhenUse] 다음 턴에 [Agility]을 1 얻음 (턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Vibration], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [Agility] = 신속 / Haste
   EN: [WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)\n[WhenUse] Gain 1 [Agility] next turn (once per turn)
   PL: [WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)\n[WhenUse] Zyskuje 1 [Agility] w następnej turze (raz na turę)
502. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
504. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1.
505. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">자신의 속도가 대상보다 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)\n[WhenUse] 다음 턴에 [Agility]을 <style="highlight">2</style> 얻음 (턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Vibration], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [Agility] = 신속 / Haste
   EN: <style="highlight">If this unit's Speed is faster than the target's, Coin Power +1</style>\n[WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)\n[WhenUse] Gain <style="highlight">2</style> [Agility] next turn (once per turn)
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Monet +1</style>\n[WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)\n[WhenUse] Zyskuje <style="highlight">2</style> [Agility] w następnej turze (raz na turę)
506. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
507. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상에게 주살이 없으면, [ConcussionYisang] 1 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ConcussionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ConcussionYisang] = 뇌진탕 / Concussion
   EN: <style="highlight">[OnSucceedAttack] If target does not have Deathrite, inflict 1 [ConcussionYisang]</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli cel nie ma Obrzędu Śmierci, nakłada 1 [ConcussionYisang]</style>
508. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높으면,\n- 코인 위력 +1\n<style="highlight">- 대상보다 2 이상 높으면, (자신의 [BreakthroughHorse] x 20)%만큼 피해량이 증가 (최대 100%)</style>\n\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)\n[WhenUse] 다음 턴에 [Agility]을 2 얻음 (턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BreakthroughHorse], [WhenUse], [Burst], [Vibration], [Agility]
   znaczenie tagów: [BreakthroughHorse] = 적진 주파 / Linebreaker; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [Agility] = 신속 / Haste
   EN: If this unit's Speed is faster than the target's:\n- Coin Power +1\n<style="highlight">- If this unit's Speed is faster than the target's by 2 or more, deal +([BreakthroughHorse] on self x 20)% damage (max 100%)</style>\n\n[WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)\n[WhenUse] Gain 2 [Agility] next turn (once per turn)
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu:\n- Moc Monet +1\n<style="highlight">- Jeżeli Szybkość jest większa o 2 lub więcej, zadaje +([BreakthroughHorse] na tej jednostce × 20)% obrażeń (maks. 100%)</style>\n\n[WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)\n[WhenUse] Zyskuje 2 [Agility] w następnej turze (raz na turę)
509. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]<style="highlight"></style>
510. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 주살이 없으면, [ConcussionYisang] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ConcussionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ConcussionYisang] = 뇌진탕 / Concussion
   EN: [OnSucceedAttack] If target doesn't have Deathrite, inflict 1 [ConcussionYisang]<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel nie ma Obrzędu Śmierci, nakłada 1 [ConcussionYisang]<style="highlight"></style>
511. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 대상에게 주살이 있으면, [Burst] 3 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011402].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] If target has Deathrite, inflict 3 [Burst]</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli cel ma Obrzęd Śmierci, nakłada 3 [Burst]</style>
512. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 선봉주파
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].name ; dataList[id=1011403].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Cavalry's Vanguard Charge
   PL: Szturm Awangardy
513. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 높으면,\n- 최종 위력 +1\n- (자신의 [BreakthroughHorse] x 10)%만큼 피해량이 증가 (최대 40%)\n\n자신의 (보호막 수치 x 2)% 만큼 피해량이 증가 (최대 50%)\n\n[BeforeUse] 자신의 [BreakthroughHorse]가 5면, 전부 소모하여 ‘흑풍마각월참’으로 발동됨\n[WhenUse] [LegStrengthHorseYisang] 3 얻음\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [BreakthroughHorse], [BeforeUse], [WhenUse], [LegStrengthHorseYisang], [Burst], [Vibration]
   znaczenie tagów: [BreakthroughHorse] = 적진 주파 / Linebreaker; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor
   EN: If this unit's Speed is faster than the target's:\n- Final Power +1\n- Deal +([BreakthroughHorse] on self x 10)% damage (max 40%)\n\nDeal +(Shield HP on self x 2)% damage (max 50%)\n\n[BeforeUse] At 5 [BreakthroughHorse], consume all of it to activate "Obsidian Stormrider's Crescent Decapitator" instead\n[WhenUse] Gain 3 [LegStrengthHorseYisang]\n[WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu:\n- Moc Końcowa +1\n- Zadaje +([BreakthroughHorse] na tej jednostce × 10)% obrażeń (maks. 40%)\n\nZadaje +(wartość Tarczy tej jednostki × 2)% obrażeń (maks. 50%)\n\n[BeforeUse] Przy 5 [BreakthroughHorse] zużywa je wszystkie, by aktywować „Sierpowe Ścięcie Obsydianowego Jeźdźca Burzy”\n[WhenUse] Zyskuje 3 [LegStrengthHorseYisang]\n[WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)
514. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011403].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
518. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [LegStrengthHorseYisang]가 2 이상이면, [ConcussionYisang] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LegStrengthHorseYisang], [ConcussionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [ConcussionYisang] = 뇌진탕 / Concussion
   EN: [OnSucceedAttack] At 2+ [LegStrengthHorseYisang], inflict 1 [ConcussionYisang]
   PL: [OnSucceedAttack] Przy 2+ [LegStrengthHorseYisang] nakłada 1 [ConcussionYisang]
520. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높으면,\n- 최종 위력 +1\n- (자신의 [BreakthroughHorse] x <style="highlight">20</style>)%만큼 피해량이 증가 (최대 <style="highlight">80</style>%)\n\n자신의 (보호막 수치 x 2)% 만큼 피해량이 증가 (최대 50%)\n\n[BeforeUse] 자신의 [BreakthroughHorse]가 5면, 전부 소모하여 ‘흑풍마각월참’으로 발동됨\n[WhenUse] [LegStrengthHorseYisang] 3 얻음\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)\n<style="highlight">[WhenUse] 자신의 [BreakthroughHorse]가 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨</style>
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=4].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BreakthroughHorse], [BeforeUse], [WhenUse], [LegStrengthHorseYisang], [Burst], [Vibration], [SuperCoin]
   znaczenie tagów: [BreakthroughHorse] = 적진 주파 / Linebreaker; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: If this unit's Speed is faster than the target's:\n- Final Power +1\n- Deal +([BreakthroughHorse] on self x <style="highlight">20</style>)% damage (max <style="highlight">80</style>%)\n\nDeal +(Shield HP on self x 2)% damage (max 50%)\n\n[BeforeUse] At 5 [BreakthroughHorse], consume all of it to activate "Obsidian Stormrider's Crescent Decapitator" instead\n[WhenUse] Gain 3 [LegStrengthHorseYisang]\n[WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)\n<style="highlight">[WhenUse] At 3+ [BreakthroughHorse], convert all Coins to [SuperCoin]s</style>
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu:\n- Moc Końcowa +1\n- Zadaje +([BreakthroughHorse] na tej jednostce × <style="highlight">20</style>)% obrażeń (maks. <style="highlight">80</style>%)\n\nZadaje +(wartość Tarczy tej jednostki × 2)% obrażeń (maks. 50%)\n\n[BeforeUse] Przy 5 [BreakthroughHorse] zużywa je wszystkie, by aktywować „Sierpowe Ścięcie Obsydianowego Jeźdźca Burzy”\n[WhenUse] Zyskuje 3 [LegStrengthHorseYisang]\n[WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)\n<style="highlight">[WhenUse] Przy 3+ [BreakthroughHorse] wszystkie monety zmieniają się w [SuperCoin]</style>
521. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">- 자신의 [BreakthroughHorse]가 3 이상이면, [Binding] 1 추가 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BreakthroughHorse], [Binding]
   znaczenie tagów: [BreakthroughHorse] = 적진 주파 / Linebreaker; [Binding] = 속박 / Bind
   EN: <style="highlight">- At 3+ [BreakthroughHorse], inflict 1 additional [Binding]</style>
   PL: <style="highlight">- Przy 3+ [BreakthroughHorse] nakłada dodatkowe 1 [Binding]</style>
522. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]<style="highlight"></style>
523. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [LegStrengthHorseYisang]가 2 이상이면, [ConcussionYisang] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [LegStrengthHorseYisang], [ConcussionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [ConcussionYisang] = 뇌진탕 / Concussion
   EN: [OnSucceedAttack] At 2+ [LegStrengthHorseYisang], inflict <style="highlight">2</style> [ConcussionYisang]
   PL: [OnSucceedAttack] Przy 2+ [LegStrengthHorseYisang] nakłada <style="highlight">2</style> [ConcussionYisang]
524. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 흑풍마각월참 [黑風馬脚月斬]
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].name ; dataList[id=1011405].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 4 (+3)
   limit: do 70 znaków
   EN: Obsidian Stormrider's Crescent Decapitator [黑風馬脚月斬]
   PL: Sierpowe Ścięcie Obsydianowego Jeźdźca Burzy [黑風馬脚月斬]
525. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 자신의 속도가 대상보다 높으면, 최종 위력 +1\n[WhenUse] 다음 턴에 자신을 제외한 모든 아군에게 [BattlefieldHorse] 1 부여 (턴 당 1회)\n[WhenUse] [LegStrengthHorseYisang] 3 얻음\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)\n[WinDuel] 자신의 속도가 대상보다 높으면, 피해량 +50%
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BattlefieldHorse], [LegStrengthHorseYisang], [Burst], [Vibration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BattlefieldHorse] = 호령 / Commanding Cry; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, Final Power +1\n[WhenUse] Apply 1 [BattlefieldHorse] on all other allies next turn (once per turn)\n[WhenUse] Gain 3 [LegStrengthHorseYisang]\n[WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)\n[WinDuel] If this unit's Speed is faster than the target's, deal +50% damage
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Końcowa +1\n[WhenUse] Nakłada w następnej turze 1 [BattlefieldHorse] na wszystkich pozostałych sojuszników (raz na turę)\n[WhenUse] Zyskuje 3 [LegStrengthHorseYisang]\n[WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)\n[WinDuel] Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +50% obrażeń
526. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011405].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011405].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] Nakłada 3 [Burst]
528. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=1011405].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] Nakłada 4 [Vibration]
529. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011405].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1011405].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1011405].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
532. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011405].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [ConcussionYisang] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1011405].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ConcussionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ConcussionYisang] = 뇌진탕 / Concussion
   EN: [OnSucceedAttack] Inflict 1 [ConcussionYisang]
   PL: [OnSucceedAttack] Nakłada 1 [ConcussionYisang]
534. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1011405].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1011405].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1011405].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높으면, 최종 위력 +1\n[WhenUse] 다음 턴에 자신을 제외한 모든 아군에게 [BattlefieldHorse] 1 부여 (턴 당 1회)\n[WhenUse] [LegStrengthHorseYisang] 3 얻음\n[WhenUse] 대상의 [Burst]과 [Vibration]의 합 5당, 코인 위력 + 1 (최대 2)\n[WinDuel] 자신의 속도가 대상보다 높으면, 피해량 +50%\n<style="highlight">[WinDuel] 메인 타겟에게 [ConcussionYisang] 1 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011405].levelList[level=4].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BattlefieldHorse], [LegStrengthHorseYisang], [Burst], [Vibration], [WinDuel], [ConcussionYisang]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BattlefieldHorse] = 호령 / Commanding Cry; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [ConcussionYisang] = 뇌진탕 / Concussion
   EN: If this unit's Speed is faster than the target's, Final Power +1\n[WhenUse] Apply 1 [BattlefieldHorse] on all other allies next turn (once per turn)\n[WhenUse] Gain 3 [LegStrengthHorseYisang]\n[WhenUse] Coin Power +1 for every 5 ([Burst] + [Vibration]) on target (max 2)\n[WinDuel] If this unit's Speed is faster than the target's, deal +50% damage\n<style="highlight">[WinDuel] Inflict 1 [ConcussionYisang] against the main target</style>
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Końcowa +1\n[WhenUse] Nakłada w następnej turze 1 [BattlefieldHorse] na wszystkich pozostałych sojuszników (raz na turę)\n[WhenUse] Zyskuje 3 [LegStrengthHorseYisang]\n[WhenUse] Moc Monet +1 za każde 5 sumy [Burst] i [Vibration] celu (maks. 2)\n[WinDuel] Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +50% obrażeń\n<style="highlight">[WinDuel] Nakłada 1 [ConcussionYisang] na główny cel</style>
538. [Obrona (ulepszenia 1,4) — nazwa] 돌진 전, 가다듬겠소.
   źródło: Skills_personality-01.json :: dataList[id=1011404].levelList[level=1].name ; dataList[id=1011404].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 50 znaków
   EN: Preparation Afore the Charge.
   PL: Przed szarżą — doprowadzę do ładu.
539. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [LegStrengthHorseYisang] 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [LegStrengthHorseYisang]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】
   EN: [CanDuelGuard] \n[StartBattle] Gain 3 [LegStrengthHorseYisang] next turn
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 3 [LegStrengthHorseYisang] w następnej turze
540. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011404].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011404].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [LegStrengthHorseYisang] 3 얻음\n<style="highlight">[EndBattle] 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 1개 제거 (턴 당 1회)</style>
   źródło: Skills_personality-01.json :: dataList[id=1011404].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [LegStrengthHorseYisang], [EndBattle]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CanDuelGuard]\n[StartBattle] Gain 3 [LegStrengthHorseYisang] next turn\n<style="highlight">[EndBattle] Remove 1 random removable negative effect applied to self (once per turn)</style>
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 3 [LegStrengthHorseYisang] w następnej turze\n<style="highlight">[EndBattle] Usuwa 1 losowy usuwalny negatywny efekt nałożony na tę jednostkę (raz na turę)</style>
542. [Pasywka bojowa (od ulepszenia 1) — nazwa] 구마지심 [狗馬之心]
   źródło: Passives.json :: dataList[id=1011402].name
   limit: do 50 znaków
   EN: The Steed's Houndlike Loyalty [狗馬之心]
   PL: Wierność Psa i Konia [狗馬之心]
543. [Pasywka bojowa (od ulepszenia 1) — opis] 홍원 군주 홍루와 [HeishouCombo] 발동 시, 홍원 군주 홍루가 [HeishouComboCountHonglu]으로 아래 효과 얻음\n- 기본 스킬의 마지막 코인 적중 시, [VibrationExplosion] 1회 (턴 당 1회)\n\n전투 인원에 가주 후보 이스마엘이 있다면, 아래 효과 적용\n- 가주 후보 이스마엘이 스킬 효과로 [Burst] 또는 [Burst] 횟수 부여 시 [Breath] 위력 3 얻음 (턴 당 2회, E.G.O 스킬에는 적용되지 않음)\n- 턴 시작 시 가주 후보 이스마엘에게 [Enhancement] 1 부여. 이스마엘의 [Breath] 위력이 10 이상이면, [Enhancement] 1 추가 부여\n- ‘흑풍마각월참’ 사용 후 가주 후보 이스마엘이 적춘 스킬로 원호 공격함 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1011402].desc
   limit: do 1000 znaków
   tokeny: zachowaj dokładnie: \n, [HeishouCombo], [HeishouComboCountHonglu], [VibrationExplosion], [Burst], [Breath], [Enhancement], [TabExplain]
   znaczenie tagów: [HeishouCombo] = 존명 / Exalted Command; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: When activating [HeishouCombo], The Lord of Hongyuan Hong Lu gains the following effect as the [HeishouComboCountHonglu] effect:\n- On Hit using a Base Skill's Final Coin, trigger [VibrationExplosion] once (once per turn)\n\nIf Family Hierarch Candidate Ishmael is on the field, activate the following:\n- When Family Hierarch Candidate Ishmael inflicts [Burst] or [Burst] Count using its Skill effects, that unit gains 3 [Breath] Potency (2 times per turn; excluding E.G.O Skills)\n- Turn Start: Apply 1 [Enhancement] on Family Hierarch Candidate Ishmael. If Ishmael has 10+ [Breath] Potency, apply 1 more [Enhancement]\n- After this unit uses the Skill "Obsidian Stormrider's Crescent Decapitator", Family Hierarch Candidate Ishmael uses "Crimson Spring" as Assist Attack[TabExplain] (once per turn)
   PL: [HeishouCombo]\nGdy Władca Hongyuan Hong Lu aktywuje [HeishouCombo], zyskuje następujący efekt jako [HeishouComboCountHonglu]:\n- Przy trafieniu ostatnią monetą Umiejętności bazowej wywołuje raz [VibrationExplosion] (raz na turę)\n\nJeżeli Kandydatka na Głowę Rodu Ishmael jest na polu walki, aktywują się następujące efekty:\n- Gdy Kandydatka na Głowę Rodu Ishmael nakłada [Burst] lub Licznika [Burst] efektami Umiejętności, zyskuje 3 Mocy [Breath] (2 razy na turę; nie dotyczy Umiejętności E.G.O)\n- Na początku tury nakłada 1 [Enhancement] na Kandydatkę na Głowę Rodu Ishmael. Jeżeli Ishmael ma 10+ Mocy [Breath], nakłada dodatkowe 1 [Enhancement]\n- Po użyciu Umiejętności „Sierpowe Ścięcie Obsydianowego Jeźdźca Burzy” Kandydatka na Głowę Rodu Ishmael atakuje „Szkarłatną Wiosną” jako Atak Wsparcia[TabExplain] (raz na turę)
544. [Pasywka bojowa (od ulepszenia 1) — nazwa] 필두선봉
   źródło: Passives.json :: dataList[id=1011403].name
   limit: do 40 znaków
   EN: Adept Vanguard
   PL: Adept Awangardy
545. [Pasywka bojowa (od ulepszenia 1) — opis] [BattlefieldHorse] 부여 시 이번 턴과 다음 턴에 [AttackUp] 3 얻음\n(해당 패시브로 이미 [AttackUp]를 얻었으면, 다음 턴에만 얻음)
   źródło: Passives.json :: dataList[id=1011403].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [BattlefieldHorse], [AttackUp]
   znaczenie tagów: [BattlefieldHorse] = 호령 / Commanding Cry; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: When applying [BattlefieldHorse], gain 3 [AttackUp] this turn and next turn\n(If this unit has already gained [AttackUp] from this passive, gain it only for the next turn)
   PL: Nakładając [BattlefieldHorse], zyskuje 3 [AttackUp] w tej i następnej turze\n(Jeżeli ten pasyw już dał tej jednostce [AttackUp], zyskuje go tylko w następnej turze)
546. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 흑풍마각 [黑風馬脚]
   źródło: Passives.json :: dataList[id=1011401].name
   limit: do 40 znaków
   EN: Obsidian Stormrider [黑風馬脚]
   PL: Obsydianowy Jeździec Burzy [黑風馬脚]
547. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 아래의 조건 만족 시 [BreakthroughHorse] 1 얻음\n- 공격 시작 시 대상보다 속도가 2 이상 높을 때\n- 자신의 스킬로 [VibrationExplosion] 효과 2회 발동시 (E.G.O 스킬 포함)\n- [LegStrengthHorseYisang]를 보유 중인 상태로 합 승리 시\n※ [BreakthroughHorse]는 턴 당 최대 3까지 얻을 수 있으며, ‘흑풍마각월참’ 스킬로는 얻을 수 없음
   źródło: Passives.json :: dataList[id=1011401].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [BreakthroughHorse], [VibrationExplosion], [LegStrengthHorseYisang]
   znaczenie tagów: [BreakthroughHorse] = 적진 주파 / Linebreaker; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】
   EN: Gain 1 [BreakthroughHorse] when meeting one of the following conditions:\n- Attack Start: When this unit's Speed is faster than the target's by 2 or more\n- When this unit triggers [VibrationExplosion] twice using its Skills (including E.G.O Skills)\n- When this unit wins a Clash while having [LegStrengthHorseYisang]\n※ Only 3 [BreakthroughHorse] can be gained per turn; cannot gain [BreakthroughHorse] using the Skill "Obsidian Stormrider's Crescent Decapitator"
   PL: Zyskuje 1 [BreakthroughHorse] przy spełnieniu jednego z warunków:\n- Na początku ataku, gdy Szybkość tej jednostki jest większa od celu o 2 lub więcej\n- Gdy ta jednostka wywoła [VibrationExplosion] dwukrotnie swoimi Umiejętnościami (w tym Umiejętnościami E.G.O)\n- Gdy ta jednostka wygra Starcie posiadając [LegStrengthHorseYisang]\n※ Maks. 3 [BreakthroughHorse] na turę; nie można zdobyć ich Umiejętnością „Sierpowe Ścięcie Obsydianowego Jeźdźca Burzy”
548. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Glut.) — nazwa] 흑풍마각 [黑風馬脚]
   źródło: Passives.json :: dataList[id=1011411].name
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Glut.) — opis] 아래의 조건 만족 시 [BreakthroughHorse] 1 얻음\n- 공격 시작 시 대상보다 속도가 2 이상 높을 때\n- 자신의 스킬로 [VibrationExplosion] 효과 2회 발동시 (E.G.O 스킬 포함)\n- [LegStrengthHorseYisang]를 보유 중인 상태로 합 승리 시\n※ [BreakthroughHorse]는 턴 당 최대 3까지 얻을 수 있으며, ‘흑풍마각월참’ 스킬로는 얻을 수 없음\n\n<style="highlight">자신에게 보호막이 있을 때, 방어 레벨이 (보호막 수치 / 10)만큼 증가 (최대 5, 소수점 버림)</style>
   źródło: Passives.json :: dataList[id=1011411].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BreakthroughHorse], [VibrationExplosion], [LegStrengthHorseYisang]
   znaczenie tagów: [BreakthroughHorse] = 적진 주파 / Linebreaker; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [LegStrengthHorseYisang] = 각력【오】 / Strider【Wu】
   EN: Gain 1 [BreakthroughHorse] when meeting one of the following conditions:\n- Attack Start: When this unit's Speed is faster than the target's by 2 or more\n- When this unit triggers [VibrationExplosion] twice using its Skills (including E.G.O Skills)\n- When this unit wins a Clash while having [LegStrengthHorseYisang]\n※ Only 3 [BreakthroughHorse] can be gained per turn; cannot gain [BreakthroughHorse] using the Skill "Obsidian Stormrider's Crescent Decapitator"\n\n<style="highlight">When this unit has Shield, gain (Shield HP / 10) Defense Level (max 5; rounded down)</style>
   PL: Zyskuje 1 [BreakthroughHorse] przy spełnieniu jednego z warunków:\n- Na początku ataku, gdy Szybkość tej jednostki jest większa od celu o 2 lub więcej\n- Gdy ta jednostka wywoła [VibrationExplosion] dwukrotnie swoimi Umiejętnościami (w tym Umiejętnościami E.G.O)\n- Gdy ta jednostka wygra Starcie posiadając [LegStrengthHorseYisang]\n※ Maks. 3 [BreakthroughHorse] na turę; nie można zdobyć ich Umiejętnością „Sierpowe Ścięcie Obsydianowego Jeźdźca Burzy”\n\n<style="highlight">Podczas posiadania Tarczy Poziom Obrony tej jednostki rośnie o (wartość Tarczy / 10) (maks. 5; zaokrąglone w dół)</style>
550. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 검은 갑각이 살을 째고 돋아 날 지키리
   źródło: Passives.json :: dataList[id=1011421].name
   limit: do 70 znaków
   EN: Obsidian Exoskeleton Shall Rend and Protect My Flesh
   PL: Czarne Pancerze Rozdzierają Ciało, by Je Chronić
551. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 최대 체력이 가장 높은 아군 1명에게 아래 효과 적용\n- 전투 시작 시 방어 레벨이 (해당 캐릭터의 이전 턴과 이번 턴 속도 차이 x 2) 만큼 증가 (최대 5. 이전 턴에 전투 인원이 아니었다면, 해당 캐릭터의 기본 속도 최솟값으로 계산)\n- 전투 시작 시 현재 체력이 최대 체력의 50% 미만이고, 이전 턴과 이번 턴 속도 차이가 3 이상이면, 체력 50 회복 (전투 당 1회)
   źródło: Passives.json :: dataList[id=1011421].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply the following effect to 1 ally that has the highest max HP\n- Combat Start: Gain (affected unit's Speed difference between this turn and last turn x 2) Defense Level (max 5; if the affected unit was not an Active participant last turn, use its minimum base Speed value to calculate)\n- Combat Start: If the affected unit is at less than 50% HP, and if the Speed difference between this turn and last turn is 3 or higher, heal 50 HP (once per Encounter)
   PL: Nakłada następujący efekt na 1 sojusznika z najwyższym Maks. HP\n- Na początku walki Poziom Obrony rośnie o (różnica Szybkości tej jednostki między tą a poprzednią turą × 2) (maks. 5; jeżeli w poprzedniej turze jednostka nie brała udziału w walce, liczy się jej minimalna bazowa Szybkość)\n- Na początku walki, jeżeli obecne HP jednostki wynosi mniej niż 50% Maks. HP, a różnica Szybkości między tą a poprzednią turą wynosi 3 lub więcej, odzyskuje 50 HP (raz na spotkanie)

## [000] The House of Spiders: The Index Nursefather — Yi Sang — 거미집 검지 아비
- ID Tożsamości: `10115` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 66 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Sinking, Poise

552. [Karta Tożsamości — tytuł] 거미집\n검지 아비
   źródło: Personalities.json :: dataList[id=10115].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders:\nThe Index Nursefather
   PL: Dom Pajęczyn:\nOjciec Wskazującego
553. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10115].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10115].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Karta Tożsamości — opis] 이상의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10115].desc
   limit: do 120 znaków
   EN: Yi Sang's 15th Identity
   PL: Piętnasta Tożsamość Yi Sanga
556. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 얼어붙은 피를 삼백삼십 휘감아
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=1].name ; dataList[id=1011501].levelList[level=2].name ; dataList[id=1011501].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 70 znaków
   EN: "Enwrap 330 Times in Long Swaths of Frozen Blood"
   PL: „Owiń Trzysta Trzydzieści Razy Wstęgami Zamarzniętej Krwi”
557. [Umiejętność 1 (×3) (ulepszenie 1) — opis] (75-[KarmaOfIndexAlly]/2)% 확률로 타격 무기가 등장\n- 타격 무기 코인 피해량 +10%\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +15%\n[WhenUse] ([UnlockBuff_Base] 단계-1)만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [WhenUse], [UnlockBuff_Base], [SuperCoin], [Breath]
   znaczenie tagów: [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Breath] = 호흡 / Poise
   EN: (75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Blunt weapon\n- Coins using Blunt weapons deal +10% damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +15% damage\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage - 1) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain +1 [Breath] Count
   PL: (75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Obuchowej\n- Monety broni Obuchowej zadają +10% obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], zadaje +15% obrażeń\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi ([UnlockBuff_Base] stopień - 1), zaczynając od ostatniej\n[WhenUse] Zyskuje +1 Licznika [Breath]
558. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 1 [Sinking]
560. [Umiejętność 1 (×3) (ulepszenie 2) — opis] (75-[KarmaOfIndexAlly]/2)% 확률로 타격 무기가 등장\n- 타격 무기 코인 피해량 +10%\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +15%\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] ([UnlockBuff_Base] 단계-1)만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=2].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [SuperCoin]
   znaczenie tagów: [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: (75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Blunt weapon\n- Coins using Blunt weapons deal +10% damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +15% damage\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage - 1) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count
   PL: (75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Obuchowej\n- Monety broni Obuchowej zadają +10% obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], zadaje +15% obrażeń\n<style="highlight">Przy 6+ sumy [Breath] tej jednostki i [Sinking] celu, Moc Monet +1</style>\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi ([UnlockBuff_Base] stopień - 1), zaczynając od ostatniej\n[WhenUse] Zyskuje +<style="highlight">2</style> Licznika [Breath]
561. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Sinking]<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 1 [Sinking]<style="highlight"></style>
563. [Umiejętność 1 (×3) (ulepszenie 4) — opis] (75-[KarmaOfIndexAlly]/2)% 확률로 타격 무기가 등장\n- 타격 무기 코인 피해량 <style="highlight">+15%</style>\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">합 위력 +1</style>, 피해량 <style="highlight">+20%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] ([UnlockBuff_Base] 단계-1)만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [SuperCoin]
   znaczenie tagów: [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: (75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Blunt weapon\n- Coins using Blunt weapons deal <style="highlight">+15%</style> damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Clash Power +1</style> and deal <style="highlight">+20%</style> damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage - 1) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain + 2 [Breath] Count
   PL: (75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Obuchowej\n- Monety broni Obuchowej zadają <style="highlight">+15%</style> obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Starcia +1</style> i zadaje <style="highlight">+20%</style> obrażeń\n<style="highlight">Moc Monet +1 za każde 6 sumy [Breath] tej jednostki i [Sinking] celu (maks. 2)</style>\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi ([UnlockBuff_Base] stopień - 1), zaczynając od ostatniej\n[WhenUse] Zyskuje + 2 Licznika [Breath]
564. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict <style="highlight">2</style> [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada <style="highlight">2</style> [Sinking]
565. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 소리 없이 손뼉 쳐 즐기고, 목소리 없이 슬피 꿰뚫어
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=1].name ; dataList[id=1011502].levelList[level=2].name ; dataList[id=1011502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 80 znaków
   EN: "Revel with Soundless Applause, Impale in Voiceless Sorrow"
   PL: „Baw się bezgłośnym klaśnięciem, przeszyj bezszelestnym żalem”
566. [Umiejętność 2 (×2) (ulepszenie 1) — opis] (75-[KarmaOfIndexAlly]/2)% 확률로 관통 무기가 등장\n- 관통 무기 코인 피해량 +10%\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 합 위력 +1\n[WhenUse] [UnlockBuff_Base] 단계만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [WhenUse], [UnlockBuff_Base], [SuperCoin], [Breath]
   znaczenie tagów: [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Breath] = 호흡 / Poise
   EN: (75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Pierce weapon\n- Coins using Pierce weapons deal +10% damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], Clash Power +1\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain 3 [Breath]
   PL: (75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Kłutej\n- Monety broni Kłutej zadają +10% obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], Moc Starcia +1\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi [UnlockBuff_Base] stopień, zaczynając od ostatniej\n[WhenUse] Zyskuje 3 [Breath]
567. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
568. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada +1 Licznika [Sinking]
570. [Umiejętność 2 (×2) (ulepszenie 2) — opis] (75-[KarmaOfIndexAlly]/2)% 확률로 관통 무기가 등장\n- 관통 무기 코인 피해량 +10%\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 합 위력 +1\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [UnlockBuff_Base] 단계만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=2].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [SuperCoin]
   znaczenie tagów: [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: (75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Pierce weapon\n- Coins using Pierce weapons deal +10% damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], Clash Power +1\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain 3 [Breath]
   PL: (75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Kłutej\n- Monety broni Kłutej zadają +10% obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], Moc Starcia +1\n<style="highlight">Przy 6+ sumy [Breath] tej jednostki i [Sinking] celu, Moc Monet +1</style>\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi [UnlockBuff_Base] stopień, zaczynając od ostatniej\n[WhenUse] Zyskuje 3 [Breath]
571. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]<style="highlight"></style>
572. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1011502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Sinking] Count<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada +1 Licznika [Sinking]<style="highlight"></style>
574. [Umiejętność 2 (×2) (ulepszenie 4) — opis] (75-[KarmaOfIndexAlly]/2)% 확률로 관통 무기가 등장\n- 관통 무기 코인 피해량 <style="highlight">+15%</style>\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">최종 위력 +1</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [UnlockBuff_Base] 단계만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=4].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [SuperCoin]
   znaczenie tagów: [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: (75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Pierce weapon\n- Coins using Pierce weapons deal <style="highlight">+15%</style> damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Final Power +1</style>\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain 3 [Breath]
   PL: (75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Kłutej\n- Monety broni Kłutej zadają <style="highlight">+15%</style> obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Końcowa +1</style>\n<style="highlight">Moc Monet +1 za każde 6 sumy [Breath] tej jednostki i [Sinking] celu (maks. 2)</style>\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi [UnlockBuff_Base] stopień, zaczynając od ostatniej\n[WhenUse] Zyskuje 3 [Breath]
575. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Sinking]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Sinking]
576. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +<style="highlight">2</style> [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +<style="highlight">2</style> Licznika [Breath]
577. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 날 세워 칼을 웃거라, 낙엽 향 나듯 폭포를 울거라
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].name ; dataList[id=1011503].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 110 znaków
   EN: "Raise and Laugh the Blade, Cry the Waterfall Like the Scent of Fallen Leaves"
   PL: „Podnieś Ostrze i Śmiej się, Płacz Wodospadem Jak Zapach Liści”
578. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 턴 시작 시 [StackYisangSpecialSkill]가 9면, ‘Furioso-Replica’로 변경됨 (턴당 1회)\n- 가장 왼쪽 슬롯의 아래 스킬 우선 변경\n- [BeforeUse] [StackYisangSpecialSkill]가 9 미만이면 스킬 3으로 발동됨\n(75-[KarmaOfIndexAlly]/2)% 확률로 참격 무기가 등장\n- 참격 무기 코인 피해량 +12.5%\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [UnlockBuff_Base] 단계만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: \n, [StackYisangSpecialSkill], [BeforeUse], [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [SuperCoin]
   znaczenie tagów: [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]; [BeforeUse] = [사용전] / [Before Use]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock …
   EN: Turn Start: At 9 [StackYisangSpecialSkill], replace this Skill with "Furioso-Replica" (once per turn)\n- Prioritizes the Skill on the leftmost Slot's bottom row on the Dashboard\n- [BeforeUse] At less than 9 [StackYisangSpecialSkill], use as Skill 3\n(75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Slash weapon\n- Coins using Slash weapons deal +12.5% damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\nAt 6+ ([Breath] on self + [Sinking] on target), Coin Power +1\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain +3 [Breath] Count
   PL: Na początku tury przy 9 [StackYisangSpecialSkill] zamienia tę Umiejętność w „Furioso-Replica” (raz na turę)\n- Priorytetowo zamienia Umiejętność z dolnego rzędu skrajnie lewego slotu\n- [BeforeUse] Przy mniej niż 9 [StackYisangSpecialSkill] aktywuje się jako Umiejętność 3\n(75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Siecznej\n- Monety broni Siecznej zadają +12,5% obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\nPrzy 6+ sumy [Breath] tej jednostki i [Sinking] celu, Moc Monet +1\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi [UnlockBuff_Base] stopień, zaczynając od ostatniej\n[WhenUse] Zyskuje +3 Licznika [Breath]
579. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [UnlockBuff_Base] 단계 1당 피해량 +10% (최대 30%)
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnlockBuff_Base]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock
   EN: Deal +10% damage for every [UnlockBuff_Base] stage (max 30%)
   PL: Zadaje +10% obrażeń za każdy stopień [UnlockBuff_Base] (maks. 30%)
582. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +1 [Breath] Count
   PL: [CriticalOnSucceedAttack] Zyskuje +1 Licznika [Breath]
583. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada +2 Licznika [Sinking]
584. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 턴 시작 시 [StackYisangSpecialSkill]가 9면, ‘Furioso-Replica’로 변경됨 (턴당 1회)\n- 가장 왼쪽 슬롯의 아래 스킬 우선 변경\n- [BeforeUse] [StackYisangSpecialSkill]가 9 미만이면 스킬 3으로 발동됨\n(75-[KarmaOfIndexAlly]/2)% 확률로 참격 무기가 등장\n- 참격 무기 코인 피해량 <style="highlight">+25%</style>\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 <style="highlight">+20%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] ([UnlockBuff_Base] 단계<style="highlight">+1</style>)만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n<style="highlight">- [UnlockBuff_Base] 단계만큼 [Breath] 추가로 얻음</style>
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=4].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StackYisangSpecialSkill], [BeforeUse], [KarmaOfIndexAlly], [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [SuperCoin]
   znaczenie tagów: [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]; [BeforeUse] = [사용전] / [Before Use]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock …
   EN: Turn Start: At 9 [StackYisangSpecialSkill], replace this Skill with "Furioso-Replica" (once per turn)\n- Prioritizes the Skill on the leftmost Slot's bottom row on the Dashboard\n- [BeforeUse] At less than 9 [StackYisangSpecialSkill], use as Skill 3\n(75 - ([KarmaOfIndexAlly] / 2))% chance to produce a Slash weapon\n- Coins using Slash weapons deal <style="highlight">+25%</style> damage\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal <style="highlight">+20%</style> damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Convert Coins equal to ([UnlockBuff_Base] stage <style="highlight">+ 1</style>) into [SuperCoin]s, beginning with the final Coin\n[WhenUse] Gain +3 [Breath] Count\n<style="highlight">- Gain additional [Breath] equal to ([UnlockBuff_Base] stage)</style>
   PL: Na początku tury przy 9 [StackYisangSpecialSkill] zamienia tę Umiejętność w „Furioso-Replica” (raz na turę)\n- Priorytetowo zamienia Umiejętność z dolnego rzędu skrajnie lewego slotu\n- [BeforeUse] Przy mniej niż 9 [StackYisangSpecialSkill] aktywuje się jako Umiejętność 3\n(75-[KarmaOfIndexAlly]/2)% szans na pojawienie się broni Siecznej\n- Monety broni Siecznej zadają <style="highlight">+25%</style> obrażeń\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], zadaje <style="highlight">+20%</style> obrażeń\n<style="highlight">Moc Monet +1 za każde 6 sumy [Breath] tej jednostki i [Sinking] celu (maks. 2)</style>\n[WhenUse] Zamienia w [SuperCoin] tyle monet, ile wynosi ([UnlockBuff_Base] stopień <style="highlight">+ 1</style>), zaczynając od ostatniej\n[WhenUse] Zyskuje +3 Licznika [Breath]\n<style="highlight">- Zyskuje dodatkowe [Breath] równe stopniowi [UnlockBuff_Base]</style>
585. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">3</style> 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain <style="highlight">3</style> [Breath]
   PL: [OnSucceedAttack] Zyskuje <style="highlight">3</style> [Breath]
586. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [UnlockBuff_Base] 단계 1당 피해량 <style="highlight">+20%</style> (최대 <style="highlight">60%</style>)
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnlockBuff_Base]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock
   EN: Deal <style="highlight">+20%</style> damage for every [UnlockBuff_Base] stage (max <style="highlight">60%</style>)
   PL: Zadaje <style="highlight">+20%</style> obrażeń za każdy 1 stopień [UnlockBuff_Base] (maks. <style="highlight">60%</style>)
588. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zyskuje +1 Licznika [Breath]<style="highlight"></style>
589. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011503].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict <style="highlight">+3</style> [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada <style="highlight">+3</style> Licznika [Sinking]
590. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] Furioso-Replica
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=3].name ; dataList[id=1011505].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 9 (+3)
   limit: do 40 znaków
   EN: Furioso-Replica
   PL: Furioso-Replica
591. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WideAreaRampage]\n조작 슬롯에 1개만 배치 가능\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n코인 위력이 변하지 않는 대신, 코인 위력이 최종적으로 증가할 때 수치 1당 최종 위력 +5 (이 스킬은 [Paralysis]의 영향을 받지 않음)\n자신의 [Breath]과 메인 타겟의 [Sinking]의 합이 6 이상이면, 최종 위력 +1\n[StartBattle]\n- 모든 코인이 [SuperCoin]으로 변경됨\n- 이 스킬 적중 시마다 [Sinking] 1 부여 또는 [Breath] 1 얻음\n- 이번 턴 동안 [StackYisangSpecialSkill]를 얻지 않음\n[WhenUse]\n- 합 위력 +3\n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n[EndSkill]\n- 적중한 모든 대상에게 다음 턴에 [Combustion] 5, [Binding] 3, [Vulnerable] 3 부여\n- [StackYisangSpecialSkill] 전부 소모
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=3].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [IndexPrescriptTargetMarkToEnemy], [Paralysis], [Breath], [Sinking], [StartBattle], [SuperCoin], [StackYisangSpecialSkill], [WhenUse], [EndSkill], [Combustion], [Binding], [Vulnerable]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Paralysis] = 마비 / Paralyze; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes] …
   EN: [WideAreaRampage]\nOnly 1 copy of this Skill can exist on the Dashboard\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\nThis Skill's Coin Power does not change; instead, for every net Coin Power increase, Final Power +5 (this Skill is not affected by [Paralysis])\nAt 6+ ([Breath] on self + [Sinking] on main target), Final Power +1\n[StartBattle]\n- Convert all Coins on this Skill to [SuperCoin]s\n- Inflict 1 [Sinking] or gain 1 [Breath] with every hit of this Skill\n- Does not gain [StackYisangSpecialSkill] for this turn\n[WhenUse]\n- Clash Power +3\n- Gain 3 [Breath] and +3 [Breath] Count\n[EndSkill]\n- Inflict 5 [Combustion], 3 [Binding], and 3 [Vulnerable] next turn to all targets this unit hit\n- Consume all [StackYisangSpecialSkill]
   PL: [WideAreaRampage]\nMoże znaleźć się tylko 1 kopia tej Umiejętności na panelu\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\nMoc Monet tej Umiejętności się nie zmienia; zamiast tego za każdy punkt ostatecznego wzrostu Mocy Monet zyskuje Moc Końcową +5 (ta Umiejętność nie podlega [Paralysis])\nPrzy 6+ sumy [Breath] tej jednostki i [Sinking] głównego celu, Moc Końcowa +1\n[StartBattle]\n- Wszystkie monety tej Umiejętności zmieniają się w [SuperCoin]\n- Przy każdym trafieniu tej Umiejętności nakłada 1 [Sinking] lub zyskuje 1 [Breath]\n- Nie zyskuje [StackYisangSpecialSkill] w tej turze\n[WhenUse]\n- Moc Starcia +3\n- Zyskuje 3 [Breath] i +3 Licznika [Breath]\n[EndSkill]\n- Nakłada w następnej turze 5 [Combustion], 3 [Binding] i 3 [Vulnerable] na wszystkie cele, które ta jednostka trafiła\n- Zużywa całe [StackYisangSpecialSkill]
592. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 9, efekt 1 — opis] 이 코인의 무기는 낫으로 확정
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=3].coinlist[#8].coindescs[#0].desc
   limit: do 120 znaków
   EN: Weapon assigned to this Coin is fixed as Scythe
   PL: Broń przypisana do tej monety jest na stałe Kosą
593. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 9, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=3].coinlist[#8].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada +3 Licznika Zatonięcia
594. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WideAreaRampage]\n조작 슬롯에 1개만 배치 가능\n이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n코인 위력이 변하지 않는 대신, 코인 위력이 최종적으로 증가할 때 수치 1당 최종 위력 +5, <style="highlight">피해량 +25%</style> (이 스킬은 [Paralysis]의 영향을 받지 않음)\n자신의 [Breath]과 메인 타겟의 [Sinking]의 합 <style="highlight">6당, 최종 위력 +1 (최대 2)</style>\n[StartBattle]\n- 모든 코인이 [SuperCoin]으로 변경됨\n- 이 스킬 적중 시마다 [Sinking] 1 부여 또는 [Breath] 1 얻음\n- 이번 턴 동안 [StackYisangSpecialSkill]를 얻지 않음\n[WhenUse]\n- 합 위력 +3\n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n[EndSkill]\n- 적중한 모든 대상에게 다음 턴에 [Combustion] 5, [Binding] 3, [Vulnerable] 3 부여\n- [StackYisangSpecialSkill] 전부 소모
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=4].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WideAreaRampage], [IndexPrescriptTargetMarkToEnemy], [Paralysis], [Breath], [Sinking], [StartBattle], [SuperCoin], [StackYisangSpecialSkill], [WhenUse], [EndSkill], [Combustion], [Binding], [Vulnerable]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Paralysis] = 마비 / Paralyze; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes] …
   EN: [WideAreaRampage]\nOnly 1 copy of this Skill can exist on the Dashboard\nIf this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\nThis Skill's Coin Power does not change; instead, for every net Coin Power increase, Final Power +5 <style="highlight">and deal +25% damage</style> (this Skill is not affected by [Paralysis])\n<style="highlight">Final Power +1 for every 6 ([Breath] on self + [Sinking] on main target) (max 2)</style>\n[StartBattle]\n- Convert all Coins on this Skill to [SuperCoin]s\n- Inflict 1 [Sinking] or gain 1 [Breath] with every hit of this Skill\n- Does not gain [StackYisangSpecialSkill] for this turn\n[WhenUse]\n- Clash Power +3\n- Gain 3 [Breath] and +3 [Breath] Count\n[EndSkill]\n- Inflict 5 [Combustion], 3 [Binding], and 3 [Vulnerable] next turn to all targets this unit hit\n- Consume all [StackYisangSpecialSkill]
   PL: [WideAreaRampage]\nMoże znaleźć się tylko 1 kopia tej Umiejętności na panelu\nJeżeli ta Umiejętność jest oznaczona [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\nMoc Monet tej Umiejętności się nie zmienia; zamiast tego za każdy punkt ostatecznego wzrostu Mocy Monet zyskuje Moc Końcową +5 <style="highlight">i zadaje +25% obrażeń</style> (ta Umiejętność nie podlega [Paralysis])\n<style="highlight">Moc Końcowa +1 za każde 6 sumy [Breath] tej jednostki i [Sinking] głównego celu (maks. 2)</style>\n[StartBattle]\n- Wszystkie monety tej Umiejętności zmieniają się w [SuperCoin]\n- Przy każdym trafieniu tej Umiejętności nakłada 1 [Sinking] lub zyskuje 1 [Breath]\n- Nie zyskuje [StackYisangSpecialSkill] w tej turze\n[WhenUse]\n- Moc Starcia +3\n- Zyskuje 3 [Breath] i +3 Licznika [Breath]\n[EndSkill]\n- Nakłada w następnej turze 5 [Combustion], 3 [Binding] i 3 [Vulnerable] na wszystkie cele, które ta jednostka trafiła\n- Zużywa całe [StackYisangSpecialSkill]
595. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 9, efekt 1 — opis] 이 코인의 무기는 낫으로 확정<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=4].coinlist[#8].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Weapon assigned to this Coin is fixed as Scythe<style="highlight"></style>
   PL: Broń przypisana do tej monety jest na stałe Kosą<style="highlight"></style>
596. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 9, efekt 2 — opis] <style="highlight">크리티컬 피해량 +90%</style>
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=4].coinlist[#8].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Deal +90% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +90% obrażeń Krytycznych</style>
597. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 9, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 침잠 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011505].levelList[level=4].coinlist[#8].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada +3 Licznika Zatonięcia<style="highlight"></style>
598. [Obrona (ulepszenia 1,4) — nazwa] 예측할 수 없는 변덕으로
   źródło: Skills_personality-01.json :: dataList[id=1011504].levelList[level=1].name ; dataList[id=1011504].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: By Unpredictable Whim
   PL: Z Nieprzewidywalnego Kaprysu
599. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신의 [Breath] 횟수 2 증가 (턴당 1회)\n[OnSucceedEvade] [Breath] 1 얻음 (턴당 2회)\n[EndBattle] [UnlockBuffAlly_2] 미만이면, 다음 효과 발동 (전투당 1회)\n- [UnlockBuffAlly_2] 얻음\n- 6 미만인 [BlessingOfIndexPrescriptAlly]가 6으로 변경됨\n- 증가한 [BlessingOfIndexPrescriptAlly] 1당 다음 턴 시작 시 [KarmaOfIndexAlly] 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011504].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Breath], [OnSucceedEvade], [EndBattle], [UnlockBuffAlly_2], [BlessingOfIndexPrescriptAlly], [KarmaOfIndexAlly]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [EndBattle] = [턴 종료 시] / [Turn End]; [UnlockBuffAlly_2] = 해금 - II / Unlock - II; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence
   EN: [StartBattle] Gain +2 [Breath] Count (once per turn)\n[OnSucceedEvade] Gain 1 [Breath] (2 times per turn)\n[EndBattle] At below [UnlockBuffAlly_2], activate the following effects (once per Encounter):\n- Gain [UnlockBuffAlly_2]\n- If [BlessingOfIndexPrescriptAlly] Stack is less than 6, raise the Stack to 6\n- Gain 5 [KarmaOfIndexAlly] at the start of the next turn for every [BlessingOfIndexPrescriptAlly] gained via the effect above
   PL: [StartBattle] Zyskuje +2 Licznika [Breath] (raz na turę)\n[OnSucceedEvade] Zyskuje 1 [Breath] (2 razy na turę)\n[EndBattle] Przy mniej niż [UnlockBuffAlly_2] aktywuje następujące efekty (raz na spotkanie):\n- Zyskuje [UnlockBuffAlly_2]\n- Jeżeli stos [BlessingOfIndexPrescriptAlly] jest niższy niż 6, podnosi go do 6\n- Za każdy [BlessingOfIndexPrescriptAlly] zdobyty tym efektem zyskuje 5 [KarmaOfIndexAlly] na początku następnej tury
600. [Obrona (ulepszenie 4) — opis] <style="highlight">[UnlockBuffAlly_3]이면, 코인 위력 +2</style>\n[StartBattle] 자신의 [Breath] 횟수 2 증가 (턴당 1회)\n[OnSucceedEvade] [Breath] <style="highlight">2</style> 얻음 (턴당 2회)\n[EndBattle] [UnlockBuffAlly_2] 미만이면, 다음 효과 발동 (전투당 1회)\n- [UnlockBuffAlly_2] 얻음\n- 6 미만인 [BlessingOfIndexPrescriptAlly]가 6으로 변경됨\n- 증가한 [BlessingOfIndexPrescriptAlly] 1당 다음 턴 시작 시 [KarmaOfIndexAlly] 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011504].levelList[level=4].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [UnlockBuffAlly_3], [StartBattle], [Breath], [OnSucceedEvade], [EndBattle], [UnlockBuffAlly_2], [BlessingOfIndexPrescriptAlly], [KarmaOfIndexAlly]
   znaczenie tagów: [UnlockBuffAlly_3] = 해금 - III / Unlock - III; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [EndBattle] = [턴 종료 시] / [Turn End]; [UnlockBuffAlly_2] = 해금 - II / Unlock - II; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence
   EN: <style="highlight">At [UnlockBuffAlly_3], Coin Power +2</style>\n[StartBattle] Gain +2 [Breath] Count (once per turn)\n[OnSucceedEvade] Gain <style="highlight">2</style> [Breath] (2 times per turn)\n[EndBattle] At below [UnlockBuffAlly_2], activate the following effects (once per Encounter):\n- Gain [UnlockBuffAlly_2]\n- If [BlessingOfIndexPrescriptAlly] Stack is less than 6, raise the Stack to 6\n- Gain 5 [KarmaOfIndexAlly] at the start of the next turn for every [BlessingOfIndexPrescriptAlly] gained via the effect above
   PL: <style="highlight">Przy [UnlockBuffAlly_3] Moc Monet +2</style>\n[StartBattle] Zyskuje +2 Licznika [Breath] (raz na turę)\n[OnSucceedEvade] Zyskuje <style="highlight">2</style> [Breath] (2 razy na turę)\n[EndBattle] Przy mniej niż [UnlockBuffAlly_2] aktywuje następujące efekty (raz na spotkanie):\n- Zyskuje [UnlockBuffAlly_2]\n- Jeżeli stos [BlessingOfIndexPrescriptAlly] jest niższy niż 6, podnosi go do 6\n- Za każdy [BlessingOfIndexPrescriptAlly] zdobyty tym efektem zyskuje 5 [KarmaOfIndexAlly] na początku następnej tury
601. [Pasywka bojowa (od ulepszenia 1) — nazwa] 단말기로 전해진 지령
   źródło: Passives.json :: dataList[id=1011502].name
   limit: do 50 znaków
   EN: Prescript Delivered on a Device
   PL: Nakaz Przekazany Terminalem
602. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시,\n- 자신의 [UnlockBuff_Base] 단계에 따라 [IndexPrescriptYi_0]/[IndexPrescriptYi_1]/[IndexPrescriptYi_2]/[IndexPrescriptYi_3] 얻음\n- 무작위 적 1명에게 [IndexPrescriptTargetToEnemy] 부여 (집중 전투면, 부위에 부여)\n- 조작 슬롯의 자신의 기본 공격 스킬에 [IndexPrescriptTargetMarkToEnemy] 부여 (슬롯당 1개, 최대 2개 부여)\n· [UnlockBuffAlly_2] 이상이면, 스킬 3에 우선 부여 (강화된 스킬 우선)\n- 흐트러짐, 행동 불가[TabExplain], 패닉, E.G.O 침식 상태면, 위의 모든 효과와 [IndexPrescript_Base_2nd] 수행 여부가 적용되지 않음
   źródło: Passives.json :: dataList[id=1011502].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [IndexPrescriptYi_0], [IndexPrescriptYi_1], [IndexPrescriptYi_2], [IndexPrescriptYi_3], [IndexPrescriptTargetToEnemy], [IndexPrescriptTargetMarkToEnemy], [UnlockBuffAlly_2], [TabExplain], [IndexPrescript_Base_2nd]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescriptYi_0] = 지령[단말기] I / Prescript: [Device] I; [IndexPrescriptYi_1] = 지령[단말기] II / Prescript: [Device] II; [IndexPrescriptYi_2] = 지령[단말기] III / Prescript: [Device] III; [IndexPrescriptYi_3] = 지령[단말기] IV / Prescript: [Device] IV; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [UnlockBuffAlly_2] = 해금 - II / Unlock - II …
   EN: Turn Start:\n- Gain [IndexPrescriptYi_0] / [IndexPrescriptYi_1] / [IndexPrescriptYi_2] / [IndexPrescriptYi_3] based on [UnlockBuff_Base] stage on self\n- Inflict [IndexPrescriptTargetToEnemy] to a random enemy (in Focused Encounters, a Part)\n- Apply [IndexPrescriptTargetMarkToEnemy] to Base Attack Skills on this unit's Dashboard (1 per Slot, max 2 Skills)\n· At [UnlockBuffAlly_2]+, the effect above prioritizes Skill 3 (prioritizes empowered Skill)\n- All of the effects above and [IndexPrescript_Base_2nd] execution checks do not trigger when this unit is Staggered, Immobilized[TabExplain], in Panic, or in E.G.O Corrosion[TabExplain]
   PL: Na początku tury:\n- Zyskuje [IndexPrescriptYi_0] / [IndexPrescriptYi_1] / [IndexPrescriptYi_2] / [IndexPrescriptYi_3] w zależności od stopnia [UnlockBuff_Base] na tej jednostce\n- Nakłada [IndexPrescriptTargetToEnemy] na 1 losowego wroga (w walkach skupionych: na część)\n- Nakłada [IndexPrescriptTargetMarkToEnemy] na Umiejętności bazowego ataku na panelu tej jednostki (1 na slot, maks. 2 Umiejętności)\n· Przy [UnlockBuffAlly_2]+ efekt ten priorytetowo obejmuje Umiejętność 3 (priorytetowo ulepszoną Umiejętność)\n- Wszystkie powyższe efekty oraz sprawdzanie wykonania [IndexPrescript_Base_2nd] nie działają, gdy ta jednostka jest Oszołomiona, Unieruchomiona[TabExplain], w Panice lub w Korozji E.G.O[TabExplain]
603. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 지령 수행 시, 정신력 회복하고 지령의 가호 얻음\n지령 실패 시, 카르마 얻음
   źródło: Passives.json :: dataList[id=1011502].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon executing Prescript, heal SP and gain Grace of the Prescript\nUpon failing Prescript, gain Karmic Consequence
   PL: Po wykonaniu Nakazu odzyskuje Poczytalność i zyskuje Łaskę Nakazu\nPo nieudanym Nakazie zyskuje Karmę
604. [Pasywka bojowa (od ulepszenia 1) — nazwa] 신탁 대행자 / 해금
   źródło: Passives.json :: dataList[id=1011503].name
   limit: do 40 znaków
   EN: The Oracle's Proxy / Unlock
   PL: Pełnomocnik Wyroczni / Odblokowanie
605. [Pasywka bojowa (od ulepszenia 1) — opis] [UnlockBuffAlly_2] 미만일 때 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 4 회복, [BlessingOfIndexPrescriptAlly] 1 얻음 (턴당 1회)\n- [IndexPrescript_Base_2nd] 수행 시 메인 타겟에게 [IndexPrescriptTargetToEnemy]이 있으면,\n대신 정신력 8 회복, [BlessingOfIndexPrescriptAlly] 3 얻음\n\n[UnlockBuffAlly_2]일 때 이번 턴에 [IndexPrescriptYi_2]을 수행했으면,\n턴 종료 시 정신력 4 회복 (턴당 1회)\n- [IndexPrescript_Base_2nd] 수행 시 [StackYisangSpecialSkill]가 9가 되었으면,\n대신 정신력 8 회복, [BlessingOfIndexPrescriptAlly] 3 얻음\n\n이번 턴에 [IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexAlly] 5 얻음\n- [UnlockBuffAlly_3]이면, [KarmaOfIndexAlly]를 얻지 않음\n- 전투 시작 시 [IndexPrescript_Base_2nd] 수행을 시도했으나, 전투 중에 대상을 타겟할 수 없게 되었으면, 턴 종료 시 [KarmaOfIndexAlly]를 얻지 않음 ([UnlockBuffAlly_2] 미만일 때 적용)\n\n턴 종료 시 [BlessingOfIndexPrescriptAlly]가 3/6/9이면, [UnlockBuffAlly_1]/[UnlockBuffAlly_2]/[UnlockBuffAlly_3] 얻음\n턴 시작 시 [UnlockBuffAlly_3]이면, [Shin_IndexFingerYisang] 얻음
   źródło: Passives.json :: dataList[id=1011503].desc
   limit: do 1440 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuffAlly_2], [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetToEnemy], [IndexPrescriptYi_2], [StackYisangSpecialSkill], [KarmaOfIndexAlly], [UnlockBuffAlly_3], [UnlockBuffAlly_1], [Shin_IndexFingerYisang]
   znaczenie tagów: [UnlockBuffAlly_2] = 해금 - II / Unlock - II; [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [IndexPrescriptYi_2] = 지령[단말기] III / Prescript: [Device] III; [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [UnlockBuffAlly_3] = 해금 - III / Unlock - III …
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn at below [UnlockBuffAlly_2], heal 4 SP and gain 1 [BlessingOfIndexPrescriptAlly] (once per turn)\n- When executing [IndexPrescript_Base_2nd], if the main target has [IndexPrescriptTargetToEnemy], heal 8 SP and gain 3 [BlessingOfIndexPrescriptAlly] instead\n\nTurn End: If this unit is at [UnlockBuffAlly_2] and [IndexPrescriptYi_2] was executed this turn, heal 4 SP (once per turn)\n- When executing [IndexPrescript_Base_2nd], if [StackYisangSpecialSkill] has reached 9 Stacks, heal 8 SP and gain 3 [BlessingOfIndexPrescriptAlly] instead\n\nTurn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 5 [KarmaOfIndexAlly]\n- At [UnlockBuffAlly_3], does not gain [KarmaOfIndexAlly]\n- If this unit attempted to execute [IndexPrescript_Base_2nd] at Combat Start, but could not target the enemy during the combat phase, does not gain [KarmaOfIndexAlly] at Turn End (applies at below [UnlockBuffAlly_2])\n\nTurn End: At 3/6/9 [BlessingOfIndexPrescriptAlly], gain [UnlockBuffAlly_1]/[UnlockBuffAlly_2]/[UnlockBuffAlly_3]\nTurn Start: At [UnlockBuffAlly_3], gain [Shin_IndexFingerYisang]
   PL: Na koniec tury: jeżeli w tej turze wykonano [IndexPrescript_Base_2nd] przy mniej niż [UnlockBuffAlly_2], odzyskuje 4 Poczytalności i zyskuje 1 [BlessingOfIndexPrescriptAlly] (raz na turę)\n- Przy wykonywaniu [IndexPrescript_Base_2nd], jeżeli główny cel ma [IndexPrescriptTargetToEnemy], zamiast tego odzyskuje 8 Poczytalności i zyskuje 3 [BlessingOfIndexPrescriptAlly]\n\nNa koniec tury: jeżeli jednostka jest na [UnlockBuffAlly_2] i w tej turze wykonano [IndexPrescriptYi_2], odzyskuje 4 Poczytalności (raz na turę)\n- Przy wykonywaniu [IndexPrescript_Base_2nd], jeżeli [StackYisangSpecialSkill] osiągnęło 9 stosów, zamiast tego odzyskuje 8 Poczytalności i zyskuje 3 [BlessingOfIndexPrescriptAlly]\n\nJeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd], na koniec tury zyskuje 5 [KarmaOfIndexAlly]\n- Przy [UnlockBuffAlly_3] nie zyskuje [KarmaOfIndexAlly]\n- Jeżeli ta jednostka próbowała wykonać [IndexPrescript_Base_2nd] na początku walki, ale nie mogła celować w wroga podczas fazy walki, nie zyskuje [KarmaOfIndexAlly] na koniec tury (dotyczy mniej niż [UnlockBuffAlly_2])\n\nNa koniec tury przy 3/6/9 [BlessingOfIndexPrescriptAlly] zyskuje [UnlockBuffAlly_1]/[UnlockBuffAlly_2]/[UnlockBuffAlly_3]\nNa początku tury przy [UnlockBuffAlly_3] zyskuje [Shin_IndexFingerYisang]
606. [Pasywka bojowa (od ulepszenia 1) — nazwa] 검지 아비
   źródło: Passives.json :: dataList[id=1011504].name
   limit: do 40 znaków
   EN: The Index Nursefather
   PL: Ojciec Wskazującego
607. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지에 첫 등장 시, [BurningWoundYisangMask] 얻음\n- 이 효과를 보유 중일 때 이번 전투에서 처음으로 흐트러지면,\n턴 종료 시 흐트러짐을 해제(강제 흐트러짐 제외)하고\n[BurningWoundYisangMask]이 [BurningWoundYisang]로 변경됨\n\n검지 대행자 - <noparse>개화</noparse> E.G.O::대행 돈키호테가 자신과 함께 전장에 있으면, 돈키호테에게 [SatisfyingEsteemNeeds] 부여
   źródło: Passives.json :: dataList[id=1011504].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [BurningWoundYisangMask], [BurningWoundYisang], [SatisfyingEsteemNeeds]
   znaczenie tagów: [BurningWoundYisangMask] = 상처를 가린 가면 / Wound-casing Mask; [BurningWoundYisang] = 이글거리는 상처 / Sizzling Wound; [SatisfyingEsteemNeeds] = 인정 욕구 충족 / Desire for Acknowledgement Sated
   EN: Upon entering the Encounter for the first time, gain [BurningWoundYisangMask]\n- Turn End: If this unit was Staggered for the first time in this Encounter while under this effect, recover from Stagger (excluding forced Stagger) and convert [BurningWoundYisangMask] to [BurningWoundYisang]\n\nApply [SatisfyingEsteemNeeds] to The Index Proxy - Effloresced E.G.O::Procuration Don Quixote when both units are on the field
   PL: Przy pierwszym pojawieniu się na etapie zyskuje [BurningWoundYisangMask]\n- Jeżeli podczas posiadania tego efektu jednostka zostanie Oszołomiona po raz pierwszy w tej walce, na koniec tury dochodzi do siebie z Oszołomienia (z wyłączeniem wymuszonego Ogłuszenia), a [BurningWoundYisangMask] zamienia się w [BurningWoundYisang]\n\nNakłada [SatisfyingEsteemNeeds] na Pełnomocnika Wskazującego - Rozkwitłe E.G.O::Pełnomocnictwo Don Quixote, gdy oba te elementy są na polu walki
608. [Pasywka bojowa (od ulepszenia 1) — nazwa] 신탁 단말기 [카두세우스]
   źródło: Passives.json :: dataList[id=1011505].name
   limit: do 40 znaków
   EN: Oracle Device [Caduceus]
   PL: Terminal Wyroczni [Kaduceusz]
609. [Pasywka bojowa (od ulepszenia 1) — opis] 기본 공격 스킬의 코인마다 무기가 무작위로 정해져 특수한 효과가 적용됨\n- [YisangWeapon01Hatchet]\n- [YisangWeapon02Stiletto]\n- [YisangWeapon03Greatsword]\n- [YisangWeapon04Rapier]\n- [YisangWeapon05Sledgehammer]\n- [YisangWeapon06Ultragreatsword]\n- [YisangWeapon07Lance]\n- [YisangWeapon08Chain]\n- [YisangWeapon09Scythe]\n\n[IndexPrescriptTargetMarkToEnemy] 스킬 사용 시, [StackYisangSpecialSkill] 1 얻음
   źródło: Passives.json :: dataList[id=1011505].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [YisangWeapon01Hatchet], [YisangWeapon02Stiletto], [YisangWeapon03Greatsword], [YisangWeapon04Rapier], [YisangWeapon05Sledgehammer], [YisangWeapon06Ultragreatsword], [YisangWeapon07Lance], [YisangWeapon08Chain], [YisangWeapon09Scythe], [IndexPrescriptTargetMarkToEnemy], [StackYisangSpecialSkill]
   znaczenie tagów: [YisangWeapon01Hatchet] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [YisangWeapon02Stiletto] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [YisangWeapon03Greatsword] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [YisangWeapon04Rapier] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [YisangWeapon05Sledgehammer] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [YisangWeapon06Ultragreatsword] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a great sword...; [YisangWeapon07Lance] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [YisangWeapon08Chain] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: A random weapon is assigned to every Coin for Base Attack Skills. Each weapon has a unique effect.\n- [YisangWeapon01Hatchet]\n- [YisangWeapon02Stiletto]\n- [YisangWeapon03Greatsword]\n- [YisangWeapon04Rapier]\n- [YisangWeapon05Sledgehammer]\n- [YisangWeapon06Ultragreatsword]\n- [YisangWeapon07Lance]\n- [YisangWeapon08Chain]\n- [YisangWeapon09Scythe]\n\nGain 1 [StackYisangSpecialSkill] when using Skills with [IndexPrescriptTargetMarkToEnemy]
   PL: Każda moneta Umiejętności bazowego ataku otrzymuje losowo przydzieloną broń o unikalnym efekcie.\n- [YisangWeapon01Hatchet]\n- [YisangWeapon02Stiletto]\n- [YisangWeapon03Greatsword]\n- [YisangWeapon04Rapier]\n- [YisangWeapon05Sledgehammer]\n- [YisangWeapon06Ultragreatsword]\n- [YisangWeapon07Lance]\n- [YisangWeapon08Chain]\n- [YisangWeapon09Scythe]\n\nZyskuje 1 [StackYisangSpecialSkill] przy użyciu Umiejętności z [IndexPrescriptTargetMarkToEnemy]
610. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 무기가 무작위로 정해짐\n‘Furioso-Replica’ 사용 시 특수 효과 얻음
   źródło: Passives.json :: dataList[id=1011505].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A random weapon is assigned\nGain special effect when using "Furioso-Replica"
   PL: Broń jest przydzielana losowo\nUżycie „Furioso-Replica” daje efekt specjalny
611. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — nazwa] 모조된 삶
   źródło: Passives.json :: dataList[id=1011501].name
   limit: do 40 znaków
   EN: Imitation of a Life
   PL: Naśladownictwo Życia
612. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — opis] 자신의 [BlessingOfIndexPrescriptAlly] 1당 [IndexPrescriptTargetMarkToEnemy] 스킬 피해량 +2% (최대 16%)\n - [BlessingOfIndexPrescriptAlly]가 9일 경우, 대신 기본 스킬의 피해량 +20%\n\n기본 공격 스킬의 [SuperCoin] 적중 시, [StackYisangSpecialSkill] 1 얻음\n- 공격 종료 시, 남은 [SuperCoin] 수만큼 [StackYisangSpecialSkill] 얻음
   źródło: Passives.json :: dataList[id=1011501].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetMarkToEnemy], [SuperCoin], [StackYisangSpecialSkill]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: Deal +2% damage with Skills marked with [IndexPrescriptTargetMarkToEnemy] for every [BlessingOfIndexPrescriptAlly] on self (max 16%)\n- At 9 [BlessingOfIndexPrescriptAlly], deal +20% damage with Base Skills instead\n\nOn Hit with Base Attack Skill's [SuperCoin]s, gain 1 [StackYisangSpecialSkill]\n- Attack End: Gain [StackYisangSpecialSkill] equal to (# of remaining [SuperCoin]s)
   PL: Zadaje +2% obrażeń Umiejętnościami oznaczonymi [IndexPrescriptTargetMarkToEnemy] za każdy [BlessingOfIndexPrescriptAlly] na tej jednostce (maks. 16%)\n - Przy 9 [BlessingOfIndexPrescriptAlly] zamiast tego zadaje +20% obrażeń Umiejętnościami bazowymi\n\nPrzy trafieniu [SuperCoin]ami Umiejętności bazowego ataku zyskuje 1 [StackYisangSpecialSkill]\n- Na koniec ataku zyskuje [StackYisangSpecialSkill] równe liczbie pozostałych [SuperCoin]
613. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — podsumowanie] 지령 표식이 새겨진 스킬이면,\n지령의 가호에 비례하여 피해량이 증가\n적중 시 정신력 회복\n조건 만족 시, [StackYisangSpecialSkill] 얻음
   źródło: Passives.json :: dataList[id=1011501].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [StackYisangSpecialSkill]
   znaczenie tagów: [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: Deal more damage with Skills marked with Mark of the Prescript based on Grace of the Prescript on self\nOn Hit: Heal SP\nGain [StackYisangSpecialSkill] when certain conditions are met
   PL: Umiejętności z Znakiem Nakazu zadają więcej obrażeń proporcjonalnie do Łaski Nakazu na tej jednostce\nPrzy trafieniu odzyskuje Poczytalność\nSpełnienie warunków daje [StackYisangSpecialSkill]
614. [Pasywka bojowa (od ulepszenia 3) — nazwa] 신탁 단말기 [카두세우스]
   źródło: Passives.json :: dataList[id=1011506].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Pasywka bojowa (od ulepszenia 3) — opis] 기본 공격 스킬의 코인마다 무기가 무작위로 정해져 특수한 효과가 적용됨\n- [YisangWeapon01Hatchet]\n- [YisangWeapon02Stiletto]\n- [YisangWeapon03Greatsword]\n- [YisangWeapon04Rapier]\n- [YisangWeapon05Sledgehammer]\n- [YisangWeapon06Ultragreatsword]\n- [YisangWeapon07Lance]\n- [YisangWeapon08Chain]\n- [YisangWeapon09Scythe]\n\n[IndexPrescriptTargetMarkToEnemy] 스킬 사용 시, [StackYisangSpecialSkill] 1 얻음\n\n<style="highlight">이번 전투에서 ‘Furioso-Replica’를 처음 사용하였다면,\n해당 턴 종료 시 [BurningWoundYisangMask]이 [BurningWoundYisang]로 변경됨\n\n턴 시작 시 [BurningWoundYisang]를 보유 중일 때,\n조작 슬롯에 ‘Furioso-Replica’가 있으면 [BlackNightmareYisang] 얻음</style>
   źródło: Passives.json :: dataList[id=1011506].desc
   limit: do 890 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [YisangWeapon01Hatchet], [YisangWeapon02Stiletto], [YisangWeapon03Greatsword], [YisangWeapon04Rapier], [YisangWeapon05Sledgehammer], [YisangWeapon06Ultragreatsword], [YisangWeapon07Lance], [YisangWeapon08Chain], [YisangWeapon09Scythe], [IndexPrescriptTargetMarkToEnemy], [StackYisangSpecialSkill], [BurningWoundYisangMask], [BurningWoundYisang], [BlackNightmareYisang]
   znaczenie tagów: [YisangWeapon01Hatchet] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [YisangWeapon02Stiletto] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [YisangWeapon03Greatsword] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [YisangWeapon04Rapier] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [YisangWeapon05Sledgehammer] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [YisangWeapon06Ultragreatsword] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a great sword...; [YisangWeapon07Lance] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [YisangWeapon08Chain] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: A random weapon is assigned to every Coin for Base Attack Skills. Each weapon has a unique effect.\n- [YisangWeapon01Hatchet]\n- [YisangWeapon02Stiletto]\n- [YisangWeapon03Greatsword]\n- [YisangWeapon04Rapier]\n- [YisangWeapon05Sledgehammer]\n- [YisangWeapon06Ultragreatsword]\n- [YisangWeapon07Lance]\n- [YisangWeapon08Chain]\n- [YisangWeapon09Scythe]\n\nGain 1 [StackYisangSpecialSkill] when using Skills with [IndexPrescriptTargetMarkToEnemy]\n\n<style="highlight">Convert [BurningWoundYisangMask] to [BurningWoundYisang] at the end of the turn this unit used "Furioso-Replica" for the first time in this Encounter\n\nTurn Start: If this unit has [BurningWoundYisang] and has "Furioso-Replica" on the Dashboard, gain [BlackNightmareYisang]</style>
   PL: Każda moneta Umiejętności bazowego ataku otrzymuje losowo przydzieloną broń o unikalnym efekcie.\n- [YisangWeapon01Hatchet]\n- [YisangWeapon02Stiletto]\n- [YisangWeapon03Greatsword]\n- [YisangWeapon04Rapier]\n- [YisangWeapon05Sledgehammer]\n- [YisangWeapon06Ultragreatsword]\n- [YisangWeapon07Lance]\n- [YisangWeapon08Chain]\n- [YisangWeapon09Scythe]\n\nZyskuje 1 [StackYisangSpecialSkill] przy użyciu Umiejętności z [IndexPrescriptTargetMarkToEnemy]\n\n<style="highlight">Jeżeli ta jednostka użyła „Furioso-Replica” po raz pierwszy w tej walce,\n[BurningWoundYisangMask] zamienia się w [BurningWoundYisang] na koniec tej tury\n\nNa początku tury, jeżeli jednostka posiada [BurningWoundYisang], a „Furioso-Replica” jest na panelu, zyskuje [BlackNightmareYisang]</style>
616. [Pasywka bojowa (od ulepszenia 3) — podsumowanie] 무기가 무작위로 정해짐\n‘Furioso-Replica’ 사용 시 특수 효과 얻음
   źródło: Passives.json :: dataList[id=1011506].summary
   (powtórzenie elementu 610 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Pasywka bojowa (od ulepszenia 3, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — nazwa] 모조된 삶
   źródło: Passives.json :: dataList[id=1011511].name
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Pasywka bojowa (od ulepszenia 3, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — opis] 자신의 [BlessingOfIndexPrescriptAlly] 1당 [IndexPrescriptTargetMarkToEnemy] 스킬 피해량 +2% (최대 16%)\n - [BlessingOfIndexPrescriptAlly]가 9일 경우, 대신 기본 스킬의 피해량 +20%\n\n기본 공격 스킬의 [SuperCoin] 적중 시, [StackYisangSpecialSkill] 1 얻음\n- 공격 종료 시, 남은 [SuperCoin] 수만큼 [StackYisangSpecialSkill] 얻음\n<style="highlight">- ‘Furioso-Replica’ 공격 종료 시, 해당 스킬의 (남은 [SuperCoin] 수/2)만큼 다음 턴에 [StackYisangSpecialSkill] 얻음 (소수점 버림)</style>\n\n<style="highlight">턴 종료 시 이번 턴에 [StackYisangSpecialSkill]가 증가하여 9가 되었을 때,\n다음 턴 시작 시 조작 슬롯에 스킬 3이 없으면, 기본 스킬 하나를 스킬 3으로 변경 (가장 왼쪽 슬롯의 아래 스킬 우선)</style>
   źródło: Passives.json :: dataList[id=1011511].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetMarkToEnemy], [SuperCoin], [StackYisangSpecialSkill]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StackYisangSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: Deal +2% damage with Skills marked with [IndexPrescriptTargetMarkToEnemy] for every [BlessingOfIndexPrescriptAlly] on self (max 16%)\n- At 9 [BlessingOfIndexPrescriptAlly], deal +20% damage with Base Skills instead\n\nOn Hit with Base Attack Skill's [SuperCoin]s, gain 1 [StackYisangSpecialSkill]\n- Attack End: Gain [StackYisangSpecialSkill] equal to (# of remaining [SuperCoin]s)\n<style="highlight">- "Furioso-Replica" Attack End: Gain [StackYisangSpecialSkill] next turn equal to (# of this Skill's remaining [SuperCoin]s / 2) (rounded down)</style>\n\n<style="highlight">If [StackYisangSpecialSkill] reached 9 Stacks this turn at Turn End, and if this unit does not have a Skill 3 on the Dashboard at the start of the next turn, convert a Base Skill to Skill 3 (prioritizes the Skill on the leftmost Slot's bottom row)</style>
   PL: Zadaje +2% obrażeń Umiejętnościami oznaczonymi [IndexPrescriptTargetMarkToEnemy] za każdy [BlessingOfIndexPrescriptAlly] na tej jednostce (maks. 16%)\n - Przy 9 [BlessingOfIndexPrescriptAlly] zamiast tego zadaje +20% obrażeń Umiejętnościami bazowymi\n\nPrzy trafieniu [SuperCoin]ami Umiejętności bazowego ataku zyskuje 1 [StackYisangSpecialSkill]\n- Na koniec ataku zyskuje [StackYisangSpecialSkill] równe liczbie pozostałych [SuperCoin]\n<style="highlight">- Na koniec ataku „Furioso-Replica” zyskuje w następnej turze [StackYisangSpecialSkill] równe (pozostałe [SuperCoin] tej Umiejętności / 2) (zaokrąglone w dół)</style>\n\n<style="highlight">Jeżeli na koniec tury [StackYisangSpecialSkill] osiągnęło 9 stosów w tej turze, a na początku następnej tury jednostka nie ma Umiejętności 3 na panelu, zamienia 1 Umiejętność bazową w Umiejętność 3 (priorytetowo dolny rząd skrajnie lewego slotu)</style>
619. [Pasywka bojowa (od ulepszenia 3, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — podsumowanie] 지령 표식이 새겨진 스킬이면,\n지령의 가호에 비례하여 피해량이 증가\n적중 시 정신력 회복\n조건 만족 시, [StackYisangSpecialSkill] 얻음
   źródło: Passives.json :: dataList[id=1011511].summary
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — nazwa] 신의 가호
   źródło: Passives.json :: dataList[id=1011521].name
   limit: do 40 znaków
   EN: Grace of God
   PL: Łaska Boga
621. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — opis] 이번 턴에 아군이 적에게 처음으로 사용한 참격, 관통, 타격 기본 공격 스킬의 피해량이 각각 +5%\n- 효과가 적용된 스킬이 검지 소속 인격의 스킬이면, 대신 +10%\n- 공격 시작 전 기준으로 적용됨
   źródło: Passives.json :: dataList[id=1011521].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +5% damage with Slash, Pierce, and Blunt Base Attack Skills that are used for the first time by any ally each turn (once per type across all allies)\n- The Index Identities deal +10% damage instead\n- This effect's application is determined Before Attack
   PL: Umiejętności bazowe Cięcia, Kłucia i Obuchu użyte po raz pierwszy w tej turze przez dowolnego sojusznika zadają po +5% obrażeń (raz na typ wśród wszystkich sojuszników)\n- Tożsamości frakcji Wskazującego zadają zamiast tego +10% obrażeń\n- Efekt jest rozliczany przed rozpoczęciem ataku
622. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Glut., posiadane 1× Gloom, posiadane 1× Pride) — podsumowanie] 이번 턴에 처음 사용한, 참격, 관통, 타격 스킬 피해량 증가
   źródło: Passives.json :: dataList[id=1011521].summary
   limit: do 120 znaków
   EN: Deal more damage with Slash, Pierce, and Blunt Skills used for the first time this turn
   PL: Umiejętności Cięcia, Kłucia i Obuchu użyte po raz pierwszy w tej turze zadają więcej obrażeń

## [000] LCE E.G.O:: Dimension Shredder — Yi Sang — LCE E.G.O:: 차원찢개
- ID Tożsamości: `10116` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 60 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

623. [Karta Tożsamości — tytuł] LCE E.G.O::\n차원찢개
   źródło: Personalities.json :: dataList[id=10116].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCE E.G.O::\nDimension Shredder
   PL: LCE E.G.O::\nRozpruwacz Wymiarów
624. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10116].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10116].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Karta Tożsamości — opis] 이상의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10116].desc
   limit: do 120 znaków
   EN: Yi Sang's 16th Identity
   PL: Szesnasta Tożsamość Yi Sanga
627. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 차원 베기
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=1].name ; dataList[id=1011601].levelList[level=2].name ; dataList[id=1011601].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Dimensional Slice
   PL: Cięcie Wymiaru
628. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수를 2 소모하여, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 2 [Charge] Count to gain Coin Power +1
   PL: [WhenUse] Zużywa 2 Licznika [Charge], by zyskać Moc Monet +1
629. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 6 증가 (스킬당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +6 [Charge] Count (once per Skill)
   PL: [OnSucceedAttack] Zyskuje +6 Licznika [Charge] (raz na Umiejętność)
630. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [DriftingDimensionYisang]를 1 소모하여 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DriftingDimensionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway
   EN: [OnSucceedAttack] Consume 1 [DriftingDimensionYisang] to Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Zużywa 1 [DriftingDimensionYisang], by ponownie użyć tej monety (raz na Umiejętność)
632. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Charge] 횟수를 2 소모하여, 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 2 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL: [WhenUse] Zużywa 2 Licznika [Charge], by zyskać Moc Monet +1<style="highlight"></style>
633. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 6 증가 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +6 [Charge] Count (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +6 Licznika [Charge] (raz na Umiejętność)<style="highlight"></style>
634. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
635. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [DriftingDimensionYisang]를 1 소모하여 이 코인 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=1011601].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DriftingDimensionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway
   EN: [OnSucceedAttack] Consume 1 [DriftingDimensionYisang] to Reuse this Coin (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Zużywa 1 [DriftingDimensionYisang], by ponownie użyć tej monety (raz na Umiejętność)<style="highlight"></style>
636. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Charge] 횟수와 대상의 [Burst], [DimensionRift]의 합 6당 최종 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [Charge] 횟수를 2 소모하여, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge], [Burst], [DimensionRift]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: <style="highlight">[WhenUse] Final Power +1 for every 6 ([Charge] Count on self + [Burst] and [DimensionRift] on target) (max 3)</style>\n[WhenUse] Consume 2 [Charge] Count to gain Coin Power +1
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 6 sumy Licznika [Charge] tej jednostki oraz [Burst] i [DimensionRift] celu (maks. 3)</style>\n[WhenUse] Zużywa 2 Licznika [Charge], by zyskać Moc Monet +1
637. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
638. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 연속 차원 베기
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].name ; dataList[id=1011602].levelList[level=2].name ; dataList[id=1011602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 50 znaków
   EN: Consecutive Dimensional Slice
   PL: Ciągłe Cięcie Wymiaru
639. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수를 5 소모하여, 최종 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Final Power +2
   PL: [WhenUse] Zużywa 5 Licznika [Charge], by zyskać Moc Końcową +2
640. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 6 증가
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +6 [Charge] Count
   PL: [OnSucceedAttack] Zyskuje +6 Licznika [Charge]
641. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [DimensionRift] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 1 [DimensionRift]
   PL: [OnSucceedAttack] Nakłada 1 [DimensionRift]
644. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [Charge] 위력 x 4)%만큼 참격 피해 (최대 20%)
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Deal Slash damage equal to ([Charge] Potency on self x 4)% of this Coin's final damage (max 20%)
   PL: [OnSucceedAttack] Zadaje obrażenia Cięciem równe (Moc [Charge] na tej jednostce × 4)% ostatecznych obrażeń tej monety (maks. 20%)
645. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Charge] 횟수를 5 소모하여, 최종 위력 +2\n<style="highlight">[WhenUse] 자신의 [Charge]이 3 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Final Power +2\n<style="highlight">[WhenUse] At 3+ [Charge] Potency, Coin Power +1</style>
   PL: [WhenUse] Zużywa 5 Licznika [Charge], by zyskać Moc Końcową +2\n<style="highlight">[WhenUse] Przy 3+ Mocy [Charge] Moc Monet +1</style>
646. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 6 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +6 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +6 Licznika [Charge]<style="highlight"></style>
647. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
648. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [DimensionRift] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 1 [DimensionRift]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [DimensionRift]<style="highlight"></style>
650. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [Charge] 위력 x 4)%만큼 참격 피해 (최대 20%)<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1011602].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Deal Slash damage equal to ([Charge] Potency on self x 4)% of this Coin's final damage (max 20%)<style="highlight"></style>
   PL: [OnSucceedAttack] Zadaje obrażenia Cięciem równe (Moc [Charge] na tej jednostce × 4)% ostatecznych obrażeń tej monety (maks. 20%)<style="highlight"></style>
651. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Burst], [DimensionRift]의 합 6당 최종 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [Charge] 횟수를 5 소모하여, 최종 위력 +2\n[WhenUse] 자신의 [Charge] 위력이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011602].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [DimensionRift], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DimensionRift] = 차원 균열 / Dimensional Rift; [Charge] = 충전 / Charge
   EN: <style="highlight">[WhenUse] Final Power +1 for every 6 ([Burst] + [DimensionRift]) on target (max 3)</style>\n[WhenUse] Consume 5 [Charge] Count to gain Final Power +2\n[WhenUse] At 3+ [Charge] Potency, Coin Power +1
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 6 sumy [Burst] i [DimensionRift] celu (maks. 3)</style>\n[WhenUse] Zużywa 5 Licznika [Charge], by zyskać Moc Końcową +2\n[WhenUse] Przy 3+ Mocy [Charge] Moc Monet +1
652. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 공간 절단
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].name ; dataList[id=1011603].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Rip Space
   PL: Rozcięcie Przestrzeni
653. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] 자신의 [Charge] 횟수가 15 이상이면, ‘사차각 왜곡 시계열 절단’으로 발동\n[WhenUse] 자신의 [Charge] 횟수가 7 이상, 15 미만이면,\n- [Charge] 횟수를 전부 소모하고, 소모한 [Charge] 횟수 7당 코인 위력 +1 (최대 2)\n\n[WhenUse] [DriftingDimensionYisang] 1, [FourDimensionYisang] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [Charge], [WhenUse], [DriftingDimensionYisang], [FourDimensionYisang]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions
   EN: [BeforeUse] At 15+ [Charge] Count, activate "Four-dimensional Refraction Time Series Severance" instead\n[WhenUse] At 7~14 [Charge] Count:\n - Consume all [Charge] Count and gain Coin Power +1 for every 7 [Charge] Count consumed (max 2)\n\n[WhenUse] Gain 1 [DriftingDimensionYisang] and 1 [FourDimensionYisang]
   PL: [BeforeUse] Przy 15+ Licznika [Charge] aktywuje „Czterowymiarowe Złamanie Szeregów Czasu”\n[WhenUse] Przy 7~14 Licznika [Charge]:\n - Zużywa całe Liczniki [Charge] i zyskuje Moc Monet +1 za każde 7 zużytego Licznika [Charge] (maks. 2)\n\n[WhenUse] Zyskuje 1 [DriftingDimensionYisang] i 1 [FourDimensionYisang]
654. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Charge]
655. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [DimensionRift] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 2 [DimensionRift]
   PL: [OnSucceedAttack] Nakłada 2 [DimensionRift]
660. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [Charge] 위력 x 4)%만큼 참격 피해 (최대 20%)
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] 자신의 [Charge] 횟수가 15 이상이면, ‘사차각 왜곡 시계열 절단’으로 발동\n[WhenUse] 자신의 [Charge] 횟수가 7 이상, 15 미만이면,\n- [Charge] 횟수를 전부 소모하고, 소모한 [Charge] 횟수 7당 코인 위력 +1 (최대 2)\n\n<style="highlight">[WhenUse] 대상의 [Burst], [DimensionRift]의 합 6당 최종 위력 +1 (최대 4)</style>\n[WhenUse] [DriftingDimensionYisang] 1, [FourDimensionYisang] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [Charge], [WhenUse], [Burst], [DimensionRift], [DriftingDimensionYisang], [FourDimensionYisang]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DimensionRift] = 차원 균열 / Dimensional Rift; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions
   EN: [BeforeUse] At 15+ [Charge] Count, activate "Four-dimensional Refraction Time Series Severance" instead\n[WhenUse] At 7~14 [Charge] Count:\n - Consume all [Charge] Count and gain Coin Power +1 for every 7 [Charge] Count consumed (max 2)\n\n<style="highlight">[WhenUse] Final Power +1 for every 6 ([Burst] + [DimensionRift]) on target (max 4)</style>\n[WhenUse] Gain 1 [DriftingDimensionYisang] and 1 [FourDimensionYisang]
   PL: [BeforeUse] Przy 15+ Licznika [Charge] aktywuje „Czterowymiarowe Złamanie Szeregów Czasu”\n[WhenUse] Przy 7~14 Licznika [Charge]:\n - Zużywa całe Liczniki [Charge] i zyskuje Moc Monet +1 za każde 7 zużytego Licznika [Charge] (maks. 2)\n\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 6 sumy [Burst] i [DimensionRift] celu (maks. 4)</style>\n[WhenUse] Zyskuje 1 [DriftingDimensionYisang] i 1 [FourDimensionYisang]
662. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Charge]<style="highlight"></style>
663. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 647 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 647 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 647 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [DimensionRift] 2 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 2 [DimensionRift]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [DimensionRift]<style="highlight"></style>
668. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [Charge] 위력 x 4)%만큼 참격 피해 (최대 20%)<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność 4 (×0) (ulepszenie 3) — nazwa] 사차각 왜곡 시계열 절단
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 4 (+3)
   limit: do 70 znaków
   EN: Four-dimensional Refraction Time Series Severance
   PL: Czterowymiarowe Złamanie Szeregów Czasu
670. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WideAreaRampage]\n[WhenUse] 메인 타겟의 [Burst], [DimensionRift]의 합 6당 최종 위력 +1 (최대 3)\n[WhenUse] [DriftingDimensionYisang] 1, [FourDimensionYisang] 1 얻음\n[WhenUse] 자신의 [Charge] 횟수를 15 소모하여, 최종 위력 +1, 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [WhenUse], [Burst], [DimensionRift], [DriftingDimensionYisang], [FourDimensionYisang], [Charge]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DimensionRift] = 차원 균열 / Dimensional Rift; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions; [Charge] = 충전 / Charge
   EN: [WideAreaRampage]\n[WhenUse] Final Power +1 for every 6 ([Burst] + [DimensionRift]) on the main target (max 3)\n[WhenUse] Gain 1 [DriftingDimensionYisang] and 1 [FourDimensionYisang]\n[WhenUse] Consume 15 [Charge] Count to gain Final Power +1 and Coin Power +2
   PL: [WideAreaRampage]\n[WhenUse] Moc Końcowa +1 za każde 6 sumy [Burst] i [DimensionRift] głównego celu (maks. 3)\n[WhenUse] Zyskuje 1 [DriftingDimensionYisang] i 1 [FourDimensionYisang]\n[WhenUse] Zużywa 15 Licznika [Charge], by zyskać Moc Końcową +1 i Moc Monet +2
671. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [FourDimensionYisang] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FourDimensionYisang]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions
   EN: [OnSucceedAttack] Gain 1 [FourDimensionYisang]
   PL: [OnSucceedAttack] Zyskuje 1 [FourDimensionYisang]
672. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 5%만큼 모든 공격 대상에게 참격 피해
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Slash damage equal to 5% of this Coin's final damage to all targets
   PL: [OnSucceedAttack] Zadaje obrażenia Cięciem równe 5% ostatecznych obrażeń tej monety wszystkim celom ataku
674. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [FourDimensionYisang] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 5%만큼 모든 공격 대상에게 참격 피해
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [FourDimensionYisang] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 5%만큼 모든 공격 대상에게 참격 피해
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [DimensionRift] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 4 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 5%만큼 모든 공격 대상에게 참격 피해
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 5 — opis] [OnSucceedAttack] 자신의 [Charge] 위력이 5 이상이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011605].levelList[level=3].coinlist[#3].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] At 5+ [Charge] Potency, Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Przy 5+ Mocy [Charge] ponownie używa tej monety (raz na Umiejętność)
685. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-01.json :: dataList[id=1011604].levelList[level=1].name ; dataList[id=1011604].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Sidestep
   PL: Unik
686. [Obrona (ulepszenie 1) — opis] [StartBattle] [DriftingDimensionYisang] 1, [FourDimensionYisang] 1 얻음 (턴당 1회)\n- 자신의 [Charge] 위력이 3 이상이면 추가로 1 얻음\n\n[StartBattle] 자신의 [Charge] 횟수가 7 미만이면, 최대 체력의 (부족한 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수를 7까지 얻음. (이 피해로 체력이 0이 되지 않음, 소수점 버림)\n\n[StartBattle] 자신의 [Charge] 횟수가 15를 초과하면, 초과하는 [Charge] 횟수를 최대 10 소모하고, 아래 효과 적용\n- (소모값)%만큼 체력 회복\n- (소모값 / 3)만큼 다음 턴에 [Agility] 얻음 (소수점 버림)
   źródło: Skills_personality-01.json :: dataList[id=1011604].levelList[level=1].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DriftingDimensionYisang], [FourDimensionYisang], [Charge], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: [StartBattle] Gain 1 [DriftingDimensionYisang] and 1 [FourDimensionYisang] (once per turn)\n - At 3+ [Charge] Potency, gain 1 additional Stack of the above effects\n\n[StartBattle] At fewer than 7 [Charge] Count, consume (7 - [Charge] Count on self)% HP to gain up to 7 [Charge] Count (this unit's HP cannot drop to 0 due to this effect; rounded down)\n\n[StartBattle] At more than 15 [Charge] Count, consume up to 10 surplus [Charge] Count and apply the following effects:\n - Heal ([Charge] Count consumed)% HP\n - Gain ([Charge] Count consumed / 3) [Agility] next turn (rounded down)
   PL: [StartBattle] Zyskuje 1 [DriftingDimensionYisang] i 1 [FourDimensionYisang] (raz na turę)\n - Przy 3+ Mocy [Charge] zyskuje dodatkowy 1 stos powyższych efektów\n\n[StartBattle] Przy mniej niż 7 Licznika [Charge] zużywa (7 - Licznik [Charge] tej jednostki)% HP, by zdobyć do 7 Licznika [Charge] (HP tej jednostki nie może spaść do 0 przez ten efekt; zaokrąglone w dół)\n\n[StartBattle] Przy więcej niż 15 Licznika [Charge] zużywa do 10 nadwyżkowego Licznika [Charge] i stosuje:\n - Odzyskuje (zużyta wartość)% HP\n - Zyskuje (zużyta wartość / 3) [Agility] w następnej turze (zaokrąglone w dół)
687. [Obrona (ulepszenie 4) — opis] <style="highlight">[StartBattle] 자신의 [Charge] 위력만큼 [ChargeForceField] 얻음 (턴당 1회. 최대 5)</style>\n[StartBattle] [DriftingDimensionYisang] 1, [FourDimensionYisang] 1 얻음 (턴당 1회)\n- 자신의 [Charge] 위력이 3 이상이면 추가로 1 얻음\n\n[StartBattle] 자신의 [Charge] 횟수가 7 미만이면, 최대 체력의 (부족한 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수를 7까지 얻음. (이 피해로 체력이 0이 되지 않음, 소수점 버림)\n\n[StartBattle] 자신의 [Charge] 횟수가 15를 초과하면, 초과하는 [Charge] 횟수를 최대 10 소모하고, 아래 효과 적용\n- (소모값)%만큼 체력 회복\n- (소모값 / 3)만큼 다음 턴에 [Agility] 얻음 (소수점 버림)
   źródło: Skills_personality-01.json :: dataList[id=1011604].levelList[level=4].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Charge], [ChargeForceField], [DriftingDimensionYisang], [FourDimensionYisang], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions; [Agility] = 신속 / Haste
   EN: <style="highlight">[StartBattle] Gain [ChargeForceField] equal to [Charge] Potency on self (once per turn; max 5)</style>\n[StartBattle] Gain 1 [DriftingDimensionYisang] and 1 [FourDimensionYisang] (once per turn)\n - At 3+ [Charge] Potency, gain 1 additional Stack of the above effects\n\n[StartBattle] At fewer than 7 [Charge] Count, consume (7 - [Charge] Count on self)% HP to gain up to 7 [Charge] Count (this unit's HP cannot drop to 0 due to this effect; rounded down)\n\n[StartBattle] At more than 15 [Charge] Count, consume up to 10 surplus [Charge] Count and apply the following effects:\n - Heal ([Charge] Count consumed)% HP\n - Gain ([Charge] Count consumed / 3) [Agility] next turn (rounded down)
   PL: <style="highlight">[StartBattle] Zyskuje [ChargeForceField] równe Mocy [Charge] tej jednostki (raz na turę; maks. 5)</style>\n[StartBattle] Zyskuje 1 [DriftingDimensionYisang] i 1 [FourDimensionYisang] (raz na turę)\n - Przy 3+ Mocy [Charge] zyskuje dodatkowy 1 stos powyższych efektów\n\n[StartBattle] Przy mniej niż 7 Licznika [Charge] zużywa (7 - Licznik [Charge] tej jednostki)% HP, by zdobyć do 7 Licznika [Charge] (HP tej jednostki nie może spaść do 0 przez ten efekt; zaokrąglone w dół)\n\n[StartBattle] Przy więcej niż 15 Licznika [Charge] zużywa do 10 nadwyżkowego Licznika [Charge] i stosuje:\n - Odzyskuje (zużyta wartość)% HP\n - Zyskuje (zużyta wartość / 3) [Agility] w następnej turze (zaokrąglone w dół)
688. [Pasywka bojowa (od ulepszenia 1) — nazwa] 뚫린 골목
   źródło: Passives.json :: dataList[id=1011602].name
   limit: do 40 znaków
   EN: Open Alley
   PL: Przebity Zaułek
689. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다 [Charge] 위력 1 얻음\n\n자신을 제외한 아군의 스킬이 적에게 적중하면, 해당 공격 종료시 [DriftingDimensionYisang]을 1 소모하여 대상에게 '차원 베기'를 발동한 후, [FourDimensionYisang] 1 얻음
   źródło: Passives.json :: dataList[id=1011602].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [DriftingDimensionYisang], [FourDimensionYisang]
   znaczenie tagów: [Charge] = 충전 / Charge; [DriftingDimensionYisang] = 차원 표류 / Dimensional Castaway; [FourDimensionYisang] = 사색 차원 / Quadricolor Dimensions
   EN: Gain 1 [Charge] Potency every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nWhen another ally's Skill hits an enemy: At Attack End, consume 1 [DriftingDimensionYisang] to activate "Dimensional Slice" against the said target; then, gain 1 [FourDimensionYisang]
   PL: Zyskuje 1 Mocy [Charge] za każde skumulowane zużycie 10 Licznika [Charge] w tym spotkaniu\n\nGdy Umiejętność innego sojusznika trafi wroga: na koniec ataku zużywa 1 [DriftingDimensionYisang], by aktywować „Cięcie Wymiaru” na tym celu; następnie zyskuje 1 [FourDimensionYisang]
690. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — nazwa] 속도와좌표와속도
   źródło: Passives.json :: dataList[id=1011601].name
   limit: do 50 znaków
   EN: VelocityAndCoordinatesAndVelocity
   PL: PrędkośćIWspółrzędneIPrędkość
691. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 자신의 [Charge] 위력)%만큼 피해량이 증가 (최대 20%)\n\n턴 종료시, (자신의 [Charge] 위력/2)만큼 다음 턴에 [Agility] 얻음 (최대 2. 소수점 버림)
   źródło: Passives.json :: dataList[id=1011601].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Agility]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Charge] Potency on self)% damage (max 20%)\n\nTurn End: Gain ([Charge] Potency on self / 2) [Agility] next turn (max 2; rounded down)
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości × Moc [Charge] tej jednostki)% obrażeń (maks. 20%)\n\nNa koniec tury zyskuje (Moc [Charge] tej jednostki / 2) [Agility] w następnej turze (maks. 2; zaokrąglone w dół)
692. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 사람은광선보다도빠르게달아나라
   źródło: Passives.json :: dataList[id=1011621].name
   limit: do 50 znaków
   EN: LetManOutrunEvenTheRayOfLight
   PL: NiechCzłowiekUciekaSzybciejNiżŚwiatło
693. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 속도가 가장 빠른 아군 1명이 [Charge] 횟수를 얻거나 소모하는 스킬 사용시, 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1011621].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Charge], [Agility]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: When 1 ally with the fastest Speed uses a Skill that gains or consumes [Charge] Count, gain 1 [Agility] next turn (once per turn)
   PL: Gdy 1 sojusznik z najwyższą Szybkością użyje Umiejętności zyskującej lub zużywającej Licznik [Charge], zyskuje 1 [Agility] w następnej turze (raz na turę)

## [?] Haute Couture:: Le Noir B3F Drying Room — Yi Sang — 오트쿠튀르:: 르누아르 B3F 건조장
- ID Tożsamości: `10117` (plik: `Personalities.json`)

694. [Karta Tożsamości — tytuł] 오트쿠튀르::\n르누아르 B3F 건조장
   źródło: Personalities.json :: dataList[id=10117].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::\nLe Noir\nB3F\nDrying Room
   PL: Haute Couture::\nLe Noir B3F Suszarnia
695. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10117].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10117].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Karta Tożsamości — opis] 이상의 열일곱번째 인격
   źródło: Personalities.json :: dataList[id=10117].desc
   limit: do 120 znaków
   EN: Yi Sang's 17th Identity
   PL: Siedemnasta Tożsamość Yi Sanga
698. [Umiejętność powiązana 1011701 (ulepszenia 1,2,4) — nazwa] 가죽 뜯기
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=1].name ; dataList[id=1011701].levelList[level=2].name ; dataList[id=1011701].levelList[level=4].name
   limit: do 40 znaków
   EN: Flaying
   PL: Zdzieranie Skóry
699. [Umiejętność powiązana 1011701 (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +1\n[DefeatDuel] 자신의 최대 체력의 5%만큼 보호막을 얻고, 자신의 [ChargeNoirAlly] 횟수 4 증가 (턴당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoirAlly], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +1\n[DefeatDuel] Gain Shield equal to 5% of this unit's max HP and gain +4 [ChargeNoirAlly] Count (once per turn)
   PL: [WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +1\n[DefeatDuel] Zyskuje Tarczę równą 5% Maks. HP tej jednostki i +4 Licznika [ChargeNoirAlly] (raz na turę)
700. [Umiejętność powiązana 1011701 (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 6 증가
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +6 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zyskuje +6 Licznika [ChargeNoirAlly]
701. [Umiejętność powiązana 1011701 (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność powiązana 1011701 (ulepszenie 2) — opis] [WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +1\n<style="highlight">[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +10%</style>\n[DefeatDuel] 자신의 최대 체력의 5%만큼 보호막을 얻고, 자신의 [ChargeNoirAlly] 횟수 4 증가 (턴당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=2].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ChargeNoirAlly], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +1\n<style="highlight">[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +10% damage</style>\n[DefeatDuel] Gain Shield equal to 5% of this unit's max HP and gain +4 [ChargeNoirAlly] Count (once per turn)
   PL: [WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +1\n<style="highlight">[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +10% obrażeń</style>\n[DefeatDuel] Zyskuje Tarczę równą 5% Maks. HP tej jednostki i +4 Licznika [ChargeNoirAlly] (raz na turę)
703. [Umiejętność powiązana 1011701 (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność powiązana 1011701 (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Vibration] 위력과 [MoodooJoesu]의 합 4당, 최종 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +1\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">20%</style>\n[DefeatDuel] 자신의 최대 체력의 5%만큼 보호막을 얻고, 자신의 [ChargeNoirAlly] 횟수 4 증가 (턴당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [MoodooJoesu], [ChargeNoirAlly], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [ChargeNoirAlly] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [MoodooJoesu]) on target (max 3)</style>\n[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +1\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">20</style>% damage\n[DefeatDuel] Gain Shield equal to 5% of this unit's max HP and gain +4 [ChargeNoirAlly] Count (once per turn)
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 sumy Mocy [Vibration] i [MoodooJoesu] celu (maks. 3)</style>\n[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +1\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">20%</style> obrażeń\n[DefeatDuel] Zyskuje Tarczę równą 5% Maks. HP tej jednostki i +4 Licznika [ChargeNoirAlly] (raz na turę)
705. [Umiejętność powiązana 1011701 (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Umiejętność powiązana 1011702 (ulepszenia 1,2,4) — nazwa] 스플리팅
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].name ; dataList[id=1011702].levelList[level=2].name ; dataList[id=1011702].levelList[level=4].name
   limit: do 40 znaków
   EN: Splitting
   PL: Splitting
707. [Umiejętność powiązana 1011702 (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +1
   PL: [WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +1
708. [Umiejętność powiązana 1011702 (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 8 증가
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +8 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zyskuje +8 Licznika [ChargeNoirAlly]
709. [Umiejętność powiązana 1011702 (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność powiązana 1011702 (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [BulletJoesu]가 3 이상이면, [HitTakeDamageUp] 1 부여 (턴당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011702].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletJoesu], [HitTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner; [HitTakeDamageUp] = 타격 취약 / Blunt Fragility
   EN: [OnSucceedAttack] At 3+ [BulletJoesu], inflict 1 [HitTakeDamageUp] (once per turn)
   PL: [OnSucceedAttack] Przy 3+ [BulletJoesu] nakłada 1 [HitTakeDamageUp] (raz na turę)
711. [Umiejętność powiązana 1011702 (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [BulletJoesu] 3 소모
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1011702].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1011702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletJoesu]
   znaczenie tagów: [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner
   EN: Spend 3 [BulletJoesu]
   PL: Zużywa 3 [BulletJoesu]
712. [Umiejętność powiązana 1011702 (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
713. [Umiejętność powiązana 1011702 (ulepszenie 2) — opis] [WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +1\n<style="highlight">[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +10%</style>
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +1\n<style="highlight">[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +10% damage</style>
   PL: [WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +1\n<style="highlight">[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +10% obrażeń</style>
714. [Umiejętność powiązana 1011702 (ulepszenie 2) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 횟수 1 증가</style>
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Vibration] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada +1 Licznika [Vibration]</style>
715. [Umiejętność powiązana 1011702 (ulepszenia 2,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=2].coinlist[#2].coindescs[#2].desc ; dataList[id=1011702].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
716. [Umiejętność powiązana 1011702 (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Vibration] 위력과 [MoodooJoesu]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +1\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">20%</style>
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [MoodooJoesu], [ChargeNoirAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [ChargeNoirAlly] = 보존 / Preservation
   EN: <style="highlight">[WhenUse] If target has 6+ ([Vibration] Potency + [MoodooJoesu]), Coin Power +1</style>\n[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +1\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">20</style>% damage
   PL: <style="highlight">[WhenUse] Jeżeli suma Mocy [Vibration] i [MoodooJoesu] celu wynosi 6 lub więcej, Moc Monet +1</style>\n[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +1\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">20%</style> obrażeń
717. [Umiejętność powiązana 1011702 (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011702].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +<style="highlight">2</style> Licznika [Vibration]
718. [Umiejętność powiązana 1011703 (ulepszenia 3–4) — nazwa] 원죄적 뇌유 텀블링
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].name ; dataList[id=1011703].levelList[level=4].name
   limit: do 70 znaków
   EN: Leather Tumbling in Brain Fat: Original Sin Style
   PL: Tumbling Skór w Tłuszczu Mózgu: W Stylu Grzechu Pierworodnego
719. [Umiejętność powiązana 1011703 (ulepszenie 3) — opis] [BeforeUse] [BulletJoesu]가 6이면, [WideAreaRampage], 공격 가중치 +2 (턴당 1회)\n\n[WhenUse] 메인 타겟의 [Vibration] 위력과 [MoodooJoesu]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 5 소모하여, 최종 위력 +2\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +10%\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +20% (집중 전투면, 부위로 판정)
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [BulletJoesu], [WideAreaRampage], [WhenUse], [Vibration], [MoodooJoesu], [ChargeNoirAlly]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [ChargeNoirAlly] = 보존 / Preservation
   EN: [BeforeUse] At 6 [BulletJoesu], activate as [WideAreaRampage] and gain +2 Atk Weight (once per turn)\n\n[WhenUse] If the main target has 6+ ([Vibration] Potency + [MoodooJoesu]), Coin Power +1\n[WhenUse] Consume 5 [ChargeNoirAlly] Count to gain Final Power +2\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +10% damage\n[WhenUse] Deal +20% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, Parts)
   PL: [BeforeUse] Przy 6 [BulletJoesu] aktywuje jako [WideAreaRampage] i zyskuje +2 wagi ataku (raz na turę)\n\n[WhenUse] Jeżeli suma Mocy [Vibration] i [MoodooJoesu] głównego celu wynosi 6 lub więcej, Moc Monet +1\n[WhenUse] Zużywa 5 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +2\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +10% obrażeń\n[WhenUse] Zadaje +20% obrażeń za każdego celu ataku poniżej wagi ataku tej Umiejętności (w walkach skupionych rozliczane na części)
720. [Umiejętność powiązana 1011703 (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 4 증가
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +4 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zyskuje +4 Licznika [ChargeNoirAlly]
721. [Umiejętność powiązana 1011703 (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność powiązana 1011703 (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [BulletJoesu] 6 소모
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletJoesu]
   znaczenie tagów: [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner
   EN: Spend 6 [BulletJoesu]
   PL: Zużywa 6 [BulletJoesu]
723. [Umiejętność powiązana 1011703 (ulepszenia 3–4) — moneta 3, efekt 2 — opis] 이 코인은 모든 공격 대상에게 적중함
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1011703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin hits all targets of the attack
   PL: Ta moneta trafia wszystkie cele ataku
724. [Umiejętność powiązana 1011703 (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność powiązana 1011703 (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1011703].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność powiązana 1011703 (ulepszenie 4) — opis] [BeforeUse] [BulletJoesu]가 6이면, [WideAreaRampage], 공격 가중치 +2 (턴당 1회)\n\n<style="highlight">[WhenUse] 메인 타겟의 [Vibration] 위력과 [MoodooJoesu]의 합 6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 5 소모하여, 최종 위력 +2\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">20%</style>\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +<style="highlight">30%</style> (집중 전투면, 부위로 판정)
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=4].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [BulletJoesu], [WideAreaRampage], [WhenUse], [Vibration], [MoodooJoesu], [ChargeNoirAlly]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [ChargeNoirAlly] = 보존 / Preservation
   EN: [BeforeUse] At 6 [BulletJoesu], activate as [WideAreaRampage] and gain +2 Atk Weight (once per turn)\n\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Vibration] Potency + [MoodooJoesu]) on the main target (max 2)</style>\n[WhenUse] Consume 5 [ChargeNoirAlly] Count to gain Final Power +2\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">20</style>% damage\n[WhenUse] Deal +<style="highlight">30</style>% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, Parts)
   PL: [BeforeUse] Przy 6 [BulletJoesu] aktywuje jako [WideAreaRampage] i zyskuje +2 wagi ataku (raz na turę)\n\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 sumy Mocy [Vibration] i [MoodooJoesu] głównego celu (maks. 2)</style>\n[WhenUse] Zużywa 5 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +2\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">20%</style> obrażeń\n[WhenUse] Zadaje +<style="highlight">30</style>% obrażeń za każdego celu ataku poniżej wagi ataku tej Umiejętności (w walkach skupionych rozliczane na części)
727. [Umiejętność powiązana 1011703 (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011703].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność powiązana 1011704 (ulepszenia 1,3,4) — nazwa] 통제를위한통제
   źródło: Skills_personality-01.json :: dataList[id=1011704].levelList[level=1].name ; dataList[id=1011704].levelList[level=3].name ; dataList[id=1011704].levelList[level=4].name
   limit: do 50 znaków
   EN: <size=120%>C</size>ONTROLLING<size=120%>O</size>VERSIGHT<size=120%>F</size>OR<size=120%>C</size>ONTROL
   PL: <size=120%>K</size>ONTROLA<size=120%>D</size>LA<size=120%>K</size>ONTROLI
729. [Umiejętność powiązana 1011704 (ulepszenie 1) — opis] [CanDuelGuard]\n\n[StartBattle] 자신의 [ChargeNoirAlly] 횟수 4 증가 (턴당 1회)\n\n[WhenUse] 대상의 [MoodooJoesu] 2당, 코인 위력 +1 (최대 3)
   źródło: Skills_personality-01.json :: dataList[id=1011704].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [ChargeNoirAlly], [WhenUse], [MoodooJoesu]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner
   EN: [CanDuelGuard]\n\n[StartBattle] Gain +4 [ChargeNoirAlly] Count (once per turn)\n\n[WhenUse] Coin Power +1 for every 2 [MoodooJoesu] on target (max 3)
   PL: [CanDuelGuard]\n\n[StartBattle] Zyskuje +4 Licznika [ChargeNoirAlly] (raz na turę)\n\n[WhenUse] Moc Monet +1 za każde 2 [MoodooJoesu] celu (maks. 3)
730. [Umiejętność powiązana 1011704 (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011704].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011704].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011704].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność powiązana 1011704 (ulepszenie 3) — opis] [CanDuelGuard]\n\n[StartBattle] 자신의 [ChargeNoirAlly] 횟수 4 증가 (턴당 1회)\n\n[WhenUse] 대상의 [MoodooJoesu] 2당, 코인 위력 +1 (최대 3)\n\n<style="highlight">[StartDuel] [RuleSanction] 1 얻음 (턴당 1회)</style>\n<style="highlight">[WinDuel] 대상에게 [RuleViolation] 1 부여 (턴당 1회)</style>
   źródło: Skills_personality-01.json :: dataList[id=1011704].levelList[level=3].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [ChargeNoirAlly], [WhenUse], [MoodooJoesu], [StartDuel], [RuleSanction], [WinDuel], [RuleViolation]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [StartDuel] = [합 시작 시] / [Clash Start]; [RuleSanction] = 규칙위반에의하는벌칙 / VIOLENCEFORRULESVIOLATED; [WinDuel] = [합 승리시] / [Clash Win] …
   EN: [CanDuelGuard]\n\n[StartBattle] Gain +4 [ChargeNoirAlly] Count (once per turn)\n\n[WhenUse] Coin Power +1 for every 2 [MoodooJoesu] on target (max 3)\n\n<style="highlight">[StartDuel] Gain 1 [RuleSanction] (once per turn)</style>\n<style="highlight">[WinDuel] Inflict 1 [RuleViolation] (once per turn)</style>
   PL: [CanDuelGuard]\n\n[StartBattle] Zyskuje +4 Licznika [ChargeNoirAlly] (raz na turę)\n\n[WhenUse] Moc Monet +1 za każde 2 [MoodooJoesu] celu (maks. 3)\n\n<style="highlight">[StartDuel] Zyskuje 1 [RuleSanction] (raz na turę)</style>\n<style="highlight">[WinDuel] Nakłada 1 [RuleViolation] na cel (raz na turę)</style>
732. [Umiejętność powiązana 1011704 (ulepszenie 4) — opis] [CanDuelGuard]\n\n[StartBattle] 자신의 [ChargeNoirAlly] 횟수 4 증가 (턴당 1회)\n\n<style="highlight">[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 최종 위력 +1</style>\n[WhenUse] 대상의 [MoodooJoesu] 2당, 코인 위력 +1 (최대 3)\n\n[StartDuel] [RuleSanction] 1 얻음 (턴당 1회)\n[WinDuel] 대상에게 [RuleViolation] 1 부여 (턴당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011704].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [ChargeNoirAlly], [WhenUse], [MoodooJoesu], [StartDuel], [RuleSanction], [WinDuel], [RuleViolation]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [StartDuel] = [합 시작 시] / [Clash Start]; [RuleSanction] = 규칙위반에의하는벌칙 / VIOLENCEFORRULESVIOLATED; [WinDuel] = [합 승리시] / [Clash Win] …
   EN: [CanDuelGuard]\n\n[StartBattle] Gain +4 [ChargeNoirAlly] Count (once per turn)\n\n<style="highlight">[WhenUse] At 3+ [ChargeNoirAlly] Potency, Final Power +1</style>\n[WhenUse] Coin Power +1 for every 2 [MoodooJoesu] on target (max 3)\n\n[StartDuel] Gain 1 [RuleSanction] (once per turn)\n[WinDuel] Inflict 1 [RuleViolation] (once per turn)
   PL: [CanDuelGuard]\n\n[StartBattle] Zyskuje +4 Licznika [ChargeNoirAlly] (raz na turę)\n\n<style="highlight">[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Końcowa +1</style>\n[WhenUse] Moc Monet +1 za każde 2 [MoodooJoesu] celu (maks. 3)\n\n[StartDuel] Zyskuje 1 [RuleSanction] (raz na turę)\n[WinDuel] Nakłada 1 [RuleViolation] na cel (raz na turę)
733. [Umiejętność powiązana 1011705 (ulepszenia 3–4) — nazwa] 퍼니싱 버니싱 피니싱
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].name ; dataList[id=1011705].levelList[level=4].name
   limit: do 50 znaków
   EN: Punishing Burnishing Finishing
   PL: Punishing Burnishing Finishing
734. [Umiejętność powiązana 1011705 (ulepszenie 3) — opis] [CantDuel]\n[WhenUse] 대상의 [Vibration] 위력과 [MoodooJoesu]의 합 4당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +2, 피해량 +20%\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 최종 위력 +1, 피해량 +30%\n\n[EndSkill] [RuleSanction] 3 감소
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Vibration], [MoodooJoesu], [ChargeNoirAlly], [EndSkill], [RuleSanction]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [ChargeNoirAlly] = 보존 / Preservation; [EndSkill] = [공격 종료시] / [Attack End]; [RuleSanction] = 규칙위반에의하는벌칙 / VIOLENCEFORRULESVIOLATED
   EN: [CantDuel]\n[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [MoodooJoesu]) on target (max 2)\n[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +2 and deal +20% damage\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Final Power +1 and deal +30% damage\n\n[EndSkill] Lose 3 [RuleSanction]
   PL: [CantDuel]\n[WhenUse] Moc Końcowa +1 za każde 4 sumy Mocy [Vibration] i [MoodooJoesu] celu (maks. 2)\n[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +2 i zadawać +20% obrażeń\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Końcowa +1 i zadaje +30% obrażeń\n\n[EndSkill] Traci 3 [RuleSanction]
735. [Umiejętność powiązana 1011705 (ulepszenie 3) — moneta 1, efekt 1 — opis] 피해량 +100%
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +100% damage
   PL: Zadaje +100% obrażeń
736. [Umiejętność powiązana 1011705 (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 4 증가
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011705].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność powiązana 1011705 (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność powiązana 1011705 (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=1011705].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność powiązana 1011705 (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 ([MoodooJoesu] x 4)%만큼 타격 피해 (최대 16%, 소수점 버림)
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MoodooJoesu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner
   EN: [OnSucceedAttack] Deal Blunt damage equal to ([MoodooJoesu] x 4)% of this Coin's final damage (max 16%; rounded down)
   PL: [OnSucceedAttack] Zadaje obrażenia Obuchem równe ([MoodooJoesu] × 4)% ostatecznych obrażeń tej monety (maks. 16%; zaokrąglone w dół)
740. [Umiejętność powiązana 1011705 (ulepszenie 4) — opis] [CantDuel]\n[WhenUse] 대상의 [Vibration] 위력과 [MoodooJoesu]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 최종 위력 +2, 피해량 +<style="highlight">40%</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 최종 위력 +<style="highlight">2</style>, 피해량 +<style="highlight">60%</style>\n\n[EndSkill] [RuleSanction] 3 감소
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [Vibration], [MoodooJoesu], [ChargeNoirAlly], [EndSkill], [RuleSanction]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner; [ChargeNoirAlly] = 보존 / Preservation; [EndSkill] = [공격 종료시] / [Attack End]; [RuleSanction] = 규칙위반에의하는벌칙 / VIOLENCEFORRULESVIOLATED
   EN: [CantDuel]\n[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [MoodooJoesu]) on target (max <style="highlight">3</style>)\n[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Final Power +2 and deal +<style="highlight">40</style>% damage\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Final Power +<style="highlight">2</style> and deal +<style="highlight">60</style>% damage\n\n[EndSkill] Lose 3 [RuleSanction]
   PL: [CantDuel]\n[WhenUse] Moc Końcowa +1 za każde 4 sumy Mocy [Vibration] i [MoodooJoesu] celu (maks. <style="highlight">3</style>)\n[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], by zyskać Moc Końcową +2 i zadawać +<style="highlight">40</style>% obrażeń\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Końcowa +<style="highlight">2</style> i zadaje +<style="highlight">60</style>% obrażeń\n\n[EndSkill] Traci 3 [RuleSanction]
741. [Umiejętność powiązana 1011705 (ulepszenie 4) — moneta 1, efekt 1 — opis] 피해량 +<style="highlight">120%</style>
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +<style="highlight">120</style>% damage
   PL: Zadaje +<style="highlight">120</style>% obrażeń
742. [Umiejętność powiązana 1011705 (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Vibration]
743. [Umiejętność powiązana 1011705 (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 ([MoodooJoesu] x <style="highlight">5</style>)%만큼 타격 피해 (최대 <style="highlight">20%</style>, 소수점 버림)
   źródło: Skills_personality-01.json :: dataList[id=1011705].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [MoodooJoesu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MoodooJoesu] = 무두질된 죄수 / Tanned Prisoner
   EN: [OnSucceedAttack] Deal Blunt damage equal to ([MoodooJoesu] x <style="highlight">5</style>)% of this Coin's final damage (max <style="highlight">20%</style>; rounded down)
   PL: [OnSucceedAttack] Zadaje obrażenia Obuchem równe ([MoodooJoesu] × <style="highlight">5</style>)% ostatecznych obrażeń tej monety (maks. <style="highlight">20%</style>; zaokrąglone w dół)
744. [Pasywka bojowa [1011701] — nazwa] 속죄적 엠보싱
   źródło: Passives.json :: dataList[id=1011701].name
   limit: do 40 znaków
   EN: Expiatory Embossing
   PL: Zadośćuczyniące Tłoczenie
745. [Pasywka bojowa [1011701] — opis] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 기본 공격 스킬 사용 시 마지막 코인이 [SuperCoin]으로 변경됨\n\n[MoreJoesu]으로 얻은 [BulletJoesu] 1당, 자신의 체력을 최대 체력의 2%만큼 회복 (턴당 최대 10%)\n- 이 효과로 체력을 초과해서 회복했으면, 초과된 수치만큼 다음 턴에 보호막 얻음
   źródło: Passives.json :: dataList[id=1011701].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [SuperCoin], [MoreJoesu], [BulletJoesu]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [MoreJoesu] = 인력 충원 / Replenish Personnel; [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner
   EN: At 3+ [ChargeNoirAlly] Potency, On Base Attack Skill Use, convert the final Coin to [SuperCoin]\n\nWhen gaining [BulletJoesu] from [MoreJoesu], heal 2% HP for every [BulletJoesu] gained (10% per turn)\n- If this effect healed beyond max HP, gain excess healing as Shield next turn
   PL: Przy 3+ Mocy [ChargeNoirAlly] ostatnia moneta Umiejętności bazowego ataku zamienia się w [SuperCoin] przy użyciu\n\nZa każdy [BulletJoesu] zdobyty przez [MoreJoesu] odzyskuje 2% HP tej jednostki (maks. 10% na turę)\n- Jeżeli ten efekt odzyskał HP ponad Maks., nadwyżkę zyskuje jako Tarczę w następnej turze
746. [Pasywka bojowa [1011702] — nazwa] 원죄적 원피수급
   źródło: Passives.json :: dataList[id=1011702].name
   limit: do 50 znaków
   EN: Reaping Raw Hide: Original Sin Style
   PL: Zbiór Surowej Skóry: W Stylu Grzechu Pierworodnego
747. [Pasywka bojowa [1011702] — opis] 상시 적용: [BulletJoesu] 6개 보유\n\n턴 종료 시 [BulletJoesu]가 6개 미만이면, [MoreJoesu]\n\n[BulletJoesu]를 소모하는 코인 시작 시 [BulletJoesu]가 부족하면, 자신의 최대 체력의 (부족한 수치 x 3)%만큼 체력 피해(보호막 피해 포함)를 받고, 부족한 수치만큼 [BulletJoesu] 얻음\n- 이 효과로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음\n\n전투 중 누적으로 자신의 [ChargeNoirAlly] 횟수를 10 소모할 때마다 [ChargeNoirAlly] 위력 1 얻음
   źródło: Passives.json :: dataList[id=1011702].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [BulletJoesu], [MoreJoesu], [ChargeNoirAlly]
   znaczenie tagów: [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner; [MoreJoesu] = 인력 충원 / Replenish Personnel; [ChargeNoirAlly] = 보존 / Preservation
   EN: Always Active: Begin Encounters with 6 [BulletJoesu]\n\nTurn End: At fewer than 6 [BulletJoesu], [MoreJoesu]\n\nAt Coin Start of a Coin that spends [BulletJoesu], if this unit does not have enough [BulletJoesu], take (missing [BulletJoesu] x 3)% HP damage (including Shield damage) and gain necessary amount of [BulletJoesu] for the Coin\n- This damage does not Stagger or reduce this unit's HP below 1\n\nGain 1 [ChargeNoirAlly] Potency every time this unit consumes 10 cumulative [ChargeNoirAlly] Count in this Encounter
   PL: Zawsze aktywne: Rozpoczyna spotkania z 6 [BulletJoesu]\n\nNa koniec tury przy mniej niż 6 [BulletJoesu] wykonuje [MoreJoesu]\n\nNa początku monety zużywającej [BulletJoesu], jeżeli brakuje [BulletJoesu], otrzymuje (brakująca wartość × 3)% obrażeń HP (wliczając obrażenia Tarczy) i zyskuje brakującą ilość [BulletJoesu]\n- Ten efekt nie powoduje Oszołomienia ani nie obniża HP poniżej 1\n\nZyskuje 1 Mocy [ChargeNoirAlly] za każde skumulowane zużycie 10 Licznika [ChargeNoirAlly] w tym spotkaniu
748. [Pasywka bojowa [1011703] — nazwa] 태너리 규칙
   źródło: Passives.json :: dataList[id=1011703].name
   limit: do 40 znaków
   EN: Rules of the Tannery
   PL: Zasady Tannery
749. [Pasywka bojowa [1011703] — opis] 턴 시작 시 [RuleViolation]이 3인 적이 없으면, 공격 스킬을 장착한 적 1명에게 아래 규칙 중 하나를 무작위로 부여함 (집중 전투면, 무작위 부위에 부여)\n- [RuleDontA]\n- [RuleDontB]\n- [RuleDontC]\n\n규칙은 자신이 가장 최근에 공격한 메인 타겟 적에게 우선 부여하고, 해당 적이 없거나 사망했으면, 본체 최대 체력이 가장 높은 적에게 우선 부여함 (대상 지정 불가능한 적은 제외)\n\n아래 조건 중 하나라도 만족 시 [RuleSanction] 1 얻고, 자신의 [ChargeNoirAlly] 횟수 4 증가\n- 자신이 부여한 규칙을 대상이 어겼을 경우\n- 턴 시작 시 [RuleViolation]이 3인 적이 있는 경우\n\n자신의 [RuleSanction]이 3 이상이면, 자신의 기본 공격 스킬 종료 시 ‘퍼니싱 버니싱 피니싱’으로 전장에 [RuleViolation]이 가장 많은 대상에게 일방 공격함 (턴당 1회, 집중 전투면, 부위로 판정)
   źródło: Passives.json :: dataList[id=1011703].desc
   limit: do 1150 znaków
   tokeny: zachowaj dokładnie: \n, [RuleViolation], [RuleDontA], [RuleDontB], [RuleDontC], [RuleSanction], [ChargeNoirAlly]
   znaczenie tagów: [RuleViolation] = 태너리 규칙 위반 / Tannery Rule Violation; [RuleDontA] = 규칙: 르누아르 지정 금지 / Rule: Targeting Le Noir Prohibited; [RuleDontB] = 규칙: 공격 스킬 지정 금지 / Rule: Targeting Attack Skills Prohibited; [RuleDontC] = 규칙: 수비 스킬 지정 금지 / Rule: Targeting Defense Skills Prohibited; [RuleSanction] = 규칙위반에의하는벌칙 / VIOLENCEFORRULESVIOLATED; [ChargeNoirAlly] = 보존 / Preservation
   EN: Turn Start: If no enemies have 3 [RuleViolation], randomly impose one of the following Rules on 1 enemy that has an Attack Skill equipped (in Focused Encounters, a random Part)\n- [RuleDontA]\n- [RuleDontB]\n- [RuleDontC]\n\nRule imposition prioritizes the enemy this unit most recently attacked as the main target. If no enemies meet that criteria, or if the enemy that does is defeated, prioritizes the enemy that has the highest Core HP (excluding untargetable enemies)\n\nIf any of the following conditions are met, gain 1 [RuleSanction] and +4 [ChargeNoirAlly] Count\n- When the target violates a Rule this unit imposed\n- When there is an enemy that has 3 [RuleViolation] at Turn Start\n\nAt 3+ [RuleSanction], at Base Attack Skill End, use "Punishing Burnishing Finishing" as an Unopposed Attack against the target that has the highest [RuleViolation] on the field (once per turn; in Focused Encounters, the Part)
   PL: Na początku tury, jeżeli żaden wróg nie ma 3 [RuleViolation], nakłada losowo jedną z poniższych zasad na 1 wroga z wyposażoną Umiejętnością ataku (w walkach skupionych: na losową część)\n- [RuleDontA]\n- [RuleDontB]\n- [RuleDontC]\n\nZasada jest nakładana priorytetowo na wroga, którego ta jednostka najpóźniej zaatakowała jako główny cel; jeżeli takiego wroga brak lub zginął, priorytetowo na wroga z najwyższym Maks. HP Rdzenia (poza wrogami niemożliwymi do wskazania)\n\nPrzy spełnieniu któregokolwiek z warunków zyskuje 1 [RuleSanction] i +4 Licznika [ChargeNoirAlly]\n- Gdy cel naruszy zasadę nałożoną przez tę jednostkę\n- Gdy na początku tury istnieje wróg z 3 [RuleViolation]\n\nPrzy 3+ [RuleSanction] na koniec Umiejętności bazowego ataku wykonuje „Punishing Burnishing Finishing” jako Atak bez oporu na celu z największym [RuleViolation] na polu (raz na turę; w walkach skupionych na części)
750. [Pasywka bojowa [1011711] — nazwa] 속죄적 엠보싱
   źródło: Passives.json :: dataList[id=1011711].name
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Pasywka bojowa [1011711] — opis] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 기본 공격 스킬 사용 시 마지막 코인이 [SuperCoin]으로 변경됨\n\n[MoreJoesu]으로 얻은 [BulletJoesu] 1당, 자신의 체력을 최대 체력의 <style="highlight">4%</style>만큼 회복 (턴당 최대 <style="highlight">20%</style>)\n- 이 효과로 체력을 초과해서 회복했으면, 초과된 수치만큼 다음 턴에 보호막 얻음
   źródło: Passives.json :: dataList[id=1011711].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeNoirAlly], [SuperCoin], [MoreJoesu], [BulletJoesu]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [MoreJoesu] = 인력 충원 / Replenish Personnel; [BulletJoesu] = 탄환 - 죄수 / Ammo - Prisoner
   EN: At 3+ [ChargeNoirAlly] Potency, On Base Attack Skill Use, convert the final Coin to [SuperCoin]\n\nWhen gaining [BulletJoesu] from [MoreJoesu], heal <style="highlight">4</style>% HP for every [BulletJoesu] gained (<style="highlight">20</style>% per turn)\n- If this effect healed beyond max HP, gain excess healing as Shield next turn
   PL: Przy 3+ Mocy [ChargeNoirAlly] ostatnia moneta Umiejętności bazowego ataku zamienia się w [SuperCoin] przy użyciu\n\nZa każdy [BulletJoesu] zdobyty przez [MoreJoesu] odzyskuje <style="highlight">4</style>% HP tej jednostki (maks. <style="highlight">20</style>% na turę)\n- Jeżeli ten efekt odzyskał HP ponad Maks., nadwyżkę zyskuje jako Tarczę w następnej turze
752. [Pasywka wsparcia [1011721] — nazwa] 규칙과 법칙의 차이
   źródło: Passives.json :: dataList[id=1011721].name
   limit: do 60 znaków
   EN: The Difference Between a Rule and a Law
   PL: Różnica Między Zasadą a Prawem
753. [Pasywka wsparcia [1011721] — opis] 전투 종료 시 [Charge] 횟수가 가장 적은 아군 [PersonalityCharge] 1명의 [Charge] 횟수 1 증가 (해당 아군 인격이 시지프 소속이면, 대신 [Charge] 횟수 2 증가)\n- 위력이 고정된 특수 [Charge]은 대상에서 제외
   źródło: Passives.json :: dataList[id=1011721].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [PersonalityCharge]
   znaczenie tagów: [Charge] = 충전 / Charge; [PersonalityCharge] = 충전 인격 / Charge ID
   EN: Combat End: 1 allied [PersonalityCharge] that has the lowest [Charge] Count gains +1 [Charge] Count (if the said ally is a "Sisyphe" Identity, it gains +2 [Charge] Count instead)\n- Does not interact with Unique [Charge] that has fixed Potency
   PL: Na koniec walki 1 sojusznik [PersonalityCharge] z najmniejszym Licznikiem [Charge] zyskuje +1 Licznika [Charge] (jeżeli Tożsamość sojusznika należy do Sisyphe, zamiast tego zyskuje +2 Licznika [Charge])\n- Nie wchodzi w interakcje z unikalnym [Charge] o stałej Mocy

## [?] Cheery Chickies Class Captain — Yi Sang — 병아리반 반장
- ID Tożsamości: `400025` (plik: `Personalities-x1p1c1.json`)

754. [Karta Tożsamości — tytuł] 병아리반 반장
   źródło: Personalities-x1p1c1.json :: dataList[id=400025].title
   limit: do 50 znaków
   EN: Cheery Chickies Class Captain
   PL: Przewodniczący Grupy Kurczaczków
755. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities-x1p1c1.json :: dataList[id=400025].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities-x1p1c1.json :: dataList[id=400025].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Karta Tożsamości — opis] 이상의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400025].desc
   limit: do 120 znaków
   EN: Yi Sang's ??? Identity
   PL: Tożsamość Yi Sanga: ???
758. [Pasywka bojowa [40002501] — nazwa] 정보쩐달
   źródło: Passives-x1p1c1.json :: dataList[id=40002501].name
   limit: do 40 znaków
   EN: Infowmashun Weway
   PL: Pszekaz Infomacji
759. [Pasywka bojowa [40002501] — opis] 조작 패널에서 자신의 뒤에 있는 아군 2명에게 피해량 증가 1 부여
   źródło: Passives-x1p1c1.json :: dataList[id=40002501].desc
   limit: do 120 znaków
   EN: Apply 1 Damage Up to 2 allies placed after this unit on the Dashboard.
   PL: Nakłada 1 Wzrostu Obrażeń na 2 sojuszników ustawionych za tą jednostką na panelu
760. [Pasywka bojowa [40002502] — nazwa] 정보쭝화
   źródło: Passives-x1p1c1.json :: dataList[id=40002502].name
   limit: do 40 znaków
   EN: Infowmashun Newtwawiwashun
   PL: Neutwalizacja Infomacji
761. [Pasywka bojowa [40002502] — opis] 정신력이 가장 낮은 아군 1명 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 10 회복
   źródło: Passives-x1p1c1.json :: dataList[id=40002502].desc
   limit: do 120 znaków
   EN: At the end of the turn, Heal 10 SP for 1 ally with the least SP if they lost SP.
   PL: Sojusznik z najniższą Poczytalnością: jeżeli w tej turze stracił Poczytalność, na koniec tury odzyskuje 10 Poczytalności
