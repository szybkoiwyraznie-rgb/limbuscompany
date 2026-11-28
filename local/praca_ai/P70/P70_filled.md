# Paczka AI P70 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 6/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P70_3c_przeciwnicy_i_anomalie_cz06.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P70_3c_przeciwnicy_i_anomalie_cz06.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c6p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c6p2
- grupa rozdziału/trybu: `a1c6p2` · plik: `Skills_Abnormality-a1c6p2.json`

1. [Umiejętność wroga [815903] (ulepszenie 1) — opis] [WhenUse] 자신보다 속도가 낮다면, 차이만큼 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815903].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, Clash Power +1 for each Speed difference (max 3)
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +1 za każdy punkt różnicy (maks. 3)
2. [Umiejętność wroga [815903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
3. [Umiejętność wroga [815903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [AttackDown] w następnej turze
4. [Umiejętność wroga [815903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion]
5. [Umiejętność wroga [815904] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815904].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Guard
6. [Umiejętność wroga [815904] (ulepszenie 1) — opis] [WhenUse] [Protection] 3 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [WhenUse] Gain 3 [Protection]
   PL: [WhenUse] zyskuje 3 [Protection]
7. [Umiejętność wroga [816001] (ulepszenie 1) — nazwa] 깨물기
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816001].levelList[level=1].name
   limit: do 40 znaków
   EN: Maul
   PL: Maul
8. [Umiejętność wroga [816001] (ulepszenie 1) — opis] 이 공격 스킬 적중시 다음 턴에 [TakeHpHealIncrease]를 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TakeHpHealIncrease]
   znaczenie tagów: [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: When this Attack Skill hits, gain [TakeHpHealIncrease] next turn
   PL: przy trafieniu tą Umiejętnością ataku zyskuje [TakeHpHealIncrease] w następnej turze
9. [Umiejętność wroga [816001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
10. [Umiejętność wroga [816001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Umiejętność wroga [816002] (ulepszenie 1) — nazwa] 식사 시간
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].name
   limit: do 40 znaków
   EN: Devouring
   PL: Devouring
12. [Umiejętność wroga [816002] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Burst]이 있다면, 기본 위력 +1
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has [Burst], Base Power +1
   PL: [WhenUse] jeżeli cel ma [Burst], Moc Bazowa +1
13. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
14. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 3 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Core and Part both gain 3 HP
   PL: [OnSucceedAttackHead] Korpus i Część zyskują po 3 HP
15. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 3 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 3 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Umiejętność wroga [816002] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 3 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816002].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność wroga [816003] (ulepszenie 1) — nazwa] 탐욕스러운 식사 시간
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].name
   limit: do 40 znaków
   EN: Ravenous Devouring
   PL: Ravenous Devouring
22. [Umiejętność wroga [816003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, [DefenseDown] 2 부여\n자신의 [TakeHpHealIncrease] 수치만큼, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [DefenseDown], [TakeHpHealIncrease]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: [WhenUse] If target has 5+ [Burst], inflict 2 [DefenseDown]\nGain +1 Base Power for every [TakeHpHealIncrease] value on self (max 3)
   PL: [WhenUse] jeżeli cel ma 5+ [Burst], nakłada 2 [DefenseDown]\nMoc Bazowa +1 za każdy [TakeHpHealIncrease] tej jednostki (maks. 3)
23. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 5 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Core and Part both gain 5 HP
   PL: [OnSucceedAttackHead] Korpus i Część zyskują po 5 HP
25. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] nakłada 5 [Burst]
26. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 5 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 5 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Umiejętność wroga [816003] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttackHead] 본체 및 부위 체력 5 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816003].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność wroga [816004] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816004].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL: Counter
32. [Umiejętność wroga [816004] (ulepszenie 1) — opis] 자신의 본체 체력이 50%이하라면, 이 스킬의 코인 적중시 본체 및 부위 체력 10 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816004].levelList[level=1].desc
   limit: do 120 znaków
   EN: At less than 50% Core HP, Core and Part heal on Coin Hit
   PL: jeżeli HP Korpusu jest poniżej 50%, Korpus i Część przywracają HP przy trafieniu Monetą
33. [Umiejętność wroga [816004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 [Burst] i 2 Licznika [Burst]
34. [Umiejętność wroga [816004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Umiejętność wroga [816401] (ulepszenie 1) — nazwa] 배트치기
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816401].levelList[level=1].name
   limit: do 40 znaków
   EN: Bat Bash
   PL: Bat Bash
36. [Umiejętność wroga [816401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Burst]
37. [Umiejętność wroga [816401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [816402] (ulepszenie 1) — nazwa] 내려박기
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816402].levelList[level=1].name
   limit: do 40 znaków
   EN: Smackdown
   PL: Smackdown
39. [Umiejętność wroga [816402] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Enhancement], [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [WinDuel] Gain 1 [Enhancement] and 1 [AttackDmgUp] next turn
   PL: [WinDuel] zyskuje 1 [Enhancement] i 1 [AttackDmgUp] w następnej turze
40. [Umiejętność wroga [816402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Umiejętność wroga [816402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność wroga [816402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
43. [Umiejętność wroga [816402] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 [Laceration] 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816402].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict [Laceration] equal to [Burst] on target
   PL: [OnSucceedAttack] nakłada [Laceration] na cel w wysokości [Burst] celu
44. [Umiejętność wroga [816403] (ulepszenie 1) — nazwa] 분풀기
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816403].levelList[level=1].name
   limit: do 40 znaków
   EN: Upheaval
   PL: Upheaval
45. [Umiejętność wroga [816403] (ulepszenie 1) — opis] 대상의 [Burst]이 5 이상이면, 합 위력 +1\n대상의 [Laceration]이 5 이상이면, 합 위력 +1\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816403].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Laceration], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 5+ [Burst], Clash Power +1\nIf target has 5+ [Laceration], Clash Power +1\n[WinDuel] Inflict +3 [Burst] Count
   PL: jeżeli cel ma 5+ [Burst], Moc Starcia +1\njeżeli cel ma 5+ [Laceration], Moc Starcia +1\n[WinDuel] nakłada 3 Licznika [Burst]
46. [Umiejętność wroga [816403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +1
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Next Coin has +1 Power
   PL: [OnSucceedAttackHead] następna Moneta ma Moc +1
47. [Umiejętność wroga [816403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Next Coin has +2 Power
   PL: [OnSucceedAttackHead] następna Moneta ma Moc +2
48. [Umiejętność wroga [816403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 3 [Paralysis] w następnej turze
49. [Umiejętność wroga [816403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL: [OnSucceedAttack] nakłada 8 [Laceration]
50. [Umiejętność wroga [816404] (ulepszenie 1) — nazwa] 속죄의 시간이다
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816404].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Repent
   PL: Time to Repent
51. [Umiejętność wroga [816404] (ulepszenie 1) — opis] [CantChangeTarget]
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantChangeTarget]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantChangeTarget]
   PL: [CantChangeTarget]
52. [Umiejętność wroga [816404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수  3, [Burst]  횟수 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Laceration] Count and 3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration] i 3 Licznika [Burst]
53. [Umiejętność wroga [816404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3, [Burst] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 3 [Burst]
54. [Umiejętność wroga [816404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3, [Burst] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność wroga [816404] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816404].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Enhancement]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [OnSucceedAttack] Gain 1 [Enhancement] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Enhancement] w następnej turze
56. [Umiejętność wroga [816405] (ulepszenie 1) — nazwa] 더욱 고통스러워야해!
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816405].levelList[level=1].name
   limit: do 40 znaków
   EN: You Must Suffer More!
   PL: You Must Suffer More!
57. [Umiejętność wroga [816405] (ulepszenie 1) — opis] [CantChangeTarget]\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WinDuel], [Burst]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: [CantChangeTarget]\n[WinDuel] Inflict 3 [Burst] Count
   PL: [CantChangeTarget]\n[WinDuel] nakłada 3 Licznika [Burst]
58. [Umiejętność wroga [816405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +1
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [816405] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność wroga [816405] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [816406] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816406].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność wroga [816406] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816406].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Enhancement]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WhenUse] Gain 1 [Enhancement] next turn
   PL: [WhenUse] zyskuje 1 [Enhancement] w następnej turze
63. [Umiejętność wroga [816407] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816407].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [816407] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816407].levelList[level=1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność wroga [816407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [816501] (ulepszenie 1) — nazwa] 치워주마
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816501].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Remove You
   PL: I'll Remove You
67. [Umiejętność wroga [816501] (ulepszenie 1) — opis] 이 공격 스킬이 입힌 피해량의 10%만큼 본체 및 부위 체력 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816501].levelList[level=1].desc
   limit: do 120 znaków
   EN: Core and Part heal by 10% of the damage dealt by this Attack Skill
   PL: Korpus i Część przywracają HP równe 10% obrażeń zadanych przez tę Umiejętność ataku
68. [Umiejętność wroga [816501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] Gain 1 [AttackUp]
   PL: [OnSucceedAttack] zyskuje 1 [AttackUp]
69. [Umiejętność wroga [816501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [816501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 1 [Agility] next turn
   PL: [OnSucceedAttackHead] zyskuje 1 [Agility] w następnej turze
71. [Umiejętność wroga [816502] (ulepszenie 1) — nazwa] 빌어먹을 놈
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816502].levelList[level=1].name
   limit: do 40 znaków
   EN: Bloody Bastard!
   PL: Bloody Bastard!
72. [Umiejętność wroga [816502] (ulepszenie 1) — opis] 대상보다 속도가 빠르다면, 합 위력+2
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816502].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's Clash Power +2
   PL: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +2
73. [Umiejętność wroga [816502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 4 [Laceration] i 2 Licznika [Laceration]
74. [Umiejętność wroga [816502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność wroga [816502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상보다 속도가 3이상 빠르다면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit's Speed is faster than the target's by 3 or more, reuse this Coin (once)
   PL: [OnSucceedAttack] jeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, używa Monety ponownie (maks. 1 raz)
76. [Umiejętność wroga [816503] (ulepszenie 1) — nazwa] 내 집이다!
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].name
   limit: do 40 znaków
   EN: This Is My Home!
   PL: This Is My Home!
77. [Umiejętność wroga [816503] (ulepszenie 1) — opis] 체력이 가장 낮은 대상 우선 공격\n[WhenUse] 대상의 현재 체력 비율이 70% 미만이면, 합 위력 +2
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Prioritize targets with the least HP\n[WhenUse] If target has less than 70% HP, Clash Power +2
   PL: priorytet: cele o najniższym HP\n[WhenUse] jeżeli aktualne HP celu wynosi mniej niż 70%, Moc Starcia +2
78. [Umiejętność wroga [816503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Agility] w następnej turze
79. [Umiejętność wroga [816503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable]
80. [Umiejętność wroga [816503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 2 Licznika [Laceration]
81. [Umiejętność wroga [816503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność wroga [816503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 20이상이면, 피해량 +100%
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 20+ [Laceration], deal +100% damage
   PL: [OnSucceedAttack] jeżeli cel ma 20+ [Laceration], zadaje +100% obrażeń
83. [Umiejętność wroga [816503] (ulepszenie 1) — moneta 4, efekt 2 — opis] [EnemyKill] 이 스킬 재사용 (최대 1)
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816503].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Reuse this Skill (1 time max)
   PL: [EnemyKill] używa ponownie tę Umiejętność (1 raz)
84. [Umiejętność wroga [816504] (ulepszenie 1) — nazwa] 네놈만은…
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816504].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Get You...!
   PL: I'll Get You...!
85. [Umiejętność wroga [816504] (ulepszenie 1) — opis] 히스클리프 우선 공격\n[WhenUse] 속도가 가장 낮은 적일 경우, 기본 위력 +3\n[WhenUse] 다음 턴에 [AaCfPbBe], [Vulnerable] 2, [Paralysis] 3, [Binding] 5 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816504].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AaCfPbBe], [Vulnerable], [Paralysis], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AaCfPbBe] = 사냥감 표시 / Marked Prey; [Vulnerable] = 취약 / Fragile; [Paralysis] = 마비 / Paralyze; [Binding] = 속박 / Bind
   EN: Prioritizes Heathcliff\n[WhenUse] If the target is the enemy with the slowest Speed, Base Power +3\n[WhenUse] Inflict [AaCfPbBe], 2 [Vulnerable], 3 [Paralysis], and 5 [Binding] next turn
   PL: priorytet: Heathcliff\n[WhenUse] jeżeli cel jest wrogiem o najniższej Szybkości, Moc Bazowa +3\n[WhenUse] nakłada [AaCfPbBe], 2 [Vulnerable], 3 [Paralysis] i 5 [Binding] w następnej turze
86. [Umiejętność wroga [816504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] Gain 1 [AttackUp] next turn
   PL: [OnSucceedAttack] zyskuje 1 [AttackUp] w następnej turze
87. [Umiejętność wroga [816504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [816505] (ulepszenie 1) — nazwa] 돌려줘…!!
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].name
   limit: do 40 znaków
   EN: Give It Back...!!
   PL: Give It Back...!!
89. [Umiejętność wroga [816505] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]
   PL: [CantDuel]
90. [Umiejętność wroga [816505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 2 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttackHead] Gain 2 [AttackUp] next turn
   PL: [OnSucceedAttackHead] zyskuje 2 [AttackUp] w następnej turze
91. [Umiejętność wroga [816505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 2 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność wroga [816505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 2 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Umiejętność wroga [816505] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], deal 30% of damage dealt as Blunt damage
   PL: [OnSucceedAttack] jeżeli cel ma 10+ [Laceration], zadaje dodatkowe obrażenia Uderzeniem równe 30% zadanych obrażeń
94. [Umiejętność wroga [816505] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5이상이면, 피해량의 50%만큼 체력 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816505].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 5+ [Laceration], heal by 50% of damage dealt
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], przywraca HP równe 50% zadanych obrażeń
95. [Umiejętność wroga [816506] (ulepszenie 1) — nazwa] 이 새끼가…
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816506].levelList[level=1].name
   limit: do 40 znaków
   EN: You Little...
   PL: You Little...
96. [Umiejętność wroga [816506] (ulepszenie 1) — opis] [AaCfPbBe]을 가지고 있는 대상 우선 공격\n대상의 속도가 자신보다 3 이상 낮다면, 이 스킬 재사용 (최대 1)
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816506].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPbBe]
   znaczenie tagów: [AaCfPbBe] = 사냥감 표시 / Marked Prey
   EN: Prioritizes targets with [AaCfPbBe]\nIf this unit's Speed is faster than the target's by 3 or more, reuse this Skill (1 time max)
   PL: priorytet: cele z [AaCfPbBe]\njeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, używa ponownie tę Umiejętność (1 raz)
97. [Umiejętność wroga [816506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 본체 및 부위 체력 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal Core and Part by 50% of damage dealt
   PL: [OnSucceedAttack] przywraca Korpusowi i Części HP równe 50% zadanych obrażeń
98. [Umiejętność wroga [816506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 본체 및 부위 체력 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Umiejętność wroga [816507] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816507].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność wroga [816507] (ulepszenie 1) — opis] 턴 종료시 보호막 체력이 남아있다면, 다음 턴에 [Protection] 4 얻음
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816507].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: If this Unit has remaining Shield HP at Turn End, gain 4 [Protection] next turn
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, zyskuje 4 [Protection] w następnej turze
101. [Umiejętność wroga [816508] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816508].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Evade
102. [Umiejętność wroga [816508] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Binding] 1 부여 (최대 2)
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816508].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Binding]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Binding] = 속박 / Bind
   EN: [OnSucceedEvade] Inflict 1 [Binding] next turn (2 times max)
   PL: [OnSucceedEvade] nakłada 1 [Binding] w następnej turze (do 2 razy)
103. [Umiejętność wroga [816509] (ulepszenie 1) — nazwa] 여긴 내자리야!
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].name
   limit: do 40 znaków
   EN: This is My Place!
   PL: This is My Place!
104. [Umiejętność wroga [816509] (ulepszenie 1) — opis] 자신의 속도가 대상보다 높으면 코인 위력 +1
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's, Coin Power +1
   PL: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Monety +1
105. [Umiejętność wroga [816509] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [816509] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Umiejętność wroga [816509] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Umiejętność wroga [816509] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Umiejętność wroga [816509] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 70%만큼 체력 회복
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=816509].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], heal by 70% of damage dealt
   PL: [OnSucceedAttack] jeżeli cel ma 10+ [Laceration], przywraca HP równe 70% zadanych obrażeń

## [a1c6p2] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c6p2
- grupa rozdziału/trybu: `a1c6p2` · plik: `Skills_Enemy-a1c6p2.json`

110. [Umiejętność wroga [9012801] (ulepszenie 1) — nazwa] 위반자 저지
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012801].levelList[level=1].name
   limit: do 40 znaków
   EN: Deter Rulebreakers
   PL: Deter Rulebreakers
111. [Umiejętność wroga [9012801] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Laceration]이 있다면, 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has [Laceration], heal 4 SP
   PL: [WhenUse] jeżeli cel ma [Laceration], przywraca 4 SP
112. [Umiejętność wroga [9012801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Umiejętność wroga [9012801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność wroga [9012802] (ulepszenie 1) — nazwa] 규약 집행
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012802].levelList[level=1].name
   limit: do 40 znaków
   EN: Rule Execution
   PL: Rule Execution
115. [Umiejętność wroga [9012802] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1
116. [Umiejętność wroga [9012802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
117. [Umiejętność wroga [9012802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], heal 5 SP
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], przywraca 5 SP
118. [Umiejętność wroga [9012802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność wroga [9012802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [9012803] (ulepszenie 1) — nazwa] 위반자 집행
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012803].levelList[level=1].name
   limit: do 40 znaków
   EN: Execute Rulebreakers
   PL: Execute Rulebreakers
121. [Umiejętność wroga [9012803] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Laceration]이 있다면, 다음 턴에 [Enhancement]를 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Laceration], [Enhancement]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WinDuel] If target has [Laceration], gain 1 [Enhancement] next turn
   PL: [WinDuel] jeżeli cel ma [Laceration], zyskuje 1 [Enhancement] w następnej turze
122. [Umiejętność wroga [9012803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 5+ [Laceration], deal 20% of damage dealt as bonus damage
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], zadaje dodatkowe obrażenia równe 20% zadanych obrażeń
123. [Umiejętność wroga [9012803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [DefenseDown]
   PL: [OnSucceedAttackHead] nakłada 1 [DefenseDown]
124. [Umiejętność wroga [9012803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [9012803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [9012804] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012804].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Umiejętność wroga [9012804] (ulepszenie 1) — opis] 턴 종료 시 보호막 체력이 남아있다면, 다음 턴에 [AttackDmgUp] 2 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: If this unit has remaining Shield HP at Turn End, gain 2 [AttackDmgUp] next turn
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, zyskuje 2 [AttackDmgUp] w następnej turze
128. [Umiejętność wroga [9012901] (ulepszenie 1) — nazwa] 위반자 처리
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012901].levelList[level=1].name
   limit: do 40 znaków
   EN: Dispose Rulebreakers
   PL: Dispose Rulebreakers
129. [Umiejętność wroga [9012901] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Laceration]이 있다면, 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012901].levelList[level=1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [9012901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
131. [Umiejętność wroga [9012901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [9012902] (ulepszenie 1) — nazwa] 규약 이행
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012902].levelList[level=1].name
   limit: do 40 znaków
   EN: Rule Fulfillment
   PL: Rule Fulfillment
133. [Umiejętność wroga [9012902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 횟수가 4 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration] Count, Coin Power +1
   PL: [WhenUse] jeżeli cel ma 4+ Licznika [Laceration], Moc Monety +1
134. [Umiejętność wroga [9012902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [9012902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [9012902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [9012902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [9012903] (ulepszenie 1) — nazwa] 위반자 처벌
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012903].levelList[level=1].name
   limit: do 40 znaków
   EN: Punish Rulebreakers
   PL: Punish Rulebreakers
139. [Umiejętność wroga [9012903] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Laceration]이 있다면, 다음 턴에 [Enhancement]를 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012903].levelList[level=1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [9012903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 4 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 4+ [Laceration] Count, deal 20% of damage dealt as bonus damage
   PL: [OnSucceedAttack] jeżeli cel ma 4+ Licznika [Laceration], zadaje dodatkowe obrażenia równe 20% zadanych obrażeń
141. [Umiejętność wroga [9012903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Umiejętność wroga [9012903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 4 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [9012903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność wroga [9012904] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012904].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [9012904] (ulepszenie 1) — opis] 턴 종료 시 보호막 체력이 남아있다면, 다음 턴에 [AttackDmgUp] 2 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9012904].levelList[level=1].desc
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [9013001] (ulepszenie 1) — nazwa] 처단 집행
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013001].levelList[level=1].name
   limit: do 40 znaków
   EN: Punishment Execution
   PL: Punishment Execution
147. [Umiejętność wroga [9013001] (ulepszenie 1) — opis] [WinDuel] 대상의 [Laceration]이 5 이상이면, 이 스킬 재사용 (최대 1)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Laceration]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuel] If target has 5+ [Laceration], reuse this Skill (once)
   PL: [WinDuel] jeżeli cel ma 5+ [Laceration], używa ponownie tę Umiejętność (1 raz)
148. [Umiejętność wroga [9013001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [9013002] (ulepszenie 1) — nazwa] 위반자 처단
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013002].levelList[level=1].name
   limit: do 40 znaków
   EN: Discipline Rulebreakers
   PL: Discipline Rulebreakers
150. [Umiejętność wroga [9013002] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 피해량 +30%
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], deal +30% damage
   PL: jeżeli cel ma 5+ [Laceration], zadaje +30% obrażeń
151. [Umiejętność wroga [9013002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has [Laceration], Inflict 2 [AttackDown] next turn
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], nakłada 2 [AttackDown] w następnej turze
152. [Umiejętność wroga [9013002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Umiejętność wroga [9013002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] (대상의 [Laceration] / 2)만큼 [Burst] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict [Burst] equal to ([Laceration]/2) on target
   PL: [OnSucceedAttack] nakłada [Burst] na cel w wysokości ([Laceration]/2)
154. [Umiejętność wroga [9013002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 7 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], heal 7 SP
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], przywraca 7 SP
155. [Umiejętność wroga [9013003] (ulepszenie 1) — nazwa] 위반 사항
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].name
   limit: do 40 znaków
   EN: Violated Clause
   PL: Violated Clause
156. [Umiejętność wroga [9013003] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 코인 위력 +1 (최대 3)\n[WinDuel] 대상의 [Laceration]이 6 이상이면, 피해량 +40%
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WinDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Coin Power +1 for every 3 [Laceration] on target (max 3)\n[WinDuel] If target has 6+ [Laceration], deal +40% damage
   PL: Moc Monety +1 za każde 3 [Laceration] celu (maks. 3)\n[WinDuel] jeżeli cel ma 6+ [Laceration], zadaje +40% obrażeń
157. [Umiejętność wroga [9013003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność wroga [9013003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność wroga [9013003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 [Burst] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict [Burst] equal to [Laceration] on target
   PL: [OnSucceedAttack] nakłada [Burst] na cel w wysokości [Laceration] celu
160. [Umiejętność wroga [9013003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 10 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], heal 10 SP
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], przywraca 10 SP
161. [Umiejętność wroga [9013003] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] 대상의 [Laceration]이 5 이상이면, 이 스킬 재사용 (최대 1)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013003].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] If target has 5+ [Laceration], reuse this Skill (once)
   PL: [OnSucceedAttackHead] jeżeli cel ma 5+ [Laceration], używa ponownie tę Umiejętność (1 raz)
162. [Umiejętność wroga [9013004] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013004].levelList[level=1].name
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Umiejętność wroga [9013004] (ulepszenie 1) — opis] [OnSucceedEvade] [Enhancement] 1 얻음 (최대 1)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Enhancement]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [OnSucceedEvade] Gain [Enhancement] (max 1)
   PL: [OnSucceedEvade] zyskuje 1 [Enhancement] (maks. 1)
164. [Umiejętność wroga [9013101] (ulepszenie 1) — nazwa] 스케치
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013101].levelList[level=1].name
   limit: do 40 znaków
   EN: Sketch
   PL: Sketch
165. [Umiejętność wroga [9013101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność wroga [9013101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [9013101] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [9013102] (ulepszenie 1) — nazwa] 붓 긋기
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].name
   limit: do 40 znaków
   EN: Brushstroke
   PL: Brushstroke
169. [Umiejętność wroga [9013102] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 기본 위력 +2
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], Base Power +2
   PL: jeżeli cel ma 5+ [Laceration], Moc Bazowa +2
170. [Umiejętność wroga [9013102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność wroga [9013102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [9013102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [9013102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność wroga [9013102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 [Burst] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Umiejętność wroga [9013103] (ulepszenie 1) — nazwa] 혈묘화
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].name
   limit: do 40 znaków
   EN: Sanguine Dots
   PL: Sanguine Dots
176. [Umiejętność wroga [9013103] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Laceration]이 있다면, 다음 턴에 [Enhancement]를 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [9013103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [9013103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [9013103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [9013103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [9013103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 5+ [Laceration], reuse this Skill (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], używa tej Monety ponownie (maks. 1 raz)
182. [Umiejętność wroga [9013103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttackHead] nakłada 2 [DefenseDown]
183. [Umiejętność wroga [9013104] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013104].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [9013104] (ulepszenie 1) — opis] 턴 종료 시 보호막 체력이 남아있다면, 다음 턴에 [AttackDmgUp] 3 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: If this unit has remaining Shield HP at Turn End, gain 3 [AttackDmgUp] next turn
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, zyskuje 3 [AttackDmgUp] w następnej turze
185. [Umiejętność wroga [9013201] (ulepszenie 1) — nazwa] 선화
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013201].levelList[level=1].name
   limit: do 40 znaków
   EN: Line Art
   PL: Line Art
186. [Umiejętność wroga [9013201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [9013201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [9013201] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013201].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Umiejętność wroga [9013202] (ulepszenie 1) — nazwa] 선 긋기
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].name
   limit: do 40 znaków
   EN: Stroke
   PL: Stroke
190. [Umiejętność wroga [9013202] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 기본 위력 +2
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [9013202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [9013202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [9013202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [9013202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 정신력 5 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [9013202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 [Burst] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [9013203] (ulepszenie 1) — nazwa] 혈점화
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].name
   limit: do 40 znaków
   EN: Sanguine Points
   PL: Sanguine Points
197. [Umiejętność wroga [9013203] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Laceration]이 있다면, 다음 턴에 [Enhancement]를 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [9013203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 4 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [9013203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [9013203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 4 이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [9013203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność wroga [9013203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 4 이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 4+ [Laceration] Count, reuse this Skill (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 4+ Licznika [Laceration], używa tej Monety ponownie (maks. 1 raz)
203. [Umiejętność wroga [9013203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [9013204] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013204].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Umiejętność wroga [9013204] (ulepszenie 1) — opis] 턴 종료 시 보호막 체력이 남아있다면, 다음 턴에 [AttackDmgUp] 3 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013204].levelList[level=1].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [9013301] (ulepszenie 1) — nazwa] 채색
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013301].levelList[level=1].name
   limit: do 40 znaków
   EN: Coloring
   PL: Coloring
207. [Umiejętność wroga [9013301] (ulepszenie 1) — opis] [WinDuel] 대상의 [Laceration]이 5 이상이면, 공격 종료 후 무작위 적에게 이 스킬 재사용 (최대 1)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013301].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Laceration]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuel] If target has 5+ [Laceration], reuse this Skill on a random enemy at Attack End (once)
   PL: [WinDuel] jeżeli cel ma 5+ [Laceration], używa ponownie tę Umiejętność na losowym wrogu po zakończeniu Ataku (1 raz)
208. [Umiejętność wroga [9013301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [9013301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [9013301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +4 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Laceration]
211. [Umiejętność wroga [9013302] (ulepszenie 1) — nazwa] 혈점묘화
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].name
   limit: do 40 znaków
   EN: Sanguine Pointillism
   PL: Sanguine Pointillism
212. [Umiejętność wroga [9013302] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 피해량 +30%
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].desc
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [9013302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있다면, 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność wroga [9013302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [9013302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown] next turn
   PL: [OnSucceedAttack] nakłada 3 [AttackDown] w następnej turze
216. [Umiejętność wroga [9013302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Umiejętność wroga [9013302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 [Burst] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [9013303] (ulepszenie 1) — nazwa] 묘화
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013303].levelList[level=1].name
   limit: do 40 znaków
   EN: Pointillism
   PL: Pointillism
219. [Umiejętność wroga [9013303] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 코인 위력 +1 (최대 4)\n[WinDuel] 대상의 [Laceration]이 6 이상이면, 피해량 +40%
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013303].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WinDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Coin Power +1 for every 3 [Laceration] on target (max 4)\n[WinDuel] If target has 6+ [Laceration], deal +40% damage
   PL: Moc Monety +1 za każde 3 [Laceration] celu (maks. 4)\n[WinDuel] jeżeli cel ma 6+ [Laceration], zadaje +40% obrażeń
220. [Umiejętność wroga [9013303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration]
   PL: [OnSucceedAttack] nakłada 10 [Laceration]
221. [Umiejętność wroga [9013303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수만큼 [Burst] 횟수 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict [Burst] Count equal to [Laceration] Count on target
   PL: [OnSucceedAttack] nakłada Licznika [Burst] na cel w wysokości Licznika [Laceration] celu
222. [Umiejętność wroga [9013303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 [Burst] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [9013304] (ulepszenie 1) — nazwa] 핏방울꽃
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].name
   limit: do 40 znaków
   EN: Bloody of the Valley
   PL: Bloody of the Valley
224. [Umiejętność wroga [9013304] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Laceration]이 있다면, 다음 턴에 [Enhancement]를 1 얻음\n[WinDuel] 대상의 [Laceration]이 10 이상이면, 다음 턴에 [Enhancement]를 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Laceration], [Enhancement]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WinDuel] If target has [Laceration], gain 1 [Enhancement] next turn\n[WinDuel] If target has 10+ [Laceration], gain 1 [Enhancement] next turn
   PL: [WinDuel] jeżeli cel ma [Laceration], zyskuje 1 [Enhancement] w następnej turze\n[WinDuel] jeżeli cel ma 10+ [Laceration], zyskuje 1 [Enhancement] w następnej turze
225. [Umiejętność wroga [9013304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 2 [DefenseDown]
226. [Umiejętność wroga [9013304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [9013304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, 이 코인 재사용 (최대 3회)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 5+ [Laceration], reuse this Skill (3 times max)
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], używa tej Monety ponownie (do 3 razy)
228. [Umiejętność wroga [9013304] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Reduce [Laceration] Count on target by 1
   PL: [OnSucceedAttack] zmniejsza Licznik [Laceration] celu o 1
229. [Umiejętność wroga [9013304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttackHead] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [9013305] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013305].levelList[level=1].name
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [9013305] (ulepszenie 1) — opis] [OnSucceedEvade] [Enhancement] 1 얻음 (최대 2)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Enhancement]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [OnSucceedEvade] Gain [Enhancement] (max 2)
   PL: [OnSucceedEvade] zyskuje 1 [Enhancement] (maks. 2)
232. [Umiejętność wroga [9013501] (ulepszenie 1) — nazwa] 기본 공격 1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013501].levelList[level=1].name
   limit: do 40 znaków
   EN: Normal Attack 1
   PL: Normal Attack 1
233. [Umiejętność wroga [9013501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] next turn
   PL: [OnSucceedAttack] nakłada 1 [AttackDown] w następnej turze
234. [Umiejętność wroga [9013501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [9013501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 2 [Paralysis]
   PL: [OnSucceedAttackHead] nakłada 2 [Paralysis]
236. [Umiejętność wroga [9013502] (ulepszenie 1) — nazwa] 기본 공격 2
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013502].levelList[level=1].name
   limit: do 40 znaków
   EN: Normal Attack 2
   PL: Normal Attack 2
237. [Umiejętność wroga [9013502] (ulepszenie 1) — opis] [WhenUse] 대상에게 [AttackDown]이 있다면, 피해량 +20%
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has [AttackDown], deal +20% damage
   PL: [WhenUse] jeżeli cel ma [AttackDown], zadaje +20% obrażeń
238. [Umiejętność wroga [9013502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [HitResistDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HitResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HitResistDown] = 타격 내성 약화 / Blunt Resist Down
   EN: [OnSucceedAttack] Inflict 1 [HitResistDown]
   PL: [OnSucceedAttack] nakłada 1 [HitResistDown]
239. [Umiejętność wroga [9013502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [HitResistDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [9013502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [HitResistDown] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [HitResistDown], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [HitResistDown] = 타격 내성 약화 / Blunt Resist Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [DefenseDown] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [HitResistDown] w następnej turze
241. [Umiejętność wroga [9013503] (ulepszenie 1) — nazwa] 기본 공격 3
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].name
   limit: do 40 znaków
   EN: Normal Attack 3
   PL: Normal Attack 3
242. [Umiejętność wroga [9013503] (ulepszenie 1) — opis] [WhenUse] 대상의 [AttackDown]가 2 이상이면, 합위력 +1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has 2+ [AttackDown], Clash Power +1
   PL: [WhenUse] jeżeli cel ma 2+ [AttackDown], Moc Starcia +1
243. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 4 SP on self
   PL: [OnSucceedAttack] przywraca 4 SP
246. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [9013503] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013503].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [9013504] (ulepszenie 1) — nazwa] 기본 공격 4
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].name
   limit: do 40 znaków
   EN: Normal Attack 4
   PL: Normal Attack 4
252. [Umiejętność wroga [9013504] (ulepszenie 1) — opis] 부정적인 효과가 가장 많은 대상 우선 공격\n[WhenUse] 대상의 [DefenseDown] 3당 합 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Prioritizes targets with the most negative effects\n[WhenUse] Clash Power +1 for every 3 [DefenseDown] on target (max 3)
   PL: priorytet: cele z największą liczbą negatywnych efektów\n[WhenUse] Moc Starcia +1 za każde 3 [DefenseDown] celu (maks. 3)
253. [Umiejętność wroga [9013504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [9013504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
255. [Umiejętność wroga [9013504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 2 [Paralysis] w następnej turze
256. [Umiejętność wroga [9013504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [AttackDown] 2당 +20% (최대 100%)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Deal +20% damage for every 2 [AttackDown] on target (max 100%)
   PL: [OnSucceedAttack] zadaje +20% obrażeń za każde 2 [AttackDown] celu (maks. 100%)
257. [Umiejętność wroga [9013504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 대상의 부정적인 효과가 3개 이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 3+ negative effects, reuse this coin (1 time max)
   PL: [OnSucceedAttackHead] jeżeli cel ma 3+ negatywnych efektów, używa Monety ponownie (maks. 1 raz)
258. [Umiejętność wroga [9013505] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013505].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [9013505] (ulepszenie 1) — opis] 대상에게 [Vulnerable]이 있다면, 기본 위력 +1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9013505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: If target has [Vulnerable], Base Power +1
   PL: jeżeli cel ma [Vulnerable], Moc Bazowa +1
260. [Umiejętność wroga [9101501] (ulepszenie 1) — nazwa] 잡배놈들이!
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101501].levelList[level=1].name
   limit: do 40 znaków
   EN: Damn Plebs...!
   PL: Damn Plebs...!
261. [Umiejętność wroga [9101501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność wroga [9101501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność wroga [9101502] (ulepszenie 1) — nazwa] 치워주마
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101502].levelList[level=1].name
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [9101502] (ulepszenie 1) — opis] [WinDuel] 기본 위력 +1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Base Power +1
   PL: [WinDuel] Moc Bazowa +1
265. [Umiejętność wroga [9101502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [AttackDown]이 있다면, 피해량 20%만큼 타격 피해 입힘
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has [AttackDown], deal 20% of damage dealt as bonus Blunt damage
   PL: [OnSucceedAttack] jeżeli cel ma [AttackDown], zadaje dodatkowe obrażenia Uderzeniem równe 20% zadanych obrażeń
266. [Umiejętność wroga [9101502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [AttackDown]이 있다면, 피해량 20%만큼 타격 피해 입힘
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Umiejętność wroga [9101503] (ulepszenie 1) — nazwa] 단추를 맞춰야해
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101503].levelList[level=1].name
   limit: do 40 znaków
   EN: Make Things Right Again
   PL: Make Things Right Again
268. [Umiejętność wroga [9101503] (ulepszenie 1) — opis] [WinDuel] 대상의 [AttackDown]가 2 이상이면, 기본 위력 +1\n[WhenUse] 대상에게 [AttackDown]이 있다면, 피해량 +30%
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101503].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [AttackDown], [WhenUse]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [WhenUse] = [사용시] / [On Use]
   EN: [WinDuel] If target has 2+ [AttackDown], Base Power +1\n[WhenUse] If target has [AttackDown], deal +30% damage
   PL: [WinDuel] jeżeli cel ma 2+ [AttackDown], Moc Bazowa +1\n[WhenUse] jeżeli cel ma [AttackDown], zadaje +30% obrażeń
269. [Umiejętność wroga [9101503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [9101503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Umiejętność wroga [9101503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [9101504] (ulepszenie 1) — nazwa] 뭉개주마
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].name
   limit: do 40 znaków
   EN: Get Crushed
   PL: Get Crushed
273. [Umiejętność wroga [9101504] (ulepszenie 1) — opis] 부정적인 효과가 가장 많은 대상 우선 공격\n[WinDuel] 대상의 [AttackDown] 3당 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [AttackDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Prioritizes targets with the most negative effects\n[WinDuel] Coin Power +1 for every 3 [AttackDown] on target (max 3)
   PL: priorytet: cele z największą liczbą negatywnych efektów\n[WinDuel] Moc Monety +1 za każde 3 [AttackDown] celu (maks. 3)
274. [Umiejętność wroga [9101504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność wroga [9101504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Umiejętność wroga [9101504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [9101504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [AttackDown] 2당 +30% (최대 120%)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Deal +30% damage for every 2 [AttackDown] on target (max 120%)
   PL: [OnSucceedAttack] zadaje +30% obrażeń za każde 2 [AttackDown] celu (maks. 120%)
278. [Umiejętność wroga [9101504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 대상의 부정적인 효과가 3개 이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [9101505] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101505].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [9101505] (ulepszenie 1) — opis] [StartBattle] 자신을 제외한 살아있는 아군 수당 보호막 체력 20을 추가로 얻음.
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 20 additional Shield HP for every surviving other ally
   PL: [StartBattle] zyskuje dodatkowo 20 HP Tarczy za każdego innego żyjącego sojusznika.
281. [Umiejętność wroga [9101601] (ulepszenie 1) — nazwa] 배트치기
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101601].levelList[level=1].name
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność wroga [9101601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [9101601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [9101602] (ulepszenie 1) — nazwa] 내려박기
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101602].levelList[level=1].name
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność wroga [9101602] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Enhancement], 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Enhancement]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WinDuel] Gain 1 [Enhancement] and 1 Damage Up next turn
   PL: [WinDuel] zyskuje 1 [Enhancement] i 1 Wzrost Obrażeń w następnej turze
286. [Umiejętność wroga [9101602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [9101602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Umiejętność wroga [9101602] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101602].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [9101602] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 [Laceration] 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101602].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność wroga [9101603] (ulepszenie 1) — nazwa] 분풀기
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101603].levelList[level=1].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność wroga [9101603] (ulepszenie 1) — opis] 대상의 [Burst]이 5 이상이면, 합 위력 +1\n대상의 [Laceration]이 5 이상이면, 합 위력 +1\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101603].levelList[level=1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Umiejętność wroga [9101603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +1
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Umiejętność wroga [9101603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [9101603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Umiejętność wroga [9101603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] (대상의 [Laceration] X [Laceration] 횟수)만큼 관통 속성 피해를 입힘
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict bonus Pierce damage equal to ([Laceration] x [Laceration] Count)
   PL: [OnSucceedAttack] zadaje dodatkowe obrażenia Przebijające równe ([Laceration] x Licznik [Laceration])
296. [Umiejętność wroga [9101604] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101604].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność wroga [9101604] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101604].levelList[level=1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [9101605] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101605].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [9101605] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Enemy-a1c6p2.json :: dataList[id=9101605].levelList[level=1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c6p2] Pasywka wroga: Passives_Abnormality-a1c6p2
- plik gry: `Passives_Abnormality-a1c6p2.json`

300. [[a1c6p2] Pasywka wroga [815901] — nazwa] 죄악 저항
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=815901].name
   limit: do 40 znaków
   EN: Sin Resistance
   PL: Sin Resistance
301. [[a1c6p2] Pasywka wroga [815901] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면, 공격 스킬 적중 시 5만큼 흐트러짐 회복
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=815901].desc
   limit: do 140 znaków
   EN: Unless this unit is Staggered or Part Broken, lower its Stagger Threshold by 5 On Hit with an Attack Skill
   PL: o ile ta jednostka nie jest w Oszołamieniu i nie ma zniszczonej Części, przy trafieniu Umiejętnością ataku obniża swój Próg Oszołomienia o 5
302. [[a1c6p2] Pasywka wroga [816001] — nazwa] 죄악 저항
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816001].name
   (powtórzenie elementu 300 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [[a1c6p2] Pasywka wroga [816001] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면, 자신이 받는 파열 피해 50% 감소
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Unless this unit is Staggered or Part Broken, take 50% less [Burst] damage
   PL: o ile ta jednostka nie jest w Oszołamieniu i nie ma zniszczonej Części, otrzymuje o 50% mniej obrażeń [Burst]
304. [[a1c6p2] Pasywka wroga [816501] — nazwa] 끊임없는 열등감
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816501].name
   limit: do 40 znaków
   EN: Endless Insecurity
   PL: Endless Insecurity
305. [[a1c6p2] Pasywka wroga [816501] — opis] 자신의 체력이 65% 이하가 되면, 합 승리시 [AttackUp] 1, [TakeHpHealIncrease]를 1 얻음\n자신의 체력이 40% 이하가 되면, 사용시 [AttackUp] 1, [TakeHpHealIncrease]를 1 얻음\n한 번이라도 조건이 만족되면, 해당 조건으로 계속 발동됨.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816501].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [TakeHpHealIncrease]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: At less than 65% HP: gain 1 [AttackUp] and 1 [TakeHpHealIncrease] on Clash Win\nAt less than 40% HP: gain 1 [AttackUp] and 1 [TakeHpHealIncrease] On Use\nThe effects linger even after the conditions no longer apply, as long as they have been activated at least once.
   PL: przy HP 65% lub mniej: zyskuje 1 [AttackUp] i 1 [TakeHpHealIncrease] po wygranej w Starciu\nprzy HP 40% lub mniej: zyskuje 1 [AttackUp] i 1 [TakeHpHealIncrease] przy użyciu Umiejętności\npodczas gdy warunek zostanie spełniony choć raz, efekt działa nadal.
306. [[a1c6p2] Pasywka wroga [816501] — podsumowanie] 조건에 따라 자기 강화 긍정 효과를 얻음.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816501].summary
   limit: do 120 znaków
   EN: Gain conditional self-enhancing positive status effects.
   PL: zyskuje warunkowe pozytywne efekty wzmacniające siebie.
307. [[a1c6p2] Pasywka wroga [816502] — nazwa] 향해지는 분노
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816502].name
   limit: do 40 znaków
   EN: Directed Wrath
   PL: Directed Wrath
308. [[a1c6p2] Pasywka wroga [816502] — opis] 첫 흐트러짐 해제 이후 합 승리 시 공격 스킬 적중시 피해량의 10%만큼 추가 분노 피해를 입힘.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816502].desc
   limit: do 160 znaków
   EN: After the first recovery from Stagger, and after Clash Win, deal 10% of the damage dealt On Hit as Wrath bonus damage.
   PL: po pierwszym dojściu do siebie z Oszołamienia, po wygranej w Starciu zadaje przy trafieniu dodatkowe obrażenia Gniewu równe 10% zadanych obrażeń.
309. [[a1c6p2] Pasywka wroga [816503] — nazwa] 포식
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816503].name
   limit: do 40 znaków
   EN: Predation
   PL: Predation
310. [[a1c6p2] Pasywka wroga [816503] — opis] 적 처치 시, 본체 및 부위 체력을 200 회복.\n다음 턴에 [Agility] 1, [DefenseUp] 3, [AttackUp] 2 얻음.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816503].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [DefenseUp], [AttackUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Kill, heal 200 HP for Core and Part.\nGain 1 [Agility], 3 [DefenseUp], and 2 [AttackUp] next turn.
   PL: przy pokonaniu wroga przywraca 200 HP Korpusowi i Części.\nzyskuje 1 [Agility], 3 [DefenseUp] i 2 [AttackUp] w następnej turze.
311. [[a1c6p2] Pasywka wroga [816504] — nazwa] 표식
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816504].name
   limit: do 40 znaków
   EN: Marked
   PL: Marked
312. [[a1c6p2] Pasywka wroga [816504] — opis] [AaCfPbBe]을 가지고 있는 대상 우선 공격
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816504].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AaCfPbBe]
   znaczenie tagów: [AaCfPbBe] = 사냥감 표시 / Marked Prey
   EN: Prioritizes targets with [AaCfPbBe]
   PL: priorytet: cele z [AaCfPbBe]
313. [[a1c6p2] Pasywka wroga [816401] — nazwa] 자기 혐오
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816401].name
   limit: do 40 znaków
   EN: Self-loathing
   PL: Self-loathing
314. [[a1c6p2] Pasywka wroga [816401] — opis] 모든 스킬이 히스클리프를 타겟으로 함.\n히스클리프가 사망하면, 자신이 전투에서 승리함.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All Skills target Heathcliff.\nWins Encounter if Heathcliff dies.
   PL: wszystkie Umiejętności wskazują Heathcliffa jako cel.\njeżeli Heathcliff ginie, ta jednostka wygrywa walkę.
315. [[a1c6p2] Pasywka wroga [816402] — nazwa] 폭발하는 감정
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816402].name
   limit: do 40 znaków
   EN: Explosive Emotions
   PL: Explosive Emotions
316. [[a1c6p2] Pasywka wroga [816402] — opis] 폭발하는 감정 계열 효과가 있는 동안 해당 속성에 취약해지고, 그 외 속성의 내성에 강인해지며, 피격 시 특수한 효과를 얻음.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816402].desc
   limit: do 230 znaków
   EN: When this unit has 'Explosive' Affinity effects: become weaker to the corresponding Affinities and become stronger against every other Affinity; gain a special effect when hit.
   PL: gdy ta jednostka ma efekty Afinności typu „Explosive”: staje się podatna na odpowiadające Afinności i odporniejsza na wszystkie pozostałe Afinności; przy trafieniu zyskuje specjalny efekt.
317. [[a1c6p2] Pasywka wroga [816403] — nazwa] 깊은 상실
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816403].name
   limit: do 40 znaków
   EN: Deep Bereavement
   PL: Deep Bereavement
318. [[a1c6p2] Pasywka wroga [816403] — opis] 폭발하는 감정 계열 효과를 획득한 턴부터 2턴이 종료되기 전에 해당 효과가 해제되면, 다음 턴부터 2턴 간 [AaCfPbBd]을 얻고, 스킬 패턴이 변경됨.\n그 때까지 해제되지 않았다면 효과가 해제되고, 다음 턴에 [AttackUp] 6, [Agility] 3을 얻음.
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816403].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPbBd], [AttackUp], [Agility]
   znaczenie tagów: [AaCfPbBd] = 깊은 상실 / Deep Bereavement; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Agility] = 신속 / Haste
   EN: If this unit loses an 'Explosive' Affinity effect before the 2nd turn after obtaining that effect ends, gain [AaCfPbBd] for the next 2 turns, and gain a new Skill pattern.\nIf this effect does not expire within that time limit, lose the effect, then gain 6 [AttackUp] and 3 [Agility] next turn.
   PL: jeżeli ta jednostka traci efekt Afinności typu „Explosive” przed końcem 2. tury od jego zdobycia, zyskuje [AaCfPbBd] na 2 następne tury, a jej wzorzec Umiejętności ulega zmianie.\njeżeli efekt nie wygaśnie w tym czasie, zostaje odebrany, a jednostka zyskuje 6 [AttackUp] i 3 [Agility] w następnej turze.
319. [[a1c6p2] Pasywka wroga [816404] — nazwa] 나오면 안되는 텍스트
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816404].name
   limit: do 40 znaków
   EN: NOTHING TO SEE HERE
   PL: NOTHING TO SEE HERE
320. [[a1c6p2] Pasywka wroga [816404] — opis] 나오면 안되는 텍스트
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816404].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [[a1c6p2] Pasywka wroga [816405] — nazwa] 악에 받친
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816405].name
   limit: do 40 znaków
   EN: Spite-driven
   PL: Spite-driven
322. [[a1c6p2] Pasywka wroga [816405] — opis] 스킬 종료 시 히스클리프에게 공격을 적중시키지 못했으면 폭발하는 감정 1 감소\n턴 종료 시 흐트러짐 상태였으면, 폭발하는 감정 3 감소\n폭발하는 감정은 한 턴 당 최대 3 감소하며, 턴 종료 시 수치가 1이면, 해당 버프가 해제됨
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816405].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit failed to land a hit on Heathcliff by Skill End, lose 1 Explosive Emotion\nIf this unit is Staggered at Turn End, lose 3 Explosive Emotion\nThis unit does not lose more than 3 Explosive Emotion per turn; if the value of Explosive Emotion is 1 at Turn End, lose the said effect
   PL: jeżeli jednostka nie trafiła Heathcliffa do końca Umiejętności, traci 1 Explosive Emotion\njeżeli na koniec tury jest w Oszołamieniu, traci 3 Explosive Emotion\nnie traci więcej niż 3 Explosive Emotion na turę; jeżeli na koniec tury wartość wynosi 1, efekt zostaje odebrany
323. [[a1c6p2] Pasywka wroga [816406] — nazwa] 복수심
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816406].name
   limit: do 40 znaków
   EN: Heart of Vengeance
   PL: Heart of Vengeance
324. [[a1c6p2] Pasywka wroga [816406] — opis] 턴 시작 시 정신력이 -45가 아니면, 정신력 15 회복.\n턴 종료 시 패닉 상태면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨.\n턴 종료 시 패닉 상태가 해제되면, 다음 턴 시작 시 [Enhancement] 2 얻음
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816406].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: If not at -45 SP, heal 15 SP.\nTurn End: If Panicked, recover from Panic at the next Turn Start and reset SP to 0.\nTurn End: If this unit recovers from Panic, gain 2 [Enhancement] at the next Turn Start
   PL: Początek tury: przy SP innym niż -45 przywraca 15 SP.\nKoniec tury: jeżeli jest w Panice, na początku następnej tury dochodzi do siebie z Paniki, a SP wraca do 0.\nKoniec tury: jeżeli dochodzi do siebie z Paniki, na początku następnej tury zyskuje 2 [Enhancement]
325. [[a1c6p2] Pasywka wroga [816505] — nazwa] 내가 설 자리
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816505].name
   limit: do 40 znaków
   EN: A Place for Me
   PL: A Place for Me
326. [[a1c6p2] Pasywka wroga [816505] — opis] 한 턴동안 체력이 40%이하로 떨어지지않음.\n패턴이 변경됨
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816505].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: HP does not drop below 40% for 1 turn.\nGains a new pattern
   PL: przez 1 turę HP nie spada poniżej 40%.\nprzybiera nowy wzorzec
327. [[a1c6p2] Pasywka wroga [816407] — nazwa] 뜻 모를 분노
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816407].name
   limit: do 40 znaków
   EN: Fathomless Wrath
   PL: Fathomless Wrath
328. [[a1c6p2] Pasywka wroga [816407] — opis] 스킬 종료 시 공격을 적중시키지 못했으면 폭발하는 감정 1 감소\n턴 종료 시 흐트러짐 상태였으면, 폭발하는 감정 3 감소\n폭발하는 감정은 한 턴 당 최대 3 감소하며, 턴 종료 시 수치가 1이면, 해당 버프가 해제됨
   źródło: Passives_Abnormality-a1c6p2.json :: dataList[id=816407].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit failed to land a hit by Skill End, lose 1 Explosive Emotion\nIf this unit is Staggered at Turn End, lose 3 Explosive Emotion\nThis unit does not lose more than 3 Explosive Emotion per turn; if the value of Explosive Emotion is 1 at Turn End, lose the said effect
   PL: jeżeli jednostka nie trafiła przeciwnika do końca Umiejętności, traci 1 Explosive Emotion\njeżeli na koniec tury jest w Oszołamieniu, traci 3 Explosive Emotion\nnie traci więcej niż 3 Explosive Emotion na turę; jeżeli na koniec tury wartość wynosi 1, efekt zostaje odebrany

## [a1c6p2] Pasywka wroga: Passives_Enemy-a1c6p2
- plik gry: `Passives_Enemy-a1c6p2.json`

329. [[a1c6p2] Pasywka wroga [9012801] — nazwa] 느슨한 이행
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9012801].name
   limit: do 40 znaków
   EN: Lenient Rule Fulfillment
   PL: Lenient Rule Fulfillment
330. [[a1c6p2] Pasywka wroga [9012801] — opis] 합 진행 시, 합 위력 -1
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9012801].desc
   limit: do 120 znaków
   EN: In a Clash, Clash Power -1
   PL: podczas Starcia, Moc Starcia -1
331. [[a1c6p2] Pasywka wroga [9012801] — podsumowanie] 합 위력 -1
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9012801].summary
   limit: do 120 znaków
   EN: Clash Power -1
   PL: Moc Starcia -1
332. [[a1c6p2] Pasywka wroga [9012802] — nazwa] 혈점
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9012802].name
   limit: do 40 znaków
   EN: Bloody Point
   PL: Bloody Point
333. [[a1c6p2] Pasywka wroga [9012802] — opis] [Laceration]이 있는 대상에게 적중 시 자신의 정신력 2 회복
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9012802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Heal 2 SP on self On Hit against targets with [Laceration]
   PL: przy trafieniu w cel z [Laceration] przywraca 2 SP
334. [[a1c6p2] Pasywka wroga [9012802] — podsumowanie] 자신의 정신력 2 회복
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9012802].summary
   limit: do 120 znaków
   EN: Heal 2 SP on self
   PL: przywraca 2 SP
335. [[a1c6p2] Pasywka wroga [9013001] — nazwa] 전력 보강
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013001].name
   limit: do 40 znaków
   EN: Reinforcements
   PL: Reinforcements
336. [[a1c6p2] Pasywka wroga [9013001] — opis] 아군이 죽음을 맞이할 때, 다음 턴부터 슬롯이 1 증가함 (최대 2)
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013001].desc
   limit: do 120 znaków
   EN: When an ally is defeated, gain 1 Slot next turn (max 2)
   PL: gdy sojusznik zostaje pokonany, zyskuje 1 Slot w następnej turze (maks. 2)
337. [[a1c6p2] Pasywka wroga [9013101] — nazwa] 본연의 멋
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013101].name
   limit: do 40 znaków
   EN: Natural Style
   PL: Natural Style
338. [[a1c6p2] Pasywka wroga [9013101] — opis] 합 진행 시, 합 위력 +1
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013101].desc
   limit: do 120 znaków
   EN: In a Clash, Clash Power +1
   PL: podczas Starcia, Moc Starcia +1
339. [[a1c6p2] Pasywka wroga [9013101] — podsumowanie] 합 위력 +1
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013101].summary
   limit: do 120 znaków
   EN: Clash Power +1
   PL: Moc Starcia +1
340. [[a1c6p2] Pasywka wroga [9013102] — nazwa] 혈점묘화
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013102].name
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [[a1c6p2] Pasywka wroga [9013102] — opis] [Laceration]이 있는 대상에게 적중 시 자신의 정신력 2 회복
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013102].desc
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [[a1c6p2] Pasywka wroga [9013301] — nazwa] 전력 보강
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013301].name
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [[a1c6p2] Pasywka wroga [9013301] — opis] 아군이 죽음을 맞이할 때, 다음 턴부터 슬롯이 1 증가함 (최대 2)
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013301].desc
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [[a1c6p2] Pasywka wroga [9013302] — nazwa] 예술의 한 점
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013302].name
   limit: do 40 znaków
   EN: A Single Point of Art
   PL: A Single Point of Art
345. [[a1c6p2] Pasywka wroga [9013302] — opis] 합 승리 시, 자신을 포함한 모든 아군의 정신력 3 회복
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9013302].desc
   limit: do 120 znaków
   EN: Clash Win: all allies, including this unit, heals 3 SP
   PL: wygrana w Starciu: wszyscy sojusznicy (łącznie z tą jednostką) przywracają po 3 SP
346. [[a1c6p2] Pasywka wroga [9101501] — nazwa] 육체 시술 - 육체 증폭
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101501].name
   limit: do 40 znaków
   EN: Body Augment - Phys. Boost
   PL: Body Augment - Phys. Boost
347. [[a1c6p2] Pasywka wroga [9101501] — opis] 턴 종료 시 자신의 정신력이 -10 이하일 때, 다음 턴에 [AttackUp] 3 얻음.
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn End: if this unit's SP is at -10 or less, gain 3 [AttackUp] next turn.
   PL: Koniec tury: jeżeli SP tej jednostki wynosi -10 lub mniej, zyskuje 3 [AttackUp] w następnej turze.
348. [[a1c6p2] Pasywka wroga [9101502] — nazwa] 전력 보강
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101502].name
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [[a1c6p2] Pasywka wroga [9101502] — opis] 아군이 죽음을 맞이할 때, 다음 턴부터 슬롯이 1 증가함 (최대 3)
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101502].desc
   limit: do 120 znaków
   EN: When an ally is defeated, gain 1 Slot next turn (max 3)
   PL: gdy sojusznik zostaje pokonany, zyskuje 1 Slot w następnej turze (maks. 3)
350. [[a1c6p2] Pasywka wroga [9101503] — nazwa] 육체 시술 - 쿨다운
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101503].name
   limit: do 40 znaków
   EN: Body Augment - Cooldown
   PL: Body Augment - Cooldown
351. [[a1c6p2] Pasywka wroga [9101503] — opis] 패닉 상태라면, 턴 종료 시 정신력이 0이 됨.
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101503].desc
   limit: do 120 znaków
   EN: When in Panic, reset SP to 0 at Turn End.
   PL: jeżeli jest w Panice, na koniec tury SP wraca do 0.
352. [[a1c6p2] Pasywka wroga [9101504] — nazwa] 이럴리가 없어
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101504].name
   limit: do 40 znaków
   EN: This Can't Be
   PL: This Can't Be
353. [[a1c6p2] Pasywka wroga [9101504] — opis] 죽은 아군 수당 다음 턴부터 [AttackDown] 2를 얻음.
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101504].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDown]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Every time an ally is defeated, gain 2 [AttackDown] starting next turn.
   PL: za każdego pokonanego sojusznika zyskuje 2 [AttackDown] od następnej tury.
354. [[a1c6p2] Pasywka wroga [9101505] — nazwa] 이번에는 이겼다...!
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101505].name
   limit: do 40 znaków
   EN: This Time, I Win...!
   PL: This Time, I Win...!
355. [[a1c6p2] Pasywka wroga [9101505] — opis] 5합 이상에서 승리할 경우, 가하는 피해량 +50%
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101505].desc
   limit: do 120 znaków
   EN: If this unit wins after 5+ Clashes, deal +50% damage
   PL: jeżeli wygrywa w 5. Starciu lub późniejszym, zadaje +50% obrażeń
356. [[a1c6p2] Pasywka wroga [9101604] — nazwa] 쓸모 없는 것들...
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101604].name
   limit: do 40 znaków
   EN: Useless Fools...
   PL: Useless Fools...
357. [[a1c6p2] Pasywka wroga [9101604] — opis] 적이 아군을 처치하면 다음 턴에 [Enhancement] 1, [Agility] 1을 얻음 (턴 당 최대 3)
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101604].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Agility]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste
   EN: If an enemy defeats an ally, gain 1 [Enhancement] and 1 [Agility] next turn (3 times per turn)
   PL: gdy wróg pokonuje sojusznika, zyskuje 1 [Enhancement] i 1 [Agility] w następnej turze (do 3 razy na turę)
358. [[a1c6p2] Pasywka wroga [9101605] — nazwa] 가시 배트
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101605].name
   limit: do 40 znaków
   EN: Spiked Bat
   PL: Spiked Bat
359. [[a1c6p2] Pasywka wroga [9101605] — opis] 공격 적중 시 피해량의 50%만큼 관통 추가 피해를 줌
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101605].desc
   limit: do 120 znaków
   EN: On Hit, inflict bonus Pierce damage equal to 50% of the damage dealt
   PL: przy trafieniu zadaje dodatkowe obrażenia Przebijające równe 50% zadanych obrażeń
360. [[a1c6p2] Pasywka wroga [9101601] — nazwa] 데드레빗츠 보스?
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101601].name
   limit: do 40 znaków
   EN: Dead Rabbits Boss?
   PL: Dead Rabbits Boss?
361. [[a1c6p2] Pasywka wroga [9101601] — opis] 턴 시작 시 자신을 제외한 정신력이 가장 낮은 아군 2명에게 [Enhancement] 1 부여\n아군이 사망할 때마다 이번 전투동안 슬롯 수 + 1
   źródło: Passives_Enemy-a1c6p2.json :: dataList[id=9101601].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: apply 1 [Enhancement] to 2 other allies with the least SP\nFor this Encounter, gain a Slot every time an ally is defeated
   PL: Początek tury: nakłada 1 [Enhancement] na 2 innych sojuszników z najmniejszym SP\nna czas tej walki zyskuje 1 Slot za każdym razem, gdy sojusznik zostaje pokonany

## [a1c6p3] Wróg / część: Enemies-a1c6p3
- plik gry: `Enemies-a1c6p3.json`

362. [[a1c6p3] Wróg / część [8166] — nazwa] 마음이 찢겨진 히스클리프
   źródło: Enemies-a1c6p3.json :: dataList[id=8166].name
   limit: do 40 znaków
   EN: Heathcliff, The Heartbroken
   PL: Heathcliff, The Heartbroken
363. [[a1c6p3] Wróg / część [816602] — nazwa] 사슬
   źródło: Enemies-a1c6p3.json :: dataList[id=816602].name
   limit: do 40 znaków
   EN: The Chain
   PL: The Chain
364. [[a1c6p3] Wróg / część [8167] — nazwa] 와일드헌트 조세핀
   źródło: Enemies-a1c6p3.json :: dataList[id=8167].name
   limit: do 40 znaków
   EN: Josephine of the Wild Hunt
   PL: Josephine of the Wild Hunt
365. [[a1c6p3] Wróg / część [8168] — nazwa] 와일드헌트 힌들리
   źródło: Enemies-a1c6p3.json :: dataList[id=8168].name
   limit: do 40 znaków
   EN: Hindley of the Wild Hunt
   PL: Hindley of the Wild Hunt
366. [[a1c6p3] Wróg / część [8169] — nazwa] 와일드헌트 린튼
   źródło: Enemies-a1c6p3.json :: dataList[id=8169].name
   limit: do 40 znaków
   EN: Linton of the Wild Hunt
   PL: Linton of the Wild Hunt
367. [[a1c6p3] Wróg / część [8170] — nazwa] 와일드헌트 빼앗겨 울부짖는 힌들리
   źródło: Enemies-a1c6p3.json :: dataList[id=8170].name
   limit: do 50 znaków
   EN: The Reaved Lamenter of the Wild Hunt
   PL: The Reaved Lamenter of the Wild Hunt
368. [[a1c6p3] Wróg / część [8171] — nazwa] 넬리
   źródło: Enemies-a1c6p3.json :: dataList[id=8171].name
   limit: do 40 znaków
   EN: Nelly
   PL: Nelly
369. [[a1c6p3] Wróg / część [8172] — nazwa] 마왕 히스클리프
   źródło: Enemies-a1c6p3.json :: dataList[id=8172].name
   limit: do 40 znaków
   EN: Erlking Heathcliff
   PL: Erlking Heathcliff
370. [[a1c6p3] Wróg / część [8173] — nazwa] 마왕 히스클리프
   źródło: Enemies-a1c6p3.json :: dataList[id=8173].name
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [[a1c6p3] Wróg / część [8174] — nazwa] 모든 캐서린
   źródło: Enemies-a1c6p3.json :: dataList[id=8174].name
   limit: do 40 znaków
   EN: Every Catherine
   PL: Every Catherine
372. [[a1c6p3] Wróg / część [8192] — nazwa] 모든 캐서린 왼손
   źródło: Enemies-a1c6p3.json :: dataList[id=8192].name
   limit: do 40 znaków
   EN: Left Hand of Every Catherine
   PL: Left Hand of Every Catherine
373. [[a1c6p3] Wróg / część [8193] — nazwa] 모든 캐서린 오른손
   źródło: Enemies-a1c6p3.json :: dataList[id=8193].name
   limit: do 50 znaków
   EN: Right Hand of Every Catherine
   PL: Right Hand of Every Catherine
374. [[a1c6p3] Wróg / część [8161] — nazwa] 분노 죄종??
   źródło: Enemies-a1c6p3.json :: dataList[id=8161].name
   limit: do 40 znaków
   EN: Peccatulum Irae??
   PL: Peccatulum Irae??
375. [[a1c6p3] Wróg / część [9999] — nazwa] 베르길리우스
   źródło: Enemies-a1c6p3.json :: dataList[id=9999].name
   limit: do 40 znaków
   EN: Vergilius
   PL: Vergilius
376. [[a1c6p3] Wróg / część [819201] — nazwa] 왼손
   źródło: Enemies-a1c6p3.json :: dataList[id=819201].name
   limit: do 40 znaków
   EN: Left Hand
   PL: Left Hand
377. [[a1c6p3] Wróg / część [819301] — nazwa] 오른손
   źródło: Enemies-a1c6p3.json :: dataList[id=819301].name
   limit: do 40 znaków
   EN: Right Hand
   PL: Right Hand

## [a1c6p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c6p3
- grupa rozdziału/trybu: `a1c6p3` · plik: `Skills_Abnormality-a1c6p3.json`

378. [Umiejętność wroga [816101] (ulepszenie 1) — nazwa] 찔러대기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816101].levelList[level=1].name
   limit: do 40 znaków
   EN: Impaling
   PL: Impaling
379. [Umiejętność wroga [816101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 6 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 6 [Combustion] i 2 Licznika [Combustion]
380. [Umiejętność wroga [816102] (ulepszenie 1) — nazwa] 베어대기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816102].levelList[level=1].name
   limit: do 40 znaków
   EN: Hewing
   PL: Hewing
381. [Umiejętność wroga [816102] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Combustion]이 있을 때, 기본 위력 +2
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Combustion]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Combustion] = 화상 / Burn
   EN: [WinDuel] If target has [Combustion], Base Power +2
   PL: [WinDuel] jeżeli cel ma [Combustion], Moc Bazowa +2
382. [Umiejętność wroga [816102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 8 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 8 [Combustion]
   PL: [OnSucceedAttack] nakłada 8 [Combustion]
383. [Umiejętność wroga [816102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 4 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +4 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Combustion]
384. [Umiejętność wroga [816102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn
   PL: [OnSucceedAttack] nakłada 1 [PenetrateTakeDamageUp] w następnej turze
385. [Umiejętność wroga [816103] (ulepszenie 1) — nazwa] 분출하는 분노
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816103].levelList[level=1].name
   limit: do 40 znaków
   EN: Erupting Wrath
   PL: Erupting Wrath
386. [Umiejętność wroga [816103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 5당, 코인 위력 +1 (최대 3)\n[WinDuel] 대상의 [Combustion]이 9이상이면, 이 스킬의 가중치 +1
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816103].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 5 [Combustion] on target (max 3)\n[WinDuel] If target has 9+ [Combustion], this Skill gains Atk Weight +1
   PL: [WhenUse] Moc Monety +1 za każde 5 [Combustion] celu (maks. 3)\n[WinDuel] jeżeli cel ma 9+ [Combustion], Waga Ataku tej Umiejętności +1
387. [Umiejętność wroga [816103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Combustion]
388. [Umiejętność wroga [816103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [CrimsonTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [CrimsonTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: [OnSucceedAttackHead] Inflict 1 [CrimsonTakeDamageUp] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [CrimsonTakeDamageUp] w następnej turze
389. [Umiejętność wroga [816104] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816104].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [816104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]이 5이상이면, 코인 위력 +2\n[WhenUse] 대상의 [Combustion]이 6이상이면, 이 스킬 재사용 (최대 2)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816104].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] If target has 5+ [Combustion], Coin Power +2\n[WhenUse] If target has 6+ [Combustion], reuse this Skill (2 times max)
   PL: [WhenUse] jeżeli cel ma 5+ [Combustion], Moc Monety +2\n[WhenUse] jeżeli cel ma 6+ [Combustion], używa ponownie tę Umiejętność (do 2 razy)
391. [Umiejętność wroga [816104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp_Weak] 10 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp_Weak]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp_Weak] = 약점 공격 시 피해 증가 / Weak-resist DMG Boost
   EN: [OnSucceedAttack] Gain 10 [AttackDmgUp_Weak] next turn
   PL: [OnSucceedAttack] zyskuje 10 [AttackDmgUp_Weak] w następnej turze
392. [Umiejętność wroga [816601] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816601].levelList[level=1].name
   limit: do 40 znaków
   EN: Brush Wounds
   PL: Brush Wounds
393. [Umiejętność wroga [816601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
394. [Umiejętność wroga [816601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttackHead] nakłada 1 Licznika [Laceration]
395. [Umiejętność wroga [816601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [816601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttackHead] nakłada 2 Licznika [Laceration]
397. [Umiejętność wroga [816602] (ulepszenie 1) — nazwa] 찢겨진 마음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816602].levelList[level=1].name
   limit: do 40 znaków
   EN: Broken Heart
   PL: Broken Heart
398. [Umiejętność wroga [816602] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [DefenseUp] 3 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [DefenseUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WinDuel] Gain 3 [DefenseUp] next turn
   PL: [WinDuel] zyskuje 3 [DefenseUp] w następnej turze
399. [Umiejętność wroga [816602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [DefenseDown] w następnej turze
400. [Umiejętność wroga [816602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 4 [Laceration]
   PL: [OnSucceedAttackHead] nakłada 4 [Laceration]
401. [Umiejętność wroga [816602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [816602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttackHead] nakłada 3 Licznika [Laceration]
403. [Umiejętność wroga [816603] (ulepszenie 1) — nazwa] 파탄, 탄식 그리고 절규
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816603].levelList[level=1].name
   limit: do 50 znaków
   EN: Ruination, Wailing, and Lamentation
   PL: Ruination, Wailing, and Lamentation
404. [Umiejętność wroga [816603] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816603].levelList[level=1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność wroga [816603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Umiejętność wroga [816603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Attack Power Up next turn
   PL: [OnSucceedAttack] zyskuje 1 Wzrost Mocy Ataku w następnej turze
407. [Umiejętność wroga [816603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [EnemyKill] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 2 Attack Power Up next turn
   PL: [EnemyKill] zyskuje 2 Wzrost Mocy Ataku w następnej turze
408. [Umiejętność wroga [816604] (ulepszenie 1) — nazwa] 인간의 말을 해서도 안되는거야
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816604].levelList[level=1].name
   limit: do 40 znaków
   EN: Undeserving of Speech
   PL: Undeserving of Speech
409. [Umiejętność wroga [816604] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 8+ [Laceration], Clash Power +1
   PL: [WhenUse] jeżeli cel ma 8+ [Laceration], Moc Starcia +1
410. [Umiejętność wroga [816604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 [Laceration]이 4이상이면, 다음 코인 피해량 +20%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] If target has 4+ [Laceration], the next Coin deals +20% damage
   PL: [OnSucceedAttackHead] jeżeli cel ma 4+ [Laceration], następna Moneta zadaje +20% obrażeń
411. [Umiejętność wroga [816604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 부정적인 효과 수가 3개 이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 3+ negative effects, reuse this coin (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 3+ negatywnych efektów, używa Monety ponownie (maks. 1 raz)
412. [Umiejętność wroga [816605] (ulepszenie 1) — nazwa] 시체자루
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].name
   limit: do 40 znaków
   EN: Bodysack
   PL: Bodysack
413. [Umiejętność wroga [816605] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5당, 기본 위력 +1 (최대 3)\n[WhenUse] 대상의 부정적인 효과 수당 합 위력 +1 (최대 2)\n[DefeatDuel] [DefenseDown] 20 얻음\n[DefeatDuel] 해방되지 못한 서글픔 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] Base Power +1 for every 5 [Laceration] on target (max 3)\n[WhenUse] Clash Power +1 for every negative effect on target (max 2)\n[DefeatDuel] Gain 20 [DefenseDown]\n[DefeatDuel] Gain 1 Fettered Woe
   PL: [WhenUse] Moc Bazowa +1 za każde 5 [Laceration] celu (maks. 3)\n[WhenUse] Moc Starcia +1 za każdy negatywny efekt celu (maks. 2)\n[DefeatDuel] zyskuje 20 [DefenseDown]\n[DefeatDuel] zyskuje 1 Fettered Woe
414. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 1 [DefenseDown]
415. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 대상의 [Laceration]이 8이상이면, 마지막 코인 피해량 +30%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] If target has 8+ [Laceration], the last Coin deals +30% damage
   PL: [OnSucceedAttackHead] jeżeli cel ma 8+ [Laceration], ostatnia Moneta zadaje +30% obrażeń
416. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 대상의 [Laceration]이 8이상이면, 마지막 코인 피해량 +30%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 대상의 [Laceration]이 8이상이면, 마지막 코인 피해량 +30%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Umiejętność wroga [816605] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이 스킬의 모든 코인이 앞면이면, 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816605].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If this Skill flips all Heads, inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] jeżeli wszystkie Monety tej Umiejętności wypadną Awersami, nakłada 2 [Vulnerable] w następnej turze
421. [Umiejętność wroga [816606] (ulepszenie 1) — nazwa] 미친 늑대의 광기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816606].levelList[level=1].name
   limit: do 40 znaków
   EN: Lunacy of the Frenzied Wolf
   PL: Lunacy of the Frenzied Wolf
422. [Umiejętność wroga [816606] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5당, 기본 위력 +1 (최대 4)\n[WhenUse] 대상의 부정적인 효과 수당 합 위력 +1 (최대 2)\n[DefeatDuel] 대상이 [AaCfPcBg]을 가지고 있다면, 다음 턴에 100만큼 흐트러짐 손상. 흐트러짐 수치가 없을 경우 0에 흐트러짐 수치를 만듦.
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816606].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel], [AaCfPcBg]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [AaCfPcBg] = 분노의 대상 / Subject of Wrath
   EN: [WhenUse] Base Power +1 for every 5 [Laceration] on target (max 4)\n[WhenUse] Clash Power +1 for every negative effect on target (max 2)\n[DefeatDuel] If target has [AaCfPcBg], raise this unit's Stagger Threshold by 100 next turn. If this unit does not have a Stagger threshold, create a new Stagger threshold at 0.
   PL: [WhenUse] Moc Bazowa +1 za każde 5 [Laceration] celu (maks. 4)\n[WhenUse] Moc Starcia +1 za każdy negatywny efekt celu (maks. 2)\n[DefeatDuel] jeżeli cel ma [AaCfPcBg], zadaje celowi 100 obrażeń Oszołamieniem w następnej turze. jeżeli cel nie ma Progu Oszołomienia, tworzy go na poziomie 0.
423. [Umiejętność wroga [816606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Umiejętność wroga [816606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność wroga [816606] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816606].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [816606] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이 스킬의 모든 코인이 적중했다면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816606].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If every Coin of this Skill hits, reuse this Coin (1 time max)
   PL: [OnSucceedAttack] jeżeli wszystkie Monety tej Umiejętności trafiły, używa Monety ponownie (maks. 1 raz)
427. [Umiejętność wroga [816607] (ulepszenie 1) — nazwa] 반사적 복수
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816607].levelList[level=1].name
   limit: do 40 znaków
   EN: Reflexive Revenge
   PL: Reflexive Revenge
428. [Umiejętność wroga [816607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
429. [Umiejętność wroga [816607] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=816607].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [817101] (ulepszenie 1) — nazwa] 불청객 표시
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817101].levelList[level=1].name
   limit: do 40 znaków
   EN: Mark Interloper
   PL: Mark Interloper
431. [Umiejętność wroga [817101] (ulepszenie 1) — opis] [WhenUse] [AaCfPcBb] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [AaCfPcBb]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AaCfPcBb] = 버틀러의 표식 / Butler's Mark
   EN: [WhenUse] Inflict 1 [AaCfPcBb]
   PL: [WhenUse] nakłada 1 [AaCfPcBb]
432. [Umiejętność wroga [817101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
433. [Umiejętność wroga [817101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 1 [DefenseUp] next turn
   PL: [OnSucceedAttack] zyskuje 1 [DefenseUp] w następnej turze
434. [Umiejętność wroga [817101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] zyskuje 2 [Breath]
435. [Umiejętność wroga [817102] (ulepszenie 1) — nazwa] 응접도 1식 사냥
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817102].levelList[level=1].name
   limit: do 40 znaków
   EN: Receiving Arts 1: The Hunt
   PL: Receiving Arts 1: The Hunt
436. [Umiejętność wroga [817102] (ulepszenie 1) — opis] [WhenUse] 대상에게 [AaCfPcBb]이 있다면, 합 위력 +1\n[WinDuel] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AaCfPcBb], [WinDuel], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AaCfPcBb] = 버틀러의 표식 / Butler's Mark; [WinDuel] = [합 승리시] / [Clash Win]; [Agility] = 신속 / Haste
   EN: [WhenUse] If target has [AaCfPcBb], Clash Power +1\n[WinDuel] Gain 1 [Agility] next turn
   PL: [WhenUse] jeżeli cel ma [AaCfPcBb], Moc Starcia +1\n[WinDuel] zyskuje 1 [Agility] w następnej turze
437. [Umiejętność wroga [817102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 1 [Paralysis] w następnej turze
438. [Umiejętność wroga [817102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] zyskuje 3 [Breath]
439. [Umiejętność wroga [817102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [817102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AaCfPcBb] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AaCfPcBb]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AaCfPcBb] = 버틀러의 표식 / Butler's Mark
   EN: [OnSucceedAttack] Inflict 1 [AaCfPcBb]
   PL: [OnSucceedAttack] nakłada 1 [AaCfPcBb]
441. [Umiejętność wroga [817103] (ulepszenie 1) — nazwa] 응접도 1역식 사냥
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817103].levelList[level=1].name
   limit: do 50 znaków
   EN: Reverse Receiving Arts 1: The Hunt
   PL: Reverse Receiving Arts 1: The Hunt
442. [Umiejętność wroga [817103] (ulepszenie 1) — opis] [WhenUse] 대상에게 [AaCfPcBb]이 있다면, 합 위력 +1\n[WinDuel] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817103].levelList[level=1].desc
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [817103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [817103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Breath]
445. [Umiejętność wroga [817103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność wroga [817103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AaCfPcBb] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [817104] (ulepszenie 1) — nazwa] 불청객 위압
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817104].levelList[level=1].name
   limit: do 40 znaków
   EN: Overwhelm Interloper
   PL: Overwhelm Interloper
448. [Umiejętność wroga [817104] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, 합 위력 +2
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, Clash Power +2
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +2
449. [Umiejętność wroga [817104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [817104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [817104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [817104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 부정적인 효과가 3개 이상이면,이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 3+ negative effects, reuse this Coin (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 3+ negatywnych efektów, używa Monety ponownie (maks. 1 raz)
453. [Umiejętność wroga [817105] (ulepszenie 1) — nazwa] 응접도 제 2식 붕괴
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817105].levelList[level=1].name
   limit: do 40 znaków
   EN: Receiving Arts 2: Collapse
   PL: Receiving Arts 2: Collapse
454. [Umiejętność wroga [817105] (ulepszenie 1) — opis] [WhenUse] 대상에게 [AaCfPcBb]이 있다면, 합 위력 +10
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [AaCfPcBb]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AaCfPcBb] = 버틀러의 표식 / Butler's Mark
   EN: [WhenUse] If target has [AaCfPcBb], Clash Power +10
   PL: [WhenUse] jeżeli cel ma [AaCfPcBb], Moc Starcia +10
455. [Umiejętność wroga [817105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 흐트러짐 바가 없다면, 200만큼 체력 피해를 줌.
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If the target does not have a Stagger Threshold, deal 200 HP damage.
   PL: [OnSucceedAttack] jeżeli cel nie ma Progu Oszołomienia, zadaje 200 obrażeń HP.
456. [Umiejętność wroga [817105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 200만큼 흐트러짐 손상
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 200
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 200
457. [Umiejętność wroga [817106] (ulepszenie 1) — nazwa] 응접도 제 7식 포착
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].name
   limit: do 40 znaków
   EN: Receiving Arts 7: Capture
   PL: Receiving Arts 7: Capture
458. [Umiejętność wroga [817106] (ulepszenie 1) — opis] [StartBattle] [AaCfPcBb]을 가진 적만큼 가중치 증가\n[WhenUse] 메인 타겟보다 속도가 3이상 빠르다면, 참격 내성 약화 2 부여\n[WhenUse] 대상에게 [AaCfPcBb]이 있다면, 합 위력 +8\n[EndBattle] 모든 [AaCfPcBb] 제거
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AaCfPcBb], [WhenUse], [EndBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AaCfPcBb] = 버틀러의 표식 / Butler's Mark; [WhenUse] = [사용시] / [On Use]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [StartBattle] Gain Atk Weight equal to the number of enemies with [AaCfPcBb]\n[WhenUse] If this unit's Speed is faster than the main target's by 3 or more, inflict 2 Slash Resist Down\n[WhenUse] If target has [AaCfPcBb], Clash Power +8\n[EndBattle] All [AaCfPcBb] expires
   PL: [StartBattle] Waga Ataku równa liczbie wrogów z [AaCfPcBb]\n[WhenUse] jeżeli Szybkość jest wyższa od Szybkości głównego celu o 3 lub więcej, nakłada 2 Osłabienia Odporności na Cięcie\n[WhenUse] jeżeli cel ma [AaCfPcBb], Moc Starcia +8\n[EndBattle] wszystkie [AaCfPcBb] znikają
459. [Umiejętność wroga [817106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [817106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [817106] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Umiejętność wroga [817106] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [817106] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [817106] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 부정적인 효과가 4개 이상이면, 피해량의 30%만큼 참격 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817106].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 4+ negative effects, deal 30% of damage dealt as bonus Slash damage
   PL: [OnSucceedAttack] jeżeli cel ma 4+ negatywnych efektów, zadaje dodatkowe obrażenia Cięcia równe 30% zadanych obrażeń
465. [Umiejętność wroga [817107] (ulepszenie 1) — nazwa] 불청객 잡이
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817107].levelList[level=1].name
   limit: do 40 znaków
   EN: Interloper Apprehension
   PL: Interloper Apprehension
466. [Umiejętność wroga [817107] (ulepszenie 1) — opis] [AaCfPcBc]이 있는 대상 우선 공격\n[DefeatDuel] 대상이 [AaCfPcBc]을 가지고 있다면, [AaCfPcBc] 소멸
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817107].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPcBc], [DefeatDuel]
   znaczenie tagów: [AaCfPcBc] = 포박술 / Binding Technique; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [AaCfPcBc]\n[DefeatDuel] If target has [AaCfPcBc] [AaCfPcBc] expires
   PL: priorytet: cele z [AaCfPcBc]\n[DefeatDuel] jeżeli cel ma [AaCfPcBc], [AaCfPcBc] znika
467. [Umiejętność wroga [817107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność wroga [817107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 6 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 6 [DefenseDown] next turn
   PL: [OnSucceedAttack] nakłada 6 [DefenseDown] w następnej turze
469. [Umiejętność wroga [817107] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 속도보다 3이상 빠르면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817107].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit's Speed is faster than the target's by 3 or more, reuse this Coin (1 time max)
   PL: [OnSucceedAttack] jeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, używa Monety ponownie (maks. 1 raz)
470. [Umiejętność wroga [817108] (ulepszenie 1) — nazwa] 응접도 제 3식 결속
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].name
   limit: do 40 znaków
   EN: Receiving Arts 3: Binding
   PL: Receiving Arts 3: Binding
471. [Umiejętność wroga [817108] (ulepszenie 1) — opis] [WhenUse] 대상이 [AaCfPcBc]을 가지고 있다면, 기본 위력 +5\n[WhenUse] 대상이 [AaCfPcBc]을 가지고 있다면, [AaCfPcBc] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AaCfPcBc]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AaCfPcBc] = 포박술 / Binding Technique
   EN: [WhenUse] If target has [AaCfPcBc], Base Power +5\n[WhenUse] If target has [AaCfPcBc], inflict 1 [AaCfPcBc]
   PL: [WhenUse] jeżeli cel ma [AaCfPcBc], Moc Bazowa +5\n[WhenUse] jeżeli cel ma [AaCfPcBc], nakłada 1 [AaCfPcBc]
472. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown] next turn
   PL: [OnSucceedAttack] nakłada 3 [DefenseDown] w następnej turze
478. [Umiejętność wroga [817108] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 부정적인 효과가 3개 이상이면,이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817108].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 3+ negative effects, reuse this coin (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 3+ negatywnych efektów, używa Monety ponownie (maks. 1 raz)
479. [Umiejętność wroga [817109] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817109].levelList[level=1].name
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność wroga [817109] (ulepszenie 1) — opis] [OnSucceedEvade] 정신력 5 회복\n[OnSucceedEvade] 다음 턴만 슬롯 1개 증가. (최대 1번)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817109].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 5 SP\n[OnSucceedEvade] Gain 1 more Slot just for the next Turn. (1 time max)
   PL: [OnSucceedEvade] przywraca 5 SP\n[OnSucceedEvade] zyskuje 1 dodatkowy Slot tylko na następną turę. (maks. 1 raz)
481. [Umiejętność wroga [817110] (ulepszenie 1) — nazwa] 응접도 제 9식 와해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817110].levelList[level=1].name
   limit: do 50 znaków
   EN: Receiving Arts 9: Dissolution
   PL: Receiving Arts 9: Dissolution
482. [Umiejętność wroga [817110] (ulepszenie 1) — opis] [AaCfPcBc]이 있는 대상 우선 공격\n대상에게 [AaCfPcBc]이 있다면, 합 위력 +10\n[AaCfPcBc]이 없는 대상일 경우 이 스킬의 피해량 0이 됨.
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817110].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPcBc]
   znaczenie tagów: [AaCfPcBc] = 포박술 / Binding Technique
   EN: Prioritizes targets with [AaCfPcBc]\nIf target has [AaCfPcBc], Base Power +10\nIf the target does not have [AaCfPcBc], this Skill deals 0 damage.
   PL: priorytet: cele z [AaCfPcBc]\njeżeli cel ma [AaCfPcBc], Moc Bazowa +10\njeżeli cel nie ma [AaCfPcBc], ta Umiejętność zadaje 0 obrażeń.
483. [Umiejętność wroga [817110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 상태로 만듦.
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target.
   PL: [OnSucceedAttack] Oszołomia cel.
484. [Umiejętność wroga [817201] (ulepszenie 1) — nazwa] 파탄난 유리 세계로 얽힌 검
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817201].levelList[level=1].name
   limit: do 50 znaków
   EN: Fused Blade of Ruined Mirror Worlds
   PL: Fused Blade of Ruined Mirror Worlds
485. [Umiejętność wroga [817201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가. [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count. Inflict 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 Licznika [Sinking]. nakłada 3 [Sinking]
486. [Umiejętność wroga [817202] (ulepszenie 1) — nazwa] 내려박기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817202].levelList[level=1].name
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [817202] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Enhancement], [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817202].levelList[level=1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Umiejętność wroga [817202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가. [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 485 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Umiejętność wroga [817202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność wroga [817202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 [Laceration] 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict [Laceration] equal to [Sinking] on target
   PL: [OnSucceedAttack] nakłada [Laceration] na cel w wysokości [Sinking] celu
491. [Umiejętność wroga [817203] (ulepszenie 1) — nazwa] 원한풀기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817203].levelList[level=1].name
   limit: do 40 znaków
   EN: Resolving Grudges
   PL: Resolving Grudges
492. [Umiejętność wroga [817203] (ulepszenie 1) — opis] 대상의 [Sinking]이 5 이상이면, 합 위력 +1\n대상의 [Laceration]이 5 이상이면, 합 위력 +1\n[WinDuel] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817203].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [Laceration], [WinDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 5+ [Sinking], Clash Power +1\nIf target has 5+ [Laceration], Clash Power +1\n[WinDuel] Inflict +3 [Sinking] Count
   PL: jeżeli cel ma 5+ [Sinking], Moc Starcia +1\njeżeli cel ma 5+ [Laceration], Moc Starcia +1\n[WinDuel] nakłada 3 Licznika [Sinking]
493. [Umiejętność wroga [817203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +1
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [817203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność wroga [817203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Umiejętność wroga [817204] (ulepszenie 1) — nazwa] 돌아온 악몽의 복수귀
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817204].levelList[level=1].name
   limit: do 50 znaków
   EN: The Nightmarish Vengeance, Returned
   PL: The Nightmarish Vengeance, Returned
497. [Umiejętność wroga [817204] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse] 대상에게 [AaCfPbBa]이 없으면 합 위력 +10\n[DefeatDuel] 다음 턴에 취약 3 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817204].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [AaCfPbBa], [DefeatDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [AaCfPbBa] = 폭발하는 우울 / Explosive Gloom; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CantChangeTarget]\n[WhenUse] If the target does not have [AaCfPbBa], Clash Power +10\n[DefeatDuel] Gain 3 Fragile next turn
   PL: [CantChangeTarget]\n[WhenUse] jeżeli cel nie ma [AaCfPbBa], Moc Starcia +10\n[DefeatDuel] zyskuje 3 Fragile w następnej turze
498. [Umiejętność wroga [817204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Umiejętność wroga [817204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 8 [Sinking]
   PL: [OnSucceedAttack] nakłada 8 [Sinking]
500. [Umiejętność wroga [817205] (ulepszenie 1) — nazwa] 죽도록 달려라 듀라한이여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817205].levelList[level=1].name
   limit: do 40 znaków
   EN: Ride for Death, Dullahan
   PL: Ride for Death, Dullahan
501. [Umiejętność wroga [817205] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 대상에게 [AaCfPbBb]가 있으면 피해량 -100%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [AaCfPbBb]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [AaCfPbBb] = 폭발하는 질투 / Explosive Envy
   EN: [CantDuel]\n[WhenUse] If target has [AaCfPbBb], deal -100% damage
   PL: [CantDuel]\n[WhenUse] jeżeli cel ma [AaCfPbBb], zadaje -100% obrażeń
502. [Umiejętność wroga [817205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL: [OnSucceedAttack] nakłada 5 [Sinking]
503. [Umiejętność wroga [817205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Sinking]
504. [Umiejętność wroga [817206] (ulepszenie 1) — nazwa] 파탄의 와일드헌트
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817206].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Hunt of Desolation
   PL: Wild Hunt of Desolation
505. [Umiejętność wroga [817206] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 대상에게 [AaCfPbBc]가 있으면 피해량 -100%\n[WhenUse] 생존한 아군 수 1명 당 피해량 +25%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817206].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [AaCfPbBc]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [AaCfPbBc] = 폭발하는 분노 / Explosive Wrath
   EN: [CantDuel]\n[WhenUse] If target has [AaCfPbBc], deal -100% damage\n[WhenUse] Deal +25% damage for every surviving ally
   PL: [CantDuel]\n[WhenUse] jeżeli cel ma [AaCfPbBc], zadaje -100% obrażeń\n[WhenUse] zadaje +25% obrażeń za każdego żyjącego sojusznika
506. [Umiejętność wroga [817207] (ulepszenie 1) — nazwa] 견뎌내기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817207].levelList[level=1].name
   limit: do 40 znaków
   EN: Withstand
   PL: Withstand
507. [Umiejętność wroga [817207] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817207].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Enhancement]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WhenUse] Gain 1 [Enhancement] next turn (once per turn)
   PL: [WhenUse] zyskuje 1 [Enhancement] w następnej turze (1 raz na turę)
508. [Umiejętność wroga [817208] (ulepszenie 1) — nazwa] 슬픔과 절규를 내뿜는 유리조각
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817208].levelList[level=1].name
   limit: do 50 znaków
   EN: Glass Shard of Wailing Sorrow
   PL: Glass Shard of Wailing Sorrow
509. [Umiejętność wroga [817208] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817208].levelList[level=1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Umiejętność wroga [817208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 [Sinking]
511. [Umiejętność wroga [817208] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817208].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność wroga [817301] (ulepszenie 1) — nazwa] 대검 베기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817301].levelList[level=1].name
   limit: do 40 znaków
   EN: Greatsword Rend
   PL: Greatsword Rend
513. [Umiejętność wroga [817301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가, [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count and 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 Licznika [Sinking] i 3 [Sinking]
514. [Umiejętność wroga [817302] (ulepszenie 1) — nazwa] 내려박기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817302].levelList[level=1].name
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność wroga [817302] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Enhancement], [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817302].levelList[level=1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność wroga [817302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가, [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność wroga [817302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność wroga [817302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 [Laceration] 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Umiejętność wroga [817303] (ulepszenie 1) — nazwa] 워더링하이츠여. 나의 부름에 응하도록
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817303].levelList[level=1].name
   limit: do 50 znaków
   EN: Heed My Call, Wuthering Heights
   PL: Heed My Call, Wuthering Heights
520. [Umiejętność wroga [817303] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 다음 턴에 와일드 헌트 유닛 1명 생성
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [TabExplain]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\n[WhenUse] Generate 1 Wild Hunt[TabExplain] unit next turn
   PL: [CantDuel]\n[WhenUse] generuje 1 jednostkę Wild Hunt[TabExplain] w następnej turze
521. [Umiejętność wroga [817304] (ulepszenie 1) — nazwa] 네 놈도 이 관에 담아주지
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817304].levelList[level=1].name
   limit: do 50 znaków
   EN: You’ll Get Shoved In This Coffin Too
   PL: You’ll Get Shoved In This Coffin Too
522. [Umiejętność wroga [817304] (ulepszenie 1) — opis] [CantDuel]\n[StartBattle] 이번 턴에 [VibrationExplosion], 흐트러짐 손상 효과로 받는 흐트러짐 피해 + 100%\n[WhenUse] 다음 턴에 자신을 포함한 모든 아군에게 [Enhancement] 3, [AttackDmgUp] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817304].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [VibrationExplosion], [WhenUse], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantDuel]\n[StartBattle] +100% to the amount of Stagger Threshold raised from [VibrationExplosion] and any other Stagger Threshold raising effects\n[WhenUse] Apply 3 [Enhancement] and 3 [AttackDmgUp] to all allies, including this unit next turn
   PL: [CantDuel]\n[StartBattle] kwota podnoszenia Progu Oszołomienia przez [VibrationExplosion] i inne efekty podnoszące Próg Oszołomienia rośnie o 100%\n[WhenUse] nakłada 3 [Enhancement] i 3 [AttackDmgUp] wszystkim sojusznikom (łącznie z tą jednostką) w następnej turze
523. [Umiejętność wroga [817305] (ulepszenie 1) — nazwa] 히스클리프들의 목을 벤다
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817305].levelList[level=1].name
   limit: do 40 znaków
   EN: Behead Heathcliffs
   PL: Behead Heathcliffs
524. [Umiejętność wroga [817305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [817305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [817306] (ulepszenie 1) — nazwa] 빈 관의 철퇴
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817306].levelList[level=1].name
   limit: do 40 znaków
   EN: Hollow Coffin Mace
   PL: Hollow Coffin Mace
527. [Umiejętność wroga [817306] (ulepszenie 1) — opis] 대상의 [Sinking]이 5 이상이면, 합 위력 +1\n대상의 [Laceration]이 5 이상이면, 합 위력 +1\n[WinDuel] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817306].levelList[level=1].desc
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność wroga [817306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [817307] (ulepszenie 1) — nazwa] 죽도록 달려라 듀라한이여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817307].levelList[level=1].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [817307] (ulepszenie 1) — moneta 2, efekt 1 — opis] [Sinking] 5 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817307].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict 5 [Sinking]
   PL: nakłada 5 [Sinking]
531. [Umiejętność wroga [817307] (ulepszenie 1) — moneta 3, efekt 1 — opis] [Sinking] 횟수 5 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817307].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict +5 [Sinking] Count
   PL: nakłada 5 Licznika [Sinking]
532. [Umiejętność wroga [817308] (ulepszenie 1) — nazwa] 견뎌내기
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817308].levelList[level=1].name
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność wroga [817308] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817308].levelList[level=1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Umiejętność wroga [817309] (ulepszenie 1) — nazwa] 마왕이 다녀가면 슬픔과 절규만이 남는다.
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817309].levelList[level=1].name
   limit: do 60 znaków
   EN: Sorrow and Lament In The Erlking's Wake.
   PL: Sorrow and Lament In The Erlking's Wake.
535. [Umiejętność wroga [817309] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4, [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817309].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Sinking] i 4 [Laceration]
536. [Umiejętność wroga [817309] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817309].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Sinking] i 2 Licznika [Laceration]
537. [Umiejętność wroga [817309] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4, [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817309].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 535 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność wroga [817309] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817309].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Umiejętność wroga [817310] (ulepszenie 1) — nazwa] 모든 히스클리프는 죽어야만 한다...
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817310].levelList[level=1].name
   limit: do 40 znaków
   EN: Every Heathcliff Must Die...
   PL: Every Heathcliff Must Die...
540. [Umiejętność wroga [817310] (ulepszenie 1) — opis] [CantChangeTarget]\n[CantDuel]\n이번 턴동안 흐트러짐 상태가 되지 않음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817310].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [CantDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantChangeTarget]\n[CantDuel]\nDoes not get Staggered this turn
   PL: [CantChangeTarget]\n[CantDuel]\nnie przechodzi w Oszołamienie w tej turze
541. [Umiejętność wroga [817310] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력의 100%만큼 피해를 줌
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817310].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal damage equal to 100% of the target's max HP
   PL: [OnSucceedAttack] zadaje obrażenia równe 100% Maks. HP celu
542. [Umiejętność wroga [817401] (ulepszenie 1) — nazwa] 소용 없어
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817401].levelList[level=1].name
   limit: do 40 znaków
   EN: It's All Pointless
   PL: It's All Pointless
543. [Umiejętność wroga [817402] (ulepszenie 1) — nazwa] 그가 불행하지 않은 세상을 위해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817402].levelList[level=1].name
   limit: do 50 znaków
   EN: For a World Without His Suffering
   PL: For a World Without His Suffering
544. [Umiejętność wroga [817402] (ulepszenie 1) — opis] [CantDuel]\n[StartBattle] 자신을 제외한 모든 아군에게 [Vulnerable] 2, [Enhancement] 2 부여\n[StartBattle] 다음 턴에 [Binding], [AttackDmgUp] 5 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817402].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [Vulnerable], [Enhancement], [Binding], [AttackDmgUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [Vulnerable] = 취약 / Fragile; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Binding] = 속박 / Bind; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantDuel]\n[StartBattle] Apply 2 [Vulnerable] and 2, [Enhancement] to all other allies\n[StartBattle] Gain 5 [Binding] and 5 [AttackDmgUp] next turn
   PL: [CantDuel]\n[StartBattle] nakłada 2 [Vulnerable] i 2 [Enhancement] wszystkim pozostałym sojusznikom\n[StartBattle] zyskuje 5 [Binding] i 5 [AttackDmgUp] w następnej turze
545. [Umiejętność wroga [817403] (ulepszenie 1) — nazwa] 모든 캐서린은 죽어야해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817403].levelList[level=1].name
   limit: do 40 znaków
   EN: Every Catherine Must Die
   PL: Every Catherine Must Die
546. [Umiejętność wroga [817403] (ulepszenie 1) — opis] [CantDuel]\n모든 손의 체력이 1이면 피해량이 0이 됨\n[StartBattle] 자신을 제외한 모든 아군에게 [Vulnerable] 2, [Enhancement] 2 부여\n[EndSkill] [AaCfPcBn] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817403].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [Vulnerable], [Enhancement], [EndSkill], [AaCfPcBn]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [Vulnerable] = 취약 / Fragile; [Enhancement] = 공격 위력 증가 / Attack Power Up; [EndSkill] = [공격 종료시] / [Attack End]; [AaCfPcBn] = 찢어지는 마음 / Breaking Heart
   EN: [CantDuel]\nIf all Hands' HP are at 1, deal 0 damage\n[StartBattle] All other allies gain 2 [Vulnerable] and 2 [Enhancement]\n[EndSkill] Gain 1 [AaCfPcBn]
   PL: [CantDuel]\njeżeli HP wszystkich Rąk wynosi 1, zadaje 0 obrażeń\n[StartBattle] nakłada 2 [Vulnerable] i 2 [Enhancement] wszystkim pozostałym sojusznikom\n[EndSkill] zyskuje 1 [AaCfPcBn]
547. [Umiejętność wroga [817403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AaCfPcBn] 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AaCfPcBn]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AaCfPcBn] = 찢어지는 마음 / Breaking Heart
   EN: [OnSucceedAttack] Inflict [AaCfPcBn]
   PL: [OnSucceedAttack] nakłada [AaCfPcBn]
548. [Umiejętność wroga [817404] (ulepszenie 1) — nazwa] 찢어지는 마음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817404].levelList[level=1].name
   limit: do 40 znaków
   EN: Breaking Heart
   PL: Breaking Heart
549. [Umiejętność wroga [817404] (ulepszenie 1) — opis] [EndSkill] [AaCfPcBn] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [AaCfPcBn]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [AaCfPcBn] = 찢어지는 마음 / Breaking Heart
   EN: [EndSkill] Gain 1 [AaCfPcBn]
   PL: [EndSkill] zyskuje 1 [AaCfPcBn]
550. [Umiejętność wroga [817404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 15%만큼 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal damage equal to 15% of max HP
   PL: [OnSucceedAttack] zadaje obrażenia równe 15% Maks. HP
551. [Umiejętność wroga [817404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [AaCfPcBn] 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność wroga [819201] (ulepszenie 1) — nazwa] 비통한 눈물
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819201].levelList[level=1].name
   limit: do 40 znaków
   EN: Tears of Sorrow
   PL: Tears of Sorrow
553. [Umiejętność wroga [819202] (ulepszenie 1) — nazwa] 비극의 손아귀
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819202].levelList[level=1].name
   limit: do 40 znaków
   EN: Clutch of Tragedy
   PL: Clutch of Tragedy
554. [Umiejętność wroga [819202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [819202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [819203] (ulepszenie 1) — nazwa] 절망의 손아귀
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819203].levelList[level=1].name
   limit: do 40 znaków
   EN: Clutch of Despair
   PL: Clutch of Despair
557. [Umiejętność wroga [819203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność wroga [819203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność wroga [819204] (ulepszenie 1) — nazwa] 무의미한 발악
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819204].levelList[level=1].name
   limit: do 40 znaków
   EN: Meaningless Writhing
   PL: Meaningless Writhing
560. [Umiejętność wroga [819204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [819205] (ulepszenie 1) — nazwa] 남은 것은 고통 뿐...
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819205].levelList[level=1].name
   limit: do 50 znaków
   EN: Misery is All That Remains...
   PL: Misery is All That Remains...
562. [Umiejętność wroga [819205] (ulepszenie 1) — opis] [DefeatDuel] [AaCfPcBn] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [AaCfPcBn]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [AaCfPcBn] = 찢어지는 마음 / Breaking Heart
   EN: [DefeatDuel] Gain 1 [AaCfPcBn]
   PL: [DefeatDuel] zyskuje 1 [AaCfPcBn]
563. [Umiejętność wroga [819205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 15%만큼 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność wroga [819206] (ulepszenie 1) — nazwa] 잡히지 않는 영혼
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=819206].levelList[level=1].name
   limit: do 40 znaków
   EN: Soul Out of Reach
   PL: Soul Out of Reach
565. [Umiejętność wroga [817001] (ulepszenie 1) — nazwa] 치워...
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817001].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Remo...
   PL: I'll Remo...
566. [Umiejętność wroga [817001] (ulepszenie 1) — opis] 이 공격 스킬이 입힌 피해량의 10%만큼 본체 및 부위 체력 회복
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817001].levelList[level=1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność wroga [817001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność wroga [817001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność wroga [817001] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność wroga [817002] (ulepszenie 1) — nazwa] ...놈
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817002].levelList[level=1].name
   limit: do 40 znaków
   EN: ... Bastard
   PL: ... Bastard
571. [Umiejętność wroga [817002] (ulepszenie 1) — opis] 대상보다 속도가 빠르다면, 합 위력+2
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817002].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's, Clash Power +2
   PL: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +2
572. [Umiejętność wroga [817002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [817002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Umiejętność wroga [817002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상보다 속도가 3이상 빠르다면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [817003] (ulepszenie 1) — nazwa] 내 집...
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].name
   limit: do 40 znaków
   EN: This is My...
   PL: This is My...
576. [Umiejętność wroga [817003] (ulepszenie 1) — opis] 체력이 가장 낮은 대상 우선 공격\n[WhenUse] 대상의 현재 체력 비율이 70% 미만이면, 합 위력 +2
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność wroga [817003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [817003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność wroga [817003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność wroga [817003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [817003] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 20이상이면, 피해량 +100%
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [817003] (ulepszenie 1) — moneta 4, efekt 2 — opis] [EnemyKill] 이 스킬 재사용 (최대 1)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817003].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [817004] (ulepszenie 1) — nazwa] 은…
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817004].levelList[level=1].name
   limit: do 40 znaków
   EN: Get...
   PL: Get...
584. [Umiejętność wroga [817004] (ulepszenie 1) — opis] 히스클리프 우선 공격\n[WhenUse] 속도가 가장 낮은 적일 경우, 기본 위력 +3\n[WhenUse] 다음 턴에 [AaCfPbBe], [Vulnerable] 2, [Paralysis] 3, [Binding] 5 부여
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817004].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AaCfPbBe], [Vulnerable], [Paralysis], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AaCfPbBe] = 사냥감 표시 / Marked Prey; [Vulnerable] = 취약 / Fragile; [Paralysis] = 마비 / Paralyze; [Binding] = 속박 / Bind
   EN: Prioritizes Heathcliff\n[WhenUse] If the target is the enemy with the slowest Speed, Base Power +3\n[WhenUse] Inflict [AaCfPbBe], 2 [Vulnerable], 3 [Paralysis], and 5 [Binding]
   PL: priorytet: Heathcliff\n[WhenUse] jeżeli cel jest wrogiem o najniższej Szybkości, Moc Bazowa +3\n[WhenUse] nakłada [AaCfPbBe], 2 [Vulnerable], 3 [Paralysis] i 5 [Binding] w następnej turze
585. [Umiejętność wroga [817004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [817004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność wroga [817005] (ulepszenie 1) — nazwa] 줘…!!
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].name
   limit: do 40 znaków
   EN: Back...!!
   PL: Back...!!
588. [Umiejętność wroga [817005] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność wroga [817005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 2 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [817005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 2 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [817005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 2 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [817005] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [817005] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5이상이면, 피해량의 50%만큼 체력 회복
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817005].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [817006] (ulepszenie 1) — nazwa] 끼가…
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817006].levelList[level=1].name
   limit: do 40 znaków
   EN: ttle...
   PL: ttle...
595. [Umiejętność wroga [817006] (ulepszenie 1) — opis] [AaCfPbBe]을 가지고 있는 대상 우선 공격\n대상의 속도가 자신보다 3 이상 낮다면, 이 스킬 재사용 (최대 1)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817006].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPbBe]
   znaczenie tagów: [AaCfPbBe] = 사냥감 표시 / Marked Prey
   EN: Prioritizes targets with [AaCfPbBe]\nIf this unit's Speed is faster than the target by 3 or more, reuse this Skill (1 time max)
   PL: priorytet: cele z [AaCfPbBe]\njeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, używa ponownie tę Umiejętność (1 raz)
596. [Umiejętność wroga [817006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 본체 및 부위 체력 회복
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność wroga [817006] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 본체 및 부위 체력 회복
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817006].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [817007] (ulepszenie 1) — nazwa] 가...
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817007].levelList[level=1].name
   limit: do 40 znaków
   EN: Gua...
   PL: Gua...
599. [Umiejętność wroga [817007] (ulepszenie 1) — opis] 턴 종료시 보호막 체력이 남아있다면, 다음 턴에 [Protection] 4 얻음
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817007].levelList[level=1].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [817008] (ulepszenie 1) — nazwa] ...피
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817008].levelList[level=1].name
   limit: do 40 znaków
   EN: ... de
   PL: ... de
601. [Umiejętność wroga [817008] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Binding] 1 부여 (최대 2)
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817008].levelList[level=1].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [817009] (ulepszenie 1) — nazwa] 여긴...!
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].name
   limit: do 40 znaków
   EN: This Is...!
   PL: This Is...!
603. [Umiejętność wroga [817009] (ulepszenie 1) — opis] 자신의 속도가 대상보다 높으면 코인 위력 +1
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność wroga [817009] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [817009] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność wroga [817009] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [817009] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 30%만큼 타격 피해
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [817009] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10이상이면, 피해량의 70%만큼 체력 회복
   źródło: Skills_Abnormality-a1c6p3.json :: dataList[id=817009].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c6p3] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c6p3
- grupa rozdziału/trybu: `a1c6p3` · plik: `Skills_Enemy-a1c6p3.json`

609. [Umiejętność wroga [9013601] (ulepszenie 1) — nazwa] ...크
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013601].levelList[level=1].name
   limit: do 40 znaków
   EN: ...nocking
   PL: ...nocking
610. [Umiejętność wroga [9013601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 5이상이면, [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has 5+ [Sinking], inflict 1 [AttackDown]
   PL: [WhenUse] jeżeli cel ma 5+ [Sinking], nakłada 1 [AttackDown]
611. [Umiejętność wroga [9013601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] nakłada 4 [Sinking]
612. [Umiejętność wroga [9013601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [9013601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [9013601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [9013602] (ulepszenie 1) — nazwa] ...시간
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013602].levelList[level=1].name
   limit: do 40 znaków
   EN: ...to Clean
   PL: ...to Clean
616. [Umiejętność wroga [9013602] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 10이하라면, [AttackDown] 2 부여\n[WinDuel] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013602].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AttackDown], [WinDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [WinDuel] = [합 승리시] / [Clash Win]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] If the target is at 10 or less SP, inflict 2 [AttackDown]\n[WinDuel] Inflict 1 [Vulnerable]
   PL: [WhenUse] jeżeli SP celu wynosi 10 lub mniej, nakłada 2 [AttackDown]\n[WinDuel] nakłada 1 [Vulnerable]
617. [Umiejętność wroga [9013602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [PlusCoinValueDown] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PlusCoinValueDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop
   EN: [OnSucceedAttack] Inflict 1 [PlusCoinValueDown] next turn
   PL: [OnSucceedAttack] nakłada 1 [PlusCoinValueDown] w następnej turze
618. [Umiejętność wroga [9013602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [9013602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable] w następnej turze
620. [Umiejętność wroga [9013603] (ulepszenie 1) — nazwa] 대로...!
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].name
   limit: do 40 znaków
   EN: ...mmands...!
   PL: ...mmands...!
621. [Umiejętność wroga [9013603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 3당 기본 위력 +1 (최대 3)\n[WinDuel] 모든 아군 정신력 5 회복
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Base Power +1 for every 3 [Sinking] on target (max 3)\n[WinDuel] All allies heal 5 SP
   PL: [WhenUse] Moc Bazowa +1 za każde 3 [Sinking] celu (maks. 3)\n[WinDuel] wszyscy sojusznicy przywracają 5 SP
622. [Umiejętność wroga [9013603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [9013603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttackHead] nakłada 2 Licznika [Sinking]
624. [Umiejętność wroga [9013603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [9013603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [9013603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność wroga [9013603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [9013604] (ulepszenie 1) — nazwa] 먼지...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].name
   limit: do 40 znaków
   EN: ...of Dust
   PL: ...of Dust
629. [Umiejętność wroga [9013604] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당, 기본 위력 +1 (최대 3)\n[WhenUse] 대상의 [Sinking] 6당, 피해량 +10% (최대 30%)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Base Power +1 for every 6 [Sinking] on target (max 3)\n[WhenUse] Deal +10% damage for every 6 [Sinking] Count on target (max 30%)
   PL: [WhenUse] Moc Bazowa +1 za każde 6 [Sinking] celu (maks. 3)\n[WhenUse] zadaje +10% obrażeń za każde 6 Licznika [Sinking] celu (maks. 30%)
630. [Umiejętność wroga [9013604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 추가 피해 입힘. [Sinking] 횟수 1 감소
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity bonus damage equal to [Sinking] on target. Reduce [Sinking] Count on target by 1
   PL: [OnSucceedAttack] zadaje celowi dodatkowe obrażenia Posępności równe [Sinking] celu. Zmniejsza Licznik [Sinking] celu o 1
631. [Umiejętność wroga [9013604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 추가 피해 입힘. [Sinking] 횟수 1 감소
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [9013604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 추가 피해 입힘
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity bonus damage equal to [Sinking] on target.
   PL: [OnSucceedAttack] zadaje celowi dodatkowe obrażenia Posępności równe [Sinking] celu.
633. [Umiejętność wroga [9013604] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność wroga [9013604] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Sinking] 횟수가 3이상이면, 이 코인 재사용. (최대 2회)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013604].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has 3+ [Sinking] Count, Reuse this Coin (twice)
   PL: [OnSucceedAttack] jeżeli cel ma 3+ Licznika [Sinking], używa Monety ponownie (do 2 razy)
635. [Umiejętność wroga [9013605] (ulepszenie 1) — nazwa] 쥐새끼...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013605].levelList[level=1].name
   limit: do 40 znaków
   EN: Slipp...
   PL: Slipp...
636. [Umiejętność wroga [9013605] (ulepszenie 1) — opis] 턴 종료 시 보호막이 남아있다면, 50만큼 흐트러짐 회복
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013605].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this unit has remaining Shield HP at Turn End, lower Stagger threshold by 50
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, obniża Próg Oszołomienia o 50
637. [Umiejętność wroga [9013701] (ulepszenie 1) — nazwa] 잡배놈...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013701].levelList[level=1].name
   limit: do 40 znaków
   EN: Damn Pl...
   PL: Damn Pl...
638. [Umiejętność wroga [9013701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [9013701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [9013702] (ulepszenie 1) — nazwa] 치워...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013702].levelList[level=1].name
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [9013702] (ulepszenie 1) — opis] [WinDuel] 기본 위력 +1
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013702].levelList[level=1].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność wroga [9013702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [AttackDown]이 있다면, 피해량 20%만큼 타격 피해 입힘
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [9013702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [AttackDown]이 있다면, 피해량 20%만큼 타격 피해 입힘
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [9013703] (ulepszenie 1) — nazwa] 단추...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013703].levelList[level=1].name
   limit: do 40 znaków
   EN: Make Things...
   PL: Make Things...
645. [Umiejętność wroga [9013703] (ulepszenie 1) — opis] [WinDuel] 대상의 [AttackDown]가 2 이상이면, 기본 위력 +1\n[WhenUse] 대상에게 [DefenseDown]이 있다면, 피해량 30%만큼 타격 피해 입힘
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013703].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [AttackDown], [WhenUse], [DefenseDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WinDuel] If target has 2+ [AttackDown], Base Power +1\n[WhenUse] If target has [DefenseDown], deal 30% of damage dealt as bonus Blunt damage
   PL: [WinDuel] jeżeli cel ma 2+ [AttackDown], Moc Bazowa +1\n[WhenUse] jeżeli cel ma [DefenseDown], zadaje dodatkowe obrażenia Uderzeniem równe 30% zadanych obrażeń
646. [Umiejętność wroga [9013703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność wroga [9013703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność wroga [9013703] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 4 회복
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013703].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [9013704] (ulepszenie 1) — nazwa] ...주마
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].name
   limit: do 40 znaków
   EN: ... ove You
   PL: ... ove You
650. [Umiejętność wroga [9013704] (ulepszenie 1) — opis] 부정적인 효과가 가장 많은 대상 우선 공격\n[WinDuel] 대상의 [DefenseDown] 3당 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefenseDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Prioritizes targets with the most negative effects\n[WinDuel] Coin Power +1 for every 3 [DefenseDown] on target (max 3)
   PL: priorytet: cele z największą liczbą negatywnych efektów\n[WinDuel] Moc Monety +1 za każde 3 [DefenseDown] celu (maks. 3)
651. [Umiejętność wroga [9013704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność wroga [9013704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [9013704] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Umiejętność wroga [9013704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [AttackDown] 2당 +30% (최대 120%)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [9013704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 대상의 부정적인 효과가 3개 이상이면, 이 코인 재사용 (1회)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 3+ negative effects, reuse this coin (once)
   PL: [OnSucceedAttackHead] jeżeli cel ma 3+ negatywnych efektów, używa Monety ponownie (1 raz)
656. [Umiejętność wroga [9013705] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013705].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Umiejętność wroga [9013705] (ulepszenie 1) — opis] [StartBattle] 살아있는 아군 수당 보호막 체력 20을 추가로 얻음
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 20 additional Shield HP for every surviving ally
   PL: [StartBattle] zyskuje dodatkowo 20 HP Tarczy za każdego żyjącego sojusznika
658. [Umiejętność wroga [9013801] (ulepszenie 1) — nazwa] 마르...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013801].levelList[level=1].name
   limit: do 40 znaków
   EN: Marc...
   PL: Marc...
659. [Umiejętność wroga [9013801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [9013802] (ulepszenie 1) — nazwa] ...트
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013802].levelList[level=1].name
   limit: do 40 znaków
   EN: ...te
   PL: ...te
661. [Umiejętność wroga [9013802] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 2개 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has 2+ negative effects, Base Power +1
   PL: [WhenUse] jeżeli cel ma 2+ negatywnych efektów, Moc Bazowa +1
662. [Umiejętność wroga [9013802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 3 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność wroga [9013803] (ulepszenie 1) — nazwa] 플...쉬
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013803].levelList[level=1].name
   limit: do 40 znaków
   EN: Fl...he
   PL: Fl...he
664. [Umiejętność wroga [9013803] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 4개 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has 4+ negative effects, Coin Power +1
   PL: [WhenUse] jeżeli cel ma 4+ negatywnych efektów, Moc Monety +1
665. [Umiejętność wroga [9013803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Umiejętność wroga [9013803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność wroga [9013803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność wroga [9013804] (ulepszenie 1) — nazwa] 꾸...와
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013804].levelList[level=1].name
   limit: do 40 znaków
   EN: Cou...oit
   PL: Cou...oit
669. [Umiejętność wroga [9013804] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 기본 위력 +2\n[WhenUse] 대상의 부정적인 효과가 5개 이상이면, 피해량 +30%
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013804].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has 5+ negative effects, Base Power +2\n[WhenUse] If target has 5+ negative effects, deal +30% damage
   PL: [WhenUse] jeżeli cel ma 5+ negatywnych efektów, Moc Bazowa +2\n[WhenUse] jeżeli cel ma 5+ negatywnych efektów, zadaje +30% obrażeń
670. [Umiejętność wroga [9013804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable]
671. [Umiejętność wroga [9013804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 619 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [9013804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 부정적인 효과가 5개 이상이면, 이 코인 재사용 (2회)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ negative effects, reuse this coin (2 times max)
   PL: [OnSucceedAttack] jeżeli cel ma 5+ negatywnych efektów, używa Monety ponownie (do 2 razy)
673. [Umiejętność wroga [9013804] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 해제 가능한 부정적인 효과 무작위 하나 제거
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013804].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove 1 random removable negative effect applied on target
   PL: [OnSucceedAttack] usuwa 1 losowy negatywny efekt celu, który można usunąć
674. [Umiejętność wroga [9013805] (ulepszenie 1) — nazwa] ...
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013805].levelList[level=1].name
   limit: do 40 znaków
   EN: ...
   PL: ...
675. [Umiejętność wroga [9013805] (ulepszenie 1) — opis] [OnSucceedEvade] 정신력 5 회복 (최대 2회)
   źródło: Skills_Enemy-a1c6p3.json :: dataList[id=9013805].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 5 SP (2 times max)
   PL: [OnSucceedEvade] przywraca 5 SP (do 2 razy)

## [a1c6p3] Pasywka wroga: Passives_Abnormality-a1c6p3
- plik gry: `Passives_Abnormality-a1c6p3.json`

676. [[a1c6p3] Pasywka wroga [816101] — nazwa] 죄악 내성
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816101].name
   limit: do 40 znaków
   EN: Sin Nullification
   PL: Sin Nullification
677. [[a1c6p3] Pasywka wroga [816101] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면 자신이 받는 [Combustion] 피해 80% 감소.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Unless this unit is Staggered or Part Broken, take 80% less [Combustion] damage.
   PL: o ile ta jednostka nie jest w Oszołamieniu i nie ma zniszczonej Części, otrzymuje o 80% mniej obrażeń [Combustion].
678. [[a1c6p3] Pasywka wroga [816102] — nazwa] 화염 전이
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816102].name
   limit: do 40 znaków
   EN: Proliferating Flame
   PL: Proliferating Flame
679. [[a1c6p3] Pasywka wroga [816102] — opis] 대상에게 [Combustion]이 있을 때, 적중시 대상의 [Combustion] 절반만큼 [Combustion]을 조작 패널 양옆 인격에게 부여함.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816102].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If the target has [Combustion]: On Hit, spread half of [Combustion] on target to 2 units adjacent to the target on the Dashboard.
   PL: gdy cel ma [Combustion], przy trafieniu rozprzestrzenia połowę [Combustion] celu na 2 jednostki przyległe do celu na Dashboardzie.
680. [[a1c6p3] Pasywka wroga [816601] — nazwa] 뒤엉킨 사냥
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816601].name
   limit: do 40 znaków
   EN: Chaotic Hunt
   PL: Chaotic Hunt
681. [[a1c6p3] Pasywka wroga [816601] — opis] 합 승리시, 다음 합에서 합 위력 -1 (최대 2)\n합 패배시, 다음 합에서 합 위력 +1 (최대 2)
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816601].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Win: Clash Power -1 for the next Clash (max 2)\nClash Lose: Clash Power +1 for the next Clash (max 2)
   PL: wygrana w Starciu: Moc Starcia -1 w następnym Starciu (maks. 2)\nprzegrana w Starciu: Moc Starcia +1 w następnym Starciu (maks. 2)
682. [[a1c6p3] Pasywka wroga [816602] — nazwa] 포기한 인간성
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816602].name
   limit: do 40 znaków
   EN: Humanity Abandoned
   PL: Humanity Abandoned
683. [[a1c6p3] Pasywka wroga [816602] — opis] 턴 시작시, [AttackDmgUp] 2 얻음.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: gain 2 [AttackDmgUp].
   PL: Początek tury: zyskuje 2 [AttackDmgUp].
684. [[a1c6p3] Pasywka wroga [816603] — nazwa] 자루
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816603].name
   limit: do 40 znaków
   EN: Sack
   PL: Sack
685. [[a1c6p3] Pasywka wroga [816603] — opis] - 사슬이 있는 동안에는 모든 부위가 [Enhancement]를 1, [AttackDmgUp]를 2 얻음\n- 사슬이 파괴시 이번 스테이지동안 턴 종료시 다음 턴에 [Binding]을 2 얻고 물리 내성이 0.7 증가함
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816603].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [AttackDmgUp], [Binding]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [Binding] = 속박 / Bind
   EN: - When this unit has the Chain, all Parts gain 1 [Enhancement] and 2 [AttackDmgUp]\n- When the Chain is broken, starting next turn, gain 2 [Binding] and +0.7 to all physical resistances until the end of this Encounter
   PL: - gdy ta jednostka ma Chain, wszystkie Części zyskują 1 [Enhancement] i 2 [AttackDmgUp]\n- gdy Chain zostaje zniszczony, od następnej tury na koniec tury zyskuje 2 [Binding], a wszystkie odporności fizyczne rosną o 0.7 do końca tej walki
686. [[a1c6p3] Pasywka wroga [816604] — nazwa] 르쌍티망
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816604].name
   limit: do 40 znaków
   EN: Ressentiment
   PL: Ressentiment
687. [[a1c6p3] Pasywka wroga [816604] — opis] 자신의 체력이 35%이하일 때, 대상이 자신보다 현재 체력 비율이 높으면 합 위력 +2
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816604].desc
   limit: do 140 znaków
   EN: When this unit has 35% or less HP: If the target has a higher HP percentage than this unit, Clash Power +2
   PL: gdy HP tej jednostki wynosi 35% lub mniej: jeżeli procent aktualnego HP celu jest wyższy, Moc Starcia +2
688. [[a1c6p3] Pasywka wroga [816605] — nazwa] 악에 받친
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816605].name
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [[a1c6p3] Pasywka wroga [816605] — opis] 자신의 현재 체력 비율이 30%이하가 되었다면\n- 타격 스킬의 피해량 +20%\n- 턴이 지남에 따라 [Enhancement] 1, [Vulnerable] 2씩 추가로 얻음. (최대 3회)
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816605].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: If this Unit's current HP percentage is 30% or less:\n- Blunt Skills Deal +20% damage\n- Gain 1 [Enhancement] and 2 [Vulnerable] with every turn that passes. (3 times max)
   PL: gdy procent aktualnego HP tej jednostki wynosi 30% lub mniej:\n- Umiejętności Uderzeniem zadają +20% obrażeń\n- z każdą upływającą turą zyskuje dodatkowo 1 [Enhancement] i 2 [Vulnerable]. (do 3 razy)
690. [[a1c6p3] Pasywka wroga [816606] — nazwa] 지옥의 사냥개
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816606].name
   limit: do 40 znaków
   EN: Infernal Hound
   PL: Infernal Hound
691. [[a1c6p3] Pasywka wroga [816606] — opis] 사슬 파괴시, 무작위 적에게 [AaCfPcBg] 부여.\n다음 턴부터 [AaCfPcBg]을 지닌 인격 우선 공격함.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816606].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPcBg]
   znaczenie tagów: [AaCfPcBg] = 분노의 대상 / Subject of Wrath
   EN: When the Chain is broken, inflict [AaCfPcBg] to a random enemy.\nStarting next turn, prioritize target with [AaCfPcBg].
   PL: gdy Chain zostaje zniszczony, nakłada [AaCfPcBg] losowemu wrogowi.\nod następnej tury priorytet: Identyfikacje z [AaCfPcBg].
692. [[a1c6p3] Pasywka wroga [817101] — nazwa] 우위
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817101].name
   limit: do 40 znaków
   EN: Superiority
   PL: Superiority
693. [[a1c6p3] Pasywka wroga [817101] — opis] 합 승리시 대상보다 속도가 빠르다면, 정신력 3 회복
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817101].desc
   limit: do 120 znaków
   EN: Clash Win: If this unit's Speed is faster than the target's, heal 3 SP
   PL: wygrana w Starciu: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, przywraca 3 SP
694. [[a1c6p3] Pasywka wroga [817102] — nazwa] 불속지객
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817102].name
   limit: do 40 znaków
   EN: The Uninvited
   PL: The Uninvited
695. [[a1c6p3] Pasywka wroga [817102] — opis] 흐트러짐 상태의 적이 있다면, 공격 스킬로 대상을 우선 지정함.\n흐트러짐 상태의 적 적중시, 피해량 +20%
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817102].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If there are Staggered enemies, this unit prioritizes Staggered targets with its Attack Skills\nDeal +20% damage to Staggered enemies On Hit
   PL: jeżeli istnieją wrogowie w Oszołamieniu, priorytet: cele w Oszołamieniu dla Umiejętności ataku\nprzy trafieniu w wroga w Oszołamieniu zadaje +20% obrażeń
696. [[a1c6p3] Pasywka wroga [817103] — nazwa] 응접도 제 9식 결박
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817103].name
   limit: do 40 znaków
   EN: Receiving Arts 9: Binding
   PL: Receiving Arts 9: Binding
697. [[a1c6p3] Pasywka wroga [817103] — opis] 패턴이 변경되고부터 전투 종료시 다음 턴에 [AaCfPcBc]이 없는 무작위 인격 한명에게 다음 턴에 [AaCfPcBc] 부여
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817103].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [AaCfPcBc]
   znaczenie tagów: [AaCfPcBc] = 포박술 / Binding Technique
   EN: After this unit gains a new pattern, and after Combat End, inflict [AaCfPcBc] to a random Identity without [AaCfPcBc] next turn
   PL: po przybraniu nowego wzorca i po zakończeniu walki nakłada [AaCfPcBc] na 1 losową Identyfikację bez [AaCfPcBc] w następnej turze
698. [[a1c6p3] Pasywka wroga [817104] — nazwa] 포박 해제
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817104].name
   limit: do 40 znaków
   EN: Release From Binds
   PL: Release From Binds
699. [[a1c6p3] Pasywka wroga [817104] — opis] 흐트러짐 상태가 되면, 수치가 2 이하인 모든 [AaCfPcBc] 제거
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817104].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AaCfPcBc]
   znaczenie tagów: [AaCfPcBc] = 포박술 / Binding Technique
   EN: All [AaCfPcBc] less than or equal to 2 expires when this unit is Staggered
   PL: gdy ta jednostka przechodzi w Oszołamienie, wszystkie [AaCfPcBc] o wartości 2 lub mniejszej znikają
700. [[a1c6p3] Pasywka wroga [817201] — nazwa] 번지는 감정
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817201].name
   limit: do 40 znaków
   EN: Spreading Emotions
   PL: Spreading Emotions
701. [[a1c6p3] Pasywka wroga [817201] — opis] 자신과 동일한 속성의 폭발하는 감정 효과를 가진 아군이 사망하면, 자신의 폭발하는 감정 효과가 제거되며, 나머지 아군을 모두 사망시키고, 다음 턴에 [AaCfPbBd]을 얻음.\n해당 속성의 폭발하는 감정 효과, 해당 속성의 보호가 모든 수감자에게 부여됨.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817201].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [AaCfPbBd]
   znaczenie tagów: [AaCfPbBd] = 깊은 상실 / Deep Bereavement
   EN: When an ally with the same Affinity to this unit's Explosive Emotions effect is defeated: lose Explosive Emotions effect on self, kill all other allies, and gain [AaCfPbBd] next turn.\nAll Sinners gain the effects of the corresponding Explosive Emotions effect, and protection against the corresponding Affinity.
   PL: gdy sojusznik z efektem Explosive Emotions tej samej Afinności co ta jednostka ginie: jednostka traci swój efekt Explosive Emotions, zabija wszystkich pozostałych sojuszników i zyskuje [AaCfPbBd] w następnej turze.\nwszyscy Grzesznicy zyskują efekt odpowiednich Explosive Emotions i ochronę przed odpowiadającą Afinnością.
702. [[a1c6p3] Pasywka wroga [817202] — nazwa] 맺힌 원한
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817202].name
   limit: do 40 znaków
   EN: Amalgamated Resentment
   PL: Amalgamated Resentment
703. [[a1c6p3] Pasywka wroga [817202] — opis] 폭발하는 감정 효과가 있는 동안 모든 스킬의 속성이 해당 속성으로 변경됨.\n폭발하는 감정 효과가 제거된 후에도 해당 페이즈동안 변경된 스킬 속성이 유지됨.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817202].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When this unit has an Explosive Emotions effect, all Skill Affinities are replaced with the corresponding Affinity.\nEven after the Explosive Emotions effect expires, the changed Skill Affinities remain changed for the rest of the Phase.
   PL: gdy ta jednostka ma efekt Explosive Emotions, Afinność wszystkich Umiejętności zmienia się na odpowiadającą Afinność.\nnawet po wygaśnięciu efektu Explosive Emotions zmienione Afinności Umiejętności pozostają do końca Fazy.
704. [[a1c6p3] Pasywka wroga [817203] — nazwa] 끝나지 않은 복수
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817203].name
   limit: do 40 znaków
   EN: Continuing Revenge
   PL: Continuing Revenge
705. [[a1c6p3] Pasywka wroga [817203] — opis] 체력이 최대 체력의 75%, 35%가 될 때마다 패턴이 변경됨.\n패턴 변경 시 자신에게 부여된 부정적인 효과의 위력, 횟수를 절반으로 감소
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817203].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gains a new pattern at 75% and 35% of max HP.\nWhen this unit gains a new pattern, halve the Potency and Count of every negative effect on self
   PL: przybiera nowy wzorzec przy 75% i 35% Maks. HP.\nprzy zmianie wzorca zmniejsza o połowę Siłę i Licznik każdego negatywnego efektu należącego do tej jednostki
706. [[a1c6p3] Pasywka wroga [9101602] — nazwa] 적의
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101602].name
   limit: do 40 znaków
   EN: Antagonism
   PL: Antagonism
707. [[a1c6p3] Pasywka wroga [9101602] — opis] 대상이 자신보다 현재 체력이 높으면 합 위력 +2, 피해량 +20%
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101602].desc
   limit: do 120 znaków
   EN: If the target's current HP is higher than this unit's, Clash Power +2 and deal +20% damage
   PL: jeżeli aktualne HP celu jest wyższe niż HP tej jednostki, Moc Starcia +2 i zadaje +20% obrażeń
708. [[a1c6p3] Pasywka wroga [9101603] — nazwa] 기다린 순간
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101603].name
   limit: do 40 znaków
   EN: Long-awaited Moment
   PL: Long-awaited Moment
709. [[a1c6p3] Pasywka wroga [9101603] — opis] 합 승리 시 자신의 정신력 5 회복\n히스클리프에게 합 패배 시 정신력 감소 10, 다음 턴에 [Binding] 2를 얻음. (턴 당 1회)\n한 턴 동안 히스클리프에게 공격을 적중하지 못했으면, 턴 종료 시 정신력 감소 5
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101603].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Clash Win: Heal 5 SP on self\nClash Lose against Heathcliff: Lose 5 SP and gain 2 [Binding] next turn. (Once per turn)\nIf this unit did not land a single hit against Heathcliff this turn, lose 5 SP at Turn End
   PL: wygrana w Starciu: przywraca 5 SP\nprzegrana w Starciu z Heathcliffem: traci 10 SP i zyskuje 2 [Binding] w następnej turze. (1 raz na turę)\njeżeli podczas tury nie trafiła Heathcliffa ani razu, na koniec tury traci 5 SP
710. [[a1c6p3] Pasywka wroga [9101606] — nazwa] 오기
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101606].name
   limit: do 40 znaków
   EN: Vying Spirit
   PL: Vying Spirit
711. [[a1c6p3] Pasywka wroga [9101606] — opis] 자신의 체력이 낮아질수록 방어 레벨 증가\n(자신의 잃은 체력 10% 당 방어 레벨 +1. 소수점 버림)
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101606].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The lower this unit's HP gets, the higher this unit's Defense Level gets\nDefense Level +1 for every 10% missing HP on self (rounded down)
   PL: im niższe HP tej jednostki, tym wyższy Poziom Obrony\n(+1 Poziom Obrony za każde 10% brakującego HP, zaokrąglone w dół)
712. [[a1c6p3] Pasywka wroga [821601] — nazwa] 파탄의 와일드헌트
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=821601].name
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [[a1c6p3] Pasywka wroga [821601] — opis] 체력이 1이 되면, 사망하지 않고 체력이 1로 유지된다.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=821601].desc
   limit: do 120 znaków
   EN: Cannot be defeated at 0 HP. HP does not drop below 1.
   PL: nie może zostać pokonana przy 0 HP. HP nie spada poniżej 1.
714. [[a1c6p3] Pasywka wroga [817401] — nazwa] 또 다른 인격
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817401].name
   limit: do 40 znaków
   EN: A Distant Identity
   PL: A Distant Identity
715. [[a1c6p3] Pasywka wroga [817401] — opis] 턴 종료 시 양손의 체력이 1이 되면, 행동 불가 상태가 된다.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817401].desc
   limit: do 120 znaków
   EN: Turn End: If both Hands are at 1 HP, become Immobilized.
   PL: Koniec tury: jeżeli HP obu Rąk wynosi 1, jednostka zostaje unieruchomiona (Immobilized).
716. [[a1c6p3] Pasywka wroga [817402] — nazwa] 싸늘한 몸
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817402].name
   limit: do 40 znaków
   EN: Cold Body
   PL: Cold Body
717. [[a1c6p3] Pasywka wroga [817402] — opis] 체력이 1 미만으로 감소하지 않는다.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817402].desc
   limit: do 120 znaków
   EN: HP does not drop below 1.
   PL: HP nie spada poniżej 1.
718. [[a1c6p3] Pasywka wroga [817403] — nazwa] 흔들리는 자아
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817403].name
   limit: do 40 znaków
   EN: A Shaky Ego
   PL: A Shaky Ego
719. [[a1c6p3] Pasywka wroga [817403] — opis] 턴 종료 시 양손의 체력이 1이 되면, 다음 턴에 보호막을 얻는다.\n보호막을 전부 제거하면, 행동 불가 상태가 된다.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817403].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: If both Hands are at 1 HP, gain Shield next turn.\nOnce the Shield is fully depleted, become Immobilized.
   PL: Koniec tury: jeżeli HP obu Rąk wynosi 1, w następnej turze zyskuje Tarczę.\npo zużyciu całej Tarczy zostaje unieruchomiona (Immobilized).
720. [[a1c6p3] Pasywka wroga [819201] — nazwa] 불행을 끊는 손
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=819201].name
   limit: do 40 znaków
   EN: Misery-severing Hand
   PL: Misery-severing Hand
721. [[a1c6p3] Pasywka wroga [819201] — opis] 체력이 1이 된 턴의 다음 턴 종료 시 다른 손의 체력이 2 이상이면, 해당 손의 현재 체력의 50%만큼 자신의 체력을 회복한다. (소수점 버림)
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=819201].desc
   limit: do 220 znaków
   EN: If the other Hand is at 2+ HP at the next Turn End after the turn in which this Hand reaches 1 HP, this unit heals HP equal to 50% of the other Hand's HP. (rounded down)
   PL: jeżeli na koniec tury następnej po turze, w której ta Ręka spadła do 1 HP, druga Ręka ma 2+ HP, jednostka przywraca HP równe 50% aktualnego HP drugiej Ręki. (zaokrąglone w dół)
722. [[a1c6p3] Pasywka wroga [821401] — nazwa] 깊은 상실
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=821401].name
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [[a1c6p3] Pasywka wroga [821401] — opis] 체력이 1인 동안 흐트러짐 상태가 되고, 체력이 1 미만으로 감소하지 않는다.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=821401].desc
   limit: do 120 znaków
   EN: Become Staggered as long as this unit's HP is at 1. The HP does not drop below 1.
   PL: podczas gdy HP wynosi 1, jednostka jest w Oszołamieniu; HP nie spada poniżej 1.
724. [[a1c6p3] Pasywka wroga [817404] — nazwa] 찢긴 마음
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817404].name
   limit: do 40 znaków
   EN: Broken Heart
   PL: Broken Heart
725. [[a1c6p3] Pasywka wroga [817404] — opis] 턴 시작 시 체력이 2 이상인 손이 있으면, [Protection] 10을 얻고, 모든 내성이 0.2로 변경된다.\n턴 시작 시 양손의 체력이 1이면, [Protection]가 해제되고, 내성이 원래 값으로 돌아온다.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817404].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Turn Start: If there is a Hand with 2+ HP, gain 10 [Protection], and all Resistance values become 0.2.\nTurn Start: If both Hands are at 1 HP, [Protection] expires, and all Resistance values revert to default values.
   PL: Początek tury: jeżeli istnieje Ręka z 2+ HP, zyskuje 10 [Protection], a wszystkie wartości Odporności wynoszą 0.2.\nPoczątek tury: jeżeli HP obu Rąk wynosi 1, [Protection] znika, a wszystkie wartości Odporności wracają do pierwotnych.
726. [[a1c6p3] Pasywka wroga [817405] — nazwa] 모든 히스클리프를 위하여
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817405].name
   limit: do 40 znaków
   EN: For Every Heathcliff
   PL: For Every Heathcliff
727. [[a1c6p3] Pasywka wroga [817405] — opis] 히스클리프와 합 진행 시 합 위력 -3, 히스클리프에게 가하는 피해량 -50%\n히스클리프가 사망하면 전투 패배
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=817405].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When Clashing against Heathcliff, Clash Power -3 and deal -50% damage against Heathcliff\nWins Encounter if Heathcliff dies
   PL: podczas Starcia z Heathcliffem: Moc Starcia -3 i zadaje -50% obrażeń Heathcliffowi\njeżeli Heathcliff ginie, ta jednostka wygrywa walkę
728. [[a1c6p3] Pasywka wroga [816408] — nazwa] 복수의 시간
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816408].name
   limit: do 40 znaków
   EN: Moment of Vengeance
   PL: Moment of Vengeance
729. [[a1c6p3] Pasywka wroga [816408] — opis] 합 승리 시 자신의 정신력 5 회복\n합 패배 시 정신력 감소 10, 다음 턴에 [Binding] 2를 얻음. (턴 당 1회)\n한 턴 동안 공격을 적중하지 못했으면, 턴 종료 시 정신력 감소 5
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816408].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Clash Win: Heal 5 SP on self\nClash Lose: Lose 5 SP and gain 2 [Binding] next turn. (Once per turn)\nIf this unit did not land a single hit this turn, lose 5 SP at Turn End
   PL: wygrana w Starciu: przywraca 5 SP\nprzegrana w Starciu: traci 10 SP i zyskuje 2 [Binding] w następnej turze. (1 raz na turę)\njeżeli podczas tury nie trafiła przeciwnika ani razu, na koniec tury traci 5 SP
730. [[a1c6p3] Pasywka wroga [9101607] — nazwa] 퇴각 불가
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101607].name
   limit: do 40 znaków
   EN: Cannot Retreat
   PL: Cannot Retreat
731. [[a1c6p3] Pasywka wroga [9101607] — opis] 이번 전투동안 히스클리프 인격의 퇴각 관련 기능이 작동하지 않음.
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=9101607].desc
   limit: do 130 znaków
   EN: For the duration of this Encounter, Retreat functions will not activate for Heathcliff Identities.
   PL: na czas tej walki funkcje odwrotu Identyfikacji Heathcliffa nie działają.
732. [[a1c6p3] Pasywka wroga [816103] — nazwa] 분노 폭발
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816103].name
   limit: do 40 znaków
   EN: Erupting Wrath
   PL: Erupting Wrath
733. [[a1c6p3] Pasywka wroga [816103] — opis] 사망 시, 모든 적에게 [Combustion] 12 부여, [Combustion] 횟수 8 증가
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On death, inflict 12 [Combustion] and +8 [Combustion] Count on all enemies
   PL: gdy ginie, nakłada 12 [Combustion] i 8 Licznika [Combustion] wszystkim wrogom
734. [[a1c6p3] Pasywka wroga [816104] — nazwa] 악몽
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816104].name
   limit: do 40 znaków
   EN: Nightmare
   PL: Nightmare
735. [[a1c6p3] Pasywka wroga [816104] — opis] 이번 턴 자신을 포함한 아군이 합에서 패배하거나 적의 공격으로 피해를 받으면, [AttackUp] 1 얻고 정신력 1 회복 (최대 12회)
   źródło: Passives_Abnormality-a1c6p3.json :: dataList[id=816104].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: In a turn, if an allied unit(including this unit) loses a Clash or takes damage from enemy attacks, gain 1 [AttackUp] and heal 1 SP (max 12 times)
   PL: w tej turze, jeżeli sojusznik (łącznie z tą jednostką) przegrywa Starcie lub otrzymuje obrażenia od ataku wroga, zyskuje 1 [AttackUp] i przywraca 1 SP (do 12 razy)

## [a1c6p3] Pasywka wroga: Passives_Enemy-a1c6p3
- plik gry: `Passives_Enemy-a1c6p3.json`

736. [[a1c6p3] Pasywka wroga [9013601] — nazwa] 다...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013601].name
   limit: do 40 znaków
   EN: ies...
   PL: ies...
737. [[a1c6p3] Pasywka wroga [9013601] — opis] 턴 종료시 흐트러짐 상태가 되었을 때, 흐트러짐 상태에서 벗어나고 정신력 20 회복. 다음 턴에 공격 레벨 증가 1 얻음. (최대 1)
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013601].desc
   limit: do 160 znaków
   EN: Turn End: if Staggered, recover from the Staggered state and heal 20 SP. Gain 1 Offense Level Up next turn. (one time max)
   PL: Koniec tury: jeżeli przechodzi w Oszołamienie, dochodzi do siebie i przywraca 20 SP. Zyskuje 1 Wzrost Poziomu Ataku w następnej turze. (maks. 1)
738. [[a1c6p3] Pasywka wroga [9013602] — nazwa] 치...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013602].name
   limit: do 40 znaków
   EN: Yo...
   PL: Yo...
739. [[a1c6p3] Pasywka wroga [9013602] — opis] 턴 종료 시 패닉 상태에서 벗어났다면, 다음 턴에 공격 위력 증가 1 얻음
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013602].desc
   limit: do 120 znaków
   EN: Turn End: if this unit recovered from Panic, gain 1 Attack Power Up next turn
   PL: Koniec tury: jeżeli dochodzi do siebie z Paniki, zyskuje 1 Wzrost Mocy Ataku w następnej turze
740. [[a1c6p3] Pasywka wroga [9013603] — nazwa] 것...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013603].name
   limit: do 40 znaków
   EN: ool...
   PL: ool...
741. [[a1c6p3] Pasywka wroga [9013603] — opis] 대상이 자신보다 속도가 낮다면, 합 위력 +2
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013603].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's, Clash Power +2
   PL: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +2
742. [[a1c6p3] Pasywka wroga [9013604] — nazwa] 가...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013604].name
   limit: do 40 znaków
   EN: oice...!
   PL: oice...!
743. [[a1c6p3] Pasywka wroga [9013604] — opis] 한 공격 스킬의 모든 코인이 적중했을 때, 코인이 모두 앞면이라면, 정신력 10 회복
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013604].desc
   limit: do 120 znaków
   EN: Heal 10 SP when every Coin of an Attack Skill hits heads
   PL: przywraca 10 SP, gdy wszystkie Monety Umiejętności ataku trafią Awersami
744. [[a1c6p3] Pasywka wroga [9013606] — nazwa] 위…
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013606].name
   limit: do 40 znaków
   EN: Threa...
   PL: Threa...
745. [[a1c6p3] Pasywka wroga [9013606] — opis] 합 진행 시, 합 위력 -1, 자신의 체력 10 피해 (이 피해로 체력이 0이 되지않음)
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013606].desc
   limit: do 160 znaków
   EN: In a Clash, Clash Power -1; take 10 HP damage on self with each Clash (this effect does not reduce this unit's HP to 0)
   PL: podczas Starcia: Moc Starcia -1 i otrzymuje 10 obrażeń HP (te obrażenia nie doprowadzą HP do 0)
746. [[a1c6p3] Pasywka wroga [9013607] — nazwa] 기...리
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013607].name
   limit: do 40 znaków
   EN: Opp... tta
   PL: Opp... tta
747. [[a1c6p3] Pasywka wroga [9013607] — opis] 합 패배시, 공격 레벨 증가 3 얻음. (턴 당 1회)
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013607].desc
   limit: do 120 znaków
   EN: Upon Clash Lose, gain 3 Offense Level Up. (Once per turn)
   PL: po przegranej w Starciu zyskuje 3 Wzrost Poziomu Ataku. (1 raz na turę)
748. [[a1c6p3] Pasywka wroga [9013701] — nazwa] 육체...증폭
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013701].name
   limit: do 40 znaków
   EN: Bod... ...st
   PL: Bod... ...st
749. [[a1c6p3] Pasywka wroga [9013701] — opis] 턴 종료 시 자신의 정신력이 -10 이하일 때, 다음 턴에 공격 레벨 증가 3 얻음.
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013701].desc
   limit: do 120 znaków
   EN: Turn End: if this unit's SP is at -10 or less, gain 3 Offense Level Up next turn.
   PL: Koniec tury: jeżeli SP tej jednostki wynosi -10 lub mniej, zyskuje 3 Wzrost Poziomu Ataku w następnej turze.
750. [[a1c6p3] Pasywka wroga [9013804] — nazwa] 뚜...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013804].name
   limit: do 40 znaków
   EN: Tou...
   PL: Tou...
751. [[a1c6p3] Pasywka wroga [9013804] — opis] 한 공격 스킬의 모든 코인이 적중했을 때, 코인이 모두 앞면이라면, 정신력 10 회복
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013804].desc
   (powtórzenie elementu 743 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [[a1c6p3] Pasywka wroga [9013801] — nazwa] 정...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013801].name
   limit: do 40 znaków
   EN: Hou...
   PL: Hou...
753. [[a1c6p3] Pasywka wroga [9013801] — opis] 공격 스킬 사용 시 대상의 체력이 70이하일 때, 기본 위력 +1, 피해량 +20%
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013801].desc
   limit: do 130 znaków
   EN: When using an Attack Skill, if target's HP is below 70, gain Base Power +1 and deal +20% damage
   PL: przy użyciu Umiejętności ataku, jeżeli HP celu wynosi 70 lub mniej, Moc Bazowa +1 i zadaje +20% obrażeń
754. [[a1c6p3] Pasywka wroga [9013802] — nazwa] ...몰이
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013802].name
   limit: do 40 znaków
   EN: ...erding
   PL: ...erding
755. [[a1c6p3] Pasywka wroga [9013802] — opis] 사용 시 자신의 속도가 대상보다 빠르면, 합 위력 +2, 피해량 +20%
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=9013802].desc
   limit: do 150 znaków
   EN: When using a Skill, if this unit's Speed is faster than the target's, gain Clash Power +2 and deal +20% damage
   PL: przy użyciu Umiejętności, jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +2 i zadaje +20% obrażeń
756. [[a1c6p3] Pasywka wroga [817001] — nazwa] ...감
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817001].name
   limit: do 40 znaków
   EN: ...rity
   PL: ...rity
757. [[a1c6p3] Pasywka wroga [817001] — opis] 자신의 체력이 65% 이하가 되면, 합 승리시 [AttackUp] 1, [TakeHpHealIncrease]를 1 얻음\n자신의 체력이 40% 이하가 되면, 사용시 [AttackUp] 1, [TakeHpHealIncrease]를 1 얻음\n한 번이라도 조건이 만족되면, 해당 조건으로 계속 발동됨.
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817001].desc
   (powtórzenie elementu 305 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [[a1c6p3] Pasywka wroga [817002] — nazwa] 향...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817002].name
   limit: do 40 znaków
   EN: Dir...
   PL: Dir...
759. [[a1c6p3] Pasywka wroga [817002] — opis] 첫 흐트러짐 해제 이후 합 승리 시 공격 스킬 적중시 피해량의 10%만큼 추가 분노 피해를 입힘.
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817002].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [[a1c6p3] Pasywka wroga [817003] — nazwa] 포...
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817003].name
   limit: do 40 znaków
   EN: Pred...
   PL: Pred...
761. [[a1c6p3] Pasywka wroga [817003] — opis] 적 처치 시, 본체 및 부위 체력을 200 회복.\n다음 턴에 [Agility] 1, [DefenseUp] 3, [AttackUp] 2 얻음.
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817003].desc
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [[a1c6p3] Pasywka wroga [817004] — nazwa] ...식
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817004].name
   limit: do 40 znaków
   EN: ...ked
   PL: ...ked
763. [[a1c6p3] Pasywka wroga [817004] — opis] [AaCfPbBe]을 가지고 있는 대상 우선 공격
   źródło: Passives_Enemy-a1c6p3.json :: dataList[id=817004].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c7p1] Wróg / część: Enemies-a1c7p1
- plik gry: `Enemies-a1c7p1.json`

764. [[a1c7p1] Wróg / część [90152] — nazwa] 차려입은 피주머니
   źródło: Enemies-a1c7p1.json :: dataList[id=90152].name
   limit: do 40 znaków
   EN: Well-dressed Bloodbag
   PL: Well-dressed Bloodbag
765. [[a1c7p1] Wróg / część [90152] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90152].desc
   limit: do 120 znaków
   EN: Unit
   PL: jednostka
766. [[a1c7p1] Wróg / część [90153] — nazwa] 꾸며진 피주머니
   źródło: Enemies-a1c7p1.json :: dataList[id=90153].name
   limit: do 40 znaków
   EN: Embellished Bloodbag
   PL: Embellished Bloodbag
767. [[a1c7p1] Wróg / część [90153] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90153].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [[a1c7p1] Wróg / część [90154] — nazwa] 미쳐버린 멋장이 혈귀
   źródło: Enemies-a1c7p1.json :: dataList[id=90154].name
   limit: do 50 znaków
   EN: Insane Fashionista Bloodfiend
   PL: Insane Fashionista Bloodfiend
769. [[a1c7p1] Wróg / część [90154] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90154].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [[a1c7p1] Wróg / część [90155] — nazwa] 실성한 멋장이 혈귀
   źródło: Enemies-a1c7p1.json :: dataList[id=90155].name
   limit: do 40 znaków
   EN: Mad Fashionista Bloodfiend
   PL: Mad Fashionista Bloodfiend
771. [[a1c7p1] Wróg / część [90155] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90155].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [[a1c7p1] Wróg / część [90156] — nazwa] 도전적인 송곳니 사냥 사무소 해결사
   źródło: Enemies-a1c7p1.json :: dataList[id=90156].name
   limit: do 50 znaków
   EN: Combative Fanghunt Office Fixer
   PL: Combative Fanghunt Office Fixer
773. [[a1c7p1] Wróg / część [90156] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90156].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [[a1c7p1] Wróg / część [90157] — nazwa] 자존심 강한 송곳니 사냥 사무소 해결사
   źródło: Enemies-a1c7p1.json :: dataList[id=90157].name
   limit: do 50 znaków
   EN: Prideful Fanghunt Office Fixer
   PL: Prideful Fanghunt Office Fixer
775. [[a1c7p1] Wróg / część [90157] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90157].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [[a1c7p1] Wróg / część [90160] — nazwa] 나쁜 도적
   źródło: Enemies-a1c7p1.json :: dataList[id=90160].name
   limit: do 40 znaków
   EN: No-good Bandit
   PL: No-good Bandit
777. [[a1c7p1] Wróg / część [90160] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90160].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [[a1c7p1] Wróg / część [90161] — nazwa] 무시무시한 곰
   źródło: Enemies-a1c7p1.json :: dataList[id=90161].name
   limit: do 40 znaków
   EN: Big, Scary Bear
   PL: Big, Scary Bear
779. [[a1c7p1] Wróg / część [90161] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=90161].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [[a1c7p1] Wróg / część [8371] — nazwa] 서부 섕크 3과 까미유
   źródło: Enemies-a1c7p1.json :: dataList[id=8371].name
   limit: do 40 znaków
   EN: Cinq West Section 3 Camille
   PL: Cinq West Section 3 Camille
781. [[a1c7p1] Wróg / część [8371] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=8371].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [[a1c7p1] Wróg / część [8372] — nazwa] ???
   źródło: Enemies-a1c7p1.json :: dataList[id=8372].name
   limit: do 40 znaków
   EN: ???
   PL: ???
783. [[a1c7p1] Wróg / część [8372] — opis] 잡몹
   źródło: Enemies-a1c7p1.json :: dataList[id=8372].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c7p1] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c7p1
- grupa rozdziału/trybu: `a1c7p1` · plik: `Skills_Abnormality-a1c7p1.json`

784. [Umiejętność wroga [837101] (ulepszenie 1) — nazwa] 알레
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837101].levelList[level=1].name
   limit: do 40 znaków
   EN: Allez
   PL: Allez
785. [Umiejętność wroga [837101] (ulepszenie 1) — opis] [WhenUse] [DuelDeclaration_Camille] 부여\n[WhenUse] 자신의 [Breath] 5 얻음\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837101].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DuelDeclaration_Camille], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DuelDeclaration_Camille] = 결투 선포 - 까미유 / Declared Duel - Camille; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Inflict [DuelDeclaration_Camille]\n[WhenUse] Gain 5 [Breath]\n[WinDuel] Gain +2 [Breath] Count
   PL: [WhenUse] nakłada [DuelDeclaration_Camille]\n[WhenUse] zyskuje 5 [Breath]\n[WinDuel] zyskuje 2 Licznika [Breath]
786. [Umiejętność wroga [837102] (ulepszenie 1) — nazwa] 꾸드르와
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837102].levelList[level=1].name
   limit: do 40 znaków
   EN: Coup Droit
   PL: Coup Droit
787. [Umiejętność wroga [837102] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL: [WhenUse] zyskuje 2 [Breath]
788. [Umiejętność wroga [837102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [Breath]
789. [Umiejętność wroga [837102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict 3 [Burst]
   PL: [OnSucceedAttack] przy Szybkości 7 lub wyższej, nakłada 3 [Burst]
790. [Umiejętność wroga [837102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] zyskuje 3 [Breath]
791. [Umiejętność wroga [837102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [837103] (ulepszenie 1) — nazwa] 팡트
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837103].levelList[level=1].name
   limit: do 40 znaków
   EN: Fente
   PL: Fente
793. [Umiejętność wroga [837103] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 7 이상이면, 코인 위력 +2\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 7+ [Breath], Coin Power +2\n[WinDuel] Gain +2 [Breath] Count
   PL: [WhenUse] przy 7+ [Breath], Moc Monety +2\n[WinDuel] zyskuje 2 Licznika [Breath]
794. [Umiejętność wroga [837103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [837103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict 3 [Burst] Count
   PL: [OnSucceedAttack] przy Szybkości 7 lub wyższej, nakłada 3 Licznika [Burst]
796. [Umiejętność wroga [837103] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837103].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +50% Damage on Critical Hit
   PL: [CriticalOnSucceedAttack] +50% obrażeń przy trafieniu krytycznym
797. [Umiejętność wroga [837104] (ulepszenie 1) — nazwa] 살뤼
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].name
   limit: do 40 znaków
   EN: Salut
   PL: Salut
798. [Umiejętność wroga [837104] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 공격자보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, Coin Power +1 (Coin Power +1 for every 2 Speed difference; max 3)
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Monety +1 (Moc Monety +1 za każde 2 punkty różnicy Szybkości; maks. 3)
799. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 4 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +4 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 4 Licznika [Breath]
800. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict 3 [Burst] and +1 [Burst] Count
   PL: [OnSucceedAttack] przy Szybkości 7 lub wyższej, nakłada 3 [Burst] i 1 Licznika [Burst]
801. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL: [OnSucceedAttack] zyskuje 5 [Breath]
802. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 800 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 800 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +100% Damage on Critical Hit
   PL: [CriticalOnSucceedAttack] +100% obrażeń przy trafieniu krytycznym
806. [Umiejętność wroga [837104] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]당 피해량 +5% (최대 50%)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837104].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +5% damage for every [Burst] on the target (Max 50%)
   PL: [OnSucceedAttack] zadaje +5% obrażeń za każde [Burst] celu (maks. 50%)
807. [Umiejętność wroga [837105] (ulepszenie 1) — nazwa] 응수
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837105].levelList[level=1].name
   limit: do 40 znaków
   EN: Parry
   PL: Parry
808. [Umiejętność wroga [837105] (ulepszenie 1) — opis] [WinDuel] 합 횟수에 비례하여 피해량이 증가 (합 횟수 1당 +10%. 최대 50%)\n[WinDuel] 다음 턴에 [Agility] 2 얻음\n[DefeatDuel] 다음 턴에 [Binding] 2 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837105].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Agility], [DefeatDuel], [Binding]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Agility] = 신속 / Haste; [DefeatDuel] = [합 패배] / [Clash Lose]; [Binding] = 속박 / Bind
   EN: [WinDuel] Deal more damage based on number of Clashes (+10% damage for every Clash, max 50%)\n[WinDuel] Gain 2 [Agility] next turn\n[DefeatDuel] Gain 2 [Binding] next turn
   PL: [WinDuel] zadaje więcej obrażeń w zależności od liczby Starć (+10% obrażeń za każde Starcie, maks. 50%)\n[WinDuel] zyskuje 2 [Agility] w następnej turze\n[DefeatDuel] zyskuje 2 [Binding] w następnej turze
809. [Umiejętność wroga [837105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [837106] (ulepszenie 1) — nazwa] 데팡시브
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837106].levelList[level=1].name
   limit: do 40 znaków
   EN: Défensive
   PL: Défensive
811. [Umiejętność wroga [837106] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837106].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Agility]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Agility] = 신속 / Haste
   EN: [OnSucceedEvade] Gain 1 [Agility] next turn
   PL: [OnSucceedEvade] zyskuje 1 [Agility] w następnej turze
812. [Umiejętność wroga [837201] (ulepszenie 1) — nazwa] 예쁘게 오려줄게!
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837201].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Cut You Up All Pretty!
   PL: I'll Cut You Up All Pretty!
813. [Umiejętność wroga [837201] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Laceration] 5 당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837201].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Clash Power +1\n[WhenUse] Coin Power +1 for every 5 [Laceration] on self (max 3)
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Starcia +1\n[WhenUse] Moc Monety +1 za każde 5 [Laceration] tej jednostki (maks. 3)
814. [Umiejętność wroga [837201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [837201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([BloodScissor] 단계 - 1)에 비례하여, 코인 재사용 1회 (최대 2)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodScissor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] Reuse Coin ([BloodScissor] Stage - 1) times (max 2)
   PL: [OnSucceedAttack] używa Monety ponownie ([BloodScissor] Etap - 1) razy (maks. 2)
816. [Umiejętność wroga [837202] (ulepszenie 1) — nazwa] 더욱 날카롭게
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837202].levelList[level=1].name
   limit: do 40 znaków
   EN: Even Sharper
   PL: Even Sharper
817. [Umiejętność wroga [837202] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 20 소모하여, 소모한 [BloodDinner] 10당 [BloodScissor] 1 얻고 정신력 3 회복.\n- 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 30을 얻음\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Laceration] 5 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837202].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodScissor], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume up to 20 [BloodDinner]; gain 1 [BloodScissor] and heal 3 SP for every 10 [BloodDinner] consumed\n- If this unit failed to consume [BloodDinner] with this Skill, gain 30 [Laceration]\n[WhenUse] If target has 6+ [Laceration], Clash Power +1\n[WhenUse] Coin Power +1 for every 5 [Laceration] on self (max 2)
   PL: [WhenUse] zużywa do 20 [BloodDinner]; za każde 10 zużytych [BloodDinner] zyskuje 1 [BloodScissor] i przywraca 3 SP\n- jeżeli ta Umiejętność nie zużyła [BloodDinner], zyskuje 30 [Laceration]\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Starcia +1\n[WhenUse] Moc Monety +1 za każde 5 [Laceration] tej jednostki (maks. 2)
818. [Umiejętność wroga [837202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [837202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [837203] (ulepszenie 1) — nazwa] 싹둑!!
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837203].levelList[level=1].name
   limit: do 40 znaków
   EN: SNIP!!
   PL: SNIP!!
821. [Umiejętność wroga [837203] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 30 소모하여, 소모한 [BloodDinner] 10당 [BloodScissor] 1 얻고 정신력 3 회복\n[WhenUse] 대상에게 [LineCutting]이 있으면, 합 위력 +5\n[LineCutting]에게 적중 시마다 정신력 5 회복
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837203].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodScissor], [LineCutting]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [LineCutting] = 재봉 대상 / Sewing Target
   EN: [WhenUse] Consume up to 30 [BloodDinner]; gain 1 [BloodScissor] and heal 3 SP for every 10 [BloodDinner] consumed\n[WhenUse] If target has [LineCutting], Clash Power +5\nHeal 5 SP on every hit against [LineCutting]
   PL: [WhenUse] zużywa do 30 [BloodDinner]; za każde 10 zużytych [BloodDinner] zyskuje 1 [BloodScissor] i przywraca 3 SP\n[WhenUse] jeżeli cel ma [LineCutting], Moc Starcia +5\nprzy każdym trafieniu w [LineCutting] przywraca 5 SP
822. [Umiejętność wroga [837203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [837203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [837203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
825. [Umiejętność wroga [837204] (ulepszenie 1) — nazwa] 너도 같이 오려줄게!
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837204].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Cut You Up Too!
   PL: I'll Cut You Up Too!
826. [Umiejętność wroga [837204] (ulepszenie 1) — opis] [BeforeAttack] [BloodScissor] 단계에 비례하여 공격 가중치 +1 (최대 2)\n[WhenUse] [BloodDinner]을 최대 30 소모하여, 소모한 [BloodDinner] 10당 [BloodScissor] 1 얻고 정신력 3 회복\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 합 위력 +2
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837204].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [BloodScissor], [WhenUse], [BloodDinner], [Laceration]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: [BeforeAttack] Atk Weight +1 for every Stage of [BloodScissor] (max 2)\n[WhenUse] Consume up to 30 [BloodDinner]; gain 1 [BloodScissor] and heal 3 SP for every 10 [BloodDinner] consumed\n[WhenUse] If target has 6+ [Laceration], Clash Power +2
   PL: [BeforeAttack] Waga Ataku +1 za każdy Etap [BloodScissor] (maks. 2)\n[WhenUse] zużywa do 30 [BloodDinner]; za każde 10 zużytych [BloodDinner] zyskuje 1 [BloodScissor] i przywraca 3 SP\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Starcia +2
827. [Umiejętność wroga [837204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
828. [Umiejętność wroga [837204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [BloodScissorScars] 1 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodScissorScars]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissorScars] = 깊게 베인 상처 / Deep Laceration
   EN: [OnSucceedAttack] Inflict 1 [BloodScissorScars] next turn
   PL: [OnSucceedAttack] nakłada 1 [BloodScissorScars] w następnej turze
829. [Umiejętność wroga [837204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 5 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttackHead] nakłada 5 [Laceration] i 2 Licznika [Laceration]
830. [Umiejętność wroga [837205] (ulepszenie 1) — nazwa] 이번에는 네 차례야
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837205].levelList[level=1].name
   limit: do 40 znaków
   EN: Now, It's Your Turn
   PL: Now, It's Your Turn
831. [Umiejętność wroga [837205] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
832. [Umiejętność wroga [837205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 827 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [837205] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [BloodScissorScars] 1 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 828 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [837205] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [LineCutting]이 됨
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837205].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LineCutting]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LineCutting] = 재봉 대상 / Sewing Target
   EN: [OnSucceedAttack] Inflict [LineCutting] next turn
   PL: [OnSucceedAttack] nakłada [LineCutting] w następnej turze
835. [Umiejętność wroga [837206] (ulepszenie 1) — nazwa] 사이좋게 오려줄게!
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Cut You Together!
   PL: I'll Cut You Together!
836. [Umiejętność wroga [837206] (ulepszenie 1) — opis] [BeforeAttack] [BloodScissor] 단계에 비례하여 공격 가중치 +1\n[WhenUse] [BloodDinner]을 최대 100 소모하여, 소모한 [BloodDinner] 10당 [BloodScissor] 1 얻고 정신력 3 회복\n[EndSkill] [BloodScissor] 10 소모
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [BloodScissor], [WhenUse], [BloodDinner], [EndSkill], [Laceration]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [EndSkill] = [공격 종료시] / [Attack End]; [Laceration] = 출혈 / Bleed
   EN: [BeforeAttack] Atk Weight +1 for every Stage of [BloodScissor]\n[WhenUse] Consume up to 100 [BloodDinner]; gain 1 [BloodScissor] and heal 3 SP for every 10 [BloodDinner] consumed\n[WhenUse] If target has 6+ [Laceration], Clash Power +2\n[EndSkill] Consume 10 [BloodScissor]
   PL: [BeforeAttack] Waga Ataku +1 za każdy Etap [BloodScissor]\n[WhenUse] zużywa do 100 [BloodDinner]; za każde 10 zużytych [BloodDinner] zyskuje 1 [BloodScissor] i przywraca 3 SP\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Starcia +2\n[EndSkill] zużywa 10 [BloodScissor]
837. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 827 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 824 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 1, efekt 3 — opis] [WinDuelAttack] 대상의 [Laceration]을 발동시킴 (최대 10). 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Activate the target's [Laceration] (max 10). The target loses 1 [Laceration] Count
   PL: [WinDuelAttack] wyzwala [Laceration] celu (do 10). Zmniejsza Licznik [Laceration] celu o 1
840. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 827 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 2, efekt 3 — opis] [WinDuelAttack] 대상의 [Laceration]을 발동시킴 (최대 10). 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 827 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 3, efekt 3 — opis] [WinDuelAttack] 대상의 [Laceration]을 발동시킴 (최대 10). 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [BloodScissor] 단계에 비례하여, 피해량 +40% (최대 120%)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodScissor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] Deal +40% damage for every [BloodScissor] Stage (max 120%)
   PL: [OnSucceedAttack] zadaje +40% obrażeń za każdy Etap [BloodScissor] (maks. 120%)
847. [Umiejętność wroga [837206] (ulepszenie 1) — moneta 4, efekt 2 — opis] [EnemyKill] 이 코인 효과로 처치했다면, 처치한 대상에게 가한 피해량의 50%만큼 회복함.
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837206].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] If this Coin effect killed the target, heal by 50% of the damage dealt against the killed target.
   PL: [EnemyKill] jeżeli ten efekt Monety pokonał cel, przywraca HP równe 50% obrażeń zadanych pokonanemu celowi.
848. [Umiejętność wroga [837207] (ulepszenie 1) — nazwa] 예의에 어긋나잖아!
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837207].levelList[level=1].name
   limit: do 40 znaków
   EN: How Discourteous!
   PL: How Discourteous!
849. [Umiejętność wroga [837207] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] [BloodScissor] 단계에 비례하여, 합 위력 +1 (최대 3)\n[WhenUse] 자신의 [Laceration] 5 당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837207].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [BloodScissor], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[WhenUse] Clash Power +1 for every [BloodScissor] Stage (max 3)\n[WhenUse] Coin Power +1 for every 5 [Laceration] on self (max 3)
   PL: [DuelCounter]\n[WhenUse] Moc Starcia +1 za każdy Etap [BloodScissor] (maks. 3)\n[WhenUse] Moc Monety +1 za każde 5 [Laceration] tej jednostki (maks. 3)
850. [Umiejętność wroga [837207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +4 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 4 [Laceration] i 4 Licznika [Laceration]
851. [Umiejętność wroga [837208] (ulepszenie 1) — nazwa] 아름답지 않은건 필요없어!!
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837208].levelList[level=1].name
   limit: do 40 znaków
   EN: I Don't Need Ugly Things!!
   PL: I Don't Need Ugly Things!!
852. [Umiejętność wroga [837208] (ulepszenie 1) — opis] [CantChangeTarget]\n현재 체력 비율이 가장 낮은 대상 우선 공격
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837208].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantChangeTarget]\nPrioritizes targets with the least HP percentage
   PL: [CantChangeTarget]\npriorytet: cele o najniższym procencie aktualnego HP
853. [Umiejętność wroga [837208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30%이하면 처치
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If the target is at 30%- HP, kill the target
   PL: [OnSucceedAttack] jeżeli HP celu wynosi 30% lub mniej, zabija cel
854. [Umiejętność wroga [837208] (ulepszenie 1) — moneta 1, efekt 2 — opis] [EnemyKill] 처치한 대상의 최대 체력 30%만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837208].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [BloodDinner]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [EnemyKill] Increase [BloodDinner] by 30% of the defeated enemy's max HP
   PL: [EnemyKill] zwiększa [BloodDinner] o 30% Maks. HP pokonanego wroga
855. [Umiejętność wroga [837208] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EnemyKill] 다음 턴에 [Vulnerable] 4 얻음
   źródło: Skills_Abnormality-a1c7p1.json :: dataList[id=837208].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Vulnerable]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Vulnerable] = 취약 / Fragile
   EN: [EnemyKill] gain 4 [Vulnerable] next turn
   PL: [EnemyKill] zyskuje 4 [Vulnerable] w następnej turze

## [a1c7p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c7p1
- grupa rozdziału/trybu: `a1c7p1` · plik: `Skills_Enemy-a1c7p1.json`

856. [Umiejętność wroga [9015201] (ulepszenie 1) — nazwa] 경혈식 찌르기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015201].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Stab
   PL: Hardblood Stab
857. [Umiejętność wroga [9015201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Umiejętność wroga [9015202] (ulepszenie 1) — nazwa] 경혈식 베어내기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Cleave
   PL: Hardblood Cleave
859. [Umiejętność wroga [9015202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 8+ [Laceration], deal +20% damage
   PL: [WhenUse] jeżeli cel ma 8+ [Laceration], zadaje +20% obrażeń
860. [Umiejętność wroga [9015202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [9015202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność wroga [9015202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration]이 6 이상이면 [HardenedBlood]을 1 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] At 6+ [Laceration], gain 1 [HardenedBlood]
   PL: [OnSucceedAttack] przy 6+ [Laceration], zyskuje 1 [HardenedBlood]
863. [Umiejętność wroga [9015202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność wroga [9015202] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8, [BloodScissor] 1 얻음.
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015202].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodScissor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] Gain 8 [Laceration] and 1 [BloodScissor]
   PL: [OnSucceedAttack] zyskuje 8 [Laceration] i 1 [BloodScissor].
865. [Umiejętność wroga [9015203] (ulepszenie 1) — nazwa] 경혈식 강화 베어내기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015203].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Powercleave
   PL: Hardblood Powercleave
866. [Umiejętność wroga [9015203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1\n[HardenedBlood]당 피해량 +5% (최대 25%)\n[EndSkill] [HardenedBlood], [BloodScissor] 전부 소모
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015203].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [EndSkill], [BloodScissor]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [EndSkill] = [공격 종료시] / [Attack End]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [WhenUse] If target has 6+ [Laceration], Base Power +1\nDeal +5% damage for every [HardenedBlood] (max 25%)\n[EndSkill] Consume all [HardenedBlood] and [BloodScissor]
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Bazowa +1\nzadaje +5% obrażeń za każde [HardenedBlood] (maks. 25%)\n[EndSkill] zużywa całe [HardenedBlood] i [BloodScissor]
867. [Umiejętność wroga [9015203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 2 Licznika [Laceration]
868. [Umiejętność wroga [9015203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])%만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal ([Laceration] on target)% HP (max 20%)
   PL: [OnSucceedAttack] przywraca HP równe ([Laceration] celu)% Maks. HP (maks. 20%)
869. [Umiejętność wroga [9015204] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015204].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [9015204] (ulepszenie 1) — opis] [WhenUse] 자신의 [HardenedBlood] 1당, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] Base Power +1 for every [HardenedBlood] on self
   PL: [WhenUse] Moc Bazowa +1 za każde [HardenedBlood] tej jednostki
871. [Umiejętność wroga [9015204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL: [OnSucceedAttackHead] nakłada 2 [Laceration]
872. [Umiejętność wroga [9015301] (ulepszenie 1) — nazwa] 경혈식 쐐기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015301].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Wedge
   PL: Hardblood Wedge
873. [Umiejętność wroga [9015301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Umiejętność wroga [9015302] (ulepszenie 1) — nazwa] 경혈식 가르기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Chop
   PL: Hardblood Chop
875. [Umiejętność wroga [9015302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 피해량 +10%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], deal +10% damage
   PL: [WhenUse] jeżeli cel ma 4+ [Laceration], zadaje +10% obrażeń
876. [Umiejętność wroga [9015302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Umiejętność wroga [9015302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność wroga [9015302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration]이 6 이상이면 [HardenedBlood]을 1 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 862 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Umiejętność wroga [9015302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Umiejętność wroga [9015302] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8, [BloodScissor] 1 얻음.
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015302].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 864 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Umiejętność wroga [9015303] (ulepszenie 1) — nazwa] 경혈식 강화 가르기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015303].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Powerchop
   PL: Hardblood Powerchop
882. [Umiejętność wroga [9015303] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 횟수가 6 이상이면, 기본 위력 +1\n[HardenedBlood]당 피해량 +5% (최대 25%)\n[EndSkill] [HardenedBlood], [BloodScissor] 전부 소모
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015303].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [EndSkill], [BloodScissor]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [EndSkill] = [공격 종료시] / [Attack End]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [WhenUse] If target has 6+ [Laceration] Count, Base Power +1\nDeal +5% damage for every [HardenedBlood] (max 25%)\n[EndSkill] Consume all [HardenedBlood] and [BloodScissor]
   PL: [WhenUse] jeżeli cel ma 6+ Licznika [Laceration], Moc Bazowa +1\nzadaje +5% obrażeń za każde [HardenedBlood] (maks. 25%)\n[EndSkill] zużywa całe [HardenedBlood] i [BloodScissor]
883. [Umiejętność wroga [9015303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 867 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Umiejętność wroga [9015303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])%만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 868 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Umiejętność wroga [9015304] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015304].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Umiejętność wroga [9015304] (ulepszenie 1) — opis] [WhenUse] 자신의 [HardenedBlood] 1당, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015304].levelList[level=1].desc
   (powtórzenie elementu 870 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Umiejętność wroga [9015304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 871 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność wroga [9015401] (ulepszenie 1) — nazwa] 축제야 축제!
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015401].levelList[level=1].name
   limit: do 40 znaków
   EN: It's a Festival, a Festival!
   PL: It's a Festival, a Festival!
889. [Umiejętność wroga [9015401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Umiejętność wroga [9015401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Umiejętność wroga [9015402] (ulepszenie 1) — nazwa] 옷 입혀줄게
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015402].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Dress Up
   PL: Let's Dress Up
892. [Umiejętność wroga [9015402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], deal +20% damage
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], zadaje +20% obrażeń
893. [Umiejętność wroga [9015402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
894. [Umiejętność wroga [9015402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, [HardenedBlood]을 1 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] If target has 5+ [Laceration], gain 1 [HardenedBlood]
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], zyskuje 1 [HardenedBlood]
