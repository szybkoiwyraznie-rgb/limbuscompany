# Paczka AI P44 (Fala 3 · 3A) — Grzesznik 02 — Faust

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P44_3a_02_faust.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P44_3a_02_faust.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #02: Faust (파우스트)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 파우스트
   źródło: Characters.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Faust
   PL: Faust
2. [Akta więźnia — nazwa] 파우스트
   źródło: IntroduceCharacter.json :: dataList[id=파우스트].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Faust — LCB 수감자
- ID Tożsamości: `10201` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 84 · szybkość: 1–3 / 2–3 / 2–4 / 2–4
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: —

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10201].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10201].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10201].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 파우스트의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10201].desc
   limit: do 120 znaków
   EN: Faust’s 1st Identity
   PL: Pierwsza Tożsamość Faust
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 내려베기
   źródło: Skills.json :: dataList[id=1020101].levelList[level=1].name ; dataList[id=1020101].levelList[level=2].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Downward Slash
   PL: Cięcie w Dół
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1020101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 1 [Paralysis]
   PL: [OnSucceedAttackHead] Nakłada 1 Paraliżu
9. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 1 부여
   źródło: Skills.json :: dataList[id=1020101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis]
   PL: [OnSucceedAttack] Nakłada 1 Paraliżu
10. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 올려베기
   źródło: Skills.json :: dataList[id=1020102].levelList[level=1].name ; dataList[id=1020102].levelList[level=2].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Upward Slash
   PL: Cięcie w Górę
11. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1020102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [AttackDown] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 2 Spadku Poziomu Ataku
12. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 3 부여
   źródło: Skills.json :: dataList[id=1020102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spadku Poziomu Ataku
13. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 후벼찌르기
   źródło: Skills.json :: dataList[id=1020103].levelList[level=3].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Drilling Stab
   PL: Wiercące Pchnięcie
14. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1020103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Reduction]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttackHead] Inflict 1 [Reduction] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Spadku Mocy Ataku
15. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1020103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spadku Mocy Ataku
16. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1020104].levelList[level=1].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
17. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Pride) — nazwa] 분석
   źródło: Passives.json :: dataList[id=1020101].name
   limit: do 40 znaków
   EN: Analytic Eye
   PL: Analiza
18. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Pride) — opis] 부정적인 효과가 걸려있는 대상에게 가하는 피해량 +10%
   źródło: Passives.json :: dataList[id=1020101].desc
   limit: do 120 znaków
   EN: Deal +10% damage to targets that have negative status effects
   PL: Zadaje +10% obrażeń celom z negatywnymi efektami
19. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 관찰
   źródło: Passives.json :: dataList[id=1020121].name
   limit: do 40 znaków
   EN: Keen Observation
   PL: Obserwacja
20. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 최대 체력이 가장 높은 아군 1명 공격 적중 시 25% 확률로 공격 레벨 감소 2 부여
   źródło: Passives.json :: dataList[id=1020121].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDown]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: 1 ally that has the highest max HP inflicts 2 [AttackDown] at 25% chance on hit
   PL: 1 Sojusznik z najwyższym Maks. HP: przy trafieniu atakiem z 25% szansą nakłada 2 Spadku Poziomu Ataku

## [00] W Corp. L2 Cleanup Agent — Faust — W사 2등급 정리 요원
- ID Tożsamości: `10202` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 88 · szybkość: 1–3 / 2–3 / 2–4 / 2–4
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge

21. [Karta Tożsamości — tytuł] W사 2등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10202].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L2\nCleanup Agent
   PL: W Corp. L2\nAgentka Oczyszczania
22. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10202].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10202].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Karta Tożsamości — opis] 파우스트의 두번째 인격
   źródło: Personalities.json :: dataList[id=10202].desc
   limit: do 120 znaków
   EN: Faust’s 2nd Identity
   PL: Druga Tożsamość Faust
25. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills.json :: dataList[id=1020201].levelList[level=1].name ; dataList[id=1020201].levelList[level=2].name ; dataList[id=1020201].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Energy Cycle
   PL: Obieg Energii
26. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1020201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 1
27. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika Ładowania
28. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL: [WhenUse] Zyskuje +2 Licznika Ładowania
29. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도약
   źródło: Skills.json :: dataList[id=1020202].levelList[level=1].name ; dataList[id=1020202].levelList[level=2].name ; dataList[id=1020202].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Leap
   PL: Skok
30. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 충전 횟수를 3 소모하여 다음 턴에 속박 4 부여
   źródło: Skills.json :: dataList[id=1020202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1020202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume 3 [Charge] Count to inflict 4 [Binding] next turn
   PL: [OnSucceedAttack] Zużywa 3 Licznika Ładowania, aby w następnej turze nałożyć 4 Spętania
31. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +3 [Charge] Count
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 3
32. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 3
33. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과충전
   źródło: Skills.json :: dataList[id=1020203].levelList[level=3].name ; dataList[id=1020203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 6 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Overcharge
   PL: Nadładowanie
34. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 충전 횟수를 5 소모하여 다음 턴에 공격 위력 감소 2 부여. 마비 3 부여
   źródło: Skills.json :: dataList[id=1020203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1020203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Reduction], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Reduction] = 공격 위력 감소 / Attack Power Down; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Consume 5 [Charge] Count to inflict 2 [Reduction] and 3 [Paralysis] next turn
   PL: [OnSucceedAttack] Zużywa 5 Licznika Ładowania, aby w następnej turze nałożyć 2 Spadku Mocy Ataku. Nakłada 3 Paraliżu
35. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 충전 횟수가 5 이상이면, 합 위력 +2
   źródło: Skills.json :: dataList[id=1020203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 5+ [Charge] Count, Clash Power +2
   PL: Przy 5+ Licznikach Ładowania Moc Starcia +2
36. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1020204].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+2)
   limit: do 40 znaków
   EN: Guard
   PL: Garda
37. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — nazwa] 자가충전
   źródło: Passives.json :: dataList[id=1020201].name
   limit: do 40 znaków
   EN: Self-charging
   PL: Samoładowanie
38. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — opis] 공격 종료 시 충전 횟수 1 증가
   źródło: Passives.json :: dataList[id=1020201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain +1 [Charge] Count at Attack End
   PL: Zyskuje 1 Licznik Ładowania na koniec ataku
39. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 무전
   źródło: Passives.json :: dataList[id=1020221].name
   limit: do 40 znaków
   EN: Radio Comms
   PL: Krótkofalówka
40. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 최대 체력이 가장 낮은 아군 1명 충전 횟수 얻는 값 +1
   źródło: Passives.json :: dataList[id=1020221].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the lowest max HP gains +1 [Charge] Count
   PL: 1 Sojusznik z najniższym Maks. HP: wartość zyskiwanych Liczników Ładowania +1

## [00] Lobotomy Corp. Remnant — Faust — 살아남은 로보토미 직원
- ID Tożsamości: `10203` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 69 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

41. [Karta Tożsamości — tytuł] 살아남은 로보토미 직원
   źródło: Personalities.json :: dataList[id=10203].title
   limit: do 40 znaków
   EN: Lobotomy Corp. Remnant
   PL: Ocalała pracownica Lobotomy Corporation
42. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10203].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10203].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Karta Tożsamości — opis] 파우스트의 세번째 인격
   źródło: Personalities.json :: dataList[id=10203].desc
   limit: do 120 znaków
   EN: Faust’s 3rd Identity
   PL: Trzecia Tożsamość Faust
45. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 단격
   źródło: Skills.json :: dataList[id=1020301].levelList[level=1].name ; dataList[id=1020301].levelList[level=2].name ; dataList[id=1020301].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Sole Strike
   PL: Samotne Uderzenie
46. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1020301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 1 Rozdarcia
47. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1020301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
48. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa Licznik Oddechu o 2
49. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 깊게베기
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].name ; dataList[id=1020302].levelList[level=2].name ; dataList[id=1020302].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Deep Cuts
   PL: Głębokie Cięcia
50. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 1 Oddechu
51. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 2 [Agility] next turn
   PL: [OnSucceedAttackHead] Zyskuje 2 Pośpiechu w następnej turze
53. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] next turn
   PL: [OnSucceedAttack] Zyskuje 1 Oddech w następnej turze
54. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 4 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 4 [Agility] next turn
   PL: [OnSucceedAttack] Zyskuje 4 Pośpiechu w następnej turze
56. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 기회 노리기
   źródło: Skills.json :: dataList[id=1020303].levelList[level=3].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+8)
   limit: do 40 znaków
   EN: Opportunistic Slash
   PL: Celowanie w Okazję
58. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +3
   źródło: Skills.json :: dataList[id=1020303].levelList[level=3].desc
   limit: do 120 znaków
   EN: If this unit took no damage last turn, Coin Power +3
   PL: Gdy ta jednostka nie otrzymała obrażeń w poprzedniej turze, Moc Monet +3
59. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills.json :: dataList[id=1020303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 5 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 5 Rozdarcia
60. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1020304].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — nazwa] 각오
   źródło: Passives.json :: dataList[id=1020301].name
   limit: do 40 znaków
   EN: Resolution
   PL: Postanowienie
62. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — opis] 다음 턴 시작 시 호흡 횟수가 4 이상이면 신속 2를 얻음
   źródło: Passives.json :: dataList[id=1020301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: At the next Turn Start, at 4+ [Breath] Count, gain 2 [Agility]
   PL: Na początku następnej tury przy 4+ Liczniku Oddechu zyskuje 2 Pośpiechu
63. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Lust) — nazwa] 지지
   źródło: Passives.json :: dataList[id=1020321].name
   limit: do 40 znaków
   EN: Backing
   PL: Poparcie
64. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Lust) — opis] 최대 체력이 가장 낮은 아군 1명 수비 스킬의 최종 위력 +2
   źródło: Passives.json :: dataList[id=1020321].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest max HP gains Final Power +2 for its Defense Skills
   PL: 1 Sojusznik z najniższym Maks. HP: Moc Końcowa Umiejętności obrony +2

## [000] The One Who Grips — Faust — 쥐는 자
- ID Tożsamości: `10204` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 66 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

65. [Karta Tożsamości — tytuł] 쥐는 자
   źródło: Personalities.json :: dataList[id=10204].title
   limit: do 40 znaków
   EN: The One Who Grips
   PL: Ta, Która Ściska
66. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10204].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10204].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Karta Tożsamości — opis] 파우스트의 네번째 인격
   źródło: Personalities.json :: dataList[id=10204].desc
   limit: do 120 znaków
   EN: Faust’s 4th Identity
   PL: Czwarta Tożsamość Faust
69. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 광소
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].name ; dataList[id=1020401].levelList[level=2].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Cackle
   PL: Chichot
70. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WinDuel] 대상의 정신력 3 감소
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].desc ; dataList[id=1020401].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Target loses 3 SP
   PL: [WinDuel] Cel traci 3 Poczytalności
71. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 못 1 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict 1 [NailPersonality]
   PL: [OnSucceedAttackHead] Nakłada 1 Gwoździa
72. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
73. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 1 [NailPersonality]
   PL: [OnSucceedAttack] Nakłada 1 Gwoździa
74. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
75. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 쥐어짐
   źródło: Skills.json :: dataList[id=1020402].levelList[level=1].name ; dataList[id=1020402].levelList[level=2].name ; dataList[id=1020402].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: The Gripping
   PL: Ściskanie
76. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 못 3 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1020402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 3 [NailPersonality]
   PL: [OnSucceedAttack] Nakłada 3 Gwoździ
77. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 주시 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [MarkOfHeresy]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [MarkOfHeresy] = 주시 / Gaze
   EN: [OnSucceedAttackHead] Inflict [MarkOfHeresy] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze Spojrzenie
78. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Paraliżu
79. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 주시 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1020402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MarkOfHeresy]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MarkOfHeresy] = 주시 / Gaze
   EN: [OnSucceedAttack] Inflict [MarkOfHeresy] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze Spojrzenie
80. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 2 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [NailPersonality]
   PL: [OnSucceedAttack] Nakłada 2 Gwoździ
81. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 처단
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].name ; dataList[id=1020403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 6 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Execution
   PL: Egzekucja
82. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 이 스킬로 적 처치 시 모든 아군의 정신력을 10 회복시키고, 모든 아군에게 관통 피해량 증가, 타격 피해량 증가 1 부여
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].desc ; dataList[id=1020403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PenetrateDamageUp], [HitDamageUp]
   znaczenie tagów: [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: On kill, heal 10 SP for all allies and apply 1 [PenetrateDamageUp] and [HitDamageUp]
   PL: Po zabiciu wroga tą Umiejętnością sojusznicy odzyskują 10 Poczytalności i zyskują 1 Wzrost Obrażeń Kłucia i Uderzenia
83. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 2 부여
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1020403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 못 2 부여
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1020403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict 2 [NailPersonality]
   PL: [OnSucceedAttackHead] Nakłada 2 Gwoździ
85. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상에게 못이 5 이상 있으면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NailPersonality]
   znaczenie tagów: [NailPersonality] = 못 / Nails
   EN: Deal +50% damage to targets that have 5+ [NailPersonality]
   PL: Jeżeli cel posiada 5+ Gwoździ, Zadaje +50% obrażeń
86. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상에게 못이 5 이상 있으면, 피해량 +70%
   źródło: Skills.json :: dataList[id=1020403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NailPersonality]
   znaczenie tagów: [NailPersonality] = 못 / Nails
   EN: Deal +70% damage to targets that have 5+ [NailPersonality]
   PL: Jeżeli cel posiada 5+ Gwoździ, Zadaje +70% obrażeń
87. [Obrona (ulepszenie 1) — nazwa] 불결하군요
   źródło: Skills.json :: dataList[id=1020404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Such Filth
   PL: Nieczystość
88. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 3 감소
   źródło: Skills.json :: dataList[id=1020404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 3 SP
   PL: [OnSucceedEvade] Cel traci 3 Poczytalności
89. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Lust) — nazwa] 휘파람
   źródło: Passives.json :: dataList[id=1020401].name
   limit: do 40 znaków
   EN: Whistles
   PL: Gwizd
90. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Lust) — opis] 전투 시작 시 정신력이 가장 낮은 아군 2명의 정신력 15 회복.\n대상이 N사 광신도면 광신 1 부여
   źródło: Passives.json :: dataList[id=1020401].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic
   EN: Combat Start: Heal 15 SP for 2 allies that have the lowest SP\nIf the ally is an "N Corp. Fanatic", also apply 1 [AssemblePersonality]
   PL: Na początku walki odzyskuje 15 Poczytalności dla 2 sojuszników z najniższą Poczytalnością.\nJeżeli celem jest Fanatyk Korporacji N, nakłada 1 Fanatyzmu
91. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 속삭임
   źródło: Passives.json :: dataList[id=1020421].name
   limit: do 40 znaków
   EN: Whispers
   PL: Szepty
92. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 전투 시작 시 정신력이 가장 낮은 아군 1명의 정신력 15 회복.\n대상이 N사 광신도면 광신 1 부여
   źródło: Passives.json :: dataList[id=1020421].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic
   EN: Combat Start: Heal 15 SP for 1 ally that has the lowest SP\nIf the ally is an "N Corp. Fanatic", also apply 1 [AssemblePersonality]
   PL: Na początku walki odzyskuje 15 Poczytalności dla 1 sojusznika z najniższą Poczytalnością.\nJeżeli celem jest Fanatyk Korporacji N, nakłada 1 Fanatyzmu

## [00] Zwei Assoc. South Section 4 — Faust — 남부 츠바이 협회 4과
- ID Tożsamości: `10205` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: —

93. [Karta Tożsamości — tytuł] 남부 츠바이 협회\n4과
   źródło: Personalities.json :: dataList[id=10205].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Zwei\nSekcja 4
94. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10205].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10205].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Karta Tożsamości — opis] 파우스트의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10205].desc
   limit: do 120 znaków
   EN: Faust’s 5th Identity
   PL: Piąta Tożsamość Faust
97. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순찰
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=1].name ; dataList[id=1020501].levelList[level=2].name ; dataList[id=1020501].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Patrolling
   PL: Patrol
98. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [DefeatDuel] 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [DefenseUp]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [DefeatDuel] Gain 2 [DefenseUp]
   PL: [DefeatDuel] Zyskuje 2 Wzrosty Poziomu Obrony
99. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttackHead] Gain 2 [DefenseUp] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 2 Wzrosty Poziomu Obrony
100. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [DefeatDuel] 방어 레벨 증가 3을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [DefenseUp]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [DefeatDuel] Gain 3 [DefenseUp]
   PL: [DefeatDuel] Zyskuje 3 Wzrosty Poziomu Obrony
101. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 Wzrosty Poziomu Obrony
102. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 2 증가\n[DefeatDuel] 방어 레벨 증가 3을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Aggro], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Aggro] = 도발치 / Aggro; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn\n[DefeatDuel] Gain 3 [DefenseUp]
   PL: [WhenUse] Zwiększa w następnej turze Prowokację slotu tej Umiejętności o 2\n[DefeatDuel] Zyskuje 3 Wzrosty Poziomu Obrony
103. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 고객 경호
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].name ; dataList[id=1020502].levelList[level=2].name ; dataList[id=1020502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Client Protection
   PL: Ochrona Klienta
104. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 현재 체력 비율이 가장 낮은 아군에게 방어 레벨 증가 2 부여 (턴 당 최대 3회 발동)
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Apply 2 [DefenseUp] to the ally that has the lowest current HP percentage (3 times per turn)
   PL: [WhenUse] Nakłada 2 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP (maks. 3 razy na turę)
105. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttackHead] Gain 1 [DefenseUp] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony
106. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 현재 체력 비율이 가장 낮은 아군에게 방어 레벨 증가 3 부여 (턴 당 최대 3회 발동)\n자신의 방어 레벨 증가 가 5 이상이면, 합 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Apply 3 [DefenseUp] to the ally that has the lowest current HP percentage (3 times per turn)\nAt 5+ [DefenseUp], Clash Power +1
   PL: [WhenUse] Nakłada 3 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP (maks. 3 razy na turę)\nPrzy 5+ Wzrostach Poziomu Obrony Moc Starcia +1
109. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 1 [DefenseUp] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony
110. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 현재 체력 비율이 가장 낮은 아군에게 방어 레벨 증가 4 부여 (턴 당 최대 3회 발동)\n자신의 방어 레벨 증가 가 5 이상이면, 합 위력 +2
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Apply 4 [DefenseUp] to the ally that has the lowest current HP percentage (3 times per turn)\nAt 5+ [DefenseUp], Clash Power +2
   PL: [WhenUse] Nakłada 4 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP (maks. 3 razy na turę)\nPrzy 5+ Wzrostach Poziomu Obrony Moc Starcia +2
113. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 치안 수호
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=3].name ; dataList[id=1020503].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Law and Order
   PL: Porządek Publiczny
114. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 방어 레벨 증가 가 5 이상이면, 코인 위력 +1\n[WinDuel] 체력 2 회복
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefenseUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At 5+ [DefenseUp], Coin Power +1\n[WinDuel] Heal 2 HP
   PL: Przy 5+ Wzrostach Poziomu Obrony Moc Monet +1\n[WinDuel] Odzyskuje 2 HP
115. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] 현재 체력 비율이 가장 낮은 아군에게 다음 턴에 신속 1, 방어 레벨 증가 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1020503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Agility], [DefenseUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Apply 1 [Agility] and 2 [DefenseUp] to the ally that has the lowest current HP percentage next turn
   PL: Nakłada w następnej turze 1 Pośpiechu i 2 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP
116. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 방어 레벨 증가 가 5 이상이면, 코인 위력 +1\n[WinDuel] 체력 4 회복
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefenseUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At 5+ [DefenseUp], Coin Power +1\n[WinDuel] Heal 4 HP
   PL: Przy 5+ Wzrostach Poziomu Obrony Moc Monet +1\n[WinDuel] Odzyskuje 4 HP
117. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] 대상이 츠바이 협회 해결사면, 신속 1, 방어 레벨 증가 1 추가 부여
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [DefenseUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: If the ally is a Zwei Association Fixer, apply an additional 1 [Agility], 1 [DefenseUp]
   PL: Jeżeli celem jest Fikser Stowarzyszenia Zwei, nakłada dodatkowo 1 Pośpiechu i 1 Wzrost Poziomu Obrony
118. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-02.json :: dataList[id=1020504].levelList[level=1].name ; dataList[id=1020504].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] Zwiększa w następnej turze Prowokację slotu tej Umiejętności o 3
120. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — nazwa] 지역 보호
   źródło: Passives.json :: dataList[id=1020501].name
   limit: do 40 znaków
   EN: Territory Protection
   PL: Ochrona Obszaru
121. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — opis] 전투 시작 시 조작 패널에서 양 옆의 아군에게 방어 레벨 증가 2 부여
   źródło: Passives.json :: dataList[id=1020501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: Apply 2 [DefenseUp] to the 2 allies adjacent to this unit on the Dashboard
   PL: Na początku walki nakłada 2 Wzrosty Poziomu Obrony na sojuszników po obu stronach w Panelu Sterowania
122. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — nazwa] 지역 보호
   źródło: Passives.json :: dataList[id=1020511].name
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — opis] 전투 시작 시 조작 패널에서 양 옆의 아군에게 방어 레벨 증가 2 부여\n대상의 체력이 50% 미만이면 추가로 2 부여
   źródło: Passives.json :: dataList[id=1020511].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: Apply 2 [DefenseUp] to the 2 allies adjacent to this unit on the Dashboard\nIf the allies have less than 50% HP, apply an additional 2 [DefenseUp]
   PL: Na początku walki nakłada 2 Wzrosty Poziomu Obrony na sojuszników po obu stronach w Panelu Sterowania.\nJeżeli ich HP jest poniżej 50%, nakłada dodatkowo 2 Wzrosty Poziomu Obrony
124. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Gloom) — nazwa] 보호 요청 수신
   źródło: Passives.json :: dataList[id=1020521].name
   limit: do 40 znaków
   EN: Protection Request Received
   PL: Otrzymano Wezwanie do Ochrony
125. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Gloom) — opis] 전투 시작 시 체력 비율이 가장 낮은 아군 1명에게 방어 레벨 증가 2 부여\n대상의 체력이 50% 미만이면 추가로 2 부여
   źródło: Passives.json :: dataList[id=1020521].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: Apply 2 [DefenseUp] to the ally that has the lowest HP percentage\nIf the ally has less than 50% HP, apply an additional 2 [DefenseUp]
   PL: Na początku walki nakłada 2 Wzrosty Poziomu Obrony na 1 sojusznika z najniższym procentem HP.\nJeżeli jego HP jest poniżej 50%, nakłada dodatkowo 2 Wzrosty Poziomu Obrony

## [000] Seven Assoc. South Section 4 — Faust — 남부 세븐 협회 4과
- ID Tożsamości: `10206` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 76 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

126. [Karta Tożsamości — tytuł] 남부 세븐 협회\n4과
   źródło: Personalities.json :: dataList[id=10206].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Seven\nSekcja 4
127. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10206].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10206].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Karta Tożsamości — opis] 파우스트의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10206].desc
   limit: do 120 znaków
   EN: Faust’s 6th Identity
   PL: Szósta Tożsamość Faust
130. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 예측 분석
   źródło: Skills.json :: dataList[id=1020601].levelList[level=1].name ; dataList[id=1020601].levelList[level=2].name ; dataList[id=1020601].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Predictive Analysis
   PL: Analiza Predykcyjna
131. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1020601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
132. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 3 이상이면 코인 위력 +1
   źródło: Skills.json :: dataList[id=1020601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: If target has 3+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1
   PL: Jeżeli cel ma 3+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color>, Moc Monet +1
133. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 파열 3 당 코인 위력 +1 (최대 2)
   źródło: Skills.json :: dataList[id=1020601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every 3 [Burst] on target (max 2)
   PL: Moc Monet +1 za każde 3 Rozdarcia na celu (maks. 2)
134. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 대상 해체
   źródło: Skills.json :: dataList[id=1020602].levelList[level=1].name ; dataList[id=1020602].levelList[level=2].name ; dataList[id=1020602].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Dissect Target
   PL: Rozbieranie Celu
135. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 3 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 3 Rozdarcia
136. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6 이상 있으면, 다음 턴에 약점 분석 부여
   źródło: Skills.json :: dataList[id=1020602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1020602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, [OnSucceedAttack], [WeaknessAnalysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WeaknessAnalysis] = 약점 분석 / Weakness Analyzed
   EN: [OnSucceedAttack] If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, inflict [WeaknessAnalysis] next turn
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color>, nakłada w następnej turze Analizę Słabości
137. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상에게 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6 이상 있으면 코인 위력 +1\n[WinDuel] 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1\n[WinDuel] Inflict +3 [Burst] Count
   PL: Jeżeli cel ma 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color>, Moc Monet +1\n[WinDuel] Zwiększa Licznik Rozdarcia celu o 3
138. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 파열 6 당 코인 위력 +1 (최대 2)\n[WinDuel] 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every 6 [Burst] on target (max 2)\n[WinDuel] Inflict +3 [Burst] Count
   PL: Moc Monet +1 za każde 6 Rozdarcia na celu (maks. 2)\n[WinDuel] Zwiększa Licznik Rozdarcia celu o 3
140. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 프로파일링
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].name ; dataList[id=1020603].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Profiling
   PL: Profilowanie
141. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 파열 3 당 피해량 +10% (최대 20%)
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Deal +10% damage for every 3 [Burst] on target (max 20%)
   PL: Zadaje +10% obrażeń za każde 3 Rozdarcia na celu (maks. 20%)
142. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
143. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 다음 턴에 신속 1, 참격 위력 증가 1을 얻음
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1020603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Agility], [SlashResultUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: [EndSkill] If target is Staggered or defeated, gain 1 [Agility], 1 [SlashResultUp] next turn
   PL: [EndSkill] Jeżeli cel zostanie Ogłuszony lub zginie, zyskuje w następnej turze 1 Pośpiechu i 1 Wzrost Mocy Cięcia
144. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 파열 3 당 피해량 +10% (최대 50%)\n[WinDuel] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: Deal +10% damage for every 3 [Burst] on target (max 50%)\n[WinDuel] Inflict +2 [Burst] Count
   PL: Zadaje +10% obrażeń za każde 3 Rozdarcia na celu (maks. 50%)\n[WinDuel] Zwiększa Licznik Rozdarcia celu o 2
145. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Obrona (ulepszenia 1,4) — nazwa] 빠르게 해결하죠
   źródło: Skills.json :: dataList[id=1020604].levelList[level=1].name ; dataList[id=1020604].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Let's Wrap It Up
   PL: Załatwmy to szybko
147. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 다음 턴에 신속 1을 얻음 (턴 당 최대 3)
   źródło: Skills.json :: dataList[id=1020604].levelList[level=1].desc ; dataList[id=1020604].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 1 [Agility] next turn (3 times per turn)
   PL: [WhenUse] Zyskuje w następnej turze 1 Pośpiechu (maks. 3 razy na turę)
148. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 차가 식기 전에...
   źródło: Passives.json :: dataList[id=1020601].name
   limit: do 40 znaków
   EN: Before the Tea Cools...
   PL: Zanim Herbata Ostygnie...
149. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 상대의 약점, 취약 속성(내성 1 초과) 으로 공격할 때, 공격 전 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>만큼 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>을 얻음 (턴 당 최대 20)
   źródło: Passives.json :: dataList[id=1020601].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, <sprite name="Breath">, <color=#f8c200>, <link="Breath">, [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: When attacking a target using a damage type the target is "Weak" or "Fatal" (Resistance>x1) to, gain [Breath] equal to [Burst] on target before the attack (max 20 per turn)
   PL: Gdy atakuje atrybutem Słabości lub Wrażliwości (przy odporności powyżej 1), zyskuje przed atakiem <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddech</link></u></color> w liczbie <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color> celu (maks. 20 na turę)
150. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — podsumowanie] 약점, 취약 속성으로 공격할 때, 공격 전 대상의 파열만큼 호흡을 얻음
   źródło: Passives.json :: dataList[id=1020601].summary
   limit: do 160 znaków
   EN: When attacking using a damage type the target is Weak or Fatal to, gain Poise equal to Rupture on target before the attack
   PL: Gdy atakuje atrybutem Słabości lub Wrażliwości, zyskuje przed atakiem Oddech w liczbie Rozdarcia celu
151. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 세븐 협회의 티타임
   źródło: Passives.json :: dataList[id=1020621].name
   limit: do 40 znaków
   EN: Seven Association Tea Time
   PL: Herbatka Stowarzyszenia Seven
152. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 속도가 가장 빠른 아군 1명이 상대의 취약 속성(내성 1.5 초과)으로 공격 시 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>에 비례하여 피해량이 증가\n(파열 1 당 1.5%. 최대 15%)
   źródło: Passives.json :: dataList[id=1020621].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, \n
   EN: 1 ally with the fastest Speed deals +1.5% damage for every <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> on target when attacking using a damage type that the target is "Fatal" (Resistance>x1.5) to (max 15%)
   PL: 1 Sojusznik z najwyższą Szybkością: gdy atakuje atrybutem Wrażliwości (przy odporności powyżej 1.5), zadaje obrażenia proporcjonalnie do <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color> celu\n(Za każde 1 Rozdarcie 1.5%. Maks. 15%)
153. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — podsumowanie] 속도가 가장 빠른 아군 1명이 취약 속성으로 공격 시 대상의 파열에 따라 피해량이 증가
   źródło: Passives.json :: dataList[id=1020621].summary
   limit: do 180 znaków
   EN: 1 ally with the fastest Speed deals more damage based on the target's Rupture when attacking using a damage type the target is Fatal to
   PL: 1 Sojusznik z najwyższą Szybkością: gdy atakuje atrybutem Wrażliwości, zadaje obrażenia proporcjonalnie do Rozdarcia celu
154. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 세븐 협회의 티타임
   źródło: Passives.json :: dataList[id=1020631].name
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — opis] 속도가 가장 빠른 아군 1명이 <style="highlight">약점, 취약 속성(내성 1 초과)</style>으로 공격 시 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>에 비례하여 피해량이 증가\n(파열 1 당 1.5%. 최대 15%)\n<style="highlight">효과를 적용받은 대상이 세븐 협회 해결사면, 피해량 추가 증가\n(파열 1 당 0.5%. 최대 5%)</style>
   źródło: Passives.json :: dataList[id=1020631].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: 1 ally with the fastest Speed deals +1.5% damage for every <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> on target when attacking using a damage type that the target is <style="highlight">"Weak" or "Fatal" (Resistance>x1)</style> to (max 15%)\n\n<style="highlight">If the ally is a Seven Association Fixer, deal additional damage (+0.5% for every [Burst]; max 5%)</style>
   PL: 1 Sojusznik z najwyższą Szybkością: gdy atakuje atrybutem <style="highlight">Słabości lub Wrażliwości (przy odporności powyżej 1)</style>, zadaje obrażenia proporcjonalnie do <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color> celu\n(Za każde 1 Rozdarcie 1.5%. Maks. 15%)\n<style="highlight">Jeżeli sojusznik, który otrzymał ten efekt, jest Fikserem Stowarzyszenia Seven, zadaje dodatkowe obrażenia\n(Za każde 1 Rozdarcie 0.5%. Maks. 5%)</style>
156. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 속도가 가장 빠른 아군 1명이 약점, 취약 속성으로 공격 시 대상의 파열에 따라 피해량이 증가\n대상이 세븐 협회 해결사면, 피해량 추가 증가
   źródło: Passives.json :: dataList[id=1020631].summary
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally with the fastest Speed deals more damage based on the target's Rupture when attacking using a damage type the target is Weak or Fatal to\nIf the ally is a Seven Association Fixer, deal additional damage
   PL: 1 Sojusznik z najwyższą Szybkością: gdy atakuje atrybutem Słabości lub Wrażliwości, zadaje obrażenia proporcjonalnie do Rozdarcia celu\nJeżeli sojusznik jest Fikserem Stowarzyszenia Seven, zadaje dodatkowe obrażenia

## [000] Lobotomy E.G.O::Regret — Faust — 로보토미 E.G.O:: 후회
- ID Tożsamości: `10207` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9101 · HP bazowe: 82 · szybkość: 2–5 / 2–5 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

157. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n후회
   źródło: Personalities.json :: dataList[id=10207].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Regret
   PL: Lobotomy E.G.O::\nSkrucha
158. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10207].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10207].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Karta Tożsamości — opis] 파우스트의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10207].desc
   limit: do 120 znaków
   EN: Faust’s 7th Identity
   PL: Siódma Tożsamość Faust
161. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 조여오는 구속구
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].name ; dataList[id=1020701].levelList[level=2].name ; dataList[id=1020701].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Contracting Straight-jacket
   PL: Ściskające Kajdany
162. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].desc ; dataList[id=1020701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik Wstrząsu o 3
163. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1020701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +3 [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Wstrząsu o 3
164. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Wstrząsu
165. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1020701].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Wstrząsu
166. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 진동 횟수 3 증가\n[DefeatDuel] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n[DefeatDuel] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik Wstrząsu o 3\n[DefeatDuel] Zwiększa własny Licznik Wstrząsu o 3
167. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 금속성 울림
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].name ; dataList[id=1020702].levelList[level=2].name ; dataList[id=1020702].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Metallic Ringing
   PL: Metaliczna Dźwięczność
168. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 진동 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik Wstrząsu o 4
169. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [AttackDown] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Spadku Poziomu Ataku
170. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] Nakłada 4 Wstrząsu
171. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [StartBattle] 자신의 진동 횟수 5를 소모하여 이 스킬의 공격 가중치 +1\n[WhenUse] 자신의 진동 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].desc ; dataList[id=1020702].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 5 [Vibration] Count on self and gain +1 Atk Weight for this Skill\n[WhenUse] Gain +4 [Vibration] Count
   PL: [StartBattle] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1\n[WhenUse] Zwiększa własny Licznik Wstrząsu o 4
172. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 진동 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +1 [Vibration] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik Wstrząsu o 1
173. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] Nakłada 5 Wstrząsu
175. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [PlusCoinValueDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop
   EN: [OnSucceedAttackHead] Inflict 1 [PlusCoinValueDown] next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Osłabienie Monet Plus
176. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spadku Poziomu Ataku
177. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PlusCoinValueDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop
   EN: [OnSucceedAttack] Inflict 1 [PlusCoinValueDown] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Osłabienie Monet Plus
178. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 풀려난 폭력성
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].name ; dataList[id=1020703].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Unleashed Violence
   PL: Uwolniona Brutalność
179. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 자신의 진동 횟수 5를 소모하여 이 스킬의 공격 가중치 +1 (최대 +2)\n[DefeatDuel] 정신력 20 감소\n대상이 보유한 부정적인 효과 1개당 피해량이 3% 증가(최대 15%)\n[EnemyKill] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel], [EnemyKill], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EnemyKill] = [적 처치 시] / [On Kill]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 5 [Vibration] Count on self and gain +1 Atk Weight for this Skill (max +2)\n[DefeatDuel] Lose 20 SP\nDeal +3% damage for every type of negative effect on target (max 15%)\n[EnemyKill] Gain +2 [Vibration] Count
   PL: [StartBattle] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1 (maks. +2)\n[DefeatDuel] Traci 20 Poczytalności\nZadaje +3% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 15%)\n[EnemyKill] Zwiększa własny Licznik Wstrząsu o 2
180. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 20%만큼 분노 피해를 줌.(최대 13)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 20% of the final Stagger Threshold raised by [VibrationExplosion] (max 13)
   PL: [OnSucceedAttack] Wybuch Wstrząsu\nPrzy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 20% końcowego podniesienia Progu Oszołomienia (maks. 13)
181. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 20%만큼 분노 피해를 줌.(최대 13)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 20%만큼 분노 피해를 줌.(최대 13)\n진동 횟수 3 감소
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 20% of the final Stagger Threshold raised by [VibrationExplosion] (max 13)\nReduce [Vibration] Count by 3
   PL: [OnSucceedAttack] Wybuch Wstrząsu\nPrzy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 20% końcowego podniesienia Progu Oszołomienia (maks. 13)\nZmniejsza Licznik Wstrząsu o 3
183. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 자신의 진동 횟수 5를 소모하여 이 스킬의 공격 가중치 +1 (최대 +2)\n[DefeatDuel] 정신력 20 감소\n대상이 보유한 부정적인 효과 1개당 피해량이 6% 증가(최대 30%)\n[EnemyKill] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel], [EnemyKill], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EnemyKill] = [적 처치 시] / [On Kill]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 5 [Vibration] Count on self and gain +1 Atk Weight for this Skill (max +2)\n[DefeatDuel] Lose 20 SP\nDeal +6% damage for every type of negative effect on target (max 30%)\n[EnemyKill] Gain +2 [Vibration] Count
   PL: [StartBattle] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1 (maks. +2)\n[DefeatDuel] Traci 20 Poczytalności\nZadaje +6% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)\n[EnemyKill] Zwiększa własny Licznik Wstrząsu o 2
184. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 30%만큼 분노 피해를 줌.(최대 20)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 30% of the final Stagger Threshold raised by [VibrationExplosion] (max 20)
   PL: [OnSucceedAttack] Wybuch Wstrząsu\nPrzy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 30% końcowego podniesienia Progu Oszołomienia (maks. 20)
185. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 30%만큼 분노 피해를 줌.(최대 20)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 30%만큼 분노 피해를 줌.(최대 20)\n진동 횟수 3 감소
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 30% of the final Stagger Threshold raised by [VibrationExplosion] (max 20)\nReduce [Vibration] Count by 3
   PL: [OnSucceedAttack] Wybuch Wstrząsu\nPrzy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 30% końcowego podniesienia Progu Oszołomienia (maks. 20)\nZmniejsza Licznik Wstrząsu o 3
187. [Obrona (ulepszenia 1,4) — nazwa] 앙금 쌓기
   źródło: Skills_personality-02.json :: dataList[id=1020704].levelList[level=1].name ; dataList[id=1020704].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Gathering Spite
   PL: Narastająca Uraza
188. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020704].levelList[level=1].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 진동 횟수 6 증가
   źródło: Skills_personality-02.json :: dataList[id=1020704].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +6 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik Wstrząsu o 6
190. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Wrath) — nazwa] 떠밀린 후회
   źródło: Passives.json :: dataList[id=1020701].name
   limit: do 40 znaków
   EN: Coerced Regret
   PL: Wymuszona Skrucha
191. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Wrath) — opis] - 합 진행 시 대상이 보유한 부정적인 효과가 3개 이상이면, 대상의 합 위력 -1\n- 자신이 생존해있을 때, [VibrationExplosion]을 당하는 적이 방어 레벨 감소 2를 얻음. (턴 당 적 1명당 최대 1회)\n- 정신 오염: 턴 종료 시 정신력이 -25 미만일 때 다음 턴에 속박 2,  타격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1020701].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [DefenseDown], [Binding], [HitResultUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Binding] = 속박 / Bind; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: - In a Clash, if target has 3+ types of negative effect, target's Clash Power -1\n- When this unit is alive, enemies affected by [VibrationExplosion] gain 2 [DefenseDown] (once per enemy per turn)\n- Mental Corruption: If at less than -25 SP at Turn End, gain 2 [Binding] and 1 [HitResultUp] next turn
   PL: - Podczas Starcia: jeżeli cel ma 3+ rodzajów negatywnych efektów, Moc Starcia celu -1\n- Dopóki ta jednostka żyje, wróg dotknięty [VibrationExplosion] zyskuje 2 Spadki Poziomu Obrony (maks. 1 raz na turę na wroga)\n- Skażenie Umysłu: jeżeli na koniec tury Poczytalność jest poniżej -25, zyskuje w następnej turze 2 Spętania i 1 Wzrost Mocy Uderzenia
192. [Pasywka bojowa (od ulepszenia 4, posiadane 6× Wrath) — nazwa] 떠밀린 후회
   źródło: Passives.json :: dataList[id=1020711].name
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Pasywka bojowa (od ulepszenia 4, posiadane 6× Wrath) — opis] - 합 진행 시 대상이 보유한 부정적인 효과 3개 당 대상의 합 위력 -1 (최대 2)\n- 자신이 생존해있을 때, [VibrationExplosion]을 당하는 적이 방어 레벨 감소 2를 얻음 (턴 당 적 1명당 최대 3회)\n- 정신 오염: 턴 종료 시 정신력이 -25 미만일 때 다음 턴에 속박 2,  타격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1020711].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [DefenseDown], [Binding], [HitResultUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Binding] = 속박 / Bind; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: - In a Clash, target's Clash Power -1 for every 3 types of negative effect it has (max -2 Clash Power)\n- When this unit is alive, enemies affected by [VibrationExplosion] gain 2 [DefenseDown] (3 times per enemy per turn)\n- Mental Corruption: If at less than -25 SP at Turn End, gain 2 [Binding] and 1 [HitResultUp] next turn
   PL: - Podczas Starcia: Moc Starcia celu -1 za każde 3 rodzaje negatywnych efektów (maks. -2 Moc Starcia)\n- Dopóki ta jednostka żyje, wróg dotknięty [VibrationExplosion] zyskuje 2 Spadki Poziomu Obrony (maks. 3 razy na turę na wroga)\n- Skażenie Umysłu: jeżeli na koniec tury Poczytalność jest poniżej -25, zyskuje w następnej turze 2 Spętania i 1 Wzrost Mocy Uderzenia
194. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 억압 작업
   źródło: Passives.json :: dataList[id=1020721].name
   limit: do 40 znaków
   EN: Repression Work
   PL: Praca Tłumiąca
195. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 속도가 가장 느린 아군 1명이 합 진행 시 대상이 보유한 부정적인 효과가 3개 이상이면, 대상의 합 위력 -1
   źródło: Passives.json :: dataList[id=1020721].desc
   limit: do 160 znaków
   EN: In a Clash, if the target of the ally with the slowest Speed has 3+ types of negative effect, target's Clash Power -1
   PL: Gdy 1 Sojusznik z najniższą Szybkością prowadzi Starcie, jeżeli jego cel ma 3+ rodzajów negatywnych efektów, Moc Starcia celu -1

## [000] Blade Lineage Salsu — Faust — 검계 살수
- ID Tożsamości: `10208` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 76 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise, Bleed

196. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=10208].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL: Ród Ostrza\nSalsu
197. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10208].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10208].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Karta Tożsamości — opis] 파우스트의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10208].desc
   limit: do 120 znaków
   EN: Faust’s 8th Identity
   PL: Ósma Tożsamość Faust
200. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 월하검무
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=1].name ; dataList[id=1020801].levelList[level=2].name ; dataList[id=1020801].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Moonlit Blade Dance
   PL: Taniec Ostrza przy Księżycu
201. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=1].desc ; dataList[id=1020801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
202. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1020801].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020801].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 1 [RedApricotBlossom]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [RedApricotBlossom]
203. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 1 [Breath]
204. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 5 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 5+ [Breath], Coin Power +1</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Przy 5+ [Breath] Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
205. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 자법
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].name ; dataList[id=1020802].levelList[level=2].name ; dataList[id=1020802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Acupuncture
   PL: Akupunktura
206. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].desc ; dataList[id=1020802].levelList[level=2].desc
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
208. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 2 [RedApricotBlossom]
   PL: [CriticalOnSucceedAttack] Nakłada 2 [RedApricotBlossom]
209. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika [Breath]
210. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1020802].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +30% damage on Critical Hit
   PL: Zadaje +30% obrażeń przy trafieniu krytycznym
211. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spętania
212. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 2 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1020802].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 2 [RedApricotBlossom]<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Nakłada 2 [RedApricotBlossom]<style="highlight"></style>
213. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 7 이상이면, 코인 위력 +1\n</style>[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 7+ [Breath], Coin Power +1\n</style>[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Przy 7+ [Breath] Moc Monet +1\n</style>[WhenUse] Zwiększa własny Licznik [Breath] o 2
214. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 흩날리는 홍매화
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].name ; dataList[id=1020803].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Red Plum Blossoms Scatter
   PL: Rozsypane Kwiaty Śliwy
215. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [RedApricotBlossom] 1 당 피해량 +3%\n[WinDuel] 자신의 [Breath] 횟수를 절반 감소하고, 감소한 양만큼 [Breath]을 얻음. (최대 10)
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [RedApricotBlossom], [WinDuel], [Breath]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: Deal +3% damage for every [RedApricotBlossom] on target\n[WinDuel] Consume half the [Breath] Count on self, then gain [Breath] equal to the [Breath] Count consumed (max 10)
   PL: Zadaje +3% obrażeń za każdy 1 [RedApricotBlossom] na celu\n[WinDuel] Zużywa połowę własnego Licznika [Breath], po czym zyskuje [Breath] w liczbie zużytego Licznika (maks. 10)
216. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 5 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1020803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 5 [RedApricotBlossom]
   PL: [CriticalOnSucceedAttack] Nakłada 5 [RedApricotBlossom]
217. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 5 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1020803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [RedApricotBlossom] 1 당 피해량 +3%\n<style="highlight">자신의 [Breath] 7 당 코인 위력 +1 (최대 3)</style>\n[WinDuel] 자신의 [Breath] 횟수를 절반 감소하고, 감소한 양만큼 [Breath]을 얻음. (최대 10)\n<style="highlight">이 스킬로 크리티컬 적중 시 [RedApricotBlossom]가 감소하지 않음</style>
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedApricotBlossom], [Breath], [WinDuel]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Deal +3% damage for every [RedApricotBlossom] on target\n<style="highlight">Coin Power +1 for every 7 [Breath] on self (max 3)</style>\n[WinDuel] Consume half the [Breath] Count on self, then gain [Breath] equal to the [Breath] Count consumed (max 10)\n<style="highlight">This Skill does not consume [RedApricotBlossom] On Crit</style>
   PL: Zadaje +3% obrażeń za każdy 1 [RedApricotBlossom] na celu\n<style="highlight">Moc Monet +1 za każde 7 [Breath] (maks. 3)</style>\n[WinDuel] Zużywa połowę własnego Licznika [Breath], po czym zyskuje [Breath] w liczbie zużytego Licznika (maks. 10)\n<style="highlight">Trafienia krytyczne tą Umiejętnością nie zużywają [RedApricotBlossom]</style>
219. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 대상의 [RedApricotBlossom]가 10이면, 참격 취약 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom], [SlashTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [CriticalOnSucceedAttack] If target has 10 [RedApricotBlossom], inflict 1 [SlashTakeDamageUp]
   PL: [CriticalOnSucceedAttack] Jeżeli cel ma 10 [RedApricotBlossom], nakłada 1 Wrażliwość na Cięcie
220. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 대상의 [RedApricotBlossom]가 10이면, 참격 취약 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Obrona (ulepszenia 1,4) — nazwa] 흘려내기
   źródło: Skills_personality-02.json :: dataList[id=1020804].levelList[level=1].name ; dataList[id=1020804].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Redirect
   PL: Przekierowanie
222. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 4 당 최종 위력 +1 (최대 3)
   źródło: Skills_personality-02.json :: dataList[id=1020804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] For every 4 [Breath] on self, gain Final Power +1 (max 3)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Breath] (maks. 3)
223. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 4 당 최종 위력 +1 (최대 5)
   źródło: Skills_personality-02.json :: dataList[id=1020804].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] For every 4 [Breath] on self, gain Final Power +1 (max 5)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Breath] (maks. 5)
224. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 매화 같이 터져나오는 피
   źródło: Passives.json :: dataList[id=1020801].name
   limit: do 40 znaków
   EN: Sanguine Plum Blossoms
   PL: Krwawe Kwiaty Śliwy
225. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 크리티컬 적중 시 [RedApricotBlossom] 1 부여. (최대 3회)
   źródło: Passives.json :: dataList[id=1020801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedApricotBlossom]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: On Crit, inflict 1 [RedApricotBlossom] (max 3 times)
   PL: Przy trafieniu krytycznym nakłada 1 [RedApricotBlossom] (maks. 3 razy)
226. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — nazwa] 매화 같이 터져나오는 피
   źródło: Passives.json :: dataList[id=1020811].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — opis] 크리티컬 적중 시 [RedApricotBlossom] 1 부여. 대상의 [RedApricotBlossom]가 10이면, 대신 방어 레벨 감소 1 부여 (최대 6회)
   źródło: Passives.json :: dataList[id=1020811].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [RedApricotBlossom], [DefenseDown]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: On Crit, inflict 1 [RedApricotBlossom]\nIf target has 10 [RedApricotBlossom], inflict 1 [DefenseDown] instead (max 6 times)
   PL: Przy trafieniu krytycznym nakłada 1 [RedApricotBlossom]. Jeżeli cel ma 10 [RedApricotBlossom], nakłada zamiast tego 1 Spadek Poziomu Obrony (maks. 6 razy)
228. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 미련 서린 검끝
   źródło: Passives.json :: dataList[id=1020821].name
   limit: do 40 znaków
   EN: Lingering Bladepoint
   PL: Ostrze Karmione Żalem
229. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 편성 순서가 가장 빠른 아군이 참격 속성 스킬로 크리티컬 적중 시 방어 레벨 감소 1 부여 (턴 당 적 1명당 최대 3)
   źródło: Passives.json :: dataList[id=1020821].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [DefenseDown]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When the ally with the earliest Deployment order hits Critically using a Slash Skill, inflict 1 [DefenseDown] (max 3 times per enemy per turn)
   PL: Gdy sojusznik z pierwszą kolejnością przydziału trafi krytycznie Umiejętnością Cięcia, nakłada 1 Spadek Poziomu Obrony (maks. 3 razy na turę na wroga)

## [00] Wuthering Heights Butler — Faust — 워더링하이츠 버틀러
- ID Tożsamości: `10209` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

230. [Karta Tożsamości — tytuł] 워더링하이츠\n버틀러
   źródło: Personalities.json :: dataList[id=10209].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wuthering Heights\nButler
   PL: Wichrowe Wzgórza\nKamerdyner
231. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10209].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10209].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Karta Tożsamości — opis] 파우스트의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10209].desc
   limit: do 120 znaków
   EN: Faust's 9th Identity
   PL: Dziewiąta Tożsamość Faust
234. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 압수
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=1].name ; dataList[id=1020901].levelList[level=2].name ; dataList[id=1020901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Confiscation
   PL: Konfiskata
235. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 2 [Sinking]
236. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
237. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Coin Power +1
   PL: [WhenUse] Jeżeli cel ma 6+ [Sinking], Moc Monet +1
238. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 불청객 맞이
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=1].name ; dataList[id=1020902].levelList[level=2].name ; dataList[id=1020902].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Interloper Reception
   PL: Powitanie Natręta
239. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Sinking] o 2
240. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 , 합 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Clash Power +1
   PL: [WhenUse] Jeżeli cel ma 5+ [Sinking], Moc Starcia +1
241. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
242. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 , 합 위력 +1\n[WhenUse] 대상의 [Sinking] 횟수가 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Clash Power +1\n[WhenUse] If target has 3+ [Sinking] Count, Coin Power +1
   PL: [WhenUse] Jeżeli cel ma 5+ [Sinking], Moc Starcia +1\n[WhenUse] Jeżeli cel ma 3+ Licznik [Sinking], Moc Monet +1
243. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
244. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 접객도 4식 봉심
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].name ; dataList[id=1020903].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Reception Arts 4: Heartseal
   PL: Sztuka Gościny 4: Pieczęć Serca
245. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1020903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [EchoOfMansion] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1020903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: [OnSucceedAttack] Inflict 2 [EchoOfMansion] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [EchoOfMansion]
247. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상에게 [EchoOfMansion]가 있으면, [Sinking] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1020903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has [EchoOfMansion], inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Jeżeli cel ma [EchoOfMansion], zwiększa Licznik [Sinking] o 3
248. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] 횟수가 5 이상이면, 코인 위력 +2
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking] Count, Coin Power +2
   PL: [WhenUse] Jeżeli cel ma 5+ Licznik [Sinking], Moc Monet +2
249. [Obrona (ulepszenia 1,4) — nazwa] 사냥 대비
   źródło: Skills_personality-02.json :: dataList[id=1020904].levelList[level=1].name ; dataList[id=1020904].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Hunting Plans
   PL: Przygotowanie do Polowania
250. [Obrona (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 10 이상이면, 코인 위력 +3
   źródło: Skills_personality-02.json :: dataList[id=1020904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 10+ [Sinking], Coin Power +3
   PL: [WhenUse] Jeżeli cel ma 10+ [Sinking], Moc Monet +3
251. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 10 이상이면, 코인 위력 +7
   źródło: Skills_personality-02.json :: dataList[id=1020904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 10+ [Sinking], Coin Power +7
   PL: [WhenUse] Jeżeli cel ma 10+ [Sinking], Moc Monet +7
252. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — nazwa] 버틀러식 대응
   źródło: Passives.json :: dataList[id=1020901].name
   limit: do 40 znaków
   EN: Butler Style Response
   PL: Reakcja według Kamerdynera
253. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — opis] - 합 승리 시 대상에게 [Sinking] 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1020901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: - Clash Win: Inflict 1 [Sinking] on target (3 times per turn)
   PL: - Po wygranym Starciu nakłada na cel 1 [Sinking] (3 razy na turę)
254. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — podsumowanie] 합 승리 시 [Sinking] 1 부여
   źródło: Passives.json :: dataList[id=1020901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Clash Win: Inflict 1 [Sinking]
   PL: Po wygranym Starciu nakłada 1 [Sinking]
255. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — nazwa] 버틀러식 대응
   źródło: Passives.json :: dataList[id=1020911].name
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — opis] - 합 승리 시 대상에게 [Sinking] 1 부여 (턴 당 3회)\n- 대상에게 [EchoOfMansion]가 있으면 대신 3 부여
   źródło: Passives.json :: dataList[id=1020911].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [EchoOfMansion]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: - Clash Win: Inflict 1 [Sinking] on target (3 times per turn)\n- If the target has [EchoOfMansion], inflict 3 [Sinking] instead
   PL: - Po wygranym Starciu nakłada na cel 1 [Sinking] (3 razy na turę)\n- Jeżeli cel ma [EchoOfMansion], nakłada zamiast tego 3 [Sinking]
257. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — podsumowanie] 합 승리 시 [Sinking] 1 부여
   źródło: Passives.json :: dataList[id=1020911].summary
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 그 날을 위한 훈련
   źródło: Passives.json :: dataList[id=1020921].name
   limit: do 40 znaków
   EN: Anticipatory Training
   PL: Trening na Ten Dzień
259. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명이 [Sinking]이 5 이상 부여된 대상에게 공격 적중 시 자신의 정신력 2 회복 (턴 당 4회)
   źródło: Passives.json :: dataList[id=1020921].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally that has the lowest SP hits an enemy that has 5+ [Sinking], the ally heals 2 SP On Hit (4 times per turn)
   PL: Gdy 1 Sojusznik z najniższą Poczytalnością trafi wroga z 5+ [Sinking], odzyskuje 2 Poczytalności (4 razy na turę)
260. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — podsumowanie] 조건 만족 시 정신력 회복
   źródło: Passives.json :: dataList[id=1020921].summary
   limit: do 120 znaków
   EN: Conditional SP healing
   PL: Warunkowe odzyskiwanie Poczytalności
261. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Gloom) — nazwa] 그 날을 위한 훈련
   źródło: Passives.json :: dataList[id=1020931].name
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명이 [Sinking]이 5 이상 부여된 대상에게 공격 적중 시 자신의 정신력 3 회복 (턴 당 4회)
   źródło: Passives.json :: dataList[id=1020931].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally that has the lowest SP hits an enemy that has 5+ [Sinking], the ally heals 3 SP On Hit (4 times per turn)
   PL: Gdy 1 Sojusznik z najniższą Poczytalnością trafi wroga z 5+ [Sinking], odzyskuje 3 Poczytalności (4 razy na turę)
263. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Gloom) — podsumowanie] 조건 만족 시 정신력 회복
   źródło: Passives.json :: dataList[id=1020931].summary
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [000] MultiCrack Office Rep — Faust — 멀티크랙 사무소 대표
- ID Tożsamości: `10210` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge

264. [Karta Tożsamości — tytuł] 멀티크랙 사무소\n대표
   źródło: Personalities.json :: dataList[id=10210].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: MultiCrack Office\nRep
   PL: Biuro MultiCrack\nSzefowa
265. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10210].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10210].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Karta Tożsamości — opis] 파우스트의 열번째 인격
   źródło: Personalities.json :: dataList[id=10210].desc
   limit: do 120 znaków
   EN: Faust's 10th Identity
   PL: Dziesiąta Tożsamość Faust
268. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 40Y-3 가동
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=1].name ; dataList[id=1021001].levelList[level=2].name ; dataList[id=1021001].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: 40Y-3 Activation
   PL: Aktywacja 40Y-3
269. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1
   PL: [WhenUse] Zużywa 5 Licznika [Charge], aby zyskać Moc Monet +1
270. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2
271. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL: [WhenUse] Zużywa 5 Licznika [Charge], aby zyskać Moc Monet +1<style="highlight"></style>
272. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o <style="highlight">3</style>
273. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 <style="highlight">+2</style>
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power <style="highlight">+2</style>
   PL: [WhenUse] Zużywa 5 Licznika [Charge], aby zyskać Moc Monet <style="highlight">+2</style>
274. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 3<style="highlight"></style>
275. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 충전 역류
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=1].name ; dataList[id=1021002].levelList[level=2].name ; dataList[id=1021002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Charge Countercurrent
   PL: Wsteczny Prąd Ładowania
276. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL: [WhenUse] Jeżeli Licznik [Charge] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Charge])% Maks. HP, aby zwiększyć Licznik [Charge] do 10\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet +1
277. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 3 이상이면, 보유한 [Charge] 횟수를 전부 소모하여 이 스킬로 소모한 [Charge] 횟수당 피해량 +([Charge])% (최대 60%)
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +([Charge])% damage for every [Charge] Count consumed by this Skill (max 60%)
   PL: Jeżeli Rezonans (z tą Umiejętnością włącznie) wynosi 3 lub więcej, zużywa cały posiadany Licznik [Charge] i zadaje +([Charge])% obrażeń za każdy 1 [Charge] zużyty tą Umiejętnością (maks. 60%)
278. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL: [WhenUse] Jeżeli Licznik [Charge] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Charge])% Maks. HP, aby zwiększyć Licznik [Charge] do 10\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet +1<style="highlight"></style>
279. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 3 이상이면, 보유한 [Charge] 횟수를 전부 소모하여 이 스킬로 소모한 [Charge] 횟수당 피해량 +<style="highlight">([Charge] + 3)% (최대 120%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +<style="highlight">([Charge] + 3)</style>% damage for every [Charge] Count consumed by this Skill (max <style="highlight">120%</style>)
   PL: Jeżeli Rezonans (z tą Umiejętnością włącznie) wynosi 3 lub więcej, zużywa cały posiadany Licznik [Charge] i zadaje obrażenia +<style="highlight">([Charge] + 3)</style>% za każdy 1 [Charge] zużyty tą Umiejętnością (maks. <style="highlight">120%</style>)
280. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 <style="highlight">+2</style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power <style="highlight">+2</style>
   PL: [WhenUse] Jeżeli Licznik [Charge] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Charge])% Maks. HP, aby zwiększyć Licznik [Charge] do 10\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet <style="highlight">+2</style>
281. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 3 이상이면, 보유한 [Charge] 횟수를 전부 소모하여 이 스킬로 소모한 [Charge] 횟수당 피해량 +<style="highlight">([Charge] + 4)% (최대 180%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +<style="highlight">([Charge] + 4)</style>% damage for every [Charge] Count consumed by this Skill (max <style="highlight">180%</style>)
   PL: Jeżeli Rezonans (z tą Umiejętnością włącznie) wynosi 3 lub więcej, zużywa cały posiadany Licznik [Charge] i zadaje obrażenia +<style="highlight">([Charge] + 4)</style>% za każdy 1 [Charge] zużyty tą Umiejętnością (maks. <style="highlight">180%</style>)
282. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 40Y-3 충전
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].name ; dataList[id=1021003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: 40Y-3 Charge
   PL: Ładowanie 40Y-3
283. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [Charge]이 2 이상이면, 코인 위력 +2
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 2+ [Charge], Coin Power +2
   PL: Przy 2+ [Charge] Moc Monet +2
284. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] + 4)만큼 자신의 [Charge] 횟수 증가 (최대 7)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + 4) [Charge] Count (max 7)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o ([Charge] + 4) (maks. 7)
285. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] ([Charge] + 4)만큼 자신의 [Charge] 횟수 증가 (최대 7)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [Charge]이 3 이상이면, [Charge]당 피해량 +4% (최대 20%)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ [Charge], deal +4% damage for every [Charge] (max 20%)
   PL: Przy 3+ [Charge] zadaje +4% obrażeń za każdy 1 [Charge] (maks. 20%)
287. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[Charge]당 코인 위력 +1 (최대 4)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: <style="highlight">Coin Power +1 for every [Charge] (max 4)</style>
   PL: <style="highlight">Moc Monet +1 za każdy 1 [Charge] (maks. 4)</style>
288. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] + <style="highlight">5</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + <style="highlight">5</style>) [Charge] Count (max <style="highlight">8</style>)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o ([Charge] + <style="highlight">5</style>) (maks. <style="highlight">8</style>)
289. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] ([Charge] + <style="highlight">5</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [Charge]이 3 이상이면, [Charge]당 피해량 <style="highlight">+8%</style> (최대 <style="highlight">40%</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ [Charge], deal <style="highlight">+8%</style> damage for every [Charge] (max <style="highlight">40%</style>)
   PL: Przy 3+ [Charge] zadaje <style="highlight">+8%</style> obrażeń za każdy 1 [Charge] (maks. <style="highlight">40%</style>)
291. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 질투 취약 1 부여\n- [Charge]이 2 이상이면, 추가로 1 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Charge], [VioletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [VioletTakeDamageUp] = 질투 취약 / Envy Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [VioletTakeDamageUp] next turn\n- At 2+ [Charge], inflict 1 additional [VioletTakeDamageUp]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada w następnej turze 1 Wrażliwość na Zazdrość\n- Przy 2+ [Charge] nakłada dodatkowo 1 Wrażliwość na Zazdrość</style>
292. [Obrona (ulepszenia 1,4) — nazwa] 충전
   źródło: Skills_personality-02.json :: dataList[id=1021004].levelList[level=1].name ; dataList[id=1021004].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Charge
   PL: Ładowanie
293. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가 (턴 당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count (2 times per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Charge] o 2 (2 razy na turę)
294. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수 <style="highlight">4</style> 증가 (턴 당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021004].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +<style="highlight">4</style> [Charge] Count (2 times per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Charge] o <style="highlight">4</style> (2 razy na turę)
295. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 전류 해체
   źródło: Passives.json :: dataList[id=1021001].name
   limit: do 40 znaków
   EN: Electrocurrent Dismantling
   PL: Rozkład Prądem
296. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n[Charge]이 2 이상이면, 피해량이 ([Charge] x 3)%만큼 증가 (최대 15%)\n\n적을 처치하면 자신과 [Charge] 횟수가 가장 적은 아군 1명이 [Charge]만큼 [Charge] 횟수 증가 (최대 3, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021001].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nAt 2+ [Charge], deal +([Charge] x 3)% damage (max 15%)\n\nOn Kill, this unit and 1 ally that has the lowest [Charge] Count gain [Charge] Count equal to [Charge] (max 3, prioritizes allies that consume or gain [Charge])
   PL: Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\nPrzy 2+ [Charge] zadaje +([Charge] x 3)% obrażeń (maks. 15%)\n\nPrzy zabiciu wroga ta jednostka i 1 Sojusznik z najniższym Licznikiem [Charge] zyskują Licznik [Charge] równy [Charge] (maks. 3; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Charge])
297. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음\n[Charge] 2 이상이면, 피해량 증가\n적 처치 시, 자신과 아군 1명 [Charge] 횟수 증가
   źródło: Passives.json :: dataList[id=1021001].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] with every 10 [Charge] Count consumption\nAt 2+ [Charge], deal more damage\nOn Kill, this unit and 1 ally gain [Charge] Count
   PL: Zużywając 10 Licznika [Charge], zyskuje [Charge]\nPrzy 2+ [Charge] zadaje więcej obrażeń\nPrzy zabiciu wroga ta jednostka i 1 Sojusznik zyskują Licznik [Charge]
298. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 전류 해체
   źródło: Passives.json :: dataList[id=1021011].name
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n[Charge]이 2 이상이면, 피해량이 ([Charge] x 3)%만큼 증가 (최대 15%)\n<style="highlight">- 대상의 체력이 50% 미만이면 ([Charge] x 5)%만큼 추가로 증가 (최대 25%)</style>\n\n적을 처치하면 자신과 [Charge] 횟수가 가장 적은 아군 <style="highlight">2</style>명이 <style="highlight">(2 + [Charge])</style>만큼 [Charge] 횟수 증가 (최대 <style="highlight">5</style>, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021011].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nAt 2+ [Charge], deal +([Charge] x 3)% damage (max 15%)\n<style="highlight">- If the target is at less than 50% HP, deal +([Charge] x 5)% more damage (max 25%)</style>\n\nOn Kill, this unit and <style="highlight">2 allies</style> that have the lowest [Charge] Count gain [Charge] Count equal to <style="highlight">([Charge] + 2)</style> (max <style="highlight">5</style>, prioritizes allies that consume or gain [Charge])
   PL: Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\nPrzy 2+ [Charge] zadaje +([Charge] x 3)% obrażeń (maks. 15%)\n<style="highlight">- Jeżeli cel ma poniżej 50% HP, zadaje dodatkowo +([Charge] x 5)% obrażeń (maks. 25%)</style>\n\nPrzy zabiciu wroga ta jednostka i <style="highlight">2</style> Sojuszników z najniższym Licznikiem [Charge] zyskują Licznik [Charge] równy <style="highlight">(2 + [Charge])</style> (maks. <style="highlight">5</style>; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Charge])
300. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음\n[Charge] 2 이상이면, 피해량이 증가\n적 처치 시, 자신과 아군 2명 [Charge] 횟수 증가
   źródło: Passives.json :: dataList[id=1021011].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] with every 10 [Charge] Count consumption\nAt 2+ [Charge], deal more damage\nOn Kill, this unit and 2 allies gain [Charge] Count
   PL: Zużywając 10 Licznika [Charge], zyskuje [Charge]\nPrzy 2+ [Charge] zadaje więcej obrażeń\nPrzy zabiciu wroga ta jednostka i 2 Sojuszników zyskują Licznik [Charge]
301. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 해체 보조 전류
   źródło: Passives.json :: dataList[id=1021021].name
   limit: do 50 znaków
   EN: Auxiliary Dismantling Current
   PL: Pomocniczy Prąd Rozkładu
302. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] [Charge] 횟수가 가장 낮은 아군 1명이 적 처치 시 [Charge] 횟수 2 증가 (턴 당 1회, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021021].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When 1 ally that has the lowest [Charge] Count kills an enemy, the ally gains +2 [Charge] Count (once per turn, prioritizes allies that consume or gain [Charge])
   PL: Gdy 1 Sojusznik z najniższym Licznikiem [Charge] zabije wroga, zyskuje 2 Licznika [Charge] (1 raz na turę; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Charge])
303. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — nazwa] 해체 보조 전류
   źródło: Passives.json :: dataList[id=1021031].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — opis] [Charge] 횟수가 가장 낮은 아군 1명이 적 처치 시 [Charge] 횟수 3 증가 (턴 당 1회, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021031].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When 1 ally that has the lowest [Charge] Count kills an enemy, the ally gains +3 [Charge] Count (once per turn, prioritizes allies that consume or gain [Charge])
   PL: Gdy 1 Sojusznik z najniższym Licznikiem [Charge] zabije wroga, zyskuje 3 Licznika [Charge] (1 raz na turę; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Charge])

## [000] LCE E.G.O:: Ardor Blossom Star — Faust — LCE E.G.O:: 홍염살
- ID Tożsamości: `10211` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

305. [Karta Tożsamości — tytuł] LCE E.G.O::\n홍염살
   źródło: Personalities.json :: dataList[id=10211].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCE E.G.O::\nArdor Blossom\nStar
   PL: LCE E.G.O::\nGwiazda Żarzącego Kwiatu
306. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10211].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10211].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Karta Tożsamości — opis] 파우스트의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10211].desc
   limit: do 120 znaków
   EN: Faust's 11th Identity
   PL: Jedenasta Tożsamość Faust
309. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 착화
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].name ; dataList[id=1021101].levelList[level=2].name ; dataList[id=1021101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Ignition
   PL: Zapłon
310. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain 7 [Combustion] and +1 [Combustion] Count
   PL: [WhenUse] Przy 10+ [Combustion] zadaje +10% obrażeń\n[WhenUse] Zyskuje 7 [Combustion] i zwiększa własny Licznik [Combustion] o 1
311. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
312. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1021101].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1021101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 2 [Combustion]
   PL: [OnSucceedAttack] Zyskuje 2 [Combustion]
313. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain 7 [Combustion] and +1 [Combustion] Count\n[WhenUse] At 10+ ([Combustion] on self + [Combustion] on target), Coin Power +1
   PL: [WhenUse] Przy 10+ [Combustion] zadaje +10% obrażeń\n[WhenUse] Zyskuje 7 [Combustion] i zwiększa własny Licznik [Combustion] o 1\n[WhenUse] Przy 10+ ([Combustion] własnej + [Combustion] celu) Moc Monet +1
316. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]자신의 [Combustion]이 10 이상이면, [Combustion] 1 추가 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] At 10+ [Combustion], inflict additional 1 [Combustion]</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 10+ [Combustion] nakłada dodatkowo 1 [Combustion]</style>
317. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1021101].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 2 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [Combustion]<style="highlight"></style>
318. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain 7 [Combustion] and +1 [Combustion] Count\n[WhenUse] Coin Power +1 for every 10 ([Combustion] on self + [Combustion] on target) (max 2)
   PL: [WhenUse] Przy 10+ [Combustion] zadaje +10% obrażeń\n[WhenUse] Zyskuje 7 [Combustion] i zwiększa własny Licznik [Combustion] o 1\n[WhenUse] Moc Monet +1 za każde 10 ([Combustion] własnej + [Combustion] celu) (maks. 2)
319. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Combustion]이 10 이상이면, [Combustion] <style="highlight">3</style> 추가 부여
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] At 10+ [Combustion], inflict additional <style="highlight">3</style> [Combustion]
   PL: [OnSucceedAttack] Przy 10+ [Combustion] nakłada dodatkowo <style="highlight">3</style> [Combustion]
320. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] E.G.O 홍염살 전개
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].name ; dataList[id=1021102].levelList[level=2].name ; dataList[id=1021102].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: E.G.O - A.B.S Activation
   PL: E.G.O Gwiazda Żarzącego Kwiatu
321. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] 자신의 [Combustion] 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain +4 [Combustion] Count
   PL: Przy 10+ [Combustion] zadaje +10% obrażeń\n[WhenUse] Zwiększa własny Licznik [Combustion] o 4
322. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021102].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1021102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
325. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Combustion]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 2 [Combustion]
326. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 [Combustion] 10 당, 피해량 +10% (최대 20%)\n[WhenUse] 자신의 [Combustion] 횟수 4 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 4 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: Deal +10% damage for every 10 [Combustion] on self (max 20%)\n[WhenUse] Gain +4 [Combustion] Count\n[WhenUse] At 4+ ([Combustion] on self + [Combustion] on target), Coin Power +1
   PL: Zadaje +10% obrażeń za każde 10 [Combustion] (maks. 20%)\n[WhenUse] Zwiększa własny Licznik [Combustion] o 4\n[WhenUse] Przy 4+ ([Combustion] własnej + [Combustion] celu) Moc Monet +1
327. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1021102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Combustion]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 3 [Combustion]
328. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 [Combustion] 10 당, 피해량 +10% (최대 20%)\n[WhenUse] 자신의 [Combustion] 횟수 4 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 4 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: Deal +10% damage for every 10 [Combustion] on self (max 20%)\n[WhenUse] Gain +4 [Combustion] Count\n[WhenUse] Coin Power +1 for every 4 ([Combustion] on self + [Combustion] on target) (max 2)
   PL: Zadaje +10% obrażeń za każde 10 [Combustion] (maks. 20%)\n[WhenUse] Zwiększa własny Licznik [Combustion] o 4\n[WhenUse] Moc Monet +1 za każde 4 ([Combustion] własnej + [Combustion] celu) (maks. 2)
329. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Combustion]이 15 이상이면, [Combustion] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 15+ [Combustion], inflict +2 [Combustion] Count on target
   PL: [OnSucceedAttack] Jeżeli cel ma 15+ [Combustion], zwiększa Licznik [Combustion] celu o 2
330. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 불에 끌리는 마음으로
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].name ; dataList[id=1021103].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Drawn by Flame
   PL: Pociągnięta Płomieniem
331. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[BeforeUse] 자신의 [Combustion]이 30 이상이면, ‘홍염살 최대 감응 【열화침식】’으로 발동\n자신의 [Combustion] 5 당, 피해량 +7.5% (최대 30%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 이상이면, 기본 위력 +1\n[WhenUse] 자신의 잃은 체력이 30% 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Combustion], [BeforeUse], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Combustion] = 화상 / Burn; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 7 [Combustion] and +1 [Combustion] Count\n[BeforeUse] At 30+ [Combustion], activate "A.B.S Max Attunement 【Degraded Corrosion】" instead\nDeal +7.5% damage for every 5 [Combustion] on self (max 30%)\n[WhenUse] At 10+ ([Combustion] on self + [Combustion] on target), Base Power +1\n[WhenUse] If this unit is missing 30%+ HP, Coin Power +1
   PL: [StartBattle] Zyskuje 7 [Combustion] i zwiększa własny Licznik [Combustion] o 1\n[BeforeUse] Przy 30+ [Combustion] zamiast tego uruchamia „Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】”\nZadaje +7.5% obrażeń za każde 5 [Combustion] (maks. 30%)\n[WhenUse] Przy 10+ ([Combustion] własnej + [Combustion] celu) Moc Bazowa +1\n[WhenUse] Jeżeli brakuje tej jednostce 30%+ HP, Moc Monet +1
332. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1021103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]
333. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1021103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[BeforeUse] 자신의 [Combustion]이 30 이상이면, ‘홍염살 최대 감응 【열화침식】’으로 발동\n자신의 [Combustion] 5 당, 피해량 +12.5% (최대 50%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 잃은 체력 30% 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=4].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Combustion], [BeforeUse], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Combustion] = 화상 / Burn; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 7 [Combustion] and +1 [Combustion] Count\n[BeforeUse] At 30+ [Combustion], activate "A.B.S Max Attunement 【Degraded Corrosion】" instead\nDeal +12.5% damage for every 5 [Combustion] on self (max 50%)\n[WhenUse] Base Power +1 for every 10 ([Combustion] on self + [Combustion] on target) (max 2)\n[WhenUse] For every 30% missing HP on this unit, Coin Power +1 (max 2)
   PL: [StartBattle] Zyskuje 7 [Combustion] i zwiększa własny Licznik [Combustion] o 1\n[BeforeUse] Przy 30+ [Combustion] zamiast tego uruchamia „Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】”\nZadaje +12.5% obrażeń za każde 5 [Combustion] (maks. 50%)\n[WhenUse] Moc Bazowa +1 za każde 10 ([Combustion] własnej + [Combustion] celu) (maks. 2)\n[WhenUse] Moc Monet +1 za każde 30% brakującego HP tej jednostki (maks. 2)
335. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 홍염살 최대 감응 【열화침식】
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].name ; dataList[id=1021105].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: A.B.S Max Attunement 【Degraded Corrosion】
   PL: Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】
336. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 이 스킬 공격 종료 시 사망함.\n- 이 스킬을 사용하는 동안 체력이 1이 되면, 체력이 1로 유지됨.\n[WhenUse] 자신의 [Combustion] 5 당 피해량 +7.5% (최대 30%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 이상이면, 기본 위력 +1\n[WhenUse] 자신의 잃은 체력 30% 당, 코인 위력 +1 (최대 2)\n[BeforeAttack] 자신의 잃은 체력 20% 당, 공격 가중치 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: This unit dies after using this Skill\n- If HP drops to 1 while using this Skill, maintains HP at 1 for the duration of the Skill\n[WhenUse] Deal +7.5% damage for every 5 [Combustion] on self (max 30%)\n[WhenUse] At 10+ ([Combustion] on self + [Combustion] on target), Base Power +1\n[WhenUse] Coin Power +1 for every 30% missing HP on self (max 2)\n[BeforeAttack] Atk Weight +1 for every 20% missing HP on self (max 2)
   PL: Ta jednostka umiera po zakończeniu ataku tą Umiejętnością.\n- Jeżeli podczas używania tej Umiejętności HP spadnie do 1, pozostaje na poziomie 1 do końca działania Umiejętności.\n[WhenUse] Zadaje +7.5% obrażeń za każde 5 [Combustion] (maks. 30%)\n[WhenUse] Przy 10+ ([Combustion] własnej + [Combustion] celu) Moc Bazowa +1\n[WhenUse] Moc Monet +1 za każde 30% brakującego HP tej jednostki (maks. 2)\n[BeforeAttack] Waga ataku +1 za każde 20% brakującego HP tej jednostki (maks. 2)
337. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021105].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021105].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 잃은 체력 20% 당, 피해량 +10% (최대 30%)
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1021105].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +10% damage for every 20% missing HP on self (max 30%)
   PL: [OnSucceedAttack] Zadaje +10% obrażeń za każde 20% brakującego HP tej jednostki (maks. 30%)
343. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬 공격 종료 시 사망함.\n- 이 스킬을 사용하는 동안 체력이 1이 되면, 체력이 1로 유지됨.\n[WhenUse] 자신의 [Combustion] 5 당 피해량 +12.5% (최대 50%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 잃은 체력 30% 당, 코인 위력 +1 (최대 3)\n[BeforeAttack] 자신의 잃은 체력 20% 당, 공격 가중치 +1 (최대 4)
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: This unit dies after using this Skill\n- If HP drops to 1 while using this Skill, maintains HP at 1 for the duration of the Skill\n[WhenUse] Deal +12.5% damage for every 5 [Combustion] on self (max 50%)\n[WhenUse] Base Power +1 for every 10 ([Combustion] on self + [Combustion] on target) (max 2)\n[WhenUse] Coin Power +1 for every 30% missing HP on self (max 3)\n[BeforeAttack] Atk Weight +1 for every 20% missing HP on self (max 4)
   PL: Ta jednostka umiera po zakończeniu ataku tą Umiejętnością.\n- Jeżeli podczas używania tej Umiejętności HP spadnie do 1, pozostaje na poziomie 1 do końca działania Umiejętności.\n[WhenUse] Zadaje +12.5% obrażeń za każde 5 [Combustion] (maks. 50%)\n[WhenUse] Moc Bazowa +1 za każde 10 ([Combustion] własnej + [Combustion] celu) (maks. 2)\n[WhenUse] Moc Monet +1 za każde 30% brakującego HP tej jednostki (maks. 3)\n[BeforeAttack] Waga ataku +1 za każde 20% brakującego HP tej jednostki (maks. 4)
344. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL: [OnSucceedAttack] Nakłada 4 [Combustion]
345. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Obrona (ulepszenia 1,4) — nazwa] 홍염살의 감응도를 올려 공명하겠습니다.
   źródło: Skills_personality-02.json :: dataList[id=1021104].levelList[level=1].name ; dataList[id=1021104].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 60 znaków
   EN: Resonating by Raising A.B.S Attunement.
   PL: Rezonans przez Dostrojenie Gwiazdy Żarzącego Kwiatu.
347. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Combustion] 5 감소 (턴 당 1회)\n[OnSucceedEvade] 자신의 [Combustion] 5 감소 (턴 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021104].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] Lose 5 [Combustion] (once per turn)\n[OnSucceedEvade] Lose 5 [Combustion] (once per turn)
   PL: [WhenUse] Traci 5 [Combustion] (1 raz na turę)\n[OnSucceedEvade] Traci 5 [Combustion] (1 raz na turę)
348. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 코인 위력 +3\n[WhenUse] 자신의 [Combustion] 5 감소 (턴 당 1회)\n[OnSucceedEvade] 자신의 [Combustion] 5 감소 (턴 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021104].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] At 10+ [Combustion], Coin Power +3\n[WhenUse] Lose 5 [Combustion] (once per turn)\n[OnSucceedEvade] Lose 5 [Combustion] (once per turn)
   PL: [WhenUse] Przy 10+ [Combustion] Moc Monet +3\n[WhenUse] Traci 5 [Combustion] (1 raz na turę)\n[OnSucceedEvade] Traci 5 [Combustion] (1 raz na turę)
349. [Pasywka bojowa (od ulepszenia 1) — nazwa] 내화
   źródło: Passives.json :: dataList[id=1021101].name
   limit: do 40 znaków
   EN: Fireproof
   PL: Ognioodporność
350. [Pasywka bojowa (od ulepszenia 1) — opis] [Combustion] 피해로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음.
   źródło: Passives.json :: dataList[id=1021101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Cannot be Staggered or fall below 1 HP due to [Combustion] damage
   PL: Nie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Combustion].
351. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — nazwa] 불나방
   źródło: Passives.json :: dataList[id=1021111].name
   limit: do 40 znaków
   EN: Flame Moth
   PL: Ćma Płomieni
352. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — opis] 전투 시작 시 자신의 잃은 체력이 80% 이상이고 [Combustion]이 30 미만이면, [Combustion]을 30까지 얻음. (스테이지 당 1회)\n\n턴 종료 시 자신의 [Combustion] 6당, 다음 턴에 [AttackUp] 1 얻음 (최대 5)\n\n사망 시 아래의 효과 발동\n- 모든 적에게 [Combustion] 2 부여. 자신의 [Combustion]을 나누어 부여 (1명당 최대 3)\n- 가장 부족한 속성의 E.G.O 자원 2종 2개씩 획득\n\n홍염살 최대 감응 【열화침식】 스킬의 효과로 사망하였으면, 효과가 강화됨\n- 모든 적에게 [Combustion] 3 부여. 자신의 [Combustion]을 나누어 부여 (1명당 최대 5)\n- 가장 부족한 속성의 E.G.O 자원 2종 2개씩 획득\n- 자신의 [Combustion]이 30 이상이었으면, 대기 해제되는 인원 1명에게 [AttackUp] 3 부여
   źródło: Passives.json :: dataList[id=1021111].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [AttackUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Combat Start: At 80%+ missing HP, and at less than 30 [Combustion], gain up to 30 [Combustion] (once per Encounter)\n\nTurn End: Gain 1 [AttackUp] next turn for every 6 [Combustion] on self (max 5)\n\nOn death, activate the following:\n- Inflict 2 [Combustion] on all enemies and inflict this unit's [Combustion] between all enemies (max 3 per enemy)\n- Gain 2 E.G.O resource for the 2 least-owned Affinities\n\nIf this unit died due to the A.B.S. Max Attunement 【Degraded Corrosion】 Skill, enhance the effect:\n- Inflict 3 [Combustion] on all enemies and inflict this unit's [Combustion] between all enemies (max 5 per enemy)\n- Gain 2 E.G.O resource for 2 least-owned E.G.O resources\n- If this unit had 30+ [Combustion], apply 3 [AttackUp] to 1 ally that Substitutes in
   PL: Na początku walki, jeżeli brakuje tej jednostce 80%+ HP i [Combustion] jest poniżej 30, zyskuje [Combustion] do 30. (1 raz na spotkanie)\n\nNa koniec tury zyskuje w następnej turze 1 [AttackUp] za każde 6 [Combustion] (maks. 5)\n\nPo śmierci uruchamia następujące efekty:\n- Nakłada 2 [Combustion] na wszystkich wrogów i dzieli własne [Combustion] między nich (maks. 3 na wroga)\n- Zyskuje po 2 zasoby E.G.O dla 2 atrybutów o najmniejszym stanie\n\nJeżeli ta jednostka umarła wskutek efektu Umiejętności „Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】”, efekt jest wzmocniony:\n- Nakłada 3 [Combustion] na wszystkich wrogów i dzieli własne [Combustion] między nich (maks. 5 na wroga)\n- Zyskuje po 2 zasoby E.G.O dla 2 atrybutów o najmniejszym stanie\n- Jeżeli ta jednostka miała 30+ [Combustion], nakłada 3 [AttackUp] na 1 Sojusznika wchodzącego z rezerwy
353. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 잔열
   źródło: Passives.json :: dataList[id=1021121].name
   limit: do 40 znaków
   EN: Residual Heat
   PL: Ciepło Resztkowe
354. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 정신력이 가장 낮은 아군 1명이 기본 스킬의 적중시 효과로 [Combustion]을 부여할 때 [Combustion] 2 추가 부여 (최대 3회 발동)\n- 피격 대상의 [Combustion]이 30 이상이면, 대신 [Combustion] 횟수 1 증가 (최대 3회 발동)
   źródło: Passives.json :: dataList[id=1021121].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally that has the lowest SP inflicts [Combustion] with a Base Skill's On Hit effect, inflict 2 additional [Combustion] (max 3 times)\n- If the target the ally is attacking has 30+ [Combustion], inflict +1 [Combustion] Count instead (max 3 times)
   PL: Gdy 1 Sojusznik z najniższą Poczytalnością nakłada [Combustion] efektem trafienia Umiejętności podstawowej, nakłada dodatkowo 2 [Combustion] (maks. 3 razy)\n- Jeżeli atakowany cel ma 30+ [Combustion], zamiast tego zwiększa Licznik [Combustion] o 1 (maks. 3 razy)

## [000] Heishou Pack - Mao Branch Adept — Faust — 흑수 - 묘 필두
- ID Tożsamości: `10212` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 76 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

355. [Karta Tożsamości — tytuł] 흑수 - 묘 필두
   źródło: Personalities.json :: dataList[id=10212].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heishou Pack -\nMao Branch Adept
   PL: Wataha Heishou -\nGałąź Mao, Adept
356. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10212].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10212].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Karta Tożsamości — opis] 파우스트의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10212].desc
   limit: do 120 znaków
   EN: Faust's 12th Identity
   PL: Dwunasta Tożsamość Faust
359. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순보
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].name ; dataList[id=1021201].levelList[level=2].name ; dataList[id=1021201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Blinkstep
   PL: Szybki Krok
360. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1
   PL: [WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1
361. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
362. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
363. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[WinDuel] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[WinDuel] Inflict +1 [Burst] Count</style>
   PL: [WhenUse] Jeżeli cel ma <style="highlight">4</style>+ [Burst], Moc Monet +1\n<style="highlight">[WinDuel] Zwiększa Licznik [Burst] o 1</style>
364. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
365. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
366. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)</style>
367. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1</style>\n[WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1\n[WinDuel] Zwiększa Licznik [Burst] o 1
368. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)<style="highlight"></style>
369. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 길을 뚫겠습니다. 주군.
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].name ; dataList[id=1021202].levelList[level=2].name ; dataList[id=1021202].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Clearing the Path, My Lord.
   PL: Przedrę drogę, mój Panie.
370. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL: [WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1\n[WinDuel] Zwiększa Licznik [Burst] o 1
371. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상에게 [BurstAgility] 또는 [BurstZilu]가 있으면, 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstAgility], [BurstZilu]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: If target has [BurstAgility] or [BurstZilu], deal +30% damage
   PL: Jeżeli cel ma [BurstAgility] lub [BurstZilu], zadaje +30% obrażeń
373. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)</style>\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Agility], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 4+ [Burst], Coin Power +1\n<style="highlight">[WhenUse] Gain 2 [Agility] next turn (once per turn)</style>\n[WinDuel] Inflict +1 [Burst] Count
   PL: [WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1\n<style="highlight">[WhenUse] Zyskuje w następnej turze 2 [Agility] (1 raz na turę)</style>\n[WinDuel] Zwiększa Licznik [Burst] o 1
374. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 대상에게 [BurstAgility] 또는 [BurstZilu]가 있으면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BurstAgility], [BurstZilu]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: If target has [BurstAgility] or [BurstZilu], deal +30% damage<style="highlight"></style>
   PL: Jeżeli cel ma [BurstAgility] lub [BurstZilu], zadaje +30% obrażeń<style="highlight"></style>
376. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 자신의 [EnhanceZilu])%만큼 피해량이 증가 (최대 50%)</style>\n<style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1</style>\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EnhanceZilu], [WhenUse], [Burst], [Agility], [WinDuel]
   znaczenie tagów: [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">If this unit's Speed is faster than the target's, deal +(Speed difference x [EnhanceZilu] on self)% damage (max 50%)</style>\n<style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] If target has 4+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Inflict +1 [Burst] Count
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x własne [EnhanceZilu])% obrażeń (maks. 50%)</style>\n<style="highlight">Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1\n[WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1</style>\n[WhenUse] Zyskuje w następnej turze 2 [Agility] (1 raz na turę)\n[WinDuel] Zwiększa Licznik [Burst] o 1
377. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Burst]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Burst]</style>
378. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] 대상에게 [BurstAgility] 또는 [BurstZilu]가 있으면, 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BurstAgility], [BurstZilu]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: If target has [BurstAgility] or [BurstZilu], deal <style="highlight">+50%</style> damage
   PL: Jeżeli cel ma [BurstAgility] lub [BurstZilu], zadaje <style="highlight">+50%</style> obrażeń
379. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 눈으로도 귀로도 쫓지 못하게.
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].name ; dataList[id=1021203].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Traceless to Sight and Sound Alike.
   PL: Ani oko, ani ucho nie dogoni.
380. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [StartBattle], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[BeforeUse] At 10+ [EnhanceZilu], activate "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\nJeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[BeforeUse] Przy 10+ [EnhanceZilu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”\n[WhenUse] Zyskuje 3 [LegStrength]\n[WinDuel] Zwiększa Licznik [Burst] o 2
381. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL: [OnSucceedAttack] Nakłada [BurstAgility]
383. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +30% damage
   PL: Przy 10+ Szybkości zadaje +30% obrażeń
385. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] Nakłada 3 [Burst]
386. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)
   PL: [OnSucceedAttack] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)
387. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)</style>\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n<style="highlight">[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1</style>\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [StartBattle], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[BeforeUse] At 10+ [EnhanceZilu], activate "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n<style="highlight">[WhenUse] If target has 15+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\n<style="highlight">Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)</style>\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[BeforeUse] Przy 10+ [EnhanceZilu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”\n<style="highlight">[WhenUse] Jeżeli cel ma 15+ [Burst], Moc Monet +1</style>\n[WhenUse] Zyskuje 3 [LegStrength]\n[WinDuel] Zwiększa Licznik [Burst] o 2
388. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [BurstAgility]<style="highlight"></style>
390. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +30% damage<style="highlight"></style>
   PL: Przy 10+ Szybkości zadaje +30% obrażeń<style="highlight"></style>
392. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Burst]<style="highlight"></style>
393. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstAgility]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict [BurstAgility]</style>
   PL: <style="highlight">[ReUseOnSucceedAttack] Nakłada [BurstAgility]</style>
395. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 흑수 묘 오의 - 운해현현
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].name ; dataList[id=1021205].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 90 znaków
   EN: Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation
   PL: Wyższy Heishou - Technika Mao: Objawienie Morza Chmur
396. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1\n[WhenUse] 자신의 속도가 10 이상이면 [Breath]을 20 얻고, 자신의 [Breath] 횟수가 4 미만이면, [Breath] 횟수를 최대 4 까지 얻음\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가\n[EndSkill] [EnhanceZilu] 10 소모
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [Breath], [LegStrength], [WinDuel], [EndSkill], [EnhanceZilu]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst], Coin Power +1\n[WhenUse] At 10+ Speed, gain 20 [Breath]; if this unit has less than 4 [Breath] Count, raise [Breath] Count up to 4\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count\n[EndSkill] Consume 10 [EnhanceZilu]
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\nJeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1\n[WhenUse] Jeżeli cel ma 15+ [Burst], Moc Monet +1\n[WhenUse] Przy 10+ Szybkości zyskuje 20 [Breath]; jeżeli Licznik [Breath] jest poniżej 4, zyskuje Licznik [Breath] do maks. 4\n[WhenUse] Zyskuje 3 [LegStrength]\n[WinDuel] Zwiększa Licznik [Burst] o 2\n[EndSkill] Zużywa 10 [EnhanceZilu]
397. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstZilu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [OnSucceedAttack] Inflict [BurstZilu]
   PL: [OnSucceedAttack] Nakłada [BurstZilu]
399. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [BurstZilu]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [ReUseOnSucceedAttack] Inflict [BurstZilu]
   PL: [ReUseOnSucceedAttack] Nakłada [BurstZilu]
405. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)</style>\n<style="highlight">[WhenUse] 대상의 [Burst] 10 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 속도가 10 이상이면 [Breath]을 20 얻고, 자신의 [Breath] 횟수가 4 미만이면, [Breath] 횟수를 최대 4 까지 얻음\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가\n[EndSkill] [EnhanceZilu] 10 소모
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [Breath], [LegStrength], [WinDuel], [EndSkill], [EnhanceZilu]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n<style="highlight">[WhenUse] Coin Power +1 for every 10 [Burst] on target (max 2)</style>\n[WhenUse] At 10+ Speed, gain 20 [Breath]; if this unit has less than 4 [Breath] Count, raise [Breath] Count up to 4\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count\n[EndSkill] Consume 10 [EnhanceZilu]
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\n<style="highlight">Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)</style>\n<style="highlight">[WhenUse] Moc Monet +1 za każde 10 [Burst] na celu (maks. 2)</style>\n[WhenUse] Przy 10+ Szybkości zyskuje 20 [Breath]; jeżeli Licznik [Breath] jest poniżej 4, zyskuje Licznik [Breath] do maks. 4\n[WhenUse] Zyskuje 3 [LegStrength]\n[WinDuel] Zwiększa Licznik [Burst] o 2\n[EndSkill] Zużywa 10 [EnhanceZilu]
406. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstZilu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [OnSucceedAttack] Inflict [BurstZilu]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [BurstZilu]<style="highlight"></style>
408. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BurstAgility] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] [BurstZilu] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstZilu]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [ReUseOnSucceedAttack] Inflict [BurstZilu]<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Nakłada [BurstZilu]<style="highlight"></style>
414. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 5 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Obrona (ulepszenia 1,4) — nazwa] 존명.
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].name ; dataList[id=1021204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: It Shall Be Done.
   PL: Zostanie to wykonane.
416. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 공격 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] [LegStrength] 3 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [SupportProtect], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[WhenUse] This Skill gains +1 Offense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Gain 3 [LegStrength]
   PL: [DuelCounter]\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[WhenUse] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)\n[WhenUse] Zyskuje 3 [LegStrength]
417. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 공격 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] [LegStrength] 3 얻음\n<style="highlight">[WhenUse] 자신의 속도가 대상보다 높을수록 기본 위력 +1 (속도 차이 2당 기본 위력 +1. 최대 2)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [SupportProtect], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[WhenUse] This Skill gains +1 Offense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Gain 3 [LegStrength]\n<style="highlight">[WhenUse] If this unit's Speed is faster than the target's by 2 or more, gain Base Power based on Speed difference (Base Power +1 for every 2 Speed difference; max 2)</style>
   PL: [DuelCounter]\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[WhenUse] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)\n[WhenUse] Zyskuje 3 [LegStrength]\n<style="highlight">[WhenUse] Zyskuje Moc Bazową zależnie od przewagi Szybkości (Moc Bazowa +1 za każde 2 różnicy Szybkości; maks. 2)</style>
420. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Obrona (ulepszenia 1,4) — nazwa] 초속호위
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=1].name ; dataList[id=1021206].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Swiftfeet Protection
   PL: Ochrona Zwinnych Stóp
423. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 방어 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [Protection]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [CanDuelGuard]\nExclusive Skill for [SupportProtect]\n[BeforeUse] At 10+ [EnhanceZilu], activates "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n[WhenUse] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Cannot be Staggered by damage until this Skill ends\n[WhenUse] Gain 2 [Protection] (once per turn)
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n[BeforeUse] Przy 10+ [EnhanceZilu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”\n[WhenUse] Ta Umiejętność zyskuje +1 Poziomu Obrony za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)\n[WhenUse] Do końca działania tej Umiejętności nie zostaje Ogłuszona przez obrażenia\n[WhenUse] Zyskuje 2 [Protection] (1 raz na turę)
424. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 방어 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 2 얻음 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [Protection]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [CanDuelGuard]\nExclusive Skill for [SupportProtect]\n[BeforeUse] At 10+ [EnhanceZilu], activates "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n[WhenUse] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Cannot be Staggered by damage until this Skill ends\n[WhenUse] Gain 2 [Protection] (once per turn)<style="highlight"></style>
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n[BeforeUse] Przy 10+ [EnhanceZilu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”\n[WhenUse] Ta Umiejętność zyskuje +1 Poziomu Obrony za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)\n[WhenUse] Do końca działania tej Umiejętności nie zostaje Ogłuszona przez obrażenia\n[WhenUse] Zyskuje 2 [Protection] (1 raz na turę)<style="highlight"></style>
426. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
427. [Pasywka bojowa (od ulepszenia 1) — nazwa] 천구성
   źródło: Passives.json :: dataList[id=1021203].name
   limit: do 40 znaków
   EN: Tianjiu Star
   PL: Gwiazda Tianjiu
428. [Pasywka bojowa (od ulepszenia 1) — opis] [BurstZilu]의 수치가 0이 되어 소멸시, [BurstVulnerableZilu]이 부여됨
   źródło: Passives.json :: dataList[id=1021203].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstZilu], [BurstVulnerableZilu]
   znaczenie tagów: [BurstZilu] = 주살【파】 / Deathrite 【Fissure】; [BurstVulnerableZilu] = 붕괴 표식 / Mark of Decay
   EN: When [BurstZilu] Stack drops to 0 and expires, gain [BurstVulnerableZilu]
   PL: Gdy Licznik [BurstZilu] spadnie do 0 i efekt wygaśnie, zyskuje [BurstVulnerableZilu]
429. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 흑수화[묘] / 묘 필두
   źródło: Passives.json :: dataList[id=1021201].name
   limit: do 60 znaków
   EN: Heishou Mutation [Mao] / Mao Branch Adept
   PL: Mutacja Heishou [Mao] / Adept Gałęzi Mao
430. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 자신의 속도가 대상보다 빠르면, 속도 차이 1 당 가하는 피해량 +2% (최대 10%)\n\n전투 중 아군이 주살 효과를 발동시킬 때마다, [EnhanceZilu] 1 얻음 (턴 당 최대 5회)\n- 자신이 발동시켰으면, [EnhanceZilu] 추가로 1 얻음\n[SupportProtect] 효과 발동시, [EnhanceZilu] 5 얻음
   źródło: Passives.json :: dataList[id=1021201].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceZilu], [SupportProtect]
   znaczenie tagów: [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [SupportProtect] = 원호 방어 / Assist Defense
   EN: If this unit's Speed is faster than the target's, deal +2% more damage for every 1 Speed difference (max 10%)\n\nGain 1 [EnhanceZilu] every time an ally triggers a Deathrite effect (5 times per turn)\n- If this unit triggered a Deathrite effect, gain 1 additional [EnhanceZilu]\nWhen activating the [SupportProtect] effect, gain 5 [EnhanceZilu]
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +2% obrażeń za każde 1 różnicy Szybkości (maks. 10%)\n\nZa każdym razem, gdy sojusznik uruchomi Obrzęd Śmierci podczas walki, zyskuje 1 [EnhanceZilu] (maks. 5 razy na turę)\n- Jeżeli ta jednostka go uruchomiła, zyskuje dodatkowo 1 [EnhanceZilu]\nPrzy uruchomieniu efektu [SupportProtect] zyskuje 5 [EnhanceZilu]
431. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — podsumowanie] 속도 차이 비례 피해량 증가[TabExplain]\n주살 또는 [SupportProtect] 효과 발동시, [EnhanceZilu] 얻음
   źródło: Passives.json :: dataList[id=1021201].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [SupportProtect], [EnhanceZilu]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade
   EN: Deal more damage based on Speed difference\nWhen activating Deathrite or [SupportProtect] effects, gain [EnhanceZilu]
   PL: Zadaje więcej obrażeń proporcjonalnie do różnicy Szybkości[TabExplain]\nPrzy Obrzędzie Śmierci lub efekcie [SupportProtect] zyskuje [EnhanceZilu]
432. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — nazwa] 쾌도
   źródło: Passives.json :: dataList[id=1021221].name
   limit: do 40 znaków
   EN: Blinkblade
   PL: Błyskawiczne Ostrze
433. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — opis] 속도가 가장 빠른 아군이 [Burst] 피해를 입히면, 다음 턴에 [AttackUp] 1 얻음 (턴 당 최대 3회)
   źródło: Passives.json :: dataList[id=1021221].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackUp]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: When 1 ally with the fastest Speed inflicts [Burst] damage, gain 1 [AttackUp] next turn (3 times per turn)
   PL: Gdy sojusznik z najwyższą Szybkością zadaje obrażenia [Burst], zyskuje w następnej turze 1 [AttackUp] (maks. 3 razy na turę)

## [000] Shi Assoc. East Section 3 — Faust — 동부 시 협회 3과
- ID Tożsamości: `10213` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 60 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Poise

434. [Karta Tożsamości — tytuł] 동부 시 협회\n3과
   źródło: Personalities.json :: dataList[id=10213].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nEast Section 3
   PL: Wschodnie Stowarzyszenie Shi\nSekcja 3
435. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10213].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10213].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Karta Tożsamości — opis] 파우스트의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10213].desc
   limit: do 120 znaków
   EN: Faust's 13th Identity
   PL: Trzynasta Tożsamość Faust
438. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 베어내기
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].name ; dataList[id=1021301].levelList[level=2].name ; dataList[id=1021301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cleave
   PL: Rozcięcie
439. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 1 [Breath]
   PL: [WhenUse] Zyskuje 1 [Breath]
440. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
441. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021301].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 4 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[WhenUse] At 4+ ([Breath] on self + [Laceration] on target), Coin Power +1</style>\n[WhenUse] Gain <style="highlight">2</style> [Breath]
   PL: <style="highlight">[WhenUse] Przy 4+ (suma własnej [Breath] i [Laceration] celu) Moc Monet +1</style>\n[WhenUse] Zyskuje <style="highlight">2</style> [Breath]
443. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 4 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 4+ ([Breath] on self + [Laceration] on target), Coin Power +1\n[WhenUse] Gain 2 [Breath] <style="highlight"></style>
   PL: [WhenUse] Przy 4+ (suma własnej [Breath] i [Laceration] celu) Moc Monet +1\n[WhenUse] Zyskuje 2 [Breath]<style="highlight"></style>
444. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Laceration]
445. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 거리 확보
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].name ; dataList[id=1021302].levelList[level=2].name ; dataList[id=1021302].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Positioning Maneuver
   PL: Zabezpieczenie Dystansu
446. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n[WhenUse] Gain +1 [Breath] Count
   PL: [WhenUse] Zadaje +11% obrażeń za każde 4 [Breath] (maks. 44%)\n[WhenUse] Zwiększa własny Licznik [Breath] o 1
447. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
448. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
449. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 2 [Laceration]
   PL: [CriticalOnSucceedAttack] Nakłada 2 [Laceration]
450. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당, 합 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[WhenUse] Clash Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 2)</style>\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n[WhenUse] Gain +1 [Breath] Count
   PL: <style="highlight">[WhenUse] Moc Starcia +1 za każde 4 (suma własnej [Breath] i [Laceration] celu) (maks. 2)</style>\n[WhenUse] Zadaje +11% obrażeń za każde 4 [Breath] (maks. 44%)\n[WhenUse] Zwiększa własny Licznik [Breath] o 1
451. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [Breath]
   PL: [OnSucceedAttack] Zyskuje <style="highlight">2</style> [Breath]
452. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당, 합 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n<style="highlight">[WhenUse] 소모한 [ArrowShiFau] 1당 피해량 +11% (최대 44%)</style>\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration], [ArrowShiFau]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ArrowShiFau] = 화살 - 시 / Arrow - Shi
   EN: [WhenUse] Clash Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max <style="highlight">4</style>)\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n<style="highlight">[WhenUse] Deal +11% damage for every [ArrowShiFau] spent (max 44%)</style>\n[WhenUse] Gain +1 [Breath] Count
   PL: [WhenUse] Moc Starcia +1 za każde 4 (suma własnej [Breath] i [Laceration] celu) (maks. <style="highlight">4</style>)\n[WhenUse] Zadaje +11% obrażeń za każde 4 [Breath] (maks. 44%)\n<style="highlight">[WhenUse] Zadaje +11% obrażeń za każdy 1 zużyty [ArrowShiFau] (maks. 44%)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 1
453. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o <style="highlight">2</style>
454. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]<style="highlight"></style>
455. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Laceration] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict 2 [Laceration]
   PL: <style="highlight">[OnSucceedAttack]</style> Nakłada 2 [Laceration]
456. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 궁섬[弓閃]
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].name ; dataList[id=1021303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Glimmering Bow [弓閃]
   PL: Lśniący Łuk [弓閃]
457. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monet +1 za każde 4 (suma własnej [Breath] i [Laceration] celu) (maks. 2)\n[WhenUse] Zadaje +11% obrażeń za każde 4 [Breath] (maks. 44%)\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
458. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1021303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +1 [Breath] Count
   PL: [CriticalOnSucceedAttack] Zyskuje +1 Licznika [Breath]
460. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1021303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Laceration] celu o 1
462. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1021303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] Nakłada 4 [Laceration]
463. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict 1 [DefenseDown] next turn (once per turn)
   PL: [CriticalOnSucceedAttack] Nakłada w następnej turze 1 [DefenseDown] (1 raz na turę)
464. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n<style="highlight">[WhenUse] 소모한 [ArrowShiFau] 1당 피해량 +11% (최대 44%)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration], [ArrowShiFau]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ArrowShiFau] = 화살 - 시 / Arrow - Shi
   EN: [WhenUse] Coin Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n<style="highlight">[WhenUse] Deal +11% damage for every [ArrowShiFau] spent (max 44%)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monet +1 za każde 4 (suma własnej [Breath] i [Laceration] celu) (maks. 2)\n[WhenUse] Zadaje +11% obrażeń za każde 4 [Breath] (maks. 44%)\n<style="highlight">[WhenUse] Zadaje +11% obrażeń za każdy 1 zużyty [ArrowShiFau] (maks. 44%)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
465. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] <style="highlight">2</style> 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">2</style> [DefenseDown] next turn (once per turn)
   PL: [CriticalOnSucceedAttack] Nakłada w następnej turze <style="highlight">2</style> [DefenseDown] (1 raz na turę)
468. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 섬궁[閃弓]
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].name ; dataList[id=1021305].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Bow's Glimmer [閃弓]
   PL: Błysk Łuku [閃弓]
469. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[AimForTheGoal] 1당 피해량 +24% (최대 72%)\n[AimForTheGoal] 1당 크리티컬 피해량 +24% (최대 72%)\n- [AimForTheGoal]이 4면, 위 두 효과 대신 크리티컬 피해량 +444%\n[WhenUse] 자신의 [Breath]이 4 이상이면, 기본 위력 +2\n[WhenUse] [AimForTheGoal] 1당 코인 위력 +2 (최대 4)\n[WhenUse] [AimForTheGoal] 1당 [Breath] 5 얻음\n[EndSkill] ([AimForTheGoal] x 5)만큼 [Breath] 감소\n[EndSkill] [SnipingArrowMode] 제거, [AimForTheGoal] 제거
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [AimForTheGoal], [WhenUse], [Breath], [EndSkill], [SnipingArrowMode]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [AimForTheGoal] = 목표 조준 / Target Aim; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [SnipingArrowMode] = 저격 자세 / Ready to Loose
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nDeal +24% damage for every [AimForTheGoal] (max 72%)\nDeal +24% damage on Critical Hit for every [AimForTheGoal] (max 72%)\n- At 4 [AimForTheGoal], instead of the two above effects, deal +444% damage on Critical Hit\n[WhenUse] At 4+ [Breath], Base Power +2\n[WhenUse] Coin Power +2 for every [AimForTheGoal] (max 4)\n[WhenUse] Gain 5 [Breath] for every [AimForTheGoal]\n[EndSkill] Lose ([AimForTheGoal] x 5) [Breath]\n[EndSkill] Remove [SnipingArrowMode] and [AimForTheGoal] from self
   PL: [CantDuel]\nZewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\nZadaje +24% obrażeń za każdy 1 [AimForTheGoal] (maks. 72%)\nZadaje +24% obrażeń przy trafieniu krytycznym za każdy 1 [AimForTheGoal] (maks. 72%)\n- Przy 4 [AimForTheGoal] zamiast dwóch powyższych efektów zadaje +444% obrażeń przy trafieniu krytycznym\n[WhenUse] Przy 4+ [Breath] Moc Bazowa +2\n[WhenUse] Moc Monet +2 za każdy 1 [AimForTheGoal] (maks. 4)\n[WhenUse] Zyskuje 5 [Breath] za każdy 1 [AimForTheGoal]\n[EndSkill] Traci ([AimForTheGoal] x 5) [Breath]\n[EndSkill] Usuwa [SnipingArrowMode] i [AimForTheGoal]
470. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ArrowInTheEyeFau] 1 부여, 부여 성공 시 [ArrowShiFau] 1 감소
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1021305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ArrowInTheEyeFau], [ArrowShiFau]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ArrowInTheEyeFau] = 박힌 화살 / Lodged Arrow; [ArrowShiFau] = 화살 - 시 / Arrow - Shi
   EN: [OnSucceedAttack] Inflict 1 [ArrowInTheEyeFau]; once inflicted, lose 1 [ArrowShiFau]
   PL: [OnSucceedAttack] Nakłada 1 [ArrowInTheEyeFau]; przy pomyślnym nałożeniu traci 1 [ArrowShiFau]
471. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [EnemyKill] 다음 턴에 [AStrokeOfDeath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1021305].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [AStrokeOfDeath]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [AStrokeOfDeath] = 절명 / Liferender
   EN: [EnemyKill] Gain 1 [AStrokeOfDeath] next turn
   PL: [EnemyKill] Zyskuje w następnej turze 1 [AStrokeOfDeath]
472. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[AimForTheGoal] 1당 피해량 +<style="highlight">48</style>% (최대 <style="highlight">144</style>%)\n[AimForTheGoal] 1당 크리티컬 피해량 +<style="highlight">48</style>% (최대 <style="highlight">144</style>%)\n- [AimForTheGoal]이 4면, 위 두 효과 대신 크리티컬 피해량 +444%\n[WhenUse] 자신의 [Breath] 4<style="highlight">당 기본 위력 +2 (최대 10)</style>\n[WhenUse] [AimForTheGoal] 1당 코인 위력 +<style="highlight">4</style> (최대 <style="highlight">10</style>)\n[WhenUse] [AimForTheGoal] 1당 [Breath] 5 얻음\n[EndSkill] (<style="highlight">([AimForTheGoal] - 1)</style> x 5)만큼 [Breath] 감소\n[EndSkill] [SnipingArrowMode] 제거, [AimForTheGoal] 제거
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=4].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [AimForTheGoal], [WhenUse], [Breath], [EndSkill], [SnipingArrowMode]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [AimForTheGoal] = 목표 조준 / Target Aim; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [SnipingArrowMode] = 저격 자세 / Ready to Loose
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nDeal +<style="highlight">48</style>% damage for every [AimForTheGoal] (max <style="highlight">144</style>%)\nDeal +<style="highlight">48</style>% damage on Critical Hit for every [AimForTheGoal] (max <style="highlight">144</style>%)\n- At 4 [AimForTheGoal], instead of the two above effects, deal +444% damage on Critical Hit\n[WhenUse] <style="highlight">Base Power +2 for every 4 [Breath] on self (max 10)</style>\n[WhenUse] Coin Power +<style="highlight">4</style> for every [AimForTheGoal] (max <style="highlight">10</style>)\n[WhenUse] Gain 5 [Breath] for every [AimForTheGoal]\n[EndSkill] Lose (<style="highlight">([AimForTheGoal] - 1)</style> x 5) [Breath]\n[EndSkill] Remove [SnipingArrowMode] and [AimForTheGoal] from self
   PL: [CantDuel]\nZewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\nZadaje +<style="highlight">48</style>% obrażeń za każdy 1 [AimForTheGoal] (maks. <style="highlight">144</style>%)\nZadaje +<style="highlight">48</style>% obrażeń przy trafieniu krytycznym za każdy 1 [AimForTheGoal] (maks. <style="highlight">144</style>%)\n- Przy 4 [AimForTheGoal] zamiast dwóch powyższych efektów zadaje +444% obrażeń przy trafieniu krytycznym\n[WhenUse] <style="highlight">Moc Bazowa +2 za każde 4 [Breath] (maks. 10)</style>\n[WhenUse] Moc Monet +<style="highlight">4</style> za każdy 1 [AimForTheGoal] (maks. <style="highlight">10</style>)\n[WhenUse] Zyskuje 5 [Breath] za każdy 1 [AimForTheGoal]\n[EndSkill] Traci (<style="highlight">([AimForTheGoal] - 1)</style> x 5) [Breath]\n[EndSkill] Usuwa [SnipingArrowMode] i [AimForTheGoal]
473. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalEnemyTargetKill] 자신의 [Breath] 횟수 4 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalEnemyTargetKill], [Breath]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[CriticalEnemyTargetKill] Gain +4 [Breath] Count</style>
   PL: <style="highlight">[CriticalEnemyTargetKill] Zwiększa własny Licznik [Breath] o 4</style>
474. [Obrona (ulepszenia 1,3,4) — nazwa] 궁도[弓刀] 전개
   źródło: Skills_personality-02.json :: dataList[id=1021304].levelList[level=1].name ; dataList[id=1021304].levelList[level=3].name ; dataList[id=1021304].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 14 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Unfold Bowblade [弓刀]
   PL: Rozwinięcie Łuk-Ostrza [弓刀]
475. [Obrona (ulepszenie 3) — opis] <style="highlight">자신에게 [ArrowShiFau]가 없으면 ‘회피’로 발동됨\n\n[StartBattle] ‘섬궁’ 사용 예정이면 ‘회피’로 변경됨\n[StartBattle] 자신에게 [SnipingArrowMode]가 있으면, 해당 턴 동안 (36 / [AimForTheGoal] 수치)만큼 보호막을 얻음 (턴당 1회)\n\n[EndBattle] 자신에게 [SnipingArrowMode]가 있고, 이번 턴에 공격 스킬을 사용하지 않았으면, 다음 턴에 [AimForTheGoal] 1 얻음 (턴당 1회)\n[EndBattle] 자신에게 [SnipingArrowMode]가 없고, [ArrowShiFau]가 1 이상이면, 다음 턴에 [SnipingArrowMode], [AimForTheGoal] 1 얻음 (턴당 1회)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021304].levelList[level=3].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArrowShiFau], [StartBattle], [SnipingArrowMode], [AimForTheGoal], [EndBattle]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [StartBattle] = [전투 시작시] / [Combat Start]; [SnipingArrowMode] = 저격 자세 / Ready to Loose; [AimForTheGoal] = 목표 조준 / Target Aim; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: <style="highlight">If this unit does not have [ArrowShiFau], activate "Evade" instead\n\n[StartBattle] If this unit is about to use "Bow's Glimmer", use "Evade" instead\n[StartBattle] If this unit has [SnipingArrowMode], gain (36 / [AimForTheGoal] Stack) Shield for the turn (once per turn)\n\n[EndBattle] If this unit has [SnipingArrowMode], and did not use an Attack Skill this turn, gain 1 [AimForTheGoal] next turn (once per turn)\n[EndBattle] If this unit does not have [SnipingArrowMode], and has 1+ [ArrowShiFau], gain 1 of each [SnipingArrowMode] and [AimForTheGoal] next turn (once per turn)</style>
   PL: <style="highlight">Jeżeli ta jednostka nie ma [ArrowShiFau], zamiast tego uruchamia „Unik”\n\n[StartBattle] Jeżeli ma zostać użyty „Błysk Łuku”, zamiast tego używa „Uniku”\n[StartBattle] Jeżeli ta jednostka ma [SnipingArrowMode], zyskuje Tarczę równą (36 / stos [AimForTheGoal]) na tę turę (1 raz na turę)\n\n[EndBattle] Jeżeli ta jednostka ma [SnipingArrowMode] i nie użyła w tej turze Umiejętności ataku, zyskuje w następnej turze 1 [AimForTheGoal] (1 raz na turę)\n[EndBattle] Jeżeli ta jednostka nie ma [SnipingArrowMode] i ma 1+ [ArrowShiFau], zyskuje w następnej turze po 1 [SnipingArrowMode] i [AimForTheGoal] (1 raz na turę)</style>
476. [Obrona (ulepszenie 4) — opis] 자신에게 [ArrowShiFau]가 없으면 ‘회피’로 발동됨\n\n[StartBattle] ‘섬궁’ 사용 예정이면 ‘회피’로 변경됨\n[StartBattle] 자신에게 [SnipingArrowMode]가 있으면, 해당 턴 동안 (<style="highlight">60</style> / [AimForTheGoal] 수치)만큼 보호막을 얻음 (턴당 1회)\n\n[EndBattle] 자신에게 [SnipingArrowMode]가 있고, 이번 턴에 공격 스킬을 사용하지 않았으면, 다음 턴에 [AimForTheGoal] 1 얻음 (턴당 1회)\n[EndBattle] 자신에게 [SnipingArrowMode]가 없고, [ArrowShiFau]가 1 이상이면, 다음 턴에 [SnipingArrowMode], [AimForTheGoal] 1 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021304].levelList[level=4].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArrowShiFau], [StartBattle], [SnipingArrowMode], [AimForTheGoal], [EndBattle]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [StartBattle] = [전투 시작시] / [Combat Start]; [SnipingArrowMode] = 저격 자세 / Ready to Loose; [AimForTheGoal] = 목표 조준 / Target Aim; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: If this unit does not have [ArrowShiFau], activate "Evade" instead\n\n[StartBattle] If this unit is about to use "Bow's Glimmer", use "Evade" instead\n[StartBattle] If this unit has [SnipingArrowMode], gain (<style="highlight">60</style> / [AimForTheGoal] Stack) Shield for the turn (once per turn)\n\n[EndBattle] If this unit has [SnipingArrowMode], and did not use an Attack Skill this turn, gain 1 [AimForTheGoal] next turn (once per turn)\n[EndBattle] If this unit does not have [SnipingArrowMode], and has 1+ [ArrowShiFau], gain 1 of each [SnipingArrowMode] and [AimForTheGoal] next turn (once per turn)
   PL: Jeżeli ta jednostka nie ma [ArrowShiFau], zamiast tego uruchamia „Unik”\n\n[StartBattle] Jeżeli ma zostać użyty „Błysk Łuku”, zamiast tego używa „Uniku”\n[StartBattle] Jeżeli ta jednostka ma [SnipingArrowMode], zyskuje Tarczę równą (<style="highlight">60</style> / stos [AimForTheGoal]) na tę turę (1 raz na turę)\n\n[EndBattle] Jeżeli ta jednostka ma [SnipingArrowMode] i nie użyła w tej turze Umiejętności ataku, zyskuje w następnej turze 1 [AimForTheGoal] (1 raz na turę)\n[EndBattle] Jeżeli ta jednostka nie ma [SnipingArrowMode] i ma 1+ [ArrowShiFau], zyskuje w następnej turze po 1 [SnipingArrowMode] i [AimForTheGoal] (1 raz na turę)
477. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-02.json :: dataList[id=1021306].levelList[level=1].name ; dataList[id=1021306].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 [Breath] 횟수 1 증가 (턴당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain +1 [Breath] Count (2 times per turn)
   PL: [OnSucceedEvade] Zwiększa własny Licznik [Breath] o 1 (2 razy na turę)
479. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 자신의 [Breath] 횟수 1 증가 (턴당 3회)
   źródło: Skills_personality-02.json :: dataList[id=1021306].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain +1 [Breath] Count (3 times per turn)
   PL: [OnSucceedEvade] Zwiększa własny Licznik [Breath] o 1 (3 razy na turę)
480. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — nazwa] 시노유미
   źródło: Passives.json :: dataList[id=1021301].name
   limit: do 40 znaków
   EN: Shi-no-Yumi
   PL: Shi-no-Yumi
481. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — opis] 자신의 [ArrowShiFau]가 4면, 기본 공격 스킬 효과로 [Breath] 위력을 얻을 때, [Breath] 횟수 1 증가 (전투당 2회, [ArrowShiFau]가 3이 될 때 발동 횟수 초기화)\n[AimForTheGoal]이 2 이상일 때 ‘섬궁’을 사용했으면, 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Passives.json :: dataList[id=1021301].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [ArrowShiFau], [Breath], [AimForTheGoal], [SlashDamageUp]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [Breath] = 호흡 / Poise; [AimForTheGoal] = 목표 조준 / Target Aim; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: At 4 [ArrowShiFau] Stack: When this unit gains [Breath] Potency from Base Attack Skill effects, gain +1 [Breath] Count (2 times per Encounter; per-Encounter cap resets when [ArrowShiFau] drops to 3)\nIf this unit used "Bow's Glimmer" Skill at 2+ [AimForTheGoal], gain 1 [SlashDamageUp] next turn
   PL: Przy 4 [ArrowShiFau]: gdy ta jednostka zyskuje Moc [Breath] efektem podstawowej Umiejętności ataku, zwiększa Licznik [Breath] o 1 (2 razy na spotkanie; licznik limitu resetuje się, gdy [ArrowShiFau] spadnie do 3)\nJeżeli ta jednostka użyła Umiejętności „Błysk Łuku” przy 2+ [AimForTheGoal], zyskuje w następnej turze 1 [SlashDamageUp]
482. [Pasywka bojowa (od ulepszenia 3) — nazwa] 저격 - 활
   źródło: Passives.json :: dataList[id=1021302].name
   limit: do 40 znaków
   EN: Snipe - Archery
   PL: Celowanie - Łuk
483. [Pasywka bojowa (od ulepszenia 3) — opis] 자신이 [SnipingArrowMode] 상태면, 가장 왼쪽에 장착한 기본 공격 스킬을 ‘섬궁’으로 변경하여 전투 시작 시 사용함.\n- 이 효과 발동시 자신의 [AimForTheGoal]이 최대 수치이고, 조작 패널과 예비 스킬 슬롯에 스킬 3이 없으면, \n가장 왼쪽 슬롯에 장착한 수비 스킬을 스킬 3으로 취급하여 ‘섬궁’으로 변경함\n\n사용하는 기본 공격 스킬에 따라 아래 효과 적용 (죄악 속성은 사용한 스킬 속성을 따름)\n- 스킬 1: 기본 위력 +1, 피해량 +11%\n- 스킬 2: 기본 위력 +1, 코인 위력 +1, 피해량 +22%\n- 스킬 3: 기본 위력 +4, 코인 위력 +4, 피해량 +44%\n\n※ E.G.O 스킬 장착하여 전투를 시작한 경우, [SnipingArrowMode]가 해제되고 ‘섬궁’이 사용되지 않음.
   źródło: Passives.json :: dataList[id=1021302].desc
   limit: do 1040 znaków
   tokeny: zachowaj dokładnie: \n, [SnipingArrowMode], [AimForTheGoal]
   znaczenie tagów: [SnipingArrowMode] = 저격 자세 / Ready to Loose; [AimForTheGoal] = 목표 조준 / Target Aim
   EN: If this unit is in [SnipingArrowMode] state, replace the leftmost Base Attack Skill equipped on the Dashboard with "Bow's Glimmer", then use it at Combat Start\n- If, at max [AimForTheGoal] Stack, this unit's Skill 3 is on neither the Dashboard nor the upcoming list of Skills when this effect activates, the Defense Skill equipped on the leftmost Skill Slot counts as a Skill 3, and will be used to activate "Bow's Glimmer"\n\nGain the following effects based on which Base Attack Skill was replaced (Sin Affinity carries over from the replaced Skill)\n- Skill 1: Base Power +1, deal +11% damage\n- Skill 2: Base Power +1, Coin Power +1, deal +22% damage\n- Skill 3: Base Power +4, Coin Power +4, deal +44% damage\n\n※ If an E.G.O Skill was equipped at Combat Start, remove [SnipingArrowMode] and this unit does not use "Bow's Glimmer"
   PL: Jeżeli ta jednostka jest w stanie [SnipingArrowMode], zamienia skrajnie lewą podstawową Umiejętność ataku na „Błysk Łuku” i używa jej na początku walki.\n- Jeżeli przy uruchomieniu tego efektu [AimForTheGoal] osiąga maksimum, a Umiejętność 3 nie ma ani w Panelu Sterowania, ani w rezerwowym slocie Umiejętności,\numiejętność obrony w skrajnie lewym slocie jest traktowana jako Umiejętność 3 i zamieniana na „Błysk Łuku”\n\nZależnie od użytej podstawowej Umiejętności ataku stosuje poniższe efekty (atrybut Grzechu pochodzi z użytej Umiejętności)\n- Umiejętność 1: Moc Bazowa +1, obrażenia +11%\n- Umiejętność 2: Moc Bazowa +1, Moc Monet +1, obrażenia +22%\n- Umiejętność 3: Moc Bazowa +4, Moc Monet +4, obrażenia +44%\n\n※ Jeżeli na początku walki wyposażono Umiejętność E.G.O, [SnipingArrowMode] zostaje zdjęty, a „Błysk Łuku” nie jest używany.
484. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust) — nazwa] 시노유미
   źródło: Passives.json :: dataList[id=1021311].name
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust) — opis] 자신의 [ArrowShiFau]가 4면, 기본 공격 스킬 효과로 [Breath] 위력을 얻을 때, [Breath] 횟수 1 증가 (전투당 <style="highlight">3</style>회, [ArrowShiFau]가 3이 될 때 발동 횟수 초기화)\n[AimForTheGoal]이 2 이상일 때 ‘섬궁’을 사용했으면, 다음 턴에 [SlashDamageUp] <style="highlight">2</style> 얻음
   źródło: Passives.json :: dataList[id=1021311].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArrowShiFau], [Breath], [AimForTheGoal], [SlashDamageUp]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [Breath] = 호흡 / Poise; [AimForTheGoal] = 목표 조준 / Target Aim; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: At 4 [ArrowShiFau] Stack: When this unit gains [Breath] Potency from Base Attack Skill effects, gain +1 [Breath] Count (<style="highlight">3</style> times per Encounter; per-Encounter cap resets when [ArrowShiFau] drops to 3)\nIf this unit used "Bow's Glimmer" Skill at 2+ [AimForTheGoal], gain <style="highlight">2</style> [SlashDamageUp] next turn
   PL: Przy 4 [ArrowShiFau]: gdy ta jednostka zyskuje Moc [Breath] efektem podstawowej Umiejętności ataku, zwiększa Licznik [Breath] o 1 (<style="highlight">3</style> razy na spotkanie; licznik limitu resetuje się, gdy [ArrowShiFau] spadnie do 3)\nJeżeli ta jednostka użyła Umiejętności „Błysk Łuku” przy 2+ [AimForTheGoal], zyskuje w następnej turze <style="highlight">2</style> [SlashDamageUp]
486. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Lust) — nazwa] 한점 노리기
   źródło: Passives.json :: dataList[id=1021321].name
   limit: do 40 znaków
   EN: Aiming for the Bullseye
   PL: Celowanie w Punkt
487. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Lust) — opis] 턴 종료 시 전투 중 스킬 및 패시브로 적에게 [Laceration] 위력을 가장 많이 부여한 아군 1명에게 다음 턴에 [PenetrateDamageUp] 1 부여 (E.G.O스킬 포함, [Laceration] 부여량이 동일하다면 편성 순서가 빠른 순으로 결정함, 해당 턴에 [Laceration] 위력을 부여하지 않았다면 발동하지 않음)
   źródło: Passives.json :: dataList[id=1021321].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: [Laceration], [PenetrateDamageUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Turn End: Apply 1 [PenetrateDamageUp] next turn to the ally who inflicted the most [Laceration] Potency to enemies with its Skills and Passives (includes those from E.G.O Skills; if multiple Identities share the highest [Laceration] inflicted record for the turn, select the Identity earliest in the Deployment order. Does not activate if no one inflicted [Laceration] Potency that turn)
   PL: Na koniec tury nakłada w następnej turze 1 [PenetrateDamageUp] na sojusznika, który w tej walce nałożył najwięcej Mocy [Laceration] na wrogów Umiejętnościami i Pasywkami (łącznie z Umiejętnościami E.G.O; przy remisie wygrywa Tożsamość wcześniejsza w kolejności przydziału; nie uruchamia się, jeżeli nikt nie nałożył Mocy [Laceration] w tej turze)

## [000] The Index Proselyte: 【Paper Slip】 — Faust — 검지 수행자: 【쪽지】
- ID Tożsamości: `10214` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 57 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise, Sinking

488. [Karta Tożsamości — tytuł] 검지 수행자:\n【쪽지】
   źródło: Personalities.json :: dataList[id=10214].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Index Proselyte:\n【Paper Slip】
   PL: Akolitka Wskazującego:\n【Karteczka】
489. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10214].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10214].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Karta Tożsamości — opis] 파우스트의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10214].desc
   limit: do 120 znaków
   EN: Faust's 14th Identity
   PL: Czternasta Tożsamość Faust
492. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 지령에 따라, 확실하게
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=1].name ; dataList[id=1021401].levelList[level=2].name ; dataList[id=1021401].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 50 znaków
   EN: Unerringly, as the Prescript Demands
   PL: Niezawodnie, zgodnie z Nakazem
493. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [WhenUse], [Breath]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
494. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]
496. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\n<style="highlight">Przy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
497. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]<style="highlight"></style>
498. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]<style="highlight"></style>
499. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">합 위력 +1</style>, 피해량 <style="highlight">+20%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Clash Power +1</style> and deal <style="highlight">+20%</style> damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Starcia +1</style> i zadaje <style="highlight">+20%</style> obrażeń\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
500. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [Sinking] 1 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [Sinking]</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Nakłada 1 [Sinking]</style>
501. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 지령을 수행하며 수행합니다
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=1].name ; dataList[id=1021402].levelList[level=2].name ; dataList[id=1021402].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 60 znaków
   EN: Undertake the Prescript, Again Undertake
   PL: Wypełnia Nakaz i doskonali siebie.
502. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 합 위력 +1\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [WhenUse], [Breath]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], Clash Power +1\n[WhenUse] Gain 3 [Breath]
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], Moc Starcia +1\n[WhenUse] Zyskuje 3 [Breath]
503. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 합 위력 +1\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 3 얻음, <style="highlight">자신의 [Breath] 횟수 1 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], Clash Power +1\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Gain 3 [Breath] and <style="highlight">+1 [Breath] Count</style>
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], Moc Starcia +1\n<style="highlight">Przy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1</style>\n[WhenUse] Zyskuje 3 [Breath] i <style="highlight">zwiększa własny Licznik [Breath] o 1</style>
506. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 1 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Sinking]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Sinking]</style>
508. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1021402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">최종 위력 +1</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] 3 얻음, 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Final Power +1</style>\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain 3 [Breath] and <style="highlight">+2</style> [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Końcowa +1</style>\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zyskuje 3 [Breath] i zwiększa własny Licznik [Breath] o <style="highlight">2</style>
510. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [Sinking] 횟수 2 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +2 [Sinking] Count</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Zwiększa Licznik [Sinking] celu o 2</style>
513. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 지령에 따라 당신을 처단하겠습니다.
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].name ; dataList[id=1021403].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 70 znaków
   EN: As the Prescript Demands, You Will Be Eliminated.
   PL: Zgodnie z Nakazem, zostaniesz wyeliminowany.
514. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 크리티컬 피해량 +20%\n자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1\n[StartBattle] [BlessingOfIndexPrescriptAlly]가 6 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [StartBattle], [BlessingOfIndexPrescriptAlly], [SuperCoin], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +20% damage on Critical Hit\nAt 6+ ([Breath] on self + [Sinking] on target), Coin Power +1\n[StartBattle] At 6+ [BlessingOfIndexPrescriptAlly], convert all Coins of this Skill to [SuperCoin]s\n[WhenUse] Gain +3 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +20% obrażeń przy trafieniu krytycznym\nPrzy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1\n[StartBattle] Przy 6+ [BlessingOfIndexPrescriptAlly] wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
515. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [BlessingOfIndexPrescriptAlly] 1당 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptAlly]가 9면, 대신 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptAlly]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript
   EN: Deal +2.5% damage for every [BlessingOfIndexPrescriptAlly] (max 20%)\n- At 9 [BlessingOfIndexPrescriptAlly], deal +30% damage instead
   PL: Zadaje +2.5% obrażeń za każdy 1 [BlessingOfIndexPrescriptAlly] (maks. 20%)\n- Przy 9 [BlessingOfIndexPrescriptAlly] zamiast tego zadaje +30% obrażeń
518. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Sinking] celu o 2
520. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">최종 위력 +1</style>, 크리티컬 피해량 <style="highlight">+30%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[StartBattle] [BlessingOfIndexPrescriptAlly]가 6 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 <style="highlight">피해량 +30%</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n<style="highlight">- ([BlessingOfIndexPrescriptAlly]/3)만큼 호흡 얻음 (소수점 버림)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [StartBattle], [BlessingOfIndexPrescriptAlly], [SuperCoin], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Final Power +1</style> and deal <style="highlight">+30%</style> damage on Critical Hit\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[StartBattle] At 6+ [BlessingOfIndexPrescriptAlly], convert all Coins of this Skill to [SuperCoin]s and <style="highlight">deal +30% damage</style>\n[WhenUse] Gain +3 [Breath] Count\n<style="highlight">- Gain [Breath] equal to ([BlessingOfIndexPrescriptAlly]/3) (rounded down)</style>
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Końcowa +1</style> i zadaje <style="highlight">+30%</style> obrażeń przy trafieniu krytycznym\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[StartBattle] Przy 6+ [BlessingOfIndexPrescriptAlly] wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin] i <style="highlight">zadaje +30% obrażeń</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n<style="highlight">- Zyskuje Oddech równy ([BlessingOfIndexPrescriptAlly]/3) (zaokrąglone w dół)</style>
521. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [BlessingOfIndexPrescriptAlly] 1당 피해량 <style="highlight">+5%</style> (최대 <style="highlight">40%</style>)\n- [BlessingOfIndexPrescriptAlly]가 9면, 대신 피해량 <style="highlight">+60%</style>
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlessingOfIndexPrescriptAlly]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript
   EN: Deal <style="highlight">+5%</style> damage for every [BlessingOfIndexPrescriptAlly] (max <style="highlight">40%</style>)\n- At 9 [BlessingOfIndexPrescriptAlly], deal <style="highlight">+60%</style> damage instead
   PL: Zadaje <style="highlight">+5%</style> obrażeń za każdy 1 [BlessingOfIndexPrescriptAlly] (maks. <style="highlight">40%</style>)\n- Przy 9 [BlessingOfIndexPrescriptAlly] zamiast tego zadaje <style="highlight">+60%</style> obrażeń
524. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [Sinking] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021403].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">+3</style> [Sinking] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Sinking] celu o <style="highlight">3</style>
526. [Obrona (ulepszenia 1,4) — nazwa] 지령이 하사한 지령으로 만들어진 천
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=1].name ; dataList[id=1021404].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 3 · monety: 3 (+3)
   limit: do 60 znaków
   EN: Prescript-granted, Prescript-woven Fabric
   PL: Tkanina utkana z zesłanego Nakazu
527. [Obrona (ulepszenie 1) — opis] [BlessingOfIndexPrescriptAlly] 3당 최종 위력 +1 (최대 3)\n[StartBattle] 자신의 최대 체력의 10%만큼 보호막 얻음 (턴당 1회)\n- [KarmaOfIndexAlly] 5당 이 효과로 얻는 보호막 수치 1% 감소, [KarmaOfIndexAlly]가 50 이상이면 보호막 얻지 않음\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptAlly], [StartBattle], [KarmaOfIndexAlly], [WhenUse], [Breath]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [StartBattle] = [전투 시작시] / [Combat Start]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every 3 [BlessingOfIndexPrescriptAlly] (max 3)\n[StartBattle] Gain Shield equal to 10% of max HP (once per turn)\n- Reduce Shield gained by 1% for every 5 [KarmaOfIndexAlly]; at 50+ [KarmaOfIndexAlly], does not gain Shield\n[WhenUse] Gain 2 [Breath]
   PL: Moc Końcowa +1 za każde 3 [BlessingOfIndexPrescriptAlly] (maks. 3)\n[StartBattle] Zyskuje Tarczę równą 10% Maks. HP (1 raz na turę)\n- Za każde 5 [KarmaOfIndexAlly] wartość Tarczy uzyskiwanej tym efektem maleje o 1%; przy 50+ [KarmaOfIndexAlly] nie zyskuje Tarczy\n[WhenUse] Zyskuje 2 [Breath]
528. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Obrona (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Obrona (ulepszenie 4) — opis] [BlessingOfIndexPrescriptAlly] 3당 최종 위력 +1, <style="highlight">피해량 +10%</style> (각각 최대 3, <style="highlight">최대 30%</style>)\n[StartBattle] 자신의 최대 체력의 <style="highlight">15%</style>만큼 보호막 얻음 (턴당 1회)\n- [KarmaOfIndexAlly] 5당 이 효과로 얻는 보호막 수치 <style="highlight">1.5%</style> 감소, [KarmaOfIndexAlly]가 50 이상이면 보호막 얻지 않음\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlessingOfIndexPrescriptAlly], [StartBattle], [KarmaOfIndexAlly], [WhenUse], [Breath]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [StartBattle] = [전투 시작시] / [Combat Start]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 and <style="highlight">deal +10% damage</style> for every 3 [BlessingOfIndexPrescriptAlly] (max 3 and <style="highlight">30%</style>, respectively)\n[StartBattle] Gain Shield equal to <style="highlight">15%</style> of max HP (once per turn)\n- Reduce Shield gained by <style="highlight">1.5%</style> for every 5 [KarmaOfIndexAlly]; at 50+ [KarmaOfIndexAlly], does not gain Shield\n[WhenUse] Gain 2 [Breath]
   PL: Moc Końcowa +1 i <style="highlight">zadaje +10% obrażeń</style> za każde 3 [BlessingOfIndexPrescriptAlly] (maks. odpowiednio 3 i <style="highlight">30%</style>)\n[StartBattle] Zyskuje Tarczę równą <style="highlight">15%</style> Maks. HP (1 raz na turę)\n- Za każde 5 [KarmaOfIndexAlly] wartość Tarczy uzyskiwanej tym efektem maleje o <style="highlight">1.5%</style>; przy 50+ [KarmaOfIndexAlly] nie zyskuje Tarczy\n[WhenUse] Zyskuje 2 [Breath]
531. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Obrona (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021404].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Pasywka bojowa (od ulepszenia 1) — nazwa] 쪽지로 전해진 지령
   źródło: Passives.json :: dataList[id=1021402].name
   limit: do 50 znaków
   EN: Prescript Delivered on Paper Slips
   PL: Nakaz przekazany Karteczką
534. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시\n- 자신의 [BlessingOfIndexPrescriptAlly] 수치에 따라 [IndexPrescriptFaust_0] / [IndexPrescriptFaust_1] / [IndexPrescriptFaust_2] /[IndexPrescriptFaust_3] 얻음\n- 무작위 적 1명에게 [IndexPrescriptTargetToEnemy] 부여 (집중 전투면, 부위에 부여)\n- 조작 슬롯의 자신의 기본 공격 스킬에 [IndexPrescriptTargetMarkToEnemy] 부여 (슬롯당 1개, 최대 2개 부여)\n· [BlessingOfIndexPrescriptAlly]가 6 이상이면, 스킬 3에 우선 부여\n- 흐트러짐, 행동 불가[TabExplain], 패닉, E.G.O 침식 상태면, 위의 모든 효과와 [IndexPrescript_Base] 수행 여부가 적용되지 않음
   źródło: Passives.json :: dataList[id=1021402].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptAlly], [IndexPrescriptFaust_0], [IndexPrescriptFaust_1], [IndexPrescriptFaust_2], [IndexPrescriptFaust_3], [IndexPrescriptTargetToEnemy], [IndexPrescriptTargetMarkToEnemy], [TabExplain], [IndexPrescript_Base]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptFaust_0] = 지령[쪽지] I / Prescript: [Paper Slip] I; [IndexPrescriptFaust_1] = 지령[쪽지] II / Prescript: [Paper Slip] II; [IndexPrescriptFaust_2] = 지령[쪽지] III / Prescript: [Paper Slip] III; [IndexPrescriptFaust_3] = 지령[쪽지] IV / Prescript: [Paper Slip] IV; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [IndexPrescript_Base] = 지령 / Prescript
   EN: Turn Start:\n- Gain [IndexPrescriptFaust_0] / [IndexPrescriptFaust_1] / [IndexPrescriptFaust_2] / [IndexPrescriptFaust_3] based on [BlessingOfIndexPrescriptAlly] on self\n- Inflict [IndexPrescriptTargetToEnemy] to a random enemy (in Focused Encounters, the Part)\n- Apply [IndexPrescriptTargetMarkToEnemy] to Base Attack Skills on this unit's Dashboard (1 per Slot, max 2 Skills)\n· At 6+ [BlessingOfIndexPrescriptAlly], the effect above prioritizes Skill 3\n- All of the effects above and [IndexPrescript_Base] execution checks do not trigger when this unit is Staggered, Immobilized[TabExplain], in Panic, or in E.G.O Corrosion[TabExplain]
   PL: Na początku tury\n- Zyskuje [IndexPrescriptFaust_0] / [IndexPrescriptFaust_1] / [IndexPrescriptFaust_2] / [IndexPrescriptFaust_3] zależnie od własnej wartości [BlessingOfIndexPrescriptAlly]\n- Nakłada [IndexPrescriptTargetToEnemy] na 1 losowego wroga (w walce skupionej: na część ciała)\n- Nakłada [IndexPrescriptTargetMarkToEnemy] na własne podstawowe Umiejętności ataku w Panelu Sterowania (1 na slot, maks. 2 Umiejętności)\n· Przy 6+ [BlessingOfIndexPrescriptAlly] efekt nakłada najpierw na Umiejętność 3\n- Jeżeli ta jednostka jest Ogłuszona, Niezdolna do działania[TabExplain], w Panice lub w Korozji E.G.O[TabExplain], żaden z powyższych efektów ani warunek wykonania [IndexPrescript_Base] nie działa
535. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 지령 얻음\n무작위 적에 지령 대상 부여\n자신의 무작위 기본 공격 스킬에 지령 표식 부여
   źródło: Passives.json :: dataList[id=1021402].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Prescript\nInflict 'The Prescript's Target' to random target\nApply 'Mark of the Prescript' on a Base Attack Skill
   PL: Zyskuje Nakaz\nNakłada Cel Nakazu na losowego wroga\nNakłada Znak Nakazu na losową własną podstawową Umiejętność ataku
536. [Pasywka bojowa (od ulepszenia 1) — nazwa] 지령의 뜻
   źródło: Passives.json :: dataList[id=1021403].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL: Wola Nakazu
537. [Pasywka bojowa (od ulepszenia 1) — opis] 이번 턴에 [IndexPrescript_Base]을 수행했으면,\n턴 종료 시 정신력 4 회복, [BlessingOfIndexPrescriptAlly] 1 얻음 (턴당 1회)\n- [IndexPrescript_Base] 수행 시 메인 타겟에게 [IndexPrescriptTargetToEnemy]이 있으면,\n대신 정신력 8 회복, [BlessingOfIndexPrescriptAlly] 3 얻음\n\n이번 턴에 [IndexPrescript_Base]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexAlly] 5 얻음\n- [BlessingOfIndexPrescriptAlly]가 9면, [KarmaOfIndexAlly]를 얻지 않음\n- 전투 시작 시 [IndexPrescript_Base] 수행을 시도했으나, 전투 중 대상을 타겟할 수 없게 되었으면, [KarmaOfIndexAlly]를 얻지 않음
   źródło: Passives.json :: dataList[id=1021403].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescript_Base], [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetToEnemy], [KarmaOfIndexAlly]
   znaczenie tagów: [IndexPrescript_Base] = 지령 / Prescript; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence
   EN: Turn End: If [IndexPrescript_Base] was executed this turn, heal 4 SP and gain 1 [BlessingOfIndexPrescriptAlly] (once per turn)\n- When executing [IndexPrescript_Base], if the main target has [IndexPrescriptTargetToEnemy], heal 8 SP and gain 3 [BlessingOfIndexPrescriptAlly] instead\n\nTurn End: If [IndexPrescript_Base] was not executed this turn, gain 5 [KarmaOfIndexAlly]\n- At 9 [BlessingOfIndexPrescriptAlly], does not gain [KarmaOfIndexAlly]\n- If this unit attempted to execute [IndexPrescript_Base] at Combat Start, but could not target the enemy during the combat phase, does not gain [KarmaOfIndexAlly]
   PL: Na koniec tury: jeżeli [IndexPrescript_Base] został wykonany w tej turze, odzyskuje 4 Poczytalności i zyskuje 1 [BlessingOfIndexPrescriptAlly] (1 raz na turę)\n- Jeżeli przy wykonywaniu [IndexPrescript_Base] główny cel ma [IndexPrescriptTargetToEnemy], zamiast tego odzyskuje 8 Poczytalności i zyskuje 3 [BlessingOfIndexPrescriptAlly]\n\nNa koniec tury: jeżeli [IndexPrescript_Base] nie został wykonany w tej turze, zyskuje 5 [KarmaOfIndexAlly]\n- Przy 9 [BlessingOfIndexPrescriptAlly] nie zyskuje [KarmaOfIndexAlly]\n- Jeżeli ta jednostka próbowała wykonać [IndexPrescript_Base] na początku walki, ale nie mogła namierzyć celu podczas walki, nie zyskuje [KarmaOfIndexAlly]
538. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 지령 수행 시, 정신력 회복하고 지령의 가호 얻음\n지령 실패 시, 카르마 얻음
   źródło: Passives.json :: dataList[id=1021403].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon executing Prescript, heal SP and gain Grace of the Prescript\nUpon failing Prescript, gain Karmic Consequence
   PL: Po wykonaniu Nakazu odzyskuje Poczytalność i zyskuje Łaskę Nakazu\nPo nieudanym Nakazie zyskuje Karmę
539. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom) — nazwa] 수행자의 검
   źródło: Passives.json :: dataList[id=1021401].name
   limit: do 40 znaków
   EN: Proselyte's Blade
   PL: Ostrze Akolity
540. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom) — opis] 자신의 [BlessingOfIndexPrescriptAlly] 1당 [IndexPrescriptTargetMarkToEnemy] 스킬 피해량 +2% (최대 16%)\n- [BlessingOfIndexPrescriptAlly]가 9면, 대신 기본 스킬 피해량 +20%\n\n[IndexPrescriptTargetToEnemy]이 있는 대상에게 기본 스킬 적중 시,\n[Breath] 1 얻고 [Sinking] 1 부여 (턴당 1회)\n- [BlessingOfIndexPrescriptAlly] 3당, 턴당 발동 가능한 횟수 +1 (최대 2)\n\n[BlessingOfIndexPrescriptAlly]가 9면, 기본 스킬의 [Sinking] 위력 부여값 +1, [Breath] 위력 획득값 +1
   źródło: Passives.json :: dataList[id=1021401].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetMarkToEnemy], [IndexPrescriptTargetToEnemy], [Breath], [Sinking]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking
   EN: Deal +2% damage with Skills marked with [IndexPrescriptTargetMarkToEnemy] for every [BlessingOfIndexPrescriptAlly] on self (max 16%)\n- At 9 [BlessingOfIndexPrescriptAlly], deal +20% damage with Base Skills instead\n\nOn Hit with a Base Skill against target that has [IndexPrescriptTargetToEnemy], gain 1 [Breath] and inflict 1 [Sinking] (once per turn)\n- Increase the number of times this effect can trigger per turn by 1 for every 3 [BlessingOfIndexPrescriptAlly] (max 2)\n\n- At 9 [BlessingOfIndexPrescriptAlly], Base Skills inflict +1 more [Sinking] Potency and this unit gains +1 more [Breath] Potency
   PL: Zadaje +2% obrażeń Umiejętnościami z [IndexPrescriptTargetMarkToEnemy] za każdy 1 [BlessingOfIndexPrescriptAlly] (maks. 16%)\n- Przy 9 [BlessingOfIndexPrescriptAlly] zamiast tego zadaje +20% obrażeń podstawowymi Umiejętnościami\n\nPrzy trafieniu podstawową Umiejętnością w cel z [IndexPrescriptTargetToEnemy], zyskuje 1 [Breath] i nakłada 1 [Sinking] (1 raz na turę)\n- Za każde 3 [BlessingOfIndexPrescriptAlly] liczba uruchomień tego efektu na turę rośnie o 1 (maks. 2)\n\nPrzy 9 [BlessingOfIndexPrescriptAlly] podstawowe Umiejętności nakładają +1 więcej Mocy Zatonięcia, a ta jednostka zyskuje +1 więcej Mocy Oddechu
541. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom) — podsumowanie] 지령 표식이 새겨진 스킬이면, 지령의 가호에 비례하여 피해량이 증가\n적중 시 호흡 얻고 침잠 부여
   źródło: Passives.json :: dataList[id=1021401].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skills marked with Mark of the Prescript deal more damage based on Grace of the Prescript Stack\nOn Hit, gain Poise and inflict Sinking
   PL: Umiejętności z wyrytym Znakiem Nakazu zadają więcej obrażeń proporcjonalnie do Łaski Nakazu\nPrzy trafieniu zyskuje Oddech i nakłada Zatonięcie
542. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom) — nazwa] 지령이 이끄는 대로…
   źródło: Passives.json :: dataList[id=1021421].name
   limit: do 40 znaków
   EN: As the Prescript Orders...
   PL: Tak, jak Nakaz nakazuje...
543. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom) — opis] 편성 순서가 가장 빠른 인격에게 효과 적용\n- 검지 소속 인격이 있으면, 해당 인격에게 우선 적용\n\n전투 시작 시 자신의 조작 슬롯 중 가장 왼쪽 스킬로 지정한 적 슬롯을 다른 아군이 같이 지정했으면, 해당 스킬의 피해량이 자신을 제외하고 해당 슬롯을 타겟한 인원 수 1명당 5% 증가\n(최대 15%, 자신과 아군 모두 기본 공격 스킬로 메인 타겟할 때 적용)
   źródło: Passives.json :: dataList[id=1021421].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Effects apply to the Identity with the earliest Deployment order\n- Prioritizes The Index-faction Identities\n\nCombat Start: If this unit's leftmost Skill on the Dashboard and other allies target the same enemy Slot, said Skill deals +5% damage for every ally targeting the same Slot excluding this unit (max 15%, applies when this unit and allies both use Base Attack Skills to main-target enemy Slot)
   PL: Efekt stosuje do Tożsamości pierwszej w kolejności przydziału\n- Najpierw Tożsamości frakcji Wskazującego\n\nNa początku walki, jeżeli inni sojusznicy namierzyli ten sam slot wroga, co skrajnie lewa Umiejętność tej jednostki w Panelu Sterowania, ta Umiejętność zadaje +5% obrażeń za każdego 1 sojusznika namierzającego ten slot, nie licząc tej jednostki\n(maks. 15%; działa, gdy ta jednostka i sojusznicy namierzają główny cel podstawową Umiejętnością ataku)
544. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom) — podsumowanie] 자신 제외 해당 슬롯 타겟한 인원 수에 비례하여 피해량이 증가
   źródło: Passives.json :: dataList[id=1021421].summary
   limit: do 120 znaków
   EN: Deal more damage based on number of other units that targeted the slot
   PL: Zadaje więcej obrażeń proporcjonalnie do liczby innych jednostek namierzających ten slot

## [000] The House of Spiders: The Ring Apprentice — Faust — 거미집 약지 제자
- ID Tożsamości: `10215` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 92 · szybkość: 3–4 / 3–5 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Charge

545. [Karta Tożsamości — tytuł] 거미집\n약지 제자
   źródło: Personalities.json :: dataList[id=10215].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders:\nThe Ring Apprentice
   PL: Dom Pajęczyn:\nUczeń Serdecznego
546. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10215].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10215].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Karta Tożsamości — opis] 파우스트의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10215].desc
   limit: do 120 znaków
   EN: Faust's 15th Identity
   PL: Piętnasta Tożsamość Faust
549. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 도축 - 갈비뼈
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=1].name ; dataList[id=1021501].levelList[level=2].name ; dataList[id=1021501].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Butcher - Ribs
   PL: Ubój - Żebra
550. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [IronMaidenPersonality] 전용 스킬
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [IronMaidenPersonality]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden
   EN: [IronMaidenPersonality] exclusive Skill
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]
551. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [DefenseDown] (1 raz na turę)
552. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1021501].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1021501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn (once per turn)
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 [DefenseUp] (1 raz na turę)
553. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [IronMaidenPersonality] 전용 스킬\n[WhenUse] 대상의 부정적인 효과 1개당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [IronMaidenPersonality], [WhenUse], [Laceration]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [IronMaidenPersonality] exclusive Skill\n[WhenUse] Clash Power +1 for every type of negative effect on target (max 2)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n[WhenUse] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 2)
554. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [IronMaidenPersonality] 전용 스킬\n[WhenUse] 대상의 부정적인 효과 1개당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 3)
   źródło: Skills_personality-02.json :: dataList[id=1021501].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [IronMaidenPersonality], [WhenUse], [Laceration]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [IronMaidenPersonality] exclusive Skill\n[WhenUse] Clash Power +1 for every type of negative effect on target (max 2)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n[WhenUse] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 3)
556. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 파시아가 굶주렸어
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=1].name ; dataList[id=1021502].levelList[level=2].name ; dataList[id=1021502].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Fascia Hungers
   PL: Fascia jest głodna.
557. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [IronMaidenPersonality] 전용 스킬\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [IronMaidenPersonality], [WhenUse], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [IronMaidenPersonality] exclusive Skill\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
558. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding] (1 raz na turę)
560. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeBodyArt] 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1021502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeBodyArt]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: [OnSucceedAttack] Gain +4 [ChargeBodyArt] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeBodyArt] o 4
561. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [IronMaidenPersonality] 전용 스킬\n<style="highlight">[WhenUse] 대상의 부정적인 효과 1개당, 합 위력 +1 (최대 2)</style>\n<style="highlight">[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=2].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IronMaidenPersonality], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [IronMaidenPersonality] exclusive Skill\n<style="highlight">[WhenUse] Clash Power +1 for every type of negative effect on target (max 2)</style>\n<style="highlight">[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)</style>\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n<style="highlight">[WhenUse] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)</style>\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 2)</style>\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
562. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
563. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [IronMaidenPersonality] 전용 스킬\n[WhenUse] 대상의 부정적인 효과 1개당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021502].levelList[level=4].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IronMaidenPersonality], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [IronMaidenPersonality] exclusive Skill\n[WhenUse] Clash Power +1 for every type of negative effect on target (max 2)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max <style="highlight">4</style>)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n[WhenUse] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. <style="highlight">4</style>)\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
564. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 억압당한 육체
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].name ; dataList[id=1021503].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Repressed Flesh
   PL: Tłumione Ciało
565. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [IronMaidenPersonality] 전용 스킬\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +3%
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [IronMaidenPersonality], [WhenUse], [Laceration], [ChargeBodyArt]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: [IronMaidenPersonality] exclusive Skill\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count to gain the following effects:\n- Final Power +2\n- Deal +3% damage for every [ChargeBodyArt] Count consumed
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 2)\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +3% obrażeń za każdy 1 zużytego Licznika [ChargeBodyArt]
566. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]
567. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1021503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1021503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDmgDown] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [AttackDmgDown] (1 raz na turę)
569. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 대상의 부정적인 효과 1개당, 피해량 +5% (최대 30%)
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1021503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +5% damage for every type of negative effect on target (max 30%)
   PL: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)
570. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1021503].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [IronMaidenPersonality] 전용 스킬\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +3%
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [IronMaidenPersonality], [WhenUse], [Laceration], [ChargeBodyArt]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: [IronMaidenPersonality] exclusive Skill\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count to gain the following effects:\n- Final Power +2\n- Deal +3% damage for every [ChargeBodyArt] Count consumed
   PL: Umiejętność wyłącznie dla [IronMaidenPersonality]\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 3)\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +3% obrażeń za każdy 1 zużytego Licznika [ChargeBodyArt]
572. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 도축 - 갈비뼈
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=1].name ; dataList[id=1021505].levelList[level=2].name ; dataList[id=1021505].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [SilverOpportunity] 전용 스킬
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SilverOpportunity]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State
   EN: [SilverOpportunity] exclusive Skill
   PL: Umiejętność wyłącznie dla [SilverOpportunity]
575. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021505].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021505].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1021505].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1021505].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [SilverOpportunity] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [WhenUse], [Laceration]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [SilverOpportunity] exclusive Skill\nDeal +5% damage for every type of negative effect on target (max 20%)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\nZadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 20%)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 2)
578. [Umiejętność 4 (×0) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021505].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [SilverOpportunity] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +10% (최대 30%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 3)
   źródło: Skills_personality-02.json :: dataList[id=1021505].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [WhenUse], [Laceration]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [SilverOpportunity] exclusive Skill\nDeal +10% damage for every type of negative effect on target (max 30%)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\nZadaje +10% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 3)
580. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 파시아 식사 시간이네요
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=1].name ; dataList[id=1021506].levelList[level=2].name ; dataList[id=1021506].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Time for Your Meal, Fascia
   PL: Czas na Posiłek dla Fascii.
581. [Umiejętność 5 (×0) (ulepszenie 1) — opis] [SilverOpportunity] 전용 스킬\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [WhenUse], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SilverOpportunity] exclusive Skill\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
582. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021506].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021506].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1021506].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1021506].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn (once per turn)
   PL: [OnSucceedAttack] Zyskuje w następnej turze 1 [Agility] (1 raz na turę)
585. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeBodyArt] 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021506].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1021506].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność 5 (×0) (ulepszenie 2) — opis] [SilverOpportunity] 전용 스킬\n<style="highlight">대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)</style>\n<style="highlight">[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=2].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [SilverOpportunity], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SilverOpportunity] exclusive Skill\n<style="highlight">Deal +5% damage for every type of negative effect on target (max 20%)</style>\n<style="highlight">[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)</style>\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\n<style="highlight">Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 20%)</style>\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. 2)</style>\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
587. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021506].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność 5 (×0) (ulepszenie 4) — opis] [SilverOpportunity] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +<style="highlight">10</style>% (최대 <style="highlight">30</style>%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021506].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [SilverOpportunity], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SilverOpportunity] exclusive Skill\nDeal +<style="highlight">10</style>% damage for every type of negative effect on target (max <style="highlight">30</style>%)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max <style="highlight">4</style>)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\nZadaje +<style="highlight">10</style>% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. <style="highlight">30</style>%)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na celu (maks. <style="highlight">4</style>)\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
589. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 억압당한 육체의 해방
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].name ; dataList[id=1021507].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 50 znaków
   EN: Liberation of the Repressed Flesh
   PL: Wyzwolenie Tłumionego Ciała
590. [Umiejętność 6 (×0) (ulepszenie 3) — opis] [SilverOpportunity] 전용 스킬\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +1%\n- [ChargeBodyArt]가 3/5 이상이면, 공격 가중치 +1/+2\n- 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SilverOpportunity] exclusive Skill\n[WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n[WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 2)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count and gain the following effects:\n- Final Power +2\n- Deal +1% damage for every [ChargeBodyArt] Count consumed\n- At 3+/5+ [ChargeBodyArt], gain +1/+2 Atk Weight\n- Convert all Coins on this Skill to [SuperCoin]s
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\n[WhenUse] Zadaje +30% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: liczy się części ciała)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na głównym celu (maks. 2)\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +1% obrażeń za każdy 1 zużytego Licznika [ChargeBodyArt]\n- Przy 3+/5+ [ChargeBodyArt] Waga ataku +1/+2\n- Wszystkie Monety tej Umiejętności stają się [SuperCoin]
591. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1021507].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1021507].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1021507].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1021507].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedAttack] Gain 1 [SlashDamageUp] next turn (once per turn)
   PL: [OnSucceedAttack] Zyskuje w następnej turze 1 [SlashDamageUp] (1 raz na turę)
596. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 대상의 부정적인 효과 1개당, 피해량 +5% (최대 30%)
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1021507].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1021507].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność 6 (×0) (ulepszenie 4) — opis] [SilverOpportunity] 전용 스킬\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +1%\n- [ChargeBodyArt]가 3/5 이상이면, 공격 가중치 +1/+2\n- 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=4].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SilverOpportunity] exclusive Skill\n[WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n[WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 3)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count and gain the following effects:\n- Final Power +2\n- Deal +1% damage for every [ChargeBodyArt] Count consumed\n- At 3+/5+ [ChargeBodyArt], gain +1/+2 Atk Weight\n- Convert all Coins on this Skill to [SuperCoin]s
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\n[WhenUse] Zadaje +30% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: liczy się części ciała)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na głównym celu (maks. 3)\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +1% obrażeń za każdy 1 zużytego Licznika [ChargeBodyArt]\n- Przy 3+/5+ [ChargeBodyArt] Waga ataku +1/+2\n- Wszystkie Monety tej Umiejętności stają się [SuperCoin]
599. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021507].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Obrona (ulepszenia 1,4) — nazwa] 전시회 준비
   źródło: Skills_personality-02.json :: dataList[id=1021504].levelList[level=1].name ; dataList[id=1021504].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Exhibition Arrangements
   PL: Przygotowanie Wystawy
601. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[IronMaidenPersonality] 전용 스킬\n[WinDuel] 공격자의 [Laceration] 횟수 1 증가 (턴당 최대 2회)\n[WinDuel] 공격자에게 공격자의 [Laceration] 위력만큼 관통 피해를 입힘 (최대 피해 20)
   źródło: Skills_personality-02.json :: dataList[id=1021504].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [IronMaidenPersonality], [WinDuel], [Laceration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [CanDuelGuard]\n[IronMaidenPersonality] exclusive Skill\n[WinDuel] Inflict +1 [Laceration] Count on the attacker (2 times per turn)\n[WinDuel] Deal Pierce damage equal to [Laceration] Potency on the attacker (max damage: 20)
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [IronMaidenPersonality]\n[WinDuel] Zwiększa Licznik [Laceration] atakującego o 1 (maks. 2 razy na turę)\n[WinDuel] Zadaje atakującemu obrażenia Kłucia równe jego Mocy [Laceration] (maks. 20 obrażeń)
602. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[IronMaidenPersonality] 전용 스킬\n[WinDuel] 공격자의 [Laceration] 횟수 2 증가 (턴당 최대 2회)\n[WinDuel] 공격자에게 <style="highlight">(공격자의 [Laceration] 위력 x 2)</style>만큼 관통 피해를 입힘 (최대 피해 <style="highlight">30</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021504].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [IronMaidenPersonality], [WinDuel], [Laceration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [CanDuelGuard]\n[IronMaidenPersonality] exclusive Skill\n[WinDuel] Inflict +2 [Laceration] Count on the attacker (2 times per turn)\n[WinDuel] Deal Pierce damage equal to <style="highlight">([Laceration] Potency on the attacker x 2)</style> (max damage: <style="highlight">30</style>)
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [IronMaidenPersonality]\n[WinDuel] Zwiększa Licznik [Laceration] atakującego o 2 (maks. 2 razy na turę)\n[WinDuel] Zadaje atakującemu obrażenia Kłucia równe <style="highlight">(Moc [Laceration] atakującego x 2)</style> (maks. <style="highlight">30</style> obrażeń)
604. [Obrona (ulepszenia 1,4) — nazwa] 시작된 전시회
   źródło: Skills_personality-02.json :: dataList[id=1021508].levelList[level=1].name ; dataList[id=1021508].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: The Exhibition Begins
   PL: Wystawa się rozpoczęła
605. [Obrona (ulepszenie 1) — opis] [SilverOpportunity] 전용 스킬\n[StartBattle] [SupportProtect] 1 얻음 (턴당 1회)\n[OnSucceedEvade] 공격자에게 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021508].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [StartBattle], [SupportProtect], [OnSucceedEvade], [Binding]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Binding] = 속박 / Bind
   EN: [SilverOpportunity] exclusive Skill\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[OnSucceedEvade] Inflict 1 [Binding] next turn against the attacker (once per turn)
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[OnSucceedEvade] Nakłada w następnej turze 1 [Binding] na atakującego (1 raz na turę)
606. [Obrona (ulepszenie 4) — opis] [SilverOpportunity] 전용 스킬\n[StartBattle] [SupportProtect] 1 얻음 (턴당 1회)\n[OnSucceedEvade] 공격자에게 다음 턴에 [Binding] 1 부여 (턴당 1회)\n[OnSucceedEvade] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021508].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [SilverOpportunity], [StartBattle], [SupportProtect], [OnSucceedEvade], [Binding], [Agility]
   znaczenie tagów: [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Binding] = 속박 / Bind; [Agility] = 신속 / Haste
   EN: [SilverOpportunity] exclusive Skill\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[OnSucceedEvade] Inflict 1 [Binding] next turn against the attacker (once per turn)\n[OnSucceedEvade] Gain 1 [Agility] next turn (once per turn)
   PL: Umiejętność wyłącznie dla [SilverOpportunity]\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[OnSucceedEvade] Nakłada w następnej turze 1 [Binding] na atakującego (1 raz na turę)\n[OnSucceedEvade] Zyskuje w następnej turze 1 [Agility] (1 raz na turę)
607. [Obrona (ulepszenia 1,4) — nazwa] 반달리즘은 사절입니다
   źródło: Skills_personality-02.json :: dataList[id=1021509].levelList[level=1].name ; dataList[id=1021509].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+4)
   limit: do 50 znaków
   EN: No Acts of Vandalism Allowed.
   PL: Wandalizmy się nie toleruje.
608. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[SilverOpportunity] 전용 스킬\n[SupportProtect] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021509].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SilverOpportunity], [SupportProtect], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [DuelCounter]\n[SilverOpportunity] exclusive Skill\n[SupportProtect] exclusive Skill\nDeal +5% damage for every type of negative effect on target (max 20%)\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: [DuelCounter]\nUmiejętność wyłącznie dla [SilverOpportunity]\nUmiejętność wyłącznie dla [SupportProtect]\nZadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 20%)\n[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
609. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021509].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021509].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[SilverOpportunity] 전용 스킬\n[SupportProtect] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +<style="highlight">10</style>% (최대 <style="highlight">30</style>%)\n[WhenUse] 대상의 [Laceration] 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-02.json :: dataList[id=1021509].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [SilverOpportunity], [SupportProtect], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [DuelCounter]\n[SilverOpportunity] exclusive Skill\n[SupportProtect] exclusive Skill\nDeal +<style="highlight">10</style>% damage for every type of negative effect on target (max <style="highlight">30</style>%)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: [DuelCounter]\nUmiejętność wyłącznie dla [SilverOpportunity]\nUmiejętność wyłącznie dla [SupportProtect]\nZadaje +<style="highlight">10</style>% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. <style="highlight">30</style>%)\n[WhenUse] Moc Monet +1 za każde 6 [Laceration] na celu <style="highlight">(maks. 2)</style>\n[WhenUse] Przy 10+ Liczniku [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt] i stosuje poniższe efekty:\n- Moc Starcia +1\n- Ostatnia Moneta tej Umiejętności staje się [SuperCoin]
611. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021509].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
612. [Pasywka bojowa (od ulepszenia 1) — nazwa] 소중한 작품 파시아
   źródło: Passives.json :: dataList[id=1021504].name
   limit: do 40 znaków
   EN: Fascia, My Precious Artwork
   PL: Fascia, Moje Ukochane Dzieło
613. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 자신의 [ChargeBodyArt] 횟수가 (전장에 있는 약지 소속 아군 수 x 2)만큼 증가 (최대 10)\n\n스킬 종료 시 해당 스킬로 체력 또는 보호막 피해를 입혔으면, 자신의 [ChargeBodyArt] 횟수 5 증가\n- 대상이 사망했으면, 추가로 횟수 3 증가\n\n전투 중 누적으로 자신의 [ChargeBodyArt] 횟수 10을 소모할 때마다 [ChargeBodyArt]를 1 얻음\n- 위 효과로 [ChargeBodyArt] 위력이 2 이상이 되면, [FasciaPersonality] 얻음\n\n기본 공격 스킬과 합 가능 반격 스킬이 [Charge] 횟수를 얻는 스킬로 취급됨
   źródło: Passives.json :: dataList[id=1021504].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeBodyArt], [FasciaPersonality], [Charge]
   znaczenie tagów: [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [FasciaPersonality] = 작품명: 파시아 / Artwork: Fascia; [Charge] = 충전 / Charge
   EN: Upon entering the Encounter for the first time, gain +(# of The Ring-faction allies on the field x 2) [ChargeBodyArt] Count (max 10)\n\nSkill End: If the Skill dealt HP or Shield damage, gain +5 [ChargeBodyArt] Count\n- If target is killed, gain +3 additional [ChargeBodyArt] Count\n\nGain 1 [ChargeBodyArt] every time this unit consumes 10 cumulative [ChargeBodyArt] Count in this Encounter\n- If the above effect brings this unit's [ChargeBodyArt] Potency to 2 or higher, gain [FasciaPersonality]\n\nBase Attack Skills and Clashable Counter Skill count as Skills that gain [Charge] Count
   PL: Przy pierwszym pojawieniu się na polu zyskuje (liczba sojuszników frakcji Serdecznego na polu x 2) Licznika [ChargeBodyArt] (maks. 10)\n\nNa koniec Umiejętności: jeżeli ta Umiejętność zadała obrażenia HP lub Tarczy, zwiększa własny Licznik [ChargeBodyArt] o 5\n- Jeżeli cel zginął, zwiększa Licznik dodatkowo o 3\n\nZa każde łączne zużycie 10 własnego Licznika [ChargeBodyArt] podczas walki zyskuje 1 [ChargeBodyArt]\n- Jeżeli wskutek tego efektu Moc [ChargeBodyArt] osiągnie 2 lub więcej, zyskuje [FasciaPersonality]\n\nPodstawowe Umiejętności ataku i Kontrę zdolną do Starcia traktuje się jak Umiejętności zyskujące Licznik [Charge]
614. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [ChargeBodyArt] 얻음
   źródło: Passives.json :: dataList[id=1021504].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeBodyArt]
   znaczenie tagów: [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: Gain [ChargeBodyArt]
   PL: Zyskuje [ChargeBodyArt]
615. [Pasywka bojowa (od ulepszenia 1) — nazwa] 보호와 억제를 위한 갑주
   źródło: Passives.json :: dataList[id=1021503].name
   limit: do 50 znaków
   EN: Armor of Protection and Repression
   PL: Zbroja dla Ochrony i Tłumienia
616. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지에 첫 등장 시 [IronMaidenPersonality] 얻음\n\n턴 종료 시 자신에게 [FasciaPersonality]가 있으면, [IronMaidenPersonality]이 소멸하고, [SilverOpportunity] 얻음 (전투당 1회)\n- 흐트러짐 상태면, 흐트러짐 해제 (강제 흐트러짐 제외)
   źródło: Passives.json :: dataList[id=1021503].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [IronMaidenPersonality], [FasciaPersonality], [SilverOpportunity]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden; [FasciaPersonality] = 작품명: 파시아 / Artwork: Fascia; [SilverOpportunity] = 구속 해제 - 창작 몰입 / The Self Unbound - Flow State
   EN: Upon entering the Encounter for the first time, gain [IronMaidenPersonality]\n\nTurn End: If this unit has [FasciaPersonality], this unit loses [IronMaidenPersonality] and gains [SilverOpportunity] (once per Encounter)\n- When Staggered, recover from Stagger (excluding forced Staggers)
   PL: Przy pierwszym pojawieniu się na polu zyskuje [IronMaidenPersonality]\n\nNa koniec tury: jeżeli ta jednostka ma [FasciaPersonality], traci [IronMaidenPersonality] i zyskuje [SilverOpportunity] (1 raz na spotkanie)\n- Jeżeli jest Ogłuszona, dochodzi do siebie z Ogłuszenia (nie licząc wymuszonego Ogłuszenia)
617. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [IronMaidenPersonality] 해제
   źródło: Passives.json :: dataList[id=1021503].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [IronMaidenPersonality]
   znaczenie tagów: [IronMaidenPersonality] = 아이언 메이든 / Iron Maiden
   EN: Remove [IronMaidenPersonality]
   PL: Usuwa [IronMaidenPersonality]
618. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 크리틱으로부터의 영감
   źródło: Passives.json :: dataList[id=1021501].name
   limit: do 40 znaków
   EN: Inspired by Critique
   PL: Natchnienie z Krytyki
619. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] [MelodyBodyArt]의 속도, 합 위력, 피해량이 증가하는 효과가 2배로 적용됨\n\n공격 적중 시 해당 공격 스킬로 부정적인 효과를 부여했으면, 공격 종료 시 자신의 정신력 4 회복 (턴당 2회)
   źródło: Passives.json :: dataList[id=1021501].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [MelodyBodyArt]
   znaczenie tagów: [MelodyBodyArt] = 신체가 울리는 선율 / Somatic Frisson-inspiring Melody
   EN: Double the amount of Speed, Clash Power, damage buff gained from [MelodyBodyArt]\n\nOn Hit, if the Attack Skill inflicted a negative effect, heal 4 SP at Attack End (2 times per turn)
   PL: Efekty [MelodyBodyArt] zwiększające Szybkość, Moc Starcia i obrażenia działają 2 razy silniej\n\nPrzy trafieniu: jeżeli ta Umiejętność ataku nałożyła negatywny efekt, odzyskuje 4 Poczytalności na koniec ataku (2 razy na turę)
620. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — podsumowanie] 자신의 정신력 회복
   źródło: Passives.json :: dataList[id=1021501].summary
   limit: do 120 znaków
   EN: Heal SP on self
   PL: Odzyskuje Poczytalność
621. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — nazwa] 크리틱으로부터의 영감
   źródło: Passives.json :: dataList[id=1021511].name
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — opis] [MelodyBodyArt]의 속도, 합 위력, 피해량이 증가하는 효과가 2배로 적용됨\n\n공격 적중 시 해당 공격 스킬로 부정적인 효과를 부여했으면, 공격 종료 시 자신의 정신력 4 회복 (턴당 2회)\n- 이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [SlashDamageUp] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1021511].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [MelodyBodyArt], [SlashDamageUp]
   znaczenie tagów: [MelodyBodyArt] = 신체가 울리는 선율 / Somatic Frisson-inspiring Melody; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: Double the amount of Speed, Clash Power, damage buff gained from [MelodyBodyArt]\n\nOn Hit, if the Attack Skill inflicted a negative effect, heal 4 SP at Attack End (2 times per turn)\n- If this unit's SP is at max, gain 1 [SlashDamageUp] next turn when this unit heals SP with this effect (once per turn)
   PL: Efekty [MelodyBodyArt] zwiększające Szybkość, Moc Starcia i obrażenia działają 2 razy silniej\n\nPrzy trafieniu: jeżeli ta Umiejętność ataku nałożyła negatywny efekt, odzyskuje 4 Poczytalności na koniec ataku (2 razy na turę)\n- Jeżeli Poczytalność tej jednostki jest pełna, odzyskując Poczytalność tym efektem zyskuje w następnej turze 1 [SlashDamageUp] (1 raz na turę)
623. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 자신의 정신력 회복\n조건 만족 시 다음 턴에 [SlashDamageUp] 얻음
   źródło: Passives.json :: dataList[id=1021511].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: Heal SP on self\nGain [SlashDamageUp] next turn if conditions are met
   PL: Odzyskuje Poczytalność\nWarunkowo zyskuje w następnej turze [SlashDamageUp]
624. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Lust, posiadane 2× Envy) — nazwa] 아이언메이든 - 가시
   źródło: Passives.json :: dataList[id=1021521].name
   limit: do 40 znaków
   EN: Iron Maiden - Spikes
   PL: Żelazna Dziewica - Kolce
625. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Lust, posiadane 2× Envy) — opis] 이번 턴에 수비 스킬을 장착한 아군이 피격 시 공격자에게 [Laceration] 4 부여 (턴당 2회)\n- 이미 [Laceration]이 있으면, 대신 공격자의 [Laceration] 횟수 2 증가
   źródło: Passives.json :: dataList[id=1021521].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When hit, allies that equipped Defense Skill on their Slots this turn inflict 4 [Laceration] on the attacker (2 times per turn)\n- If the attacker already has [Laceration], inflict +2 [Laceration] Count instead
   PL: Gdy w tej turze sojusznik z wyposażoną Umiejętnością obrony zostanie trafiony, nakłada 4 [Laceration] na atakującego (2 razy na turę)\n- Jeżeli atakujący ma już [Laceration], zamiast tego zwiększa jego Licznik [Laceration] o 2
626. [Pasywka wsparcia (od ulepszenia 3, posiadane 1× Lust, posiadane 2× Envy) — podsumowanie] 피격 시 공격자에게 [Laceration] 부여
   źródło: Passives.json :: dataList[id=1021521].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When hit, inflict [Laceration] on the attacker
   PL: Przy trafieniu nakłada [Laceration] na atakującego

## [000] Dawn Office Fixer — Faust — 새벽 사무소 해결사
- ID Tożsamości: `10216` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9109 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Burn, Tremor

627. [Karta Tożsamości — tytuł] 새벽 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10216].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dawn Office\nFixer
   PL: Biuro Świtu\nFikser
628. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10216].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10216].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Karta Tożsamości — opis] 파우스트의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10216].desc
   limit: do 120 znaków
   EN: Faust's 16th Identity
   PL: Szesnasta Tożsamość Faust
631. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 여명의 섬광
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=1].name ; dataList[id=1021601].levelList[level=2].name ; dataList[id=1021601].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flash of Sunup
   PL: Błysk Świtu
632. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [StigmaWorkshopCelloCaseOne] 10당, 합 위력 +1 (최대 2)\n[WhenUse] [StigmaWorkshopCelloCaseOne]이 20 이상이면, 마지막 코인 1회 재사용
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: [WhenUse] Clash Power +1 for every 10 [StigmaWorkshopCelloCaseOne] (max 2)\n[WhenUse] At 20+ [StigmaWorkshopCelloCaseOne], Reuse the final Coin once
   PL: [WhenUse] Moc Starcia +1 za każde 10 [StigmaWorkshopCelloCaseOne] (maks. 2)\n[WhenUse] Przy 20+ [StigmaWorkshopCelloCaseOne] używa ostatniej monety ponownie
633. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
635. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] [StigmaWorkshopCelloCaseOne] 10당, 합 위력 +1 (최대 2)\n[WhenUse] [StigmaWorkshopCelloCaseOne]이 20 이상이면, 마지막 코인 1회 재사용
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)</style>\n[WhenUse] Clash Power +1 for every 10 [StigmaWorkshopCelloCaseOne] (max 2)\n[WhenUse] At 20+ [StigmaWorkshopCelloCaseOne], Reuse the final Coin once
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. 2)</style>\n[WhenUse] Moc Starcia +1 za każde 10 [StigmaWorkshopCelloCaseOne] (maks. 2)\n[WhenUse] Przy 20+ [StigmaWorkshopCelloCaseOne] używa ostatniej monety ponownie
636. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
637. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]<style="highlight"></style>
638. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n<style="highlight">[WhenUse] [StigmaWorkshopCelloCaseOne] 4 얻음</style>\n[WhenUse] [StigmaWorkshopCelloCaseOne] 10당, 합 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] [StigmaWorkshopCelloCaseOne]이 20 이상이면, 마지막 코인 1회 재사용
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: [WhenUse] Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max <style="highlight">3</style>)\n<style="highlight">[WhenUse] Gain 4 [StigmaWorkshopCelloCaseOne]</style>\n[WhenUse] Clash Power +1 for every 10 [StigmaWorkshopCelloCaseOne] (max <style="highlight">3</style>)\n[WhenUse] At 20+ [StigmaWorkshopCelloCaseOne], Reuse the final Coin once
   PL: [WhenUse] Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. <style="highlight">3</style>)\n<style="highlight">[WhenUse] Zyskuje 4 [StigmaWorkshopCelloCaseOne]</style>\n[WhenUse] Moc Starcia +1 za każde 10 [StigmaWorkshopCelloCaseOne] (maks. <style="highlight">3</style>)\n[WhenUse] Przy 20+ [StigmaWorkshopCelloCaseOne] używa ostatniej monety ponownie
639. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여, <style="highlight">[Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] and <style="highlight">+1 [Combustion] Count</style>
   PL: [OnSucceedAttack] Nakłada 2 [Combustion] i <style="highlight">zwiększa Licznik [Combustion] o 1</style>
640. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 나비 베기
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=1].name ; dataList[id=1021602].levelList[level=2].name ; dataList[id=1021602].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Butterfly Slash
   PL: Cięcie Motyla
641. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [StigmaWorkshopCelloCaseOne] 10당,\n- 합 위력 +1 (최대 2)\n- 마지막 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: [WhenUse] For every 10 [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Clash Power +1 (max 2)\n- Reuse the final Coin once (2 times per Skill)
   PL: [WhenUse] Za każde 10 [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Moc Starcia +1 (maks. 2)\n- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)
642. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [ReUseOnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: [ReUseOnSucceedAttack] Inflict 1 [Combustion]
   PL: [ReUseOnSucceedAttack] Nakłada 1 [Combustion]
644. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [ReUseOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (once per Skill)
   PL: [ReUseOnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1 (1 raz na Umiejętność)
645. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)\n[WhenUse] [StigmaWorkshopCelloCaseOne] 3 얻음</style>\n[WhenUse] [StigmaWorkshopCelloCaseOne] 10당,\n- 합 위력 +1 (최대 2)\n- 마지막 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] Gain 3 [StigmaWorkshopCelloCaseOne]</style>\n[WhenUse] For every 10 [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Clash Power +1 (max 2)\n- Reuse the final Coin once (2 times per Skill)
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. 2)\n[WhenUse] Zyskuje 3 [StigmaWorkshopCelloCaseOne]</style>\n[WhenUse] Za każde 10 [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Moc Starcia +1 (maks. 2)\n- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)
646. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [StigmaWorkshopCelloCaseOne]이 10 이상이면,\n- [Combustion] 횟수 1 증가\n- [Vibration] 횟수 1 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [StigmaWorkshopCelloCaseOne], [Combustion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] At 10+ [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Inflict +1 [Combustion] Count\n- Inflict +1 [Vibration] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 10+ [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Zwiększa Licznik [Combustion] o 1\n- Zwiększa Licznik [Vibration] o 1</style>
647. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [ReUseOnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1021602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: [ReUseOnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
649. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1021602].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [ReUseOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (once per Skill)<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1 (1 raz na Umiejętność)<style="highlight"></style>
650. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] [StigmaWorkshopCelloCaseOne] <style="highlight">6</style> 얻음\n[WhenUse] [StigmaWorkshopCelloCaseOne] 10당,\n- 합 위력 +1 (최대 <style="highlight">3</style>)\n- 마지막 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: [WhenUse] Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max <style="highlight">3</style>)\n[WhenUse] Gain <style="highlight">6</style> [StigmaWorkshopCelloCaseOne]\n[WhenUse] For every 10 [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Clash Power +1 (max <style="highlight">3</style>)\n- Reuse the final Coin once (2 times per Skill)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. <style="highlight">3</style>)\n[WhenUse] Zyskuje <style="highlight">6</style> [StigmaWorkshopCelloCaseOne]\n[WhenUse] Za każde 10 [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Moc Starcia +1 (maks. <style="highlight">3</style>)\n- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)
651. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [StigmaWorkshopCelloCaseOne] <style="highlight">10당,\n- [Combustion] 횟수 1 증가 (최대 2)\n- [Vibration] 횟수 1 증가 (최대 2)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [StigmaWorkshopCelloCaseOne], [Combustion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] <style="highlight">For every 10 [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Inflict +1 [Combustion] Count (max 2)\n- Inflict +1 [Vibration] Count (max 2)</style>
   PL: [OnSucceedAttack] <style="highlight">Za każde 10 [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Zwiększa Licznik [Combustion] o 1 (maks. 2)\n- Zwiększa Licznik [Vibration] o 1 (maks. 2)</style>
652. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 사출
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=3].name ; dataList[id=1021603].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Eject
   PL: Wystrzał
653. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] [StigmaWorkshopCelloCaseOne]이 30이면, ‘사출-정오’로 발동됨 (턴당 1회)\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [StigmaWorkshopCelloCaseOne] 5 얻음\n[WhenUse] [StigmaWorkshopCelloCaseOne] 10당,\n- 합 위력 +1 (최대 2)\n- 대상의 [Combustion] 횟수 1 증가 (최대 2)\n- 대상의 [Vibration] 횟수 1 증가 (최대 2)\n- 마지막 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=3].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [StigmaWorkshopCelloCaseOne], [WhenUse], [Combustion], [Vibration], [TabExplain]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [BeforeUse] At 30 [StigmaWorkshopCelloCaseOne], activate "Eject - High Noon[TabExplain]" instead (once per turn)\n[WhenUse] If target has 6+ ([Combustion] + [Vibration]), Coin Power +1\n[WhenUse] Gain 5 [StigmaWorkshopCelloCaseOne]\n[WhenUse] For every 10 [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Clash Power +1 (max 2)\n- Inflict +1 [Combustion] Count (max 2)\n- Inflict +1 [Vibration] Count (max 2)\n- Reuse the final Coin once (2 times per Skill)
   PL: [BeforeUse] Przy 30 [StigmaWorkshopCelloCaseOne] zamiast tego uruchamia „Wystrzał - Południe” (1 raz na turę)\n[WhenUse] Jeżeli cel ma 6+ (suma [Combustion] i [Vibration]), Moc Monet +1\n[WhenUse] Zyskuje 5 [StigmaWorkshopCelloCaseOne]\n[WhenUse] Za każde 10 [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Moc Starcia +1 (maks. 2)\n- Zwiększa Licznik [Combustion] celu o 1 (maks. 2)\n- Zwiększa Licznik [Vibration] celu o 1 (maks. 2)\n- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)
654. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
655. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationIgnition]
656. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (2 times per Skill)
   PL: [OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1 (2 razy na Umiejętność)
657. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [ReUseOnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 643 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] [StigmaWorkshopCelloCaseOne]이 30이면, ‘사출-정오’로 발동됨 (턴당 1회)\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [StigmaWorkshopCelloCaseOne] <style="highlight">8</style> 얻음\n[WhenUse] [StigmaWorkshopCelloCaseOne] 10당,\n- 합 위력 +1 (최대 <style="highlight">3</style>)\n- 대상의 [Combustion] 횟수 1 증가 (최대 <style="highlight">3</style>)\n- 대상의 [Vibration] 횟수 1 증가 (최대 <style="highlight">3</style>)\n- 마지막 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=4].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [StigmaWorkshopCelloCaseOne], [WhenUse], [Combustion], [Vibration], [TabExplain]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [BeforeUse] At 30 [StigmaWorkshopCelloCaseOne], activate "Eject - High Noon[TabExplain]" instead (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)</style>\n[WhenUse] Gain <style="highlight">8</style> [StigmaWorkshopCelloCaseOne]\n[WhenUse] For every 10 [StigmaWorkshopCelloCaseOne], gain the following effects:\n- Clash Power +1 (max <style="highlight">3</style>)\n- Inflict +1 [Combustion] Count (max <style="highlight">3</style>)\n- Inflict +1 [Vibration] Count (max <style="highlight">3</style>)\n- Reuse the final Coin once (2 times per Skill)
   PL: [BeforeUse] Przy 30 [StigmaWorkshopCelloCaseOne] zamiast tego uruchamia „Wystrzał - Południe” (1 raz na turę)\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> (suma [Combustion] i [Vibration] celu) <style="highlight">(maks. 2)</style>\n[WhenUse] Zyskuje <style="highlight">8</style> [StigmaWorkshopCelloCaseOne]\n[WhenUse] Za każde 10 [StigmaWorkshopCelloCaseOne] zyskuje następujące efekty:\n- Moc Starcia +1 (maks. <style="highlight">3</style>)\n- Zwiększa Licznik [Combustion] celu o 1 (maks. <style="highlight">3</style>)\n- Zwiększa Licznik [Vibration] celu o 1 (maks. <style="highlight">3</style>)\n- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)
659. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
660. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationIgnition]<style="highlight"></style>
661. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 <style="highlight">3</style>회)
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (<style="highlight">3</style> times per Skill)
   PL: [OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1 (<style="highlight">3</style> razy na Umiejętność)
662. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [ReUseOnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność 4 (×0) (ulepszenia 2–4) — nazwa] 연계
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=2].name ; dataList[id=1021605].levelList[level=3].name ; dataList[id=1021605].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Seconded Offensive
   PL: Łączenie
664. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가 (턴당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count (2 times per turn)
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] o 1 (2 razy na turę)
665. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가 (턴당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count (2 times per turn)
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] o 1 (2 razy na turę)
666. [Umiejętność 4 (×0) (ulepszenie 3) — opis] <style="highlight">[WhenUse] [StigmaWorkshopCelloCaseOne] 1당, 피해량 +1% (최대 30%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: <style="highlight">[WhenUse] Deal +1% damage for every [StigmaWorkshopCelloCaseOne] on self (max 30%)</style>
   PL: <style="highlight">[WhenUse] Zadaje +1% obrażeń za każdy 1 [StigmaWorkshopCelloCaseOne] (maks. 30%)</style>
667. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1021605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] o 1 (2 razy na turę)<style="highlight"></style>
668. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1021605].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] o 1 (2 razy na turę)<style="highlight"></style>
669. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WhenUse] [StigmaWorkshopCelloCaseOne] <style="highlight">수치에 따라\n- 1당, 피해량 +2% (최대 60%)\n- 10당, 최종 위력 +1 (최대 3)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021605].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [StigmaWorkshopCelloCaseOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: <style="highlight">[WhenUse] Gain the following effects based on [StigmaWorkshopCelloCaseOne] Stack:\n- Deal +2% damage for every Stack (max 60%)\n- Final Power +1 for every 10 Stacks (max 3)</style>
   PL: <style="highlight">[WhenUse] Zyskuje następujące efekty zależnie od stosu [StigmaWorkshopCelloCaseOne]:\n- Zadaje +2% obrażeń za każdy 1 stos (maks. 60%)\n- Moc Końcowa +1 za każde 10 stosów (maks. 3)</style>
670. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 사출-정오
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].name ; dataList[id=1021606].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Eject - High Noon
   PL: Wystrzał - Południe
671. [Umiejętność 5 (×0) (ulepszenie 3) — opis] [WideAreaRampage]\n이 스킬 적중 시마다 대상에게\n- [Combustion] 1 또는 [Vibration] 1 부여\n- [VibrationIgnition]이 없으면, [VibrationIgnition]로 [Switch_Vibration] (대상별 1회)\n[WhenUse]\n- 합 위력 +3\n- 메인 타겟의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1, 합 위력 +2\n- 모든 타겟의 [Combustion] 횟수 2 증가\n- 모든 타겟의 [Vibration] 횟수 2 증가\n[EndSkill]\n- 적중한 모든 대상에게 다음 턴에 [ResultReduction] 1 부여 (턴당 1회)\n- [Firstlight] 1 얻음\n- [CaseOverheating] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [Combustion], [Vibration], [VibrationIgnition], [Switch_Vibration], [WhenUse], [EndSkill], [ResultReduction], [Firstlight], [CaseOverheating]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [ResultReduction] = 위력 감소 / Power Down …
   EN: [WideAreaRampage]\nActivate the following effects on target with every hit of this Skill:\n- Inflict 1 [Combustion] or 1 [Vibration]\n- If target has no [VibrationIgnition], trigger [Switch_Vibration] into [VibrationIgnition] (once per target)\n[WhenUse]\n- Clash Power +3\n- If the main target has 6+ ([Combustion] + [Vibration]), Coin Power +1 and Clash Power +2\n- Inflict +2 [Combustion] Count on all targets\n- Inflict +2 [Vibration] Count on all targets\n[EndSkill]\n- Inflict 1 [ResultReduction] next turn on all targets hit (once per turn)\n- Gain 1 [Firstlight]\n- Gain 1 [CaseOverheating]
   PL: [WideAreaRampage]\nPrzy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:\n- Nakłada 1 [Combustion] lub 1 [Vibration]\n- Jeżeli cel nie ma [VibrationIgnition], wywołuje [Switch_Vibration] do [VibrationIgnition] (1 raz na cel)\n[WhenUse]\n- Moc Starcia +3\n- Jeżeli główny cel ma 6+ (suma [Combustion] i [Vibration]), Moc Monet +1 i Moc Starcia +2\n- Zwiększa Licznik [Combustion] wszystkich celów o 2\n- Zwiększa Licznik [Vibration] wszystkich celów o 2\n[EndSkill]\n- Nakłada w następnej turze 1 [ResultReduction] na wszystkich trafionych celów (1 raz na turę)\n- Zyskuje 1 [Firstlight]\n- Zyskuje 1 [CaseOverheating]
672. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] 이 코인 재사용 (최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: Reuse this Coin (max 2 times)
   PL: Używa tej monety ponownie (maks. 2 razy)
676. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 진동 횟수 1 감소 (스킬당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (2 times per Skill)
   PL: [OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik Wstrząsu celu o 1 (2 razy na Umiejętność)
677. [Umiejętność 5 (×0) (ulepszenie 4) — opis] [WideAreaRampage]\n<style="highlight">피해량 +(자신과 타겟의 [Combustion] 위력 합)% (최대 20%, 대상별로 적용)</style>\n이 스킬 적중 시마다 대상에게\n- [Combustion] 1 또는 [Vibration] 1 부여\n- [VibrationIgnition]이 없으면, [VibrationIgnition]로 [Switch_Vibration] (대상별 1회)\n[WhenUse]\n- 합 위력 +3\n- 메인 타겟의 [Combustion]과 [Vibration]의 합 <style="highlight">6당, 코인 위력 +1, 합 위력 +2 (각각 최대 2, 4)</style>\n- 모든 타겟의 [Combustion] 횟수 <style="highlight">3</style> 증가\n- 모든 타겟의 [Vibration] 횟수 <style="highlight">3</style> 증가\n[EndSkill]\n- 적중한 모든 대상에게 다음 턴에 [ResultReduction] 1 부여 (턴당 1회)\n- [Firstlight] 1 얻음\n- [CaseOverheating] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].desc
   limit: do 900 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WideAreaRampage], [Combustion], [Vibration], [VibrationIgnition], [Switch_Vibration], [WhenUse], [EndSkill], [ResultReduction], [Firstlight], [CaseOverheating]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [ResultReduction] = 위력 감소 / Power Down …
   EN: [WideAreaRampage]\n<style="highlight">Deal +([Combustion] on self + [Combustion] on target)% damage (max 20%, counted per target)</style>\nActivate the following effects on target with every hit of this Skill:\n- Inflict 1 [Combustion] or 1 [Vibration]\n- If target has no [VibrationIgnition], trigger [Switch_Vibration] into [VibrationIgnition] (once per target)\n[WhenUse]\n- Clash Power +3\n<style="highlight">- Coin Power +1 and Clash Power +2 for every 6 ([Combustion] + [Vibration]) on the main target (max 2 and 4 respectively)</style>\n- Inflict +<style="highlight">3</style> [Combustion] Count on all targets\n- Inflict +<style="highlight">3</style> [Vibration] Count on all targets\n[EndSkill]\n- Inflict 1 [ResultReduction] next turn on all targets hit (once per turn)\n- Gain 1 [Firstlight]\n- Gain 1 [CaseOverheating]
   PL: [WideAreaRampage]\n<style="highlight">Zadaje +(suma Mocy [Combustion] tej jednostki i celu)% obrażeń (maks. 20%; liczone osobno dla każdego celu)</style>\nPrzy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:\n- Nakłada 1 [Combustion] lub 1 [Vibration]\n- Jeżeli cel nie ma [VibrationIgnition], wywołuje [Switch_Vibration] do [VibrationIgnition] (1 raz na cel)\n[WhenUse]\n- Moc Starcia +3\n- Moc Monet +1 i Moc Starcia +2 za każde <style="highlight">6</style> (suma [Combustion] i [Vibration] głównego celu) <style="highlight">(maks. odpowiednio 2 i 4)</style>\n- Zwiększa Licznik [Combustion] wszystkich celów o <style="highlight">3</style>\n- Zwiększa Licznik [Vibration] wszystkich celów o <style="highlight">3</style>\n[EndSkill]\n- Nakłada w następnej turze 1 [ResultReduction] na wszystkich trafionych celów (1 raz na turę)\n- Zyskuje 1 [Firstlight]\n- Zyskuje 1 [CaseOverheating]
678. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] 이 코인 재사용 (최대 2회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Reuse this Coin (max 2 times)<style="highlight"></style>
   PL: Używa tej monety ponownie (maks. 2 razy)<style="highlight"></style>
682. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[Firstlight]이 있으면, 피해량 +(대상의 [Combustion] 위력/2)% (최대 20%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Firstlight], [Combustion]
   znaczenie tagów: [Firstlight] = 전투 감각 / Battle Instinct; [Combustion] = 화상 / Burn
   EN: <style="highlight">If this unit has [Firstlight], deal +([Combustion] Potency on target / 2)% damage (max 20%)</style>
   PL: <style="highlight">Jeżeli ta jednostka ma [Firstlight], zadaje +(Moc [Combustion] celu / 2)% obrażeń (maks. 20%)</style>
683. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 진동 횟수 1 감소 (스킬당 <style="highlight">3</style>회)
   źródło: Skills_personality-02.json :: dataList[id=1021606].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (<style="highlight">3</style> times per Skill)
   PL: [OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik Wstrząsu celu o 1 (<style="highlight">3</style> razy na Umiejętność)
684. [Obrona (ulepszenia 1,3,4) — nazwa] 낙인
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=1].name ; dataList[id=1021604].levelList[level=3].name ; dataList[id=1021604].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Stigmatize
   PL: Napiętnowanie
685. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Combustion] 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Combustion] 5 감소 (턴당 1회)\n[WinDuel] 자신의 [Combustion] 3 감소 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Combustion], [WinDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n[WhenUse] At 5+ [Combustion], Coin Power +1\n[WhenUse] Lose 5 [Combustion] (once per turn)\n[WinDuel] Lose 3 [Combustion] (once per turn)
   PL: [DuelCounter]\n[WhenUse] Przy 5+ [Combustion] Moc Monet +1\n[WhenUse] Traci 5 [Combustion] (1 raz na turę)\n[WinDuel] Traci 3 [Combustion] (1 raz na turę)
686. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여 (턴당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Combustion] (2 razy na turę)
687. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)
688. [Obrona (ulepszenie 3) — opis] [DuelCounter]\n<style="highlight">[BeforeUse] [StigmaWorkshopCelloCaseOne]이 30이면, ‘정오의 해체’로 발동됨 (턴당 1회)\n- [CaseOverheating]이 있으면, 이 효과가 발동하지 않음\n[WhenUse] 자신의 [Combustion]이 5 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Combustion] 5 감소 (턴당 1회)\n[WinDuel] 자신의 [Combustion] 3 감소 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=3].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [BeforeUse], [StigmaWorkshopCelloCaseOne], [CaseOverheating], [WhenUse], [Combustion], [WinDuel], [TabExplain]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [BeforeUse] = [사용전] / [Before Use]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [CaseOverheating] = 과열된 관 / Overheated Coffin; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n<style="highlight">[BeforeUse] At 30 [StigmaWorkshopCelloCaseOne], activate "Dismemberment at High Noon[TabExplain]" instead (once per turn)\n- If this unit has [CaseOverheating], the effect above does not activate\n[WhenUse] At 5+ [Combustion], Coin Power +1</style>\n[WhenUse] Lose 5 [Combustion] (once per turn)\n[WinDuel] Lose 3 [Combustion] (once per turn)
   PL: [DuelCounter]\n<style="highlight">[BeforeUse] Przy 30 [StigmaWorkshopCelloCaseOne] zamiast tego uruchamia „Rozczłonkowanie w Południe” (1 raz na turę)\n- Jeżeli ta jednostka ma [CaseOverheating], ten efekt nie uruchamia się\n[WhenUse] Przy 5+ [Combustion] Moc Monet +1</style>\n[WhenUse] Traci 5 [Combustion] (1 raz na turę)\n[WinDuel] Traci 3 [Combustion] (1 raz na turę)
689. [Obrona (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1021604].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion] (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion] (2 razy na turę)<style="highlight"></style>
690. [Obrona (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1021604].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)<style="highlight"></style>
691. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">[StartBattle] [StigmaWorkshopCelloCaseOne] 6 얻음 (전투당 1회)</style>\n[BeforeUse] [StigmaWorkshopCelloCaseOne]이 30이면, ‘정오의 해체’로 발동됨 (턴당 1회)\n- [CaseOverheating]이 있으면, 이 효과가 발동하지 않음\n[WhenUse] 자신의 [Combustion] <style="highlight">5당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Combustion] 5 감소 (턴당 1회)\n[WinDuel] 자신의 [Combustion] 3 감소 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021604].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [StigmaWorkshopCelloCaseOne], [BeforeUse], [CaseOverheating], [WhenUse], [Combustion], [WinDuel], [TabExplain]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [BeforeUse] = [사용전] / [Before Use]; [CaseOverheating] = 과열된 관 / Overheated Coffin; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n<style="highlight">[StartBattle] Gain 6 [StigmaWorkshopCelloCaseOne] (once per Encounter)</style>\n[BeforeUse] At 30 [StigmaWorkshopCelloCaseOne], activate "Dismemberment at High Noon[TabExplain]" instead (once per turn)\n- If this unit has [CaseOverheating], the effect above does not activate\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Combustion] on self (max 2)</style>\n[WhenUse] Lose 5 [Combustion] (once per turn)\n[WinDuel] Lose 3 [Combustion] (once per turn)
   PL: [DuelCounter]\n<style="highlight">[StartBattle] Zyskuje 6 [StigmaWorkshopCelloCaseOne] (1 raz na spotkanie)</style>\n[BeforeUse] Przy 30 [StigmaWorkshopCelloCaseOne] zamiast tego uruchamia „Rozczłonkowanie w Południe” (1 raz na turę)\n- Jeżeli ta jednostka ma [CaseOverheating], ten efekt nie uruchamia się\n[WhenUse] Moc Monet +1 za każde <style="highlight">5</style> [Combustion] <style="highlight">(maks. 2)</style>\n[WhenUse] Traci 5 [Combustion] (1 raz na turę)\n[WinDuel] Traci 3 [Combustion] (1 raz na turę)
692. [Obrona (ulepszenia 3–4) — nazwa] 정오의 해체
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].name ; dataList[id=1021607].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Dismemberment at High Noon
   PL: Rozczłonkowanie w Południe
693. [Obrona (ulepszenie 3) — opis] [WideAreaRampage]\n피해량 +(자신의 잃은 체력 비율/2)% (최대 25%)\n이 스킬 적중 시마다 대상에게\n- [Combustion] 1 또는 [Vibration] 1 부여\n- [VibrationIgnition]이 없으면, [VibrationIgnition]로 [Switch_Vibration] (대상별 1회)\n[WhenUse]\n- 합 위력 +3\n- 메인 타겟의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1, 합 위력 +2\n- 모든 타겟의 [Combustion] 횟수 2 증가\n- 모든 타겟의 [Vibration] 횟수 2 증가\n[EndSkill]\n- 보유한 [Combustion]을 최대 30 소모하여 최대 체력의 (5 + 소모한 [Combustion])%만큼 체력 회복 (최대 35%)\n- [StigmaWorkshopCelloCaseOne] 모두 소모\n- [Firstlight] 3 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [Combustion], [Vibration], [VibrationIgnition], [Switch_Vibration], [WhenUse], [EndSkill], [StigmaWorkshopCelloCaseOne], [Firstlight]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin …
   EN: [WideAreaRampage]\nDeal +(missing HP percentage on self / 2)% damage (max 25%)\nActivate the following effects on target with every hit of this Skill:\n- Inflict 1 [Combustion] or 1 [Vibration]\n- If target does not have [VibrationIgnition], trigger [Switch_Vibration] into [VibrationIgnition] (once per target)\n[WhenUse]\n- Clash Power +3\n- If the main target has 6+ ([Combustion] + [Vibration]), Coin Power +1 and Clash Power +2\n- Inflict +2 [Combustion] Count on all targets\n- Inflict +2 [Vibration] Count on all targets\n[EndSkill]\n- Consume up to 30 [Combustion] on self and heal (5 + [Combustion] consumed)% HP (max 35%)\n- Consume all [StigmaWorkshopCelloCaseOne] on self\n- Gain 3 [Firstlight]
   PL: [WideAreaRampage]\nZadaje +(brakujące % HP tej jednostki / 2)% obrażeń (maks. 25%)\nPrzy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:\n- Nakłada 1 [Combustion] lub 1 [Vibration]\n- Jeżeli cel nie ma [VibrationIgnition], wywołuje [Switch_Vibration] do [VibrationIgnition] (1 raz na cel)\n[WhenUse]\n- Moc Starcia +3\n- Jeżeli główny cel ma 6+ (suma [Combustion] i [Vibration]), Moc Monet +1 i Moc Starcia +2\n- Zwiększa Licznik [Combustion] wszystkich celów o 2\n- Zwiększa Licznik [Vibration] wszystkich celów o 2\n[EndSkill]\n- Zużywa do 30 [Combustion] i odzyskuje HP równe (5 + zużyte [Combustion])% Maks. HP (maks. 35%)\n- Zużywa całe [StigmaWorkshopCelloCaseOne]\n- Zyskuje 3 [Firstlight]
694. [Obrona (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Obrona (ulepszenie 3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Obrona (ulepszenie 3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Obrona (ulepszenie 3) — moneta 3, efekt 2 — opis] 이 코인 재사용 (최대 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Obrona (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 진동 횟수 1 감소 (스킬당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 676 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Obrona (ulepszenie 4) — opis] [WideAreaRampage]\n피해량 +(<style="highlight">자신의 잃은 체력 비율</style>)% (최대 <style="highlight">50%</style>)\n<style="highlight">피해량 +(타겟의 [Combustion] 위력)% (최대 20%, 대상별로 적용)</style>\n이 스킬 적중 시마다 대상에게\n- [Combustion] 1 또는 [Vibration] 1 부여\n- [VibrationIgnition]이 없으면, [VibrationIgnition]로 [Switch_Vibration] (대상별 1회)\n[WhenUse]\n- 합 위력 +3\n- 메인 타겟의 [Combustion]과 [Vibration]의 합 <style="highlight">6당, 코인 위력 +1, 합 위력 +2 (각각 최대 2, 4)</style>\n- 모든 타겟의 [Combustion] 횟수 <style="highlight">3</style> 증가\n- 모든 타겟의 [Vibration] 횟수 <style="highlight">3</style> 증가\n[EndSkill]\n- 보유한 [Combustion]을 최대 30 소모하여 최대 체력의 (<style="highlight">20</style> + 소모한 [Combustion])%만큼 체력 회복 (최대 <style="highlight">50%</style>)\n- [StigmaWorkshopCelloCaseOne] 모두 소모\n- [Firstlight] 3 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WideAreaRampage], [Combustion], [Vibration], [VibrationIgnition], [Switch_Vibration], [WhenUse], [EndSkill], [StigmaWorkshopCelloCaseOne], [Firstlight]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin …
   EN: [WideAreaRampage]\nDeal +(<style="highlight">missing HP percentage on self</style>)% damage (max <style="highlight">50%</style>)\n<style="highlight">Deal +([Combustion] Potency on target)% damage (max 20%, counted per target)</style>\nActivate the following effects on target with every hit of this Skill:\n- Inflict 1 [Combustion] or 1 [Vibration]\n- If target does not have [VibrationIgnition], trigger [Switch_Vibration] into [VibrationIgnition] (once per target)\n[WhenUse]\n- Clash Power +3\n- <style="highlight">Coin Power +1 and Clash Power +2 for every 6 ([Combustion] + [Vibration]) on the main target (max 2 and 4 respectively)</style>\n- Inflict +<style="highlight">3</style> [Combustion] Count on all targets\n- Inflict +<style="highlight">3</style> [Vibration] Count on all targets\n[EndSkill]\n- Consume up to 30 [Combustion] on self and heal (<style="highlight">20</style> + [Combustion] consumed)% HP (max <style="highlight">50%</style>)\n- Consume all [StigmaWorkshopCelloCaseOne] on self\n- Gain 3 [Firstlight]
   PL: [WideAreaRampage]\nZadaje +(<style="highlight">brakujące % HP tej jednostki</style>)% obrażeń (maks. <style="highlight">50%</style>)\n<style="highlight">Zadaje +(Moc [Combustion] celu)% obrażeń (maks. 20%; liczone osobno dla każdego celu)</style>\nPrzy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:\n- Nakłada 1 [Combustion] lub 1 [Vibration]\n- Jeżeli cel nie ma [VibrationIgnition], wywołuje [Switch_Vibration] do [VibrationIgnition] (1 raz na cel)\n[WhenUse]\n- Moc Starcia +3\n- Moc Monet +1 i Moc Starcia +2 za każde <style="highlight">6</style> (suma [Combustion] i [Vibration] głównego celu) <style="highlight">(maks. odpowiednio 2 i 4)</style>\n- Zwiększa Licznik [Combustion] wszystkich celów o <style="highlight">3</style>\n- Zwiększa Licznik [Vibration] wszystkich celów o <style="highlight">3</style>\n[EndSkill]\n- Zużywa do 30 [Combustion] i odzyskuje HP równe (<style="highlight">20</style> + zużyte [Combustion])% Maks. HP (maks. <style="highlight">50%</style>)\n- Zużywa całe [StigmaWorkshopCelloCaseOne]\n- Zyskuje 3 [Firstlight]
700. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Obrona (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Obrona (ulepszenie 4) — moneta 3, efekt 2 — opis] 이 코인 재사용 (최대 2회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Obrona (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[Firstlight]이 있으면, 피해량 +(대상의 [Combustion] 위력)% (최대 20%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Firstlight], [Combustion]
   znaczenie tagów: [Firstlight] = 전투 감각 / Battle Instinct; [Combustion] = 화상 / Burn
   EN: <style="highlight">If this unit has [Firstlight], deal +([Combustion] Potency on target)% damage (max 20%)</style>
   PL: <style="highlight">Jeżeli ta jednostka ma [Firstlight], zadaje +(Moc [Combustion] celu)% obrażeń (maks. 20%)</style>
705. [Obrona (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 진동 횟수 1 감소 (스킬당 <style="highlight">3</style>회)
   źródło: Skills_personality-02.json :: dataList[id=1021607].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Pasywka bojowa (od ulepszenia 1) — nazwa] 단열 코트
   źródło: Passives.json :: dataList[id=1021602].name
   limit: do 40 znaków
   EN: Heatproof Coat
   PL: Płaszcz Termiczny
707. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 [StigmaWorkshopCelloCaseOne] 0 얻음\n\n[Combustion] 피해로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음\n[Combustion] 효과로 받는 피해량 -50% (소수점 버림)\n- 체력이 50% 미만이면 효과가 강화되어, [Combustion] 효과로 받는 피해량 -75% (소수점 버림)
   źródło: Passives.json :: dataList[id=1021602].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [StigmaWorkshopCelloCaseOne], [Combustion]
   znaczenie tagów: [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [Combustion] = 화상 / Burn
   EN: Upon entering the Encounter for the first time, gain 0 [StigmaWorkshopCelloCaseOne]\n\nCannot be Staggered or fall below 1 HP due to [Combustion] damage\nTake -50% damage from [Combustion] effects (rounded down)\n- At less than 50% HP, take -75% damage from [Combustion] effects instead (rounded down)
   PL: Przy pierwszym pojawieniu się na polu zyskuje 0 [StigmaWorkshopCelloCaseOne]\n\nNie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Combustion]\nOtrzymuje -50% obrażeń od efektów [Combustion] (zaokrąglone w dół)\n- Przy HP poniżej 50% efekt się wzmacnia: otrzymuje -75% obrażeń od efektów [Combustion] (zaokrąglone w dół)
708. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 화상 효과로 받는 피해가 감소
   źródło: Passives.json :: dataList[id=1021602].summary
   limit: do 120 znaków
   EN: Take less damage from Burn effects
   PL: Otrzymuje mniej obrażeń od efektów Podpalenia
709. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] 당신이 만약 열을 다루는 공방 장비를 사용하기로 마음먹었다면, 더 많은 돈을 지불할 각오 또한 해야 한다. 단순히 더 날카롭고 튼튼하기만 하면 되는 통상적인 무기와 달리, 열을 내뿜는 무기는 자신이 그 열에 휘말리지 않도록 여러 밑작업이 필요하기 때문이다.\n\n물론 무작정 불을 지르는 무기나. 불이 잘 붙지 않는 원단 같은 건 쉽게 구할 수 있다. 하지만 사용자가 원하는 순간에, 원하는 만큼의 열을 섬세하게 가하는 무기와 열 자체를 막아주는 원단을 얻기 위해서는 보통 큰 비용을 치러야 하고, 그 사용법을 몸에 익히기 위한 노력도 게을리해선 안 된다.\n\n만약 그렇게 비용과 시간을 투자했다면, 그만큼 당신을 부르는 일거리가 많아질 것이다.
   źródło: Passives.json :: dataList[id=1021602].flavor
   limit: do 1240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If you have made up your mind to use Workshop gears that utilize heat, then you had best be prepared to pay a slew of hidden costs. Unlike conventional weapons, whose variables are in the more obviously observable territory, such as sharpness and durability, weapons that radiate heat require all manner of groundwork to ensure that the wielder is not consumed by that very heat. And that requires money.\n\nIt is, of course, a simple enough thing to procure weapons that set things ablaze outright or fabrics that do not catch fire easily. But to obtain a weapon whose heat output can be fine-tuned and controlled at any given moment according to the wielder's every need, or outlier fabrics that ward off heat <i>completely</i>—such exceptional gear costs not only a fortune but also the wielder's constant training to be as exceptional in handling them.\n\nNaturally, if you have invested that much money and time, the returns will come in the form of many more contracts requiring your services.
   PL: Jeżeli postanowiłeś korzystać ze sprzętu warsztatowego wykorzystującego ciepło, musisz być też przygotowany na zapłacenie znacznie wyższej ceny. W przeciwieństwie do zwykłej broni, której parametry — ostrość i wytrzymałość — łatwo ocenić, broń emanująca żarem wymaga mnóstwa przygotowań, by jej użytkownik nie został przez ten żar pochłonięty.\n\nOczywiście broń, która po prostu podpala wrogów, albo tkaniny, które trudno podpalić, łatwo zdobyć. Ale żeby zdobyć broń, która w dowolnej chwili i z dokładnością dostarcza tyle ciepła, ile użytkownik potrzebuje, albo tkaniny całkowicie blokujące ciepło, trzeba zwykle zapłacić grubo — i nie wolno też zaniedbywać treningu, by nauczyć się ich obsługi.\n\nA jeżeli zainwestowałeś tyle pieniędzy i czasu, to proporcjonalnie wzrośnie liczba zleceń, którymi będą cię szarpać.
710. [Pasywka bojowa (od ulepszenia 1) — nazwa] 선배
   źródło: Passives.json :: dataList[id=1021603].name
   limit: do 40 znaków
   EN: Seonbae
   PL: Seonbae
711. [Pasywka bojowa (od ulepszenia 1) — opis] 새벽 사무소[TabExplain] 해결사 싱클레어가 전장에 있으면, 다음 효과 발동\n- 새벽 사무소[TabExplain] 해결사 싱클레어가 [DawnFaust] 얻음\n- 새벽 사무소[TabExplain] 해결사 파우스트가 사망한 상태면, 턴 시작 시 새벽 사무소[TabExplain] 해결사 싱클레어가 보유한 [DawnFaust]가 [DawnFaustDying]로 변경됨
   źródło: Passives.json :: dataList[id=1021603].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [DawnFaust], [DawnFaustDying]
   znaczenie tagów: [DawnFaust] = 정오 / High Noon; [DawnFaustDying] = 고독한 정오 / Loneliness at High Noon
   EN: If Dawn Office[TabExplain] Fixer Sinclair is on the field, activate the following effects:\n- Dawn Office[TabExplain] Fixer Sinclair gains [DawnFaust]\n- Turn Start: If Dawn Office[TabExplain] Fixer Faust is defeated, convert [DawnFaust] on Dawn Office[TabExplain] Fixer Sinclair into [DawnFaustDying]
   PL: Jeżeli na polu jest Fikser Biura Świtu[TabExplain] Sinclair, uruchamia następujące efekty:\n- Fikser Biura Świtu[TabExplain] Sinclair zyskuje [DawnFaust]\n- Na początku tury: jeżeli Fikserka Biura Świtu[TabExplain] Faust jest pokonana, [DawnFaust] Fiksera Biura Świtu[TabExplain] Sinclaira zmienia się w [DawnFaustDying]
712. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — nazwa] 포이어팔터[스티그마 공방]
   źródło: Passives.json :: dataList[id=1021601].name
   limit: do 50 znaków
   EN: Feuerfalter [Stigma Workshop]
   PL: Feuerfalter [Pracownia Stigmy]
713. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — opis] 자신 이외의 새벽 사무소[TabExplain] 소속 인격이 다음 조건 만족 시,\n새벽 사무소[TabExplain] 해결사 파우스트가 ‘연계’ 사용 (인격별 턴당 1회)\n- 기본 스킬 공격 종료 시 적중한 적이 흐트러졌을 때, 대상에게 사용\n(해당 스킬 공격 시작 전 이미 흐트러짐 상태였으면 발동하지 않음)\n- 새벽 사무소[TabExplain] 대표 그레고르의 ‘새벽을 가르는 검’, ‘새벽녘’ 또는\n새벽 사무소[TabExplain] 해결사 싱클레어의 ‘낙인’, ‘타오르는 일격’ 공격 종료 시, 적중한 적에게 사용 (흐트러진 대상 우선)\n\n새벽 사무소[TabExplain] 해결사 싱클레어가 전장에 있으면,\n새벽 사무소[TabExplain] 해결사 파우스트가 사용하는 기본 스킬의 재사용 코인 적중 시\n대상 적의 [Combustion] 위력만큼 분노 피해를 추가로 입힘 (최대 10, 턴당 최대 20)\n- [Combustion]이 발동한 것으로 취급
   źródło: Passives.json :: dataList[id=1021601].desc
   limit: do 1220 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When other Dawn Office[TabExplain] Identities meet the following conditions, Dawn Office[TabExplain] Fixer Faust uses the "Seconded Offensive" Skill against the targeted enemy (once per turn per Identity)\n- At Base Skill Attack End: If the enemy that was hit is Staggered, use "Seconded Offensive" against said enemy\n(Does not activate if the said enemy was already Staggered Before Attack of the said Skill)\n- At Attack End of the following Skills, use "Seconded Offensive" on the enemy they hit (prioritizes Staggered targets):\n  · Dawn Office[TabExplain] Rep Gregor's "Dawnsplitter" and "Crack of Dawn"\n  · Dawn Office[TabExplain] Fixer Sinclair's "Stigmatize" and "Blazing[TabExplain] Strike"\n\nIf Dawn Office[TabExplain] Fixer Sinclair is on the field: On Hit using Reused Coins of Dawn Office[TabExplain] Fixer Faust's Base Skills, deal additional Wrath damage equal to [Combustion] on targeted enemy (max 10; max 20 per turn)\n- Counts as activating [Combustion]
   PL: Jeżeli inne Tożsamości Biura Świtu[TabExplain] spełnią poniższe warunki, Fikserka Biura Świtu[TabExplain] Faust używa Umiejętności „Łączenie” na namierzonym wrogu (1 raz na turę na Tożsamość)\n- Na koniec ataku podstawowej Umiejętności: jeżeli trafiony wróg został Ogłuszony, używa „Łączenia” na tym wrogu\n(Nie uruchamia się, jeżeli wróg był już Ogłuszony przed atakiem tej Umiejętności)\n- Na koniec ataku Umiejętności „Ostrze Rozcinające Świt” i „Biały Świt” Szefa Biura Świtu[TabExplain] Gregora albo Umiejętności „Napiętnowanie” i „Płonące Uderzenie” Fiksera Biura Świtu[TabExplain] Sinclaira używa „Łączenia” na trafionym wrogu (najpierw Ogłuszeni)\n\nJeżeli na polu jest Fikser Biura Świtu[TabExplain] Sinclair, gdy ponownie użyte monety podstawowych Umiejętności Fikserki Biura Świtu[TabExplain] Faust trafią, zadaje dodatkowe obrażenia Gniewu równe Mocy [Combustion] namierzonego wroga (maks. 10, maks. 20 na turę)\n- Liczy się jako uruchomienie [Combustion]
714. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — podsumowanie] 추가 공격 발동\n재사용 코인 적중 시 화상 위력에 비례하여 분노 피해 입힘
   źródło: Passives.json :: dataList[id=1021601].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Activate additional attack\nOn Hit using Reused Coins, deal Wrath damage based on Burn Potency
   PL: Uruchamia dodatkowy atak\nPrzy trafieniu ponownie użytych monet zadaje obrażenia Gniewu proporcjonalnie do Mocy Podpalenia
715. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — tekst klimatyczny] 캐리어 또는 악기 케이스와 같이 생긴 이 무기를 쓰는 이유는 명확하다. 첫 번째는 일상에 녹아들기 위함이다. 전투에서 활용하기 어렵고 복잡한 유형의 무기는 오히려 그 비효율성 때문에 무기로 인식되지 않을 확률이 높다.\n두 번째는 캐리어의 모양, 그 자체로 인해 생기는 수납력이다. 그렇기에 무언가를 담는 형태의 무기는 제뱌찌 협회에서 적극적으로 사용한다.\n\n다만, 이러한 장점과 별개로 공방 장비를 쓰는 이들 사이에서 평가는 좋지 않다. 이 무기를 다루기 위해 투자한 시간을 다른 무기에 쏟았다면, 더 강해졌을 것이라거나, 겉멋이나 든 요즘 해결사들이 쓰는 장비라는 말을 종종 들을 수 있다.\n\n이러한 까다로운 장비를 들고 있는 사람을 만났을 때, 그 사람이 고등급 해결사, 혹은 직책 높은 조직원이라는 것은… 역설적이게도 다른 의미를 가진다. 그렇기에 공방에서 이 장비의 명칭은 캐리어가 아닌 관, 코핀으로 불리고 있다. 그리고 관에는 으레 나비가 따라붙는다.
   źródło: Passives.json :: dataList[id=1021601].flavor
   limit: do 1730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The appeal of a weapon shaped like a suitcase or a musical instrument case is clear enough.\n\nFirst, the user may blend into the cover of daily life without raising alarm. Though arms of this sort are unwieldy and complicated to make use of in battle, that perceived shortcoming makes them less likely to be recognized as tools of killing.\n\nSecondly, weapons fashioned into the form of a case afford storage capacity. Container-shaped arms, for example, are actively used by the Fixers of the Devyat' Association.\n\nSuch convenience, however, does not automatically win favors from those who elect Workshop gear as their weapon of choice. The common opinion is that anyone who invests so much time in mastering this sort of weaponry would be better served by training with something else—in fact, the user would often hear snide remarks from other combatants, ranging from "Fixers these days" to "showy and pretentious."\n\nBut should one let this reputation for impracticality drop one's guard when facing an opponent armed with such a finicky piece of equipment, especially if they happen to be a high-ranking Fixer or a Syndicate officer, one will find that the laughable "containers" or "cases" carry quite a different weight—a weight grave enough for any Workshop worth its name to call them "coffins." And coffins, as a matter of fact, have a way of inviting butterflies.
   PL: Zasadą tej broni, wyglądającej jak walizka albo futerał na instrument, jest oczywista. Po pierwsze: pozwala wtapiać się w codzienność. Broń trudna do wykorzystania w boju i skomplikowana w obsłudze jest z reguły w ogóle niepostrzegana jako broń — właśnie przez swoją niepraktyczność.\nPo drugie: sam kształt walizki zapewnia pojemność przenośni. Dlatego broń o formie pojemnika aktywnie używają Fikserzy Stowarzyszenia Diewiat'.\n\nTe zalety nie zmieniają jednak faktu, że opinia o niej wśród użytkowników sprzętu warsztatowego jest zła. Często można usłyszeć, że gdyby czas poświęcony na opanowanie tej broni poświęcono na inną, ktoś byłby silniejszy; albo że to sprzęt dla współczesnych fikserów, którzy chcą tylko błyszczeć.\n\nKiedy spotkasz kogoś uzbrojonego w tak wybredny sprzęt, a jest nim wysokiej rangi fikser albo wysoko postawiony członek organizacji… paradoksalnie znaczy to co innego. Dlatego w warsztatach nazywa się tę broń nie walizką, lecz trumną. A trumnom zawsze towarzyszą motyle.
716. [Pasywka bojowa (od ulepszenia 3, posiadane 3× Wrath) — nazwa] 포이어팔터[스티그마 공방]
   źródło: Passives.json :: dataList[id=1021611].name
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Pasywka bojowa (od ulepszenia 3, posiadane 3× Wrath) — opis] <style="highlight">자신에게 [Firstlight]이 있을 때 전투 시작 시 (수치 x 3)만큼 [StigmaWorkshopCelloCaseOne] 얻음</style>\n\n자신 이외의 새벽 사무소[TabExplain] 소속 인격이 다음 조건 만족 시,\n새벽 사무소[TabExplain] 해결사 파우스트가 ‘연계’ 사용 (인격별 턴당 1회)\n- 기본 스킬 공격 종료 시 적중한 적이 흐트러졌을 때, 대상에게 사용\n(해당 스킬 공격 시작 전 이미 흐트러짐 상태였으면 발동하지 않음)\n- 새벽 사무소[TabExplain] 대표 그레고르의 ‘새벽을 가르는 검’, ‘새벽녘’ 또는\n새벽 사무소[TabExplain] 해결사 싱클레어의 ‘낙인’, ‘타오르는 일격’ 공격 종료 시, 적중한 적에게 사용 (흐트러진 대상 우선)\n\n새벽 사무소[TabExplain] 해결사 싱클레어가 전장에 있으면,\n새벽 사무소[TabExplain] 해결사 파우스트가 사용하는 기본 스킬의 재사용 코인 적중 시\n대상 적의 [Combustion] 위력만큼 분노 피해를 추가로 입힘 (최대 10, 턴당 최대 20)\n- [Combustion]이 발동한 것으로 취급
   źródło: Passives.json :: dataList[id=1021611].desc
   limit: do 1340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Firstlight], [StigmaWorkshopCelloCaseOne], [TabExplain], [Combustion]
   znaczenie tagów: [Firstlight] = 전투 감각 / Battle Instinct; [StigmaWorkshopCelloCaseOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [Combustion] = 화상 / Burn
   EN: <style="highlight">Combat Start: When this unit has [Firstlight], gain (Stack x 3) [StigmaWorkshopCelloCaseOne]</style>\n\nWhen other Dawn Office[TabExplain] Identities meet the following conditions, Dawn Office[TabExplain] Fixer Faust uses the "Seconded Offensive" Skill against the targeted enemy (once per turn per Identity)\n- At Base Skill Attack End: If the enemy that was hit is Staggered, use "Seconded Offensive" against said enemy\n(Does not activate if the said enemy was already Staggered Before Attack of the said Skill)\n- At Attack End of the following Skills, use "Seconded Offensive" on the enemy they hit (prioritizes Staggered targets):\n  · Dawn Office[TabExplain] Rep Gregor's "Dawnsplitter" and "Crack of Dawn"\n  · Dawn Office[TabExplain] Fixer Sinclair's "Stigmatize" and "Blazing[TabExplain] Strike"\n\nIf Dawn Office[TabExplain] Fixer Sinclair is on the field: On Hit using Reused Coins of Dawn Office[TabExplain] Fixer Faust's Base Skills, deal additional Wrath damage equal to [Combustion] on the targeted enemy (max 10; max 20 per turn)\n- Counts as activating [Combustion]
   PL: <style="highlight">Na początku walki, gdy ta jednostka ma [Firstlight], zyskuje (stos x 3) [StigmaWorkshopCelloCaseOne]</style>\n\nJeżeli inne Tożsamości Biura Świtu[TabExplain] spełnią poniższe warunki, Fikserka Biura Świtu[TabExplain] Faust używa Umiejętności „Łączenie” na namierzonym wrogu (1 raz na turę na Tożsamość)\n- Na koniec ataku podstawowej Umiejętności: jeżeli trafiony wróg został Ogłuszony, używa „Łączenia” na tym wrogu\n(Nie uruchamia się, jeżeli wróg był już Ogłuszony przed atakiem tej Umiejętności)\n- Na koniec ataku Umiejętności „Ostrze Rozcinające Świt” i „Biały Świt” Szefa Biura Świtu[TabExplain] Gregora albo Umiejętności „Napiętnowanie” i „Płonące Uderzenie” Fiksera Biura Świtu[TabExplain] Sinclaira używa „Łączenia” na trafionym wrogu (najpierw Ogłuszeni)\n\nJeżeli na polu jest Fikser Biura Świtu[TabExplain] Sinclair, gdy ponownie użyte monety podstawowych Umiejętności Fikserki Biura Świtu[TabExplain] Faust trafią, zadaje dodatkowe obrażenia Gniewu równe Mocy [Combustion] namierzonego wroga (maks. 10, maks. 20 na turę)\n- Liczy się jako uruchomienie [Combustion]
718. [Pasywka bojowa (od ulepszenia 3, posiadane 3× Wrath) — podsumowanie] 전투 감각이 있으면, 불꽃나비의 관 얻음\n추가 공격 발동\n재사용 코인 적중 시 화상 위력에 비례하여 분노 피해 입힘
   źródło: Passives.json :: dataList[id=1021611].summary
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit has Battle Instinct, gain Fire Butterfly Coffin\nActivate additional attack\nOn Hit using Reused Coins, deal Wrath damage based on Burn Potency
   PL: Jeżeli ma Wyczucie Walki, zyskuje Trumnę Ognistego Motyla\nUruchamia dodatkowy atak\nPrzy trafieniu ponownie użytych monet zadaje obrażenia Gniewu proporcjonalnie do Mocy Podpalenia
719. [Pasywka bojowa (od ulepszenia 3, posiadane 3× Wrath) — tekst klimatyczny] 캐리어 또는 악기 케이스와 같이 생긴 이 무기를 쓰는 이유는 명확하다. 첫 번째는 일상에 녹아들기 위함이다. 전투에서 활용하기 어렵고 복잡한 유형의 무기는 오히려 그 비효율성 때문에 무기로 인식되지 않을 확률이 높다.\n두 번째는 캐리어의 모양, 그 자체로 인해 생기는 수납력이다. 그렇기에 무언가를 담는 형태의 무기는 제뱌찌 협회에서 적극적으로 사용한다.\n\n다만, 이러한 장점과 별개로 공방 장비를 쓰는 이들 사이에서 평가는 좋지 않다. 이 무기를 다루기 위해 투자한 시간을 다른 무기에 쏟았다면, 더 강해졌을 것이라거나, 겉멋이나 든 요즘 해결사들이 쓰는 장비라는 말을 종종 들을 수 있다.\n\n이러한 까다로운 장비를 들고 있는 사람을 만났을 때, 그 사람이 고등급 해결사, 혹은 직책 높은 조직원이라는 것은… 역설적이게도 다른 의미를 가진다. 그렇기에 공방에서 이 장비의 명칭은 캐리어가 아닌 관, 코핀으로 불리고 있다. 그리고 관에는 으레 나비가 따라붙는다.
   źródło: Passives.json :: dataList[id=1021611].flavor
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath, posiadane 3× Lust) — nazwa] 고독한 해결사
   źródło: Passives.json :: dataList[id=1021621].name
   limit: do 40 znaków
   EN: The Lone Fixer
   PL: Samotny Fixer
721. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath, posiadane 3× Lust) — opis] 전투 시작 시 생존한 인격이 대기 인원을 전부 포함하여 1명이면,\n해당 인격이 [AttackUp] 3, [DefenseUp] 3 얻음
   źródło: Passives.json :: dataList[id=1021621].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: If there is only 1 surviving Identity, including Backup units, the said Identity gains 3 [AttackUp] and 3 [DefenseUp]
   PL: Na początku walki, jeżeli na polu jest tylko 1 Tożsamość — łącznie z rezerwą —\nta Tożsamość zyskuje 3 [AttackUp] i 3 [DefenseUp]
722. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath, posiadane 3× Lust) — podsumowanie] 공격 레벨 증가 3, 방어 레벨 증가 3 얻음
   źródło: Passives.json :: dataList[id=1021621].summary
   limit: do 120 znaków
   EN: Gain 3 Offense Level Up and 3 Defense Level Up
   PL: Zyskuje 3 Wzrosty Poziomu Ataku i 3 Wzrosty Poziomu Obrony

## [?] Early Elephants Class Captain — Faust — 코끼리반 반장
- ID Tożsamości: `400026` (plik: `Personalities-x1p1c1.json`)

723. [Karta Tożsamości — tytuł] 코끼리반 반장
   źródło: Personalities-x1p1c1.json :: dataList[id=400026].title
   limit: do 50 znaków
   EN: Early Elephants Class Captain
   PL: Kapitan Grupy Słoników
724. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities-x1p1c1.json :: dataList[id=400026].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities-x1p1c1.json :: dataList[id=400026].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Karta Tożsamości — opis] 파우스트의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400026].desc
   limit: do 120 znaków
   EN: Faust's ??? Identity
   PL: Tożsamość ??? Faust
727. [Pasywka bojowa [40002601] — nazwa] 뿐석
   źródło: Passives-x1p1c1.json :: dataList[id=40002601].name
   limit: do 40 znaków
   EN: Anawytic Ewe
   PL: Anawytic Ewe
728. [Pasywka bojowa [40002601] — opis] 부정적인 효과가 걸려있는 대상에게 가하는 피해량 +10%
   źródło: Passives-x1p1c1.json :: dataList[id=40002601].desc
   limit: do 120 znaków
   EN: Deal +10% damage to units with negative status effects.
   PL: Zadaje +10% obrażeń celom z negatywnymi efektami
729. [Pasywka bojowa [40002602] — nazwa] 관짤
   źródło: Passives-x1p1c1.json :: dataList[id=40002602].name
   limit: do 40 znaków
   EN: Keen Obsewashun
   PL: Keen Obsewashun
730. [Pasywka bojowa [40002602] — opis] 최대 체력이 가장 높은 아군 1명 공격 적중 시 25% 확률로 공격 레벨 감소 2 부여
   źródło: Passives-x1p1c1.json :: dataList[id=40002602].desc
   limit: do 120 znaków
   EN: 1 ally with the highest Max HP inflicts 2 Offense Level Down with attacks at a 25% chance.
   PL: 1 Sojusznik z najwyższym Maks. HP: przy trafieniu atakiem z 25% szansą nakłada 2 Spadku Poziomu Ataku
