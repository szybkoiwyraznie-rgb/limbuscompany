# Paczka AI P72 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 8/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P72_3c_przeciwnicy_i_anomalie_cz08.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P72_3c_przeciwnicy_i_anomalie_cz08.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c7p3] Pasywka wroga: Passives_Abnormality-a1c7p3
- plik gry: `Passives_Abnormality-a1c7p3.json`

1. [[a1c7p3] Pasywka wroga [837601] — podsumowanie] 공격 직전 대상에게 [Burst]이 있으면, 20%확률로 [Burst] 횟수 1 증가
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837601].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If the target has [Burst] immediately before attack, 20% chance to inflict +1 [Burst] Count
   PL:
2. [[a1c7p3] Pasywka wroga [837602] — nazwa] 덩굴 얽힌 말
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837602].name
   limit: do 40 znaków
   EN: Bramble Steed
   PL:
3. [[a1c7p3] Pasywka wroga [837602] — opis] 생성된 가시 올가미만큼 속도가 증가함.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837602].desc
   limit: do 120 znaków
   EN: Gain Speed equal to the generated 'Barbed Lasso' Unit on the field
   PL:
4. [[a1c7p3] Pasywka wroga [837603] — nazwa] 서로 뒤엉키는 가시 덩굴
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837603].name
   limit: do 40 znaków
   EN: Interlocking Brambles
   PL:
5. [[a1c7p3] Pasywka wroga [837603] — opis] 최대 체력 40%이하가 되면, 패턴 변경됨.\n매 턴마다 모든 적에게 적의 속도만큼 [Burst]을 부여함\n부여하는 [ThornNoose]가 2가 됨\n매 턴이 지날 때마다 [AttackUp], [DefenseDown] 2씩 얻음 (최대 12)
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837603].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [ThornNoose], [AttackUp], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [ThornNoose] = 가시 올가미 / Barbed Lasso; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: At 40%- HP, gain a new pattern\nEvery turn, inflict [Burst] equal to each enemy's Speed against each enemy\nInflict 2 [ThornNoose] instead\nGain 2 [AttackUp] and [DefenseDown] with every passing turn (max 12)
   PL:
6. [[a1c7p3] Pasywka wroga [838006] — nazwa] 꿈결
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838006].name
   limit: do 40 znaków
   EN: In Dreams
   PL:
7. [[a1c7p3] Pasywka wroga [838006] — opis] 전투 시작 시, [Dreamy] 얻음.\n전투 시작 시, 전장에 흩뿌려진 잠재된 피가 드러나 [BloodDinner] 400 얻음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838006].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Dreamy], [BloodDinner]
   znaczenie tagów: [Dreamy] = 꿈결속 망설임 / Dreamy Hesitation; [BloodDinner] = 혈찬 / Bloodfeast
   EN: Encounter Start: gain [Dreamy].\nEncounter Start: the sleeping blood drenching the battlefield will surface, increasing [BloodDinner] by 400.
   PL:
8. [[a1c7p3] Pasywka wroga [838001] — nazwa] 귀기울여 듣게되어버린 이야기와 두근거림
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838001].name
   limit: do 60 znaków
   EN: The Enthralling Tales, the Beating Passion
   PL:
9. [[a1c7p3] Pasywka wroga [838001] — opis] 80%, 60%, 40%가 되었을 때, 체력이 더이상 떨어지지 않고 패턴이 변경됨\n패턴 변경 시, 흐트러짐 상태가 해제되고 다음 턴에 속도가 10이됨
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838001].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon hitting 80%, 60%, and 40% HP, no longer take damage and gain a new pattern\nUpon gaining a new pattern, recover from Stagger and raise Speed to 10 next turn
   PL:
10. [[a1c7p3] Pasywka wroga [838002] — nazwa] 이 지긋지긋한 병에서 벗어날수 있다면
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838002].name
   limit: do 70 znaków
   EN: If we can be freed from this excruciating sickness
   PL:
11. [[a1c7p3] Pasywka wroga [838002] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 입힌 피해량의 40%만큼 부위와 본체 체력 회복.\n- 자신의 [Laceration] 위력 1당, 이 패시브의 회복량 1% 증가 (최대 20%)\n- 파괴 불가 코인의 경우 합 패배 후 적중 시 이 효과는 발동되지 않음.\n매 턴 시작 시 ([BloodDinner] / 10)만큼 자신의 체력을 회복함. (최대 50)\n매 턴 시작 시 정신력이 -15 이하라면, (20 - 자신의 정신력)만큼 [BloodDinner]을 소모하여 정신력 회복. 합 위력 증가 2 얻음\n적 처치 시, [BloodArmor]을 5 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838002].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [BloodArmor]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood
   EN: On Hit, if the target has [Laceration], heal Part and Core by 40% of the damage dealt.\n- This Passive heals +1% more HP for every [Laceration] Potency on self (max 20%)\n- For Unbreakable Coins: this effect does not activate on Hit After Clash Lose.\nEvery Turn Start: heal ([BloodDinner]/10) HP. (max 50)\nEvery Turn Start: at -15 or less SP, consume (20 - current SP) [BloodDinner] to gain SP and gain 2 Clash Power Up\nOn Kill, gain 5 [BloodArmor]
   PL:
12. [[a1c7p3] Pasywka wroga [838002] — podsumowanie] 공격 적중 시, 대상에게 [Laceration]이 있으면 체력 회복
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838002].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Hit, if the target has [Laceration], heal HP
   PL:
13. [[a1c7p3] Pasywka wroga [838003] — nazwa] 나도 모험을 해도 되는걸까
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838003].name
   limit: do 50 znaków
   EN: Can I go on an adventure, too?
   PL:
14. [[a1c7p3] Pasywka wroga [838003] — opis] 턴 종료 시 [BloodDinner] 300당 다음 턴에 속도 최솟값, 최댓값 +1
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: Turn End: Min & Max Speed +1 next turn for every 300 [BloodDinner]
   PL:
15. [[a1c7p3] Pasywka wroga [838004] — nazwa] 혈찬
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838004].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL:
16. [[a1c7p3] Pasywka wroga [838004] — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 적 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 최대로 드러난다.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838004].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit.\nWhen this unit enters the field, the sleeping blood drenching the battlefield will flood the surface.
   PL:
17. [[a1c7p3] Pasywka wroga [838005] — nazwa] 경혈
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838005].name
   limit: do 40 znaków
   EN: Hardblood
   PL:
18. [[a1c7p3] Pasywka wroga [838005] — opis] 전투 시작 시, [BloodArmor]을 1 얻음\n- [BloodArmor]이 1 미만으로 감소하지 않음.\n- [BloodArmor]이 10 이상이면, [BloodArmor_2nd]로 전환됨.\n- [BloodArmor] 가 20 이상이면, [BloodArmor_3rd]로 전환됨.\n단계에 따라 속도 최솟값, 최댓값 1 증가 (최대 2)\n[BloodArmor]이 소모되어, 부족해지면 이전 단계가 됨
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838005].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [BloodArmor], [BloodArmor_2nd], [BloodArmor_3rd]
   znaczenie tagów: [BloodArmor] = 경혈 / Hardblood; [BloodArmor_2nd] = 경혈 II / Hardblood II; [BloodArmor_3rd] = 경혈 III / Hardblood III
   EN: Combat Start: gain 1 [BloodArmor]\n- [BloodArmor] cannot drop below 1\n- At 10+ [BloodArmor], convert them to [BloodArmor_2nd].\n- At 20+ [BloodArmor], convert them to [BloodArmor_3rd].\nGain Min & Max Speed based on the Stage of this effect (max 2)\nIf this unit consumes [BloodArmor] and drops below the above thresholds, revert to previous Stages accordingly
   PL:
19. [[a1c7p3] Pasywka wroga [838007] — nazwa] 하지만 어버이가 있고, 가족이 있고, 외면할 수 없는
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838007].name
   limit: do 80 znaków
   EN: But I have my Father and my Family whom I cannot abandon
   PL:
20. [[a1c7p3] Pasywka wroga [838007] — opis] 턴 종료 시 패닉이면 패닉을 해제하고, [BloodDinner]을 100 소모해서 [Enhancement] 3을 얻음\n- [BloodDinner]을 소모하지 못했으면 [Laceration]을 30 얻고 [Enhancement] 3, 피해량 증가 2를 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=838007].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [Enhancement], [Laceration]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Laceration] = 출혈 / Bleed
   EN: Turn End: If Panicked, recover from Panic, and consume 100 [BloodDinner] to gain 3 [Enhancement]\n- If this unit failed to consume [BloodDinner], gain 30 [Laceration], 3 [Enhancement], and 2 Damage Up
   PL:
21. [[a1c7p3] Pasywka wroga [837701] — nazwa] 가시 올가미
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837701].name
   limit: do 40 znaków
   EN: Barbed Lasso
   PL:
22. [[a1c7p3] Pasywka wroga [837701] — opis] 사망시, 자신이 붙잡고 있는 적의 [ThornNoose] 제거
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ThornNoose]
   znaczenie tagów: [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: When this unit dies, the [ThornNoose] of the enemy bound to this unit expires
   PL:
23. [[a1c7p3] Pasywka wroga [839401] — nazwa] 지정 보호
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839401].name
   limit: do 40 znaków
   EN: Designated Protection
   PL:
24. [[a1c7p3] Pasywka wroga [839401] — opis] 턴 시작 시 체력이 감소하여 이전 턴과 체력 비율이 가장 차이가 많이 나는 아군에게 방어 레벨 증가 2 부여
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839401].desc
   limit: do 150 znaków
   EN: At Turn Start, apply 2 Defense Level Up to the ally who lost the most HP percentage between this Turn and last Turn
   PL:
25. [[a1c7p3] Pasywka wroga [840301] — nazwa] 깨져 흩날리는 경혈
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=840301].name
   limit: do 50 znaków
   EN: Shattering, Scattering Hardblood
   PL:
26. [[a1c7p3] Pasywka wroga [840301] — opis] 적의 공격, 상태이상 피해로 사망 시 [BloodDinner] 30 증가, 무작위 E.G.O 자원 2개 증가. 스스로 제거된 경우 발동되지 않음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=840301].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: When this unit is killed due to enemy attack or Status effect damage, increase [BloodDinner] by 30, and increase E.G.O resource of a random Affinity by 2. Does not activate if this unit killed itself.
   PL:
27. [[a1c7p3] Pasywka wroga [840302] — nazwa] 미쳐터져버리고만 싶어요!
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=840302].name
   limit: do 40 znaków
   EN: This Explosive Insanity!
   PL:
28. [[a1c7p3] Pasywka wroga [840302] — opis] 턴 종료 시 생존한 상태면, 다음 턴에 자폭 스킬 사용. 자폭 스킬을 사용한 턴 종료 시 사망하지 않았다면 사망함.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=840302].desc
   limit: do 250 znaków
   EN: If this unit is still alive by Turn End, use the self-detonation Skill next turn. If this unit is still alive at the same Turn End as the turn this unit used the self-detonation Skill, dies.
   PL:
29. [[a1c7p3] Pasywka wroga [839001] — nazwa] 본체 체력 1 유지
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839001].name
   limit: do 40 znaków
   EN: Fix Core HP to 1
   PL:
30. [[a1c7p3] Pasywka wroga [839001] — opis] 본체의 체력이 1 미만으로 감소하지 않음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839001].desc
   limit: do 120 znaków
   EN: Core HP does not drop below 1.
   PL:
31. [[a1c7p3] Pasywka wroga [839002] — nazwa] 버려지고 곪은 라만차랜드
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839002].name
   limit: do 60 znaków
   EN: La Manchaland, Abandoned and Festering
   PL:
32. [[a1c7p3] Pasywka wroga [839002] — opis] 일정 주기로 혈귀와 피주머니가 담긴 곤돌라를 생성함. 곤돌라가 생성될 때 일정 수의 혈귀와 피주머니가 함께 등장할 수 있음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839002].desc
   limit: do 230 znaków
   EN: Generates Gondolas filled with Bloodfiends and Bloodbags at a set interval. A certain number of Bloodfiends and Bloodbags may arrive at the field when a Gondola is generated.
   PL:
33. [[a1c7p3] Pasywka wroga [839003] — nazwa] 영원히 도는 풍차,대관람차 그리고 우리
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839003].name
   limit: do 70 znaków
   EN: The Eternal Cycle of Windmills, Wheels, and Us
   PL:
34. [[a1c7p3] Pasywka wroga [839003] — opis] 곤돌라가 생성되어있을 때 공격할 수 없음.\n스킬 피해로 체력이 감소하지 않음. [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 효과로 체력 피해를 받지 않음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839003].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Cannot be attacked when there is a Gondola on the field.\nDoes not lose HP due to Skill damage. Does not take HP damage due to [Combustion], [Laceration], [Vibration], [Burst], or [Sinking].
   PL:
35. [[a1c7p3] Pasywka wroga [839004] — nazwa] 다시... 다시 도는거란다.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839004].name
   limit: do 40 znaków
   EN: Here we go... another lap.
   PL:
36. [[a1c7p3] Pasywka wroga [839004] — opis] 턴 종료 시 또는 전투 진행 중 [FerrisWheel]가 0이고, 다음 턴에 등장할 적이 없으면, 다음 페이즈로 넘어감.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839004].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [FerrisWheel]
   znaczenie tagów: [FerrisWheel] = 돌고도는 관람차 / The Endless Wheel
   EN: If [FerrisWheel] is at 0 and there are no units to be spawned next turn at Turn End or during the combat phase, move on to the next phase.
   PL:
37. [[a1c7p3] Pasywka wroga [839005] — nazwa] 굶주림과 노쇠
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839005].name
   limit: do 40 znaków
   EN: Starved and Withered
   PL:
38. [[a1c7p3] Pasywka wroga [839005] — opis] 전투 시작 시, [StarvingDonqui] 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839005].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingDonqui]
   znaczenie tagów: [StarvingDonqui] = 굶주림과 노쇠 / Starved and Withered
   EN: Gain [StarvingDonqui] at the start of the Encounter
   PL:
39. [[a1c7p3] Pasywka wroga [841001] — nazwa] 다시 도는 피의 충동
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841001].name
   limit: do 40 znaków
   EN: Returning Bloodlust
   PL:
40. [[a1c7p3] Pasywka wroga [841001] — opis] - [RegainedStrength]이 10 이상이면, [RegainedStrength_2nd] 로 전환됨.\n- [RegainedStrength]이 20 이상이면, [RegainedStrength_3rd] 로 전환됨.\n- [RegainedStrength]이 소모되어, 부족해지면 이전 단계가 됨
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841001].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [RegainedStrength], [RegainedStrength_2nd], [RegainedStrength_3rd]
   znaczenie tagów: [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [RegainedStrength_2nd] = 다시 도는 피의 충동 II / Returning Bloodlust II; [RegainedStrength_3rd] = 다시 도는 피의 충동 III / Returning Bloodlust III
   EN: - At 10+ [RegainedStrength], convert them to [RegainedStrength_2nd].\n- At 20+ [RegainedStrength], convert them to [RegainedStrength_3rd].\n- If this unit consumes [RegainedStrength] and drops it below the above thresholds, revert to previous Stages accordingly
   PL:
41. [[a1c7p3] Pasywka wroga [841002] — nazwa] 돈키호테식 경혈
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841002].name
   limit: do 40 znaków
   EN: Don Quixote Hardblood Arts
   PL:
42. [[a1c7p3] Pasywka wroga [841002] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 입힌 체력 피해량의 30%만큼 부위와 본체 체력 회복. \n파괴 불가 코인의 경우, 합 패배 후 적중 시 이 효과는 발동되지 않음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841002].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Hit, if the target has [Laceration], heal this unit's Part & Core by 30% of the HP damage dealt.\nFor Unbreakable Coins: this effect does not activate on Hit after Clash Lose.
   PL:
43. [[a1c7p3] Pasywka wroga [841003] — nazwa] 낯선 만찬
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841003].name
   limit: do 40 znaków
   EN: An Unfamiliar Banquet
   PL:
44. [[a1c7p3] Pasywka wroga [841003] — opis] 한 턴에 체력을 자신의 최대 체력의 15% 이상 회복했거나, 적의 [Laceration]을 흡수했으면, 다음 턴에 [Binding] 3 얻음. (턴 당 1회)\n자신의 스킬로 대상을 처치한 경우, 다음 턴에 [AttackDown] 2 , [DefenseDown] 1 얻음. (최대 3회 발동)
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841003].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Binding], [AttackDown], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: If this unit healed more than 15% of its max HP, or siphoned the enemy's [Laceration], gain 3 [Binding] next turn. (once per turn)\nIf this unit killed the target with its Skill, gain 2 [AttackDown] and 1 [DefenseDown] next turn. (3 times per turn)
   PL:
45. [[a1c7p3] Pasywka wroga [841004] — nazwa] 가족을 위하여…
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841004].name
   limit: do 40 znaków
   EN: For the Family...
   PL:
46. [[a1c7p3] Pasywka wroga [841004] — opis] 턴 종료 시 패닉 상태면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨.\n패닉 상태가 해제될 때\n- [BloodDinner]을 30 소모하여 다음 턴에 [Enhancement] 2, [Agility] 1 얻고, 정신력 30 회복\n- [BloodDinner]을 소모하지 못한 경우, [Laceration] 40을 얻고 즉시 발동시킨 후, 자신의 [Laceration] 횟수 5 감소.\n- 이후 다음 턴에 [Enhancement] 2를 얻고, 정신력 30 회복
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841004].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [Enhancement], [Agility], [Laceration]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste; [Laceration] = 출혈 / Bleed
   EN: Turn End: If Panicked, recover from Panic at the next Turn Start and reset SP to 0.\nWhen recovering from Panic:\n- Consume 30 [BloodDinner] to gain 2 [Enhancement] and 1 [Agility] next turn, and heal 30 SP.\n- If this unit failed to consume [BloodDinner], gain 40 [Laceration], immediately take the damage from [Laceration], then lose 5 [Laceration] Count.\n- Then, gain 2 [Enhancement] next turn and heal 30 SP
   PL:
47. [[a1c7p3] Pasywka wroga [841101] — nazwa] 헛되고 안일했던 꿈의 조각
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841101].name
   limit: do 60 znaków
   EN: Broken Fragment of a Futile, Naive Dream
   PL:
48. [[a1c7p3] Pasywka wroga [841101] — opis] 이 유닛이 제거되면 [BloodDinner] 30 증가\n수감자에 의해 처치 시 꿈꾸는 모험의 기억 생성
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841101].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is eliminated, increase [BloodDinner] by 30\nWhen killed by a Sinner, generate Memories of the Dreaming Adventure
   PL:
49. [[a1c7p3] Pasywka wroga [841102] — nazwa] 가족을 등진 이기적인 바램
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841102].name
   limit: do 60 znaków
   EN: A Selfish Wish at the Expense of the Family
   PL:
50. [[a1c7p3] Pasywka wroga [841102] — opis] 돈키호테에게 처치되면\n- 돈키호테가 [RegainedStrength] 5 얻음.\n-모든 수감자가 색욕 피해를 30 받고, [Laceration] 위력 8, [Laceration] 횟수 8 얻음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841102].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [RegainedStrength], [Laceration]
   znaczenie tagów: [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [Laceration] = 출혈 / Bleed
   EN: When killed by Don Quixote:\n- Don Quixote gains 5 [RegainedStrength].\n- All Sinners take 30 Lust damage and gain 8 [Laceration] Potency and Count.
   PL:
51. [[a1c7p3] Pasywka wroga [841301] — nazwa] 지나온 모험의 기억들
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841301].name
   limit: do 50 znaków
   EN: Memories of the Journeys Past
   PL:
52. [[a1c7p3] Pasywka wroga [841301] — opis] 매 턴 시작 시 모든 수감자 정신력 5 회복.\n돈키호테 수감자에게 특수한 효과 부여
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All Sinners gain 5 SP at every Turn Start.\nDon Quixote the Sinner gains a special effect
   PL:
53. [[a1c7p3] Pasywka wroga [841302] — nazwa] 되새기는 의지
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841302].name
   limit: do 40 znaków
   EN: Reminders of Determination
   PL:
54. [[a1c7p3] Pasywka wroga [841302] — opis] 돈키호테에게 처치되면 돈키호테에게 이번 턴과 다음 턴에 [Reduction] 3 부여.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841302].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: When killed by Don Quixote: Don Quixote gains 3 [Reduction] this turn and next turn.
   PL:
55. [[a1c7p3] Pasywka wroga [841201] — nazwa] 경혈 쐐기 구속
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841201].name
   limit: do 40 znaków
   EN: Hardblood Wedge Gaol
   PL:
56. [[a1c7p3] Pasywka wroga [841201] — opis] 이 유닛이 제거되면 다음 턴에 이 유닛에게 꿰뚫렸던 아군의 [Penetration] 상태가 해제됨.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841201].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Penetration]
   znaczenie tagów: [Penetration] = 굳어가는 피 / Congealing Blood
   EN: When this unit is eliminated, the ally who was impaled by this unit will lose the [Penetration] status next turn.
   PL:
57. [[a1c7p3] Pasywka wroga [841202] — nazwa] 깨져 흩날리는 경혈
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841202].name
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [[a1c7p3] Pasywka wroga [841202] — opis] 이 유닛이 제거되면 수량이 가장 부족한 ego 자원 3개, 무작위 ego 자원 3개 획득.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841202].desc
   limit: do 120 znaków
   EN: When this unit is eliminated, gain 3 E.G.O resources for the least-owned E.G.O resource.
   PL:
59. [[a1c7p3] Pasywka wroga [841203] — nazwa] 안에서부터 결정화 되어가는 피
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841203].name
   limit: do 50 znaków
   EN: Internal Blood Crystallization
   PL:
60. [[a1c7p3] Pasywka wroga [841203] — opis] 생성된 다음 턴까지 처치되지 않았으면, 해당 턴 종료 시 이 유닛이 제거되며, 제거 시 효과가 발동됨.\n이후 이 유닛에게 꿰뚫렸던 아군이 최대 체력의 30%만큼 고정 피해를 받고, [Laceration] 위력 10, 횟수 5를 얻음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841203].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If this unit is not eliminated by the turn after its generation, this unit will be eliminated at Turn End, activating the following effect.\nThe ally who was impaled by this unit takes fixed damage equal to 30% of their max HP, and gains 10 [Laceration] Potency and +5 [Laceration] Count.
   PL:
61. [[a1c7p3] Pasywka wroga [841204] — nazwa] 굳어버린 모든 피
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841204].name
   limit: do 40 znaków
   EN: Total Blood Coagulation
   PL:
62. [[a1c7p3] Pasywka wroga [841204] — opis] 진짜 돈키호테에게 처치되면, 사망시 효과가 발동되고, 이 유닛에게 꿰뚫렸던 아군이 사망함.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841204].desc
   limit: do 150 znaków
   EN: When killed by true Don Quixote, activate the on-death effect, and the ally impaled by this unit will be killed.
   PL:
63. [[a1c7p3] Pasywka wroga [841103] — nazwa] 품어서는 안될 무책임했던 꿈이었던거야
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841103].name
   limit: do 70 znaków
   EN: I never should've dreamed this irresponsible dream
   PL:
64. [[a1c7p3] Pasywka wroga [841103] — opis] 자신에게 [Precarious]이 있으면, 처치 시 꿈꾸는 모험의 기억이 생성되지 않음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841103].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Precarious]
   znaczenie tagów: [Precarious] = 무책임한 꿈 / Irresponsible Dream
   EN: If this unit has [Precarious], Memories of the Dreaming Adventure will not be generated on death
   PL:
65. [[a1c7p3] Pasywka wroga [839006] — nazwa] 황금가지의 강제 조율
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839006].name
   limit: do 60 znaków
   EN: The Golden Bough's Forced Arbitration
   PL:
66. [[a1c7p3] Pasywka wroga [839006] — opis] 전투 시작 시, [ConfinementOfGoldenBranch] 얻음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=839006].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ConfinementOfGoldenBranch]
   znaczenie tagów: [ConfinementOfGoldenBranch] = 황금가지의 강제 조율 / The Golden Bough's Forced Arbitration
   EN: Encounter Start: gain [ConfinementOfGoldenBranch].
   PL:
67. [[a1c7p3] Pasywka wroga [841005] — nazwa] 좀 더 해보렴
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841005].name
   limit: do 40 znaków
   EN: Please, try again
   PL:
68. [[a1c7p3] Pasywka wroga [841005] — opis] 패턴 변경 시 자신의 부위에 부여된 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 위력을 절반으로 감소.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841005].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: When gaining a new pattern, halve the Potency of [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] on this unit's Parts.
   PL:
69. [[a1c7p3] Pasywka wroga [841104] — nazwa] 모험은 여기서 끝이다.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841104].name
   limit: do 40 znaków
   EN: The adventure ends here.
   PL:
70. [[a1c7p3] Pasywka wroga [841104] — opis] 매 턴 시작 시 돈키호테가 보호막을 얻음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=841104].desc
   limit: do 120 znaków
   EN: Don Quixote gains Shield at every Turn Start.
   PL:

## [a1c8p1] Wróg / część: Enemies-a1c8p1
- plik gry: `Enemies-a1c8p1.json`

71. [[a1c8p1] Wróg / część [90195] — nazwa] 부적 달린 항아리 괴물
   źródło: Enemies-a1c8p1.json :: dataList[id=90195].name
   limit: do 40 znaków
   EN: Talisman Jar Monster
   PL:
72. [[a1c8p1] Wróg / część [90195] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90195].desc
   limit: do 120 znaków
   EN: Unit
   PL:
73. [[a1c8p1] Wróg / część [90196] — nazwa] 못박힌 항아리 괴물
   źródło: Enemies-a1c8p1.json :: dataList[id=90196].name
   limit: do 40 znaków
   EN: Nailed Jar Monster
   PL:
74. [[a1c8p1] Wróg / część [90196] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90196].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [[a1c8p1] Wróg / część [90197] — nazwa] 얽매인 항아리 괴물
   źródło: Enemies-a1c8p1.json :: dataList[id=90197].name
   limit: do 40 znaków
   EN: Entangled Jar Monster
   PL:
76. [[a1c8p1] Wróg / część [90197] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90197].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [[a1c8p1] Wróg / część [91022] — nazwa] 먹고 먹힌 고독 항아리 괴물
   źródło: Enemies-a1c8p1.json :: dataList[id=91022].name
   limit: do 80 znaków
   EN: Monster from the Gorged and Devoured Jar of Loneliness
   PL:
78. [[a1c8p1] Wróg / część [91022] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=91022].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [[a1c8p1] Wróg / część [90198] — nazwa] 은밀한 박도 습격자
   źródło: Enemies-a1c8p1.json :: dataList[id=90198].name
   limit: do 40 znaków
   EN: Furtive Podao Assailant
   PL:
80. [[a1c8p1] Wróg / część [90198] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90198].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [[a1c8p1] Wróg / część [90199] — nazwa] 날렵한 박도 습격자
   źródło: Enemies-a1c8p1.json :: dataList[id=90199].name
   limit: do 40 znaków
   EN: Swift Podao Assailant
   PL:
82. [[a1c8p1] Wróg / część [90199] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90199].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [[a1c8p1] Wróg / część [90200] — nazwa] 거대한 박도 습격자
   źródło: Enemies-a1c8p1.json :: dataList[id=90200].name
   limit: do 40 znaków
   EN: Large Podao Assailant
   PL:
84. [[a1c8p1] Wróg / część [90200] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90200].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [[a1c8p1] Wróg / część [91021] — nazwa] 취수야객
   źródło: Enemies-a1c8p1.json :: dataList[id=91021].name
   limit: do 50 znaków
   EN: Night Drifter of the Drunken Palm
   PL:
86. [[a1c8p1] Wróg / część [91021] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=91021].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [[a1c8p1] Wróg / część [90201] — nazwa] 붕대묶인 목인장
   źródło: Enemies-a1c8p1.json :: dataList[id=90201].name
   limit: do 40 znaków
   EN: Bandaged Wooden Dummy
   PL:
88. [[a1c8p1] Wróg / część [90201] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90201].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [[a1c8p1] Wróg / część [90202] — nazwa] 가시돋친 목인장
   źródło: Enemies-a1c8p1.json :: dataList[id=90202].name
   limit: do 40 znaków
   EN: Spiked Wooden Dummy
   PL:
90. [[a1c8p1] Wróg / część [90202] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90202].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [[a1c8p1] Wróg / część [90203] — nazwa] 기습해오는 날렵한 괴한
   źródło: Enemies-a1c8p1.json :: dataList[id=90203].name
   limit: do 40 znaków
   EN: Swift Ambushing Stranger
   PL:
92. [[a1c8p1] Wróg / część [90203] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90203].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [[a1c8p1] Wróg / część [90204] — nazwa] 쫓아오는 날렵한 괴한
   źródło: Enemies-a1c8p1.json :: dataList[id=90204].name
   limit: do 40 znaków
   EN: Swift Pursuing Stranger
   PL:
94. [[a1c8p1] Wróg / część [90204] — opis] 잡몹
   źródło: Enemies-a1c8p1.json :: dataList[id=90204].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c8p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c8p1
- grupa rozdziału/trybu: `a1c8p1` · plik: `Skills_Enemy-a1c8p1.json`

95. [Umiejętność wroga [9020301] (ulepszenie 1) — nazwa] 급소 꿰뚫기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020301].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressure Point Penetration
   PL:
96. [Umiejętność wroga [9020301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
97. [Umiejętność wroga [9020302] (ulepszenie 1) — nazwa] 급소 부수기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020302].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressure Point Crush
   PL:
98. [Umiejętność wroga [9020302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3 이상이면, 합 위력 + 1\n[WhenUse] 대상의 [Vibration]이 4 이상이면, 코인 위력 + 1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020302].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 3+ [Laceration], Clash Power +1\n[WhenUse] If target has 4+ [Vibration], Coin Power +1
   PL:
99. [Umiejętność wroga [9020302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
100. [Umiejętność wroga [9020302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Umiejętność wroga [9020303] (ulepszenie 1) — nazwa] 가마 부수기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].name
   limit: do 40 znaków
   EN: Palanquin Crush
   PL:
102. [Umiejętność wroga [9020303] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3 이상이면, 합 위력 + 1\n[WhenUse] 대상의 [Vibration]이 4 이상이면, 코인 위력 + 1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Umiejętność wroga [9020303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
104. [Umiejętność wroga [9020303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
105. [Umiejętność wroga [9020303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [9020303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
107. [Umiejętność wroga [9020303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
108. [Umiejętność wroga [9020303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Umiejętność wroga [9020304] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020304].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL:
110. [Umiejętność wroga [9020304] (ulepszenie 1) — opis] [WhenUse] 자신이 보유한 부정적인 효과 1개당 3의 보호막을 얻음 (최대 10)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Shield for every type of negative effect on self (max 10)
   PL:
111. [Umiejętność wroga [9020401] (ulepszenie 1) — nazwa] 급소 찌르기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020401].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressure Point Stab
   PL:
112. [Umiejętność wroga [9020401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Umiejętność wroga [9020402] (ulepszenie 1) — nazwa] 급소 타격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020402].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressure Point Strike
   PL:
114. [Umiejętność wroga [9020402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3 이상이면, 합 위력 + 1\n[WhenUse] 대상의 [Vibration]이 4 이상이면, 코인 위력 + 1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020402].levelList[level=1].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Umiejętność wroga [9020402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Umiejętność wroga [9020402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Umiejętność wroga [9020403] (ulepszenie 1) — nazwa] 가마 터트리기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].name
   limit: do 40 znaków
   EN: Palanquin Buster
   PL:
118. [Umiejętność wroga [9020403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 횟수가 3 이상이면, 합 위력 + 1\n[WhenUse] 대상의 [Vibration] 횟수가 4 이상이면, 코인 위력 + 1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 3+ [Laceration] Count, Clash Power +1\n[WhenUse] If target has 4+ [Vibration] Count, Coin Power +1
   PL:
119. [Umiejętność wroga [9020403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [9020403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Umiejętność wroga [9020403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Umiejętność wroga [9020403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Umiejętność wroga [9020403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność wroga [9020403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [9020404] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020404].levelList[level=1].name
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [9020404] (ulepszenie 1) — opis] [WhenUse] 자신이 보유한 부정적인 효과 1개당 3의 보호막을 얻음 (최대 10)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020404].levelList[level=1].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Umiejętność wroga [9020101] (ulepszenie 1) — nazwa] 일점 타격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020101].levelList[level=1].name
   limit: do 40 znaków
   EN: Pinpoint Strike
   PL:
128. [Umiejętność wroga [9020101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] next turn
   PL:
129. [Umiejętność wroga [9020102] (ulepszenie 1) — nazwa] 원회점타
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020102].levelList[level=1].name
   limit: do 50 znaków
   EN: Circular Roundhouse Point-Strike
   PL:
130. [Umiejętność wroga [9020102] (ulepszenie 1) — opis] 자신이 보유한 부정적인 효과 1개당 합 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020102].levelList[level=1].desc
   limit: do 120 znaków
   EN: Gain Clash Power +1 for every type of negative effect on self (max 3)
   PL:
131. [Umiejętność wroga [9020102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown] next turn
   PL:
132. [Umiejętność wroga [9020103] (ulepszenie 1) — nazwa] 원회타
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020103].levelList[level=1].name
   limit: do 40 znaków
   EN: Circular Roundhouse Strike
   PL:
133. [Umiejętność wroga [9020103] (ulepszenie 1) — opis] 자신이 보유한 부정적인 효과 1개당 합 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020103].levelList[level=1].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [9020103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [9020103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [9020103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [9020104] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020104].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL:
138. [Umiejętność wroga [9020104] (ulepszenie 1) — opis] 자신이 보유한 부정적인 효과 1개당 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020104].levelList[level=1].desc
   limit: do 120 znaków
   EN: Gain Coin Power +1 for every type of negative effect on self (max 3)
   PL:
139. [Umiejętność wroga [9020201] (ulepszenie 1) — nazwa] 중앙 타격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020201].levelList[level=1].name
   limit: do 40 znaków
   EN: Center Strike
   PL:
140. [Umiejętność wroga [9020201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] next turn
   PL:
141. [Umiejętność wroga [9020202] (ulepszenie 1) — nazwa] 반회점타
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020202].levelList[level=1].name
   limit: do 50 znaków
   EN: Semicircular Roundhouse Point-Strike
   PL:
142. [Umiejętność wroga [9020202] (ulepszenie 1) — opis] 자신이 보유한 부정적인 효과 1개당 합 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020202].levelList[level=1].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [9020202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn
   PL:
144. [Umiejętność wroga [9020203] (ulepszenie 1) — nazwa] 반회타
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020203].levelList[level=1].name
   limit: do 50 znaków
   EN: Semicircular Roundhouse Strike
   PL:
145. [Umiejętność wroga [9020203] (ulepszenie 1) — opis] 자신이 보유한 부정적인 효과 1개당 합 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020203].levelList[level=1].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [9020203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność wroga [9020203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność wroga [9020203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [9020204] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020204].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [9020204] (ulepszenie 1) — opis] 자신이 보유한 부정적인 효과 1개당 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020204].levelList[level=1].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [9019501] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019501].levelList[level=1].name
   limit: do 40 znaków
   EN: Clawing
   PL:
152. [Umiejętność wroga [9019501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
153. [Umiejętność wroga [9019502] (ulepszenie 1) — nazwa] 연속 할퀴기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019502].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Clawing
   PL:
154. [Umiejętność wroga [9019502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 4+ [Burst], Base Power +1
   PL:
155. [Umiejętność wroga [9019502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
156. [Umiejętność wroga [9019502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Umiejętność wroga [9019503] (ulepszenie 1) — nazwa] 뜯어내기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019503].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear Off
   PL:
158. [Umiejętność wroga [9019503] (ulepszenie 1) — opis] [WhenUse] 잃어버린 체력 20%당, 기본 위력 +1 (최대 4)\n[WhenUse] 대상의 [Burst] 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019503].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Base Power +1 for every 20% missing HP on self (max 4)\n[WhenUse] Coin Power +1 for every 6 [Burst] (max 2)
   PL:
159. [Umiejętność wroga [9019503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Umiejętność wroga [9019503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Umiejętność wroga [9019503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
162. [Umiejętność wroga [9019503] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019503].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +3 [Burst] Count
   PL:
163. [Umiejętność wroga [9019504] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019504].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [9019504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL:
165. [Umiejętność wroga [9019505] (ulepszenie 1) — nazwa] 뛰어드는 금 간 항아리
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019505].levelList[level=1].name
   limit: do 40 znaków
   EN: Leaping Cracked Jar
   PL:
166. [Umiejętność wroga [9019505] (ulepszenie 1) — opis] [EndSkill] 다음 턴에 아래의 효과중 2개를 무작위로 부여. 10의 피해를 주고 사망함\n- [AttackDown] 3\n- [DefenseDown] 3\n- [Paralysis] 1\n- [Binding] 2
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019505].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [AttackDown], [DefenseDown], [Paralysis], [Binding]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Paralysis] = 마비 / Paralyze; [Binding] = 속박 / Bind
   EN: [EndSkill] Randomly inflict 2 of the following effects next turn. Dies after dealing 10 damage\n- 3 [AttackDown]\n- 3 [DefenseDown]\n- 1 [Paralysis]\n- 2 [Binding]
   PL:
167. [Umiejętność wroga [9019505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [9019601] (ulepszenie 1) — nazwa] 손톱 긁기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019601].levelList[level=1].name
   limit: do 40 znaków
   EN: Claw Scratch
   PL:
169. [Umiejętność wroga [9019601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
170. [Umiejętność wroga [9019602] (ulepszenie 1) — nazwa] 연속 긁기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019602].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Scratching
   PL:
171. [Umiejętność wroga [9019602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019602].levelList[level=1].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [9019602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [9019602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność wroga [9019603] (ulepszenie 1) — nazwa] 달라붙기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019603].levelList[level=1].name
   limit: do 40 znaków
   EN: Latching On
   PL:
175. [Umiejętność wroga [9019603] (ulepszenie 1) — opis] [WhenUse] 잃어버린 체력 20%당, 기본 위력 +1 (최대 4)\n[WhenUse] 대상의 [Burst] 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019603].levelList[level=1].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Umiejętność wroga [9019603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [9019603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [9019603] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019603].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [9019603] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019603].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [9019604] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019604].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [9019604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst] and +1 [Burst] Count
   PL:
182. [Umiejętność wroga [9019605] (ulepszenie 1) — nazwa] 뛰어드는 금 간 항아리
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019605].levelList[level=1].name
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [9019605] (ulepszenie 1) — opis] [EndSkill] 다음 턴에 아래의 효과중 2개를 무작위로 부여. 10의 피해를 주고 사망함\n- [AttackDown] 3\n- [DefenseDown] 3\n- [Paralysis] 1\n- [Binding] 2
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019605].levelList[level=1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [9019605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [9019701] (ulepszenie 1) — nazwa] 상처 파헤치기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019701].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound Digging
   PL:
186. [Umiejętność wroga [9019701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [9019702] (ulepszenie 1) — nazwa] 연속 파헤치기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019702].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Digging
   PL:
188. [Umiejętność wroga [9019702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 4+ [Burst], Coin Power +1
   PL:
189. [Umiejętność wroga [9019702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność wroga [9019702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [9019703] (ulepszenie 1) — nazwa] 살점 파헤치기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019703].levelList[level=1].name
   limit: do 40 znaków
   EN: Flesh Digging
   PL:
192. [Umiejętność wroga [9019703] (ulepszenie 1) — opis] [WhenUse] 잃어버린 체력 20%당, 기본 위력 +1 (최대 4)\n[WhenUse] 대상의 [Burst] 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019703].levelList[level=1].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [9019703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
194. [Umiejętność wroga [9019703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [9019703] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019703].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [9019703] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 4 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019703].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +4 [Burst] Count
   PL:
197. [Umiejętność wroga [9019704] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019704].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [9019704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [9019705] (ulepszenie 1) — nazwa] 뛰어드는 금 간 항아리
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019705].levelList[level=1].name
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [9019705] (ulepszenie 1) — opis] [EndSkill] 다음 턴에 아래의 효과중 2개를 무작위로 부여. 10의 피해를 주고 사망함\n- [AttackDown] 3\n- [DefenseDown] 3\n- [Paralysis] 1\n- [Binding] 2
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019705].levelList[level=1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [9019705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność wroga [9102201] (ulepszenie 1) — nazwa] 상처 할퀴기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102201].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound Clawing
   PL:
203. [Umiejętność wroga [9102201] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102201].levelList[level=1].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [9102201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Umiejętność wroga [9102201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [9102201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [9102201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [9102202] (ulepszenie 1) — nazwa] 살점 뜯기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102202].levelList[level=1].name
   limit: do 40 znaków
   EN: Flesh Tearing
   PL:
209. [Umiejętność wroga [9102202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 4 [Burst] on target (max 2)
   PL:
210. [Umiejętność wroga [9102202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [9102202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
212. [Umiejętność wroga [9102203] (ulepszenie 1) — nazwa] 고독 속 몸부림
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].name
   limit: do 40 znaków
   EN: Writhing in Loneliness
   PL:
213. [Umiejętność wroga [9102203] (ulepszenie 1) — opis] [WhenUse] 잃어버린 체력 10%당, 기본 위력 +1 (최대 5)\n[WhenUse] 대상의 [Burst] 4 당, 코인 위력 +1 (최대 3)\n\n[WhenUse] 대상의 ([Burst] + [Burst] 횟수)가 10 이상이면, 대상의 [Burst] 횟수만큼 [Burst] 횟수 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Base Power +1 for every 10% missing HP on self (max 5)\n[WhenUse] Coin Power +1 for every 4 [Burst] on target (max 3)\n\n[WhenUse] If target has 10+ ([Burst] + [Burst] Count), inflict [Burst] Count equal to [Burst] Count on target
   PL:
214. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
217. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] ([Burst] + [Burst] 횟수)가 15 이상이면, ([Burst] 위력 × [Burst] 횟수) 만큼의 탐식 피해를 입힘. (최대 40)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 15+ ([Burst] + [Burst] Count), inflict ([Burst] Potency x [Burst] Count) Gluttony damage. (max 40)
   PL:
225. [Umiejętność wroga [9102203] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102203].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +5 [Laceration] Count
   PL:
226. [Umiejętność wroga [9102204] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102204].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [9102204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
228. [Umiejętność wroga [9102204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [9102204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Burst]이 5 이상이면, 이 코인 재사용 (최대 2회)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 5+ [Burst], reuse this Skill (2 times max)
   PL:
230. [Umiejętność wroga [9102205] (ulepszenie 1) — nazwa] 뛰어드는 금 간 항아리
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102205].levelList[level=1].name
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [9102205] (ulepszenie 1) — opis] [EndSkill] 다음 턴에 아래의 효과중 3개를 무작위로 부여. 30의 피해를 주고 사망함\n- [AttackDown] 4\n- [DefenseDown] 4\n- [Paralysis] 2\n- [Binding] 2
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102205].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [AttackDown], [DefenseDown], [Paralysis], [Binding]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Paralysis] = 마비 / Paralyze; [Binding] = 속박 / Bind
   EN: [EndSkill] Randomly inflict 3 of the following effects next turn. Dies after dealing 30 damage\n- 4 [AttackDown]\n- 4 [DefenseDown]\n- 2 [Paralysis]\n- 2 [Binding]
   PL:
232. [Umiejętność wroga [9102205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [9019801] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019801].levelList[level=1].name
   limit: do 40 znaków
   EN: Slash
   PL:
234. [Umiejętność wroga [9019801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [9019802] (ulepszenie 1) — nazwa] 몰아붙이기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019802].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressuring
   PL:
236. [Umiejętność wroga [9019802] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 5+ [Laceration], Clash Power +1
   PL:
237. [Umiejętność wroga [9019802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [9019802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Umiejętność wroga [9019803] (ulepszenie 1) — nazwa] 파상처단
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019803].levelList[level=1].name
   limit: do 40 znaków
   EN: Ruptured Image Execution
   PL:
240. [Umiejętność wroga [9019803] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 5 [Laceration] on target (max 2)
   PL:
241. [Umiejętność wroga [9019803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [9019803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [9019803] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +1% damage for every ([Laceration] + [Laceration] Count) on the target (max 20%)
   PL:
244. [Umiejętność wroga [9019804] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019804].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [9019804] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Base Power +1
   PL:
246. [Umiejętność wroga [9019804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
247. [Umiejętność wroga [9019804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown] next turn
   PL:
248. [Umiejętność wroga [9019901] (ulepszenie 1) — nazwa] 쓸어내기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019901].levelList[level=1].name
   limit: do 40 znaków
   EN: Sweep Away
   PL:
249. [Umiejętność wroga [9019901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [9019902] (ulepszenie 1) — nazwa] 밀어붙이기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019902].levelList[level=1].name
   limit: do 40 znaków
   EN: Cornering
   PL:
251. [Umiejętność wroga [9019902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019902].levelList[level=1].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [9019902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [9019902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [9019903] (ulepszenie 1) — nazwa] 파상처리
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019903].levelList[level=1].name
   limit: do 50 znaków
   EN: Execution of the Ruptured Image
   PL:
255. [Umiejętność wroga [9019903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019903].levelList[level=1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [9019903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [9019903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [9019903] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [9019904] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019904].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność wroga [9019904] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019904].levelList[level=1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [9019904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność wroga [9019904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9019904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown] next turn
   PL:
263. [Umiejętność wroga [9020001] (ulepszenie 1) — nazwa] 받아베기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020001].levelList[level=1].name
   limit: do 40 znaków
   EN: Parrying Slash
   PL:
264. [Umiejętność wroga [9020001] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 8+ [Laceration], Clash Power +1
   PL:
265. [Umiejętność wroga [9020001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [9020002] (ulepszenie 1) — nazwa] 몰아베기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020002].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressuring Slash
   PL:
267. [Umiejętność wroga [9020002] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020002].levelList[level=1].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [9020002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [9020002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [9020003] (ulepszenie 1) — nazwa] 파도베기
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020003].levelList[level=1].name
   limit: do 40 znaków
   EN: Waveslash
   PL:
271. [Umiejętność wroga [9020003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020003].levelList[level=1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [9020003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [9020003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność wroga [9020003] (ulepszenie 1) — moneta 2, efekt 2 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność wroga [9020003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
276. [Umiejętność wroga [9020004] (ulepszenie 1) — nazwa] 마출겁세
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020004].levelList[level=1].name
   limit: do 50 znaków
   EN: Becalming of a Bewildered Steed
   PL:
277. [Umiejętność wroga [9020004] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 5 [Laceration] on target (max 3)
   PL:
278. [Umiejętność wroga [9020004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL:
279. [Umiejętność wroga [9020004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [9020004] (ulepszenie 1) — moneta 2, efekt 2 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +2% (최대 50%)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +2% damage for every ([Laceration] + [Laceration] Count) on the target (max 50%)
   PL:
281. [Umiejętność wroga [9020005] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020005].levelList[level=1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność wroga [9020005] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020005].levelList[level=1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [9020005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [9020005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
285. [Umiejętność wroga [9020005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown], [DefenseDown] 3 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9020005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown] and [DefenseDown] next turn
   PL:
286. [Umiejętność wroga [9102101] (ulepszenie 1) — nazwa] 전선참
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102101].levelList[level=1].name
   limit: do 40 znaków
   EN: Frontal Swirl
   PL:
287. [Umiejętność wroga [9102101] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 기본 위력 +1\n[WhenUse] [SipOfAlcohol] 1 얻음
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SipOfAlcohol]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SipOfAlcohol] = 한 모금 / Swig
   EN: [WhenUse] If target has 5+ [Laceration], Base Power +1\n[WhenUse] Gain 1 [SipOfAlcohol]
   PL:
288. [Umiejętność wroga [9102101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [9102102] (ulepszenie 1) — nazwa] 인도주
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102102].levelList[level=1].name
   limit: do 50 znaków
   EN: Way of the Open-throat Chugging
   PL:
290. [Umiejętność wroga [9102102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 기본 위력 +1 (최대 2)\n[WhenUse] [SipOfAlcohol] 1 얻음
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102102].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SipOfAlcohol]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SipOfAlcohol] = 한 모금 / Swig
   EN: [WhenUse] Base Power +1 for every 5 [Laceration] on target (max 2)\n[WhenUse] Gain 1 [SipOfAlcohol]
   PL:
291. [Umiejętność wroga [9102102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Umiejętność wroga [9102102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Umiejętność wroga [9102103] (ulepszenie 1) — nazwa] 낙주
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102103].levelList[level=1].name
   limit: do 40 znaków
   EN: Waterfall
   PL:
294. [Umiejętność wroga [9102103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n\n[DefeatDuel] [SipOfAlcohol] 3 소모
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel], [SipOfAlcohol]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [SipOfAlcohol] = 한 모금 / Swig
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1\n\n[DefeatDuel] Lose 3 [SipOfAlcohol]
   PL:
295. [Umiejętność wroga [9102103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [9102103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność wroga [9102103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [9102103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [WinDuelAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Inflict +3 [Laceration] Count
   PL:
299. [Umiejętność wroga [9102104] (ulepszenie 1) — nazwa] 취
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102104].levelList[level=1].name
   limit: do 40 znaków
   EN: Drunklaim
   PL:
300. [Umiejętność wroga [9102104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)\n[WhenUse] [SipOfAlcohol]이 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102104].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SipOfAlcohol], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SipOfAlcohol] = 한 모금 / Swig; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Coin Power +1 for every 5 [Laceration] on target (max 2)\n[WhenUse] At 3+ [SipOfAlcohol], convert all Coins on this Skill to [SuperCoin]s
   PL:
301. [Umiejętność wroga [9102104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność wroga [9102104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność wroga [9102104] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [9102104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [SipOfAlcohol]이 3 이상이면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SipOfAlcohol]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SipOfAlcohol] = 한 모금 / Swig
   EN: [OnSucceedAttack] If this unit has 3+ [SipOfAlcohol], reuse this Skill once (once per Skill)
   PL:
305. [Umiejętność wroga [9102105] (ulepszenie 1) — nazwa] 취회공
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102105].levelList[level=1].name
   limit: do 40 znaków
   EN: Drunken Returning Strike
   PL:
306. [Umiejętność wroga [9102105] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 5+ [Laceration], Base Power +1
   PL:
307. [Umiejętność wroga [9102105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [9102105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 4 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 4 [Paralysis] next turn
   PL:
309. [Umiejętność wroga [9102105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown], [DefenseDown] 5 부여
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 5 [AttackDown] and [DefenseDown] next turn
   PL:
310. [Umiejętność wroga [9102106] (ulepszenie 1) — nazwa] 진진종참
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102106].levelList[level=1].name
   limit: do 40 znaków
   EN: True Decapitation Deathblow
   PL:
311. [Umiejętność wroga [9102106] (ulepszenie 1) — opis] [StartBattle] 이 스킬이 종료되기 전까지 체력이 1 이하가 되지 않음.\n[WhenUse] [AttackUp] 10 얻음\n[WhenUse] [Enhancement] 5 얻음\n[WhenUse] [AttackDmgUp] 10 얻음
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102106].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [AttackUp], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] HP does not drop below 1 before this Skill ends.\n[WhenUse] Gain 10 [AttackUp]\n[WhenUse] Gain 5 [Enhancement]\n[WhenUse] Gain 10 [AttackDmgUp]
   PL:
312. [Umiejętność wroga [9102106] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 100%)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +1% damage for every ([Laceration] + [Laceration] Count) on the target (max 100%)
   PL:
313. [Umiejętność wroga [9102106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [SipOfAlcohol] 5 얻음
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SipOfAlcohol]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SipOfAlcohol] = 한 모금 / Swig
   EN: [OnSucceedAttack] Gain 5 [SipOfAlcohol]
   PL:
314. [Umiejętność wroga [9102107] (ulepszenie 1) — nazwa] 취고
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102107].levelList[level=1].name
   limit: do 40 znaków
   EN: Intoxicated Leaning
   PL:
315. [Umiejętność wroga [9102107] (ulepszenie 1) — opis] [WhenUse] 자신의 [SipOfAlcohol]당 보호막 5 얻음 (최대 25)\n[WhenUse] 자신을 타겟팅하고 있는 스킬 수만큼 [SipOfAlcohol]을 얻음 (최대 5)
   źródło: Skills_Enemy-a1c8p1.json :: dataList[id=9102107].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SipOfAlcohol]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SipOfAlcohol] = 한 모금 / Swig
   EN: [WhenUse] Gain 5 Shield for every [SipOfAlcohol] on self (max 25)\n[WhenUse] Gain [SipOfAlcohol] equal to the number of Skills targeting this unit (max 5)
   PL:

## [a1c8p1] Pasywka wroga: Passives_Enemy-a1c8p1
- plik gry: `Passives_Enemy-a1c8p1.json`

316. [[a1c8p1] Pasywka wroga [9020301] — nazwa] 수월한 임무
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020301].name
   limit: do 40 znaków
   EN: Easy Money
   PL:
317. [[a1c8p1] Pasywka wroga [9020301] — opis] 턴 종료 시, 이번 턴에 공격이 적중했다면 다음 턴에 [Enhancement] 1 을 얻음\n대상이 홍루라면, 다음 턴에 [ParryingResultUp] 1, [AttackDmgUp] 1을 추가로 얻음
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020301].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [ParryingResultUp], [AttackDmgUp]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: If this unit hit a target this turn, gain 1 [Enhancement] next turn\nIf the target is Hong Lu, gain 1 [ParryingResultUp] and 1 [AttackDmgUp] next turn as well
   PL:
318. [[a1c8p1] Pasywka wroga [9020302] — nazwa] 이게 아닌데
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020302].name
   limit: do 40 znaków
   EN: oh no
   PL:
319. [[a1c8p1] Pasywka wroga [9020302] — opis] 합 패배 시, 정신력 5 감소\n흐트러짐 시, 다음 턴에 [Vulnerable] 2를 얻음 (턴 당 1회)
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020302].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Lose 5 SP on Clash Lose\nWhen Staggered, gain 2 [Vulnerable] next turn (once per turn)
   PL:
320. [[a1c8p1] Pasywka wroga [9020101] — nazwa] 훈련용 인형
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020101].name
   limit: do 40 znaków
   EN: Training Dummy
   PL:
321. [[a1c8p1] Pasywka wroga [9020101] — opis] 받은 피해가 최소 10 이상이어야 피해를 받음\n그 이하의 피해는 0으로 받음
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Can be damaged only with damages equal to or higher than 10\nAll damage under 10 is nullified
   PL:
322. [[a1c8p1] Pasywka wroga [9020102] — nazwa] 성장하는 훈련용 인형
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020102].name
   limit: do 40 znaków
   EN: Upgradable Training Dummy
   PL:
323. [[a1c8p1] Pasywka wroga [9020102] — opis] 턴 종료 시 스킬 적중을 성공하지 못했으면, 성공하지 못한 턴 수만큼 다음 턴에 [ParryingResultUp] 얻음\n적에게 스킬 적중 시 누적된 값이 초기화됨
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020102].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn End: if this unit failed to hit with a Skill, gain [ParryingResultUp] next turn equal to the number of turns this unit failed to hit\nIf this unit hits an enemy with a Skill, reset the above stack
   PL:
324. [[a1c8p1] Pasywka wroga [9020103] — nazwa] 기본기 다지기
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020103].name
   limit: do 40 znaków
   EN: Remember the Basics
   PL:
325. [[a1c8p1] Pasywka wroga [9020103] — opis] 턴 종료 시, 공격 스킬 4개 이상에 피격 당했으면, 자신을 공격한 모든 적에게 피격당한 턴 수만큼 다음 턴에 [AttackDmgUp] 1 부여\n공격 스킬 3개 이하에 피격 당했다면, 누적된 값이 초기화됨
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020103].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: if this unit was hit by 4 or more Attack Skills, to all enemies that attacked this unit, apply 1 [AttackDmgUp] next turn for every turn this unit was hit\nIf this unit was hit by 3 or fewer Attack Skills, reset the above stack
   PL:
326. [[a1c8p1] Pasywka wroga [9019501] — nazwa] 엇나간 저주
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019501].name
   limit: do 40 znaków
   EN: Off-mark Curse
   PL:
327. [[a1c8p1] Pasywka wroga [9019501] — opis] 흐트러짐 상태가 되었을 때, 마지막으로 공격한 대상의 [Burst] 위력과 [Burst] 횟수가 절반으로 감소함
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019501].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: When this unit is Staggered, halve the [Burst] Potency and [Burst] Count on the target this unit hit last
   PL:
328. [[a1c8p1] Pasywka wroga [9019502] — nazwa] 단지에 깃든 저주
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019502].name
   limit: do 40 znaków
   EN: Jar-haunting Curse
   PL:
329. [[a1c8p1] Pasywka wroga [9019502] — opis] 턴 종료 시, 이번 턴에 스킬 적중했다면 다음 턴에 [Enhancement] 1 얻음\n자신이 스스로 사망할 경우, 다음 턴에 모든 아군에게 [Enhancement] 1 부여
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019502].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn End: If this unit hit a target this turn, gain 1 [Enhancement] next turn\nIf this unit kills itself, apply 1 [Enhancement] to all allies
   PL:
330. [[a1c8p1] Pasywka wroga [9019601] — nazwa] 단지에 깃든 저주
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019601].name
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [[a1c8p1] Pasywka wroga [9019601] — opis] 스킬 적중 시, 대상의 남은 [Burst] 횟수가 1이라면, [Burst] 횟수 1 증가 (턴 당 2회)\n공격 적중 시, 대상의 남은 [Burst]이 1이라면, [Burst] 2 부여 (턴 당 2회)\n자신이 스스로 사망할 경우, 모든 적에게 [Burst] 2 부여, [Burst] 횟수 1 증가
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019601].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: On Skill hit: if target has 1 remaining [Burst] Count, inflict +1 [Burst] Count (2 times per turn)\nOn Hit: if target has 1 remaining [Burst], inflict 2 [Burst] (2 times per turn)\nIf this unit kills itself, inflict 2 [Burst] and +1 [Burst] Count on all enemies
   PL:
332. [[a1c8p1] Pasywka wroga [9019701] — nazwa] 단지에 깃든 저주
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019701].name
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [[a1c8p1] Pasywka wroga [9019701] — opis] 스킬 적중 시, [Burst]이 4 이상인 대상이라면, 다음 턴에 [DefenseDown] 1 부여 (턴 당 3회)\n자신이 스스로 사망할 경우, 다음 턴에 모든 적에게 [DefenseDown] 3 부여
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019701].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: On Skill hit: if target has 4+ [Burst], inflict 1 [DefenseDown] next turn (3 times per turn)\nIf this unit kills itself, inflict 3 [DefenseDown] on all enemies
   PL:
334. [[a1c8p1] Pasywka wroga [9102201] — nazwa] 엇나간 저주
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102201].name
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [[a1c8p1] Pasywka wroga [9102201] — opis] 흐트러짐 상태가 되었을 때, 마지막으로 공격한 대상의 [Burst] 위력과 [Burst] 횟수가 전부 감소
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102201].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: When this unit is Staggered, eliminate the [Burst] Potency and [Burst] Count on the target this unit hit last
   PL:
336. [[a1c8p1] Pasywka wroga [9102202] — nazwa] 주귀 단지
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102202].name
   limit: do 40 znaków
   EN: Cursed Spirit Jar
   PL:
337. [[a1c8p1] Pasywka wroga [9102202] — opis] 적중시 대상의 ([Burst] 위력 + [Burst] 횟수)가 5 이상이면, [DefenseDown] 1 부여 (턴 당 최대 5)
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102202].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: On Hit, if the target has 5+ ([Burst] Potency + [Burst] Count), inflict 1 [DefenseDown] (5 times per turn)
   PL:
338. [[a1c8p1] Pasywka wroga [9102203] — nazwa] 단지에 깃든 저주
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102203].name
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [[a1c8p1] Pasywka wroga [9102203] — opis] 턴 종료 시, 등장하고 진행된 턴 수에 따라 모든 적에게 [Poison]을 부여함 (최대 5)\n자신이 스스로 사망할 경우, 다음 턴에 모든 적에게 (진행된 턴 x 5)만큼 [Poison]을 부여함 (최대 25), [Burst] 횟수 2 증가
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102203].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Poison], [Burst]
   znaczenie tagów: [Poison] = 독 / Poison; [Burst] = 파열 / Rupture
   EN: Turn End: against all enemies, inflict [Poison] equal to the number of turns that passed since this unit joined the battle (max 5)\nIf this unit kills itself, apply (# of turns x 5) [Poison] and inflict +2 [Burst] Count on all enemies next turn (max 25)
   PL:
340. [[a1c8p1] Pasywka wroga [9019801] — nazwa] 그간의 피해
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019801].name
   limit: do 40 znaków
   EN: Damage Taken
   PL:
341. [[a1c8p1] Pasywka wroga [9019801] — opis] 전투 중 피격당했을 때, 해당 턴동안 가하는 피해량 +10%\n전투 중 피격당했을 때, 합 승리시, 가하는 피해량 +20%
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019801].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit during the combat phase: +10% damage for the turn\nWhen hit during the combat phase: on Clash Win, +20% damage
   PL:
342. [[a1c8p1] Pasywka wroga [9019802] — nazwa] 목표 - 가보옥
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019802].name
   limit: do 40 znaków
   EN: Target - Jia Baoyu
   PL:
343. [[a1c8p1] Pasywka wroga [9019802] — opis] 홍루를 우선 공격함
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019802].desc
   limit: do 120 znaków
   EN: Prioritizes Hong Lu
   PL:
344. [[a1c8p1] Pasywka wroga [9019803] — nazwa] 또렷해지는 목표
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019803].name
   limit: do 40 znaków
   EN: Focusing on Target
   PL:
345. [[a1c8p1] Pasywka wroga [9019803] — opis] 자신의 체력이 70% 이상일 때, 턴 종료 시, 홍루에게 스킬이 적중하지 못했다면 다음 턴에 [Reduction] 1 얻음\n자신의 체력이 70% 미만일 때, 턴 종료 시, 홍루에게 스킬이 적중하지 못했다면, 다음 턴동안 부여하는 [Laceration], [Laceration] 횟수 +1
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9019803].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Reduction], [Laceration]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down; [Laceration] = 출혈 / Bleed
   EN: At 70%+ HP: at Turn End, if this unit failed to hit Hong Lu with a Skill, gain 1 [Reduction] next turn\nAt less than 70% HP: at Turn End, if this unit failed to hit Hong Lu with a Skill, inflict +1 more [Laceration] and [Laceration] Count next turn
   PL:
346. [[a1c8p1] Pasywka wroga [9020001] — nazwa] 임무 수행
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020001].name
   limit: do 40 znaków
   EN: Mission Progress
   PL:
347. [[a1c8p1] Pasywka wroga [9020001] — opis] 자신의 잃은 체력 1%당 가하는 피해량 +0.5% (최대 50%)
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020001].desc
   limit: do 120 znaków
   EN: Deal +0.5% damage for every 1% missing HP on self (max 50%)
   PL:
348. [[a1c8p1] Pasywka wroga [9020002] — nazwa] 뚜렷해지는 목표
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020002].name
   limit: do 40 znaków
   EN: Honing in on Target
   PL:
349. [[a1c8p1] Pasywka wroga [9020002] — opis] 자신의 체력이 70% 이상일 때, 턴 종료 시, 홍루에게 스킬이 적중하지 못했다면 다음 턴에 [Reduction] 1 얻음\n자신의 체력이 70% 미만일 때, 턴 종료 시, 홍루에게 스킬이 적중하지 못했다면, 다음 턴에 [Enhancement] 1 얻음\n- 다음 턴동안 부여하는 [Laceration], [Laceration] 횟수 +1
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9020002].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Reduction], [Enhancement], [Laceration]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Laceration] = 출혈 / Bleed
   EN: At 70%+ HP: at Turn End, if this unit failed to hit Hong Lu with a Skill, gain 1 [Reduction] next turn\nAt less than 70% HP: at Turn End, if this unit failed to hit Hong Lu with a Skill, gain 1 [Enhancement] next turn\n- inflict +1 more [Laceration] and [Laceration] Count next turn
   PL:
350. [[a1c8p1] Pasywka wroga [9102101] — nazwa] 그간의 피해
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102101].name
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [[a1c8p1] Pasywka wroga [9102101] — opis] 전투 중 피격당했을 때, 해당 턴동안 가하는 피해량 +20%\n전투 중 합 패배시 해당 스킬로부터 받는 피해량 +15%
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102101].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit during the combat phase: +20% damage for the turn\nDuring the combat phase: On Clash Lose, take +15% damage from the Skill
   PL:
352. [[a1c8p1] Pasywka wroga [9102102] — nazwa] 만취 수행
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102102].name
   limit: do 40 znaków
   EN: Plastered Training
   PL:
353. [[a1c8p1] Pasywka wroga [9102102] — opis] 자신의 잃은 체력 1%당 가하는 피해량 +2% (최대 100%)
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102102].desc
   limit: do 120 znaków
   EN: Deal +2% damage for every 1% missing HP on self (max 100%)
   PL:
354. [[a1c8p1] Pasywka wroga [9102103] — nazwa] 이런 이런… 딸꾹 이러면 안되겠지
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102103].name
   limit: do 50 znaków
   EN: Well, well... Hic. This won't do
   PL:
355. [[a1c8p1] Pasywka wroga [9102103] — opis] 자신의 체력이 50% 남았을 때, 흐트러짐 상태를 해제하고 이번 턴을 종료함.\n다음 턴에 속도가 10으로 고정됨
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 50% HP, recover from Stagger and end this turn.\nFix this unit's Speed to 10 next turn
   PL:
356. [[a1c8p1] Pasywka wroga [9102104] — nazwa] 확고해진 목표
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102104].name
   limit: do 40 znaków
   EN: Clear Target
   PL:
357. [[a1c8p1] Pasywka wroga [9102104] — opis] 자신의 체력이 70% 이상일 때, 턴 종료 시, 홍루에게 스킬이 적중하지 못했다면, 다음 턴에 [AttackDown] 3 얻음\n자신의 체력이 70% 미만일 때, 턴 종료 시, 홍루에게 스킬이 적중하지 못했다면, 다음 턴에 [AttackUp] 6 얻음
   źródło: Passives_Enemy-a1c8p1.json :: dataList[id=9102104].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDown], [AttackUp]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: At 70%+ HP: at Turn End, if this unit failed to hit Hong Lu with a Skill, gain 3 [AttackDown] next turn\nAt less than 70% HP: at Turn End, if this unit failed to hit Hong Lu with a Skill, gain 6 [AttackUp] next turn
   PL:

## [a1c8p2] Wróg / część: Enemies-a1c8p2
- plik gry: `Enemies-a1c8p2.json`

358. [[a1c8p2] Wróg / część [90205] — nazwa] 내리박힌 실패작
   źródło: Enemies-a1c8p2.json :: dataList[id=90205].name
   limit: do 40 znaków
   EN: Impaled Failure
   PL:
359. [[a1c8p2] Wróg / część [90205] — opis] 잡몹
   źródło: Enemies-a1c8p2.json :: dataList[id=90205].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [[a1c8p2] Wróg / część [90206] — nazwa] 피어난 실패작
   źródło: Enemies-a1c8p2.json :: dataList[id=90206].name
   limit: do 40 znaków
   EN: Blooming Failure
   PL:
361. [[a1c8p2] Wróg / część [90206] — opis] 잡몹
   źródło: Enemies-a1c8p2.json :: dataList[id=90206].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [[a1c8p2] Wróg / część [90207] — nazwa] 얽힌 실패작
   źródło: Enemies-a1c8p2.json :: dataList[id=90207].name
   limit: do 40 znaków
   EN: Entangled Failure
   PL:
363. [[a1c8p2] Wróg / część [90207] — opis] 잡몹
   źródło: Enemies-a1c8p2.json :: dataList[id=90207].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [[a1c8p2] Wróg / część [90208] — nazwa] 사특한 주살승
   źródło: Enemies-a1c8p2.json :: dataList[id=90208].name
   limit: do 40 znaków
   EN: Wicked Deathrite Monk
   PL:
365. [[a1c8p2] Wróg / część [90208] — opis] 잡몹
   źródło: Enemies-a1c8p2.json :: dataList[id=90208].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [[a1c8p2] Wróg / część [90209] — nazwa] 귀기 어린 주살승
   źródło: Enemies-a1c8p2.json :: dataList[id=90209].name
   limit: do 50 znaków
   EN: Evil-possessed Deathrite Monk
   PL:
367. [[a1c8p2] Wróg / część [90209] — opis] 잡몹
   źródło: Enemies-a1c8p2.json :: dataList[id=90209].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [[a1c8p2] Wróg / część [1137] — nazwa] 가치우
   źródło: Enemies-a1c8p2.json :: dataList[id=1137].name
   limit: do 40 znaków
   EN: Jia Qiu
   PL:
369. [[a1c8p2] Wróg / część [1133] — nazwa] 자로
   źródło: Enemies-a1c8p2.json :: dataList[id=1133].name
   limit: do 40 znaków
   EN: Zilu
   PL:
370. [[a1c8p2] Wróg / część [1141] — nazwa] 가치우
   źródło: Enemies-a1c8p2.json :: dataList[id=1141].name
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [[a1c8p2] Wróg / część [1157] — nazwa] 설반
   źródło: Enemies-a1c8p2.json :: dataList[id=1157].name
   limit: do 40 znaków
   EN: Xue Pan
   PL:
372. [[a1c8p2] Wróg / część [1158] — nazwa] 사이화
   źródło: Enemies-a1c8p2.json :: dataList[id=1158].name
   limit: do 40 znaków
   EN: Shi Yihua
   PL:
373. [[a1c8p2] Wróg / część [90210] — nazwa] 날렵한 사씨 가문 사병
   źródło: Enemies-a1c8p2.json :: dataList[id=90210].name
   limit: do 40 znaków
   EN: Swift Shi Family Mercenary
   PL:
374. [[a1c8p2] Wróg / część [90211] — nazwa] 능숙한 사씨 가문 사병
   źródło: Enemies-a1c8p2.json :: dataList[id=90211].name
   limit: do 40 znaków
   EN: Veteran Shi Family Mercenary
   PL:
375. [[a1c8p2] Wróg / część [90212] — nazwa] 묵직한 사씨 가문 사병
   źródło: Enemies-a1c8p2.json :: dataList[id=90212].name
   limit: do 40 znaków
   EN: Heavy Shi Family Mercenary
   PL:
376. [[a1c8p2] Wróg / część [1159] — nazwa] 왕청산
   źródło: Enemies-a1c8p2.json :: dataList[id=1159].name
   limit: do 40 znaków
   EN: Wang Qingshan
   PL:
377. [[a1c8p2] Wróg / część [115901] — nazwa] 몸통
   źródło: Enemies-a1c8p2.json :: dataList[id=115901].name
   limit: do 40 znaków
   EN: Body
   PL:
378. [[a1c8p2] Wróg / część [1167] — nazwa] 사화?
   źródło: Enemies-a1c8p2.json :: dataList[id=1167].name
   limit: do 40 znaków
   EN: Shi Hua... something?
   PL:
379. [[a1c8p2] Wróg / część [1160] — nazwa] 사사정
   źródło: Enemies-a1c8p2.json :: dataList[id=1160].name
   limit: do 40 znaków
   EN: Shi Sijing
   PL:
380. [[a1c8p2] Wróg / część [1179] — nazwa] 사화정
   źródło: Enemies-a1c8p2.json :: dataList[id=1179].name
   limit: do 40 znaków
   EN: Shi Huazhen
   PL:

## [a1c8p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c8p2
- grupa rozdziału/trybu: `a1c8p2` · plik: `Skills_Abnormality-a1c8p2.json`

381. [Umiejętność wroga [113101] (ulepszenie 1) — nazwa] 초격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113101].levelList[level=1].name
   limit: do 40 znaków
   EN: Startling Strike
   PL:
382. [Umiejętność wroga [113101] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 3 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 3+ [Burst], Clash Power +1
   PL:
383. [Umiejętność wroga [113101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność wroga [113102] (ulepszenie 1) — nazwa] 억제
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113102].levelList[level=1].name
   limit: do 40 znaków
   EN: Restraint
   PL:
385. [Umiejętność wroga [113102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113102].levelList[level=1].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność wroga [113102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [113102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [113102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [113102] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 (속도 / 3)만큼 이 코인을 재사용함 (최대 2번)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113102].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Reuse this Coin (this unit's Speed / 3) times (max 2)
   PL:
390. [Umiejętność wroga [113103] (ulepszenie 1) — nazwa] 쾌격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].name
   limit: do 40 znaków
   EN: Feather Strike
   PL:
391. [Umiejętność wroga [113103] (ulepszenie 1) — opis] 자신의 속도가 메인 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the main target's gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 3)\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +3 [Burst] Count
   PL:
392. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL:
395. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상에게 [BurstAgility]이 있으면, 피해량 +50%
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstAgility]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: If target has [BurstAgility], deal +50% damage
   PL:
397. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [LegStrength] 3 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [LegStrength]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [UnBrokenCoinOnSucceedAttack] Gain 3 [LegStrength]
   PL:
398. [Umiejętność wroga [113103] (ulepszenie 1) — moneta 3, efekt 4 — opis] [WinDuelAttack] 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113103].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] Reuse this Coin once (once per Skill)
   PL:
399. [Umiejętność wroga [113104] (ulepszenie 1) — nazwa] 준비 동작
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113104].levelList[level=1].name
   limit: do 40 znaków
   EN: Windup
   PL:
400. [Umiejętność wroga [113104] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility]을 3 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 3 [Agility] next turn
   PL:
401. [Umiejętność wroga [113201] (ulepszenie 1) — nazwa] 추격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113201].levelList[level=1].name
   limit: do 40 znaków
   EN: Pursuit
   PL:
402. [Umiejętność wroga [113201] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 3 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113201].levelList[level=1].desc
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [113201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność wroga [113202] (ulepszenie 1) — nazwa] 압도
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113202].levelList[level=1].name
   limit: do 40 znaków
   EN: Overwhelm
   PL:
405. [Umiejętność wroga [113202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113202].levelList[level=1].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Umiejętność wroga [113202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność wroga [113202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Umiejętność wroga [113202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Umiejętność wroga [113202] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 (속도 / 3)만큼 이 코인을 재사용함 (최대 2번)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113202].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [113203] (ulepszenie 1) — nazwa] 암격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].name
   limit: do 40 znaków
   EN: Umbra Strike
   PL:
411. [Umiejętność wroga [113203] (ulepszenie 1) — opis] 자신의 속도가 메인 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].desc
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상에게 [BurstAgility]이 있으면, 피해량 +50%
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [LegStrength] 3 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [113203] (ulepszenie 1) — moneta 3, efekt 4 — opis] [WinDuelAttack] 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113203].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [113204] (ulepszenie 1) — nazwa] 준비 동작
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113204].levelList[level=1].name
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Umiejętność wroga [113204] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility]을 3 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113204].levelList[level=1].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Umiejętność wroga [113701] (ulepszenie 1) — nazwa] 문(問)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113701].levelList[level=1].name
   limit: do 40 znaków
   EN: Question (問)
   PL:
422. [Umiejętność wroga [113701] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Burst], Coin Power +1
   PL:
423. [Umiejętność wroga [113701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Umiejętność wroga [113702] (ulepszenie 1) — nazwa] 답(答)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113702].levelList[level=1].name
   limit: do 40 znaków
   EN: Answer (答)
   PL:
425. [Umiejętność wroga [113702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113702].levelList[level=1].desc
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [113702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL:
427. [Umiejętność wroga [113703] (ulepszenie 1) — nazwa] 비례물동(非禮勿動)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].name
   limit: do 50 znaków
   EN: Act Not With Impropriety (非禮勿動)
   PL:
428. [Umiejętność wroga [113703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 횟수 2당, 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 4 [Burst] on target (max 2)\n[WhenUse] Clash Power +1 for every 2 [Burst] Count on target (max 3)
   PL:
429. [Umiejętność wroga [113703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [113703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [WinDuelAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Binding]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Binding] = 속박 / Bind
   EN: [WinDuelAttack] Inflict 1 [Binding] next turn
   PL:
431. [Umiejętność wroga [113703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [113703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność wroga [113703] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BurstStop] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113703].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstStop]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstStop] = 주살【물동】 / Deathrite 【Halt】
   EN: [OnSucceedAttack] Inflict [BurstStop]
   PL:
434. [Umiejętność wroga [113704] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113704].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL:
435. [Umiejętność wroga [113704] (ulepszenie 1) — opis] 이 스킬을 사용하지 못했다면, 다음 턴에 [Binding] 1 얻음\n[WhenUse] 대상의 [Burst] 2당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113704].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [WhenUse], [Burst]
   znaczenie tagów: [Binding] = 속박 / Bind; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: If this unit failed to use this Skill, gain 1 [Binding] next turn\n[WhenUse] Coin Power +1 for every 2 [Burst] on target (max 3)
   PL:
436. [Umiejętność wroga [113705] (ulepszenie 1) — nazwa] 뇌정만균
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113705].levelList[level=1].name
   limit: do 40 znaków
   EN: Thunderstrike
   PL:
437. [Umiejętność wroga [113705] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 5+ [Burst], Coin Power +1\n[WinDuel] Inflict +2 [Burst] Count
   PL:
438. [Umiejętność wroga [113705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [113705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstWave] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstWave]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstWave] = 주살【즉감】 / Deathrite 【Wane】
   EN: [OnSucceedAttack] Inflict [BurstWave]
   PL:
440. [Umiejętność wroga [113706] (ulepszenie 1) — nazwa] 베어라. 묘
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113706].levelList[level=1].name
   limit: do 40 znaków
   EN: Cut them Down, Mao
   PL:
441. [Umiejętność wroga [113706] (ulepszenie 1) — opis] [WhenUse] 정신력 10 회복\n[WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113706].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Heal 10 SP\n[WhenUse] If target has 5+ [Burst], Coin Power +1\n[WinDuel] Inflict 2 [Burst]
   PL:
442. [Umiejętność wroga [113706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [113706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [113706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [113706] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BurstSuppress] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113706].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstSuppress]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstSuppress] = 주살【철주】 / Deathrite 【Impede】
   EN: [OnSucceedAttack] Inflict [BurstSuppress]
   PL:
446. [Umiejętność wroga [113707] (ulepszenie 1) — nazwa] 좀 더 몰아쳐야겠구나
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].name
   limit: do 40 znaków
   EN: I Must Push You Further
   PL:
447. [Umiejętność wroga [113707] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 횟수 2당, 합 위력 +1 (최대 3)\n[WinDuel] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 4 [Burst] on target (max 2)\n[WhenUse] Clash Power +1 for every 2 [Burst] Count on target (max 3)\n[WinDuel] Inflict 2 [Burst] and +2 [Burst] Count
   PL:
448. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 4 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +4 [Burst] Count
   PL:
450. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Burst]
   PL:
452. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [113707] (ulepszenie 1) — moneta 4, efekt 2 — opis] 대상의 ([Burst] 위력 + [Burst] 횟수)당 피해량 +5% (최대 200%)\n[OnSucceedAttack] 대상의 모든 주살을 0으로 만듦
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113707].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [OnSucceedAttack]
   znaczenie tagów: [Burst] = 파열 / Rupture; [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Deal +5% damage for every ([Burst] Potency on target + [Burst] Count on target) (max 200%)\n[OnSucceedAttack] Reduce all Deathrites on target to 0
   PL:
455. [Umiejętność wroga [113708] (ulepszenie 1) — nazwa] 나서지 마라
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113708].levelList[level=1].name
   limit: do 40 znaków
   EN: Do Not Meddle
   PL:
456. [Umiejętność wroga [113708] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 3)\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113708].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 4 [Burst] on target (max 3)\n[WinDuel] Inflict +2 [Burst] Count
   PL:
457. [Umiejętność wroga [113708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [113708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność wroga [113708] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstWave] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113708].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [113301] (ulepszenie 1) — nazwa] 초격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113301].levelList[level=1].name
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [113301] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Burst], Clash Power +1
   PL:
462. [Umiejętność wroga [113301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [113302] (ulepszenie 1) — nazwa] 척살
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113302].levelList[level=1].name
   limit: do 40 znaków
   EN: Perforating Kill
   PL:
464. [Umiejętność wroga [113302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1\n[WhenUse] [LegStrength] 3 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [LegStrength]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [WhenUse] If target has 5+ [Burst], Coin Power +1\n[WhenUse] Gain 3 [LegStrength]
   PL:
465. [Umiejętność wroga [113302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność wroga [113302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstAgility]이 있으면, 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] If target has [BurstAgility], gain 1 [Agility] next turn
   PL:
467. [Umiejętność wroga [113303] (ulepszenie 1) — nazwa] 표각
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113303].levelList[level=1].name
   limit: do 40 znaków
   EN: Etching Strike
   PL:
468. [Umiejętność wroga [113303] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113303].levelList[level=1].desc
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność wroga [113303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność wroga [113303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność wroga [113303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność wroga [113304] (ulepszenie 1) — nazwa] 각주살검 - 순보
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].name
   limit: do 50 znaków
   EN: Cursewrit Butcherblade - Blinkstep
   PL:
473. [Umiejętność wroga [113304] (ulepszenie 1) — opis] [BurstAgility]이 있는 대상을 우선 공격함\n[StartBattle] [SupportProtect] 1 얻음\n자신과 대상의 속도 차이 2 당 피해량 +15% (최대 60%)\n[WhenUse] 대상의 [Burst] 5 당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 횟수 2 당, 기본 위력 +1 (최대 3)\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [BurstAgility], [StartBattle], [SupportProtect], [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Prioritizes targets with [BurstAgility]\n[StartBattle] Gain 1 [SupportProtect]\nDeal +15% damage for every 2 Speed difference between this unit and the target (max 60%)\n[WhenUse] Coin Power +1 for every 5 [Burst] on the target (max 2)\n[WhenUse] Base Power +1 for every 2 [Burst] Count on the target (max 3)\n[WinDuel] Inflict +2 [Burst] Count
   PL:
474. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL:
478. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상에게 [BurstAgility]이 있으면, 피해량 +50%
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność wroga [113304] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113304].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Reuse this Coin once (once per Skill)
   PL:
482. [Umiejętność wroga [113305] (ulepszenie 1) — nazwa] 각주
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113305].levelList[level=1].name
   limit: do 40 znaków
   EN: Cursewrit
   PL:
483. [Umiejętność wroga [113305] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 대상보다 3 이상 빠르면, 합 위력 +1\n[WhenUse] 대상에게 [BurstAgility]이 있으면, 이 스킬에서 부여하는 [Burst] 횟수 1 추가 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113305].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BurstAgility], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [Burst] = 파열 / Rupture
   EN: [WhenUse] If this unit's Speed is faster than the target's by 3 or more, Clash Power +1\n[WhenUse] If target has [BurstAgility], inflict +1 more [Burst] Count with this Skill
   PL:
484. [Umiejętność wroga [113305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Umiejętność wroga [113305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Umiejętność wroga [113305] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [113306] (ulepszenie 1) — nazwa] 금제 부분 해방 : <천구성도>
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].name
   limit: do 70 znaków
   EN: Incomplete Seal Release: <Tianjiu Star's Blade>
   PL:
488. [Umiejętność wroga [113306] (ulepszenie 1) — opis] 자신과 대상의 속도 차이 2 당 피해량 +20% (최대 60%)\n[WhenUse] 대상의 [Burst] 5 당, 코인 위력 +1 (최대 3)\n[WhenUse] 대상의 [Burst] 횟수 2 당, 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: +20% damage for every 2 Speed difference between this unit and the target (max 60%)\n[WhenUse] Coin Power +1 for every 5 [Burst] on target (max 3)\n[WhenUse] Clash Power +1 for every 2 [Burst] Count on target (max 3)
   PL:
489. [Umiejętność wroga [113306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność wroga [113306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst] Count
   PL:
491. [Umiejętność wroga [113306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Umiejętność wroga [113306] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Burst]
   PL:
493. [Umiejętność wroga [113306] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [113306] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113306].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstZilu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [OnSucceedAttack] Inflict [BurstZilu]
   PL:
495. [Umiejętność wroga [114101] (ulepszenie 1) — nazwa] 다시 물으마
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114101].levelList[level=1].name
   limit: do 40 znaków
   EN: I Ask Again
   PL:
496. [Umiejętność wroga [114101] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 합 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 5+ [Burst], Clash Power +1\n[WinDuel] Inflict +2 [Burst] Count
   PL:
497. [Umiejętność wroga [114101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Umiejętność wroga [114101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Umiejętność wroga [114102] (ulepszenie 1) — nazwa] 비례물동(非禮勿動)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114102].levelList[level=1].name
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [114102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 합 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114102].levelList[level=1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [114102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność wroga [114102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Umiejętność wroga [114102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstStop] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność wroga [114103] (ulepszenie 1) — nazwa] 나서지 마라
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114103].levelList[level=1].name
   limit: do 40 znaków
   EN: You Will Not Meddle
   PL:
505. [Umiejętność wroga [114103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 합 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114103].levelList[level=1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność wroga [114103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność wroga [114103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność wroga [114103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstSuppress] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność wroga [114104] (ulepszenie 1) — nazwa] 뇌정만균 - 파(波)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114104].levelList[level=1].name
   limit: do 40 znaków
   EN: Thunderstrike - Ripple (波)
   PL:
510. [Umiejętność wroga [114104] (ulepszenie 1) — opis] 주살 종류를 가장 많이 가진 대상 우선 공격\n[WhenUse] 메인 타겟의 [Burst] 2당, 코인 위력 +1 (최대 4)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114104].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: Prioritizes targets with the most types of Deathrite\n[WhenUse] Coin Power +1 for every 2 [Burst] on the main target (max 4)
   PL:
511. [Umiejętność wroga [114104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność wroga [114104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 주살이 2종류 이상 있는 대상일 경우, [BurstWave] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstWave]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstWave] = 주살【즉감】 / Deathrite 【Wane】
   EN: [OnSucceedAttack] If the target has 2+ types of Deathrite, inflict [BurstWave]
   PL:
513. [Umiejętność wroga [114105] (ulepszenie 1) — nazwa] 흑수 묘 연계 - 난격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].name
   limit: do 60 znaków
   EN: Heishou - Mao Linkstrike - Bladestorm
   PL:
514. [Umiejętność wroga [114105] (ulepszenie 1) — opis] [WhenUse] 정신력 10 회복\n[WhenUse] 대상의 [Burst] 5 당, 코인 위력 +1 (최대 2)\n[WinDuel] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Heal 10 SP\n[WhenUse] Coin Power +1 for every 5 [Burst] on target (max 2)\n[WinDuel] Inflict 2 [Burst]
   PL:
515. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [114105] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114105].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność wroga [114106] (ulepszenie 1) — nazwa] 자로여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].name
   limit: do 40 znaków
   EN: Heed Me, Zilu
   PL:
524. [Umiejętność wroga [114106] (ulepszenie 1) — opis] [WhenUse] 정신력 10 회복\n[WhenUse] 대상의 [Burst] 5 당, 코인 위력 +1 (최대 2)\n[WinDuel] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].desc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność wroga [114106] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114106].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność wroga [114107] (ulepszenie 1) — nazwa] 주살 쇄도
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114107].levelList[level=1].name
   limit: do 40 znaków
   EN: Deathrite Deluge
   PL:
534. [Umiejętność wroga [114107] (ulepszenie 1) — opis] [CantChangeTarget]\n주살 종류를 가장 많이 가진 대상우선 공격\n[WhenUse] 대상의 주살 수당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114107].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]
   EN: [CantChangeTarget]\nPrioritizes targets with the most types of Deathrite\n[WhenUse] Coin Power +1 for every type of Deathrite on target (max 3)
   PL:
535. [Umiejętność wroga [114107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność wroga [114107] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상의 ([Burst] 위력 + [Burst] 횟수 + 보유한 주살 종류)당 피해량 +5% (최대 200%)\n[OnSucceedAttack] 대상의 모든 주살을 0으로 만듦
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [OnSucceedAttack]
   znaczenie tagów: [Burst] = 파열 / Rupture; [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Deal +5% damage for every ([Burst] Potency on target + [Burst] Count on target + number of Deathrite types on target) (max 200%)\n[OnSucceedAttack] Reduce all Deathrites on target to 0
   PL:
537. [Umiejętność wroga [114108] (ulepszenie 1) — nazwa] 답하라, 가보옥
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].name
   limit: do 40 znaków
   EN: Answer Me, Jia Baoyu
   PL:
538. [Umiejętność wroga [114108] (ulepszenie 1) — opis] [CantChangeTarget]\n홍루를 우선 공격함\n[WinDuel] [Burst] 횟수 4 증가\n[DefeatDuel] 대상이 홍루면, [Teaching] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WinDuel], [Burst], [DefeatDuel], [Teaching]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [Teaching] = 문답 / Dialogues
   EN: [CantChangeTarget]\nPrioritizes Hong Lu\n[WinDuel] Inflict +4 [Burst] Count\n[DefeatDuel] If the target is Hong Lu, inflict 1 [Teaching]
   PL:
539. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst]
   PL:
541. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność wroga [114108] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114108].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Umiejętność wroga [114109] (ulepszenie 1) — nazwa] 천강성 - 격(格)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].name
   limit: do 40 znaków
   EN: Tiangang Star - Form (格)
   PL:
548. [Umiejętność wroga [114109] (ulepszenie 1) — opis] 홍루를 우선 공격함\n대상의 [Teaching]당, 코인 위력 -2\n[DefeatDuel] 이 공격으로 흐트러짐 상태가 되지 않음. 이번 전투동안 [DefenseDown] 24 얻음\n[DefeatDuel] 피해량이 50%만큼 감소함
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Teaching], [DefeatDuel], [DefenseDown]
   znaczenie tagów: [Teaching] = 문답 / Dialogues; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Prioritizes Hong Lu\nCoin Power -2 for every [Teaching] on target\n[DefeatDuel] Cannot Stagger with this attack. Gain 24 [DefenseDown] for this Encounter\n[DefeatDuel] Deal -50% damage
   PL:
549. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [114109] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 ([Burst] 위력 + [Burst] 횟수 + 보유한 주살 종류)당 피해량 +5% (최대 100%)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114109].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Deal +5% damage for every ([Burst] Potency on target + [Burst] Count on target + number of Deathrite types on target) (max 100%)
   PL:
557. [Umiejętność wroga [115701] (ulepszenie 1) — nazwa] 나약한 것..
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115701].levelList[level=1].name
   limit: do 40 znaków
   EN: Weaklings...
   PL:
558. [Umiejętność wroga [115701] (ulepszenie 1) — opis] [StartBattle] 속도가 가장 빠른 아군에게 [AttackDmgUp] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] Apply 2 [AttackDmgUp] to the fastest ally
   PL:
559. [Umiejętność wroga [115701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność wroga [115701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [115702] (ulepszenie 1) — nazwa] 우둔한 놈들..
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115702].levelList[level=1].name
   limit: do 40 znaków
   EN: Dolts...
   PL:
562. [Umiejętność wroga [115702] (ulepszenie 1) — opis] [StartBattle] 속도가 가장 느린 아군에게 다음 턴에 [Agility] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Agility] = 신속 / Haste
   EN: [StartBattle] Apply 2 [Agility] to the slowest ally next turn
   PL:
563. [Umiejętność wroga [115702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność wroga [115702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
565. [Umiejętność wroga [115703] (ulepszenie 1) — nazwa] 죽여버리겠어!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].name
   limit: do 40 znaków
   EN: I'm Gonna Kill You!
   PL:
566. [Umiejętność wroga [115703] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[WhenUse] 대상의 [Burst] 6 당, 코인 위력 +1 (최대 2)\n[DefeatDuel] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] If target has 3+ types of negative effects, Base Power +1\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)\n[DefeatDuel] Gain 1 [Vulnerable]
   PL:
567. [Umiejętność wroga [115703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność wroga [115703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność wroga [115703] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL:
570. [Umiejętność wroga [115703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [115703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność wroga [115703] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115703].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [115704] (ulepszenie 1) — nazwa] 뛰어들어라!!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115704].levelList[level=1].name
   limit: do 40 znaków
   EN: Jump In!!
   PL:
574. [Umiejętność wroga [115704] (ulepszenie 1) — opis] [WhenUse] 정신력 15 회복\n[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[EndSkill] 현재 체력이 가장 낮은 항아리 1개가 대상에게 ‘뛰어드는 금 간 항아리’ 스킬 발동 (흐트러짐 무시)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115704].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Heal 15 SP\n[WhenUse] If target has 3+ types of negative effects, Base Power +1\n[EndSkill] 1 Jar with the least current HP uses the Skill 'Leaping Cracked Jar' at the target (ignores Stagger)
   PL:
575. [Umiejętność wroga [115704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność wroga [115704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
577. [Umiejętność wroga [115704] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115704].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [115705] (ulepszenie 1) — nazwa] 좋은 구경은 더 해야지?
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115705].levelList[level=1].name
   limit: do 60 znaków
   EN: Let's Watch This Spectacle, All Together!
   PL:
579. [Umiejętność wroga [115705] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 항아리 2개 소환\n[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115705].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Summon 2 Jars next turn\n[WhenUse] If target has 3+ negative effects, Base Power +1
   PL:
580. [Umiejętność wroga [115705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [115705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [115705] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115705].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [115901] (ulepszenie 1) — nazwa] 부령술(符靈術) - 부격
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115901].levelList[level=1].name
   limit: do 60 znaków
   EN: Spirit Talisman School - Talisman Strike
   PL:
584. [Umiejętność wroga [115901] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 잃은 체력 30%당 합 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115901].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Final Power +1 for every 4 [Burst] on target (max 3)\n[WhenUse] Clash Power +1 for every 30% missing HP on self (max 2)
   PL:
585. [Umiejętność wroga [115901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst] and +2 [Burst] Count
   PL:
586. [Umiejętność wroga [115901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttack] Inflict 10 [OminousTalisman]
   PL:
587. [Umiejętność wroga [115902] (ulepszenie 1) — nazwa] 부령술(符靈術) - 효력 발동
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115902].levelList[level=1].name
   limit: do 60 znaków
   EN: Spirit Talisman School - Trigger Effect
   PL:
588. [Umiejętność wroga [115902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 잃은 체력 30%당 합 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115902].levelList[level=1].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność wroga [115902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +2 [Burst] Count
   PL:
590. [Umiejętność wroga [115902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [115902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [OminousTalisman] 2 소모
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttack] Reduce [OminousTalisman] on target by 2
   PL:
592. [Umiejętność wroga [115903] (ulepszenie 1) — nazwa] 부령술(符靈術) - 주살 인형
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115903].levelList[level=1].name
   limit: do 60 znaków
   EN: Spirit Talisman School - Deathrite Doll
   PL:
593. [Umiejętność wroga [115903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 4)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Final Power +1 for every 4 [Burst] on target (max 4)
   PL:
594. [Umiejętność wroga [115903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [115903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność wroga [115903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [OminousTalisman] 5 소모
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [UnBrokenCoinOnSucceedAttack] Reduce [OminousTalisman] on target by 5
   PL:
597. [Umiejętność wroga [115904] (ulepszenie 1) — nazwa] 부령술(符靈術) - 사기 폭주
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].name
   limit: do 50 znaków
   EN: Spirit Talisman School - Vilerage
   PL:
598. [Umiejętność wroga [115904] (ulepszenie 1) — opis] [StartBattle] 자신의 잃은 체력 20%당 가중치 +1 (최대 4)\n[WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 4)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해, 효과로 대상이 흐트러지지 않음\n[EndSkill] 이 스킬로 사망한 적이 있다면, 자신을 포함한 모든 아군에게 다음 턴에 [ResultEnhancement] 2, [AttackDmgUp] 2 부여 (턴당 1회)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Burst], [DefeatDuel], [EndSkill], [ResultEnhancement], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [ResultEnhancement] = 위력 증가 / Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] Atk Weight +1 for every 20% missing HP on self (max 4)\n[WhenUse] Final Power +1 for every 4 [Burst] on target (max 4\n[DefeatDuel] Deal -50% damage; this Skill cannot Stagger the target with damage or effect\n[EndSkill] If this Skill has defeated an enemy, apply 2 [ResultEnhancement] and 2 [AttackDmgUp] to all allies, including this unit, next turn (once per turn)
   PL:
599. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność wroga [115904] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [OminousTalisman] 전부 소모
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115904].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [UnBrokenCoinOnSucceedAttack] Remove all [OminousTalisman] on target
   PL:
607. [Umiejętność wroga [115801] (ulepszenie 1) — nazwa] 받아라!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115801].levelList[level=1].name
   limit: do 40 znaków
   EN: Take This!
   PL:
608. [Umiejętność wroga [115801] (ulepszenie 1) — opis] [WhenUse] 대상의 보유한 부정적인 효과 2개당 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Coin Power +1 for every 2 types of negative effect on target (max 2)
   PL:
609. [Umiejętność wroga [115801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MadFeather]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MadFeather] = 눈알 깃 / Eyeball Pinion
   EN: [OnSucceedAttack] Inflict 1 [MadFeather]
   PL:
610. [Umiejętność wroga [115801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność wroga [115801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [115801] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115801].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [115802] (ulepszenie 1) — nazwa] 무릎을 꿇으라!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].name
   limit: do 40 znaków
   EN: KNEEL!
   PL:
614. [Umiejętność wroga [115802] (ulepszenie 1) — opis] [CantIdentify]\n[WhenUse] 대상의 보유한 부정적인 효과 2개당 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]
   EN: [CantIdentify]\n[WhenUse] Coin Power +1 for every 2 types of negative effect on target (max 2)
   PL:
615. [Umiejętność wroga [115802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność wroga [115802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [115802] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [115802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [115802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [115802] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115802].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [115803] (ulepszenie 1) — nazwa] 네 놈 꼬라지를 봐라!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115803].levelList[level=1].name
   limit: do 40 znaków
   EN: Look at You Flaming Idiots!
   PL:
622. [Umiejętność wroga [115803] (ulepszenie 1) — opis] [WhenUse] 대상이 보유한 부정적인 효과 2개당 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Coin Power +1 for every 2 types of negative effect on target (max 2)
   PL:
623. [Umiejętność wroga [115803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [115803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [115803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst] 1회 발동. 대상의 [Burst] 횟수 1 감소
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Activate [Burst] on target once. Target loses 1 [Burst] Count
   PL:
626. [Umiejętność wroga [115803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [MadFeather] 수치만큼 [Laceration] 위력, [Burst] 위력 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MadFeather], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MadFeather] = 눈알 깃 / Eyeball Pinion; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict [Laceration] and [Burst] Potency equal to [MadFeather] Stack
   PL:
627. [Umiejętność wroga [115804] (ulepszenie 1) — nazwa] 예를 갖추거라!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].name
   limit: do 40 znaków
   EN: Know Your Place!
   PL:
628. [Umiejętność wroga [115804] (ulepszenie 1) — opis] [WideAreaRampage]\n[WhenUse] 자신의 체력을 최대 체력의 3%만큼 소모 (이 피해로 사망하지 않음)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [WhenUse]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]
   EN: [WideAreaRampage]\n[WhenUse] Consume 3% HP on self (this damage does not kill this unit)
   PL:
629. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [ShamrockTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ShamrockTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ShamrockTakeDamageUp] = 탐식 취약 / Gluttony Fragility
   EN: [OnSucceedAttack] Inflict 1 [ShamrockTakeDamageUp] next turn
   PL:
633. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [MadFeather] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MadFeather]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MadFeather] = 눈알 깃 / Eyeball Pinion
   EN: [OnSucceedAttack] Inflict 2 [MadFeather]
   PL:
635. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [ShamrockTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [MadFeather] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MadFeather]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MadFeather] = 눈알 깃 / Eyeball Pinion
   EN: [OnSucceedAttack] Inflict 3 [MadFeather]
   PL:
639. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [115804] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [ShamrockTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115804].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [115805] (ulepszenie 1) — nazwa] 고개를 조아리라!
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115805].levelList[level=1].name
   limit: do 40 znaków
   EN: Kowtow Before Me!
   PL:
642. [Umiejętność wroga [115805] (ulepszenie 1) — opis] [CantIdentify]\n[WhenUse] 자신의 체력을 최대 체력의 5%만큼 소모 (이 피해로 사망하지 않음)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115805].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]
   EN: [CantIdentify]\n[WhenUse] Consume 5% HP on self (this damage does not kill this unit)
   PL:
643. [Umiejętność wroga [115805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [115805] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 ([MadFeather] 수치 x 10)만큼 [Burst]을 부여하고, 대상의 [MadFeather] 전부 소멸
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115805].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [MadFeather], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [MadFeather] = 눈알 깃 / Eyeball Pinion; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict ([MadFeather] on target x 10) [Burst]; all [MadFeather] on target expires
   PL:
645. [Umiejętność wroga [115805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst] 2회 발동. 대상의 [Burst] 횟수 2 감소
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Activate [Burst] on target 2 times. Target loses 2 [Burst] Count
   PL:
646. [Umiejętność wroga [115806] (ulepszenie 1) — nazwa] 기회를 주마
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115806].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Give You a Chance
   PL:
647. [Umiejętność wroga [115806] (ulepszenie 1) — opis] [DuelCounter]\n[DefeatDuel] 대상이 보유한 [MadFeather] 전부 소멸
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115806].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DefeatDuel], [MadFeather]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [MadFeather] = 눈알 깃 / Eyeball Pinion
   EN: [DuelCounter] \n[DefeatDuel] All [MadFeather] on target expires
   PL:
648. [Umiejętność wroga [115806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MadFeather] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [115806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MadFeather] 1 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Umiejętność wroga [115806] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=115806].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność wroga [116701] (ulepszenie 1) — nazwa] 충도류(充刀流) - 내려베기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116701].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Blade Style - Downward Cleave
   PL:
652. [Umiejętność wroga [116701] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여, 최종 위력 + 1 (최대 2)\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116701].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Final Power +1 (max 2)\n[WhenUse] Gain +2 [Charge] Count
   PL:
653. [Umiejętność wroga [116701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
654. [Umiejętność wroga [116701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [116702] (ulepszenie 1) — nazwa] 충도류(充刀流) - 휘둘러베기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116702].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Blade Style - Windup Slash
   PL:
656. [Umiejętność wroga [116702] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여, 합 위력 + 1 (최대 2)\n[WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116702].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Clash Power +1 (max 2)\n[WhenUse] Gain +5 [Charge] Count
   PL:
657. [Umiejętność wroga [116702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność wroga [116702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [116702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [116702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [116703] (ulepszenie 1) — nazwa] 충도류(充刀流) - 베어부수기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Blade Style - Crushing Slice
   PL:
662. [Umiejętność wroga [116703] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여, 코인 위력 + 1 (최대 2)\n[WhenUse] [Charge] 횟수를 5 이상 소모했다면, [Burst] 부여량 +2\n[WhenUse] [Charge] 횟수를 10 소모했다면, [Burst] 횟수 3 증가\n[WhenUse] [Charge] 횟수가 5 이상 10 미만이면, [Burst] 위력을 2 × (13 - 현재 [Charge] 횟수)만큼 획득하여 [Charge] 횟수가 10으로 증가\n[DefeatDuel] 피해량이 75%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [Burst], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1 (max 2)\n[WhenUse] If this unit consumed 5+ [Charge] Count, inflict +2 more [Burst]\n[WhenUse] If this unit consumed 10+ [Charge] Count, inflict +3 [Burst] Count\n[WhenUse] At 5~9 [Charge] Count, gain 2(13 - current [Charge] Count) [Burst] to raise this unit's [Charge] Count to 10\n[DefeatDuel] Deal -75% damage; damage dealt by this Skill cannot Stagger the target
   PL:
663. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 위력만큼 탐식 피해를 주고, [Burst] 횟수 1 감소 (최대 30)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict Gluttony damage equal to [Burst] Potency on target; then, reduce [Burst] Count by 1 (max 30)
   PL:
671. [Umiejętność wroga [116703] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 스킬 사용시 소모한 [Charge] 횟수 5당 [Burst] 횟수 2 부여 (최대 4)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116703].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count for every 5 [Charge] Count consumed On Use (max 4)
   PL:
672. [Umiejętność wroga [116704] (ulepszenie 1) — nazwa] 충도류(充刀流) - 흐름 베기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116704].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Blade Style - Flowing Slash
   PL:
673. [Umiejętność wroga [116704] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +5 [Charge] Count
   PL:
674. [Umiejętność wroga [116704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność wroga [116704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność wroga [116001] (ulepszenie 1) — nazwa] 충권류(充拳流) - 마주치기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116001].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Fist Style - Faceoff
   PL:
677. [Umiejętność wroga [116001] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Charge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116001].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [WhenUse] Final Power +1 for every 4 [Burst] on target (max 2)\n[WhenUse] Gain +3 [Charge] Count
   PL:
678. [Umiejętność wroga [116001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count
   PL:
679. [Umiejętność wroga [116001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [116002] (ulepszenie 1) — nazwa] 충권류(充拳流) - 휘둘러치기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116002].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Fist Style - Roundhouse Punch
   PL:
681. [Umiejętność wroga [116002] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 5당, 최종 위력 +1 (최대 2)\n[WhenUse] [Charge] 횟수를 5 소모하여, 최종 위력 + 1\n[WhenUse] [Charge] 횟수가 5 이상 10 미만이면, [Burst] 위력 2 × (13 - 현재 [Charge] 횟수)만큼 획득하여 [Charge] 횟수가 10으로 증가 (턴 당 1회)\n[WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116002].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [WhenUse] Final Power +1 for every 5 [Burst] on target (max 2)\n[WhenUse] Consume 5 [Charge] Count to gain Final Power +1\n[WhenUse] At 5~9 [Charge] Count, gain 2(13 - current [Charge] Count) [Burst] Potency to raise [Charge] Count to 10 (once per turn)\n[WhenUse] Gain +5 [Charge] Count
   PL:
682. [Umiejętność wroga [116002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +5 [Charge] Count
   PL:
683. [Umiejętność wroga [116002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [116002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge]이 2 이상이면 [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 2+ [Charge], inflict +2 [Burst] Count
   PL:
685. [Umiejętność wroga [116003] (ulepszenie 1) — nazwa] 충권류(充拳流) - 쳐 부수기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Fist Style - Destroy
   PL:
686. [Umiejętność wroga [116003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 6당, 최종 위력 +1 (최대 2) \n[WhenUse] [Charge] 횟수를 5 소모하여, 코인 위력 + 1 (최대 3)\n[WhenUse] [Charge] 횟수를 5 이상 소모했다면, [Burst] 부여량 +2\n[WhenUse] [Charge] 횟수를 10 이상 소모했다면, 대상의 [Burst] 횟수 3 증가\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 6 [Burst] on target (max 2)\n[WhenUse] Consume 5 [Charge] Count to gain Coin Power +1 (max 3)\n[WhenUse] If this unit consumed 5+ [Charge] Count, inflict +2 more [Burst]\n[WhenUse] If this unit consumed 10+ [Charge] Count, inflict +3 [Burst] Count\n[DefeatDuel] Deal -80% damage; damage dealt by this Skill cannot Stagger the target
   PL:
687. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Charge] 횟수 소모 시 [OminousTalisman] 10 부여\n- 소모한 [Charge] 횟수가 10 이상이면, 초과한 [Charge] 횟수만큼 대상의 [Burst] 횟수 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Charge], [OminousTalisman], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [OminousTalisman] = 불길한 부적 / Omen Talisman; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If this unit consumed [Charge] Count, inflict 10 [OminousTalisman]\n- If this unit consumed 10+ [Charge] Count, inflict ([Charge] Count consumed - 10) [Burst] Count
   PL:
691. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [OminousTalisman] 전부 소모
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttack] Remove all [OminousTalisman] on target
   PL:
693. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 스킬 사용시 소모한 [Charge] 횟수가 5 이상이라면 [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Charge], [OminousTalisman]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Charge] = 충전 / Charge; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [UnBrokenCoinOnSucceedAttack] If this unit consumed 5+ [Charge] Count On Use, inflict 10 [OminousTalisman]
   PL:
695. [Umiejętność wroga [116003] (ulepszenie 1) — moneta 3, efekt 3 — opis] [WinDuelAttack] 스킬 사용시 소모한 [Charge] 횟수가 10 이상이라면 [OminousTalisman] 전부 소모
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116003].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Charge], [OminousTalisman]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Charge] = 충전 / Charge; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [WinDuelAttack] If this unit consumed 10+ [Charge] Count On Use, consume all [OminousTalisman] on target
   PL:
696. [Umiejętność wroga [116004] (ulepszenie 1) — nazwa] 충권류(充拳流) - 흐름맞추기
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116004].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Fist Style - Rhythm Matching
   PL:
697. [Umiejętność wroga [116004] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116004].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność wroga [116004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [116004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [OminousTalisman] 3 소모
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=116004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttack] Reduce [OminousTalisman] on target by 3
   PL:
700. [Umiejętność wroga [113307] (ulepszenie 1) — nazwa] 초속호위
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113307].levelList[level=1].name
   limit: do 40 znaków
   EN: Swiftfeet Protection
   PL:
701. [Umiejętność wroga [113307] (ulepszenie 1) — opis] [CanDuelGuard]\n[BeforeUse] [SupportProtect]가 2 이상이면, 흑수 묘 오의 - 운해현현으로 발동됨\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 5% 당, 이 스킬의 방어 레벨이 1 증가 (최대 10)\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113307].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [BeforeUse], [SupportProtect], [WhenUse]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [BeforeUse] = [사용전] / [Before Use]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]
   EN: [CanDuelGuard]\n[BeforeUse] At 2+ [SupportProtect], activates 'Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation' instead\n[WhenUse] Gain 1 Defense Level for every 5% HP this unit cumulatively lost in this Encounter (max 10)\n[WhenUse] Cannot be Staggered by damage until this Skill ends
   PL:
702. [Umiejętność wroga [113307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [113308] (ulepszenie 1) — nazwa] 흑수 묘 오의 - 운해현현
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].name
   limit: do 90 znaków
   EN: Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation
   PL:
704. [Umiejętność wroga [113308] (ulepszenie 1) — opis] 자신과 대상의 속도 차이 2 당 피해량 +20% (최대 60%)\n[WhenUse] 대상의 [Burst] 5 당, 코인 위력 +1 (최대 3)\n[WhenUse] 대상의 [Burst] 횟수 2 당, 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].desc
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność wroga [113308] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Umiejętność wroga [113308] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność wroga [113308] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Umiejętność wroga [113308] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [113308] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [113308] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=113308].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [114110] (ulepszenie 1) — nazwa] 휩쓸고 몰아쳐라
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114110].levelList[level=1].name
   limit: do 40 znaków
   EN: Like a Roaring Storm
   PL:
712. [Umiejętność wroga [114110] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n이 스킬은 홍루를 제외한 인원을 공격함\n다음 턴에 홍루를 제외한 다른 인격들을 흑수 - 묘를 이용해 흐트러짐 상태로 만듦, 자신의 흐트러짐 상태를 해제함\n[EndSkill] 턴이 종료함
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114110].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\n[CantChangeTarget]\nThis Skill attacks targets that aren't Hong Lu\nUses the Heishou Pack - Mao Branch to Stagger every Identity except for Hong Lu next turn; this unit recovers from Stagger\n[EndSkill] Ends turn
   PL:
713. [Umiejętność wroga [114110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p2.json :: dataList[id=114110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c8p2] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c8p2
- grupa rozdziału/trybu: `a1c8p2` · plik: `Skills_Enemy-a1c8p2.json`

714. [Umiejętność wroga [9021001] (ulepszenie 1) — nazwa] 충부류(充斧流) - 찍기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021001].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Slam
   PL:
715. [Umiejętność wroga [9021001] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL:
716. [Umiejętność wroga [9021001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność wroga [9021001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Umiejętność wroga [9021002] (ulepszenie 1) — nazwa] 충부류(充斧流) - 휘두르기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021002].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Swing
   PL:
719. [Umiejętność wroga [9021002] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021002].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [9021002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [9021002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [9021002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność wroga [9021002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Umiejętność wroga [9021003] (ulepszenie 1) — nazwa] 충부류(充斧流) - 분쇄
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021003].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Crush
   PL:
725. [Umiejętność wroga [9021003] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여, 코인 위력 + 1 (최대 2)\n[BeforeAttack] [Charge] 횟수를 5 이상 소모했다면, [Burst] 부여량 +1\n[BeforeAttack] [Charge] 횟수를 10 소모했다면, [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021003].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [BeforeAttack], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Consume 5 [Charge] Count on self to gain Coin Power +1 (max 2)\n[BeforeAttack] If this unit consumed 5+ [Charge] Count, inflict +1 more [Burst]\n[BeforeAttack] Is this unit consumed 10 [Charge] Count, inflict +3 [Burst] Count
   PL:
726. [Umiejętność wroga [9021003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [9021003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 소모한 [Charge] 횟수 5 당 [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] for every 5 [Charge] Count consumed On Use
   PL:
728. [Umiejętność wroga [9021004] (ulepszenie 1) — nazwa] 충부류(充斧流) - 흐름타기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021004].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Rhythm
   PL:
729. [Umiejętność wroga [9021004] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021004].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [9021004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [9021101] (ulepszenie 1) — nazwa] 충부류(充斧流) - 쪼개기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021101].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Cleave
   PL:
732. [Umiejętność wroga [9021101] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021101].levelList[level=1].desc
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Umiejętność wroga [9021101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność wroga [9021102] (ulepszenie 1) — nazwa] 충부류(充斧流) - 휘감기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021102].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Coil
   PL:
735. [Umiejętność wroga [9021102] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021102].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Umiejętność wroga [9021102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [9021102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność wroga [9021102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność wroga [9021102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Umiejętność wroga [9021103] (ulepszenie 1) — nazwa] 충부류(充斧流) - 폭쇄
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021103].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Burst
   PL:
741. [Umiejętność wroga [9021103] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여, 코인 위력 + 1 (최대 2)\n[BeforeAttack] [Charge] 횟수를 5 이상 소모했다면, [Burst] 부여량 +1\n[BeforeAttack] [Charge] 횟수를 10 소모했다면, [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021103].levelList[level=1].desc
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [9021103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Umiejętność wroga [9021103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 소모한 [Charge] 횟수 5 당 [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 727 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność wroga [9021104] (ulepszenie 1) — nazwa] 충부류(充斧流) - 흐름타기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021104].levelList[level=1].name
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [9021104] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021104].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Umiejętność wroga [9021104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność wroga [9021201] (ulepszenie 1) — nazwa] 충부류(充斧流) - 쪼개부수기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021201].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Axe Style - Cleave and Crush
   PL:
748. [Umiejętność wroga [9021201] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021201].levelList[level=1].desc
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Umiejętność wroga [9021201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
750. [Umiejętność wroga [9021201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [9021202] (ulepszenie 1) — nazwa] 충부류(充斧流) - 감아부수기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021202].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Axe Style - Windup Crush
   PL:
752. [Umiejętność wroga [9021202] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021202].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność wroga [9021202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [9021202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Umiejętność wroga [9021202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Umiejętność wroga [9021202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Umiejętność wroga [9021203] (ulepszenie 1) — nazwa] 충부류(充斧流) - 파쇄
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021203].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge Axe Style - Shatter
   PL:
758. [Umiejętność wroga [9021203] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여, 코인 위력 + 1 (최대 2)\n[BeforeAttack] [Charge] 횟수를 5 이상 소모했다면, [Burst] 부여량 +2\n[BeforeAttack] [Charge] 횟수를 10 소모했다면, [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021203].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [BeforeAttack], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Consume 5 [Charge] Count on self to gain Coin Power +1 (max 2)\n[BeforeAttack] If this unit consumed 5+ [Charge] Count, inflict +2 more [Burst]\n[BeforeAttack] Is this unit consumed 10 [Charge] Count, inflict +3 [Burst] Count
   PL:
759. [Umiejętność wroga [9021203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 6 [Burst]
   PL:
760. [Umiejętność wroga [9021203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Umiejętność wroga [9021203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Umiejętność wroga [9021203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst] 위력만큼 탐식 피해를 주고, [Burst] 횟수 1 감소 (최대 30)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność wroga [9021204] (ulepszenie 1) — nazwa] 충부류(充斧流) - 흐름맞추기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021204].levelList[level=1].name
   limit: do 50 znaków
   EN: Charge Axe Style - Rhythm Matching
   PL:
764. [Umiejętność wroga [9021204] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021204].levelList[level=1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność wroga [9021204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność wroga [9021204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9021204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Umiejętność wroga [9020501] (ulepszenie 1) — nazwa] 부딪히기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020501].levelList[level=1].name
   limit: do 40 znaków
   EN: Collide
   PL:
768. [Umiejętność wroga [9020501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [9020501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [9020502] (ulepszenie 1) — nazwa] 난동 피우기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020502].levelList[level=1].name
   limit: do 40 znaków
   EN: Pandemonium
   PL:
771. [Umiejętność wroga [9020502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 4+ [Burst], Clash Power +1
   PL:
772. [Umiejętność wroga [9020502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność wroga [9020502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność wroga [9020502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseUp] 2 얻음
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttackHead] Gain 2 [DefenseUp] next turn
   PL:
775. [Umiejętność wroga [9020503] (ulepszenie 1) — nazwa] 발악 찍기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020503].levelList[level=1].name
   limit: do 40 znaków
   EN: Frantic Pummel
   PL:
776. [Umiejętność wroga [9020503] (ulepszenie 1) — opis] [StartBattle] 체력이 50% 이하면, 이 스킬의 세 번째 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 대상의 [Burst] 4당, 합 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020503].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [WhenUse], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [StartBattle] At 50%- HP, convert the third Coin of this Skill to [SuperCoin]\n[WhenUse] Clash Power +1 for every 4 [Burst] on target (max 2)
   PL:
777. [Umiejętność wroga [9020503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [9020503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여, [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst] and +3 [Burst] Count
   PL:
779. [Umiejętność wroga [9020503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [WinDuelAttack] 최대 체력의 (자신이 보유한 [DefenseUp] 수치)%만큼 체력 회복 (최대 10%)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [DefenseUp]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WinDuelAttack] Heal ([DefenseUp] Stack on self)% HP on self (max 10%)
   PL:
780. [Umiejętność wroga [9020504] (ulepszenie 1) — nazwa] 웅크리기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020504].levelList[level=1].name
   limit: do 40 znaków
   EN: Prone
   PL:
781. [Umiejętność wroga [9020504] (ulepszenie 1) — opis] [WhenUse] 최대 체력의 10%만큼 보호막 얻음
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain Shield equal to 10% of Max HP
   PL:
782. [Umiejętność wroga [9020601] (ulepszenie 1) — nazwa] 부딪히기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020601].levelList[level=1].name
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [9020601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [9020602] (ulepszenie 1) — nazwa] 난동 피우기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020602].levelList[level=1].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [9020602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020602].levelList[level=1].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [9020602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [9020602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [9020602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신을 제외한 체력 비율이 제일 낮은 아군 1명을 자신의 최대 체력 5%만큼 회복
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 other ally with the least HP percentage by 5% of this unit's Max HP
   PL:
789. [Umiejętność wroga [9020603] (ulepszenie 1) — nazwa] 발악 날리기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020603].levelList[level=1].name
   limit: do 40 znaków
   EN: Frantic Volley
   PL:
790. [Umiejętność wroga [9020603] (ulepszenie 1) — opis] [StartBattle] 체력이 50% 이하면, 이 스킬의 세 번째 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 대상의 [Burst] 4당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020603].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [WhenUse], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [StartBattle] At 50%- HP, convert the third Coin of this Skill to [SuperCoin]\n[WhenUse] Base Power +1 for every 4 [Burst] on target (max 2)
   PL:
791. [Umiejętność wroga [9020603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [9020603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [9020603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [WinDuelAttack] 자신을 포함하여 체력 비율이 제일 낮은 아군 2명을 자신의 최대 체력 10%만큼 회복
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] Heal 2 allies, including this unit, with the least HP percentage by 10% of this unit's Max HP
   PL:
794. [Umiejętność wroga [9020604] (ulepszenie 1) — nazwa] 웅크리기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020604].levelList[level=1].name
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [9020604] (ulepszenie 1) — opis] [OnSucceedEvade] [Burst] 횟수 2 증가 (턴당 2회)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Burst]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Burst] = 파열 / Rupture
   EN: [OnSucceedEvade] Inflict +2 [Burst] Count (2 times per turn)
   PL:
796. [Umiejętność wroga [9020701] (ulepszenie 1) — nazwa] 부딪히기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020701].levelList[level=1].name
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [9020701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [9020702] (ulepszenie 1) — nazwa] 난동 피우기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020702].levelList[level=1].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [9020702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020702].levelList[level=1].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [9020702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [9020703] (ulepszenie 1) — nazwa] 발악 휘두르기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020703].levelList[level=1].name
   limit: do 40 znaków
   EN: Frantic Swinging
   PL:
802. [Umiejętność wroga [9020703] (ulepszenie 1) — opis] [StartBattle] 체력이 50% 이하면, 이 스킬의 세 번째 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020703].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [WhenUse], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [StartBattle] At 50%- HP, convert the third Coin of this Skill to [SuperCoin]\n[WhenUse] Coin Power +1 for every 4 [Burst] on target (max 2)
   PL:
803. [Umiejętność wroga [9020703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [9020703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [9020703] (ulepszenie 1) — moneta 3, efekt 1 — opis] 피해량 +(자신의 잃은 체력 비율)% (최대 50%)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +(missing HP percentage on self)% damage (max 50%)
   PL:
806. [Umiejętność wroga [9020703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 이 스킬을 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse this Skill (1 time max)
   PL:
807. [Umiejętność wroga [9020704] (ulepszenie 1) — nazwa] 웅크리기
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020704].levelList[level=1].name
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [9020704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [9020801] (ulepszenie 1) — nazwa] 부령술(符靈術) - 부격
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020801].levelList[level=1].name
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [9020801] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Final Power +1 for every 4 [Burst] on target (max 2)
   PL:
811. [Umiejętność wroga [9020801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Umiejętność wroga [9020801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność wroga [9020802] (ulepszenie 1) — nazwa] 부령술(符靈術) - 효력 발동
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020802].levelList[level=1].name
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [9020802] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020802].levelList[level=1].desc
   (powtórzenie elementu 810 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [9020802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność wroga [9020802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [9020802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [OminousTalisman] 2 소모
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 591 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [9020803] (ulepszenie 1) — nazwa] 부령술(符靈術) - 주살 인형
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020803].levelList[level=1].name
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [9020803] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020803].levelList[level=1].desc
   (powtórzenie elementu 810 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [9020803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Umiejętność wroga [9020803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [OminousTalisman] 5 소모
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttack] Reduce [OminousTalisman] on target by 5
   PL:
822. [Umiejętność wroga [9020804] (ulepszenie 1) — nazwa] 부령술(符靈術) - 방어
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020804].levelList[level=1].name
   limit: do 50 znaków
   EN: Spirit Talisman School - Defend
   PL:
823. [Umiejętność wroga [9020804] (ulepszenie 1) — opis] [StartBattle] (20 - 자신의 정신력)만큼 보호막 얻음 (최소 0, 최대 20)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain (20 - this unit's SP) Shield (min 0, max 20)
   PL:
824. [Umiejętność wroga [9020901] (ulepszenie 1) — nazwa] 부령술(符靈術) - 부격
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020901].levelList[level=1].name
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [9020901] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Final Power +1 for every 4 [Burst] on target (max 3)
   PL:
826. [Umiejętność wroga [9020901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [9020901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [9020902] (ulepszenie 1) — nazwa] 부령술(符靈術) - 효력 발동
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020902].levelList[level=1].name
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [9020902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020902].levelList[level=1].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność wroga [9020902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność wroga [9020902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność wroga [9020902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [OminousTalisman] 3 소모
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [9020903] (ulepszenie 1) — nazwa] 부령술(符靈術) - 집행
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].name
   limit: do 50 znaków
   EN: Spirit Talisman School - Execution
   PL:
834. [Umiejętność wroga [9020903] (ulepszenie 1) — opis] [StartBattle] 정신력이 -30 이하면, 이 스킬의 마지막 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 이 스킬의 기본 위력이 75%만큼 감소 (소수점 버림)\n[WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [DefeatDuel], [WhenUse], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [StartBattle] At -30 SP or less, convert this Skill's final Coin to [SuperCoin]\n[DefeatDuel] Reduce this Skill's Base Power by 75% (rounded down)\n[WhenUse] Final Power +1 for every 4 [Burst] on target (max 3)
   PL:
835. [Umiejętność wroga [9020903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [9020903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [9020903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [9020903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttackTail] Inflict 10 [OminousTalisman]
   PL:
839. [Umiejętność wroga [9020903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [OminousTalisman] 5 소모
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [9020904] (ulepszenie 1) — nazwa] 부령술(符靈術) - 사기 폭발
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].name
   limit: do 50 znaków
   EN: Spirit Talisman School - Vile Burst
   PL:
841. [Umiejętność wroga [9020904] (ulepszenie 1) — opis] [StartBattle] 정신력 -10당 최종 위력 +1 (최대 3)\n[DefeatDuel] 이 스킬의 기본 위력이 75%만큼 감소(소수점 버림)하고 피해, 효과로 대상이 흐트러지지 않음\n[EndSkill] 정신력이 0으로 초기화
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Final Power +1 for every 10 SP below 0 (max 3)\n[DefeatDuel] Reduce this Skill's Base Power by 75% (rounded down); also, this Skill's damage or effect cannot stagger the target(s)\n[EndSkill] Reset SP to 0
   PL:
842. [Umiejętność wroga [9020904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [9020904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [9020904] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [OminousTalisman]
   PL:
845. [Umiejętność wroga [9020904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [9020904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [OminousTalisman] 전부 소모
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność wroga [9020905] (ulepszenie 1) — nazwa] 부령술(符靈術) - 방어
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020905].levelList[level=1].name
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [9020905] (ulepszenie 1) — opis] [StartBattle] (20 - 자신의 정신력)만큼 보호막 얻음 (최소 0, 최대 40)
   źródło: Skills_Enemy-a1c8p2.json :: dataList[id=9020905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain (20 - this unit's SP) Shield (min 0, max 40)
   PL:

## [a1c8p2] Pasywka wroga: Passives_Abnormality-a1c8p2
- plik gry: `Passives_Abnormality-a1c8p2.json`

849. [[a1c8p2] Pasywka wroga [113101] — nazwa] 기습 실패
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113101].name
   limit: do 40 znaków
   EN: Failed Ambush
   PL:
850. [[a1c8p2] Pasywka wroga [113101] — opis] 턴 종료 시, 이번 턴에 합에서 패배했으면 다음 턴에 [Binding] 2를 얻음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Turn End: if this unit lost a Clash this turn, gain 2 [Binding] next turn
   PL:
851. [[a1c8p2] Pasywka wroga [113102] — nazwa] 가치우의 시험
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113102].name
   limit: do 40 znaków
   EN: Jia Qiu's Test
   PL:
852. [[a1c8p2] Pasywka wroga [113102] — opis] 첫 턴 시작 시, [RepressedMurderousIntendTwo] 얻음\n홍루 사망시, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [RepressedMurderousIntendTwo]
   znaczenie tagów: [RepressedMurderousIntendTwo] = 눌린 살기 / Concealed Bloodthirst
   EN: First Turn Start: gain [RepressedMurderousIntendTwo]\nEnds Encounter when Hong Lu dies
   PL:
853. [[a1c8p2] Pasywka wroga [113701] — nazwa] 개화 E.G.O::이립
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113701].name
   limit: do 40 znaków
   EN: Effloresced E.G.O::Érlì
   PL:
854. [[a1c8p2] Pasywka wroga [113701] — opis] 첫 턴 시작시, 정신력을 30 회복하고 [ExaminationOfQiu]을 얻음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ExaminationOfQiu]
   znaczenie tagów: [ExaminationOfQiu] = 일말의 기대 / A Sliver of Anticipation
   EN: First Turn Start: heal 30 SP and gain [ExaminationOfQiu]
   PL:
855. [[a1c8p2] Pasywka wroga [113702] — nazwa] 삭폄(削貶)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113702].name
   limit: do 40 znaków
   EN: Deteriorate (削貶)
   PL:
856. [[a1c8p2] Pasywka wroga [113702] — opis] 대상의 부정적인 효과가 4개 이상이면, 합 위력 +1
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113702].desc
   limit: do 120 znaków
   EN: If target has 4+ negative effects, Clash Power +1
   PL:
857. [[a1c8p2] Pasywka wroga [113703] — nazwa] 주살[물동(勿動)]
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113703].name
   limit: do 40 znaków
   EN: Deathrite [Halt (勿動)]
   PL:
858. [[a1c8p2] Pasywka wroga [113703] — opis] [BurstStop]가 있는 대상에게 가하는 피해량 +10%
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstStop]
   znaczenie tagów: [BurstStop] = 주살【물동】 / Deathrite 【Halt】
   EN: Deal +10% damage against targets with [BurstStop]
   PL:
859. [[a1c8p2] Pasywka wroga [113704] — nazwa] 주살[철주(掣肘)]
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113704].name
   limit: do 40 znaków
   EN: Deathrite [Impede (掣肘)]
   PL:
860. [[a1c8p2] Pasywka wroga [113704] — opis] [BurstSuppress]가 있는 대상에게 피격 시, 받는 피해량 -20%
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113704].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstSuppress]
   znaczenie tagów: [BurstSuppress] = 주살【철주】 / Deathrite 【Impede】
   EN: Take -20% damage from targets with [BurstSuppress]
   PL:
861. [[a1c8p2] Pasywka wroga [113706] — nazwa] 자로여
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113706].name
   limit: do 40 znaków
   EN: Heed me, Zilu
   PL:
862. [[a1c8p2] Pasywka wroga [113706] — opis] 체력이 85% 이하일 때, 패턴 변경\n체력이 60% 이하일 때, 페이즈 변경
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113706].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gains a new pattern at 85% HP\nEnter a new phase at 60% HP
   PL:
863. [[a1c8p2] Pasywka wroga [113707] — nazwa] 그 길의 끝은 여기까지구나
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113707].name
   limit: do 40 znaków
   EN: This is where your path ends
   PL:
864. [[a1c8p2] Pasywka wroga [113707] — opis] 홍루 사망시, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113707].desc
   limit: do 120 znaków
   EN: Ends encounter when Hong Lu dies
   PL:
865. [[a1c8p2] Pasywka wroga [113708] — nazwa] 압도
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113708].name
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [[a1c8p2] Pasywka wroga [113708] — opis] 인격의 체력이 1 이하가 되면, 전투에서 후퇴시킴
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113708].desc
   limit: do 120 znaków
   EN: When an Identity's HP drops to 1 or below, retreat them from the Encounter
   PL:
867. [[a1c8p2] Pasywka wroga [113301] — nazwa] 가늠하기
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113301].name
   limit: do 40 znaków
   EN: Estimation
   PL:
868. [[a1c8p2] Pasywka wroga [113301] — opis] 턴 종료 시, 합에서 패배한 수만큼 다음 턴에 속박 1을 얻음 (최대 6)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113301].desc
   limit: do 120 znaków
   EN: Turn End: for every Clash this unit lost, gain 1 Binding next turn (max 6)
   PL:
869. [[a1c8p2] Pasywka wroga [113302] — nazwa] 신(心) 발산
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113302].name
   limit: do 40 znaków
   EN: Shin (心) Radiance
   PL:
870. [[a1c8p2] Pasywka wroga [113302] — opis] 첫 턴 시작 시, 정신력을 30 회복함\n체력이 85% 이하일 때, 패턴 변경\n체력이 60%이하가 되면 턴 시작 시, 보호막 500 얻음\n- 이후 체력이 1 이하로 감소하지 않음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113302].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: First Turn Start: heal 30 SP\nGains a new pattern at 85% HP\nGain 500 Shield at Turn Start, at 60% HP\n- After this effect activates, this unit does not drop below 1 HP
   PL:
871. [[a1c8p2] Pasywka wroga [114101] — nazwa] 개화 E.G.O::이립
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114101].name
   (powtórzenie elementu 853 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [[a1c8p2] Pasywka wroga [114101] — opis] 첫 턴 시작시, [ExaminationOfQiu]을 얻음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ExaminationOfQiu]
   znaczenie tagów: [ExaminationOfQiu] = 일말의 기대 / A Sliver of Anticipation
   EN: First Turn Start: gain [ExaminationOfQiu]
   PL:
873. [[a1c8p2] Pasywka wroga [114102] — nazwa] 폄(貶)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114102].name
   limit: do 40 znaków
   EN: Diminish (貶)
   PL:
874. [[a1c8p2] Pasywka wroga [114102] — opis] 대상이 가진 주살 종류가 3개 이상이면, 코인 위력 +1
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114102].desc
   limit: do 120 znaków
   EN: If target has 3+ types of Deathrites, Coin Power +1
   PL:
875. [[a1c8p2] Pasywka wroga [114104] — nazwa] 다시 묻지
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114104].name
   limit: do 40 znaków
   EN: I will ask again
   PL:
876. [[a1c8p2] Pasywka wroga [114104] — opis] 전체 체력의 50% 이하가 되면, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114104].desc
   limit: do 120 znaków
   EN: Ends the Encounter at 50% HP
   PL:
877. [[a1c8p2] Pasywka wroga [114105] — nazwa] 기합
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114105].name
   limit: do 40 znaków
   EN: Focus
   PL:
878. [[a1c8p2] Pasywka wroga [114105] — opis] '답을 떠올려'를 사용할 때, 흑수를 소환함
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114105].desc
   limit: do 120 znaków
   EN: When using 'Bring Forth a Real Answer', summon the Heishou
   PL:
879. [[a1c8p2] Pasywka wroga [114106] — nazwa] 기합
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114106].name
   (powtórzenie elementu 877 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [[a1c8p2] Pasywka wroga [114106] — opis] 페이즈 시작시에 가지고 있던 [Burst], [Combustion], [Sinking], [Vibration], [Laceration] 위력과 [Burst], [Combustion], [Sinking], [Vibration], [Laceration] 횟수를 절반씩 가지고 전투 시작함.
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114106].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [Burst], [Combustion], [Sinking], [Vibration], [Laceration]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Combustion] = 화상 / Burn; [Sinking] = 침잠 / Sinking; [Vibration] = 진동 / Tremor; [Laceration] = 출혈 / Bleed
   EN: Begins the Encounter with half the Potency and Count for the following effects this unit had at the start of this phase: [Burst], [Combustion], [Sinking], [Vibration], [Laceration]
   PL:
881. [[a1c8p2] Pasywka wroga [113709] — nazwa] 현가불철
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113709].name
   limit: do 40 znaków
   EN: Infinite Song of Erudition
   PL:
882. [[a1c8p2] Pasywka wroga [113709] — opis] 공격 종료 시 대상의 주살 수당, 정신력 5 회복\n적중 시 대상의 주살이 발동했을 때, 발동한 주살 수당, 정신력 3 회복
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=113709].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack End: heal 5 SP for every Deathrite on the target\nOn Hit, when the target's Deathrite is triggered, heal 3 SP for every Deathrite triggered
   PL:
883. [[a1c8p2] Pasywka wroga [114107] — nazwa] 나는 아직 듣지 못했다.
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114107].name
   limit: do 40 znaków
   EN: I still await your answer.
   PL:
884. [[a1c8p2] Pasywka wroga [114107] — opis] 매 턴 시작 시, 본체와 부위에 보호막 900을 얻음.\n- 홍루에게 [Teaching]이 있으면, 수치당 300을 감소해서 얻음\n- 홍루에게 [Teaching] 3 이상있으면, 이후 전투동안 보호막을 얻지 않음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114107].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Teaching]
   znaczenie tagów: [Teaching] = 문답 / Dialogues
   EN: Every Turn Start: Core and Part gain 900 Shield.\n- When Hong Lu has [Teaching], lose 300 Shield per Stack on Hong Lu\n- When Hong Lu has 3+ [Teaching], this unit does not gain Shield for the rest of the Encounter
   PL:
885. [[a1c8p2] Pasywka wroga [115701] — nazwa] 증오심
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115701].name
   limit: do 40 znaków
   EN: Hate
   PL:
886. [[a1c8p2] Pasywka wroga [115701] — opis] 홍루와 합 진행 시 스킬 최종 위력 +2
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115701].desc
   limit: do 120 znaków
   EN: Final Power +2 in Clashes against Hong Lu
   PL:
887. [[a1c8p2] Pasywka wroga [115702] — nazwa] 풀려난 저주
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115702].name
   limit: do 40 znaków
   EN: Unleashed Curse
   PL:
888. [[a1c8p2] Pasywka wroga [115702] — opis] 턴 시작시 이번 전투에서 사망한 항아리의 수만큼 [AttackUp] 얻음 (최대 5)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115702].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: gain [AttackUp] equal to the number of Jars defeated in this Encounter (max 5)
   PL:
889. [[a1c8p2] Pasywka wroga [115703] — nazwa] 고통 돌려주기
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115703].name
   limit: do 40 znaków
   EN: Returning the Pain
   PL:
890. [[a1c8p2] Pasywka wroga [115703] — opis] 자신의 잃은 체력 1%당 가하는 피해량 +1% (최대 50%)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115703].desc
   limit: do 120 znaków
   EN: Deal +1% damage for every 1% missing HP on self (max 50%)
   PL:
891. [[a1c8p2] Pasywka wroga [115801] — nazwa] 불로불사의 환?
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115801].name
   limit: do 40 znaków
   EN: Bolus of... Immortality?
   PL:
892. [[a1c8p2] Pasywka wroga [115801] — opis] 스킬 적중시 가한 피해의 10%만큼 체력 회복 (소수점 버림)\n대상에게 [MadFeather]이 있다면, (대상의 [MadFeather] 수치)% 만큼 추가로 회복
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115801].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [MadFeather]
   znaczenie tagów: [MadFeather] = 눈알 깃 / Eyeball Pinion
   EN: On Hit with a Skill: heal 10% of the damage dealt (rounded down)\nIf target has [MadFeather], heal additional ([MadFeather] Stack on target)% HP
   PL:
893. [[a1c8p2] Pasywka wroga [115802] — nazwa] 기분 째지는데!
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115802].name
   limit: do 40 znaków
   EN: I'VE NEVER FELT BETTER!
   PL:
894. [[a1c8p2] Pasywka wroga [115802] — opis] 자신의 공격 적중시, 정신력 3 회복
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115802].desc
   limit: do 120 znaków
   EN: On Hit, heal 3 SP on self
   PL:
895. [[a1c8p2] Pasywka wroga [115803] — nazwa] 이 몸은 이제 시작이다!
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115803].name
   limit: do 50 znaków
   EN: MY REVENGEANCE HAS JUST BEGUN!
   PL:
896. [[a1c8p2] Pasywka wroga [115803] — opis] 합에서 패배할 때마다, 다음 턴에 [AttackUp] 1 얻음 (최대 3)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Gain 1 [AttackUp] next turn every time this unit loses a Clash (max 3)
   PL:
897. [[a1c8p2] Pasywka wroga [115804] — nazwa] 깃털 파열상
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115804].name
   limit: do 40 znaków
   EN: Rupture by Feathers
   PL:
898. [[a1c8p2] Pasywka wroga [115804] — opis] 한 턴에 동일한 대상에게 공격 3회 적중시마다, 대상에게 다음 턴에 [Vulnerable] 1 부여
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115804].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Whenever this unit hits the same target three times in the same turn, inflict 1 [Vulnerable] next turn
   PL:
899. [[a1c8p2] Pasywka wroga [115805] — nazwa] 광폭
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115805].name
   limit: do 40 znaków
   EN: Rampage
   PL:
900. [[a1c8p2] Pasywka wroga [115805] — opis] 자신이 이번 전투에서 잃은 체력 누적 15%당 공격 레벨 1 증가[TabExplain], 방어 레벨 1 감소[TabExplain] (최대 6)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115805].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Offense Level +1 and Defense Level -1 for every 15% HP this unit cumulatively lost in this Encounter (max 6)
   PL:
901. [[a1c8p2] Pasywka wroga [115901] — nazwa] 앞선 전투에서의 부상
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115901].name
   limit: do 40 znaków
   EN: Wounded
   PL:
902. [[a1c8p2] Pasywka wroga [115901] — opis] 스테이지 시작 시, 체력이 80%인 상태로 전투 시작
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115901].desc
   limit: do 120 znaków
   EN: Encounter Start: enters the battle with 80% HP
   PL:
903. [[a1c8p2] Pasywka wroga [115902] — nazwa] 주살승을 부리는 자
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115902].name
   limit: do 50 znaków
   EN: Master of the Deathrite Monks
   PL:
904. [[a1c8p2] Pasywka wroga [115902] — opis] 턴 종료 시 자신의 정신력이 20 이하면, 정신력이 제일 높은 무작위 아군 3명의 정신력을 각각 10만큼 소모하여 그 수치만큼 자신의 정신력 회복\n\n턴 시작 시, 정신력이 -20 이하인 모든 아군(자신 제외)에게 [AttackDmgUp] 2 부여
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115902].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: at 20 or less SP, this unit siphons 10 SP from 3 random allies with the highest SP to heal its own SP\n\nTurn Start: Apply 2 [AttackDmgUp] to all other allies with -20 or less SP
   PL:
905. [[a1c8p2] Pasywka wroga [115903] — nazwa] 사특한 기운
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115903].name
   limit: do 40 znaków
   EN: Wicked Energy
   PL:
906. [[a1c8p2] Pasywka wroga [115903] — opis] [OminousTalisman]을 적에게 부여할 때 대상이 이미 [OminousTalisman]을 보유하였다면, 대상이 보유한 [OminousTalisman]을 최대 3만큼 소모하고 그 수치만큼 이번 턴과 다음 턴에 [DefenseDown] 부여
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115903].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: [OminousTalisman], [DefenseDown]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When inflicting [OminousTalisman] on an enemy, if the target already has [OminousTalisman], consume up to 3 [OminousTalisman] on the target and inflict the same value as [DefenseDown] Stacks to the target this turn and next turn
   PL:
907. [[a1c8p2] Pasywka wroga [115904] — nazwa] 젠장... 저 놈들을 처리해!
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115904].name
   limit: do 40 znaków
   EN: Dammit... Take them out!
   PL:
908. [[a1c8p2] Pasywka wroga [115904] — opis] 이번 전투에서 자신의 체력이 최대 체력의 절반 이하가 되는 피해를 받으면 해당 피해를 받지 않고 턴이 즉시 종료되며, 등장 순서의 제일 뒤로 이동함 (흐트러짐 상태일 경우, 즉시 해제)\n\n등장할 적이 더 이상 없거나 충분하지 않으면 (이번 턴에 사망한 적이 추가로 등장할 적의 수보다 많은 경우), 이 효과가 발동하지 않음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115904].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In this Encounter, if this unit takes damage that brings this unit's HP down to half or less, nullify that damage and end the turn. Then, move to the rearmost position of the Substitution order (when Staggered, recover immediately)\n\nIf there are no more enemies to Substitute in, or if there aren't enough of them left, (as in, if there are more dead enemies this turn than there are waiting to Substitute into the Encounter) this effect does not activate
   PL:
909. [[a1c8p2] Pasywka wroga [115905] — nazwa] 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115905].name
   limit: do 40 znaków
   EN: The Battle's End
   PL:
910. [[a1c8p2] Pasywka wroga [115905] — opis] 이번 전투에서 왕청산이 체력을 전부 잃게 되면, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115905].desc
   limit: do 120 znaków
   EN: When Wang Qingshan loses all HP in this Encounter, the Encounter ends
   PL:
911. [[a1c8p2] Pasywka wroga [116701] — nazwa] 윽… 이 놈의 문양이…!
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116701].name
   limit: do 50 znaków
   EN: Ugh... these damn engravings...!
   PL:
912. [[a1c8p2] Pasywka wroga [116701] — opis] 턴 종료 시, 자신의 [Charge]이 7 이상이면, 다음 턴에 [DefenseDown] 4, [AttackDmgUp] 3 얻음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: at 7+ [Charge], gain 4 [DefenseDown] and 3 [AttackDmgUp] next turn
   PL:
913. [[a1c8p2] Pasywka wroga [116702] — nazwa] 네 허접한 무기와는 차원이 다르지
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116702].name
   limit: do 60 znaków
   EN: Your shabby weapons are incomparable to mine
   PL:
914. [[a1c8p2] Pasywka wroga [116702] — opis] 해당 턴에 [Burst]을 4 이상 부여했다면, 턴 종료 시 [Charge] 횟수 3을 얻음 (턴 당 1회)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116702].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Burst], [Charge]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: If this unit inflicted 4 or more [Burst] during this turn, gain +3 [Charge] Count at Turn End (once per turn)
   PL:
915. [[a1c8p2] Pasywka wroga [116703] — nazwa] 겨우 이 정도야?
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116703].name
   limit: do 40 znaków
   EN: Is that all you've got?
   PL:
916. [[a1c8p2] Pasywka wroga [116703] — opis] 턴 시작 시, 자신의 [Charge] 1 당, [AttackDmgUp] 1 얻음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: gain 1 [AttackDmgUp] for every [Charge] on self
   PL:
917. [[a1c8p2] Pasywka wroga [116704] — nazwa] 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116704].name
   (powtórzenie elementu 909 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [[a1c8p2] Pasywka wroga [116704] — opis] 이번 전투에서 사화?(이)가 체력을 전부 잃게 되면, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116704].desc
   limit: do 120 znaków
   EN: When Shi Hua... something? loses all HP in this Encounter, the Encounter ends
   PL:
919. [[a1c8p2] Pasywka wroga [116705] — nazwa] 전격도 보호막 전개
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116705].name
   limit: do 40 znaków
   EN: Deploy Lightning Shield
   PL:
920. [[a1c8p2] Pasywka wroga [116705] — opis] 턴 시작 시, 자신에게 [Charge]이 있으면 보호막을 (100 - (([Charge] - 1) x 10)) 얻음. 자신의 [Charge]이 7 이상이면, 이후 전투동안 이 패시브로 인한 보호막을 얻지 않음.
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116705].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Turn Start: if this unit has [Charge], gain (100 - (([Charge] - 1) x 10)) Shield. At 7+ [Charge], this unit no longer gains Shield with this Passive.
   PL:
921. [[a1c8p2] Pasywka wroga [116001] — nazwa] 인적 자원은 이렇게 응용하는 거다
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116001].name
   limit: do 60 znaków
   EN: That's how you use your human resources
   PL:
922. [[a1c8p2] Pasywka wroga [116001] — opis] 턴 시작 시 자신의 체력이 50% 이하면, 무작위 사씨 가문 사병을 1명 희생하여 (자신의 최대 체력 10% + 희생한 대상의 최대 체력 50%)만큼 체력을 회복하고 정신력 25만큼 회복, 흐트러짐 상태에서 해제됨 (턴 당 1회)
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116001].desc
   limit: do 270 znaków
   EN: Turn Start: if this unit has 50% or less HP, sacrifice a random Shi Family Mercenary to heal (10% of this unit's HP + 50% of the sacrificed unit's HP) HP, heal 25 SP, and recover from Stagger (once per turn)
   PL:
923. [[a1c8p2] Pasywka wroga [116002] — nazwa] 금강불괴
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116002].name
   limit: do 50 znaków
   EN: Jin Gang, Unbreakable Diamond
   PL:
924. [[a1c8p2] Pasywka wroga [116002] — opis] 턴 시작 시, [Protection] 5 얻음\n- 자신의 [Charge]에 따라 턴 시작 시 획득하는 수치가 감소\n- 자신의 [Charge]이 5 이상이라면,  이후 전투 동안 이 패시브로 인한 [Protection]를 획득하지 않음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116002].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [Charge]
   znaczenie tagów: [Protection] = 보호 / Protection; [Charge] = 충전 / Charge
   EN: Turn Start: gain 5 [Protection]\n- Gain fewer Stacks depending on this unit's [Charge]\n- At 5+ [Charge], this unit no longer gains [Protection] with this Passive
   PL:
925. [[a1c8p2] Pasywka wroga [116003] — nazwa] 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116003].name
   (powtórzenie elementu 909 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [[a1c8p2] Pasywka wroga [116003] — opis] 이번 전투에서 사사정이 체력을 전부 잃게 되면, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=116003].desc
   limit: do 120 znaków
   EN: When Shi Sijing loses all HP in this Encounter, the Encounter ends
   PL:
927. [[a1c8p2] Pasywka wroga [115704] — nazwa] 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115704].name
   (powtórzenie elementu 909 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [[a1c8p2] Pasywka wroga [115704] — opis] 이번 전투에서 설반이 체력을 전부 잃게 되면, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115704].desc
   limit: do 120 znaków
   EN: When Xue Pan loses all HP in this Encounter, the Encounter ends
   PL:
929. [[a1c8p2] Pasywka wroga [115806] — nazwa] 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115806].name
   (powtórzenie elementu 909 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [[a1c8p2] Pasywka wroga [115806] — opis] 이번 전투에서 사이화가 체력을 전부 잃게 되면, 전투 종료
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=115806].desc
   limit: do 120 znaków
   EN: When Shi Yihua loses all HP in this Encounter, the Encounter ends
   PL:
931. [[a1c8p2] Pasywka wroga [114401] — nazwa] 주군이시여
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114401].name
   limit: do 40 znaków
   EN: My Lord
   PL:
932. [[a1c8p2] Pasywka wroga [114401] — opis] 턴 시작 시, 정신력을 30 회복함\n턴 시작 시, 보호막을 500까지 얻음\n- 체력이 1 이하로 떨어지지 않음
   źródło: Passives_Abnormality-a1c8p2.json :: dataList[id=114401].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: heal 30 SP\nTurn Start: gain up to 500 Shield\n- This unit does not drop below 1 HP
   PL:

## [a1c8p2] Pasywka wroga: Passives_Enemy-a1c8p2
- plik gry: `Passives_Enemy-a1c8p2.json`

933. [[a1c8p2] Pasywka wroga [9021001] — nazwa] 가주 후보 견제
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021001].name
   limit: do 40 znaków
   EN: Rival Candidate
   PL:
934. [[a1c8p2] Pasywka wroga [9021001] — opis] 대상이 홍루라면, 피해량 +10%
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021001].desc
   limit: do 120 znaków
   EN: Deal +10% damage against Hong Lu
   PL:
935. [[a1c8p2] Pasywka wroga [9021002] — nazwa] 사(史)제 충전 회로
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021002].name
   limit: do 50 znaków
   EN: Shi(史) Family Charge Circuitry
   PL:
936. [[a1c8p2] Pasywka wroga [9021002] — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n턴 종료 시, [Charge]이 2 이상이면, 다음 턴에 [ParryingResultUp] 1 얻음
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021002].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [ParryingResultUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nTurn End: At 2+ [Charge], gain 1 [ParryingResultUp] next turn
   PL:
937. [[a1c8p2] Pasywka wroga [9021003] — nazwa] 충전 회로 발동
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021003].name
   limit: do 40 znaków
   EN: Charge Circuitry Activation
   PL:
938. [[a1c8p2] Pasywka wroga [9021003] — opis] 대상의 [Burst] 6 당, 피해량 +5% (최대 10%)
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Deal +5% damage for every 6 [Burst] on target (Max 10%)
   PL:
939. [[a1c8p2] Pasywka wroga [9021004] — nazwa] 과부하
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021004].name
   limit: do 40 znaków
   EN: Overload
   PL:
940. [[a1c8p2] Pasywka wroga [9021004] — opis] 턴 종료 시, 자신의 [Charge]이 3 이상이면, 다음 턴에 [DefenseDown] 3, [AttackDmgUp] 1 얻음
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021004].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: at 3+ [Charge], gain 3 [DefenseDown] and 1 [AttackDmgUp] next turn
   PL:
941. [[a1c8p2] Pasywka wroga [9021201] — nazwa] 심한 과부하
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021201].name
   limit: do 40 znaków
   EN: Severe Overload
   PL:
942. [[a1c8p2] Pasywka wroga [9021201] — opis] 턴 종료 시, 자신의 [Charge]이 5 이상이면, 다음 턴에 [DefenseDown] 4, [AttackDmgUp] 3 얻음
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9021201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: at 5+ [Charge], gain 4 [DefenseDown] and 3 [AttackDmgUp] next turn
   PL:
943. [[a1c8p2] Pasywka wroga [9020501] — nazwa] 실험 목표 - 생장
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020501].name
   limit: do 40 znaków
   EN: Experiment Goal - Maturation
   PL:
944. [[a1c8p2] Pasywka wroga [9020501] — opis] 턴 시작 시, (이번 전투 동안 적에게 스킬 공격으로 피해를 받은 횟수/2)만큼 [DefenseUp] 얻음 (최대 10)\n\n처음으로 흐트러진 이후에는 이 효과가 사라지고, 다음 턴 부터 턴 시작 시 [DefenseDown] 10 얻음
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020501].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseUp], [DefenseDown]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: gain [DefenseUp] equal to (number of times this unit was hit by the enemies' Skill Attacks / 2) (max 10)\n\nLose this effect when Staggered for the first time; then, at the next Turn Start, gain 10 [DefenseDown]
   PL:
945. [[a1c8p2] Pasywka wroga [9020601] — nazwa] 실험 목표 - 발아
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020601].name
   limit: do 50 znaków
   EN: Experiment Goal - Germination
   PL:
946. [[a1c8p2] Pasywka wroga [9020601] — opis] 체력이 최대 상태가 아니면 턴 시작 시, 잃은 체력의 80%만큼 자신의 체력을 회복\n- 회복할 때마다 이 패시브의 효과가 절반으로 감소 (최소 10%까지 감소, 체력을 1 이상 회복하는 경우에만 적용됨)\n- 흐트러짐 상태에서는 이 효과가 발동하지 않음\n\n처음으로 흐트러진 이후 또는 회복 효과가 최소가 되면 매 턴 시작 시 [Vulnerable] 3 얻음
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020601].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn Start: if this unit isn't at max HP, heal 80% of the missing HP\n- With every healing, halve the healing effect of this Passive by half (halves down to 10% minimum; applies only when this unit heals more than 1 HP)\n- Does not activate when Staggered\n\nAfter this unit is Staggered for the first time, or when the healing effect is reduced to its minimum, gain 3 [Vulnerable] at every Turn Start
   PL:
947. [[a1c8p2] Pasywka wroga [9020701] — nazwa] 실험 목표 - 만발
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020701].name
   limit: do 40 znaków
   EN: Experiment Goal - Blossom
   PL:
948. [[a1c8p2] Pasywka wroga [9020701] — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 다음 턴까지 체력이 1로 유지되고 피해량 +50% (전투당 1회)\n\n흐트러짐 상태에서는 이 효과가 발동하지 않음
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020701].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When this unit takes damage that brings its HP down to 0, and maintain this unit's HP at 1 until the next turn; deal +50% damage (once per Encounter)\n\nDoes not activate when Staggered
   PL:
949. [[a1c8p2] Pasywka wroga [9020801] — nazwa] 부적술사
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020801].name
   limit: do 40 znaków
   EN: Talisman Sorcerer
   PL:
950. [[a1c8p2] Pasywka wroga [9020801] — opis] [OminousTalisman]을 적에게 부여할 때마다 자신의 정신력 10을 소모함\n\n[OminousTalisman]을 보유한 대상에게 가하는 피해량이 (0 - 자신의 정신력)%만큼 증가 (최대 30%, 최소 0%)
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020801].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: Whenever this unit inflicts [OminousTalisman] against an enemy, lose 10 SP\n\nAgainst targets with [OminousTalisman], deal +(0 - SP on self)% damage (max 30%, min 0%)
   PL:
951. [[a1c8p2] Pasywka wroga [9020802] — nazwa] 불길함 전이
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020802].name
   limit: do 40 znaków
   EN: Proliferating Misfortune
   PL:
952. [[a1c8p2] Pasywka wroga [9020802] — opis] 사망 시, [OminousTalisman]이 없는 무작위 적에게 [OminousTalisman] 10 부여\n- 모든 적이 [OminousTalisman]을 보유하였다면, 대신 모든 적의 [OminousTalisman] 1 감소
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020802].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: On death, apply 10 [OminousTalisman] against a random enemy without [OminousTalisman]\n- If all enemies already have [OminousTalisman], then reduce all enemies' [OminousTalisman] by 1 instead
   PL:
953. [[a1c8p2] Pasywka wroga [9020803] — nazwa] 사특한 기운
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020803].name
   (powtórzenie elementu 905 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [[a1c8p2] Pasywka wroga [9020803] — opis] [OminousTalisman]을 적에게 부여할 때 대상이 이미 [OminousTalisman]을 보유하였다면, 대상이 보유한 [OminousTalisman]을 1~2만큼 소모하고 그 수치만큼 이번 턴과 다음 턴에 [DefenseDown] 부여
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020803].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: [OminousTalisman], [DefenseDown]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When inflicting [OminousTalisman] on an enemy, if the target already has [OminousTalisman], consume 1~2 [OminousTalisman] on the target and inflict the same value as [DefenseDown] Stacks to the target this turn and next turn
   PL:
955. [[a1c8p2] Pasywka wroga [9020901] — nazwa] 뛰어난 부적술사
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020901].name
   limit: do 40 znaków
   EN: Skilled Talisman Sorcerer
   PL:
956. [[a1c8p2] Pasywka wroga [9020901] — opis] [OminousTalisman]을 적에게 부여할 때마다 자신의 정신력 10을 소모함\n\n[OminousTalisman]을 보유한 대상에게 가하는 피해량이 (10 - 자신의 정신력)%만큼 증가 (최대 50%, 최소 0%)
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020901].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: Whenever this unit inflicts [OminousTalisman] against an enemy, lose 10 SP\n\nAgainst targets with [OminousTalisman], deal +(10 - SP on self)% damage (max 50%, min 0%)
   PL:
957. [[a1c8p2] Pasywka wroga [9020902] — nazwa] 흡혼요법
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020902].name
   limit: do 40 znaków
   EN: Soul Siphon Technique
   PL:
958. [[a1c8p2] Pasywka wroga [9020902] — opis] 턴 시작 시 자신의 체력이 50% 이하면, 무작위 사특한 주살승을 1명 희생하여 (자신의 최대 체력 10% + 희생한 대상의 최대 체력 50%)만큼 체력을 회복, 25만큼 정신력을 회복, 흐트러짐 상태에서 해제됨 (턴당 1회)
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020902].desc
   limit: do 250 znaków
   EN: Turn Start: at 50% or less HP, sacrifice a random Wicked Deathrite Monk to heal (10% of this unit's HP + 50% of the sacrificed unit's HP) HP, heal 25 SP, and recover from Stagger (once per turn)
   PL:
959. [[a1c8p2] Pasywka wroga [9020903] — nazwa] 사특한 기운
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020903].name
   (powtórzenie elementu 905 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [[a1c8p2] Pasywka wroga [9020903] — opis] [OminousTalisman]을 적에게 부여할 때 대상이 이미 [OminousTalisman]을 보유하였다면, 대상이 보유한 [OminousTalisman]을 최대 3만큼 소모하고 그 수치만큼 이번 턴과 다음 턴에 [DefenseDown] 부여
   źródło: Passives_Enemy-a1c8p2.json :: dataList[id=9020903].desc
   (powtórzenie elementu 906 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c8p3] Wróg / część: Enemies-a1c8p3
- plik gry: `Enemies-a1c8p3.json`

961. [[a1c8p3] Wróg / część [1145] — nazwa] 뇌횡
   źródło: Enemies-a1c8p3.json :: dataList[id=1145].name
   limit: do 40 znaków
   EN: Lei Heng
   PL:
962. [[a1c8p3] Wróg / część [1145] — opis] 본체
   źródło: Enemies-a1c8p3.json :: dataList[id=1145].desc
   limit: do 120 znaków
   EN: Core
   PL:
963. [[a1c8p3] Wróg / część [114501] — nazwa] 몸통
   źródło: Enemies-a1c8p3.json :: dataList[id=114501].name
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [[a1c8p3] Wróg / część [114501] — opis] 부위
   źródło: Enemies-a1c8p3.json :: dataList[id=114501].desc
   limit: do 120 znaków
   EN: Part
   PL:
965. [[a1c8p3] Wróg / część [1171] — nazwa] 엄격한 엄지 솔다토
   źródło: Enemies-a1c8p3.json :: dataList[id=1171].name
   limit: do 40 znaków
   EN: Stern Soldato of the Thumb
   PL:
966. [[a1c8p3] Wróg / część [1171] — opis] 본체
   źródło: Enemies-a1c8p3.json :: dataList[id=1171].desc
   (powtórzenie elementu 962 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [[a1c8p3] Wróg / część [117101] — nazwa] 몸통
   źródło: Enemies-a1c8p3.json :: dataList[id=117101].name
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [[a1c8p3] Wróg / część [117101] — opis] 부위
   źródło: Enemies-a1c8p3.json :: dataList[id=117101].desc
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [[a1c8p3] Wróg / część [1139] — nazwa] 재빠른 N사 E.G.O::끈적임
   źródło: Enemies-a1c8p3.json :: dataList[id=1139].name
   limit: do 50 znaków
   EN: Swift N Corp. E.G.O::Sticking
   PL:
970. [[a1c8p3] Wróg / część [1139] — opis] 본체
   źródło: Enemies-a1c8p3.json :: dataList[id=1139].desc
   (powtórzenie elementu 962 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [[a1c8p3] Wróg / część [113901] — nazwa] 몸통
   źródło: Enemies-a1c8p3.json :: dataList[id=113901].name
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [[a1c8p3] Wróg / część [113901] — opis] 부위
   źródło: Enemies-a1c8p3.json :: dataList[id=113901].desc
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [[a1c8p3] Wróg / część [1140] — nazwa] 날렵한 N사 E.G.O::끈적임
   źródło: Enemies-a1c8p3.json :: dataList[id=1140].name
   limit: do 50 znaków
   EN: Nimble N Corp. E.G.O::Sticking
   PL:
974. [[a1c8p3] Wróg / część [1140] — opis] 부위
   źródło: Enemies-a1c8p3.json :: dataList[id=1140].desc
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [[a1c8p3] Wróg / część [114001] — nazwa] 몸통
   źródło: Enemies-a1c8p3.json :: dataList[id=114001].name
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [[a1c8p3] Wróg / część [114001] — opis] 부위
   źródło: Enemies-a1c8p3.json :: dataList[id=114001].desc
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [[a1c8p3] Wróg / część [90217] — nazwa] 엄격한 엄지 솔다토
   źródło: Enemies-a1c8p3.json :: dataList[id=90217].name
   (powtórzenie elementu 965 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [[a1c8p3] Wróg / część [90218] — nazwa] 각 잡힌 엄지 솔다토
   źródło: Enemies-a1c8p3.json :: dataList[id=90218].name
   limit: do 40 znaków
   EN: Rigid Soldato of the Thumb
   PL:
979. [[a1c8p3] Wróg / część [1135] — nazwa] N사 E.G.O::경멸,경외 가환
   źródło: Enemies-a1c8p3.json :: dataList[id=1135].name
   limit: do 60 znaków
   EN: N Corp. E.G.O::Contempt, Awe Jia Huan
   PL:
980. [[a1c8p3] Wróg / część [1136] — nazwa] N사 E.G.O::흉탄 구보
   źródło: Enemies-a1c8p3.json :: dataList[id=1136].name
   limit: do 50 znaków
   EN: N Corp. E.G.O::Fell Bullet Gubo
   PL:
981. [[a1c8p3] Wróg / część [1146] — nazwa] 가모
   źródło: Enemies-a1c8p3.json :: dataList[id=1146].name
   limit: do 40 znaków
   EN: Jia Mu
   PL:
982. [[a1c8p3] Wróg / część [1152] — nazwa] 혼각온량흑수[混覺轀輬黑獸]
   źródło: Enemies-a1c8p3.json :: dataList[id=1152].name
   limit: do 70 znaków
   EN: Muddled Heishou of the Corpse Palanquin [混覺轀輬黑獸]
   PL:
983. [[a1c8p3] Wróg / część [115202] — nazwa] 가마
   źródło: Enemies-a1c8p3.json :: dataList[id=115202].name
   limit: do 40 znaków
   EN: Palanquin
   PL:
984. [[a1c8p3] Wróg / część [1153] — nazwa] 보옥
   źródło: Enemies-a1c8p3.json :: dataList[id=1153].name
   limit: do 40 znaków
   EN: Baoyu, the Precious Jade
   PL:
985. [[a1c8p3] Wróg / część [115301] — nazwa] 옥
   źródło: Enemies-a1c8p3.json :: dataList[id=115301].name
   limit: do 40 znaków
   EN: Jade
   PL:
986. [[a1c8p3] Wróg / część [1154] — nazwa] 하늘 어르신
   źródło: Enemies-a1c8p3.json :: dataList[id=1154].name
   limit: do 40 znaków
   EN: Heavenly Elder
   PL:
987. [[a1c8p3] Wróg / część [1155] — nazwa] 땅 어르신
   źródło: Enemies-a1c8p3.json :: dataList[id=1155].name
   limit: do 40 znaków
   EN: Earthly Elder
   PL:
988. [[a1c8p3] Wróg / część [1156] — nazwa] 뇌 어르신
   źródło: Enemies-a1c8p3.json :: dataList[id=1156].name
   limit: do 40 znaków
   EN: Brain Elder
   PL:
