# Paczka AI P79 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 15/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P79_3c_przeciwnicy_i_anomalie_cz15.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P79_3c_przeciwnicy_i_anomalie_cz15.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Abnormality
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Abnormality.json`

1. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Fragile next turn
   PL:
2. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed next turn
   PL:
3. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
4. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [Umiejętność wroga [802504] (ulepszenie 1) — nazwa] 광폭한 추격
   źródło: Skills_Abnormality.json :: dataList[id=802504].levelList[level=1].name
   limit: do 40 znaków
   EN: Furious Chase
   PL:
9. [Umiejętność wroga [802504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 횟수 6 증가
   źródło: Skills_Abnormality.json :: dataList[id=802504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +6 Bleed Count next turn
   PL:
10. [Umiejętność wroga [802504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 파열 횟수 6 증가
   źródło: Skills_Abnormality.json :: dataList[id=802504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +6 Rupture Count next turn
   PL:
11. [Umiejętność wroga [802505] (ulepszenie 1) — nazwa] 날 선 경계
   źródło: Skills_Abnormality.json :: dataList[id=802505].levelList[level=1].name
   limit: do 40 znaków
   EN: Sharp Alertness
   PL:
12. [Umiejętność wroga [802701] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality.json :: dataList[id=802701].levelList[level=1].name
   limit: do 40 znaków
   EN: Claw
   PL:
13. [Umiejętność wroga [802701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed next turn
   PL:
14. [Umiejętność wroga [802702] (ulepszenie 1) — nazwa] 경계
   źródło: Skills_Abnormality.json :: dataList[id=802702].levelList[level=1].name
   limit: do 40 znaków
   EN: Lookout
   PL:
15. [Umiejętność wroga [802703] (ulepszenie 1) — nazwa] 눈 먼 돌진
   źródło: Skills_Abnormality.json :: dataList[id=802703].levelList[level=1].name
   limit: do 40 znaków
   EN: Blind Charge
   PL:
16. [Umiejętność wroga [802703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=802703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed next turn
   PL:
17. [Umiejętność wroga [802703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=802703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [802801] (ulepszenie 1) — nazwa] 휘감는 팔
   źródło: Skills_Abnormality.json :: dataList[id=802801].levelList[level=1].name
   limit: do 40 znaków
   EN: Coiling Arms
   PL:
19. [Umiejętność wroga [802801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=802801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze next turn
   PL:
20. [Umiejętność wroga [802802] (ulepszenie 1) — nazwa] 똬리 틀기
   źródło: Skills_Abnormality.json :: dataList[id=802802].levelList[level=1].name
   limit: do 40 znaków
   EN: Coil Up
   PL:
21. [Umiejętność wroga [802802] (ulepszenie 1) — opis] [DefeatDuel] 본능을 1 잃음
   źródło: Skills_Abnormality.json :: dataList[id=802802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Lose 1 Instincts
   PL:
22. [Umiejętność wroga [802802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 20 회복, 출혈 횟수 5 증가
   źródło: Skills_Abnormality.json :: dataList[id=802802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20 HP; Inflict +5 Bleed Count
   PL:
23. [Umiejętność wroga [802803] (ulepszenie 1) — nazwa] 양팔 휘두르기
   źródło: Skills_Abnormality.json :: dataList[id=802803].levelList[level=1].name
   limit: do 40 znaków
   EN: Swinging Arms
   PL:
24. [Umiejętność wroga [802803] (ulepszenie 1) — opis] 파괴된 팔의 수만큼 스킬 위력 감소
   źródło: Skills_Abnormality.json :: dataList[id=802803].levelList[level=1].desc
   limit: do 120 znaków
   EN: Skill Power -1 for each broken arm
   PL:
25. [Umiejętność wroga [802803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed and 1 Paralyze next turn
   PL:
26. [Umiejętność wroga [802803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [802803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4, 마비 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=802803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed and 2 Paralyze next turn
   PL:
28. [Umiejętność wroga [802804] (ulepszenie 1) — nazwa] 양팔 후려치기
   źródło: Skills_Abnormality.json :: dataList[id=802804].levelList[level=1].name
   limit: do 40 znaków
   EN: Thrashing Arms
   PL:
29. [Umiejętność wroga [802804] (ulepszenie 1) — opis] [DefeatDuel] 본능을 1 잃음
   źródło: Skills_Abnormality.json :: dataList[id=802804].levelList[level=1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Umiejętność wroga [802804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 10. 다음 턴에 속박 5 부여.
   źródło: Skills_Abnormality.json :: dataList[id=802804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10; Inflict 5 Bind next turn
   PL:
31. [Umiejętność wroga [802805] (ulepszenie 1) — nazwa] 숨죽이기
   źródło: Skills_Abnormality.json :: dataList[id=802805].levelList[level=1].name
   limit: do 40 znaków
   EN: Held Breath
   PL:
32. [Umiejętność wroga [802805] (ulepszenie 1) — opis] [StartBattle] 본능을 1 얻음
   źródło: Skills_Abnormality.json :: dataList[id=802805].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 1 Instincts
   PL:
33. [Umiejętność wroga [802807] (ulepszenie 1) — nazwa] 고통의 몸부림
   źródło: Skills_Abnormality.json :: dataList[id=802807].levelList[level=1].name
   limit: do 40 znaków
   EN: Pained Writhing
   PL:
34. [Umiejętność wroga [802807] (ulepszenie 1) — opis] [WhenUse] 체력 12 소모. 다음 턴에 출혈 5를 얻음
   źródło: Skills_Abnormality.json :: dataList[id=802807].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 12 HP; Gain 5 Bleed next turn
   PL:
35. [Umiejętność wroga [802807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 독 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=802807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Poison next turn
   PL:
36. [Umiejętność wroga [802807] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 독 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=802807].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność wroga [802807] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 독 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=802807].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [802808] (ulepszenie 1) — nazwa] 고통의 발악
   źródło: Skills_Abnormality.json :: dataList[id=802808].levelList[level=1].name
   limit: do 40 znaków
   EN: Pained Struggle
   PL:
39. [Umiejętność wroga [802808] (ulepszenie 1) — opis] [WhenUse] 체력 12 소모. 다음 턴에 자신의 출혈 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=802808].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 12 HP; Gain +3 Bleed Count next turn
   PL:
40. [Umiejętność wroga [802808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 6 부여
   źródło: Skills_Abnormality.json :: dataList[id=802808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Paralyze next turn
   PL:
41. [Umiejętność wroga [802808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 6 부여
   źródło: Skills_Abnormality.json :: dataList[id=802808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność wroga [802902] (ulepszenie 1) — nazwa] 깊은 찌르기
   źródło: Skills_Abnormality.json :: dataList[id=802902].levelList[level=1].name
   limit: do 40 znaków
   EN: Deep Thrust
   PL:
43. [Umiejętność wroga [802902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 6 부여
   źródło: Skills_Abnormality.json :: dataList[id=802902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Bleed next turn
   PL:
44. [Umiejętność wroga [802903] (ulepszenie 1) — nazwa] 쥐어짐
   źródło: Skills_Abnormality.json :: dataList[id=802903].levelList[level=1].name
   limit: do 40 znaków
   EN: The Gripping
   PL:
45. [Umiejętność wroga [802903] (ulepszenie 1) — opis] [StartBattle] 다음 턴동안 대상을 주시함
   źródło: Skills_Abnormality.json :: dataList[id=802903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gazes into the target for the next turn
   PL:
46. [Umiejętność wroga [802904] (ulepszenie 1) — nazwa] 광소
   źródło: Skills_Abnormality.json :: dataList[id=802904].levelList[level=1].name
   limit: do 40 znaków
   EN: Cackle
   PL:
47. [Umiejętność wroga [802904] (ulepszenie 1) — opis] [WhenUse] 대상에게 정신피해 10
   źródło: Skills_Abnormality.json :: dataList[id=802904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Deal 10 SP damage
   PL:
48. [Umiejętność wroga [802904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Abnormality.json :: dataList[id=802904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Attack Power Up next turn
   PL:
49. [Umiejętność wroga [802905] (ulepszenie 1) — nazwa] 죄악을 꿰뚫는 못
   źródło: Skills_Abnormality.json :: dataList[id=802905].levelList[level=1].name
   limit: do 40 znaków
   EN: Sin-skewering Nail
   PL:
50. [Umiejętność wroga [802905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 N Corp’s Nails next turn
   PL:
51. [Umiejętność wroga [802905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [802905] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [802906] (ulepszenie 1) — nazwa] 정화
   źródło: Skills_Abnormality.json :: dataList[id=802906].levelList[level=1].name
   limit: do 40 znaków
   EN: Purify
   PL:
54. [Umiejętność wroga [802906] (ulepszenie 1) — opis] [WhenUse] 대상 체력이 30%미만이면 스킬 위력 +2
   źródło: Skills_Abnormality.json :: dataList[id=802906].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target’s HP is below 30%, Skill Power +2
   PL:
55. [Umiejętność wroga [802906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] N사의 못 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 N Corp’s Nails
   PL:
56. [Umiejętność wroga [802906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] N사의 못 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [802906] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] N사의 못 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802906].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność wroga [802906] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상에게 N사의 못이 5이상 있으면, 흐트러짐 상태로 만들고 N사의 못을 없앰
   źródło: Skills_Abnormality.json :: dataList[id=802906].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ N Corp’s Nails, Stagger them and remove the Nails
   PL:
59. [Umiejętność wroga [802907] (ulepszenie 1) — nazwa] 처단할지어다!
   źródło: Skills_Abnormality.json :: dataList[id=802907].levelList[level=1].name
   limit: do 40 znaków
   EN: I Shall Claim Your Life!
   PL:
60. [Umiejętność wroga [802907] (ulepszenie 1) — opis] [WhenUse] 대상 체력이 30%미만이면 스킬 위력 +2
   źródło: Skills_Abnormality.json :: dataList[id=802907].levelList[level=1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [802907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 못이 5이상 있으면, 흐트러짐 상태로 만듦
   źródło: Skills_Abnormality.json :: dataList[id=802907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Nails, Stagger them
   PL:
62. [Umiejętność wroga [802907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 못 수치X3만큼 피해를 주고 못을 없앰
   źródło: Skills_Abnormality.json :: dataList[id=802907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal damage by 3x Nails on target, then remove the Nails
   PL:
63. [Umiejętność wroga [802908] (ulepszenie 1) — nazwa] 처단할지어다!
   źródło: Skills_Abnormality.json :: dataList[id=802908].levelList[level=1].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [802908] (ulepszenie 1) — opis] [DefeatDuel] 흐트러짐 상태가 됨
   źródło: Skills_Abnormality.json :: dataList[id=802908].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] User becomes Staggered
   PL:
65. [Umiejętność wroga [802908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상을 흐트러짐 상태로 만들고, 다음 턴에 취약 10 부여
   źródło: Skills_Abnormality.json :: dataList[id=802908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target and inflict 10 Fragile next turn
   PL:
66. [Umiejętność wroga [802910] (ulepszenie 1) — nazwa] 가소로워
   źródło: Skills_Abnormality.json :: dataList[id=802910].levelList[level=1].name
   limit: do 40 znaków
   EN: You Are Nothing
   PL:
67. [Umiejętność wroga [802910] (ulepszenie 1) — opis] [OnSucceedEvade] 대상에게 정신피해 5
   źródło: Skills_Abnormality.json :: dataList[id=802910].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Deal 5 SP damage
   PL:
68. [Umiejętność wroga [803001] (ulepszenie 1) — nazwa] 첫 사람의 날개
   źródło: Skills_Abnormality.json :: dataList[id=803001].levelList[level=1].name
   limit: do 40 znaków
   EN: Protoplast’s Wings
   PL:
69. [Umiejętność wroga [803002] (ulepszenie 1) — nazwa] 첫 사람의 날개
   źródło: Skills_Abnormality.json :: dataList[id=803002].levelList[level=1].name
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [803003] (ulepszenie 1) — nazwa] 무구한 날개짓
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].name
   limit: do 40 znaków
   EN: Innocent Flutters
   PL:
71. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL:
72. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL:
73. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność wroga [803003] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803003].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność wroga [803004] (ulepszenie 1) — nazwa] 부러진 날개
   źródło: Skills_Abnormality.json :: dataList[id=803004].levelList[level=1].name
   limit: do 40 znaków
   EN: Broken Wings
   PL:
80. [Umiejętność wroga [803004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność wroga [803004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność wroga [803004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [803004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [803005] (ulepszenie 1) — nazwa] 부러진 날개
   źródło: Skills_Abnormality.json :: dataList[id=803005].levelList[level=1].name
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [803005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [803005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [803005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [803005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność wroga [803006] (ulepszenie 1) — nazwa] 격노한 날개짓
   źródło: Skills_Abnormality.json :: dataList[id=803006].levelList[level=1].name
   limit: do 40 znaków
   EN: Enraged Flutters
   PL:
90. [Umiejętność wroga [803007] (ulepszenie 1) — nazwa] 고결한 정화
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].name
   limit: do 40 znaków
   EN: Noble Purification
   PL:
91. [Umiejętność wroga [803007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność wroga [803007] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Umiejętność wroga [803007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność wroga [803007] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [803007] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność wroga [803007] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803007].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Umiejętność wroga [803008] (ulepszenie 1) — nazwa] 영예로운 쥐어짐
   źródło: Skills_Abnormality.json :: dataList[id=803008].levelList[level=1].name
   limit: do 40 znaków
   EN: Honorable Grip
   PL:
98. [Umiejętność wroga [803008] (ulepszenie 1) — opis] [WhenUse] 대상의 체력이 30%미만이면 피해량 +100%
   źródło: Skills_Abnormality.json :: dataList[id=803008].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target’s HP is below 30%, +100% Damage
   PL:
99. [Umiejętność wroga [803008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 체력이 30% 미만이면 즉시 처치하고, 체력을 30 회복\n다음 턴에 공격 위력 증가를 2 얻음
   źródło: Skills_Abnormality.json :: dataList[id=803008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target’s HP is below 30%, kill them and heal 30 HP\nGain 2 Attack Power Up next turn
   PL:
100. [Umiejętność wroga [803009] (ulepszenie 1) — nazwa] 참회하라!!
   źródło: Skills_Abnormality.json :: dataList[id=803009].levelList[level=1].name
   limit: do 40 znaków
   EN: Repent!!
   PL:
101. [Umiejętność wroga [803009] (ulepszenie 1) — opis] [WhenUse] 대상의 체력이 30%미만이면 피해량 +100%
   źródło: Skills_Abnormality.json :: dataList[id=803009].levelList[level=1].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Umiejętność wroga [803009] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803009].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Fragile next turn
   PL:
103. [Umiejętność wroga [803009] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803009].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed next turn
   PL:
104. [Umiejętność wroga [803010] (ulepszenie 1) — nazwa] 온전한 살덩이
   źródło: Skills_Abnormality.json :: dataList[id=803010].levelList[level=1].name
   limit: do 40 znaków
   EN: Peerless Flesh
   PL:
105. [Umiejętność wroga [803101] (ulepszenie 1) — nazwa] 손뼉치기
   źródło: Skills_Abnormality.json :: dataList[id=803101].levelList[level=1].name
   limit: do 40 znaków
   EN: Clap
   PL:
106. [Umiejętność wroga [803101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Attack Power Down next turn
   PL:
107. [Umiejętność wroga [803102] (ulepszenie 1) — nazwa] 강한 손뼉치기
   źródło: Skills_Abnormality.json :: dataList[id=803102].levelList[level=1].name
   limit: do 40 znaków
   EN: Powerful Clap
   PL:
108. [Umiejętność wroga [803102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 위력 감소 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Attack Power Down next turn
   PL:
109. [Umiejętność wroga [803103] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality.json :: dataList[id=803103].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Whip
   PL:
110. [Umiejętność wroga [803103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Umiejętność wroga [803103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Fragile next turn
   PL:
112. [Umiejętność wroga [803104] (ulepszenie 1) — nazwa] 주머니 압박
   źródło: Skills_Abnormality.json :: dataList[id=803104].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressing Sac
   PL:
113. [Umiejętność wroga [803104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL:
114. [Umiejętność wroga [803105] (ulepszenie 1) — nazwa] 혈사포
   źródło: Skills_Abnormality.json :: dataList[id=803105].levelList[level=1].name
   limit: do 40 znaków
   EN: Blood Cannon
   PL:
115. [Umiejętność wroga [803105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed
   PL:
116. [Umiejętność wroga [803105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 20 부여
   źródło: Skills_Abnormality.json :: dataList[id=803105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 20 Bleed
   PL:
117. [Umiejętność wroga [803106] (ulepszenie 1) — nazwa] 종혈
   źródło: Skills_Abnormality.json :: dataList[id=803106].levelList[level=1].name
   limit: do 40 znaków
   EN: Clotting
   PL:
118. [Umiejętność wroga [803106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 30 부여
   źródło: Skills_Abnormality.json :: dataList[id=803106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 30 Bleed
   PL:
119. [Umiejętność wroga [803201] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality.json :: dataList[id=803201].levelList[level=1].name
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [803201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed next turn
   PL:
121. [Umiejętność wroga [803202] (ulepszenie 1) — nazwa] 등압
   źródło: Skills_Abnormality.json :: dataList[id=803202].levelList[level=1].name
   limit: do 40 znaków
   EN: Constant Voltage
   PL:
122. [Umiejętność wroga [803202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 1 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture next turn
   PL:
123. [Umiejętność wroga [803203] (ulepszenie 1) — nazwa] 등압추격
   źródło: Skills_Abnormality.json :: dataList[id=803203].levelList[level=1].name
   limit: do 40 znaków
   EN: Electromotive Pursuit
   PL:
124. [Umiejętność wroga [803203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 1 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [803203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 4 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Rupture next turn
   PL:
126. [Umiejętność wroga [803204] (ulepszenie 1) — nazwa] 하울링
   źródło: Skills_Abnormality.json :: dataList[id=803204].levelList[level=1].name
   limit: do 40 znaków
   EN: Howl
   PL:
127. [Umiejętność wroga [803204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL:
128. [Umiejętność wroga [803204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 수비 위력 감소 4 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Defense Power Down
   PL:
129. [Umiejętność wroga [803205] (ulepszenie 1) — nazwa] 전격 하울링
   źródło: Skills_Abnormality.json :: dataList[id=803205].levelList[level=1].name
   limit: do 40 znaków
   EN: Electrified Howl
   PL:
130. [Umiejętność wroga [803205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 3 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Rupture next turn
   PL:
131. [Umiejętność wroga [803206] (ulepszenie 1) — nazwa] 피뢰
   źródło: Skills_Abnormality.json :: dataList[id=803206].levelList[level=1].name
   limit: do 40 znaków
   EN: Lightning Rod
   PL:
132. [Umiejętność wroga [803206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture next turn
   PL:
133. [Umiejętność wroga [803206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 파열 5 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture next turn
   PL:
134. [Umiejętność wroga [803207] (ulepszenie 1) — nazwa] 적뢰
   źródło: Skills_Abnormality.json :: dataList[id=803207].levelList[level=1].name
   limit: do 40 znaków
   EN: Red Bolts
   PL:
135. [Umiejętność wroga [803207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 10 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Rupture next turn
   PL:
136. [Umiejętność wroga [803208] (ulepszenie 1) — nazwa] 하울링
   źródło: Skills_Abnormality.json :: dataList[id=803208].levelList[level=1].name
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [803208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL:
138. [Umiejętność wroga [803208] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 수비 위력 감소 4 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803208].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [803301] (ulepszenie 1) — nazwa] 휘감는 팔
   źródło: Skills_Abnormality.json :: dataList[id=803301].levelList[level=1].name
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [803301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [803302] (ulepszenie 1) — nazwa] 휘두르기
   źródło: Skills_Abnormality.json :: dataList[id=803302].levelList[level=1].name
   limit: do 40 znaków
   EN: Swipe
   PL:
142. [Umiejętność wroga [803302] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=803302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Attack Power Up next turn
   PL:
143. [Umiejętność wroga [803302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 3, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed and 1 Paralyze next turn
   PL:
144. [Umiejętność wroga [803302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 3, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [803303] (ulepszenie 1) — nazwa] 후려치기
   źródło: Skills_Abnormality.json :: dataList[id=803303].levelList[level=1].name
   limit: do 40 znaków
   EN: Thwack
   PL:
146. [Umiejętność wroga [803303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여.
   źródło: Skills_Abnormality.json :: dataList[id=803303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL:
147. [Umiejętność wroga [803304] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality.json :: dataList[id=803304].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL:
148. [Umiejętność wroga [803305] (ulepszenie 1) — nazwa] 독액 뿜기
   źródło: Skills_Abnormality.json :: dataList[id=803305].levelList[level=1].name
   limit: do 40 znaków
   EN: Poison Spray
   PL:
149. [Umiejętność wroga [803305] (ulepszenie 1) — opis] [WhenUse]체력 6 소모. 다음 턴에 출혈 5를 얻음
   źródło: Skills_Abnormality.json :: dataList[id=803305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 6 HP; Gain 5 Bleed next turn
   PL:
150. [Umiejętność wroga [803305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 독 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [803305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 독 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność wroga [803401] (ulepszenie 1) — nazwa] 꼬고고곡
   źródło: Skills_Abnormality.json :: dataList[id=803401].levelList[level=1].name
   limit: do 40 znaków
   EN: Bawkbawbawbawk
   PL:
153. [Umiejętność wroga [803401] (ulepszenie 1) — opis] 정신력이 가장 낮은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803401].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the least SP
   PL:
154. [Umiejętność wroga [803401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality.json :: dataList[id=803401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL:
155. [Umiejętność wroga [803402] (ulepszenie 1) — nazwa] 꼬고곡
   źródło: Skills_Abnormality.json :: dataList[id=803402].levelList[level=1].name
   limit: do 40 znaków
   EN: Babawbawk
   PL:
156. [Umiejętność wroga [803402] (ulepszenie 1) — opis] 정신력이 가장 낮은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803402].levelList[level=1].desc
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Umiejętność wroga [803402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality.json :: dataList[id=803402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 7 HP
   PL:
158. [Umiejętność wroga [803402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 침잠 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Sinking
   PL:
159. [Umiejętność wroga [803403] (ulepszenie 1) — nazwa] 끄그극
   źródło: Skills_Abnormality.json :: dataList[id=803403].levelList[level=1].name
   limit: do 40 znaków
   EN: Keghgh
   PL:
160. [Umiejętność wroga [803403] (ulepszenie 1) — opis] 이번 턴동안 피해를 당하지 않았다면, 다음 턴에 모든 아군에게 공격 위력 증가 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803403].levelList[level=1].desc
   limit: do 120 znaków
   EN: If user doesn’t take damage this turn, apply 2 Attack Power Up to all allies next turn
   PL:
161. [Umiejętność wroga [803501] (ulepszenie 1) — nazwa] 꼬오곡
   źródło: Skills_Abnormality.json :: dataList[id=803501].levelList[level=1].name
   limit: do 40 znaków
   EN: Baaawkbawk
   PL:
162. [Umiejętność wroga [803501] (ulepszenie 1) — opis] 체력이 가장 낮은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803501].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the least HP
   PL:
163. [Umiejętność wroga [803501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=803501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Fragile
   PL:
164. [Umiejętność wroga [803502] (ulepszenie 1) — nazwa] 꼬고꼭
   źródło: Skills_Abnormality.json :: dataList[id=803502].levelList[level=1].name
   limit: do 40 znaków
   EN: Bawkbabawk
   PL:
165. [Umiejętność wroga [803502] (ulepszenie 1) — opis] 체력이 가장 낮은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803502].levelList[level=1].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność wroga [803502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality.json :: dataList[id=803502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [803502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 출혈 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Bleed
   PL:
168. [Umiejętność wroga [803503] (ulepszenie 1) — nazwa] 끄극
   źródło: Skills_Abnormality.json :: dataList[id=803503].levelList[level=1].name
   limit: do 40 znaków
   EN: Khgh
   PL:
169. [Umiejętność wroga [803503] (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 -15
   źródło: Skills_Abnormality.json :: dataList[id=803503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 15 SP
   PL:
170. [Umiejętność wroga [803601] (ulepszenie 1) — nazwa] 끄끄끅!
   źródło: Skills_Abnormality.json :: dataList[id=803601].levelList[level=1].name
   limit: do 40 znaków
   EN: Khghgh!
   PL:
171. [Umiejętność wroga [803601] (ulepszenie 1) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +3
   źródło: Skills_Abnormality.json :: dataList[id=803601].levelList[level=1].desc
   limit: do 120 znaków
   EN: If user took no damage last turn, Coin Power +3
   PL:
172. [Umiejętność wroga [803601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 3 얻음
   źródło: Skills_Abnormality.json :: dataList[id=803601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 3 Haste next turn
   PL:
173. [Umiejętność wroga [803602] (ulepszenie 1) — nazwa] 끄끄옥!
   źródło: Skills_Abnormality.json :: dataList[id=803602].levelList[level=1].name
   limit: do 40 znaków
   EN: Kawkbaawk!
   PL:
174. [Umiejętność wroga [803602] (ulepszenie 1) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +3
   źródło: Skills_Abnormality.json :: dataList[id=803602].levelList[level=1].desc
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Umiejętność wroga [803602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality.json :: dataList[id=803602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Umiejętność wroga [803602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 마비 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Paralyze next turn
   PL:
177. [Umiejętność wroga [803603] (ulepszenie 1) — nazwa] 끄극!
   źródło: Skills_Abnormality.json :: dataList[id=803603].levelList[level=1].name
   limit: do 40 znaków
   EN: Krgh!
   PL:
178. [Umiejętność wroga [803701] (ulepszenie 1) — nazwa] 끄극
   źródło: Skills_Abnormality.json :: dataList[id=803701].levelList[level=1].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [803701] (ulepszenie 1) — opis] 체력이 가장 높은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803701].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the most HP
   PL:
180. [Umiejętność wroga [803701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=803701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Paralyze
   PL:
181. [Umiejętność wroga [803702] (ulepszenie 1) — nazwa] 끄꾸우곡
   źródło: Skills_Abnormality.json :: dataList[id=803702].levelList[level=1].name
   limit: do 40 znaków
   EN: Khgaawahk
   PL:
182. [Umiejętność wroga [803702] (ulepszenie 1) — opis] 체력이 가장 높은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803702].levelList[level=1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [803702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality.json :: dataList[id=803702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [803702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL:
185. [Umiejętność wroga [803703] (ulepszenie 1) — nazwa] 끅!
   źródło: Skills_Abnormality.json :: dataList[id=803703].levelList[level=1].name
   limit: do 40 znaków
   EN: Khk!
   PL:
186. [Umiejętność wroga [803801] (ulepszenie 1) — nazwa] 끄!
   źródło: Skills_Abnormality.json :: dataList[id=803801].levelList[level=1].name
   limit: do 40 znaków
   EN: Kgh!
   PL:
187. [Umiejętność wroga [803801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bleed
   PL:
188. [Umiejętność wroga [803801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
189. [Umiejętność wroga [803802] (ulepszenie 1) — nazwa] 끄극!
   źródło: Skills_Abnormality.json :: dataList[id=803802].levelList[level=1].name
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność wroga [803802] (ulepszenie 1) — opis] 정신력이 가장 낮은 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=803802].levelList[level=1].desc
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [803802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [803803] (ulepszenie 1) — nazwa] 끄극...
   źródło: Skills_Abnormality.json :: dataList[id=803803].levelList[level=1].name
   limit: do 40 znaków
   EN: Krgh…
   PL:
193. [Umiejętność wroga [803901] (ulepszenie 1) — nazwa] 끄!
   źródło: Skills_Abnormality.json :: dataList[id=803901].levelList[level=1].name
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [803901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
195. [Umiejętność wroga [803901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Tremor
   PL:
196. [Umiejętność wroga [803902] (ulepszenie 1) — nazwa] 끅
   źródło: Skills_Abnormality.json :: dataList[id=803902].levelList[level=1].name
   limit: do 40 znaków
   EN: Khk
   PL:
197. [Umiejętność wroga [803902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [803902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=803902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 195 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [803902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마비 1, 진동 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze and 5 Tremor
   PL:
200. [Umiejętność wroga [803902] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Abnormality.json :: dataList[id=803902].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL:
201. [Umiejętność wroga [803903] (ulepszenie 1) — nazwa] 끄그극!
   źródło: Skills_Abnormality.json :: dataList[id=803903].levelList[level=1].name
   limit: do 40 znaków
   EN: Keghgh!
   PL:
202. [Umiejętność wroga [803903] (ulepszenie 1) — opis] 정신력이 가장 낮은 대상 우선 공격\n적중 시 생닭 생산
   źródło: Skills_Abnormality.json :: dataList[id=803903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Targets the unit with the least SP\n[OnSucceedAttack] Spawn a Raw Chicken
   PL:
203. [Umiejętność wroga [803903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Sinking
   PL:
204. [Umiejętność wroga [803904] (ulepszenie 1) — nazwa] 끄그그그극
   źródło: Skills_Abnormality.json :: dataList[id=803904].levelList[level=1].name
   limit: do 40 znaków
   EN: Khghghghgk
   PL:
205. [Umiejętność wroga [803904] (ulepszenie 1) — opis] [WinDuel] 최종 위력 + 1
   źródło: Skills_Abnormality.json :: dataList[id=803904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Final Power +1
   PL:
206. [Umiejętność wroga [803904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=803904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [803904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Abnormality.json :: dataList[id=803904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [803905] (ulepszenie 1) — nazwa] 끄그극...
   źródło: Skills_Abnormality.json :: dataList[id=803905].levelList[level=1].name
   limit: do 40 znaków
   EN: Keghgh…
   PL:
209. [Umiejętność wroga [804101] (ulepszenie 1) — nazwa] 들이받기
   źródło: Skills_Abnormality.json :: dataList[id=804101].levelList[level=1].name
   limit: do 40 znaków
   EN: Ram
   PL:
210. [Umiejętność wroga [804101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Burn
   PL:
211. [Umiejętność wroga [804101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [804102] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Abnormality.json :: dataList[id=804102].levelList[level=1].name
   limit: do 40 znaków
   EN: Pin Down
   PL:
213. [Umiejętność wroga [804102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=804102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Burn Count
   PL:
214. [Umiejętność wroga [804103] (ulepszenie 1) — nazwa] 돌진
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge In
   PL:
215. [Umiejętność wroga [804103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn
   PL:
216. [Umiejętność wroga [804103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL:
217. [Umiejętność wroga [804103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [804103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [804103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [804103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Abnormality.json :: dataList[id=804103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [804104] (ulepszenie 1) — nazwa] 넘쳐흐르는 슬픔
   źródło: Skills_Abnormality.json :: dataList[id=804104].levelList[level=1].name
   limit: do 40 znaków
   EN: Overflowing Sorrow
   PL:
222. [Umiejętność wroga [804104] (ulepszenie 1) — opis] [DefeatDuel] 해소되지 않은 슬픔 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 1 Unresolved Sorrow
   PL:
223. [Umiejętność wroga [804104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 15 감소
   źródło: Skills_Abnormality.json :: dataList[id=804104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 15 SP
   PL:
224. [Umiejętność wroga [804104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 대상의 흐트러짐 손상
   źródło: Skills_Abnormality.json :: dataList[id=804104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 50% of damage dealt
   PL:
225. [Umiejętność wroga [804105] (ulepszenie 1) — nazwa] 뜨거운 울음소리
   źródło: Skills_Abnormality.json :: dataList[id=804105].levelList[level=1].name
   limit: do 40 znaków
   EN: Heated Cries
   PL:
226. [Umiejętność wroga [804105] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 신속, 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Haste and 1 Attack Power Up next turn
   PL:
227. [Umiejętność wroga [804105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 울렁이는 감정 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Wavering Emotions
   PL:
228. [Umiejętność wroga [804105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=804105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Sinking Count
   PL:
229. [Umiejętność wroga [804106] (ulepszenie 1) — nazwa] 뜨거운 비명소리
   źródło: Skills_Abnormality.json :: dataList[id=804106].levelList[level=1].name
   limit: do 40 znaków
   EN: Heated Screams
   PL:
230. [Umiejętność wroga [804106] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 신속, 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804106].levelList[level=1].desc
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [804106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 울렁이는 감정 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność wroga [804106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Sinking
   PL:
233. [Umiejętność wroga [804106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 울렁이는 감정 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [804106] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804106].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [804201] (ulepszenie 1) — nazwa] 섬광 섬광
   źródło: Skills_Abnormality.json :: dataList[id=804201].levelList[level=1].name
   limit: do 40 znaków
   EN: Flash; Flash;
   PL:
236. [Umiejętność wroga [804202] (ulepszenie 1) — nazwa] 스캔합니다
   źródło: Skills_Abnormality.json :: dataList[id=804202].levelList[level=1].name
   limit: do 40 znaków
   EN: Scanning . . .
   PL:
237. [Umiejętność wroga [804203] (ulepszenie 1) — nazwa] 근접 촬영 시작
   źródło: Skills_Abnormality.json :: dataList[id=804203].levelList[level=1].name
   limit: do 40 znaków
   EN: Proximity Shooting
   PL:
238. [Umiejętność wroga [804501] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Abnormality.json :: dataList[id=804501].levelList[level=1].name
   limit: do 40 znaków
   EN: Bite
   PL:
239. [Umiejętność wroga [804501] (ulepszenie 1) — opis] [WhenUse] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality.json :: dataList[id=804501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 2 Self-charge\n[DefeatDuel] Lose 1 Self-charge
   PL:
240. [Umiejętność wroga [804501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여, 출혈 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed and +2 Bleed Count
   PL:
241. [Umiejętność wroga [804502] (ulepszenie 1) — nazwa] 꼬리찌르기
   źródło: Skills_Abnormality.json :: dataList[id=804502].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Poke
   PL:
242. [Umiejętność wroga [804502] (ulepszenie 1) — opis] [WhenUse] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality.json :: dataList[id=804502].levelList[level=1].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [804502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여, 출혈 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [804502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [804503] (ulepszenie 1) — nazwa] 감아 조이기
   źródło: Skills_Abnormality.json :: dataList[id=804503].levelList[level=1].name
   limit: do 40 znaków
   EN: Wrapping Coil
   PL:
246. [Umiejętność wroga [804503] (ulepszenie 1) — opis] [WhenUse] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality.json :: dataList[id=804503].levelList[level=1].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [804503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile
   PL:
248. [Umiejętność wroga [804503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bind next turn
   PL:
249. [Umiejętność wroga [804504] (ulepszenie 1) — nazwa] 전류 주입
   źródło: Skills_Abnormality.json :: dataList[id=804504].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Load
   PL:
250. [Umiejętność wroga [804504] (ulepszenie 1) — opis] [WhenUse] 자가 충전 1 얻음\n대상에게 마비가 있다면 피해량 +10%
   źródło: Skills_Abnormality.json :: dataList[id=804504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Self-charge\nDeal +10% damage to targets with Paralyze
   PL:
251. [Umiejętność wroga [804504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [804505] (ulepszenie 1) — nazwa] 전기 방류
   źródło: Skills_Abnormality.json :: dataList[id=804505].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Release
   PL:
253. [Umiejętność wroga [804505] (ulepszenie 1) — opis] [WhenUse] 자가 충전 1 얻음\n대상에게 마비가 있다면 피해량 +10%
   źródło: Skills_Abnormality.json :: dataList[id=804505].levelList[level=1].desc
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [804505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [804506] (ulepszenie 1) — nazwa] 전기 방출
   źródło: Skills_Abnormality.json :: dataList[id=804506].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Discharge
   PL:
256. [Umiejętność wroga [804506] (ulepszenie 1) — opis] [WhenUse] 자가 충전 1 얻음\n대상에게 마비가 있다면 피해량 +20%
   źródło: Skills_Abnormality.json :: dataList[id=804506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Self-charge\nDeal +20% damage to targets with Paralyze
   PL:
257. [Umiejętność wroga [804506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [804506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze
   PL:
259. [Umiejętność wroga [804507] (ulepszenie 1) — nazwa] 초고압 전기 방출
   źródło: Skills_Abnormality.json :: dataList[id=804507].levelList[level=1].name
   limit: do 50 znaków
   EN: High-voltage Electric Discharge
   PL:
260. [Umiejętność wroga [804507] (ulepszenie 1) — opis] 가지고 있는 자가 충전 전부 소모
   źródło: Skills_Abnormality.json :: dataList[id=804507].levelList[level=1].desc
   limit: do 120 znaków
   EN: Spend all Self-charge
   PL:
261. [Umiejętność wroga [804507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność wroga [804507] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 축전 상태일 때, 최종 피해량의 40%만큼 고정 피해
   źródło: Skills_Abnormality.json :: dataList[id=804507].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Capacitor, deal 40% of damage dealt as fixed damage
   PL:
263. [Umiejętność wroga [804507] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마비 3, 축전 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804507].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze and 1 Capacitor
   PL:
264. [Umiejętność wroga [804508] (ulepszenie 1) — nazwa] 똬리틀기
   źródło: Skills_Abnormality.json :: dataList[id=804508].levelList[level=1].name
   limit: do 40 znaków
   EN: Coil Up
   PL:
265. [Umiejętność wroga [804508] (ulepszenie 1) — opis] 이 스킬이 슬롯에 있을 때 머리 부위 현재 체력만큼 보호막 얻음.
   źródło: Skills_Abnormality.json :: dataList[id=804508].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this skill is on a slot, gain shield by the head's current HP
   PL:
266. [Umiejętność wroga [804509] (ulepszenie 1) — nazwa] 꿈틀거리는 머리
   źródło: Skills_Abnormality.json :: dataList[id=804509].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Head
   PL:
267. [Umiejętność wroga [804509] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n[WhenUse] 자가 충전 2 소모\n[DefeatDuel] 자가 충전 2 소모
   źródło: Skills_Abnormality.json :: dataList[id=804509].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy with the least HP\n[WhenUse] Spend 2 Self-charge\n[DefeatDuel] Lose 2 Self-charge
   PL:
268. [Umiejętność wroga [804509] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804509].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [804510] (ulepszenie 1) — nazwa] 꿈틀거리는 꼬리
   źródło: Skills_Abnormality.json :: dataList[id=804510].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Tail
   PL:
270. [Umiejętność wroga [804510] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n[WhenUse] 자가 충전 2 소모\n[DefeatDuel] 자가 충전 3 소모
   źródło: Skills_Abnormality.json :: dataList[id=804510].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy with the least HP\n[WhenUse] Spend 2 Self-charge\n[DefeatDuel] Lose 3 Self-charge
   PL:
271. [Umiejętność wroga [804510] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804510].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [804601] (ulepszenie 1) — nazwa] 침울한 신음
   źródło: Skills_Abnormality.json :: dataList[id=804601].levelList[level=1].name
   limit: do 40 znaków
   EN: Gloomy Moan
   PL:
273. [Umiejętność wroga [804601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL:
274. [Umiejętność wroga [804602] (ulepszenie 1) — nazwa] 몰아치는 침잠
   źródło: Skills_Abnormality.json :: dataList[id=804602].levelList[level=1].name
   limit: do 40 znaków
   EN: Raging Withdrawal
   PL:
275. [Umiejętność wroga [804602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL:
276. [Umiejętność wroga [804602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [804603] (ulepszenie 1) — nazwa] 슬픔의 반동
   źródło: Skills_Abnormality.json :: dataList[id=804603].levelList[level=1].name
   limit: do 40 znaków
   EN: Sorrowful Recoil
   PL:
278. [Umiejętność wroga [804603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=804603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count
   PL:
279. [Umiejętność wroga [804603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
280. [Umiejętność wroga [804604] (ulepszenie 1) — nazwa] 슬픔의 격류
   źródło: Skills_Abnormality.json :: dataList[id=804604].levelList[level=1].name
   limit: do 40 znaków
   EN: Sorrowful Torrent
   PL:
281. [Umiejętność wroga [804604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL:
282. [Umiejętność wroga [804604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [804604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
284. [Umiejętność wroga [804605] (ulepszenie 1) — nazwa] 무언가를 찾는 울음소리
   źródło: Skills_Abnormality.json :: dataList[id=804605].levelList[level=1].name
   limit: do 40 znaków
   EN: Cries Seeking Something
   PL:
285. [Umiejętność wroga [804605] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 낡은 우산 소환
   źródło: Skills_Abnormality.json :: dataList[id=804605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Spawn an Old Umbrella next turn
   PL:
286. [Umiejętność wroga [804605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [804605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 낡은 우산 수만큼 가하는 피해량 +15%
   źródło: Skills_Abnormality.json :: dataList[id=804605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal +15% damage for each Old Umbrella
   PL:
288. [Umiejętność wroga [804606] (ulepszenie 1) — nazwa] 기다림
   źródło: Skills_Abnormality.json :: dataList[id=804606].levelList[level=1].name
   limit: do 40 znaków
   EN: Waiting
   PL:
289. [Umiejętność wroga [804606] (ulepszenie 1) — opis] [StartBattle] 모든 적 정신력 -20
   źródło: Skills_Abnormality.json :: dataList[id=804606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] All enemies lose 20 SP
   PL:
290. [Umiejętność wroga [804701] (ulepszenie 1) — nazwa] 얽혀가는 부적
   źródło: Skills_Abnormality.json :: dataList[id=804701].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangling Talisman
   PL:
291. [Umiejętność wroga [804701] (ulepszenie 1) — opis] [WhenUse] 대상에게 얽혀온 저주 부적 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 2 Entangled Curse Talisman
   PL:
292. [Umiejętność wroga [804701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여. 파열 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture and +2 Rupture Count next turn
   PL:
293. [Umiejętność wroga [804702] (ulepszenie 1) — nazwa] 쌓여가는 저주
   źródło: Skills_Abnormality.json :: dataList[id=804702].levelList[level=1].name
   limit: do 40 znaków
   EN: Cumulating Curse
   PL:
294. [Umiejętność wroga [804702] (ulepszenie 1) — opis] [WhenUse] 대상에게 얽혀온 저주 부적 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 1 Entangled Curse Talisman
   PL:
295. [Umiejętność wroga [804702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 가지고 있는 얽혀온 저주 부적 만큼 얽혀온 저주 부적 부여
   źródło: Skills_Abnormality.json :: dataList[id=804702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Entangled Curse Talisman by target's Entangled Curse Talisman
   PL:
296. [Umiejętność wroga [804702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture next turn
   PL:
297. [Umiejętność wroga [804702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 2 부여. 다음 턴에 파열 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture and +2 Rupture Count next turn
   PL:
298. [Umiejętność wroga [804703] (ulepszenie 1) — nazwa] 누구도 울지 않도록
   źródło: Skills_Abnormality.json :: dataList[id=804703].levelList[level=1].name
   limit: do 40 znaków
   EN: So That No One Will Cry
   PL:
299. [Umiejętność wroga [804703] (ulepszenie 1) — opis] [EndBattle] 다시 붙여진 저주 부적 전부 소멸
   źródło: Skills_Abnormality.json :: dataList[id=804703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Remove all Reattached Curse Talisman
   PL:
300. [Umiejętność wroga [804703] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804703].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze next turn
   PL:
301. [Umiejętność wroga [804703] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 속박 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804703].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Bind next turn
   PL:
302. [Umiejętność wroga [804704] (ulepszenie 1) — nazwa] 이전하는 부적
   źródło: Skills_Abnormality.json :: dataList[id=804704].levelList[level=1].name
   limit: do 40 znaków
   EN: Transferring Talisman
   PL:
303. [Umiejętność wroga [804704] (ulepszenie 1) — opis] [WhenUse] 대상의 얽혀온 저주 부적 을 전부 소멸. 소멸시킨만큼 다시 붙여진 저주 부적 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804704].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Remove all Entangled Curse Talisman from target; Gain the same amount of Reattached Curse Talisman
   PL:
304. [Umiejętność wroga [804705] (ulepszenie 1) — nazwa] 복제되는 저주
   źródło: Skills_Abnormality.json :: dataList[id=804705].levelList[level=1].name
   limit: do 40 znaków
   EN: Proliferating Curse
   PL:
305. [Umiejętność wroga [804705] (ulepszenie 1) — opis] [WhenUse] 대상이 가지고 있는 얽혀온 저주 부적 만큼 얽혀온 저주 부적 부여
   źródło: Skills_Abnormality.json :: dataList[id=804705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict Entangled Curse Talisman by target's Entangled Curse Talisman
   PL:
306. [Umiejętność wroga [804801] (ulepszenie 1) — nazwa] 취하고 싶나?
   źródło: Skills_Abnormality.json :: dataList[id=804801].levelList[level=1].name
   limit: do 40 znaków
   EN: Wanna Get Drunk?
   PL:
307. [Umiejętność wroga [804801] (ulepszenie 1) — opis] 합 진행 시 고양 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804801].levelList[level=1].desc
   limit: do 120 znaków
   EN: In a clash, give 1 Morale Boost
   PL:
308. [Umiejętność wroga [804801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여, 진동 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Tremor and +2 Tremor Count
   PL:
309. [Umiejętność wroga [804802] (ulepszenie 1) — nazwa] 나눠 마시자!
   źródło: Skills_Abnormality.json :: dataList[id=804802].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Share the Drink!
   PL:
310. [Umiejętność wroga [804802] (ulepszenie 1) — opis] 합 진행 시 고양 1 부여\n[WhenUse] 체력 5% 회복
   źródło: Skills_Abnormality.json :: dataList[id=804802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: In a clash, give 1 Morale Boost\n[WhenUse] Heal 5% HP
   PL:
311. [Umiejętność wroga [804802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Umiejętność wroga [804803] (ulepszenie 1) — nazwa] 남은건 이것 뿐이네!
   źródło: Skills_Abnormality.json :: dataList[id=804803].levelList[level=1].name
   limit: do 40 znaków
   EN: This is All I Got!
   PL:
313. [Umiejętność wroga [804803] (ulepszenie 1) — opis] 합 진행 시 고양 2 부여\n진동을 가진 대상 우선 공격
   źródło: Skills_Abnormality.json :: dataList[id=804803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a Clash, give 2 Morale Boost\nPrioritizes enemies with Tremor
   PL:
314. [Umiejętność wroga [804803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 진동 횟수만큼 진동 폭발
   źródło: Skills_Abnormality.json :: dataList[id=804803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst by target's Tremor Count
   PL:
315. [Umiejętność wroga [804804] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality.json :: dataList[id=804804].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Have This!
   PL:
316. [Umiejętność wroga [804804] (ulepszenie 1) — opis] [CantDuel]\n대상 변경 불가.\n고양 을 가진 대상 우선 공격\n대상에게 취기 가 없다면, 합 위력 +5
   źródło: Skills_Abnormality.json :: dataList[id=804804].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nCannot be redirected\nPrioritizes enemies with Morale Boost\nIf target has no Tipsy, Clash Power +5
   PL:
317. [Umiejętność wroga [804804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 고양을 가지고 있다면, 고양 만큼 피해량 +10%
   źródło: Skills_Abnormality.json :: dataList[id=804804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Morale Boost, deal +10% damage for each Count
   PL:
318. [Umiejętność wroga [804804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 취기 를 가지고 있다면, 주는 피해가 0이 되고 자신의 체력 -50
   źródło: Skills_Abnormality.json :: dataList[id=804804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Tipsy, deal 0 damage, and user loses 50 HP
   PL:
319. [Umiejętność wroga [804804] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 고양 혹은 취기 전부 소모 시킴
   źródło: Skills_Abnormality.json :: dataList[id=804804].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove all Morale Boost or Tipsy
   PL:
320. [Umiejętność wroga [804805] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality.json :: dataList[id=804805].levelList[level=1].name
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Umiejętność wroga [804805] (ulepszenie 1) — opis] 고양을 가진 대상 우선 공격\n대상에게 취기 가 없다면, 합 위력 +5
   źródło: Skills_Abnormality.json :: dataList[id=804805].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritizes enemies with Morale Boost\nIf target has no Tipsy, Clash Power +5
   PL:
322. [Umiejętność wroga [804805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 고양 을 가지고 있다면, 고양 만큼 피해량 +100%
   źródło: Skills_Abnormality.json :: dataList[id=804805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Morale Boost, deal +100% damage for each Count
   PL:
323. [Umiejętność wroga [804805] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 취기 를 가지고 있다면, 주는 피해가 0이 되고 자신의 체력 -50
   źródło: Skills_Abnormality.json :: dataList[id=804805].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [804805] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 고양 혹은 취기 전부 소모 시킴
   źródło: Skills_Abnormality.json :: dataList[id=804805].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność wroga [804806] (ulepszenie 1) — nazwa] 이번에는 안돼!
   źródło: Skills_Abnormality.json :: dataList[id=804806].levelList[level=1].name
   limit: do 40 znaków
   EN: Not This Time!
   PL:
326. [Umiejętność wroga [804806] (ulepszenie 1) — opis] 요정주 우선 대상 공격
   źródło: Skills_Abnormality.json :: dataList[id=804806].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes Fairy Wine
   PL:
327. [Umiejętność wroga [804806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 요정주를 공격했다면, 다음 턴에 체력 10% 회복, 공격 위력 증가 2, 신속 2, 보호 2를 얻음.
   źródło: Skills_Abnormality.json :: dataList[id=804806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this attacks Fairy Wine, heal 10% HP next turn, and gain 2 Attack Power Up, 2 Haste, and 2 Protection
   PL:
328. [Umiejętność wroga [804807] (ulepszenie 1) — nazwa] 이 요정주가 좋나?
   źródło: Skills_Abnormality.json :: dataList[id=804807].levelList[level=1].name
   limit: do 40 znaków
   EN: You Like This Brew?
   PL:
329. [Umiejętność wroga [804807] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 속박 1 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804807].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Bind next turn
   PL:
330. [Umiejętność wroga [805101] (ulepszenie 1) — nazwa] 요정주
   źródło: Skills_Abnormality.json :: dataList[id=805101].levelList[level=1].name
   limit: do 40 znaków
   EN: Fairy Wine
   PL:
331. [Umiejętność wroga [805101] (ulepszenie 1) — opis] [WhenUse] 상대의 고양을 수치만큼 취기로 변환
   źródło: Skills_Abnormality.json :: dataList[id=805101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Convert opponent's Morale Boost into Tipsy
   PL:
332. [Umiejętność wroga [805201] (ulepszenie 1) — nazwa] 흩뿌려지는 슬픔
   źródło: Skills_Abnormality.json :: dataList[id=805201].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Sorrow
   PL:
333. [Umiejętność wroga [805201] (ulepszenie 1) — opis] [EndSkill] 모든 적의 파열 횟수 2, 침잠 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=805201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Inflict +2 Rupture Count and +2 Sinking Count to all enemies
   PL:
334. [Umiejętność wroga [804301] (ulepszenie 1) — nazwa] 아릿한 기억
   źródło: Skills_Abnormality.json :: dataList[id=804301].levelList[level=1].name
   limit: do 40 znaków
   EN: Stinging Memories
   PL:
335. [Umiejętność wroga [804301] (ulepszenie 1) — opis] [WinDuel] 정신력 8 회복\n[DefeatDuel] 정신력 5 감소
   źródło: Skills_Abnormality.json :: dataList[id=804301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefeatDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WinDuel] Heal 8 SP\n[DefeatDuel] Lose 5 SP
   PL:
336. [Umiejętność wroga [804301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2, 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Sinking and 2 Rupture
   PL:
337. [Umiejętność wroga [804301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 2, 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [804301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 2, 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność wroga [804302] (ulepszenie 1) — nazwa] 가시 돋친 추억
   źródło: Skills_Abnormality.json :: dataList[id=804302].levelList[level=1].name
   limit: do 40 znaków
   EN: Thorny Memories
   PL:
340. [Umiejętność wroga [804302] (ulepszenie 1) — opis] [WinDuel] 정신력 8 회복\n[DefeatDuel] 정신력 5 감소
   źródło: Skills_Abnormality.json :: dataList[id=804302].levelList[level=1].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność wroga [804302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność wroga [804302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=804302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność wroga [804303] (ulepszenie 1) — nazwa] 자기 방어
   źródło: Skills_Abnormality.json :: dataList[id=804303].levelList[level=1].name
   limit: do 40 znaków
   EN: Self-defense
   PL:
344. [Umiejętność wroga [804303] (ulepszenie 1) — opis] [DefeatDuel] 자신의 정신력 8 감소, 침잠 3을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Lose 8 SP and gain 3 Sinking
   PL:
345. [Umiejętność wroga [804303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2, 공격 위력 감소 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind and 2 Attack Power Down next turn
   PL:
346. [Umiejętność wroga [804304] (ulepszenie 1) — nazwa] 아려오는 마음
   źródło: Skills_Abnormality.json :: dataList[id=804304].levelList[level=1].name
   limit: do 40 znaków
   EN: Aching Heart
   PL:
347. [Umiejętność wroga [804304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [804304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가.
   źródło: Skills_Abnormality.json :: dataList[id=804304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count.
   PL:
349. [Umiejętność wroga [804304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 대상의 흐트러짐 손상
   źródło: Skills_Abnormality.json :: dataList[id=804304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [804305] (ulepszenie 1) — nazwa] 전부 잠겨버려
   źródło: Skills_Abnormality.json :: dataList[id=804305].levelList[level=1].name
   limit: do 40 znaków
   EN: Sink It All
   PL:
351. [Umiejętność wroga [804305] (ulepszenie 1) — opis] [WhenUse] 정신력 30 감소, 침잠 5를 얻음. 다음 턴에 침식되는 마음을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 30 SP and gain 5 Sinking; Gain Corroding Heart next turn
   PL:
352. [Umiejętność wroga [804305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 15 감소.
   źródło: Skills_Abnormality.json :: dataList[id=804305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 15 SP.
   PL:
353. [Umiejętność wroga [804305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 8, 독 8 부여
   źródło: Skills_Abnormality.json :: dataList[id=804305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 8 Sinking and 8 Poison next turn
   PL:
354. [Umiejętność wroga [804306] (ulepszenie 1) — nazwa] 저리 치워
   źródło: Skills_Abnormality.json :: dataList[id=804306].levelList[level=1].name
   limit: do 40 znaków
   EN: Get It Away
   PL:
355. [Umiejętność wroga [804306] (ulepszenie 1) — opis] [OnDefeatEvade] 정신력 8 감소
   źródło: Skills_Abnormality.json :: dataList[id=804306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnDefeatEvade]
   znaczenie tagów: [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: [OnDefeatEvade] Lose 8 SP
   PL:
356. [Umiejętność wroga [804307] (ulepszenie 1) — nazwa] 건드리지마...!
   źródło: Skills_Abnormality.json :: dataList[id=804307].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't Touch Me...!
   PL:
357. [Umiejętność wroga [804307] (ulepszenie 1) — opis] [StartBattle] 가시 를 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804307].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain Thorns
   PL:
358. [Umiejętność wroga [804401] (ulepszenie 1) — nazwa] 흩날리는 향기
   źródło: Skills_Abnormality.json :: dataList[id=804401].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Fragrance
   PL:
359. [Umiejętność wroga [804401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Umiejętność wroga [804401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Blooming
   PL:
361. [Umiejętność wroga [804401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [804401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność wroga [804402] (ulepszenie 1) — nazwa] 아릿한 향기
   źródło: Skills_Abnormality.json :: dataList[id=804402].levelList[level=1].name
   limit: do 40 znaków
   EN: Pungent Fragrance
   PL:
364. [Umiejętność wroga [804402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 개화 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Blooming
   PL:
365. [Umiejętność wroga [804402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 개화 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność wroga [804403] (ulepszenie 1) — nazwa] 피어나는 봉우리
   źródło: Skills_Abnormality.json :: dataList[id=804403].levelList[level=1].name
   limit: do 40 znaków
   EN: Flowering Buds
   PL:
367. [Umiejętność wroga [804403] (ulepszenie 1) — opis] 다음 턴에 꽃 2개를 생성.\n꽃이 4개 생성되어있는 경우, 대신 가장 단계가 낮은 꽃 중 무작위 1개의 단계를 1 상승
   źródło: Skills_Abnormality.json :: dataList[id=804403].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Spawn 2 flowers next turn\nIf there are 4 flowers present, instead raise the level of a lowest-level flower by 1
   PL:
368. [Umiejętność wroga [804403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=804403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Umiejętność wroga [804403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 개화 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Blooming
   PL:
370. [Umiejętność wroga [804404] (ulepszenie 1) — nazwa] 만발하는 꽃처럼...
   źródło: Skills_Abnormality.json :: dataList[id=804404].levelList[level=1].name
   limit: do 50 znaków
   EN: Like Flowers in Full Bloom...
   PL:
371. [Umiejętność wroga [804404] (ulepszenie 1) — opis] [WhenUse] 개화 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 3 Blooming
   PL:
372. [Umiejętność wroga [804404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność wroga [804404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność wroga [804405] (ulepszenie 1) — nazwa] 찬란한 봄바람
   źródło: Skills_Abnormality.json :: dataList[id=804405].levelList[level=1].name
   limit: do 40 znaków
   EN: Magnificent Spring Breeze
   PL:
375. [Umiejętność wroga [804405] (ulepszenie 1) — opis] 살아있는 곧 피어날 꽃 1개 당 최종 위력 +5\n\n[EndSkill] 모든 곧 피어날 꽃 제거
   źródło: Skills_Abnormality.json :: dataList[id=804405].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: Gain +5 Final Power for each living Soon-to-bloom Flower\n\n[EndSkill] Remove all Soon-to-bloom Flowers
   PL:
376. [Umiejętność wroga [804405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 -15
   źródło: Skills_Abnormality.json :: dataList[id=804405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 15 SP
   PL:
377. [Umiejętność wroga [804405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 개화 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=804405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność wroga [804406] (ulepszenie 1) — nazwa] 흙을 덮어야 해
   źródło: Skills_Abnormality.json :: dataList[id=804406].levelList[level=1].name
   limit: do 40 znaków
   EN: Must Cover With Dirt
   PL:
379. [Umiejętność wroga [804406] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 대결 부여
   źródło: Skills_Abnormality.json :: dataList[id=804406].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict Dueling next turn
   PL:
380. [Umiejętność wroga [804407] (ulepszenie 1) — nazwa] 흐드러지는 꽃
   źródło: Skills_Abnormality.json :: dataList[id=804407].levelList[level=1].name
   limit: do 40 znaków
   EN: Flowering Glory
   PL:
381. [Umiejętność wroga [804407] (ulepszenie 1) — opis] [StartBattle] 보호 10을 얻음\n[DefeatDuel] 흩어지는 꽃잎 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804407].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 10 Protection\n[DefeatDuel] Gain 1 Scattering Petals
   PL:
382. [Umiejętność wroga [804408] (ulepszenie 1) — nazwa] 허물어지는 꽃
   źródło: Skills_Abnormality.json :: dataList[id=804408].levelList[level=1].name
   limit: do 40 znaków
   EN: Withering Flower
   PL:
383. [Umiejętność wroga [804408] (ulepszenie 1) — opis] [StartBattle] 보호 10을 얻음\n[DefeatDuel] 흩어지는 꽃잎 3을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804408].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 10 Protection\n[DefeatDuel] Gain 3 Scattering Petals
   PL:
384. [Umiejętność wroga [804409] (ulepszenie 1) — nazwa] 절정의 향기
   źródło: Skills_Abnormality.json :: dataList[id=804409].levelList[level=1].name
   limit: do 40 znaków
   EN: Culminating Fragrance
   PL:
385. [Umiejętność wroga [804409] (ulepszenie 1) — opis] [CantDuel]\n대상이 만개 상태면 피해량 +100%
   źródło: Skills_Abnormality.json :: dataList[id=804409].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nIf target is Fully Bloomed, deal +100% damage
   PL:
386. [Umiejętność wroga [804409] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 만개 상태면, 대상을 흐트러짐 상태로 만들고 만개 상태를 해제시킴.
   źródło: Skills_Abnormality.json :: dataList[id=804409].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Fully Bloomed, stagger them and remove the effect
   PL:
387. [Umiejętność wroga [804409] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=804409].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [804409] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804409].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL:
389. [Umiejętność wroga [804409] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Abnormality.json :: dataList[id=804409].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +5 Rupture Count
   PL:
390. [Umiejętność wroga [804410] (ulepszenie 1) — nazwa] 알싸한 잔향
   źródło: Skills_Abnormality.json :: dataList[id=804410].levelList[level=1].name
   limit: do 40 znaków
   EN: Piquant Scent
   PL:
391. [Umiejętność wroga [804410] (ulepszenie 1) — opis] [OnSucceedEvade] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=804410].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Inflict 1 Blooming
   PL:
392. [Umiejętność wroga [804411] (ulepszenie 1) — nazwa] 찰나를 기다리며
   źródło: Skills_Abnormality.json :: dataList[id=804411].levelList[level=1].name
   limit: do 40 znaków
   EN: Awaiting the Moment
   PL:
393. [Umiejętność wroga [804411] (ulepszenie 1) — opis] [StartBattle] 보호 5를 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804411].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 5 Protection
   PL:
394. [Umiejętność wroga [805401] (ulepszenie 1) — nazwa] 꽃바람
   źródło: Skills_Abnormality.json :: dataList[id=805401].levelList[level=1].name
   limit: do 40 znaków
   EN: Floral Breeze
   PL:
395. [Umiejętność wroga [805401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [805402] (ulepszenie 1) — nazwa] 향긋한 꽃바람
   źródło: Skills_Abnormality.json :: dataList[id=805402].levelList[level=1].name
   limit: do 40 znaków
   EN: Fragrant Breeze
   PL:
397. [Umiejętność wroga [805402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność wroga [805402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność wroga [805403] (ulepszenie 1) — nazwa] 알싸한 꽃바람
   źródło: Skills_Abnormality.json :: dataList[id=805403].levelList[level=1].name
   limit: do 40 znaków
   EN: Pungent Breeze
   PL:
400. [Umiejętność wroga [805403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność wroga [805403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [805403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 개화 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [805404] (ulepszenie 1) — nazwa] 머금은 향기
   źródło: Skills_Abnormality.json :: dataList[id=805404].levelList[level=1].name
   limit: do 40 znaków
   EN: Borne Scent
   PL:
404. [Umiejętność wroga [805404] (ulepszenie 1) — opis] [WhenUse] 체력 10 회복
   źródło: Skills_Abnormality.json :: dataList[id=805404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 10 HP
   PL:
405. [Umiejętność wroga [805405] (ulepszenie 1) — nazwa] 활짝 피어난 꽃
   źródło: Skills_Abnormality.json :: dataList[id=805405].levelList[level=1].name
   limit: do 40 znaków
   EN: Fully Bloomed
   PL:
406. [Umiejętność wroga [805405] (ulepszenie 1) — opis] [DefeatDuel] 이 유닛이 처치됨
   źródło: Skills_Abnormality.json :: dataList[id=805405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] This unit is defeated
   PL:
407. [Umiejętność wroga [805501] (ulepszenie 1) — nazwa] 만개
   źródło: Skills_Abnormality.json :: dataList[id=805501].levelList[level=1].name
   limit: do 40 znaków
   EN: Full Bloom
   PL:
408. [Umiejętność wroga [805501] (ulepszenie 1) — opis] 행동 불가\n턴 종료 시 정신력 -20.\n정신력이 -45가 된 경우 정신력을 최대로 회복하고, 다음 턴에 아찔한 정신 상태가 됨\n2턴 동안 해제되지 않으면, 턴 종료 시 상태 해제
   źródło: Skills_Abnormality.json :: dataList[id=805501].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot act\nAt the end of the turn, lose 20 SP\nIf SP reaches -45, fully heal SP, then gain Dazzled Mind next turn\nIf this effect isn't removed for 2 turns, remove it at the end of the turn
   PL:
409. [Umiejętność wroga [804901] (ulepszenie 1) — nazwa] 당신도 텅 비었군요
   źródło: Skills_Abnormality.json :: dataList[id=804901].levelList[level=1].name
   limit: do 40 znaków
   EN: You're Empty As Well
   PL:
410. [Umiejętność wroga [804901] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 텅 빈 징표 부여
   źródło: Skills_Abnormality.json :: dataList[id=804901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict Empty Mark next turn
   PL:
411. [Umiejętność wroga [804901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 10 부여
   źródło: Skills_Abnormality.json :: dataList[id=804901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Rupture
   PL:
412. [Umiejętność wroga [804902] (ulepszenie 1) — nazwa] 가지치기
   źródło: Skills_Abnormality.json :: dataList[id=804902].levelList[level=1].name
   limit: do 40 znaków
   EN: Prune
   PL:
413. [Umiejętność wroga [804902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [804902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=804902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [804903] (ulepszenie 1) — nazwa] 가지치기
   źródło: Skills_Abnormality.json :: dataList[id=804903].levelList[level=1].name
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [804903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=804903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [804903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량만큼 체력 회복
   źródło: Skills_Abnormality.json :: dataList[id=804903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by damage dealt
   PL:
418. [Umiejętność wroga [804904] (ulepszenie 1) — nazwa] 솎아내기
   źródło: Skills_Abnormality.json :: dataList[id=804904].levelList[level=1].name
   limit: do 40 znaków
   EN: Thinning
   PL:
419. [Umiejętność wroga [804904] (ulepszenie 1) — opis] 대상에게 텅 빈 징표 가 있으면 피해량 50%\n[DefeatDuel] 다음 턴에 취약 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +50% damage to targets with Empty Mark\n[DefeatDuel] Gain 1 Fragile next turn
   PL:
420. [Umiejętność wroga [804904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량만큼 체력 회복\n대상에게 텅 빈 징표 가 있으면, 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by damage dealt\nIf target has Empty Mark, gain 1 Attack Power Up next turn
   PL:
421. [Umiejętność wroga [804904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량만큼 체력 회복\n대상에게 텅 빈 징표 가 있으면, 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [804905] (ulepszenie 1) — nazwa] 파괴
   źródło: Skills_Abnormality.json :: dataList[id=804905].levelList[level=1].name
   limit: do 40 znaków
   EN: Destruction
   PL:
423. [Umiejętność wroga [804905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 10 부여
   źródło: Skills_Abnormality.json :: dataList[id=804905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Bleed
   PL:
424. [Umiejętność wroga [804906] (ulepszenie 1) — nazwa] 아직 부족해...
   źródło: Skills_Abnormality.json :: dataList[id=804906].levelList[level=1].name
   limit: do 40 znaków
   EN: Still Not Enough...
   PL:
425. [Umiejętność wroga [804906] (ulepszenie 1) — opis] 무작위 아군 공격
   źródło: Skills_Abnormality.json :: dataList[id=804906].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets a random friendly unit
   PL:
426. [Umiejętność wroga [804906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여. 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality.json :: dataList[id=804906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed; Heal by 25% of damage dealt
   PL:
427. [Umiejętność wroga [804906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여. 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality.json :: dataList[id=804906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Umiejętność wroga [804906] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 무작위 이로운 효과 1개를 흡수하여 다음 턴에 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804906].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Absorb 1 random positive status effect from target and gain it next turn
   PL:
429. [Umiejętność wroga [804907] (ulepszenie 1) — nazwa] 채워야 해...
   źródło: Skills_Abnormality.json :: dataList[id=804907].levelList[level=1].name
   limit: do 40 znaków
   EN: Must Fill...
   PL:
430. [Umiejętność wroga [804907] (ulepszenie 1) — opis] 무작위 대상 공격
   źródło: Skills_Abnormality.json :: dataList[id=804907].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets a random unit
   PL:
431. [Umiejętność wroga [804907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 무작위 이로운 효과 1개를 흡수하여 다음 턴에 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [804907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 5 증가
   źródło: Skills_Abnormality.json :: dataList[id=804907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply +5 Bleed Count
   PL:
433. [Umiejętność wroga [804908] (ulepszenie 1) — nazwa] 텅 비어버렸어
   źródło: Skills_Abnormality.json :: dataList[id=804908].levelList[level=1].name
   limit: do 40 znaków
   EN: It's All Empty
   PL:
434. [Umiejętność wroga [804908] (ulepszenie 1) — opis] [DefeatDuel] 파열 10을 얻음
   źródło: Skills_Abnormality.json :: dataList[id=804908].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 10 Rupture
   PL:
435. [Umiejętność wroga [804909] (ulepszenie 1) — nazwa] 이젠 늦어버렸어
   źródło: Skills_Abnormality.json :: dataList[id=804909].levelList[level=1].name
   limit: do 40 znaków
   EN: It's Too Late Now
   PL:
436. [Umiejętność wroga [804909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=804909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Fragile
   PL:
437. [Umiejętność wroga [804910] (ulepszenie 1) — nazwa] 전부 타버렸어
   źródło: Skills_Abnormality.json :: dataList[id=804910].levelList[level=1].name
   limit: do 40 znaków
   EN: It's All Burned Up
   PL:
438. [Umiejętność wroga [804910] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2, 파열 5, 출혈 5 부여. 피해량의 10%만큼 체력 회복
   źródło: Skills_Abnormality.json :: dataList[id=804910].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile, 5 Rupture, and 5 Bleed; Heal by 10% of damage dealt
   PL:
439. [Umiejętność wroga [804911] (ulepszenie 1) — nazwa] 소용 없어요
   źródło: Skills_Abnormality.json :: dataList[id=804911].levelList[level=1].name
   limit: do 40 znaków
   EN: It's No Use
   PL:
440. [Umiejętność wroga [805001] (ulepszenie 1) — nazwa] 경작
   źródło: Skills_Abnormality.json :: dataList[id=805001].levelList[level=1].name
   limit: do 40 znaków
   EN: Cultivate
   PL:
441. [Umiejętność wroga [805001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박1, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bind and 1 Paralyze next turn
   PL:
442. [Umiejętność wroga [805001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박1, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [805002] (ulepszenie 1) — nazwa] 파종
   źródło: Skills_Abnormality.json :: dataList[id=805002].levelList[level=1].name
   limit: do 40 znaków
   EN: Dissemination
   PL:
444. [Umiejętność wroga [805002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [805002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność wroga [805002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 씨앗 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=805002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Seeds next turn
   PL:
447. [Umiejętność wroga [805003] (ulepszenie 1) — nazwa] 촉진
   źródło: Skills_Abnormality.json :: dataList[id=805003].levelList[level=1].name
   limit: do 40 znaków
   EN: Facilitate
   PL:
448. [Umiejętność wroga [805003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 씨앗 1 부여. 대상에게 씨앗이 있으면, 씨앗 1 추가 부여
   źródło: Skills_Abnormality.json :: dataList[id=805003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Seeds; if target already has Seeds, inflict 1 more
   PL:
449. [Umiejętność wroga [805003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 씨앗 1 부여. 대상에게 씨앗이 있으면, 씨앗 1 추가 부여
   źródło: Skills_Abnormality.json :: dataList[id=805003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [805003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 씨앗 1 부여. 대상에게 씨앗이 있으면, 씨앗 1 추가 부여
   źródło: Skills_Abnormality.json :: dataList[id=805003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [805004] (ulepszenie 1) — nazwa] 과잉 생장
   źródło: Skills_Abnormality.json :: dataList[id=805004].levelList[level=1].name
   limit: do 40 znaków
   EN: Overgrowth
   PL:
452. [Umiejętność wroga [805004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 씨앗 3, 과잉 회복 부여, 대상의 체력을 15 회복시킴
   źródło: Skills_Abnormality.json :: dataList[id=805004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Seeds and Overheal; Heal target's HP by 15
   PL:
453. [Umiejętność wroga [805005] (ulepszenie 1) — nazwa] 수확의 시간
   źródło: Skills_Abnormality.json :: dataList[id=805005].levelList[level=1].name
   limit: do 40 znaków
   EN: Time of Harvest
   PL:
454. [Umiejętność wroga [805005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 3, 출혈 10 부여\n대상이 양분 흡수 상태인 경우, 체력을 20 회복하고 다음 턴에 공격 위력 증가 2를 얻음
   źródło: Skills_Abnormality.json :: dataList[id=805005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Fragile and 10 Bleed\nIf target has Nutrient Drain, heal 20 HP, and gain 2 Attack Power Up next turn
   PL:
455. [Umiejętność wroga [805006] (ulepszenie 1) — nazwa] 양분이 되어주세요
   źródło: Skills_Abnormality.json :: dataList[id=805006].levelList[level=1].name
   limit: do 40 znaków
   EN: Please Be My Nutrient
   PL:
456. [Umiejętność wroga [805006] (ulepszenie 1) — opis] [WhenUse] 모든 욕망의 나무의 체력 15 회복. 욕망의 나무가 없는 경우 1개 생성
   źródło: Skills_Abnormality.json :: dataList[id=805006].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] All Trees of Desires heal 15 HP; If there are no Trees of Desires, spawn one
   PL:
457. [Umiejętność wroga [805006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 10 회복, 씨앗 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=805006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 HP; Inflict 3 Seeds
   PL:
458. [Umiejętność wroga [806001] (ulepszenie 1) — nazwa] 자라나는 성과
   źródło: Skills_Abnormality.json :: dataList[id=806001].levelList[level=1].name
   limit: do 40 znaków
   EN: Growing Results
   PL:
459. [Umiejętność wroga [806001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 씨앗 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=806001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Seeds
   PL:
460. [Umiejętność wroga [806001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 씨앗 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=806001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [806002] (ulepszenie 1) — nazwa] 기대
   źródło: Skills_Abnormality.json :: dataList[id=806002].levelList[level=1].name
   limit: do 40 znaków
   EN: Expectation
   PL:
462. [Umiejętność wroga [805801] (ulepszenie 1) — nazwa] 확산하는 뿌리
   źródło: Skills_Abnormality.json :: dataList[id=805801].levelList[level=1].name
   limit: do 40 znaków
   EN: Expanding Roots
   PL:
463. [Umiejętność wroga [805801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=805801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [805801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=805801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Tremor Count
   PL:
465. [Umiejętność wroga [805802] (ulepszenie 1) — nazwa] 파고드는 뿌리
   źródło: Skills_Abnormality.json :: dataList[id=805802].levelList[level=1].name
   limit: do 40 znaków
   EN: Burrowing Roots
   PL:
466. [Umiejętność wroga [805802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=805802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność wroga [805802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=805802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność wroga [805803] (ulepszenie 1) — nazwa] 동요하는 미끼
   źródło: Skills_Abnormality.json :: dataList[id=805803].levelList[level=1].name
   limit: do 40 znaków
   EN: Quivering Lure
   PL:
469. [Umiejętność wroga [805803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=805803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Tremor Count
   PL:
470. [Umiejętność wroga [805803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=805803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 195 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność wroga [805803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 2 감소
   źródło: Skills_Abnormality.json :: dataList[id=805803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Reduce target's Defense Level by 2 next turn
   PL:
472. [Umiejętność wroga [805804] (ulepszenie 1) — nazwa] 잠식하는 줄기
   źródło: Skills_Abnormality.json :: dataList[id=805804].levelList[level=1].name
   limit: do 40 znaków
   EN: Encroaching Stems
   PL:
473. [Umiejętność wroga [805804] (ulepszenie 1) — opis] [WinDuel] 대상에게 파열이 있다면, 파열 횟수 +2
   źródło: Skills_Abnormality.json :: dataList[id=805804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] If target has Rupture, inflict +2 Rupture Count
   PL:
474. [Umiejętność wroga [805804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=805804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [805805] (ulepszenie 1) — nazwa] 드러난 심연
   źródło: Skills_Abnormality.json :: dataList[id=805805].levelList[level=1].name
   limit: do 40 znaków
   EN: Uncovered Abyss
   PL:
476. [Umiejętność wroga [805805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 가지고 있는 파열만큼 진동 부여
   źródło: Skills_Abnormality.json :: dataList[id=805805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Tremor by target's Rupture
   PL:
477. [Umiejętność wroga [805805] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality.json :: dataList[id=805805].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
478. [Umiejętność wroga [805806] (ulepszenie 1) — nazwa] 단단한 가지
   źródło: Skills_Abnormality.json :: dataList[id=805806].levelList[level=1].name
   limit: do 40 znaków
   EN: Hard Branches
   PL:
479. [Umiejętność wroga [805806] (ulepszenie 1) — opis] [StartBattle] 보호 3 얻음
   źródło: Skills_Abnormality.json :: dataList[id=805806].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 3 Protection
   PL:
480. [Umiejętność wroga [805901] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Abnormality.json :: dataList[id=805901].levelList[level=1].name
   limit: do 40 znaków
   EN: Skim Wounds
   PL:
481. [Umiejętność wroga [805901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 출혈을 가지고 있다면, 마비 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, inflict 1 Paralyze
   PL:
482. [Umiejętność wroga [805901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=805901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL:
483. [Umiejętność wroga [805901] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 출혈 횟수가 2 이상이면 출혈 5 부여.
   źródło: Skills_Abnormality.json :: dataList[id=805901].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 2+ Bleed Count, inflict 5 Bleed
   PL:
484. [Umiejętność wroga [805902] (ulepszenie 1) — nazwa] 옭아매인 상처
   źródło: Skills_Abnormality.json :: dataList[id=805902].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangled Injury
   PL:
485. [Umiejętność wroga [805902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 출혈을 가지고 있다면, 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=805902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, inflict 1 Bind next turn
   PL:
486. [Umiejętność wroga [805902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=805902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [805903] (ulepszenie 1) — nazwa] 묻어오는 살점
   źródło: Skills_Abnormality.json :: dataList[id=805903].levelList[level=1].name
   limit: do 40 znaków
   EN: Smeared Flesh
   PL:
488. [Umiejętność wroga [805903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=805903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Umiejętność wroga [805903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 출혈을 가지고 있다면, 체력 20 회복
   źródło: Skills_Abnormality.json :: dataList[id=805903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, heal 20 HP
   PL:
490. [Umiejętność wroga [805903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈 횟수가 2 이상이면 출혈 5 부여.
   źródło: Skills_Abnormality.json :: dataList[id=805903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność wroga [805904] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Abnormality.json :: dataList[id=805904].levelList[level=1].name
   limit: do 40 znaków
   EN: Casting Shade
   PL:
492. [Umiejętność wroga [805904] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 거대 클로버 생성\n[DefeatDuel] 거대 클로버의 체력이 70%인 상태로 생성됨.
   źródło: Skills_Abnormality.json :: dataList[id=805904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Spawn a Giant Clover next turn\n[DefeatDuel] The Giant Clover spawns with 70% HP
   PL:
493. [Umiejętność wroga [805904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 전부 소모
   źródło: Skills_Abnormality.json :: dataList[id=805904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove all Bleed Count
   PL:
494. [Umiejętność wroga [805905] (ulepszenie 1) — nazwa] 소화
   źródło: Skills_Abnormality.json :: dataList[id=805905].levelList[level=1].name
   limit: do 40 znaków
   EN: Churning
   PL:
495. [Umiejętność wroga [805905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]당 자신의 전체 체력의 1%만큼 회복\n출혈 횟수 전부 소모
   źródło: Skills_Abnormality.json :: dataList[id=805905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal by 1% of Max HP per target's [Laceration]\nRemove all Bleed Count
   PL:
496. [Umiejętność wroga [806401] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Abnormality.json :: dataList[id=806401].levelList[level=1].name
   limit: do 40 znaków
   EN: Nibble
   PL:
497. [Umiejętność wroga [806402] (ulepszenie 1) — nazwa] 탐욕스러운 식사
   źródło: Skills_Abnormality.json :: dataList[id=806402].levelList[level=1].name
   limit: do 40 znaków
   EN: Greedy Gluttons
   PL:
498. [Umiejętność wroga [806402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 체력 1 회복
   źródło: Skills_Abnormality.json :: dataList[id=806402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 HP
   PL:
499. [Umiejętność wroga [806402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 체력 1 회복
   źródło: Skills_Abnormality.json :: dataList[id=806402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [806402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 체력 1 회복
   źródło: Skills_Abnormality.json :: dataList[id=806402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [806501] (ulepszenie 1) — nazwa] 구르기
   źródło: Skills_Abnormality.json :: dataList[id=806501].levelList[level=1].name
   limit: do 40 znaków
   EN: Roll
   PL:
502. [Umiejętność wroga [806502] (ulepszenie 1) — nazwa] 나태한 손아귀
   źródło: Skills_Abnormality.json :: dataList[id=806502].levelList[level=1].name
   limit: do 40 znaków
   EN: Slothful Grip
   PL:
503. [Umiejętność wroga [806502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=806502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bind next turn
   PL:
504. [Umiejętność wroga [806601] (ulepszenie 1) — nazwa] 지지기
   źródło: Skills_Abnormality.json :: dataList[id=806601].levelList[level=1].name
   limit: do 40 znaków
   EN: Sear
   PL:
505. [Umiejętność wroga [806602] (ulepszenie 1) — nazwa] 폭발하는 분노
   źródło: Skills_Abnormality.json :: dataList[id=806602].levelList[level=1].name
   limit: do 40 znaków
   EN: Explosive Wrath
   PL:
506. [Umiejętność wroga [806602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 화상 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=806602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Burn next turn
   PL:
507. [Umiejętność wroga [806701] (ulepszenie 1) — nazwa] 쏘아대기
   źródło: Skills_Abnormality.json :: dataList[id=806701].levelList[level=1].name
   limit: do 40 znaków
   EN: Fire Off
   PL:
508. [Umiejętność wroga [806702] (ulepszenie 1) — nazwa] 터져나오는 우울
   źródło: Skills_Abnormality.json :: dataList[id=806702].levelList[level=1].name
   limit: do 40 znaków
   EN: Bursting Gloom
   PL:
509. [Umiejętność wroga [806702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=806702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Sinking next turn
   PL:
510. [Umiejętność wroga [806801] (ulepszenie 1) — nazwa] 내려찍기
   źródło: Skills_Abnormality.json :: dataList[id=806801].levelList[level=1].name
   limit: do 40 znaków
   EN: Strike Down
   PL:
511. [Umiejętność wroga [806802] (ulepszenie 1) — nazwa] 꿰뚫는 욕망
   źródło: Skills_Abnormality.json :: dataList[id=806802].levelList[level=1].name
   limit: do 40 znaków
   EN: Piercing Lust
   PL:
512. [Umiejętność wroga [806802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=806802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed next turn
   PL:
513. [Umiejętność wroga [806901] (ulepszenie 1) — nazwa] 갈아내기
   źródło: Skills_Abnormality.json :: dataList[id=806901].levelList[level=1].name
   limit: do 40 znaków
   EN: Grind
   PL:
514. [Umiejętność wroga [806902] (ulepszenie 1) — nazwa] 교만한 분쇄
   źródło: Skills_Abnormality.json :: dataList[id=806902].levelList[level=1].name
   limit: do 40 znaków
   EN: Prideful Runover
   PL:
515. [Umiejętność wroga [806902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=806902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Fragile next turn
   PL:
516. [Umiejętność wroga [806902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=806902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność wroga [826301] (ulepszenie 1) — nazwa] 여왕의 명령
   źródło: Skills_Abnormality.json :: dataList[id=826301].levelList[level=1].name
   limit: do 40 znaków
   EN: Queen's Decree
   PL:
518. [Umiejętność wroga [826301] (ulepszenie 1) — opis] [StartBattle] [PreparedMeat]가 없는 무작위 아군 1명에게 [PreparedMeat] 부여
   źródło: Skills_Abnormality.json :: dataList[id=826301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [PreparedMeat]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [PreparedMeat] = 준비된 고기 / Prepared Meat
   EN: [StartBattle] Inflict 1 [PreparedMeat] to a random ally without [PreparedMeat]
   PL:
519. [Umiejętność wroga [826302] (ulepszenie 1) — nazwa] 날갯짓
   źródło: Skills_Abnormality.json :: dataList[id=826302].levelList[level=1].name
   limit: do 40 znaków
   EN: Wingbeat
   PL:
520. [Umiejętność wroga [826302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=826302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
521. [Umiejętność wroga [826302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=826302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [826303] (ulepszenie 1) — nazwa] 포식
   źródło: Skills_Abnormality.json :: dataList[id=826303].levelList[level=1].name
   limit: do 40 znaków
   EN: Predation
   PL:
523. [Umiejętność wroga [826303] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상 있으면, 코인 위력 +1
   źródło: Skills_Abnormality.json :: dataList[id=826303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], Coin Power +1
   PL:
524. [Umiejętność wroga [826303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 3%만큼 본체의 체력 회복
   źródło: Skills_Abnormality.json :: dataList[id=826303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 3% of Max HP to the Core
   PL:
525. [Umiejętność wroga [826304] (ulepszenie 1) — nazwa] 굶주린 날갯짓
   źródło: Skills_Abnormality.json :: dataList[id=826304].levelList[level=1].name
   limit: do 40 znaków
   EN: Starved Fluttering
   PL:
526. [Umiejętność wroga [826304] (ulepszenie 1) — opis] [Hunger]이 3 이상이면 코인 위력 +1\n대상에게 [Laceration]이 5 이상 있으면, 코인 위력 +1
   źródło: Skills_Abnormality.json :: dataList[id=826304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Hunger], [Laceration]
   znaczenie tagów: [Hunger] = 굶주림 / Hunger; [Laceration] = 출혈 / Bleed
   EN: At 3+ [Hunger], Coin Power +1\nIf target has 5+ [Laceration], Coin Power +1
   PL:
527. [Umiejętność wroga [826304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=826304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
528. [Umiejętność wroga [826304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=826304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [826304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=826304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [826305] (ulepszenie 1) — nazwa] 광포한 굶주림
   źródło: Skills_Abnormality.json :: dataList[id=826305].levelList[level=1].name
   limit: do 40 znaków
   EN: Ravening Hunger
   PL:
531. [Umiejętność wroga [826305] (ulepszenie 1) — opis] [CantIdentify]\n[PreparedMeat]가 부여된 대상 우선 공격\n대상에게 [Laceration]이 5 이상 있으면, 코인 위력 +1\n대상에게 [PreparedMeat]가 있으면, 코인 위력 +10\n파괴된 팔 부위 1개당 코인 위력 -5\n[TargetKill] 이번 전투동안 모든 부위가 [Enhancement] 2 얻음 (중첩 가능)
   źródło: Skills_Abnormality.json :: dataList[id=826305].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [PreparedMeat], [Laceration], [TargetKill], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [PreparedMeat] = 준비된 고기 / Prepared Meat; [Laceration] = 출혈 / Bleed; [TargetKill] = [대상 처치 시] / [On Target Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nPrioritizes targets with [PreparedMeat]\nIf target has 5 +[Laceration], Coin Power +1\nIf target has [PreparedMeat], Coin Power +10\nCoin Power -5 for every broken Arm Part\n[TargetKill] All Parts gain 2 [Enhancement] for the Encounter (stackable)
   PL:
532. [Umiejętność wroga [826305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 코인 1회 재사용 (스킬당 최대 3회)
   źródło: Skills_Abnormality.json :: dataList[id=826305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse Coin once (3 times per Skill)
   PL:
533. [Umiejętność wroga [826305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 본체의 체력 10 회복
   źródło: Skills_Abnormality.json :: dataList[id=826305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core heals 10 HP
   PL:
534. [Umiejętność wroga [826306] (ulepszenie 1) — nazwa] 휴식
   źródło: Skills_Abnormality.json :: dataList[id=826306].levelList[level=1].name
   limit: do 40 znaków
   EN: Respite
   PL:
535. [Umiejętność wroga [826307] (ulepszenie 1) — nazwa] 보살핌의 대가
   źródło: Skills_Abnormality.json :: dataList[id=826307].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Pay for My Care
   PL:
536. [Umiejętność wroga [826307] (ulepszenie 1) — opis] [StartBattle] [PreparedMeat]가 없는 모든 아군에게 [PreparedMeat] 부여
   źródło: Skills_Abnormality.json :: dataList[id=826307].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [PreparedMeat]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [PreparedMeat] = 준비된 고기 / Prepared Meat
   EN: [StartBattle] Inflict 1 [PreparedMeat] to all allies without [PreparedMeat]
   PL:
537. [Umiejętność wroga [826401] (ulepszenie 1) — nazwa] 와구와구
   źródło: Skills_Abnormality.json :: dataList[id=826401].levelList[level=1].name
   limit: do 40 znaków
   EN: Munch Munch
   PL:
538. [Umiejętność wroga [826401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 3 회복
   źródło: Skills_Abnormality.json :: dataList[id=826401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core heals 3 HP
   PL:
539. [Umiejętność wroga [826401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 3 회복
   źródło: Skills_Abnormality.json :: dataList[id=826401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [826402] (ulepszenie 1) — nazwa] 식탐
   źródło: Skills_Abnormality.json :: dataList[id=826402].levelList[level=1].name
   limit: do 40 znaków
   EN: Gluttony
   PL:
541. [Umiejętność wroga [826402] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상 있으면, 코인 위력 +1
   źródło: Skills_Abnormality.json :: dataList[id=826402].levelList[level=1].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Umiejętność wroga [826402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 10 회복
   źródło: Skills_Abnormality.json :: dataList[id=826402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 533 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Umiejętność wroga [826402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality.json :: dataList[id=826402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [826403] (ulepszenie 1) — nazwa] 작은 날갯짓
   źródło: Skills_Abnormality.json :: dataList[id=826403].levelList[level=1].name
   limit: do 40 znaków
   EN: Tiny Wingbeat
   PL:
545. [Umiejętność wroga [826403] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상 있으면, 코인 위력 +1
   źródło: Skills_Abnormality.json :: dataList[id=826403].levelList[level=1].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność wroga [826403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=826403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
547. [Umiejętność wroga [826403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=826403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność wroga [826403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=826403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność wroga [826404] (ulepszenie 1) — nazwa] 휴식
   źródło: Skills_Abnormality.json :: dataList[id=826404].levelList[level=1].name
   (powtórzenie elementu 534 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność wroga [114301] (ulepszenie 1) — nazwa] 쫓고 물어뜯기
   źródło: Skills_Abnormality.json :: dataList[id=114301].levelList[level=1].name
   limit: do 40 znaków
   EN: Pursue and Bite
   PL:
551. [Umiejętność wroga [114301] (ulepszenie 1) — opis] 가장 속도가 낮은 대상 공격
   źródło: Skills_Abnormality.json :: dataList[id=114301].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the slowest Speed
   PL:

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Abnormality91-4
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Abnormality91-4.json`

552. [Umiejętność wroga [806301] (ulepszenie 1) — nazwa] 마구 마구 찍기
   źródło: Skills_Abnormality91-4.json :: dataList[id=806301].levelList[level=1].name
   limit: do 40 znaków
   EN: Brutal Pummelling
   PL:
553. [Umiejętność wroga [806301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [806301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [806301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [806302] (ulepszenie 1) — nazwa] 세게! 찍기
   źródło: Skills_Abnormality91-4.json :: dataList[id=806302].levelList[level=1].name
   limit: do 40 znaków
   EN: Powerful! Pummel
   PL:
557. [Umiejętność wroga [806302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 4 증가
   źródło: Skills_Abnormality91-4.json :: dataList[id=806302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +4 Rupture Count
   PL:
558. [Umiejętność wroga [806303] (ulepszenie 1) — nazwa] 게거품
   źródło: Skills_Abnormality91-4.json :: dataList[id=806303].levelList[level=1].name
   limit: do 40 znaków
   EN: Foaming
   PL:
559. [Umiejętność wroga [806303] (ulepszenie 1) — opis] [CantIdentify]
   źródło: Skills_Abnormality91-4.json :: dataList[id=806303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]
   PL:
560. [Umiejętność wroga [806303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Abnormality91-4.json :: dataList[id=806303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [806303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Abnormality91-4.json :: dataList[id=806303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność wroga [806304] (ulepszenie 1) — nazwa] 등딱지 어택!!!
   źródło: Skills_Abnormality91-4.json :: dataList[id=806304].levelList[level=1].name
   limit: do 40 znaków
   EN: Shell Attack!!!
   PL:
563. [Umiejętność wroga [806304] (ulepszenie 1) — opis] [CantIdentify]\n대상의 파열 횟수 5마다 피해량 +20%
   źródło: Skills_Abnormality91-4.json :: dataList[id=806304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify] \nDeal +20% damage per 5 Rupture Count on target
   PL:
564. [Umiejętność wroga [806304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Umiejętność wroga [806304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Abnormality91-4.json :: dataList[id=806304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność wroga [806305] (ulepszenie 1) — nazwa] 게판 벌이기
   źródło: Skills_Abnormality91-4.json :: dataList[id=806305].levelList[level=1].name
   limit: do 40 znaków
   EN: Crab Rave
   PL:
567. [Umiejętność wroga [806305] (ulepszenie 1) — opis] [CantIdentify]\n대상의 파열 횟수 5마다 피해량 +20%\n[EndSkill] 턴 종료 시 자신 제외 5마리 이하인 경우, 게 3마리를 불러옴 (최대 5마리)
   źródło: Skills_Abnormality91-4.json :: dataList[id=806305].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify] Damage +20% per 5 Rupture Count on Target\n[EndSkill] Summon 3 Crabs if there are less than 5 other Crabs on field at the end of the turn (Max 5)
   PL:
568. [Umiejętność wroga [806305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność wroga [806306] (ulepszenie 1) — nazwa] 거품 두르기
   źródło: Skills_Abnormality91-4.json :: dataList[id=806306].levelList[level=1].name
   limit: do 40 znaków
   EN: Foam Armor
   PL:
570. [Umiejętność wroga [806306] (ulepszenie 1) — opis] [StartBattle] 보호막 체력이 있는 상태에서 피격시 피해 7 반사.\n파열 1 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806306].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] When attacked while this unit has Shield HP, deal 7 damage back to the attacker, and inflict 1 Rupture
   PL:
571. [Umiejętność wroga [806307] (ulepszenie 1) — nazwa] 거품 두르기
   źródło: Skills_Abnormality91-4.json :: dataList[id=806307].levelList[level=1].name
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność wroga [806307] (ulepszenie 1) — opis] [StartBattle] 보호막 체력이 있는 상태에서 피격시 피해 7 반사.\n파열 1 부여
   źródło: Skills_Abnormality91-4.json :: dataList[id=806307].levelList[level=1].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Abnormality91-5-hard
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Abnormality91-5-hard.json`

573. [Umiejętność wroga [107804] (ulepszenie 1) — nazwa] 포장하겠어요
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Get Packing
   PL:
574. [Umiejętność wroga [107804] (ulepszenie 1) — opis] 자신에게 [AaCeSeBa]가 있다면, 코인 효과에 다음 턴에 [Paralysis] 1 부여 추가\n가장 느린 대상 우선 공격\n[EndBattle] 모든 [Charge] 횟수 소모
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [AaCeSeBa], [Paralysis], [EndBattle], [Charge]
   znaczenie tagów: [AaCeSeBa] = 호!호!호! / HO! HO! HO!; [Paralysis] = 마비 / Paralyze; [EndBattle] = [턴 종료 시] / [Turn End]; [Charge] = 충전 / Charge
   EN: If this unit has [AaCeSeBa], add 'Inflict 1 [Paralysis] next turn' to Coin effects\nTargets the unit with the slowest Speed\n[EndBattle] Spend all [Charge] Count
   PL:
575. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
576. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 3 얻음.
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath].
   PL:
577. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath]만큼 추가 피해
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Deal bonus damage equal to [Breath] on self
   PL:
579. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Breath] 1 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] and +3 [Breath] Count
   PL:
580. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack]  [Protection], [Enhancement], [Vulnerable], [Paralysis] 중 무작위 1개 효과를 3 부여
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection], [Enhancement], [Vulnerable], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Randomly select 1 of 4 effects ([Protection], [Enhancement], [Vulnerable], [Paralysis]). Inflict or apply 3 of the selected effect.
   PL:
582. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수만큼 대상의 정신력을 감소
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Target loses SP equal to [Charge] Count on this unit
   PL:
583. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 3, efekt 4 — opis] [EnemyKill] 모든 적의 정신력 10 감소.
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] All enemies lose 10 Sp.
   PL:
584. [Umiejętność wroga [107804] (ulepszenie 1) — moneta 3, efekt 5 — opis] [EnemyKillFail] 다음 턴에 [Paralysis] 2 얻음.
   źródło: Skills_Abnormality91-5-hard.json :: dataList[id=107804].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKillFail], [Paralysis]
   znaczenie tagów: [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Paralysis] = 마비 / Paralyze
   EN: [EnemyKillFail] Gain 2 [Paralysis] next turn.
   PL:

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Abnormality_Mirror7-extreme
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Abnormality_Mirror7-extreme.json`

585. [Umiejętność wroga [139001] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139001].levelList[level=1].name
   limit: do 40 znaków
   EN: Slam
   PL:
586. [Umiejętność wroga [139001] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Combustion]이나 [Laceration]이 있으면, 기본 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has [Combustion] or [Laceration], Base Power +2
   PL:
587. [Umiejętność wroga [139001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
588. [Umiejętność wroga [139001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +4 [Laceration] Count
   PL:
589. [Umiejętność wroga [139002] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139002].levelList[level=1].name
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [139002] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Combustion]이나 [Laceration]이 있으면, 기본 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139002].levelList[level=1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [139002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [139002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [139003] (ulepszenie 1) — nazwa] 땅울림
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139003].levelList[level=1].name
   limit: do 40 znaków
   EN: Quake
   PL:
594. [Umiejętność wroga [139003] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Combustion]이나 [Laceration]이 있으면, 합 위력 +3
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has [Combustion] or [Laceration], Clash Power +3
   PL:
595. [Umiejętność wroga [139003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
596. [Umiejętność wroga [139004] (ulepszenie 1) — nazwa] 산제물 의식
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139004].levelList[level=1].name
   limit: do 40 znaków
   EN: Live Offering
   PL:
597. [Umiejętność wroga [139004] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Combustion]이나 [Laceration]이 있으면, 합 위력 +3
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139004].levelList[level=1].desc
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [139004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count next turn
   PL:
599. [Umiejętność wroga [139005] (ulepszenie 1) — nazwa] 타오르는 우주
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139005].levelList[level=1].name
   limit: do 40 znaków
   EN: Universe Aflame
   PL:
600. [Umiejętność wroga [139006] (ulepszenie 1) — nazwa] 굳건한 제단
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139006].levelList[level=1].name
   limit: do 40 znaków
   EN: Stalwart Altar
   PL:
601. [Umiejętność wroga [139006] (ulepszenie 1) — opis] [StartBattle] [Combustion]이 있는 모든 적의 [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139006].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Combustion]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Combustion] = 화상 / Burn
   EN: [StartBattle] Inflict +3 [Combustion] Count on all enemies that have [Combustion]
   PL:
602. [Umiejętność wroga [139007] (ulepszenie 1) — nazwa] 타오르는 우주
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139007].levelList[level=1].name
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [139007] (ulepszenie 1) — opis] [CantDuel]\n아군을 타겟으로 지정
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139007].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nTargets allies
   PL:
604. [Umiejętność wroga [139101] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139101].levelList[level=1].name
   limit: do 40 znaków
   EN: Lunge
   PL:
605. [Umiejętność wroga [139101] (ulepszenie 1) — opis] [WhenUse] 자신을 제외한 살아있는 종말 토우 1명당 합 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Clash Power +1 for every other surviving Doomsday Clay Doll
   PL:
606. [Umiejętność wroga [139101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [139102] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139102].levelList[level=1].name
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [139102] (ulepszenie 1) — opis] [WhenUse] 자신을 제외한 살아있는 종말 토우 1명당 합 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139102].levelList[level=1].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [139102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
610. [Umiejętność wroga [139102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność wroga [139201] (ulepszenie 1) — nazwa] 불 뿜기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139201].levelList[level=1].name
   limit: do 40 znaków
   EN: Belch Fire
   PL:
612. [Umiejętność wroga [139201] (ulepszenie 1) — opis] [WhenUse] 자신을 제외한 살아있는 종말 토우 1명당 합 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Clash Power +2 for every other surviving Doomsday Clay Doll
   PL:
613. [Umiejętność wroga [139201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL:
614. [Umiejętność wroga [139201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, [Combustion] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has [Laceration], inflict 5 [Combustion]
   PL:
615. [Umiejętność wroga [139202] (ulepszenie 1) — nazwa] 고통스러운 찌르기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139202].levelList[level=1].name
   limit: do 40 znaków
   EN: Severe Lunge
   PL:
616. [Umiejętność wroga [139202] (ulepszenie 1) — opis] [WhenUse] 자신을 제외한 살아있는 종말 토우 1명당 합 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139202].levelList[level=1].desc
   (powtórzenie elementu 612 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [139202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
618. [Umiejętność wroga [139202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL:
619. [Umiejętność wroga [139203] (ulepszenie 1) — nazwa] 고통스러운 할퀴기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139203].levelList[level=1].name
   limit: do 40 znaków
   EN: Raw Claw
   PL:
620. [Umiejętność wroga [139203] (ulepszenie 1) — opis] [WhenUse] 자신을 제외한 살아있는 종말 토우 1명당 합 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139203].levelList[level=1].desc
   (powtórzenie elementu 612 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [139203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [139203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, [Combustion] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [139203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [139203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [139301] (ulepszenie 1) — nazwa] 6463
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139301].levelList[level=1].name
   limit: do 40 znaków
   EN: 6463
   PL:
626. [Umiejętność wroga [139301] (ulepszenie 1) — opis] [AccumulatedPastMirror] 50당 피해량 +10%\n[WhenUse] 대상의 [Vibration] 위력과 횟수의 합 10당 기본 위력 +1 (최대 3)\n[WhenUse] 자신의 [AccumulatedPastMirror]가 홀수이면, 이 스킬의 피해량 +30%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139301].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPastMirror], [WhenUse], [Vibration]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: Deal +10% damage for every 50 [AccumulatedPastMirror]\n[WhenUse] Base Power +1 for every 10 ([Vibration] Potency + Count) on target (max 3)\n[WhenUse] If this unit's [AccumulatedPastMirror] is an odd number, this Skill deals +30% damage
   PL:
627. [Umiejętność wroga [139301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +2 [Vibration] Count
   PL:
628. [Umiejętność wroga [139301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL:
629. [Umiejętność wroga [139302] (ulepszenie 1) — nazwa] 6753
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139302].levelList[level=1].name
   limit: do 40 znaków
   EN: 6753
   PL:
630. [Umiejętność wroga [139302] (ulepszenie 1) — opis] [AccumulatedPastMirror] 50당 피해량 +10%\n[WhenUse] 대상의 [Vibration] 위력과 횟수의 합 10당 기본 위력 +1 (최대 3)\n[WhenUse] 자신의 [AccumulatedPastMirror]가 짝수이면, [Protection] 3 얻음 (턴당 1회)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139302].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPastMirror], [WhenUse], [Vibration], [Protection]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Protection] = 보호 / Protection
   EN: Deal +10% damage for every 50 [AccumulatedPastMirror]\n[WhenUse] Base Power +1 for every 10 ([Vibration] Potency + Count) on target (max 3)\n[WhenUse] If this unit's [AccumulatedPastMirror] is an even number, gain 3 [Protection] (once per turn)
   PL:
631. [Umiejętność wroga [139302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 627 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [139302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL:
633. [Umiejętność wroga [139303] (ulepszenie 1) — nazwa] 853
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139303].levelList[level=1].name
   limit: do 40 znaków
   EN: 853
   PL:
634. [Umiejętność wroga [139303] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 5 당, 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Clash Power +1 for every 5 [Breath] on self (max 3)
   PL:
635. [Umiejętność wroga [139303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 627 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [139303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [139303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50% 만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 50% of damage dealt
   PL:
638. [Umiejętność wroga [139303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AccumulatedPastMirror]당 피해량 +1% (최대 50%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AccumulatedPastMirror]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past
   EN: [OnSucceedAttack] Deal +1% damage for every [AccumulatedPastMirror] (max 50%)
   PL:
639. [Umiejętność wroga [139304] (ulepszenie 1) — nazwa] 5384
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139304].levelList[level=1].name
   limit: do 40 znaków
   EN: 5384
   PL:
640. [Umiejętność wroga [139304] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration] 위력과 횟수의 합 10당 합 위력 +2 (최대 4)\n[WhenUse] 모든 부위에 [Breath] 3, [Breath] 횟수 3을 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139304].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Breath] = 호흡 / Poise
   EN: [WhenUse] Clash Power +2 for every 10 ([Vibration] Potency + Count) on target (max 4)\n[WhenUse] All Parts gain 3 [Breath] and +3 [Breath] Count
   PL:
641. [Umiejętność wroga [139304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath]만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Raise Stagger Threshold equal to [Breath]
   PL:
642. [Umiejętność wroga [139304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3당 피해량 +20% (최대 100%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Deal +20% damage for every 3 [Breath] (max 100%)
   PL:
643. [Umiejętność wroga [139304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 모든 부위에 [Breath] 4를 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] All Parts gain 4 [Breath]
   PL:
644. [Umiejętność wroga [139305] (ulepszenie 1) — nazwa] 6475384
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139305].levelList[level=1].name
   limit: do 40 znaków
   EN: 6475384
   PL:
645. [Umiejętność wroga [139305] (ulepszenie 1) — opis] [Breath]이 7 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 7+ [Breath], Coin Power +1
   PL:
646. [Umiejętność wroga [139305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath]이 5 이상이면, 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] At 5+ [Breath], raise Stagger Threshold by 50% of damage dealt
   PL:
647. [Umiejętność wroga [139305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 모든 부위에 [Breath] 8, [Breath] 횟수 4를 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] All Parts gain 8 [Breath] and +4 [Breath] Count
   PL:
648. [Umiejętność wroga [139305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [139305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Umiejętność wroga [139306] (ulepszenie 1) — nazwa] 974569A
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139306].levelList[level=1].name
   limit: do 40 znaków
   EN: 974569A
   PL:
651. [Umiejętność wroga [139306] (ulepszenie 1) — opis] [Breath]이 10 이상이면, 스킬 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 10+ [Breath], Skill Power +2
   PL:
652. [Umiejętność wroga [139306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [AccumulatedPastMirror]당 피해량 +1% (최대 200%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AccumulatedPastMirror]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past
   EN: Deal +1% damage for every [AccumulatedPastMirror] (max 200%)
   PL:
653. [Umiejętność wroga [139306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [AccumulatedPastMirror] 50당 [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소 (최대 5회 발동)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AccumulatedPastMirror], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] for every 50 [AccumulatedPastMirror]; then, reduce target's [Vibration] Count by 1 (max 5 times)
   PL:
654. [Umiejętność wroga [139401] (ulepszenie 1) — nazwa] 끄!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139401].levelList[level=1].name
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [139401] (ulepszenie 1) — opis] [WhenUse] 살아있는 닭 1마리당 합 위력 +1\n[WhenUse] 살아있는 닭 2마리당 부정적인 효과 부여량 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139401].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Clash Power +1 for every surviving Raw Chicken\n[WhenUse] Inflict +1 additional negative effect for every 2 surviving Raw Chicken
   PL:
656. [Umiejętność wroga [139401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Umiejętność wroga [139401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL:
658. [Umiejętność wroga [139402] (ulepszenie 1) — nazwa] 끅
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].name
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [139402] (ulepszenie 1) — opis] [WhenUse] 살아있는 닭 1마리당 합 위력 +1\n[WhenUse] 살아있는 닭 2마리당 부정적인 효과 부여량 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].desc
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [139402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [139402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Umiejętność wroga [139402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność wroga [139402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 1, [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] and +5 [Vibration] Count
   PL:
664. [Umiejętność wroga [139402] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139402].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
665. [Umiejętność wroga [139403] (ulepszenie 1) — nazwa] 끄그극!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139403].levelList[level=1].name
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Umiejętność wroga [139403] (ulepszenie 1) — opis] 정신력이 가장 낮은 대상 우선 공격\n[OnSucceedAttack] 생닭 생산
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Prioritizes targets that have the lowest SP\n[OnSucceedAttack] Spawn a Raw Chicken
   PL:
667. [Umiejętność wroga [139403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 7 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 7 [Sinking]
   PL:
668. [Umiejętność wroga [139403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 정신력 10 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 10 SP
   PL:
669. [Umiejętność wroga [139404] (ulepszenie 1) — nazwa] 끄그극…
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139404].levelList[level=1].name
   limit: do 40 znaków
   EN: Keghgh...
   PL:
670. [Umiejętność wroga [139404] (ulepszenie 1) — opis] [StartBattle] (살아있는 닭 x 100) 만큼 보호막 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain (surviving Raw Chicken x 100) Shield
   PL:
671. [Umiejętność wroga [139501] (ulepszenie 1) — nazwa] 꼬옥곡
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139501].levelList[level=1].name
   limit: do 40 znaków
   EN: Cluckkegh
   PL:
672. [Umiejętność wroga [139501] (ulepszenie 1) — opis] 체력이 가장 낮은 대상 우선 공격\n[WhenUse] 대상보다 속도가 낮으면, 자신의 속도 만큼 합 위력 증가[TabExplain] (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139501].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Prioritizes targets that have the lowest HP\n[WhenUse] If this unit's Speed is slower than the target's, gain Clash Power equal to this unit's Speed (max 3)
   PL:
673. [Umiejętność wroga [139501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL:
674. [Umiejętność wroga [139502] (ulepszenie 1) — nazwa] 꼬고꼭
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139502].levelList[level=1].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność wroga [139502] (ulepszenie 1) — opis] 체력이 가장 낮은 대상 우선 공격\n[WhenUse] 대상보다 속도가 낮으면, 자신의 속도 만큼 합 위력 증가[TabExplain] (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139502].levelList[level=1].desc
   (powtórzenie elementu 672 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność wroga [139502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [139502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
678. [Umiejętność wroga [139502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [139502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [139503] (ulepszenie 1) — nazwa] 끄극
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139503].levelList[level=1].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [139503] (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 -15
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139503].levelList[level=1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [139601] (ulepszenie 1) — nazwa] 끄끄끅!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139601].levelList[level=1].name
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Umiejętność wroga [139601] (ulepszenie 1) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +3\n[WhenUse] 대상보다 속도가 높으면, 자신의 속도 만큼 합 위력 증가[TabExplain] (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139601].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If this unit did not take damage in the previous turn, Coin Power +3\n[WhenUse] If this unit's Speed is faster than the target's, gain Clash Power equal to this unit's Speed (max 3)
   PL:
684. [Umiejętność wroga [139601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 3 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 3 [Agility] next turn
   PL:
685. [Umiejętność wroga [139602] (ulepszenie 1) — nazwa] 끄끄옥!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139602].levelList[level=1].name
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność wroga [139602] (ulepszenie 1) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +3\n[WhenUse] 대상보다 속도가 높으면, 자신의 속도 만큼 합 위력 증가[TabExplain] (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139602].levelList[level=1].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Umiejętność wroga [139602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Umiejętność wroga [139602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Umiejętność wroga [139602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [139602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL:
691. [Umiejętność wroga [139603] (ulepszenie 1) — nazwa] 끄극!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139603].levelList[level=1].name
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność wroga [139603] (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 -15
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139603].levelList[level=1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Umiejętność wroga [139701] (ulepszenie 1) — nazwa] 끄극
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139701].levelList[level=1].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [139701] (ulepszenie 1) — opis] 체력이 가장 높은 대상 우선 공격\n[WhenUse] 대상보다 속도가 낮으면, 자신의 속도 만큼 합 위력 증가[TabExplain] (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139701].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Prioritizes targets that have the highest HP\n[WhenUse] If this unit's Speed is slower than the target's, gain Clash Power equal to this unit's Speed (max 3)
   PL:
695. [Umiejętność wroga [139701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL:
696. [Umiejętność wroga [139702] (ulepszenie 1) — nazwa] 끄꾸우곡
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139702].levelList[level=1].name
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Umiejętność wroga [139702] (ulepszenie 1) — opis] 체력이 가장 높은 대상 우선 공격\n[WhenUse] 대상보다 속도가 낮으면, 자신의 속도 만큼 합 위력 증가[TabExplain] (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139702].levelList[level=1].desc
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność wroga [139702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [139702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność wroga [139702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 7 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [139702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1, [Paralysis] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Binding] and 1 [Paralysis] next turn
   PL:
702. [Umiejętność wroga [139703] (ulepszenie 1) — nazwa] 끅!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139703].levelList[level=1].name
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [139703] (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 -15
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139703].levelList[level=1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność wroga [139801] (ulepszenie 1) — nazwa] 울음 찰싹
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139801].levelList[level=1].name
   limit: do 40 znaków
   EN: Crying Slap
   PL:
705. [Umiejętność wroga [139801] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 -15
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Target loses 15 SP
   PL:
706. [Umiejętność wroga [139801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność wroga [139801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5, [Sinking] 횟수 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking] and +5 [Sinking] Count
   PL:
708. [Umiejętność wroga [139802] (ulepszenie 1) — nazwa] 우울음 철썩
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139802].levelList[level=1].name
   limit: do 40 znaków
   EN: Gloomy Slap
   PL:
709. [Umiejętność wroga [139802] (ulepszenie 1) — opis] [StartDuel] 대상의 정신력 +10
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartDuel]
   znaczenie tagów: [StartDuel] = [합 시작 시] / [Clash Start]
   EN: [StartDuel] Target heals 10 SP
   PL:
710. [Umiejętność wroga [139802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [AlwaysUse] 피해의 절반만큼 정신력 피해를 입힘
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AlwaysUse]
   znaczenie tagów: [AlwaysUse] = [상시] / [Constant]
   EN: [AlwaysUse] Deal SP damage by half of damage displayed
   PL:
711. [Umiejętność wroga [139802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [AlwaysUse] 피해는 0이 됨
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AlwaysUse]
   znaczenie tagów: [AlwaysUse] = [상시] / [Constant]
   EN: [AlwaysUse] No HP damage is dealt
   PL:
712. [Umiejętność wroga [139803] (ulepszenie 1) — nazwa] 녹아내릴 눈알
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139803].levelList[level=1].name
   limit: do 40 znaków
   EN: Melty Eyeball
   PL:
713. [Umiejętność wroga [139803] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 -10\n정신력이 0 미만인 대상 공격 시 피해량 +50%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Target loses 10 SP\nIf target's SP is below 0, deal +50% Damage
   PL:
714. [Umiejętność wroga [139803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking]만큼 추가 체력 피해
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Deal Bonus HP damage equal to [Sinking] Potency on target
   PL:
715. [Umiejętność wroga [139803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking]만큼 추가 정신력 피해
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Deal Bonus SP damage equal to [Sinking] Potency on target
   PL:
716. [Umiejętność wroga [139804] (ulepszenie 1) — nazwa] 몰아치는 우울
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139804].levelList[level=1].name
   limit: do 40 znaków
   EN: Gushing Gloom
   PL:
717. [Umiejętność wroga [139804] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 -5\n[Sinking]이 가장 많은 대상 우선 공격\n정신력이 0 미만인 대상 공격 시 피해량 +30%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139804].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Target loses 5 SP\nPrioritizes targets that have the most [Sinking]\nIf target has less than 0 SP, deal +30% damage
   PL:
718. [Umiejętność wroga [139804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
719. [Umiejętność wroga [139804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking]만큼 추가 체력 피해
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 714 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [139804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking]만큼 추가 정신력 피해
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [139805] (ulepszenie 1) — nazwa] 눈알추
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139805].levelList[level=1].name
   limit: do 40 znaków
   EN: Eyeball Weight
   PL:
722. [Umiejętność wroga [139805] (ulepszenie 1) — opis] [DefeatDuel] 모든 스킬 취소\n[DefeatDuel] [Vulnerable] 3 얻음\n정신력이 0 미만인 대상 공격 시 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139805].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [Vulnerable]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [DefeatDuel] Cancel all Skills\n[DefeatDuel] Gain 3 [Vulnerable]\nIf target has less than 0 SP, deal +100% damage
   PL:
723. [Umiejętność wroga [139805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 가지고 있는 [Sinking], [Sinking] 횟수를 2배로 만듦
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Double target's [Sinking] and [Sinking] Count
   PL:
724. [Umiejętność wroga [139806] (ulepszenie 1) — nazwa] 꾸엉
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139806].levelList[level=1].name
   limit: do 40 znaków
   EN: Croohoo
   PL:
725. [Umiejętność wroga [139806] (ulepszenie 1) — opis] [StartBattle] [Protection] 2 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139806].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] Gain 2 [Protection]
   PL:
726. [Umiejętność wroga [139901] (ulepszenie 1) — nazwa] 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139901].levelList[level=1].name
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [139901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL:
728. [Umiejętność wroga [139902] (ulepszenie 1) — nazwa] 강한 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139902].levelList[level=1].name
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność wroga [139902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 3 [Reduction] next turn
   PL:
730. [Umiejętność wroga [139903] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139903].levelList[level=1].name
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [139903] (ulepszenie 1) — opis] [DefeatDuel] 모든 스킬 취소\n[DefeatDuel] [Vulnerable] 3 얻음\n정신력이 0 미만인 대상 공격 시 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139903].levelList[level=1].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [139903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
733. [Umiejętność wroga [139903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 3 [Vulnerable] next turn
   PL:
734. [Umiejętność wroga [139904] (ulepszenie 1) — nazwa] 주머니 압박
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139904].levelList[level=1].name
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [139904] (ulepszenie 1) — opis] [DefeatDuel] 모든 스킬 취소\n[DefeatDuel] [Vulnerable] 3 얻음\n정신력이 0 미만인 대상 공격 시 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139904].levelList[level=1].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Umiejętność wroga [139904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [139905] (ulepszenie 1) — nazwa] 혈사포
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139905].levelList[level=1].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność wroga [139905] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL:
739. [Umiejętność wroga [139905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Umiejętność wroga [139905] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If target has a negative effect, deal +50% damage
   PL:
741. [Umiejętność wroga [139905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 20 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 20 [Laceration]
   PL:
742. [Umiejętność wroga [139906] (ulepszenie 1) — nazwa] 종혈
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139906].levelList[level=1].name
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Umiejętność wroga [139906] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139906].levelList[level=1].desc
   (powtórzenie elementu 738 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność wroga [139906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [139906] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If target has a negative effect, deal +100% damage
   PL:
746. [Umiejętność wroga [139906] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 30 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=139906].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 30 [Laceration]
   PL:
747. [Umiejętność wroga [140001] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140001].levelList[level=1].name
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Umiejętność wroga [140001] (ulepszenie 1) — opis] 자신의 [DogThunder] 1당, 코인 위력 +2 (최대 6)\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +20% (최대 80%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140001].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DogThunder], [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [DogThunder] = 번개 / Lightning; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: Coin Power +2 for every [DogThunder] on self (max 6)\n[WhenUse] Deal +20% damage for every 5 ([Laceration] + [Burst] on target) (max 80%)
   PL:
749. [Umiejętność wroga [140001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Laceration] 10 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration] next turn
   PL:
750. [Umiejętność wroga [140002] (ulepszenie 1) — nazwa] 등압
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140002].levelList[level=1].name
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [140002] (ulepszenie 1) — opis] 자신의 [DogThunder] 1당, 코인 위력 +2 (최대 6)\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +20% (최대 80%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140002].levelList[level=1].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność wroga [140002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst] next turn
   PL:
753. [Umiejętność wroga [140003] (ulepszenie 1) — nazwa] 등압추격
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140003].levelList[level=1].name
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [140003] (ulepszenie 1) — opis] 자신의 [DogThunder] 1당, 코인 위력 +1 (최대 3)\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +15% (최대 60%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140003].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DogThunder], [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [DogThunder] = 번개 / Lightning; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every [DogThunder] on self (max 3)\n[WhenUse] Deal +15% damage for every 5 ([Laceration] + [Burst] on target) (max 60%)
   PL:
755. [Umiejętność wroga [140003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Umiejętność wroga [140003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +4 [Burst] Count next turn
   PL:
757. [Umiejętność wroga [140004] (ulepszenie 1) — nazwa] 하울링
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140004].levelList[level=1].name
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Umiejętność wroga [140004] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
759. [Umiejętność wroga [140004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Umiejętność wroga [140004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Paralysis]
   PL:
761. [Umiejętność wroga [140004] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140004].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
762. [Umiejętność wroga [140004] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Disarming] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140004].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Disarming]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: [OnSucceedAttack] Inflict 4 [Disarming]
   PL:
763. [Umiejętność wroga [140005] (ulepszenie 1) — nazwa] 전격 하울링
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140005].levelList[level=1].name
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność wroga [140005] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140005].levelList[level=1].desc
   (powtórzenie elementu 758 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność wroga [140005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność wroga [140005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Umiejętność wroga [140005] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 10 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140005].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 10 [Burst] next turn
   PL:
768. [Umiejętność wroga [140006] (ulepszenie 1) — nazwa] 피뢰
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140006].levelList[level=1].name
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [140006] (ulepszenie 1) — opis] 자신의 [DogThunder] 1당, 코인 위력 +1 (최대 3)\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +20% (최대 80%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140006].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DogThunder], [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [DogThunder] = 번개 / Lightning; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every [DogThunder] on self (max 3)\n[WhenUse] Deal +20% damage for every 5 ([Laceration] + [Burst] on target) (max 80%)
   PL:
770. [Umiejętność wroga [140006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 5 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst] and +2 [Burst] Count next turn
   PL:
771. [Umiejętność wroga [140007] (ulepszenie 1) — nazwa] 적뢰
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140007].levelList[level=1].name
   (powtórzenie elementu 134 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Umiejętność wroga [140007] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +15% (최대 60%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140007].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] Deal +15% damage for every 5 ([Laceration] + [Burst]) on target (max 60%)
   PL:
773. [Umiejętność wroga [140007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 10 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność wroga [140007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count next turn
   PL:
775. [Umiejętność wroga [140008] (ulepszenie 1) — nazwa] 하울링
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140008].levelList[level=1].name
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [140008] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140008].levelList[level=1].desc
   (powtórzenie elementu 758 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Umiejętność wroga [140008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [140008] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140008].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Umiejętność wroga [140008] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Disarming] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140008].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Umiejętność wroga [140101] (ulepszenie 1) — nazwa] 기괴한 눈동자
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140101].levelList[level=1].name
   limit: do 40 znaków
   EN: Eerie Eyes
   PL:
781. [Umiejętność wroga [140101] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 0미만이면, 기본 위력 +2\n[WhenUse] [Aggressive] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggressive]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggressive] = 본능 / Instincts
   EN: [WhenUse] If target has less than 0 SP, Base Power +2\n[WhenUse] Gain 1 [Aggressive]
   PL:
782. [Umiejętność wroga [140101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 7
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 7 SP damage
   PL:
783. [Umiejętność wroga [140101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 7
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [140102] (ulepszenie 1) — nazwa] 어설픈 모방
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140102].levelList[level=1].name
   limit: do 40 znaków
   EN: Imperfect Imitation
   PL:
785. [Umiejętność wroga [140102] (ulepszenie 1) — opis] 피격 당한 공격을 모방하여 사용.\n[WhenUse] 대상에게 정신 피해 10\n[WhenUse] [Aggressive] 2 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggressive]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggressive] = 본능 / Instincts
   EN: Copies a Skill that hit this unit\n[WhenUse] Deal 10 SP damage\n[WhenUse] Gain 2 [Aggressive]
   PL:
786. [Umiejętność wroga [140103] (ulepszenie 1) — nazwa] 껍데기 고치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140103].levelList[level=1].name
   limit: do 40 znaków
   EN: Adjust Shell
   PL:
787. [Umiejętność wroga [140103] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 0미만이면, 기본 위력 +2\n[WhenUse] [Aggressive] 5 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140103].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggressive], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggressive] = 본능 / Instincts; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has less than 0 SP, Base Power +2\n[WhenUse] Gain 5 [Aggressive]\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
788. [Umiejętność wroga [140103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność wroga [140103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신 피해 7
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [140103] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 최대 체력의 10%만큼 체력 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140103].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal 10% HP
   PL:
791. [Umiejętność wroga [140104] (ulepszenie 1) — nazwa] 뼈 폭발
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140104].levelList[level=1].name
   limit: do 40 znaków
   EN: Bone Blast
   PL:
792. [Umiejętność wroga [140104] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 0미만이면, 기본 위력 +2\n[WhenUse] [Aggressive] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140104].levelList[level=1].desc
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [140104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność wroga [140104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration]
   PL:
795. [Umiejętność wroga [140201] (ulepszenie 1) — nazwa] 기괴한 눈동자
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140201].levelList[level=1].name
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [140201] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 0미만이면, 기본 위력 +2\n[WhenUse] [Aggressive] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140201].levelList[level=1].desc
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [140201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL:
798. [Umiejętność wroga [140201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 797 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [140202] (ulepszenie 1) — nazwa] 어설픈 모방
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140202].levelList[level=1].name
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [140202] (ulepszenie 1) — opis] 피격 당한 공격을 모방하여 사용.\n[WhenUse] 대상에게 정신 피해 10\n[WhenUse] [Aggressive] 2 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140202].levelList[level=1].desc
   (powtórzenie elementu 785 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [140203] (ulepszenie 1) — nazwa] 껍데기 고치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140203].levelList[level=1].name
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [140203] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 0미만이면, 기본 위력 +2\n[WhenUse] [Aggressive] 5 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140203].levelList[level=1].desc
   (powtórzenie elementu 787 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność wroga [140203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [140203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신 피해 5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 797 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [140203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 최대 체력의 10%만큼 체력 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [140204] (ulepszenie 1) — nazwa] 뼈 폭발
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140204].levelList[level=1].name
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [140204] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 0미만이면, 기본 위력 +2\n[WhenUse] [Aggressive] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140204].levelList[level=1].desc
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [140204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [140204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 794 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [140301] (ulepszenie 1) — nazwa] 거친 할퀴기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140301].levelList[level=1].name
   limit: do 40 znaków
   EN: Violent Scratch
   PL:
811. [Umiejętność wroga [140301] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 3+ [Laceration], Coin Power +1
   PL:
812. [Umiejętność wroga [140301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
813. [Umiejętność wroga [140301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [140301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [140302] (ulepszenie 1) — nazwa] 광적인 돌진
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140302].levelList[level=1].name
   limit: do 40 znaków
   EN: Rabid Ram
   PL:
816. [Umiejętność wroga [140302] (ulepszenie 1) — opis] 체력이 가장 낮은 적 공격\n[WhenUse] 대상의 [Laceration]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140302].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Targets the unit that has the lowest HP\n[WhenUse] If target has 3+ [Laceration], Coin Power +1
   PL:
817. [Umiejętność wroga [140302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
818. [Umiejętność wroga [140302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 817 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [140303] (ulepszenie 1) — nazwa] 갈기갈기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear Apart
   PL:
820. [Umiejętność wroga [140303] (ulepszenie 1) — opis] 체력이 가장 낮은 적 공격\n[WhenUse] 대상의 [Laceration]이 3 이상이면, 코인 위력 +1\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the unit that has the lowest HP\n[WhenUse] If target has 3+ [Laceration], Coin Power +1\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
821. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL:
825. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [140303] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140303].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL:
829. [Umiejętność wroga [140304] (ulepszenie 1) — nazwa] 광폭한 추격
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140304].levelList[level=1].name
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność wroga [140304] (ulepszenie 1) — opis] 체력이 가장 낮은 적 공격\n[WhenUse] 대상의 [Laceration] 3당, 기본 위력 +2 (최대 4)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140304].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Targets the unit that has the lowest HP\n[WhenUse] Base Power +2 for every 3 [Laceration] on target (max 4)
   PL:
831. [Umiejętność wroga [140304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 6 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +6 [Laceration] Count
   PL:
832. [Umiejętność wroga [140304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +3 [Burst] Count
   PL:
833. [Umiejętność wroga [140305] (ulepszenie 1) — nazwa] 날 선 경계
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140305].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [140305] (ulepszenie 1) — opis] [OnSucceedEvade] [Aggressive] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Aggressive]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Aggressive] = 본능 / Instincts
   EN: [OnSucceedEvade] Gain 1 [Aggressive]
   PL:
835. [Umiejętność wroga [140401] (ulepszenie 1) — nazwa] 휘감는 팔
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140401].levelList[level=1].name
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [140401] (ulepszenie 1) — opis] [WhenUse] 대상에게 부정적인 효과가 2개 이상 있으면, 기본 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has 2+ types of negative effect, Base Power +2
   PL:
837. [Umiejętność wroga [140401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [140402] (ulepszenie 1) — nazwa] 똬리 틀기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140402].levelList[level=1].name
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [140402] (ulepszenie 1) — opis] [WhenUse] 대상에게 부정적인 효과가 2개 이상 있으면, 코인 위력 +1\n[DefeatDuel] [Aggressive] 1 잃음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140402].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Aggressive]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Aggressive] = 본능 / Instincts
   EN: [WhenUse] If target has 2+ types of negative effect, Coin Power +1\n[DefeatDuel] Lose 1 [Aggressive]
   PL:
840. [Umiejętność wroga [140402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 20 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20 HP
   PL:
841. [Umiejętność wroga [140402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
842. [Umiejętność wroga [140403] (ulepszenie 1) — nazwa] 양팔 휘두르기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140403].levelList[level=1].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
