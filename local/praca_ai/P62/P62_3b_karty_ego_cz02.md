# Paczka AI P62 (Fala 3 · 3B) — Karty E.G.O, umiejętności i pasywki (część 2/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P62_3b_karty_ego_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P62_3b_karty_ego_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## E.G.O [20309] In the Name of Love and Hate (사랑과 증오의 이름으로) — Don Quixote
- postać: Don Quixote (돈키호테) · ID E.G.O: `20309`

1. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신을 제외한 무작위 아군 1 + (질투 공명 수 / 3)명에게 [MagicalGirlResponse] 1 부여 (최대 3명)\n<style="highlight">- 자신에게 [MagicalGirlAppear]이 있으면, 대신하여 무작위 아군 1 + (질투 공명 수 / 3)에게 [MagicalGirlResponse] 2 부여 (최대 3명)</style>\n\n[BeforeAttack] ([Charge] - 1)만큼 공격 가중치 증가 (최대 <style="highlight">5</style>)\n[EndSkill]  자신의 [Charge] 횟수를 전부 소모하여 체력 비율이 가장 낮은 아군 2 + (질투 공명 수 / 2)명의 체력을 (소모한 [Charge] 횟수)%만큼 회복  (최대 5명, 최대 <style="highlight">8</style>%)\n\n[EndSkill] 로보토미 E.G.O::사랑과 증오의 이름으로 돈키호테이면, [ArcanaQueenOfHate] 1 얻음
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=3].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [MagicalGirlResponse], [MagicalGirlAppear], [Charge], [EndSkill], [ArcanaQueenOfHate]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [MagicalGirlResponse] = 마법소녀의 영창 / Magical Girl's Chant; [MagicalGirlAppear] = 마법소녀 등장! / Here Comes Magical Girl!; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana
   EN: [BeforeAttack] Apply 1 [MagicalGirlResponse] to (1 + (Envy Reson. / 3)) random other allies (max 3 allies)\n<style="highlight">- If this unit has [MagicalGirlAppear], apply 2 [MagicalGirlResponse] to (1 + (Envy Reson. / 3)) random other allies instead (max 3 allies)</style>\n\n[BeforeAttack] Gain +([Charge] - 1) Atk Weight (max <style="highlight">5</style>)\n[EndSkill] Consume all [Charge] Count on self to heal (2 + (Envy Reson. / 2)) allies with the least HP percentages by ([Charge] Count consumed)% HP (max 5 allies, max <style="highlight">8</style>%)\n\n[EndSkill] If this unit is Lobotomy E.G.O::In the Name of Love and Hate Don Quixote, gain 1 [ArcanaQueenOfHate]
   PL:
2. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst]을 ([Charge] - 1)만큼 부여 (최대 <style="highlight">3</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [Burst] (max <style="highlight">3</style>)
   PL:
3. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신을 제외한 무작위 아군 1 + (질투 공명 수 / <style="highlight">2</style>)명에게 [MagicalGirlResponse] 1 부여 (최대 <style="highlight">4</style>명)\n- 자신에게 [MagicalGirlAppear]이 있으면, 대신하여 무작위 아군 1 + (질투 공명 수 /<style="highlight"> 2</style>)에게 [MagicalGirlResponse] 2 부여 (최대 <style="highlight">4</style>명)\n\n[BeforeAttack] ([Charge] - 1)만큼 공격 가중치 증가 (최대 5)\n<style="highlight">- 자신에게 [MagicalGirlAppear]이 있으면, 대신하여 [Charge]만큼 공격 가중치 증가 (최대 5)</style>\n\n[EndSkill]  자신의 [Charge] 횟수를 전부 소모하여 체력 비율이 가장 낮은 아군 2 + (질투 공명 수 / 2)명의 체력을 (소모한 [Charge] 횟수)%만큼 회복  (최대 5명, 최대 <style="highlight">10</style>%)\n\n[EndSkill] 로보토미 E.G.O::사랑과 증오의 이름으로 돈키호테이면, [ArcanaQueenOfHate] 1 얻음
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=4].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [MagicalGirlResponse], [MagicalGirlAppear], [Charge], [EndSkill], [ArcanaQueenOfHate]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [MagicalGirlResponse] = 마법소녀의 영창 / Magical Girl's Chant; [MagicalGirlAppear] = 마법소녀 등장! / Here Comes Magical Girl!; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana
   EN: [BeforeAttack] Apply 1 [MagicalGirlResponse] to (1 + (Envy Reson. / <style="highlight">2</style>)) random other allies (max <style="highlight">4</style> allies)\n- If this unit has [MagicalGirlAppear], apply 2 [MagicalGirlResponse] to (1 + (Envy Reson. / <style="highlight">2</style>)) random other allies instead (max <style="highlight">4</style> allies)\n\n[BeforeAttack] Gain +([Charge] - 1) Atk Weight (max 5)\n<style="highlight">- If this unit has [MagicalGirlAppear], gain +([Charge]) Atk Weight instead (max 5)</style>\n\n[EndSkill] Consume all [Charge] Count on self to heal (2 + (Envy Reson. / 2)) allies with the least HP percentages by ([Charge] Count consumed)% HP (max 5 allies, max <style="highlight">10</style>%)\n\n[EndSkill] If this unit is Lobotomy E.G.O::In the Name of Love and Hate Don Quixote, gain 1 [ArcanaQueenOfHate]
   PL:
4. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">2</style> 증가 (턴 당 최대 <style="highlight">10</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">2</style> [Charge] Count (<style="highlight">10</style> per turn)
   PL:
5. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VillainMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: [OnSucceedAttack] Inflict [VillainMark] against the main target next turn
   PL:
6. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst]을 ([Charge] - 1)만큼 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [Burst] (max <style="highlight">4</style>)
   PL:
7. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 4 — opis] <style="highlight">- 자신에게 [MagicalGirlAppear]이 있으면, [Burst] 횟수 1 증가</style>
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030911].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [MagicalGirlAppear], [Burst]
   znaczenie tagów: [MagicalGirlAppear] = 마법소녀 등장! / Here Comes Magical Girl!; [Burst] = 파열 / Rupture
   EN: <style="highlight">- If this unit has [MagicalGirlAppear], inflict +1 [Burst] Count</style>
   PL:
8. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 맥시마이즈드 리버스드 아르카나 슬레이브 -  이레이징 오브 헤이트리드
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].name ; dataList[id=2030921].levelList[level=3].name ; dataList[id=2030921].levelList[level=4].name
   limit: do 70 znaków
   EN: Maximized Reversed Arcana Slave - Erasure of Hatred
   PL:
9. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 증오의 여왕
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].abName ; dataList[id=2030921].levelList[level=3].abName ; dataList[id=2030921].levelList[level=4].abName
   limit: do 40 znaków
   EN: The Queen of Hatred
   PL:
10. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] [Charge]만큼 공격 가중치 증가 (최대 5)\n\n[BeforeAttack] 자신의 [Charge] 횟수를 전부 소모하여 소모한 [Charge] 횟수당 피해량 +1% (최대 20%)\n\n[BeforeAttack] 메인 타겟에게 [VillainMark]이 있으면, [Charge]당 피해량 +3% (최대 15%)\n\n[BeforeAttack] 질투 공명 수 3당, 피해량 +5% (최대 10%, 소수점 버림)\n\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -12 (최대 -24)\n\n[EndSkill] 로보토미 E.G.O::사랑과 증오의 이름으로 돈키호테이면, [HystericGauge] 1 얻음
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge], [VillainMark], [EndSkill], [HystericGauge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [VillainMark] = 악당 표식 / Mark of Villainy; [EndSkill] = [공격 종료시] / [Attack End]; [HystericGauge] = 히스테리 / Hysteria
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain +([Charge]) Atk Weight (max 5)\n\n[BeforeAttack] Consume all [Charge] Count and deal +1% more damage for every [Charge] Count consumed (max 20%)\n\n[BeforeAttack] If the main target has [VillainMark], deal +3% damage for every [Charge] (max 15%)\n\n[BeforeAttack] Deal +5% damage for every 3 Envy Reson. (max 10%, rounded down)\n\n[BeforeAttack] Base Power -12 for every Cracked Coin (max -24)\n\n[EndSkill] If this unit is a Lobotomy E.G.O::In the Name of Love and Hate Don Quixote, gain 1 [HystericGauge]
   PL:
11. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2030921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2030921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
12. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가 (턴 당 최대 7)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count (7 times per turn)
   PL:
13. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2030921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2030921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2030921].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [VillainMark]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: [OnSucceedAttackTail] Inflict [VillainMark] against the main target next turn
   PL:
15. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking]을 ([Charge] - 1)만큼 부여 (최대 2)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [Sinking] (max 2)
   PL:
16. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] [Charge]만큼 공격 가중치 증가 (최대 5)\n<style="highlight">- 자신에게 [NoVillain]가 있으면, 대신하여 ([Charge] + 1)만큼 공격 가중치 증가 (최대 5)</style>\n\n[BeforeAttack] 자신의 [Charge] 횟수를 전부 소모하여 소모한 [Charge] 횟수당 피해량 +<style="highlight">2</style>% (최대 <style="highlight">40</style>%)\n\n[BeforeAttack] 메인 타겟에게 [VillainMark]이 있으면, [Charge]당 피해량 +<style="highlight">5</style>% (최대 <style="highlight">25</style>%)\n<style="highlight">-  자신에게 [HystericGauge]가 있으면, 대신하여 [Charge]당 피해량 +7% (최대 35%)</style>\n\n[BeforeAttack] 질투 공명 수 2당, 피해량 +<style="highlight">7</style>% (최대 <style="highlight">21</style>%, 소수점 버림)\n\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -12 (최대 -24)\n\n[EndSkill] 로보토미 E.G.O::사랑과 증오의 이름으로 돈키호테이면, [HystericGauge] 1 얻음
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=3].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge], [NoVillain], [VillainMark], [HystericGauge], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [NoVillain] = 역변-리버스드 / Regressive Transformation - Reversed; [VillainMark] = 악당 표식 / Mark of Villainy; [HystericGauge] = 히스테리 / Hysteria; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain +([Charge]) Atk Weight (max 5)\n<style="highlight">- If this unit has [NoVillain], gain +([Charge] + 1) Atk Weight instead (max 5)</style>\n\n[BeforeAttack] Consume all [Charge] Count and deal +<style="highlight">2</style>% more damage for every [Charge] Count consumed (max <style="highlight">40</style>%)\n\n[BeforeAttack] If the main target has [VillainMark], deal +<style="highlight">5</style>% damage for every [Charge] (max <style="highlight">25</style>%)\n<style="highlight">- If this unit has [HystericGauge], deal +7% damage for every [Charge] instead (max 35%)</style>\n\n[BeforeAttack] Deal +<style="highlight">7</style>% damage for every 2 Envy Reson. (max <style="highlight">21</style>%, rounded down)\n\n[BeforeAttack] Base Power -12 for every Cracked Coin (max -24)\n\n[EndSkill] If this unit is a Lobotomy E.G.O::In the Name of Love and Hate Don Quixote, gain 1 [HystericGauge]
   PL:
17. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가 (턴 당 최대 <style="highlight">10</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count (<style="highlight">10</style> per turn)
   PL:
18. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking]을 ([Charge] - 1)만큼 부여 (최대 <style="highlight">3</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [Sinking] (max <style="highlight">3</style>)
   PL:
19. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] [Charge]만큼 공격 가중치 증가 (최대 5)\n- 자신에게 [NoVillain]가 있으면, 대신하여 ([Charge] + 1)만큼 공격 가중치 증가 (최대 5)\n\n[BeforeAttack] 자신의 [Charge] 횟수를 전부 소모하여 소모한 [Charge] 횟수당 피해량 <style="highlight">+2.5</style>% (최대 <style="highlight">50</style>%)\n\n[BeforeAttack] 메인 타겟에게 [VillainMark]이 있으면, [Charge]당 피해량 +5% (최대 25%)\n-  자신에게 [HystericGauge]가 있으면, 대신하여 [Charge]당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">50</style>%)\n\n[BeforeAttack] 질투 공명 수 2당, 피해량 <style="highlight">+10%</style> (최대 <style="highlight">30%</style>, 소수점 버림)\n\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -12 (최대 -24)\n\n[EndSkill] 로보토미 E.G.O::사랑과 증오의 이름으로 돈키호테이면, [HystericGauge] 1 얻음
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=4].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge], [NoVillain], [VillainMark], [HystericGauge], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [NoVillain] = 역변-리버스드 / Regressive Transformation - Reversed; [VillainMark] = 악당 표식 / Mark of Villainy; [HystericGauge] = 히스테리 / Hysteria; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain +([Charge]) Atk Weight (max 5)\n- If this unit has [NoVillain], gain +([Charge] + 1) Atk Weight instead (max 5)\n\n[BeforeAttack] Consume all [Charge] Count and deal <style="highlight">+2.5%</style> more damage for every [Charge] Count consumed (max <style="highlight">50</style>%)\n\n[BeforeAttack] If the main target has [VillainMark], deal +5% damage for every [Charge] (max 25%)\n- If this unit has [HystericGauge], deal +<style="highlight">10</style>% damage for every [Charge] instead (max <style="highlight">50</style>%)\n\n[BeforeAttack] Deal+<style="highlight">10</style>% damage for every 2 Envy Reson. (max <style="highlight">30</style>%, rounded down)\n\n[BeforeAttack] Base Power -12 for every Cracked Coin (max -24)\n\n[EndSkill] If this unit is a Lobotomy E.G.O::In the Name of Love and Hate Don Quixote, gain 1 [HystericGauge]
   PL:
20. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가 (턴 당 최대 <style="highlight">14</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count (<style="highlight">14</style> per turn)
   PL:
21. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]</style> 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VillainMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict [VillainMark] against the main target next turn
   PL:
22. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking]을 ([Charge] - 1)만큼 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [Sinking] (max <style="highlight">4</style>)
   PL:
23. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 4 — opis] <style="highlight">- 자신에게 [NoVillain]가 있으면, [Sinking] 횟수 1 증가</style>
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2030921].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [NoVillain], [Sinking]
   znaczenie tagów: [NoVillain] = 역변-리버스드 / Regressive Transformation - Reversed; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">- If this unit has [NoVillain], inflict +1 [Sinking] Count</style>
   PL:
24. [Pasywka E.G.O — nazwa] 아르카나 적성 회로
   źródło: Passive_Ego.json :: dataList[id=2030911].name
   limit: do 40 znaków
   EN: Arcana Aptitude Circuit
   PL:
25. [Pasywka E.G.O — opis] 전투 중 누적으로 [Charge] 횟수를 10 소모할 때마다, [Charge] 1 얻음\n- 이미 자신의 [Charge] 횟수를 소모하여 [Charge]을 얻고 있다면, 중복되지 않음\n- 자신의 [Charge]당 자신의 [Charge] 횟수를 소모하는 기본 공격 스킬의 피해량 +5% (최대 25%)\n\n로보토미 E.G.O::사랑과 증오의 이름으로 돈키호테이면, 스킬 3이 1개 추가됨
   źródło: Passive_Ego.json :: dataList[id=2030911].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count\n- If this unit already gains [Charge] by consuming [Charge] Count on self, this effect does not stack with that effect\n- This unit's Base Attack Skills that consume [Charge] Count: deal +5% damage for every [Charge] on self (max 25%)\n\nIf this unit is Lobotomy E.G.O::In the Name of Love and Hate Don Quixote, gain 1 additional Skill 3 use
   PL:

## E.G.O [20310] I'll Go fer Scissors. How 'Bout You? (난 가위를 낼게, 너는?) — Don Quixote
- postać: Don Quixote (돈키호테) · ID E.G.O: `20310`

26. [Karta E.G.O — nazwa] 난 가위를 낼게, 너는?
   źródło: Egos.json :: dataList[id=20310].name
   limit: do 50 znaków
   EN: I'll Go fer Scissors. How 'Bout You?
   PL:
27. [Karta E.G.O — opis] 돈키호테의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20310].desc
   limit: do 120 znaków
   EN: Don Quixote’s E.G.O Gear
   PL:
28. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 난 가위를 낼게, 너는?
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=1].name ; dataList[id=2031011].levelList[level=3].name ; dataList[id=2031011].levelList[level=4].name
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 놀아줄래
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=1].abName ; dataList[id=2031011].levelList[level=3].abName ; dataList[id=2031011].levelList[level=4].abName
   limit: do 40 znaków
   EN: Will You Play?
   PL:
30. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [WinDuelEndSkill] 현재 체력 비율이 가장 낮은 아군 (2 + 질투 공명 수 / 2)명의 체력을 각자의 최대 체력 2%만큼 회복하고 정신력 5 회복 (최대 3명)\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 20)\n[DefeatDuel] 메인 타겟에게 가하는 피해량 +100%
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuelEndSkill], [DefeatDuel]
   znaczenie tagów: [WinDuelEndSkill] = [합 승리 후 공격 종료 시] / [Attack End After Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WinDuelEndSkill] Heal 2% HP and 5 SP each for (2 + Envy Reson. / 2) allies that have the lowest current HP percentages (max 3 units)\n[DefeatDuel] Gain (Envy Reson. x 5) Shield (max 20)\n[DefeatDuel] Deal +100% damage to the main target
   PL:
31. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2031011].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2031011].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [WinDuelAttack] 다음 턴에 [ResultReduction] 1 부여 (대상별 턴당 1회)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2031011].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2031011].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [ResultReduction]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [ResultReduction] = 위력 감소 / Power Down
   EN: [WinDuelAttack] Inflict 1 [ResultReduction] next turn (once per turn per target)
   PL:
33. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2031011].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2031011].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
34. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [WinDuelEndSkill] 현재 체력 비율이 가장 낮은 아군 (2 + 질투 공명 수 / 2)명의 체력을 각자의 최대 체력 <style="highlight">4</style>%만큼 회복하고 정신력 5 회복 (최대 <style="highlight">4</style>명)\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 <style="highlight">25</style>)\n[DefeatDuel] 메인 타겟에게 가하는 피해량 +<style="highlight">150</style>%
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuelEndSkill], [DefeatDuel]
   znaczenie tagów: [WinDuelEndSkill] = [합 승리 후 공격 종료 시] / [Attack End After Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WinDuelEndSkill] Heal <style="highlight">4</style>% HP and 5 SP each for (2 + Envy Reson. / 2) allies that have the lowest current HP percentages (max <style="highlight">4</style> units)\n[DefeatDuel] Gain (Envy Reson. x 5) Shield (max <style="highlight">25</style>)\n[DefeatDuel] Deal +<style="highlight">150</style>% damage to the main target
   PL:
35. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [WinDuelEndSkill] 현재 체력 비율이 가장 낮은 아군 (2 + 질투 공명 수 / 2)명의 체력을 각자의 최대 체력 <style="highlight">6</style>%만큼 회복하고 정신력 5 회복 (최대 4명)\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 <style="highlight">30</style>)\n[DefeatDuel] 메인 타겟에게 가하는 피해량 +<style="highlight">200</style>%
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031011].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuelEndSkill], [DefeatDuel]
   znaczenie tagów: [WinDuelEndSkill] = [합 승리 후 공격 종료 시] / [Attack End After Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WinDuelEndSkill] Heal <style="highlight">6</style>% HP and 5 SP each for (2 + Envy Reson. / 2) allies that have the lowest current HP percentages (max 4 units)\n[DefeatDuel] Gain (Envy Reson. x 5) Shield (max <style="highlight">30</style>)\n[DefeatDuel] Deal +<style="highlight">200</style>% damage to the main target
   PL:
36. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 난 가위를 낼게, 너는?
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].name ; dataList[id=2031021].levelList[level=3].name ; dataList[id=2031021].levelList[level=4].name
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 놀아줄래
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].abName ; dataList[id=2031021].levelList[level=3].abName ; dataList[id=2031021].levelList[level=4].abName
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n질투 공명 수가 2 이상이면, 최종 위력 +1\n[WinDuel] 메인 타겟에게 가하는 피해량 +60%\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 20)\n[DefeatDuel] 이 스킬의 [ResultReduction] 부여량 +1
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WinDuel], [DefeatDuel], [ResultReduction]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down
   EN: [CantIdentify]\nTargets randomly\nAt 2+ Envy Reson., Final Power +1\n[WinDuel] Deal +60% damage to the main target\n[DefeatDuel] Gain Shield equal to (Envy Reson. x 5) (max 20)\n[DefeatDuel] This Skill inflicts +1 more [ResultReduction]
   PL:
39. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2031021].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2031021].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2031021].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2031021].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2031021].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2031021].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여 (대상별 턴당 1회)
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2031021].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2031021].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Inflict 1 [ResultReduction] next turn (once per turn per target)
   PL:
43. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=2031021].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2031021].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
44. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n질투 공명 수 2<style="highlight">당</style>, 최종 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] 메인 타겟에게 가하는 피해량 +<style="highlight">80</style>%\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 <style="highlight">25</style>)\n[DefeatDuel] 이 스킬의 [ResultReduction] 부여량 +1
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=3].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WinDuel], [DefeatDuel], [ResultReduction]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down
   EN: [CantIdentify]\nTargets randomly\nFinal Power +1 <style="highlight">for every 2 Envy Reson. (max 2)</style>\n[WinDuel] Deal +<style="highlight">80</style>% damage to the main target\n[DefeatDuel] Gain Shield equal to (Envy Reson. x 5) (max <style="highlight">25</style>)\n[DefeatDuel] This Skill inflicts +1 more [ResultReduction]
   PL:
45. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n질투 공명 수 2당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WinDuel] 메인 타겟에게 가하는 피해량 +<style="highlight">100</style>%\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 <style="highlight">30</style>)\n[DefeatDuel] 이 스킬의 [ResultReduction] 부여량 +1
   źródło: Skills_Ego_Personality-03.json :: dataList[id=2031021].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WinDuel], [DefeatDuel], [ResultReduction]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down
   EN: [CantIdentify]\nTargets randomly\nFinal Power +1 for every 2 Envy Reson. (max <style="highlight">3</style>)\n[WinDuel] Deal +<style="highlight">100</style>% damage to the main target\n[DefeatDuel] Gain Shield equal to (Envy Reson. x 5) (max <style="highlight">30</style>)\n[DefeatDuel] This Skill inflicts +1 more [ResultReduction]
   PL:
46. [Pasywka E.G.O — nazwa] 이번엔 그대가 바늘을 삼킬 차례라네..!
   źródło: Passive_Ego.json :: dataList[id=2031011].name
   limit: do 50 znaków
   EN: 'Tis Thy Turn to Swallow the Needle!
   PL:
47. [Pasywka E.G.O — opis] 질투 속성인 스킬의 피해량 +10%\n- 질투 공명 수 1당, 추가로 해당 스킬의 피해량 +1% (최대 7%)\n\n턴 시작 시 (이번 전투 동안 누적된 자신의 체력 피해(보호막 피해 포함) / 20)만큼 [AttackUp] 얻음 (최대 3)\n\n전투 시작 시 질투 완전 공명을 했으면, 모든 적에게 [NiddleEGO] 1 부여 (집중 전투일 경우, 부위로 판정)
   źródło: Passive_Ego.json :: dataList[id=2031011].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [NiddleEGO]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [NiddleEGO] = 바늘 / Needle
   EN: Envy Skills deal +10% damage\n- Said Skills deal +1% more damage for every 1 Envy Reson. (max 7%)\n\nTurn Start: Gain [AttackUp] equal to (cumulative HP damage taken by this unit in this Encounter (including Shield damage) / 20) (max 3)\n\nCombat Start: On Envy A-Reson., inflict 1 [NiddleEGO] to all enemies (in Focused Encounters, all Parts)
   PL:

## E.G.O [20401] Forest for the Flames (삼라염상) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20401`

48. [Karta E.G.O — nazwa] 삼라염상
   źródło: Egos.json :: dataList[id=20401].name
   limit: do 40 znaków
   EN: Forest for the Flames
   PL:
49. [Karta E.G.O — opis] 료슈의 기본 EGO 장비
   źródło: Egos.json :: dataList[id=20401].desc
   limit: do 120 znaków
   EN: Ryōshū’s Base E.G.O
   PL:
50. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 삼라염상
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=1].name ; dataList[id=2040111].levelList[level=3].name ; dataList[id=2040111].levelList[level=4].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 료슈
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=1].abName ; dataList[id=2040111].levelList[level=3].abName ; dataList[id=2040111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Ryōshū
   PL:
52. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 4 [Combustion]
   PL:
53. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 6 부여
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL:
54. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackHead] Inflict 1 [Vulnerable] next turn
   PL:
55. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
56. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2040111].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Pasywka E.G.O — nazwa] 예술
   źródło: Passive_Ego.json :: dataList[id=2040111].name
   limit: do 40 znaków
   EN: Art
   PL:
58. [Pasywka E.G.O — opis] 이전 턴에 자신이 처치한 적의 수당 5%만큼 가하는 피해 증가, 받는 피해 증가
   źródło: Passive_Ego.json :: dataList[id=2040111].desc
   limit: do 120 znaków
   EN: Deal and take +5% damage for every enemy this unit defeated last turn
   PL:

## E.G.O [20402] 4th Match Flame (4번째 성냥불) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20402`

59. [Karta E.G.O — nazwa] 4번째 성냥불
   źródło: Egos.json :: dataList[id=20402].name
   limit: do 40 znaków
   EN: 4th Match Flame
   PL:
60. [Karta E.G.O — opis] 료슈 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20402].desc
   limit: do 120 znaków
   EN: Ryōshū’s E.G.O Gear
   PL:
61. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4,5) — nazwa] 4번째 성냥불
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=1].name ; dataList[id=2040211].levelList[level=3].name ; dataList[id=2040211].levelList[level=4].name ; dataList[id=2040211].levelList[level=5].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4,5) — źródło (Anomalia)] 불타버린 소녀
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=1].abName ; dataList[id=2040211].levelList[level=3].abName ; dataList[id=2040211].levelList[level=4].abName ; dataList[id=2040211].levelList[level=5].abName
   limit: do 40 znaków
   EN: Scorched Girl
   PL:
63. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상에게 [Combustion]이 있으면 스킬 위력 +2.\n[EnemyKill] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [EnemyKill], [Enhancement]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Skill Power +2 against units that have [Combustion]\n[EnemyKill] Gain 1 [Enhancement] next turn
   PL:
64. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040211].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040211].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
65. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 대상에게 [Combustion]이 있으면 스킬 위력 +2.\n[EnemyKill] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [EnemyKill], [Enhancement]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Skill Power +2 against units that have [Combustion]\n[EnemyKill] Gain 2 [Enhancement] next turn
   PL:
66. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상에게 [Combustion]이 있으면 스킬 위력 +2.\n대상의 화상 위력 1당 5%만큼 피해량이 증가 (최대 100%)\n[EnemyKill] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [EnemyKill], [Enhancement]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Skill Power +2 against units that have [Combustion]\nDeal +5% damage per 1 [Combustion] on target (Max 100%)\n[EnemyKill] Gain +2 [Enhancement] next turn
   PL:
67. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — opis] 대상에게 [Combustion]이 있으면 스킬 위력 +2.\n<style="highlight">[BeforeAttack] 모든 공격 대상의 [Combustion]의 합</style> 1당<style="highlight">,</style> 피해량 +5% (최대 100%)\n[EnemyKill] 다음 턴에 [Enhancement] 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=5].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [BeforeAttack], [EnemyKill], [Enhancement]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Skill Power +2 against units that have [Combustion]\n<style="highlight">[BeforeAttack]</style> Deal +5% damage for every <style="highlight">1 total sum of [Combustion] on all targets</style> (max 100%)\n[EnemyKill] Gain 2 [Enhancement] next turn
   PL:
68. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <style="highlight">이 코인 최종 피해량의 (대상의 [Combustion] 위력 x 2)%만큼 분노 피해 (최대 20%)</style>
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Deal (([Combustion] on target x 2)% of this Coin's final damage) Wrath damage (max 20%)</style>
   PL:
69. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여<style="highlight"></style>
   źródło: Skills_Ego.json :: dataList[id=2040211].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]<style="highlight"></style>
   PL:
70. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4,5) — nazwa] 4번째 성냥불
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=1].name ; dataList[id=2040221].levelList[level=3].name ; dataList[id=2040221].levelList[level=4].name ; dataList[id=2040221].levelList[level=5].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4,5) — źródło (Anomalia)] 불타버린 소녀
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=1].abName ; dataList[id=2040221].levelList[level=3].abName ; dataList[id=2040221].levelList[level=4].abName ; dataList[id=2040221].levelList[level=5].abName
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Combustion]이 있으면 스킬 위력 +2.\n[EnemyKill] 다음 턴에 공격 위력 증가 2 얻음.\n[EnemyKillFail] 다음 턴에 화상 10을 얻음
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Combustion], [EnemyKill], [EnemyKillFail], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [EnemyKill] = [적 처치 시] / [On Kill]; [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\nSkill Power +2 against units that have [Combustion]\n[EnemyKill] Gain 2 [Enhancement] next turn\n[EnemyKillFail] Gain 10 [Combustion] next turn
   PL:
73. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040221].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040221].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Combustion]이 있으면 스킬 위력 +4.\n[EnemyKill] 다음 턴에 공격 위력 증가 3 얻음.\n[EnemyKillFail] 다음 턴에 공격 위력 증가 3, 화상 10 얻음
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Combustion], [EnemyKill], [EnemyKillFail], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [EnemyKill] = [적 처치 시] / [On Kill]; [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\nSkill Power +4 against units that have [Combustion]\n[EnemyKill] Gain 3 [Enhancement] next turn\n[EnemyKillFail] Gain 3 [Enhancement] and 10 [Combustion] next turn
   PL:
75. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Combustion]이 있으면 스킬 위력 +4.\n대상의 화상 위력 1당 5%만큼 피해량이 증가 (최대 100%)\n[EnemyKill] 다음 턴에 공격 위력 증가 3 얻음.\n[EnemyKillFail] 다음 턴에 공격 위력 증가 3, 화상 10 얻음
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Combustion], [EnemyKill], [EnemyKillFail], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [EnemyKill] = [적 처치 시] / [On Kill]; [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\nSkill Power +4 against units that have [Combustion]\nDeal +5% damage per 1 [Combustion] on target (Max 100%)\n[EnemyKill] Gain 3 [Enhancement] next turn\n[EnemyKillFail] Gain 3 [Enhancement] and 10 [Combustion] next turn
   PL:
76. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Combustion]이 있으면 스킬 위력 +4.\n<style="highlight">[BeforeAttack] 모든 공격 대상의 [Combustion]의 합</style> 1당<style="highlight">,</style> 피해량 +5% (최대 100%)\n<style="highlight">[DefeatDuel] 기본 위력 -16</style>\n[EnemyKill] 다음 턴에 [Enhancement] 3 얻음\n[EnemyKillFail] 다음 턴에 [Enhancement] 3, [Combustion] 10 얻음
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=5].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Combustion], [BeforeAttack], [DefeatDuel], [EnemyKill], [Enhancement], [EnemyKillFail]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]
   EN: [CantIdentify]\nTargets randomly\nSkill Power +4 against units that have [Combustion]\n<style="highlight">[BeforeAttack]</style> Deal +5% damage for every <style="highlight">1 total sum of [Combustion] on all targets</style> (max 100%)\n<style="highlight">[DefeatDuel] Base Power -16</style>\n[EnemyKill] Gain 3 [Enhancement] next turn\n[EnemyKillFail] Gain 3 [Enhancement] and 10 [Combustion] next turn
   PL:
77. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[SuperCoin]</style>
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: <style="highlight">[SuperCoin]</style>
   PL:
78. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <style="highlight">이 코인 최종 피해량의 (대상의 [Combustion] 위력 x 3)%만큼 분노 피해 (최대 30%)</style>
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Deal (([Combustion] on target x 3)% of this Coin's final damage) Wrath damage (max 30%)</style>
   PL:
79. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 4 부여<style="highlight"></style>
   źródło: Skills_Ego.json :: dataList[id=2040221].levelList[level=5].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Pasywka E.G.O — nazwa] 4번째 성냥불
   źródło: Passive_Ego.json :: dataList[id=2040211].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Pasywka E.G.O — opis] 4번째로 사용하는 스킬의 최종 위력 +4, 적중 시마다 화상 4 부여
   źródło: Passive_Ego.json :: dataList[id=2040211].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Every 4th Skill this unit uses gains Final Power +4 and inflicts 4 [Combustion] On Hit
   PL:
82. [Pasywka E.G.O — nazwa] 4번째 성냥불
   źródło: Passive_Ego.json :: dataList[id=2040212].name
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Pasywka E.G.O — opis] 4번째로 사용하는 스킬의 최종 위력 +4, 적중 시마다 [Combustion] 4 부여\n- 해당 스킬이 분노 속성이면, 추가로 피해량 +(모든 공격 대상의 화상 위력 / 2)% (최대 20%)\n- 해당 스킬이 E.G.O 스킬이면, 첫번째 코인 시작 시\n· 더하기 코인이면, 정신력 10 회복\n· 빼기 코인이면, 정신력 15 감소 (이 효과로 정신력이 -40 미만이 되지 않음)
   źródło: Passive_Ego.json :: dataList[id=2040212].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Every 4th Skill this unit uses gains Final Power +4 and inflicts 4 [Combustion] On Hit\n- If the said Skill is a Wrath Skill, deal +([Combustion] Potency on all targets / 2)% additional damage (max 20%)\n- If the said Skill is an E.G.O Skill, apply the following effects at Coin Start of the first Coin:\n· If the said Coin is a Plus Coin, heal 10 SP\n· If the said Coin is a Minus Coin, lose 15 SP (this effect cannot reduce this unit's SP below -40)
   PL:
84. [Pasywka E.G.O — podsumowanie] 4번째로 사용하는 스킬이 강화됨
   źródło: Passive_Ego.json :: dataList[id=2040212].summary
   limit: do 120 znaków
   EN: Every 4th Skill used is enhanced
   PL:

## E.G.O [20403] Red Eyes (적안) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20403`

85. [Karta E.G.O — nazwa] 적안
   źródło: Egos.json :: dataList[id=20403].name
   limit: do 40 znaków
   EN: Red Eyes
   PL:
86. [Karta E.G.O — opis] 료슈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20403].desc
   limit: do 120 znaków
   EN: Ryōshū’s E.G.O Gear
   PL:
87. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 적안
   źródło: Skills_Ego.json :: dataList[id=2040311].levelList[level=1].name ; dataList[id=2040311].levelList[level=3].name ; dataList[id=2040311].levelList[level=4].name
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 거미봉오리
   źródło: Skills_Ego.json :: dataList[id=2040311].levelList[level=1].abName ; dataList[id=2040311].levelList[level=3].abName ; dataList[id=2040311].levelList[level=4].abName
   limit: do 40 znaków
   EN: Spider Bud
   PL:
89. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Ego.json :: dataList[id=2040311].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040311].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040311].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL:
90. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Binding]이 3 이상 있을 때 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_Ego.json :: dataList[id=2040311].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2040311].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040311].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 3+ [Binding], inflict 1 Plus Coin Drop next turn
   PL:
91. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 속도가 자신보다 느릴 때 다음 턴에 참격 취약 2 부여
   źródło: Skills_Ego.json :: dataList[id=2040311].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2040311].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target's Speed is slower than user's, inflict 2 Slash Fragility next turn
   PL:
92. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 적안
   źródło: Skills_Ego.json :: dataList[id=2040321].levelList[level=1].name ; dataList[id=2040321].levelList[level=3].name
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 거미봉오리
   źródło: Skills_Ego.json :: dataList[id=2040321].levelList[level=1].abName ; dataList[id=2040321].levelList[level=3].abName
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2040321].levelList[level=1].desc ; dataList[id=2040321].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly
   PL:
95. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Ego.json :: dataList[id=2040321].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040321].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Binding]이 3 이상 있을 때 다음 턴에 더하기 코인 약화 2 부여
   źródło: Skills_Ego.json :: dataList[id=2040321].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2040321].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 3+ [Binding], inflict 2 Plus Coin Drop next turn
   PL:
97. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 속도가 자신보다 느릴 때 다음 턴에 참격 취약 1-3 부여
   źródło: Skills_Ego.json :: dataList[id=2040321].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target's Speed is slower than user's, inflict 1-3 Slash Fragility next turn
   PL:
98. [Pasywka E.G.O — nazwa] 거미줄
   źródło: Passive_Ego.json :: dataList[id=2040311].name
   limit: do 40 znaków
   EN: Spider's Webs
   PL:
99. [Pasywka E.G.O — opis] 합 승리 시 다음 턴에 속박 1 부여 (턴 당 최대 3회)
   źródło: Passive_Ego.json :: dataList[id=2040311].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: On Clash Win, inflict 1 [Binding] next turn (3 times per turn)
   PL:

## E.G.O [20404] Red Eyes (Open) (적안(開)) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20404`

100. [Karta E.G.O — nazwa] 적안(開)
   źródło: Egos.json :: dataList[id=20404].name
   limit: do 40 znaków
   EN: Red Eyes (Open)
   PL:
101. [Karta E.G.O — opis] 료슈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20404].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 적안(開)
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=1].name ; dataList[id=2040411].levelList[level=3].name ; dataList[id=2040411].levelList[level=4].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 거미봉오리
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=1].abName ; dataList[id=2040411].levelList[level=3].abName ; dataList[id=2040411].levelList[level=4].abName
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — opis] 메인 공격 대상의 속도가 자신보다 3 이상 느릴 때 코인 위력 +4
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=1].desc ; dataList[id=2040411].levelList[level=3].desc
   limit: do 120 znaków
   EN: If main target's Speed is slower than user's by 3 or more, Coin Power +4
   PL:
105. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Binding]이 3 이상 있을 때 피해량 +20%
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 3+ [Binding], deal +20% damage
   PL:
106. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이 스킬로 대상을 흐트러짐 상태로 만들거나 처치하면, 체력이 가장 낮은 아군 1명과 자신의 체력을 최대 체력의 10%만큼 회복
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this skill staggers or defeats a target, heal user and the ally with the least HP by 10% of Max HP
   PL:
107. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 메인 공격 대상의 속도가 자신보다 3 이상 느릴 때 코인 위력 +7
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=4].desc
   limit: do 120 znaków
   EN: If main target's Speed is slower than user's by 3 or more, Coin Power +7
   PL:
108. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Binding]이 3 이상 있을 때 피해량 +40%
   źródło: Skills_Ego.json :: dataList[id=2040411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 3+ [Binding], deal +40% damage
   PL:
109. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 적안(開)
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=1].name ; dataList[id=2040421].levelList[level=3].name ; dataList[id=2040421].levelList[level=4].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 거미봉오리
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=1].abName ; dataList[id=2040421].levelList[level=3].abName ; dataList[id=2040421].levelList[level=4].abName
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격\n메인 공격 대상의 속도가 자신보다 3 이상 느릴 때 최종 위력 +7
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=1].desc ; dataList[id=2040421].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly\nIf main target's Speed is slower than user's by 3 or more, Final Power +7
   PL:
112. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Binding]이 3 이상 있을 때 피해량 +30%
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 3+ [Binding], deal +30% damage
   PL:
113. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이 스킬로 대상을 흐트러짐 상태로 만들거나 처치하면, 체력이 가장 낮은 아군 1명과 자신의 체력을 최대 체력의 10%만큼 회복
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n메인 공격 대상의 속도가 자신보다 3 이상 느릴 때 최종 위력 +10
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly\nIf main target's Speed is slower than user's by 3 or more, Final Power +10
   PL:
115. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Binding]이 3 이상 있을 때 피해량 +50%
   źródło: Skills_Ego.json :: dataList[id=2040421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 3+ [Binding], deal +50% damage
   PL:
116. [Pasywka E.G.O — nazwa] 포식
   źródło: Passive_Ego.json :: dataList[id=2040411].name
   limit: do 40 znaków
   EN: Predator
   PL:
117. [Pasywka E.G.O — opis] 이번 턴에 최대 체력의 10%를 초과하여 체력을 회복한 경우, 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Passive_Ego.json :: dataList[id=2040411].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: If this unit healed more than 10% of its Max HP this turn, gain 1 [Enhancement] next turn.
   PL:

## E.G.O [20405] Soda (소다) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20405`

118. [Karta E.G.O — nazwa] 소다
   źródło: Egos.json :: dataList[id=20405].name
   limit: do 40 znaków
   EN: Soda
   PL:
119. [Karta E.G.O — opis] 료슈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20405].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4,5) — nazwa] 소다
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=1].name ; dataList[id=2040511].levelList[level=3].name ; dataList[id=2040511].levelList[level=4].name ; dataList[id=2040511].levelList[level=5].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4,5) — źródło (Anomalia)] 웰치어스
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=1].abName ; dataList[id=2040511].levelList[level=3].abName ; dataList[id=2040511].levelList[level=4].abName ; dataList[id=2040511].levelList[level=5].abName
   limit: do 40 znaków
   EN: Wellcheers
   PL:
122. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Sinking
   PL:
123. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [EnemyKill] 현재 보유 중인 E.G.O 자원 중 무작위 속성 1개의 E.G.O 자원을 3개 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 3 E.G.O resources of a random Affinity currently owned
   PL:
124. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Sinking
   PL:
125. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [EnemyKill] 현재 보유 중인 E.G.O 자원 중 무작위 속성 1개의 E.G.O 자원을 3개 얻음. 모든 아군의 정신력 3 회복
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 3 E.G.O resources of a random Affinity currently owned; All allies heal 3 SP
   PL:
126. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Sinking
   PL:
127. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — opis] <style="highlight">대상의 현재 체력이 최대 체력의 25% 미만이면, 피해량 +40%\n[BeforeAttack] 최대 공명수가 4 이상이면, 공격 가중치 +1\n\n[EndSkill] 다음 턴에 자신을 포함한 무작위 아군 2+ (최대 공명 수)명에게 [GainSinStockAdder] 1 부여 (최대 7명)\n[EndSkill] 공격 대상 중 흐트러짐이나 패닉 상태인 대상이 있으면, 가장 적게 보유한 E.G.O 자원 1개를 얻음. 자신의 정신력 3 회복</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=5].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill], [GainSinStockAdder]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp
   EN: <style="highlight">If target has less than 25% HP, deal +40% damage\n[BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n\n[EndSkill] Apply 1 [GainSinStockAdder] next turn to (2 + highest Reson.) random allies, including this unit (max 7)\n[EndSkill] If there are Staggered or Panicked units among targets, gain 1 E.G.O resource for the least-owned Affinity; heal 3 SP</style>
   PL:
128. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 4 부여</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 4 [Vibration]</style>
   PL:
129. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 6 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 6 [Sinking]<style="highlight"></style>
   PL:
130. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 3 — opis] [EnemyKill] 현재 보유 중인 E.G.O 자원 중 무작위 속성 1개의 E.G.O 자원을 3개 얻음. 모든 아군의 정신력 3 회복<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040511].levelList[level=5].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 3 E.G.O resources of a random Affinity currently owned; All allies heal 3 SP<style="highlight"></style>
   PL:
131. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4,5) — nazwa] 소다
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=1].name ; dataList[id=2040521].levelList[level=3].name ; dataList[id=2040521].levelList[level=4].name ; dataList[id=2040521].levelList[level=5].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4,5) — źródło (Anomalia)] 웰치어스
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=1].abName ; dataList[id=2040521].levelList[level=3].abName ; dataList[id=2040521].levelList[level=4].abName ; dataList[id=2040521].levelList[level=5].abName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=1].desc ; dataList[id=2040521].levelList[level=3].desc ; dataList[id=2040521].levelList[level=4].desc
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [EndSkill] 모든 아군에게 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">E.G.O 자원 획득량 +</color></link></u>1 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2040521].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="GainSinStockAdder">, <color=#f8c200>, <u>, <link="GainSinStockAdder">, </color>, </link>, </u>, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] All allies gain +1 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">E.G.O Resource Amp</color></link></u>.
   PL:
136. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 모든 아군에게 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">E.G.O 자원 획득량 +</color></link></u>1, 다음 턴에 신속 1 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="GainSinStockAdder">, <color=#f8c200>, <u>, <link="GainSinStockAdder">, </color>, </link>, </u>, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] All allies gain +1 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">E.G.O Resource Amp</color></link></u>., apply 1 Haste next turn
   PL:
139. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — opis] [CantIdentify]\n무작위 대상 공격\n\n<style="highlight">대상의 현재 체력이 최대 체력의 25% 미만이면, 피해량 +40%\n[DefeatDuel] 기본 위력 -12\n[BeforeAttack] 최대 공명수가 4 이상이면, 공격 가중치 +1\n[EndSkill] 공격 대상 중 흐트러짐이나 패닉 상태인 대상이 있으면, 가장 적게 보유한 E.G.O 자원 1개를 얻음. 자신의 정신력 3 회복</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=5].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [DefeatDuel], [BeforeAttack], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n\n<style="highlight">If target has less than 25% HP, deal +40% damage\n[DefeatDuel] Base Power -12\n[BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n[EndSkill] If there are Staggered or Panicked units among targets, gain 1 E.G.O resource for the least-owned Affinity; heal 3 SP</style>
   PL:
140. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[SuperCoin]</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=5].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 4 부여</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=5].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 6 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=5].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 4 — opis] [EndSkill] 모든 아군에게 [GainSinStockAdder] 1, 다음 턴에 [Agility] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=5].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [GainSinStockAdder], [Agility]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp; [Agility] = 신속 / Haste
   EN: [EndSkill] All allies gain 1 [GainSinStockAdder], apply 1 [Agility] next turn<style="highlight"></style>
   PL:
144. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 5 — opis] <style="highlight">[EndSkillTail] 다음 턴에 모든 아군에게 [GainSinStockAdder] 1 부여 (턴 당 1회)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040521].levelList[level=5].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkillTail], [GainSinStockAdder]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]; [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp
   EN: <style="highlight">[EndSkillTail] All allies gain 1 [GainSinStockAdder] next turn (once per turn)</style>
   PL:
145. [Pasywka E.G.O — nazwa] 뚜껑 따인 음료수
   źródło: Passive_Ego.json :: dataList[id=2040511].name
   limit: do 40 znaków
   EN: Opened Can
   PL:
146. [Pasywka E.G.O — opis] [Sinking]이 5 이상 부여된 적에게 공격 적중 시 수비 위력 감소 1 부여 (턴 당 최대 5회)
   źródło: Passive_Ego.json :: dataList[id=2040511].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking], [Disarming]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: On Hit, if target has 5+ [Sinking], inflict 1 [Disarming] (5 times per turn)
   PL:
147. [Pasywka E.G.O — nazwa] 뚜껑 따인 음료수
   źródło: Passive_Ego.json :: dataList[id=2040512].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Pasywka E.G.O — opis] [Sinking]이 5 이상 부여된 적에게 공격 적중 시 [Disarming] 1 부여 (턴 당 최대 5회)\n\n<style="highlight">흐트러짐 또는 패닉 상태인 적에게 공격 적중 시 다음 턴에 [AttackUp] 1 얻음 (턴 당 3회. 집중 전투인 경우, 본체로 판정)</style>
   źródło: Passive_Ego.json :: dataList[id=2040512].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Sinking], [Disarming], [AttackUp]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Disarming] = 수비 위력 감소 / Defense Power Down; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Hit, if target has 5+ [Sinking], inflict 1 [Disarming] (5 times per turn)\n\n<style="highlight">On Hit against an enemy in Staggered or Panic states, gain 1 [AttackUp] next turn (3 times per turn; in Focused Encounters, the Core)</style>
   PL:

## E.G.O [20406] Blind Obsession (맹목) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20406`

149. [Karta E.G.O — nazwa] 맹목
   źródło: Egos.json :: dataList[id=20406].name
   limit: do 40 znaków
   EN: Blind Obsession
   PL:
150. [Karta E.G.O — opis] 료슈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20406].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 맹목
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040611].levelList[level=1].name ; dataList[id=2040611].levelList[level=3].name ; dataList[id=2040611].levelList[level=4].name
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 꿈먹는 탁류
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040611].levelList[level=1].abName ; dataList[id=2040611].levelList[level=3].abName ; dataList[id=2040611].levelList[level=4].abName
   limit: do 40 znaków
   EN: Dream-Devouring Siltcurrent
   PL:
153. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 호흡 4 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040611].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] Gain 4 Poise
   PL:
154. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040611].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040611].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL:
155. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040611].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2040611].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040611].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Gain +2 Charge Count
   PL:
156. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] [BeforeAttack] 호흡 4 얻음\n[EndSkill] 이 스킬이 적중한 대상 중 사망한 캐릭터 수만큼 호흡 2를 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040611].levelList[level=3].desc ; dataList[id=2040611].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain 4 Poise\n[EndSkill] Gain 2 Poise for every unit defeated by this Skill
   PL:
157. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 맹목
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040621].levelList[level=1].name ; dataList[id=2040621].levelList[level=3].name ; dataList[id=2040621].levelList[level=4].name
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 꿈먹는 탁류
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040621].levelList[level=1].abName ; dataList[id=2040621].levelList[level=3].abName ; dataList[id=2040621].levelList[level=4].abName
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 호흡 4 얻음. 자신의 충전 횟수를 2씩 소모하여, 호흡 1을 얻음 (최대 10)\n[EndSkill] 이 스킬이 적중한 대상 중 사망한 캐릭터 수만큼 자신의 충전 횟수 4 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040621].levelList[level=1].desc ; dataList[id=2040621].levelList[level=3].desc ; dataList[id=2040621].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain 4 Poise. Consume 2 Charge Count to gain 1 Poise (Max 10)\n[EndSkill] Gain +4 Charge Count for every unit defeated by this Skill
   PL:
160. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040621].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2040621].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Poise Count
   PL:
161. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 [Breath]이 10 이상이면, 크리티컬 피해량 +30%
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] At 10+ [Breath], gain +30% Critical Damage
   PL:
162. [Pasywka E.G.O — nazwa] 꿈 먹기
   źródło: Passive_Ego.json :: dataList[id=2040611].name
   limit: do 40 znaków
   EN: Dream Devouring
   PL:
163. [Pasywka E.G.O — opis] 오만 속성 스킬로 크리티컬 적중 시 호흡 횟수 1 증가 (턴 당 최대 3회)
   źródło: Passive_Ego.json :: dataList[id=2040611].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On Crit with a Pride affinity Skill, gain 1 [Breath] Count (3 times per turn)
   PL:

## E.G.O [20407] Contempt, Awe (경멸, 경외) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20407`

164. [Karta E.G.O — nazwa] 경멸, 경외
   źródło: Egos.json :: dataList[id=20407].name
   limit: do 40 znaków
   EN: Contempt, Awe
   PL:
165. [Karta E.G.O — opis] 료슈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20407].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 경멸, 경외
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=1].name ; dataList[id=2040711].levelList[level=3].name ; dataList[id=2040711].levelList[level=4].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 경멸의 나선
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=1].abName ; dataList[id=2040711].levelList[level=3].abName ; dataList[id=2040711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Spiral of Contempt
   PL:
168. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 최대 공명 수만큼 공격 가중치 증가 (최대 2)\n[BeforeAttack] (최대 공명 수 + 1)만큼 [GazePersonality] 얻음 (최대 7)\n[EndSkill] 2턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [GazePersonality], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson.) Atk Weight (max 2)\n[BeforeAttack] Gain (highest Reson. + 1) [GazePersonality] (max 7)\n[EndSkill] For 2 turns, lose 10 SP at Turn End
   PL:
169. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [EndSkill] [Laceration] 10을 공격 대상에게 균등하게 나눠서 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Laceration]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Laceration] = 출혈 / Bleed
   EN: [EndSkill] Evenly inflict 10 [Laceration] between all targets
   PL:
170. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 최대 공명 수만큼 공격 가중치 증가 (최대 <style="highlight">4</style>)\n[BeforeAttack] (최대 공명 수 + 1)만큼 [GazePersonality] 얻음 (최대 7)\n[EndSkill] 2턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [GazePersonality], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson.) Atk Weight (max <style="highlight">4</style>)\n[BeforeAttack] Gain (highest Reson. + 1) [GazePersonality] (max 7)\n[EndSkill] For 2 turns, lose 10 SP at Turn End
   PL:
171. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [EndSkill] [Laceration] <style="highlight">15</style>를 공격 대상에게 균등하게 나눠서 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [Laceration]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Laceration] = 출혈 / Bleed
   EN: [EndSkill] Evenly inflict <style="highlight">15</style> [Laceration] between all targets
   PL:
172. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 최대 공명 수만큼 공격 가중치 증가 (최대 <style="highlight">6</style>)\n[BeforeAttack] <style="highlight">이번 턴과 다음 턴에</style> (최대 공명 수 + 1)만큼 [GazePersonality] 얻음 (최대 7)\n<style="highlight">[EndSkill] 이 스킬을 포함하여 색욕 공명을 했다면, 자신이 보유한 기본 공격 스킬과 동일한 속성의 E.G.O 자원 +1</style>\n[EndSkill] 2턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [GazePersonality], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson.) Atk Weight (max <style="highlight">6</style>)\n[BeforeAttack] Gain (highest Reson. + 1) [GazePersonality] <style="highlight">this turn and next turn</style> (max 7)\n<style="highlight">[EndSkill] If this Skill was part of a Lust Reson., gain 1 E.G.O resource in Affinities corresponding to each of this unit's Attack Skills</style>\n[EndSkill] For 2 turns, lose 10 SP at Turn End
   PL:
173. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [EndSkill] [Laceration] 15를 공격 대상에게 균등하게 나눠서 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [Laceration]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Laceration] = 출혈 / Bleed
   EN: [EndSkill] Evenly inflict 15 [Laceration] between all targets<style="highlight"></style>
   PL:
174. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 경멸, 경외
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=1].name ; dataList[id=2040721].levelList[level=3].name ; dataList[id=2040721].levelList[level=4].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 경멸의 나선
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=1].abName ; dataList[id=2040721].levelList[level=3].abName ; dataList[id=2040721].levelList[level=4].abName
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] [GazePersonality] 7 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=1].desc ; dataList[id=2040721].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [GazePersonality]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GazePersonality] = 경멸의 시선 / Gaze of Contempt
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain 7 [GazePersonality]
   PL:
177. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, 피해량 +(대상의 [Laceration] 위력과 [Laceration] 횟수의 합)% (최대 20%)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], deal +([Laceration] on target + [Laceration] Count on target)% damage (max 20%)
   PL:
178. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] (1 + 최대 공명 수 x 1.5) 부여 (최대 10, 소수점 버림)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (1 + (highest Reson. x 1.5)) [Laceration] (max 10, rounded down)
   PL:
179. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
180. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, 피해량 +(대상의 [Laceration] 위력과 [Laceration] 횟수의 합)% (최대 <style="highlight">40%</style>)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], deal +([Laceration] on target + [Laceration] Count on target)% damage (max <style="highlight">40%</style>)
   PL:
181. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">(3 + 최대 공명 수 x 2)</style> 부여 (최대 <style="highlight">15</style>, 소수점 버림)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">(3 + (highest Reson. x 2))</style> [Laceration] (max <style="highlight">15</style>, rounded down)
   PL:
182. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">3</style> [Laceration] Count
   PL:
183. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] [GazePersonality] 7 얻음\n<style="highlight">[EndSkill] 이 스킬을 포함하여 색욕 공명을 했다면, 자신이 보유한 기본 공격 스킬과 동일한 속성의 E.G.O 자원 +1</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [GazePersonality], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain 7 [GazePersonality]\n<style="highlight">[EndSkill] If this Skill was a part of a Lust Reson., gain 1 E.G.O resource in Affinities corresponding to each of this unit's Attack Skills</style>
   PL:
184. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, 피해량 +(대상의 [Laceration] 위력과 [Laceration] 횟수의 합)% (최대 <style="highlight">60%</style>)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], deal +([Laceration] on target + [Laceration] Count on target)% damage (max <style="highlight">60%</style>)
   PL:
185. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">(10 + 최대 공명 수 x 2.5)</style> 부여 (최대 <style="highlight">25</style>, 소수점 버림)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">(10 + (highest Reson. x 2.5))</style> [Laceration] (max <style="highlight">25</style>, rounded down)
   PL:
186. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040721].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">5</style> [Laceration] Count
   PL:
187. [Pasywka E.G.O — nazwa] 시선의 흔적
   źródło: Passive_Ego.json :: dataList[id=2040711].name
   limit: do 40 znaków
   EN: Mark of the Gaze
   PL:
188. [Pasywka E.G.O — opis] 자신이 적에게 기본 공격 스킬을 사용할 때마다 자신이 사용한 스킬 속성 이외의 제일 적게 보유한 무작위 속성 E.G.O 자원 1개를 추가로 얻음 (턴 당 2회)
   źródło: Passive_Ego.json :: dataList[id=2040711].desc
   limit: do 280 znaków
   EN: Whenever this unit uses a base Attack Skill against an enemy, gain 1 additional E.G.O resource for a random, least-owned Affinity that doesn't correspond to the Affinity of the Attack Skill used (2 times per turn)
   PL:

## E.G.O [20408] Thoracalgia (흉통) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20408`

189. [Karta E.G.O — nazwa] 흉통
   źródło: Egos.json :: dataList[id=20408].name
   limit: do 40 znaków
   EN: Thoracalgia
   PL:
190. [Karta E.G.O — opis] 료슈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20408].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 흉통
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=1].name ; dataList[id=2040811].levelList[level=3].name ; dataList[id=2040811].levelList[level=4].name
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 지난 날의 침낭
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=1].abName ; dataList[id=2040811].levelList[level=3].abName ; dataList[id=2040811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Sleeping Bag of a Bygone Day
   PL:
193. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 최대 공명 수만큼 [Breath] 얻음 (최대 4)\n- [Breath]이 15 이상이면, 대신 최종 위력 + (최대 공명 수) (최대 4)\n[BeforeAttack] (최대 공명 수/2)만큼 [Breath] 횟수 증가 (최대 2)\n- [Breath] 횟수가 5 이상이면, 대신 코인 위력 + (최대 공명 수/2) (최대 2)\n[TargetKill] 다음 턴에 [HoldingBreath] 1 얻음 (턴 당 최대 2)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Breath], [TargetKill], [HoldingBreath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [TargetKill] = [대상 처치 시] / [On Target Kill]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [BeforeAttack] Gain (highest Reson.) [Breath] (max 4)\n- At 15+ [Breath], gain Final Power +(highest Reson.) instead (max 4)\n[BeforeAttack] Gain (highest Reson. / 2) [Breath] Count (max 2)\n- At 5+ [Breath] Count, gain Coin Power +(highest Reson. / 2) instead (max 2)\n[TargetKill] Gain 1 [HoldingBreath] next turn (2 times per turn)
   PL:
194. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [HoldingBreath] 2 얻음 (턴 당 1회)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HoldingBreath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [OnSucceedAttack] Gain 2 [HoldingBreath] (once per turn)
   PL:
195. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 최대 공명 수만큼 [Breath] 얻음 (최대 <style="highlight">6</style>)\n- [Breath]이 15 이상이면, 대신 최종 위력 + (최대 공명 수) (최대 <style="highlight">6</style>)\n[BeforeAttack] (최대 공명 수/2)만큼 [Breath] 횟수 증가 (최대 2)\n- [Breath] 횟수가 5 이상이면, 대신 코인 위력 + (최대 공명 수/2) (최대 2)\n[TargetKill] 다음 턴에 [HoldingBreath] <style="highlight">2</style> 얻음 (턴 당 최대 <style="highlight">4</style>)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=3].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Breath], [TargetKill], [HoldingBreath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [TargetKill] = [대상 처치 시] / [On Target Kill]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [BeforeAttack] Gain (highest Reson.) [Breath] (max <style="highlight">6</style>)\n- At 15+ [Breath], gain Final Power +(highest Reson.) instead (max <style="highlight">6</style>)\n[BeforeAttack] Gain (highest Reson. / 2) [Breath] Count (max 2)\n- At 5+ [Breath] Count, gain Coin Power +(highest Reson. / 2) instead (max 2)\n[TargetKill] Gain <style="highlight">2</style> [HoldingBreath] next turn (<style="highlight">4</style> times per turn)
   PL:
196. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] <style="highlight">크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합)% (최대 20%)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: <style="highlight">Deal +([Breath] Potency + Count)% damage on Critical Hit (max 20%)</style>
   PL:
197. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [HoldingBreath] 2 얻음 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [HoldingBreath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [OnSucceedAttack] Gain 2 [HoldingBreath] (once per turn)<style="highlight"></style>
   PL:
198. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 최대 공명 수만큼 [Breath] 얻음 (최대 6)\n- [Breath]이 15 이상이면, 대신 최종 위력 + (최대 공명 수) (최대 6)\n[BeforeAttack] (최대 공명 수/2)만큼 [Breath] 횟수 증가 (최대 <style="highlight">3</style>)\n- [Breath] 횟수가 5 이상이면, 대신 코인 위력 + (최대 공명 수/2) (최대 <style="highlight">3</style>)\n[TargetKill] 다음 턴에 [HoldingBreath] 2 얻음 (턴 당 최대 <style="highlight">6</style>)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Breath], [TargetKill], [HoldingBreath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [TargetKill] = [대상 처치 시] / [On Target Kill]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [BeforeAttack] Gain (highest Reson.) [Breath] (max 6)\n- At 15+ [Breath], gain Final Power +(highest Reson.) instead (max 6)\n[BeforeAttack] Gain (highest Reson. / 2) [Breath] Count (max <style="highlight">3</style>)\n- At 5+ [Breath] Count, gain Coin Power +(highest Reson. / 2) instead (max <style="highlight">3</style>)\n[TargetKill] Gain 2 [HoldingBreath] next turn (<style="highlight">6</style> times per turn)
   PL:
199. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합)% (최대 <style="highlight">40%</style>)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Deal +([Breath] Potency + Count)% damage on Critical Hit (max <style="highlight">40%</style>)
   PL:
200. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [HoldingBreath] <style="highlight">4</style> 얻음 (턴 당 1회)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040811].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [HoldingBreath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [OnSucceedAttack] Gain <style="highlight">4</style> [HoldingBreath] (once per turn)
   PL:
201. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 흉통
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=1].name ; dataList[id=2040821].levelList[level=3].name ; dataList[id=2040821].levelList[level=4].name
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 지난 날의 침낭
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=1].abName ; dataList[id=2040821].levelList[level=3].abName ; dataList[id=2040821].levelList[level=4].abName
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n체력이 가장 낮은 대상 우선 공격 (아군 우선 지정)\n공격 대상에 아군이 포함되어 있으면 피해량 +30%\n\n[BeforeAttack] [Breath]이 15 미만이면, 최대 체력의 10%만큼 체력을 소모하여 [Breath] 5 얻고, [Breath] 횟수 5 증가\n- 이 효과로 흐트러지거나 사망하지 않음\n\n[EndSkill] 대상이 사망했으면, 다음 턴에 [HoldingBreath] 2 얻음 (턴 당 1회). 대상이 아군이면 아래 효과 추가 발동\n- 처치된 아군으로 인해 대기 해제되거나 전투에 참여하는 아군이 [Breath] 2 얻고, [Breath] 횟수 2 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=1].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Breath], [EndSkill], [HoldingBreath]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [CantIdentify]\nPrioritizes targets with the least HP (prioritizes allies)\nIf an ally is one of this Skill's targets, deal +30% damage\n\n[BeforeAttack] At less than 15 [Breath], consume 10% HP to gain 5 [Breath] and +5 [Breath] Count\n- Cannot be Staggered or defeated due to this effect\n\n[EndSkill] If target is defeated, gain 2 [HoldingBreath] next turn. (once per turn) If the said target was an ally, activate the following as well:\n- Allies that are made to participate or are Substituted into this Encounter due to the defeated allies gain 2 [Breath] and +2 [Breath] Count
   PL:
204. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [HoldingBreath] 4 얻음 (턴 당 1회)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HoldingBreath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [OnSucceedAttack] Gain 4 [HoldingBreath] (once per turn)
   PL:
205. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n체력이 가장 낮은 대상 우선 공격 (아군 우선 지정)\n공격 대상에 아군이 포함되어 있으면 피해량 +30%\n\n[BeforeAttack] [Breath]이 15 미만이면, 최대 체력의 10%만큼 체력을 소모하여 [Breath] 5 얻고, [Breath] 횟수 5 증가\n- 이 효과로 흐트러지거나 사망하지 않음\n<style="highlight">- 공격 대상에 포함된 아군 1명당 [Breath] 1 얻음 (최대 2)</style>\n\n[EndSkill] 대상이 사망했으면, 다음 턴에 [HoldingBreath] 2 얻음 (턴 당 1회). 대상이 아군이면 아래 효과 추가 발동\n- 처치된 아군으로 인해 대기 해제되거나 전투에 참여하는 아군이 [Breath] <style="highlight">4</style> 얻고, [Breath] 횟수 2 증가\n<style="highlight">- 이 스킬로 소모한 정신력의 절반만큼 회복</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=3].desc
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Breath], [EndSkill], [HoldingBreath]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [CantIdentify]\nPrioritizes targets with the least HP (prioritizes allies)\nIf an ally is one of this Skill's targets, deal +30% damage\n\n[BeforeAttack] At less than 15 [Breath], consume 10% HP to gain 5 [Breath] and +5 [Breath] Count\n- Cannot be Staggered or defeated due to this effect\n<style="highlight">- Gain 1 [Breath] for every ally targeted by this Skill (max 2)</style>\n\n[EndSkill] If target is defeated, gain 2 [HoldingBreath] next turn. (once per turn) If the said target was an ally, activate the following as well:\n- Allies that are made to participate or are Substituted into this Encounter due to the defeated allies gain <style="highlight">4</style> [Breath] and +2 [Breath] Count\n<style="highlight">- Recover half of SP used by this Skill</style>
   PL:
206. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] <style="highlight">크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합)% (최대 20%)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [HoldingBreath] 4 얻음 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [HoldingBreath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [OnSucceedAttack] Gain 4 [HoldingBreath] (once per turn)<style="highlight"></style>
   PL:
208. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n체력이 가장 낮은 대상 우선 공격 (아군 우선 지정)\n공격 대상에 아군이 포함되어 있으면 피해량 +30%\n\n[BeforeAttack] [Breath]이 15 미만이면, 최대 체력의 10%만큼 체력을 소모하여 [Breath] 5 얻고, [Breath] 횟수 5 증가\n- 이 효과로 흐트러지거나 사망하지 않음\n- 공격 대상에 포함된 아군 1명당 [Breath] <style="highlight">2</style> 얻음 (최대 <style="highlight">4</style>)\n\n[EndSkill] 대상이 사망했으면, 다음 턴에 [HoldingBreath] 3 얻음 (턴 당 1회). 대상이 아군이면 아래 효과 추가 발동\n- 처치된 아군으로 인해 대기 해제되거나 전투에 참여하는 아군이 [Breath] 4 얻고, [Breath] 횟수 <style="highlight">4</style> 증가\n<style="highlight">- 이 스킬로 소모한 정신력을 회복하고, 소모한 E.G.O 자원을 속성 별로 1개씩 얻음</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=4].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Breath], [EndSkill], [HoldingBreath]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [CantIdentify]\nPrioritizes targets with the least HP (prioritizes allies)\nIf an ally is one of this Skill's targets, deal +30% damage\n\n[BeforeAttack] At less than 15 [Breath], consume 10% HP to gain 5 [Breath] and +5 [Breath] Count\n- Cannot be Staggered or defeated due to this effect\n- Gain <style="highlight">2</style> [Breath] for every ally targeted by this Skill (max <style="highlight">4</style>)\n\n[EndSkill] If target is defeated, gain 3 [HoldingBreath] next turn. (once per turn) If the said target was an ally, activate the following as well:\n- Allies that are made to participate or are Substituted into this Encounter due to the defeated allies gain 4 [Breath] and +<style="highlight">4</style> [Breath] Count\n<style="highlight">- Recover SP used by this Skill and regain 1 of each E.G.O resources consumed</style>
   PL:
209. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합)% (최대 <style="highlight">40%</style>)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [HoldingBreath] <style="highlight">7</style> 얻음 (턴 당 1회)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [HoldingBreath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HoldingBreath] = 깊은 들숨 / Deep Inhale
   EN: [OnSucceedAttack] Gain <style="highlight">7</style> [HoldingBreath] (once per turn)
   PL:
211. [Pasywka E.G.O — nazwa] 숨
   źródło: Passive_Ego.json :: dataList[id=2040811].name
   limit: do 40 znaków
   EN: Breath
   PL:
212. [Pasywka E.G.O — opis] 이 E.G.O 스킬을 사용한 다음 턴 시작 시, [NebulizerInhale] 1 얻음 (턴 당 1회)\n- 이 스킬로 적을 처치하였다면 처치한 대상 수만큼 [NebulizerInhale] 추가로 얻음\n- 이 스킬로 아군을 처치하였다면 (처치한 대상 수 X 2)만큼 [NebulizerInhale] 추가로 얻음\n- 이 수치는 이번 전투 동안 누적됨
   źródło: Passive_Ego.json :: dataList[id=2040811].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [NebulizerInhale]
   znaczenie tagów: [NebulizerInhale] = 네뷸라이저 β / Nebulizer β
   EN: Next Turn Start after using this E.G.O Skill: gain 1 [NebulizerInhale] (once per turn)\n- If this Skill defeated enemies, gain additional [NebulizerInhale] equal to the number of targets defeated\n- If this Skill defeated allies, gain (targets defeated x 2) additional [NebulizerInhale]\n- This value Stacks over this Encounter's duration
   PL:

## E.G.O [20409] Great Trichiliocosm [三千大世界] (삼천대세계 [三千大世界]) — Ryōshū
- postać: Ryōshū (료슈) · ID E.G.O: `20409`

213. [Karta E.G.O — nazwa] 삼천대세계 [三千大世界]
   źródło: Egos.json :: dataList[id=20409].name
   limit: do 40 znaków
   EN: Great Trichiliocosm [三千大世界]
   PL:
214. [Karta E.G.O — opis] 료슈 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20409].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 삼천대세계[三千大世界]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].name ; dataList[id=2040911].levelList[level=3].name ; dataList[id=2040911].levelList[level=4].name
   limit: do 40 znaków
   EN: Great Trichiliocosm [三千大世界]
   PL:
216. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 나생접[羅生蝶]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].abName ; dataList[id=2040911].levelList[level=3].abName ; dataList[id=2040911].levelList[level=4].abName
   limit: do 50 znaków
   EN: Butterfly of Entangled Lives [羅生蝶]
   PL:
217. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] (최대 공명 수)만큼 [Breath] 얻음 (최대 7)\n\n[EndSkill] [RyoshuEGOPF] 1 얻음\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Breath], [EndSkill], [RyoshuEGOPF]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [BeforeAttack] Gain (highest Reson.) [Breath] (max 7)\n\n[EndSkill] Gain 1 [RyoshuEGOPF]\n[EndSkill] Lose 10 SP at Turn End for 3 turns
   PL:
218. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
220. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
222. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +30% Damage on Critical Hit
   PL:
224. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnStartCoin] 자신의 [RyoshuEGOPF]을 모두 소모하고, 소모한 수치 5당 피해량 +1% (최대 100%)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [OnStartCoin] Consume all [RyoshuEGOPF] on self and deal +1% damage for every 5 [RyoshuEGOPF] consumed (max 100%)
   PL:
225. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 3 — podsumowanie] [OnStartCoin] [RyoshuEGOPF]에 비례하여 피해량이 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=1].coinlist[#2].coindescs[#2].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [OnStartCoin] Deal more damage based on [RyoshuEGOPF]
   PL:
226. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (최대 공명 수)만큼 [Breath] 얻음 (최대 7)\n<style="highlight">[BeforeAttack] 자신의 [Breath] 횟수 2 증가</style>\n\n[EndSkill] [RyoshuEGOPF] 1 얻음\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Breath], [EndSkill], [RyoshuEGOPF]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [BeforeAttack] Gain (highest Reson.) [Breath] (max 7)\n<style="highlight">[BeforeAttack] Gain +2 [Breath] Count</style>\n\n[EndSkill] Gain 1 [RyoshuEGOPF]\n[EndSkill] Lose 10 SP at Turn End for 3 turns
   PL:
227. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
228. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040911].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL:
229. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Binding] next turn</style>
   PL:
230. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2040911].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2040911].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL:
232. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttack] 마지막 코인 위력 +3 (스킬 당 1회)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: <style="highlight">[CriticalOnSucceedAttack] Coin Power +3 for the final Coin (once per Skill)</style>
   PL:
233. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2040911].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2040911].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: +30% Damage on Critical Hit<style="highlight"></style>
   PL:
235. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 3 — opis] <style="highlight">[OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 위력) 10당 피해량 +1% (최대 30%)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Combustion], [Laceration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnStartCoin] Deal +1% damage for every 10 ([Combustion] Potency + [Laceration] Potency) on all targets (max 30%)</style>
   PL:
236. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 4 — opis] <style="highlight">[OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 횟수) 10당 코인 위력 +1 (최대 3)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Combustion], [Laceration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnStartCoin] Coin Power +1 for every 10 ([Combustion] Count + [Laceration] Count) on all targets (max 3)</style>
   PL:
237. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 5 — opis] [OnStartCoin] 자신의 [RyoshuEGOPF]을 모두 소모하고, 소모한 수치 5당 피해량 +1% (최대 100%)\n- 공격 대상이 1명이면, 이 효과가 1.5배로 적용됨 (집중 전투인 경우, 본체를 기준으로 판정)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#2].coindescs[#4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [OnStartCoin] Consume all [RyoshuEGOPF] on self and deal +1% damage for every 5 [RyoshuEGOPF] consumed (max 100%)\n- When attacking just a single target, the damage modifying effect above is applied at 1.5x its value (in Focused Encounters, a Core and its connected Parts count as a single target)
   PL:
238. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 5 — podsumowanie] <style="highlight">[OnStartCoin] [RyoshuEGOPF]에 비례하여 피해량이 증가</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=3].coinlist[#2].coindescs[#4].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: <style="highlight">[OnStartCoin] Deal more damage based on [RyoshuEGOPF]</style>
   PL:
239. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (최대 공명 수)만큼 [Breath] 얻음 (최대 7)\n[BeforeAttack] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가\n\n[EndSkill] [RyoshuEGOPF] 1 얻음\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Breath], [EndSkill], [RyoshuEGOPF]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [BeforeAttack] Gain (highest Reson.) [Breath] (max 7)\n[BeforeAttack] Gain <style="highlight">+3</style> [Breath] Count\n\n[EndSkill] Gain 1 [RyoshuEGOPF]\n[EndSkill] Lose 10 SP at Turn End for 3 turns
   PL:
240. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn<style="highlight"></style>
   PL:
241. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] 마지막 코인 위력 <style="highlight">+5</style> (스킬 당 1회)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Coin Power <style="highlight">+5</style> for the final Coin (once per Skill)
   PL:
242. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 위력) 10당 피해량 +1% <style="highlight">(최대 50%)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Combustion], [Laceration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [OnStartCoin] Deal +1% damage for every 10 ([Combustion] Potency + [Laceration] Potency) on all targets <style="highlight">(max 50%)</style>
   PL:
243. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 횟수) 10당 코인 위력 +1 <style="highlight">(최대 5)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Combustion], [Laceration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [OnStartCoin] Coin Power +1 for every 10 ([Combustion] Count + [Laceration] Count) on all targets <style="highlight">(max 5)</style>
   PL:
244. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 5 — opis] [OnStartCoin] 자신의 [RyoshuEGOPF]을 모두 소모하고, 소모한 수치 5당 피해량 +1% <style="highlight">(최대 198%)</style>\n- 공격 대상이 1명이면, 이 효과가 <style="highlight">2배</style>로 적용됨 (집중 전투인 경우, 본체를 기준으로 판정)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [OnStartCoin] Consume all [RyoshuEGOPF] on self and deal +1% damage for every 5 [RyoshuEGOPF] consumed <style="highlight">(max 198%)</style>\n- When attacking just a single target, the damage modifying effect above is applied at <style="highlight">2x</style> its value (in Focused Encounters, a Core and its connected Parts count as a single target)
   PL:
245. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 5 — podsumowanie] [OnStartCoin] [RyoshuEGOPF]에 비례하여 피해량이 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040911].levelList[level=4].coinlist[#2].coindescs[#4].summary
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 삼천대세계[三千大世界]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].name ; dataList[id=2040921].levelList[level=3].name ; dataList[id=2040921].levelList[level=4].name
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 나생접[羅生蝶]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].abName ; dataList[id=2040921].levelList[level=3].abName ; dataList[id=2040921].levelList[level=4].abName
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 20을 초과하는 [Breath]을 최대 20까지 소모하여, 소모한 [Breath] 1당 최대 체력의 1% 회복 (최소 1), 이 스킬 피해량 +1%\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [RyoshuEGOPF]이 999면, 기본 위력 +1\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -3 (최대 -9)\n\n[EndSkill] [RyoshuEGOPF] 10 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Breath], [RyoshuEGOPF], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Consume a maximum of 20 surplus [Breath] past 20 [Breath] on self, and for every [Breath] consumed, heal 1% of max HP (min 1 HP) and deal +1% damage with this Skill\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] At 999 [RyoshuEGOPF], Base Power +1\n[BeforeAttack] Base Power -3 for every Cracked Coin (max -9)\n\n[EndSkill] Gain 10 [RyoshuEGOPF]
   PL:
249. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnStartCoin] 자신의 [RyoshuEGOPF]을 모두 소모하고, 소모한 수치 5당 피해량 +1% (최대 100%)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 3 — podsumowanie] [OnStartCoin] [RyoshuEGOPF]에 비례하여 피해량이 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=1].coinlist[#2].coindescs[#2].summary
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 20을 초과하는 [Breath]을 최대 20까지 소모하여, 소모한 [Breath] 1당 최대 체력의 1% 회복 (최소 1), 이 스킬 피해량 +1%\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [RyoshuEGOPF]이 999면, 기본 위력 <style="highlight">+2</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -3 (최대 -9)\n\n[EndSkill] [RyoshuEGOPF] <style="highlight">20</style> 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Breath], [RyoshuEGOPF], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Consume a maximum of 20 surplus [Breath] past 20 [Breath] on self, and for every [Breath] consumed, heal 1% of max HP (min 1 HP) and deal +1% damage with this Skill\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] At 999 [RyoshuEGOPF], Base Power <style="highlight">+2</style>\n[BeforeAttack] Base Power -3 for every Cracked Coin (max -9)\n\n[EndSkill] Gain <style="highlight">20</style> [RyoshuEGOPF]
   PL:
258. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2040921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2040921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2040921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2040921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttack] 마지막 코인 피해량 +30% (스킬 당 1회)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: <style="highlight">[CriticalOnSucceedAttack] Deal +30% damage with the final Coin (once per Skill)</style>
   PL:
264. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2040921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2040921].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 3 — opis] <style="highlight">[OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 위력) 10당 피해량 +1% (최대 30%)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 4 — opis] <style="highlight">[OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 횟수) 10당 최종 위력 +1 (최대 3)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Combustion], [Laceration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnStartCoin] Final Power +1 for every 10 ([Combustion] Count + [Laceration] Count) on all targets (max 3)</style>
   PL:
268. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 5 — opis] [OnStartCoin] 자신의 [RyoshuEGOPF]을 모두 소모하고, 소모한 수치 5당 피해량 +1% (최대 100%)\n<style="highlight">- 공격 대상이 1명이면, 이 효과가 1.5배로 적용됨 (집중 전투인 경우, 본체를 기준으로 판정)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#2].coindescs[#4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [OnStartCoin] Consume all [RyoshuEGOPF] on self and deal +1% damage for every 5 [RyoshuEGOPF] consumed (max 100%)\n<style="highlight">- When attacking just a single target, the damage modifying effect above is applied at 1.5x its value (in Focused Encounters, a Core and its connected Parts count as a single target)</style>
   PL:
269. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 5 — podsumowanie] [OnStartCoin] [RyoshuEGOPF]에 비례하여 피해량이 증가
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=3].coinlist[#2].coindescs[#4].summary ; dataList[id=2040921].levelList[level=4].coinlist[#2].coindescs[#4].summary
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 20을 초과하는 [Breath]을 최대 20까지 소모하여, 소모한 [Breath] 1당 최대 체력의 1% 회복 (최소 1), 이 스킬 피해량 +1%\n[BeforeAttack] 자신의 [Breath] 횟수 <style="highlight">5</style> 증가\n[BeforeAttack] 자신의 [RyoshuEGOPF]이 999면, 기본 위력 <style="highlight">+3</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -3 (최대 -9)\n\n[EndSkill] [RyoshuEGOPF] <style="highlight">33</style> 얻음
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Breath], [RyoshuEGOPF], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Consume a maximum of 20 surplus [Breath] past 20 [Breath] on self, and for every [Breath] consumed, heal 1% of max HP (min 1 HP) and deal +1% damage with this Skill\n[BeforeAttack] Gain <style="highlight">+5</style> [Breath] Count\n[BeforeAttack] At 999 [RyoshuEGOPF], Base Power <style="highlight">+3</style>\n[BeforeAttack] Base Power -3 for every Cracked Coin (max -9)\n\n[EndSkill] Gain <style="highlight">33</style> [RyoshuEGOPF]
   PL:
271. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] 마지막 코인 피해량 <style="highlight">+50%</style> (스킬 당 1회)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal <style="highlight">+50%</style> damage with the final Coin (once per Skill)
   PL:
273. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 위력) 10당 피해량 +1% <style="highlight">(최대 50%)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnStartCoin] (모든 대상의 [Combustion] + [Laceration] 횟수) 10당 최종 위력 +1 <style="highlight">(최대 5)</style>
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Combustion], [Laceration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [OnStartCoin] Final Power +1 for every 10 ([Combustion] Count + [Laceration] Count) on all targets <style="highlight">(max 5)</style>
   PL:
275. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 5 — opis] [OnStartCoin] 자신의 [RyoshuEGOPF]을 모두 소모하고, 소모한 수치 5당 피해량 <style="highlight">+1.25% (최대 248%)</style>\n- 공격 대상이 1명이면, 이 효과가 <style="highlight">2배</style>로 적용됨 (집중 전투인 경우, 본체를 기준으로 판정)
   źródło: Skills_Ego_Personality-04.json :: dataList[id=2040921].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnStartCoin], [RyoshuEGOPF]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [OnStartCoin] Consume all [RyoshuEGOPF] on self and deal <style="highlight">+1.25%</style> damage for every 5 [RyoshuEGOPF] consumed <style="highlight">(max 248%)</style>\n- When attacking just a single target, the damage modifying effect above is applied at <style="highlight">2x</style> its value (in Focused Encounters, a Core and its connected Parts count as a single target)
   PL:
276. [Pasywka E.G.O — nazwa] 삼도[三途]
   źródło: Passive_Ego.json :: dataList[id=2040911].name
   limit: do 40 znaków
   EN: Sanzu [三途]
   PL:
277. [Pasywka E.G.O — opis] 공격 스킬 종료 시 적이 흐트러짐 상태가 되었거나 사망했으면, 다음 턴에 [CriticalDamageUp] 1 얻음 (턴당 3회)
   źródło: Passive_Ego.json :: dataList[id=2040911].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [CriticalDamageUp]
   znaczenie tagów: [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up
   EN: After using an Attack Skill, if the enemy is Staggered or defeated, gain 1 [CriticalDamageUp] next turn (3 times per turn)
   PL:

## E.G.O [20501] Chains of Others (타인의 사슬) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20501`

278. [Karta E.G.O — nazwa] 타인의 사슬
   źródło: Egos-a1c9p3.json :: dataList[id=205011].name
   limit: do 40 znaków
   EN: Chains of Others
   PL:
279. [Karta E.G.O — opis] 뫼르소 연출 전용 EGO 장비
   źródło: Egos-a1c9p3.json :: dataList[id=205011].desc
   limit: do 120 znaków
   EN: Meursault's Battle Cinematic Exclusive E.G.O
   PL:
280. [Karta E.G.O — nazwa] 타인의 사슬
   źródło: Egos.json :: dataList[id=20501].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Karta E.G.O — opis] 뫼르소의 기본 EGO 장비
   źródło: Egos.json :: dataList[id=20501].desc
   limit: do 120 znaków
   EN: Meursault’s Base E.G.O
   PL:
282. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 타인의 사슬
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=1].name ; dataList[id=2050111].levelList[level=3].name ; dataList[id=2050111].levelList[level=4].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 뫼르소
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=1].abName ; dataList[id=2050111].levelList[level=3].abName ; dataList[id=2050111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Meursault
   PL:
284. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 3 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2050111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Gain 3 [Binding] next turn
   PL:
286. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 2 [Reduction] next turn
   PL:
287. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Gain 2 [Reduction] next turn
   PL:
288. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 5 부여
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 5 [Binding] next turn
   PL:
289. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 5 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Gain 5 [Binding] next turn
   PL:
290. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 4 부여
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2050111].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 4 [Reduction] next turn
   PL:
291. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 4 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Gain 4 [Reduction] next turn
   PL:
292. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttackHead] 다음 턴에 보호 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 2 Protection next turn
   PL:
293. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 3 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Gain 3 [Reduction] next turn
   PL:
294. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 다음 턴에 보호 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2050111].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Protection next turn
   PL:
295. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — nazwa] 타인의 사슬
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — źródło (Anomalia)] 뫼르소
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].abName
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 5 부여
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 5 [Binding] next turn
   PL:
298. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 얻음
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Gain 3 [Binding] next turn
   PL:
299. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 4 부여
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 4 [Reduction] next turn
   PL:
300. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 3 얻음
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Gain 3 [Reduction] next turn
   PL:
301. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 2 얻음
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2050112].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 2 [Protection] next turn
   PL:
302. [Pasywka E.G.O — nazwa] 판단 거부
   źródło: Passive_Ego.json :: dataList[id=2050111].name
   limit: do 40 znaków
   EN: Refusal to Judge
   PL:
303. [Pasywka E.G.O — opis] 전투 시작 시 자신이 3개 이상의 스킬의 타겟이 되었다면, 보호 3을 얻음
   źródło: Passive_Ego.json :: dataList[id=2050111].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Combat Start: Gain 3 [Protection] if this unit is targeted by 3 or more Skills
   PL:

## E.G.O [20502] Screwloose Wallop (나사빠진 일격) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20502`

304. [Karta E.G.O — nazwa] 나사빠진 일격
   źródło: Egos.json :: dataList[id=20502].name
   limit: do 40 znaków
   EN: Screwloose Wallop
   PL:
305. [Karta E.G.O — opis] 뫼르소 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20502].desc
   limit: do 120 znaków
   EN: Meursault’s E.G.O Gear
   PL:
306. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 나사빠진 일격
   źródło: Skills_Ego.json :: dataList[id=2050211].levelList[level=1].name ; dataList[id=2050211].levelList[level=3].name
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 너 맞아볼래? 매우?
   źródło: Skills_Ego.json :: dataList[id=2050211].levelList[level=1].abName ; dataList[id=2050211].levelList[level=3].abName
   limit: do 50 znaków
   EN: You Want To Get Beat? Hurtily?
   PL:
308. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 보호 3 얻음
   źródło: Skills_Ego.json :: dataList[id=2050211].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Gain 3 Protection
   PL:
309. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 3 부여
   źródło: Skills_Ego.json :: dataList[id=2050211].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050211].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 3 [Paralysis]
   PL:
310. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 보호 3 얻음\n[EndSkill] 다음 턴에 시술 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2050211].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Gain 3 Protection\n[EndSkill] Gain 1 Surgery next turn
   PL:
311. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 나사빠진 일격
   źródło: Skills_Ego.json :: dataList[id=2050221].levelList[level=1].name ; dataList[id=2050221].levelList[level=3].name
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 너 맞아볼래? 매우?
   źródło: Skills_Ego.json :: dataList[id=2050221].levelList[level=1].abName ; dataList[id=2050221].levelList[level=3].abName
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [EndSkill] 다음 턴에 시술 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2050221].levelList[level=1].desc ; dataList[id=2050221].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Gain 2 Surgery next turn
   PL:
314. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 3 부여
   źródło: Skills_Ego.json :: dataList[id=2050221].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050221].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량의 30%만큼 흐트러짐 손상 입힘
   źródło: Skills_Ego.json :: dataList[id=2050221].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Raise Stagger Threshold by 30% of damage dealt
   PL:
316. [Pasywka E.G.O — nazwa] 마지막 개조
   źródło: Passive_Ego.json :: dataList[id=2050211].name
   limit: do 40 znaków
   EN: Final Augment
   PL:
317. [Pasywka E.G.O — opis] 체력이 25%미만일 때 <나사빠진 일격> E.G.O 스킬 사용시 매 턴마다 공격 위력 증가, 수비 위력 증가, 신속 3을 얻고, 3턴 뒤 사망함.
   źródło: Passive_Ego.json :: dataList[id=2050211].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Endurance], [Agility]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up; [Agility] = 신속 / Haste
   EN: If the E.G.O Skill <Screwloose Wallop> is used when this unit is at less than 25% HP, this unit gains 3 [Enhancement], [Endurance], and [Agility] every turn, but dies in 3 turns
   PL:

## E.G.O [20503] Pursuance (집행) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20503`

318. [Karta E.G.O — nazwa] 집행
   źródło: Egos.json :: dataList[id=20503].name
   limit: do 40 znaków
   EN: Pursuance
   PL:
319. [Karta E.G.O — opis] 뫼르소 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20503].desc
   (powtórzenie elementu 305 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 집행
   źródło: Skills_Ego.json :: dataList[id=2050311].levelList[level=1].name ; dataList[id=2050311].levelList[level=3].name
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 하늘 집행관의 보좌
   źródło: Skills_Ego.json :: dataList[id=2050311].levelList[level=1].abName ; dataList[id=2050311].levelList[level=3].abName
   limit: do 40 znaków
   EN: Heavenly Executor’s Scribe
   PL:
322. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 자신을 제외하고 현재 체력이 가장 낮은 아군 2명 최대 체력의 15%만큼 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2050311].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 2 other allies with the least HP for 15% of Max HP
   PL:
323. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2050311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackHead] Trigger [VibrationExplosion]
   PL:
324. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 자신을 제외하고 현재 체력이 가장 낮은 아군 2명 최대 체력의 30%만큼 체력을 회복, 다음 턴에 보호 2 부여
   źródło: Skills_Ego.json :: dataList[id=2050311].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 2 other allies with the least HP for 30% of Max HP; Apply 2 Protection next turn
   PL:
325. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2050311].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
326. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 집행
   źródło: Skills_Ego.json :: dataList[id=2050321].levelList[level=1].name ; dataList[id=2050321].levelList[level=3].name
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 하늘 집행관의 보좌
   źródło: Skills_Ego.json :: dataList[id=2050321].levelList[level=1].abName ; dataList[id=2050321].levelList[level=3].abName
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신을 제외하고 현재 체력이 가장 낮은 아군 2명에게 다음 턴에 취약 1 부여, 다음 턴에 피해량 증가 2 부여
   źródło: Skills_Ego.json :: dataList[id=2050321].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantIdentify] Targets randomly\n[EndSkill] Apply 1 [Vulnerable] and 2 [AttackDmgUp] next turn to 2 other allies with the least HP
   PL:
329. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2050321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신을 제외하고 현재 체력이 가장 낮은 아군 2명에게 다음 턴에 취약 2 부여, 다음 턴에 피해량 증가 3 부여
   źródło: Skills_Ego.json :: dataList[id=2050321].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantIdentify] Targets randomly\n[EndSkill] Apply 2 [Vulnerable] and 3 [AttackDmgUp] next turn to 2 other allies with the least HP
   PL:
331. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2050321].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Pasywka E.G.O — nazwa] 하늘의 계시
   źródło: Passive_Ego.json :: dataList[id=2050311].name
   limit: do 40 znaków
   EN: Revelation from Above
   PL:
333. [Pasywka E.G.O — opis] 조작 패널에서 가장 왼쪽의 스킬로 합 승리 시 다음 턴에 무작위 아군에게 공격 위력 증가 또는 수비 위력 증가 1 부여
   źródło: Passive_Ego.json :: dataList[id=2050311].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Endurance]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: After winning a Clash with the leftmost Skill on the Dashboard, apply 1 [Enhancement] or [Endurance] to a random ally next turn
   PL:

## E.G.O [20504] Capote (카포테) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20504`

334. [Karta E.G.O — nazwa] 카포테
   źródło: Egos.json :: dataList[id=20504].name
   limit: do 40 znaków
   EN: Capote
   PL:
335. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20504].desc
   limit: do 120 znaków
   EN: Meursault’s E.G.O Gear
   PL:
336. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 카포테
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=1].name ; dataList[id=2050411].levelList[level=3].name ; dataList[id=2050411].levelList[level=4].name
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 놋쇠 황소
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=1].abName ; dataList[id=2050411].levelList[level=3].abName ; dataList[id=2050411].levelList[level=4].abName
   limit: do 40 znaków
   EN: Brazen Bull
   PL:
338. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 다음 턴에 신속 1, 분노 위력 증가 1, 타격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Agility]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste
   EN: [EndSkill] Gain 1 [Agility], 1 Wrath Power Up, and 1 Blunt Power Up next turn
   PL:
339. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 화상 수치만큼 진동 부여
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2050411].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Vibration] by [Combustion] on target
   PL:
341. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 3 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 적 5명의 화상 횟수 1 증가
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 3; if the [VibrationExplosion] Staggered the target, inflict +1 [Combustion] Count on 5 random enemies
   PL:
342. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] [EndSkill] 다음 턴에 신속 2, 분노 위력 증가 1, 타격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=3].desc ; dataList[id=2050411].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Agility]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste
   EN: [EndSkill] Gain 2 [Agility], 1 Wrath Power Up, and 1 Blunt Power Up next turn
   PL:
343. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 7 부여
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 7 [Combustion]
   PL:
344. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 무작위 적 5명에게 화상 2 부여
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] on 5 random enemies
   PL:
345. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 2 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 적 5명의 화상 횟수 2 증가
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 2; if the [VibrationExplosion] Staggered the target, inflict +2 [Combustion] Count on 5 random enemies
   PL:
346. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 10 부여
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion]
   PL:
347. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 무작위 적 5명에게 화상 3 부여
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] on 5 random enemies
   PL:
348. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 2 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 적 5명의 화상 횟수 3 증가
   źródło: Skills_Ego.json :: dataList[id=2050411].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 2; if the [VibrationExplosion] Staggered the target, inflict +3 [Combustion] Count on 5 random enemies
   PL:
349. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 카포테
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=1].name ; dataList[id=2050421].levelList[level=3].name ; dataList[id=2050421].levelList[level=4].name
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 놋쇠 황소
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=1].abName ; dataList[id=2050421].levelList[level=3].abName ; dataList[id=2050421].levelList[level=4].abName
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 다음 턴에 신속 1, 분노 위력 증가 1, 타격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Gain 1 [Agility], 1 Wrath Power Up, and 1 Blunt Power Up next turn
   PL:
352. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 6 부여
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 화상 수치만큼 진동 부여
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2050421].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 3 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 캐릭터 5명의 화상 횟수 2 증가
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 3; if the [VibrationExplosion] Staggered the target, inflict +2 [Combustion] Count on 5 random units
   PL:
355. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 다음 턴에 신속 2, 분노 위력 증가 1, 타격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=3].desc ; dataList[id=2050421].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Gain 2 [Agility], 1 Wrath Power Up, and 1 Blunt Power Up next turn
   PL:
356. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 10 부여
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 무작위 캐릭터 5명에게 화상 2 부여
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] on 5 random units
   PL:
358. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 2 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 캐릭터 5명의 화상 횟수 3 증가
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 2; if the [VibrationExplosion] Staggered the target, inflict +3 [Combustion] Count on 5 random units
   PL:
359. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 12 부여
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 12 [Combustion]
   PL:
360. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 무작위 캐릭터 5명에게 화상 3 부여
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] on 5 random units
   PL:
361. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 2 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 캐릭터 5명의 화상 횟수 4 증가
   źródło: Skills_Ego.json :: dataList[id=2050421].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 2; if the [VibrationExplosion] Staggered the target, inflict +4 [Combustion] Count on 5 random units
   PL:
362. [Pasywka E.G.O — nazwa] 삭히지 못한 흥분
   źródło: Passive_Ego.json :: dataList[id=2050411].name
   limit: do 40 znaków
   EN: Untempered Agitation
   PL:
363. [Pasywka E.G.O — opis] 전투 시작 시 자신이 2개 이상의 스킬의 타겟이 되었다면, 스킬 기본 위력이 1 증가하고, 피격 시 공격자에게 화상 1 부여 (턴 당 최대 5회)
   źródło: Passive_Ego.json :: dataList[id=2050411].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Combat Start: If this unit is targeted by 2 or more Skills, this unit’s Skills gain +1 Base Power; when hit, inflict 1 [Combustion] on the attacker (5 times per turn)
   PL:

## E.G.O [20505] Regret (후회) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20505`

364. [Karta E.G.O — nazwa] 후회
   źródło: Egos.json :: dataList[id=20505].name
   limit: do 40 znaków
   EN: Regret
   PL:
365. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20505].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 후회
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=1].name ; dataList[id=2050511].levelList[level=3].name ; dataList[id=2050511].levelList[level=4].name
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 버려진 살인마
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=1].abName ; dataList[id=2050511].levelList[level=3].abName ; dataList[id=2050511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Forsaken Murderer
   PL:
368. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — opis] [BeforeAttack] 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 1개 제거
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=1].desc ; dataList[id=2050511].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] Remove 1 random removable negative effect applied to self
   PL:
369. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가, (분노 완전 공명 수)/3만큼 추가 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050511].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count; Inflict (Wrath A-Reson. /3) additional [Vibration] Count
   PL:
370. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 대상에게 흐트러짐 구간이 없는 경우,\n최종 흐트러짐 손상의 (6 + 2x(분노 완전 공명 수))%만큼 분노 피해를 줌
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nIf target does not have a Stagger Threshold upon [VibrationExplosion],\nDeal Wrath Damage by (6 + 2x(Wrath A-Reson.))% of the final Stagger Threshold raised
   PL:
372. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 2개 제거
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] Remove 2 random removable negative effects applied to self
   PL:
373. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가, (분노 완전 공명 수)/3만큼 추가 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count; Inflict (Wrath A-Reson. /3) additional [Vibration] Count
   PL:
374. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 대상에게 흐트러짐 구간이 없는 경우,\n최종 흐트러짐 손상의 (12 + 3x(분노 완전 공명 수))%만큼 분노 피해를 줌.
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nIf target does not have a Stagger Threshold upon [VibrationExplosion],\nDeal Wrath Damage by (12 + 3x(Wrath A-Reson.))% of the final Stagger Threshold raised.
   PL:
375. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 후회
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=1].name ; dataList[id=2050521].levelList[level=3].name ; dataList[id=2050521].levelList[level=4].name
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 버려진 살인마
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=1].abName ; dataList[id=2050521].levelList[level=3].abName ; dataList[id=2050521].levelList[level=4].abName
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신에게 부정적인 효과가 부여되어 있으면 공격 가중치 +1
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=1].desc ; dataList[id=2050521].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] If this unit has a negative status effect, Atk Weight +1
   PL:
378. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발.\n진동 폭발 시 진동 수치의 30%만큼 흐트러짐 손상 증가.\n진동 횟수 1 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion].\nAmount of Stagger Threshold raised by [VibrationExplosion] increases by 30% of [Vibration] on target.\nReduce [Vibration] Count by 1
   PL:
379. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [EndSkill] 다음 턴에 속박 3, 타격 위력 증가 1을 얻음.
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2050521].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Binding], [HitResultUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: [EndSkill] Gain 3 [Binding] and 1 [HitResultUp] next turn.
   PL:
380. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발.\n진동 폭발 시 진동 수치의 40%만큼 흐트러짐 손상 증가.\n진동 폭발 시 대상에게 흐트러짐 구간이 없는 경우,\n최종 흐트러짐 손상의 (6 + 2x(분노 완전 공명 수))%만큼 분노 피해를 줌.\n진동 횟수 1 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nAmount of Stagger Threshold raised by [VibrationExplosion] increases by 40% of [Vibration] on target.\nIf target does not have a Stagger Threshold upon [VibrationExplosion],\nDeal Wrath Damage by (6 + 2x(Wrath A-Reson.))% of the final Stagger Threshold raised\nReduce [Vibration] Count by 1
   PL:
381. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신에게 부정적인 효과가 부여되어 있으면 공격 가중치 +2
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] If this unit has a negative status effect, Atk Weight +2
   PL:
382. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발.\n진동 폭발 시 진동 수치의 50%만큼 흐트러짐 손상 증가.\n진동 폭발 시 대상에게 흐트러짐 구간이 없는 경우,\n최종 흐트러짐 손상의 (12 + 3x(분노 완전 공명 수))%만큼 분노 피해를 줌.\n진동 횟수 1 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nAmount of Stagger Threshold raised by [VibrationExplosion] increases by 50% of [Vibration] on target.\nIf target does not have a Stagger Threshold upon [VibrationExplosion],\nDeal Wrath Damage by (12 + 3x(Wrath A-Reson.))% of the final Stagger Threshold raised\nReduce [Vibration] Count by 1
   PL:
383. [Pasywka E.G.O — nazwa] 구속당한 분노
   źródło: Passive_Ego.json :: dataList[id=2050511].name
   limit: do 40 znaków
   EN: Bound Wrath
   PL:
384. [Pasywka E.G.O — opis] 자신의 조작 패널에서 가장 왼쪽에 위치한 스킬의 기본 위력 1 감소. 코인 위력 2 증가\n턴 시작 시 속도가 4 이하면, 타격 위력 증가 1을 얻음.
   źródło: Passive_Ego.json :: dataList[id=2050511].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [HitResultUp]
   znaczenie tagów: [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: Base Power -1 and Coin Power +2 to the leftmost Skill on this unit's Dashboard\nTurn Start: At 4- Speed, Gain 1 [HitResultUp]
   PL:

## E.G.O [20506] Electric Screaming (전기울음) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20506`

385. [Karta E.G.O — nazwa] 전기울음
   źródło: Egos.json :: dataList[id=20506].name
   limit: do 40 znaków
   EN: Electric Screaming
   PL:
386. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20506].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 전기울음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050611].levelList[level=1].name ; dataList[id=2050611].levelList[level=3].name ; dataList[id=2050611].levelList[level=4].name
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 꿈꾸는 전기양
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050611].levelList[level=1].abName ; dataList[id=2050611].levelList[level=3].abName ; dataList[id=2050611].levelList[level=4].abName
   limit: do 40 znaków
   EN: Dreaming Electric Sheep
   PL:
389. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 자신의 [Charge] 횟수 8 증가\n[EndSkill] 자신을 제외하고 [Charge] 횟수가 가장 낮은 아군 1명의 [Charge] 횟수 8 증가\n- (최대 질투 공명 수 - 2)만큼 부여 대상 수 증가 (최대 3)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050611].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain +8 [Charge] Count\n[EndSkill] Apply +8 [Charge] Count to 1 other ally that has the least [Charge] Count\n- Number of affected allies grows by (highest Envy Reson. - 2) (max 3)
   PL:
390. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050611].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050611].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
391. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신의 [Charge] 횟수 8 증가\n[EndSkill] 자신을 제외하고 [Charge] 횟수가 가장 낮은 아군 1명의 [Charge] 횟수 8 증가\n- (최대 질투 공명 수 - 2)만큼 부여 대상 수 증가 (최대 4)\n- 최대 질투 공명 수가 4 이상이면, 자신과 부여 대상에게 [VioletDamageUp] 1 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050611].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [EndSkill], [VioletDamageUp]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: [BeforeAttack] Gain +8 [Charge] Count\n[EndSkill] Apply +8 [Charge] Count to 1 other ally that has the least [Charge] Count\n- Number of affected allies grows by (highest Envy Reson. - 2) (max 4)\n- At 4+ (highest Envy Reson.), apply 1 [VioletDamageUp] to self and all affected allies
   PL:
392. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신의 [Charge] 횟수 12 증가\n[EndSkill] 자신을 제외하고 [Charge] 횟수가 가장 낮은 아군 1명의 [Charge] 횟수 8 증가\n- (최대 질투 공명 수 - 2)만큼 부여 대상 수 증가 (최대 <style="highlight">5</style>)\n- 최대 질투 공명 수가 4 이상이면, 자신과 부여 대상에게 [VioletDamageUp] 1 부여\n<style="highlight">- 최대 질투 공명 수가 6 이상이면, 자신과 부여 대상에게 [VioletDamageUp] 1 부여</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050611].levelList[level=4].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Charge], [EndSkill], [VioletDamageUp]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: [BeforeAttack] Gain +12 [Charge] Count\n[EndSkill] Apply +8 [Charge] Count to 1 other ally that has the least [Charge] Count\n- Number of affected allies grows by (highest Envy Reson. - 2) (max <style="highlight">5</style>)\n- At 4+ (highest Envy Reson.), apply 1 [VioletDamageUp] to self and all affected allies\n<style="highlight">- At 6+ (highest Envy Reson.), apply 1 [VioletDamageUp] to self and all affected allies</style>
   PL:
393. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 전기울음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=1].name ; dataList[id=2050621].levelList[level=3].name ; dataList[id=2050621].levelList[level=4].name
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 꿈꾸는 전기양
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=1].abName ; dataList[id=2050621].levelList[level=3].abName ; dataList[id=2050621].levelList[level=4].abName
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 질투 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)\n[BeforeAttack] 자신의 [Charge] 횟수가 10이상이면, [Charge] 횟수를 최대 20 소모하여 소모한 [Charge] 횟수 1 당 피해량 +2% (최대 40%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain Atk Weight equal to (highest Envy Reson. - 2) (max 2)\n[BeforeAttack] If this unit has 10+ [Charge] Count, spend up to 20 [Charge] Count; deal +2% damage for every [Charge] Count consumed (max 40%)
   PL:
396. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 1 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050621].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis]
   PL:
397. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2050621].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 질투 공명 수 - 2)만큼 공격 가중치 증가 (최대 <style="highlight">3</style>)\n[BeforeAttack] 자신의 [Charge] 횟수가 10이상이면, [Charge] 횟수를 최대 20 소모하여 소모한 [Charge] 횟수 1 당 피해량 +<style="highlight">2.5</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=3].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain Atk Weight equal to (highest Envy Reson. - 2) (max <style="highlight">3</style>)\n[BeforeAttack] If this unit has 10+ [Charge] Count, spend up to 20 [Charge] Count; deal +<style="highlight">2.5</style>% damage for every [Charge] Count consumed (max <style="highlight">50</style>%)
   PL:
399. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 질투 공명 수 - 2)만큼 공격 가중치 증가 (최대 3)\n<style="highlight">[BeforeAttack] 자신의 충전 횟수가 10 이상이면, 적중시 효과로 부여하는 효과가 2회 부여됨</style>\n[BeforeAttack] 자신의 [Charge] 횟수가 10이상이면, [Charge] 횟수를 최대 20 소모하여 소모한 [Charge] 횟수 1 당 피해량 +<style="highlight">3</style>% (최대 <style="highlight">60</style>%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050621].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain Atk Weight equal to (highest Envy Reson. - 2) (max 3)\n<style="highlight">[BeforeAttack] At 10+ [Charge] Count, apply the effects applied from 'On Hit' twice</style>\n[BeforeAttack] If this unit has 10+ [Charge] Count, spend up to 20 [Charge] Count; deal +<style="highlight">3</style>% damage for every [Charge] Count consumed (max <style="highlight">60</style>%)
   PL:
400. [Pasywka E.G.O — nazwa] 과부하 케이블
   źródło: Passive_Ego.json :: dataList[id=2050611].name
   limit: do 40 znaków
   EN: Overloading Cables
   PL:
401. [Pasywka E.G.O — opis] 전투 시작 시 공명이 4 이상 발동하였다면, [AttackUp] 2, [DefenseUp] 2 얻음.\n해당 공명이 질투 공명이었다면, 자신의 조작 패널 양 옆 아군에게도 부여
   źródło: Passive_Ego.json :: dataList[id=2050611].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: At 4+ Reson., gain 2 [AttackUp] and 2 [DefenseUp].\nIf the Reson. was an Envy Reson., apply the above effects to the 2 units adjacent to this unit on the Dashboard as well
   PL:

## E.G.O [20507] Yearning-Mircalla (갈망-미르칼라) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20507`

402. [Karta E.G.O — nazwa] 갈망-미르칼라
   źródło: Egos.json :: dataList[id=20507].name
   limit: do 40 znaków
   EN: Yearning-Mircalla
   PL:
403. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20507].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 갈망 - 미르칼라
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].name ; dataList[id=2050711].levelList[level=3].name ; dataList[id=2050711].levelList[level=4].name
   limit: do 40 znaków
   EN: Yearning - Mircalla
   PL:
405. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 사백송이의 장미
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].abName ; dataList[id=2050711].levelList[level=3].abName ; dataList[id=2050711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Four-hundred Roses
   PL:
406. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] For 3 turns, lose 10 SP at Turn End
   PL:
407. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2050711].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2050711].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 2 — opis] [WinDuelAttack] [RoseWedge] 횟수 2 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [RoseWedge]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: [WinDuelAttack] Inflict +2 [RoseWedge] Count
   PL:
411. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [RoseWedge] 횟수 1 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RoseWedge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: [OnSucceedAttack] Inflict +1 [RoseWedge] Count
   PL:
412. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=2050711].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=2050711].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 2 — opis] [WinDuelAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Activate [Laceration] on target once (target loses 1 [Laceration] Count)
   PL:
414. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL:
415. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050711].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 최대 공명이 4 이상이면, 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] At 4+ highest Reson., activate [Laceration] on target once (target loses 1 [Laceration] Count)</style>
   PL:
417. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2050711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 최대 공명이 4 이상이면, 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [WinDuelAttack] [RoseWedge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2050711].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [RoseWedge]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: [WinDuelAttack] Inflict +2 [RoseWedge] Count<style="highlight"></style>
   PL:
420. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [RoseWedge] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RoseWedge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: [OnSucceedAttack] Inflict +1 [RoseWedge] Count<style="highlight"></style>
   PL:
421. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 4, efekt 2 — opis] [WinDuelAttack] 대상의 [Laceration] <style="highlight">1 + (최대 공명 수 / 2)회 발동. (최대 3회. 발동된 횟수만큼 [Laceration] 횟수 감소)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Activate the target's [Laceration] <style="highlight">(1 + (highest Reson./2)) times. (3 times max; target loses [Laceration] Count equal to the number of times it was activated)
   PL:
422. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 [Laceration] <style="highlight">6 당 코인 위력 +1 (최대 2)</style>\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL:
423. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 최대 공명이 4 이상이면, 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] At 4+ highest Reson., activate [Laceration] on target once (target loses 1 [Laceration] Count)<style="highlight"></style>
   PL:
424. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 최대 공명이 4 이상이면, 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [RoseWedge] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RoseWedge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [RoseWedge] Count
   PL:
426. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 4, efekt 2 — opis] [WinDuelAttack] 대상의 [Laceration] 1 + (최대 공명 수 / 2)회 발동. (최대 3회. 발동된 횟수만큼 [Laceration] 횟수 감소)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Activate the target's [Laceration] (1 + (highest Reson./2)) times. (3 times max; target loses [Laceration] Count equal to the number of times it was activated)<style="highlight"></style>
   PL:
427. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 4, efekt 3 — opis] <style="highlight">[EnemyKill] 적의 남은 체력을 초과하여 피해를 준 경우, 초과한 피해량을 고정 피해로 적 전체에 나눠서 가함. (최소 1)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050711].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: <style="highlight">[EnemyKill] When dealing excess damage past the enemy's remaining HP, deal the excess damage as fixed damage between all enemies. (min 1)</style>
   PL:
428. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 갈망 - 미르칼라
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].name ; dataList[id=2050721].levelList[level=3].name ; dataList[id=2050721].levelList[level=4].name
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 사백송이의 장미
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].abName ; dataList[id=2050721].levelList[level=3].abName ; dataList[id=2050721].levelList[level=4].abName
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] 자신의 최대 체력의 10% 만큼 소모하여, 모든 적과 아군이 (자신이 소모한 체력 / 2)만큼 피해를 받음\n- 자신의 현재 체력이 최대 체력의 50% 미만이면, 대신 모든 아군에게 [Laceration]을 5 부여하고 1회 발동시킴 ([Laceration] 횟수 1 감소). 아군이 입은 [Laceration] 피해만큼 자신의 체력을 회복
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [Laceration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] Consume up to 10% of this unit's max HP and deal (HP consumed / 2) damage to all enemies and allies\n- At less than 50% of this unit's max HP, inflict and activate 5 [Laceration] on all allies once instead (lose 1 [Laceration] Count). Heal HP equal to the amount of [Laceration] damage dealt to allies
   PL:
431. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신과 대상에게 [Laceration] 2 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] on self and the target
   PL:
432. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신과 대상에게 [Laceration] 2 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2050721].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2050721].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 2 — opis] [WinDuelAttack] [RoseWedge] 횟수 2 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [RoseWedge] 횟수 1 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 4 — opis] - 대상에게 [RoseWedge]가 없었으면, [RoseWedge] 위력이 추가로 4 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RoseWedge]
   znaczenie tagów: [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: - If target did not have [RoseWedge], inflict 4 additional [RoseWedge] Potency
   PL:
437. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=2050721].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=2050721].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 4, efekt 2 — opis] [WinDuelAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">자신과 대상의 [Laceration] 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 최대 체력의 10% 만큼 소모하여, 모든 적과 아군이 (자신이 소모한 체력 / 2) 만큼 피해를 받음\n- 자신의 현재 체력이 최대 체력의 50% 미만이면, 대신 모든 아군에게 [Laceration]을 5 부여하고 1회 발동시킴 ([Laceration] 횟수 1 감소). 아군이 입은 [Laceration] 피해만큼 자신의 체력을 회복
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Laceration], [WhenUse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">At 6+ ([Laceration] on self + [Laceration] on target), Coin Power +1</style>\n[WhenUse] Consume up to 10% of this unit's max HP and deal (HP consumed / 2) damage to all enemies and allies\n- At less than 50% of this unit's max HP, inflict and activate 5 [Laceration] on all allies once instead (lose 1 [Laceration] Count). Heal HP equal to the amount of [Laceration] damage dealt to allies
   PL:
440. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신과 대상에게 [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration] on self and the target
   PL:
441. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신과 대상에게 [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [WinDuelAttack] [RoseWedge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2050721].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [RoseWedge] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] - 대상에게 [RoseWedge]가 없었으면, [RoseWedge] 위력이 추가로 4 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=2050721].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [RoseWedge]
   znaczenie tagów: [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: - If target did not have [RoseWedge], inflict 4 additional [RoseWedge] Potency<style="highlight"></style>
   PL:
445. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 4, efekt 2 — opis] [WinDuelAttack] 대상의 [Laceration] <style="highlight">1 + (최대 공명 수 /2)회 발동. (최대 3회, 발동된 횟수만큼 [Laceration] 횟수 감소)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Activate the target's [Laceration] <style="highlight">(1 + (highest Reson./2)) times. (3 times max; target loses [Laceration] Count equal to the number of times it was activated)</style>
   PL:
446. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n자신과 대상의 [Laceration] 합 6 당 코인 위력 +1 <style="highlight">(최대 3)</style>\n[WhenUse] 자신의 최대 체력의 10% 만큼 소모하여, 모든 적과 아군이 (자신이 소모한 체력 / 2) 만큼 피해를 받음\n- 자신의 현재 체력이 최대 체력의 50% 미만이면, 대신 모든 아군에게 [Laceration]을 5 부여하고 1회 발동시킴 ([Laceration] 횟수 1 감소). 아군이 입은 [Laceration] 피해만큼 자신의 체력을 회복
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Laceration], [WhenUse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: [CantIdentify]\nTargets randomly\nCoin Power +1 for every 6 ([Laceration] on self + [Laceration] on target) <style="highlight">(max 3)</style>\n[WhenUse] Consume up to 10% of this unit's max HP and deal (HP consumed / 2) damage to all enemies and allies\n- At less than 50% of this unit's max HP, inflict and activate 5 [Laceration] on all allies instead (lose 1 [Laceration] Count). Heal HP equal to the amount of [Laceration] damage dealt to allies
   PL:
447. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신과 대상에게 [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] on self and the target<style="highlight"></style>
   PL:
448. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신과 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Activate [Laceration] on self and the target once (both lose 1 [Laceration] Count)</style>
   PL:
449. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신과 대상에게 [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신과 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [RoseWedge] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 4, efekt 2 — opis] [WinDuelAttack] 대상의 [Laceration] 1 + (최대 공명 수 /2)회 발동. (최대 3회, 발동된 횟수만큼 [Laceration] 횟수 감소)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Activate the target's [Laceration] (1 + (highest Reson./2)) times. (3 times max; target loses [Laceration] Count equal to the number of times it was activated)<style="highlight"></style>
   PL:
453. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 4, efekt 3 — opis] <style="highlight">[EnemyKill] 적의 남은 체력을 초과하여 피해를 준 경우, 초과한 피해량을 고정 피해로 적 전체에 나눠서 가함. (최소 1)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050721].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Pasywka E.G.O — nazwa] 잔혹한 만찬
   źródło: Passive_Ego.json :: dataList[id=2050711].name
   limit: do 40 znaków
   EN: Bloodthirsty Banquet
   PL:
455. [Pasywka E.G.O — opis] 자신이 [Laceration] 피해를 가하거나 받을 때, [Laceration] 피해만큼 자신의 체력을 회복 (턴 당 최대 10)\n- [Laceration]을 부여하는 스킬, 코인 효과 발동 시, 대상에게 [RoseWedge]가 있으면 대상에게 [Laceration] 1 부여. (턴 당 2회)
   źródło: Passive_Ego.json :: dataList[id=2050711].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [RoseWedge]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [RoseWedge] = 장미 쐐기 / Rose Wedge
   EN: When this unit deals or takes [Laceration] damage, heal HP equal to the [Laceration] damage (max 10 per turn)\n- When activating a Skill/Coin effect that inflicts [Laceration], if the target has [RoseWedge], inflict 1 [Laceration] against the target. (2 times per turn)
   PL:

## E.G.O [20508] Crushbound Past (분쇄될 과거) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20508`

456. [Karta E.G.O — nazwa] 분쇄될 과거
   źródło: Egos.json :: dataList[id=20508].name
   limit: do 40 znaków
   EN: Crushbound Past
   PL:
457. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20508].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 분쇄될 과거
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].name ; dataList[id=2050811].levelList[level=3].name ; dataList[id=2050811].levelList[level=4].name
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 증기 운반 기계
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].abName ; dataList[id=2050811].levelList[level=3].abName ; dataList[id=2050811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Steam Transport Machine
   PL:
460. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소\n[EndSkill] 홀수 턴에 (나태 공명 수)가 홀수거나, 짝수 턴에 (나태 공명 수)가 짝수면 정신력 10 회복
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] For 3 turns, lose 10 SP at Turn End\n[EndSkill] When activating odd-numbered (Sloth Reson.) in odd-numbered turns, or when activating even-numbered (Sloth Reson.) in even-numbered turns, heal 10 SP
   PL:
461. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
462. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] (나태 공명 수 / 2) 만큼 [Vibration] 횟수 증가 (최대 3)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +(Sloth Reson. / 2) [Vibration] Count (max 3)
   PL:
463. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 메인 타겟이면, 대상의 현재 [Vibration]으로 [FusionVibration]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [FusionVibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [OnSucceedAttack] If it's the main target, trigger [FusionVibration] into the target's current [Vibration] type
   PL:
464. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL:
465. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnStartCoin] 메인 타겟의 [Vibration] 1당, 이 코인의 피해량 +1% (최대 50%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] This Coin deals +1% damage for every [Vibration] on the main target (max 50%)
   PL:
466. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnStartCoin] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수) 1당, 이 코인의 피해량 +1% (최대 100%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] This Coin deals +1% damage for every ([Vibration] + [Vibration] Count) on the main target (max 100%)
   PL:
467. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
468. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 이 코인의 효과로 인한 피해량 증가량이 100% 이상이면, [VibrationExplosion] 2회. [Vibration] 횟수 2 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this Coin's effects raised the damage dealt by +100% or more, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL:
469. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">[BeforeAttack] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수)가 30 이상이면, 가중치 +1</style>\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소\n[EndSkill] 홀수 턴에 (나태 공명 수)가 홀수거나, 짝수 턴에 (나태 공명 수)가 짝수면 정신력 10 회복
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Vibration], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">[BeforeAttack] If the main target has 30+ ([Vibration] + [Vibration] Count), gain +1 Atk Weight</style>\n[EndSkill] For 3 turns, lose 10 SP at Turn End\n[EndSkill] When activating odd-numbered (Sloth Reson.) in odd-numbered turns, or when activating even-numbered (Sloth Reson.) in even-numbered turns, heal 10 SP
   PL:
470. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count<style="highlight"></style>
   PL:
471. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] (나태 공명 수 / 2) 만큼 [Vibration] 횟수 증가 (최대 3)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050811].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +(Sloth Reson. / 2) [Vibration] Count (max 3)<style="highlight"></style>
   PL:
472. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 메인 타겟이면, 대상의 현재 [Vibration]으로 [FusionVibration]<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2050811].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [FusionVibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [OnSucceedAttack] If it's the main target, trigger [FusionVibration] into the target's current [Vibration] type<style="highlight"></style>
   PL:
473. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2050811].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]<style="highlight"></style>
   PL:
474. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnStartCoin] 메인 타겟의 [Vibration] 1당, 이 코인의 피해량 +1% (최대 50%)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2050811].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] This Coin deals +1% damage for every [Vibration] on the main target (max 50%)<style="highlight"></style>
   PL:
475. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnStartCoin] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수) 1당, 이 코인의 피해량 +1% (최대 100%)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=2050811].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] This Coin deals +1% damage for every ([Vibration] + [Vibration] Count) on the main target (max 100%)<style="highlight"></style>
   PL:
476. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=2050811].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
477. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 이 코인의 효과로 인한 피해량 증가량이 100% 이상이면, [VibrationExplosion] 2회. [Vibration] 횟수 2 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this Coin's effects raised the damage dealt by +100% or more, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2<style="highlight"></style>
   PL:
478. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수)가 30 이상이면, 가중치 +1\n<style="highlight">- 100 이상이면, 대신 가중치 +3</style>\n<style="highlight">[BeforeAttack] 최대 공명 수 2 당, 공격하는 모든 대상에게 진동 1 부여 (최대 3)</style>\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소\n<style="highlight">[EndSkill] 자신의 최대 체력의 ([AccumulatedPastSinner] x 2)% 만큼 체력 회복</style>\n[EndSkill] 홀수 턴에 (나태 공명 수)가 홀수거나, 짝수 턴에 (나태 공명 수)가 짝수면 정신력 10 회복
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=4].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Vibration], [EndSkill], [AccumulatedPastSinner]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]; [AccumulatedPastSinner] = 축적된 과거 / Accumulated Past
   EN: [BeforeAttack] If the main target has 30+ ([Vibration] + [Vibration] Count), gain +1 Atk Weight\n<style="highlight">- At 100+, gain +3 Atk Weight instead</style>\n<style="highlight">[BeforeAttack] For every 2 highest Reson., inflict 1 [Vibration] against all targets this unit attacks (max 3)</style>\n[EndSkill] For 3 turns, lose 10 SP at Turn End\n<style="highlight">[EndSkill] Heal ([AccumulatedPastSinner] x 2)% HP</style>\n[EndSkill] When activating odd-numbered (Sloth Reson.) in odd-numbered turns, or when activating even-numbered (Sloth Reson.) in even-numbered turns, heal 10 SP
   PL:
479. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 4, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 이 코인의 효과로 인한 피해량 증가량이 50% 이상이면, [VibrationExplosion] 1회.</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Coin's effects raised the damage dealt by +50% or more, trigger [VibrationExplosion] once.</style>
   PL:
480. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 4, efekt 4 — opis] [OnSucceedAttack] 이 코인의 효과로 인한 피해량 증가량이 100% 이상이면, [VibrationExplosion] 2회. [Vibration] 횟수 2 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050811].levelList[level=4].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 분쇄될 과거
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].name ; dataList[id=2050821].levelList[level=3].name ; dataList[id=2050821].levelList[level=4].name
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 증기 운반 기계
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].abName ; dataList[id=2050821].levelList[level=3].abName ; dataList[id=2050821].levelList[level=4].abName
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n최대 공명 수 당, 피해량 +10% (최대 100%)\n- 최대 공명이 나태 공명이었으면, 대신 피해량 +20% (최대 100%)\n[BeforeAttack] 홀수 턴에 (나태 공명 수)가 짝수거나, 짝수 턴에 (나태 공명 수)가 홀수면 피해량 +12%
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets randomly\nDeal +10% damage for every highest Reson. (max 100%)\n- If the highest Reson. was a Sloth Reson., deal +20% damage for every highest Reson. instead (max 100%)\n[BeforeAttack] When activating even-numbered (Sloth Reson.) in odd-numbered turns, or when activating odd-numbered (Sloth Reson.) in even-numbered turns, deal +12% damage
   PL:
484. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnStartCoin] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수) 1당, 이 코인의 피해량 +1% (최대 100%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5, [Vibration] 횟수 2 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +2 [Vibration] Count
   PL:
486. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] (나태 공명 수) 만큼 [Vibration] 횟수 증가 (최대 6)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +(Sloth Reson.) [Vibration] Count (max 6)
   PL:
487. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 메인 타겟이면, 대상의 현재 [Vibration]으로 [FusionVibration]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. [Vibration] 횟수 2 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL:
489. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] 이 코인의 효과로 인한 피해량 증가량이 100% 이상이면, [VibrationExplosion] 2회. [Vibration] 횟수 2 감소
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=1].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n최대 공명 수 당, 피해량 +10% (최대 100%)\n- 최대 공명이 나태 공명이었으면, 대신 피해량 +20% (최대 100%)\n<style="highlight">[BeforeAttack] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수)가 30 이상이면, 가중치 +2</style>\n[BeforeAttack] 홀수 턴에 (나태 공명 수)가 짝수거나, 짝수 턴에 (나태 공명 수)가 홀수면 피해량 +12%
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor
   EN: [CantIdentify]\nTargets randomly\nDeal +10% damage for every highest Reson. (max 100%)\n- If the highest Reson. was a Sloth Reson., deal +20% damage for every highest Reson. instead (max 100%)\n<style="highlight">[BeforeAttack] If the main target has 30+ ([Vibration] + [Vibration] Count), gain +2 Atk Weight</style>\n[BeforeAttack] When activating even-numbered (Sloth Reson.) in odd-numbered turns, or when activating odd-numbered (Sloth Reson.) in even-numbered turns, deal +12% damage
   PL:
491. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnStartCoin] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수) 1당, 이 코인의 피해량 +1% (최대 100%)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5, [Vibration] 횟수 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +2 [Vibration] Count<style="highlight"></style>
   PL:
493. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] (나태 공명 수) 만큼 [Vibration] 횟수 증가 (최대 6)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2050821].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +(Sloth Reson.) [Vibration] Count (max 6)<style="highlight"></style>
   PL:
494. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 메인 타겟이면, 대상의 현재 [Vibration]으로 [FusionVibration]<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2050821].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. [Vibration] 횟수 2 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=2050821].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2<style="highlight"></style>
   PL:
496. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 6 — opis] [OnSucceedAttack] 이 코인의 효과로 인한 피해량 증가량이 100% 이상이면, [VibrationExplosion] 2회. [Vibration] 횟수 2 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=3].coinlist[#0].coindescs[#5].desc ; dataList[id=2050821].levelList[level=4].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n최대 공명 수 당, 피해량 +10% (최대 100%)\n- 최대 공명이 나태 공명이었으면, 대신 피해량 +20% (최대 100%)\n[BeforeAttack] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수)가 30 이상이면, 가중치 +2\n[BeforeAttack] 홀수 턴에 (나태 공명 수)가 짝수거나, 짝수 턴에 (나태 공명 수)가 홀수면 피해량 +12%\n<style="highlight">[EndSkill] 자신의 최대 체력의 ([AccumulatedPastSinner] x 3)% 만큼 체력 회복</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=4].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Vibration], [EndSkill], [AccumulatedPastSinner]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]; [AccumulatedPastSinner] = 축적된 과거 / Accumulated Past
   EN: [CantIdentify]\nTargets randomly\nDeal +10% damage for every highest Reson. (max 100%)\n- If the highest Reson. was a Sloth Reson., deal +20% damage for every highest Reson. instead (max 100%)\n[BeforeAttack] If the main target has 30+ ([Vibration] + [Vibration] Count), gain +2 Atk Weight\n[BeforeAttack] When activating even-numbered (Sloth Reson.) in odd-numbered turns, or when activating odd-numbered (Sloth Reson.) in even-numbered turns, deal +12% damage\n<style="highlight">[EndSkill] Heal ([AccumulatedPastSinner] x 3)% HP</style>
   PL:
498. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnStartCoin] 메인 타겟의 ([Vibration] 위력 + [Vibration] 횟수) 1당, 이 코인의 피해량 <style="highlight">+2%</style> (최대 100%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] This Coin deals <style="highlight">+2%</style> damage for every ([Vibration] on the main target + [Vibration] Count on the main target) (max 100%)
   PL:
499. [Pasywka E.G.O — nazwa] 메트로놈
   źródło: Passive_Ego.json :: dataList[id=2050811].name
   limit: do 40 znaków
   EN: Metronome
   PL:
500. [Pasywka E.G.O — opis] 턴 시작시, 홀수 턴이면 [AttackDmgUp] 1, 짝수 턴이면 [Protection] 1 얻음\n- 메트로놈 E.G.O 기프트와 중첩하여 발동되지 않음. (해당 기프트가 강화 상태인 경우, 이 효과의 값을 차감한 뒤 얻음)\n- 다른 아군에게 부여하는 효과는 영향을 주지 않음\n\nEGO스킬 사용 시, 다음 턴에 [AccumulatedPastSinner] 1 얻음 (전투 당 1회)\n- 이후 턴 종료시마다, [AccumulatedPastSinner] 1 얻음
   źródło: Passive_Ego.json :: dataList[id=2050811].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [Protection], [AccumulatedPastSinner]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Protection] = 보호 / Protection; [AccumulatedPastSinner] = 축적된 과거 / Accumulated Past
   EN: Turn Start: in odd-numbered turns, gain 1 [AttackDmgUp]; in even-numbered turns, gain 1 [Protection]\n- Does not stack with the Metronome E.G.O Gift. (If the said E.G.O Gift is at an enhanced state, its effect subtracts the values gained from this effect)\n- Does not affect the instances of its effect applied to other allies\n\nWhen using E.G.O Skill, gain 1 [AccumulatedPastSinner] next turn (once per Encounter)\n- Gain 1 [AccumulatedPastSinner] at every subsequent Turn End
   PL:

## E.G.O [20509] Shadow-vested Bladesinger [着影揮刀] (착영휘도[着影揮刀]) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20509`

501. [Karta E.G.O — nazwa] 착영휘도[着影揮刀]
   źródło: Egos.json :: dataList[id=20509].name
   limit: do 50 znaków
   EN: Shadow-vested Bladesinger [着影揮刀]
   PL:
502. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20509].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 착영휘도[着影揮刀]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=1].name ; dataList[id=2050911].levelList[level=3].name ; dataList[id=2050911].levelList[level=4].name
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 그슨대
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=1].abName ; dataList[id=2050911].levelList[level=3].abName ; dataList[id=2050911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Geseundae
   PL:
505. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 전투에서 처음 사용 시 정신력 소모량 15 감소\n- 검계 우두머리 뫼르소면, 필요한 E.G.O 자원이 분노 1, 오만 1, 질투 1 감소\n자신의 [Breath] 4당, 합 위력 +1, 피해량 +6% (각각 최대 4, 최대 12%)\n이번 전투에서 [AlcoholKimPersonal]를 얻었으면, 메인 타겟에게 가하는 피해량 +60%\n- 검계 우두머리 뫼르소면, 해당 효과가 피해량 +120%로 적용\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 2, 소수점 버림)\n[BeforeAttack] 편성 순서가 가장 빠른 아군 (3 + 최대 공명 수)명의 [Breath] 횟수 4 증가\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 검계 소속 아군 인격 4명의 정신력 10 회복\n[EndSkill] 다음 턴에 [AlcoholKimPersonal] 4 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=1].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [AlcoholKimPersonal], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When used for the first time in an Encounter, consume 15 less SP\n- If Blade Lineage Mentor Meursault used this Skill, also consume 1 fewer Wrath, Pride, and Envy E.G.O resources\n\nClash Power +1 and deal +6% damage for every 4 [Breath] on self (max 4, max 12% respectively)\n\nIf this unit gained [AlcoholKimPersonal] during this Encounter, deal +60% damage against the main target\n- Blade Lineage Mentor Meursault deals +120% damage against the main target instead\n\n[BeforeAttack] Gain +(highest Reson. / 2) Atk Weight (max 2, rounded down)\n[BeforeAttack] (3 + highest Reson.) allies with the earliest Deployment orders gain +4 [Breath] Count\n[EndSkill] 4 other allied Blade Lineage Identities that have the lowest SP heal 10 SP\n[EndSkill] Gain 4 [AlcoholKimPersonal] next turn
   PL:
506. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050911].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2050911].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2050911].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 전투에서 처음 사용 시 정신력 소모량 15 감소\n- 검계 우두머리 뫼르소면, 필요한 E.G.O 자원이 분노 1, 오만 1, 질투 1 감소\n자신의 [Breath] 4당, 합 위력 +1, 피해량 +6% (각각 최대 <style="highlight">6</style>, 최대 <style="highlight">24</style>%)\n이번 전투에서 [AlcoholKimPersonal]를 얻었으면, 메인 타겟에게 가하는 피해량 +<style="highlight">80</style>%\n- 검계 우두머리 뫼르소면, 해당 효과가 피해량 +<style="highlight">160</style>%로 적용\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 2, 소수점 버림)\n[BeforeAttack] 편성 순서가 가장 빠른 아군 (3 + 최대 공명 수)명의 [Breath] 횟수 4 증가\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 검계 소속 아군 인격 4명의 정신력 10 회복\n[EndSkill] 다음 턴에 [AlcoholKimPersonal] 4 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=3].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [AlcoholKimPersonal], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When used for the first time in an Encounter, consume 15 less SP\n- If Blade Lineage Mentor Meursault used this Skill, also consume 1 fewer Wrath, Pride, and Envy E.G.O resources\n\nClash Power +1 and deal +6% damage for every 4 [Breath] on self (max <style="highlight">6</style>, max <style="highlight">24</style>% respectively)\n\nIf this unit gained [AlcoholKimPersonal] during this Encounter, deal +<style="highlight">80</style>% damage against the main target\n- Blade Lineage Mentor Meursault deals +<style="highlight">160</style>% damage against the main target instead\n\n[BeforeAttack] Gain +(highest Reson. / 2) Atk Weight (max 2, rounded down)\n[BeforeAttack] (3 + highest Reson.) allies with the earliest Deployment orders gain +4 [Breath] Count\n[EndSkill] 4 other allied Blade Lineage Identities that have the lowest SP heal 10 SP\n[EndSkill] Gain 4 [AlcoholKimPersonal] next turn
   PL:
509. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 전투에서 처음 사용 시 정신력 소모량 15 감소\n- 검계 우두머리 뫼르소면, 필요한 E.G.O 자원이 분노 1, 오만 1, 질투 1 감소\n자신의 [Breath] 4당, 합 위력 +1, 피해량 +6% (각각 최대 <style="highlight">8</style>, 최대 <style="highlight">30</style>%)\n이번 전투에서 [AlcoholKimPersonal]를 얻었으면, 메인 타겟에게 가하는 피해량 +<style="highlight">100</style>%\n- 검계 우두머리 뫼르소면, 해당 효과가 피해량 +<style="highlight">200</style>%로 적용\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 2, 소수점 버림)\n[BeforeAttack] 편성 순서가 가장 빠른 아군 (3 + 최대 공명 수)명의 [Breath] 횟수 4 증가\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 검계 소속 아군 인격 4명의 정신력 10 회복\n[EndSkill] 다음 턴에 [AlcoholKimPersonal] 4 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050911].levelList[level=4].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [AlcoholKimPersonal], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When used for the first time in an Encounter, consume 15 less SP\n- If Blade Lineage Mentor Meursault used this Skill, also consume 1 fewer Wrath, Pride, and Envy E.G.O resources\n\nClash Power +1 and deal +6% damage for every 4 [Breath] on self (max <style="highlight">8</style>, max <style="highlight">30</style>% respectively)\n\nIf this unit gained [AlcoholKimPersonal] during this Encounter, deal +<style="highlight">100</style>% damage against the main target\n- Blade Lineage Mentor Meursault deals +<style="highlight">200</style>% damage against the main target instead\n\n[BeforeAttack] Gain +(highest Reson. / 2) Atk Weight (max 2, rounded down)\n[BeforeAttack] (3 + highest Reson.) allies with the earliest Deployment orders gain +4 [Breath] Count\n[EndSkill] 4 other allied Blade Lineage Identities that have the lowest SP heal 10 SP\n[EndSkill] Gain 4 [AlcoholKimPersonal] next turn
   PL:
510. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 착영휘도[着影揮刀]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].name ; dataList[id=2050921].levelList[level=3].name ; dataList[id=2050921].levelList[level=4].name
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 그슨대
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].abName ; dataList[id=2050921].levelList[level=3].abName ; dataList[id=2050921].levelList[level=4].abName
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [Breath] 4당, 합 위력 +2, 피해량 +6% (각각 최대 8, 최대 12%)\n이번 전투에서 [AlcoholKimPersonal]를 얻었으면, 메인 타겟에게 가하는 피해량 +60%\n- 검계 우두머리 뫼르소면, 해당 효과가 피해량 +120%로 적용\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -8)\n[BeforeAttack] 모든 적과 아군이 [Breath] 횟수 4, [SlashDamageUp] 1, [SlashTakeDamageUp] 1 얻음\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 검계 소속 아군 인격 4명의 정신력 10 회복\n[EndSkill] 다음 턴에 [AlcoholKimPersonal] 4 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Breath], [AlcoholKimPersonal], [BeforeAttack], [SlashDamageUp], [SlashTakeDamageUp], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n\nClash Power +2 and deal +6% damage for every 4 [Breath] on self (max 8, max 12% respectively)\n\nIf this unit gained [AlcoholKimPersonal] during this Encounter, deal +60% damage against the main target\n- Blade Lineage Mentor Meursault deals +120% damage against the main target\n\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -8)\n[BeforeAttack] All enemies and allies gain +4 [Breath] Count, 1 [SlashDamageUp] and 1 [SlashTakeDamageUp]\n\n[EndSkill] 4 other allied Blade Lineage Identities that have the lowest SP heal 10 SP\n[EndSkill] Gain 4 [AlcoholKimPersonal] next turn
   PL:
513. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2050921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2050921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 마지막 코인의 최종 위력 +2 (코인당 1회)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2050921].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2050921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] The final Coin gains Final Power +2 (once per Coin)
   PL:
515. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2050921].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2050921].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
516. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2050921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2050921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 마지막 코인의 최종 위력 +2 (코인당 1회)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2050921].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2050921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=2050921].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=2050921].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2050921].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2050921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 마지막 코인의 최종 위력 +2 (코인당 1회)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2050921].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2050921].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=2050921].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2050921].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=2050921].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=2050921].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=1].coinlist[#3].coindescs[#1].desc ; dataList[id=2050921].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=2050921].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [Breath] 4당, 합 위력 +2, 피해량 +6% (각각 최대 <style="highlight">12</style>, 최대 <style="highlight">24</style>%)\n이번 전투에서 [AlcoholKimPersonal]를 얻었으면, 메인 타겟에게 가하는 피해량 +<style="highlight">80</style>%\n- 검계 우두머리 뫼르소면, 해당 효과가 피해량 +<style="highlight">160</style>%로 적용\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -8)\n[BeforeAttack] 모든 적과 아군이 [Breath] 횟수 4, [SlashDamageUp] 1, [SlashTakeDamageUp] 1 얻음\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 검계 소속 아군 인격 4명의 정신력 10 회복\n[EndSkill] 다음 턴에 [AlcoholKimPersonal] 4 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=3].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Breath], [AlcoholKimPersonal], [BeforeAttack], [SlashDamageUp], [SlashTakeDamageUp], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n\nClash Power +2 and deal +6% damage for every 4 [Breath] on self (max <style="highlight">12</style>, max <style="highlight">24</style>% respectively)\n\nIf this unit gained [AlcoholKimPersonal] during this Encounter, deal +<style="highlight">80</style>% damage against the main target\n- Blade Lineage Mentor Meursault deals +<style="highlight">160</style>% damage against the main target\n\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -8)\n[BeforeAttack] All enemies and allies gain +4 [Breath] Count, 1 [SlashDamageUp] and 1 [SlashTakeDamageUp]\n\n[EndSkill] 4 other allied Blade Lineage Identities that have the lowest SP heal 10 SP\n[EndSkill] Gain 4 [AlcoholKimPersonal] next turn
   PL:
525. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [Breath] 4당, 합 위력 +2, 피해량 +6% (각각 최대 <style="highlight">16</style>, 최대 <style="highlight">30</style>%)\n이번 전투에서 [AlcoholKimPersonal]를 얻었으면, 메인 타겟에게 가하는 피해량 +<style="highlight">100</style>%\n- 검계 우두머리 뫼르소면, 해당 효과가 피해량 +<style="highlight">200</style>%로 적용\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -8)\n[BeforeAttack] 모든 적과 아군이 [Breath] 횟수 4, [SlashDamageUp] 1, [SlashTakeDamageUp] 1 얻음\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 검계 소속 아군 인격 4명의 정신력 10 회복\n[EndSkill] 다음 턴에 [AlcoholKimPersonal] 4 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2050921].levelList[level=4].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Breath], [AlcoholKimPersonal], [BeforeAttack], [SlashDamageUp], [SlashTakeDamageUp], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n\nClash Power +2 and deal +6% damage for every 4 [Breath] on self (max <style="highlight">16</style>, max <style="highlight">30</style>% respectively)\n\nIf this unit gained [AlcoholKimPersonal] during this Encounter, deal +<style="highlight">100</style>% damage against the main target\n- Blade Lineage Mentor Meursault deals +<style="highlight">200</style>% damage against the main target\n\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -8)\n[BeforeAttack] All enemies and allies gain +4 [Breath] Count, 1 [SlashDamageUp] and 1 [SlashTakeDamageUp]\n\n[EndSkill] 4 other allied Blade Lineage Identities that have the lowest SP heal 10 SP\n[EndSkill] Gain 4 [AlcoholKimPersonal] next turn
   PL:
526. [Pasywka E.G.O — nazwa] 칼끝에 맺힌 술방울
   źródło: Passive_Ego.json :: dataList[id=2050911].name
   limit: do 50 znaków
   EN: Beads of Liquor at Bladepoint
   PL:
527. [Pasywka E.G.O — opis] [AlwaysUseEGOPassive2050911]\n\n기본 스킬의 공격 적중 시 대상에게 [Laceration] 2 부여 (스킬당 1회)\n\n이 인격은 [Laceration], [Breath]을 부여하는 인격으로 취급됨\n- 이 효과로 인해서 기본 스킬이 [Laceration]과 [Breath]을 부여하는 스킬로 취급됨\n\n[WhenUseEGOPassive]\n\n아군 사망 시 다음 턴에 [AlcoholKimPersonal] 1 얻음\n- 사망한 아군이 검계 소속이면, 대신 [AlcoholKimPersonal] 2 얻음\n\n턴 시작 시 자신에게 [AlcoholKimPersonal]가 있으면, [GhostKimPersonal] 상태가 됨\n- 검계 우두머리 뫼르소면, 추가로 [RootSoupKimPersonal] 얻음\n\n턴 시작 시 자신에게 [AlcoholKimPersonal]가 없으면, 자신의 [GhostKimPersonal], [GrudgePersonal], [RootSoupKimPersonal] 소멸함\n\n[AlcoholKimPersonal]가 있을 때 체력이 0이 되는 피해를 받으면, 자신의 체력을 최대 체력의 ([AlcoholKimPersonal] 수치 x 25)%만큼 회복하고 [AlcoholKimPersonal] 소멸함 (전투당 1회, 인격 패시브 우선 발동)\n- 흐트러짐 상태면, 흐트러짐 해제 (강제 흐트러짐 제외)
   źródło: Passive_Ego.json :: dataList[id=2050911].desc
   limit: do 1400 znaków
   tokeny: zachowaj dokładnie: \n, [AlwaysUseEGOPassive2050911], [Laceration], [Breath], [WhenUseEGOPassive], [AlcoholKimPersonal], [GhostKimPersonal], [RootSoupKimPersonal], [GrudgePersonal]
   znaczenie tagów: [AlwaysUseEGOPassive2050911] = [검계 우두머리 뫼르소 전용 상시 효과] / [Always Active - Blade Lineage Mentor Meursault Exclusive Effect]; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise; [WhenUseEGOPassive] = [사용 효과] / [Effect on Use]; [AlcoholKimPersonal] = 추모주 / Drink to the Fallen; [GhostKimPersonal] = 원한 / Resentment; [RootSoupKimPersonal] = 한 서린 검집 / Resentful Scabbard; [GrudgePersonal] = 맺혀가는 응어리 / Growing Resentment
   EN: [AlwaysUseEGOPassive2050911]\n\nOn Hit with a Base Skill, inflict 2 [Laceration] on target (once per Skill)\n\nThis Identity counts as an "Identity that applies [Laceration] and [Breath]"\n- This Identity's Base Skills count as "Skills that apply [Laceration] and [Breath]"\n\n[WhenUseEGOPassive]\n\nWhen an ally is defeated, gain 1 [AlcoholKimPersonal] next turn\n- If the defeated ally is in Blade Lineage, gain 2 [AlcoholKimPersonal] instead\n\nTurn Start: If this unit has [AlcoholKimPersonal], enter [GhostKimPersonal] state\n- Blade Lineage Mentor Meursault gains [RootSoupKimPersonal] as well when the above effect activates\n\nTurn Start: If this unit does not have [AlcoholKimPersonal], the following effects expire - [GhostKimPersonal], [GrudgePersonal], and [RootSoupKimPersonal]\n\nWhen this unit has [AlcoholKimPersonal]: When this unit takes damage that brings its HP down to 0, heal ([AlcoholKimPersonal] Stack x 25)% HP; then, [AlcoholKimPersonal] expires (once per Encounter; this effect activates after Identity Passives with similar effects)\n- When Staggered, recover from Stagger (excluding forced Staggers)
   PL:
528. [Pasywka E.G.O — podsumowanie] [AlcoholKimPersonal] 얻음
   źródło: Passive_Ego.json :: dataList[id=2050911].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AlcoholKimPersonal]
   znaczenie tagów: [AlcoholKimPersonal] = 추모주 / Drink to the Fallen
   EN: Gain [AlcoholKimPersonal]
   PL:

## E.G.O [20510] Hollow (구멍) — Meursault
- postać: Meursault (뫼르소) · ID E.G.O: `20510`

529. [Karta E.G.O — nazwa] 구멍
   źródło: Egos.json :: dataList[id=20510].name
   limit: do 40 znaków
   EN: Hollow
   PL:
530. [Karta E.G.O — opis] 뫼르소의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20510].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 구멍
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].name ; dataList[id=2051011].levelList[level=3].name ; dataList[id=2051011].levelList[level=4].name
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 구멍난 사람
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].abName ; dataList[id=2051011].levelList[level=3].abName ; dataList[id=2051011].levelList[level=4].abName
   limit: do 40 znaków
   EN: Hollowed Man
   PL:
533. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 스킬 시전 중 공격 대상 사망 시, 체력이 가장 낮은 공격 대상을 우선 지정 (집중 전투의 경우, 부위로 판정)\n\n(자신의 [Breath] 위력 + [Charge] 횟수) 4당 합 위력 +1 (최대 5)\n자신의 [BulletHole] 1당 합 위력 +2\n\n[BeforeAttack] 자신의 [Breath] 횟수 3, [Charge] 횟수 5 증가\n[BeforeAttack] 정신력을 (5-보유한 [BulletHole]) x 3 만큼 소모하여, [BulletHole]을 최대치로 얻음\n\n[EndSkill] [BlackWingHole] 2 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Charge], [BulletHole], [BeforeAttack], [EndSkill], [BlackWingHole]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [BulletHole] = 잿빛 탄환 / Ashen Bullet; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [BlackWingHole] = 검은 날개 / Black Wings
   EN: If the target is defeated before this Skill is finished, prioritize a target that has the lowest HP (for Focused Encounters, the Part)\n\nClash Power +1 for every 4 ([Breath] Potency + [Charge] Count) on self (max 5)\nClash Power +2 for every [BulletHole] on self\n\n[BeforeAttack] Gain +3 [Breath] Count and +5 [Charge] Count\n[BeforeAttack] Consume 3(5 - [BulletHole] on self) SP to gain up to max [BulletHole]\n\n[EndSkill] Gain 2 [BlackWingHole]
   PL:
534. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] 이 코인은 메인 타겟에게만 적중함
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin hits only the main target
   PL:
536. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [BulletHole] 1 소모
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletHole]
   znaczenie tagów: [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: Spend 1 [BulletHole]
   PL:
537. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 4 — opis] 크리티컬 피해량 +10%
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   EN: Deal +10% damage on Critical Hit
   PL:
538. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 5 — opis] 처음 사용한 코인이면,\n- 피해량 +(자신의 [Charge] 횟수 x 5)% (최대 100%)\n- 크리티컬 피해량 +(자신의 [Breath] 위력 x 횟수)% (최대 100%)\n- 해당 코인에 한해 대상의 관통 속성 내성을 취약으로 변경함
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Breath]
   znaczenie tagów: [Charge] = 충전 / Charge; [Breath] = 호흡 / Poise
   EN: If this is the first Coin:\n- Deal +([Charge] Count x 5)% damage (max 100%)\n- Deal +([Breath] Potency x Count)% damage on Critical Hit (max 100%)\n- For this Coin, change target's Pierce Resist. to Fatal
   PL:
539. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
540. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 7 — opis] [EndCoin] [BulletHole]이 1 이상이면 이 코인 재사용 (스킬당 4회)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#0].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [BulletHole]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: [EndCoin] At 1+ [BulletHole], Reuse this Coin (4 times per Skill)
   PL:
541. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +30% damage on Critical Hit
   PL:
543. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
544. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 스킬 시전 중 공격 대상 사망 시, 체력이 가장 낮은 공격 대상을 우선 지정 (집중 전투의 경우, 부위로 판정)\n\n(자신의 [Breath] 위력 + [Charge] 횟수) 4당 합 위력 +1 (최대 <style="highlight">7</style>)\n자신의 [BulletHole] 1당 합 위력 +2\n\n[BeforeAttack] 자신의 [Breath] 횟수 3, [Charge] 횟수 5 증가\n[BeforeAttack] 정신력을 (5-보유한 [BulletHole]) x 3 만큼 소모하여, [BulletHole]을 최대치로 얻음\n\n[EndSkill] [BlackWingHole] 2 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Charge], [BulletHole], [BeforeAttack], [EndSkill], [BlackWingHole]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [BulletHole] = 잿빛 탄환 / Ashen Bullet; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [BlackWingHole] = 검은 날개 / Black Wings
   EN: If the target is defeated before this Skill is finished, prioritize a target that has the lowest HP (for Focused Encounters, the Part)\n\nClash Power +1 for every 4 ([Breath] Potency + [Charge] Count) on self (max <style="highlight">7</style>)\nClash Power +2 for every [BulletHole] on self\n\n[BeforeAttack] Gain +3 [Breath] Count and +5 [Charge] Count\n[BeforeAttack] Consume 3(5 - [BulletHole] on self) SP to gain up to max [BulletHole]\n\n[EndSkill] Gain 2 [BlackWingHole]
   PL:
545. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] 이 코인은 메인 타겟에게만 적중함<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: This Coin hits only the main target<style="highlight"></style>
   PL:
547. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [BulletHole] 1 소모<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletHole]
   znaczenie tagów: [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: Spend 1 [BulletHole]<style="highlight"></style>
   PL:
548. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 4 — opis] 크리티컬 피해량 <style="highlight">+15%</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal <style="highlight">+15%</style> damage on Critical Hit
   PL:
549. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] 처음 사용한 코인이면,\n- 피해량 +(자신의 [Charge] 횟수 x 5)% (최대 100%)\n- 크리티컬 피해량 +(자신의 [Breath] 위력 x 횟수)% (최대 100%)\n- 해당 코인에 한해 대상의 관통 속성 내성을 취약으로 변경함<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [Breath]
   znaczenie tagów: [Charge] = 충전 / Charge; [Breath] = 호흡 / Poise
   EN: If this is the first Coin:\n- Deal +([Charge] Count x 5)% damage (max 100%)\n- Deal +([Breath] Potency x Count)% damage on Critical Hit (max 100%)\n- For this Coin, change target's Pierce Resist. to Fatal<style="highlight"></style>
   PL:
550. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]<style="highlight"></style>
   PL:
551. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 7 — opis] <style="highlight">[CriticalOnSucceedAttack] 마지막 코인 위력 +1</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: <style="highlight">[CriticalOnSucceedAttack] Final Coin Power +1</style>
   PL:
552. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 8 — opis] [EndCoin] [BulletHole]이 1 이상이면 이 코인 재사용 (스킬당 4회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#0].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin], [BulletHole]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: [EndCoin] At 1+ [BulletHole], Reuse this Coin (4 times per Skill)<style="highlight"></style>
   PL:
553. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2051011].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+50%</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal <style="highlight">+50%</style> damage on Critical Hit
   PL:
555. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] <style="highlight">[OnStartCoin] 공격 대상이 1명이면, 피해량 +50% (집중 전투의 경우, 본체로 판정)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]
   EN: <style="highlight">[OnStartCoin] When attacking just 1 target, deal +50% damage (in Focused Encounters, a Core)</style>
   PL:
556. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=3].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count<style="highlight"></style>
   PL:
557. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 스킬 시전 중 공격 대상 사망 시, 체력이 가장 낮은 공격 대상을 우선 지정 (집중 전투의 경우, 부위로 판정)\n\n(자신의 [Breath] 위력 + [Charge] 횟수) 4당 합 위력 +1 (최대 <style="highlight">10</style>)\n자신의 [BulletHole] 1당 합 위력 +2\n\n[BeforeAttack] 자신의 [Breath] 횟수 3, [Charge] 횟수 5 증가\n[BeforeAttack] 정신력을 (5-보유한 [BulletHole]) x 3 만큼 소모하여, [BulletHole]을 최대치로 얻음\n\n[EndSkill] [BlackWingHole] 2 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Charge], [BulletHole], [BeforeAttack], [EndSkill], [BlackWingHole]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [BulletHole] = 잿빛 탄환 / Ashen Bullet; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [BlackWingHole] = 검은 날개 / Black Wings
   EN: If the target is defeated before this Skill is finished, prioritize a target that has the lowest HP (for Focused Encounters, the Part)\n\nClash Power +1 for every 4 ([Breath] Potency + [Charge] Count) on self (max <style="highlight">10</style>)\nClash Power +2 for every [BulletHole] on self\n\n[BeforeAttack] Gain +3 [Breath] Count and +5 [Charge] Count\n[BeforeAttack] Consume 3(5 - [BulletHole] on self) SP to gain up to max [BulletHole]\n\n[EndSkill] Gain 2 [BlackWingHole]
   PL:
558. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 4 — opis] 크리티컬 피해량 <style="highlight">+20%</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal <style="highlight">+20%</style> damage on Critical Hit
   PL:
559. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 6 — opis] <style="highlight">[OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여 (스킬당 1회)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] (once per Skill)</style>
   PL:
560. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 7 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#6].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 8 — opis] [CriticalOnSucceedAttack] 마지막 코인 위력 +1<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Final Coin Power +1<style="highlight"></style>
   PL:
562. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 9 — opis] [EndCoin] [BulletHole]이 1 이상이면 이 코인 재사용 (스킬당 4회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#0].coindescs[#8].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +50%<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +50% damage on Critical Hit<style="highlight"></style>
   PL:
564. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnStartCoin] 공격 대상이 1명이면, 피해량 <style="highlight">+100%</style> (집중 전투의 경우, 본체로 판정)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]
   EN: [OnStartCoin] When attacking just 1 target, deal +<style="highlight">100</style>% damage (in Focused Encounters, a Core)
   PL:
565. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 4 — opis] <style="highlight">[OnStartCoin] 자신의 [Charge] 횟수 4당 코인 위력 +1 (최대 5)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnStartCoin] Coin Power +1 for every 4 [Charge] Count (max 5)</style>
   PL:
566. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 5 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051011].levelList[level=4].coinlist[#1].coindescs[#4].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 구멍
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].name ; dataList[id=2051021].levelList[level=3].name ; dataList[id=2051021].levelList[level=4].name
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 구멍난 사람
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].abName ; dataList[id=2051021].levelList[level=3].abName ; dataList[id=2051021].levelList[level=4].abName
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n이 스킬은 수비 스킬을 발동시키지 않음 (합 가능 수비 포함)\n(자신의 [Breath] 위력 + [Charge] 횟수) 4당 합 위력 +1 (최대 5)\n[BeforeAttack] 자신에게 [BulletHole]이 없으면, [BulletHole] 1 얻음\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -4)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Breath], [Charge], [BeforeAttack], [BulletHole]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: [CantIdentify]\nTargets randomly\nThis Skill does not trigger Defense Skills (including Clashable Defense Skills)\nClash Power +1 for every 4 ([Breath] Potency + [Charge] Count) on self (max 5)\n[BeforeAttack] If this unit does not have [BulletHole], gain 1 [BulletHole]\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -4)
   PL:
570. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnStartCoin] [BlackWingHole] 5 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [BlackWingHole]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BlackWingHole] = 검은 날개 / Black Wings
   EN: [OnStartCoin] Gain 5 [BlackWingHole]
   PL:
572. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnStartCoin] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: [OnStartCoin] Gain +5 [Charge] Count
   PL:
573. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnStartCoin] [Breath] 5 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [Breath]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Breath] = 호흡 / Poise
   EN: [OnStartCoin] Gain 5 [Breath]
   PL:
574. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] 이 코인의 뒷면 확률은 정신력과 관계 없이 (자신이 보유한 [BulletHole] x 20)% 확률로 적용됨
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletHole]
   znaczenie tagów: [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: This Coin has ([BulletHole] on self x 20)% chance to flip Tails regardless of this unit's SP
   PL:
576. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 3 — opis] [CoinHead]\n- 이 코인은 적중하지 않음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CoinHead]
   znaczenie tagów: [CoinHead] = [앞면] / [Heads]
   EN: [CoinHead]\n- This Coin does not hit
   PL:
577. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 4 — opis] - [EndCoin] [Breath] 5 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [Breath]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [Breath] = 호흡 / Poise
   EN: - [EndCoin] Gain 5 [Breath]
   PL:
578. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 5 — opis] - [EndCoin] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [Breath]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [Breath] = 호흡 / Poise
   EN: - [EndCoin] Gain +3 [Breath] Count
   PL:
579. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 6 — opis] - [EndCoin] [BulletHole] 2 얻음
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [BulletHole]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: - [EndCoin] Gain 2 [BulletHole]
   PL:
580. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 7 — opis] - [EndCoin] 이 스킬에서 소모한 E.G.O 자원을 절반 돌려받음 (소수점 버림)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: - [EndCoin] Refund half of the E.G.O resources consumed by this Skill (rounded down)
   PL:
581. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 8 — opis] [CoinTail]\n- 피해량 +(자신의 충전 횟수 x 3)% (최대 60%)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CoinTail], [Charge]
   znaczenie tagów: [CoinTail] = [뒷면] / [Tails]; [Charge] = 충전 / Charge
   EN: [CoinTail]\n- Deal +([Charge] Count x 3)% damage (max 60%)
   PL:
582. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 9 — opis] - 크리티컬 피해량 +70%
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#8].desc
   limit: do 120 znaków
   EN: - Deal +70% damage on Critical Hit
   PL:
583. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 10 — opis] - [OnSucceedAttack] 이 코인 최종 피해량의 10%만큼 관통 피해
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#9].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: - [OnSucceedAttack] Deal Pierce damage equal to 10% of this Coin's final damage
   PL:
584. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 11 — opis] - [EndCoin] 자신의 [BulletHole] 전부 소모
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [BulletHole]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: - [EndCoin] Consume all [BulletHole] on self
   PL:
585. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 12 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#11].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
586. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 13 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=1].coinlist[#1].coindescs[#12].desc
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n이 스킬은 수비 스킬을 발동시키지 않음 (합 가능 수비 포함)\n(자신의 [Breath] 위력 + [Charge] 횟수) 4당 합 위력 +1 (최대 <style="highlight">7</style>)\n\n<style="highlight">[BeforeAttack] 공격 대상이 1명이면, 피해량 +100% (집중 전투의 경우, 본체로 판정)</style>\n[BeforeAttack] 자신에게 [BulletHole]이 없으면, [BulletHole] 1 얻음\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -4)
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Breath], [Charge], [BeforeAttack], [BulletHole]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: [CantIdentify]\nTargets randomly\nThis Skill does not trigger Defense Skills (including Clashable Defense Skills)\nClash Power +1 for every 4 ([Breath] Potency + [Charge] Count) on self (max <style="highlight">7</style>)\n\n<style="highlight">[BeforeAttack] When attacking just 1 target, deal +100% damage (in Focused Encounters, a Core)</style>\n[BeforeAttack] If this unit does not have [BulletHole], gain 1 [BulletHole]\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -4)
   PL:
588. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2051021].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnStartCoin] [BlackWingHole] 5 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2051021].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [BlackWingHole]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BlackWingHole] = 검은 날개 / Black Wings
   EN: [OnStartCoin] Gain 5 [BlackWingHole]<style="highlight"></style>
   PL:
590. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnStartCoin] 자신의 [Charge] 횟수 5 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2051021].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: [OnStartCoin] Gain +5 [Charge] Count<style="highlight"></style>
   PL:
591. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnStartCoin] [Breath] 5 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2051021].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Breath]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Breath] = 호흡 / Poise
   EN: [OnStartCoin] Gain 5 [Breath]<style="highlight"></style>
   PL:
592. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] 이 코인의 뒷면 확률은 정신력과 관계 없이 (자신이 보유한 [BulletHole] x 20)% 확률로 적용됨<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletHole]
   znaczenie tagów: [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: This Coin has ([BulletHole] on self x 20)% chance to flip Tails regardless of this unit's SP<style="highlight"></style>
   PL:
594. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [CoinHead]\n- 이 코인은 적중하지 않음<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CoinHead]
   znaczenie tagów: [CoinHead] = [앞면] / [Heads]
   EN: [CoinHead]\n- This Coin does not hit<style="highlight"></style>
   PL:
595. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 4 — opis] - [EndCoin] [Breath] 5 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin], [Breath]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [Breath] = 호흡 / Poise
   EN: - [EndCoin] Gain 5 [Breath]<style="highlight"></style>
   PL:
596. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 5 — opis] - [EndCoin] 자신의 [Breath] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#4].desc ; dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin], [Breath]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [Breath] = 호흡 / Poise
   EN: - [EndCoin] Gain +3 [Breath] Count<style="highlight"></style>
   PL:
597. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 6 — opis] - [EndCoin] [BulletHole] 2 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin], [BulletHole]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: - [EndCoin] Gain 2 [BulletHole]<style="highlight"></style>
   PL:
598. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 7 — opis] - [EndCoin] 이 스킬에서 소모한 E.G.O 자원을 절반 돌려받음 (소수점 버림)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: - [EndCoin] Refund half of the E.G.O resources consumed by this Skill (rounded down)<style="highlight"></style>
   PL:
599. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 8 — opis] [CoinTail]\n- 피해량 +(자신의 충전 횟수 x <style="highlight">4)% (최대 80%)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CoinTail], [Charge]
   znaczenie tagów: [CoinTail] = [뒷면] / [Tails]; [Charge] = 충전 / Charge
   EN: [CoinTail]\n- Deal +([Charge] Count x <style="highlight">4)% damage (max 80%)</style>
   PL:
600. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 9 — opis] - 크리티컬 피해량 <style="highlight">+100%</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#8].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: - Deal <style="highlight">+100%</style> damage on Critical Hit
   PL:
601. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 10 — opis] - [OnSucceedAttack] 이 코인 최종 피해량의 <style="highlight">15%</style>만큼 관통 피해
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#9].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: - [OnSucceedAttack] Deal Pierce damage equal to <style="highlight">15</style>% of this Coin's final damage
   PL:
602. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 11 — opis] - [EndCoin] 자신의 [BulletHole] 전부 소모<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin], [BulletHole]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BulletHole] = 잿빛 탄환 / Ashen Bullet
   EN: - [EndCoin] Consume all [BulletHole] on self<style="highlight"></style>
   PL:
603. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 12 — opis] [OnSucceedAttack] [Sinking] 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#11].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]<style="highlight"></style>
   PL:
604. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 13 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=3].coinlist[#1].coindescs[#12].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n이 스킬은 수비 스킬을 발동시키지 않음 (합 가능 수비 포함)\n(자신의 [Breath] 위력 + [Charge] 횟수) 4당 합 위력 +1 (최대 <style="highlight">10</style>)\n\n[BeforeAttack] 공격 대상이 1명이면, 피해량 <style="highlight">+200% (집중 전투의 경우, 본체로 판정)\n[BeforeAttack] 최종 위력 +(자신의 [BulletHole] 수치)</style>\n[BeforeAttack] 자신에게 [BulletHole]이 없으면, [BulletHole] 1 얻음\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -4)\n<style="highlight">[EnemyKill] 정신력 5 회복</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Breath], [Charge], [BeforeAttack], [BulletHole], [EnemyKill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BulletHole] = 잿빛 탄환 / Ashen Bullet; [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [CantIdentify]\nTargets randomly\nThis Skill does not trigger Defense Skills (including Clashable Defense Skills)\nClash Power +1 for every 4 ([Breath] Potency + [Charge] Count) on self (max <style="highlight">10</style>)\n\n[BeforeAttack] When attacking just 1 target, deal +<style="highlight">200</style>% damage (in Focused Encounters, a Core)\n<style="highlight">[BeforeAttack] Gain Final Power +([BulletHole] on self)</style>\n[BeforeAttack] If this unit does not have [BulletHole], gain 1 [BulletHole]\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -4)\n<style="highlight">[EnemyKill] Heal 5 SP</style>
   PL:
606. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 5 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 6 — opis] <style="highlight">- [EndCoin] 자신에게 부여된 해제 가능한 부정적인 효과 무작위 1개 제거</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: <style="highlight">- [EndCoin] Remove 1 random removable negative effect applied to self</style>
   PL:
608. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 7 — opis] - [EndCoin] [BulletHole] 2 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#6].desc
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 8 — opis] - [EndCoin] 이 스킬에서 소모한 E.G.O 자원을 절반 돌려받음 (소수점 버림)<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#7].desc
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 9 — opis] [CoinTail]\n- 피해량 +(자신의 충전 횟수 x <style="highlight">5)% (최대 100%)</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#8].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CoinTail], [Charge]
   znaczenie tagów: [CoinTail] = [뒷면] / [Tails]; [Charge] = 충전 / Charge
   EN: [CoinTail]\n- Deal +([Charge] Count x <style="highlight">5)% damage (max 100%)</style>
   PL:
611. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 10 — opis] - 크리티컬 피해량 <style="highlight">+130%</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#9].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: - Deal +<style="highlight">130</style>% damage on Critical Hit
   PL:
612. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 11 — opis] - [OnSucceedAttack] 이 코인 최종 피해량의 <style="highlight">20%</style>만큼 관통 피해
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: - [OnSucceedAttack] Deal Pierce damage equal to <style="highlight">20</style>% of this Coin's final damage
   PL:
613. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 12 — opis] <style="highlight">- [EnemyKill] 자신의 최대 체력의 5%만큼 체력 회복</style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#11].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: <style="highlight">- [EnemyKill] Heal 5% HP</style>
   PL:
614. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 13 — opis] - [EndCoin] 자신의 [BulletHole] 전부 소모<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#12].desc
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 14 — opis] [OnSucceedAttack] [Sinking] 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#13].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 15 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-05.json :: dataList[id=2051021].levelList[level=4].coinlist[#1].coindescs[#14].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Pasywka E.G.O — nazwa] 레모라지 앵테른(l'hémorragie interne)
   źródło: Passive_Ego.json :: dataList[id=2051011].name
   limit: do 50 znaków
   EN: L'Hémorragie interne
   PL:
618. [Pasywka E.G.O — opis] [AlwaysUseEGOPassive]\n자신의 [BulletHole]이 5면, ‘구멍’ E.G.O 스킬(각성, 침식) 사용 시 E.G.O 자원을 소모하지 않음\n\n턴 시작 시 [BulletHole] 1 얻음\n\n[WhenUseEGOPassive]\n턴 시작 시, [BlackWingHole] 1 얻음\n\n자신이 [Bullet]을 누적 3개 소모하거나 잃을 때마다 정신력을 5 회복하고, 다음 턴에 [ResultEnhancement] 1 얻음 (특수 [Bullet] 포함. 턴당 [Bullet] 최대 9개까지 판정)
   źródło: Passive_Ego.json :: dataList[id=2051011].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [AlwaysUseEGOPassive], [BulletHole], [WhenUseEGOPassive], [BlackWingHole], [Bullet], [ResultEnhancement]
   znaczenie tagów: [AlwaysUseEGOPassive] = [상시 효과] / [Always Active]; [BulletHole] = 잿빛 탄환 / Ashen Bullet; [WhenUseEGOPassive] = [사용 효과] / [Effect on Use]; [BlackWingHole] = 검은 날개 / Black Wings; [Bullet] = 탄환 / Ammo; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [AlwaysUseEGOPassive]\nIf this unit has 5 [BulletHole], does not consume E.G.O Resource when using "Hollow" E.G.O's Skills (both Awakening and Corrosion)\n\nTurn Start: Gain 1 [BulletHole]\n\n[WhenUseEGOPassive]\nTurn Start: Gain 1 [BlackWingHole]\n\nHeal 5 SP every time this unit consumes or loses 3 cumulative [Bullet], and gain 1 [ResultEnhancement] next turn (including Unique [Bullet]; counts up to 9 [Bullet] per turn)
   PL:
619. [Pasywka E.G.O — tekst klimatyczny] 타자의 시선이 나에게 박혀 구멍을 내고 온갖 것을 쏟아내게 한다. 쏟아져 나온 것은 탄환이 되어 다시 네게 쏘아져 구멍을 뚫는다.
   źródło: Passive_Ego.json :: dataList[id=2051011].flavor
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The gaze of another nails into me, driving a hollow from which multitudes spill forth.\nThe discharge is then forged into a bullet that punches a hollow into you.
   PL:

## E.G.O [20601] Land of Illusion (허환경) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20601`

620. [Karta E.G.O — nazwa] 허환경
   źródło: Egos-a1c9p3.json :: dataList[id=206011].name
   limit: do 40 znaków
   EN: Land of Illusion
   PL:
621. [Karta E.G.O — opis] 홍루 연출 전용 EGO 장비
   źródło: Egos-a1c9p3.json :: dataList[id=206011].desc
   limit: do 120 znaków
   EN: Hong Lu's Battle Cinematic Exclusive E.G.O
   PL:
622. [Karta E.G.O — nazwa] 허환경
   źródło: Egos.json :: dataList[id=20601].name
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Karta E.G.O — opis] 홍루 기본 EGO 장비
   źródło: Egos.json :: dataList[id=20601].desc
   limit: do 120 znaków
   EN: Hong Lu’s Base E.G.O
   PL:
624. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 허환경
   źródło: Skills_Ego.json :: dataList[id=2060111].levelList[level=1].name ; dataList[id=2060111].levelList[level=3].name ; dataList[id=2060111].levelList[level=4].name
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 홍루
   źródło: Skills_Ego.json :: dataList[id=2060111].levelList[level=1].abName ; dataList[id=2060111].levelList[level=3].abName ; dataList[id=2060111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Hong Lu
   PL:
626. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills_Ego.json :: dataList[id=2060111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL:
627. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] [EndSkill] 정신력 15 회복
   źródło: Skills_Ego.json :: dataList[id=2060111].levelList[level=3].desc ; dataList[id=2060111].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 15 SP
   PL:
628. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Ego.json :: dataList[id=2060111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
629. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 다음 턴에 모든 아군의 정신력 감소 효율 -2, E.G.O 사용시 정신력 감소량 -2
   źródło: Skills_Ego.json :: dataList[id=2060111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Next turn: -2 SP Loss Efficiency to all allies; -2 to amount of SP lost from E.G.O use
   PL:
630. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — nazwa] 허환경
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2060112].levelList[level=4].name
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — źródło (Anomalia)] 홍루
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2060112].levelList[level=4].abName
   (powtórzenie elementu 625 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [EndSkill] 본인과 아군의 정신력 15 회복\n[EndSkill] 본인과 아군의 화상 제거
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2060112].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 15 SP for this unit and all allies\n[EndSkill] Remove Burn from this unit and all allies
   PL:
633. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2060112].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Pasywka E.G.O — nazwa] 파문
   źródło: Passive_Ego.json :: dataList[id=2060111].name
   limit: do 40 znaków
   EN: Ripple
   PL:
635. [Pasywka E.G.O — opis] 전투 시작 시 정신력이 가장 낮은 아군의 정신력을 조작 패널에서 가장 높은 자신의 완전 공명 수만큼 회복 \n패닉 상태의 아군 제외
   źródło: Passive_Ego.json :: dataList[id=2060111].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Combat Start: Heal (this unit's highest A-Reson.) SP for the ally that has the least SP, excluding allies in Panic
   PL:

## E.G.O [20602] Roseate Desire (분홍욕망) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20602`

636. [Karta E.G.O — nazwa] 분홍욕망
   źródło: Egos.json :: dataList[id=20602].name
   limit: do 40 znaków
   EN: Roseate Desire
   PL:
637. [Karta E.G.O — opis] 홍루 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20602].desc
   limit: do 120 znaków
   EN: Hong Lu’s E.G.O Gear
   PL:
638. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 분홍욕망
   źródło: Skills_Ego.json :: dataList[id=2060211].levelList[level=1].name ; dataList[id=2060211].levelList[level=3].name ; dataList[id=2060211].levelList[level=4].name
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 분홍신
   źródło: Skills_Ego.json :: dataList[id=2060211].levelList[level=1].abName ; dataList[id=2060211].levelList[level=3].abName ; dataList[id=2060211].levelList[level=4].abName
   limit: do 40 znaków
   EN: Pink Shoes
   PL:
640. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 수비 위력 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2060211].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2060211].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060211].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Power Down
   PL:
641. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2060211].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL:
642. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 4 부여
   źródło: Skills_Ego.json :: dataList[id=2060211].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 4 [DefenseDown]
   PL:
643. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 5 부여
   źródło: Skills_Ego.json :: dataList[id=2060211].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 5 [DefenseDown]
   PL:
644. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 분홍욕망
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=1].name ; dataList[id=2060221].levelList[level=3].name ; dataList[id=2060221].levelList[level=4].name
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 분홍신
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=1].abName ; dataList[id=2060221].levelList[level=3].abName ; dataList[id=2060221].levelList[level=4].abName
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n속도가 가장 빠른 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=1].desc ; dataList[id=2060221].levelList[level=3].desc ; dataList[id=2060221].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets the unit with the fastest Speed
   PL:
647. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 수비 위력 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2060221].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060221].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 다음 턴에 속박 4 부여
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Binding]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackTail] Inflict 4 [Binding] next turn
   PL:
650. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 4 부여
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 4 부여
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2060221].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 4 [Binding] next turn
   PL:
652. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 5 부여
   źródło: Skills_Ego.json :: dataList[id=2060221].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 643 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Pasywka E.G.O — nazwa] 구속하는 리본
   źródło: Passive_Ego.json :: dataList[id=2060211].name
   limit: do 40 znaków
   EN: Binding Ribbons
   PL:
654. [Pasywka E.G.O — opis] 조작 패널에서 가장 왼쪽의 스킬로 공격하는 대상에게 공격 종료 시 \n다음 턴에 (색욕 완전 공명 수/4)만큼 색욕 취약 부여
   źródło: Passive_Ego.json :: dataList[id=2060211].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [ScarletTakeDamageUp]
   znaczenie tagów: [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: Inflict (Lust A-Reson. / 4) [ScarletTakeDamageUp] next turn on the target of the leftmost Skill on the Dashboard at the Skill's Attack End
   PL:

## E.G.O [20603] Dimension Shredder (차원찢개) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20603`

655. [Karta E.G.O — nazwa] 차원찢개
   źródło: Egos.json :: dataList[id=20603].name
   limit: do 40 znaków
   EN: Dimension Shredder
   PL:
656. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20603].desc
   limit: do 120 znaków
   EN: Hong Lu’s E.G.O Gear
   PL:
657. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 차원찢개
   źródło: Skills_Ego.json :: dataList[id=2060311].levelList[level=1].name ; dataList[id=2060311].levelList[level=3].name
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 길 잃은 승객
   źródło: Skills_Ego.json :: dataList[id=2060311].levelList[level=1].abName ; dataList[id=2060311].levelList[level=3].abName
   limit: do 40 znaków
   EN: Wayward Passenger
   PL:
659. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 가장 뒤에 있는 대상 공격 (일반 전투 한정)\n\n[BeforeAttack] 충전 횟수 3 증가. 다음 턴에 신속 2를 얻음
   źródło: Skills_Ego.json :: dataList[id=2060311].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [Agility]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: Targets the rearmost unit (In regular encounters)\n\n[BeforeAttack] Gain +3 [Charge] Count; Gain 2 [Agility] next turn
   PL:
660. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 1, 차원 균열 2 부여
   źródło: Skills_Ego.json :: dataList[id=2060311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] and 2 [DimensionRift]
   PL:
661. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 가장 뒤에 있는 대상 공격 (일반 전투 한정)\n\n[BeforeAttack] 충전 횟수 5 증가. 다음 턴에 신속 2를 얻음
   źródło: Skills_Ego.json :: dataList[id=2060311].levelList[level=3].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [Agility]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: Targets the rearmost unit (In regular encounters)\n\n[BeforeAttack] Gain +5 [Charge] Count; Gain 2 [Agility] next turn
   PL:
662. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 1, 차원 균열 4 부여
   źródło: Skills_Ego.json :: dataList[id=2060311].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] and 4 [DimensionRift]
   PL:
663. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 차원찢개
   źródło: Skills_Ego.json :: dataList[id=2060321].levelList[level=1].name ; dataList[id=2060321].levelList[level=3].name
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 길 잃은 승객
   źródło: Skills_Ego.json :: dataList[id=2060321].levelList[level=1].abName ; dataList[id=2060321].levelList[level=3].abName
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n현재 체력이 가장 많은 대상 공격\n\n[BeforeAttack] 다음 턴에 신속 2를 얻음.\n충전 횟수 10을 소모하여 적중시 부여하는 취약, 차원 균열 +1
   źródło: Skills_Ego.json :: dataList[id=2060321].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Agility], [Charge], [Vulnerable], [DimensionRift]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Agility] = 신속 / Haste; [Charge] = 충전 / Charge; [Vulnerable] = 취약 / Fragile; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [CantIdentify]\nTargets the unit with the most HP\n\n[BeforeAttack] Gain 2 [Agility] next turn\nSpend 10 [Charge] Count to inflict +1 more [Vulnerable] and [DimensionRift] On Hit with this Skill
   PL:
666. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 1, 차원 균열 3 부여
   źródło: Skills_Ego.json :: dataList[id=2060321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] and 3 [DimensionRift]
   PL:
667. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n현재 체력이 가장 많은 대상 공격\n\n[BeforeAttack] 다음 턴에 신속 <style="highlight">3</style>을 얻음.\n충전 횟수 10을 소모하여 적중시 부여하는 취약, 차원 균열  <style="highlight">+2</style>
   źródło: Skills_Ego.json :: dataList[id=2060321].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Agility], [Charge], [Vulnerable], [DimensionRift]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Agility] = 신속 / Haste; [Charge] = 충전 / Charge; [Vulnerable] = 취약 / Fragile; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [CantIdentify]\nTargets the unit with the most HP\n\n[BeforeAttack] Gain <style="highlight">3</style> [Agility] next turn\nSpend 10 [Charge] Count to inflict <style="highlight">+2</style> more [Vulnerable] and [DimensionRift] On Hit with this Skill
   PL:
668. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 1, 차원 균열 4 부여
   źródło: Skills_Ego.json :: dataList[id=2060321].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Pasywka E.G.O — nazwa] 뒤얽힌 현상 복구
   źródło: Passive_Ego.json :: dataList[id=2060311].name
   limit: do 50 znaków
   EN: Entangled Phenomena Restoration
   PL:
670. [Pasywka E.G.O — opis] 부정적인 효과를 가진 적에게 공격 적중 시 자신의 충전 횟수 1 증가 (턴 당 최대 4회)\n체력이 0이 될 때 충전 횟수를 전부 소모하고, 소모한 값에 비례하여 체력 회복 (전투당 1회 발동. 회복량 최대값: 전체 체력의 25%)
   źródło: Passive_Ego.json :: dataList[id=2060311].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: On Hit against an enemy that has negative status effects, gain +1 [Charge] Count (4 times per turn).\nWhen HP falls to 0, consume all [Charge] Count and heal HP based on Stacks consumed (once per Encounter; max 25% HP)
   PL:

## E.G.O [20604] Soda (소다) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20604`

671. [Karta E.G.O — nazwa] 소다
   źródło: Egos.json :: dataList[id=20604].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20604].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 소다
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=1].name ; dataList[id=2060411].levelList[level=3].name ; dataList[id=2060411].levelList[level=4].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 웰치어스
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=1].abName ; dataList[id=2060411].levelList[level=3].abName ; dataList[id=2060411].levelList[level=4].abName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndSkillHead] 현재 체력 비율이 가장 낮은 아군 2명의 체력 10 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]
   EN: [EndSkillHead] Heal 2 allies with the lowest HP percentages for 10 HP
   PL:
676. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndSkillTail] 정신력이 가장 낮은 아군 2명의 정신력 10 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillTail]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]
   EN: [EndSkillTail] Heal 10 SP for 2 allies with the least SP
   PL:
677. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [EndSkillHead] 현재 체력 비율이 가장 낮은 아군 2명의 체력 12 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]
   EN: [EndSkillHead] Heal 2 allies with the lowest HP percentages for 12 HP
   PL:
678. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [EndSkillTail] 정신력이 가장 낮은 아군 2명의 정신력 12 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillTail]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]
   EN: [EndSkillTail] Heal 12 SP for 2 allies with the least SP
   PL:
679. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalEndSkill] 현재 체력 비율이 가장 낮은 아군 1명의 체력 6 회복, 정신력이 가장 낮은 아군 1명의 정신력 6 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [CriticalEndSkill]
   znaczenie tagów: [CriticalEndSkill] = [크리티컬 공격 종료 시] / [Crit Attack End]
   EN: [CriticalEndSkill] Heal the ally with the lowest HP percentage for 6 HP; Heal the ally with the least SP for 6 SP
   PL:
680. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [EndSkillHead] 현재 체력 비율이 가장 낮은 아군 2명의 체력 15 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]
   EN: [EndSkillHead] Heal 2 allies with the lowest HP percentages for 15 HP
   PL:
681. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkillTail] 정신력이 가장 낮은 아군 2명의 정신력 15 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillTail]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]
   EN: [EndSkillTail] Heal 15 SP for 2 allies with the least SP
   PL:
682. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [CriticalEndSkill] 현재 체력 비율이 가장 낮은 아군 1명의 체력 8 회복, 정신력이 가장 낮은 아군 1명의 정신력 8 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060411].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [CriticalEndSkill]
   znaczenie tagów: [CriticalEndSkill] = [크리티컬 공격 종료 시] / [Crit Attack End]
   EN: [CriticalEndSkill] Heal the ally with the lowest HP percentage for 8 HP; Heal the ally with the least SP for 8 SP
   PL:
683. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 소다
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=1].name ; dataList[id=2060421].levelList[level=3].name ; dataList[id=2060421].levelList[level=4].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 웰치어스
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=1].abName ; dataList[id=2060421].levelList[level=3].abName ; dataList[id=2060421].levelList[level=4].abName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=1].desc ; dataList[id=2060421].levelList[level=3].desc ; dataList[id=2060421].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify] Targets the unit with the least HP
   PL:
686. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2060421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bind next turn
   PL:
687. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor
   PL:
688. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Tremor
   PL:
689. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL:
690. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Tremor
   PL:
691. [Pasywka E.G.O — nazwa] 먼 바다의 갈매기 울음 소리
   źródło: Passive_Ego.json :: dataList[id=2060411].name
   limit: do 60 znaków
   EN: Seagull Squawking Of The Distant Seas
   PL:
692. [Pasywka E.G.O — opis] 적 사망 시 정신력이 가장 낮은 아군 1명의 정신력 1 회복\n적이 사망할 때마다 회복량 2 증가 (최대 9)\n웨이브 시작시 증가된 값 초기화
   źródło: Passive_Ego.json :: dataList[id=2060411].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When an enemy is defeated, the ally that has the least SP heals 1 SP\nWhenever an enemy is defeated, the amount of SP healed increases by 2 (max 9)\nThe amount above is reset at the start of a new wave
   PL:

## E.G.O [20605] Effervescent Corrosion (들끓는 부식) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20605`

693. [Karta E.G.O — nazwa] 들끓는 부식
   źródło: Egos.json :: dataList[id=20605].name
   limit: do 40 znaków
   EN: Effervescent Corrosion
   PL:
694. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20605].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 들끓는 부식
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=1].name ; dataList[id=2060511].levelList[level=3].name ; dataList[id=2060511].levelList[level=4].name
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 걷는 진주
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=1].abName ; dataList[id=2060511].levelList[level=3].abName ; dataList[id=2060511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Ambling Pearl
   PL:
697. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (탐식 공명 수/2)만큼 파열 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2060511].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Rupture by (Gluttony Reson. /2)
   PL:
698. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL:
699. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신의 체력이 최대 체력의 50% 미만이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 50%- HP, Atk Weight +1
   PL:
700. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 탐식 취약 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Gluttony Fragility next turn
   PL:
701. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2060511].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn<style="highlight"></style>
   PL:
702. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신의 체력이 최대 체력의 50% 미만이면, 공격 가중치 +1\n최대 체력의 25% 미만이면, 추가로 공격 가중치 +1
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 50%- HP, Atk Weight +1;\nAt 25%- HP, gain an additional Atk Weight +1
   PL:
703. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 탐식 취약 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Gluttony Fragility next turn
   PL:
704. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 들끓는 부식
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=1].name ; dataList[id=2060521].levelList[level=3].name ; dataList[id=2060521].levelList[level=4].name
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 걷는 진주
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=1].abName ; dataList[id=2060521].levelList[level=3].abName ; dataList[id=2060521].levelList[level=4].abName
   (powtórzenie elementu 696 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n본체 체력이 가장 낮은 대상 공격
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets the unit with the least HP
   PL:
707. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (탐식 공명 수/3)만큼 파열 횟수 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2060521].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Rupture Count by (Gluttony Reson. /3)
   PL:
708. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 자신의 체력 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20% of damage dealt
   PL:
709. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2060521].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2060521].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n본체 체력이 가장 낮은 대상 공격\n[BeforeAttack] 자신의 체력이 최대 체력의 50% 미만이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTarget the unit with the least HP\n[BeforeAttack] At 50%- HP, Atk Weight +1
   PL:
711. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 30%만큼 자신의 체력 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 30% of damage dealt
   PL:
712. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n본체 체력이 가장 낮은 대상 공격\n[BeforeAttack] 자신의 체력이 최대 체력의 50% 미만이면, 공격 가중치 +1\n최대 체력의 25% 미만이면, 추가로 공격 가중치 +1
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTarget the unit with the least HP\n[BeforeAttack] At 50%- HP, Atk Weight +1\nAt 25%- HP, additional Atk Weight +1
   PL:
713. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 자신의 체력 회복
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 50% of damage dealt
   PL:
714. [Pasywka E.G.O — nazwa] 녹색 진액
   źródło: Passive_Ego.json :: dataList[id=2060511].name
   limit: do 40 znaków
   EN: Green Slime
   PL:
715. [Pasywka E.G.O — opis] 피격 시 현재 체력이 최대 체력의 50% 미만이면, 공격자에게 파열 1 부여. (턴 당 가장 많은 탐식 완전 공명 수만큼 발동)
   źródło: Passive_Ego.json :: dataList[id=2060511].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If struck at less than 50% HP, inflict 1 [Burst] on the attacker. (Activates (Highest Gluttony A-Reson) times per turn)
   PL:

## E.G.O [20606] Cavernous Wailing (낮은울음) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20606`

716. [Karta E.G.O — nazwa] 낮은울음
   źródło: Egos.json :: dataList[id=20606].name
   limit: do 40 znaków
   EN: Cavernous Wailing
   PL:
717. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20606].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 낮은울음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=1].name ; dataList[id=2060611].levelList[level=3].name ; dataList[id=2060611].levelList[level=4].name
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 울음 두꺼비
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=1].abName ; dataList[id=2060611].levelList[level=3].abName ; dataList[id=2060611].levelList[level=4].abName
   limit: do 40 znaków
   EN: Blubbering Toad
   PL:
720. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상에게 [Vibration]이 있으면, 피해량 +(대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 20%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has [Vibration], deal +(([Vibration] on target + [Vibration] Count on target)/2)% damage (max 20%)
   PL:
721. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
722. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 대상에게 [Vibration]이 있으면, 피해량 +(대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 <style="highlight">25%</style>)\n<style="highlight">- 최대 공명 수가 4 이상이면, 대신 피해량 +(5 + 대상이 보유한 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 35%)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=3].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has [Vibration], deal +(([Vibration] on target + [Vibration] Count on target)/2)% damage (max <style="highlight">25%</style>)\n<style="highlight">- At 4+ highest Reson., deal +(5 + ([Vibration] on target + [Vibration] Count on target)/2)% damage instead (max 35%)</style>
   PL:
724. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3, <style="highlight">[Vibration] 횟수 2</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and <style="highlight">+2 [Vibration] Count</style>
   PL:
725. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [VibrationEcho] 으로 [Switch_Vibration]</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationEcho], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: <style="highlight">[OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationEcho]</style>
   PL:
726. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2060611].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상에게 [Vibration]이 있으면, 피해량 +(<style="highlight">5</style> + 대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 <style="highlight">30%</style>)\n- 최대 공명 수가 4 이상이면, 대신 피해량 +(<style="highlight">7.5</style> + 대상이 보유한 [Vibration] 위력과 [Vibration] 횟수의 합/<style="highlight">1.5</style>)% (최대 <style="highlight">40%</style>)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has [Vibration], deal +(<style="highlight">5 +</style> ([Vibration] on target + [Vibration] Count on target)/2)% damage (max <style="highlight">30%</style>)\n- At 4+ highest Reson., deal +(<style="highlight">7.5 +</style> ([Vibration] on target + [Vibration] Count on target)/<style="highlight">1.5</style>)% damage instead (max <style="highlight">40%</style>)
   PL:
728. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3, [Vibration] 횟수 <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and <style="highlight">+3</style> [Vibration] Count
   PL:
729. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationEcho] 으로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060611].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationEcho], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationEcho]<style="highlight"></style>
   PL:
730. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 낮은울음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=1].name ; dataList[id=2060621].levelList[level=3].name ; dataList[id=2060621].levelList[level=4].name
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 울음 두꺼비
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=1].abName ; dataList[id=2060621].levelList[level=3].abName ; dataList[id=2060621].levelList[level=4].abName
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Vibration]이 있으면, 피해량 +(대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 25%)\n- 최대 공명 수가 4 이상이면, 피해량 최대 수치가 35%로 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Vibration] = 진동 / Tremor
   EN: [CantIdentify]\nTargets randomly\nIf target has [Vibration], deal +(([Vibration] on target + [Vibration] Count on target)/2)% damage (max 25%)\n- At 4+ highest Reson., raise the above cap to (max 35%)
   PL:
733. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3, [Vibration] 횟수 3 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count
   PL:
734. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Vibration]이 있으면, 피해량 +(대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 <style="highlight">30%</style>)\n- 최대 공명 수가 4 이상이면, <style="highlight">대신 피해량 +(5 + 대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 40%)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=3].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Vibration] = 진동 / Tremor
   EN: [CantIdentify]\nTargets randomly\nIf target has [Vibration], deal +(([Vibration] on target + [Vibration] Count on target)/2)% damage (max <style="highlight">30%</style>)\n- At 4+ highest Reson., <style="highlight">deal +(5 + ([Vibration] on target + [Vibration] Count on target)/2)% damage instead (max 40%)</style>
   PL:
736. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3, [Vibration] 횟수 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count<style="highlight"></style>
   PL:
737. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [VibrationEcho] 으로 [Switch_Vibration]</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
739. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 4 — opis] <style="highlight">[OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
740. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Vibration]이 있으면, 피해량 +(<style="highlight">5</style> + 대상의 [Vibration] 위력과 [Vibration] 횟수의 합/2)% (최대 <style="highlight">40%</style>)\n- 최대 공명 수가 4 이상이면, 대신 피해량 +(<style="highlight">7.5</style> + 대상의 [Vibration] 위력과 [Vibration] 횟수의 합/<style="highlight">1.5</style>)% (최대 <style="highlight">50%</style>)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Vibration] = 진동 / Tremor
   EN: [CantIdentify]\nTargets randomly\nIf target has [Vibration], deal +(<style="highlight">5</style> + ([Vibration] on target + [Vibration] Count on target)/2)% damage (max <style="highlight">40%</style>)\n- At 4+ highest Reson., deal +(<style="highlight">7.5</style> + ([Vibration] on target + [Vibration] Count on target)/<style="highlight">1.5</style>)% damage instead (max <style="highlight">50%</style>)
   PL:
741. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">6</style>, [Vibration] 횟수 <style="highlight">6</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">6</style> [Vibration] and <style="highlight">+6</style> [Vibration] Count
   PL:
742. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationEcho] 으로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 729 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060621].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Pasywka E.G.O — nazwa] 우울감
   źródło: Passive_Ego.json :: dataList[id=2060611].name
   limit: do 40 znaków
   EN: Gloominess
   PL:
746. [Pasywka E.G.O — opis] 자신이 적에게 스킬을 사용하여 [VibrationExplosion] 부여 시, 다음 턴에 [AttackDown] 1, [DefenseDown] 2 부여. (턴 당 최대 3회, E.G.O 스킬 포함)
   źródło: Passive_Ego.json :: dataList[id=2060611].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [AttackDown], [DefenseDown]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When this unit uses a Skill to trigger [VibrationExplosion] on an enemy, inflict 1 [AttackDown] and 2 [DefenseDown] on the enemy next turn. (3 times per turn, including E.G.O Skills)
   PL:
747. [Pasywka E.G.O — podsumowanie] [VibrationExplosion] 부여 시, 다음 턴에 [AttackDown] 1, [DefenseDown] 2 부여
   źródło: Passive_Ego.json :: dataList[id=2060611].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [AttackDown], [DefenseDown]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When triggering [VibrationExplosion], inflict 1 [AttackDown] and 2 [DefenseDown] next turn
   PL:

## E.G.O [20607] Lasso (올가미) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20607`

748. [Karta E.G.O — nazwa] 올가미
   źródło: Egos.json :: dataList[id=20607].name
   limit: do 40 znaków
   EN: Lasso
   PL:
749. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20607].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 올가미
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].name ; dataList[id=2060711].levelList[level=3].name ; dataList[id=2060711].levelList[level=4].name
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 장미 사냥꾼
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].abName ; dataList[id=2060711].levelList[level=3].abName ; dataList[id=2060711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Rose Hunter
   PL:
752. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 [Burst] 7 당 코인 위력 +1 (최대 2)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every 7 [Burst] on target (max 2)
   PL:
753. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Snare] 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Snare]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Snare] = 올가미 / Lasso
   EN: [OnSucceedAttack] Inflict 2 [Snare]
   PL:
754. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 탐식 공명 수 2 당, [Burst] 횟수 1 증가 (최대 3)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count for every 2 Gluttony Reson. (max 3)
   PL:
755. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
757. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">대상과 자신의 속도의 합이 6 이상이면, 코인 위력 +1</style>\n대상의 [Burst] 7 당 코인 위력 +1 (최대 2)\n<style="highlight">[BeforeAttack] 다음 턴에 [Agility] 2 얻음</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [BeforeAttack], [Agility]
   znaczenie tagów: [Burst] = 파열 / Rupture; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Agility] = 신속 / Haste
   EN: <style="highlight">If the sum of this unit and the target's Speed is 6 or greater, Coin Power +1</style>\nCoin Power +1 for every 7 [Burst] on target (max 2)\n<style="highlight">[BeforeAttack] Gain 2 [Agility] next turn
   PL:
758. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Snare] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2060711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Snare]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Snare] = 올가미 / Lasso
   EN: [OnSucceedAttack] Inflict 2 [Snare]<style="highlight"></style>
   PL:
759. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 탐식 공명 수 2 당, [Burst] 횟수 1 증가 (최대 3)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count for every 2 Gluttony Reson. (max 3)<style="highlight"></style>
   PL:
760. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 4, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도/2만큼 [Laceration]을 무작위로 공격 대상에게 나누어 부여 (최대 3)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Randomly inflict [Laceration] equal to (this unit's Speed/2) between the targets (max 3)</style>
   PL:
761. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도/2만큼 [Burst]을 무작위로 공격 대상에게 나누어 부여 (최대 3)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Randomly inflict [Burst] equal to (this unit's Speed/2) between the targets (max 3)</style>
   PL:
762. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상과 자신의 속도의 합이 6 이상이면, 코인 위력 +1\n대상의 [Burst] 7 당 코인 위력 +1 (최대 2)\n[BeforeAttack] 다음 턴에 [Agility] 2 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [BeforeAttack], [Agility]
   znaczenie tagów: [Burst] = 파열 / Rupture; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Agility] = 신속 / Haste
   EN: If the sum of this unit and the target's Speed is 6 or greater, Coin Power +1\nCoin Power +1 for every 7 [Burst] on target (max 2)\n[BeforeAttack] Gain 2 [Agility] next turn<style="highlight"></style>
   PL:
763. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [TakeHpHealReduce] 2 부여</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: <style="highlight">[OnSucceedAttack] Inflict 2 [TakeHpHealReduce] next turn</style>
   PL:
764. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 탐식 공명 수 2 당, [Burst] 횟수 1 증가 (최대 3)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 759 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 4, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도만큼 [Laceration]을 무작위로 공격 대상에게 나누어 부여 (최대 7)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Randomly inflict [Laceration] equal to this unit's Speed between the targets (max 7)</style>
   PL:
766. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도만큼 [Burst]을 무작위로 공격 대상에게 나누어 부여 (최대 7)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060711].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Randomly inflict [Burst] equal to this unit's Speed between the targets (max 7)</style>
   PL:
767. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 올가미
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].name ; dataList[id=2060721].levelList[level=3].name ; dataList[id=2060721].levelList[level=4].name
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 장미 사냥꾼
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].abName ; dataList[id=2060721].levelList[level=3].abName ; dataList[id=2060721].levelList[level=4].abName
   (powtórzenie elementu 751 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 [Burst] 7 당 코인 위력 +1 (최대 2)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Burst]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Burst] = 파열 / Rupture
   EN: [CantIdentify]\nTargets randomly\nCoin Power +1 for every 7 [Burst] on target (max 2)
   PL:
770. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Snare] 3 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Snare]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Snare] = 올가미 / Lasso
   EN: [OnSucceedAttack] Inflict 3 [Snare]
   PL:
771. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
773. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1 당 피해량 +1% (최대 20%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal +1% damage for every [Laceration] on target (Max 20%)
   PL:
774. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 1 당 피해량 +1% (최대 20%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +1% damage for every [Burst] on target (Max 20%)
   PL:
775. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">대상과 자신의 속도의 합이 6 이상이면, 코인 위력 +1</style>\n대상의 [Burst] 7 당 코인 위력 +1 (최대 2)\n<style="highlight">[BeforeAttack] 다음 턴에 [Agility] 2 얻음</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Burst], [BeforeAttack], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Burst] = 파열 / Rupture; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">If the sum of this unit and the target's Speed is 6 or greater, Coin Power +1</style>\nCoin Power +1 for every 7 [Burst] on target (max 2)\n<style="highlight">[BeforeAttack] Gain 2 [Agility] next turn</style>
   PL:
776. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Snare] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Snare]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Snare] = 올가미 / Lasso
   EN: [OnSucceedAttack] Inflict 3 [Snare]<style="highlight"></style>
   PL:
777. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL:
778. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count<style="highlight"></style>
   PL:
779. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1 당 피해량 +1% <style="highlight">(최대 30%)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal +1% damage for every [Laceration] on target <style="highlight">(max 30%)</style>
   PL:
780. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 1 당 피해량 +1% <style="highlight">(최대 30%)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +1% damage for every [Burst] on target <style="highlight">(max 30%)</style>
   PL:
781. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상과 자신의 속도의 합이 6 이상이면, 코인 위력 +1\n대상의 [Burst] 7 당 코인 위력 +1 (최대 2)\n[BeforeAttack] 다음 턴에 [Agility] 2 얻음\n<style="highlight">[BeforeAttack] 탐식 또는 색욕 공명이 4 이상이면 공격 가중치 +1</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Burst], [BeforeAttack], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Burst] = 파열 / Rupture; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets randomly\nIf the sum of this unit and the target's Speed is 6 or greater, Coin Power +1\nCoin Power +1 for every 7 [Burst] on target (max 2)\n[BeforeAttack] Gain 2 [Agility] next turn\n<style="highlight">[BeforeAttack] At 4+ Gluttony or Lust Reson., gain +1 Atk Weight</style>
   PL:
782. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [TakeHpHealReduce] 3 부여</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: <style="highlight">[OnSucceedAttack] Inflict 3 [TakeHpHealReduce] next turn</style>
   PL:
783. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 777 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 778 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1 당 피해량 +1% (최대 30%)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal +1% damage for every [Laceration] on target (max 30%)<style="highlight"></style>
   PL:
786. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 1 당 피해량 +1% (최대 30%)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060721].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +1% damage for every [Burst] on target (max 30%)<style="highlight"></style>
   PL:
787. [Pasywka E.G.O — nazwa] 사냥의 시간
   źródło: Passive_Ego.json :: dataList[id=2060711].name
   limit: do 40 znaków
   EN: Time to Hunt
   PL:
788. [Pasywka E.G.O — opis] [Burst], [Laceration] 피해로 적 또는 아군이 사망하면, 무작위 적 1명에게 [Snare] 2를 부여하고, 다음 턴에 [Agility] 1 얻음 (턴 당 1회)
   źródło: Passive_Ego.json :: dataList[id=2060711].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Burst], [Laceration], [Snare], [Agility]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed; [Snare] = 올가미 / Lasso; [Agility] = 신속 / Haste
   EN: If an enemy or an ally is killed due to [Burst] or [Laceration] damage, inflict 2 [Snare] against a random enemy, and gain 1 [Agility] next turn (once per turn)
   PL:

## E.G.O [20608] Tears of the Tarnished Blood [汚血泣淚] (오혈읍루 [汚血泣淚]) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20608`

789. [Karta E.G.O — nazwa] 오혈읍루 [汚血泣淚]
   źródło: Egos.json :: dataList[id=20608].name
   limit: do 50 znaków
   EN: Tears of the Tarnished Blood [汚血泣淚]
   PL:
790. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20608].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 오혈읍루 - 시[始]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060811].levelList[level=1].name ; dataList[id=2060811].levelList[level=3].name ; dataList[id=2060811].levelList[level=4].name
   limit: do 60 znaków
   EN: Tears of the Tarnished Blood - Inception [始]
   PL:
792. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 응룡
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060811].levelList[level=1].abName ; dataList[id=2060811].levelList[level=3].abName ; dataList[id=2060811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Yinglong
   PL:
793. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [CantDuel]\n대상 수비 스킬 무시\n이 스킬은 적에게 적중하지 않음\n[EndSkill] [DragonLance] 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060811].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [EndSkill], [DragonLance]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [EndSkill] = [공격 종료시] / [Attack End]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]
   EN: [CantDuel]\nIgnores the target's Defense Skill\nThis Skill does not hit an enemy\n[EndSkill] Gain [DragonLance]
   PL:
794. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] 이 스킬의 최종 위력만큼 자신이 고정 피해를 받음\n- 이 피해로 흐트러지거나 체력이 1 미만으로 감소하지 않음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060811].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This unit takes fixed damage by this Skill's Final Power\n- This damage does not Stagger or reduce this unit's HP below 1
   PL:
