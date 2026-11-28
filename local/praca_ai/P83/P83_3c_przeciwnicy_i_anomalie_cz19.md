# Paczka AI P83 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 19/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P83_3c_przeciwnicy_i_anomalie_cz19.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P83_3c_przeciwnicy_i_anomalie_cz19.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [refraction2] Wróg / część: Enemies_Refraction2
- plik gry: `Enemies_Refraction2.json`

1. [[refraction2] Wróg / część [8570] — nazwa] 굴절된 질투를 머금은 장미
   źródło: Enemies_Refraction2.json :: dataList[id=8570].name
   limit: do 40 znaków
   EN: Refracted Envy-drenched Rose
   PL:
2. [[refraction2] Wróg / część [8570] — opis] 본체
   źródło: Enemies_Refraction2.json :: dataList[id=8570].desc
   limit: do 120 znaków
   EN: Core
   PL:
3. [[refraction2] Wróg / część [857001] — nazwa] 꽃
   źródło: Enemies_Refraction2.json :: dataList[id=857001].name
   limit: do 40 znaków
   EN: Flower
   PL:
4. [[refraction2] Wróg / część [857001] — opis] 부위
   źródło: Enemies_Refraction2.json :: dataList[id=857001].desc
   limit: do 120 znaków
   EN: Part
   PL:

## [refraction2] Umiejętności wrogów / Anomalii — Skills_Abnormality_Refraction2
- grupa rozdziału/trybu: `refraction2` · plik: `Skills_Abnormality_Refraction2.json`

5. [Umiejętność wroga [853901] (ulepszenie 1) — nazwa] 침울한 신음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853901].levelList[level=1].name
   limit: do 40 znaków
   EN: Gloomy Moan
   PL:
6. [Umiejętność wroga [853901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL:
7. [Umiejętność wroga [853902] (ulepszenie 1) — nazwa] 몰아치는 침잠
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853902].levelList[level=1].name
   limit: do 40 znaków
   EN: Unrelenting Sinking
   PL:
8. [Umiejętność wroga [853902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL:
9. [Umiejętność wroga [853902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
10. [Umiejętność wroga [853903] (ulepszenie 1) — nazwa] 슬픔의 반동
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853903].levelList[level=1].name
   limit: do 40 znaków
   EN: Sorrowful Recoil
   PL:
11. [Umiejętność wroga [853903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count
   PL:
12. [Umiejętność wroga [853903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
13. [Umiejętność wroga [853904] (ulepszenie 1) — nazwa] 슬픔의 격류
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853904].levelList[level=1].name
   limit: do 40 znaków
   EN: Sorrowful Torrent
   PL:
14. [Umiejętność wroga [853904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL:
15. [Umiejętność wroga [853904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
16. [Umiejętność wroga [853904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
17. [Umiejętność wroga [853905] (ulepszenie 1) — nazwa] 무언가를 찾는 울음소리
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853905].levelList[level=1].name
   limit: do 40 znaków
   EN: Cries Seeking Something
   PL:
18. [Umiejętność wroga [853905] (ulepszenie 1) — opis] 합 진행 시 살아있는 낡은 우산당 합 위력 +2\n낡은 우산당 피해량 +25%\n턴 종료 시 낡은 우산 모두 소멸\n턴 종료 시 1턴에 얻은 <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">보호 우산</color></link></u>만큼 <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">보호 우산</color></link></u>을 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853905].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <sprite name="WaveFoxUmbrella">, <color=#f8c200>, <u>, <link="WaveFoxUmbrella">, </color>, </link>, </u>, \n
   EN: Clash Power +2 for every surviving Old Umbrella\nDeal +25% damage for every Old Umbrella\nAt the end of the turn, all Old Umbrella expire\nAt the end of the turn, gain <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">Protection Umbrella</color></link></u> equal to the number of <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">Protection Umbrella</color></link></u> gained in the first turn
   PL:
19. [Umiejętność wroga [853905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Sinking
   PL:
20. [Umiejętność wroga [853906] (ulepszenie 1) — nazwa] 기다림
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853906].levelList[level=1].name
   limit: do 40 znaków
   EN: Waiting
   PL:
21. [Umiejętność wroga [853906] (ulepszenie 1) — opis] [StartBattle] 모든 적 정신력 -20
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853906].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] All enemies lose 20 SP
   PL:
22. [Umiejętność wroga [853907] (ulepszenie 1) — nazwa] 날카로운 반응
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853907].levelList[level=1].name
   limit: do 40 znaków
   EN: Volatile Response
   PL:
23. [Umiejętność wroga [853907] (ulepszenie 1) — opis] [StartBattle] <sprite name="Thorn"><color=#a16a3b><u><link="Thorn">가시</color></link></u>를 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853907].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Thorn">, <color=#a16a3b>, <u>, <link="Thorn">, </color>, </link>, </u>, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain <sprite name="Thorn"><color=#a16a3b><u><link="Thorn">Thorns</color></link></u>
   PL:
24. [Umiejętność wroga [853908] (ulepszenie 1) — nazwa] 날카로운 반응
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853908].levelList[level=1].name
   limit: do 40 znaków
   EN: Volatile Reaction
   PL:
25. [Umiejętność wroga [853908] (ulepszenie 1) — opis] [StartBattle] <sprite name="Thorn"><color=#a16a3b><u><link="Thorn">가시</color></link></u>를 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853908].levelList[level=1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
26. [Umiejętność wroga [853909] (ulepszenie 1) — nazwa] 애원하는 울음소리
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853909].levelList[level=1].name
   limit: do 40 znaków
   EN: Pleading Cries
   PL:
27. [Umiejętność wroga [853909] (ulepszenie 1) — opis] 합 진행 시 살아있는 낡은 우산당 합 위력 +2\n낡은 우산당 피해량 +25%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853909].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +2 for every surviving Old Umbrella\nDeal +25% for every Old Umbrella
   PL:
28. [Umiejętność wroga [853909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=853909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Umiejętność wroga [854001] (ulepszenie 1) — nazwa] 흩뿌려지는 슬픔
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854001].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Sorrow
   PL:
30. [Umiejętność wroga [854001] (ulepszenie 1) — opis] [EndSkill] 모든 적의 파열 횟수 3, 침잠 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Inflict +3 Rupture Count and +3 Sinking Count to all enemies
   PL:
31. [Umiejętność wroga [854101] (ulepszenie 1) — nazwa] 전류 주입
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854101].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Load
   PL:
32. [Umiejętność wroga [854101] (ulepszenie 1) — opis] [StartBattle] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 2 소모\n대상에게 <sprite name="Paralysis"><color=#e30000><u><link="Paralysis">마비</color></link></u>가 있다면 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854101].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="Paralysis">, <color=#e30000>, <u>, <link="Paralysis">, </color>, </link>, </u>, \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 2 Self-charge\n[DefeatDuel] Lose 2 Self-charge\nDeal +10% damage to targets with <sprite name="Paralysis"><color=#e30000><u><link="Paralysis">Paralyze</color></link></u>
   PL:
33. [Umiejętność wroga [854101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze next turn
   PL:
34. [Umiejętność wroga [854102] (ulepszenie 1) — nazwa] 전기 방류
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854102].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Release
   PL:
35. [Umiejętność wroga [854102] (ulepszenie 1) — opis] [StartBattle] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 2 소모\n대상에게 <sprite name="Paralysis"><color=#e30000><u><link="Paralysis">마비</color></link></u>가 있다면 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854102].levelList[level=1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność wroga [854102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność wroga [854103] (ulepszenie 1) — nazwa] 전기 방출
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854103].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Discharge
   PL:
38. [Umiejętność wroga [854103] (ulepszenie 1) — opis] [StartBattle] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 2 소모\n대상에게 <sprite name="Paralysis"><color=#e30000><u><link="Paralysis">마비</color></link></u>가 있다면 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854103].levelList[level=1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Umiejętność wroga [854103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile next turn
   PL:
40. [Umiejętność wroga [854103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bind next turn
   PL:
41. [Umiejętność wroga [854103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność wroga [854104] (ulepszenie 1) — nazwa] 초고압 전기 방출
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854104].levelList[level=1].name
   limit: do 50 znaków
   EN: High-voltage Electric Discharge
   PL:
43. [Umiejętność wroga [854104] (ulepszenie 1) — opis] [WhenUse] <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">자가 충전</color></link></u>이 5 이상이면, 초과된 <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">자가 충전</color></link></u>마다 피해량 +20%\n[WhenUse] <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">자가 충전</color></link></u>당 합 위력 +1\n[WhenUse] 자가 충전 전부 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854104].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="SelfCharge">, <color=#a16a3b>, <u>, <link="SelfCharge">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 5+ <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">Self-charge</color></link></u>, deal +20% damage for each Count of <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">Self-charge</color></link></u> over 5\n[WhenUse] Clash Power +1 for every <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">Self-charge</color></link></u>\n[WhenUse] Spend all Self-charge
   PL:
44. [Umiejętność wroga [854104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Fragile next turn
   PL:
45. [Umiejętność wroga [854104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze next turn
   PL:
46. [Umiejętność wroga [854105] (ulepszenie 1) — nazwa] 똬리틀기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854105].levelList[level=1].name
   limit: do 40 znaków
   EN: Coil Up
   PL:
47. [Umiejętność wroga [854105] (ulepszenie 1) — opis] 이 스킬이 슬롯에 있을 때 머리 부위가 <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">자가 충전</color></link></u>당 50의 보호막 체력을 얻음.\n머리 부위가 파괴된 상태라면, <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">자가 충전</color></link></u>당 25의 보호막 체력을 얻음.\n자가 충전 1당 얻은 보호막 체력만큼 잃으면, 자가 충전 1씩 소모.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854105].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <sprite name="SelfCharge">, <color=#a16a3b>, <u>, <link="SelfCharge">, </color>, </link>, </u>, \n
   EN: If this Skill is on a slot, head gains 50 Shield HP for every <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">Self-charge</color></link></u>.\nIf the head is broken, gain 25 Shield HP for every <sprite name="SelfCharge"><color=#a16a3b><u><link="SelfCharge">Self-charge instead.</color></link></u>\nSpend 1 Self-charge for every amount of Shield HP lost equal to the Shield HP gained for every Self-charge
   PL:
48. [Umiejętność wroga [854106] (ulepszenie 1) — nazwa] 꿈틀거리는 머리
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854106].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Head
   PL:
49. [Umiejętność wroga [854106] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n[WhenUse] 자가 충전 1 소모\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854106].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy with the least HP\n[WhenUse] Spend 1 Self-charge\n[DefeatDuel] Lose 1 Self-charge
   PL:
50. [Umiejętność wroga [854106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [854107] (ulepszenie 1) — nazwa] 꿈틀거리는 꼬리
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854107].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Tail
   PL:
52. [Umiejętność wroga [854107] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n[WhenUse] 자가 충전 1 소모\n[DefeatDuel] 자가 충전 2 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854107].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy with the least HP\n[WhenUse] Spend 1 Self-charge\n[DefeatDuel] Lose 2 Self-charge
   PL:
53. [Umiejętność wroga [854107] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854107].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Umiejętność wroga [854201] (ulepszenie 1) — nazwa] 취하고 싶나?
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854201].levelList[level=1].name
   limit: do 40 znaków
   EN: Wanna Get Drunk?
   PL:
55. [Umiejętność wroga [854201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여, 진동 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Tremor and +2 Tremor Count
   PL:
56. [Umiejętność wroga [854202] (ulepszenie 1) — nazwa] 나눠 마시자!
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854202].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Share the Drink!
   PL:
57. [Umiejętność wroga [854202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL:
58. [Umiejętność wroga [854202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 체력 5% 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5% of Max HP
   PL:
59. [Umiejętność wroga [854203] (ulepszenie 1) — nazwa] 남은건 이것 뿐이네!
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854203].levelList[level=1].name
   limit: do 40 znaków
   EN: This is All I Got!
   PL:
60. [Umiejętność wroga [854203] (ulepszenie 1) — opis] <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>을 가진 대상 우선 공격
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Vibration">, <color=#e30000>, <u>, <link="Vibration">, </color>, </link>, </u>
   EN: Prioritizes enemies with <sprite name="Vibration"><color=#e30000><u><link="Vibration">Tremor</color></link></u>
   PL:
61. [Umiejętność wroga [854203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Tremor
   PL:
62. [Umiejętność wroga [854203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 진동 횟수만큼 [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] by target's Tremor Count
   PL:
63. [Umiejętność wroga [854203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 진동 횟수 전부 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend all of target's Tremor Count
   PL:
64. [Umiejętność wroga [854204] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854204].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Have This!
   PL:
65. [Umiejętność wroga [854204] (ulepszenie 1) — opis] 대상에게 <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>가 없다면, 합 위력 +8\n[WhenUse] 대상이 <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>가 없다면, 피해량 +150%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Tipsiness">, <color=#a16a3b>, <u>, <link="TipsinessRail">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If target has no <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">Tipsy</color></link></u>, Clash Power +8 \n[WhenUse] If target has no <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">Tipsy</color></link></u>, deal +150% damage
   PL:
66. [Umiejętność wroga [854204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>가 5 이상이라면, 가하는 피해가 0이 됨.\n신사 요정이 다음 턴에 흐트러짐 상태가 됨.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="Tipsiness">, <color=#a16a3b>, <u>, <link="TipsinessRail">, </color>, </link>, </u>, \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">Tipsy</color></link></u>, deal 0 damage.\nFairy Gentleman will be Staggered next turn.
   PL:
67. [Umiejętność wroga [854204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>를 전부 소모 시킴.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Tipsiness">, <color=#a16a3b>, <u>, <link="TipsinessRail">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove all <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">Tipsy</color></link></u>.
   PL:
68. [Umiejętność wroga [854205] (ulepszenie 1) — nazwa] 이 요정주가 좋나?
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854205].levelList[level=1].name
   limit: do 40 znaków
   EN: You Like This Brew?
   PL:
69. [Umiejętność wroga [854205] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 속박 3 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Bind next turn
   PL:
70. [Umiejętność wroga [854206] (ulepszenie 1) — nazwa] 한 잔 할텐가?
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854206].levelList[level=1].name
   limit: do 40 znaków
   EN: Have a Swig!
   PL:
71. [Umiejętność wroga [854206] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 요정주 소환\n[DefeatDuel] 요정주 체력 70%로 소환됨
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854206].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Summon Fairy Wine next turn\n[DefeatDuel] Fairy Wine summoned at 70% HP
   PL:
72. [Umiejętność wroga [854206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Umiejętność wroga [854206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL:
74. [Umiejętność wroga [854301] (ulepszenie 1) — nazwa] 달콤한 요정주
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854301].levelList[level=1].name
   limit: do 40 znaków
   EN: Sweet Fairy Wine
   PL:
75. [Umiejętność wroga [854301] (ulepszenie 1) — opis] 인격에게 죽었을 때, 모든 인격에게 다음 턴에 취기 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854301].levelList[level=1].desc
   limit: do 120 znaków
   EN: When killed by an Identity, apply 5 Tipsy to all Identities next turn
   PL:
76. [Umiejętność wroga [854401] (ulepszenie 1) — nazwa] 얽혀가는 부적
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854401].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangling Talisman
   PL:
77. [Umiejętność wroga [854401] (ulepszenie 1) — opis] [WhenUse] 대상에게 얽혀온 저주 부적 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 3 Entangled Curse Talisman
   PL:
78. [Umiejętność wroga [854401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여. 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture and +2 Rupture Count next turn
   PL:
79. [Umiejętność wroga [854402] (ulepszenie 1) — nazwa] 쌓여가는 저주
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854402].levelList[level=1].name
   limit: do 40 znaków
   EN: Cumulating Curse
   PL:
80. [Umiejętność wroga [854402] (ulepszenie 1) — opis] [WhenUse] 대상이 가지고 있는 <sprite name="WrappedCurseTag"><color=#a16a3b><u><link="WrappedCurseTag">얽혀온 저주 부적</color></link></u>만큼 얽혀온 저주 부적 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="WrappedCurseTag">, <color=#a16a3b>, <u>, <link="WrappedCurseTag">, </color>, </link>, </u>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict Entangling Talisman equal to the number of <sprite name="WrappedCurseTag"><color=#a16a3b><u><link="WrappedCurseTag">Entangling Talisman</color></link></u> on target
   PL:
81. [Umiejętność wroga [854402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 5 부여. 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture and +2 Rupture Count next turn
   PL:
82. [Umiejętność wroga [854402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여. 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [854403] (ulepszenie 1) — nazwa] 누구도 울지 않도록
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].name
   limit: do 40 znaków
   EN: So That No One Will Cry
   PL:
84. [Umiejętność wroga [854403] (ulepszenie 1) — opis] [EndBattle] 다시 붙여진 저주 부적 전부 소멸\n[WhenUse] 가지고 있는 <sprite name="ReattachedCurseTag"><color=#a16a3b><u><link="ReattachedCurseTag">다시 붙여진 저주 부적</color></link></u>이 10개 이상이면, 코인 위력 -1
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <sprite name="ReattachedCurseTag">, <color=#a16a3b>, <u>, <link="ReattachedCurseTag">, </color>, </link>, </u>, \n, [EndBattle], [WhenUse]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [WhenUse] = [사용시] / [On Use]
   EN: [EndBattle] Remove all Reattached Curse Talisman\n[WhenUse] If at 10+ <sprite name="ReattachedCurseTag"><color=#a16a3b><u><link="ReattachedCurseTag">Reattached Curse Talisman</color></link></u>, -1 Coin Power
   PL:
85. [Umiejętność wroga [854403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture next turn
   PL:
86. [Umiejętność wroga [854403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [854403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [854403] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność wroga [854403] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność wroga [854403] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854403].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bind next turn
   PL:
91. [Umiejętność wroga [854404] (ulepszenie 1) — nazwa] 이전하는 부적
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854404].levelList[level=1].name
   limit: do 40 znaków
   EN: Transferring Talisman
   PL:
92. [Umiejętność wroga [854404] (ulepszenie 1) — opis] [WhenUse] 대상의 <sprite name="WrappedCurseTag"><color=#a16a3b><u><link="WrappedCurseTag">얽혀온 저주 부적</color></link></u>을 전부 소멸.\n소멸시킨만큼 다시 붙여진 저주 부적 얻음\n[StartBattle] 모든 부위에 보호 3 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854404].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <sprite name="WrappedCurseTag">, <color=#a16a3b>, <u>, <link="WrappedCurseTag">, </color>, </link>, </u>, \n, [WhenUse], [StartBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [WhenUse] Remove all <sprite name="WrappedCurseTag"><color=#a16a3b><u><link="WrappedCurseTag">Entangled Curse Talisman</color></link></u> from target.\nGain Reattached Curse Talisman equal to number of Entangled Curse removed\n[StartBattle] All parts gain 3 Protection
   PL:
93. [Umiejętność wroga [854405] (ulepszenie 1) — nazwa] 복제되는 저주
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854405].levelList[level=1].name
   limit: do 40 znaków
   EN: Proliferating Curse
   PL:
94. [Umiejętność wroga [854405] (ulepszenie 1) — opis] [WhenUse] 대상이 가지고 있는 <sprite name="WrappedCurseTag"><color=#a16a3b><u><link="WrappedCurseTag">얽혀온 저주 부적</color></link></u>만큼 얽혀온 저주 부적 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854405].levelList[level=1].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [854501] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854501].levelList[level=1].name
   limit: do 40 znaków
   EN: Skim Wounds
   PL:
96. [Umiejętność wroga [854501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈 횟수가 2이상일 때, 출혈 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 2+ Bleed Count, inflict 5 Bleed
   PL:
97. [Umiejętność wroga [854501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 출혈 횟수가 2이상일 때, 마비 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 2+ Bleed Count, inflict 1 Paralyze
   PL:
98. [Umiejętność wroga [854501] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 출혈 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854501].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply +4 Bleed Count
   PL:
99. [Umiejętność wroga [854502] (ulepszenie 1) — nazwa] 옭아매인 상처
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854502].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangled Injury
   PL:
100. [Umiejętność wroga [854502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
101. [Umiejętność wroga [854503] (ulepszenie 1) — nazwa] 묻어오는 살점
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854503].levelList[level=1].name
   limit: do 40 znaków
   EN: Smeared Flesh
   PL:
102. [Umiejętność wroga [854503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Umiejętność wroga [854503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>을 가지고 있다면, 체력 25 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, heal 25 HP
   PL:
104. [Umiejętność wroga [854503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈 횟수가 2이상일 때 출혈 5 부여.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 2+ Bleed Count, inflict 5 Bleed
   PL:
105. [Umiejętność wroga [854503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>을 가지고 있다면, 체력 25 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [854504] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854504].levelList[level=1].name
   limit: do 40 znaków
   EN: Casting Shade
   PL:
107. [Umiejętność wroga [854504] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 굴절된 클로버 생성.\n[DefeatDuel] 굴절된 클로버의 체력이 50%인 상태로 생성됨.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854504].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Spawn a Refracted Clover next turn.\n[DefeatDuel] The Refracted Clover spawns with 50% HP.
   PL:
108. [Umiejętność wroga [854504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>당 피해량 +5%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +5% damage for every <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> on target
   PL:
109. [Umiejętność wroga [854504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 출혈 전부 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend all of target's Bleed
   PL:
110. [Umiejętność wroga [854505] (ulepszenie 1) — nazwa] 소화
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854505].levelList[level=1].name
   limit: do 40 znaków
   EN: Churning
   PL:
111. [Umiejętność wroga [854505] (ulepszenie 1) — opis] [StartBattle] 모든 부위 보호 3 얻음.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] All parts gain 3 Protection.
   PL:
112. [Umiejętność wroga [854505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>당 자신의 전체 체력의 1%만큼 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 1% of Max HP for every <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> on target
   PL:
113. [Umiejętność wroga [854505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 출혈 횟수 1 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 1 Bleed Count from target
   PL:
114. [Umiejętność wroga [854701] (ulepszenie 1) — nazwa] 취하고 싶나?
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854701].levelList[level=1].name
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Umiejętność wroga [854701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여, 진동 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Umiejętność wroga [854702] (ulepszenie 1) — nazwa] 나눠 마시자!
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854702].levelList[level=1].name
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Umiejętność wroga [854702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Umiejętność wroga [854702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 체력 5% 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność wroga [854703] (ulepszenie 1) — nazwa] 남은건 이것 뿐이네!
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854703].levelList[level=1].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [854703] (ulepszenie 1) — opis] <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>을 가진 대상 우선 공격
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854703].levelList[level=1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Umiejętność wroga [854703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Umiejętność wroga [854703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 진동 횟수만큼 [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Umiejętność wroga [854703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 진동 횟수 전부 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność wroga [854704] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854704].levelList[level=1].name
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [854704] (ulepszenie 1) — opis] 대상에게 <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>가 없다면, 합 위력 +8\n[WhenUse] 대상이 <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>가 없다면, 피해량 +150%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854704].levelList[level=1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [854704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>가 5 이상이라면, 가하는 피해가 0이 됨.\n신사 요정이 다음 턴에 흐트러짐 상태가 됨.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Umiejętność wroga [854704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <sprite name="Tipsiness"><color=#a16a3b><u><link="TipsinessRail">취기</color></link></u>를 전부 소모 시킴.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność wroga [854705] (ulepszenie 1) — nazwa] 이 요정주가 좋나?
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854705].levelList[level=1].name
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Umiejętność wroga [854705] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 속박 3 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854705].levelList[level=1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [854706] (ulepszenie 1) — nazwa] 한 잔 할텐가?
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854706].levelList[level=1].name
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Umiejętność wroga [854706] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 요정주 소환\n[DefeatDuel] 요정주 체력 50%로 소환됨
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Summon Fairy Wine next turn\n[DefeatDuel] Fairy Wine summoned at 50% HP
   PL:
132. [Umiejętność wroga [854706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność wroga [854706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [854801] (ulepszenie 1) — nazwa] 달콤한 요정주
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854801].levelList[level=1].name
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [854801] (ulepszenie 1) — opis] 인격에게 죽었을 때, 모든 인격에게 다음 턴에 취기 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854801].levelList[level=1].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [854901] (ulepszenie 1) — nazwa] 걸려든 미끼
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854901].levelList[level=1].name
   limit: do 40 znaków
   EN: Snagged Lure
   PL:
137. [Umiejętność wroga [854901] (ulepszenie 1) — opis] [CantDuel] 요정이 살아있는 턴만큼 공격 가중치가 증가함.\n<sprite name="FairyCharm"><color=#a16a3b><u><link="FairyCharm">매혹</color></link></u>에 걸린 인격 우선 공격.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="FairyCharm">, <color=#a16a3b>, <u>, <link="FairyCharm">, </color>, </link>, </u>, \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel] +1 Atk Weight for every turn Fairy is alive.\nPrioritizes Identities with <sprite name="FairyCharm"><color=#a16a3b><u><link="FairyCharm">Charmed</color></link></u>.
   PL:
138. [Umiejętność wroga [854901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [854901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [854901] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 본체, 몸통 체력 15 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854901].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core, Body heals 15 HP
   PL:
141. [Umiejętność wroga [854902] (ulepszenie 1) — nazwa] 파고드는 뿌리
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854902].levelList[level=1].name
   limit: do 40 znaków
   EN: Burrowing Roots
   PL:
142. [Umiejętność wroga [854902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [854902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL:
144. [Umiejętność wroga [854903] (ulepszenie 1) — nazwa] 확산하는 뿌리
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854903].levelList[level=1].name
   limit: do 40 znaków
   EN: Expanding Roots
   PL:
145. [Umiejętność wroga [854903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL:
146. [Umiejętność wroga [854903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed
   PL:
147. [Umiejętność wroga [854904] (ulepszenie 1) — nazwa] 잠식하는 줄기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854904].levelList[level=1].name
   limit: do 40 znaków
   EN: Encroaching Stems
   PL:
148. [Umiejętność wroga [854904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 파열 수치당 피해량 +5%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +5% damage for every Rupture on target
   PL:
149. [Umiejętność wroga [854905] (ulepszenie 1) — nazwa] 드러난 심연
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854905].levelList[level=1].name
   limit: do 40 znaków
   EN: Uncovered Abyss
   PL:
150. [Umiejętność wroga [854905] (ulepszenie 1) — opis] 대상에게 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 5이상 있다면 피해량 +100%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: Deal +100% damage to targets with 5+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>
   PL:
151. [Umiejętność wroga [854906] (ulepszenie 1) — nazwa] 매혹된 자아
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854906].levelList[level=1].name
   limit: do 40 znaków
   EN: Charmed Consciousness
   PL:
152. [Umiejętność wroga [854906] (ulepszenie 1) — opis] 요정초롱을 공격할 때 피해가 0이 된다.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854906].levelList[level=1].desc
   limit: do 120 znaków
   EN: Attacking Faelantern deals 0 damage.
   PL:
153. [Umiejętność wroga [855001] (ulepszenie 1) — nazwa] 차원 베기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855001].levelList[level=1].name
   limit: do 40 znaków
   EN: Dimensional Slice
   PL:
154. [Umiejętność wroga [855001] (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 3 증가\n[DefeatDuel] 자신의 충전 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +3 Charge Count\n[DefeatDuel] Spend 2 Charge Count
   PL:
155. [Umiejętność wroga [855001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [855002] (ulepszenie 1) — nazwa] 연속 차원 베기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855002].levelList[level=1].name
   limit: do 50 znaków
   EN: Consecutive Dimensional Slice
   PL:
157. [Umiejętność wroga [855002] (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 3 증가\n[DefeatDuel] 자신의 충전 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855002].levelList[level=1].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność wroga [855002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 차원 균열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Dimensional Rift
   PL:
159. [Umiejętność wroga [855002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 차원 균열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Umiejętność wroga [855003] (ulepszenie 1) — nazwa] 부산물 뱉기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855003].levelList[level=1].name
   limit: do 40 znaków
   EN: Discharge Byproducts
   PL:
161. [Umiejętność wroga [855003] (ulepszenie 1) — opis] [DefeatDuel] 자신의 충전 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Spend 2 Charge Count
   PL:
162. [Umiejętność wroga [855003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Umiejętność wroga [855004] (ulepszenie 1) — nazwa] 공간 절단
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855004].levelList[level=1].name
   limit: do 40 znaków
   EN: Rip Space
   PL:
164. [Umiejętność wroga [855004] (ulepszenie 1) — opis] 충전 횟수가 10 이상이면, 충전 횟수 10을 소모하고 합 위력 +5, 피해량 +100%\n충전 횟수가 10 미만이면, 본체 체력 100을 소모함. 피해량 +80%\n이 스킬로는 체력이 0이 되지 않음.
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855004].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 10+ Charge Count, spend 10 Charge Count and gain Clash Power +5 and deal +100% damage\nAt 10- Charge Count, spend 100 Core HP and deal +80% damage\nThis skill does not reduce the unit's HP to 0.
   PL:
165. [Umiejętność wroga [855004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL:
166. [Umiejętność wroga [855004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 차원 균열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [855004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [855004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 차원 균열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność wroga [855005] (ulepszenie 1) — nazwa] 준비된 반격
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855005].levelList[level=1].name
   limit: do 40 znaków
   EN: Prepared Retribution
   PL:
170. [Umiejętność wroga [855005] (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855005].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +1 Charge Count
   PL:
171. [Umiejętność wroga [855005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [855005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [855006] (ulepszenie 1) — nazwa] 부산물 토하기
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855006].levelList[level=1].name
   limit: do 40 znaków
   EN: Vomit Byproducts
   PL:
174. [Umiejętność wroga [855006] (ulepszenie 1) — opis] [WhenUse] 대상에게 차원 균열이 있다면, 피해량 +10%\n[DefeatDuel] 자신의 충전 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855006].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has Dimensional Rift, deal +10% damage\n[DefeatDuel] Spend 2 Charge Count
   PL:
175. [Umiejętność wroga [855006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 차원 균열 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Dimensional Rift
   PL:
176. [Umiejętność wroga [855007] (ulepszenie 1) — nazwa] 고속 공간 절단
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855007].levelList[level=1].name
   limit: do 40 znaków
   EN: High-speed Rip Space
   PL:
177. [Umiejętność wroga [855007] (ulepszenie 1) — opis] 가장 많이 가지고 있는 차원 효과만큼 합 위력이 증가\n자신이 가지고 있는 차원 효과만큼 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855007].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power equal to the number of Dimensional Rift effect with the highest stack\nDeal +10% damage for every Dimensional Rift effect on self
   PL:
178. [Umiejętność wroga [855007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [855008] (ulepszenie 1) — nazwa] 기회 포착
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855008].levelList[level=1].name
   limit: do 40 znaków
   EN: Opportunity Spotted
   PL:
180. [Umiejętność wroga [855008] (ulepszenie 1) — opis] [WhenUse] 대상에게 차원 균열이 있다면, 피해량 +20%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855008].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has Dimensional Rift, +20% Damage
   PL:
181. [Umiejętność wroga [855008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 차원 균열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [855009] (ulepszenie 1) — nazwa] 틈새 공격
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855009].levelList[level=1].name
   limit: do 40 znaków
   EN: Rift Attack
   PL:
183. [Umiejętność wroga [855009] (ulepszenie 1) — opis] [WhenUse] 대상에게 차원 균열이 있다면, 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855009].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has Dimensional Rift, +10% Damage
   PL:
184. [Umiejętność wroga [855009] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 차원 균열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855009].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [855101] (ulepszenie 1) — nazwa] 맞물리는 순간
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855101].levelList[level=1].name
   limit: do 40 znaków
   EN: Interlocking Moment
   PL:
186. [Umiejętność wroga [855101] (ulepszenie 1) — opis] [DefeatDuel] 자신의 충전 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855101].levelList[level=1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [855101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 맞물리는 시간 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Interlocking Time
   PL:
188. [Umiejętność wroga [855101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 마비 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Paralyze
   PL:
189. [Umiejętność wroga [855102] (ulepszenie 1) — nazwa] 시간 흡수
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855102].levelList[level=1].name
   limit: do 40 znaków
   EN: Siphon Time
   PL:
190. [Umiejętność wroga [855102] (ulepszenie 1) — opis] 충전 횟수가 3당 스킬 위력 +1\n[WhenUse] 자신의 충전 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Skill Power +1 for every 3 Charge Count\n[WhenUse] Gain +4 Charge Count
   PL:
191. [Umiejętność wroga [855102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 시간 대여 3 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 3 Borrowed Time next turn
   PL:
192. [Umiejętność wroga [855102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL:
193. [Umiejętność wroga [855103] (ulepszenie 1) — nazwa] 가속되는 순간
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855103].levelList[level=1].name
   limit: do 40 znaków
   EN: Accelerating Moment
   PL:
194. [Umiejętność wroga [855103] (ulepszenie 1) — opis] <sprite name="TimeRental"><color=#f8c200><u><link="TimeRental">시간 대여</color></link></u>당 스킬 위력 +1\n[DefeatDuel] 자신의 충전 횟수 3 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="TimeRental">, <color=#f8c200>, <u>, <link="TimeRental">, </color>, </link>, </u>, \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Skill Power +1 for every <sprite name="TimeRental"><color=#f8c200><u><link="TimeRental">Borrowed Time</color></link></u>\n[DefeatDuel] Spend 3 Charge Count
   PL:
195. [Umiejętność wroga [855103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 맞물리는 시간 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Interlocking Time
   PL:
196. [Umiejętność wroga [855103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [855103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] <sprite name="TimeRental"><color=#f8c200><u><link="TimeRental">시간 대여</color></link></u>당 피해량 +20%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="TimeRental">, <color=#f8c200>, <u>, <link="TimeRental">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +20% damage for every <sprite name="TimeRental"><color=#f8c200><u><link="TimeRental">Borrowed Time</color></link></u>
   PL:
198. [Umiejętność wroga [855103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +4 Charge Count
   PL:
199. [Umiejętność wroga [855104] (ulepszenie 1) — nazwa] 충전 방어
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855104].levelList[level=1].name
   limit: do 40 znaków
   EN: Charged Defense
   PL:
200. [Umiejętność wroga [855104] (ulepszenie 1) — opis] [StartBattle] 자신의 충전 횟수 1 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain +1 Charge Count
   PL:
201. [Umiejętność wroga [855501] (ulepszenie 1) — nazwa] 6463
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855501].levelList[level=1].name
   limit: do 40 znaków
   EN: 6463
   PL:
202. [Umiejętność wroga [855501] (ulepszenie 1) — opis] <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">축적된 과거</color></link></u> 50당 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPast">, </color>, </link>, </u>
   EN: Deal +10% damage for every 50 <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">Accumulated Past</color></link></u>
   PL:
203. [Umiejętność wroga [855501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [855502] (ulepszenie 1) — nazwa] 6753
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855502].levelList[level=1].name
   limit: do 40 znaków
   EN: 6753
   PL:
205. [Umiejętność wroga [855502] (ulepszenie 1) — opis] <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">축적된 과거</color></link></u> 50당 피해량 +10%
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855502].levelList[level=1].desc
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [855502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL:
207. [Umiejętność wroga [855503] (ulepszenie 1) — nazwa] 853
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855503].levelList[level=1].name
   limit: do 40 znaków
   EN: 853
   PL:
208. [Umiejętność wroga [855503] (ulepszenie 1) — opis] [Breath]이 5이상이면, 합 위력 +1
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 5+ [Breath], Clash Power +1
   PL:
209. [Umiejętność wroga [855503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [855503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 50% of damage dealt
   PL:
211. [Umiejętność wroga [855503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">축적된 과거</color></link></u>당 피해량 +1% (최대 50%)
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPast">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +1% damage for every <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">Accumulated Past</color></link></u> (Max 50%)
   PL:
212. [Umiejętność wroga [855504] (ulepszenie 1) — nazwa] 5384
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855504].levelList[level=1].name
   limit: do 40 znaków
   EN: 5384
   PL:
213. [Umiejętność wroga [855504] (ulepszenie 1) — opis] [WhenUse] 모든 부위에 [Breath] 3, [Breath] 횟수 3을 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] All parts gain 3 [Breath] and +3 [Breath] Count
   PL:
214. [Umiejętność wroga [855504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath]만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Raise Stagger Threshold equal to [Breath]
   PL:
215. [Umiejętność wroga [855504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3당 피해량 +20% (최대 100%)
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Deal +20% damage per 3 [Breath] (Max 100%)
   PL:
216. [Umiejętność wroga [855504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 모든 부위에 [Breath] 4를 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath] to all Parts
   PL:
217. [Umiejętność wroga [855505] (ulepszenie 1) — nazwa] 6475384
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855505].levelList[level=1].name
   limit: do 40 znaków
   EN: 6475384
   PL:
218. [Umiejętność wroga [855505] (ulepszenie 1) — opis] [Breath]이 7이상이면, 코인 위력 +1
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 7+ [Breath], Coin Power +1
   PL:
219. [Umiejętność wroga [855505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath]이 5이상이면, 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] At 5+ [Breath], raise Stagger Threshold by 50% of damage dealt
   PL:
220. [Umiejętność wroga [855505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 모든 부위에 [Breath] 8, [Breath] 횟수 4를 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] All Parts gain 8 [Breath] and +4 [Breath] Count
   PL:
221. [Umiejętność wroga [855506] (ulepszenie 1) — nazwa] 974569A
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855506].levelList[level=1].name
   limit: do 40 znaków
   EN: 974569A
   PL:
222. [Umiejętność wroga [855506] (ulepszenie 1) — opis] [Breath]이 10이상이면, 스킬 위력 +2
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 10+ [Breath], Skill Power +2
   PL:
223. [Umiejętność wroga [855506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">축적된 과거</color></link></u>당 피해량 +1% (최대 200%)
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPast">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +1% damage for every <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">Accumulated Past</color></link></u> (Max 200%)
   PL:
224. [Umiejętność wroga [855601] (ulepszenie 1) — nazwa] 영겁의 정원으로
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855601].levelList[level=1].name
   limit: do 40 znaków
   EN: To the Garden of Infinity
   PL:
225. [Umiejętność wroga [855601] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 면류관 부여. 자신에게 부여된 모든 효과 제거\n자신의 본체 체력이 40% 미만이면 다음 턴에 장미 유닛이 강화 상태 로 생성됨
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855601].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\n[WhenUse] Apply Crown of Thorns and eliminate all effects on self\nIf Core has less than 40% HP, Roses will spawn in Power-up States next turn
   PL:
226. [Umiejętność wroga [855602] (ulepszenie 1) — nazwa] 정지
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855602].levelList[level=1].name
   limit: do 40 znaków
   EN: Stop
   PL:
227. [Umiejętność wroga [855602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 2, 진동 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn and 2 Tremor
   PL:
228. [Umiejętność wroga [855602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL:
229. [Umiejętność wroga [855602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 2, 진동 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [855602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [855603] (ulepszenie 1) — nazwa] 구속
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855603].levelList[level=1].name
   limit: do 40 znaków
   EN: Captivity
   PL:
232. [Umiejętność wroga [855603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [855603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3, 파열 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed and 3 Rupture
   PL:
234. [Umiejętność wroga [855603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 체력이 가장 낮은 장미 유닛의 체력 10 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal the Rose with the lowest HP percentages for 10 HP
   PL:
235. [Umiejętność wroga [855604] (ulepszenie 1) — nazwa] 끝없는 피어남
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855604].levelList[level=1].name
   limit: do 40 znaków
   EN: Endless Blooming
   PL:
236. [Umiejętność wroga [855604] (ulepszenie 1) — opis] 면류관이 없는 대상 우선 공격
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855604].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes enemies without Crown of Thorns
   PL:
237. [Umiejętność wroga [855604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1, 속박 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze and 1 Bind next turn
   PL:
238. [Umiejętność wroga [855604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 면류관 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply Crown of Thorns
   PL:
239. [Umiejętność wroga [855604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 30 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core heals 30 HP
   PL:
240. [Umiejętność wroga [855605] (ulepszenie 1) — nazwa] 단절의 벽
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855605].levelList[level=1].name
   limit: do 40 znaków
   EN: Wall Of Separation
   PL:
241. [Umiejętność wroga [855605] (ulepszenie 1) — opis] 생존한 장미 유닛 당 위력 +2\n생존한 장미가 없으면 다음 턴에 취약 2를 얻음
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Power +2 for each surviving Rose\nIf there are no surviving Roses, gain 2 Fragile next turn
   PL:
242. [Umiejętność wroga [855605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 30 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [855606] (ulepszenie 1) — nazwa] 영원을 바라며
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855606].levelList[level=1].name
   limit: do 40 znaków
   EN: Wishing for Eternity
   PL:
244. [Umiejętność wroga [855606] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 무작위 장미 1개에게 공격 위력 증가 1 부여\n보호막이 있는동안 피격 시 공격자에게 침잠 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855606].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Attack Power Up to 1 random Rose next turn\nIf attacked while Shielded, inflict 1 Sinking on the attacker
   PL:
245. [Umiejętność wroga [855607] (ulepszenie 1) — nazwa] 함께 이 곳에서
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855607].levelList[level=1].name
   limit: do 40 znaków
   EN: Here, With You
   PL:
246. [Umiejętność wroga [855607] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 무작위 장미 1개에게 수비 위력 증가 1 부여\n보호막이 있는동안 피격 시 공격자에게 침잠 1 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=855607].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Defense Power Up to 1 random Rose next turn\nIf attacked while Shielded, inflict 1 Sinking on the attacker
   PL:
247. [Umiejętność wroga [856401] (ulepszenie 1) — nazwa] 타오르는 분노
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856401].levelList[level=1].name
   limit: do 40 znaków
   EN: Burning Wrath
   PL:
248. [Umiejętność wroga [856401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn
   PL:
249. [Umiejętność wroga [856401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [856401] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856401].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [856402] (ulepszenie 1) — nazwa] 흩날리는 분노
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856402].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Wrath
   PL:
252. [Umiejętność wroga [856402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Burn Count
   PL:
253. [Umiejętność wroga [856402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [856501] (ulepszenie 1) — nazwa] 다가오는 색욕
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].name
   limit: do 40 znaków
   EN: Approaching Lust
   PL:
255. [Umiejętność wroga [856501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
256. [Umiejętność wroga [856501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user’s Stagger Threshold by 50% of damage dealt
   PL:
257. [Umiejętność wroga [856501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [856501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [856501] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność wroga [856501] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856501].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [856502] (ulepszenie 1) — nazwa] 파고드는 색욕
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856502].levelList[level=1].name
   limit: do 40 znaków
   EN: Burrowing Lust
   PL:
262. [Umiejętność wroga [856502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed Count
   PL:
263. [Umiejętność wroga [856502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [856502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność wroga [856601] (ulepszenie 1) — nazwa] 굳어진 나태
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856601].levelList[level=1].name
   limit: do 40 znaków
   EN: Petrified Sloth
   PL:
266. [Umiejętność wroga [856601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 8 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 8 Tremor
   PL:
267. [Umiejętność wroga [856602] (ulepszenie 1) — nazwa] 완고한 나태
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856602].levelList[level=1].name
   limit: do 40 znaków
   EN: Stubborn Sloth
   PL:
268. [Umiejętność wroga [856602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 8 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [856602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Trigger Tremor Burst
   PL:
270. [Umiejętność wroga [856603] (ulepszenie 1) — nazwa] 잠든 나태
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856603].levelList[level=1].name
   limit: do 40 znaków
   EN: Slumbering Sloth
   PL:
271. [Umiejętność wroga [856603] (ulepszenie 1) — opis] 보호막이 있는동안 피격 시 자신과 대상에게 진동 폭발
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856603].levelList[level=1].desc
   limit: do 120 znaków
   EN: If attacked while Shielded, trigger Tremor Burst on self and the attacker
   PL:
272. [Umiejętność wroga [856701] (ulepszenie 1) — nazwa] 게걸스런 탐식
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856701].levelList[level=1].name
   limit: do 40 znaków
   EN: Voracious Gluttony
   PL:
273. [Umiejętność wroga [856701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność wroga [856702] (ulepszenie 1) — nazwa] 무성한 탐식
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856702].levelList[level=1].name
   limit: do 40 znaków
   EN: Prevalent Gluttony
   PL:
275. [Umiejętność wroga [856702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +4 Rupture Count
   PL:
276. [Umiejętność wroga [856703] (ulepszenie 1) — nazwa] 쉼 없는 탐식
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856703].levelList[level=1].name
   limit: do 40 znaków
   EN: Restless Gluttony
   PL:
277. [Umiejętność wroga [856703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 25% of damage dealt
   PL:
278. [Umiejętność wroga [856703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [856703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [856703] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856703].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [856801] (ulepszenie 1) — nazwa] 넘치는 우울
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856801].levelList[level=1].name
   limit: do 40 znaków
   EN: Overflowing Gloom
   PL:
282. [Umiejętność wroga [856801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Sinking
   PL:
283. [Umiejętność wroga [856802] (ulepszenie 1) — nazwa] 차오르는 우울
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856802].levelList[level=1].name
   limit: do 40 znaków
   EN: Rising Gloom
   PL:
284. [Umiejętność wroga [856802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Sinking Count
   PL:
285. [Umiejętność wroga [856802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność wroga [856803] (ulepszenie 1) — nazwa] 감싼 우울
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856803].levelList[level=1].name
   limit: do 40 znaków
   EN: Embracing Gloom
   PL:
287. [Umiejętność wroga [856803] (ulepszenie 1) — opis] 보호막이 있는동안 피격 시 자신과 대상에게 침잠 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856803].levelList[level=1].desc
   limit: do 120 znaków
   EN: If attacked while Shielded, inflict +1 Sinking Count on self and the attacker
   PL:
288. [Umiejętność wroga [856901] (ulepszenie 1) — nazwa] 내뱉은 오만
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856901].levelList[level=1].name
   limit: do 40 znaków
   EN: Spouting Pride
   PL:
289. [Umiejętność wroga [856901] (ulepszenie 1) — opis] [WhenUse] 모든 아군에게 호흡 3 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 3 Poise to all allies
   PL:
290. [Umiejętność wroga [856902] (ulepszenie 1) — nazwa] 치켜든 오만
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856902].levelList[level=1].name
   limit: do 40 znaków
   EN: Erect Pride
   PL:
291. [Umiejętność wroga [856902] (ulepszenie 1) — opis] [WhenUse] 모든 아군의 호흡 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] All allies gain +2 Poise Count
   PL:
292. [Umiejętność wroga [856902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Poise Count
   PL:
293. [Umiejętność wroga [856902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [856903] (ulepszenie 1) — nazwa] 날 선 오만
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856903].levelList[level=1].name
   limit: do 40 znaków
   EN: Touchy Pride
   PL:
295. [Umiejętność wroga [857001] (ulepszenie 1) — nazwa] 쌓이는 질투
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=857001].levelList[level=1].name
   limit: do 40 znaków
   EN: Heaping Envy
   PL:
296. [Umiejętność wroga [857001] (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 3 증가\n[DefeatDuel] 자신의 충전 횟수 3 소모
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=857001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +3 Charge Count\n[DefeatDuel] Spend 3 Charge Count
   PL:
297. [Umiejętność wroga [857001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=857001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Charge Count
   PL:
298. [Umiejętność wroga [857001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=857001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [857002] (ulepszenie 1) — nazwa] 뻗어가는 질투
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=857002].levelList[level=1].name
   limit: do 40 znaków
   EN: Spreading Envy
   PL:
300. [Umiejętność wroga [857002] (ulepszenie 1) — opis] [WhenUse] 충전 횟수를 10 소모하여 코인 위력 +4
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=857002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Spend 10 Charge to gain +4 Coin Power
   PL:
301. [Umiejętność wroga [856001] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856001].levelList[level=1].name
   limit: do 40 znaków
   EN: Dimensional Leap
   PL:
302. [Umiejętność wroga [856001] (ulepszenie 1) — opis] 이 차원이 남아있다면, 피해량이 10% 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856001].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, deal +10% damage
   PL:
303. [Umiejętność wroga [856101] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856101].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [856101] (ulepszenie 1) — opis] 이 차원이 남아있다면, 최대 체력이 20% 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856101].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, max HP +20%
   PL:
305. [Umiejętność wroga [856201] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856201].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [856201] (ulepszenie 1) — opis] 이 차원이 남아있다면, 속도 1 증가
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856201].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, gain 1 Speed
   PL:
307. [Umiejętność wroga [856301] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856301].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [856301] (ulepszenie 1) — opis] 이 차원이 남아있다면, 코인 위력 +1
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=856301].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, Coin Power +1
   PL:
309. [Umiejętność wroga [854406] (ulepszenie 1) — nazwa] 누구도 울지 않도록
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].name
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [854406] (ulepszenie 1) — opis] [EndBattle] 다시 붙여진 저주 부적 전부 소멸\n[WhenUse] 가지고 있는 <sprite name="ReattachedCurseTag"><color=#a16a3b><u><link="ReattachedCurseTag">다시 붙여진 저주 부적</color></link></u>이 10개 이상이면, 코인 위력 -1
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [854406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Umiejętność wroga [854406] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność wroga [854406] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność wroga [854406] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność wroga [854406] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [854406] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 5 부여
   źródło: Skills_Abnormality_Refraction2.json :: dataList[id=854406].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction2] Pasywka wroga: Passives_Abnormality_Refraction2
- plik gry: `Passives_Abnormality_Refraction2.json`

317. [[refraction2] Pasywka wroga [853901] — nazwa] 부서진 우산
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853901].name
   limit: do 40 znaków
   EN: Broken Umbrella
   PL:
318. [[refraction2] Pasywka wroga [853901] — opis] 몸통 부위 파괴 시, 매 턴마다 몸통 부위 피해량 감소 1 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853901].desc
   limit: do 120 znaków
   EN: When the Body is broken, the Body gains 1 Damage Down every turn
   PL:
319. [[refraction2] Pasywka wroga [853902] — nazwa] 다해진 우산
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853902].name
   limit: do 40 znaków
   EN: Ragged Umbrella
   PL:
320. [[refraction2] Pasywka wroga [853902] — opis] 머리 부위 파괴 시, 매 턴마다 피해량 감소 1 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853902].desc
   limit: do 120 znaków
   EN: When the Head is broken, gain 1 Damage Down every turn
   PL:
321. [[refraction2] Pasywka wroga [853903] — nazwa] 마지막 발버둥
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853903].name
   limit: do 40 znaków
   EN: Last Struggle
   PL:
322. [[refraction2] Pasywka wroga [853903] — opis] 체력이 전체 체력의 15%만큼 남았다면, 매 턴마다 속박 10, 공격 위력 감소 1 얻음\n새로 소환된 낡은 우산 체력 30% 증가. 매 턴마다 무언가를 찾는 울음소리 사용
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853903].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 15% HP, this unit gains 10 Bind and 1 Attack Power Down every turn\nNewly spawned Old Umbrellas have 30% more HP. Uses 'Cries Seeking Something' every turn.
   PL:
323. [[refraction2] Pasywka wroga [853904] — nazwa] 허영된 마음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853904].name
   limit: do 40 znaków
   EN: Vain Heart
   PL:
324. [[refraction2] Pasywka wroga [853904] — opis] 1턴 시작 시 <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">보호 우산</color></link></u>을 2 얻음. (최대 6)\n<sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">보호 우산</color></link></u>을 얻을 때 "순환 횟수"만큼 추가로 얻음.\n보유중인 <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">보호 우산</color></link></u>만큼 <sprite name="Protection"><color=#f8c200><u><link="Protection">보호</color></link></u>를 얻음\n기다림 스킬이 슬롯에 있다면, 낡은 우산을 <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">보호 우산</color></link></u>만큼 소환
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853904].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <sprite name="WaveFoxUmbrella">, <color=#f8c200>, <u>, <link="WaveFoxUmbrella">, </color>, </link>, </u>, <sprite name="Protection">, <link="Protection">, \n
   EN: Gain 2 <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">Protection Umbrella</color></link></u> at the start of Turn 1 (max 6)\nGain additional <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">Protection Umbrella</color></link></u> equal to the number of "Cycle Counts"\nGain <sprite name="Protection"><color=#f8c200><u><link="Protection">Protection</color></link></u> equal to <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">Protection Umbrella</color></link></u>\nIf "Waiting Skill" is slotted, summon Old Umbrella equal to <sprite name="WaveFoxUmbrella"><color=#f8c200><u><link="WaveFoxUmbrella">Protection Umbrella</color></link></u>
   PL:
325. [[refraction2] Pasywka wroga [853905] — nazwa] 굴절된 파열과 침잠
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853905].name
   limit: do 50 znaków
   EN: Refracted Rupture and Sinking
   PL:
326. [[refraction2] Pasywka wroga [853905] — opis] <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>과 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>과 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853905].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, <sprite name="Sinking">, <link="Sinking">, \n
   EN: <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> and <sprite name="Sinking"><color=#e30000><u><link="Sinking">Sinking</color></link></u> Potency maxes out at 30.\n<sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> and <sprite name="Sinking"><color=#e30000><u><link="Sinking">Sinking</color></link></u> Count maxes out at 5.
   PL:
327. [[refraction2] Pasywka wroga [853906] — nazwa] 굴절 출혈 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853906].name
   limit: do 40 znaków
   EN: Apply Refracted Bleed
   PL:
328. [[refraction2] Pasywka wroga [853906] — opis] <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=853906].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, [TabExplain]
   EN: When gaining <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
329. [[refraction2] Pasywka wroga [854001] — nazwa] 버려진 낡은 우산
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854001].name
   limit: do 40 znaków
   EN: Old and Abandoned
   PL:
330. [[refraction2] Pasywka wroga [854001] — opis] 이 유닛이 인격에 의해 처치되면 다음 턴에 처치한 캐릭터 신속 2 얻음.\n떠돌이 여우 모든 부위에 속박 2 부여.\n떠돌이 여우에게 우산 파편 1 부여.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854001].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When this unit is defeated, the unit that defeated it gains 2 Haste next turn.\nAll Drifting Fox parts are inflicted with 2 Bind.\nApply 1 Umbrella Splinters to Drifting Fox.
   PL:
331. [[refraction2] Pasywka wroga [854101] — nazwa] 쇠퇴한 생명력
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854101].name
   limit: do 40 znaków
   EN: Deteriorated Persistence
   PL:
332. [[refraction2] Pasywka wroga [854101] — opis] 방어 스킬 사용 후 보호막 체력이 전부 소모되었다면, 다음 턴에 공격 레벨 감소 3, 취약 3을 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854101].desc
   limit: do 150 znaków
   EN: If Shield HP is fully depleted after using a Defense Skill, gain 3 Offense Level Down and 3 Fragile next turn
   PL:
333. [[refraction2] Pasywka wroga [854102] — nazwa] 단단한 갑각
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854102].name
   limit: do 40 znaków
   EN: Solid Exoskeleton
   PL:
334. [[refraction2] Pasywka wroga [854102] — opis] 머리가 부위 파괴 상태가 아니라면\n매 턴마다 몸통이 보호 3을 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If Head is not broken, the Body gains 3 Protection every turn
   PL:
335. [[refraction2] Pasywka wroga [854104] — nazwa] 굴절된 충전
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854104].name
   limit: do 40 znaków
   EN: Refracted Charge
   PL:
336. [[refraction2] Pasywka wroga [854104] — opis] 대상에게 충전이 있다면, 공격 적중 시 대상의 충전 횟수를 1 감소시키고 자가 충전 1을 얻음. (턴 당 3번)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854104].desc
   limit: do 140 znaków
   EN: On Hit: If target has Charge, reduce target's Charge Count by 1 and gain 1 Self-charge (3 times per turn)
   PL:
337. [[refraction2] Pasywka wroga [854103] — nazwa] 굴절된 출혈과 진동
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854103].name
   limit: do 40 znaków
   EN: Refracted Bleed and Tremor
   PL:
338. [[refraction2] Pasywka wroga [854103] — opis] <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, <sprite name="Vibration">, <link="Vibration">, \n
   EN: <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> and <sprite name="Vibration"><color=#e30000><u><link="Vibration">Tremor</color></link></u> Potency maxes out at 30.\n<sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> and <sprite name="Vibration"><color=#e30000><u><link="Vibration">Tremor</color></link></u> Count maxes out at 5.
   PL:
339. [[refraction2] Pasywka wroga [854105] — nazwa] 자가 충전
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854105].name
   limit: do 40 znaków
   EN: Self-charge
   PL:
340. [[refraction2] Pasywka wroga [854105] — opis] 1턴 시작 시, 자가 충전 3을 얻음\n순환 횟수가 늘어날수록 얻는 자가 충전이 1씩 증가함. (최대 8)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854105].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 3 Self-charge at the start of Turn 1\nGain 1 additional Self-charge for each Cycle Count (max 8)
   PL:
341. [[refraction2] Pasywka wroga [854201] — nazwa] 세포 분열
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854201].name
   limit: do 40 znaków
   EN: Mitosis
   PL:
342. [[refraction2] Pasywka wroga [854201] — opis] 팔 부위 파괴 시, 모든 부위 매 턴마다 공격 위력 감소 1 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854201].desc
   limit: do 120 znaków
   EN: When the arm is broken, all parts gain 1 Attack Power Down every turn.
   PL:
343. [[refraction2] Pasywka wroga [854202] — nazwa] 눈독 들인 요정주
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854202].name
   limit: do 40 znaków
   EN: Enticing Fairy Wine
   PL:
344. [[refraction2] Pasywka wroga [854202] — opis] 요정주가 있을 때, 모든 부위 <sprite name="Binding"><color=#e30000><u><link="Binding">속박</color></link></u>을 5 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854202].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Binding">, <color=#e30000>, <u>, <link="Binding">, </color>, </link>, </u>
   EN: When Fairy Wine is on the field, all Parts gain 5 <sprite name="Binding"><color=#e30000><u><link="Binding">Bind</color></link></u>
   PL:
345. [[refraction2] Pasywka wroga [854203] — nazwa] 굴절된 출혈과 진동
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854203].name
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [[refraction2] Pasywka wroga [854203] — opis] <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854203].desc
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [[refraction2] Pasywka wroga [854204] — nazwa] 굴절 파열 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854204].name
   limit: do 40 znaków
   EN: Apply Refracted Rupture
   PL:
348. [[refraction2] Pasywka wroga [854204] — opis] <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854204].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, [TabExplain]
   EN: When gaining <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
349. [[refraction2] Pasywka wroga [854301] — nazwa] 요정주
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854301].name
   limit: do 40 znaków
   EN: Fairy Wine
   PL:
350. [[refraction2] Pasywka wroga [854301] — opis] 인격에게 죽었을 때, 모든 인격에게 다음 턴에 취기 5를 부여.\n죽지 않았을 때, 신사 요정에게 다음 턴에 체력 10% 회복, 공격 위력 증가 2, 신속 2, 보호 2를 부여함.\n턴 종료 시 소멸
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854301].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When defeated by an Identity, inflict 5 Tipsy on all Identities next turn\nIf not defeated, Fairy Gentleman heals 10% HP and gains 2 Attack Power Up, 2 Haste, and 2 Protection next turn\nExpires at Turn End
   PL:
351. [[refraction2] Pasywka wroga [854401] — nazwa] 부서진 수단
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854401].name
   limit: do 40 znaków
   EN: Broken Means
   PL:
352. [[refraction2] Pasywka wroga [854401] — opis] 팔 부위 파괴 시, 매 턴마다 팔 부위에 공격 위력 감소 1 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854401].desc
   limit: do 120 znaków
   EN: When the Arm is broken, the Arm gains 1 Attack Power Down every turn
   PL:
353. [[refraction2] Pasywka wroga [854402] — nazwa] 굴절 침잠 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854402].name
   limit: do 40 znaków
   EN: Apply Refracted Sinking
   PL:
354. [[refraction2] Pasywka wroga [854402] — opis] <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854402].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <sprite name="Sinking">, <color=#e30000>, <u>, <link="Sinking">, </color>, </link>, </u>, [TabExplain]
   EN: When gaining <sprite name="Sinking"><color=#e30000><u><link="Sinking">Sinking</color></link></u>, gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
355. [[refraction2] Pasywka wroga [854501] — nazwa] 잃어버린 수단
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854501].name
   limit: do 40 znaków
   EN: Lost Means
   PL:
356. [[refraction2] Pasywka wroga [854501] — opis] 팔 부위 파괴 시, 매 턴마다 공격 위력 감소 1 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854501].desc
   limit: do 120 znaków
   EN: When the arm is broken, the unit gains 1 Attack Power Down every turn.
   PL:
357. [[refraction2] Pasywka wroga [854502] — nazwa] 훼손된 그늘
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854502].name
   limit: do 40 znaków
   EN: Damaged Shade
   PL:
358. [[refraction2] Pasywka wroga [854502] — opis] 머리 부위 파괴 시, 매 턴마다 방어 레벨 감소 2 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854502].desc
   limit: do 120 znaków
   EN: When the head is broken, the unit gains 2 Defense Level Down every turn.
   PL:
359. [[refraction2] Pasywka wroga [854503] — nazwa] 굴절된 출혈과 진동
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854503].name
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [[refraction2] Pasywka wroga [854503] — opis] <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854503].desc
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [[refraction2] Pasywka wroga [854504] — nazwa] 굴절 파열 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854504].name
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [[refraction2] Pasywka wroga [854504] — opis] <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854504].desc
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [[refraction2] Pasywka wroga [854601] — nazwa] 오염시키는 잎사귀
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854601].name
   limit: do 40 znaków
   EN: Contaminating Leaf
   PL:
364. [[refraction2] Pasywka wroga [854601] — opis] 매 턴 시작 시 키다리 요정과 신사 요정이 체력 회복 증가 3, 공격 위력 증가 1을 얻음.\n4턴 이상 클로버가 생존해 있다면, 추가로 공격 위력 증가 1, 피해량 증가 2를 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854601].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply the following effects on Fairy-Long-Legs and Fairy Gentleman:\n- Turn Start: Gain 3 HP Healing Boost and 1 Attack Power Up\n- If the Clover survives for 4+ Turns, gain an additional 1 Attack Power Up and 2 Damage Up
   PL:
365. [[refraction2] Pasywka wroga [854701] — nazwa] 세포 분열
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854701].name
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [[refraction2] Pasywka wroga [854701] — opis] 팔 부위 파괴 시, 매 턴마다 공격 위력 감소 1 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854701].desc
   limit: do 120 znaków
   EN: When the arm is broken, the unit gains 1 Attack Power Down every turn.
   PL:
367. [[refraction2] Pasywka wroga [854702] — nazwa] 눈독 들인 요정주
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854702].name
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [[refraction2] Pasywka wroga [854702] — opis] 요정주가 있을 때, <sprite name="Binding"><color=#e30000><u><link="Binding">속박</color></link></u>을 5 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854702].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Binding">, <color=#e30000>, <u>, <link="Binding">, </color>, </link>, </u>
   EN: When Fairy Wine is on the field, all Parts gain 5 <sprite name="Binding"><color=#e30000><u><link="Binding">Bind</color></link></u>
   PL:
369. [[refraction2] Pasywka wroga [854703] — nazwa] 굴절된 출혈과 진동
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854703].name
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [[refraction2] Pasywka wroga [854703] — opis] <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>과 <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854703].desc
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [[refraction2] Pasywka wroga [854704] — nazwa] 굴절 파열 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854704].name
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [[refraction2] Pasywka wroga [854704] — opis] <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854704].desc
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [[refraction2] Pasywka wroga [854801] — nazwa] 요정주
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854801].name
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [[refraction2] Pasywka wroga [854801] — opis] 인격에게 죽었을 때, 모든 인격에게 다음 턴에 취기 5를 부여.\n죽지 않았을 때, 신사 요정에게 다음 턴에 체력 10% 회복, 공격 위력 증가 2, 신속 2, 보호 2를 부여함.\n턴 종료 시 소멸
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854801].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [[refraction2] Pasywka wroga [854901] — nazwa] 매혹
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854901].name
   limit: do 40 znaków
   EN: Charmed
   PL:
376. [[refraction2] Pasywka wroga [854901] — opis] 속도가 가장 낮은 적에게 매혹 부여.\n순환 횟수에 따라 매혹 인원 증가.\n요정 부위 재생 시 매혹 인원 증가.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854901].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict Charmed to the enemy with the slowest Speed\nNumber of targets increases with every Cycle Count\nNumber of targets increases when Fairy is restored
   PL:
377. [[refraction2] Pasywka wroga [854902] — nazwa] 드러난 심연
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854902].name
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [[refraction2] Pasywka wroga [854902] — opis] 요정 부위 파괴 시, 몸통이 드러남.\n몸통이 다시 숨을 때, 가지고 있는 버프 및 디버프 전부 삭제.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854902].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reveal Body when Fairy is broken\nAll Buffs and Debuffs expire when the Body hides again
   PL:
379. [[refraction2] Pasywka wroga [854903] — nazwa] 앞선 미끼
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854903].name
   limit: do 40 znaków
   EN: Leading Lure
   PL:
380. [[refraction2] Pasywka wroga [854903] — opis] 요정 부위를 공격 당해도 본체 체력이 소모되지 않음.\n<sprite name="FairyCharm"><color=#a16a3b><u><link="FairyCharm">매혹</color></link></u>된 인원 수에 따라 공격 슬롯이 증가함.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854903].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <sprite name="FairyCharm">, <color=#a16a3b>, <u>, <link="FairyCharm">, </color>, </link>, </u>, \n
   EN: Cannot damage Core by damaging the Fairy.\nTargets more slots based on the number of <sprite name="FairyCharm"><color=#a16a3b><u><link="FairyCharm">Charmed</color></link></u> units.
   PL:
381. [[refraction2] Pasywka wroga [854904] — nazwa] 파괴된 밑동
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854904].name
   limit: do 40 znaków
   EN: Broken Stump
   PL:
382. [[refraction2] Pasywka wroga [854904] — opis] 몸통 부위가 파괴되면, 요정 재생 시 체력이 60%로 재생함.\n몸통 부위가 파괴되면, 스킬에 의한 본체 체력 회복 +20
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854904].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Body is broken:\n- Fairy will have 60% of its max HP upon restoration\n- Core heals +20 more HP from Skill effects
   PL:
383. [[refraction2] Pasywka wroga [854905] — nazwa] 진화하는 미끼
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854905].name
   limit: do 40 znaków
   EN: Evolving Lure
   PL:
384. [[refraction2] Pasywka wroga [854905] — opis] 요정 부위 재생 시 최대 체력이 20% 증가.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854905].desc
   limit: do 120 znaków
   EN: Fairy gains 20% increased Max HP when restored.
   PL:
385. [[refraction2] Pasywka wroga [854906] — nazwa] 굴절된 파열과 침잠
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854906].name
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [[refraction2] Pasywka wroga [854906] — opis] <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>과 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>과 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854906].desc
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [[refraction2] Pasywka wroga [854907] — nazwa] 요정 가루
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854907].name
   limit: do 40 znaków
   EN: Fairy Dust
   PL:
388. [[refraction2] Pasywka wroga [854907] — opis] 요정이 죽었을 때, 모든 인격이 다음 턴에 호흡 5, 호흡 횟수 2 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854907].desc
   limit: do 120 znaków
   EN: When the Fairy is killed, all Identities gain 5 Poise and 2 Poise Count next turn
   PL:
389. [[refraction2] Pasywka wroga [855001] — nazwa] 차원 도주
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855001].name
   limit: do 40 znaków
   EN: Dimensional Escape
   PL:
390. [[refraction2] Pasywka wroga [855001] — opis] 2턴부터 일정 턴마다 차원으로 숨음.\n모든 부위가 흐트러짐 상태이면, 다음 턴에 숨음.\n차원으로 숨었을 때에는, 흐트러짐 상태가 되지 않음.\n본체 체력이 최대 체력의 30% 이하면, 차원으로 숨지 않음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855001].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting from turn 2, escape to a 'Dimensional Rift' every few turns.\nWhen all parts are Staggered, escape to a 'Dimensional Rift' next turn.\nCannot be Staggered while inside a 'Dimensional Rift'.\nWhen Core is at 30% or less HP, does not escape to a 'Dimensional Rift'.
   PL:
391. [[refraction2] Pasywka wroga [855002] — nazwa] 갇혀버린 차원 탈출
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855002].name
   limit: do 40 znaków
   EN: Trapped Dimensional Escape
   PL:
392. [[refraction2] Pasywka wroga [855002] — opis] 모든 차원이 생성된 턴에 파괴되면, 다음 턴에 스스로 차원을 찢고 나옴.\n이후 충전 횟수 5를 잃고, 모든 부위가 흐트러짐 손상 30을 입음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855002].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When all 'Dimensional Rifts' are broken on the same turn they are created, voluntarily emerge from a 'Dimensional Rift' next turn.\nAfterward, lose 5 Charge Count and raise Stagger Threshold by 30 on all parts.
   PL:
393. [[refraction2] Pasywka wroga [855003] — nazwa] 차원 굴절 칼날 수복
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855003].name
   limit: do 60 znaków
   EN: Regenerate Dimensional Refraction Blade
   PL:
394. [[refraction2] Pasywka wroga [855003] — opis] 칼날 부위가 파괴되면, 충전 횟수 5를 잃고,\n다음 턴 종료 시 충전 횟수 2를 소모하여 칼날 부위를 회복함.\n칼날 부위가 파괴된 상태면, 매 턴 시작 시 공격 레벨 감소 2를 얻음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855003].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the blade part is broken, lose 5 Charge Count,\nand at the end of the next turn, recover blade part by spending 2 Charge Count.\nWhen the blade part is broken, gain 2 Offense Level Down at the start of every turn.
   PL:
395. [[refraction2] Pasywka wroga [855004] — nazwa] 굴절된 화상과 파열
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855004].name
   limit: do 40 znaków
   EN: Refracted Burn and Rupture
   PL:
396. [[refraction2] Pasywka wroga [855004] — opis] <sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>과 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>과 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855004].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Combustion">, <color=#e30000>, <u>, <link="Combustion">, </color>, </link>, </u>, <sprite name="Burst">, <link="Burst">, \n
   EN: <sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u> and <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> Potency maxes out at 30.\n<sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u> and <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> Count maxes out at 5.
   PL:
397. [[refraction2] Pasywka wroga [855005] — nazwa] 굴절 진동 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855005].name
   limit: do 40 znaków
   EN: Apply Refracted Tremor
   PL:
398. [[refraction2] Pasywka wroga [855005] — opis] <sprite name="Vibration"><color=#e30000><u><link="Vibration">진동</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855005].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="Vibration">, <color=#e30000>, <u>, <link="Vibration">, </color>, </link>, </u>, [TabExplain]
   EN: When gaining <sprite name="Vibration"><color=#e30000><u><link="Vibration">Tremor</color></link></u>, gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
399. [[refraction2] Pasywka wroga [856001] — nazwa] 피가 흐르는 차원
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856001].name
   limit: do 40 znaków
   EN: Hemorrhaging Dimension
   PL:
400. [[refraction2] Pasywka wroga [856001] — opis] 피가 흐르는 차원을 통과했다면, 피해량 +10%
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal +10% damage after passing through the Hemorrhaging Dimension[TabExplain]
   PL:
401. [[refraction2] Pasywka wroga [856101] — nazwa] 독이 들끓는 차원
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856101].name
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL:
402. [[refraction2] Pasywka wroga [856101] — opis] 독이 들끓는 차원을 통과했다면, 본체 최대 체력 +20%
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Core gains +20% max HP after passing through the Poisonous Dimension[TabExplain]
   PL:
403. [[refraction2] Pasywka wroga [856201] — nazwa] 끊임없이 진동하는 차원
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856201].name
   limit: do 40 znaków
   EN: Tremoring Dimension
   PL:
404. [[refraction2] Pasywka wroga [856201] — opis] 끊임없이 진동하는 차원을 통과했다면, 속도 최솟값 +1, 속도 최댓값 +1
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Min & Max Speed +1 after passing through the Tremoring Dimension[TabExplain]
   PL:
405. [[refraction2] Pasywka wroga [856301] — nazwa] 전류를 뿜어내는 차원
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856301].name
   limit: do 40 znaków
   EN: Electrifying Dimension
   PL:
406. [[refraction2] Pasywka wroga [856301] — opis] 전류를 뿜어내는 차원을 통과했다면, 코인 위력 +1
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Gain +1 Coin Power after passing through the Electrifying Dimension[TabExplain]
   PL:
407. [[refraction2] Pasywka wroga [855101] — nazwa] 황금 시간
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855101].name
   limit: do 40 znaków
   EN: Golden Time
   PL:
408. [[refraction2] Pasywka wroga [855101] — opis] 턴 종료 시 체력이 6% ~ 24%사이로 남았을 때, 전체 체력의 80%만큼 본체와 부위체력 즉시 회복. 흐트러짐 상태 해제. (최대 1회)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855101].desc
   limit: do 190 znaków
   EN: At the end of the turn, if the HP is between 6% and 24%, Core parts instantly heal up to 80% of Max HP, and recover from stagger. (One-time only)
   PL:
409. [[refraction2] Pasywka wroga [855102] — nazwa] 시간 역행 반동
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855102].name
   limit: do 40 znaków
   EN: Time Reversion Retroaction
   PL:
410. [[refraction2] Pasywka wroga [855102] — opis] 황금 시간 발동 이후, 턴 시작 시 취약 2 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855102].desc
   limit: do 120 znaków
   EN: After activating Golden Time, gain 2 Fragile at the start of the turn.
   PL:
411. [[refraction2] Pasywka wroga [855103] — nazwa] 과충전
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855103].name
   limit: do 40 znaków
   EN: Overcharge
   PL:
412. [[refraction2] Pasywka wroga [855103] — opis] 턴 종료 시 충전 횟수가 5이상이면, 다음 턴에 피해량 증가 3 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855103].desc
   limit: do 120 znaków
   EN: If at 5+ Charge Count at the end of the turn, gain 3 Damage Up next turn
   PL:
413. [[refraction2] Pasywka wroga [855104] — nazwa] 굴절된 파열과 침잠
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855104].name
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [[refraction2] Pasywka wroga [855104] — opis] <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>과 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>과 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855104].desc
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [[refraction2] Pasywka wroga [855105] — nazwa] 굴절 화상 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855105].name
   limit: do 40 znaków
   EN: Apply Refracted Burn
   PL:
416. [[refraction2] Pasywka wroga [855105] — opis] <sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855105].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="Combustion">, <color=#e30000>, <u>, <link="Combustion">, </color>, </link>, </u>, [TabExplain]
   EN: When gaining <sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u>, gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
417. [[refraction2] Pasywka wroga [855501] — nazwa] 돌아오는 과거
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855501].name
   limit: do 40 znaków
   EN: Returning Past
   PL:
418. [[refraction2] Pasywka wroga [855501] — opis] <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">축적된 과거</color></link></u>가 50 이상이면, 본체 체력이 80% 이하일 때 턴 종료 시 <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">축적된 과거</color></link></u>를 50 소모하여 본체 체력을 200 회복함.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855501].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPastMirror">, </color>, </link>, </u>
   EN: If at 50+ <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">Accumulated Past</color></link></u>, and if Core's HP is less than or equal to 80%, Core gains 200 HP by spending 50 <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">Accumulated Past</color></link></u>.
   PL:
419. [[refraction2] Pasywka wroga [855502] — nazwa] 소실된 과거
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855502].name
   limit: do 40 znaków
   EN: Misplaced Past
   PL:
420. [[refraction2] Pasywka wroga [855502] — opis] 몸통 부위 파괴 시, <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">축적된 과거</color></link></u> 전부 소모.\n몸통 부위 파괴 시, 다음 턴부터 이번 전투동안 몸통 부위가 모든 속성과 공격 유형에 대하여 내성(0.5)이 됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855502].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPastMirror">, </color>, </link>, </u>, \n
   EN: When the body is broken, spend all <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">Accumulated Past</color></link></u>.\nWhen the body is broken, all Attack Types and Affinities become ineffective(0.5) against the body starting next turn until the end of this encounter.
   PL:
421. [[refraction2] Pasywka wroga [855503] — nazwa] 파괴된 배연 기관
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855503].name
   limit: do 40 znaków
   EN: Broken Exhaust Port
   PL:
422. [[refraction2] Pasywka wroga [855503] — opis] 증기총 부위 파괴 시, 모든 부위의 호흡 전부 소모.\n증기총 부위가 파괴된 이후, <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>을 얻을 때마다 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u>을 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>만큼 얻음.\n증기총 부위가 파괴된 이후, 매 공격 스킬 사용 시 호흡 1을 잃음.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855503].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, <sprite name="Vulnerable">, <color=#e30000>, <link="Vulnerable">, \n
   EN: When the Steam Blaster is broken, completely spend all parts' Poise.\nAfter the Steam Blaster is broken, gain <sprite name="Vulnerable"><color=#f8c200><u><link="Vulnerable">Fragile</color></link></u> equal to the number of <sprite name="Breath"><color=#e30000><u><link="Breath">Poise</color></link></u> every time this unit gains <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u>.\nAfter the Steam Blaster is broken, lose 1 Poise every time this unit uses an Attack Skill.
   PL:
423. [[refraction2] Pasywka wroga [855504] — nazwa] 굴절된 화상과 출혈
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855504].name
   limit: do 40 znaków
   EN: Refracted Burn and Bleed
   PL:
424. [[refraction2] Pasywka wroga [855504] — opis] <sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>과 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>의 위력이 30까지만 누적됨.\n<sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>과 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>의 횟수가 5까지만 누적됨.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855504].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Combustion">, <color=#e30000>, <u>, <link="Combustion">, </color>, </link>, </u>, <sprite name="Laceration">, <link="Laceration">, \n
   EN: <sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u> and <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> Potency maxes out at 30.\n<sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u> and <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> Count maxes out at 5.
   PL:
425. [[refraction2] Pasywka wroga [855505] — nazwa] 굴절 침잠 부과
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855505].name
   (powtórzenie elementu 353 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [[refraction2] Pasywka wroga [855505] — opis] <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</color></link></u>을 얻을 때 위력과 횟수를 1 추가로 얻음. (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855505].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [[refraction2] Pasywka wroga [855506] — nazwa] 새어나오는 증기
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855506].name
   limit: do 40 znaków
   EN: Leaking Steam
   PL:
428. [[refraction2] Pasywka wroga [855506] — opis] 증기총 부위 피격 시, <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>과 호흡 횟수 1 감소
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855506].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: When the Steam Blaster is hit, lose 1 <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> and 1 Poise Count
   PL:
429. [[refraction2] Pasywka wroga [855507] — nazwa] 겹쳐지는 과거
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855507].name
   limit: do 40 znaków
   EN: Overlapping Past
   PL:
430. [[refraction2] Pasywka wroga [855507] — opis] 매 턴마다 축적된 과거 80당 공격 위력 증가 1 얻음.\n<sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">축적된 과거</color></link></u>가 80을 넘었다면, 슬롯 1개 추가.
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855507].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPast">, </color>, </link>, </u>, \n
   EN: Gain 1 Attack Power Up for every 80 Accumulated Past every turn.\nAt 80+ <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPast">Accumulated Past</color></link></u>, gain +1 Slot.
   PL:
431. [[refraction2] Pasywka wroga [855508] — nazwa] 메트로놈
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855508].name
   limit: do 40 znaków
   EN: Metronome
   PL:
432. [[refraction2] Pasywka wroga [855508] — opis] <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">축적된 과거</color></link></u>가 홀수이면 [Vulnerable]과 [AttackDmgUp]를 3 얻음\n짝수이면, [Protection]와 [AttackDmgDown]를 3 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855508].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <sprite name="AccumulatedPast">, <color=#a16a3b>, <u>, <link="AccumulatedPastMirror">, </color>, </link>, </u>, \n, [Vulnerable], [AttackDmgUp], [Protection], [AttackDmgDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up; [Protection] = 보호 / Protection; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: If the <sprite name="AccumulatedPast"><color=#a16a3b><u><link="AccumulatedPastMirror">Accumulated Past</color></link></u> is an odd number, gain 3 [Vulnerable] and [AttackDmgUp]\nIf it is an even number, gain 3 [Protection] and [AttackDmgDown]
   PL:
433. [[refraction2] Pasywka wroga [855601] — nazwa] 영원한 굴레
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855601].name
   limit: do 40 znaków
   EN: Eternal Yoke
   PL:
434. [[refraction2] Pasywka wroga [855601] — opis] 최대 체력이 (순환 횟수 X 5)%만큼 증가.\n가하는 피해량이 (순환 횟수 X 5)%만큼 감소
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max HP increases by (Cycle Count X 5)%.\nDeal (Cycle Count X 5)% less damage
   PL:
435. [[refraction2] Pasywka wroga [855602] — nazwa] 부서진 표지판
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855602].name
   limit: do 40 znaków
   EN: Broken Sign
   PL:
436. [[refraction2] Pasywka wroga [855602] — opis] 표지판 부위가 파괴되면 장미의 최대 체력 감소
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855602].desc
   limit: do 120 znaków
   EN: When the Sign is broken, Rose loses Max HP
   PL:
437. [[refraction2] Pasywka wroga [855603] — nazwa] 흩어진 살점
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855603].name
   limit: do 40 znaków
   EN: Scattered Flesh
   PL:
438. [[refraction2] Pasywka wroga [855603] — opis] 살 부위가 파괴되면 본체의 최대 체력 감소
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855603].desc
   limit: do 120 znaków
   EN: When the flesh is broken, Core loses Max HP
   PL:
439. [[refraction2] Pasywka wroga [855604] — nazwa] 하나의 덩쿨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855604].name
   limit: do 40 znaków
   EN: Singular Vine
   PL:
440. [[refraction2] Pasywka wroga [855604] — opis] 장미를 처치하면 본체와 살 부위의 체력이 30 감소.\n이후 이번 전투 동안 해당 죄악 속성의 내성이 0.1 증가함 (중첩 가능)
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855604].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a Rose is defeated, Core and Flesh lose 30 HP\nGain 0.1 Resistance to the corresponding Sin Affinity during this encounter (Stackable)
   PL:
441. [[refraction2] Pasywka wroga [856401] — nazwa] 증오
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856401].name
   limit: do 40 znaków
   EN: Hatred
   PL:
442. [[refraction2] Pasywka wroga [856401] — opis] 피격 시 마다 다음 턴에 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856401].desc
   limit: do 120 znaków
   EN: When hit, gain 1 Offense Level Up and 1 Defense Level Down next turn
   PL:
443. [[refraction2] Pasywka wroga [856402] — nazwa] 잔화
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856402].name
   limit: do 40 znaków
   EN: Embers
   PL:
444. [[refraction2] Pasywka wroga [856402] — opis] 피격으로 사망 시 대상에게 받은 피해량만큼 피해를 주고, 화상 5 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856402].desc
   limit: do 120 znaków
   EN: When defeated by a direct hit, return the damage to the attacker and inflict 5 Burn
   PL:
445. [[refraction2] Pasywka wroga [856403] — nazwa] 활짝 핀 죄악
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856403].name
   limit: do 40 znaków
   EN: Blossoming Sins
   PL:
446. [[refraction2] Pasywka wroga [856403] — opis] 피어나는 죄 가 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856403].desc
   limit: do 120 znaków
   EN: If at 4 Blooming Sin, enter Power-up state for this encounter
   PL:
447. [[refraction2] Pasywka wroga [856404] — nazwa] 끓어오르는 분노
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856404].name
   limit: do 40 znaków
   EN: Boiling Wrath
   PL:
448. [[refraction2] Pasywka wroga [856404] — opis] 강화 상태일 때 스킬의 효과로 부여하는 화상 +1.\n강화 상태에서 사망 시 모든 아군에게 화상 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856404].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Power-up state, inflict +1 more Burn with Skill effects\nIf killed during Power-up state, inflict 4 Burn Count to all allies
   PL:
449. [[refraction2] Pasywka wroga [856405] — nazwa] 덩쿨에 핀 장미
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856405].name
   limit: do 40 znaków
   EN: Rose on a Vine
   PL:
450. [[refraction2] Pasywka wroga [856405] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856405].desc
   limit: do 120 znaków
   EN: Dies when the Core of Sign of Roses is killed
   PL:
451. [[refraction2] Pasywka wroga [856501] — nazwa] 일방적 욕망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856501].name
   limit: do 40 znaków
   EN: One-sided Desire
   PL:
452. [[refraction2] Pasywka wroga [856501] — opis] 합 진행 시 최종 위력 -2, 일방 공격 시 최종 위력 +2
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856501].desc
   limit: do 120 znaków
   EN: In a clash, Final Power -2; In an unopposed attack, Final Power +2
   PL:
453. [[refraction2] Pasywka wroga [856502] — nazwa] 활짝 핀 죄악
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856502].name
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [[refraction2] Pasywka wroga [856502] — opis] 피어나는 죄 가 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856502].desc
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [[refraction2] Pasywka wroga [856503] — nazwa] 일렁이는 색욕
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856503].name
   limit: do 40 znaków
   EN: Shimmering Lust
   PL:
456. [[refraction2] Pasywka wroga [856503] — opis] 강화 상태일 때 스킬의 효과로 부여하는 출혈 +1.\n강화 상태에서 사망 시 모든 아군에게 출혈 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856503].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Power-up state, inflict +1 more Bleed with Skill effects\nIf killed during Power-up state, inflict 4 Bleed Count to all allies
   PL:
457. [[refraction2] Pasywka wroga [856504] — nazwa] 덩쿨에 핀 장미
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856504].name
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [[refraction2] Pasywka wroga [856504] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856504].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [[refraction2] Pasywka wroga [856601] — nazwa] 무기력
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856601].name
   limit: do 40 znaków
   EN: Powerless
   PL:
460. [[refraction2] Pasywka wroga [856601] — opis] 피격 시 다음 턴에 흐트러짐 상태가 아니면 보호 5를 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856601].desc
   limit: do 120 znaków
   EN: When hit, gain 5 Protection next turn unless Staggered
   PL:
461. [[refraction2] Pasywka wroga [856602] — nazwa] 노란 장미 2
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856602].name
   limit: do 40 znaków
   EN: Yellow Rose 2
   PL:
462. [[refraction2] Pasywka wroga [856602] — opis] 피어남이 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856602].desc
   limit: do 120 znaków
   EN: If at 4 Blooming Sin, enter Power-up state for this encounter
   PL:
463. [[refraction2] Pasywka wroga [856603] — nazwa] 짓누르는 나태
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856603].name
   limit: do 40 znaków
   EN: Crushing Sloth
   PL:
464. [[refraction2] Pasywka wroga [856603] — opis] 강화 상태일 때 스킬의 효과로 부여하는 진동 +1.\n강화 상태에서 사망 시 모든 아군에게 진동 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856603].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Power-up state, inflict +1 more Tremor with Skill effects\nIf killed during Power-up state, inflict 4 Tremor Count to all allies
   PL:
465. [[refraction2] Pasywka wroga [856604] — nazwa] 노란 장미 4
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856604].name
   limit: do 40 znaków
   EN: Yellow Rose 4
   PL:
466. [[refraction2] Pasywka wroga [856604] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856604].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [[refraction2] Pasywka wroga [856701] — nazwa] 허기
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856701].name
   limit: do 40 znaków
   EN: Hunger
   PL:
468. [[refraction2] Pasywka wroga [856701] — opis] 턴 종료 시 이번 턴에 피해를 주지 못한 경우 파열 취약 2를 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856701].desc
   limit: do 120 znaków
   EN: If this unit fails to deal damage in a turn, gain 2 Rupture Fragility
   PL:
469. [[refraction2] Pasywka wroga [856702] — nazwa] 초록 장미 2
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856702].name
   limit: do 40 znaków
   EN: Green Rose 2
   PL:
470. [[refraction2] Pasywka wroga [856702] — opis] 피어남이 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856702].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [[refraction2] Pasywka wroga [856703] — nazwa] 자라나는 탐식
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856703].name
   limit: do 40 znaków
   EN: Growing Gluttony
   PL:
472. [[refraction2] Pasywka wroga [856703] — opis] 강화 상태일 때 스킬의 효과로 부여하는 파열 +1.\n강화 상태에서 사망 시 모든 아군에게 파열 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856703].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Power-up state, inflict +1 more Rupture with Skill effects\nIf killed during Power-up state, inflict 4 Rupture Count to all allies
   PL:
473. [[refraction2] Pasywka wroga [856704] — nazwa] 초록 장미 4
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856704].name
   limit: do 40 znaków
   EN: Green Rose 4
   PL:
474. [[refraction2] Pasywka wroga [856704] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856704].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [[refraction2] Pasywka wroga [856801] — nazwa] 불안
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856801].name
   limit: do 40 znaków
   EN: Anxiety
   PL:
476. [[refraction2] Pasywka wroga [856801] — opis] 합 진행 시 최종 위력 +2, 일방 공격 시 최종 위력 -2
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856801].desc
   limit: do 120 znaków
   EN: In a clash, Final Power +2; In an unopposed attack, Final Power -2
   PL:
477. [[refraction2] Pasywka wroga [856802] — nazwa] 자기 파괴
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856802].name
   limit: do 40 znaków
   EN: Self Destruction
   PL:
478. [[refraction2] Pasywka wroga [856802] — opis] 피격 시 다음 턴에 우울 내성이 약점(1.5)으로 변경되고, 보호 5 를 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856802].desc
   limit: do 120 znaków
   EN: When hit, Gloom Resist turns into Gloom Weak(1.5) and gain 5 Protection
   PL:
479. [[refraction2] Pasywka wroga [856803] — nazwa] 파란 장미 3
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856803].name
   limit: do 40 znaków
   EN: Blue Rose 3
   PL:
480. [[refraction2] Pasywka wroga [856803] — opis] 피어남이 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856803].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [[refraction2] Pasywka wroga [856804] — nazwa] 일렁이는 우울
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856804].name
   limit: do 40 znaków
   EN: Shimmering Gloom
   PL:
482. [[refraction2] Pasywka wroga [856804] — opis] 강화 상태일 때 스킬의 효과로 부여하는 침잠 +1.\n강화 상태에서 사망 시 모든 아군에게 침잠 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856804].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Power-up state, inflict +1 more Sinking with Skill effects\nIf killed during Power-up state, inflict 4 Sinking Count to all allies
   PL:
483. [[refraction2] Pasywka wroga [856805] — nazwa] 파란 장미 5
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856805].name
   limit: do 40 znaków
   EN: Blue Rose 5
   PL:
484. [[refraction2] Pasywka wroga [856805] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856805].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [[refraction2] Pasywka wroga [856901] — nazwa] 비난
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856901].name
   limit: do 40 znaków
   EN: Outlash
   PL:
486. [[refraction2] Pasywka wroga [856901] — opis] 매 턴 시작 시 아군에게 호흡 1, 호흡 횟수 1 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856901].desc
   limit: do 120 znaków
   EN: At the start of every turn, apply 1 Poise and 1 Poise count to allies
   PL:
487. [[refraction2] Pasywka wroga [856902] — nazwa] 우월함
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856902].name
   limit: do 40 znaków
   EN: Superiority
   PL:
488. [[refraction2] Pasywka wroga [856902] — opis] 이 유닛이 생존해있으면, 각 아군이 자신의 호흡 1 당 크리티컬 피해량 +5%
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856902].desc
   limit: do 120 znaków
   EN: If this unit is alive, every ally gains +5% Critical Damage per Poise on self
   PL:
489. [[refraction2] Pasywka wroga [856903] — nazwa] 남색 장미 3
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856903].name
   limit: do 40 znaków
   EN: Azure Rose 3
   PL:
490. [[refraction2] Pasywka wroga [856903] — opis] 피어남이 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856903].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [[refraction2] Pasywka wroga [856904] — nazwa] 부풀어오른 오만
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856904].name
   limit: do 40 znaków
   EN: Overinflated Pride
   PL:
492. [[refraction2] Pasywka wroga [856904] — opis] 강화 상태일 때 턴 시작 시, 스킬의 효과로 부여하는 호흡 +1.\n강화 상태에서 사망 시 모든 적에게 호흡 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856904].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If starting a turn in a Power-up state, gain +1 more Poise with Skill effects\nIf killed during Power-up state, apply 4 Poise Count to all enemies
   PL:
493. [[refraction2] Pasywka wroga [856905] — nazwa] 남색 장미 5
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856905].name
   limit: do 40 znaków
   EN: Azure Rose 5
   PL:
494. [[refraction2] Pasywka wroga [856905] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=856905].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [[refraction2] Pasywka wroga [857001] — nazwa] 시기
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857001].name
   limit: do 40 znaków
   EN: Jealousness
   PL:
496. [[refraction2] Pasywka wroga [857001] — opis] 매 턴 시작 시 무작위 아군 2명에게 충전 횟수 1 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857001].desc
   limit: do 120 znaków
   EN: At the start of the turn, apply 1 Charge Count to 2 random allies
   PL:
497. [[refraction2] Pasywka wroga [857002] — nazwa] 열등감
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857002].name
   limit: do 40 znaków
   EN: Inferiority Complex
   PL:
498. [[refraction2] Pasywka wroga [857002] — opis] 이 유닛이 생존해있으면, 각 아군이 자신의 충전 횟수 1 당 피해량 +5%
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857002].desc
   limit: do 120 znaków
   EN: If this unit is alive, each ally gains +5% Critical Damage per Charge Count on self
   PL:
499. [[refraction2] Pasywka wroga [857003] — nazwa] 보란 장미 3
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857003].name
   limit: do 40 znaków
   EN: Purple Rose 3
   PL:
500. [[refraction2] Pasywka wroga [857003] — opis] 피어남이 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857003].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [[refraction2] Pasywka wroga [857004] — nazwa] 번뜩이는 질투
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857004].name
   limit: do 40 znaków
   EN: Glaring Envy
   PL:
502. [[refraction2] Pasywka wroga [857004] — opis] 강화 상태일 때 턴 시작 시, 스킬의 효과로 부여하는 충전 횟수 +1.\n강화 상태에서 사망 시 모든 적에게 충전 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857004].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If starting a turn in a Power-up state, inflict +1 more Charge Count with Skill effects\nIf killed during Power-up state, apply 4 Charge Count to all enemies
   PL:
503. [[refraction2] Pasywka wroga [857005] — nazwa] 보란 장미 5
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857005].name
   limit: do 40 znaków
   EN: Purple Rose 5
   PL:
504. [[refraction2] Pasywka wroga [857005] — opis] 장미 표지판 본체 잡으면 사망
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=857005].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [[refraction2] Pasywka wroga [855605] — nazwa] 활짝 핀 죄악
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855605].name
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [[refraction2] Pasywka wroga [855605] — opis] 피어나는 죄 가 4가 되면 이번 전투동안 강화 상태가 됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855605].desc
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [[refraction2] Pasywka wroga [855606] — nazwa] 덩쿨에 핀 장미
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855606].name
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [[refraction2] Pasywka wroga [855606] — opis] 장미 표지판이 제압되면 함께 제압됨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855606].desc
   limit: do 120 znaków
   EN: Dies when Sign of Roses is defeated
   PL:
509. [[refraction2] Pasywka wroga [854403] — nazwa] 옮겨붙는 불씨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854403].name
   limit: do 40 znaków
   EN: Spreading Ember
   PL:
510. [[refraction2] Pasywka wroga [854403] — opis] 턴 종료 시 자신에게 <sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>이 있다면, <sprite name="WrappedCurseTagRe"><color=#a16a3b><u><link="WrappedCurseTagRe">얽혀온 저주 부적</color></link></u>을 가지고 있는 모든 대상에게 가지고 있는 <sprite name="Combustion"><color=#e30000><u><link="Combustion">화상</color></link></u>만큼 다음 턴에 화상 부여
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=854403].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <sprite name="Combustion">, <color=#e30000>, <u>, <link="Combustion">, </color>, </link>, </u>, <sprite name="WrappedCurseTagRe">, <color=#a16a3b>, <link="WrappedCurseTagRe">
   EN: At the end of the turn, if this unit has <sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u>, inflict the same amount of <sprite name="Combustion"><color=#e30000><u><link="Combustion">Burn</color></link></u> to all units with <sprite name="WrappedCurseTagRe"><color=#a16a3b><u><link="WrappedCurseTagRe">Entangled Curse Talisman</color></link></u> next turn
   PL:
511. [[refraction2] Pasywka wroga [855607] — nazwa] 죄를 머금은 가시 덩쿨
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855607].name
   limit: do 40 znaków
   EN: Sin-drenched Brambles
   PL:
512. [[refraction2] Pasywka wroga [855607] — opis] 매 턴마다 모든 부위가 면류관 효과를 가진 수감자 수만큼 보호 를 얻음
   źródło: Passives_Abnormality_Refraction2.json :: dataList[id=855607].desc
   limit: do 130 znaków
   EN: Every turn, all parts gain Protection equal to the number of Sinners with the Crown of Thorns effect
   PL:

## [refraction2_bokgak] Umiejętności wrogów / Anomalii — Skills_Abnormality_Refraction2_bokgak
- grupa rozdziału/trybu: `refraction2_bokgak` · plik: `Skills_Abnormality_Refraction2_bokgak.json`

513. [Umiejętność wroga [962201] (ulepszenie 1) — nazwa] 얽혀가는 부적
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962201].levelList[level=1].name
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Umiejętność wroga [962201] (ulepszenie 1) — opis] [WhenUse] 대상에게 [WrappedCurseTagRe] 3 부여\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 대상의 [Burst]을 발동 시키지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962201].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WrappedCurseTagRe], [DefeatDuel], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WrappedCurseTagRe] = 얽혀온 저주 부적 / Entangled Curse Talisman; [DefeatDuel] = [합 패배] / [Clash Lose]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Inflict 3 [WrappedCurseTagRe] on target\n\n[DefeatDuel]\n- Damage dealt by this Skill cannot Stagger the target\n- Does not activate [Burst] on target
   PL:
515. [Umiejętność wroga [962201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
516. [Umiejętność wroga [962201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst] and +2 [Burst] Count
   PL:
517. [Umiejętność wroga [962202] (ulepszenie 1) — nazwa] 쌓여가는 저주
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962202].levelList[level=1].name
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność wroga [962202] (ulepszenie 1) — opis] [WhenUse] 대상이 가지고 있는 [WrappedCurseTagRe]만큼 [WrappedCurseTagRe] 부여\n- 대상에게 [WrappedCurseTagRe]이 없으면 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962202].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WrappedCurseTagRe]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WrappedCurseTagRe] = 얽혀온 저주 부적 / Entangled Curse Talisman
   EN: [WhenUse] Inflict [WrappedCurseTagRe] equal to [WrappedCurseTagRe] on target\n- If target does not have [WrappedCurseTagRe], inflict 3 [WrappedCurseTagRe]
   PL:
519. [Umiejętność wroga [962202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst] and +2 [Burst] Count
   PL:
520. [Umiejętność wroga [962202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 516 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Umiejętność wroga [962203] (ulepszenie 1) — nazwa] 누구도 울지 않도록
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].name
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [962203] (ulepszenie 1) — opis] [WhenUse] 가지고 있는 [ReattachedCurseTag_Re]이 10개 이상이면, 코인 위력 -1\n[WhenUse] 대상의 [WrappedCurseTagRe]이 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 최종 위력 -10, 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 대상의 [Burst]을 발동 시키지 않음\n[EndBattle] [ReattachedCurseTag_Re] 전부 소멸
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReattachedCurseTag_Re], [WrappedCurseTagRe], [SuperCoin], [DefeatDuel], [Burst], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReattachedCurseTag_Re] = 다시 붙여진 저주 부적 / Reattached Curse Talisman; [WrappedCurseTagRe] = 얽혀온 저주 부적 / Entangled Curse Talisman; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [Burst] = 파열 / Rupture; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] At 10+ [ReattachedCurseTag_Re], Coin Power -1\n[WhenUse] If target has 3+ [WrappedCurseTagRe], convert all Coins on this Skill into [SuperCoin]s\n\n[DefeatDuel]\n- Final Power -10, deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n- Does not activate [Burst] on target\n[EndBattle] All [ReattachedCurseTag_Re] expires
   PL:
523. [Umiejętność wroga [962203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst] and +1 [Burst] Count
   PL:
524. [Umiejętność wroga [962203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [962203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [962203] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność wroga [962203] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 5 [Paralysis] next turn
   PL:
528. [Umiejętność wroga [962203] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962203].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 5 [Binding] next turn
   PL:
529. [Umiejętność wroga [962204] (ulepszenie 1) — nazwa] 이전하는 부적
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962204].levelList[level=1].name
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [962204] (ulepszenie 1) — opis] [StartBattle] 모든 부위에 [Protection] 3 얻음\n[WhenUse] 대상의 [WrappedCurseTagRe]을 전부 소멸\n- 소멸시킨 만큼 [ReattachedCurseTag_Re] 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962204].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Protection], [WhenUse], [WrappedCurseTagRe], [ReattachedCurseTag_Re]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [WrappedCurseTagRe] = 얽혀온 저주 부적 / Entangled Curse Talisman; [ReattachedCurseTag_Re] = 다시 붙여진 저주 부적 / Reattached Curse Talisman
   EN: [StartBattle] All Parts gain 3 [Protection]\n[WhenUse] All [WrappedCurseTagRe] on target expires\n- Gain [ReattachedCurseTag_Re] equal to the [WrappedCurseTagRe] Stack expired
   PL:
531. [Umiejętność wroga [962205] (ulepszenie 1) — nazwa] 복제되는 저주
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962205].levelList[level=1].name
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność wroga [962205] (ulepszenie 1) — opis] [WhenUse] 대상이 가지고 있는 [WrappedCurseTagRe]만큼 [WrappedCurseTagRe] 부여\n- 대상에게 [WrappedCurseTagRe]이 없으면 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962205].levelList[level=1].desc
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność wroga [962206] (ulepszenie 1) — nazwa] 누구도 울지 않도록
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].name
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Umiejętność wroga [962206] (ulepszenie 1) — opis] [WhenUse] 가지고 있는 [ReattachedCurseTag_Re]이 10개 이상이면, 코인 위력 -1\n[WhenUse] 대상의 [WrappedCurseTagRe]이 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 최종 위력 -10, 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 대상의 [Burst]을 발동 시키지 않음\n[EndBattle] [ReattachedCurseTag_Re] 전부 소멸
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].desc
   (powtórzenie elementu 522 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność wroga [962206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność wroga [962206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [962206] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność wroga [962206] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Umiejętność wroga [962206] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [962206] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962206].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Umiejętność wroga [962301] (ulepszenie 1) — nazwa] 6463
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962301].levelList[level=1].name
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Umiejętność wroga [962301] (ulepszenie 1) — opis] [AccumulatedPast] 50당 피해량 +10%\n[WhenUse] 자신의 [AccumulatedPast]가 홀수이면, 이 스킬의 피해량 +30%\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962301].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPast], [WhenUse], [DefeatDuel]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +10% damage for every 50 [AccumulatedPast] on self\n[WhenUse] If this unit's [AccumulatedPast] is an odd number, this Skill deals +30% damage\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL:
543. [Umiejętność wroga [962301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [962301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Binding] next turn
   PL:
545. [Umiejętność wroga [962302] (ulepszenie 1) — nazwa] 6753
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962302].levelList[level=1].name
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność wroga [962302] (ulepszenie 1) — opis] [AccumulatedPast] 50당 피해량 +10%\n[WhenUse] 자신의 [AccumulatedPast]가 짝수이면, [Protection] 3 얻음 (턴당 1회)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962302].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPast], [WhenUse], [Protection]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: Deal +10% damage for every 50 [AccumulatedPast]\n[WhenUse] If this unit's [AccumulatedPast] is an even number, gain 3 [Protection] (once per turn)
   PL:
547. [Umiejętność wroga [962302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność wroga [962303] (ulepszenie 1) — nazwa] 853
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962303].levelList[level=1].name
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność wroga [962303] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 5당 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Clash Power +1 for every 5 [Breath] on self (max 3)
   PL:
550. [Umiejętność wroga [962303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Umiejętność wroga [962303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność wroga [962303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AccumulatedPast]당 피해량 +1% (최대 50%)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AccumulatedPast]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AccumulatedPast] = 축적된 과거 / Accumulated Past
   EN: [OnSucceedAttack] Deal +1% damage for every [AccumulatedPast] (max 50%)
   PL:
553. [Umiejętność wroga [962304] (ulepszenie 1) — nazwa] 5384
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].name
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [962304] (ulepszenie 1) — opis] [WhenUse] 모든 부위에 [Breath] 3, [Breath] 횟수 3을 얻음\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] All Parts gain 3 [Breath] and +3 [Breath] Count\n\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
555. [Umiejętność wroga [962304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [962304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath]만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Raise Stagger Threshold equal to [Breath] on self
   PL:
557. [Umiejętność wroga [962304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność wroga [962304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3당 피해량 +20% (최대 100%)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Deal +20% damage for every 3 [Breath] (max 100%)
   PL:
559. [Umiejętność wroga [962304] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 모든 부위에 [Breath] 4를 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962304].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] All Parts gain 4 [Breath]
   PL:
560. [Umiejętność wroga [962305] (ulepszenie 1) — nazwa] 6475384
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962305].levelList[level=1].name
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [962305] (ulepszenie 1) — opis] 자신의 [Breath]이 7이상이면, 코인 위력 +1\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962305].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [DefeatDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: At 7+ [Breath], Coin Power +1\n\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
562. [Umiejętność wroga [962305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność wroga [962305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath]이 5이상이면, 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] At 5+ [Breath], raise Stagger Threshold by 50% of damage dealt
   PL:
564. [Umiejętność wroga [962305] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 모든 부위에 [Breath] 8, [Breath] 횟수 4를 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Umiejętność wroga [962306] (ulepszenie 1) — nazwa] 974569A
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962306].levelList[level=1].name
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność wroga [962306] (ulepszenie 1) — opis] 자신의 [Breath]이 10 이상이면, 스킬 위력 +2
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 10+ [Breath], Skill Power +2
   PL:
567. [Umiejętność wroga [962306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [AccumulatedPast]당 피해량 +1% (최대 200%)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AccumulatedPast]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past
   EN: Deal +1% damage for every [AccumulatedPast] (max 200%)
   PL:
568. [Umiejętność wroga [962401] (ulepszenie 1) — nazwa] 침울한 신음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962401].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność wroga [962401] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Sinking]의 합 3당 최종 위력 +1 (최대 2)\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962401].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Sinking], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 3 ([Burst] + [Sinking]) on target (max 2)\n\n[DefeatDuel]\n- Damage dealt by this Skill cannot Stagger the target
   PL:
570. [Umiejętność wroga [962401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [962401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL:
572. [Umiejętność wroga [962402] (ulepszenie 1) — nazwa] 몰아치는 침잠
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962402].levelList[level=1].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [962402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Sinking]의 합 3당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Final Power +1 for every 3 ([Burst] + [Sinking]) on target (max 2)
   PL:
574. [Umiejętność wroga [962402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
575. [Umiejętność wroga [962402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
576. [Umiejętność wroga [962403] (ulepszenie 1) — nazwa] 슬픔의 반동
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962403].levelList[level=1].name
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność wroga [962403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Sinking]의 합 3당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962403].levelList[level=1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [962403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL:
579. [Umiejętność wroga [962403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
580. [Umiejętność wroga [962404] (ulepszenie 1) — nazwa] 슬픔의 격류
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962404].levelList[level=1].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [962404] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Sinking]의 합 3당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962404].levelList[level=1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [962404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
583. [Umiejętność wroga [962404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
584. [Umiejętność wroga [962404] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962404].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL:
585. [Umiejętność wroga [962405] (ulepszenie 1) — nazwa] 무언가를 찾는 울음소리
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962405].levelList[level=1].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [962405] (ulepszenie 1) — opis] 낡은 우산당 피해량 +25%\n[WhenUse] 살아있는 낡은 우산당 합 위력 +2\n[DefeatDuel]\n- 최종 위력 -10, 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 대상의 [Burst]과 [Sinking]을 발동 시키지 않음\n[EndBattle] 낡은 우산 모두 소멸\n[EndBattle] 1턴에 얻은 [WaveFoxUmbrella]만큼 [WaveFoxUmbrella]을 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962405].levelList[level=1].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Burst], [Sinking], [EndBattle], [WaveFoxUmbrella]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [EndBattle] = [턴 종료 시] / [Turn End]; [WaveFoxUmbrella] = 보호 우산 / Protection Umbrella
   EN: Deal +25% damage for every Old Umbrella\n[WhenUse] Clash Power +2 for every surviving Old Umbrella\n\n[DefeatDuel]\n- Final Power -10, deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n- Does not activate [Burst] and [Sinking] on target\n\n[EndBattle] All Old Umbrella expires\n[EndBattle] Gain [WaveFoxUmbrella] equal to the [WaveFoxUmbrella] Stack gained in the first turn
   PL:
587. [Umiejętność wroga [962405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność wroga [962405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
589. [Umiejętność wroga [962406] (ulepszenie 1) — nazwa] 기다림
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962406].levelList[level=1].name
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [962406] (ulepszenie 1) — opis] [StartBattle] 모든 적 정신력 -20
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962406].levelList[level=1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [962407] (ulepszenie 1) — nazwa] 날카로운 반응
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962407].levelList[level=1].name
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [962407] (ulepszenie 1) — opis] [StartBattle] [Thorn]를 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962407].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Thorn]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Thorn] = 가시 / Thorns
   EN: [StartBattle] Gain [Thorn]
   PL:
593. [Umiejętność wroga [962408] (ulepszenie 1) — nazwa] 날카로운 반응
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962408].levelList[level=1].name
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [962408] (ulepszenie 1) — opis] [StartBattle] [Thorn]를 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962408].levelList[level=1].desc
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [962409] (ulepszenie 1) — nazwa] 애원하는 울음소리
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962409].levelList[level=1].name
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność wroga [962409] (ulepszenie 1) — opis] 합 진행 시 살아있는 낡은 우산당 합 위력 +2\n낡은 우산당 피해량 +25%\n[DefeatDuel]\n- 최종 위력 -10, 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 대상의 [Burst]과 [Sinking]을 발동 시키지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962409].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [Burst], [Sinking]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: In a Clash, Clash Power +2 for every surviving Old Umbrella\nDeal +25% damage for every Old Umbrella\n\n[DefeatDuel]\n- Final Power -10, deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n- Does not activate [Burst] and [Sinking] on target
   PL:
597. [Umiejętność wroga [962409] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962409].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [962409] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962409].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [962501] (ulepszenie 1) — nazwa] 흩뿌려지는 슬픔
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962501].levelList[level=1].name
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [962501] (ulepszenie 1) — opis] [EndSkill] 모든 적의 [Burst] 횟수 3, [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Burst], [Sinking]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [EndSkill] Inflict +3 [Burst] Count and +3 [Sinking] Count on all enemies
   PL:
601. [Umiejętność wroga [961801] (ulepszenie 1) — nazwa] 맞물리는 순간
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961801].levelList[level=1].name
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [961801] (ulepszenie 1) — opis] [Charge] 횟수 3당 기본 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 3 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961801].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Gain Base Power +1 for every 3 [Charge] Count\n[WhenUse] Gain +3 [Charge] Count\n[DefeatDuel] Consume 2 [Charge] Count
   PL:
603. [Umiejętność wroga [961801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [InterlockingTimeBokGak] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [InterlockingTimeBokGak]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [InterlockingTimeBokGak] = 맞물리는 시간 / Interlocking Time
   EN: [OnSucceedAttack] Inflict 1 [InterlockingTimeBokGak]
   PL:
604. [Umiejętność wroga [961801] (ulepszenie 1) — moneta 1, efekt 2 — opis] - 대상에게 부정적인 효과가 있으면, 대신 [InterlockingTimeBokGak] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [InterlockingTimeBokGak]
   znaczenie tagów: [InterlockingTimeBokGak] = 맞물리는 시간 / Interlocking Time
   EN: - If target has a negative effect, inflict 2 [InterlockingTimeBokGak] instead
   PL:
605. [Umiejętność wroga [961801] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961801].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność wroga [961802] (ulepszenie 1) — nazwa] 시간 흡수
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961802].levelList[level=1].name
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [961802] (ulepszenie 1) — opis] [Charge] 횟수 3당 기본 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: Base Power +1 for every 3 [Charge] Count\n[WhenUse] Gain +4 [Charge] Count
   PL:
608. [Umiejętność wroga [961802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [TimeRental_Re] 3 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TimeRental_Re]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRental_Re] = 시간 대여 / Borrowed Time
   EN: [OnSucceedAttack] Gain 3 [TimeRental_Re] next turn
   PL:
609. [Umiejętność wroga [961802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL:
610. [Umiejętność wroga [961803] (ulepszenie 1) — nazwa] 가속되는 순간
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].name
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność wroga [961803] (ulepszenie 1) — opis] [TimeRental_Re]당 기본 위력 +1\n[DefeatDuel]\n- 자신의 [Charge] 횟수 3 소모\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [TimeRental_Re], [DefeatDuel], [Charge]
   znaczenie tagów: [TimeRental_Re] = 시간 대여 / Borrowed Time; [DefeatDuel] = [합 패배] / [Clash Lose]; [Charge] = 충전 / Charge
   EN: Base Power +1 for every [TimeRental_Re]\n\n[DefeatDuel]\n- Consume 3 [Charge] Count\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
612. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
614. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [InterlockingTimeBokGak] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [InterlockingTimeBokGak] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [InterlockingTimeBokGak]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [InterlockingTimeBokGak] = 맞물리는 시간 / Interlocking Time
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [InterlockingTimeBokGak]
   PL:
616. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +4 [Charge] Count
   PL:
618. [Umiejętność wroga [961803] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [TimeRental_Re]당 피해량 +20%
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961803].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [TimeRental_Re]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [TimeRental_Re] = 시간 대여 / Borrowed Time
   EN: [UnBrokenCoinOnSucceedAttack] Deal +20% damage for every [TimeRental_Re]
   PL:
619. [Umiejętność wroga [961804] (ulepszenie 1) — nazwa] 충전 방어
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961804].levelList[level=1].name
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [961804] (ulepszenie 1) — opis] [StartBattle] 자신의 충전 횟수 2 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Charge]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge
   EN: [StartBattle] Gain +2 [Charge] Count
   PL:
621. [Umiejętność wroga [962001] (ulepszenie 1) — nazwa] 걸려든 미끼
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962001].levelList[level=1].name
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [962001] (ulepszenie 1) — opis] [CantDuel]\n[FairyCharm]에 걸린 수감자를 우선으로 지정\n공격 가중치가 [FairyCharm]에 걸린 수감자 수만큼 적용됨
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962001].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [FairyCharm]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [FairyCharm] = 매혹 / Charmed
   EN: [CantDuel]\nPrioritizes Sinners who are [FairyCharm]\nThis Skill's Atk Weight = Number of Sinners who are [FairyCharm]
   PL:
623. [Umiejętność wroga [962001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [962001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
625. [Umiejętność wroga [962001] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 본체, 몸통 체력 15 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962001].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core and Body heal 15 HP
   PL:
626. [Umiejętność wroga [962002] (ulepszenie 1) — nazwa] 파고드는 뿌리
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962002].levelList[level=1].name
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność wroga [962002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [962002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
629. [Umiejętność wroga [962003] (ulepszenie 1) — nazwa] 확산하는 뿌리
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962003].levelList[level=1].name
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [962003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL:
631. [Umiejętność wroga [962003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
632. [Umiejętność wroga [962004] (ulepszenie 1) — nazwa] 침식하는 줄기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962004].levelList[level=1].name
   limit: do 40 znaków
   EN: Infusing Stems
   PL:
633. [Umiejętność wroga [962004] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
634. [Umiejętność wroga [962004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność wroga [962004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 수치당 피해량 +5% (최대 100%)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +5% damage for every [Burst] on target (max 100%)
   PL:
636. [Umiejętność wroga [962005] (ulepszenie 1) — nazwa] 드러난 심연
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962005].levelList[level=1].name
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [962005] (ulepszenie 1) — opis] 대상의 [Burst]이 5이상이면, 피해량 +100%\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962005].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [DefeatDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 5+ [Burst], deal +100% damage\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
638. [Umiejętność wroga [962005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [962006] (ulepszenie 1) — nazwa] 매혹된 자아
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962006].levelList[level=1].name
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [962006] (ulepszenie 1) — opis] 요정 초롱을 공격할 때 피해가 0으로 적용됨
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962006].levelList[level=1].desc
   limit: do 120 znaków
   EN: Attacking Faelantern deals 0 damage
   PL:
641. [Umiejętność wroga [962007] (ulepszenie 1) — nazwa] 걸려든 미끼
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962007].levelList[level=1].name
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność wroga [962007] (ulepszenie 1) — opis] [CantDuel]\n[FairyCharm]에 걸린 수감자를 우선으로 지정\n공격 가중치가 [FairyCharm]에 걸린 수감자 수만큼 적용됨
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962007].levelList[level=1].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [962007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +3 [Burst] Count
   PL:
644. [Umiejętność wroga [962007] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962007].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +3 [Laceration] Count
   PL:
645. [Umiejętność wroga [962007] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 본체, 몸통 체력 30 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962007].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core and Body heal 30 HP
   PL:
646. [Umiejętność wroga [962101] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962101].levelList[level=1].name
   limit: do 40 znaków
   EN: Bite
   PL:
647. [Umiejętność wroga [962101] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 2 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 기본 위력 +2\n[DefeatDuel] [SelfCharge] 1 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962101].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 2 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Base Power +2\n[DefeatDuel] Lose 1 [SelfCharge]
   PL:
648. [Umiejętność wroga [962101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL:
649. [Umiejętność wroga [962102] (ulepszenie 1) — nazwa] 꼬리찌르기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962102].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Poke
   PL:
650. [Umiejętność wroga [962102] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 2 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 코인 위력 +1\n[DefeatDuel] [SelfCharge] 1 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962102].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 2 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Coin Power +1\n[DefeatDuel] Lose 1 [SelfCharge]
   PL:
651. [Umiejętność wroga [962102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność wroga [962102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [962103] (ulepszenie 1) — nazwa] 감아 조이기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962103].levelList[level=1].name
   limit: do 40 znaków
   EN: Wrapping Coil
   PL:
654. [Umiejętność wroga [962103] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 3 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 기본 위력 +2\n[DefeatDuel] [SelfCharge] 1 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962103].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 3 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Base Power +2\n[DefeatDuel] Lose 1 [SelfCharge]
   PL:
655. [Umiejętność wroga [962103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność wroga [962103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL:
657. [Umiejętność wroga [962103] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962103].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
658. [Umiejętność wroga [962104] (ulepszenie 1) — nazwa] 전류 주입
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962104].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [962104] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 1 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 코인 위력 +1\n대상에게 [Paralysis]가 있다면 피해량 +30%\n[DefeatDuel] [SelfCharge] 2 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962104].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [Paralysis], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 1 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Coin Power +1\nIf target has [Paralysis], deal +30% damage\n[DefeatDuel] Lose 2 [SelfCharge]
   PL:
660. [Umiejętność wroga [962104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
661. [Umiejętność wroga [962104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis]
   PL:
662. [Umiejętność wroga [962105] (ulepszenie 1) — nazwa] 전기 방류
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962105].levelList[level=1].name
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność wroga [962105] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 1 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 코인 위력 +1\n대상에게 [Paralysis]가 있다면 피해량 +30%\n[DefeatDuel] [SelfCharge] 3 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962105].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [Paralysis], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 1 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Coin Power +1\nIf target has [Paralysis], deal +30% damage\n[DefeatDuel] Lose 3 [SelfCharge]
   PL:
664. [Umiejętność wroga [962105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność wroga [962105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Umiejętność wroga [962105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność wroga [962106] (ulepszenie 1) — nazwa] 전기 방출
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962106].levelList[level=1].name
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność wroga [962106] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 1 얻음\n대상에게 [Paralysis]가 있다면 피해량 +30%
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962106].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [Paralysis]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [Paralysis] = 마비 / Paralyze
   EN: [StartBattle] Gain 1 [SelfCharge]\nIf target has [Paralysis], deal +30% damage
   PL:
669. [Umiejętność wroga [962106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Umiejętność wroga [962106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 5 [Paralysis]
   PL:
671. [Umiejętność wroga [962107] (ulepszenie 1) — nazwa] 초고압 전기 방출
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [962107] (ulepszenie 1) — opis] [WhenUse] 자신의 [SelfCharge]이 7초과라면, 초과된 [SelfCharge]마다 피해량 +10% (최대 120%)\n[WhenUse] 가지고 있는 [SelfCharge] 전부 소모하고, 소모한 [SelfCharge]이 10 이상이면, 합 위력 +5\n[DefeatDuel] 이 공격 스킬이 가하는 피해는 0이 됨
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SelfCharge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SelfCharge] = 자가 충전 / Self-charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At more than 7 [SelfCharge], deal +10% damage for every excess [SelfCharge] past 7 (max 120%)\n[WhenUse] Lose all [SelfCharge] on self; if this unit lost 10+ [SelfCharge], gain Clash Power +5\n[DefeatDuel] This Attack Skill deals 0 damage
   PL:
673. [Umiejętność wroga [962107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność wroga [962107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 메인 대상에게 [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Vulnerable] on the main target
   PL:
675. [Umiejętność wroga [962107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność wroga [962107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ElectricStorage] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ElectricStorage]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ElectricStorage] = 축전 / Capacitor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [ElectricStorage]
   PL:
677. [Umiejętność wroga [962107] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 메인 대상에게 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Paralysis] on the main target
   PL:
678. [Umiejętność wroga [962107] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 대상이 [ElectricStorage] 상태일 때, 이 코인 최종 피해량의 40%만큼 고정 피해
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962107].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ElectricStorage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ElectricStorage] = 축전 / Capacitor
   EN: [OnSucceedAttack] If target has [ElectricStorage], deal 40% of this Coin's final damage as fixed damage
   PL:
679. [Umiejętność wroga [962108] (ulepszenie 1) — nazwa] 똬리틀기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962108].levelList[level=1].name
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [962108] (ulepszenie 1) — opis] [TurnStartBattle] 머리 부위 현재 체력만큼 보호막 얻음\n[EndBattle] 머리 부위에 보호막이 있으면, 다음 턴에 [SelfCharge] 10 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962108].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [TurnStartBattle], [EndBattle], [SelfCharge]
   znaczenie tagów: [TurnStartBattle] = [턴 시작 시] / [Turn Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [SelfCharge] = 자가 충전 / Self-charge
   EN: [TurnStartBattle] The Head Part gains Shield by its current HP\n[EndBattle] If the Head Part has Shield, gain 10 [SelfCharge] next turn
   PL:
681. [Umiejętność wroga [962109] (ulepszenie 1) — nazwa] 꿈틀거리는 머리
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962109].levelList[level=1].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [962109] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n대상에게 [Paralysis]가 있다면 피해량 +50%\n대상이 수비 스킬을 장착했으면, 피해량 -100%\n[SelfCharge] 1당 기본 위력 +1\n[WhenUse] [SelfCharge] 1 소모\n[WhenUse] 대상이 수비 스킬을 장착했으면, [SelfCharge] 2 소모\n[DefeatDuel] [SelfCharge] 2 추가 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962109].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Paralysis], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [Paralysis] = 마비 / Paralyze; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets that have the lowest HP\nIf target has [Paralysis], deal +50% damage\nIf target has used a Defense Skill, deal -100% damage\nBase Power +1 for every [SelfCharge]\n[WhenUse] Lose 1 [SelfCharge]\n[WhenUse] If target has equipped Defense Skills, lose 2 [SelfCharge]\n[DefeatDuel] Lose 2 additional [SelfCharge]
   PL:
683. [Umiejętność wroga [962109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [962109] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962109].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność wroga [962110] (ulepszenie 1) — nazwa] 꿈틀거리는 꼬리
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962110].levelList[level=1].name
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność wroga [962110] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n대상에게 [Paralysis]가 있다면 피해량 +50%\n대상이 수비 스킬을 장착했으면, 피해량 -100%\n[SelfCharge] 1당 기본 위력 +1\n[WhenUse] [SelfCharge] 1 소모\n[WhenUse] 대상이 수비 스킬을 장착했으면, [SelfCharge] 2 소모\n[DefeatDuel] [SelfCharge] 2 추가 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962110].levelList[level=1].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Umiejętność wroga [962110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
688. [Umiejętność wroga [962110] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962110].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Umiejętność wroga [962110] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=962110].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [960101] (ulepszenie 1) — nazwa] 취하고 싶나?
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960101].levelList[level=1].name
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Umiejętność wroga [960101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +2 [Vibration] Count
   PL:
692. [Umiejętność wroga [960102] (ulepszenie 1) — nazwa] 나눠 마시자!
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960102].levelList[level=1].name
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Umiejętność wroga [960102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [960102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 본체와 이 스킬을 사용한 부위의 체력 5% 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] The Core and the Part that used this Skill heal 5% HP
   PL:
695. [Umiejętność wroga [960103] (ulepszenie 1) — nazwa] 남은건 이것 뿐이네!
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960103].levelList[level=1].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Umiejętność wroga [960103] (ulepszenie 1) — opis] [Vibration]을 가진 대상 우선 공격
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Prioritize targets that have [Vibration]
   PL:
697. [Umiejętność wroga [960103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL:
698. [Umiejętność wroga [960103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수만큼 [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] equal to [Vibration] Count on target
   PL:
699. [Umiejętność wroga [960103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 전부 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume all [Vibration] Count on target
   PL:
700. [Umiejętność wroga [960104] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960104].levelList[level=1].name
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [960104] (ulepszenie 1) — opis] [TipsinessRail]가 없는 대상 우선 공격\n대상에게 [TipsinessRail]가 없다면, 합 위력 +8\n[WhenUse] 대상이 [TipsinessRail]가 없다면, 피해량 +200%\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960104].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [TipsinessRail], [WhenUse], [DefeatDuel]
   znaczenie tagów: [TipsinessRail] = 취기 / Tipsy; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets that do not have [TipsinessRail]\nIf target does not have [TipsinessRail], Clash Power +8\n[WhenUse] If target does not have [TipsinessRail], deal +200% damage\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
702. [Umiejętność wroga [960104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [960104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [TipsinessRail]가 5 이상이라면, 가하는 피해가 0이 됨.
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TipsinessRail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TipsinessRail] = 취기 / Tipsy
   EN: [OnSucceedAttack] If target has 5+ [TipsinessRail], deal 0 damage
   PL:
704. [Umiejętność wroga [960104] (ulepszenie 1) — moneta 1, efekt 3 — opis] 신사 요정이 다음 턴에 흐트러짐 상태가 됨
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960104].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   EN: Fairy Gentleman becomes Staggered next turn
   PL:
705. [Umiejętność wroga [960104] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [TipsinessRail]를 전부 소모 시킴
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960104].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TipsinessRail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TipsinessRail] = 취기 / Tipsy
   EN: [OnSucceedAttack] Remove all [TipsinessRail] on target
   PL:
706. [Umiejętność wroga [960105] (ulepszenie 1) — nazwa] 이 요정주가 좋나?
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960105].levelList[level=1].name
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność wroga [960105] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Binding] 3 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind
   EN: [WhenUse] Gain 3 [Binding] next turn
   PL:
708. [Umiejętność wroga [960106] (ulepszenie 1) — nazwa] 한 잔 할텐가?
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960106].levelList[level=1].name
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [960106] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 굴절된 요정주 소환\n[DefeatDuel] 굴절된 요정주 체력 50%로 소환됨\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960106].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Summon Refracted Fairy Wine next turn\n[DefeatDuel] Refracted Fairy Wine summoned at 50% HP\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
710. [Umiejętność wroga [960106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [960106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Vibration]
   PL:
712. [Umiejętność wroga [960106] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960106].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]
   PL:
713. [Umiejętność wroga [960201] (ulepszenie 1) — nazwa] 달콤한 요정주
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960201].levelList[level=1].name
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność wroga [960301] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960301].levelList[level=1].name
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [960301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 2이상일 때, [Laceration] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 2+ [Laceration] Count, inflict 5 [Laceration]
   PL:
716. [Umiejętność wroga [960301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 2이상일 때, [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] If target has 2+ [Laceration] Count, inflict 1 [Paralysis]
   PL:
717. [Umiejętność wroga [960301] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960301].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +4 [Laceration] Count
   PL:
718. [Umiejętność wroga [960302] (ulepszenie 1) — nazwa] 옭아매인 상처
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960302].levelList[level=1].name
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [960302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [960303] (ulepszenie 1) — nazwa] 묻어오는 살점
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960303].levelList[level=1].name
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [960303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [960303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 [Laceration]을 가지고 있다면, 본체와 이 스킬을 사용한 부위 체력 25 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], the Core and the Part that used this Skill heal 25 HP
   PL:
723. [Umiejętność wroga [960303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 2이상일 때 [Laceration] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 2+ [Laceration] Count, inflict 5 [Laceration]
   PL:
724. [Umiejętność wroga [960303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 [Laceration]을 가지고 있다면, 본체와 이 스킬을 사용한 부위 체력 25 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [960304] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960304].levelList[level=1].name
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność wroga [960304] (ulepszenie 1) — opis] [Laceration] 위력이 가장 높은 대상 우선 공격\n[StartBattle] 다음 턴에 굴절된 클로버 생성\n[DefeatDuel] 굴절된 클로버의 체력이 50%인 상태로 생성됨\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960304].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [StartBattle], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes target that has the most [Laceration] Potency\n[StartBattle] Summon Refracted Clover next turn\n[DefeatDuel] Refracted Clover summoned at 50% HP\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
727. [Umiejętność wroga [960304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [960304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 피해량 +(5 x 대상의 [Laceration] 위력 x [Laceration] 횟수)% (최대 200%)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Deal +(5 x [Laceration] on target x [Laceration] Count on target)% damage (max 200%)
   PL:
729. [Umiejętność wroga [960304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 전부 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Consume all [Laceration] on target
   PL:
730. [Umiejętność wroga [960305] (ulepszenie 1) — nazwa] 소화
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960305].levelList[level=1].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [960305] (ulepszenie 1) — opis] [StartBattle] 모든 부위 [Protection] 3 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] All Parts gain 3 [Protection]
   PL:
732. [Umiejętność wroga [960305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1당, 자신의 전체 체력의 1%만큼 본체와 이 스킬을 사용한 부위 체력 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal the Core and the Part that used this Skill by 1% of this unit's max HP for every [Laceration] on target
   PL:
733. [Umiejętność wroga [960305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수 1 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Consume 1 [Laceration] Count on target
   PL:
734. [Umiejętność wroga [960501] (ulepszenie 1) — nazwa] 차원 베기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960501].levelList[level=1].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [960501] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +3 [Charge] Count\n[DefeatDuel] Consume 2 [Charge] Count
   PL:
736. [Umiejętność wroga [960501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [960502] (ulepszenie 1) — nazwa] 연속 차원 베기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960502].levelList[level=1].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność wroga [960502] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960502].levelList[level=1].desc
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność wroga [960502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 3 [DimensionRift]
   PL:
740. [Umiejętność wroga [960502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 739 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Umiejętność wroga [960503] (ulepszenie 1) — nazwa] 부산물 뱉기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960503].levelList[level=1].name
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [960503] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 4 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +4 [Charge] Count\n[DefeatDuel] Consume 2 [Charge] Count
   PL:
743. [Umiejętność wroga [960503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność wroga [960504] (ulepszenie 1) — nazwa] 공간 절단
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].name
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [960504] (ulepszenie 1) — opis] [Charge] 횟수가 10 이상이면, [Charge] 횟수 10을 소모하고 합 위력 +5, 피해량 +100%\n[Charge] 횟수가 10 미만이면, 본체 체력 100을 소모함. 피해량 +80% (이 효과로 자신의 체력이 1 미만으로 감소하지 않음)\n[DefeatDuel] 아래 효과 적용\n- [Paralysis] 2 얻음\n- 피해량이 80%만큼 감소함\n- 이 스킬로 대상이 흐트러지지 않음\n- 대상의 [Burst] 효과를 발동시키지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [DefeatDuel], [Paralysis], [Burst]
   znaczenie tagów: [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [Burst] = 파열 / Rupture
   EN: At 10+ [Charge] Count, consume 10 [Charge] Count to gain Clash Power +5 and deal +100% damage\nAt less than 10 [Charge] Count, consume 100 Core HP. Deal +80% damage (This unit's HP cannot drop below 1 due to this Skill's effect)\n\n[DefeatDuel] Gain the following effects:\n- Gain 2 [Paralysis]\n- Deal -80% damage\n- This Skill cannot Stagger the target\n- Does not activate [Burst] on target
   PL:
746. [Umiejętność wroga [960504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność wroga [960504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Charge]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackHead] Gain +2 [Charge] Count
   PL:
748. [Umiejętność wroga [960504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [DimensionRift]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [DimensionRift]
   PL:
749. [Umiejętność wroga [960504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Umiejętność wroga [960504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 747 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [960504] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960504].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność wroga [960505] (ulepszenie 1) — nazwa] 준비된 반격
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960505].levelList[level=1].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność wroga [960505] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +1 [Charge] Count
   PL:
754. [Umiejętność wroga [960505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Umiejętność wroga [960505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Umiejętność wroga [960506] (ulepszenie 1) — nazwa] 부산물 토하기
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960506].levelList[level=1].name
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Umiejętność wroga [960506] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 [DimensionRift]이 있다면, 피해량 +10%\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960506].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DimensionRift], [DefeatDuel], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DimensionRift] = 차원 균열 / Dimensional Rift; [DefeatDuel] = [합 패배] / [Clash Lose]; [Charge] = 충전 / Charge
   EN: [WhenUse] If the main target has [DimensionRift], deal +10% damage\n[DefeatDuel] Consume 2 [Charge] Count
   PL:
758. [Umiejętność wroga [960506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Umiejętność wroga [960506] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [DimensionRift] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [DimensionRift]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [DimensionRift]
   PL:
760. [Umiejętność wroga [960507] (ulepszenie 1) — nazwa] 고속 공간 절단
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960507].levelList[level=1].name
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Umiejętność wroga [960507] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[DefeatDuel]\n- [Reduction] 2, [Paralysis] 1 얻음\n- 피해량이 90%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n가장 많이 가지고 있는 포탈 효과만큼 합 위력 증가[TabExplain]\n자신이 가지고 있는 포탈 효과만큼 피해량 +10%
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960507].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [Reduction], [Paralysis], [TabExplain]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Reduction] = 공격 위력 감소 / Attack Power Down; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered before using this Skill\n[DefeatDuel]\n- Gain 2 [Reduction] and 1 [Paralysis]\n- Deal -90% damage and damage dealt by this Skill cannot Stagger the target\nGain Clash Power +1 for every most-owned Dimension effect on self\nDeal +10% damage for every Dimension effect on self
   PL:
762. [Umiejętność wroga [960507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność wroga [960507] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960507].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Burst]
   PL:
764. [Umiejętność wroga [960508] (ulepszenie 1) — nazwa] 기회 포착
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960508].levelList[level=1].name
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność wroga [960508] (ulepszenie 1) — opis] [WhenUse] 대상에게 [DimensionRift]이 있다면, 피해량 +20%
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960508].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DimensionRift]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [WhenUse] If target has [DimensionRift], deal +20% damage
   PL:
766. [Umiejętność wroga [960508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 739 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Umiejętność wroga [960509] (ulepszenie 1) — nazwa] 틈새 공격
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960509].levelList[level=1].name
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Umiejętność wroga [960509] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 [DimensionRift]이 있다면, 피해량 +10%
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960509].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DimensionRift]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [WhenUse] If the main target has [DimensionRift], deal +10% damage
   PL:
769. [Umiejętność wroga [960509] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960509].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 739 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [960601] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960601].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Umiejętność wroga [960601] (ulepszenie 1) — opis] 이 차원이 남아있다면, 피해량이 10% 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960601].levelList[level=1].desc
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Umiejętność wroga [960701] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960701].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność wroga [960701] (ulepszenie 1) — opis] 이 차원이 남아있다면, 본체 최대 체력이 20% 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960701].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, Core max HP +20%
   PL:
774. [Umiejętność wroga [960801] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960801].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność wroga [960801] (ulepszenie 1) — opis] 이 차원이 남아있다면, 최소 속도와 최대 속도 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960801].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, Min & Max Speed +1
   PL:
776. [Umiejętność wroga [960901] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960901].levelList[level=1].name
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Umiejętność wroga [960901] (ulepszenie 1) — opis] 이 차원이 남아있다면, 코인 위력 +1
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=960901].levelList[level=1].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [961001] (ulepszenie 1) — nazwa] 영겁의 정원으로
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961001].levelList[level=1].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Umiejętność wroga [961001] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 전장에 있는 모든 수감자에게 [PrepareSinRose]을 부여\n[WhenUse] 자신의 본체 체력이 40% 미만이면, 다음 턴에 장미가 [EnhanceRose]로 생성됨
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961001].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [PrepareSinRose], [EnhanceRose]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [PrepareSinRose] = 면류관 / Crown of Thorns; [EnhanceRose] = 강화 상태 / Power-up State
   EN: [CantDuel]\n[WhenUse] Apply [PrepareSinRose] on all Sinners on the field\n[WhenUse] If Core has less than 40% HP, Roses will spawn in [EnhanceRose] next turn
   PL:
780. [Umiejętność wroga [961002] (ulepszenie 1) — nazwa] 정지
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].name
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [961002] (ulepszenie 1) — opis] 이번 전투에서 사망한 수감자 1명당, 최종 위력 +1\n[WhenUse] 대상의 부정적인 효과 2개당, 최종 위력 +1 (최대 3)\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 for every Sinner defeated in this Encounter\n[WhenUse] Final Power +1 for every 2 types of negative effects on target (max 3)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
782. [Umiejętność wroga [961002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [961002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2, [Vibration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Combustion] and 2 [Vibration]
   PL:
784. [Umiejętność wroga [961002] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL:
785. [Umiejętność wroga [961002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [961002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2, [Vibration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 783 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [961002] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961002].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [961003] (ulepszenie 1) — nazwa] 구속
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].name
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność wroga [961003] (ulepszenie 1) — opis] 이번 전투에서 사망한 수감자 1명당, 최종 위력 +1\n[WhenUse] 대상의 부정적인 효과 2개당, 최종 위력 +1 (최대 3)\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].desc
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [961003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [961003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [961003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [961003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3, [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and 3 [Burst]
   PL:
794. [Umiejętność wroga [961003] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 체력이 가장 낮은 장미의 체력을 최대 체력의 10%만큼 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961003].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal 10% HP for the Rose that has the lowest HP
   PL:
795. [Umiejętność wroga [961004] (ulepszenie 1) — nazwa] 끝없는 피어남
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [961004] (ulepszenie 1) — opis] [PrepareSinRose]이 없는 대상 우선 공격\n이번 전투에서 사망한 수감자 1명당, 최종 위력 +1\n[WhenUse] 대상의 부정적인 효과 2개당, 최종 위력 +1 (최대 3)\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [PrepareSinRose], [WhenUse], [DefeatDuel]
   znaczenie tagów: [PrepareSinRose] = 면류관 / Crown of Thorns; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets that do not have [PrepareSinRose]\nFinal Power +1 for every Sinner defeated in this Encounter\n[WhenUse] Final Power +1 for every 2 types of negative effects on target (max 3)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
797. [Umiejętność wroga [961004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [961004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 1, [Binding] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Paralysis] and 1 [Binding] next turn
   PL:
799. [Umiejętność wroga [961004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [961004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [PrepareSinRose] 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [PrepareSinRose]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [PrepareSinRose] = 면류관 / Crown of Thorns
   EN: [UnBrokenCoinOnSucceedAttack] Inflict [PrepareSinRose]
   PL:
801. [Umiejętność wroga [961004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [961004] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 본체의 체력을 본체의 최대 체력의 5%만큼 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961004].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal the Core by 5% of its max HP
   PL:
803. [Umiejętność wroga [961005] (ulepszenie 1) — nazwa] 단절의 벽
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961005].levelList[level=1].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [961005] (ulepszenie 1) — opis] 생존한 장미 하나당, 기본 위력 +3\n[EndBattle] 생존한 장미가 없으면, 다음 턴에 [Vulnerable] 2를 얻음
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961005].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle], [Vulnerable]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [Vulnerable] = 취약 / Fragile
   EN: Base Power +3 for every surviving Rose\n[EndBattle] If there are no surviving Roses, gain 2 [Vulnerable] next turn
   PL:
805. [Umiejętność wroga [961005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 본체의 체력을 본체의 최대 체력의 5%만큼 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal the Core by 5% of its max HP
   PL:
806. [Umiejętność wroga [961006] (ulepszenie 1) — nazwa] 영원을 바라며
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961006].levelList[level=1].name
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [961006] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 무작위 장미 하나에게 [Enhancement] 1 부여\n보호막이 있는 동안 피격 시 공격자에게 [Sinking] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961006].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Enhancement], [Sinking]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Sinking] = 침잠 / Sinking
   EN: [StartBattle] Apply 1 [Enhancement] to 1 random Rose next turn\nWhen hit while this unit has Shield, inflict 1 [Sinking] on the attacker
   PL:
808. [Umiejętność wroga [961007] (ulepszenie 1) — nazwa] 함께 이 곳에서
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961007].levelList[level=1].name
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [961007] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 무작위 장미 하나에게 [Endurance] 1 부여\n보호막이 있는 동안 피격 시 공격자에게 [Sinking] 1 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961007].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Endurance], [Sinking]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Endurance] = 수비 위력 증가 / Defense Power Up; [Sinking] = 침잠 / Sinking
   EN: [StartBattle] Apply 1 [Endurance] to 1 random Rose next turn\nWhen hit while this unit has Shield, inflict 1 [Sinking] on the attacker
   PL:
810. [Umiejętność wroga [961101] (ulepszenie 1) — nazwa] 타오르는 분노
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961101].levelList[level=1].name
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [961101] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)
   PL:
812. [Umiejętność wroga [961101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
813. [Umiejętność wroga [961101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [961101] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [961102] (ulepszenie 1) — nazwa] 흩날리는 분노
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961102].levelList[level=1].name
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność wroga [961102] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961102].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [961102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
818. [Umiejętność wroga [961102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 817 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [961201] (ulepszenie 1) — nazwa] 다가오는 색욕
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].name
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [961201] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Umiejętność wroga [961201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [961201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [961201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [961201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [961201] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [961201] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961201].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [961202] (ulepszenie 1) — nazwa] 파고드는 색욕
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961202].levelList[level=1].name
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [961202] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961202].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [961202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
830. [Umiejętność wroga [961202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność wroga [961202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność wroga [961301] (ulepszenie 1) — nazwa] 굳어진 나태
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961301].levelList[level=1].name
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [961301] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961301].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [961301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 8 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 8 [Vibration]
   PL:
835. [Umiejętność wroga [961302] (ulepszenie 1) — nazwa] 완고한 나태
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961302].levelList[level=1].name
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [961302] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961302].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [961302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 8 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 834 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [961302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackHead] Trigger [VibrationExplosion]
   PL:
839. [Umiejętność wroga [961303] (ulepszenie 1) — nazwa] 잠든 나태
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961303].levelList[level=1].name
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [961303] (ulepszenie 1) — opis] 보호막이 있는 동안 피격 시 자신과 대상에게 [VibrationExplosion]\n[WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961303].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [WhenUse]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [WhenUse] = [사용시] / [On Use]
   EN: When hit while this unit has Shield, trigger [VibrationExplosion] on self and target\n[WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)
   PL:
841. [Umiejętność wroga [961401] (ulepszenie 1) — nazwa] 게걸스런 탐식
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961401].levelList[level=1].name
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [961401] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961401].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [961401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [961402] (ulepszenie 1) — nazwa] 무성한 탐식
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961402].levelList[level=1].name
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [961402] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961402].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [961402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +4 [Burst] Count
   PL:
847. [Umiejętność wroga [961403] (ulepszenie 1) — nazwa] 쉼 없는 탐식
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961403].levelList[level=1].name
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [961403] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961403].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność wroga [961403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 25% of HP damage dealt
   PL:
850. [Umiejętność wroga [961403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 체력 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność wroga [961403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 체력 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Umiejętność wroga [961403] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 체력 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961403].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Umiejętność wroga [961501] (ulepszenie 1) — nazwa] 넘치는 우울
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961501].levelList[level=1].name
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność wroga [961501] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961501].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność wroga [961501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 6 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 6 [Sinking]
   PL:
856. [Umiejętność wroga [961502] (ulepszenie 1) — nazwa] 차오르는 우울
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961502].levelList[level=1].name
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność wroga [961502] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961502].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Umiejętność wroga [961502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
859. [Umiejętność wroga [961502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 858 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność wroga [961503] (ulepszenie 1) — nazwa] 감싼 우울
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961503].levelList[level=1].name
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [961503] (ulepszenie 1) — opis] 보호막이 있는 동안 피격 시 자신과 대상에게 [Sinking] 횟수 1 증가\n[WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961503].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [WhenUse]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: When hit while this unit has Shield, gain +1 [Sinking] Count and inflict +1 [Sinking] Count on target\n[WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)
   PL:
862. [Umiejętność wroga [961601] (ulepszenie 1) — nazwa] 내뱉은 오만
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961601].levelList[level=1].name
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność wroga [961601] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)\n[WhenUse] 모든 아군에게 [Breath] 3 부여
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961601].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)\n[WhenUse] Apply 3 [Breath] on all allies
   PL:
864. [Umiejętność wroga [961602] (ulepszenie 1) — nazwa] 치켜든 오만
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961602].levelList[level=1].name
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność wroga [961602] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)\n[WhenUse] 모든 아군의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961602].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)\n[WhenUse] Apply +2 [Breath] Count on all allies
   PL:
866. [Umiejętność wroga [961602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
867. [Umiejętność wroga [961602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 866 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Umiejętność wroga [961603] (ulepszenie 1) — nazwa] 날 선 오만
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961603].levelList[level=1].name
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Umiejętność wroga [961603] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961603].levelList[level=1].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [961701] (ulepszenie 1) — nazwa] 쌓이는 질투
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961701].levelList[level=1].name
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność wroga [961701] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)\n[WhenUse] 자신의 [Charge] 횟수 3 증가\n[DefeatDuel] 자신의 [Charge] 횟수 3 감소
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961701].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)\n[WhenUse] Gain +3 [Charge] Count\n[DefeatDuel] Lose 3 [Charge] Count
   PL:
872. [Umiejętność wroga [961701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count
   PL:
873. [Umiejętność wroga [961701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 872 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Umiejętność wroga [961702] (ulepszenie 1) — nazwa] 뻗어가는 질투
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961702].levelList[level=1].name
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Umiejętność wroga [961702] (ulepszenie 1) — opis] [WhenUse] 자신과 다른 죄악 속성의 장미 하나당, 기본 위력 +1 (최대 6)\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +4
   źródło: Skills_Abnormality_Refraction2_bokgak.json :: dataList[id=961702].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Base Power +1 for every Rose that has a different Affinity from this unit (max 6)\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +4
   PL:

## [refraction2bokgak] Pasywka wroga: Passives_Abnormality_Refraction2BokGak
- plik gry: `Passives_Abnormality_Refraction2BokGak.json`

876. [[refraction2bokgak] Pasywka wroga [962201] — nazwa] 부서진 수단
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962201].name
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [[refraction2bokgak] Pasywka wroga [962201] — opis] 팔 부위 파괴 시, 매 턴마다 팔 부위에 [Reduction] 1 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: When the Arm is broken, the Arm gains 1 [Reduction] every turn
   PL:
878. [[refraction2bokgak] Pasywka wroga [962202] — nazwa] 굴절 침잠 부과
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962202].name
   (powtórzenie elementu 353 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [[refraction2bokgak] Pasywka wroga [962202] — opis] [Sinking]을 얻을 때 위력과 횟수를 1 추가로 얻음 (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962202].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Sinking], [TabExplain]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When gaining [Sinking], gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
880. [[refraction2bokgak] Pasywka wroga [962301] — nazwa] 돌아오는 과거
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962301].name
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [[refraction2bokgak] Pasywka wroga [962301] — opis] [AccumulatedPast]가 50 이상이면, 본체 체력이 80% 이하일 때 턴 종료 시 [AccumulatedPast]를 50 소모하여 본체 체력을 200 회복함
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962301].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [AccumulatedPast]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past
   EN: At 50+ [AccumulatedPast], and if Core HP is at 80%-, the Core heals 200 HP by consuming 50 [AccumulatedPast] at Turn End
   PL:
882. [[refraction2bokgak] Pasywka wroga [962302] — nazwa] 소실된 과거
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962302].name
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [[refraction2bokgak] Pasywka wroga [962302] — opis] 몸통 부위 파괴 시, [AccumulatedPast] 전부 소모\n몸통 부위 파괴 시, 몸통 부위에 아래 효과가 이번 전투동안 적용됨\n- 이번 턴부터 죄악 내성이 0.5가 됨\n- 다음 턴부터 물리 내성이 0.5가 됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962302].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPast]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past
   EN: When the Body is broken, consume all [AccumulatedPast]\nWhen the Body is broken, apply the following effects on the Body for this Encounter:\n- Affinity Resist. becomes 0.5 starting from this turn\n- Attack Type Resist. becomes 0.5 starting from the next turn
   PL:
884. [[refraction2bokgak] Pasywka wroga [962303] — nazwa] 파괴된 배연 기관
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962303].name
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [[refraction2bokgak] Pasywka wroga [962303] — opis] 증기총 부위 파괴 시, 모든 부위의 [Breath] 전부 소모\n증기총 부위가 파괴된 이후, [Breath]을 얻을 때마다 [Vulnerable]을 1 얻음\n증기총 부위가 파괴된 이후, 매 공격 스킬 사용 시 [Breath] 1을 잃음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962303].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Vulnerable]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vulnerable] = 취약 / Fragile
   EN: When Steam Blaster is broken, completely lose [Breath] on all Parts\nOnce Steam Blaster is broken, every time this unit gains [Breath], gain 1 [Vulnerable] for every [Breath] gained\nOnce Steam Blaster is broken, lose 1 [Breath] On Use of an Attack Skill
   PL:
886. [[refraction2bokgak] Pasywka wroga [962304] — nazwa] 굴절된 화상과 출혈
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962304].name
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [[refraction2bokgak] Pasywka wroga [962304] — opis] [Combustion]과 [Laceration]의 위력이 30까지만 누적됨\n[Combustion]과 [Laceration]의 횟수가 5까지만 누적됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962304].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [Combustion] and [Laceration] Potency max out at 30\n[Combustion] and [Laceration] Count max out at 5
   PL:
888. [[refraction2bokgak] Pasywka wroga [962305] — nazwa] 굴절 침잠 부과
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962305].name
   (powtórzenie elementu 353 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [[refraction2bokgak] Pasywka wroga [962305] — opis] [Sinking]을 얻을 때 위력과 횟수를 1 추가로 얻음 (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962305].desc
   (powtórzenie elementu 879 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [[refraction2bokgak] Pasywka wroga [962306] — nazwa] 새어나오는 증기
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962306].name
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [[refraction2bokgak] Pasywka wroga [962306] — opis] 증기총 부위 피격 시, [Breath]과 [Breath] 횟수 1 감소
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962306].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When Steam Blaster is hit, lose 1 [Breath] and 1 [Breath] Count
   PL:
892. [[refraction2bokgak] Pasywka wroga [962307] — nazwa] 겹쳐지는 과거
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962307].name
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [[refraction2bokgak] Pasywka wroga [962307] — opis] 매 턴마다 [AccumulatedPast] 80당 [Enhancement] 1 얻음\n[AccumulatedPast]가 80을 넘었다면, 슬롯 1개 추가
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962307].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPast], [Enhancement]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Gain 1 [Enhancement] for every 80 [AccumulatedPast] every turn\nAt 80+ [AccumulatedPast], gain +1 Slot
   PL:
894. [[refraction2bokgak] Pasywka wroga [962308] — nazwa] 메트로놈
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962308].name
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [[refraction2bokgak] Pasywka wroga [962308] — opis] [AccumulatedPast]가 홀수이면 [Vulnerable]과 [AttackDmgUp]를 3 얻음\n짝수이면, [Protection]와 [AttackDmgDown]를 3 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962308].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPast], [Vulnerable], [AttackDmgUp], [Protection], [AttackDmgDown]
   znaczenie tagów: [AccumulatedPast] = 축적된 과거 / Accumulated Past; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up; [Protection] = 보호 / Protection; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: If [AccumulatedPast] is an odd number, gain 3 [Vulnerable] and [AttackDmgUp]\nIf it is an even number, gain 3 [Protection] and [AttackDmgDown]
   PL:
896. [[refraction2bokgak] Pasywka wroga [962401] — nazwa] 부서진 우산
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962401].name
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [[refraction2bokgak] Pasywka wroga [962401] — opis] 몸통 부위 파괴 시, 매 턴마다 몸통 부위 [AttackDmgDown] 1 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgDown]
   znaczenie tagów: [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: When the Body is broken, the Body gains 1 [AttackDmgDown] every turn
   PL:
898. [[refraction2bokgak] Pasywka wroga [962402] — nazwa] 다해진 우산
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962402].name
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [[refraction2bokgak] Pasywka wroga [962402] — opis] 머리 부위 파괴 시, 매 턴마다 [AttackDmgDown] 1 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962402].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgDown]
   znaczenie tagów: [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: When the Head is broken, gain 1 [AttackDmgDown] every turn
   PL:
900. [[refraction2bokgak] Pasywka wroga [962403] — nazwa] 마지막 발버둥
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962403].name
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [[refraction2bokgak] Pasywka wroga [962403] — opis] 체력이 전체 체력의 15%만큼 남았다면, \n- 매 턴마다 [Binding] 10, [Reduction] 1 얻음\n- 새로 소환된 낡은 우산 체력 30% 증가\n- 매 턴마다 ‘무언가를 찾는 울음소리’ 또는 ‘애원하는 울음소리’ 사용
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962403].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [Reduction]
   znaczenie tagów: [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: At 15% HP, trigger the following effects:\n- Gain 10 [Binding] and 1 [Reduction] every turn\n- Newly spawned Old Umbrellas have 30% more HP\n- Use "Cries Seeking Something" or "Pleading Cries" every turn
   PL:
902. [[refraction2bokgak] Pasywka wroga [962404] — nazwa] 허영된 마음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962404].name
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [[refraction2bokgak] Pasywka wroga [962404] — opis] 1턴 시작 시 [WaveFoxUmbrella]을 2 얻음 (최대 6)\n[WaveFoxUmbrella]을 얻을 때 순환 횟수만큼 추가로 얻음\n보유 중인 [WaveFoxUmbrella]만큼 [Protection]를 얻음\n기다림 스킬이 슬롯에 있다면, 낡은 우산을 [WaveFoxUmbrella]만큼 소환
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962404].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [WaveFoxUmbrella], [Protection]
   znaczenie tagów: [WaveFoxUmbrella] = 보호 우산 / Protection Umbrella; [Protection] = 보호 / Protection
   EN: Gain 2 [WaveFoxUmbrella] at the start of Turn 1 (max 6)\nWhen gaining [WaveFoxUmbrella], gain additional [WaveFoxUmbrella] equal to the number of "Cycle Counts"\nGain [Protection] equal to [WaveFoxUmbrella] on self\nIf "Waiting" Skill is Slotted, spawn Old Umbrella equal to [WaveFoxUmbrella]
   PL:
904. [[refraction2bokgak] Pasywka wroga [962405] — nazwa] 굴절된 파열과 침잠
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962405].name
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [[refraction2bokgak] Pasywka wroga [962405] — opis] [Burst]과 [Sinking]의 위력이 30까지만 누적됨\n[Burst]과 [Sinking]의 횟수가 5까지만 누적됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962405].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Sinking]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [Burst] and [Sinking] Potency max out at 30\n[Burst] and [Sinking] Count max out at 5
   PL:
906. [[refraction2bokgak] Pasywka wroga [962406] — nazwa] 굴절 출혈 부과
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962406].name
   (powtórzenie elementu 327 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [[refraction2bokgak] Pasywka wroga [962406] — opis] [Laceration]을 얻을 때 위력과 횟수를 1 추가로 얻음 (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962406].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Laceration], [TabExplain]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When gaining [Laceration], gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
908. [[refraction2bokgak] Pasywka wroga [962501] — nazwa] 버려진 낡은 우산
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962501].name
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [[refraction2bokgak] Pasywka wroga [962501] — opis] 이 유닛이 인격의 스킬 종료시 사망했으면, 해당 인격이 정신력 10 회복, 다음 턴에 [Agility] 2 얻음\n\n이 유닛 사망 시, 떠돌이 여우에게 모든 부위에 [ShardOfUmbrella] 1과 [Binding] 2 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962501].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [ShardOfUmbrella], [Binding]
   znaczenie tagów: [Agility] = 신속 / Haste; [ShardOfUmbrella] = 우산 파편 / Umbrella Splinters; [Binding] = 속박 / Bind
   EN: When this unit is defeated at Skill End of an Identity, the said Identity heals 10 SP and gains 2 [Agility] next turn \n\nWhen this unit is defeated, inflict 1 [ShardOfUmbrella] and 2 [Binding] on all Drifting Fox Parts
   PL:
910. [[refraction2bokgak] Pasywka wroga [961801] — nazwa] 황금 시간
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961801].name
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [[refraction2bokgak] Pasywka wroga [961801] — opis] 턴 종료 시 체력이 6% ~ 24% 사이로 남았을 때, 전체 체력의 80%만큼 본체와 부위 체력 즉시 회복. 흐트러짐 상태 해제 (전투당 1회)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961801].desc
   limit: do 200 znaków
   EN: Turn End: If the HP is between 6% and 24%, the Core and Parts instantly heal up to 80% of max HP, and this unit recovers from Stagger (once per Encounter)
   PL:
912. [[refraction2bokgak] Pasywka wroga [961802] — nazwa] 시간 역행 반동
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961802].name
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
