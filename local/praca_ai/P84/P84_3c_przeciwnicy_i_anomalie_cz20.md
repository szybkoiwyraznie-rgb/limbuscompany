# Paczka AI P84 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 20/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P84_3c_przeciwnicy_i_anomalie_cz20.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P84_3c_przeciwnicy_i_anomalie_cz20.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [refraction2bokgak] Pasywka wroga: Passives_Abnormality_Refraction2BokGak
- plik gry: `Passives_Abnormality_Refraction2BokGak.json`

1. [[refraction2bokgak] Pasywka wroga [961802] — opis] 황금 시간 발동 이후, 턴 시작 시 [Vulnerable] 2 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: After activating Golden Time, gain 2 [Vulnerable] at the next Turn Start
   PL:
2. [[refraction2bokgak] Pasywka wroga [961803] — nazwa] 과충전
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961803].name
   limit: do 40 znaków
   EN: Overcharge
   PL:
3. [[refraction2bokgak] Pasywka wroga [961803] — opis] 턴 종료 시 [Charge] 횟수가 5 이상이면, 다음 턴에 [AttackDmgUp] 3 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: At 5+ [Charge] Count, gain 3 [AttackDmgUp] next turn
   PL:
4. [[refraction2bokgak] Pasywka wroga [961804] — nazwa] 굴절된 파열과 침잠
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961804].name
   limit: do 50 znaków
   EN: Refracted Rupture and Sinking
   PL:
5. [[refraction2bokgak] Pasywka wroga [961804] — opis] [Burst]과 [Sinking]의 위력이 30까지만 누적됨\n[Burst]과 [Sinking]의 횟수가 5까지만 누적됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961804].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Sinking]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [Burst] and [Sinking] Potency max out at 30\n[Burst] and [Sinking] Count max out at 5
   PL:
6. [[refraction2bokgak] Pasywka wroga [961805] — nazwa] 굴절 화상 부과
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961805].name
   limit: do 40 znaków
   EN: Apply Refracted Burn
   PL:
7. [[refraction2bokgak] Pasywka wroga [961805] — opis] [Combustion]을 얻을 때 위력과 횟수를 1 추가로 얻음 (순환[TabExplain] 버프는 해당하지 않음)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961805].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Combustion], [TabExplain]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When gaining [Combustion], gain 1 additional Potency and Count (does not apply on Cycle[TabExplain]-related buffs)
   PL:
8. [[refraction2bokgak] Pasywka wroga [962001] — nazwa] 매혹
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962001].name
   limit: do 40 znaków
   EN: Charmed
   PL:
9. [[refraction2bokgak] Pasywka wroga [962001] — opis] 속도가 가장 낮은 적에게 [FairyCharm] 부여\n순환 횟수에 따라 [FairyCharm] 인원 증가\n요정 부위 재생 시 [FairyCharm] 인원 증가
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962001].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [FairyCharm]
   znaczenie tagów: [FairyCharm] = 매혹 / Charmed
   EN: Inflict [FairyCharm] on the enemy with the slowest Speed\nNumber of [FairyCharm] targets increases with every Cycle Count\nNumber of [FairyCharm] targets increases when Fairy is restored
   PL:
10. [[refraction2bokgak] Pasywka wroga [962002] — nazwa] 드러난 심연
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962002].name
   limit: do 40 znaków
   EN: Uncovered Abyss
   PL:
11. [[refraction2bokgak] Pasywka wroga [962002] — opis] 요정 부위 파괴 시, 몸통이 드러남\n몸통이 다시 숨을 때, 가지고 있는 버프 및 디버프 전부 삭제
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962002].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reveal Body when Fairy is broken\nAll Buffs and Debuffs expire when the Body hides again
   PL:
12. [[refraction2bokgak] Pasywka wroga [962003] — nazwa] 앞선 미끼
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962003].name
   limit: do 40 znaków
   EN: Leading Lure
   PL:
13. [[refraction2bokgak] Pasywka wroga [962003] — opis] 요정 부위를 공격 당해도 본체 체력이 소모되지 않음\n[FairyCharm]된 수에 따라 공격 슬롯이 증가함
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962003].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [FairyCharm]
   znaczenie tagów: [FairyCharm] = 매혹 / Charmed
   EN: Cannot damage Core by damaging the Fairy\nTargets more Slots based on the number of [FairyCharm] enemies
   PL:
14. [[refraction2bokgak] Pasywka wroga [962004] — nazwa] 파괴된 밑동
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962004].name
   limit: do 40 znaków
   EN: Broken Stump
   PL:
15. [[refraction2bokgak] Pasywka wroga [962004] — opis] 몸통 부위가 파괴되면,\n- 요정이 재생될 때 체력이 60%인 상태로 적용됨\n- 스킬로 본체 체력을 회복할 때, 회복량 +20
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962004].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Body is broken:\n- Fairy will have 60% of its max HP upon restoration\n- Core heals +20 more HP from Skill effects
   PL:
16. [[refraction2bokgak] Pasywka wroga [962005] — nazwa] 진화하는 미끼
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962005].name
   limit: do 40 znaków
   EN: Evolving Lure
   PL:
17. [[refraction2bokgak] Pasywka wroga [962005] — opis] 요정 부위가 재생될 때마다 최대 체력 30% 증가
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962005].desc
   limit: do 120 znaków
   EN: Fairy gains 30% increased max HP with each restoration
   PL:
18. [[refraction2bokgak] Pasywka wroga [962006] — nazwa] 굴절된 파열과 침잠
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962006].name
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [[refraction2bokgak] Pasywka wroga [962006] — opis] [Burst]과 [Sinking]의 위력이 30까지만 누적됨\n[Burst]과 [Sinking]의 횟수가 5까지만 누적됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962006].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [[refraction2bokgak] Pasywka wroga [962007] — nazwa] 요정 가루
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962007].name
   limit: do 40 znaków
   EN: Fairy Dust
   PL:
21. [[refraction2bokgak] Pasywka wroga [962007] — opis] 요정이 죽었을 때, 모든 인격이 다음 턴에 [Breath] 5, [Breath] 횟수 2 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962007].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When the Fairy is killed, all Identities gain 5 [Breath] and +2 [Breath] Count next turn
   PL:
22. [[refraction2bokgak] Pasywka wroga [962101] — nazwa] 쇠퇴한 생명력
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962101].name
   limit: do 40 znaków
   EN: Deteriorated Persistence
   PL:
23. [[refraction2bokgak] Pasywka wroga [962101] — opis] 방어 스킬 사용 후 보호막 체력이 전부 소모되었다면, 다음 턴에 모든 부위가 [AttackDown] 3, [Vulnerable] 3을 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962101].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [AttackDown], [Vulnerable]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down; [Vulnerable] = 취약 / Fragile
   EN: If Shield HP is fully depleted after using a Defense Skill, all Parts gain 3 [AttackDown] and 3 [Vulnerable] next turn
   PL:
24. [[refraction2bokgak] Pasywka wroga [962102] — nazwa] 단단한 갑각
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962102].name
   limit: do 40 znaków
   EN: Solid Exoskeleton
   PL:
25. [[refraction2bokgak] Pasywka wroga [962102] — opis] 머리가 부위 파괴 상태가 아니라면, 매 턴마다 몸통이 [Protection] 3을 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: If Head is not broken, the Body gains 3 [Protection] every turn
   PL:
26. [[refraction2bokgak] Pasywka wroga [962103] — nazwa] 자가 충전
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962103].name
   limit: do 40 znaków
   EN: Self-charge
   PL:
27. [[refraction2bokgak] Pasywka wroga [962103] — opis] 1턴 시작 시, [SelfCharge] 3을 얻음\n순환 횟수가 늘어날수록 얻는 [SelfCharge]이 1씩 증가함 (최대 8)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962103].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [SelfCharge]
   znaczenie tagów: [SelfCharge] = 자가 충전 / Self-charge
   EN: Gain 3 [SelfCharge] at the start of Turn 1\nGain 1 additional [SelfCharge] for each Cycle Count (max 8)
   PL:
28. [[refraction2bokgak] Pasywka wroga [962104] — nazwa] 살아있는 신경
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962104].name
   limit: do 40 znaków
   EN: Living Nerves
   PL:
29. [[refraction2bokgak] Pasywka wroga [962104] — opis] 죽음을 맞이하면 해당 턴 스킬 전부 취소\n위 효과 발동 시 [SelfCharge] 10 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962104].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [SelfCharge]
   znaczenie tagów: [SelfCharge] = 자가 충전 / Self-charge
   EN: Upon death, all Skills are cancelled for the turn\nGain 10 [SelfCharge] when the effect above activates
   PL:
30. [[refraction2bokgak] Pasywka wroga [962105] — nazwa] 굴절된 출혈과 진동
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962105].name
   limit: do 40 znaków
   EN: Refracted Bleed and Tremor
   PL:
31. [[refraction2bokgak] Pasywka wroga [962105] — opis] [Laceration]과 [Vibration]의 위력이 30까지만 누적됨\n[Laceration]과 [Vibration]의 횟수가 5까지만 누적됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962105].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vibration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [Laceration] and [Vibration] Potency max out at 30\n[Laceration] and [Vibration] Count max out at 5
   PL:
32. [[refraction2bokgak] Pasywka wroga [962106] — nazwa] 굴절된 충전
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962106].name
   limit: do 40 znaków
   EN: Refracted Charge
   PL:
33. [[refraction2bokgak] Pasywka wroga [962106] — opis] 대상에게 [Charge]이 있다면, 공격 적중 시 대상의 [Charge] 횟수를 1 감소시키고 [SelfCharge] 1을 얻음 (턴당 3번, 특수 충전 포함, 위력 고정인 특수 충전 제외)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=962106].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [Charge], [SelfCharge]
   znaczenie tagów: [Charge] = 충전 / Charge; [SelfCharge] = 자가 충전 / Self-charge
   EN: On Hit: If target has [Charge], reduce target's [Charge] Count by 1 and gain 1 [SelfCharge] (3 times per turn, including 'Unique Charge', excluding 'Unique Charge' with fixed Potency)
   PL:
34. [[refraction2bokgak] Pasywka wroga [960101] — nazwa] 기억된 강화 육체
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960101].name
   limit: do 40 znaków
   EN: Reminisced Augmentation
   PL:
35. [[refraction2bokgak] Pasywka wroga [960101] — opis] 왼팔 부위 파괴 시, 매 턴마다 [Reduction] 4 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: When the Left Arm is broken, gain 4 [Reduction] every turn
   PL:
36. [[refraction2bokgak] Pasywka wroga [960102] — nazwa] 눈독 들인 요정주
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960102].name
   limit: do 40 znaków
   EN: Enticing Fairy Wine
   PL:
37. [[refraction2bokgak] Pasywka wroga [960102] — opis] 턴 시작시 요정주가 있으면, 모든 부위가 [Binding] 5 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Turn Start: When Fairy Wine is on the field, all Parts gain 5 [Binding]
   PL:
38. [[refraction2bokgak] Pasywka wroga [960201] — nazwa] 요정주
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960201].name
   limit: do 40 znaków
   EN: Fairy Wine
   PL:
39. [[refraction2bokgak] Pasywka wroga [960201] — opis] 체력이 0이 되면, 무작위 인격 3명에게 다음 턴에 [TipsinessRail] 5를 부여하고, 남은 인격에게 다음 턴에 [ParryingResultDown] 5를 부여함\n\n턴 종료시 요정주가 소멸하고, 다음 턴에 신사 요정의 본체 체력 10% 회복, [Enhancement] 2, [Agility] 2, [Protection] 2를 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960201].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [TipsinessRail], [ParryingResultDown], [Enhancement], [Agility], [Protection]
   znaczenie tagów: [TipsinessRail] = 취기 / Tipsy; [ParryingResultDown] = 합 위력 감소 / Clash Power Down; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste; [Protection] = 보호 / Protection
   EN: At 0 HP, inflict 5 [TipsinessRail] on 3 random Identities next turn, and inflict 5 [ParryingResultDown] on the other Identities next turn\n\nTurn End: Fairy Wine is removed from the field; Fairy Gentleman heals 10% Core HP and gains 2 [Enhancement], 2 [Agility], and 2 [Protection] next turn
   PL:
40. [[refraction2bokgak] Pasywka wroga [960301] — nazwa] 잃어버린 수단
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960301].name
   limit: do 40 znaków
   EN: Lost Means
   PL:
41. [[refraction2bokgak] Pasywka wroga [960301] — opis] 왼팔 부위 파괴 시, 매 턴마다 [Reduction] 4 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960301].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [[refraction2bokgak] Pasywka wroga [960302] — nazwa] 훼손된 그늘
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960302].name
   limit: do 40 znaków
   EN: Damaged Shade
   PL:
43. [[refraction2bokgak] Pasywka wroga [960302] — opis] 머리 부위 파괴 시, 매 턴마다 [DefenseDown] 5 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960302].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseDown]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When the Head is broken, gain 5 [DefenseDown] every turn
   PL:
44. [[refraction2bokgak] Pasywka wroga [960401] — nazwa] 오염시키는 잎사귀
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960401].name
   limit: do 40 znaków
   EN: Contaminating Leaf
   PL:
45. [[refraction2bokgak] Pasywka wroga [960401] — opis] 키다리 요정과 신사 요정에게 아래 효과 부여\n- 매 턴 시작 시 [Enhancement] 1 부여\n- 턴 종료 시 다음 턴에 [Enhancement] 1, [AttackDmgUp] 1 부여 (매 턴마다 얻는 효과량 +1)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960401].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [AttackDmgUp]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Apply the following effects on Fairy-Long-Legs and Fairy Gentleman:\n- Turn Start: Gain 1 [Enhancement]\n- Turn End: Gain 1 [Enhancement] and 1 [AttackDmgUp] next turn (gain +1 more every turn)
   PL:
46. [[refraction2bokgak] Pasywka wroga [960501] — nazwa] 차원 도주
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960501].name
   limit: do 40 znaków
   EN: Dimensional Escape
   PL:
47. [[refraction2bokgak] Pasywka wroga [960501] — opis] 두 번째 턴부터 일정 턴마다 4개의 무작위 차원을 소환하여 몸을 숨김.\n- 모든 부위가 흐트러짐 상태이면, 다음 턴에 발동\n- 차원으로 몸을 숨긴 상태에서는 흐트러짐 상태가 되지 않음.
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960501].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting from Turn 2, this unit summons 4 random Dimensions and hides\n- When all Parts are Staggered, this effect activates next turn\n- Cannot be Staggered while hidden inside a "Dimensional Rift"
   PL:
48. [[refraction2bokgak] Pasywka wroga [960502] — nazwa] 갇혀버린 차원 탈출
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960502].name
   limit: do 40 znaków
   EN: Trapped Dimensional Escape
   PL:
49. [[refraction2bokgak] Pasywka wroga [960502] — opis] 차원이 모두 파괴되면, 다음 턴에 차원에서 빠져나와 자신을 드러냄\n이후 [Charge] 횟수 5를 잃고, 모든 부위가 흐트러짐 손상 30을 입음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960502].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When all "Dimensional Rifts" are broken, this unit voluntarily emerges from a "Dimensional Rift" next turn\nAfterward, this unit loses 5 [Charge] Count and all of its Parts' Stagger Thresholds are raised by 30
   PL:
50. [[refraction2bokgak] Pasywka wroga [960503] — nazwa] 차원 굴절 칼날 수복
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960503].name
   limit: do 60 znaków
   EN: Regenerate Dimensional Refraction Blade
   PL:
51. [[refraction2bokgak] Pasywka wroga [960503] — opis] 칼날 부위가 파괴되면, [Charge] 횟수 5를 잃음\n다음 턴 종료 시 [Charge] 횟수 2를 소모하여 파괴된 칼날 부위를 회복함.\n\n칼날 부위가 파괴된 상태면, 매 턴 시작 시 [AttackDown] 2를 얻음.
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960503].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [AttackDown]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: When the Blade Part is broken, lose 5 [Charge] Count\nAt the next Turn End, consume 2 [Charge] Count to restore the broken Blade\n\nWhile the Blade Part is broken, gain 2 [AttackDown] at every Turn Start
   PL:
52. [[refraction2bokgak] Pasywka wroga [960504] — nazwa] 차원 강제 개방 시도 - 억지력 부분해제
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960504].name
   limit: do 90 znaków
   EN: Forced Dimensional Breach Attempt - Partial Deterrence Release
   PL:
53. [[refraction2bokgak] Pasywka wroga [960504] — opis] 본체 체력이 60% 이하가 되면, 턴이 종료되고 패턴이 변경됨\n- 차원 도주[TabExplain] 패시브 비활성화\n- 갇혀버린 차원 탈출 패시브 비활성화\n- 양팔이 파괴되지 않은 상태면, 일정 턴마다 강력한 스킬을 사용
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960504].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain]
   EN: At 60% or less Core HP, end turn and gain a new pattern\n- Deactivate "Dimensional Escape" Passive\n- Deactivate "Trapped Dimensional Escape" Passive\n- If neither of the arms is broken, use a powerful Skill every few turns
   PL:
54. [[refraction2bokgak] Pasywka wroga [960601] — nazwa] 피가 흐르는 차원
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960601].name
   limit: do 40 znaków
   EN: Hemorrhaging Dimension
   PL:
55. [[refraction2bokgak] Pasywka wroga [960601] — opis] 피가 흐르는 차원을 통과했다면, 피해량 +10%
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal +10% damage after passing through the Hemorrhaging Dimension[TabExplain]
   PL:
56. [[refraction2bokgak] Pasywka wroga [960701] — nazwa] 독이 들끓는 차원
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960701].name
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL:
57. [[refraction2bokgak] Pasywka wroga [960701] — opis] 독이 들끓는 차원을 통과했다면, 본체 최대 체력이 20% 증가
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Core gains +20% max HP after passing through the Poisonous Dimension[TabExplain]
   PL:
58. [[refraction2bokgak] Pasywka wroga [960801] — nazwa] 끊임없이 진동하는 차원
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960801].name
   limit: do 40 znaków
   EN: Tremoring Dimension
   PL:
59. [[refraction2bokgak] Pasywka wroga [960801] — opis] 끊임없이 진동하는 차원을 통과했다면, 최소 속도와 최대 속도 1 증가
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Min & Max Speed +1 after passing through the Tremoring Dimension[TabExplain]
   PL:
60. [[refraction2bokgak] Pasywka wroga [960901] — nazwa] 전류를 뿜어내는 차원
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960901].name
   limit: do 40 znaków
   EN: Electrifying Dimension
   PL:
61. [[refraction2bokgak] Pasywka wroga [960901] — opis] 전류를 뿜어내는 차원을 통과했다면, 코인 위력 +1
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=960901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Coin Power +1 after passing through the Electrifying Dimension[TabExplain]
   PL:
62. [[refraction2bokgak] Pasywka wroga [961001] — nazwa] 영원한 굴레
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961001].name
   limit: do 40 znaków
   EN: Eternal Yoke
   PL:
63. [[refraction2bokgak] Pasywka wroga [961001] — opis] 최대 체력이 (순환 횟수 X 5)%만큼 증가\n가하는 피해량이 (순환 횟수 X 5)%만큼 감소
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max HP increases by (Cycle Count x 5)%\nDeal -(Cycle Count x 5)% damage
   PL:
64. [[refraction2bokgak] Pasywka wroga [961002] — nazwa] 부서진 표지판
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961002].name
   limit: do 40 znaków
   EN: Broken Sign
   PL:
65. [[refraction2bokgak] Pasywka wroga [961002] — opis] 표지판 부위가 파괴되면 장미의 최대 체력이 20%만큼 감소
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961002].desc
   limit: do 120 znaków
   EN: When the Sign is broken, Rose loses 20% max HP
   PL:
66. [[refraction2bokgak] Pasywka wroga [961003] — nazwa] 흩어진 살점
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961003].name
   limit: do 40 znaków
   EN: Scattered Flesh
   PL:
67. [[refraction2bokgak] Pasywka wroga [961003] — opis] 살 부위가 파괴되면 본체의 최대 체력이 20%만큼 감소
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961003].desc
   limit: do 120 znaków
   EN: When the Flesh is broken, Core loses 20% max HP
   PL:
68. [[refraction2bokgak] Pasywka wroga [961004] — nazwa] 하나의 덩쿨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961004].name
   limit: do 40 znaków
   EN: Singular Vine
   PL:
69. [[refraction2bokgak] Pasywka wroga [961004] — opis] 장미 처치 시 본체와 살 부위의 체력 30 감소\n- 이후, 이번 전투 동안 해당 죄악 속성의 내성 0.1 증가 (중첩 가능)
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961004].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a Rose is defeated, Core and Flesh lose 30 HP\n- Gain 0.1 Resistance to the corresponding Sin Affinity for this Encounter (Stackable)
   PL:
70. [[refraction2bokgak] Pasywka wroga [961007] — nazwa] 죄를 머금은 가시 덩쿨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961007].name
   limit: do 40 znaków
   EN: Sin-drenched Brambles
   PL:
71. [[refraction2bokgak] Pasywka wroga [961007] — opis] 매 턴마다 모든 부위가 [PrepareSinRose] 효과를 가진 수감자 1명당, [Protection] 1, [DefenseUp] 4 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961007].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [PrepareSinRose], [Protection], [DefenseUp]
   znaczenie tagów: [PrepareSinRose] = 면류관 / Crown of Thorns; [Protection] = 보호 / Protection; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Every turn, all Parts gain 1 [Protection] and 4 [DefenseUp] for every Sinner that has the [PrepareSinRose] effect
   PL:
72. [[refraction2bokgak] Pasywka wroga [961005] — nazwa] 활짝 핀 죄악
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961005].name
   limit: do 40 znaków
   EN: Blossoming Sins
   PL:
73. [[refraction2bokgak] Pasywka wroga [961005] — opis] [BloomingRose]가 4가 되면, 이번 전투동안 [EnhanceRose]가 됨
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961005].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloomingRose], [EnhanceRose]
   znaczenie tagów: [BloomingRose] = 피어나는 죄 / Blooming Sin; [EnhanceRose] = 강화 상태 / Power-up State
   EN: At 4 [BloomingRose], enter [EnhanceRose] for this Encounter
   PL:
74. [[refraction2bokgak] Pasywka wroga [961006] — nazwa] 덩쿨에 핀 장미
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961006].name
   limit: do 40 znaków
   EN: Rose on a Vine
   PL:
75. [[refraction2bokgak] Pasywka wroga [961006] — opis] 장미 표지판 본체 사망 시 사망
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961006].desc
   limit: do 120 znaków
   EN: Dies when the Core of Sign of Roses is killed
   PL:
76. [[refraction2bokgak] Pasywka wroga [961101] — nazwa] 증오
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961101].name
   limit: do 40 znaków
   EN: Hatred
   PL:
77. [[refraction2bokgak] Pasywka wroga [961101] — opis] 피격 시 마다 다음 턴에 [AttackUp] 1, [DefenseDown] 1을 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When hit, gain 1 [AttackUp] and 1 [DefenseDown] next turn
   PL:
78. [[refraction2bokgak] Pasywka wroga [961102] — nazwa] 잔화
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961102].name
   limit: do 40 znaków
   EN: Embers
   PL:
79. [[refraction2bokgak] Pasywka wroga [961102] — opis] 사망 시 대상에게 받은 피해량만큼 피해를 주고, [Combustion] 5 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When defeated, return the damage to the attacker and inflict 5 [Combustion]
   PL:
80. [[refraction2bokgak] Pasywka wroga [961104] — nazwa] 끓어오르는 분노
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961104].name
   limit: do 40 znaków
   EN: Boiling Wrath
   PL:
81. [[refraction2bokgak] Pasywka wroga [961104] — opis] [EnhanceRose]일 때 스킬의 효과로 부여하는 [Combustion] +1\n[EnhanceRose]에서 사망 시 모든 아군에게 [Combustion] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961104].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Combustion]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Combustion] = 화상 / Burn
   EN: If this unit is in [EnhanceRose], inflict +1 more [Combustion] using Skill effects\nIf killed while in [EnhanceRose], inflict +4 [Combustion] Count to all allies
   PL:
82. [[refraction2bokgak] Pasywka wroga [961203] — nazwa] 일렁이는 색욕
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961203].name
   limit: do 40 znaków
   EN: Shimmering Lust
   PL:
83. [[refraction2bokgak] Pasywka wroga [961203] — opis] [EnhanceRose]일 때 스킬의 효과로 부여하는 [Laceration] +1\n[EnhanceRose]에서 사망 시 모든 아군에게 [Laceration] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961203].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Laceration]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Laceration] = 출혈 / Bleed
   EN: If this unit is in [EnhanceRose], inflict +1 more [Laceration] using Skill effects\nIf killed while in [EnhanceRose], inflict +4 [Laceration] Count to all allies
   PL:
84. [[refraction2bokgak] Pasywka wroga [961301] — nazwa] 무기력
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961301].name
   limit: do 40 znaków
   EN: Powerless
   PL:
85. [[refraction2bokgak] Pasywka wroga [961301] — opis] 피격 시 다음 턴에 흐트러짐 상태가 아니면 [Protection] 5를 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: When hit, gain 5 [Protection] next turn unless Staggered
   PL:
86. [[refraction2bokgak] Pasywka wroga [961303] — nazwa] 짓누르는 나태
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961303].name
   limit: do 40 znaków
   EN: Crushing Sloth
   PL:
87. [[refraction2bokgak] Pasywka wroga [961303] — opis] [EnhanceRose]일 때 스킬의 효과로 부여하는 [Vibration] +1\n[EnhanceRose]에서 사망 시 모든 아군에게 [Vibration] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961303].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Vibration]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Vibration] = 진동 / Tremor
   EN: If this unit is in [EnhanceRose], inflict +1 more [Vibration] using Skill effects\nIf killed while in [EnhanceRose], inflict +4 [Vibration] Count to all allies
   PL:
88. [[refraction2bokgak] Pasywka wroga [961401] — nazwa] 허기
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961401].name
   limit: do 40 znaków
   EN: Hunger
   PL:
89. [[refraction2bokgak] Pasywka wroga [961401] — opis] 턴 종료 시 이번 턴에 피해를 주지 못한 경우 다음 턴에 [BurstVulnerable] 2를 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstVulnerable]
   znaczenie tagów: [BurstVulnerable] = 파열 취약 / Rupture Fragility
   EN: Turn End: If this unit failed to deal damage this turn, gain 2 [BurstVulnerable] next turn
   PL:
90. [[refraction2bokgak] Pasywka wroga [961403] — nazwa] 자라나는 탐식
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961403].name
   limit: do 40 znaków
   EN: Growing Gluttony
   PL:
91. [[refraction2bokgak] Pasywka wroga [961403] — opis] [EnhanceRose]일 때 스킬의 효과로 부여하는 [Burst] +1\n[EnhanceRose]에서 사망 시 모든 아군에게 [Burst] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961403].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Burst]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Burst] = 파열 / Rupture
   EN: If this unit is in [EnhanceRose], inflict +1 more [Burst] using Skill effects\nIf killed while in [EnhanceRose], inflict +4 [Burst] Count to all allies
   PL:
92. [[refraction2bokgak] Pasywka wroga [961502] — nazwa] 자기 파괴
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961502].name
   limit: do 40 znaków
   EN: Self Destruction
   PL:
93. [[refraction2bokgak] Pasywka wroga [961502] — opis] 피격 시 다음 턴에 우울 내성이 약점(1.5)으로 변경되고, [Protection] 5 를 얻음
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: When hit, change Gloom Resist. to Weak(1.5) and gain 5 [Protection] next turn
   PL:
94. [[refraction2bokgak] Pasywka wroga [961504] — nazwa] 일렁이는 우울
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961504].name
   limit: do 40 znaków
   EN: Shimmering Gloom
   PL:
95. [[refraction2bokgak] Pasywka wroga [961504] — opis] [EnhanceRose]일 때 스킬의 효과로 부여하는 [Sinking] +1\n[EnhanceRose]에서 사망 시 모든 아군에게 [Sinking] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961504].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Sinking]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Sinking] = 침잠 / Sinking
   EN: If this unit is in [EnhanceRose], inflict +1 more [Sinking] using Skill effects\nIf killed while in [EnhanceRose], inflict +4 [Sinking] Count to all allies
   PL:
96. [[refraction2bokgak] Pasywka wroga [961604] — nazwa] 부풀어오른 오만
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961604].name
   limit: do 40 znaków
   EN: Overinflated Pride
   PL:
97. [[refraction2bokgak] Pasywka wroga [961604] — opis] [EnhanceRose]일 때 턴 시작 시, 스킬의 효과로 부여하는 [Breath] +1\n[EnhanceRose]에서 사망 시 모든 적에게 [Breath] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961604].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Breath]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Breath] = 호흡 / Poise
   EN: Turn Start: If this unit is in [EnhanceRose], apply +1 more [Breath] using Skill effects\nIf killed while in [EnhanceRose], apply +4 [Breath] Count on all enemies
   PL:
98. [[refraction2bokgak] Pasywka wroga [961704] — nazwa] 번뜩이는 질투
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961704].name
   limit: do 40 znaków
   EN: Glaring Envy
   PL:
99. [[refraction2bokgak] Pasywka wroga [961704] — opis] [EnhanceRose]일 때 턴 시작 시, 스킬의 효과로 부여하는 [Charge] 횟수 +1\n[EnhanceRose]에서 사망 시 모든 적에게 [Charge] 횟수 4 부여
   źródło: Passives_Abnormality_Refraction2BokGak.json :: dataList[id=961704].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceRose], [Charge]
   znaczenie tagów: [EnhanceRose] = 강화 상태 / Power-up State; [Charge] = 충전 / Charge
   EN: Turn Start: If this unit is in [EnhanceRose], apply +1 more [Charge] Count using Skill effects\nIf killed while in [EnhanceRose], apply +4 [Charge] Count on all enemies
   PL:

## [refraction3] Wróg / część: Enemies_Refraction3
- plik gry: `Enemies_Refraction3.json`

100. [[refraction3] Wróg / część [999999] — nazwa] 몸통
   źródło: Enemies_Refraction3.json :: dataList[id=999999].name
   limit: do 40 znaków
   EN: Body
   PL:
101. [[refraction3] Wróg / część [999999] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=999999].desc
   limit: do 120 znaków
   EN: Part
   PL:
102. [[refraction3] Wróg / część [8577] — nazwa] 굴절된 홍염나방
   źródło: Enemies_Refraction3.json :: dataList[id=8577].name
   limit: do 40 znaków
   EN: Refracted Ardor Blossom Moth
   PL:
103. [[refraction3] Wróg / część [8577] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8577].desc
   limit: do 120 znaków
   EN: Core
   PL:
104. [[refraction3] Wróg / część [857701] — nazwa] 몸통
   źródło: Enemies_Refraction3.json :: dataList[id=857701].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [[refraction3] Wróg / część [857701] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=857701].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [[refraction3] Wróg / część [857702] — nazwa] 날개
   źródło: Enemies_Refraction3.json :: dataList[id=857702].name
   limit: do 40 znaków
   EN: Wings
   PL:
107. [[refraction3] Wróg / część [857702] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=857702].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [[refraction3] Wróg / część [8578] — nazwa] 굴절된 머금은 목화
   źródło: Enemies_Refraction3.json :: dataList[id=8578].name
   limit: do 40 znaków
   EN: Refracted Drenched Gossypium
   PL:
109. [[refraction3] Wróg / część [8578] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8578].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [[refraction3] Wróg / część [857801] — nazwa] 몸통
   źródło: Enemies_Refraction3.json :: dataList[id=857801].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [[refraction3] Wróg / część [857801] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=857801].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [[refraction3] Wróg / część [8585] — nazwa] 굴절된 경멸의 나선
   źródło: Enemies_Refraction3.json :: dataList[id=8585].name
   limit: do 40 znaków
   EN: Refracted Spiral of Contempt
   PL:
113. [[refraction3] Wróg / część [8585] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8585].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [[refraction3] Wróg / część [858501] — nazwa] 몸통
   źródło: Enemies_Refraction3.json :: dataList[id=858501].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [[refraction3] Wróg / część [858501] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=858501].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [[refraction3] Wróg / część [858502] — nazwa] 손
   źródło: Enemies_Refraction3.json :: dataList[id=858502].name
   limit: do 40 znaków
   EN: Hands
   PL:
117. [[refraction3] Wróg / część [858502] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=858502].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [[refraction3] Wróg / część [8571] — nazwa] 굴절된 살갗 예언자
   źródło: Enemies_Refraction3.json :: dataList[id=8571].name
   limit: do 40 znaków
   EN: Refracted Skin Prophet
   PL:
119. [[refraction3] Wróg / część [8571] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8571].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [[refraction3] Wróg / część [8572] — nazwa] 굴절된 촛불
   źródło: Enemies_Refraction3.json :: dataList[id=8572].name
   limit: do 40 znaków
   EN: Refracted Candle
   PL:
121. [[refraction3] Wróg / część [8572] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8572].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [[refraction3] Wróg / część [8573] — nazwa] 굴절된 걷는 진주
   źródło: Enemies_Refraction3.json :: dataList[id=8573].name
   limit: do 40 znaków
   EN: Refracted Ambling Pearl
   PL:
123. [[refraction3] Wróg / część [8573] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8573].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [[refraction3] Wróg / część [8574] — nazwa] 굴절된 녹색 점액
   źródło: Enemies_Refraction3.json :: dataList[id=8574].name
   limit: do 40 znaków
   EN: Refracted Green Slime
   PL:
125. [[refraction3] Wróg / część [8574] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8574].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [[refraction3] Wróg / część [8575] — nazwa] 굴절된 꿈먹는 탁류
   źródło: Enemies_Refraction3.json :: dataList[id=8575].name
   limit: do 60 znaków
   EN: Refracted Dream-Devouring Siltcurrent
   PL:
127. [[refraction3] Wróg / część [8575] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8575].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [[refraction3] Wróg / część [8576] — nazwa] 굴절된 표류물
   źródło: Enemies_Refraction3.json :: dataList[id=8576].name
   limit: do 40 znaków
   EN: Refracted Flotsam
   PL:
129. [[refraction3] Wróg / część [8576] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8576].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [[refraction3] Wróg / część [8579] — nazwa] 굴절된 에이해브
   źródło: Enemies_Refraction3.json :: dataList[id=8579].name
   limit: do 40 znaków
   EN: Refracted Ahab
   PL:
131. [[refraction3] Wróg / część [8579] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8579].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [[refraction3] Wróg / część [8580] — nazwa] 굴절된 퀴케그
   źródło: Enemies_Refraction3.json :: dataList[id=8580].name
   limit: do 40 znaków
   EN: Refracted Queequeg
   PL:
133. [[refraction3] Wróg / część [8580] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8580].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [[refraction3] Wróg / część [8581] — nazwa] 굴절된 스타벅
   źródło: Enemies_Refraction3.json :: dataList[id=8581].name
   limit: do 40 znaków
   EN: Refracted Starbuck
   PL:
135. [[refraction3] Wróg / część [8581] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8581].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [[refraction3] Wróg / część [8582] — nazwa] 굴절된 개화 E.G.O::가스하푼
   źródło: Enemies_Refraction3.json :: dataList[id=8582].name
   limit: do 60 znaków
   EN: Refracted Effloresced E.G.O::GasHarpoon
   PL:
137. [[refraction3] Wróg / część [8582] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8582].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [[refraction3] Wróg / część [85822] — nazwa] 굴절된 개화 E.G.O::가스하푼
   źródło: Enemies_Refraction3.json :: dataList[id=85822].name
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [[refraction3] Wróg / część [85822] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=85822].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [[refraction3] Wróg / część [85823] — nazwa] 굴절된 개화 E.G.O::가스하푼
   źródło: Enemies_Refraction3.json :: dataList[id=85823].name
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [[refraction3] Wróg / część [85823] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=85823].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [[refraction3] Wróg / część [8583] — nazwa] 굴절된 눈이 먼 피쿼드타운 주민
   źródło: Enemies_Refraction3.json :: dataList[id=8583].name
   limit: do 60 znaków
   EN: Refracted Blinded Pequod Town Villager
   PL:
143. [[refraction3] Wróg / część [8583] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8583].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [[refraction3] Wróg / część [8584] — nazwa] 굴절된 입이 막힌 피쿼드타운 주민
   źródło: Enemies_Refraction3.json :: dataList[id=8584].name
   limit: do 60 znaków
   EN: Refracted Gagged Pequod Town Villager
   PL:
145. [[refraction3] Wróg / część [8584] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8584].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [[refraction3] Wróg / część [8586] — nazwa] 굴절된 구멍 손바닥 고래 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8586].name
   limit: do 60 znaków
   EN: Refracted Whale of the Porous Hand Mermaid
   PL:
147. [[refraction3] Wróg / część [8586] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8586].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [[refraction3] Wróg / część [8587] — nazwa] 굴절된 구멍 손바닥 고래 병정 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8587].name
   limit: do 70 znaków
   EN: Refracted Whale of the Porous Hand Soldier Mermaid
   PL:
149. [[refraction3] Wróg / część [8587] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8587].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [[refraction3] Wróg / część [8588] — nazwa] 굴절된 눈이 먼 피쿼드타운 주민
   źródło: Enemies_Refraction3.json :: dataList[id=8588].name
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [[refraction3] Wróg / część [8588] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8588].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [[refraction3] Wróg / część [8589] — nazwa] 굴절된 입이 막힌 피쿼드타운 주민
   źródło: Enemies_Refraction3.json :: dataList[id=8589].name
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [[refraction3] Wróg / część [8589] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8589].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [[refraction3] Wróg / część [8590] — nazwa] 굴절된 쌍갈고리 해적단 콧수염 조직원
   źródło: Enemies_Refraction3.json :: dataList[id=8590].name
   limit: do 60 znaków
   EN: Refracted Moustachioed Twinhooks Pirate
   PL:
155. [[refraction3] Wróg / część [8590] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8590].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [[refraction3] Wróg / część [8591] — nazwa] 굴절된 쌍갈고리 해적단 반다나 조직원
   źródło: Enemies_Refraction3.json :: dataList[id=8591].name
   limit: do 60 znaków
   EN: Refracted Bandana-wearing Twinhooks Pirate
   PL:
157. [[refraction3] Wróg / część [8591] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8591].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [[refraction3] Wróg / część [8592] — nazwa] 굴절된 쌍갈고리 해적단 날렵한 조직원
   źródło: Enemies_Refraction3.json :: dataList[id=8592].name
   limit: do 50 znaków
   EN: Refracted Agile Twinhooks Pirate
   PL:
159. [[refraction3] Wróg / część [8592] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8592].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [[refraction3] Wróg / część [8593] — nazwa] 굴절된 쌍갈고리 해적단 든든한 조직원
   źródło: Enemies_Refraction3.json :: dataList[id=8593].name
   limit: do 50 znaków
   EN: Refracted Tough Twinhooks Pirate
   PL:
161. [[refraction3] Wróg / część [8593] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8593].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [[refraction3] Wróg / część [8594] — nazwa] 굴절된 쌍갈고리 해적단 부선장 스미
   źródło: Enemies_Refraction3.json :: dataList[id=8594].name
   limit: do 60 znaków
   EN: Refracted Twinhook Pirates First Mate Smee
   PL:
163. [[refraction3] Wróg / część [8594] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8594].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [[refraction3] Wróg / część [8595] — nazwa] 굴절된 창백해진 것-방패
   źródło: Enemies_Refraction3.json :: dataList[id=8595].name
   limit: do 50 znaków
   EN: Refracted Pallidified Thing-Shield
   PL:
165. [[refraction3] Wróg / część [8595] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8595].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [[refraction3] Wróg / część [8596] — nazwa] 굴절된 창백해진 것-곤봉
   źródło: Enemies_Refraction3.json :: dataList[id=8596].name
   limit: do 50 znaków
   EN: Refracted Pallidified Thing-Club
   PL:
167. [[refraction3] Wróg / część [8596] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8596].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [[refraction3] Wróg / część [8597] — nazwa] 굴절된 창백해진 것-해적
   źródło: Enemies_Refraction3.json :: dataList[id=8597].name
   limit: do 50 znaków
   EN: Refracted Pallidified Thing-Pirate
   PL:
169. [[refraction3] Wróg / część [8597] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8597].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [[refraction3] Wróg / część [8598] — nazwa] 굴절된 창백해진 것-갈고리
   źródło: Enemies_Refraction3.json :: dataList[id=8598].name
   limit: do 50 znaków
   EN: Refracted Pallidified Thing-Hook
   PL:
171. [[refraction3] Wróg / część [8598] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8598].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [[refraction3] Wróg / część [8599] — nazwa] 굴절된 창백한 흰색 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8599].name
   limit: do 50 znaków
   EN: Refracted Pallid White Mermaid
   PL:
173. [[refraction3] Wróg / część [8599] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8599].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [[refraction3] Wróg / część [8600] — nazwa] 굴절된 창백한 푸른 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8600].name
   limit: do 50 znaków
   EN: Refracted Pallid Blue Mermaid
   PL:
175. [[refraction3] Wróg / część [8600] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8600].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [[refraction3] Wróg / część [8601] — nazwa] 굴절된 창백한 얽힌 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8601].name
   limit: do 50 znaków
   EN: Refracted Pallid Entwined Mermaid
   PL:
177. [[refraction3] Wróg / część [8601] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8601].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [[refraction3] Wróg / część [8602] — nazwa] 굴절된 창백하고도 푸른 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8602].name
   limit: do 50 znaków
   EN: Refracted Pallid and Blue Mermaid
   PL:
179. [[refraction3] Wróg / część [8602] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8602].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [[refraction3] Wróg / część [8603] — nazwa] 굴절된 천가닥 줄기 고래 인어
   źródło: Enemies_Refraction3.json :: dataList[id=8603].name
   limit: do 70 znaków
   EN: Refracted Whale of the Thousand Strands Mermaid
   PL:
181. [[refraction3] Wróg / część [8603] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8603].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [[refraction3] Wróg / część [8604] — nazwa] 굴절된 손아귀
   źródło: Enemies_Refraction3.json :: dataList[id=8604].name
   limit: do 40 znaków
   EN: Refracted Grasp
   PL:
183. [[refraction3] Wróg / część [8604] — opis] 본체
   źródło: Enemies_Refraction3.json :: dataList[id=8604].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [[refraction3] Wróg / część [860401] — nazwa] 손아귀
   źródło: Enemies_Refraction3.json :: dataList[id=860401].name
   limit: do 40 znaków
   EN: Grasp
   PL:
185. [[refraction3] Wróg / część [860401] — opis] 부위
   źródło: Enemies_Refraction3.json :: dataList[id=860401].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction3] Umiejętności wrogów / Anomalii — Skills_Abnormality_Refraction3
- grupa rozdziału/trybu: `refraction3` · plik: `Skills_Abnormality_Refraction3.json`

186. [Umiejętność wroga [857801] (ulepszenie 1) — nazwa] 목화 심기
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857801].levelList[level=1].name
   limit: do 40 znaków
   EN: Gossypium Planting
   PL:
187. [Umiejętność wroga [857801] (ulepszenie 1) — opis] [WhenUse] 대상에게 [MRcAfBa] 3 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [MRcAfBa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MRcAfBa] = 목화 / Gossypium
   EN: [WhenUse] Inflict 3 [MRcAfBa]
   PL:
188. [Umiejętność wroga [857801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL:
189. [Umiejętność wroga [857802] (ulepszenie 1) — nazwa] 상처 심기
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857802].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound Planting
   PL:
190. [Umiejętność wroga [857802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
191. [Umiejętność wroga [857802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 4 [Laceration]
   PL:
192. [Umiejętność wroga [857803] (ulepszenie 1) — nazwa] 빨아들이는 뿌리
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857803].levelList[level=1].name
   limit: do 40 znaków
   EN: Draining Roots
   PL:
193. [Umiejętność wroga [857803] (ulepszenie 1) — opis] [CantDuel]\n속도가 가장 느린 [MRcAfBa]를 가진 대상 공격\n대상의 ([MRcAfBa] X 10)%만큼 피해량이 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857803].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [MRcAfBa]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MRcAfBa] = 목화 / Gossypium
   EN: [CantDuel]\nAmong targets with [MRcAfBa], attack the unit with the slowest Speed;\nDeal +([MRcAfBa] x 10)% damage
   PL:
194. [Umiejętność wroga [857803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 ([MRcAfBa] X 5)%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MRcAfBa]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MRcAfBa] = 목화 / Gossypium
   EN: [OnSucceedAttack] Heal by ([MRcAfBa] x 5)% of damage dealt
   PL:
195. [Umiejętność wroga [857803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 ([MRcAfBa] X 5)%만큼 체력 회복
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [857804] (ulepszenie 1) — nazwa] 뒤덮는 목화
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857804].levelList[level=1].name
   limit: do 40 znaków
   EN: Flourishing Gossypium
   PL:
197. [Umiejętność wroga [857804] (ulepszenie 1) — opis] [Laceration]이 가장 많은 대상 공격\n[WhenUse] 메인 타겟이 [Laceration]이 가장 많은 적이면, 기본 위력 +5, 부여하는 효과 2배
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857804].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Attacks the target with the most [Laceration]\n[WhenUse] If the main target is the target with the most [Laceration], Base Power +5, inflict x2 the effects
   PL:
198. [Umiejętność wroga [857804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2, [ScarletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [OnSucceedAttack] Inflict 2 [Binding] and 2 [ScarletTakeDamageUp] next turn
   PL:
199. [Umiejętność wroga [857804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration] and +4 [Laceration] Count
   PL:
200. [Umiejętność wroga [857805] (ulepszenie 1) — nazwa] 흩뿌려지는 목화
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857805].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Gossypium
   PL:
201. [Umiejętność wroga [857805] (ulepszenie 1) — opis] 체력이 가장 낮은 [MRcAfBa]를 가진 대상 공격\n[WhenUse] 메인 타겟이 [Laceration]이 가장 많은 적이면, 기본 위력 +5\n[EndBattle] 다음 턴에 [MRcAfBb] 상태가 해제됨.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857805].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [MRcAfBa], [WhenUse], [Laceration], [EndBattle], [MRcAfBb]
   znaczenie tagów: [MRcAfBa] = 목화 / Gossypium; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndBattle] = [턴 종료 시] / [Turn End]; [MRcAfBb] = 붉게 물든 목화 / Red-stained Gossypium
   EN: Among targets with [MRcAfBa], attack the unit with the least HP\n[WhenUse] If the main target is the target with the most [Laceration], Base Power +5\n[EndBattle] [MRcAfBb] state expires next turn.
   PL:
202. [Umiejętność wroga [857805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL:
203. [Umiejętność wroga [857805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [857806] (ulepszenie 1) — nazwa] 흩어지는 바람
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857806].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Wind
   PL:
205. [Umiejętność wroga [857806] (ulepszenie 1) — opis] [OnSucceedEvade] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857806].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Laceration]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedEvade] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL:
206. [Umiejętność wroga [857807] (ulepszenie 1) — nazwa] 뒤덮혀오는 목화
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857807].levelList[level=1].name
   limit: do 40 znaków
   EN: Encroaching Gossypium
   PL:
207. [Umiejętność wroga [857807] (ulepszenie 1) — opis] [CantDuel]\n가장 느린 대상 우선 공격\n이 공격 스킬이 가하는 피해가 0이 됨.\n[StartBattle] 다음 턴에 [MRcAfBb] 상태가 됨.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857807].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [MRcAfBb]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [MRcAfBb] = 붉게 물든 목화 / Red-stained Gossypium
   EN: [CantDuel]\nPrioritizes the unit with the slowest Speed\nDamage dealt by this Attack Skill is fixed to 0.\n[StartBattle] Enter [MRcAfBb] state next turn.
   PL:
208. [Umiejętność wroga [857807] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MRcAfBa] 3 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857807].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MRcAfBa]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MRcAfBa] = 목화 / Gossypium
   EN: [OnSucceedAttack] Inflict 3 [MRcAfBa]
   PL:
209. [Umiejętność wroga [857808] (ulepszenie 1) — nazwa] 흩뿌려지는 붉게 물든 목화
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857808].levelList[level=1].name
   limit: do 50 znaków
   EN: Scattering Red-stained Gossypium
   PL:
210. [Umiejętność wroga [857808] (ulepszenie 1) — opis] [Laceration]이 가장 많은 대상을 우선 공격\n[WhenUse] 메인 타겟이 [Laceration]이 가장 많은 적이면, 기본 위력 +10\n대상의 [Laceration]이 10 이상이면, 피해량 +50%
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857808].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Prioritizes the target with the most [Laceration]\n[WhenUse] If the main target is the target with the most [Laceration], Base Power +10\nIf target has 10+ [Laceration], deal +50% damage
   PL:
211. [Umiejętność wroga [857808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration] 5 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +4 [Laceration] Count
   PL:
212. [Umiejętność wroga [857808] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 자신의 체력 회복
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857808].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal HP equal to [Laceration] on target
   PL:
213. [Umiejętność wroga [857808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration] 5 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność wroga [857808] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]만큼 자신의 체력 회복
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857808].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [857701] (ulepszenie 1) — nazwa] 화염 강타
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857701].levelList[level=1].name
   limit: do 40 znaków
   EN: Flame Strike
   PL:
216. [Umiejętność wroga [857701] (ulepszenie 1) — opis] [WhenUse] [MRcAiBa] 1 얻음
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [MRcAiBa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MRcAiBa] = 불씨 / Ember
   EN: [WhenUse] Gain 1 [MRcAiBa]
   PL:
217. [Umiejętność wroga [857701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +2 [Combustion] Count
   PL:
218. [Umiejętność wroga [857702] (ulepszenie 1) — nazwa] 홍염익
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857702].levelList[level=1].name
   limit: do 40 znaków
   EN: Ardor Blossom Pinions
   PL:
219. [Umiejętność wroga [857702] (ulepszenie 1) — opis] [WhenUse] [MRcAiBa] 1 얻음
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857702].levelList[level=1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [857702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [CrimsonResistDown] 2 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CrimsonResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CrimsonResistDown] = 분노 내성 약화 / Wrath Resist Down
   EN: [OnSucceedAttack] Inflict 2 [CrimsonResistDown] next turn
   PL:
221. [Umiejętność wroga [857703] (ulepszenie 1) — nazwa] 점화
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857703].levelList[level=1].name
   limit: do 40 znaków
   EN: Spark
   PL:
222. [Umiejętność wroga [857703] (ulepszenie 1) — opis] [WinDuel] 대상의 [Combustion]만큼 [Combustion] 부여.\n[WhenUse] 대상의 [Combustion] 횟수 2 증가.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857703].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Combustion], [WhenUse]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: [WinDuel] Inflict [Combustion] equal to [Combustion] on target.\n[WhenUse] Inflict +2 [Combustion] Count.
   PL:
223. [Umiejętność wroga [857703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [MRcAiBb]가 3 이상이면, [Combustion] 횟수 2 증가, [Combustion] 10, [MRcAiBc]를 2 부여.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MRcAiBb], [Combustion], [MRcAiBc]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MRcAiBb] = 아른거리는 불씨 / Shimmering Ember; [Combustion] = 화상 / Burn; [MRcAiBc] = 점화 / Spark
   EN: [OnSucceedAttack] If target has 3+ [MRcAiBb], inflict +2 [Combustion] Count, 10 [Combustion], and 2 [MRcAiBc].
   PL:
224. [Umiejętność wroga [857703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 6 부여, [Combustion] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion] and +4 [Combustion] Count
   PL:
225. [Umiejętność wroga [857703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [CrimsonResistDown] 2 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [857704] (ulepszenie 1) — nazwa] 분진 폭발
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857704].levelList[level=1].name
   limit: do 40 znaków
   EN: Dust Explosion
   PL:
227. [Umiejętność wroga [857704] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]이 7이상이면, 이 스킬의 합 위력 +2
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] If target has 7+ [Combustion], this Skill gains Clash Power +2
   PL:
228. [Umiejętność wroga [857704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 횟수 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL:
229. [Umiejętność wroga [857704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 가장 느린 적에게 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 횟수 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Against the enemy with the slowest Speed, inflict [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL:
230. [Umiejętność wroga [857704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL:
231. [Umiejętność wroga [857704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 가장 느린 적에게 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Against the enemy with the slowest Speed, inflict [Combustion] equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL:
232. [Umiejętność wroga [857705] (ulepszenie 1) — nazwa] 홍염살
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].name
   limit: do 40 znaków
   EN: Ardor Blossom Star
   PL:
233. [Umiejętność wroga [857705] (ulepszenie 1) — opis] (이번 턴에 홍염나방이 사용할 분노 스킬 수 * 2)만큼 합 위력이 증가\n[WhenUse] 모든 적에게 (홍염나방이 사용할 분노 스킬 수 * 2)만큼 [Combustion] 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: Gain Clash Power equal to (# of Wrath Skills that the Ardor Blossom Moth will use this turn x2)\n[WhenUse] Inflict (# of Wrath Skills that the Ardor Blossom Moth will use this turn x2) [Combustion] to all enemies
   PL:
234. [Umiejętność wroga [857705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [857705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 가장 느린 적에게 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 부여, [Combustion] 횟수 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Against the enemy with the slowest Speed, Inflict [Combustion] and [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL:
236. [Umiejętność wroga [857705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność wroga [857705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 가장 느린 적에게 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 [Combustion] 부여, [Combustion] 횟수 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [857705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상 입힘
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt
   PL:
239. [Umiejętność wroga [857705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [EndSkill] 이 피해로 흐트러짐 상태가 된 적에게 [Combustion] 10 부여.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Combustion]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn
   EN: [EndSkill] Inflict 10 [Combustion] against targets that have been Staggered by this
   PL:
240. [Umiejętność wroga [857706] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857706].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL:
241. [Umiejętność wroga [857706] (ulepszenie 1) — opis] [WhenUseEvade] 대상에게 [Combustion] 4 부여.\n[OnSucceedEvade] 다음 턴에 [MRcAiBa] 1 얻음.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUseEvade], [Combustion], [OnSucceedEvade], [MRcAiBa]
   znaczenie tagów: [WhenUseEvade] = [회피 사용시] / [On Evade Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [MRcAiBa] = 불씨 / Ember
   EN: [WhenUseEvade] Inflict 4 [Combustion].\n[OnSucceedEvade] Gain 1 [MRcAiBa] next turn.
   PL:
242. [Umiejętność wroga [857712] (ulepszenie 1) — nazwa] 불씨 지피기
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857712].levelList[level=1].name
   limit: do 40 znaków
   EN: Stoke the Flames
   PL:
243. [Umiejętność wroga [857712] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n이 공격 스킬이 가하는 피해는 0이 됨.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857712].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantDuel]\n[CantChangeTarget]\nDamage dealt by this Attack Skill is fixed to 0.
   PL:
244. [Umiejętność wroga [857712] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [MRcAiBb] 2 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857712].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MRcAiBb]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MRcAiBb] = 아른거리는 불씨 / Shimmering Ember
   EN: [OnSucceedAttack] Inflict 2 [MRcAiBb] next turn
   PL:
245. [Umiejętność wroga [858501] (ulepszenie 1) — nazwa] 꿰뚫을지니
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858501].levelList[level=1].name
   limit: do 40 znaków
   EN: It Shall Penetrate
   PL:
246. [Umiejętność wroga [858501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
247. [Umiejętność wroga [858501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +2 [Laceration] Count
   PL:
248. [Umiejętność wroga [858502] (ulepszenie 1) — nazwa] 천천히 스며들지니
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].name
   limit: do 40 znaków
   EN: It Shall Be Insidious
   PL:
249. [Umiejętność wroga [858502] (ulepszenie 1) — opis] [WinDuel] 코인 효과로 부여하는 [Vulnerable]과 [Binding]이 2배가 됨.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Vulnerable], [Binding]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Vulnerable] = 취약 / Fragile; [Binding] = 속박 / Bind
   EN: [WinDuel] Double the [Vulnerable] and [Binding] inflicted by Coin effects.
   PL:
250. [Umiejętność wroga [858502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL:
251. [Umiejętność wroga [858502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackHead] Inflict 1 [Vulnerable] next turn
   PL:
252. [Umiejętność wroga [858502] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 1 [Binding] next turn
   PL:
253. [Umiejętność wroga [858502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [858502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration], [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed; [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
255. [Umiejętność wroga [858503] (ulepszenie 1) — nazwa] 쥘지어다
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858503].levelList[level=1].name
   limit: do 40 znaków
   EN: It Shall Grip
   PL:
256. [Umiejętność wroga [858503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown] next turn
   PL:
257. [Umiejętność wroga [858503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseDown] 3 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 3 [DefenseDown] next turn
   PL:
258. [Umiejętność wroga [858503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL:
259. [Umiejętność wroga [858503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttackHead] Gain 1 [AttackDmgUp] next turn
   PL:
260. [Umiejętność wroga [858504] (ulepszenie 1) — nazwa] 옥죄이니
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858504].levelList[level=1].name
   limit: do 40 znaków
   EN: It Shall Constrict
   PL:
261. [Umiejętność wroga [858504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [MRcAmBb] 3 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MRcAmBb]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MRcAmBb] = 손아귀 / Grasp
   EN: [OnSucceedAttack] Inflict 3 [MRcAmBb]
   PL:
262. [Umiejętność wroga [858504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn
   PL:
263. [Umiejętność wroga [858504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [MRcAmBb] 3 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [858504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność wroga [858505] (ulepszenie 1) — nazwa] 지나칠지니
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858505].levelList[level=1].name
   limit: do 40 znaków
   EN: It Shall Shun
   PL:
266. [Umiejętność wroga [858505] (ulepszenie 1) — opis] 손아귀가 생존해 있다면, 최종 위력 +5
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858505].levelList[level=1].desc
   limit: do 120 znaków
   EN: If there is a surviving 'Grasp' unit, Final Power +5
   PL:
267. [Umiejętność wroga [858505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration] and +3 [Laceration] Count
   PL:
268. [Umiejętność wroga [858505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 정신력 10 피해
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage
   PL:
269. [Umiejętność wroga [858505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 20만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Raise Stagger Threshold by 20
   PL:
270. [Umiejętność wroga [858506] (ulepszenie 1) — nazwa] 모든 것을 경멸할지어다
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858506].levelList[level=1].name
   limit: do 40 znaków
   EN: And it Shall Contempt All
   PL:
271. [Umiejętność wroga [858506] (ulepszenie 1) — opis] 손아귀가 생존해 있다면, 최종 위력 +5\n[EndBattle] 모든 적의 시선 제거
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858506].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle], [MRcAmBc]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [MRcAmBc] = 시선 / Gaze
   EN: If there is a surviving 'Grasp' unit, Final Power +5\n[EndBattle] Remove [MRcAmBc] from all enemies
   PL:
272. [Umiejętność wroga [858506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration] and +2 [Laceration] Count
   PL:
273. [Umiejętność wroga [858506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration] and +2 [Laceration] Count
   PL:
274. [Umiejętność wroga [858506] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 15 피해
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858506].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 SP damage
   PL:
275. [Umiejętność wroga [858506] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] 30만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858506].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Raise Stagger Threshold by 30
   PL:
276. [Umiejętność wroga [858507] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858507].levelList[level=1].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [858507] (ulepszenie 1) — opis] [OnSucceedEvade] 대상에게 정신력 4 피해
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858507].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Deal 4 SP damage
   PL:
278. [Umiejętność wroga [857101] (ulepszenie 1) — nazwa] 6장 5절
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857101].levelList[level=1].name
   limit: do 40 znaków
   EN: 6:5
   PL:
279. [Umiejętność wroga [857101] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n대상의 피해를 자신이 받음. 다음 턴에 흐트러짐.\n[AaCePcBa]이 없는 무작위 적에게 다음 턴에 표식 부여.\n[EndBattle] 모든 촛불 체력 최대치까지 회복
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857101].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [AaCePcBa], [EndBattle]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [AaCePcBa] = 표식 / Marked; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CantDuel][CantChangeTarget]\nTake damage in the target's place. Get staggered next turn.\nInflict Marked on a random enemy without [AaCePcBa].\n[EndBattle] All Candles heal to Max HP
   PL:
280. [Umiejętność wroga [857101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 최대 체력을 5%만큼 감소.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] This unit's max HP decreases by 5%.
   PL:
281. [Umiejętność wroga [857101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 화상 10 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Burn on self
   PL:
282. [Umiejętność wroga [857101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 최대 체력을 5%만큼 감소.
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [857101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신에게 화상 10 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [857102] (ulepszenie 1) — nazwa] 예언을 멸시치 말라
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857102].levelList[level=1].name
   limit: do 40 znaków
   EN: Scorn Not the Prophecy
   PL:
285. [Umiejętność wroga [857102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Combustion] 5 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion] and +2 [Combustion] Count on target
   PL:
286. [Umiejętność wroga [857102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 체력 20 회복
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=857102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20 HP on self
   PL:
287. [Umiejętność wroga [858201] (ulepszenie 1) — nazwa] 퍼져나오는 백화
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858201].levelList[level=1].name
   limit: do 40 znaków
   EN: Insidious Pallidification
   PL:
288. [Umiejętność wroga [858201] (ulepszenie 1) — opis] [StartBattle] 최대 체력의 10%만큼 보호막을 얻음. 퀴케그의 자아 1 당 최대 체력의 0.3%만큼 보호막을 추가로 얻음.\n 보호막이 있는동안 피격 시 대상의 정신력 5 감소.\n피격 시 퀴케그의 자아 10당 스킬 1회 재사용
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858201].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 10% of Max HP as Shield. For every Queequeg's Ego, gain additional 0.3% of Max HP as additional Shield.\nWhen attacked while Shielded, attacker loses 5 SP\nWhen attacked, use this Skill once for every 10 Queequeg's Ego
   PL:
289. [Umiejętność wroga [858201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
290. [Umiejętność wroga [858201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality_Refraction3.json :: dataList[id=858201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction3] Pasywka wroga: Passives_Abnormality_Refraction3
- plik gry: `Passives_Abnormality_Refraction3.json`

291. [[refraction3] Pasywka wroga [858801] — nazwa] 주입된 증오와 미움
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858801].name
   limit: do 50 znaków
   EN: Injected Hatred and Animosity
   PL:
292. [[refraction3] Pasywka wroga [858801] — opis] 턴 종료 시 본체 체력이 50% 미만이면, 다음 턴에 [Enhancement] 1을 얻음. (전투 당 1회 발동)
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn End: At 50%- Core HP, gain 1 [Enhancement] next turn. (once per encounter)
   PL:
293. [[refraction3] Pasywka wroga [857801] — nazwa] 흰 목화
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857801].name
   limit: do 40 znaków
   EN: White Gossypium
   PL:
294. [[refraction3] Pasywka wroga [857801] — opis] 턴 종료 시 흐트러짐 상태인 적이 흐트러짐 상태에서 풀려나는 대신 다음 턴에 (흐트러짐 단계 × 8)만큼 [Laceration], [Reduction] 2를 얻음.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857801].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Reduction]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: Turn End: un-Stagger enemies, and inflict (Stagger LV x 8) [Laceration] and 2 [Reduction] on them next turn.
   PL:
295. [[refraction3] Pasywka wroga [857802] — nazwa] 얽혀오는 뿌리
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857802].name
   limit: do 40 znaków
   EN: Binding Roots
   PL:
296. [[refraction3] Pasywka wroga [857802] — opis] 턴 종료 시, 목화를 보유한 모든 적에게 다음 턴에 [Binding] 1 부여
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Turn End: Apply 1 [Binding] to all enemies with Gossypium
   PL:
297. [[refraction3] Pasywka wroga [857803] — nazwa] 붉게 물든 목화
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857803].name
   limit: do 40 znaków
   EN: Red-stained Gossypium
   PL:
298. [[refraction3] Pasywka wroga [857803] — opis] 남은 본체 체력이 20%이하일 때, 턴 종료 시 [MRcAfBb] 상태가 됨. 이후 [MRcAfBb] 상태가 해제되지 않음.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MRcAfBb]
   znaczenie tagów: [MRcAfBb] = 붉게 물든 목화 / Red-stained Gossypium
   EN: At 20%- Core HP, become [MRcAfBb] at Turn End. This [MRcAfBb] does not expire.
   PL:
299. [[refraction3] Pasywka wroga [857804] — nazwa] 피를 머금을
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857804].name
   limit: do 40 znaków
   EN: To be Drenched in Blood
   PL:
300. [[refraction3] Pasywka wroga [857804] — opis] 공격 스킬로 적중 시 대상의 [Laceration]만큼 체력 회복.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857804].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When hitting a target with an Attack Skill, heal HP equal to [Laceration] on target.
   PL:
301. [[refraction3] Pasywka wroga [857805] — nazwa] 목화 심기
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857805].name
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [[refraction3] Pasywka wroga [857805] — opis] 흩뿌려지는 목화로 합 패배 시, 다음 턴에 뒤덮혀오는 목화를 사용함.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857805].desc
   limit: do 120 znaków
   EN: If this unit loses a Clash using Scattering Gossypium, use Encroaching Gossypium next turn.
   PL:
303. [[refraction3] Pasywka wroga [857806] — nazwa] 흐드러지는 목화
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857806].name
   limit: do 40 znaków
   EN: Flowering Gossypium
   PL:
304. [[refraction3] Pasywka wroga [857806] — opis] 몸통 부위 파괴되면, 모든 적의 목화 절반 감소.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857806].desc
   limit: do 120 znaków
   EN: When the Body Part is broken, halve the value of Gossypium on all enemies.
   PL:
305. [[refraction3] Pasywka wroga [857701] — nazwa] 타오르는 불씨
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857701].name
   limit: do 40 znaków
   EN: Flaming Ember
   PL:
306. [[refraction3] Pasywka wroga [857701] — opis] 불씨 수만큼 다른 속성의 스킬 분노 속성으로 변경함.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857701].desc
   limit: do 130 znaków
   EN: Convert a number of non-Wrath Affinity Skills equal to the value of Ember into Wrath Affinity.
   PL:
307. [[refraction3] Pasywka wroga [857702] — nazwa] 맞물리는 홍염
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857702].name
   limit: do 40 znaków
   EN: Interlocking Ardor Blossom
   PL:
308. [[refraction3] Pasywka wroga [857702] — opis] 이번 턴에 홍염나방이 사용할 분노 스킬 수만큼 적중 시 [Combustion] 부여.\n적중시 (이번 턴에 홍염나방이 사용할 분노 스킬 수 X 2)만큼 체력 회복함.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857702].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On Hit, inflict [Combustion] equal to (# of Wrath Affinity Skills that the Ardor Blossom Moth will use this turn).\nOn Hit, heal HP equal to (# of Wrath Affinity Skills that the Ardor Blossom Moth will use this turn x 2).
   PL:
309. [[refraction3] Pasywka wroga [857703] — nazwa] 마지막 불씨
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857703].name
   limit: do 40 znaków
   EN: The Last Ember
   PL:
310. [[refraction3] Pasywka wroga [857703] — opis] 체력이 30%이하가 되었을 때, 얻는 [MRcAiBa] +1
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MRcAiBa]
   znaczenie tagów: [MRcAiBa] = 불씨 / Ember
   EN: At 30%- HP, gain +1 more [MRcAiBa]
   PL:
311. [[refraction3] Pasywka wroga [857704] — nazwa] 불씨 지피기
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857704].name
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [[refraction3] Pasywka wroga [857704] — opis] 홍염살을 사용할 때, 환상체의 [MRcAiBa]가 0개라면 불씨 지피기를 사용함.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857704].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MRcAiBa]
   znaczenie tagów: [MRcAiBa] = 불씨 / Ember
   EN: When using Ardor Blossom Star, if the Abnormality has 0 [MRcAiBa], use Stoke the Flames.
   PL:
313. [[refraction3] Pasywka wroga [858501] — nazwa] 경멸과 시선
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858501].name
   limit: do 40 znaków
   EN: Contempt and Gaze
   PL:
314. [[refraction3] Pasywka wroga [858501] — opis] 대상에게 손 부위 피격당 [MRcAmBc]을 1 부여. (턴 당 최대 3회)\n[MRcAmBa]이 있다면, [MRcAmBc] 얻을 수 없음.\n[MRcAmBa]이 있는 손아귀가 파괴되면, 다음 턴에 환상체 모든 부위에 [Vulnerable] 3 얻음.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858501].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [MRcAmBc], [MRcAmBa], [Vulnerable]
   znaczenie tagów: [MRcAmBc] = 시선 / Gaze; [MRcAmBa] = 경멸 / Contempt; [Vulnerable] = 취약 / Fragile
   EN: Inflict 1 [MRcAmBc] against the target every time the 'Hands' Part is hit. (3 times per turn)\nUnits with [MRcAmBa] cannot gain [MRcAmBc].\nWhen 'Grasp' unit with [MRcAmBa] is broken, all Abnormality Parts gain 3 [Vulnerable] next turn.
   PL:
315. [[refraction3] Pasywka wroga [858502] — nazwa] 전부를 보는 시선
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858502].name
   limit: do 40 znaków
   EN: All-beholding Gaze
   PL:
316. [[refraction3] Pasywka wroga [858502] — opis] 현재 본체 체력이 최대 체력의 30%이하가 되면, 모든 인격의 [MRcAmBa], [MRcAmBc]을 제거하고 모든 인격에게 [MRcAmBd]를 부여함.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858502].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [MRcAmBa], [MRcAmBc], [MRcAmBd]
   znaczenie tagów: [MRcAmBa] = 경멸 / Contempt; [MRcAmBc] = 시선 / Gaze; [MRcAmBd] = 전부를 보는 시선 / All-beholding Gaze
   EN: When the Core HP drops below 30% of Max HP, remove [MRcAmBa] and [MRcAmBc] from all Identities; then, inflict [MRcAmBd] against all Identities.
   PL:
317. [[refraction3] Pasywka wroga [858503] — nazwa] 손아귀 분쇄
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858503].name
   limit: do 40 znaków
   EN: Crushing Grasp
   PL:
318. [[refraction3] Pasywka wroga [858503] — opis] 특정 턴마다, [MRcAmBbDisplay]를 가지고 있는 인격이 없다면, 분쇄를 사용함.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858503].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MRcAmBbDisplay]
   znaczenie tagów: [MRcAmBbDisplay] = 손아귀 / Grasp
   EN: On certain turns, if none of the enemies have [MRcAmBbDisplay], use Crush.
   PL:
319. [[refraction3] Pasywka wroga [858504] — nazwa] 덧붙여진 경멸
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858504].name
   limit: do 40 znaków
   EN: Compounded Contempt
   PL:
320. [[refraction3] Pasywka wroga [858504] — opis] 턴 종료 시 [Combustion], [Laceration], [Vibration], [Burst], [Sinking]이 10 이상 부여되어있으면, 다음 턴에 부여된 수치 10 당 각 상태이상마다 [CrimsonTakeDamageUp], [ScarletTakeDamageUp], [AmberTakeDamageUp], [ShamrockTakeDamageUp], [AzureTakeDamageUp] 1을 얻음. (최대 3)
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858504].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [CrimsonTakeDamageUp], [ScarletTakeDamageUp], [AmberTakeDamageUp], [ShamrockTakeDamageUp], [AzureTakeDamageUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility …
   EN: Turn End: Gain 1 [CrimsonTakeDamageUp], [ScarletTakeDamageUp], [AmberTakeDamageUp], [ShamrockTakeDamageUp], or [AzureTakeDamageUp] (Max 3) for every 10 Potency of [Combustion], [Laceration], [Vibration], [Burst], or [Sinking] on self, respectively.
   PL:
321. [[refraction3] Pasywka wroga [858505] — nazwa] 꿰뚫린 시선
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858505].name
   limit: do 40 znaków
   EN: Penetrated Gaze
   PL:
322. [[refraction3] Pasywka wroga [858505] — opis] 크리티컬 적중으로 피격 시 스킬당 1회 [IndigoTakeDamageUp] 1을 얻음 (최대 3)\n[Charge] 횟수를 8 이상 소모한 스킬에 피격 시 스킬당 1회 [VioletTakeDamageUp] 1을 얻음. (최대 3)
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858505].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [IndigoTakeDamageUp], [Charge], [VioletTakeDamageUp]
   znaczenie tagów: [IndigoTakeDamageUp] = 오만 취약 / Pride Fragility; [Charge] = 충전 / Charge; [VioletTakeDamageUp] = 질투 취약 / Envy Fragility
   EN: When hit with a Critical Hit, gain 1 [IndigoTakeDamageUp] once per Skill (Max 3)\nWhen hit with a Skill that consumed 8+ [Charge] Count, gain 1 [VioletTakeDamageUp] once per Skill. (Max 3)
   PL:
323. [[refraction3] Pasywka wroga [860401] — nazwa] 손아귀
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=860401].name
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [[refraction3] Pasywka wroga [860401] — opis] 턴 종료 시, [MRcAmBbDisplay] 수치가 2이하라면 대상의 최대 체력 절반만큼 피해를 줌. 경멸의 나선 모든 부위를 피해만큼 회복시킴.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=860401].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [MRcAmBbDisplay]
   znaczenie tagów: [MRcAmBbDisplay] = 손아귀 / Grasp
   EN: Turn End: at 2 or fewer [MRcAmBbDisplay] Stack, deal damage equal to half of the target's Max HP. Then, all Parts of Spiral of <noparse>Contempt</noparse> heals the same amount of HP as the damage dealt by this effect.
   PL:
325. [[refraction3] Pasywka wroga [860402] — nazwa] 구출
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=860402].name
   limit: do 40 znaków
   EN: Rescue
   PL:
326. [[refraction3] Pasywka wroga [860402] — opis] 경멸을 가지고 있는 상태로 손아귀가 되었다면, 인격에 의해 손아귀가 파괴될 때, 턴 종료 시 모든 인격의 경멸 없앰.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=860402].desc
   limit: do 180 znaków
   EN: Turn End: If this unit had <noparse>Contempt</noparse> when getting Grasped, remove <noparse>Contempt</noparse> from all Identities when the Grasp is broken by an Identity.
   PL:
327. [[refraction3] Pasywka wroga [857301] — nazwa] 노출된 진주
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857301].name
   limit: do 40 znaków
   EN: Exposed Pearl
   PL:
328. [[refraction3] Pasywka wroga [857301] — opis] 턴 시작시 자신의 녹색 점액이 0이면, 흐트러짐 상태가 됨. 진주 부위가 흐트러짐 상태일 때, 진주 부위의 속성 내성이 0.5씩 감소함.\n흐트러짐이 풀릴 때, 녹색 점액 10을 얻음.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857301].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: If at 0 Green Slime, become Staggered. When the Pearl Part is Staggered, Pearl Part loses all Affinity Resistances by 0.5.\nGain 10 Green Slime when recovering from Stagger.
   PL:
329. [[refraction3] Pasywka wroga [857302] — nazwa] 모여드는 점액
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857302].name
   limit: do 40 znaków
   EN: Gathering Slime
   PL:
330. [[refraction3] Pasywka wroga [857302] — opis] 잠식 액체를 사용하는 턴에 속도가 3이 됨.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857302].desc
   limit: do 120 znaków
   EN: Fix this Part's speed to 3 for a turn when using Devouring Fluid.
   PL:
331. [[refraction3] Pasywka wroga [857401] — nazwa] 오염시키는 점액
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857401].name
   limit: do 40 znaków
   EN: Contaminating Slime
   PL:
332. [[refraction3] Pasywka wroga [857401] — opis] 턴 종료시, 모든 적에게 (4 + 살아있는 녹색 점액)만큼 독 부여.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857401].desc
   limit: do 120 znaków
   EN: Turn End: Apply (4 + Surviving Green Slime) Poison to all enemies.
   PL:
333. [[refraction3] Pasywka wroga [857501] — nazwa] 수중 호흡
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857501].name
   limit: do 40 znaków
   EN: Underwater Breathing
   PL:
334. [[refraction3] Pasywka wroga [857501] — opis] 2턴부터 매 턴마다 형광등 부위가 파괴 상태가 아니라면, 이번 턴에 호흡 10을 얻음. 호흡 횟수 3 증가.\n2턴부터 매 턴마다 형광등 부위가 파괴 상태라면, 이번 턴에 마비 1. 피해량 감소 1 얻음.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=857501].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting from turn 2, gain 10 Poise this turn if the Fluorescence Part isn't broken. Gain +3 Poise Count.\nStarting from turn 2, gain 1 Paralyze and 1 Damage Down this turn if the Fluorescence Part is broken.
   PL:
335. [[refraction3] Pasywka wroga [858601] — nazwa] 연결된 고통
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858601].name
   limit: do 40 znaków
   EN: Connected Hurt
   PL:
336. [[refraction3] Pasywka wroga [858601] — opis] 사망한다면, 연결된 인어들에게 체력 10의 피해를 주고 다음 턴에 공격 위력 증가 2를 부여.
   źródło: Passives_Abnormality_Refraction3.json :: dataList[id=858601].desc
   limit: do 120 znaków
   EN: Upon death, deal 10 damage to connected Mermaids. Then, apply 2 Damage Up next turn.
   PL:

## [refraction4] Wróg / część: Enemies_Refraction4
- plik gry: `Enemies_Refraction4.json`

337. [[refraction4] Wróg / część [8605] — nazwa] 굴절된 어느 날의 초상
   źródło: Enemies_Refraction4.json :: dataList[id=8605].name
   limit: do 50 znaków
   EN: Refracted Portrait of a Certain Day
   PL:
338. [[refraction4] Wróg / część [8605] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8605].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [[refraction4] Wróg / część [8606] — nazwa] 굴절된 초상화
   źródło: Enemies_Refraction4.json :: dataList[id=8606].name
   limit: do 40 znaków
   EN: Refracted Portrait
   PL:
340. [[refraction4] Wróg / część [8606] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8606].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [[refraction4] Wróg / część [8607] — nazwa] 굴절된 초상화
   źródło: Enemies_Refraction4.json :: dataList[id=8607].name
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [[refraction4] Wróg / część [8607] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8607].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [[refraction4] Wróg / część [8608] — nazwa] 굴절된 꿈꾸는 전기양
   źródło: Enemies_Refraction4.json :: dataList[id=8608].name
   limit: do 50 znaków
   EN: Refracted Dreaming Electric Sheep
   PL:
344. [[refraction4] Wróg / część [8608] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8608].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [[refraction4] Wróg / część [8628] — nazwa] 굴절된 발전기
   źródło: Enemies_Refraction4.json :: dataList[id=8628].name
   limit: do 40 znaków
   EN: Refracted Generator
   PL:
346. [[refraction4] Wróg / część [8628] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8628].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [[refraction4] Wróg / część [8624] — nazwa] 굴절된 심취한 약지 연구원?
   źródło: Enemies_Refraction4.json :: dataList[id=8624].name
   limit: do 60 znaków
   EN: Refracted Enamored Researcher of the Ring?
   PL:
348. [[refraction4] Wróg / część [8625] — nazwa] 굴절된 광적인 약지 연구원?
   źródło: Enemies_Refraction4.json :: dataList[id=8625].name
   limit: do 60 znaków
   EN: Refracted Mad Researcher of the Ring?
   PL:
349. [[refraction4] Wróg / część [8626] — nazwa] 굴절된 점묘파 약지 연구원?
   źródło: Enemies_Refraction4.json :: dataList[id=8626].name
   limit: do 70 znaków
   EN: Refracted Pointillist Researcher of the Ring?
   PL:
350. [[refraction4] Wróg / część [8627] — nazwa] 굴절된 넬리
   źródło: Enemies_Refraction4.json :: dataList[id=8627].name
   limit: do 40 znaków
   EN: Refracted Nelly
   PL:
351. [[refraction4] Wróg / część [8618] — nazwa] 굴절된 빼앗겨 울부짖는 힌들리
   źródło: Enemies_Refraction4.json :: dataList[id=8618].name
   limit: do 60 znaków
   EN: Refracted Hindley, The Reaved Lamenter
   PL:
352. [[refraction4] Wróg / część [8611] — nazwa] 굴절된 날렵한 에드가 가문 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8611].name
   limit: do 50 znaków
   EN: Refracted Swift Edgar Family Butler
   PL:
353. [[refraction4] Wróg / część [8612] — nazwa] 굴절된 재빠른 에드가 가문 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8612].name
   limit: do 50 znaków
   EN: Refracted Fast Edgar Family Butler
   PL:
354. [[refraction4] Wróg / część [8613] — nazwa] 굴절된 노련한 에드가 가문 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8613].name
   limit: do 60 znaków
   EN: Refracted Veteran Edgar Family Butler
   PL:
355. [[refraction4] Wróg / część [8614] — nazwa] 굴절된 교묘한 에드가 가문 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8614].name
   limit: do 50 znaków
   EN: Refracted Shifty Edgar Family Butler
   PL:
356. [[refraction4] Wróg / część [8615] — nazwa] 굴절된 숙달된 에드가 가문 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8615].name
   limit: do 60 znaków
   EN: Refracted Trained Edgar Family Butler
   PL:
357. [[refraction4] Wróg / część [8616] — nazwa] 굴절된 노련한 에드가 가문 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8616].name
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [[refraction4] Wróg / część [8609] — nazwa] 굴절된 험악한 워더링하이츠 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8609].name
   limit: do 60 znaków
   EN: Refracted Hostile Wuthering Heights Butler
   PL:
359. [[refraction4] Wróg / część [8610] — nazwa] 굴절된 단련한 워더링하이츠 버틀러
   źródło: Enemies_Refraction4.json :: dataList[id=8610].name
   limit: do 60 znaków
   EN: Refracted Trained Wuthering Heights Butler
   PL:
360. [[refraction4] Wróg / część [8617] — nazwa] 굴절된 조세핀
   źródło: Enemies_Refraction4.json :: dataList[id=8617].name
   limit: do 40 znaków
   EN: Refracted Josephine
   PL:
361. [[refraction4] Wróg / część [8629] — nazwa] 굴절된 묶인 왕
   źródło: Enemies_Refraction4.json :: dataList[id=8629].name
   limit: do 40 znaków
   EN: The Refracted King in Binds
   PL:
362. [[refraction4] Wróg / część [8619] — nazwa] 굴절된 결연한 흑운회 조직원
   źródło: Enemies_Refraction4.json :: dataList[id=8619].name
   limit: do 60 znaków
   EN: Refracted Determined Kurokumo Henchman
   PL:
363. [[refraction4] Wróg / część [8620] — nazwa] 굴절된 긴장한 흑운회 조직원
   źródło: Enemies_Refraction4.json :: dataList[id=8620].name
   limit: do 50 znaków
   EN: Refracted Tense Kurokumo Henchman
   PL:
364. [[refraction4] Wróg / część [8621] — nazwa] 굴절된 능숙한 흑운회 조직원
   źródło: Enemies_Refraction4.json :: dataList[id=8621].name
   limit: do 50 znaków
   EN: Refracted Adept Kurokumo Henchwoman
   PL:
365. [[refraction4] Wróg / część [8622] — nazwa] 굴절된 나른한 흑운회 조직원
   źródło: Enemies_Refraction4.json :: dataList[id=8622].name
   limit: do 50 znaków
   EN: Refracted Tired Kurokumo Henchwoman
   PL:
366. [[refraction4] Wróg / część [8623] — nazwa] 굴절된 흑운회 부조장 쥰
   źródło: Enemies_Refraction4.json :: dataList[id=8623].name
   limit: do 50 znaków
   EN: Refracted Kurokumo Clan Captain Jun
   PL:
367. [[refraction4] Wróg / część [8280] — nazwa] 굴절된 질투 죄종
   źródło: Enemies_Refraction4.json :: dataList[id=8280].name
   limit: do 50 znaków
   EN: Refracted Peccatulum Invidiae
   PL:
368. [[refraction4] Wróg / część [8280] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8280].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [[refraction4] Wróg / część [8292] — nazwa] 굴절된 질투 죄종?
   źródło: Enemies_Refraction4.json :: dataList[id=8292].name
   limit: do 50 znaków
   EN: Refracted Peccatulum Invidiae?
   PL:
370. [[refraction4] Wróg / część [8292] — opis] 본체
   źródło: Enemies_Refraction4.json :: dataList[id=8292].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction4] Umiejętności wrogów / Anomalii — Skills_Abnormality_Refraction4
- grupa rozdziału/trybu: `refraction4` · plik: `Skills_Abnormality_Refraction4.json`

371. [Umiejętność wroga [860501] (ulepszenie 1) — nazwa] 이곳에서 나가세요
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860501].levelList[level=1].name
   limit: do 40 znaków
   EN: Leave This Place
   PL:
372. [Umiejętność wroga [860501] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 4 이상이면, 합 위력 +1
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 4+ [Sinking], Clash Power +1
   PL:
373. [Umiejętność wroga [860501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
374. [Umiejętność wroga [860502] (ulepszenie 1) — nazwa] 그런 표정은 짓지 마시죠
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860502].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't Make That Face
   PL:
375. [Umiejętność wroga [860502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 횟수가 3 이상이면, 합 위력 +1
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 3+ [Sinking] Count, Clash Power +1
   PL:
376. [Umiejętność wroga [860502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
377. [Umiejętność wroga [860502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność wroga [860503] (ulepszenie 1) — nazwa] 당신은 누군가요?
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].name
   limit: do 40 znaków
   EN: Who Might You Be?
   PL:
379. [Umiejętność wroga [860503] (ulepszenie 1) — opis] [UninvitedGuest] 대상 우선 공격\n대상이 [UninvitedGuest]을 가지고 있을 경우, 이 스킬에서 부여하는 [Sinking], [Sinking] 횟수 +1
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [UninvitedGuest], [Sinking]
   znaczenie tagów: [UninvitedGuest] = 불청객 / Interloper; [Sinking] = 침잠 / Sinking
   EN: Prioritizes [UninvitedGuest]\nIf target has [UninvitedGuest], inflict +1 more [Sinking] Potency and Count with this Skill
   PL:
380. [Umiejętność wroga [860503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
381. [Umiejętność wroga [860503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność wroga [860503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność wroga [860503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność wroga [860503] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상에게 [UninvitedGuest]이 있다면, 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860503].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [UninvitedGuest], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [UninvitedGuest] = 불청객 / Interloper; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] If target has [UninvitedGuest], Inflict 2 [Paralysis] next turn
   PL:
385. [Umiejętność wroga [860504] (ulepszenie 1) — nazwa] 불청객인가요?
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].name
   limit: do 40 znaków
   EN: Interloper, Are You?
   PL:
386. [Umiejętność wroga [860504] (ulepszenie 1) — opis] [UninvitedGuest] 대상 우선 공격\n대상이 [UninvitedGuest]을 가지고 있을 경우, 이 스킬에서 부여하는 [Sinking], [Sinking] 횟수 +1
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].desc
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [860504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
388. [Umiejętność wroga [860504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 [Sinking] Count
   PL:
389. [Umiejętność wroga [860504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [860504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [UninvitedGuest]이 있다면, 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność wroga [860504] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860504].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [860505] (ulepszenie 1) — nazwa] 불청객은 나가세요
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860505].levelList[level=1].name
   limit: do 40 znaków
   EN: Leave, Interloper
   PL:
393. [Umiejętność wroga [860505] (ulepszenie 1) — opis] [UninvitedGuest] 대상 우선 공격\n[UninvitedGuest]을 가진 적만큼 가중치 증가\n[WhenUse] [UninvitedGuest]을 가진 적만큼 합 위력이 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860505].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [UninvitedGuest], [WhenUse]
   znaczenie tagów: [UninvitedGuest] = 불청객 / Interloper; [WhenUse] = [사용시] / [On Use]
   EN: Prioritizes [UninvitedGuest]\nGain Atk Weight equal to number of enemies with [UninvitedGuest]\n[WhenUse] Gain Clash Power equal to the number of enemies with [UninvitedGuest]
   PL:
394. [Umiejętność wroga [860505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Umiejętność wroga [860505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [860505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [SinkingSurge]
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SinkingSurge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingSurge] = 침잠쇄도 / Sinking Deluge
   EN: [OnSucceedAttack] Cause [SinkingSurge]
   PL:
397. [Umiejętność wroga [860506] (ulepszenie 1) — nazwa] 나의 주인님
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860506].levelList[level=1].name
   limit: do 40 znaków
   EN: My Master
   PL:
398. [Umiejętność wroga [860506] (ulepszenie 1) — opis] [DefeatDuel] 연결된 초상화의 모습을 보여줌
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Reveals the Portrait attached to this Skill Slot
   PL:
399. [Umiejętność wroga [860506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność wroga [860507] (ulepszenie 1) — nazwa] 슬픈 주인님
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860507].levelList[level=1].name
   limit: do 40 znaków
   EN: My Tragic Master
   PL:
401. [Umiejętność wroga [860507] (ulepszenie 1) — opis] [DefeatDuel] 연결된 초상화의 모습을 보여줌
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860507].levelList[level=1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [860507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [860601] (ulepszenie 1) — nazwa] 주인님...?
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860601].levelList[level=1].name
   limit: do 40 znaków
   EN: Master...?
   PL:
404. [Umiejętność wroga [860701] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860701].levelList[level=1].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność wroga [860801] (ulepszenie 1) — nazwa] 뿔 들이박기
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860801].levelList[level=1].name
   limit: do 40 znaków
   EN: Horned Charge
   PL:
406. [Umiejętność wroga [860801] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +1 [Charge] Count
   PL:
407. [Umiejętność wroga [860801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn
   PL:
408. [Umiejętność wroga [860802] (ulepszenie 1) — nazwa] 양뿔 들이박기
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860802].levelList[level=1].name
   limit: do 40 znaków
   EN: Ram Charge
   PL:
409. [Umiejętność wroga [860802] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860802].levelList[level=1].desc
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [860802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] next turn
   PL:
411. [Umiejętność wroga [860802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Umiejętność wroga [860803] (ulepszenie 1) — nazwa] 양울음
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860803].levelList[level=1].name
   limit: do 40 znaków
   EN: Lamb's Cry
   PL:
413. [Umiejętność wroga [860803] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL:
414. [Umiejętność wroga [860803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL:
415. [Umiejętność wroga [860804] (ulepszenie 1) — nazwa] 번개 조작
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860804].levelList[level=1].name
   limit: do 40 znaków
   EN: Lightning Manipulation
   PL:
416. [Umiejętność wroga [860804] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860804].levelList[level=1].desc
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [860804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL:
418. [Umiejętność wroga [860804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [860805] (ulepszenie 1) — nazwa] 전기울음
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860805].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Screaming
   PL:
420. [Umiejętność wroga [860805] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 4당 가중치 +1 (최대 5)\n[WhenUse] 자신의 [Charge] 횟수 5당 합 위력 +3 (최대 4)\n[WhenUse] 자신의 [Charge] 횟수 6당 [VioletDamageUp] 1 얻음 (최대 3)\n[EndBattle] 모든 [Charge] 횟수 소모. [ConnectedPlug] 제거
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860805].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [VioletDamageUp], [EndBattle], [ConnectedPlug]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up; [EndBattle] = [턴 종료 시] / [Turn End]; [ConnectedPlug] = 연결된 플러그 / Plugged In
   EN: [WhenUse] Atk Weight +1 for every 4 [Charge] Count on self (max 5)\n[WhenUse] Clash Power +3 for every 5 [Charge] Count on self (max 4)\n[WhenUse] Gain 1 [VioletDamageUp] for every 6 [Charge] Count on self (max 3)\n[EndBattle] All [Charge] Count on self expires. Loses [ConnectedPlug]
   PL:
421. [Umiejętność wroga [860805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 4 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 4 [DefenseDown] next turn
   PL:
422. [Umiejętność wroga [860805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 4 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 4 [AttackDown] next turn
   PL:
423. [Umiejętność wroga [860805] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860805].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL:
424. [Umiejętność wroga [860806] (ulepszenie 1) — nazwa] 전기울음
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860806].levelList[level=1].name
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność wroga [860806] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [Protection] 10 얻음\n[WhenUse] 자신의 [Charge] 횟수 4당 가중치 +1 (최대 5)\n[WhenUse] 자신의 [Charge] 횟수 5당 합 위력 +3 (최대 4)\n[WhenUse] 자신의 [Charge] 횟수 6당 [VioletDamageUp] 1 얻음 (최대 3)
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860806].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Protection], [Charge], [VioletDamageUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection; [Charge] = 충전 / Charge; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: [CantDuel]\n[WhenUse] Gain 10 [Protection]\n[WhenUse] Atk Weight +1 for every 4 [Charge] Count on self (max 5)\n[WhenUse] Clash Power +3 for every 5 [Charge] Count on self (max 4)\n[WhenUse] Gain 1 [VioletDamageUp] for every 6 [Charge] Count on self (max 3)
   PL:
426. [Umiejętność wroga [860807] (ulepszenie 1) — nazwa] 접지 거부
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860807].levelList[level=1].name
   limit: do 40 znaków
   EN: Grounding Refusal
   PL:
427. [Umiejętność wroga [860807] (ulepszenie 1) — opis] [AntiSheepGround]가 있는 인격 우선 공격\n[ConnectedPlug]당 합 위력 +1\n[StartBattle] (3 - [ConnectedPlug] 수) * 2만큼 [Protection]를 얻음\n[WhenUse] 자신의 [Charge] 횟수 1 증가\n[DefeatDuel] 대상에게 [AntiSheepGround]가 있다면, [ConnectedPlug] 1 얻음
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860807].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [AntiSheepGround], [ConnectedPlug], [StartBattle], [Protection], [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [AntiSheepGround] = 대양전 접지 플러그 / Anti-Ovine Grounding Plug; [ConnectedPlug] = 연결된 플러그 / Plugged In; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [AntiSheepGround]\nClash Power +1 for every [ConnectedPlug]\n[StartBattle] Gain 2(3 - [ConnectedPlug]) [Protection]\n[WhenUse] Gain +1 [Charge] Count\n[DefeatDuel] If target has [AntiSheepGround], gain 1 [ConnectedPlug]
   PL:
428. [Umiejętność wroga [860807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność wroga [860807] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860807].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [862801] (ulepszenie 1) — nazwa] 과충전 방출
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862801].levelList[level=1].name
   limit: do 40 znaków
   EN: Overcharge Release
   PL:
431. [Umiejętność wroga [862801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [862901] (ulepszenie 1) — nazwa] 휘감는 체념
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862901].levelList[level=1].name
   limit: do 40 znaków
   EN: Enveloping Resignation
   PL:
433. [Umiejętność wroga [862901] (ulepszenie 1) — opis] 대상의 [Sinking]이 6 이상이면 코인 위력 +1\n[WinDuel] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [WinDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 6+ [Sinking], Coin Power +1\n[WinDuel] Inflict +3 [Sinking] Count
   PL:
434. [Umiejętność wroga [862901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
435. [Umiejętność wroga [862901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [862902] (ulepszenie 1) — nazwa] 옥죄는 절망
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862902].levelList[level=1].name
   limit: do 40 znaków
   EN: Strangling Despair
   PL:
437. [Umiejętność wroga [862902] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당 코인 위력+1 (최대 2)\n[WinDuel] [Sinking] 횟수 3 증가\n[DefeatDuel] [Sinking] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862902].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [WinDuel], [DefeatDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Coin Power +1 for every 6 [Sinking] on target (max 2)\n[WinDuel] Inflict +3 [Sinking] Count\n[DefeatDuel] Reduce [Sinking] Count by 1
   PL:
438. [Umiejętność wroga [862902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [862902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [862902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność wroga [862903] (ulepszenie 1) — nazwa] 사슬 끊기
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862903].levelList[level=1].name
   limit: do 40 znaków
   EN: Chainbreaker
   PL:
442. [Umiejętność wroga [862903] (ulepszenie 1) — opis] 대상에게 [Binding]이 있으면 합 위력 +1\n [WinDuel] [Sinking] 횟수 4 증가\n[DefeatDuel] [Sinking] 위력 2 감소
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862903].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [WinDuel], [Sinking], [DefeatDuel]
   znaczenie tagów: [Binding] = 속박 / Bind; [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [Binding], Clash Power +1\n[WinDuel] Inflict +4 [Sinking] Count\n[DefeatDuel] Reduce [Sinking] Potency by 2
   PL:
443. [Umiejętność wroga [862903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [862903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [862903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność wroga [862903] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862903].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [862904] (ulepszenie 1) — nazwa] 구속의 사슬
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862904].levelList[level=1].name
   limit: do 40 znaków
   EN: Chains of Binding
   PL:
448. [Umiejętność wroga [862904] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당 코인 위력 +1(최대 2)\n[DefeatDuel] [Sinking] 횟수 2 감소\n[DefeatDuel] [BandageOfTheBoundKing] 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862904].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [DefeatDuel], [BandageOfTheBoundKing]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]; [BandageOfTheBoundKing] = 묶인 왕의 붕대 / Bandages of the King in Binds
   EN: Coin Power + for every 6 [Sinking] on target (max 2)\n[DefeatDuel] Reduce [Sinking] Count by 2\n[DefeatDuel] Apply [BandageOfTheBoundKing]
   PL:
449. [Umiejętność wroga [862904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여\n[OnSucceedAttack] 대상의 [Sinking] 만큼 [Vibration] 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Binding], [Sinking], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Sinking] = 침잠 / Sinking; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn\n[OnSucceedAttack] Inflict [Vibration] equal to [Sinking] on target
   PL:
450. [Umiejętność wroga [862904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
451. [Umiejętność wroga [862905] (ulepszenie 1) — nazwa] 가라앉으라
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862905].levelList[level=1].name
   limit: do 40 znaków
   EN: Thou Wilt Sink
   PL:
452. [Umiejętność wroga [862905] (ulepszenie 1) — opis] 대상에게 [Binding]이 있으면 합 위력 +1\n[WinDuel] [Sinking] 횟수 2 증가\n[DefeatDuel] [Sinking] 위력 4 감소
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862905].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [WinDuel], [Sinking], [DefeatDuel]
   znaczenie tagów: [Binding] = 속박 / Bind; [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [Binding], Clash Power +1\n[WinDuel] Inflict +2 [Sinking] Count\n[DefeatDuel] Reduce [Sinking] Potency by 4
   PL:
453. [Umiejętność wroga [862905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SinkingSurge]
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [862906] (ulepszenie 1) — nazwa] 왕의 앞으로 오라
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862906].levelList[level=1].name
   limit: do 50 znaków
   EN: Present Thyself Before the King
   PL:
455. [Umiejętność wroga [862906] (ulepszenie 1) — opis] [CantDuel]\n[StartBattle] 다음 턴에 [Binding] 5, [ComeForwardToTheKing] 1, [Enhancement] 2 얻음.\n[WhenUse] [BandageOfTheBoundKing]가 부여된 대상에게 보호막 300 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862906].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [Binding], [ComeForwardToTheKing], [Enhancement], [WhenUse], [BandageOfTheBoundKing]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [Binding] = 속박 / Bind; [ComeForwardToTheKing] = 알현의 시간 / Moment of Audience; [Enhancement] = 공격 위력 증가 / Attack Power Up; [WhenUse] = [사용시] / [On Use]; [BandageOfTheBoundKing] = 묶인 왕의 붕대 / Bandages of the King in Binds
   EN: [CantDuel]\n[StartBattle] Gain 5 [Binding], 1 [ComeForwardToTheKing], and 2 [Enhancement] next turn.\n[WhenUse] Apply 300 Shield to targets with [BandageOfTheBoundKing]
   PL:
456. [Umiejętność wroga [862906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 피해를 주었으면, 대상의 [Sinking]만큼 [Vibration] 부여
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit dealt damage to the target, inflict [Vibration] equal to [Sinking] on target
   PL:
457. [Umiejętność wroga [862906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=862906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [860602] (ulepszenie 1) — nazwa] 주인님의 초상화
   źródło: Skills_Abnormality_Refraction4.json :: dataList[id=860602].levelList[level=1].name
   limit: do 40 znaków
   EN: Master's Portrait
   PL:

## [refraction4] Pasywka wroga: Passives_Abnormality_Refraction4
- plik gry: `Passives_Abnormality_Refraction4.json`

459. [[refraction4] Pasywka wroga [860501] — nazwa] 초상화 잔상 목도
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860501].name
   limit: do 40 znaków
   EN: Portrait Afterimage Sighting
   PL:
460. [[refraction4] Pasywka wroga [860501] — opis] 주인님의 초상화와 연결된 슬롯일 경우, 초상화의 색상과 같은 색의 파장이 일어남
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860501].desc
   limit: do 210 znaków
   EN: If a Skill Slot is attached to the Master's Portrait, a shockwave in the same color as the aura around the Master's Portrait occurs when the Portrait is revealed
   PL:
461. [[refraction4] Pasywka wroga [860502] — nazwa] 불청객 쫓기
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860502].name
   limit: do 40 znaków
   EN: Throwing Out the Interloper
   PL:
462. [[refraction4] Pasywka wroga [860502] — opis] 초상화가 있을 때\n- 턴 종료시 초상화가 등장한지 3턴이 지났다면,\n- [UninvitedGuest]이 없는 편성 순서가 가장 빠른 적에게 [UninvitedGuest] 부여\n- 모든 초상화를 불태움. 불태운 가짜 초상화의 2배만큼 모든 적에게 [Sinking] 부여, [Sinking] 횟수 증가. 다음 턴에 [AttackUp], [Protection]를 얻음
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860502].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [UninvitedGuest], [Sinking], [AttackUp], [Protection]
   znaczenie tagów: [UninvitedGuest] = 불청객 / Interloper; [Sinking] = 침잠 / Sinking; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Protection] = 보호 / Protection
   EN: When the Portraits are present:\n- Turn End: Once 3 turns have passed since the Portraits have appeared...\n     - Inflict [UninvitedGuest] to the earliest-Deployed enemy without [UninvitedGuest]\n     - Incinerate all Portraits. Inflict double the amount of fake Portraits burned as [Sinking] Potency and Count against all enemies. Gain [AttackUp] and [Protection] next turn
   PL:
463. [[refraction4] Pasywka wroga [860503] — nazwa] 불청객 사냥
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860503].name
   limit: do 40 znaków
   EN: Interloper Hunt
   PL:
464. [[refraction4] Pasywka wroga [860503] — opis] 대상에게 [UninvitedGuest]이 있을 경우, 합 위력 +1, 피해량 +20%
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860503].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UninvitedGuest]
   znaczenie tagów: [UninvitedGuest] = 불청객 / Interloper
   EN: If the target has [UninvitedGuest], Clash Power +1 and deal +20% damage
   PL:
465. [[refraction4] Pasywka wroga [860507] — nazwa] 아아 주인님…
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860507].name
   limit: do 40 znaków
   EN: Ooh, Dear Master...
   PL:
466. [[refraction4] Pasywka wroga [860507] — opis] 초상화가 있을 때, 속성 및 공격 유형 내성이 0.5씩 감소 및 [Protection] 8을 얻음.\n적이 주인님의 초상화를 처치했다면, [UninvitedGuest]을 부여, 다음 턴동안 자신의 물리 내성이 0.5 상승하고 취약 5 얻음.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860507].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [UninvitedGuest]
   znaczenie tagów: [Protection] = 보호 / Protection; [UninvitedGuest] = 불청객 / Interloper
   EN: When the Portraits are present, reduce Affinity & Attack Type Resistances by 0.5, and gain 8 [Protection].\nIf the enemies defeated the Master's Portrait, inflict [UninvitedGuest] to the unit that defeated it; then gain 0.5 Phys. Resistances and 5 Fragile for the next turn.
   PL:
467. [[refraction4] Pasywka wroga [860505] — nazwa] 당신도 불청객의 식구군요?
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860505].name
   limit: do 50 znaków
   EN: You Must Be the Interloper's Family?
   PL:
468. [[refraction4] Pasywka wroga [860505] — opis] [UninvitedGuest]을 소유한 적이 생기면, 자신의 체력이 10% 떨어질 때마다 [UninvitedGuest]이 없는 적에게 [UninvitedGuest] 1 부여 (최대 4명)
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860505].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [UninvitedGuest]
   znaczenie tagów: [UninvitedGuest] = 불청객 / Interloper
   EN: When an enemy has [UninvitedGuest], inflict [UninvitedGuest] against an enemy without [UninvitedGuest] every time this unit loses 10% of its HP (max 4 enemies)
   PL:
469. [[refraction4] Pasywka wroga [860601] — nazwa] 따라오는 눈길
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860601].name
   limit: do 40 znaków
   EN: Peering Gaze
   PL:
470. [[refraction4] Pasywka wroga [860601] — opis] 존재하는 동안 모든 적에게 [Sinking] 1 부여, [Sinking] 횟수 1 증가
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: As long as this unit exists, inflict 1 [Sinking] Potency and Count every turn
   PL:
471. [[refraction4] Pasywka wroga [860602] — nazwa] 불청객
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860602].name
   limit: do 40 znaków
   EN: Interloper
   PL:
472. [[refraction4] Pasywka wroga [860602] — opis] 자신이 죽을 때, 마지막으로 자신을 공격했던 대상에게 [UninvitedGuest] 부여\n- 4명 이상의 적이 [UninvitedGuest]을 가지고 있다면 부여하지 않음
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860602].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [UninvitedGuest]
   znaczenie tagów: [UninvitedGuest] = 불청객 / Interloper
   EN: When this unit is defeated, inflict [UninvitedGuest] against the enemy that attacked this unit last\n- If 4+ enemies have [UninvitedGuest], this effect does not activate
   PL:
473. [[refraction4] Pasywka wroga [860701] — nazwa] 따라오는 눈길
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860701].name
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [[refraction4] Pasywka wroga [860701] — opis] 존재하는 동안 모든 적에게 [Sinking] 1 부여, [Sinking] 횟수 1 증가
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860701].desc
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [[refraction4] Pasywka wroga [860702] — nazwa] 불청객
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860702].name
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [[refraction4] Pasywka wroga [860702] — opis] 자신이 죽을 때, 마지막으로 자신을 공격했던 대상에게 [UninvitedGuest] 부여\n- 4명 이상의 적이 [UninvitedGuest]을 가지고 있다면 부여하지 않음
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860702].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [[refraction4] Pasywka wroga [860801] — nazwa] 낯설지 않은 플러그
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860801].name
   limit: do 40 znaków
   EN: A Familiar Connector
   PL:
478. [[refraction4] Pasywka wroga [860801] — opis] [ConnectedPlug]당 속도 최소값 1증가, [Vulnerable] 1, [AttackDmgUp] 1을 얻음\n[ConnectedPlug]가 3이 되어 다음 턴에 흐트러짐 상태가 된다면 [Vulnerable] 4를 얻음
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860801].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [ConnectedPlug], [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [ConnectedPlug] = 연결된 플러그 / Plugged In; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: For every [ConnectedPlug], gain 1 Min. Speed value, 1 [Vulnerable], and 1 [AttackDmgUp]\nWhen this unit is Staggered next turn due to having 3 [ConnectedPlug], gain 4 [Vulnerable]
   PL:
479. [[refraction4] Pasywka wroga [860802] — nazwa] 과전류
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860802].name
   limit: do 40 znaków
   EN: Overcurrent
   PL:
480. [[refraction4] Pasywka wroga [860802] — opis] 턴 종료시 자신의 [Charge] 횟수 10당 다음 턴에 [VioletDamageUp] 1 얻음 (최대 2)
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [VioletDamageUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: Turn End: For every 10 [Charge] Count on self, gain 1 [VioletDamageUp] next turn (max 2)
   PL:
481. [[refraction4] Pasywka wroga [860803] — nazwa] 벗어나고 싶은
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860803].name
   limit: do 40 znaków
   EN: Want to be Free
   PL:
482. [[refraction4] Pasywka wroga [860803] — opis] 전체 체력의 25%만큼 남았을 때, 다음 턴부터 턴이 지날때마다\n- [ParryingResultUp] 1씩 추가로 얻음\n- [AttackDmgUp] 1씩 추가로 얻음\n- [Vulnerable] 1씩 추가로 얻음
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860803].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [ParryingResultUp], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: At 25% HP, starting this turn, gain 1 of the following every turn. The values are cumulative and do not expire.\n- Gain 1 [ParryingResultUp]\n- Gain 1 [AttackDmgUp]\n- Gain 1 [Vulnerable]
   PL:
483. [[refraction4] Pasywka wroga [860804] — nazwa] 발전기
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860804].name
   limit: do 40 znaków
   EN: Generator
   PL:
484. [[refraction4] Pasywka wroga [860804] — opis] 턴 종료시 자신에게 [ConnectedPlug]와 [ThundercloudFormation]이 없다면, 다음 턴에 발전기를 한 번 소환함.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860804].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [ConnectedPlug], [ThundercloudFormation]
   znaczenie tagów: [ConnectedPlug] = 연결된 플러그 / Plugged In; [ThundercloudFormation] = 전운집 / Gathering Lightning Cloud
   EN: Turn End: If this unit does not have [ConnectedPlug] and [ThundercloudFormation], summon a Generator once next turn.
   PL:
485. [[refraction4] Pasywka wroga [862801] — nazwa] 전운집
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862801].name
   limit: do 40 znaków
   EN: Gathering Lightning Cloud
   PL:
486. [[refraction4] Pasywka wroga [862801] — opis] 턴 종료 시 전기양에게 다음 턴에 [ThundercloudFormation] 4 부여.\n이미 있다면, 부여하지 않음.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862801].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [ThundercloudFormation]
   znaczenie tagów: [ThundercloudFormation] = 전운집 / Gathering Lightning Cloud
   EN: Turn End: Apply 4 [ThundercloudFormation] to the Dreaming Electric Sheep next turn.\nDoes not apply more of this effect if it already has this effect.
   PL:
487. [[refraction4] Pasywka wroga [862802] — nazwa] 떼어내진 대양전 접지 플러그
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862802].name
   limit: do 50 znaków
   EN: Detached Anti-Ovine Grounding Plug
   PL:
488. [[refraction4] Pasywka wroga [862802] — opis] 피격 시, 공격자에게 다음 턴에 [AntiSheepGround] 1 부여 (턴 당 1회)
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AntiSheepGround]
   znaczenie tagów: [AntiSheepGround] = 대양전 접지 플러그 / Anti-Ovine Grounding Plug
   EN: When hit, inflict 1 [AntiSheepGround] to the Attacker (once per turn)
   PL:
489. [[refraction4] Pasywka wroga [862803] — nazwa] 안전 제일 플러그
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862803].name
   limit: do 40 znaków
   EN: Safety Plug
   PL:
490. [[refraction4] Pasywka wroga [862803] — opis] 받는 모든 피해가 0이 됨
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862803].desc
   limit: do 120 znaków
   EN: Reduces all damage taken to 0
   PL:
491. [[refraction4] Pasywka wroga [862901] — nazwa] 연회의 서막
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862901].name
   limit: do 40 znaków
   EN: Prelude of the Banquet
   PL:
492. [[refraction4] Pasywka wroga [862901] — opis] 2턴 시작 시 묶인 왕의 하수인을 소환한다.\n묶인 왕의 하수인은 사망 시 또 다른 하수인으로 대체되며, 총 12명의 하수인이 소환된다.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862901].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn 2 Start: Summon the retinue of the King in Binds.\nThe King has twelve retainers. Upon the death of a retainer, another will fill its place until there are none.
   PL:
493. [[refraction4] Pasywka wroga [862902] — nazwa] 연회의 끝
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862902].name
   limit: do 40 znaków
   EN: Closing of the Banquet
   PL:
494. [[refraction4] Pasywka wroga [862902] — opis] 하수인이 모두 사망하면, 전투에 직접 참여한다.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862902].desc
   limit: do 120 znaków
   EN: When all retainers are defeated, the King joins the fight.
   PL:
495. [[refraction4] Pasywka wroga [862903] — nazwa] 나오면 안되는 텍스트
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862903].name
   limit: do 40 znaków
   EN: NOTHING TO SEE HERE
   PL:
496. [[refraction4] Pasywka wroga [862903] — opis] 나오면 안되는 텍스트
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862903].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [[refraction4] Pasywka wroga [862904] — nazwa] 끊어지는 붕대
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862904].name
   limit: do 40 znaków
   EN: Snapping Bandages
   PL:
498. [[refraction4] Pasywka wroga [862904] — opis] 몸통 부위 파괴 시 모든 적에게 [BandageOfTheBoundKing]를 부여한다.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=862904].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BandageOfTheBoundKing]
   znaczenie tagów: [BandageOfTheBoundKing] = 묶인 왕의 붕대 / Bandages of the King in Binds
   EN: When the Body Part is destroyed, apply [BandageOfTheBoundKing] on all enemies.
   PL:
499. [[refraction4] Pasywka wroga [828001] — nazwa] 묶인 왕의 하수인
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828001].name
   limit: do 50 znaków
   EN: Retainer of the King in Binds
   PL:
500. [[refraction4] Pasywka wroga [828001] — opis] 이번 전투동안 [BandageOfTheBoundKing], [BigWelcome]를 얻음.\n매 턴 시작 시 묶인 왕이 이 캐릭터에게 가호를 부여함.\n묶인 왕의 가호는 턴마다 [Enhancement]를 부여, 정신력 회복, 체력 회복 순으로 달라짐. 생존한 묶인 왕의 하수인(질투 죄종)의 수가 6명 미만이면, 부여되는 가호가 강화됨.
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828001].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [BandageOfTheBoundKing], [BigWelcome], [Enhancement]
   znaczenie tagów: [BandageOfTheBoundKing] = 묶인 왕의 붕대 / Bandages of the King in Binds; [BigWelcome] = 성대한 환대 / Grand Welcome; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: - Gain [BandageOfTheBoundKing] and [BigWelcome] for this Encounter.\n- At every Turn Start, the King in Binds blesses this unit with grace.\n- The grace of the King in Binds changes every turn, in the following order: [Enhancement], SP Heal, and HP Heal. If there are less than 6 surviving Retainers(Peccatulum Invidiae), boost the grace's strength.
   PL:
501. [[refraction4] Pasywka wroga [828002] — nazwa] 나오면 안되는 텍스트
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828002].name
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [[refraction4] Pasywka wroga [828002] — opis] 나오면 안되는 텍스트
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828002].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [[refraction4] Pasywka wroga [828003] — nazwa] 나오면 안되는 텍스트
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828003].name
   limit: do 40 znaków
   EN: LOOK AWAY!
   PL:
504. [[refraction4] Pasywka wroga [828003] — opis] 나오면 안되는 텍스트
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828003].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [[refraction4] Pasywka wroga [860506] — nazwa] 굴절된 힘겨루기
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860506].name
   limit: do 40 znaków
   EN: Refracted Struggle
   PL:
506. [[refraction4] Pasywka wroga [860506] — opis] 동일한 대상과의 합이 10합 이상이면, 합 판정 시 합 위력이 현재 (합 횟수 / 10)만큼 랜덤하게 증가 또는 감소함. (소수점 버림)
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=860506].desc
   limit: do 160 znaków
   EN: At 10+ Clashes against the same enemy, randomly gain or lose Clash Power by (Clash Count / 10) in a Clash. (rounded down)
   PL:
507. [[refraction4] Pasywka wroga [828004] — nazwa] 질투 죄종 2형
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828004].name
   limit: do 40 znaków
   EN: Peccatulum Invidiae Class 2
   PL:
508. [[refraction4] Pasywka wroga [828004] — opis] 가하는 피해량 +15%, 받는 피해량 -15%
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828004].desc
   limit: do 120 znaków
   EN: Deal +15% damage and take -15% damage
   PL:
509. [[refraction4] Pasywka wroga [828005] — nazwa] 굴절된 정신
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828005].name
   limit: do 40 znaków
   EN: Refracted Mind
   PL:
510. [[refraction4] Pasywka wroga [828005] — opis] 시작 정신력 +30
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828005].desc
   limit: do 120 znaków
   EN: Entry SP +30
   PL:
511. [[refraction4] Pasywka wroga [828006] — nazwa] 굴절된 정신
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828006].name
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [[refraction4] Pasywka wroga [828006] — opis] 시작 정신력 -20
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828006].desc
   limit: do 120 znaków
   EN: Entry SP -20
   PL:
513. [[refraction4] Pasywka wroga [828007] — nazwa] 굴절된 정신
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828007].name
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [[refraction4] Pasywka wroga [828007] — opis] 시작 정신력 +45
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828007].desc
   limit: do 120 znaków
   EN: Entry SP +45
   PL:
515. [[refraction4] Pasywka wroga [828008] — nazwa] 굴절된 정신
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828008].name
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [[refraction4] Pasywka wroga [828008] — opis] 시작 정신력 +20
   źródło: Passives_Abnormality_Refraction4.json :: dataList[id=828008].desc
   limit: do 120 znaków
   EN: Entry SP +20
   PL:

## [refraction5] Wróg / część: Enemies_Refraction5
- plik gry: `Enemies_Refraction5.json`

517. [[refraction5] Wróg / część [8630] — nazwa] 굴절된 흉탄의 사수
   źródło: Enemies_Refraction5.json :: dataList[id=8630].name
   limit: do 40 znaków
   EN: Refracted Der Fluchschütze
   PL:
518. [[refraction5] Wróg / część [8630] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8630].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [[refraction5] Wróg / część [8631] — nazwa] 굴절된 옛 G사 부장
   źródło: Enemies_Refraction5.json :: dataList[id=8631].name
   limit: do 50 znaków
   EN: Refracted Old G Corp. Head Manager
   PL:
520. [[refraction5] Wróg / część [8631] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8631].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [[refraction5] Wróg / część [8632] — nazwa] 굴절된 지난 날의 침낭
   źródło: Enemies_Refraction5.json :: dataList[id=8632].name
   limit: do 60 znaków
   EN: Refracted Sleeping Bag of a Bygone Day
   PL:
522. [[refraction5] Wróg / część [8632] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8632].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [[refraction5] Wróg / część [863201] — nazwa] 머리
   źródło: Enemies_Refraction5.json :: dataList[id=863201].name
   limit: do 40 znaków
   EN: Head
   PL:
524. [[refraction5] Wróg / część [863201] — opis] 부위
   źródło: Enemies_Refraction5.json :: dataList[id=863201].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [[refraction5] Wróg / część [863202] — nazwa] 몸통
   źródło: Enemies_Refraction5.json :: dataList[id=863202].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [[refraction5] Wróg / część [863202] — opis] 부위
   źródło: Enemies_Refraction5.json :: dataList[id=863202].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [[refraction5] Wróg / część [863203] — nazwa] 사람
   źródło: Enemies_Refraction5.json :: dataList[id=863203].name
   limit: do 40 znaków
   EN: Person
   PL:
528. [[refraction5] Wróg / część [863203] — opis] 부위
   źródło: Enemies_Refraction5.json :: dataList[id=863203].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [[refraction5] Wróg / część [8634] — nazwa] 굴절된 이발사
   źródło: Enemies_Refraction5.json :: dataList[id=8634].name
   limit: do 40 znaków
   EN: The Refracted Barber
   PL:
530. [[refraction5] Wróg / część [8634] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8634].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [[refraction5] Wróg / część [8635] — nazwa] 굴절된 아파하는 테디
   źródło: Enemies_Refraction5.json :: dataList[id=8635].name
   limit: do 40 znaków
   EN: Refracted Hurting Teddy Bear
   PL:
532. [[refraction5] Wróg / część [8635] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8635].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [[refraction5] Wróg / część [8636] — nazwa] 굴절된 장미 사냥꾼
   źródło: Enemies_Refraction5.json :: dataList[id=8636].name
   limit: do 40 znaków
   EN: Refracted Rose Hunter
   PL:
534. [[refraction5] Wróg / część [8636] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8636].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [[refraction5] Wróg / część [8637] — nazwa] 굴절된 가시 올가미
   źródło: Enemies_Refraction5.json :: dataList[id=8637].name
   limit: do 40 znaków
   EN: Refracted Barbed Lasso
   PL:
536. [[refraction5] Wróg / część [8637] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8637].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [[refraction5] Wróg / część [8638] — nazwa] 굴절된 돌시네아
   źródło: Enemies_Refraction5.json :: dataList[id=8638].name
   limit: do 40 znaków
   EN: Refracted Dulcinea
   PL:
538. [[refraction5] Wróg / część [8638] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8638].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [[refraction5] Wróg / część [8639] — nazwa] 굴절된 괴로운 행렬의 피주머니
   źródło: Enemies_Refraction5.json :: dataList[id=8639].name
   limit: do 60 znaków
   EN: Refracted Bloodbag of the Painful Parade
   PL:
540. [[refraction5] Wróg / część [8639] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8639].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [[refraction5] Wróg / część [8640] — nazwa] 굴절된 뒤따르는 행렬의 피주머니
   źródło: Enemies_Refraction5.json :: dataList[id=8640].name
   limit: do 60 znaków
   EN: Refracted Bloodbag of the Rear Parade
   PL:
542. [[refraction5] Wróg / część [8640] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8640].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [[refraction5] Wróg / część [8641] — nazwa] 굴절된 행복한 행렬의 혈귀
   źródło: Enemies_Refraction5.json :: dataList[id=8641].name
   limit: do 60 znaków
   EN: Refracted Bloodfiend of the Happy Parade
   PL:
544. [[refraction5] Wróg / część [8641] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8641].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [[refraction5] Wróg / część [8642] — nazwa] 굴절된 즐거운 행렬의 혈귀
   źródło: Enemies_Refraction5.json :: dataList[id=8642].name
   limit: do 60 znaków
   EN: Refracted Bloodfiend of the Joyful Parade
   PL:
546. [[refraction5] Wróg / część [8642] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8642].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [[refraction5] Wróg / część [8643] — nazwa] 굴절된 신부
   źródło: Enemies_Refraction5.json :: dataList[id=8643].name
   limit: do 40 znaków
   EN: The Refracted Priest
   PL:
548. [[refraction5] Wróg / część [8643] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8643].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [[refraction5] Wróg / część [8644] — nazwa] 굴절된 이발사
   źródło: Enemies_Refraction5.json :: dataList[id=8644].name
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [[refraction5] Wróg / część [8644] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8644].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [[refraction5] Wróg / część [8645] — nazwa] 굴절된 돌시네아
   źródło: Enemies_Refraction5.json :: dataList[id=8645].name
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [[refraction5] Wróg / część [8645] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8645].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [[refraction5] Wróg / część [8646] — nazwa] 굴절된 도전적인 송곳니 사냥 사무소 해결사
   źródło: Enemies_Refraction5.json :: dataList[id=8646].name
   limit: do 60 znaków
   EN: Refracted Combative Fanghunt Office Fixer
   PL:
554. [[refraction5] Wróg / część [8646] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8646].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [[refraction5] Wróg / część [8647] — nazwa] 굴절된 자존심 강한 송곳니 사냥 사무소 해결사
   źródło: Enemies_Refraction5.json :: dataList[id=8647].name
   limit: do 60 znaków
   EN: Refracted Prideful Fanghunt Office Fixer
   PL:
556. [[refraction5] Wróg / część [8647] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8647].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [[refraction5] Wróg / część [8648] — nazwa] 굴절된 나태 죄종??
   źródło: Enemies_Refraction5.json :: dataList[id=8648].name
   limit: do 50 znaków
   EN: Refracted Peccatulum Pigritiae??
   PL:
558. [[refraction5] Wróg / część [8648] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8648].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [[refraction5] Wróg / część [8649] — nazwa] 굴절된 우울 죄종??
   źródło: Enemies_Refraction5.json :: dataList[id=8649].name
   limit: do 50 znaków
   EN: Refracted Peccatulum Morositatis??
   PL:
560. [[refraction5] Wróg / część [8649] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8649].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [[refraction5] Wróg / część [8650] — nazwa] 굴절된 뒤틀린 호엔하임
   źródło: Enemies_Refraction5.json :: dataList[id=8650].name
   limit: do 50 znaków
   EN: Refracted Distorted Hohenheim
   PL:
562. [[refraction5] Wróg / część [8650] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8650].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [[refraction5] Wróg / część [8651] — nazwa] 굴절된 절망하는 피주머니
   źródło: Enemies_Refraction5.json :: dataList[id=8651].name
   limit: do 50 znaków
   EN: Refracted Despairing Bloodbag
   PL:
564. [[refraction5] Wróg / część [8651] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8651].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [[refraction5] Wróg / część [8652] — nazwa] 굴절된 전락한 피주머니
   źródło: Enemies_Refraction5.json :: dataList[id=8652].name
   limit: do 40 znaków
   EN: Refracted Disgraced Bloodbag
   PL:
566. [[refraction5] Wróg / część [8652] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8652].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [[refraction5] Wróg / część [8633] — nazwa] 굴절된 사백송이의 장미
   źródło: Enemies_Refraction5.json :: dataList[id=8633].name
   limit: do 40 znaków
   EN: Refracted Four-hundred Roses
   PL:
568. [[refraction5] Wróg / część [8633] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8633].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [[refraction5] Wróg / część [863301] — nazwa] 몸통
   źródło: Enemies_Refraction5.json :: dataList[id=863301].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [[refraction5] Wróg / część [863301] — opis] 부위
   źródło: Enemies_Refraction5.json :: dataList[id=863301].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [[refraction5] Wróg / część [863302] — nazwa] 머리
   źródło: Enemies_Refraction5.json :: dataList[id=863302].name
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [[refraction5] Wróg / część [863302] — opis] 부위
   źródło: Enemies_Refraction5.json :: dataList[id=863302].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [[refraction5] Wróg / część [8684] — nazwa] 굴절된 짙어진 패잔병
   źródło: Enemies_Refraction5.json :: dataList[id=8684].name
   limit: do 40 znaków
   EN: Refracted Downcast Veteran
   PL:
574. [[refraction5] Wróg / część [8684] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8684].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [[refraction5] Wróg / część [8683] — nazwa] 굴절된 분노 죄종??
   źródło: Enemies_Refraction5.json :: dataList[id=8683].name
   limit: do 40 znaków
   EN: Refracted Peccatulum Irae??
   PL:
576. [[refraction5] Wróg / część [8683] — opis] 본체
   źródło: Enemies_Refraction5.json :: dataList[id=8683].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction5] Umiejętności wrogów / Anomalii — Skills_Abnormality_Refraction5
- grupa rozdziału/trybu: `refraction5` · plik: `Skills_Abnormality_Refraction5.json`

577. [Umiejętność wroga [863001] (ulepszenie 1) — nazwa] 후방 사격
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863001].levelList[level=1].name
   limit: do 40 znaków
   EN: Rear Line Fire
   PL:
578. [Umiejętność wroga [863001] (ulepszenie 1) — opis] 이 스킬에서 크리티컬 피해량 +10%\n[WhenUse] 자신의 [Breath] 10 이상이면, 기본 위력 +1\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863001].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: This Skill deals +10% damage on Critical Hit\n[WhenUse] At 10+ [Breath], Base Power +1\n[WhenUse] Gain 2 [Breath]
   PL:
579. [Umiejętność wroga [863001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL:
580. [Umiejętność wroga [863001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 4 [Laceration]
   PL:
581. [Umiejętność wroga [863002] (ulepszenie 1) — nazwa] 전방 사격
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863002].levelList[level=1].name
   limit: do 40 znaków
   EN: Front Line Fire
   PL:
582. [Umiejętność wroga [863002] (ulepszenie 1) — opis] 이 스킬에서 크리티컬 피해량 +10%\n[WhenUse] 자신의 [Breath] 10 이상이면, 기본 위력 +1\n[WhenUse] [Breath] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863002].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: This Skill deals +10% damage on Critical Hit\n[WhenUse] At 10+ [Breath], Base Power +1\n[WhenUse] Gain +3 [Breath] Count
   PL:
583. [Umiejętność wroga [863002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność wroga [863002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
585. [Umiejętność wroga [863003] (ulepszenie 1) — nazwa] 꿰뚫으리라
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].name
   limit: do 40 znaków
   EN: Punch Through
   PL:
586. [Umiejętność wroga [863003] (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음\n[WhenUse] 자신의 [Breath] 10 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 5 당, 코인 위력 +1 (최대 2)\n[WinDuel] 이 공격 스킬의 크리티컬 피해량 +50%
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 2 [Breath]\n[WhenUse] At 10+ [Breath], Base Power +1\n[WhenUse] Coin Power +1 for every 5 [Breath] Count on self (max 2)\n[WinDuel] This Attack Skill deals +50% damage on Critical Hit
   PL:
587. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
588. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
589. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 1, efekt 3 — opis] 이 코인에는 메인 타겟만 피해를 입음.
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target.
   PL:
590. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음\n- 첫번째 코인에서 대상이 흐트러짐 상태가 아니거나 처치하지 못했다면, 서브 타겟 중 무작위 1명이 피해를 입음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Coin deals damage only against the sub-targets\n- If the first Coin failed to kill the ally or if the target wasn't Staggered, 1 random sub-target takes damage
   PL:
592. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [863003] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863003].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [863004] (ulepszenie 1) — nazwa] 재장전 사격
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863004].levelList[level=1].name
   limit: do 40 znaków
   EN: Reload, Fire
   PL:
595. [Umiejętność wroga [863004] (ulepszenie 1) — opis] 이 공격 스킬의 크리티컬 피해량 +50%\n[WhenUse] 자신의 [Breath] 횟수 5 당, 코인 위력 +1 (최대 3)\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863004].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: This Skill deals +50% damage on Critical Hit\n[WhenUse] Coin Power +1 for every 5 [Breath] Count on self (max 3)\n[WhenUse] Gain 3 [Breath]
   PL:
596. [Umiejętność wroga [863004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 코인 1회 재사용
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse Coin once
   PL:
597. [Umiejętność wroga [863005] (ulepszenie 1) — nazwa] 헛점 파악
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863005].levelList[level=1].name
   limit: do 40 znaków
   EN: See Through Defenses
   PL:
598. [Umiejętność wroga [863005] (ulepszenie 1) — opis] [DefeatDuel] 자신의 [Breath] 절반만큼 잃음\n- 이번 턴동안 얻는 [Breath]도 절반이 됨\n- 다음 턴에 [Paralysis] 4 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863005].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [Breath], [Paralysis]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Breath] = 호흡 / Poise; [Paralysis] = 마비 / Paralyze
   EN: [DefeatDuel] Halve [Breath] on self\n- Any [Breath] gained during this turn are halved as well\n- Gain 4 [Paralysis] next turn
   PL:
599. [Umiejętność wroga [863005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [863005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [863006] (ulepszenie 1) — nazwa] 대상 지정 사격
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].name
   limit: do 40 znaków
   EN: Designated Target Fire
   PL:
602. [Umiejętność wroga [863006] (ulepszenie 1) — opis] [FellBulletMark]를 가진 대상 공격\n자신의 [Breath] 5당, 코인 위력 +1 (최대 2)\n자신의 [Breath] 횟수 3당, 기본 위력 +1 (최대 3)\n[WhenUse] 메인 타겟에게 [FellBulletMark]가 없다면, [Paralysis] 1, [Vulnerable] 3 얻음\n[EndSkill] 대상이 사망했으면, [Breath] 10 얻음, 모든 적의 정신력 15 감소
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [FellBulletMark], [Breath], [WhenUse], [Paralysis], [Vulnerable], [EndSkill]
   znaczenie tagów: [FellBulletMark] = 징표 / Stigmatized; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [Vulnerable] = 취약 / Fragile; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Attacks the target with [FellBulletMark]\nCoin Power +1 for every 5 [Breath] on self (max 2)\nBase Power +1 for every 3 [Breath] Count on self (max 3)\n[WhenUse] If the main target does not have [FellBulletMark], gain 1 [Paralysis] and 3 [Vulnerable]\n[EndSkill] If the target is defeated, gain 10 [Breath] and lower every enemy's SP by 15
   PL:
603. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 1, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음.
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 1, efekt 3 — opis] 대상에게 [FellBulletMark]가 있다면, 피해량 +100%
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [FellBulletMark]
   znaczenie tagów: [FellBulletMark] = 징표 / Stigmatized
   EN: If target has [FellBulletMark], deal +100% damage
   PL:
606. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상에게 [FellBulletMark]가 있다면, 다음 턴에 [Breath] 10 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FellBulletMark], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FellBulletMark] = 징표 / Stigmatized; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] If target has [FellBulletMark], gain 10 [Breath] next turn
   PL:
607. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음\n- 첫번째 코인에서 대상을 처치하지 못했다면, 서브 타겟 중 무작위 2명이 피해를 입음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Coin deals damage only against the sub-targets\n- If the first Coin failed to kill the target, 2 random sub-targets take damage
   PL:
609. [Umiejętność wroga [863006] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 5, [Laceration] 5 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863006].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Sinking] and 5 [Laceration]
   PL:
610. [Umiejętność wroga [863007] (ulepszenie 1) — nazwa] 대상 조정 사격
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].name
   limit: do 40 znaków
   EN: Target Readjustment Fire
   PL:
611. [Umiejętność wroga [863007] (ulepszenie 1) — opis] [CantIdentify]\n[CantChangeTarget]\n[FellBulletMark] 우선 공격\n징표를 공격하지 못했으면, 스킬이 취소됨.\n자신의 [Breath] 5당, 코인 위력 +1 (최대 2)\n자신의 [Breath] 횟수 3당, 기본 위력 +1 (최대 3)\n[EndSkill] 대상이 사망했으면, [Breath] 10 얻음, 모든 적의 정신력 15 감소
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [CantChangeTarget], [FellBulletMark], [Breath], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [FellBulletMark] = 징표 / Stigmatized; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\n[CantChangeTarget]\nPrioritizes the target with [FellBulletMark]\nIf this unit failed to attack the Stigmatized target, cancel this Skill.\nCoin Power +1 for every 5 [Breath] on self (max 2)\nBase Power +1 for every 3 [Breath] Count on self (max 3)\n[EndSkill] If the target is defeated, gain 10 [Breath] and lower every enemy's SP by 15
   PL:
612. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 1, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target
   PL:
614. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상에게 [FellBulletMark]가 있으면, 대상이 사망함
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [FellBulletMark]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [FellBulletMark] = 징표 / Stigmatized
   EN: [UnBrokenCoinOnSucceedAttack] If target has [FellBulletMark], kill the target
   PL:
615. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Breath] 10 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 10 [Breath] next turn
   PL:
616. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음\n- 첫번째 코인에서 대상을 처치하지 못했다면, 서브 타겟 중 무작위 1명이 피해를 입음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Coin deals damage only against the sub-targets\n- If the first Coin failed to kill the target, 1 random sub-target takes damage
   PL:
618. [Umiejętność wroga [863007] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 5, [Laceration] 5 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863007].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [863201] (ulepszenie 1) — nazwa] 깨물기
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863201].levelList[level=1].name
   limit: do 40 znaków
   EN: Maul
   PL:
620. [Umiejętność wroga [863201] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 4당 최종 위력 +1 (최대 5)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Final Power +1 for every 4 [Breath] Potency on self (max 5)
   PL:
621. [Umiejętność wroga [863201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 위력 3 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] Potency
   PL:
622. [Umiejętność wroga [863201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Breath] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +3 [Breath] Count
   PL:
623. [Umiejętność wroga [863202] (ulepszenie 1) — nazwa] 아작내기
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863202].levelList[level=1].name
   limit: do 40 znaków
   EN: Devastate
   PL:
624. [Umiejętność wroga [863202] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 4당 최종 위력 +1 (최대 5)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863202].levelList[level=1].desc
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [863202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 위력 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] Potency
   PL:
626. [Umiejętność wroga [863202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +2 [Breath] Count
   PL:
627. [Umiejętność wroga [863202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 위력 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 625 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [863202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność wroga [863203] (ulepszenie 1) — nazwa] 고통스런 숨소리
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863203].levelList[level=1].name
   limit: do 40 znaków
   EN: Labored Breathing
   PL:
630. [Umiejętność wroga [863203] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 8당 최종 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 횟수 8당 코인 위력 +1 (최대 5)\n[DefeatDuel] 자신의 [Breath] 위력이 절반으로 감소\n[EndSkill] 자신의 [Breath] 위력과 [Breath] 횟수가 절반으로 감소
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863203].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Final Power +1 for every 8 [Breath] Potency on self (max 5)\n[WhenUse] Coin Power +1 for every 8 [Breath] Count on self (max 5)\n[DefeatDuel] Halve [Breath] Potency on self\n[EndSkill] Halve [Breath] Potency and Count on self
   PL:
631. [Umiejętność wroga [863203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [863203] (ulepszenie 1) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +([Breath] 위력)%
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Deal +([Breath] Potency)% damage on Critical Hit
   PL:
633. [Umiejętność wroga [863211] (ulepszenie 1) — nazwa] 웅크리기
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863211].levelList[level=1].name
   limit: do 40 znaków
   EN: Prone
   PL:
634. [Umiejętność wroga [863211] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 4당 최종 위력 +1 (최대 5)\n[WhenUse] [Breath] 위력 4 얻음\n- 체력이 50% 이하면, [Breath] 횟수 4 추가로 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863211].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Final Power +1 for every 4 [Breath] Potency on self (max 5)\n[WhenUse] Gain 4 [Breath] Potency\n- At 50%- HP, also gain +4 [Breath] Count
   PL:
635. [Umiejętność wroga [863212] (ulepszenie 1) — nazwa] 그건… 내꺼야!
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863212].levelList[level=1].name
   limit: do 40 znaków
   EN: That's... MINE!
   PL:
636. [Umiejętność wroga [863212] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse] 자신의 [Breath] 위력 4당 합 위력 +1 (최대 3)\n[WhenUse] 자신의 [Breath] 횟수 4당 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863212].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [Breath]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CantChangeTarget]\n[WhenUse] Clash Power +1 for every 4 [Breath] Potency on self (max 3)\n[WhenUse] Clash Power +1 for every 4 [Breath] Count on self (max 3)
   PL:
637. [Umiejętność wroga [863212] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863212].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność wroga [863212] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상이 보유한 [Breath] 위력과 [Breath] 횟수를 각각 가져옴 (각각 최대 6)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863212].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Siphons [Breath] Potency and [Breath] Count from the target (max 6 each)
   PL:
639. [Umiejętność wroga [863212] (ulepszenie 1) — moneta 1, efekt 3 — opis] [DefeatDuelAttack] 대상이 보유한 [Breath] 위력과 [Breath] 횟수를 각각 1/3만큼 가져옴 (각각 최대 2)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863212].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [DefeatDuelAttack], [Breath]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Breath] = 호흡 / Poise
   EN: [DefeatDuelAttack] Siphons 1/3 of the [Breath] Potency and [Breath] Count on the target (max 2 each)
   PL:
640. [Umiejętność wroga [863213] (ulepszenie 1) — nazwa] 고통 함께하기
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].name
   limit: do 40 znaków
   EN: Share the Pain
   PL:
641. [Umiejętność wroga [863213] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 8당 최종 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 횟수 8당 코인 위력 +1 (최대 5)\n[DefeatDuel] 피해량이 75%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [Breath] 위력과 [Breath] 횟수가 절반으로 감소
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Final Power +1 for every 8 [Breath] Potency on self (max 5)\n[WhenUse] Coin Power +1 for every 8 [Breath] Count on self (max 5)\n[DefeatDuel] Deal -75% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Halve [Breath] Potency and Count on self
   PL:
642. [Umiejętność wroga [863213] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [863213] (ulepszenie 1) — moneta 1, efekt 2 — opis] [WinDuelAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Binding]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Binding] = 속박 / Bind
   EN: [WinDuelAttack] Inflict 2 [Binding] next turn
   PL:
644. [Umiejętność wroga [863213] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [863213] (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vulnerable]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vulnerable] = 취약 / Fragile
   EN: [WinDuelAttack] Inflict 2 [Vulnerable]
   PL:
646. [Umiejętność wroga [863213] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność wroga [863213] (ulepszenie 1) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합)%
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863213].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Deal +([Breath] Potency + [Breath] Count)% damage on Critical Hit
   PL:
648. [Umiejętność wroga [863221] (ulepszenie 1) — nazwa] 고통스런 삶에서의 해방
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863221].levelList[level=1].name
   limit: do 50 znaków
   EN: Freed from the Life of Suffering
   PL:
649. [Umiejętność wroga [863221] (ulepszenie 1) — opis] [StartBattle] [Vulnerable] 2 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863221].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vulnerable]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vulnerable] = 취약 / Fragile
   EN: [StartBattle] Gain 2 [Vulnerable]
   PL:
650. [Umiejętność wroga [863301] (ulepszenie 1) — nazwa] 집요한 상처내기
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863301].levelList[level=1].name
   limit: do 40 znaków
   EN: Tenacious Wound
   PL:
651. [Umiejętność wroga [863301] (ulepszenie 1) — opis] 대상의 [Laceration] 위력이 6 이상이면, 이 스킬에서 부여하는 [Laceration] 위력과 횟수의 값 +1
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863301].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration] Potency, +1 to [Laceration] Potency and Count inflicted by this Skill
   PL:
652. [Umiejętność wroga [863301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [863301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
654. [Umiejętność wroga [863301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [863301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
656. [Umiejętność wroga [863302] (ulepszenie 1) — nazwa] 상처내기
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863302].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound
   PL:
657. [Umiejętność wroga [863302] (ulepszenie 1) — opis] 대상의 [Laceration] 위력이 6 이상이면, 이 스킬에서 부여하는 [Laceration] 위력과 횟수의 값 +1
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863302].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność wroga [863302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [863302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [863303] (ulepszenie 1) — nazwa] 죄어오는 가시덩굴
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863303].levelList[level=1].name
   limit: do 40 znaków
   EN: Brambles that Constrict
   PL:
661. [Umiejętność wroga [863303] (ulepszenie 1) — opis] 대상의 [Laceration] 위력이 6 이상이면, 이 스킬에서 부여하는 [Laceration] 위력의 값 +1
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration] Potency, +1 to [Laceration] Potency inflicted by this Skill
   PL:
662. [Umiejętność wroga [863303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność wroga [863303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
664. [Umiejętność wroga [863303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration]
   PL:
665. [Umiejętność wroga [863311] (ulepszenie 1) — nazwa] 목마른 꽃잎
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863311].levelList[level=1].name
   limit: do 40 znaków
   EN: Polydipsic Petals
   PL:
666. [Umiejętność wroga [863311] (ulepszenie 1) — opis] [Laceration] 위력과 횟수의 합이 가장 높은 대상에게 시전\n[WhenUse] 대상의 [Laceration] 위력이 6 이상이면, 최종 위력 +2
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863311].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Attacks the target with the highest sum of [Laceration] Potency + Count\n[WhenUse] If target has 6+ [Laceration] Potency, Final Power +2
   PL:
667. [Umiejętność wroga [863311] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ScarletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [OnSucceedAttack] Inflict 2 [ScarletTakeDamageUp]
   PL:
668. [Umiejętność wroga [863311] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863311].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target once (reduce [Laceration] Count by 1)
   PL:
669. [Umiejętność wroga [863312] (ulepszenie 1) — nazwa] 폭발하는 꽃잎
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863312].levelList[level=1].name
   limit: do 40 znaków
   EN: Bursting Petals
   PL:
670. [Umiejętność wroga [863312] (ulepszenie 1) — opis] [Laceration] 위력과 횟수의 합이 가장 높은 대상에게 시전\n[WhenUse] 대상의 [Laceration] 위력이 6 이상이면, 최종 위력 +2
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863312].levelList[level=1].desc
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność wroga [863312] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ScarletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863312].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 667 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [863312] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 모두 발동 ([Laceration] 횟수 모두 감소)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863312].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate all [Laceration] on the target (completely reduce [Laceration] Count)
   PL:
673. [Umiejętność wroga [863313] (ulepszenie 1) — nazwa] 가시 폭풍
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863313].levelList[level=1].name
   limit: do 40 znaków
   EN: Storm of Spikes
   PL:
674. [Umiejętność wroga [863313] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 위력이 6 이상이면, 최종 위력 +2
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863313].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration] Potency, Final Power +2
   PL:
675. [Umiejętność wroga [863313] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1회 감소)
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863313].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target once (reduce [Laceration] Count by 1)
   PL:
676. [Umiejętność wroga [863314] (ulepszenie 1) — nazwa] 목마른 가시
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].name
   limit: do 40 znaków
   EN: Polydipsic Thorn
   PL:
677. [Umiejętność wroga [863314] (ulepszenie 1) — opis] [StartBattle] [AttackDmgUp] 3, [Vulnerable] 2 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: [StartBattle] Gain 3 [AttackDmgUp] and 2 [Vulnerable]
   PL:
678. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
681. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność wroga [863314] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863314].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Umiejętność wroga [863315] (ulepszenie 1) — nazwa] 멈추지 않는 피
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].name
   limit: do 40 znaków
   EN: Endless Spring of Blood
   PL:
688. [Umiejętność wroga [863315] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 이 스킬과 합을 하는 대상은 합을 진행하는 동안 [Laceration] 횟수가 감소하지 않음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[WhenUse] Targets that clash against this Skill do not lose [Laceration] Count while clashing
   PL:
689. [Umiejętność wroga [863315] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [863315] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]을 1회 발동시키고, 해당 [Laceration] 피해로 생성된 [BloodDinner]을 즉시 소모함
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Activate [Laceration] on the target once, and immediately consume [BloodDinner] generated by the [Laceration] damage
   PL:
691. [Umiejętność wroga [863315] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność wroga [863315] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]을 1회 발동시키고, 해당 [Laceration] 피해로 생성된 [BloodDinner]을 즉시 소모함
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Umiejętność wroga [863315] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [863315] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]을 1회 발동시키고, 해당 [Laceration] 피해로 생성된 [BloodDinner]을 즉시 소모함
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863315].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Umiejętność wroga [863316] (ulepszenie 1) — nazwa] 양분 탐닉
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863316].levelList[level=1].name
   limit: do 40 znaków
   EN: Nutrient Craving
   PL:
696. [Umiejętność wroga [863316] (ulepszenie 1) — opis] [BloodDinner]이 100 이상이면 사용\n[EndBattle] [BloodDinner]을 최대 100 소모하여 아래 효과 적용\n- 소모한 [BloodDinner]만큼 본체와 몸통 부위 체력 회복\n- 소모한 [BloodDinner] 20 당 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863316].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [EndBattle], [AttackUp]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [EndBattle] = [턴 종료 시] / [Turn End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Activates at 100+ [BloodDinner]\n[EndBattle] Consume up to 100 [BloodDinner] to activate the following effects:\n- Heal the Core and the Body Parts' HP by [BloodDinner] consumed\n- Gain 1 [AttackUp] next turn for every 20 [BloodDinner] consumed
   PL:
697. [Umiejętność wroga [863317] (ulepszenie 1) — nazwa] 갈망하는 가시덩굴
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863317].levelList[level=1].name
   limit: do 40 znaków
   EN: Brambles that Yearn
   PL:
698. [Umiejętność wroga [863317] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 100 소모하여 아래 효과 적용\n- 소모한 [BloodDinner]만큼 본체와 몸통 부위 체력 회복\n- 소모한 [BloodDinner] 20 당 이 스킬의 최종 위력 +1\n[DefeatDuel] 최종 위력 -5\n[EndSkill] 이 스킬로 소모한 [BloodDinner]이 30 미만이면, 다음 턴에 [Vulnerable] 2 얻음
   źródło: Skills_Abnormality_Refraction5.json :: dataList[id=863317].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [DefeatDuel], [EndSkill], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] Consume up to 100 [BloodDinner] to activate the following effects:\n- Heal the Core and the Body Parts' HP by [BloodDinner] consumed\n- This Skill gains Final Power +1 for every 20 [BloodDinner] consumed\n[DefeatDuel] Final Power -5\n[EndSkill] If this Skill consumed less than 30 [BloodDinner], gain 2 [Vulnerable] next turn
   PL:

## [refraction5] Pasywka wroga: Passives_Abnormality_Refraction5
- plik gry: `Passives_Abnormality_Refraction5.json`

699. [[refraction5] Pasywka wroga [863001] — nazwa] 근접 전투
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863001].name
   limit: do 40 znaków
   EN: Melee Combat
   PL:
700. [[refraction5] Pasywka wroga [863001] — opis] 자신보다 속도가 느리다면, 속도차만큼 피해량 +10% (최대 30%)\n자신보다 속도가 빠르다면, 속도차만큼 피해량 -10% (최대 30%)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863001].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every Speed difference (max 30%)\nIf this unit's Speed is slower than the target's deal -10% damage for every Speed difference (max 30%)
   PL:
701. [[refraction5] Pasywka wroga [863002] — nazwa] 약진
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863002].name
   limit: do 40 znaków
   EN: Charge Forth
   PL:
702. [[refraction5] Pasywka wroga [863002] — opis] 자신의 [Breath] 5 당, 속도 최솟값, 최댓값 1 증가 (최대 4)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863002].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Raise Min & Max Speed values by 1 for every 5 [Breath] on self (max 4)
   PL:
703. [[refraction5] Pasywka wroga [863003] — nazwa] 과녁 소환
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863003].name
   limit: do 40 znaków
   EN: Summon Targets
   PL:
704. [[refraction5] Pasywka wroga [863003] — opis] 남은 체력이 전체 체력의 75% 이하일 때, 패턴 변경\n패턴 변경 시 옛 G사 부장과 짙어진 패잔병을 소환하고, 현재 체력이 가장 낮은 대상에게 징표 부여.\n- 자신의 속도 최솟값, 최댓값이 1이 됨.\n- 보호막 체력 300을 얻음.
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863003].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 75%- HP, gain a new pattern\nWhen gaining a new pattern, summon G Corp. Head Manager and Downcast Veteran; then, inflict Stigmatized on the target with the least current HP\n- Change Min & Max Speed values on self to 1.\n- Gain 300 Shield HP.
   PL:
705. [[refraction5] Pasywka wroga [863004] — nazwa] 대상 지정
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863004].name
   limit: do 40 znaków
   EN: Designate Target
   PL:
706. [[refraction5] Pasywka wroga [863004] — opis] 대상 지정 사격, 대상 조정 사격을 사용할 때, 속도가 가장 느린 대상 중 현재 체력이 가장 낮은 대상에게 [FellBulletMark] 부여
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863004].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [FellBulletMark]
   znaczenie tagów: [FellBulletMark] = 징표 / Stigmatized
   EN: When using Designated Target Fire or Target Readjustment Fire: among targets with the slowest Speed, inflict [FellBulletMark] against target with the least current HP
   PL:
707. [[refraction5] Pasywka wroga [863201] — nazwa] 산소 공급
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863201].name
   limit: do 40 znaków
   EN: Oxygen Supply
   PL:
708. [[refraction5] Pasywka wroga [863201] — opis] 지난 날의 침낭이 등장한 첫 턴 시작 시, [Breath] 위력 10, [Breath] 횟수 10을 얻음\n\n턴 종료 시 [Breath] 위력 또는 [Breath] 횟수가 10 미만이면, 본체의 최대 체력의 2%만큼 머리의 체력을 소모하여 [Breath] 5 얻고 [Breath] 횟수 5 증가 (이 효과로 파괴되거나 사망하지 않음)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863201].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At the first Turn Start of the turn Sleeping Bag of a Bygone Day appeared, it gains 10 [Breath] Potency and +10 [Breath] Count\n\nTurn End: at less than 10 [Breath] Potency or [Breath] Count, consume HP from the Head Part equal to 2% of the Core's max HP to gain 5 [Breath] and +5 [Breath] Count (cannot be Part broken or defeated due to this effect)
   PL:
709. [[refraction5] Pasywka wroga [863202] — nazwa] 깊은 들숨
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863202].name
   limit: do 40 znaków
   EN: Deep Breath
   PL:
710. [[refraction5] Pasywka wroga [863202] — opis] [Breath]으로 인하여 발동하는 크리티컬 확률이 1.5배로 증가\n\n크리티컬 발동 시,\n- [Breath] 위력이 15 이상이면, (보유한 [Breath] 위력/5)만큼 소모하여 크리티컬 피해량이 (소모한 [Breath] 위력 x 4)%만큼 증가\n- [Breath] 횟수가 15 이상이면, (보유한 [Breath] 횟수/5)만큼 소모하여 크리티컬 피해량이 (소모한 [Breath] 횟수 x 8)%만큼 증가
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863202].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Multiply Critical Chance from [Breath] effects by x 1.5\n\nOn Crit:\n- At 15+ [Breath] Potency, consume up to ([Breath] Potency on self / 5) [Breath] Potency to deal +([Breath] Potency consumed x 4)% damage on Crit\n- At 15+ [Breath] Count, consume up to ([Breath] Count on self / 5) [Breath] Count to deal +([Breath] Count consumed x 8)% damage on Crit
   PL:
711. [[refraction5] Pasywka wroga [863203] — nazwa] 산소 포화 상태
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863203].name
   limit: do 40 znaków
   EN: Oxygen-saturated
   PL:
712. [[refraction5] Pasywka wroga [863203] — opis] ‘그건… 내꺼야!’를 사용하는 턴이면 자신의 속도가 1로 고정되고 턴 시작 시, 스테이지 내 모든 대상에게 [Breath] 위력 6, [Breath] 횟수 6 부여\n\n해당 턴 종료 시에 [Breath] 위력 5, [Breath] 횟수 5를 초과한 수치만큼 전부 소모하고, 다음 턴 시작 시 그 수치만큼 머리에 [Breath] 위력과 [Breath] 횟수를 부여
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863203].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: In the turn this unit uses 'That's... Mine!', fix its Speed to 1. At Turn Start, apply 6 [Breath] Potency and +6 [Breath] Count to all units present on the Stage.\n\nAt the end of the same turn, consume any excess [Breath] Potency and [Breath] Count past 5 Potency and 5 Count; then, at the next Turn Start, apply the same amount of [Breath] Potency and [Breath] Count consumed to the Head Part
   PL:
713. [[refraction5] Pasywka wroga [863204] — nazwa] 늑골 파괴
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863204].name
   limit: do 40 znaków
   EN: Shattered Ribcage
   PL:
714. [[refraction5] Pasywka wroga [863204] — opis] 몸통 파괴 시, 다음 턴에 몸통 부위가 사라지고 사람 부위가 드러남
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863204].desc
   limit: do 130 znaków
   EN: When the Body Part is broken, remove the Body Part next turn and replace it with a Person Part
   PL:
715. [[refraction5] Pasywka wroga [863205] — nazwa] 늑골 재생
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863205].name
   limit: do 40 znaków
   EN: Ribcage Regeneration
   PL:
716. [[refraction5] Pasywka wroga [863205] — opis] 전투 종료 시, 사람이 보유한 [Breath] 위력과 [Breath] 횟수가 반감됨\n다음 턴에 사람 부위가 사라지고 몸통 부위가 회복되어 드러남
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863205].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At Combat End, halve the [Breath] Potency and [Breath] Count on the Person Part\nNext Turn, the Person Part disappears and is replaced by Body Part
   PL:
717. [[refraction5] Pasywka wroga [863206] — nazwa] 끊어지는 고통
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863206].name
   limit: do 40 znaków
   EN: Excruciating Suffering
   PL:
718. [[refraction5] Pasywka wroga [863206] — opis] 합에서 패배하여 피격받을 때마다 [Breath] 위력 1 감소\n\n일방 공격으로 피격받을 때마다 [Breath] 횟수 1 감소\n\n크리티컬, 패시브 발동 여부와 관계 없이 [Breath] 위력과 [Breath] 횟수가 항상 5 미만으로 내려가지 않음
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863206].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Every time this unit loses a Clash and takes a hit, lose 1 [Breath] Potency\n\nEvery time this unit is hit by an Unopposed Attack, lose 1 [Breath] Count\n\nThis unit's [Breath] Potency and [Breath] Count, regardless of whether an attack hit Critically or whether its Passive activated, does not drop below 5
   PL:
719. [[refraction5] Pasywka wroga [863207] — nazwa] 절규 소리
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863207].name
   limit: do 40 znaków
   EN: Anguished Screaming
   PL:
720. [[refraction5] Pasywka wroga [863207] — opis] 본체의 체력이 40% 이하가 되면 다음 턴에 ‘고통 함께하기’를 사용
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863207].desc
   limit: do 120 znaków
   EN: At 40% or less Core HP, use 'Share the Pain' next turn
   PL:
721. [[refraction5] Pasywka wroga [863208] — nazwa] 후유증
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863208].name
   limit: do 40 znaków
   EN: After Effect
   PL:
722. [[refraction5] Pasywka wroga [863208] — opis] 사람 사망 시, 다음 턴까지 몸통과 머리의 참격, 관통, 타격 내성 +0.2 (전투당 1회)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863208].desc
   limit: do 180 znaków
   EN: When the Person dies, both the Body and the Head Parts gain +0.2 Resistance to Slash, Pierce, and Blunt until next turn (once per Encounter)
   PL:
723. [[refraction5] Pasywka wroga [863301] — nazwa] 탐닉하는 꽃잎
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863301].name
   limit: do 40 znaków
   EN: Indulgent Petals
   PL:
724. [[refraction5] Pasywka wroga [863301] — opis] 턴 종료시 [BloodDinner]이 20 이상이면, 최대 50까지 소모하여 소모한 [BloodDinner]만큼 본체와 머리 부위 체력 회복\n- 머리 부위가 흐트러졌거나, 파괴된 상태면 발동하지 않음
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863301].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: Turn End: at 20+ [BloodDinner], consume up to 50 [BloodDinner] and heal the Core and the Head Parts equal to [BloodDinner] consumed\n- Does not activate if the Head Part is either Staggered or Destroyed
   PL:
725. [[refraction5] Pasywka wroga [863302] — nazwa] 한 방울의 양분
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863302].name
   limit: do 40 znaków
   EN: A Drop of Nourishment
   PL:
726. [[refraction5] Pasywka wroga [863302] — opis] 공격 종료 시 자신의 공격 스킬로 입힌 피해량의 절반만큼 본체, 부위 체력 회복\n- 머리 부위가 흐트러졌거나, 파괴된 상태면 발동하지 않음
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863302].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack End: Heal the Core and the Part equal to the amount of damage this unit's Attack Skill dealt\n- Does not activate if the Head Part is either Staggered or Destroyed
   PL:
727. [[refraction5] Pasywka wroga [863303] — nazwa] 갈망
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863303].name
   limit: do 40 znaków
   EN: Yearning
   PL:
728. [[refraction5] Pasywka wroga [863303] — opis] 턴 종료시 이번 턴에 자신이 체력을 회복했으면, 회복한 체력 10 당 다음 턴에 [AttackUp] 1, [DefenseDown] 1 얻음 (최대 10)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863303].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn End: if this unit healed HP, gain 1 [AttackUp] and 1 [DefenseDown] next turn for every 10 HP healed (max 10)
   PL:
729. [[refraction5] Pasywka wroga [863304] — nazwa] 잔혹한 혈향
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863304].name
   limit: do 40 znaków
   EN: Bloodthirsty Stench
   PL:
730. [[refraction5] Pasywka wroga [863304] — opis] 현재 [BloodDinner]이 100 이상이면 특수 스킬 사용\n턴 종료시, 자신의 [BloodDinner_Accumulation]이 500 이상이거나, 자신의 현재 체력이 최대 체력의 60% 미만이면 패턴이 변경됨
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863304].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: At 100+ [BloodDinner], use a special Skill\nTurn End: at 500+ [BloodDinner_Accumulation] by this unit, or if this unit is at less than 60% HP, gain a new pattern
   PL:
731. [[refraction5] Pasywka wroga [863305] — nazwa] 굴절된 죄악
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863305].name
   limit: do 40 znaków
   EN: Refracted Sin
   PL:
732. [[refraction5] Pasywka wroga [863305] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]의 위력이 50까지만 누적됨 (특수 화상, 출혈, 진동, 파열, 침잠 포함)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863305].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] Potency only stacks up to 50 (including the Unique variations of above Keywords)
   PL:
733. [[refraction5] Pasywka wroga [863306] — nazwa] 날카로운 가시
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863306].name
   limit: do 40 znaków
   EN: Sharp Thorn
   PL:
734. [[refraction5] Pasywka wroga [863306] — opis] 몸통 부위에 스킬로 피해를 입으면, 공격자의 [Laceration] 횟수 1 증가 (인격 당 턴 당 1회)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863306].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If this unit's Body Part takes damage from an enemy Skill, inflict +1 [Laceration] Count on the attacker (once per turn per Identity)
   PL:
735. [[refraction5] Pasywka wroga [863307] — nazwa] 끝없는 갈증
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863307].name
   limit: do 40 znaków
   EN: Endless Thirst
   PL:
736. [[refraction5] Pasywka wroga [863307] — opis] 턴 시작시 자신의 [BloodDinner_Accumulation] 100 당 [DefenseDown] 1 얻음 (최대 10)\n턴 시작시 자신의 [BloodDinner_Accumulation] 200 당 [TakeHpHealIncrease] 1 얻음 (최대 5)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863307].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner_Accumulation], [DefenseDown], [TakeHpHealIncrease]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: Turn Start: gain 1 [DefenseDown] for every 100 [BloodDinner_Accumulation] by this unit (max 10)\nTurn Start: gain 1 [TakeHpHealIncrease] for every 200 [BloodDinner_Accumulation] by this unit (max 5)
   PL:
737. [[refraction5] Pasywka wroga [863308] — nazwa] 끝없는 갈망
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863308].name
   limit: do 40 znaków
   EN: Endless Yearning
   PL:
738. [[refraction5] Pasywka wroga [863308] — opis] 3배수 턴마다 선택지 이벤트 발생.
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863308].desc
   limit: do 120 znaków
   EN: Triggers a Choice Event every 'multiple of 3' turns.
   PL:
739. [[refraction5] Pasywka wroga [863309] — nazwa] 굴절률 증가
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863309].name
   limit: do 40 znaków
   EN: Increased Refraction Rate
   PL:
740. [[refraction5] Pasywka wroga [863309] — opis] 이 캐릭터가 등장한지 9턴 경과하면, 다음 턴부터 [AttackUp]를 10턴 이상 경과한 턴 당 1씩 얻음 (최대 10)
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863309].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: If 9 turns have passed since this unit appeared on the field, starting next turn, gain 1 [AttackUp] every turn past the 10th turn (max 10)
   PL:
741. [[refraction5] Pasywka wroga [863101] — nazwa] 지정 사살
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863101].name
   limit: do 40 znaków
   EN: Designated Execution
   PL:
742. [[refraction5] Pasywka wroga [863101] — opis] 흉탄의 사수에게 사망 시 다음 턴에 흉탄의 사수에게 [Agility] 1, [Enhancement] 1, [AttackDmgUp] 2 부여
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863101].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Agility], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: When killed by Der Fluchschütze, apply 1 [Agility], 1 [Enhancement], and 2 [AttackDmgUp] next turn to Der Fluchschütze
   PL:
743. [[refraction5] Pasywka wroga [863102] — nazwa] 선수필승
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863102].name
   limit: do 40 znaków
   EN: First Strike Wins
   PL:
744. [[refraction5] Pasywka wroga [863102] — opis] 수감자에게 사망 시 자신을 처치한 속성의 E.G.O 자원 3개를 줌
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863102].desc
   limit: do 130 znaków
   EN: When killed by a Sinner, give 3 E.G.O resources in the affinity of the Skill that killed this unit
   PL:
745. [[refraction5] Pasywka wroga [863103] — nazwa] 내가 아니야
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863103].name
   limit: do 40 znaków
   EN: Not Me
   PL:
746. [[refraction5] Pasywka wroga [863103] — opis] 전투 시작 시 자신에게 징표가 없으면, 보호막 300을 얻음.
   źródło: Passives_Abnormality_Refraction5.json :: dataList[id=863103].desc
   limit: do 120 znaków
   EN: If this unit doesn't have Stigmatized at Combat Start, gain 300 Shield.
   PL:

## [refraction6] Wróg / część: Enemies_Refraction6
- plik gry: `Enemies_Refraction6.json`

747. [[refraction6] Wróg / część [9563] — nazwa] 굴절된 나생접::고치
   źródło: Enemies_Refraction6.json :: dataList[id=9563].name
   limit: do 70 znaków
   EN: Refracted Butterfly of Entangled Lives::The Pupa
   PL:
748. [[refraction6] Wróg / część [9563] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9563].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [[refraction6] Wróg / część [956301] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=956301].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [[refraction6] Wróg / część [956301] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956301].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [[refraction6] Wróg / część [9564] — nazwa] 굴절된 나생접 환영::과거
   źródło: Enemies_Refraction6.json :: dataList[id=9564].name
   limit: do 80 znaków
   EN: Refracted Illusory Butterfly of Entangled Lives::The Past
   PL:
752. [[refraction6] Wróg / część [9564] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9564].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [[refraction6] Wróg / część [956401] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=956401].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [[refraction6] Wróg / część [956401] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956401].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [[refraction6] Wróg / część [9565] — nazwa] 굴절된 나생접 환영::현재
   źródło: Enemies_Refraction6.json :: dataList[id=9565].name
   limit: do 80 znaków
   EN: Refracted Illusory Butterfly of Entangled Lives::The Present
   PL:
756. [[refraction6] Wróg / część [9565] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9565].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [[refraction6] Wróg / część [956501] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=956501].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [[refraction6] Wróg / część [956501] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956501].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [[refraction6] Wróg / część [9566] — nazwa] 굴절된 나생접 환영::미래
   źródło: Enemies_Refraction6.json :: dataList[id=9566].name
   limit: do 80 znaków
   EN: Refracted Illusory Butterfly of Entangled Lives::The Future
   PL:
760. [[refraction6] Wróg / część [9566] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9566].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [[refraction6] Wróg / część [956601] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=956601].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [[refraction6] Wróg / część [956601] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956601].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [[refraction6] Wróg / część [9567] — nazwa] 굴절된 나생접::나비
   źródło: Enemies_Refraction6.json :: dataList[id=9567].name
   limit: do 70 znaków
   EN: Refracted Butterfly of Entangled Lives::Imago
   PL:
764. [[refraction6] Wróg / część [9567] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9567].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [[refraction6] Wróg / część [956701] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=956701].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [[refraction6] Wróg / część [956701] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956701].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [[refraction6] Wróg / część [9556] — nazwa] 굴절된 놀아줄래
   źródło: Enemies_Refraction6.json :: dataList[id=9556].name
   limit: do 40 znaków
   EN: Refracted Will You Play?
   PL:
768. [[refraction6] Wróg / część [9556] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9556].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [[refraction6] Wróg / część [955601] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=955601].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [[refraction6] Wróg / część [955601] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=955601].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [[refraction6] Wróg / część [955602] — nazwa] 인형
   źródło: Enemies_Refraction6.json :: dataList[id=955602].name
   limit: do 40 znaków
   EN: Stuffed Toy
   PL:
772. [[refraction6] Wróg / część [955602] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=955602].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [[refraction6] Wróg / część [9568] — nazwa] 굴절된 응룡
   źródło: Enemies_Refraction6.json :: dataList[id=9568].name
   limit: do 40 znaków
   EN: Refracted Yinglong
   PL:
774. [[refraction6] Wróg / część [9568] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9568].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [[refraction6] Wróg / część [956801] — nazwa] 역린
   źródło: Enemies_Refraction6.json :: dataList[id=956801].name
   limit: do 40 znaków
   EN: Inverted Scale
   PL:
776. [[refraction6] Wróg / część [956801] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956801].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [[refraction6] Wróg / część [956802] — nazwa] 머리
   źródło: Enemies_Refraction6.json :: dataList[id=956802].name
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [[refraction6] Wróg / część [956802] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956802].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [[refraction6] Wróg / część [9569] — nazwa] 굴절된 응룡
   źródło: Enemies_Refraction6.json :: dataList[id=9569].name
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [[refraction6] Wróg / część [9569] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9569].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [[refraction6] Wróg / część [956901] — nazwa] 매화첨
   źródło: Enemies_Refraction6.json :: dataList[id=956901].name
   limit: do 40 znaków
   EN: Flower-burying Wedge
   PL:
782. [[refraction6] Wróg / część [956901] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956901].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [[refraction6] Wróg / część [956902] — nazwa] 역린
   źródło: Enemies_Refraction6.json :: dataList[id=956902].name
   (powtórzenie elementu 775 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [[refraction6] Wróg / część [956902] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956902].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [[refraction6] Wróg / część [956903] — nazwa] 머리
   źródło: Enemies_Refraction6.json :: dataList[id=956903].name
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [[refraction6] Wróg / część [956903] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956903].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [[refraction6] Wróg / część [956904] — nazwa] 몸통
   źródło: Enemies_Refraction6.json :: dataList[id=956904].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [[refraction6] Wróg / część [956904] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=956904].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [[refraction6] Wróg / część [9570] — nazwa] 굴절된 홍옥[紅玉]
   źródło: Enemies_Refraction6.json :: dataList[id=9570].name
   limit: do 60 znaków
   EN: Refracted Hongyu, the Crimson Jade [紅玉]
   PL:
790. [[refraction6] Wróg / część [9570] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9570].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [[refraction6] Wróg / część [957001] — nazwa] 홍옥[紅玉]
   źródło: Enemies_Refraction6.json :: dataList[id=957001].name
   limit: do 40 znaków
   EN: Hongyu, the Crimson Jade
   PL:
792. [[refraction6] Wróg / część [957001] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=957001].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
