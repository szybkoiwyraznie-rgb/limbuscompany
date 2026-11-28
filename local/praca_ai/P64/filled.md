# Paczka AI P64 (Fala 3 · 3B) — Karty E.G.O, umiejętności i pasywki (część 4/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P64_3b_karty_ego_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P64_3b_karty_ego_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## E.G.O [20908] Indicant's Trial (지정 재판) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20908`

1. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 3 — opis] [EnemyKill] 현재 체력 비율이 가장 낮은 아군 (1 + 최대 공명 수)명에게 [CrimsonResultUp] 1, [CrimsonDamageUp] 1 부여 (최대 <style="highlight">5</style>명, 스킬당 1회)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [CrimsonResultUp], [CrimsonDamageUp]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [CrimsonResultUp] = 분노 위력 증가 / Wrath Power Up; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: [EnemyKill] Apply 1 [CrimsonResultUp] and 1 [CrimsonDamageUp] to (1 + highest Reson.) allies with the least HP percentages (max <style="highlight">5</style> allies; once per Skill)
   PL: [EnemyKill] nakłada 1 [CrimsonResultUp] i 1 [CrimsonDamageUp] na (1 + najwyższy Rezonans) sojuszników z najniższym aktualnym procentem HP (maks. <style="highlight">5</style> sojuszników, 1 raz na Umiejętność)
2. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] <style="highlight">10</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict <style="highlight">10</style> [Combustion]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada <style="highlight">10</style> [Combustion]
3. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[UnBrokenCoinOnSucceedAttack] [Combustion] 횟수 1 증가</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[UnBrokenCoinOnSucceedAttack] Inflict +1 [Combustion] Count</style>
   PL: <style="highlight">[UnBrokenCoinOnSucceedAttack] nakłada +1 Licznika [Combustion]</style>
4. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 메인 타겟이면, [BirdCage] (1 + 분노 공명 수)만큼 부여 (최대 <style="highlight">5</style>)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [BirdCage]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BirdCage] = 달궈진 새장 / Searing Birdcage
   EN: [UnBrokenCoinOnSucceedAttack] If this hits the main target, inflict (1 + Wrath Reson.) [BirdCage] on main target (max <style="highlight">5</style>)
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli celem jest cel główny, nakłada (1 + Rezonans Gniewu) [BirdCage] (maks. <style="highlight">5</style>)
5. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] 메인 타겟의 [Combustion] 위력당 메인 타겟에게 가하는 피해량 +<style="highlight">2</style>% (최대 <style="highlight">100</style>%)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +<style="highlight">2</style>% damage on the main target for every [Combustion] Potency on the main target (max <style="highlight">100</style>%)
   PL: zadaje +<style="highlight">2</style>% obrażeń głównemu celowi za każde 1 Siły [Combustion] głównego celu (maks. <style="highlight">100</style>%)
6. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [EnemyKill] 현재 체력 비율이 가장 낮은 아군 (1 + 최대 공명 수)명에게 [CrimsonResultUp] 1, [CrimsonDamageUp] 1 부여 (최대 <style="highlight">6</style>명, 스킬당 1회)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [CrimsonResultUp], [CrimsonDamageUp]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [CrimsonResultUp] = 분노 위력 증가 / Wrath Power Up; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: [EnemyKill] Apply 1 [CrimsonResultUp] and 1 [CrimsonDamageUp] to (1 + highest Reson.) allies with the least HP percentages (max <style="highlight">6</style> allies; once per Skill)
   PL: [EnemyKill] nakłada 1 [CrimsonResultUp] i 1 [CrimsonDamageUp] na (1 + najwyższy Rezonans) sojuszników z najniższym aktualnym procentem HP (maks. <style="highlight">6</style> sojuszników, 1 raz na Umiejętność)
7. [Pasywka E.G.O — nazwa] 작열유희
   źródło: Passive_Ego.json :: dataList[id=2090811].name
   limit: do 40 znaków
   EN: Blazing Amusement
   PL: Płonąca Rozrywka
8. [Pasywka E.G.O — opis] [Combustion] 횟수가 10 이상인 대상 사망 시 모든 적에게 대상의 [Combustion] 횟수를 나누어 부여하고, 자신의 정신력 8 회복 (집중 전투인 경우 모든 부위에 나누어 부여. 대상당 최대 부여량: 3, 턴 당 2회 발동)\n- 자신의 정신력이 최대치면, 대신 정신력이 가장 낮은 아군 1명 정신력 5 회복
   źródło: Passive_Ego.json :: dataList[id=2090811].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When a target that has 10+ [Combustion] Count is defeated, inflict the [Combustion] Count on target between all enemies and heal 8 SP on self (in Focused Encounters, between all Parts; 3 max per target, 2 times per turn)\n- At max SP, heal 5 SP for 1 ally that has the least SP instead
   PL: po pokonaniu celu posiadającego 10+ Licznika [Combustion] rozdziela Licznik [Combustion] celu między wszystkich wrogów i odzyskuje 8 SP (w walkach skupionych rozdziela między wszystkie Części; maks. 3 na cel, uruchamia się 2 razy na turę)\n- przy maksymalnym SP zamiast tego odzyskuje 5 SP dla 1 sojusznika z najniższym SP

## E.G.O [20909] Into the Sunset (노을 속으로) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20909`

9. [Karta E.G.O — nazwa] 노을 속으로
   źródło: Egos.json :: dataList[id=20909].name
   limit: do 40 znaków
   EN: Into the Sunset
   PL: W Zmierzch
10. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20909].desc
   limit: do 120 znaków
   EN: Rodion’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Rodion
11. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 노을 속으로
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=1].name ; dataList[id=2090911].levelList[level=3].name ; dataList[id=2090911].levelList[level=4].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 노을 나그네
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=1].abName ; dataList[id=2090911].levelList[level=3].abName ; dataList[id=2090911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Sunset Wayfarer
   PL: Wędrowiec Zmierzchu
13. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 5%만큼 회복하고 [ScarletMothRodion] 2 부여 (최소 체력 회복량: 1)\n- (색욕 공명 수 - 1) 만큼 회복 대상 수 증가 (최대 2명)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [ScarletMothRodion]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ScarletMothRodion] = 주홍 나방 / Scarlet Moth
   EN: [EndSkill] Heal 5% HP for 2 allies that have the lowest current HP percentages and apply 2 [ScarletMothRodion] to the said allies (minimum HP healed: 1)\n- Heal additional allies equal to (Lust Reson. - 1) (max 2 allies)
   PL: [EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o 5% Maks. HP i nakłada 2 [ScarletMothRodion] na tych sojuszników (minimalna ilość leczonego HP: 1)\n- liczba leczonych sojuszników rośnie o (Rezonans Żądzy - 1) (maks. 2 sojuszników)
14. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]
15. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
16. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">[WhenUse] 모든 대상의 [Combustion]과 [Laceration]의 합 6당 합 위력 +1 (최대 2)</style>\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 <style="highlight">8%</style>만큼 회복하고 [ScarletMothRodion] 2 부여 (최소 체력 회복량: 1)\n- (색욕 공명 수 - 1) 만큼 회복 대상 수 증가 (최대 2명)\n<style="highlight">- 회복 대상이 색욕 속성 스킬을 장착했으면, 정신력 3 회복</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=3].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Laceration], [EndSkill], [ScarletMothRodion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [ScarletMothRodion] = 주홍 나방 / Scarlet Moth
   EN: <style="highlight">[WhenUse] Clash Power +1 for every 6 ([Combustion] + [Laceration]) on all targets (max 2)</style>\n[EndSkill] Heal <style="highlight">8%</style> HP for 2 allies that have the lowest current HP percentages and apply 2 [ScarletMothRodion] to the said allies (minimum HP healed: 1)\n- Heal additional allies equal to (Lust Reson. - 1) (max 2 allies)\n<style="highlight">- If the healed ally has equipped a Lust Skill, heal 3 SP on the said ally as well</style>
   PL: <style="highlight">[WhenUse] Moc Walce +1 za każde 6 (suma [Combustion] i [Laceration]) na wszystkich celach (maks. 2)</style>\n[EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o <style="highlight">8%</style> Maks. HP i nakłada 2 [ScarletMothRodion] na tych sojuszników (minimalna ilość leczonego HP: 1)\n- liczba leczonych sojuszników rośnie o (Rezonans Żądzy - 1) (maks. 2 sojuszników)\n<style="highlight">- jeżeli leczony sojusznik ma wyposażoną Umiejętność Żądzy, dodatkowo odzyskuje 3 SP</style>
17. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Combustion]
18. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Laceration]
19. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [WhenUse] 모든 대상의 [Combustion]과 [Laceration]의 합 6당 합 위력 +1 (최대 2)\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 <style="highlight">10%</style>만큼 회복하고 [ScarletMothRodion] 2 부여 (최소 체력 회복량: 1)\n- (색욕 공명 수 - 1) 만큼 회복 대상 수 증가 (최대 2명)\n- 회복 대상이 색욕 속성 스킬을 장착했으면, 정신력 <style="highlight">6</style> 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Laceration], [EndSkill], [ScarletMothRodion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [ScarletMothRodion] = 주홍 나방 / Scarlet Moth
   EN: [WhenUse] Clash Power +1 for every 6 ([Combustion] + [Laceration]) on all targets (max 2)\n[EndSkill] Heal <style="highlight">10%</style> HP for 2 allies that have the lowest current HP percentages and apply 2 [ScarletMothRodion] to the said allies (minimum HP healed: 1)\n- Heal additional allies equal to (Lust Reson. - 1) (max 2 allies)\n- If the healed ally has equipped a Lust Skill, heal <style="highlight">6</style> SP on the said ally as well
   PL: [WhenUse] Moc Walce +1 za każde 6 (suma [Combustion] i [Laceration]) na wszystkich celach (maks. 2)\n[EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o <style="highlight">10%</style> Maks. HP i nakłada 2 [ScarletMothRodion] na tych sojuszników (minimalna ilość leczonego HP: 1)\n- liczba leczonych sojuszników rośnie o (Rezonans Żądzy - 1) (maks. 2 sojuszników)\n- jeżeli leczony sojusznik ma wyposażoną Umiejętność Żądzy, dodatkowo odzyskuje <style="highlight">6</style> SP
20. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]<style="highlight"></style>
21. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]<style="highlight"></style>
22. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[EndCoin] 적중한 대상에게 다음 턴에 [CrimsonTakeDamageUp] 1, [ScarletTakeDamageUp] 1 부여</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090911].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndCoin], [CrimsonTakeDamageUp], [ScarletTakeDamageUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: <style="highlight">[EndCoin] Inflict 1 [CrimsonTakeDamageUp] and 1 [ScarletTakeDamageUp] next turn on target hit</style>
   PL: <style="highlight">[EndCoin] następnej tury nakłada 1 [CrimsonTakeDamageUp] i 1 [ScarletTakeDamageUp] trafionemu celowi</style>
23. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 노을 속으로
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].name ; dataList[id=2090921].levelList[level=3].name ; dataList[id=2090921].levelList[level=4].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 노을 나그네
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].abName ; dataList[id=2090921].levelList[level=3].abName ; dataList[id=2090921].levelList[level=4].abName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 모든 대상의 [Combustion]과 [Laceration]의 합 4당 피해량 +5% (최대 15%)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -12)\n[EndSkill] 무작위 아군에게 [ScarletMothRodion] 1씩 3번 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Combustion], [Laceration], [EndSkill], [ScarletMothRodion]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [ScarletMothRodion] = 주홍 나방 / Scarlet Moth
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Deal +5% damage for every 4 ([Combustion] + [Laceration]) on all targets (max 15%)\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -12)\n[EndSkill] Apply 1 [ScarletMothRodion] 3 times between random allies
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zadaje +5% obrażeń za każde 4 (suma [Combustion] i [Laceration]) na wszystkich celach (maks. 15%)\n[BeforeAttack] Moc Bazowa -6 za każdą zniszczoną Monetę (maks. -12)\n[EndSkill] rozdziela 3 razy po 1 [ScarletMothRodion] między losowych sojuszników
26. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2090921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
27. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
28. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2090921].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1
29. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 4 — opis] [EndCoin] 적중한 대상에게 다음 턴에 [CrimsonTakeDamageUp] 1 부여 (턴당 1회)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#0].coindescs[#3].desc ; dataList[id=2090921].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2090921].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [CrimsonTakeDamageUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: [EndCoin] Inflict 1 [CrimsonTakeDamageUp] next turn on target hit (once per turn)
   PL: [EndCoin] następnej tury nakłada 1 [CrimsonTakeDamageUp] trafionemu celowi (1 raz na turę)
30. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2090921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2090921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
32. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=2090921].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
33. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 4 — opis] [EndCoin] 적중한 대상에게 다음 턴에 [ScarletTakeDamageUp] 1 부여 (턴당 1회)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=1].coinlist[#1].coindescs[#3].desc ; dataList[id=2090921].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=2090921].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [ScarletTakeDamageUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [EndCoin] Inflict 1 [ScarletTakeDamageUp] next turn on target hit (once per turn)
   PL: [EndCoin] następnej tury nakłada 1 [ScarletTakeDamageUp] trafionemu celowi (1 raz na turę)
34. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 모든 대상의 [Combustion]과 [Laceration]의 합 4당 피해량 +5% (최대 15%)\n<style="highlight">- 분노 완전 공명이나 색욕 완전 공명이 있으면, 추가로 피해량 +10%</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -12)\n[EndSkill] 무작위 아군에게 [ScarletMothRodion] 1씩 <style="highlight">4번</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=3].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Combustion], [Laceration], [EndSkill], [ScarletMothRodion]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [ScarletMothRodion] = 주홍 나방 / Scarlet Moth
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Deal +5% damage for every 4 ([Combustion] + [Laceration]) on all targets (max 15%)\n<style="highlight">- If there is a Wrath A-Reson. or a Lust A-Reson., deal an additional +10% damage</style>\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -12)\n[EndSkill] Apply 1 [ScarletMothRodion] <style="highlight">4</style> times between random allies
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zadaje +5% obrażeń za każde 4 (suma [Combustion] i [Laceration]) na wszystkich celach (maks. 15%)\n<style="highlight">- przy Rezonansie Absolutnym Gniewu lub Rezonansie Absolutnym Żądzy dodatkowo zadaje +10% obrażeń</style>\n[BeforeAttack] Moc Bazowa -6 za każdą zniszczoną Monetę (maks. -12)\n[EndSkill] rozdziela 1 [ScarletMothRodion] <style="highlight">4 razy</style> między losowych sojuszników
35. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
36. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Laceration]
37. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 모든 대상의 [Combustion]과 [Laceration]의 합 4당 피해량 <style="highlight">+10% (최대 30%)</style>\n- 분노 완전 공명이나 색욕 완전 공명이 있으면, 추가로 피해량 <style="highlight">+20%</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 <style="highlight">-5 (최대 -10)</style>\n[EndSkill] 무작위 아군에게 [ScarletMothRodion] 1씩 <style="highlight">5번</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Combustion], [Laceration], [EndSkill], [ScarletMothRodion]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [ScarletMothRodion] = 주홍 나방 / Scarlet Moth
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">[BeforeAttack] Deal +10% damage for every 4 ([Combustion] + [Laceration]) on all targets (max 30%)</style>\n- If there is a Wrath A-Reson. or a Lust A-Reson., deal an additional <style="highlight">+20%</style>damage\n<style="highlight">[BeforeAttack] Base Power -5 for every Cracked Coin (max -10)</style>\n[EndSkill] Apply 1 [ScarletMothRodion] <style="highlight">5</style> times between random allies
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zadaje <style="highlight">+10% (maks. 30%)</style> obrażeń za każde 4 (suma [Combustion] i [Laceration]) na wszystkich celach\n- przy Rezonansie Absolutnym Gniewu lub Rezonansie Absolutnym Żądzy dodatkowo zadaje <style="highlight">+20%</style> obrażeń\n[BeforeAttack] Moc Bazowa <style="highlight">-5 (maks. -10)</style> za każdą zniszczoną Monetę\n[EndSkill] rozdziela 1 [ScarletMothRodion] <style="highlight">5 razy</style> między losowych sojuszników
38. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]<style="highlight"></style>
39. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o <style="highlight">2</style>
40. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]<style="highlight"></style>
41. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090921].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o <style="highlight">2</style>
42. [Pasywka E.G.O — nazwa] 나방과 나비의 차이
   źródło: Passive_Ego.json :: dataList[id=2090911].name
   limit: do 60 znaków
   EN: What Distinguishes Moths from Butterflies
   PL: Czym Ćmy Różnią się od Motyli
43. [Pasywka E.G.O — opis] 조작 패널에서 가장 왼쪽에 장착한 자신의 기본 공격 스킬이\n분노 또는 색욕 속성 스킬이면,\n해당 스킬로 메인 타겟에게 입힌 피해량의 30%만큼\n무작위 적 1명에게 공격 종료시 해당 스킬 죄악 속성 피해를 입힘 (최대 피해 30, 집중 전투의 경우, 부위로 판정)\n\n위 효과로 최대 피해를 입혔으면 다음 턴에 해당 죄악 속성 <noparse>피해량 증가</noparse> 1 얻고 2턴 동안 위 효과가 발동되지 않음
   źródło: Passive_Ego.json :: dataList[id=2090911].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: If this unit's leftmost Base Attack Skill on the Dashboard is a Wrath or a Lust Skill, at Attack End, deal 30% of the damage dealt against the main target with that Skill as its corresponding Affinity damage to a random enemy (max 30 damage; for Focused Encounters, a Part)\n\nIf this unit dealt the maximum possible damage with the above effect, gain 1 Affinity DMG Up for the corresponding Affinity next turn, and disable the above effect from triggering for 2 turns
   PL: jeżeli skrajna lewa Podstawowa Umiejętność Ataku tej jednostki na Pulpicie jest Umiejętnością Gniewu lub Żądzy, na koniec ataku zadaje 1 losowemu wrogowi 30% obrażeń zadanych głównemu celowi tą Umiejętnością jako obrażenia odpowiadającego Grzechu (maks. 30 obrażeń; w walkach skupionych per Część)\n\njeżeli tym efektem zadała maksymalne możliwe obrażenia, następnej tury zyskuje 1 zwiększenia zadawanych obrażeń odpowiadającego Grzechu, a powyższy efekt nie może się uruchomić przez 2 tury

## E.G.O [20910] Mirror-touch (거울촉각) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20910`

44. [Karta E.G.O — nazwa] 거울촉각
   źródło: Egos.json :: dataList[id=20910].name
   limit: do 40 znaków
   EN: Mirror-touch
   PL: Lustrzany Dotyk
45. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20910].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 거울촉각
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].name ; dataList[id=2091011].levelList[level=3].name ; dataList[id=2091011].levelList[level=4].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 길 잃은 마음
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].abName ; dataList[id=2091011].levelList[level=3].abName ; dataList[id=2091011].levelList[level=4].abName
   limit: do 40 znaków
   EN: Wandering Heart
   PL: Błądzące Serce
48. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 자신의 [Breath] 위력과 메인 타겟의 [Vibration] 위력의 합 6당, 합 위력 +1 (최대 2)\n[BeforeAttack] (2 + 최대 공명 수)만큼 [Breath] 얻음 (최대 8)\n[BeforeAttack] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 공격 대상 중 무작위 적에게 (1 + 최대 공명 수)만큼 [EmpathicDistressAlly]을 1씩 나누어 부여 (최대 5)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Vibration], [BeforeAttack], [EndSkill], [EmpathicDistressAlly]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [EmpathicDistressAlly] = 감각 균열 / Fracturing of the Senses
   EN: Clash Power +1 for every 6 ([Breath] Potency on self + [Vibration] Potency on the main target) (max 2)\n[BeforeAttack] Gain (2 + highest Reson.) [Breath] (max 8)\n[BeforeAttack] Gain +2 [Breath] Count\n[EndSkill] Randomly inflict (1 + highest Reson.) [EmpathicDistressAlly] between targets, 1 Stack at a time (max 5)
   PL: Moc Walki +1 za każde 6 (Siła [Breath] tej jednostki + Siła [Vibration] głównego celu) (maks. 2)\n[BeforeAttack] zyskuje (2 + najwyższy Rezonans) [Breath] (maks. 8)\n[BeforeAttack] zyskuje +2 Licznika [Breath]\n[EndSkill] rozdziela (1 + najwyższy Rezonans) Liczników [EmpathicDistressAlly] między losowych celów ataku, po 1 na raz (maks. 5)
49. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
50. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
51. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2091011].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2091011].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown]
   PL: [OnSucceedAttack] nakłada 2 [AttackDown]
52. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2091011].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2091011].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
53. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 자신의 [Breath] 위력과 메인 타겟의 [Vibration] 위력의 합 6당, 합 위력 +1 (최대 <style="highlight">3</style>)\n[BeforeAttack] (<style="highlight">3</style> + 최대 공명 수)만큼 [Breath] 얻음 (최대 8)\n[BeforeAttack] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가\n[EndSkill] 공격 대상 중 무작위 적에게 (1 + 최대 공명 수)만큼 [EmpathicDistressAlly]을 1씩 나누어 부여 (최대 5)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=3].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Vibration], [BeforeAttack], [EndSkill], [EmpathicDistressAlly]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [EmpathicDistressAlly] = 감각 균열 / Fracturing of the Senses
   EN: Clash Power +1 for every 6 ([Breath] Potency on self + [Vibration] Potency on the main target) (max <style="highlight">3</style>)\n[BeforeAttack] Gain (<style="highlight">3</style> + highest Reson.) [Breath] (max 8)\n[BeforeAttack] Gain +<style="highlight">3</style> [Breath] Count\n[EndSkill] Randomly inflict (1 + highest Reson.) [EmpathicDistressAlly] between targets, 1 Stack at a time (max 5)
   PL: Moc Walki +1 za każde 6 (Siła [Breath] tej jednostki + Siła [Vibration] głównego celu) (maks. <style="highlight">3</style>)\n[BeforeAttack] zyskuje (<style="highlight">3</style> + najwyższy Rezonans) [Breath] (maks. 8)\n[BeforeAttack] zyskuje +<style="highlight">3</style> Licznika [Breath]\n[EndSkill] rozdziela (1 + najwyższy Rezonans) Liczników [EmpathicDistressAlly] między losowych celów ataku, po 1 na raz (maks. 5)
54. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
55. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +<style="highlight">2</style> Licznika [Vibration]
56. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 자신의 [Breath] 위력과 메인 타겟의 [Vibration] 위력의 합 6당, 합 위력 +1 (최대 <style="highlight">4</style>)\n[BeforeAttack] (<style="highlight">4</style> + 최대 공명 수)만큼 [Breath] 얻음 (최대 8)\n[BeforeAttack] 자신의 [Breath] 횟수 <style="highlight">4</style> 증가\n[EndSkill] 공격 대상 중 무작위 적에게 (1 + 최대 공명 수)만큼 [EmpathicDistressAlly]을 1씩 나누어 부여 (최대 5)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Vibration], [BeforeAttack], [EndSkill], [EmpathicDistressAlly]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [EmpathicDistressAlly] = 감각 균열 / Fracturing of the Senses
   EN: Clash Power +1 for every 6 ([Breath] Potency on self + [Vibration] Potency on the main target) (max <style="highlight">4</style>)\n[BeforeAttack] Gain (<style="highlight">4</style> + highest Reson.) [Breath] (max 8)\n[BeforeAttack] Gain +<style="highlight">4</style> [Breath] Count\n[EndSkill] Randomly inflict (1 + highest Reson.) [EmpathicDistressAlly] between targets, 1 Stack at a time (max 5)
   PL: Moc Walki +1 za każde 6 (Siła [Breath] tej jednostki + Siła [Vibration] głównego celu) (maks. <style="highlight">4</style>)\n[BeforeAttack] zyskuje (<style="highlight">4</style> + najwyższy Rezonans) [Breath] (maks. 8)\n[BeforeAttack] zyskuje +<style="highlight">4</style> Licznika [Breath]\n[EndSkill] rozdziela (1 + najwyższy Rezonans) Liczników [EmpathicDistressAlly] między losowych celów ataku, po 1 na raz (maks. 5)
57. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Vibration]
58. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091011].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] celu o <style="highlight">3</style>
59. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 거울촉각
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].name ; dataList[id=2091021].levelList[level=3].name ; dataList[id=2091021].levelList[level=4].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 길 잃은 마음
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].abName ; dataList[id=2091021].levelList[level=3].abName ; dataList[id=2091021].levelList[level=4].abName
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [Breath] 위력과 메인 타겟의 [Vibration] 위력의 합 6당, 합 위력 +1 (최대 2)\n[BeforeAttack] (2 + 최대 공명 수)만큼 [Breath] 얻음 (최대 10)\n[BeforeAttack] 자신의 [Breath] 횟수 2 증가\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -4 (최대 -12)\n[BeforeAttack] 자신의 [Breath] 횟수가 10 이상이면, 자신의 [Breath] 횟수를 4 소모하고, 메인 타겟에게 가하는 크리티컬 피해량 +20%\n[EndSkill] 공격 대상 중 무작위 적에게 (1 + 최대 공명 수)만큼 [EmpathicDistressAlly]을 1씩 나누어 부여 (최대 5)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Breath], [Vibration], [BeforeAttack], [EndSkill], [EmpathicDistressAlly]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [EmpathicDistressAlly] = 감각 균열 / Fracturing of the Senses
   EN: [CantIdentify]\nTargets randomly\nClash Power +1 for every 6 ([Breath] Potency on self + [Vibration] Potency on the main target) (max 2)\n[BeforeAttack] Gain (2 + highest Reson.) [Breath] (max 10)\n[BeforeAttack] Gain +2 [Breath] Count\n[BeforeAttack] Base Power -4 for every Cracked Coin (max -12)\n[BeforeAttack] At 10+ [Breath] Count, consume 4 [Breath] Count on self and deal +20% damage on Critical Hit against the main target\n[EndSkill] Randomly inflict (1 + highest Reson.) [EmpathicDistressAlly] between targets, 1 Stack at a time (max 5)
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Walki +1 za każde 6 (Siła [Breath] tej jednostki + Siła [Vibration] głównego celu) (maks. 2)\n[BeforeAttack] zyskuje (2 + najwyższy Rezonans) [Breath] (maks. 10)\n[BeforeAttack] zyskuje +2 Licznika [Breath]\n[BeforeAttack] Moc Bazowa -4 za każdą zniszczoną Monetę (maks. -12)\n[BeforeAttack] przy 10+ Licznika [Breath] zużywa 4 Licznika [Breath] i zadaje +20% obrażeń krytycznych głównemu celowi\n[EndSkill] rozdziela (1 + najwyższy Rezonans) Liczników [EmpathicDistressAlly] między losowych celów ataku, po 1 na raz (maks. 5)
62. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2091021].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2091021].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
64. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2091021].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2091021].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 4 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#0].coindescs[#3].desc ; dataList[id=2091021].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2091021].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 4+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli cel ma 4+ Licznika [Vibration], wyzwala [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
66. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2091021].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2091021].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2091021].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2091021].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 4 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=2091021].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=2091021].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2091021].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2091021].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 3 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown]
   PL: [OnSucceedAttack] nakłada 3 [AttackDown]
71. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [Breath] 위력과 메인 타겟의 [Vibration] 위력의 합 6당, 합 위력 +1 (최대 <style="highlight">3</style>)\n[BeforeAttack] (<style="highlight">3</style> + 최대 공명 수)만큼 [Breath] 얻음 (최대 10)\n[BeforeAttack] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -4 (최대 -12)\n[BeforeAttack] 자신의 [Breath] 횟수가 10 이상이면, 자신의 [Breath] 횟수를 4 소모하고, 메인 타겟에게 가하는 크리티컬 피해량 +<style="highlight">30</style>%\n[EndSkill] 공격 대상 중 무작위 적에게 (1 + 최대 공명 수)만큼 [EmpathicDistressAlly]을 1씩 나누어 부여 (최대 5)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=3].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Breath], [Vibration], [BeforeAttack], [EndSkill], [EmpathicDistressAlly]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [EmpathicDistressAlly] = 감각 균열 / Fracturing of the Senses
   EN: [CantIdentify]\nTargets randomly\nClash Power +1 for every 6 ([Breath] Potency on self + [Vibration] Potency on the main target) (max <style="highlight">3</style>)\n[BeforeAttack] Gain (<style="highlight">3</style> + highest Reson.) [Breath] (max 10)\n[BeforeAttack] Gain +<style="highlight">3</style> [Breath] Count\n[BeforeAttack] Base Power -4 for every Cracked Coin (max -12)\n[BeforeAttack] At 10+ [Breath] Count, consume 4 [Breath] Count on self and deal +<style="highlight">30</style>% damage on Critical Hit against the main target\n[EndSkill] Randomly inflict (1 + highest Reson.) [EmpathicDistressAlly] between targets, 1 Stack at a time (max 5)
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Walki +1 za każde 6 (Siła [Breath] tej jednostki + Siła [Vibration] głównego celu) (maks. <style="highlight">3</style>)\n[BeforeAttack] zyskuje (<style="highlight">3</style> + najwyższy Rezonans) [Breath] (maks. 10)\n[BeforeAttack] zyskuje +<style="highlight">3</style> Licznika [Breath]\n[BeforeAttack] Moc Bazowa -4 za każdą zniszczoną Monetę (maks. -12)\n[BeforeAttack] przy 10+ Licznika [Breath] zużywa 4 Licznika [Breath] i zadaje +<style="highlight">30</style>% obrażeń krytycznych głównemu celowi\n[EndSkill] rozdziela (1 + najwyższy Rezonans) Liczników [EmpathicDistressAlly] między losowych celów ataku, po 1 na raz (maks. 5)
73. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 횟수 1 증가</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Vibration] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada +1 Licznika [Vibration]</style>
75. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [AttackDown] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2091021].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 3 [AttackDown]<style="highlight"></style>
76. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=2091021].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
77. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [Breath] 위력과 메인 타겟의 [Vibration] 위력의 합 6당, 합 위력 +1 (최대 <style="highlight">4</style>)\n[BeforeAttack] (<style="highlight">4</style> + 최대 공명 수)만큼 [Breath] 얻음 (최대 10)\n[BeforeAttack] 자신의 [Breath] 횟수 <style="highlight">4</style> 증가\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -4 (최대 -12)\n[BeforeAttack] 자신의 [Breath] 횟수가 10 이상이면, 자신의 [Breath] 횟수를 4 소모하고, 메인 타겟에게 가하는 크리티컬 피해량 +<style="highlight">40</style>%\n[EndSkill] 공격 대상 중 무작위 적에게 (1 + 최대 공명 수)만큼 [EmpathicDistressAlly]을 1씩 나누어 부여 (최대 5)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=4].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Breath], [Vibration], [BeforeAttack], [EndSkill], [EmpathicDistressAlly]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [EmpathicDistressAlly] = 감각 균열 / Fracturing of the Senses
   EN: [CantIdentify]\nTargets randomly\nClash Power +1 for every 6 ([Breath] Potency on self + [Vibration] Potency on the main target) (max <style="highlight">4</style>)\n[BeforeAttack] Gain (<style="highlight">4</style> + highest Reson.) [Breath] (max 10)\n[BeforeAttack] Gain +<style="highlight">4</style> [Breath] Count\n[BeforeAttack] Base Power -4 for every Cracked Coin (max -12)\n[BeforeAttack] At 10+ [Breath] Count, consume 4 [Breath] Count on self and deal +<style="highlight">40</style>% damage on Critical Hit against the main target\n[EndSkill] Randomly inflict (1 + highest Reson.) [EmpathicDistressAlly] between targets, 1 Stack at a time (max 5)
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Walki +1 za każde 6 (Siła [Breath] tej jednostki + Siła [Vibration] głównego celu) (maks. <style="highlight">4</style>)\n[BeforeAttack] zyskuje (<style="highlight">4</style> + najwyższy Rezonans) [Breath] (maks. 10)\n[BeforeAttack] zyskuje +<style="highlight">4</style> Licznika [Breath]\n[BeforeAttack] Moc Bazowa -4 za każdą zniszczoną Monetę (maks. -12)\n[BeforeAttack] przy 10+ Licznika [Breath] zużywa 4 Licznika [Breath] i zadaje +<style="highlight">40</style>% obrażeń krytycznych głównemu celowi\n[EndSkill] rozdziela (1 + najwyższy Rezonans) Liczników [EmpathicDistressAlly] między losowych celów ataku, po 1 na raz (maks. 5)
78. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">5</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">5</style> [Vibration]
   PL: [OnSucceedAttack] nakłada <style="highlight">5</style> [Vibration]
79. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2091021].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Pasywka E.G.O — nazwa] 분열된 촉각
   źródło: Passive_Ego.json :: dataList[id=2091011].name
   limit: do 40 znaków
   EN: Schismatic Stereognosis
   PL: Rozłamowa Stereognozja
81. [Pasywka E.G.O — opis] [Breath] 위력 또는 횟수를 얻을 때, 자신의 [Breath] 횟수 1 증가 (턴당 2회)\n\n자신이 [PersonalityBreath] 또는 [PersonalityVibration]이면, 기본 공격 가중치가 1이거나 [WideAreaRampage]인 기본 스킬로 가하는 피해량 +10%\n\n공격 종료 시 대상이 흐트러짐 상태거나 사망했으면, 다음 턴에 대상이 보유한 [Vibration] 위력의 1/3만큼을 다른 무작위 적들에게 나누어 부여 (소수점 올림, 집중 전투면, 부위로 판정)\n- 이 효과는 E.G.O 기프트 거울 촉각 공감각 효과와 중첩되어 발동하지 않음
   źródło: Passive_Ego.json :: dataList[id=2091011].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [PersonalityBreath], [PersonalityVibration], [WideAreaRampage], [Vibration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [PersonalityBreath] = 호흡 인격 / Poise ID; [PersonalityVibration] = 진동 인격 / Tremor ID; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Vibration] = 진동 / Tremor
   EN: When this unit gains [Breath] Potency or Count, gain +1 [Breath] Count (2 times per turn)\n\nIf this unit is a [PersonalityBreath] or a [PersonalityVibration], Base Skills that have 1 base Atk Weight or are [WideAreaRampage] deal +10% damage\n\nAt Attack End, if target is Staggered or defeated, randomly inflict 1/3 of [Vibration] Potency on target between other random enemies next turn (rounded up; for Focused Encounters, Parts)\n- This effect does not stack with the effects of the E.G.O Gift "Mirror Tactile Synaesthesia"
   PL: gdy ta jednostka zyskuje Siłę lub Licznik [Breath], zyskuje +1 Licznika [Breath] (2 razy na turę)\n\njeżeli ta jednostka jest [PersonalityBreath] lub [PersonalityVibration], Podstawowe Umiejętności z bazową Wagą Ataku 1 lub typu [WideAreaRampage] zadają +10% obrażeń\n\nna koniec ataku jeżeli cel jest Oszołomiony lub pokonany, następnej tury rozdziela 1/3 Siły [Vibration] celu między innych losowych wrogów (zaokrąglone w górę; w walkach skupionych per Część)\n- nie kumuluje się z efektami Prezentu E.G.O „Lustrzana Dotykowa Synestezja”

## E.G.O [21001] Branch of Knowledge (지식나무의 가지) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21001`

82. [Karta E.G.O — nazwa] 지식나무의 가지
   źródło: Egos.json :: dataList[id=21001].name
   limit: do 40 znaków
   EN: Branch of Knowledge
   PL: Gałąź Wiedzy
83. [Karta E.G.O — opis] 싱클레어의 기본 EGO 장비
   źródło: Egos.json :: dataList[id=21001].desc
   limit: do 120 znaków
   EN: Sinclair’s Base E.G.O
   PL: Podstawowy Sprzęt E.G.O Sinclair
84. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 지식나무의 가지
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=1].name ; dataList[id=2100111].levelList[level=3].name ; dataList[id=2100111].levelList[level=4].name
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 싱클레어
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=1].abName ; dataList[id=2100111].levelList[level=3].abName ; dataList[id=2100111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair
86. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 6 부여
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 6 [Burst]
   PL: [OnSucceedAttackHead] nakłada 6 [Burst]
87. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 10 감소
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lose 10 SP
   PL: [OnSucceedAttack] traci 10 SP
88. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 12 부여
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 12 [Burst]
   PL: [OnSucceedAttackHead] nakłada 12 [Burst]
89. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 정신력 10 감소
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Lose 10 SP
   PL: [OnSucceedAttackHead] traci 10 SP
90. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 정신력 10 회복
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Heal 10 SP
   PL: [OnSucceedAttackTail] odzyskuje 10 SP
91. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 정신력 10 감소. <style="highlight">다음 턴에 공격 위력 증가 1을 얻음</style>
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Enhancement]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [OnSucceedAttackHead] Lose 10 SP. <style="highlight">Gain 1 [Enhancement] next turn</style>
   PL: [OnSucceedAttackHead] traci 10 SP. <style="highlight">następnej tury zyskuje 1 [Enhancement]</style>
92. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttackTail] 정신력 10 회복. <style="highlight">다음 턴에 보호 1을 얻음</style>
   źródło: Skills_Ego.json :: dataList[id=2100111].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Gain 10 SP. <style="highlight">Gain 1 Protection next turn</style>
   PL: [OnSucceedAttackTail] zyskuje 10 SP. <style="highlight">następnej tury zyskuje 1 [Protection]</style>
93. [Pasywka E.G.O — nazwa] 불안정
   źródło: Passive_Ego.json :: dataList[id=2100111].name
   limit: do 40 znaków
   EN: Unstable
   PL: Niestabilność
94. [Pasywka E.G.O — opis] 한 스킬에서 공격 적중 시 이전에 판정한 코인과 다른 면의 코인 나오면 정신력 -5, 이번 턴에 피해량 증가 1을 얻음 (턴 당 최대 3회)
   źródło: Passive_Ego.json :: dataList[id=2100111].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: If a Coin hits with a different side from the previous Coin of the same Skill, lose 5 SP and gain 1 [AttackDmgUp] this turn (3 times per turn)
   PL: przy trafieniu Monetą inną stroną niż poprzednia Moneta tej samej Umiejętności, traci 5 SP i w tej turze zyskuje 1 [AttackDmgUp] (maks. 3 razy na turę)

## E.G.O [21002] Impending Day (다가올날) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21002`

95. [Karta E.G.O — nazwa] 다가올날
   źródło: Egos.json :: dataList[id=21002].name
   limit: do 40 znaków
   EN: Impending Day
   PL: Nadchodzący Dzień
96. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21002].desc
   limit: do 120 znaków
   EN: Sinclair’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Sinclair
97. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 다가올날
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=1].name ; dataList[id=2100211].levelList[level=3].name ; dataList[id=2100211].levelList[level=4].name
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 종말달력
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=1].abName ; dataList[id=2100211].levelList[level=3].abName ; dataList[id=2100211].levelList[level=4].abName
   limit: do 40 znaków
   EN: Doomsday Calendar
   PL: Kalendarz Zagłady
99. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 체력이 25%미만일 때 피해량 +10%
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target’s HP is below 25%, deal +10% damage
   PL: przy HP celu niższym niż 25%, zadaje +10% obrażeń
100. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [EnemyKill] 아군 전체가 각자 최대 체력의 10%만큼 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal all allies for 10% of their Max HP
   PL: [EnemyKill] odzyskuje HP równe 10% Maks. HP dla wszystkich sojuszników
101. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 대상의 체력이 25%미만일 때 피해량 +20%
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=3].desc
   limit: do 120 znaków
   EN: If target’s HP is below 25%, deal +20% damage
   PL: przy HP celu niższym niż 25%, zadaje +20% obrażeń
102. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [EnemyKill] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100211].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] Gain 1 [Enhancement] next turn
   PL: [EnemyKill] następnej tury zyskuje 1 [Enhancement]
103. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [EnemyKill] 아군 전체가 각자 최대 체력의 15%만큼 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100211].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal all allies for 15% of their Max HP
   PL: [EnemyKill] odzyskuje HP równe 15% Maks. HP dla wszystkich sojuszników
104. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 체력이 25%미만일 때 피해량 +40%
   źródło: Skills_Ego.json :: dataList[id=2100211].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target’s HP is below 25%, +40% Damage
   PL: przy HP celu niższym niż 25%, zadaje +40% obrażeń
105. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 다가올날
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=1].name ; dataList[id=2100221].levelList[level=3].name ; dataList[id=2100221].levelList[level=4].name
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 종말달력
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=1].abName ; dataList[id=2100221].levelList[level=3].abName ; dataList[id=2100221].levelList[level=4].abName
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 체력이 25%미만일 때 피해량 +15%
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly\nIf target’s HP is below 25%, +15% Damage
   PL: [CantIdentify]\nAtakuje losowy cel\nprzy HP celu niższym niż 25%, +15% obrażeń
108. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [EnemyKillFail] 다음 턴에 출혈 10 얻음
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100221].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100221].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKillFail], [Laceration]
   znaczenie tagów: [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Laceration] = 출혈 / Bleed
   EN: [EnemyKillFail] Gain 10 [Laceration] next turn
   PL: [EnemyKillFail] następnej tury zyskuje 10 [Laceration]
109. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 체력이 25%미만일 때 피해량 +25%
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly\nIf target’s HP is below 25%, +25% Damage
   PL: [CantIdentify]\nAtakuje losowy cel\nprzy HP celu niższym niż 25%, +25% obrażeń
110. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [EnemyKillFail] 다음 턴에 공격 위력 증가 3 얻음
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100221].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKillFail], [Enhancement]
   znaczenie tagów: [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKillFail] Gain 3 [Enhancement] next turn
   PL: [EnemyKillFail] następnej tury zyskuje 3 [Enhancement]
111. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 체력이 25%미만일 때 피해량 +50%
   źródło: Skills_Ego.json :: dataList[id=2100221].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly\nIf target’s HP is below 25%, +50% Damage
   PL: [CantIdentify]\nAtakuje losowy cel\nprzy HP celu niższym niż 25%, +50% obrażeń
112. [Pasywka E.G.O — nazwa] 산제물 의식
   źródło: Passive_Ego.json :: dataList[id=2100211].name
   limit: do 40 znaków
   EN: Live Offering
   PL: Żywa Ofiara
113. [Pasywka E.G.O — opis] 공격, 반격 스킬로 적 처치 시 처치한 스킬의 E.G.O 자원을 5개 획득
   źródło: Passive_Ego.json :: dataList[id=2100211].desc
   limit: do 140 znaków
   EN: After defeating an enemy with an attack or counter skill, gain 5 E.G.O resources of that skill’s Affinity.
   PL: po pokonaniu wroga Umiejętnością Ataku lub Kontry, zyskuje 5 zasobów E.G.O odpowiadających Grzechowi tej Umiejętności.

## E.G.O [21003] Lifetime Stew (평생 스튜) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21003`

114. [Karta E.G.O — nazwa] 평생 스튜
   źródło: Egos.json :: dataList[id=21003].name
   limit: do 40 znaków
   EN: Lifetime Stew
   PL: Dożywotni Gulasz
115. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21003].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4,5) — nazwa] 평생 스튜
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=1].name ; dataList[id=2100311].levelList[level=3].name ; dataList[id=2100311].levelList[level=4].name ; dataList[id=2100311].levelList[level=5].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4,5) — źródło (Anomalia)] 바질리스프크
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=1].abName ; dataList[id=2100311].levelList[level=3].abName ; dataList[id=2100311].levelList[level=4].abName ; dataList[id=2100311].levelList[level=5].abName
   limit: do 40 znaków
   EN: Basilisoup
   PL: Basilisoup
118. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격\n대상이 아군인 경우, 피해량이 항상 0으로 고정
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=1].desc ; dataList[id=2100311].levelList[level=3].desc ; dataList[id=2100311].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets the unit with the least HP\nIf target is an ally, this deals 0 damage
   PL: [CantIdentify]\nAtakuje cel z najniższym HP\njeżeli celem jest sojusznik, zadaje zawsze 0 obrażeń
119. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상이 아군인 경우, 자신의 최대 체력의 5% 만큼 대상의 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target is an ally, heal them for 5% of user’s Max HP
   PL: [OnSucceedAttackHead] jeżeli celem jest sojusznik, leczy HP celu o 5% Maks. HP tej jednostki
120. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 화상 7 부여. 대상이 아군인 경우, 다음 턴에 신속 2 부여
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Combustion], [Agility]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Combustion] = 화상 / Burn; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackTail] Inflict 7 [Combustion]; if target is an ally, give 2 [Agility] next turn
   PL: [OnSucceedAttackTail] nakłada 7 Podpalenia; jeżeli celem jest sojusznik, następnej tury nakłada 2 [Agility]
121. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상이 아군인 경우, 자신의 최대 체력의 10% 만큼 대상의 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100311].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target is an ally, heal them for 10% of user’s Max HP
   PL: [OnSucceedAttackHead] jeżeli celem jest sojusznik, leczy HP celu o 10% Maks. HP tej jednostki
122. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 화상 7 부여. 대상이 아군인 경우, 다음 턴에 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">E.G.O 자원 획득량 +</color></link></u> 1, 신속 2 부여
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100311].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <sprite name="GainSinStockAdder">, <color=#f8c200>, <u>, <link="GainSinStockAdder">, </color>, </link>, </u>, [OnSucceedAttackTail], [Combustion], [Agility]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Combustion] = 화상 / Burn; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackTail] Inflict 7 [Combustion]; if target is an ally, give 2 [Agility] and 1 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">E.G.O Resource Amp</color></link></u> next turn
   PL: [OnSucceedAttackTail] nakłada 7 Podpalenia; jeżeli celem jest sojusznik, następnej tury nakłada 2 [Agility] i 1 <sprite name="GainSinStockAdder"><color=#f8c200><u><link="GainSinStockAdder">Wzmocnienia Zasobów E.G.O</link></u></color>
123. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — opis] [CantIdentify]\n현재 체력이 가장 낮은 대상 공격\n<style="highlight">스킬 사용 시 필요한 탐식 E.G.O 자원이 0으로 변경됨\n대상이 아군인 경우, 피해량이 항상 0으로 고정되고 수비 스킬을 발동하지 않음 (합 가능 수비 포함)\n[DefeatDuel] 기본 위력 -8\n[EndSkill] 이 스킬이 아군에게 적중했으면, 자신의 정신력을 이 스킬의 타겟으로 지정된 아군의 수만큼 회복\n[EndSkill] 자신의 최대 체력의 (5 x 이 스킬의 타겟으로 지정된 아군 수)% 만큼 자신의 체력 회복 (최소 5%, 최대 20%)\n[EndSkill] 다음 턴에 [GainSinStockAdder] 1, [Agility] 2 얻음</style>
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=5].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [DefeatDuel], [EndSkill], [GainSinStockAdder], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets the unit with the least HP\n<style="highlight">Required Gluttony E.G.O resource to use this Skill is reduced to 0\nIf target is an ally, this Skill deals 0 damage and does not trigger Defense Skills (including Clashable Defense Skills)\n[DefeatDuel] Base Power -8\n[EndSkill] If this Skill hit an ally, this unit heals SP equal to the number of allies targeted by this Skill\n[EndSkill] Heal this unit for (5 x number of allies targeted by this Skill)% Max HP (min 5%, max 20%)\n[EndSkill] Gain 1 [GainSinStockAdder] and 2 [Agility] next turn</style>
   PL: [CantIdentify]\nAtakuje cel z najniższym aktualnym HP\n<style="highlight">wymagany zasób E.G.O Obżarstwa do użycia tej Umiejętności wynosi 0\njeżeli celem jest sojusznik, zadaje zawsze 0 obrażeń i nie uruchamia Umiejętności Obrony (wliczając Umiejętności Obrony zdolne do Starcia)\n[DefeatDuel] Moc Bazowa -8\n[EndSkill] jeżeli ta Umiejętność trafiła sojusznika, odzyskuje SP równe liczbie sojuszników wskazanych celami tej Umiejętności\n[EndSkill] odzyskuje HP równe (5 x liczba sojuszników wskazanych celami tej Umiejętności)% Maks. HP tej jednostki (min. 5%, maks. 20%)\n[EndSkill] następnej tury zyskuje 1 [GainSinStockAdder] i 2 [Agility]</style>
124. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[SuperCoin]</style>
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: <style="highlight">[SuperCoin]</style>
   PL: <style="highlight">[SuperCoin]</style>
125. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상이 아군인 경우,</style>
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] If target is an ally,</style>
   PL: <style="highlight">[OnSucceedAttack] jeżeli celem jest sojusznik,</style>
126. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 3 — opis] <style="highlight">- 자신의 최대 체력의 (5 x 이 스킬의 타겟으로 지정된 아군 수)%만큼 대상의 체력 회복 (최대 20%)</style>
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=5].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">- Heal target for (5 x number of allies targeted by this Skill)% of user's Max HP (max 20%)</style>
   PL: <style="highlight">- leczy HP celu równe (5 x liczba sojuszników wskazanych celami tej Umiejętności)% Maks. HP tej jednostki (maks. 20%)</style>
127. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 4 — opis] <style="highlight">- 다음 턴에 [GainSinStockAdder] 1, [Agility] 2 부여</style>
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=5].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [GainSinStockAdder], [Agility]
   znaczenie tagów: [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp; [Agility] = 신속 / Haste
   EN: <style="highlight">- Apply 1 [GainSinStockAdder] and 2 [Agility] next turn</style>
   PL: <style="highlight">- następnej tury nakłada 1 [GainSinStockAdder] i 2 [Agility]</style>
128. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 5 — opis] [OnSucceedAttackTail] [Combustion] 7 부여<style="highlight"></style>
   źródło: Skills_Ego.json :: dataList[id=2100311].levelList[level=5].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Combustion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackTail] Inflict 7 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttackTail] nakłada 7 [Combustion]<style="highlight"></style>
129. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4,5) — nazwa] 평생 스튜
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=1].name ; dataList[id=2100321].levelList[level=3].name ; dataList[id=2100321].levelList[level=4].name ; dataList[id=2100321].levelList[level=5].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4,5) — źródło (Anomalia)] 바질리스프크
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=1].abName ; dataList[id=2100321].levelList[level=3].abName ; dataList[id=2100321].levelList[level=4].abName ; dataList[id=2100321].levelList[level=5].abName
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격\n\n[BeforeAttack] 무작위 E.G.O 자원을 3개 소모하여 피해량 10% 증가
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets the unit with the least HP\n\n[BeforeAttack] Spend 3 random E.G.O resources to boost damage by 10%
   PL: [CantIdentify]\nAtakuje cel z najniższym HP\n\n[BeforeAttack] zużywa 3 losowe zasoby E.G.O, by zwiększyć obrażenia o 10%
132. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 2 증가
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100321].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100321].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Podpalenia
133. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격\n\n[BeforeAttack] 무작위 E.G.O 자원을 3개 소모하여 피해량 20% 증가
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets the unit with the least HP\n\n[BeforeAttack] Spend 3 random E.G.O resources to boost damage by 20%
   PL: [CantIdentify]\nAtakuje cel z najniższym HP\n\n[BeforeAttack] zużywa 3 losowe zasoby E.G.O, by zwiększyć obrażenia o 20%
134. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격\n\n[BeforeAttack] 무작위 E.G.O 자원을 3개 소모하여 피해량 30% 증가
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets the unit with the least HP\n\n[BeforeAttack] Spend 3 random E.G.O resources to boost damage by 30%
   PL: [CantIdentify]\nAtakuje cel z najniższym HP\n\n[BeforeAttack] zużywa 3 losowe zasoby E.G.O, by zwiększyć obrażenia o 30%
135. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — opis] [CantIdentify]\n현재 체력이 가장 낮은 대상 공격\n<style="highlight">스킬 사용 시 필요한 탐식 E.G.O 자원이 0으로 변경됨\n[DefeatDuel] 기본 위력 -12\n[BeforeAttack] 모든 공격 대상의 [Combustion] 위력 합 4당 피해량 +15% (최대 60%)\n[BeforeAttack] 가장 많은 E.G.O 자원을 최대 3개 소모하여, 소모한 자원 1당 피해량 +10% (최대 30%)</style>
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=5].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [DefeatDuel], [BeforeAttack], [Combustion]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn
   EN: [CantIdentify]\nTargets the unit with the least HP\n<style="highlight">Required Gluttony E.G.O resource to use this Skill is reduced to 0\n[DefeatDuel] Base Power -12\n[BeforeAttack] Deal +15% damage for every 4 ([Combustion] Potency on all targets) (max 60%)\n[BeforeAttack] Consume up to 3 of the most-owned E.G.O resource, and deal +10% damage for every 1 of the said E.G.O resource consumed (max 30%)</style>
   PL: [CantIdentify]\nAtakuje cel z najniższym aktualnym HP\n<style="highlight">wymagany zasób E.G.O Obżarstwa do użycia tej Umiejętności wynosi 0\n[DefeatDuel] Moc Bazowa -12\n[BeforeAttack] zadaje +15% obrażeń za każde 4 (suma Siły [Combustion] wszystkich celów ataku) (maks. 60%)\n[BeforeAttack] zużywa maks. 3 najbardziej posiadanych zasobów E.G.O i zadaje +10% obrażeń za każdy 1 zużyty zasób E.G.O (maks. 30%)</style>
136. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[SuperCoin]</style>
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=5].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Combustion] 2 부여</style>
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Inflict 2 [Combustion]</style>
   PL: <style="highlight">[OnSucceedAttack] [Combustion] 2 Podpalenia</style>
138. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=5].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada +2 Licznika [Combustion]<style="highlight"></style>
139. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 4 — opis] <style="highlight">[UnBrokenCoinOnSucceedAttack] 스킬 효과로 E.G.O 자원을 소모했을 경우, 이 코인 최종 피해량의 50% 만큼 색욕 피해</style>
   źródło: Skills_Ego.json :: dataList[id=2100321].levelList[level=5].coinlist[#0].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: <style="highlight">[UnBrokenCoinOnSucceedAttack] If E.G.O resource was spent due to this Skill's effect, deal Lust damage equal to 50% of this Coin's final damage</style>
   PL: <style="highlight">[UnBrokenCoinOnSucceedAttack] jeżeli zużyto zasób E.G.O przez efekt tej Umiejętności, zadaje obrażenia Żądzy równe 50% końcowych obrażeń tej Monety</style>
140. [Pasywka E.G.O — nazwa] 스튜 분출
   źródło: Passive_Ego.json :: dataList[id=2100311].name
   limit: do 40 znaków
   EN: Stew Spewage
   PL: Wyrzut Gulaszu
141. [Pasywka E.G.O — opis] 뒷면 적중 시 대상이 적인 경우, 화상 1 부여
   źródło: Passive_Ego.json :: dataList[id=2100311].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On Tails Hit, inflict 1 [Combustion] if target is an enemy
   PL: przy trafieniu Reszką, jeżeli celem jest wróg, nakłada 1 Podpalenia
142. [Pasywka E.G.O — nazwa] 스튜 분출
   źródło: Passive_Ego.json :: dataList[id=2100312].name
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Pasywka E.G.O — opis] 뒷면 적중 시 대상이 적인 경우, [Combustion] 1 부여\n\n<style="highlight">적에게 [Combustion] 위력 또는 횟수를 부여하는 기본 공격 스킬 사용 시\n\n- 더하기 코인 스킬이면\n· 정신력이 40 미만이면, 정신력 4 회복\n· 정신력이 40 이상이면, 피해량 +10%\n\n- 빼기 코인 스킬이면\n· 정신력이 -25 초과면, 정신력 4 감소 (이 효과로 정신력이 -40미만으로 내려가지 않음)\n· 정신력이 -25 이하면, 피해량 +10%</style>
   źródło: Passive_Ego.json :: dataList[id=2100312].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On Tails Hit, inflict 1 [Combustion] if target is an enemy\n\n<style="highlight">When using Base Attack Skills that inflict [Combustion] Potency or Count against enemies,\n\n- For Plus Coin Skills:\n· At lower than 40 SP, heal 4 SP\n· At 40 or higher SP, deal +10% damage\n\n- For Minus Coin Skills:\n· At higher than -25 SP, lose 4 SP (this effect cannot reduce this unit's SP below -40)\n· At -25 or lower SP, deal +10% damage</style>
   PL: przy trafieniu Reszką, jeżeli celem jest wróg, nakłada 1 [Combustion]\n\n<style="highlight">przy użyciu Podstawowych Umiejętności Ataku nakładających Siłę lub Licznik [Combustion] na wrogów,\n\n- dla Umiejętności z Monetą Plus:\n· przy SP niższym niż 40 odzyskuje 4 SP\n· przy SP 40 lub wyższym zadaje +10% obrażeń\n\n- dla Umiejętności z Monetą Minus:\n· przy SP wyższym niż -25 traci 4 SP (ten efekt nie obniża SP tej jednostki poniżej -40)\n· przy SP -25 lub niższym zadaje +10% obrażeń</style>
144. [Pasywka E.G.O — podsumowanie] 뒷면 적중시 [Combustion] 부여, 정신력 회복 및 감소 또는 <noparse>피해량 증가</noparse>
   źródło: Passive_Ego.json :: dataList[id=2100312].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On Tails Hit, inflict [Combustion] on target. Heal or lose SP on self; or deal more damage
   PL: przy trafieniu Reszką nakłada [Combustion] na cel. odzyskuje lub traci SP; albo zadaje więcej obrażeń

## E.G.O [21004] Lantern (초롱) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21004`

145. [Karta E.G.O — nazwa] 초롱
   źródło: Egos.json :: dataList[id=21004].name
   limit: do 40 znaków
   EN: Lantern
   PL: Lampa
146. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21004].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 초롱
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=1].name ; dataList[id=2100411].levelList[level=3].name ; dataList[id=2100411].levelList[level=4].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 요정초롱
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=1].abName ; dataList[id=2100411].levelList[level=3].abName ; dataList[id=2100411].levelList[level=4].abName
   limit: do 40 znaków
   EN: Faelantern
   PL: Wróżkowa Latarnia
149. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 3 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 3 Rozdarcia
150. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 10%만큼 회복.
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 2 allies with the lowest HP Percentages by 10% of Max HP.
   PL: [OnSucceedAttack] leczy 2 sojuszników z najniższym aktualnym procentem HP o 10% Maks. HP.
151. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신의 체력이 50%미만이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 50%- HP, Atk Weight +1
   PL: [BeforeAttack] przy własnym HP niższym niż 50%, Waga Ataku +1
152. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 12%만큼 회복.
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 2 allies with the lowest HP by 12% of Max HP.
   PL: [OnSucceedAttack] leczy 2 sojuszników z najniższym aktualnym procentem HP o 12% Maks. HP.
153. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신의 체력이 50%미만이면, 공격 가중치 +2
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 50%- HP, Atk Weight +2
   PL: [BeforeAttack] przy własnym HP niższym niż 50%, Waga Ataku +2
154. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
155. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 15%만큼 회복.
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 2 allies with the lowest HP by 15% of Max HP.
   PL: [OnSucceedAttack] leczy 2 sojuszników z najniższym aktualnym procentem HP o 15% Maks. HP.
156. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 초롱
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=1].name ; dataList[id=2100421].levelList[level=3].name ; dataList[id=2100421].levelList[level=4].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 요정초롱
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=1].abName ; dataList[id=2100421].levelList[level=3].abName ; dataList[id=2100421].levelList[level=4].abName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n체력이 가장 많은 대상 공격
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify] \nTarget the unit with the most HP
   PL: [CantIdentify]\nAtakuje cel z najwyższym HP
159. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 파열 횟수 2 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Burst]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackTail] Inflict +2 [Burst] Count
   PL: [OnSucceedAttackTail] nakłada +2 Licznika [Burst]
160. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 체력을 피해량의 30%만큼 회복
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal self by 30% of damage dealt
   PL: [OnSucceedAttack] leczy własne HP o 30% zadanych obrażeń
161. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n체력이 가장 많은 대상 공격\n[BeforeAttack] 자신의 체력이 50% 미만이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTarget the unit with the most HP\n[BeforeAttack] At 50%- HP, Atk Weight +1
   PL: [CantIdentify]\nAtakuje cel z najwyższym HP\n[BeforeAttack] przy własnym HP niższym niż 50%, Waga Ataku +1
162. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 파열 횟수 3 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Burst]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackTail] Inflict +3 [Burst] Count
   PL: [OnSucceedAttackTail] nakłada +3 Licznika [Burst]
163. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 3 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 3 [DefenseDown]
164. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 체력을 피해량의 50%만큼 회복
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2100421].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal self by 50% of damage dealt
   PL: [OnSucceedAttack] leczy własne HP o 50% zadanych obrażeń
165. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n체력이 가장 많은 대상 공격\n[BeforeAttack] 자신의 체력이 50% 미만이면, 공격 가중치 +2
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTarget the unit with the most HP\n[BeforeAttack] At 50%- HP, Atk Weight +2
   PL: [CantIdentify]\nAtakuje cel z najwyższym HP\n[BeforeAttack] przy własnym HP niższym niż 50%, Waga Ataku +2
166. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o 3
167. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 5 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 5 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 5 [DefenseDown]
168. [Pasywka E.G.O — nazwa] 미끼 요정
   źródło: Passive_Ego.json :: dataList[id=2100411].name
   limit: do 40 znaków
   EN: Fairy Lure
   PL: Wabik Wróżek
169. [Pasywka E.G.O — opis] 전투 시작 시 자신을 메인 타겟으로 공격하는 대상을 처치하면, 자신의 체력을 최대 체력의 (3 + (탐식 완전 공명 수))% 만큼 회복
   źródło: Passive_Ego.json :: dataList[id=2100411].desc
   limit: do 140 znaków
   EN: After defeating an enemy that main-targets this unit at Combat Start, heal (3 + (Gluttony A-Reson.))% HP
   PL: po pokonaniu wroga atakującego tę jednostkę jako cel główny, na początku walki leczy HP o (3 + (Rezonans Absolutny Obżarstwa))% Maks. HP

## E.G.O [21005] 9:2 (9장 2절) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21005`

170. [Karta E.G.O — nazwa] 9장 2절
   źródło: Egos.json :: dataList[id=21005].name
   limit: do 40 znaków
   EN: 9:2
   PL: 9:2
171. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21005].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 9장 2절
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=1].name ; dataList[id=2100511].levelList[level=3].name ; dataList[id=2100511].levelList[level=4].name
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 살갗 예언자
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=1].abName ; dataList[id=2100511].levelList[level=3].abName ; dataList[id=2100511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Skin Prophet
   PL: Prorok Skóry
174. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 없으면 화상 4 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100511].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has no [Combustion], inflict 4 Burn
   PL: [OnSucceedAttack] jeżeli cel nie ma [Combustion], nakłada 4 Podpalenia
175. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2100511].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Burn
   PL: [OnSucceedAttack] nakłada 4 Podpalenia
176. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (색욕 공명 수)가 4 이상이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 4+ (Lust Reson.), Atk Weight +1
   PL: [BeforeAttack] przy 4+ (Rezonansie Żądzy) Waga Ataku +1
177. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (색욕 공명 수)가 4 이상이면, 공격 가중치 +1\n[BeforeAttack] (최대 색욕 완전 공명 수)가 4 이상이면, 추가로 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 4+ (Lust Reson.), Atk Weight +1\n[BeforeAttack] At 4+ (Highest Lust A-Reson.), additional Atk Weight +1
   PL: [BeforeAttack] przy 4+ (Rezonansie Żądzy) Waga Ataku +1\n[BeforeAttack] przy 4+ (najwyższym Rezonansie Absolutnym Żądzy) dodatkowo Waga Ataku +1
178. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 대상의 [Combustion]이 10 이상이면 다음 턴에 공격 위력 감소 1, 수비 위력 감소 1 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100511].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Combustion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackTail] If target has 10+ [Combustion], inflict 1 Attack Power Down and 1 Defense Power Down next turn
   PL: [OnSucceedAttackTail] jeżeli cel ma 10+ [Combustion], następnej tury nakłada 1 Redukcji Mocy Ataku i 1 Redukcji Mocy Obrony
179. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 9장 2절
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=1].name ; dataList[id=2100521].levelList[level=3].name ; dataList[id=2100521].levelList[level=4].name
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 살갗 예언자
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=1].abName ; dataList[id=2100521].levelList[level=3].abName ; dataList[id=2100521].levelList[level=4].abName
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly
   PL: [CantIdentify]\nAtakuje losowy cel
182. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 없으면 화상 6 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100521].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has no [Combustion], inflict 6 Burn
   PL: [OnSucceedAttack] jeżeli cel nie ma [Combustion], nakłada 6 Podpalenia
183. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2100521].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (색욕 공명 수)가 4 이상이면 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 4+ (Lust Reson.), Atk Weight +1
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy 4+ (Rezonansie Żądzy) Waga Ataku +1
185. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 대상의 [Combustion]이 10 이상이면 다음 턴에 색욕 취약 1 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Combustion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackTail] If target has 10+ [Combustion], inflict 1 Lust Fragility next turn
   PL: [OnSucceedAttackTail] jeżeli cel ma 10+ [Combustion], następnej tury nakłada 1 Kruchości Żądzy
186. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (색욕 공명 수)가 4 이상이면, 공격 가중치 +1\n[BeforeAttack] (최대 색욕 완전 공명 수)가 4 이상이면, 추가로 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 4+ (Lust Reson.), Atk Weight +1\n[BeforeAttack] At 4+ (Highest Lust A-Reson), additional Atk Weight +1
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy 4+ (Rezonansie Żądzy) Waga Ataku +1\n[BeforeAttack] przy 4+ (najwyższym Rezonansie Absolutnym Żądzy) dodatkowo Waga Ataku +1
187. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 대상의 [Combustion]이 10 이상이면 다음 턴에 색욕 취약 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100521].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Combustion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackTail] If target has 10+ [Combustion], inflict 2 Lust Fragility next turn
   PL: [OnSucceedAttackTail] jeżeli cel ma 10+ [Combustion], następnej tury nakłada 2 Kruchości Żądzy
188. [Pasywka E.G.O — nazwa] 파멸의 예언
   źródło: Passive_Ego.json :: dataList[id=2100511].name
   limit: do 40 znaków
   EN: Prophecy of Ruin
   PL: Proroctwo Zagłady
189. [Pasywka E.G.O — opis] 색욕 속성 스킬의 앞면 적중 시 자신과 대상에게 정신력 피해 4를 입힘.\n(정신력이 없는 대상에게는 정신력 피해가 적용되지 않음)\n색욕 속성 스킬로 처치 시 색욕 E.G.O 자원을 5개 획득
   źródło: Passive_Ego.json :: dataList[id=2100511].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Heads Hit with a Lust affinity Skill, lower this unit and the target's SP by 4.\n(Does not work against targets that are Non-SP Units)\nGain 5 Lust E.G.O resources On Kill with a Lust affinity Skill
   PL: przy trafieniu Orłem Umiejętnością Żądzy, zadaje 4 obrażeń SP sobie i celowi.\n(nie działa wobec celów będących jednostkami bez SP)\npo pokonaniu wroga Umiejętnością Żądzy, zyskuje 5 zasobów E.G.O Żądzy

## E.G.O [21006] Cavernous Wailing (낮은울음) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21006`

190. [Karta E.G.O — nazwa] 낮은울음
   źródło: Egos.json :: dataList[id=21006].name
   limit: do 40 znaków
   EN: Cavernous Wailing
   PL: Niskie Ualenie
191. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21006].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 낮은울음
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].name ; dataList[id=2100611].levelList[level=3].name ; dataList[id=2100611].levelList[level=4].name
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 울음 두꺼비
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].abName ; dataList[id=2100611].levelList[level=3].abName ; dataList[id=2100611].levelList[level=4].abName
   limit: do 40 znaków
   EN: Blubbering Toad
   PL: Szlochająca Ropucha
194. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 최대 공명 수가 4 이상이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 4+ highest Reson., Atk Weight +1
   PL: [BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1
195. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndSkill] 자신과 현재 체력이 가장 적은 아군 1명에게 자신의 최대 체력 10%만큼 보호막을 부여하고, [ShieldManagerCryingToad] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [ShieldManagerCryingToad]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: [EndSkill] Apply 10% of this unit's max HP as Shield to self and 1 other ally with the least current HP, and apply 2 [ShieldManagerCryingToad] as well
   PL: [EndSkill] nakłada Tarczę równą 10% Maks. HP tej jednostki na siebie i 1 sojusznika z najniższym aktualnym HP oraz nakłada 2 [ShieldManagerCryingToad]
196. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] - 최대 공명 수가 4 이상이면, 부여 대상 수 +1
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: - At 4+ highest Reson., apply it to 1 more ally
   PL: - przy najwyższym Rezonansie 4+ nakłada na 1 dodatkowego sojusznika
197. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] - 대상에게 이미 [ShieldManagerCryingToad]이 있으면, [ShieldManagerCryingToad] 수치를 2로 변경
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - If the affected unit already has [ShieldManagerCryingToad], change the [ShieldManagerCryingToad] value to 2
   PL: - jeżeli wskazana jednostka ma już [ShieldManagerCryingToad], zmienia wartość [ShieldManagerCryingToad] na 2
198. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 4 — opis] - 최대 우울 완전 공명 수가 4 이상이면, 이 스킬의 [ShieldManagerCryingToad] 수치가 3으로 부여, 적용됨
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - At 4+ highest Gloom A-Reson., this Skill's above effects change to 'apply 3 [ShieldManagerCryingToad]' and 'change the [ShieldManagerCryingToad] value to 3' instead.
   PL: - przy 4+ (najwyższym Rezonansie Absolutnym Posępności) powyższe efekty tej Umiejętności zmieniają się odpowiednio na „nakłada 3 [ShieldManagerCryingToad]" i „zmienia wartość [ShieldManagerCryingToad] na 3"
199. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">[BeforeAttack] (최대 공명 수-2)만큼 공격 가중치 증가 (최대 2)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: <style="highlight">[BeforeAttack] Gain (highest Reson. - 2) Atk Weight (max 2)</style>
   PL: <style="highlight">[BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 2)</style>
200. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [EndSkill] 자신과 현재 체력이 가장 적은 아군 <style="highlight">1+(최대 공명 수-2)</style>명에게 자신의 최대 체력 <style="highlight">14%</style>만큼 보호막을 부여하고, [ShieldManagerCryingToad] 2 부여 <style="highlight">(자신 제외 최대 부여 대상 수: 3)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [ShieldManagerCryingToad]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: [EndSkill] Apply <style="highlight">14%</style> of this unit's max HP as Shield to self and <style="highlight">(1 + (highest Reson. - 2))</style> allies with the least current HP, and apply 2 [ShieldManagerCryingToad] as well\n<style="highlight">(max # of other allies that gain [ShieldManagerCryingToad]: 3)</style>
   PL: [EndSkill] nakłada Tarczę równą <style="highlight">14%</style> Maks. HP tej jednostki na siebie i <style="highlight">1+(najwyższy Rezonans - 2)</style> sojuszników z najniższym aktualnym HP oraz nakłada 2 [ShieldManagerCryingToad] <style="highlight">(maks. liczba innych sojuszników zyskujących [ShieldManagerCryingToad]: 3)</style>
201. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] - 대상에게 이미 [ShieldManagerCryingToad]이 있으면, [ShieldManagerCryingToad] 수치를 2로 변경<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100611].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - If the affected unit already has [ShieldManagerCryingToad], change the [ShieldManagerCryingToad] value to 2<style="highlight"></style>
   PL: - jeżeli wskazana jednostka ma już [ShieldManagerCryingToad], zmienia wartość [ShieldManagerCryingToad] na 2<style="highlight"></style>
202. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] - 최대 우울 완전 공명 수가 4 이상이면, 이 스킬의 [ShieldManagerCryingToad] 수치가 3으로 부여, 적용됨<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2100611].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - At 4+ highest Gloom A-Reson., this Skill's above effects change to 'apply 3 [ShieldManagerCryingToad]' and 'change the [ShieldManagerCryingToad] value to 3' instead.<style="highlight"></style>
   PL: - przy 4+ (najwyższym Rezonansie Absolutnym Posępności) powyższe efekty tej Umiejętności zmieniają się odpowiednio na „nakłada 3 [ShieldManagerCryingToad]" i „zmienia wartość [ShieldManagerCryingToad] na 3"<style="highlight"></style>
203. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (최대 공명 수-2)만큼 공격 가중치 증가 (최대 2)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] Gain (highest Reson. - 2) Atk Weight (max 2)<style="highlight"></style>
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 2)<style="highlight"></style>
204. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [EndSkill] 자신과 현재 체력이 가장 적은 아군 1+(최대 공명 수-2)명에게 자신의 최대 체력 <style="highlight">20%</style>만큼 보호막을 부여하고, [ShieldManagerCryingToad] 2 부여 (자신 제외 최대 부여 대상 수: 3)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [ShieldManagerCryingToad]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: [EndSkill] Apply <style="highlight">20%</style> of this unit's max HP as Shield to self and (1 + (highest Reson. - 2)) allies with the least current HP, and apply 2 [ShieldManagerCryingToad] as well\n(max # of other allies that gain [ShieldManagerCryingToad]: 3)
   PL: [EndSkill] nakłada Tarczę równą <style="highlight">20%</style> Maks. HP tej jednostki na siebie i 1+(najwyższy Rezonans - 2) sojuszników z najniższym aktualnym HP oraz nakłada 2 [ShieldManagerCryingToad] (maks. liczba innych sojuszników zyskujących [ShieldManagerCryingToad]: 3)
205. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 낮은울음
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].name ; dataList[id=2100621].levelList[level=3].name ; dataList[id=2100621].levelList[level=4].name
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 울음 두꺼비
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].abName ; dataList[id=2100621].levelList[level=3].abName ; dataList[id=2100621].levelList[level=4].abName
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 최대 공명 수가 4 이상이면, 공격 가중치 +1\n[BeforeAttack] 다음 턴에 이 스킬 슬롯의 [Aggro] 5 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Aggro]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Aggro] = 도발치 / Aggro
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 4+ highest Reson., Atk Weight +1\n[BeforeAttack] Gain +5 [Aggro] to this Skill Slot next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n[BeforeAttack] następnej tury zyskuje 5 [Aggro] na tym Slocie Umiejętności
208. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Sinking] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] nakłada 2 [Sinking]
209. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndSkill] 자신에게 자신의 최대 체력 (15+최대 공명 수x2.5)% 만큼 보호막을 부여하고, [ShieldManagerCryingToad] 2 부여. (최대 25%)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [ShieldManagerCryingToad]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: [EndSkill] Gain (15 + 2.5(highest Reson.))% of this unit's max HP as Shield to self and gain 2 [ShieldManagerCryingToad]. (max 25%)
   PL: [EndSkill] nakłada na siebie Tarczę równą (15 + najwyższy Rezonans x 2.5)% Maks. HP tej jednostki i zyskuje 2 [ShieldManagerCryingToad]. (maks. 25%)
210. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] - 자신에게 이미 [ShieldManagerCryingToad]이 있으면, [ShieldManagerCryingToad] 수치를 2로 변경
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - If this unit already has [ShieldManagerCryingToad], change the [ShieldManagerCryingToad] value to 2
   PL: - jeżeli ta jednostka ma już [ShieldManagerCryingToad], zmienia wartość [ShieldManagerCryingToad] na 2
211. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 4 — opis] - 최대 우울 완전 공명 수가 4 이상이면, 이 스킬의 [ShieldManagerCryingToad] 수치가 3으로 부여, 적용됨
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - At 4+ highest Gloom A-Reson., this Skill's above effects change to 'gain 3 [ShieldManagerCryingToad]' and 'change the [ShieldManagerCryingToad] value to 3' instead.
   PL: - przy 4+ (najwyższym Rezonansie Absolutnym Posępności) powyższe efekty tej Umiejętności zmieniają się odpowiednio na „zyskuje 3 [ShieldManagerCryingToad]" i „zmienia wartość [ShieldManagerCryingToad] na 3"
212. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">[BeforeAttack] (최대 공명 수-2)만큼 공격 가중치 증가 (최대 2)</style>\n[BeforeAttack] 다음 턴에 이 스킬 슬롯의 <style="highlight">[Aggro] 10</style> 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Aggro]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Aggro] = 도발치 / Aggro
   EN: [CantIdentify]\nTargets Randomly\n<style="highlight">[BeforeAttack] Gain (highest Reson. - 2) Atk Weight (max 2)</style>\n[BeforeAttack] Gain <style="highlight">+10 [Aggro]</style> to this Skill Slot next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">[BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 2)</style>\n[BeforeAttack] następnej tury zyskuje <style="highlight">10 [Aggro]</style> na tym Slocie Umiejętności
213. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 2 [Sinking]<style="highlight"></style>
214. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [EndSkill] 자신에게 자신의 최대 체력 (<style="highlight">18</style>+최대 공명 수x<style="highlight">3</style>)% 만큼 보호막을 부여하고, [ShieldManagerCryingToad] 2 부여. (최대 <style="highlight">30%</style>)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [ShieldManagerCryingToad]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: [EndSkill] Gain (<style="highlight">18</style> + <style="highlight">3</style>(highest Reson.))% of this unit's max HP as Shield to self and gain 2 [ShieldManagerCryingToad]. (max <style="highlight">30%</style>)
   PL: [EndSkill] nakłada na siebie Tarczę równą (<style="highlight">18</style> + najwyższy Rezonans x <style="highlight">3</style>)% Maks. HP tej jednostki i zyskuje 2 [ShieldManagerCryingToad]. (maks. <style="highlight">30%</style>)
215. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] - 자신에게 이미 [ShieldManagerCryingToad]이 있으면, [ShieldManagerCryingToad] 수치를 2로 변경<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2100621].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ShieldManagerCryingToad]
   znaczenie tagów: [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: - If this unit already has [ShieldManagerCryingToad], change the [ShieldManagerCryingToad] value to 2<style="highlight"></style>
   PL: - jeżeli ta jednostka ma już [ShieldManagerCryingToad], zmienia wartość [ShieldManagerCryingToad] na 2<style="highlight"></style>
216. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] - 최대 우울 완전 공명 수가 4 이상이면, 이 스킬의 [ShieldManagerCryingToad] 수치가 3으로 부여, 적용됨<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2100621].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 공명 수-2)만큼 공격 가중치 증가 (최대 2)\n[BeforeAttack] 다음 턴에 이 스킬 슬롯의 [Aggro] 10 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Aggro]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Aggro] = 도발치 / Aggro
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (highest Reson. - 2) Atk Weight (max 2)\n[BeforeAttack] Gain +10 [Aggro] to this Skill Slot next turn<style="highlight"></style>
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 2)\n[BeforeAttack] następnej tury zyskuje 10 [Aggro] na tym Slocie Umiejętności<style="highlight"></style>
218. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Sinking] 2, <style="highlight">[Sinking] 횟수 3</style> 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and <style="highlight">+3 [Sinking] Count</style>
   PL: [OnSucceedAttack] nakłada 2 [Sinking] i <style="highlight">3 Licznika [Sinking]</style>
219. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 자신에게 자신의 최대 체력 (<style="highlight">20</style>+최대 공명 수x<style="highlight">5</style>)% 만큼 보호막을 부여하고, [ShieldManagerCryingToad] 2 부여. (최대 <style="highlight">40%</style>)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [ShieldManagerCryingToad]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: [EndSkill] Gain (<style="highlight">20</style> + <style="highlight">5</style>(highest Reson.))% of this unit's max HP as Shield to self and gain 2 [ShieldManagerCryingToad]. (max <style="highlight">40%</style>)
   PL: [EndSkill] nakłada na siebie Tarczę równą (<style="highlight">20</style> + najwyższy Rezonans x <style="highlight">5</style>)% Maks. HP tej jednostki i zyskuje 2 [ShieldManagerCryingToad]. (maks. <style="highlight">40%</style>)
220. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 5 — opis] <style="highlight">- 우울 공명이 4 이상이면, 자신에게 자신의 최대 체력 10%만큼 보호막 추가 부여</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100621].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">- At 4+ Gloom Reson., gain additional Shield equal to 10% of this unit's max HP</style>
   PL: <style="highlight">- przy Rezonansie Posępności 4+ dodatkowo nakłada na siebie Tarczę równą 10% Maks. HP tej jednostki</style>
221. [Pasywka E.G.O — nazwa] 눈물막
   źródło: Passive_Ego.json :: dataList[id=2100611].name
   limit: do 40 znaków
   EN: Tear Film
   PL: Błona Łez
222. [Pasywka E.G.O — opis] 턴 시작 시 자신에게 보호막이 적용 중일 때, [Protection] 1 얻음\n자신에게 [ShieldManagerCryingToad]이 적용 중일 때, [Protection] 1 추가로 얻음
   źródło: Passive_Ego.json :: dataList[id=2100611].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [ShieldManagerCryingToad]
   znaczenie tagów: [Protection] = 보호 / Protection; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: Turn Start: If this unit has Shield, gain 1 [Protection]\nIf this unit is under [ShieldManagerCryingToad]'s effect, gain 1 additional [Protection]
   PL: na początku tury, gdy na tej jednostce działa Tarcza, zyskuje 1 [Protection]\ngdy na tej jednostce działa [ShieldManagerCryingToad], dodatkowo zyskuje 1 [Protection]
223. [Pasywka E.G.O — podsumowanie] 보호막 적용 중일 때, [Protection] 1 얻음\n[ShieldManagerCryingToad] 적용 중일 때, [Protection] 1 얻음
   źródło: Passive_Ego.json :: dataList[id=2100611].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [ShieldManagerCryingToad]
   znaczenie tagów: [Protection] = 보호 / Protection; [ShieldManagerCryingToad] = 울음 방울 / Blubberbubble
   EN: If this unit has Shield, gain 1 [Protection]\nIf [ShieldManagerCryingToad] is active, gain 1 [Protection]
   PL: gdy na tej jednostce działa Tarcza, zyskuje 1 [Protection]\ngdy działa [ShieldManagerCryingToad], zyskuje 1 [Protection]

## E.G.O [21007] Hex Nail (저주못) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21007`

224. [Karta E.G.O — nazwa] 저주못
   źródło: Egos.json :: dataList[id=21007].name
   limit: do 40 znaków
   EN: Hex Nail
   PL: Gwóźdź Klątwy
225. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21007].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 저주못
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=1].name ; dataList[id=2100711].levelList[level=3].name ; dataList[id=2100711].levelList[level=4].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 아파하는 테디
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=1].abName ; dataList[id=2100711].levelList[level=3].abName ; dataList[id=2100711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Hurting Teddy Bear
   PL: Cierpiący Miś
228. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 대상에게 [Curse]가 있다면 즉시 해당 효과를 2번 발동시키고 [Curse] 2 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Curse]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Curse] = 저주 / Curse
   EN: [EndSkill] If target has [Curse], immediately activate it twice and reduce it by 2
   PL: [EndSkill] jeżeli cel ma [Curse], natychmiast uruchamia jego efekt 2 razy i zmniejsza [Curse] o 2
229. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL: [OnSucceedAttackHead] Nakłada 2 [Laceration]
230. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여\n- [Curse]와 [NailPersonality]을 제외한 대상의 부정적 효과 3개당 [Curse] 1 추가로 부여 (최대 2)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Curse], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [Curse]\n- Inflict 1 additional [Curse] for every 3 negative effect on target that aren't [Curse] or [NailPersonality] (max 2)
   PL: [OnSucceedAttack] nakłada 2 [Curse]\n- dodatkowo nakłada 1 [Curse] za każde 3 negatywnych efektów na celu innych niż [Curse] i [NailPersonality] (maks. 2)
231. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [NailPersonality]
   PL: [OnSucceedAttack] nakłada 2 [NailPersonality]
232. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">[BeforeAttack] 이 스킬을 포함하여 질투 공명이 4 이상이면 공격 가중치 +1</style>\n[EndSkill] 대상에게 [Curse]가 있다면 즉시 해당 효과를 2번 발동시키고 [Curse] 2 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill], [Curse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Curse] = 저주 / Curse
   EN: <style="highlight">[BeforeAttack] At 4+ Envy Reson. including this Skill, Atk Weight +1</style>\n[EndSkill] If target has [Curse], immediately activate it twice and reduce it by 2
   PL: <style="highlight">[BeforeAttack] przy Rezonansie Zazdrości 4+ (wliczając tę Umiejętność), Waga Ataku +1</style>\n[EndSkill] jeżeli cel ma [Curse], natychmiast uruchamia jego efekt 2 razy i zmniejsza [Curse] o 2
233. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100711].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttackHead] nakłada 2 [Laceration]<style="highlight"></style>
234. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여\n- [Curse]와 [NailPersonality]을 제외한 대상의 부정적 효과 3개당 [Curse] 1 추가로 부여 (최대 2)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Curse], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [Curse]\n- Inflict 1 additional [Curse] for every 3 negative effect on target that aren't [Curse] or [NailPersonality] (max 2)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 2 [Curse]\n- dodatkowo nakłada 1 [Curse] za każde 3 negatywnych efektów na celu innych niż [Curse] i [NailPersonality] (maks. 2)<style="highlight"></style>
235. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [NailPersonality]
   PL: [OnSucceedAttack] nakłada <style="highlight">3</style> [NailPersonality]
236. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttackHead] 다음 턴에 [Binding] 2 부여 (턴 당 1회)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 2 [Binding] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttackHead] następnej tury nakłada 2 [Binding] (1 raz na turę)</style>
237. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] <style="highlight">[BeforeAttack] 이 스킬을 포함하여 공명 수 3당 공격 가중치 +1 (최대 2)</style>\n[EndSkill] 대상에게 [Curse]가 있다면 즉시 해당 효과를 2번 발동시키고 [Curse] 2 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill], [Curse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Curse] = 저주 / Curse
   EN: <style="highlight">[BeforeAttack] For every 3 Envy Reson. including this Skill, Atk Weight +1 (max 2)</style>\n[EndSkill] If target has [Curse], immediately activate it twice and reduce it by 2
   PL: <style="highlight">[BeforeAttack] za każde 3 Rezonansu Zazdrości (wliczając tę Umiejętność), Waga Ataku +1 (maks. 2)</style>\n[EndSkill] jeżeli cel ma [Curse], natychmiast uruchamia jego efekt 2 razy i zmniejsza [Curse] o 2
238. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여\n- [Curse]와 [NailPersonality]을 제외한 대상의 부정적 효과 <style="highlight">2</style>개당 [Curse] 1 추가로 부여 (최대 2)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Curse], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [Curse]\n- Inflict 1 additional [Curse] for every <style="highlight">2</style> negative effect on target that aren't [Curse] or [NailPersonality] (max 2)
   PL: [OnSucceedAttack] nakłada 2 [Curse]\n- dodatkowo nakłada 1 [Curse] za każde <style="highlight">2</style> negatywnych efektów na celu innych niż [Curse] i [NailPersonality] (maks. 2)
239. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 3 [NailPersonality]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 3 [NailPersonality]<style="highlight"></style>
240. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Curse]가 4 이상이면, [ParryingResultDown] 1 부여 (턴 당 1회)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Curse], [ParryingResultDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse; [ParryingResultDown] = 합 위력 감소 / Clash Power Down
   EN: <style="highlight">[OnSucceedAttack] At 4+ [Curse], inflict 1 [ParryingResultDown] (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] jeżeli cel ma 4+ [Curse], nakłada 1 [ParryingResultDown] (1 raz na turę)</style>
241. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 4 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 2 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100711].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 2 [Binding] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttackHead] następnej tury nakłada 2 [Binding] (1 raz na turę)<style="highlight"></style>
242. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 저주못
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=1].name ; dataList[id=2100721].levelList[level=3].name ; dataList[id=2100721].levelList[level=4].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 아파하는 테디
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=1].abName ; dataList[id=2100721].levelList[level=3].abName ; dataList[id=2100721].levelList[level=4].abName
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 대상에게 [Curse]가 있다면 즉시 해당 효과를 2번 발동시키고 [Curse] 2 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Curse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Curse] = 저주 / Curse
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] If target has [Curse], immediately activate it twice and reduce it by 2
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] jeżeli cel ma [Curse], natychmiast uruchamia jego efekt 2 razy i zmniejsza [Curse] o 2
245. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Laceration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackTail] Inflict 2 [Laceration]
   PL: [OnSucceedAttackTail] nakłada 2 [Laceration]
246. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 4 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 4 [Curse]
   PL: [OnSucceedAttack] nakłada 4 [Curse]
247. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 대상에게 [Curse]가 있다면 즉시 해당 효과를 2번 발동시키고 [Curse] 2 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=3].desc ; dataList[id=2100721].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [Curse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Curse] = 저주 / Curse
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] If target has [Curse], immediately activate it twice and reduce it by 2<style="highlight"></style>
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] jeżeli cel ma [Curse], natychmiast uruchamia jego efekt 2 razy i zmniejsza [Curse] o 2<style="highlight"></style>
249. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Laceration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackTail] Inflict <style="highlight">3</style> [Laceration]
   PL: [OnSucceedAttackTail] nakłada <style="highlight">3</style> [Laceration]
250. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 4 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2100721].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 4 [Curse]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 4 [Curse]<style="highlight"></style>
251. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttackTail] 다음 턴에 [Binding] 2 부여 (턴 당 1회)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Binding]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttackTail] Inflict 2 [Binding] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttackTail] następnej tury nakłada 2 [Binding] (1 raz na turę)</style>
253. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Laceration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackTail] Inflict 3 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttackTail] nakłada 3 [Laceration]<style="highlight"></style>
254. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 이 스킬을 포함하여 질투 공명이 4 이상이면, [ParryingResultDown] 1 부여 (턴 당 1회)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ParryingResultDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ParryingResultDown] = 합 위력 감소 / Clash Power Down
   EN: <style="highlight">[OnSucceedAttack] At 4+ Envy Reson. including this Skill, inflict 1 [ParryingResultDown] (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] przy Rezonansie Zazdrości 4+ (wliczając tę Umiejętność), nakłada 1 [ParryingResultDown] (1 raz na turę)</style>
256. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 4 — opis] [OnSucceedAttackTail] 다음 턴에 [Binding] 2 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Binding]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackTail] Inflict 2 [Binding] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttackTail] następnej tury nakłada 2 [Binding] (1 raz na turę)<style="highlight"></style>
257. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 5 — opis] <style="highlight">[OnSucceedAttackTail] 다음 턴에 [DefenseDown] 2 부여 (턴 당 1회)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100721].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttackTail] Inflict 2 [DefenseDown] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttackTail] następnej tury nakłada 2 [DefenseDown] (1 raz na turę)</style>
258. [Pasywka E.G.O — nazwa] 눌어붙은 가죽
   źródło: Passive_Ego.json :: dataList[id=2100711].name
   limit: do 40 znaków
   EN: Grimy Hide
   PL: Zaskorupiona Skóra
259. [Pasywka E.G.O — opis] 전투 시작 시 자신에게 부정적인 효과가 부여되어 있으면 [ParryingResultUp] 1, [Endurance] 1 얻음\n- 자신에게 부여된 부정적 효과 3개당 [Protection] 1 얻음 (최대 2)
   źródło: Passive_Ego.json :: dataList[id=2100711].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [ParryingResultUp], [Endurance], [Protection]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up; [Protection] = 보호 / Protection
   EN: Combat Start: if this unit has a negative effect, gain 1 [ParryingResultUp] and 1 [Endurance]\n- Gain 1 [Protection] for every 3 negative effect on self (max 2)
   PL: Początek walki: jeżeli ta jednostka ma nałożony negatywny efekt, zyskuje 1 [ParryingResultUp] i 1 [Endurance]\n- zyskuje 1 [Protection] za każde 3 negatywnych efektów na sobie (maks. 2)

## E.G.O [21008] Tears of the Tarnished Blood [汚血泣淚] (오혈읍루 [汚血泣淚]) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21008`

260. [Karta E.G.O — nazwa] 오혈읍루 [汚血泣淚]
   źródło: Egos.json :: dataList[id=21008].name
   limit: do 50 znaków
   EN: Tears of the Tarnished Blood [汚血泣淚]
   PL: Łzy Splamionej Krwi [汚血泣淚]
261. [Karta E.G.O — opis] 싱클레어의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21008].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 오혈읍루
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].name ; dataList[id=2100811].levelList[level=3].name ; dataList[id=2100811].levelList[level=4].name
   limit: do 40 znaków
   EN: Tears of the Tarnished Blood
   PL: Łzy Splamionej Krwi
263. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 응룡
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].abName ; dataList[id=2100811].levelList[level=3].abName ; dataList[id=2100811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Yinglong
   PL: Yinglong
264. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [StartBattle] [YesdragonNodie] 얻음\n[BeforeAttack] 탐식 공명 수만큼 [YesdragonSelf] 얻음 (최대 5)\n[BeforeAttack] (자신의 [YesdragonSelf] x 2) 만큼 체력 피해 받음\n- 이 효과로 체력이 흐트러짐 구간 이하가 되면 흐트러지지 않고, 자신의 현재 체력보다 높은 흐트러짐 구간 제거\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [YesdragonNodie], [BeforeAttack], [YesdragonSelf], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [YesdragonNodie] = 불허[不許] / Denial [不許]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Gain [YesdragonNodie]\n[BeforeAttack] Gain [YesdragonSelf] equal to Gluttony Reson. (max 5)\n[BeforeAttack] Take ([YesdragonSelf] on self x 2) HP damage\n- Does not get Staggered if this lowers this unit's HP below a Stagger Threshold; instead, remove the Stagger Threshold higher than this unit's current HP\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: [StartBattle] zyskuje [YesdragonNodie]\n[BeforeAttack] zyskuje tyle [YesdragonSelf], ile wynosi Rezonans Obżarstwa (maks. 5)\n[BeforeAttack] otrzymuje (posiadane [YesdragonSelf] x 2) obrażeń HP\n- jeżeli przez ten efekt HP spadłoby poniżej progu Oszołomienia, ta jednostka nie zostaje Oszołamiona; zamiast tego usuwa próg Oszołomienia wyższy niż jej aktualne HP\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
265. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
266. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
267. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 30% 미만이거나, [YesdragonSelf] 수치가 20이면 이 코인 재사용 (스킬 당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [YesdragonSelf]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: [OnSucceedAttack] If this unit has 30% or less HP, or is at 20 [YesdragonSelf] Stack, Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] jeżeli aktualne HP tej jednostki jest poniżej 30% Maks. HP albo [YesdragonSelf] wynosi 20, ponownie używa tej Monety (1 raz na Umiejętność)
268. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] 자신의 모든 체력을 소모하여 이 코인의 피해량 +20% (턴 당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Consume all HP on self to deal +20% damage with this Coin (once per Turn)
   PL: [ReUseOnSucceedAttack] zużywa całe własne HP, by zadawać +20% obrażeń tą Monetą (1 raz na turę)
269. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">자신의 [YesdragonSelf]이 6 이상이면, 코인 위력 +1</style>\n[StartBattle] [YesdragonNodie] 얻음\n[BeforeAttack] 탐식 공명 수만큼 [YesdragonSelf] 얻음 (최대 5)\n[BeforeAttack] (자신의 [YesdragonSelf] x 2) 만큼 체력 피해 받음\n- 이 효과로 체력이 흐트러짐 구간 이하가 되면 흐트러지지 않고, 자신의 현재 체력보다 높은 흐트러짐 구간 제거\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=3].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [YesdragonSelf], [StartBattle], [YesdragonNodie], [BeforeAttack], [EndSkill]
   znaczenie tagów: [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [StartBattle] = [전투 시작시] / [Combat Start]; [YesdragonNodie] = 불허[不許] / Denial [不許]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">At 6+ [YesdragonSelf], Coin Power +1</style>\n[StartBattle] Gain [YesdragonNodie]\n[BeforeAttack] Gain [YesdragonSelf] equal to Gluttony Reson. (max 5)\n[BeforeAttack] Take ([YesdragonSelf] on self x 2) HP damage\n- Does not get Staggered if this lowers this unit's HP below a Stagger Threshold; instead, remove the Stagger Threshold higher than this unit's current HP\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: <style="highlight">przy 6+ [YesdragonSelf] Moc Monety +1</style>\n[StartBattle] zyskuje [YesdragonNodie]\n[BeforeAttack] zyskuje tyle [YesdragonSelf], ile wynosi Rezonans Obżarstwa (maks. 5)\n[BeforeAttack] otrzymuje (posiadane [YesdragonSelf] x 2) obrażeń HP\n- jeżeli przez ten efekt HP spadłoby poniżej progu Oszołomienia, ta jednostka nie zostaje Oszołamiona; zamiast tego usuwa próg Oszołomienia wyższy niż jej aktualne HP\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
270. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
271. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Burst]
272. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 30% 미만이거나, [YesdragonSelf] 수치가 20이면 이 코인 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [YesdragonSelf]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: [OnSucceedAttack] If this unit has 30% or less HP, or is at 20 [YesdragonSelf] Stack, Reuse this Coin (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli aktualne HP tej jednostki jest poniżej 30% Maks. HP albo [YesdragonSelf] wynosi 20, ponownie używa tej Monety (1 raz na Umiejętność)<style="highlight"></style>
273. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] 자신의 모든 체력을 소모하여 이 코인의 피해량 +20% (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Consume all HP on self to deal +20% damage with this Coin (once per Turn)<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] zużywa całe własne HP, by zadawać +20% obrażeń tą Monetą (1 raz na turę)<style="highlight"></style>
274. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] <style="highlight">자신의 [YesdragonSelf] 6 당 코인 위력 +1 (최대 3)</style>\n[StartBattle] [YesdragonNodie] 얻음\n[BeforeAttack] 탐식 공명 수만큼 [YesdragonSelf] 얻음 (최대 5)\n[BeforeAttack] (자신의 [YesdragonSelf] x 2) 만큼 체력 피해 받음\n- 이 효과로 체력이 흐트러짐 구간 이하가 되면 흐트러지지 않고, 자신의 현재 체력보다 높은 흐트러짐 구간 제거\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [YesdragonSelf], [StartBattle], [YesdragonNodie], [BeforeAttack], [EndSkill]
   znaczenie tagów: [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [StartBattle] = [전투 시작시] / [Combat Start]; [YesdragonNodie] = 불허[不許] / Denial [不許]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">Coin Power +1 for every 6 [YesdragonSelf] on self (max 3)</style>\n[StartBattle] Gain [YesdragonNodie]\n[BeforeAttack] Gain [YesdragonSelf] equal to Gluttony Reson. (max 5)\n[BeforeAttack] Take ([YesdragonSelf] on self x 2) HP damage\n- Does not get Staggered if this lowers this unit's HP below a Stagger Threshold; instead, remove the Stagger Threshold higher than this unit's current HP\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: <style="highlight">Moc Monety +1 za każde 6 [YesdragonSelf] na tej jednostce (maks. 3)</style>\n[StartBattle] zyskuje [YesdragonNodie]\n[BeforeAttack] zyskuje tyle [YesdragonSelf], ile wynosi Rezonans Obżarstwa (maks. 5)\n[BeforeAttack] otrzymuje (posiadane [YesdragonSelf] x 2) obrażeń HP\n- jeżeli przez ten efekt HP spadłoby poniżej progu Oszołomienia, ta jednostka nie zostaje Oszołamiona; zamiast tego usuwa próg Oszołomienia wyższy niż jej aktualne HP\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
275. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">자신의 잃은 체력 2%당 피해량 +1% (최대 40%)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight"> Deal +1% damage for every 2% missing HP on self (max 40%)</style>
   PL: <style="highlight">zadaje +1% obrażeń za każde 2% brakującego HP (maks. 40%)</style>
276. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Burst]<style="highlight"></style>
277. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 30% 미만이거나, [YesdragonSelf] 수치가 20이면 이 코인 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 4 — opis] [ReUseOnSucceedAttack] 자신의 모든 체력을 소모하여 이 코인의 피해량 +20% (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100811].levelList[level=4].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 오혈읍루
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].name ; dataList[id=2100821].levelList[level=3].name ; dataList[id=2100821].levelList[level=4].name
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 응룡
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].abName ; dataList[id=2100821].levelList[level=3].abName ; dataList[id=2100821].levelList[level=4].abName
   (powtórzenie elementu 263 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[StartBattle] [YesdragonNodie] 얻음\n[BeforeAttack] (탐식 공명 수+4)만큼 [YesdragonSelf] 얻음 (최대 10)\n[BeforeAttack] (자신의 [YesdragonSelf] x 2) 만큼 체력 피해 받음\n- 이 효과로 체력이 흐트러짐 구간 이하가 되면 흐트러지지 않고, 자신의 현재 체력보다 높은 흐트러짐 구간 제거
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [StartBattle], [YesdragonNodie], [BeforeAttack], [YesdragonSelf]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [StartBattle] = [전투 시작시] / [Combat Start]; [YesdragonNodie] = 불허[不許] / Denial [不許]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: [CantIdentify]\nTargets randomly\n[StartBattle] Gain [YesdragonNodie]\n[BeforeAttack] Gain (Gluttony Reson. + 4) [YesdragonSelf] (max 10)\n[BeforeAttack] Take ([YesdragonSelf] on self x 2) HP damage\nDoes not get Staggered if this lowers this unit's HP below a Stagger Threshold; instead, remove the Stagger Threshold higher than this unit's current HP
   PL: [CantIdentify]\nAtakuje losowy cel\n[StartBattle] zyskuje [YesdragonNodie]\n[BeforeAttack] zyskuje (Rezonans Obżarstwa + 4) [YesdragonSelf] (maks. 10)\n[BeforeAttack] otrzymuje (posiadane [YesdragonSelf] x 2) obrażeń HP\n- jeżeli przez ten efekt HP spadłoby poniżej progu Oszołomienia, ta jednostka nie zostaje Oszołamiona; zamiast tego usuwa próg Oszołomienia wyższy niż jej aktualne HP
282. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 30% 미만이거나, [YesdragonSelf] 수치가 20이면 이 코인 재사용 (스킬 당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [ReUseOnSucceedAttack] 자신의 모든 체력을 소모하여 이 코인의 피해량 +20% (턴 당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">자신의 [YesdragonSelf]이 10 이상이면, 기본 위력 +1</style>\n[StartBattle] [YesdragonNodie] 얻음\n[BeforeAttack] (탐식 공명 수+4)만큼 [YesdragonSelf] 얻음 (최대 10)\n[BeforeAttack] (자신의 [YesdragonSelf] x 2) 만큼 체력 피해 받음\n- 이 효과로 체력이 흐트러짐 구간 이하가 되면 흐트러지지 않고, 자신의 현재 체력보다 높은 흐트러짐 구간 제거
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=3].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [YesdragonSelf], [StartBattle], [YesdragonNodie], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [StartBattle] = [전투 시작시] / [Combat Start]; [YesdragonNodie] = 불허[不許] / Denial [不許]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">At 10+ [YesdragonSelf], Base Power +1</style>\n[StartBattle] Gain [YesdragonNodie]\n[BeforeAttack] Gain (Gluttony Reson. + 4) [YesdragonSelf] (max 10)\n[BeforeAttack] Take ([YesdragonSelf] on self x 2) HP damage\nDoes not get Staggered if this lowers this unit's HP below a Stagger Threshold; instead, remove the Stagger Threshold higher than this unit's current HP
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">przy 10+ [YesdragonSelf] Moc Bazowa +1</style>\n[StartBattle] zyskuje [YesdragonNodie]\n[BeforeAttack] zyskuje (Rezonans Obżarstwa + 4) [YesdragonSelf] (maks. 10)\n[BeforeAttack] otrzymuje (posiadane [YesdragonSelf] x 2) obrażeń HP\n- jeżeli przez ten efekt HP spadłoby poniżej progu Oszołomienia, ta jednostka nie zostaje Oszołamiona; zamiast tego usuwa próg Oszołomienia wyższy niż jej aktualne HP
287. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 30% 미만이거나, [YesdragonSelf] 수치가 20이면 이 코인 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [ReUseOnSucceedAttack] 자신의 모든 체력을 소모하여 이 코인의 피해량 +20% (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">자신의 [YesdragonSelf] 10 당 기본 위력 +1 (최대 2)</style>\n[StartBattle] [YesdragonNodie] 얻음\n[BeforeAttack] (탐식 공명 수+4)만큼 [YesdragonSelf] 얻음 (최대 10)\n[BeforeAttack] (자신의 [YesdragonSelf] x 2) 만큼 체력 피해 받음\n- 이 효과로 체력이 흐트러짐 구간 이하가 되면 흐트러지지 않고, 자신의 현재 체력보다 높은 흐트러짐 구간 제거
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=4].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [YesdragonSelf], [StartBattle], [YesdragonNodie], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [YesdragonSelf] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [StartBattle] = [전투 시작시] / [Combat Start]; [YesdragonNodie] = 불허[不許] / Denial [不許]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">Base Power +1 for every 10 [YesdragonSelf] on self (max 2)</style>\n[StartBattle] Gain [YesdragonNodie]\n[BeforeAttack] Gain (Gluttony Reson. + 4) [YesdragonSelf] (max 10)\n[BeforeAttack] Take ([YesdragonSelf] on self x 2) HP damage\nDoes not get Staggered if this lowers this unit's HP below a Stagger Threshold; instead, remove the Stagger Threshold higher than this unit's current HP
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">Moc Bazowa +1 za każde 10 [YesdragonSelf] na tej jednostce (maks. 2)</style>\n[StartBattle] zyskuje [YesdragonNodie]\n[BeforeAttack] zyskuje (Rezonans Obżarstwa + 4) [YesdragonSelf] (maks. 10)\n[BeforeAttack] otrzymuje (posiadane [YesdragonSelf] x 2) obrażeń HP\n- jeżeli przez ten efekt HP spadłoby poniżej progu Oszołomienia, ta jednostka nie zostaje Oszołamiona; zamiast tego usuwa próg Oszołomienia wyższy niż jej aktualne HP
292. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">자신의 잃은 체력 2%당 피해량 +1% (최대 40%)</style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 30% 미만이거나, [YesdragonSelf] 수치가 20이면 이 코인 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] 자신의 모든 체력을 소모하여 이 코인의 피해량 +20% (턴 당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100821].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Pasywka E.G.O — nazwa] 읍루
   źródło: Passive_Ego.json :: dataList[id=2100811].name
   limit: do 40 znaków
   EN: Crying Tears
   PL: Płaczące Łzy
297. [Pasywka E.G.O — opis] - 턴 종료시, 이번 턴에 자신이 부정적인 효과를 보유했거나 자신의 체력이나 정신력이 감소했으면 정신력 5 회복.\n- 아군이나 자신이 사망한 경우 다음 턴에 모든 적에게 [Vulnerable] 1 부여 (턴 당 최대 1회)
   źródło: Passive_Ego.json :: dataList[id=2100811].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: - Turn End: If this unit had a negative effect or lost its HP or SP, heal 5 SP.\n- If this unit or an ally is defeated, inflict 1 [Vulnerable] to all enemies next turn (once per turn)
   PL: - na koniec tury, jeżeli ta jednostka miała negatywny efekt albo straciła HP lub SP, odzyskuje 5 SP.\n- jeżeli ta jednostka lub sojusznik został pokonany, następnej tury nakłada 1 [Vulnerable] na wszystkich wrogów (maks. 1 raz na turę)

## E.G.O [21009] Harmony (하모니) — Sinclair
- postać: Sinclair (싱클레어) · ID E.G.O: `21009`

298. [Karta E.G.O — nazwa] 하모니
   źródło: Egos.json :: dataList[id=21009].name
   limit: do 40 znaków
   EN: Harmony
   PL: Harmonia
299. [Karta E.G.O — opis] 싱클레어 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21009].desc
   limit: do 120 znaków
   EN: Sinclair’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Sinclair
300. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 하모니
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].name ; dataList[id=2100911].levelList[level=3].name ; dataList[id=2100911].levelList[level=4].name
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 노래하는 기계
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].abName ; dataList[id=2100911].levelList[level=3].abName ; dataList[id=2100911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Singing Machine
   PL: Śpiewająca Maszyna
302. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 메인 타겟의 [Laceration]과 [Combustion]의 합 2당, 합 위력 +1 (최대 6)\n자신의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse> (최대 10%)\n서브 타겟에게 가하는 피해량 -50%\n[TargetKill] 모든 아군이 다음 턴에 [ThatIsRhythm] 2 얻음 (스킬당 1회)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 (1 + 최대 공명 수)명의 정신력 8 회복 (최대 4명)\n[EndSkill] 2턴 동안 전투 종료 시 정신력 8 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Laceration], [Combustion], [TargetKill], [ThatIsRhythm], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [TargetKill] = [대상 처치 시] / [On Target Kill]; [ThatIsRhythm] = 리듬 / Rhythm; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Clash Power +1 for every 2 ([Laceration] + [Combustion]) on the main target (max 6)\nDeal more damage based on missing HP on self (max 10%)\nDeal -50% damage against sub-targets\n[TargetKill] All allies gain 2 [ThatIsRhythm] next turn (once per Skill)\n[EndSkill] Heal 8 SP for (1 + highest Reson.) other allies with the least SP (max 4 units)\n[EndSkill] For 2 turns, lose 8 SP at Combat End
   PL: Moc Walki +1 za każde 2 (suma [Laceration] i [Combustion]) na celu głównym (maks. 6)\nzadaje więcej obrażeń w zależności od brakującego HP (maks. 10%)\nzadaje -50% obrażeń celom pobocznym\n[TargetKill] wszyscy sojusznicy następnej tury zyskują 2 [ThatIsRhythm] (1 raz na Umiejętność)\n[EndSkill] odzyskuje 8 SP dla (1 + najwyższy Rezonans) sojuszników z najniższym SP innych niż ta jednostka (maks. 4 jednostki)\n[EndSkill] przez 2 tury traci 8 SP na koniec walki
303. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100911].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2100911].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2100911].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 자신의 체력이 10% 이상이면, 4 ~ 8 만큼 체력 피해 입음 (코인당 1회)\n- 이후 이 코인 재사용 (스킬당 최대 4회)\n- 이 효과로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2100911].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2100911].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] At 10%+ HP, take 4 ~ 8 HP damage (once per Coin)\n- Then, Reuse this Coin (4 times per Skill)\n- This damage does not Stagger or reduce this unit's HP below 1
   PL: [OnSucceedAttackHead] przy HP 10% lub wyższym, otrzymuje 4 ~ 8 obrażeń HP (1 raz na Monetę)\n- po czym ponownie używa tej Monety (maks. 4 razy na Umiejętność)\n- te obrażenia nie Oszołamiają i nie obniżają HP tej jednostki poniżej 1
306. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 1 — podsumowanie] [OnSucceedAttackHead] 자신의 체력 소모 후 이 코인 재사용
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#2].coindescs[#0].summary ; dataList[id=2100911].levelList[level=3].coinlist[#2].coindescs[#0].summary ; dataList[id=2100911].levelList[level=4].coinlist[#2].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] After consuming HP on self, Reuse this Coin
   PL: [OnSucceedAttackHead] po zużyciu własnego HP, ponownie używa tej Monety
307. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2100911].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2100911].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=2100911].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2100911].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 무작위 아군 1명이 다음 턴에 [ThatIsRhythm] 1 얻음 (코인당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThatIsRhythm]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThatIsRhythm] = 리듬 / Rhythm
   EN: [OnSucceedAttack] A random ally gains 1 [ThatIsRhythm] next turn (once per Coin)
   PL: [OnSucceedAttack] 1 losowy sojusznik następnej tury zyskuje 1 [ThatIsRhythm] (1 raz na Monetę)
310. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 메인 타겟의 [Laceration]과 [Combustion]의 합 2당, 합 위력 +1 (최대 <style="highlight">8</style>)\n자신의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse> (최대 <style="highlight">15</style>%)\n서브 타겟에게 가하는 피해량 -50%\n[TargetKill] 모든 아군이 다음 턴에 [ThatIsRhythm] 2 얻음 (스킬당 1회)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 (1 + 최대 공명 수)명의 정신력 <style="highlight">10</style> 회복 (최대 4명)\n[EndSkill] 2턴 동안 전투 종료 시 정신력 8 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=3].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [Laceration], [Combustion], [TargetKill], [ThatIsRhythm], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [TargetKill] = [대상 처치 시] / [On Target Kill]; [ThatIsRhythm] = 리듬 / Rhythm; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Clash Power +1 for every 2 ([Laceration] + [Combustion]) on the main target (max <style="highlight">8</style>)\nDeal more damage based on missing HP on self (max <style="highlight">15</style>%)\nDeal -50% damage against sub-targets\n[TargetKill] All allies gain 2 [ThatIsRhythm] next turn (once per Skill)\n[EndSkill] Heal <style="highlight">10</style> SP for (1 + highest Reson.) other allies with the least SP (max 4 units)\n[EndSkill] For 2 turns, lose 8 SP at Combat End
   PL: Moc Walki +1 za każde 2 (suma [Laceration] i [Combustion]) na celu głównym (maks. <style="highlight">8</style>)\nzadaje więcej obrażeń w zależności od brakującego HP (maks. <style="highlight">15</style>%)\nzadaje -50% obrażeń celom pobocznym\n[TargetKill] wszyscy sojusznicy następnej tury zyskują 2 [ThatIsRhythm] (1 raz na Umiejętność)\n[EndSkill] odzyskuje <style="highlight">10</style> SP dla (1 + najwyższy Rezonans) sojuszników z najniższym SP innych niż ta jednostka (maks. 4 jednostki)\n[EndSkill] przez 2 tury traci 8 SP na koniec walki
311. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 무작위 아군 1명이 다음 턴에 [ThatIsRhythm] <style="highlight">1 ~ 2</style> 얻음 (코인당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThatIsRhythm]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThatIsRhythm] = 리듬 / Rhythm
   EN: [OnSucceedAttack] A random ally gains <style="highlight">1 ~ 2</style> [ThatIsRhythm] next turn (once per Coin)
   PL: [OnSucceedAttack] 1 losowy sojusznik następnej tury zyskuje <style="highlight">1 ~ 2</style> [ThatIsRhythm] (1 raz na Monetę)
312. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 메인 타겟의 [Laceration]과 [Combustion]의 합 2당, 합 위력 +1 (최대 <style="highlight">10</style>)\n자신의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse> (최대 <style="highlight">20</style>%)\n서브 타겟에게 가하는 피해량 -50%\n[TargetKill] 모든 아군이 다음 턴에 [ThatIsRhythm] 2 얻음 (스킬당 1회)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 (1 + 최대 공명 수)명의 정신력 <style="highlight">12</style> 회복 (최대 4명)\n[EndSkill] 2턴 동안 전투 종료 시 정신력 8 감소
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [Laceration], [Combustion], [TargetKill], [ThatIsRhythm], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [TargetKill] = [대상 처치 시] / [On Target Kill]; [ThatIsRhythm] = 리듬 / Rhythm; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Clash Power +1 for every 2 ([Laceration] + [Combustion]) on the main target (max <style="highlight">10</style>)\nDeal more damage based on missing HP on self (max <style="highlight">20</style>%)\nDeal -50% damage against sub-targets\n[TargetKill] All allies gain 2 [ThatIsRhythm] next turn (once per Skill)\n[EndSkill] Heal <style="highlight">12 SP</style> for (1 + highest Reson.) other allies with the least SP (max 4 units)\n[EndSkill] For 2 turns, lose 8 SP at Combat End
   PL: Moc Walki +1 za każde 2 (suma [Laceration] i [Combustion]) na celu głównym (maks. <style="highlight">10</style>)\nzadaje więcej obrażeń w zależności od brakującego HP (maks. <style="highlight">20</style>%)\nzadaje -50% obrażeń celom pobocznym\n[TargetKill] wszyscy sojusznicy następnej tury zyskują 2 [ThatIsRhythm] (1 raz na Umiejętność)\n[EndSkill] odzyskuje <style="highlight">12</style> SP dla (1 + najwyższy Rezonans) sojuszników z najniższym SP innych niż ta jednostka (maks. 4 jednostki)\n[EndSkill] przez 2 tury traci 8 SP na koniec walki
313. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 무작위 아군 1명이 다음 턴에 [ThatIsRhythm] 1 ~ <style="highlight">3</style> 얻음 (코인당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100911].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThatIsRhythm]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThatIsRhythm] = 리듬 / Rhythm
   EN: [OnSucceedAttack] A random ally gains 1 ~ <style="highlight">3</style> [ThatIsRhythm] next turn (once per Coin)
   PL: [OnSucceedAttack] 1 losowy sojusznik następnej tury zyskuje 1 ~ <style="highlight">3</style> [ThatIsRhythm] (1 raz na Monetę)
314. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 하모니
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].name ; dataList[id=2100921].levelList[level=3].name ; dataList[id=2100921].levelList[level=4].name
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 노래하는 기계
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].abName ; dataList[id=2100921].levelList[level=3].abName ; dataList[id=2100921].levelList[level=4].abName
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n메인 타겟의 [Laceration]과 [Combustion]의 합 2당, 합 위력 +1 (최대 6)\n자신의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse> (최대 10%)\n서브 타겟에게 가하는 피해량 -50%\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 2, 소수점 버림)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -6)\n[EndSkill] 정신력이 가장 낮은 아군 4명의 정신력 10 회복\n[EndSkill] 모든 아군이 다음 턴에 [ThatIsRhythm] 2, [CrimsonDamageUp] 1, [ScarletDamageUp] 1, [VioletDamageUp] 1, [Vulnerable] 1 얻음\n- 대상을 처치했으면, 이 효과 한 번 더 발동
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [CantIdentify], [Laceration], [Combustion], [BeforeAttack], [EndSkill], [ThatIsRhythm], [CrimsonDamageUp], [ScarletDamageUp], [VioletDamageUp], [Vulnerable]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [ThatIsRhythm] = 리듬 / Rhythm; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up; [ScarletDamageUp] = 색욕 피해량 증가 / Lust DMG Up …
   EN: [CantIdentify]\nTargets randomly\nClash Power +1 for every 2 ([Laceration] + [Combustion]) on the main target (max 6)\nDeal more damage based on missing HP on self (max 10%)\nDeal -50% damage against sub-targets\n[BeforeAttack] Gain Atk Weight equal to (highest Reson. / 2) (max 2; rounded down)\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -6)\n[EndSkill] Heal 10 SP for 4 other allies with the least SP\n[EndSkill] All allies gain 2 [ThatIsRhythm], 1 [CrimsonDamageUp], 1 [ScarletDamageUp], 1 [VioletDamageUp], 1 [Vulnerable] next turn\n- If target was killed, activate the effect above once more
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Walki +1 za każde 2 (suma [Laceration] i [Combustion]) na celu głównym (maks. 6)\nzadaje więcej obrażeń w zależności od brakującego HP (maks. 10%)\nzadaje -50% obrażeń celom pobocznym\n[BeforeAttack] zyskuje Wagę Ataku równą (najwyższy Rezonans / 2) (maks. 2, zaokrąglone w dół)\n[BeforeAttack] -2 do Mocy Bazowej za każdą zniszczoną Monetę (maks. -6)\n[EndSkill] odzyskuje 10 SP dla 4 sojuszników z najniższym SP innych niż ta jednostka\n[EndSkill] wszyscy sojusznicy następnej tury zyskują 2 [ThatIsRhythm], 1 [CrimsonDamageUp], 1 [ScarletDamageUp], 1 [VioletDamageUp], 1 [Vulnerable]\n- jeżeli cel został pokonany, uruchamia powyższy efekt jeszcze raz
317. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2100921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2100921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2100921].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2100921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2100921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2100921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2100921].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2100921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2100921].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2100921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 10% 이상이면, 10 ~ 20 만큼 체력 피해 입음 (코인당 1회)\n- 이후 이 효과로 소모된 체력의 합이 50미만이면, 이 코인 재사용 (스킬당 최대 4회)\n- 이 효과로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2100921].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2100921].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10%+ HP, take 10 ~ 20 HP damage (once per Coin)\n- Then, Reuse this Coin if the sum of HP lost due to this effect is less than 50 (4 times per Skill)\n- This damage does not Stagger or reduce this unit's HP below 1
   PL: [OnSucceedAttack] przy HP 10% lub wyższym, otrzymuje 10 ~ 20 obrażeń HP (1 raz na Monetę)\n- po czym ponownie używa tej Monety, jeżeli suma HP zużytego przez ten efekt jest niższa niż 50 (maks. 4 razy na Umiejętność)\n- te obrażenia nie Oszołamiają i nie obniżają HP tej jednostki poniżej 1
323. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 2 — podsumowanie] [OnSucceedAttack] 자신의 체력 소모\n조건 만족 시 이 코인 재사용
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#2].coindescs[#1].summary ; dataList[id=2100921].levelList[level=3].coinlist[#2].coindescs[#1].summary ; dataList[id=2100921].levelList[level=4].coinlist[#2].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Consume HP on self\nReuse this Coin if conditions are met
   PL: [OnSucceedAttack] zużywa własne HP\nponownie używa tej Monety, jeżeli warunki są spełnione
324. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=2100921].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2100921].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#2].coindescs[#3].desc ; dataList[id=2100921].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=2100921].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 무작위 아군 1명이 다음 턴에 [ThatIsRhythm] 1 얻음 (코인당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=1].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n메인 타겟의 [Laceration]과 [Combustion]의 합 2당, 합 위력 +1 (최대 <style="highlight">8</style>)\n자신의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse> (최대 <style="highlight">15</style>%)\n서브 타겟에게 가하는 피해량 -50%\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 2, 소수점 버림)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -6)\n[EndSkill] 정신력이 가장 낮은 아군 4명의 정신력 <style="highlight">12</style> 회복\n[EndSkill] 모든 아군이 다음 턴에 [ThatIsRhythm] 2, [CrimsonDamageUp] 1, [ScarletDamageUp] 1, [VioletDamageUp] 1, [Vulnerable] 1 얻음\n- 대상을 처치했으면, 이 효과 한 번 더 발동
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=3].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [CantIdentify], [Laceration], [Combustion], [BeforeAttack], [EndSkill], [ThatIsRhythm], [CrimsonDamageUp], [ScarletDamageUp], [VioletDamageUp], [Vulnerable]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [ThatIsRhythm] = 리듬 / Rhythm; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up; [ScarletDamageUp] = 색욕 피해량 증가 / Lust DMG Up …
   EN: [CantIdentify]\nTargets randomly\nClash Power +1 for every 2 ([Laceration] + [Combustion]) on the main target (max <style="highlight">8</style>)\nDeal more damage based on missing HP on self (max <style="highlight">15</style>%)\nDeal -50% damage against sub-targets\n[BeforeAttack] Gain Atk Weight equal to (highest Reson. / 2) (max 2; rounded down)\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -6)\n[EndSkill] Heal <style="highlight">12</style> SP for 4 other allies with the least SP\n[EndSkill] All allies gain 2 [ThatIsRhythm], 1 [CrimsonDamageUp], 1 [ScarletDamageUp], 1 [VioletDamageUp], 1 [Vulnerable] next turn\n- If target was killed, activate the effect above once more
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Walki +1 za każde 2 (suma [Laceration] i [Combustion]) na celu głównym (maks. <style="highlight">8</style>)\nzadaje więcej obrażeń w zależności od brakującego HP (maks. <style="highlight">15</style>%)\nzadaje -50% obrażeń celom pobocznym\n[BeforeAttack] zyskuje Wagę Ataku równą (najwyższy Rezonans / 2) (maks. 2, zaokrąglone w dół)\n[BeforeAttack] -2 do Mocy Bazowej za każdą zniszczoną Monetę (maks. -6)\n[EndSkill] odzyskuje <style="highlight">12</style> SP dla 4 sojuszników z najniższym SP innych niż ta jednostka\n[EndSkill] wszyscy sojusznicy następnej tury zyskują 2 [ThatIsRhythm], 1 [CrimsonDamageUp], 1 [ScarletDamageUp], 1 [VioletDamageUp], 1 [Vulnerable]\n- jeżeli cel został pokonany, uruchamia powyższy efekt jeszcze raz
328. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 무작위 아군 1명이 다음 턴에 [ThatIsRhythm] <style="highlight">1 ~ 2</style> 얻음 (코인당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=3].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n메인 타겟의 [Laceration]과 [Combustion]의 합 2당, 합 위력 +1 (최대 <style="highlight">10</style>)\n자신의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse> (최대 <style="highlight">20</style>%)\n서브 타겟에게 가하는 피해량 -50%\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 2, 소수점 버림)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -6)\n[EndSkill] 정신력이 가장 낮은 아군 4명의 정신력 <style="highlight">15</style> 회복\n[EndSkill] 모든 아군이 다음 턴에 [ThatIsRhythm] 2, [CrimsonDamageUp] 1, [ScarletDamageUp] 1, [VioletDamageUp] 1, [Vulnerable] 1 얻음\n- 대상을 처치했으면, 이 효과 한 번 더 발동
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=4].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [CantIdentify], [Laceration], [Combustion], [BeforeAttack], [EndSkill], [ThatIsRhythm], [CrimsonDamageUp], [ScarletDamageUp], [VioletDamageUp], [Vulnerable]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [ThatIsRhythm] = 리듬 / Rhythm; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up; [ScarletDamageUp] = 색욕 피해량 증가 / Lust DMG Up …
   EN: [CantIdentify]\nTargets randomly\nClash Power +1 for every 2 ([Laceration] + [Combustion]) on the main target (max <style="highlight">10</style>)\nDeal more damage based on missing HP on self (max <style="highlight">20</style>%)\nDeal -50% damage against sub-targets\n[BeforeAttack] Gain Atk Weight equal to (highest Reson. / 2) (max 2; rounded down)\n[BeforeAttack] Base Power -2 for every Cracked Coin (max -6)\n[EndSkill] Heal <style="highlight">15</style> SP for 4 other allies with the least SP\n[EndSkill] All allies gain 2 [ThatIsRhythm], 1 [CrimsonDamageUp], 1 [ScarletDamageUp], 1 [VioletDamageUp], 1 [Vulnerable] next turn\n- If target was killed, activate the effect above once more
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Walki +1 za każde 2 (suma [Laceration] i [Combustion]) na celu głównym (maks. <style="highlight">10</style>)\nzadaje więcej obrażeń w zależności od brakującego HP (maks. <style="highlight">20</style>%)\nzadaje -50% obrażeń celom pobocznym\n[BeforeAttack] zyskuje Wagę Ataku równą (najwyższy Rezonans / 2) (maks. 2, zaokrąglone w dół)\n[BeforeAttack] -2 do Mocy Bazowej za każdą zniszczoną Monetę (maks. -6)\n[EndSkill] odzyskuje <style="highlight">15</style> SP dla 4 sojuszników z najniższym SP innych niż ta jednostka\n[EndSkill] wszyscy sojusznicy następnej tury zyskują 2 [ThatIsRhythm], 1 [CrimsonDamageUp], 1 [ScarletDamageUp], 1 [VioletDamageUp], 1 [Vulnerable]\n- jeżeli cel został pokonany, uruchamia powyższy efekt jeszcze raz
330. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 무작위 아군 1명이 다음 턴에 [ThatIsRhythm] 1 ~ <style="highlight">3</style> 얻음 (코인당 1회)
   źródło: Skills_Ego_Personality-10.json :: dataList[id=2100921].levelList[level=4].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Pasywka E.G.O — nazwa] 그건, 리듬이었어요
   źródło: Passive_Ego.json :: dataList[id=2100911].name
   limit: do 40 znaków
   EN: That... was Indeed a Rhythm
   PL: To... Był Na Prawdę Rytm
332. [Pasywka E.G.O — opis] 턴 시작 시 [ThatIsRhythm] 2 얻음\n\n대상 처치 시 자신의 체력을 최대 체력의 5%만큼 회복하고, 자신의 정신력 5 회복 (턴당 1회)\n- E.G.O 스킬 - 하모니로 처치했으면 위 효과가 2배로 적용됨\n\n이번 턴에 자신의 정신력이 감소했으면, 턴 종료 시 자신의 정신력을 (4 + 적 전체의 [Combustion]과 [Laceration] 위력의 합 / 10)만큼 회복 (최대 10, 소수점 버림)
   źródło: Passive_Ego.json :: dataList[id=2100911].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [ThatIsRhythm], [Combustion], [Laceration]
   znaczenie tagów: [ThatIsRhythm] = 리듬 / Rhythm; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: Turn Start: Gain 2 [ThatIsRhythm]\n\nOn Target Kill: This unit heals 5% HP and 5 SP (once per turn)\n- If target was killed by E.G.O Skill - Harmony, double the amount this effect heals\n\nTurn End: If this unit lost SP this turn, heal (4 + sum of [Combustion] and [Laceration] on all enemies / 10) SP (max 10; rounded down)
   PL: na początku tury zyskuje 2 [ThatIsRhythm]\n\npo pokonaniu celu ta jednostka odzyskuje 5% HP i 5 SP (1 raz na turę)\n- jeżeli cel został pokonany Umiejętnością E.G.O „Harmonia", ten efekt leczy podwójną ilość\n\nna koniec tury, jeżeli ta jednostka straciła SP w tej turze, odzyskuje (4 + suma Siły [Combustion] i [Laceration] wszystkich wrogów / 10) SP (maks. 10, zaokrąglone w dół)

## E.G.O [21101] To Páthos Máthos (토 파토스 마토스) — Outis
- postać: Outis (오티스) · ID E.G.O: `21101`

333. [Karta E.G.O — nazwa] 토 파토스 마토스
   źródło: Egos-a1c9p3.json :: dataList[id=211011].name
   limit: do 40 znaków
   EN: To Páthos Máthos
   PL: To Páthos Máthos
334. [Karta E.G.O — opis] 오티스 연출 전용 EGO 장비
   źródło: Egos-a1c9p3.json :: dataList[id=211011].desc
   limit: do 120 znaków
   EN: Outis's Battle Cinematic Exclusive E.G.O
   PL: Wyłączny Sprzęt E.G.O Outis ze Scenką Walki
335. [Karta E.G.O — nazwa] 토 파토스 마토스
   źródło: Egos.json :: dataList[id=21101].name
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Karta E.G.O — opis] 오티스의 기본 EGO 장비
   źródło: Egos.json :: dataList[id=21101].desc
   limit: do 120 znaków
   EN: Outis’s Base E.G.O
   PL: Podstawowy Sprzęt E.G.O Outis
337. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 토 파토스 마토스
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=1].name ; dataList[id=2110111].levelList[level=3].name ; dataList[id=2110111].levelList[level=4].name
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 오티스
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=1].abName ; dataList[id=2110111].levelList[level=3].abName ; dataList[id=2110111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Outis
   PL: Outis
339. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 체력이 50%미만일 때 피해량+10%
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has less than 50% HP, deal +10% damage
   PL: jeżeli HP celu jest niższe niż 50%, zadaje +10% obrażeń
340. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
341. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] 대상의 체력이 50%미만일 때 피해량+30%
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=3].desc ; dataList[id=2110111].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has less than 50% HP, deal +30% damage
   PL: jeżeli HP celu jest niższe niż 50%, zadaje +30% obrażeń
342. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 4 부여
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL: [OnSucceedAttack] Nakłada 4 Rozdarcia
343. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EnemyKill] 무작위 아군 1명에게 피해량 증가 1 부여
   źródło: Skills_Ego.json :: dataList[id=2110111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [AttackDmgUp]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [EnemyKill] Give 1 [AttackDmgUp] to a random ally
   PL: [EnemyKill] daje 1 [AttackDmgUp] losowemu sojusznikowi
344. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — nazwa] 토 파토스 마토스
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2110112].levelList[level=4].name
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — źródło (Anomalia)] 오티스
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2110112].levelList[level=4].abName
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 체력이 50%미만일 때 피해량 +30%
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2110112].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target’s HP is below 50%, deal +30% damage
   PL: jeżeli HP celu jest niższe niż 50%, zadaje +30% obrażeń
347. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2110112].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL: [OnSucceedAttack] Nakłada 4 [Burst]
348. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EnemyKill] 무작위 아군 1명에게 [AttackDmgUp] 1 부여
   źródło: Skills_Ego_Personality-a1c9p3.json :: dataList[id=2110112].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [AttackDmgUp]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [EnemyKill] Apply 1 [AttackDmgUp] to a random ally
   PL: [EnemyKill] nakłada 1 [AttackDmgUp] na losowego sojusznika
349. [Pasywka E.G.O — nazwa] 완벽한 전술
   źródło: Passive_Ego.json :: dataList[id=2110111].name
   limit: do 40 znaków
   EN: Tactical Perfection
   PL: Doskonała Taktyka
350. [Pasywka E.G.O — opis] 매 턴마다 한번도 피격 당하지 않을 경우, 다음 턴에 피해량 증가 1을 얻음 (최대 3회 중첩 가능)
   źródło: Passive_Ego.json :: dataList[id=2110111].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Gain 1 [AttackDmgUp] next turn if this unit isn't hit during a turn. Gain 1 more [AttackDmgUp] with every consecutive turn this unit isn't hit (max 3)
   PL: jeżeli ta jednostka nie zostanie trafiona w trakcie tury, następnej tury zyskuje 1 [AttackDmgUp]. za każdą kolejną turę bez trafienia zyskuje 1 dodatkowy [AttackDmgUp] (maks. 3)

## E.G.O [21102] Ebony Stem (검은줄기) — Outis
- postać: Outis (오티스) · ID E.G.O: `21102`

351. [Karta E.G.O — nazwa] 검은줄기
   źródło: Egos.json :: dataList[id=21102].name
   limit: do 40 znaków
   EN: Ebony Stem
   PL: Hebanowa Łodyga
352. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21102].desc
   limit: do 120 znaków
   EN: Outis’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Outis
353. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 검은줄기
   źródło: Skills_Ego.json :: dataList[id=2110211].levelList[level=1].name ; dataList[id=2110211].levelList[level=3].name
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 흑단여왕의 사과
   źródło: Skills_Ego.json :: dataList[id=2110211].levelList[level=1].abName ; dataList[id=2110211].levelList[level=3].abName
   limit: do 40 znaków
   EN: Ebony Queen's Apple
   PL: Jabłko Hebanowej Królowej
355. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110211].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110211].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110211].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110211].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
357. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 탐식 취약 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110211].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Gluttony Fragility
   PL: [OnSucceedAttack] nakłada 2 Kruchości Obżarstwa
358. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 검은줄기
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=1].name ; dataList[id=2110221].levelList[level=3].name
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 흑단여왕의 사과
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=1].abName ; dataList[id=2110221].levelList[level=3].abName
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=1].desc ; dataList[id=2110221].levelList[level=3].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 3 [Laceration]
   PL: [OnSucceedAttackHead] Nakłada 3 Krwawienia
363. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] Nakłada 5 Rozdarcia
364. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
365. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 탐식 취약 3 부여
   źródło: Skills_Ego.json :: dataList[id=2110221].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Gluttony Fragility
   PL: [OnSucceedAttack] nakłada 3 Kruchości Obżarstwa
366. [Pasywka E.G.O — nazwa] 불신의 줄기
   źródło: Passive_Ego.json :: dataList[id=2110211].name
   limit: do 40 znaków
   EN: Stem of Distrust
   PL: Łodyga Nieufności
367. [Pasywka E.G.O — opis] 매 턴마다 관통 피해량 증가 1을 얻음\n앞면 적중 시 다음 턴에 속박 1 부여, 파열 횟수 1 증가
   źródło: Passive_Ego.json :: dataList[id=2110211].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [PenetrateDamageUp], [Binding], [Burst]
   znaczenie tagów: [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [Binding] = 속박 / Bind; [Burst] = 파열 / Rupture
   EN: Gain 1 [PenetrateDamageUp] every turn\nHeads Hit: Inflict 1 [Binding] and +1 [Burst] Count next turn
   PL: co turę zyskuje 1 [PenetrateDamageUp]\nprzy trafieniu Orłem następnej tury nakłada 1 [Binding] i +1 Licznika [Burst]

## E.G.O [21103] Ya Śūnyatā Tad Rūpam (공즉시색) — Outis
- postać: Outis (오티스) · ID E.G.O: `21103`

368. [Karta E.G.O — nazwa] 공즉시색
   źródło: Egos.json :: dataList[id=21103].name
   limit: do 40 znaków
   EN: Ya Śūnyatā Tad Rūpam
   PL: Ya Śūnyatā Tad Rūpam
369. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21103].desc
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 공즉시색
   źródło: Skills_Ego.json :: dataList[id=2110311].levelList[level=1].name ; dataList[id=2110311].levelList[level=3].name
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 나는 비워내느니
   źródło: Skills_Ego.json :: dataList[id=2110311].levelList[level=1].abName ; dataList[id=2110311].levelList[level=3].abName
   limit: do 40 znaków
   EN: My Form Empties
   PL: Wolę się Opróżnić
372. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 정신력 12 회복
   źródło: Skills_Ego.json :: dataList[id=2110311].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 12 SP
   PL: [EndSkill] odzyskuje 12 SP
373. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 색욕 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2110311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Lust Fragility
   PL: [OnSucceedAttack] nakłada 1 Kruchości Żądzy
374. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 정신력 18 회복\n[EndSkill] 본인 제외 무작위 아군 2명에게 공격 위력 증가 1 부여
   źródło: Skills_Ego.json :: dataList[id=2110311].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [Enhancement]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndSkill] Heal 18 SP\n[EndSkill] Apply 1 [Enhancement] to 2 random other allies
   PL: [EndSkill] odzyskuje 18 SP\n[EndSkill] nakłada 1 [Enhancement] na 2 innych losowych sojuszników
375. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 색욕 취약 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110311].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Lust Fragility
   PL: [OnSucceedAttack] nakłada 2 Kruchości Żądzy
376. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 공즉시색
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=1].name ; dataList[id=2110321].levelList[level=3].name
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 나는 비워내느니
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=1].abName ; dataList[id=2110321].levelList[level=3].abName
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=1].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 색욕 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackTail] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttackTail] nakłada 1 [Vulnerable]
381. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 취약 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackTail] Gain 1 [Vulnerable]
   PL: [OnSucceedAttackTail] zyskuje 1 [Vulnerable]
382. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 본인 제외 무작위 아군 2명에게 공격 위력 증가 1 부여
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Apply 1 [Enhancement] to 2 random other allies
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] nakłada 1 [Enhancement] na 2 innych losowych sojuszników
383. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 색욕 취약 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable]
385. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 취약 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2110321].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackTail] Gain 2 [Vulnerable]
   PL: [OnSucceedAttackTail] zyskuje 2 [Vulnerable]
386. [Pasywka E.G.O — nazwa] 비워냄
   źródło: Passive_Ego.json :: dataList[id=2110311].name
   limit: do 40 znaków
   EN: Emptying
   PL: Opróżnianie
387. [Pasywka E.G.O — opis] 매 턴마다 색욕 피해량 증가 1을 얻음. 자신의 정신력이 0 미만이면 추가로 1을 더 얻음
   źródło: Passive_Ego.json :: dataList[id=2110311].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [ScarletDamageUp]
   znaczenie tagów: [ScarletDamageUp] = 색욕 피해량 증가 / Lust DMG Up
   EN: Gain 1 [ScarletDamageUp] every turn\nGain 1 more when this unit has less than 0 SP
   PL: co turę zyskuje 1 [ScarletDamageUp]. jeżeli SP tej jednostki jest niższe niż 0, dodatkowo zyskuje 1

## E.G.O [21104] Sunshower (여우비) — Outis
- postać: Outis (오티스) · ID E.G.O: `21104`

388. [Karta E.G.O — nazwa] 여우비
   źródło: Egos.json :: dataList[id=21104].name
   limit: do 40 znaków
   EN: Sunshower
   PL: Lisi Deszcz
389. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21104].desc
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 여우비
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=1].name ; dataList[id=2110411].levelList[level=3].name ; dataList[id=2110411].levelList[level=4].name
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 떠돌이 여우
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=1].abName ; dataList[id=2110411].levelList[level=3].abName ; dataList[id=2110411].levelList[level=4].abName
   limit: do 40 znaków
   EN: Drifting Fox
   PL: Błędny Lis
392. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 호흡 횟수 4 증가
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] Gain +4 [Breath] Count
   PL: [BeforeAttack] zyskuje +4 Licznika [Breath]
393. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] następnej tury nakłada 2 [Binding]
394. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]
   PL: [CriticalOnSucceedAttack] wywołuje [VibrationExplosion]
395. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 호흡 횟수 6 증가
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] Gain +6 [Breath] Count
   PL: [BeforeAttack] zyskuje +6 Licznika [Breath]
396. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] Nakłada 4 [Sinking]
397. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 진동 폭발. 침잠 횟수 2 증가
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; Inflict +2 [Sinking] Count
   PL: [CriticalOnSucceedAttack] wywołuje [VibrationExplosion]; nakłada +2 Licznika [Sinking]
399. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 호흡 횟수 7 증가
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] Gain +7 [Breath] Count
   PL: [BeforeAttack] zyskuje +7 Licznika [Breath]
400. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 6 [Sinking]
   PL: [OnSucceedAttack] Nakłada 6 Zatonięcia
401. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spętania
402. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 진동 폭발. 침잠 횟수 3 증가
   źródło: Skills_Ego.json :: dataList[id=2110411].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; Inflict +3 [Sinking] Count
   PL: [CriticalOnSucceedAttack] wywołuje [VibrationExplosion]; nakłada +3 Licznika [Sinking]
403. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 여우비
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=1].name ; dataList[id=2110421].levelList[level=3].name ; dataList[id=2110421].levelList[level=4].name
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 떠돌이 여우
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=1].abName ; dataList[id=2110421].levelList[level=3].abName ; dataList[id=2110421].levelList[level=4].abName
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격\n[BeforeAttack] 호흡 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Breath]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise
   EN: [CantIdentify]\nTargets the unit with the least HP\n[BeforeAttack] Gain +5 [Breath] Count
   PL: [CantIdentify]\nAtakuje cel z najniższym HP\n[BeforeAttack] zyskuje +5 Licznika [Breath]
406. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — opis] [CantIdentify]\n체력이 가장 낮은 대상 공격\n[BeforeAttack] 호흡 횟수 7 증가
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=3].desc ; dataList[id=2110421].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Breath]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise
   EN: [CantIdentify]\nTargets the unit with the least HP\n[BeforeAttack] Gain +7 [Breath] Count
   PL: [CantIdentify]\nAtakuje cel z najniższym HP\n[BeforeAttack] zyskuje +7 Licznika [Breath]
409. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 4 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 진동 폭발. 침잠 횟수, 파열 횟수 2 증가
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Sinking], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Sinking] = 침잠 / Sinking; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; Inflict +2 [Sinking] Count and [Burst] Count
   PL: [CriticalOnSucceedAttack] wywołuje [VibrationExplosion]; nakłada +2 Licznika [Sinking] i Licznika [Burst]
413. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 6 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 6 [Burst]
   PL: [OnSucceedAttack] nakłada 6 [Burst]
415. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 진동 폭발. 침잠 횟수, 파열 횟수 3 증가
   źródło: Skills_Ego.json :: dataList[id=2110421].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Sinking], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Sinking] = 침잠 / Sinking; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; Inflict +3 [Sinking] Count and [Burst] Count
   PL: [CriticalOnSucceedAttack] wywołuje [VibrationExplosion]; nakłada +3 Licznika [Sinking] i Licznika [Burst]
417. [Pasywka E.G.O — nazwa] 사냥의 호흡
   źródło: Passive_Ego.json :: dataList[id=2110411].name
   limit: do 40 znaków
   EN: Breath of the Hunt
   PL: Oddech Polowania
418. [Pasywka E.G.O — opis] 합 종료 시 호흡 2를 얻음\n흐트러짐 상태가 되면 보호 2를 얻고, 흐트러짐 상태에서 돌아올 때 호흡 5를 얻음
   źródło: Passive_Ego.json :: dataList[id=2110411].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Protection]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Protection] = 보호 / Protection
   EN: After a clash, gain 2 [Breath]\nWhen staggered, gain 2 [Protection]; when recovering from stagger, gain 5 [Breath]
   PL: po zakończeniu starcia zyskuje 2 [Breath]\ngdy zostaje Oszołamiona, zyskuje 2 [Protection]; gdy wraca z Oszołomienia, zyskuje 5 [Breath]

## E.G.O [21105] Holiday (홀리데이) — Outis
- postać: Outis (오티스) · ID E.G.O: `21105`

419. [Karta E.G.O — nazwa] 홀리데이
   źródło: Egos.json :: dataList[id=21105].name
   limit: do 40 znaków
   EN: Holiday
   PL: Holiday
420. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21105].desc
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 홀리데이
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=1].name ; dataList[id=2110511].levelList[level=3].name ; dataList[id=2110511].levelList[level=4].name
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 산돌프
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=1].abName ; dataList[id=2110511].levelList[level=3].abName ; dataList[id=2110511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Sandolph
   PL: Sandolph
423. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110511].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL: [OnSucceedAttack] Wybuch Wstrząsu
424. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndSkill] 현재 정신력이 가장 낮은 아군 2명에게 가장 높은 공명 속성의 피해량 증가를 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Apply 1 'Damage Up' for the Affinity with the highest Resonance count to 2 allies with the least SP
   PL: [EndSkill] nakłada 1 zwiększenia zadawanych obrażeń odpowiadającego Afiniczności z najwyższym Rezonansem na 2 sojuszników z najniższym aktualnym SP
425. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [EndSkill] 현재 정신력이 가장 낮은 아군 2명의 정신력 20 회복
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 20 SP for 2 allies with the least SP
   PL: [EndSkill] odzyskuje 20 SP dla 2 sojuszników z najniższym aktualnym SP
426. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [EndSkill] 현재 정신력이 가장 낮은 아군 3명에게 가장 높은 공명 속성의 피해량 증가를 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Apply 1 'Damage Up' for the Affinity with the highest Resonance count to 3 allies with the least SP
   PL: [EndSkill] nakłada 1 zwiększenia zadawanych obrażeń odpowiadającego Afiniczności z najwyższym Rezonansem na 3 sojuszników z najniższym aktualnym SP
427. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [EndSkill] 현재 정신력이 가장 낮은 아군 3명의 정신력 20 회복
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 20 SP for 3 allies with the least SP
   PL: [EndSkill] odzyskuje 20 SP dla 3 sojuszników z najniższym aktualnym SP
428. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 현재 정신력이 가장 낮은 아군 4명에게 가장 높은 공명 속성의 피해량 증가를 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Apply 1 'Damage Up' for the Affinity with the highest Resonance count to 4 allies with the least SP
   PL: [EndSkill] nakłada 1 zwiększenia zadawanych obrażeń odpowiadającego Afiniczności z najwyższym Rezonansem na 4 sojuszników z najniższym aktualnym SP
429. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EndSkill] 현재 정신력이 가장 낮은 아군 4명의 정신력 20 회복
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110511].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 20 SP for 4 allies with the least SP
   PL: [EndSkill] odzyskuje 20 SP dla 4 sojuszników z najniższym aktualnym SP
430. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 홀리데이
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=1].name ; dataList[id=2110521].levelList[level=3].name ; dataList[id=2110521].levelList[level=4].name
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 산돌프
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=1].abName ; dataList[id=2110521].levelList[level=3].abName ; dataList[id=2110521].levelList[level=4].abName
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 체력이 최대 체력의 10%만큼 감소
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=1].desc ; dataList[id=2110521].levelList[level=3].desc ; dataList[id=2110521].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] This unit loses 10% HP
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] ta jednostka traci 10% HP
433. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신력 10 피해
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110521].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 10 SP
   PL: [OnSucceedAttack] cel traci 10 SP
434. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110521].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2110521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 가장 높은 공명 속성의 취약을 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Fragility to the Affinity with the highest Resonance count
   PL: [OnSucceedAttackTail] nakłada 1 Kruchości odpowiadającej Afiniczności z najwyższym Rezonansem
436. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 가장 높은 공명 속성의 취약을 2 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 2 Fragility for the Affinity with the highest Resonance count
   PL: [OnSucceedAttackTail] nakłada 2 Kruchości odpowiadającej Afiniczności z najwyższym Rezonansem
437. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [EndSkillTail] 가장 높은 공명 속성의 피해량 증가를 1 얻음
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2110521].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillTail]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]
   EN: [EndSkillTail] Gain 1 'Damage Up' to the Affinity with the highest Resonance count
   PL: [EndSkillTail] zyskuje 1 zwiększenia zadawanych obrażeń odpowiadającego Afiniczności z najwyższym Rezonansem
438. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 가장 높은 공명 속성의 취약을 2 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110521].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragility for the Affinity with the highest Resonance count
   PL: [OnSucceedAttack] nakłada 2 Kruchości odpowiadającej Afiniczności z najwyższym Rezonansem
439. [Pasywka E.G.O — nazwa] 평등한 선물
   źródło: Passive_Ego.json :: dataList[id=2110511].name
   limit: do 40 znaków
   EN: Fair Presents
   PL: Równe Prezenty
440. [Pasywka E.G.O — opis] 자신을 제외한 아군에게 스킬, 코인 효과로 긍정적인 버프를 부여할 때 무작위 적 1명에게 화상, 출혈, 진동, 파열, 침잠 중 무작위 효과 1개의 위력 1 부여 (턴 당 최대 5회 발동. 적 1명 당 최대 5회 부여 가능, 환상체의 경우 무작위 부위에 부여됨.)
   źródło: Passive_Ego.json :: dataList[id=2110511].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: When applying positive effects to other allies with Skill effects or Coin effects, randomly select one of the following effects: [Combustion], [Laceration], [Vibration], [Burst], or [Sinking].\nThen, inflict 1 Potency of the selected effect to 1 random enemy. (Activates 5 times per Turn. Can be applied up to 5 times per enemy. For abnormalities, applied to a random Part.)
   PL: gdy nakłada pozytywne efekty na innych sojuszników efektami Umiejętności lub Monet, nakłada 1 Siły 1 losowo wybranego z następujących efektów: [Combustion], [Laceration], [Vibration], [Burst] lub [Sinking] na 1 losowego wroga (uruchamia się maks. 5 razy na turę. maks. 5 nakładań na 1 wroga, w przypadku aberracji na losową Część.)

## E.G.O [21106] Binds (구속) — Outis
- postać: Outis (오티스) · ID E.G.O: `21106`

441. [Karta E.G.O — nazwa] 구속
   źródło: Egos.json :: dataList[id=21106].name
   limit: do 40 znaków
   EN: Binds
   PL: Niewola
442. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21106].desc
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 구속
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=1].name ; dataList[id=2110611].levelList[level=3].name ; dataList[id=2110611].levelList[level=4].name
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 묶인 왕
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=1].abName ; dataList[id=2110611].levelList[level=3].abName ; dataList[id=2110611].levelList[level=4].abName
   limit: do 40 znaków
   EN: The King in Binds
   PL: Król w Okowach
445. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] (오만 또는 나태 공명 중 가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Pride or Sloth Reson. - 2) Atk Weight (max 2)\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans Pychy lub Lenistwa - 2) Wagi Ataku (maks. 2)\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
446. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] Nakłada 4 [Vibration]
447. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationCrack]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110611].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2110611].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationCrack], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationCrack] = 진동 - 균열 / Tremor - Fracture; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationCrack]
   PL: [OnSucceedAttack] wywołuje [Switch_Vibration] w [VibrationCrack]
448. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2110611].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2110611].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion]
449. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (오만 또는 나태 공명 중 가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)\n[VibrationExplosion] 시 흐트러짐 손상 50% 증가\n[EndSkill] 3턴 동안 턴 종료 시 정신력 9 감소
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [VibrationExplosion], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Pride or Sloth Reson. - 2) Atk Weight (max 2)\nAmount of Stagger Threshold raised by [VibrationExplosion] increases by 50%\n[EndSkill] For 3 turns, lose 9 SP at Turn End
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans Pychy lub Lenistwa - 2) Wagi Ataku (maks. 2)\nilość progu Oszołomienia podnoszona przez [VibrationExplosion] rośnie o 50%\n[EndSkill] przez 3 tury traci 9 SP na koniec tury
450. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] Nakłada 5 [Vibration]
451. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (오만 또는 나태 공명 중 가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)\n[VibrationExplosion] 시 흐트러짐 손상 100% 증가\n[EndSkill] 3턴 동안 턴 종료 시 정신력 8 감소
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [VibrationExplosion], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Pride or Sloth Reson. - 2) Atk Weight (max 2)\nAmount of Stagger Threshold raised by [VibrationExplosion] increases by 100%\n[EndSkill] For 3 turns, lose 8 SP at Turn End
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans Pychy lub Lenistwa - 2) Wagi Ataku (maks. 2)\nilość progu Oszołomienia podnoszona przez [VibrationExplosion] rośnie o 100%\n[EndSkill] przez 3 tury traci 8 SP na koniec tury
452. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL: [OnSucceedAttack] nakłada 6 [Vibration]
453. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 구속
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].name ; dataList[id=2110621].levelList[level=3].name ; dataList[id=2110621].levelList[level=4].name
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 묶인 왕
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].abName ; dataList[id=2110621].levelList[level=3].abName ; dataList[id=2110621].levelList[level=4].abName
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (오만 또는 나태 공명 중 가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (highest Pride or Sloth Reson. - 2) Atk Weight (max 2)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans Pychy lub Lenistwa - 2) Wagi Ataku (maks. 2)
456. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110621].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
458. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationCrack]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2110621].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2110621].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (오만 또는 나태 공명 중 가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)\n[VibrationExplosion] 시 흐트러짐 손상 50% 증가
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=3].desc ; dataList[id=2110621].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [VibrationExplosion]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (highest Pride or Sloth Reson. - 2) Atk Weight (max 2)\nAmount of Stagger Threshold raised by [VibrationExplosion] increases by 50%
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans Pychy lub Lenistwa - 2) Wagi Ataku (maks. 2)\nilość progu Oszołomienia podnoszona przez [VibrationExplosion] rośnie o 50%
461. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttackTail] [VibrationExplosion]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2110621].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackTail] Trigger [VibrationExplosion]
   PL: [OnSucceedAttackTail] wywołuje [VibrationExplosion]
463. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion]<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]<style="highlight"></style>
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion]<style="highlight"></style>
464. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Vibration]
466. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttackTail] [VibrationExplosion]<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackTail] Trigger [VibrationExplosion]<style="highlight"></style>
   PL: [OnSucceedAttackTail] wywołuje [VibrationExplosion]<style="highlight"></style>
467. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [VibrationExplosion]<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110621].levelList[level=4].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Pasywka E.G.O — nazwa] 성대한 환대
   źródło: Passive_Ego.json :: dataList[id=2110611].name
   limit: do 40 znaków
   EN: Grand Welcome
   PL: Wspaniałe Powitanie
469. [Pasywka E.G.O — opis] 자신의 공격 종료 시 대상이 흐트러짐 상태가 되었거나 사망하였으면, 오만 속성 E.G.O 자원 +1, 나머지 속성의 E.G.O 자원 중 무작위 1종 +1 (턴 당 최대 3회 발동)
   źródło: Passive_Ego.json :: dataList[id=2110611].desc
   limit: do 220 znaków
   EN: Attack End: If the target this unit attacked is Staggered or defeated, gain +1 Pride E.G.O resource and +1 E.G.O resource for 1 other random Affinity (3 times per turn)
   PL: na koniec ataku tej jednostki, jeżeli cel stał się Oszołomiony lub został pokonany, zyskuje +1 zasobu E.G.O Pychy i +1 zasobu E.G.O 1 losowej innej Afiniczności (uruchamia się maks. 3 razy na turę)

## E.G.O [21107] Dimension Shredder (차원찢개) — Outis
- postać: Outis (오티스) · ID E.G.O: `21107`

470. [Karta E.G.O — nazwa] 차원찢개
   źródło: Egos.json :: dataList[id=21107].name
   limit: do 40 znaków
   EN: Dimension Shredder
   PL: Rozdzieracz Wymiarów
471. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21107].desc
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 차원찢개
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=1].name ; dataList[id=2110711].levelList[level=3].name ; dataList[id=2110711].levelList[level=4].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 길 잃은 승객
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=1].abName ; dataList[id=2110711].levelList[level=3].abName ; dataList[id=2110711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Wayward Passenger
   PL: Zbłąkany Pasażer
474. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 최대 공명이 4 이상이면, 공격 가중치 1 증가\n[BeforeAttack] 보유한 [Charge] 횟수가 10 미만일 때, 최대 체력의 15%만큼 체력을 소모하여 [Charge] 횟수를 10 얻음 (이 피해로 체력이 0이 되지않음, 소수점 버림)\n[BeforeAttack] [Charge] 횟수를 최대 40 소모하여 소모한 [Charge] 횟수당 피해량 +1% (최대 10%)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n[BeforeAttack] At less than 10 [Charge] Count, consume 15% HP to gain +10 [Charge] Count (this damage does not reduce this unit's HP to 0; rounded down)\n[BeforeAttack] Consume up to 40 [Charge] Count and deal +1% damage for every [Charge] Count consumed (max 10%)
   PL: [BeforeAttack] przy najwyższym Rezonansie 4+ zyskuje +1 Wagi Ataku\n[BeforeAttack] przy mniej niż 10 Licznika [Charge], zużywa 15% HP, by zyskać 10 Licznika [Charge] (te obrażenia nie obniżają HP tej jednostki do 0, zaokrąglone w dół)\n[BeforeAttack] zużywa maks. 40 Licznika [Charge] i zadaje +1% obrażeń za każdy zużyty Licznik [Charge] (maks. 10%)
475. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] - 1)만큼 [DimensionRift] 부여 (최대 1)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [DimensionRift] (max 1)
   PL: [OnSucceedAttack] nakłada ([Charge] - 1) [DimensionRift] (maks. 1)
476. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Charge]만큼 다음 턴에 [Agility] 1, [ChargeLoad] 1 얻음 (한 스킬당 최대 1)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Agility], [ChargeLoad]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste; [ChargeLoad] = 부하 / Load
   EN: [OnSucceedAttack] Gain 1 [Agility] and 1 [ChargeLoad] next turn for every [Charge] (max 1 of each per Skill)
   PL: [OnSucceedAttack] za każdy [Charge] następnej tury zyskuje 1 [Agility] i 1 [ChargeLoad] (maks. 1 każdego na Umiejętność)
477. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [EnemyKill] [Charge] 횟수 2 증가
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Charge]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Charge] = 충전 / Charge
   EN: [EnemyKill] Gain +2 [Charge] Count
   PL: [EnemyKill] zyskuje +2 Licznika [Charge]
478. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 최대 공명이 <style="highlight">3</style> 이상이면, 공격 가중치 1 증가\n[BeforeAttack] 보유한 [Charge] 횟수가 10 미만일 때, 최대 체력의 15%만큼 체력을 소모하여 [Charge] 횟수를 10 얻음 (이 피해로 체력이 0이 되지않음, 소수점 버림)\n[BeforeAttack] [Charge] 횟수를 최대 40 소모하여 소모한 [Charge] 횟수당 피해량 +1% (최대 <style="highlight">20</style>%)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=3].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] At <style="highlight">3</style>+ highest Reson., gain +1 Atk Weight\n[BeforeAttack] At less than 10 [Charge] Count, consume 15% HP to gain +10 [Charge] Count (this damage does not reduce this unit's HP to 0; rounded down)\n[BeforeAttack] Consume up to 40 [Charge] Count and deal +1% damage for every [Charge] Count consumed (max <style="highlight">20</style>%)
   PL: [BeforeAttack] przy najwyższym Rezonansie <style="highlight">3</style>+ zyskuje +1 Wagi Ataku\n[BeforeAttack] przy mniej niż 10 Licznika [Charge], zużywa 15% HP, by zyskać 10 Licznika [Charge] (te obrażenia nie obniżają HP tej jednostki do 0, zaokrąglone w dół)\n[BeforeAttack] zużywa maks. 40 Licznika [Charge] i zadaje +1% obrażeń za każdy zużyty Licznik [Charge] (maks. <style="highlight">20</style>%)
479. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] - 1)만큼 [DimensionRift] 부여 (최대 <style="highlight">2</style>)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [DimensionRift] (max <style="highlight">2</style>)
   PL: [OnSucceedAttack] nakłada ([Charge] - 1) [DimensionRift] (maks. <style="highlight">2</style>)
480. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Charge]만큼 다음 턴에 [Agility] 1, [ChargeLoad] 1 얻음 (한 스킬당 최대 <style="highlight">2</style>)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [Agility], [ChargeLoad]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste; [ChargeLoad] = 부하 / Load
   EN: [OnSucceedAttack] Gain 1 [Agility] and 1 [ChargeLoad] next turn for every [Charge] (max <style="highlight">2</style> of each per Skill)
   PL: [OnSucceedAttack] za każdy [Charge] następnej tury zyskuje 1 [Agility] i 1 [ChargeLoad] (maks. <style="highlight">2</style> każdego na Umiejętność)
481. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [EnemyKill] [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2110711].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Charge]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Charge] = 충전 / Charge
   EN: [EnemyKill] Gain +2 [Charge] Count<style="highlight"></style>
   PL: [EnemyKill] zyskuje +2 Licznika [Charge]<style="highlight"></style>
482. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] <style="highlight">(최대 공명 수 - 2)만큼</style> 공격 가중치 증가 <style="highlight">(최대 2)</style>\n[BeforeAttack] 보유한 [Charge] 횟수가 10 미만일 때, 최대 체력의 <style="highlight">10</style>%만큼 체력을 소모하여 [Charge] 횟수를 10 얻음 (이 피해로 체력이 0이 되지않음, 소수점 버림)\n[BeforeAttack] [Charge] 횟수를 최대 40 소모하여 소모한 [Charge] 횟수당 피해량 +1% (최대 <style="highlight">30</style>%)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] Gain <style="highlight">(highest Reson. - 2)</style> Atk Weight <style="highlight">(max 2)</style>\n[BeforeAttack] At less than 10 [Charge] Count, consume <style="highlight">10</style>% HP to gain +10 [Charge] Count (this damage does not reduce this unit's HP to 0; rounded down)\n[BeforeAttack] Consume up to 40 [Charge] Count and deal +1% damage for every [Charge] Count consumed (max <style="highlight">30</style>%)
   PL: [BeforeAttack] zyskuje <style="highlight">(najwyższy Rezonans - 2)</style> Wagi Ataku <style="highlight">(maks. 2)</style>\n[BeforeAttack] przy mniej niż 10 Licznika [Charge], zużywa <style="highlight">10</style>% HP, by zyskać 10 Licznika [Charge] (te obrażenia nie obniżają HP tej jednostki do 0, zaokrąglone w dół)\n[BeforeAttack] zużywa maks. 40 Licznika [Charge] i zadaje +1% obrażeń za każdy zużyty Licznik [Charge] (maks. <style="highlight">30</style>%)
483. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] - 1)만큼 [DimensionRift] 부여 (최대 2)<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [DimensionRift] (max 2)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada ([Charge] - 1) [DimensionRift] (maks. 2)<style="highlight"></style>
484. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Charge]만큼 다음 턴에 [Agility] 1, [ChargeLoad] 1 얻음 (한 스킬당 최대 <style="highlight">3</style>)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110711].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [Agility], [ChargeLoad]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste; [ChargeLoad] = 부하 / Load
   EN: [OnSucceedAttack] Gain 1 [Agility] and 1 [ChargeLoad] next turn for every [Charge] (max <style="highlight">3</style> of each per Skill)
   PL: [OnSucceedAttack] za każdy [Charge] następnej tury zyskuje 1 [Agility] i 1 [ChargeLoad] (maks. <style="highlight">3</style> każdego na Umiejętność)
485. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 차원찢개
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=1].name ; dataList[id=2110721].levelList[level=3].name ; dataList[id=2110721].levelList[level=4].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 길 잃은 승객
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=1].abName ; dataList[id=2110721].levelList[level=3].abName ; dataList[id=2110721].levelList[level=4].abName
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 최대 공명이 4 이상이면, 공격 가중치 1 증가\n[BeforeAttack] 보유한 [Charge] 횟수가 최대치 미만일 때, 최대 체력의 (부족한 [Charge] 횟수 X 1.5)%만큼 체력을 소모하여 [Charge] 횟수를 최대치까지 얻음 (최대 [Charge] 횟수 획득량 : 30.  이 피해로 체력이 0이 되지않음, 소수점 버림)\n[BeforeAttack] [Charge] 횟수를 최대 40 소모하여 소모한 [Charge] 횟수당 피해량 +2% (최대 20%)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n[BeforeAttack] At less than maximum [Charge] Count, consume (missing [Charge] Count x 1.5)% HP to gain up to max [Charge] Count (max [Charge] Count obtainable from this effect: 30. This damage does not reduce this unit's HP to 0; rounded down)\n[BeforeAttack] Consume up to 40 [Charge] Count and deal +2% damage for every [Charge] Count consumed (max 20%)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 4+ zyskuje +1 Wagi Ataku\n[BeforeAttack] przy mniej niż maksymalny Licznik [Charge], zużywa (brakujący Licznik [Charge] x 1.5)% HP, by zyskać Licznik [Charge] do maksimum (maks. ilość zyskiwanego Licznika [Charge] z tego efektu: 30. te obrażenia nie obniżają HP tej jednostki do 0, zaokrąglone w dół)\n[BeforeAttack] zużywa maks. 40 Licznika [Charge] i zadaje +2% obrażeń za każdy zużyty Licznik [Charge] (maks. 20%)
488. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] - 1)만큼 [DimensionRift] 부여 (최대 2)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [DimensionRift] (max 2)
   PL: [OnSucceedAttack] nakłada ([Charge] - 1) [DimensionRift] (maks. 2)
489. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Charge]만큼 다음 턴에 [Agility] 1, [ChargeLoad] 1 얻음 (한 스킬당 최대 2)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110721].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Agility], [ChargeLoad]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste; [ChargeLoad] = 부하 / Load
   EN: [OnSucceedAttack] Gain 1 [Agility] and 1 [ChargeLoad] next turn for every [Charge] (max 2 of each per Skill)
   PL: [OnSucceedAttack] za każdy [Charge] następnej tury zyskuje 1 [Agility] i 1 [ChargeLoad] (maks. 2 każdego na Umiejętność)
490. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [EnemyKill] [Charge] 횟수 2 증가
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 최대 공명이 4 이상이면, 공격 가중치 1 증가\n[BeforeAttack] 보유한 [Charge] 횟수가 최대치 미만일 때, 최대 체력의 (부족한 [Charge] 횟수 X <style="highlight">1.2</style>)%만큼 체력을 소모하여 [Charge] 횟수를 최대치까지 얻음 (최대 [Charge] 횟수 획득량 : 30.  이 피해로 체력이 0이 되지않음, 소수점 버림)\n[BeforeAttack] [Charge] 횟수를 최대 40 소모하여 소모한 [Charge] 횟수당 피해량 +2% (최대 <style="highlight">40</style>%)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=3].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n[BeforeAttack] At less than maximum [Charge] Count, consume (missing [Charge] Count x <style="highlight">1.2</style>)% HP to gain up to max [Charge] Count (max [Charge] Count obtainable from this effect: 30. This damage does not reduce this unit's HP to 0; rounded down)\n[BeforeAttack] Consume up to 40 [Charge] Count and deal +2% damage for every [Charge] Count consumed (max <style="highlight">40</style>%)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 4+ zyskuje +1 Wagi Ataku\n[BeforeAttack] przy mniej niż maksymalny Licznik [Charge], zużywa (brakujący Licznik [Charge] x <style="highlight">1.2</style>)% HP, by zyskać Licznik [Charge] do maksimum (maks. ilość zyskiwanego Licznika [Charge] z tego efektu: 30. te obrażenia nie obniżają HP tej jednostki do 0, zaokrąglone w dół)\n[BeforeAttack] zużywa maks. 40 Licznika [Charge] i zadaje +2% obrażeń za każdy zużyty Licznik [Charge] (maks. <style="highlight">40</style>%)
492. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] - 1)만큼 [DimensionRift] 부여 (최대 2)<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [EnemyKill] [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2110721].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] <style="highlight">(최대 공명 수 - 2)만큼</style> 공격 가중치 증가 <style="highlight">(최대 2)</style>\n[BeforeAttack] 보유한 [Charge] 횟수가 최대치 미만일 때, 최대 체력의 <style="highlight">(부족한 [Charge] 횟수)%</style>만큼 체력을 소모하여 [Charge] 횟수를 최대치까지 얻음 (최대 [Charge] 횟수 획득량 : 30.  이 피해로 체력이 0이 되지않음, 소수점 버림)\n[BeforeAttack] [Charge] 횟수를 최대 40 소모하여 소모한 [Charge] 횟수당 피해량 +2% (최대 <style="highlight">60</style>%)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain <style="highlight">(highest Reson. - 2)</style> Atk Weight <style="highlight">(max 2)</style>\n[BeforeAttack] At less than maximum [Charge] Count, consume <style="highlight">(missing [Charge] Count)%</style> HP to gain up to max [Charge] Count (max [Charge] Count obtainable from this effect: 30. This damage does not reduce this unit's HP to 0; rounded down)\n[BeforeAttack] Consume up to 40 [Charge] Count and deal +2% damage for every [Charge] Count consumed (max <style="highlight">60</style>%)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje <style="highlight">(najwyższy Rezonans - 2)</style> Wagi Ataku <style="highlight">(maks. 2)</style>\n[BeforeAttack] przy mniej niż maksymalny Licznik [Charge], zużywa <style="highlight">(brakujący Licznik [Charge])%</style> HP, by zyskać Licznik [Charge] do maksimum (maks. ilość zyskiwanego Licznika [Charge] z tego efektu: 30. te obrażenia nie obniżają HP tej jednostki do 0, zaokrąglone w dół)\n[BeforeAttack] zużywa maks. 40 Licznika [Charge] i zadaje +2% obrażeń za każdy zużyty Licznik [Charge] (maks. <style="highlight">60</style>%)
495. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] - 1)만큼 [DimensionRift] 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict ([Charge] - 1) [DimensionRift] (max <style="highlight">4</style>)
   PL: [OnSucceedAttack] nakłada ([Charge] - 1) [DimensionRift] (maks. <style="highlight">4</style>)
496. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Charge]만큼 다음 턴에 [Agility] 1, [ChargeLoad] 1 얻음 (한 스킬당 최대 <style="highlight">3</style>)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110721].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Pasywka E.G.O — nazwa] 헤메이는 자
   źródło: Passive_Ego.json :: dataList[id=2110711].name
   limit: do 40 znaków
   EN: Rambling Man
   PL: Błądzący Człowiek
498. [Pasywka E.G.O — opis] [Charge] 횟수 최대치 +5\n([Charge] - 1)당 [Charge] 횟수를 소모하는 스킬의 피해량 +2% (최대 10%)
   źródło: Passive_Ego.json :: dataList[id=2110711].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Max [Charge] Count +5\nSkills that consume [Charge] Count deal +2% damage for every ([Charge] - 1) (max 10%)
   PL: maks. Licznik [Charge] +5\nUmiejętności zużywające Licznik [Charge] zadają +2% obrażeń za każde ([Charge] - 1) (maks. 10%)
499. [Pasywka E.G.O — podsumowanie] [Charge] 횟수를 소모하는 스킬의 피해량이 증가
   źródło: Passive_Ego.json :: dataList[id=2110711].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Skills that consume [Charge] Count deal more damage
   PL: Umiejętności zużywające Licznik [Charge] zadają więcej obrażeń

## E.G.O [21108] Magic Bullet (마탄) — Outis
- postać: Outis (오티스) · ID E.G.O: `21108`

500. [Karta E.G.O — nazwa] 마탄
   źródło: Egos.json :: dataList[id=21108].name
   limit: do 40 znaków
   EN: Magic Bullet
   PL: Magiczna Amunicja
501. [Karta E.G.O — opis] 오티스의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21108].desc
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 마탄
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=1].name ; dataList[id=2110811].levelList[level=3].name ; dataList[id=2110811].levelList[level=4].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 마탄의 사수
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=1].abName ; dataList[id=2110811].levelList[level=3].abName ; dataList[id=2110811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Der Freischütz
   PL: Der Freischütz
504. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 [Combustion] 수치 3당 피해량 +1% (최대 10%)\n[BeforeAttack] [FreischutzShotCount]이 0이면, [FreischutzShotCount] 1 얻음.\n- [FreischutzShotCount] 수치에 따라 발사할 탄환이 정해짐\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] 최대 공명 수만큼 [FreischutzShotCount]을 얻음 (최소 1, 최대 4)\n[EndSkill] 메인 타겟이 사망했으면, [Combustion]이 있는 모든 적에게 [DarkFlame] 2 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=1].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [BeforeAttack], [FreischutzShotCount], [FreishutzOutisEgoBullet_1st], [FreishutzOutisEgoBullet_2nd], [FreishutzOutisEgoBullet_3rd], [FreishutzOutisEgoBullet_4th], [FreishutzOutisEgoBullet_5th], [FreishutzOutisEgoBullet_6th], [FreishutzOutisEgoBullet_7th], [EndSkill], [DarkFlame]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [FreishutzOutisEgoBullet_1st] = 첫번째 마탄 / The First Magic Bullet; [FreishutzOutisEgoBullet_2nd] = 두번째 마탄 / The Second Magic Bullet; [FreishutzOutisEgoBullet_3rd] = 세번째 마탄 / The Third Magic Bullet; [FreishutzOutisEgoBullet_4th] = 네번째 마탄 / The Fourth Magic Bullet; [FreishutzOutisEgoBullet_5th] = 다섯번째 마탄 / The Fifth Magic Bullet …
   EN: Deal +1% damage for every 3 [Combustion] on target (max 10%)\n[BeforeAttack] At 0 [FreischutzShotCount], gain 1 [FreischutzShotCount].\n- [FreischutzShotCount] value determines the bullet to fire.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] Gain [FreischutzShotCount] equal to the highest Reson. (min. 1, max 4)\n[EndSkill] If the main target is defeated, inflict 2 [DarkFlame] against all enemies that have [Combustion]
   PL: zadaje +1% obrażeń za każde 3 Licznika [Combustion] na celu (maks. 10%)\n[BeforeAttack] przy 0 [FreischutzShotCount], zyskuje 1 [FreischutzShotCount].\n- wartość [FreischutzShotCount] określa wystrzeliwany pocisk.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] zyskuje tyle [FreischutzShotCount], ile wynosi najwyższy Rezonans (min. 1, maks. 4)\n[EndSkill] jeżeli cel główny został pokonany, nakłada 2 [DarkFlame] na wszystkich wrogów z [Combustion]
505. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [FreischutzShotCount]만큼 [Combustion] 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FreischutzShotCount], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] equal to [FreischutzShotCount]
   PL: [OnSucceedAttack] nakłada tyle [Combustion], ile wynosi [FreischutzShotCount]
506. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [FreischutzShotCount]만큼 [DarkFlame] 부여 (턴 당 대상 1명마다 최대 1회 부여)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110811].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2110811].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FreischutzShotCount], [DarkFlame]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [DarkFlame] = 흑염 / Dark Flame
   EN: [OnSucceedAttack] Inflict [DarkFlame] equal to [FreischutzShotCount] (once per turn for each unit)
   PL: [OnSucceedAttack] nakłada tyle [DarkFlame], ile wynosi [FreischutzShotCount] (maks. 1 raz na turę na każdy cel)
507. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 대상의 [Combustion] 수치 3당 피해량 +<style="highlight">2</style>% (최대 <style="highlight">20</style>%)\n[BeforeAttack] [FreischutzShotCount]이 0이면, [FreischutzShotCount] 1 얻음.\n- [FreischutzShotCount] 수치에 따라 발사할 탄환이 정해짐\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] 최대 공명 수만큼 [FreischutzShotCount]을 얻음 (최소 1, 최대 4)\n[EndSkill] 메인 타겟이 사망했으면, [Combustion]이 있는 모든 적에게 [DarkFlame] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=3].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [BeforeAttack], [FreischutzShotCount], [FreishutzOutisEgoBullet_1st], [FreishutzOutisEgoBullet_2nd], [FreishutzOutisEgoBullet_3rd], [FreishutzOutisEgoBullet_4th], [FreishutzOutisEgoBullet_5th], [FreishutzOutisEgoBullet_6th], [FreishutzOutisEgoBullet_7th], [EndSkill], [DarkFlame]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [FreishutzOutisEgoBullet_1st] = 첫번째 마탄 / The First Magic Bullet; [FreishutzOutisEgoBullet_2nd] = 두번째 마탄 / The Second Magic Bullet; [FreishutzOutisEgoBullet_3rd] = 세번째 마탄 / The Third Magic Bullet; [FreishutzOutisEgoBullet_4th] = 네번째 마탄 / The Fourth Magic Bullet; [FreishutzOutisEgoBullet_5th] = 다섯번째 마탄 / The Fifth Magic Bullet …
   EN: Deal +<style="highlight">2</style>% damage for every 3 [Combustion] on target (max <style="highlight">20</style>%)\n[BeforeAttack] At 0 [FreischutzShotCount], gain 1 [FreischutzShotCount].\n- [FreischutzShotCount] value determines the bullet to fire.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] Gain [FreischutzShotCount] equal to the highest Reson. (min. 1, max 4)\n[EndSkill] If the main target is defeated, inflict <style="highlight">3</style> [DarkFlame] against all enemies that have [Combustion]
   PL: zadaje +<style="highlight">2</style>% obrażeń za każde 3 Licznika [Combustion] na celu (maks. <style="highlight">20</style>%)\n[BeforeAttack] przy 0 [FreischutzShotCount], zyskuje 1 [FreischutzShotCount].\n- wartość [FreischutzShotCount] określa wystrzeliwany pocisk.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] zyskuje tyle [FreischutzShotCount], ile wynosi najwyższy Rezonans (min. 1, maks. 4)\n[EndSkill] jeżeli cel główny został pokonany, nakłada <style="highlight">3</style> [DarkFlame] na wszystkich wrogów z [Combustion]
508. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 [Combustion] 수치 3당 피해량 +<style="highlight">3</style>% (최대 <style="highlight">30</style>%)\n[BeforeAttack] [FreischutzShotCount]이 0이면, [FreischutzShotCount] 1 얻음.\n- [FreischutzShotCount] 수치에 따라 발사할 탄환이 정해짐\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] 최대 공명 수만큼 [FreischutzShotCount]을 얻음 (최소 1, 최대 4)\n[EndSkill] 메인 타겟이 사망했으면, [Combustion]이 있는 모든 적에게 [DarkFlame] <style="highlight">4</style> 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110811].levelList[level=4].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [BeforeAttack], [FreischutzShotCount], [FreishutzOutisEgoBullet_1st], [FreishutzOutisEgoBullet_2nd], [FreishutzOutisEgoBullet_3rd], [FreishutzOutisEgoBullet_4th], [FreishutzOutisEgoBullet_5th], [FreishutzOutisEgoBullet_6th], [FreishutzOutisEgoBullet_7th], [EndSkill], [DarkFlame]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [FreishutzOutisEgoBullet_1st] = 첫번째 마탄 / The First Magic Bullet; [FreishutzOutisEgoBullet_2nd] = 두번째 마탄 / The Second Magic Bullet; [FreishutzOutisEgoBullet_3rd] = 세번째 마탄 / The Third Magic Bullet; [FreishutzOutisEgoBullet_4th] = 네번째 마탄 / The Fourth Magic Bullet; [FreishutzOutisEgoBullet_5th] = 다섯번째 마탄 / The Fifth Magic Bullet …
   EN: Deal +<style="highlight">3</style>% damage for every 3 [Combustion] on target (max <style="highlight">30</style>%)\n[BeforeAttack] At 0 [FreischutzShotCount], gain 1 [FreischutzShotCount].\n- [FreischutzShotCount] value determines the bullet to fire.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] Gain [FreischutzShotCount] equal to the highest Reson. (min. 1, max 4)\n[EndSkill] If the main target is defeated, inflict <style="highlight">4</style> [DarkFlame] against all enemies that have [Combustion]
   PL: zadaje +<style="highlight">3</style>% obrażeń za każde 3 Licznika [Combustion] na celu (maks. <style="highlight">30</style>%)\n[BeforeAttack] przy 0 [FreischutzShotCount], zyskuje 1 [FreischutzShotCount].\n- wartość [FreischutzShotCount] określa wystrzeliwany pocisk.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] zyskuje tyle [FreischutzShotCount], ile wynosi najwyższy Rezonans (min. 1, maks. 4)\n[EndSkill] jeżeli cel główny został pokonany, nakłada <style="highlight">4</style> [DarkFlame] na wszystkich wrogów z [Combustion]
509. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 마탄
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=1].name ; dataList[id=2110821].levelList[level=3].name ; dataList[id=2110821].levelList[level=4].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 마탄의 사수
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=1].abName ; dataList[id=2110821].levelList[level=3].abName ; dataList[id=2110821].levelList[level=4].abName
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 [Combustion] 수치 3당 피해량 +1% (최대 10%)\n[BeforeAttack] [FreischutzShotCount]이 0이면, [FreischutzShotCount] 1 얻음.\n- [FreischutzShotCount] 수치에 따라 발사할 탄환이 정해짐\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] 최대 공명 수만큼 [FreischutzShotCount]을 얻음 (최소 1, 최대 4)\n[EndSkill] 메인 타겟이 사망했으면, [Combustion]이 있는 모든 대상에게 [DarkFlame] 3 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=1].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Combustion], [BeforeAttack], [FreischutzShotCount], [FreishutzOutisEgoBullet_1st], [FreishutzOutisEgoBullet_2nd], [FreishutzOutisEgoBullet_3rd], [FreishutzOutisEgoBullet_4th], [FreishutzOutisEgoBullet_5th], [FreishutzOutisEgoBullet_6th], [FreishutzOutisEgoBullet_7th], [EndSkill], [DarkFlame]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [FreishutzOutisEgoBullet_1st] = 첫번째 마탄 / The First Magic Bullet; [FreishutzOutisEgoBullet_2nd] = 두번째 마탄 / The Second Magic Bullet; [FreishutzOutisEgoBullet_3rd] = 세번째 마탄 / The Third Magic Bullet; [FreishutzOutisEgoBullet_4th] = 네번째 마탄 / The Fourth Magic Bullet …
   EN: [CantIdentify]\nTargets randomly\nDeal +1% damage for every 3 [Combustion] on target (max 10%)\n[BeforeAttack] At 0 [FreischutzShotCount], gain 1 [FreischutzShotCount].\n- [FreischutzShotCount] value determines the bullet to fire.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] Gain [FreischutzShotCount] equal to the highest Reson. (min. 1, max 4)\n[EndSkill] If the main target is defeated, inflict 3 [DarkFlame] against all enemies that have [Combustion]
   PL: [CantIdentify]\nAtakuje losowy cel\nzadaje +1% obrażeń za każde 3 Licznika [Combustion] na celu (maks. 10%)\n[BeforeAttack] przy 0 [FreischutzShotCount], zyskuje 1 [FreischutzShotCount].\n- wartość [FreischutzShotCount] określa wystrzeliwany pocisk.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] zyskuje tyle [FreischutzShotCount], ile wynosi najwyższy Rezonans (min. 1, maks. 4)\n[EndSkill] jeżeli cel główny został pokonany, nakłada 3 [DarkFlame] na wszystkich wrogów z [Combustion]
512. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [FreischutzShotCount]만큼 [Combustion] 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110821].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [FreischutzShotCount]만큼 [DarkFlame] 부여 (턴 당 대상 1명마다 최대 1회 부여)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 [Combustion] 수치 3당 피해량 +<style="highlight">2</style>% (최대 <style="highlight">20</style>%)\n[BeforeAttack] [FreischutzShotCount]이 0이면, [FreischutzShotCount] 1 얻음.\n- [FreischutzShotCount] 수치에 따라 발사할 탄환이 정해짐\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] 최대 공명 수만큼 [FreischutzShotCount]을 얻음 (최소 1, 최대 4)\n[EndSkill] 메인 타겟이 사망했으면, [Combustion]이 있는 모든 대상에게 [DarkFlame] <style="highlight">5</style> 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=3].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Combustion], [BeforeAttack], [FreischutzShotCount], [FreishutzOutisEgoBullet_1st], [FreishutzOutisEgoBullet_2nd], [FreishutzOutisEgoBullet_3rd], [FreishutzOutisEgoBullet_4th], [FreishutzOutisEgoBullet_5th], [FreishutzOutisEgoBullet_6th], [FreishutzOutisEgoBullet_7th], [EndSkill], [DarkFlame]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [FreishutzOutisEgoBullet_1st] = 첫번째 마탄 / The First Magic Bullet; [FreishutzOutisEgoBullet_2nd] = 두번째 마탄 / The Second Magic Bullet; [FreishutzOutisEgoBullet_3rd] = 세번째 마탄 / The Third Magic Bullet; [FreishutzOutisEgoBullet_4th] = 네번째 마탄 / The Fourth Magic Bullet …
   EN: [CantIdentify]\nTargets randomly\nDeal +<style="highlight">2</style>% damage for every 3 [Combustion] on target (max <style="highlight">20</style>%)\n[BeforeAttack] At 0 [FreischutzShotCount], gain 1 [FreischutzShotCount].\n- [FreischutzShotCount] value determines the bullet to fire.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] Gain [FreischutzShotCount] equal to the highest Reson. (min. 1, max 4)\n[EndSkill] If the main target is defeated, inflict <style="highlight">5</style> [DarkFlame] against all enemies that have [Combustion]
   PL: [CantIdentify]\nAtakuje losowy cel\nzadaje +<style="highlight">2</style>% obrażeń za każde 3 Licznika [Combustion] na celu (maks. <style="highlight">20</style>%)\n[BeforeAttack] przy 0 [FreischutzShotCount], zyskuje 1 [FreischutzShotCount].\n- wartość [FreischutzShotCount] określa wystrzeliwany pocisk.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] zyskuje tyle [FreischutzShotCount], ile wynosi najwyższy Rezonans (min. 1, maks. 4)\n[EndSkill] jeżeli cel główny został pokonany, nakłada <style="highlight">5</style> [DarkFlame] na wszystkich wrogów z [Combustion]
515. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([FreischutzShotCount] / 3)만큼 [Combustion] 횟수 증가 (소수점 버림)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FreischutzShotCount], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +([FreischutzShotCount] / 3) [Combustion] Count (rounded down)
   PL: [OnSucceedAttack] nakłada +([FreischutzShotCount] / 3) Licznika [Combustion] (zaokrąglone w dół)
516. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [FreischutzShotCount]만큼 [DarkFlame] 부여 (턴 당 대상 1명마다 최대 1회 부여)<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2110821].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FreischutzShotCount], [DarkFlame]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [DarkFlame] = 흑염 / Dark Flame
   EN: [OnSucceedAttack] Inflict [DarkFlame] equal to [FreischutzShotCount] (once per turn for each unit)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada tyle [DarkFlame], ile wynosi [FreischutzShotCount] (maks. 1 raz na turę na każdy cel)<style="highlight"></style>
517. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 [Combustion] 수치 3당 피해량 +<style="highlight">3</style>% (최대 <style="highlight">30</style>%)\n[BeforeAttack] [FreischutzShotCount]이 0이면, [FreischutzShotCount] 1 얻음.\n- [FreischutzShotCount] 수치에 따라 발사할 탄환이 정해짐\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] 최대 공명 수만큼 [FreischutzShotCount]을 얻음 (최소 1, 최대 4)\n[EndSkill] 메인 타겟이 사망했으면, [Combustion]이 있는 모든 대상에게 [DarkFlame] <style="highlight">7</style> 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=4].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Combustion], [BeforeAttack], [FreischutzShotCount], [FreishutzOutisEgoBullet_1st], [FreishutzOutisEgoBullet_2nd], [FreishutzOutisEgoBullet_3rd], [FreishutzOutisEgoBullet_4th], [FreishutzOutisEgoBullet_5th], [FreishutzOutisEgoBullet_6th], [FreishutzOutisEgoBullet_7th], [EndSkill], [DarkFlame]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [FreishutzOutisEgoBullet_1st] = 첫번째 마탄 / The First Magic Bullet; [FreishutzOutisEgoBullet_2nd] = 두번째 마탄 / The Second Magic Bullet; [FreishutzOutisEgoBullet_3rd] = 세번째 마탄 / The Third Magic Bullet; [FreishutzOutisEgoBullet_4th] = 네번째 마탄 / The Fourth Magic Bullet …
   EN: [CantIdentify]\nTargets randomly\nDeal +<style="highlight">3</style>% damage for every 3 [Combustion] on target (max <style="highlight">30</style>%)\n[BeforeAttack] At 0 [FreischutzShotCount], gain 1 [FreischutzShotCount].\n- [FreischutzShotCount] value determines the bullet to fire.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] Gain [FreischutzShotCount] equal to the highest Reson. (min. 1, max 4)\n[EndSkill] If the main target is defeated, inflict <style="highlight">7</style> [DarkFlame] against all enemies that have [Combustion]
   PL: [CantIdentify]\nAtakuje losowy cel\nzadaje +<style="highlight">3</style>% obrażeń za każde 3 Licznika [Combustion] na celu (maks. <style="highlight">30</style>%)\n[BeforeAttack] przy 0 [FreischutzShotCount], zyskuje 1 [FreischutzShotCount].\n- wartość [FreischutzShotCount] określa wystrzeliwany pocisk.\n· [FreishutzOutisEgoBullet_1st]\n· [FreishutzOutisEgoBullet_2nd]\n· [FreishutzOutisEgoBullet_3rd]\n· [FreishutzOutisEgoBullet_4th]\n· [FreishutzOutisEgoBullet_5th]\n· [FreishutzOutisEgoBullet_6th]\n· [FreishutzOutisEgoBullet_7th]\n[EndSkill] zyskuje tyle [FreischutzShotCount], ile wynosi najwyższy Rezonans (min. 1, maks. 4)\n[EndSkill] jeżeli cel główny został pokonany, nakłada <style="highlight">7</style> [DarkFlame] na wszystkich wrogów z [Combustion]
518. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([FreischutzShotCount] / <style="highlight">2</style>)만큼 [Combustion] 횟수 증가 (소수점 버림)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FreischutzShotCount], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +([FreischutzShotCount] / <style="highlight">2</style>) [Combustion] Count (rounded down)
   PL: [OnSucceedAttack] nakłada +([FreischutzShotCount] / <style="highlight">2</style>) Licznika [Combustion] (zaokrąglone w dół)
519. [Pasywka E.G.O — nazwa] 일곱 개의 탄환
   źródło: Passive_Ego.json :: dataList[id=2110811].name
   limit: do 40 znaków
   EN: Seven Bullets
   PL: Siedem Pocisków
520. [Pasywka E.G.O — opis] 기본 공격 스킬로 적중 시, 자신의 ([FreischutzShotCount] / 3)만큼 [Combustion] 부여 (턴 당 최대 3회 부여)\n- 로보토미 E.G.O:: 마탄[TabExplain] 오티스 인격인 경우, 대신 자신의 [FreischutzShotCount]만큼 [Combustion] 부여 (턴 당 최대 3회 부여)\n- 대상의 [Combustion] 위력이 30 이상이면, 위 효과를 대신하여 [DarkFlame] 1 부여 (턴 당 최대 2회 부여)
   źródło: Passive_Ego.json :: dataList[id=2110811].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [FreischutzShotCount], [Combustion], [TabExplain], [DarkFlame]
   znaczenie tagów: [FreischutzShotCount] = 마탄 / Magic Bullet; [Combustion] = 화상 / Burn; [DarkFlame] = 흑염 / Dark Flame
   EN: - On Hit with Base Attack Skills: inflict ([FreischutzShotCount] / 3) [Combustion] (3 times per turn)\n- For Lobotomy E.G.O::Magic Bullet[TabExplain] Outis Identity, inflict ([FreischutzShotCount]) [Combustion] instead (3 times per turn)\n- If the target has 30+ [Combustion], inflict 1 [DarkFlame] instead of the above effect (2 times per turn)
   PL: przy trafieniu Podstawową Umiejętnością Ataku, nakłada tyle [Combustion], ile wynosi ([FreischutzShotCount] / 3) (maks. 3 na turę)\n- w przypadku Tożsamości Outis Lobotomy E.G.O::Magic Bullet[TabExplain], zamiast tego nakłada tyle [Combustion], ile wynosi [FreischutzShotCount] (maks. 3 na turę)\n- jeżeli Siła [Combustion] celu wynosi 30 lub więcej, zamiast tego nakłada 1 [DarkFlame] (maks. 2 na turę)

## E.G.O [21109] I'll Go fer Scissors. How 'Bout You? (난 가위를 낼게, 너는?) — Outis
- postać: Outis (오티스) · ID E.G.O: `21109`

521. [Karta E.G.O — nazwa] 난 가위를 낼게, 너는?
   źródło: Egos.json :: dataList[id=21109].name
   limit: do 50 znaków
   EN: I'll Go fer Scissors. How 'Bout You?
   PL: Ja Graję Nożyczki. A Ty?
522. [Karta E.G.O — opis] 오티스 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21109].desc
   limit: do 120 znaków
   EN: Outis’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Outis
523. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 난 가위를 낼게, 너는?
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].name ; dataList[id=2110911].levelList[level=3].name ; dataList[id=2110911].levelList[level=4].name
   (powtórzenie elementu 521 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 놀아줄래
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].abName ; dataList[id=2110911].levelList[level=3].abName ; dataList[id=2110911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Will You Play?
   PL: Pobawisz się?
525. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 일방 공격 시 이 스킬의 [UnBrokenCoinOnSucceedAttack] 효과가 발동하지 않음\n[WinDuel] 질투 공명 수만큼 질투 E.G.O 자원을 소모하고 소모한 자원 1당, 제일 적은 E.G.O 자원을 1씩 나누어 얻음 (최대 소모량 4)\n[DefeatDuel] 최종 위력이 4 감소하는 대신 (질투 공명 수 x 5)만큼 보호막 얻음 (최대 20)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack], [WinDuel], [DefeatDuel]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: On Unopposed Attack: Does not activate this skill's [UnBrokenCoinOnSucceedAttack] effects\n[WinDuel] Consume Envy E.G.O resource by Envy Reson., and for every Envy E.G.O resource consumed, gain 1 E.G.O resource each for the least-owned Affinities (max consumable Envy resource: 4)\n[DefeatDuel] Final Power -4 and gain Shield equal to (Envy Reson. x 5) (max 20)
   PL: przy ataku bez oporu: nie uruchamia efektów [UnBrokenCoinOnSucceedAttack] tej Umiejętności\n[WinDuel] zużywa zasób E.G.O Zazdrości w ilości równej Rezonansowi Zazdrości, a za każdy zużyty zasób E.G.O zyskuje po 1 zasobu E.G.O każdej z najmniej posiadanych Afiniczności (maks. zużywanego zasobu Zazdrości: 4)\n[DefeatDuel] Moc Końcowa -4 i zyskuje Tarczę równą (Rezonans Zazdrości x 5) (maks. 20)
526. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110911].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 각자의 최대 체력 6%만큼 회복 (스킬당 1회)\n- 자신을 제외한 질투 속성인 기본 공격 스킬을 보유하지 않은 아군은 회복 대상이 되지 않음
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal 2 allies with the lowest HP percentage by 6% of their max HP (once per Skill)\n- Ignores allies without Envy Base Attack Skills when choosing targets for healing (excluding this unit)
   PL: [UnBrokenCoinOnSucceedAttack] leczy 2 sojuszników z najniższym aktualnym procentem HP o 6% ich Maks. HP (1 raz na Umiejętność)\n- przy wyborze celów leczenia pomija sojuszników bez Podstawowej Umiejętności Ataku Zazdrości (z wyłączeniem tej jednostki)
528. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — podsumowanie] [UnBrokenCoinOnSucceedAttack] 체력 회복
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].coinlist[#0].coindescs[#1].summary ; dataList[id=2110911].levelList[level=3].coinlist[#0].coindescs[#1].summary ; dataList[id=2110911].levelList[level=4].coinlist[#0].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal HP
   PL: [UnBrokenCoinOnSucceedAttack] leczy HP
529. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NiddleEGO] 2 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2110911].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2110911].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddleEGO]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddleEGO] = 바늘 / Needle
   EN: [OnSucceedAttack] Inflict 2 [NiddleEGO]
   PL: [OnSucceedAttack] nakłada 2 [NiddleEGO]
530. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [NailPersonality] 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 1 [NailPersonality]
   PL: [OnSucceedAttack] nakłada 1 [NailPersonality]
531. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 일방 공격 시 이 스킬의 [UnBrokenCoinOnSucceedAttack] 효과가 발동하지 않음\n[WinDuel] 질투 공명 수만큼 질투 E.G.O 자원을 소모하고 소모한 자원 1당, 제일 적은 E.G.O 자원을 1씩 나누어 얻음 (최대 소모량 5)\n[DefeatDuel] 최종 위력이 4 감소하는 대신 (질투 공명 수 x 5)만큼 보호막 얻음 (최대 25)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack], [WinDuel], [DefeatDuel]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: On Unopposed Attack: Does not activate this skill's [UnBrokenCoinOnSucceedAttack] effects\n[WinDuel] Consume Envy E.G.O resource by Envy Reson., and for every Envy E.G.O resource consumed, gain 1 E.G.O resource each for the least-owned Affinities (max consumable Envy resource: 5)\n[DefeatDuel] Final Power -4 and gain Shield equal to (Envy Reson. x 5) (max 25)
   PL: przy ataku bez oporu: nie uruchamia efektów [UnBrokenCoinOnSucceedAttack] tej Umiejętności\n[WinDuel] zużywa zasób E.G.O Zazdrości w ilości równej Rezonansowi Zazdrości, a za każdy zużyty zasób E.G.O zyskuje po 1 zasobu E.G.O każdej z najmniej posiadanych Afiniczności (maks. zużywanego zasobu Zazdrości: 5)\n[DefeatDuel] Moc Końcowa -4 i zyskuje Tarczę równą (Rezonans Zazdrości x 5) (maks. 25)
532. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 각자의 최대 체력 8%만큼 회복 (스킬당 1회)\n- 자신을 제외한 질투 속성인 기본 공격 스킬을 보유하지 않은 아군은 회복 대상이 되지 않음
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal 2 allies with the lowest HP percentage by 8% of their max HP (once per Skill)\n- Ignores allies without Envy Base Attack Skills when choosing targets for healing (excluding this unit)
   PL: [UnBrokenCoinOnSucceedAttack] leczy 2 sojuszników z najniższym aktualnym procentem HP o 8% ich Maks. HP (1 raz na Umiejętność)\n- przy wyborze celów leczenia pomija sojuszników bez Podstawowej Umiejętności Ataku Zazdrości (z wyłączeniem tej jednostki)
533. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Curse] 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2110911].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 1 [Curse]
   PL: [OnSucceedAttack] nakłada 1 [Curse]
534. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [NailPersonality] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=2110911].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 1 [NailPersonality]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 1 [NailPersonality]<style="highlight"></style>
535. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 일방 공격 시 이 스킬의 [UnBrokenCoinOnSucceedAttack] 효과가 발동하지 않음\n[WinDuel] 질투 공명 수만큼 질투 E.G.O 자원을 소모하고 소모한 자원 1당, 제일 적은 E.G.O 자원을 1씩 나누어 얻음 (최대 소모량 6)\n[DefeatDuel] 최종 위력이 4 감소하는 대신 (질투 공명 수 x 5)만큼 보호막 얻음 (최대 30)
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=4].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack], [WinDuel], [DefeatDuel]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: On Unopposed Attack: Does not activate this skill's [UnBrokenCoinOnSucceedAttack] effects\n[WinDuel] Consume Envy E.G.O resource by Envy Reson., and for every Envy E.G.O resource consumed, gain 1 E.G.O resource each for the least-owned Affinities (max consumable Envy resource: 6)\n[DefeatDuel] Final Power -4 and gain Shield equal to (Envy Reson. x 5) (max 30)
   PL: przy ataku bez oporu: nie uruchamia efektów [UnBrokenCoinOnSucceedAttack] tej Umiejętności\n[WinDuel] zużywa zasób E.G.O Zazdrości w ilości równej Rezonansowi Zazdrości, a za każdy zużyty zasób E.G.O zyskuje po 1 zasobu E.G.O każdej z najmniej posiadanych Afiniczności (maks. zużywanego zasobu Zazdrości: 6)\n[DefeatDuel] Moc Końcowa -4 i zyskuje Tarczę równą (Rezonans Zazdrości x 5) (maks. 30)
536. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 현재 체력 비율이 가장 낮은 아군 2명의 체력을 각자의 최대 체력 10%만큼 회복 (스킬당 1회)\n- 자신을 제외한 질투 속성인 기본 공격 스킬을 보유하지 않은 아군은 회복 대상이 되지 않음
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110911].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal 2 allies with the lowest HP percentage by 10% of their max HP (once per Skill)\n- Ignores allies without Envy Base Attack Skills when choosing targets for healing (excluding this unit)
   PL: [UnBrokenCoinOnSucceedAttack] leczy 2 sojuszników z najniższym aktualnym procentem HP o 10% ich Maks. HP (1 raz na Umiejętność)\n- przy wyborze celów leczenia pomija sojuszników bez Podstawowej Umiejętności Ataku Zazdrości (z wyłączeniem tej jednostki)
537. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 난 가위를 낼게, 너는?
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].name ; dataList[id=2110921].levelList[level=3].name ; dataList[id=2110921].levelList[level=4].name
   (powtórzenie elementu 521 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 놀아줄래
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].abName ; dataList[id=2110921].levelList[level=3].abName ; dataList[id=2110921].levelList[level=4].abName
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n질투 공명 수가 2 이상이면, 최종 위력 +1\n[WinDuel] 질투 공명 수 2당, 공격 가중치 +1 (최대 2)\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 20)\n[DefeatDuel] 이 스킬의 [NiddleEGO], [NailPersonality] 부여량 +1
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WinDuel], [DefeatDuel], [NiddleEGO], [NailPersonality]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [NiddleEGO] = 바늘 / Needle; [NailPersonality] = 못 / Nails
   EN: [CantIdentify]\nTargets randomly\nAt 2+ Envy Reson., Final Power +1\n[WinDuel] Atk Weight +1 for every 2 Envy Reson. (max 2)\n[DefeatDuel] Gain Shield equal to (Envy Reson. x 5) (max 20)\n[DefeatDuel] This Skill inflicts +1 more [NiddleEGO] and [NailPersonality]
   PL: [CantIdentify]\nAtakuje losowy cel\nprzy Rezonansie Zazdrości 2+ Moc Końcowa +1\n[WinDuel] Waga Ataku +1 za każde 2 Rezonansu Zazdrości (maks. 2)\n[DefeatDuel] zyskuje Tarczę równą (Rezonans Zazdrości x 5) (maks. 20)\n[DefeatDuel] ta Umiejętność nakłada o +1 więcej [NiddleEGO] i [NailPersonality]
540. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2110921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2110921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NiddleEGO] 3 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2110921].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2110921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddleEGO]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddleEGO] = 바늘 / Needle
   EN: [OnSucceedAttack] Inflict 3 [NiddleEGO]
   PL: [OnSucceedAttack] nakłada 3 [NiddleEGO]
542. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2110921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2110921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2110921].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2110921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 1 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2110921].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2110921].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n질투 공명 수 2<style="highlight">당</style>, 최종 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] 질투 공명 수 2당, 공격 가중치 +1 (최대 2)\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 <style="highlight">25</style>)\n[DefeatDuel] 이 스킬의 [NiddleEGO], <style="highlight">[Curse]</style>, [NailPersonality] 부여량 +1
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WinDuel], [DefeatDuel], [NiddleEGO], [Curse], [NailPersonality]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [NiddleEGO] = 바늘 / Needle; [Curse] = 저주 / Curse; [NailPersonality] = 못 / Nails
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">Final Power +1 for every 2 Envy Reson. (max 2)</style>\n[WinDuel] Atk Weight +1 for every 2 Envy Reson. (max 2)\n[DefeatDuel] Gain Shield equal to (Envy Reson. x 5) (max <style="highlight">25</style>)\n[DefeatDuel] This Skill inflicts +1 more [NiddleEGO], <style="highlight">[Curse]</style>, and [NailPersonality]
   PL: [CantIdentify]\nAtakuje losowy cel\nza <style="highlight">każde</style> 2 Rezonansu Zazdrości Moc Końcowa +1 <style="highlight">(maks. 2)</style>\n[WinDuel] Waga Ataku +1 za każde 2 Rezonansu Zazdrości (maks. 2)\n[DefeatDuel] zyskuje Tarczę równą (Rezonans Zazdrości x 5) (maks. <style="highlight">25</style>)\n[DefeatDuel] ta Umiejętność nakłada o +1 więcej [NiddleEGO], <style="highlight">[Curse]</style> i [NailPersonality]
546. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Curse] 2 부여
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2110921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 2 [Curse]
   PL: [OnSucceedAttack] nakłada 2 [Curse]
547. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n질투 공명 수 2당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WinDuel] 질투 공명 수 2당, 공격 가중치 +1 (최대 2)\n[DefeatDuel] (질투 공명 수 x 5)만큼 보호막 얻음 (최대 <style="highlight">30</style>)\n[DefeatDuel] 이 스킬의 [NiddleEGO], [Curse], [NailPersonality] 부여량 +1<style="highlight"></style>
   źródło: Skills_Ego_Personality-11.json :: dataList[id=2110921].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WinDuel], [DefeatDuel], [NiddleEGO], [Curse], [NailPersonality]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [NiddleEGO] = 바늘 / Needle; [Curse] = 저주 / Curse; [NailPersonality] = 못 / Nails
   EN: [CantIdentify]\nTargets randomly\nFinal Power +1 for every 2 Envy Reson. (max <style="highlight">3</style>)\n[WinDuel] Atk Weight +1 for every 2 Envy Reson. (max 2)\n[DefeatDuel] Gain Shield equal to (Envy Reson. x 5) (max <style="highlight">30</style>)\n[DefeatDuel] This Skill inflicts +1 more [NiddleEGO], [Curse], and [NailPersonality]<style="highlight"></style>
   PL: [CantIdentify]\nAtakuje losowy cel\nza każde 2 Rezonansu Zazdrości Moc Końcowa +1 (maks. <style="highlight">3</style>)\n[WinDuel] Waga Ataku +1 za każde 2 Rezonansu Zazdrości (maks. 2)\n[DefeatDuel] zyskuje Tarczę równą (Rezonans Zazdrości x 5) (maks. <style="highlight">30</style>)\n[DefeatDuel] ta Umiejętność nakłada o +1 więcej [NiddleEGO], [Curse] i [NailPersonality]<style="highlight"></style>
548. [Pasywka E.G.O — nazwa] 저주벌칙
   źródło: Passive_Ego.json :: dataList[id=2110911].name
   limit: do 40 znaków
   EN: Loser's Penalty: Voodoo
   PL: Kara dla Przegranych: Voodoo
549. [Pasywka E.G.O — opis] 합 승리 시, 대상에게 4만큼 질투 피해를 입힘\n- 대상의 체력이 33%미만이거나 자신의 체력이 33% 미만이면, 다음 턴에 [ResultReduction] 1 부여 (턴당 1회)\n- E.G.O 기프트 <noparse>저주</noparse> 인형이 발동한 턴에는 이 패시브 효과로 [ResultReduction]를 부여하지 않음
   źródło: Passive_Ego.json :: dataList[id=2110911].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ResultReduction]
   znaczenie tagów: [ResultReduction] = 위력 감소 / Power Down
   EN: On Clash Win, deal 4 Envy damage to target\n- At less than 33% HP, or if target has less than 33% HP, inflict 1 [ResultReduction] next turn (once per turn)\n- This Passive's effect does not inflict [ResultReduction] in the same turn the E.G.O Gift <noparse>Voodoo Doll</noparse> activated
   PL: przy wygranej starciu zadaje celowi 4 obrażeń Zazdrości\n- jeżeli HP celu jest niższe niż 33% albo własne HP jest niższe niż 33%, następnej tury nakłada 1 [ResultReduction] (1 raz na turę)\n- w turze, w której uruchomił się Prezent E.G.O „Laleczka Voodoo", ten efekt pasywny nie nakłada [ResultReduction]
550. [Pasywka E.G.O — podsumowanie] 합 승리 시, 질투 피해를 입힘\n조건 만족 시, 다음 턴에 [ResultReduction] 부여
   źródło: Passive_Ego.json :: dataList[id=2110911].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [ResultReduction]
   znaczenie tagów: [ResultReduction] = 위력 감소 / Power Down
   EN: Clash Win: Deal Envy damage\nIf conditions are met, inflict [ResultReduction] next turn
   PL: przy wygranej starciu zadaje obrażenia Zazdrości\njeżeli warunki są spełnione, następnej tury nakłada [ResultReduction]

## E.G.O [21201] Suddenly, One Day (어느날 갑자기) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21201`

551. [Karta E.G.O — nazwa] 어느날 갑자기
   źródło: Egos.json :: dataList[id=21201].name
   limit: do 40 znaków
   EN: Suddenly, One Day
   PL: Nagle, Pewnego Dnia
552. [Karta E.G.O — opis] 그레고르의 기본 EGO 장비
   źródło: Egos.json :: dataList[id=21201].desc
   limit: do 120 znaków
   EN: Gregor’s Base E.G.O
   PL: Podstawowy Sprzęt E.G.O Gregor
553. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 어느날 갑자기
   źródło: Skills_Ego.json :: dataList[id=2120111].levelList[level=1].name ; dataList[id=2120111].levelList[level=3].name ; dataList[id=2120111].levelList[level=4].name
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 그레고르
   źródło: Skills_Ego.json :: dataList[id=2120111].levelList[level=1].abName ; dataList[id=2120111].levelList[level=3].abName ; dataList[id=2120111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor
555. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과 3 부여
   źródło: Skills_Ego.json :: dataList[id=2120111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] nakłada 3 wartości 1 losowego z efektów: [Combustion], [Laceration], [Vibration], [Burst] lub [Sinking]
556. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과 6 부여
   źródło: Skills_Ego.json :: dataList[id=2120111].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 6 of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] nakłada 6 wartości 1 losowego z efektów: [Combustion], [Laceration], [Vibration], [Burst] lub [Sinking]
557. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과 10 부여
   źródło: Skills_Ego.json :: dataList[id=2120111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 10 of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] nakłada 10 wartości 1 losowego z efektów: [Combustion], [Laceration], [Vibration], [Burst] lub [Sinking]
558. [Pasywka E.G.O — nazwa] 이형발작
   źródło: Passive_Ego.json :: dataList[id=2120111].name
   limit: do 40 znaków
   EN: Uncontrolled Morph
   PL: Niekontrolowana Przemiana
559. [Pasywka E.G.O — opis] 턴 시작 시 체력이 25% 미만이면 체력을 15 회복하고, 보호 2를 얻음.\n해당 효과 발동 시 자신을 제외한 무작위 아군과 적 1명의 정신력 감소 효율 +2
   źródło: Passive_Ego.json :: dataList[id=2120111].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [MentalSystemResultDecrease_Typo]
   znaczenie tagów: [Protection] = 보호 / Protection; [MentalSystemResultDecrease_Typo] = 정신력 감소 효율 / SP Loss Efficiency
   EN: Turn Start: At less than 25% HP, heal 15 HP and gain 2 [Protection]\nWhen the above effect activates, inflict +2 [MentalSystemResultDecrease_Typo] on 1 random other ally and 1 random enemy
   PL: na początku tury, przy HP niższym niż 25%, odzyskuje 15 HP i zyskuje 2 [Protection]\ngdy ten efekt się uruchomi, nakłada +2 [MentalSystemResultDecrease_Typo] na 1 innego losowego sojusznika i 1 losowego wroga

## E.G.O [21202] Legerdemain (눈속임) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21202`

560. [Karta E.G.O — nazwa] 눈속임
   źródło: Egos.json :: dataList[id=21202].name
   limit: do 40 znaków
   EN: Legerdemain
   PL: Kuglarstwo
561. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21202].desc
   limit: do 120 znaków
   EN: Gregor’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Gregor
562. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 눈속임
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=1].name ; dataList[id=2120211].levelList[level=3].name ; dataList[id=2120211].levelList[level=4].name
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 황금빛의 사과
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=1].abName ; dataList[id=2120211].levelList[level=3].abName ; dataList[id=2120211].levelList[level=4].abName
   limit: do 40 znaków
   EN: Golden Apple
   PL: Złociste Jabłko
564. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
565. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 마비 2 부여
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 2 [Paralysis]
   PL: [OnSucceedAttackHead] nakłada 2 [Paralysis]
566. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120211].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Wybuch Wstrząsu
567. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] Nakłada 4 Wstrząsu
568. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 마비 4 부여
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 4 [Paralysis]
   PL: [OnSucceedAttackHead] nakłada 4 [Paralysis]
569. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 6 부여
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL: [OnSucceedAttack] Nakłada 6 [Vibration]
570. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 마비 4 부여
   źródło: Skills_Ego.json :: dataList[id=2120211].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 4 [Paralysis]
   PL: [OnSucceedAttack] nakłada 4 [Paralysis]
571. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 눈속임
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=1].name ; dataList[id=2120221].levelList[level=3].name ; dataList[id=2120221].levelList[level=4].name
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 황금빛의 사과
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=1].abName ; dataList[id=2120221].levelList[level=3].abName ; dataList[id=2120221].levelList[level=4].abName
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=1].desc ; dataList[id=2120221].levelList[level=3].desc ; dataList[id=2120221].levelList[level=4].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
575. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 마비 2 부여
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120221].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] Nakłada 4 Krwawienia
577. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 4 부여
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2120221].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 구더기 4 부여
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Muckworm]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Muckworm] = 구더기 / Maggots
   EN: [OnSucceedAttack] Inflict 4 [Muckworm]
   PL: [OnSucceedAttack] nakłada 4 [Muckworm]
579. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 구더기 6 부여
   źródło: Skills_Ego.json :: dataList[id=2120221].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Muckworm]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Muckworm] = 구더기 / Maggots
   EN: [OnSucceedAttack] Inflict 6 [Muckworm]
   PL: [OnSucceedAttack] nakłada 6 [Muckworm]
580. [Pasywka E.G.O — nazwa] 구더기
   źródło: Passive_Ego.json :: dataList[id=2120211].name
   limit: do 40 znaków
   EN: Maggots
   PL: Czerwie
581. [Pasywka E.G.O — opis] 공격 적중 시 (탐식 완전 공명 수 x 8)% 확률로 구더기 5 부여
   źródło: Passive_Ego.json :: dataList[id=2120211].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Muckworm]
   znaczenie tagów: [Muckworm] = 구더기 / Maggots
   EN: On Hit, inflict 5 [Muckworm] with a (Gluttony A-Reson. x 8)% chance
   PL: przy trafieniu nakłada 5 [Muckworm] z szansą (Rezonans Absolutny Obżarstwa x 8)%

## E.G.O [21203] Lantern (초롱) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21203`

582. [Karta E.G.O — nazwa] 초롱
   źródło: Egos.json :: dataList[id=21203].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21203].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 초롱
   źródło: Skills_Ego.json :: dataList[id=2120311].levelList[level=1].name ; dataList[id=2120311].levelList[level=3].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 요정초롱
   źródło: Skills_Ego.json :: dataList[id=2120311].levelList[level=1].abName ; dataList[id=2120311].levelList[level=3].abName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 40%만큼 자신의 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2120311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 40% of damage dealt
   PL: [OnSucceedAttack] leczy własne HP o 40% zadanych obrażeń
587. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 60%만큼 자신의 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2120311].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 60% of damage dealt
   PL: [OnSucceedAttack] leczy własne HP o 60% zadanych obrażeń
588. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 초롱
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=1].name ; dataList[id=2120321].levelList[level=3].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 요정초롱
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=1].abName ; dataList[id=2120321].levelList[level=3].abName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n체력이 가장 많은 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=1].desc ; dataList[id=2120321].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify] \nTargets the unit with the most HP
   PL: [CantIdentify]\nAtakuje cel z najwyższym HP
591. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 20%만큼 자신의 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20% of damage dealt
   PL: [OnSucceedAttack] leczy własne HP o 20% zadanych obrażeń
592. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 자신의 체력 회복
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 30% of damage dealt
   PL: [OnSucceedAttack] leczy własne HP o 30% zadanych obrażeń
594. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills_Ego.json :: dataList[id=2120321].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 5 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 5 Rozdarcia
595. [Pasywka E.G.O — nazwa] 양분 흡수
   źródło: Passive_Ego.json :: dataList[id=2120311].name
   limit: do 40 znaków
   EN: Nutrient Absorption
   PL: Pobór Substancji
596. [Pasywka E.G.O — opis] 파열이 부여된 적 처치 시 최대 체력의  (탐식 완전 공명 수)% 만큼 체력 회복
   źródło: Passive_Ego.json :: dataList[id=2120311].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: After defeating an enemy that has [Burst], heal (Gluttony A-Reson.)% HP.
   PL: po pokonaniu wroga posiadającego [Burst], odzyskuje HP równe (Rezonans Absolutny Obżarstwa)% Maks. HP.

## E.G.O [21204] AEDD (AEDD) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21204`

597. [Karta E.G.O — nazwa] AEDD
   źródło: Egos.json :: dataList[id=21204].name
   limit: do 40 znaków
   EN: AEDD
   PL: AEDD
598. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21204].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] AEDD
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=1].name ; dataList[id=2120411].levelList[level=3].name ; dataList[id=2120411].levelList[level=4].name
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 충격 지네
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=1].abName ; dataList[id=2120411].levelList[level=3].abName ; dataList[id=2120411].levelList[level=4].abName
   limit: do 40 znaków
   EN: Shock Centipede
   PL: Wstrząsowa Stonoga
601. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 자신의 충전 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] Gain +5 [Charge] Count
   PL: [BeforeAttack] zyskuje +5 Licznika [Charge]
602. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방출 전류 5 부여
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EmittedCurrent]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EmittedCurrent] = 방출 전류 / Spark Discharge
   EN: [OnSucceedAttack] Inflict 5 [EmittedCurrent]
   PL: [OnSucceedAttack] nakłada 5 [EmittedCurrent]
603. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신의 충전 횟수 7 증가
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] Gain +7 [Charge] Count
   PL: [BeforeAttack] zyskuje +7 Licznika [Charge]
604. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방출 전류 10 부여
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EmittedCurrent]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EmittedCurrent] = 방출 전류 / Spark Discharge
   EN: [OnSucceedAttack] Inflict 10 [EmittedCurrent]
   PL: [OnSucceedAttack] nakłada 10 [EmittedCurrent]
605. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신의 충전 횟수 10 증가
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] Gain +10 [Charge] Count
   PL: [BeforeAttack] zyskuje +10 Licznika [Charge]
606. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방출 전류 15 부여
   źródło: Skills_Ego.json :: dataList[id=2120411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EmittedCurrent]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EmittedCurrent] = 방출 전류 / Spark Discharge
   EN: [OnSucceedAttack] Inflict 15 [EmittedCurrent]
   PL: [OnSucceedAttack] nakłada 15 [EmittedCurrent]
607. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] AEDD
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=1].name ; dataList[id=2120421].levelList[level=3].name ; dataList[id=2120421].levelList[level=4].name
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 충격 지네
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=1].abName ; dataList[id=2120421].levelList[level=3].abName ; dataList[id=2120421].levelList[level=4].abName
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n충전을 보유한 무작위 대상 우선 공격\n[BeforeAttack] 자신의 충전 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nPrioritizes units with [Charge]\n[BeforeAttack] Gain +5 [Charge] Count
   PL: [CantIdentify]\npriorytetowo atakuje jednostki posiadające [Charge]\n[BeforeAttack] zyskuje +5 Licznika [Charge]
610. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방출 전류 5 부여. 대상의 충전 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EmittedCurrent], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EmittedCurrent] = 방출 전류 / Spark Discharge; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 5 [EmittedCurrent] and +5 [Charge] Count
   PL: [OnSucceedAttack] nakłada 5 [EmittedCurrent] i +5 Licznika [Charge] celu
611. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n충전을 보유한 무작위 대상 우선 공격\n[BeforeAttack] 자신의 충전 횟수 7 증가
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nPrioritizes units with [Charge]\n[BeforeAttack] Gain +7 [Charge] Count
   PL: [CantIdentify]\npriorytetowo atakuje jednostki posiadające [Charge]\n[BeforeAttack] zyskuje +7 Licznika [Charge]
612. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방출 전류 10 부여. 대상의 충전 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EmittedCurrent], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EmittedCurrent] = 방출 전류 / Spark Discharge; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 10 [EmittedCurrent] and +5 [Charge] Count
   PL: [OnSucceedAttack] nakłada 10 [EmittedCurrent] i +5 Licznika [Charge] celu
613. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n충전을 보유한 무작위 대상 우선 공격\n[BeforeAttack] 자신의 충전 횟수 10 증가
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nPrioritizes units with [Charge]\n[BeforeAttack] Gain +10 [Charge] Count
   PL: [CantIdentify]\npriorytetowo atakuje jednostki posiadające [Charge]\n[BeforeAttack] zyskuje +10 Licznika [Charge]
614. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방출 전류 15 부여. 대상의 충전 횟수 7 증가
   źródło: Skills_Ego.json :: dataList[id=2120421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EmittedCurrent], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EmittedCurrent] = 방출 전류 / Spark Discharge; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 15 [EmittedCurrent] and +7 [Charge] Count
   PL: [OnSucceedAttack] nakłada 15 [EmittedCurrent] i +7 Licznika [Charge] celu
615. [Pasywka E.G.O — nazwa] 교류 방출
   źródło: Passive_Ego.json :: dataList[id=2120411].name
   limit: do 40 znaków
   EN: Alternating Discharge
   PL: Naprzemienne Wyładowanie
616. [Pasywka E.G.O — opis] 앞면 적중 시 자신의 충전 횟수 2를 소모하여 충전을 보유한 아군 중 충전 횟수가 가장 낮은 아군 1명의 충전 횟수 1 증가
   źródło: Passive_Ego.json :: dataList[id=2120411].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: On Heads Hit, consume 2 [Charge] Count to apply +1 [Charge] Count on the [Charge]-possessing ally that has the lowest [Charge] Count
   PL: przy trafieniu Orłem zużywa 2 Licznika [Charge], by nakładać +1 Licznika [Charge] na sojusznika posiadającego [Charge] z najniższym Licznikiem [Charge]

## E.G.O [21205] Garden of Thorns (가시 화원) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21205`

617. [Karta E.G.O — nazwa] 가시 화원
   źródło: Egos.json :: dataList[id=21205].name
   limit: do 40 znaków
   EN: Garden of Thorns
   PL: Ogród Cierni
618. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21205].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 가시 화원
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=1].name ; dataList[id=2120511].levelList[level=3].name ; dataList[id=2120511].levelList[level=4].name
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 장미 표지판
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=1].abName ; dataList[id=2120511].levelList[level=3].abName ; dataList[id=2120511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Sign of Roses
   PL: Znak Róż
621. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 가장 높은 공명이 3 이상이면, 공격 가중치 +1\n[WhenUse] 아군 1 + (가장 높은 공명 수)명에게 해당 공명 속성의 피해량 증가와 위력 증가를 1 부여\n- 해당 공명이 4 이상이면, 해당 속성 피해량 증가를 1 추가 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] At 3+ highest Reson., Atk Weight +1\n[WhenUse] Apply 1 '(Corresponding Sin Affinity) Damage Up' and '1 (Corresponding Sin Affinity) Power Up' to (1 + # of highest Reson.) allies.\n- At 4+ Corresponding Reson., apply 1 additional '(Corresponding Sin Affinity) Damage Up'
   PL: [BeforeAttack] przy najwyższym Rezonansie 3+ Waga Ataku +1\n[WhenUse] nakłada 1 zwiększenia zadawanych obrażeń i 1 zwiększenia Mocy Umiejętności odpowiadającego Afiniczności tego Rezonansu na (1 + najwyższy Rezonans) sojuszników\n- przy odpowiednim Rezonansie 4+ dodatkowo nakłada 1 zwiększenia zadawanych obrażeń odpowiadającego tej Afiniczności
622. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndSkill] 체력 비율이 가장 낮은 아군 1명의 체력을 최대 체력의 15% 만큼 회복\n- (가장 높은 공명 수 - 2)만큼 회복 대상 증가 (최대 3)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 1 ally with the lowest HP percentage for 15% HP of their max HP\n- Heal (highest Reson. - 2) more allies (max 3)
   PL: [EndSkill] leczy 1 sojusznika z najniższym aktualnym procentem HP o 15% jego Maks. HP\n- leczy (najwyższy Rezonans - 2) dodatkowych sojuszników (maks. 3)
623. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)\n[WhenUse] 아군 2 + (가장 높은 공명 수)명에게 해당 공명 속성의 피해량 증가와 위력 증가를 1 부여\n- 해당 공명이 4 이상이면, 해당 속성 피해량 증가를 1 추가 부여\n- 해당 공명이 5 이상이면, 해당 속성 위력 증가를 1 추가 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=3].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] Gain (# of highest Reson. - 2) Atk Weight (Max 2)\n[WhenUse] Apply 1 '(Corresponding Sin Affinity) Damage Up' and '1 (Corresponding Sin Affinity) Power Up' to (2 + # of highest Reson.) allies.\n- At 4+ Corresponding Reson., apply 1 additional '(Corresponding Sin Affinity) Damage Up'\n- At 5+ Corresponding Reson., apply 1 additional '(Corresponding Sin Affinity) Power Up'
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 2)\n[WhenUse] nakłada 1 zwiększenia zadawanych obrażeń i 1 zwiększenia Mocy Umiejętności odpowiadającego Afiniczności tego Rezonansu na (2 + najwyższy Rezonans) sojuszników\n- przy odpowiednim Rezonansie 4+ dodatkowo nakłada 1 zwiększenia zadawanych obrażeń odpowiadającego tej Afiniczności\n- przy odpowiednim Rezonansie 5+ dodatkowo nakłada 1 zwiększenia Mocy Umiejętności odpowiadającego tej Afiniczności
624. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [EndSkill] 체력 비율이 가장 낮은 아군 2명의 체력을 최대 체력의 18% 만큼 회복\n- (가장 높은 공명 수 - 2)만큼 회복 대상 증가 (최대 3)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 2 allies with the lowest HP percentages for 18% HP of their max HP\n- Heal (highest Reson. - 2) more allies (max 3)
   PL: [EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o 18% ich Maks. HP\n- leczy (najwyższy Rezonans - 2) dodatkowych sojuszników (maks. 3)
625. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 3)\n[WhenUse] 아군 4 + (가장 높은 공명 수)명에게 해당 공명 속성의 피해량 증가와 위력 증가를 1 부여\n- 해당 공명이 4 이상이면, 해당 속성 피해량 증가를 1 추가 부여\n- 해당 공명이 5 이상이면, 해당 속성 위력 증가를 1 추가 부여\n- 해당 공명이 완전 공명 6 이상이면, 다음 턴에도 동일한 효과 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=4].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] Gain (# of highest Reson. - 2) Atk Weight (Max 3)\n[WhenUse] Apply 1 '(Corresponding Sin Affinity) Damage Up' and '1 (Corresponding Sin Affinity) Power Up' to (4 + # of highest Reson.) allies.\n- At 4+ Corresponding Reson., apply 1 additional '(Corresponding Sin Affinity) Damage Up'\n- At 5+ Corresponding Reson., apply 1 additional '(Corresponding Sin Affinity) Power Up'\n- At 6+ Corresponding A-Reson., apply the above effects next turn as well
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 3)\n[WhenUse] nakłada 1 zwiększenia zadawanych obrażeń i 1 zwiększenia Mocy Umiejętności odpowiadającego Afiniczności tego Rezonansu na (4 + najwyższy Rezonans) sojuszników\n- przy odpowiednim Rezonansie 4+ dodatkowo nakłada 1 zwiększenia zadawanych obrażeń odpowiadającego tej Afiniczności\n- przy odpowiednim Rezonansie 5+ dodatkowo nakłada 1 zwiększenia Mocy Umiejętności odpowiadającego tej Afiniczności\n- przy odpowiednim Rezonansie Absolutnym 6+ nakłada te same efekty następnej tury
626. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [EndSkill] 체력 비율이 가장 낮은 아군 4명의 체력을 최대 체력의 22% 만큼 회복\n- (가장 높은 공명 수 - 2)만큼 회복 대상 증가 (최대 3)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 4 allies with the lowest HP percentages for 22% HP of their max HP\n- Heal (highest Reson. - 2) more allies (max 3)
   PL: [EndSkill] leczy 4 sojuszników z najniższym aktualnym procentem HP o 22% ich Maks. HP\n- leczy (najwyższy Rezonans - 2) dodatkowych sojuszników (maks. 3)
627. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 가시 화원
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=1].name ; dataList[id=2120521].levelList[level=3].name ; dataList[id=2120521].levelList[level=4].name
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 장미 표지판
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=1].abName ; dataList[id=2120521].levelList[level=3].abName ; dataList[id=2120521].levelList[level=4].abName
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 가장 높은 공명이 3 이상이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 3+ highest Reson., Atk Weight +1
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 3+ Waga Ataku +1
630. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AttackDmgDown] 1 부여. 다음 턴에 [Binding] 2 부여.
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgDown], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [AttackDmgDown]. Inflict 2 [Binding] next turn.
   PL: [OnSucceedAttack] nakłada 1 [AttackDmgDown]. następnej tury nakłada 2 [Binding].
631. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 가장 높은 공명 속성의 취약과 위력 감소를 1 부여\n- 해당 공명이 4 이상이면, 해당 속성 취약을 1 추가 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 'Fragility' and 1 'Power Down' for the Sin Affinity with the highest Reson. count\n- At 4+ Corresponding Reson., inflict 1 additional '(Corresponding Sin Affinity) Fragility'
   PL: [OnSucceedAttack] nakłada 1 Kruchości i 1 Redukcji Mocy odpowiadającej Grzechowi z najwyższym Rezonansem\n- przy odpowiednim Rezonansie 4+ dodatkowo nakłada 1 Kruchości odpowiadającej tej Afiniczności
632. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 2)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (highest Reson. - 2) Atk Weight (max 2)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 2)
633. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AttackDmgDown] 1 부여. 다음 턴에 [Binding] 2 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgDown], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [AttackDmgDown]. Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [AttackDmgDown]. następnej tury nakłada 2 [Binding]
634. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 가장 높은 공명 속성의 취약과 위력 감소를 1 부여\n- 해당 공명이 4 이상이면, 해당 속성 취약을 1 추가 부여\n- 해당 공명이 5 이상이면, 해당 속성 위력 감소를 1 추가 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 'Fragility' and 1 'Power Down' for the Sin Affinity with the highest Resonance count\n- At 4+ Corresponding Reson., inflict 1 additional '(Corresponding Sin Affinity) Fragility'\n- At 5+ Corresponding Reson., inflict 1 additional '(Corresponding Sin Affinity) Power Down'
   PL: [OnSucceedAttack] nakłada 1 Kruchości i 1 Redukcji Mocy odpowiadającej Grzechowi z najwyższym Rezonansem\n- przy odpowiednim Rezonansie 4+ dodatkowo nakłada 1 Kruchości odpowiadającej tej Afiniczności\n- przy odpowiednim Rezonansie 5+ dodatkowo nakłada 1 Redukcji Mocy odpowiadającej tej Afiniczności
635. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (가장 높은 공명 수 - 2)만큼 공격 가중치 증가 (최대 3)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (highest Reson. - 2) Atk Weight (max 3)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans - 2) Wagi Ataku (maks. 3)
636. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 가장 높은 공명 속성의 취약과 위력 감소를 1 부여\n- 해당 공명이 4 이상이면, 해당 속성 취약을 1 추가 부여\n- 해당 공명이 5 이상이면, 해당 속성 위력 감소를 1 추가 부여\n- 해당 공명이 완전 공명 6 이상이면, 다음 턴에도 동일한 효과 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 'Fragility' and 1 'Power Down' for the Sin Affinity with the highest Resonance count\n- At 4+ Corresponding Reson., inflict 1 additional '(Corresponding Sin Affinity) Fragility'\n- At 5+ Corresponding Reson., inflict 1 additional '(Corresponding Sin Affinity) Power Down'\n- At 6+ Corresponding A-Reson., apply the above effects next turn as well
   PL: [OnSucceedAttack] nakłada 1 Kruchości i 1 Redukcji Mocy odpowiadającej Grzechowi z najwyższą liczbą Rezonansu\n- przy odpowiednim Rezonansie 4+ dodatkowo nakłada 1 Kruchości odpowiadającej tej Afiniczności\n- przy odpowiednim Rezonansie 5+ dodatkowo nakłada 1 Redukcji Mocy odpowiadającej tej Afiniczności\n- przy odpowiednim Rezonansie Absolutnym 6+ nakłada te same efekty następnej tury
637. [Pasywka E.G.O — nazwa] 장미 면류관
   źródło: Passive_Ego.json :: dataList[id=2120511].name
   limit: do 40 znaków
   EN: Crown of Roses
   PL: Korona z Róż
638. [Pasywka E.G.O — opis] 턴 시작 시, 무작위 적 1명에게 파열 위력 2 부여.(집중 전투인 경우, 모든 부위에 부여)\n완전 공명을 발동하였다면 전투 시작 시, 모든 적에게 파열 위력 2 부여.
   źródło: Passive_Ego.json :: dataList[id=2120511].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Turn Start: Inflict 2 [Burst] Potency on a random enemy(In Focused Encounters, all parts)\nWhen activating Absolute Resonance, inflict 2 [Burst] Potency on all enemies at Combat Start
   PL: na początku tury nakłada 2 Siły [Burst] na 1 losowego wroga.(w walkach skupionych na wszystkie Części)\njeżeli wywołano Rezonans Absolutny, na początku walki nakłada 2 Siły [Burst] na wszystkich wrogów.

## E.G.O [21206] Bygone Days (지난 날) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21206`

639. [Karta E.G.O — nazwa] 지난 날
   źródło: Egos.json :: dataList[id=21206].name
   limit: do 40 znaków
   EN: Bygone Days
   PL: Dni Przeszłe
640. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21206].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 지난 날
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120611].levelList[level=1].name ; dataList[id=2120611].levelList[level=3].name ; dataList[id=2120611].levelList[level=4].name
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 어느 날의 초상
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120611].levelList[level=1].abName ; dataList[id=2120611].levelList[level=3].abName ; dataList[id=2120611].levelList[level=4].abName
   limit: do 40 znaków
   EN: Portrait of a Certain Day
   PL: Portret Pewnego Dnia
643. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 자신과 자신을 제외한 정신력이 가장 낮은 아군 2명의 정신력 10 회복\n- 대상이 사망하지 않았다면, 대상의 [Sinking] 횟수를 5 소모하고, 대상의 [Sinking] 위력만큼 회복 대상의 정신력 추가 회복 (최대 회복량 : 20)\n- 대상이 사망했다면, 무작위 적 2명에게 [Sinking] 3 부여 (집중 전투인 경우, 무작위 부위에 부여)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120611].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [Sinking]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Sinking] = 침잠 / Sinking
   EN: [EndSkill] Heal 10 SP to self and 2 other allies with the least SP\n- If target survives this attack, consume 5 [Sinking] Count on target, then heal additional SP(to self & affected allies) equal to [Sinking] Potency on target (Max SP heal: 20)\n- If target is defeated, inflict 3 [Sinking] on 2 random enemies (For Focused Encounters, random Parts)
   PL: [EndSkill] odzyskuje 10 SP dla siebie i 2 sojuszników z najniższym SP innych niż ta jednostka\n- jeżeli cel przeżył ten atak, zużywa 5 Licznika [Sinking] celu i dodatkowo leczy SP (siebie oraz wskazanych sojuszników) o wartość Siły [Sinking] celu (maks. leczenia SP: 20)\n- jeżeli cel został pokonany, nakłada 3 [Sinking] na 2 losowych wrogów (w walkach skupionych na losowe Części)
644. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 자신과 자신을 제외한 정신력이 가장 낮은 아군 2명의 정신력 <style="highlight">12</style> 회복\n- 대상이 사망하지 않았다면, 대상의 [Sinking] 횟수를 5 소모하고, 대상의 [Sinking] 위력만큼 회복 대상의 정신력 추가 회복 (최대 회복량 : 20)\n- 대상이 사망했다면, 무작위 적 2명에게 [Sinking] 3, <style="highlight">[Curse] 1</style> 부여 (집중 전투인 경우, 무작위 부위에 부여)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120611].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [Sinking], [Curse]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Sinking] = 침잠 / Sinking; [Curse] = 저주 / Curse
   EN: [EndSkill] Heal <style="highlight">12</style> SP to self and 2 other allies with the least SP\n- If target survives this attack, consume 5 [Sinking] Count on target, then heal additional SP(to self & affected allies) equal to [Sinking] Potency on target (Max SP heal: 20)\n- If target is defeated, inflict 3 [Sinking] and <style="highlight">1 [Curse]</style> on 2 random enemies (For Focused Encounters, random Parts)
   PL: [EndSkill] odzyskuje <style="highlight">12</style> SP dla siebie i 2 sojuszników z najniższym SP innych niż ta jednostka\n- jeżeli cel przeżył ten atak, zużywa 5 Licznika [Sinking] celu i dodatkowo leczy SP (siebie oraz wskazanych sojuszników) o wartość Siły [Sinking] celu (maks. leczenia SP: 20)\n- jeżeli cel został pokonany, nakłada 3 [Sinking] i <style="highlight">1 [Curse]</style> na 2 losowych wrogów (w walkach skupionych na losowe Części)
645. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [EndSkill] 자신과 자신을 제외한 정신력이 가장 낮은 아군 2명의 정신력 <style="highlight">15</style> 회복\n- 대상이 사망하지 않았다면, 대상의 [Sinking] 횟수를 <style="highlight">3</style> 소모하고, 대상의 [Sinking] 위력만큼 회복 대상의 정신력 추가 회복 (최대 회복량 : 20)\n- 대상이 사망했다면, 무작위 적 <style="highlight">3</style> 명에게 [Sinking] 3, [Curse] 1 부여 (집중 전투인 경우, 무작위 부위에 부여)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120611].levelList[level=4].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [Sinking], [Curse]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Sinking] = 침잠 / Sinking; [Curse] = 저주 / Curse
   EN: [EndSkill] Heal <style="highlight">15</style> SP to self and 2 other allies with the least SP\n- If target survives this attack, consume <style="highlight">3</style> [Sinking] Count on target, then heal additional SP(to self & affected allies) equal to [Sinking] Potency on target (Max SP heal: 20)\n- If target is defeated, inflict 3 [Sinking] and 1 [Curse] on <style="highlight">3</style> random enemies (For Focused Encounters, random Parts)
   PL: [EndSkill] odzyskuje <style="highlight">15</style> SP dla siebie i 2 sojuszników z najniższym SP innych niż ta jednostka\n- jeżeli cel przeżył ten atak, zużywa <style="highlight">3</style> Licznika [Sinking] celu i dodatkowo leczy SP (siebie oraz wskazanych sojuszników) o wartość Siły [Sinking] celu (maks. leczenia SP: 20)\n- jeżeli cel został pokonany, nakłada 3 [Sinking] i 1 [Curse] na <style="highlight">3</style> losowych wrogów (w walkach skupionych na losowe Części)
646. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 지난 날
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=1].name ; dataList[id=2120621].levelList[level=3].name ; dataList[id=2120621].levelList[level=4].name
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 어느 날의 초상
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=1].abName ; dataList[id=2120621].levelList[level=3].abName ; dataList[id=2120621].levelList[level=4].abName
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=1].desc ; dataList[id=2120621].levelList[level=3].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AzureTakeDamageUp] 2 부여. 우울 공명이 3 이상이면 추가 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] Inflict 2 [AzureTakeDamageUp]. At 3+ Gloom Reson., inflict 1 additional [AzureTakeDamageUp]
   PL: [OnSucceedAttack] nakłada 2 [AzureTakeDamageUp]. przy Rezonansie Posępności 3+ dodatkowo nakłada 1 [AzureTakeDamageUp]
650. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2120621].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2120621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
651. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Curse] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 533 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AzureTakeDamageUp] 2 부여. 우울 공명 3 당 추가 1 부여 (최대 2)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] Inflict 2 [AzureTakeDamageUp]. Inflict 1 additional [AzureTakeDamageUp] for every 3 Gloom Reson. (max 2)
   PL: [OnSucceedAttack] nakłada 2 [AzureTakeDamageUp]. dodatkowo nakłada 1 [AzureTakeDamageUp] za każde 3 Rezonansu Posępności (maks. 2)
653. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Curse] 2 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상에게 [Curse]가 있으면 피해량 +50%
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Curse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Curse] = 저주 / Curse
   EN: [CantIdentify]\nTargets randomly\nIf target has [Curse], deal +50% damage
   PL: [CantIdentify]\nAtakuje losowy cel\njeżeli cel ma [Curse], zadaje +50% obrażeń
655. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AzureTakeDamageUp] 2 부여. 우울 공명 2 당 추가 1 부여 (최대 2)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] Inflict 2 [AzureTakeDamageUp]. Inflict 1 additional [AzureTakeDamageUp] for every 2 Gloom Reson. (max 2)
   PL: [OnSucceedAttack] nakłada 2 [AzureTakeDamageUp]. dodatkowo nakłada 1 [AzureTakeDamageUp] za każde 2 Rezonansu Posępności (maks. 2)
656. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Curse] 3 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120621].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 3 [Curse]
   PL: [OnSucceedAttack] nakłada 3 [Curse]
657. [Pasywka E.G.O — nazwa] 되돌릴 수 있다면...
   źródło: Passive_Ego.json :: dataList[id=2120611].name
   limit: do 40 znaków
   EN: If I Could Go Back...
   PL: Gdybym Mógł Wrócić...
658. [Pasywka E.G.O — opis] 자신의 공격 종료 시 대상이 사망한 경우, 가장 수량이 적은 E.G.O. 자원 1개 획득.\n대상의 ([Sinking] 위력 + 횟수) 5 당 추가로 1개 획득 (최대 3)\n(가장 수량이 적은 E.G.O 자원이 2개 이상이면, 부족한 자원 중 무작위로 획득)
   źródło: Passive_Ego.json :: dataList[id=2120611].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Attack End: If the target is defeated after this unit's attack, gain 1 E.G.O resource for the least-owned E.G.O resource.\nGain 1 additional E.G.O resource for every 5 ([Sinking] Potency + Count) (max 3)\n(If there are 2 or more "least-owned E.G.O resource", select 1 of those Affinities at random to gain an E.G.O resource)
   PL: na koniec ataku tej jednostki, jeżeli cel został pokonany, zyskuje 1 zasobu najmniej posiadanej Afiniczności E.G.O.\ndodatkowo zyskuje 1 zasobu za każde 5 (Siła [Sinking] celu + Licznik) (maks. 3)\n(jeżeli najmniej posiadanych Afiniczności E.G.O jest 2 lub więcej, zyskuje losowo zasób 1 z nich)

## E.G.O [21207] Solemn Lament (엄숙한 애도) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21207`

659. [Karta E.G.O — nazwa] 엄숙한 애도
   źródło: Egos.json :: dataList[id=21207].name
   limit: do 40 znaków
   EN: Solemn Lament
   PL: Uroczysty Lament
660. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21207].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 엄숙한 애도
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].name ; dataList[id=2120711].levelList[level=3].name ; dataList[id=2120711].levelList[level=4].name
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 죽은 나비들의 장례
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].abName ; dataList[id=2120711].levelList[level=3].abName ; dataList[id=2120711].levelList[level=4].abName
   limit: do 50 znaków
   EN: Funeral of the Dead Butterflies
   PL: Pogrzeb Martwych Motyli
663. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 이 스킬의 코인을 굴릴 때, 공격 대상 중에 하나를 무작위로 선택해 공격.\n- 첫 코인은 반드시 메인 공격 대상에게 적중함.\n- 모든 적중시 효과, 해당 코인의 피해는 위 효과에서 선택된 공격 대상에게만 적용됨.\n이 스킬의 효과로 [SinkingWhite] 부여시 앞면이 나올 확률로 죽은나비를 부여. 부여하지 않은 경우, 산나비를 부여. ([SinkingWhite] 1당 개별 판정)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n, [SinkingWhite]
   znaczenie tagów: [SinkingWhite] = 나비 / Butterfly
   EN: When this Skill flips Coins, each Coin flips against a random enemy among its targets.\n- The first Coin always targets the main target\n- All 'On Hit' effects and all damage dealt by each Coin are inflicted only against the random target the Coin selected\nWhen inflicting [SinkingWhite] using this Skill's effects: (Chance to flip Heads)% chance to inflict The Departed. If this unit did not inflict The Departed, inflict The Living instead. (calculates every [SinkingWhite] Stack independently)
   PL: gdy ta Umiejętność rzuca Monety, każda Moneta trafia losowo wybranego wroga wśród celów ataku.\n- pierwsza Moneta zawsze trafia cel główny.\n- wszystkie efekty przy trafieniu i obrażenia danej Monety działają wyłącznie na losowo wybranego przez nią cel.\ngdy nakłada [SinkingWhite] efektami tej Umiejętności, z szansą równą szansie na Orła nakłada Odeszli. jeżeli nie nakłada Odeszli, nakłada zamiast tego Żywi. (osobne rozstrzygnięcie dla każdego 1 [SinkingWhite])
664. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 무작위 [SinkingWhite] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2120711].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120711].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 1 random [SinkingWhite]
   PL: [OnSucceedAttack] nakłada 1 losowego [SinkingWhite]
665. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 무작위 [SinkingWhite] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2120711].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2120711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 무작위 [SinkingWhite] 1 ~ 2부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 1~2 random [SinkingWhite]
   PL: [OnSucceedAttack] nakłada 1 ~ 2 losowych [SinkingWhite]
667. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 2 ~ 6 감소
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lose 2~6 SP
   PL: [OnSucceedAttack] traci 2 ~ 6 SP
668. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력이 0 이상이면, 이 코인 재사용 (스킬 당 최대 5회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 0+ SP, Reuse this Coin (5 times max per Skill)
   PL: [OnSucceedAttack] przy SP 0 lub wyższym, ponownie używa tej Monety (maks. 5 razy na Umiejętność)
669. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 이 스킬의 코인을 굴릴 때, 공격 대상 중에 하나를 무작위로 선택해 공격.\n- 첫 코인은 반드시 메인 공격 대상에게 적중함.\n- 모든 적중시 효과, 해당 코인의 피해는 위 효과에서 선택된 공격 대상에게만 적용됨.\n이 스킬의 효과로 [SinkingWhite] 부여시 앞면이 나올 확률로 죽은나비를 부여. 부여하지 않은 경우, 산나비를 부여. ([SinkingWhite] 1당 개별 판정)\n<style="highlight">[EndSkill] (적중한 3코인 수 x 2)만큼 정신력 회복</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=3].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [SinkingWhite], [EndSkill]
   znaczenie tagów: [SinkingWhite] = 나비 / Butterfly; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When this Skill flips Coins, each Coin flips against a random enemy among its targets.\n- The first Coin always targets the main target\n- All 'On Hit' effects and all damage dealt by each Coin are inflicted only against the random target the Coin selected\nWhen inflicting [SinkingWhite] using this Skill's effects: (Chance to flip Heads)% chance to inflict The Departed. If this unit did not inflict The Departed, inflict The Living instead. (calculates every [SinkingWhite] Stack independently)\n<style="highlight">[EndSkill] Heal (# of Coin 3 hits x 2) SP</style>
   PL: gdy ta Umiejętność rzuca Monety, każda Moneta trafia losowo wybranego wroga wśród celów ataku.\n- pierwsza Moneta zawsze trafia cel główny.\n- wszystkie efekty przy trafieniu i obrażenia danej Monety działają wyłącznie na losowo wybranego przez nią cel.\ngdy nakłada [SinkingWhite] efektami tej Umiejętności, z szansą równą szansie na Orła nakłada Odeszli. jeżeli nie nakłada Odeszli, nakłada zamiast tego Żywi. (osobne rozstrzygnięcie dla każdego 1 [SinkingWhite])\n<style="highlight">[EndSkill] odzyskuje (liczba trafień 3. Monety x 2) SP</style>
670. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 무작위 [SinkingWhite] 1 ~ 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2120711].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 1~2 random [SinkingWhite]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 1 ~ 2 losowych [SinkingWhite]<style="highlight"></style>
671. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 2 ~ 6 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2120711].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lose 2~6 SP<style="highlight"></style>
   PL: [OnSucceedAttack] traci 2 ~ 6 SP<style="highlight"></style>
672. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력이 0 이상이면, 이 코인 재사용 (스킬 당 최대 5회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2120711].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 0+ SP, Reuse this Coin (5 times max per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] przy SP 0 lub wyższym, ponownie używa tej Monety (maks. 5 razy na Umiejętność)<style="highlight"></style>
673. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 이 스킬의 코인을 굴릴 때, 공격 대상 중에 하나를 무작위로 선택해 공격.\n- 첫 코인은 반드시 메인 공격 대상에게 적중함.\n- 모든 적중시 효과, 해당 코인의 피해는 위 효과에서 선택된 공격 대상에게만 적용됨.\n이 스킬의 효과로 [SinkingWhite] 부여시 앞면이 나올 확률로 죽은나비를 부여. 부여하지 않은 경우, 산나비를 부여. ([SinkingWhite] 1당 개별 판정)\n[EndSkill] <style="highlight">(적중한 3코인 수 x 3)</style>만큼 정신력 회복
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120711].levelList[level=4].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [SinkingWhite], [EndSkill]
   znaczenie tagów: [SinkingWhite] = 나비 / Butterfly; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When this Skill flips Coins, each Coin flips against a random enemy among its targets.\n- The first Coin always targets the main target\n- All 'On Hit' effects and all damage dealt by each Coin are inflicted only against the random target the Coin selected\nWhen inflicting [SinkingWhite] using this Skill's effects: (Chance to flip Heads)% chance to inflict The Departed. If this unit did not inflict The Departed, inflict The Living instead. (calculates every [SinkingWhite] Stack independently)\n[EndSkill] Heal <style="highlight">(# of Coin 3 hits x 3)</style> SP
   PL: gdy ta Umiejętność rzuca Monety, każda Moneta trafia losowo wybranego wroga wśród celów ataku.\n- pierwsza Moneta zawsze trafia cel główny.\n- wszystkie efekty przy trafieniu i obrażenia danej Monety działają wyłącznie na losowo wybranego przez nią cel.\ngdy nakłada [SinkingWhite] efektami tej Umiejętności, z szansą równą szansie na Orła nakłada Odeszli. jeżeli nie nakłada Odeszli, nakłada zamiast tego Żywi. (osobne rozstrzygnięcie dla każdego 1 [SinkingWhite])\n[EndSkill] odzyskuje <style="highlight">(liczba trafień 3. Monety x 3)</style> SP
674. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 엄숙한 애도
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=1].name ; dataList[id=2120721].levelList[level=3].name ; dataList[id=2120721].levelList[level=4].name
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 죽은 나비들의 장례
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=1].abName ; dataList[id=2120721].levelList[level=3].abName ; dataList[id=2120721].levelList[level=4].abName
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 정신력이 0 미만이면, 정신력이 낮을수록 피해량이 증가 (최대 45%)\n정신력이 없는 대상에게는 [Sinking] 2당 피해량 1% 증가 (최대 45%)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Sinking]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking
   EN: [CantIdentify]\nTargets randomly\nIf target has less than 0 SP, deal more damage the further their SP value is from 0 (+1% damage for every missing SP, max 45%)\nFor targets that are Non-SP Units, deal +1% damage for every 2 [Sinking] on target (max 45%)
   PL: [CantIdentify]\nAtakuje losowy cel\njeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)\nw przypadku celów będących jednostkami bez SP, zadaje +1% obrażeń za każde 2 [Sinking] na celu (maks. 45%)
677. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SinkingWhite](산나비) 4 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 4 [SinkingWhite](The Living)
   PL: [OnSucceedAttack] nakłada 4 [SinkingWhite](Żywi)
678. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [SinkingWhite](죽은나비) 4 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 4 [SinkingWhite](The Departed)
   PL: [OnSucceedAttack] nakłada 4 [SinkingWhite](Odeszli)
679. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 정신력이 0 미만이면, 정신력이 낮을수록 피해량이 증가 (최대 45%)\n정신력이 없는 대상에게는 [Sinking] 2당 피해량 1% 증가 (최대 45%)\n<style="highlight">[EnemyKill] 정신력 5 회복</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=3].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Sinking], [EnemyKill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking; [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [CantIdentify]\nTargets randomly\nIf target has less than 0 SP, deal more damage the further their SP value is from 0 (+1% damage for every missing SP, max 45%)\nFor targets that are Non-SP Units, deal +1% damage for every 2 [Sinking] on target (max 45%)\n<style="highlight">[EnemyKill] Heal 5 SP</style>
   PL: [CantIdentify]\nAtakuje losowy cel\njeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)\nw przypadku celów będących jednostkami bez SP, zadaje +1% obrażeń za każde 2 [Sinking] na celu (maks. 45%)\n<style="highlight">[EnemyKill] odzyskuje 5 SP</style>
680. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SinkingWhite](산나비) 4 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 4 [SinkingWhite](The Living)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 4 [SinkingWhite](Żywi)<style="highlight"></style>
681. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [SinkingWhite](죽은나비) 4 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 4 [SinkingWhite](The Departed)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 4 [SinkingWhite](Odeszli)<style="highlight"></style>
682. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 횟수 3 증가</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttack] Inflict +3 [Sinking] Count</style>
   PL: <style="highlight">[OnSucceedAttack] nakłada +3 Licznika [Sinking]</style>
683. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 정신력이 0 미만이면, 정신력이 낮을수록 피해량이 증가 (최대 45%)\n정신력이 없는 대상에게는 [Sinking] 2당 피해량 1% 증가 (최대 45%)\n[EnemyKill] 정신력 5 회복<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Sinking], [EnemyKill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking; [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [CantIdentify]\nTargets randomly\nIf target has less than 0 SP, deal more damage the further their SP value is from 0 (+1% damage for every missing SP, max 45%)\nFor targets that are Non-SP Units, deal +1% damage for every 2 [Sinking] on target (max 45%)\n[EnemyKill] Heal 5 SP<style="highlight"></style>
   PL: [CantIdentify]\nAtakuje losowy cel\njeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)\nw przypadku celów będących jednostkami bez SP, zadaje +1% obrażeń za każde 2 [Sinking] na celu (maks. 45%)\n[EnemyKill] odzyskuje 5 SP<style="highlight"></style>
684. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SinkingWhite](산나비) 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 5 [SinkingWhite](The Living)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 5 [SinkingWhite](Żywi)<style="highlight"></style>
685. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [SinkingWhite](죽은나비) 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict 5 [SinkingWhite](The Departed)<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 5 [SinkingWhite](Odeszli)<style="highlight"></style>
686. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] o 3<style="highlight"></style>
687. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 4 — opis] <style="highlight">[OnSucceedAttack] 대상의 체력이 50% 이하면, 대상의 모든 [SinkingWhite]만큼 우울 피해\n- 산나비와 죽은나비의 합으로 계산</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120721].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: <style="highlight">[OnSucceedAttack] If target has 50%- HP, inflict Gloom Damage equal to "All" [SinkingWhite] values on target\n- "All" = the sum of both The Living and The Departed on target</style>
   PL: <style="highlight">[OnSucceedAttack] jeżeli HP celu wynosi 50% lub mniej, zadaje obrażenia Posępności równe wszystkim wartościom [SinkingWhite] na celu\n- obliczane jako suma Żywych i Odeszłych</style>
688. [Pasywka E.G.O — nazwa] 애도
   źródło: Passive_Ego.json :: dataList[id=2120711].name
   limit: do 40 znaków
   EN: Lament
   PL: Kondolencje
689. [Pasywka E.G.O — opis] 턴 종료시 자신이 부정적인 효과를 보유하고 있으면, 다음 턴에 [Enhancement] 1 얻음\n패닉 상태인 대상이나 E.G.O 침식 상태인 대상을 공격할 때, 피해량 + 15%
   źródło: Passive_Ego.json :: dataList[id=2120711].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn End: if this unit has a negative effect, gain 1 [Enhancement] next turn\nWhen attacking targets that are either in Panic or in E.G.O Corrosion: deal +15% damage
   PL: na koniec tury, jeżeli ta jednostka ma negatywny efekt, następnej tury zyskuje 1 [Enhancement]\nprzy atakowaniu celów w panice lub w erosji E.G.O, zadaje +15% obrażeń

## E.G.O [21208] Christmas Nightmare (크리스마스 악몽) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21208`

690. [Karta E.G.O — nazwa] 크리스마스 악몽
   źródło: Egos.json :: dataList[id=21208].name
   limit: do 40 znaków
   EN: Christmas Nightmare
   PL: Bożonarodzeniowy Koszmar
691. [Karta E.G.O — opis] 그레고르의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21208].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 크리스마스 악몽
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].name ; dataList[id=2120811].levelList[level=3].name ; dataList[id=2120811].levelList[level=4].name
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 아늑한 침대
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].abName ; dataList[id=2120811].levelList[level=3].abName ; dataList[id=2120811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Cozy Bed
   PL: Przytulne Łóżko
694. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 자신의 체력이 최대치면, 턴 종료시 정신력을 10 회복하고 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Enhancement]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndSkill] At max HP, heal 10 SP at Turn End and gain 1 [Enhancement] next turn
   PL: [EndSkill] przy pełnym HP, na koniec tury odzyskuje 10 SP i następnej tury zyskuje 1 [Enhancement]
695. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2120811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2120811].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2120811].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] Nakłada 4 [Sinking]
698. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태면 다음 턴에 [Reduction] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] If target is in Staggered, Low Morale, or Panic states, inflict 1 [Reduction] next turn
   PL: [OnSucceedAttack] jeżeli cel jest Oszołomiony, w Niskim Moralu lub w Panice, następnej tury nakłada 1 [Reduction]
699. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">대상의 정신력이 0 미만이면, 0 미만의 정신력 1 당 피해량 +1% (최대 45%)</style>\n[EndSkill] 자신의 체력이 최대치면, 턴 종료시 정신력을 10 회복하고 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=3].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [Enhancement]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: <style="highlight">If target has less than 0 SP, deal +1% damage for every SP value below 0 (max 45%)</style>\n[EndSkill] At max HP, heal 10 SP at Turn End and gain 1 [Enhancement] next turn
   PL: <style="highlight">jeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)</style>\n[EndSkill] przy pełnym HP, na koniec tury odzyskuje 10 SP i następnej tury zyskuje 1 [Enhancement]
700. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 잃은 체력의 (2 + 최대 공명 수)% 만큼 회복 (스킬 당 최대 30%)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal (2 + highest Reson.)% of the missing HP on self (max 30% per Skill)
   PL: [OnSucceedAttack] leczy własne brakujące HP o (2 + najwyższy Rezonans)% (maks. 30% na Umiejętność)
701. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2120811].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 4 [Sinking]<style="highlight"></style>
702. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태면 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] If target is in Staggered, Low Morale, or Panic states, inflict 1 [Reduction] next turn<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli cel jest Oszołomiony, w Niskim Moralu lub w Panice, następnej tury nakłada 1 [Reduction]<style="highlight"></style>
703. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 정신력이 0 미만이면, 0 미만의 정신력 1 당 피해량 +1% (최대 45%)\n[EndSkill] 자신의 체력이 최대치면, 턴 종료시 정신력을 <style="highlight">15</style> 회복하고 다음 턴에 [Enhancement] 1 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [Enhancement]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: If target has less than 0 SP, deal +1% damage for every SP value below 0 (max 45%)\n[EndSkill] At max HP, heal <style="highlight">15</style> SP at Turn End and gain 1 [Enhancement] next turn<style="highlight"></style>
   PL: jeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)\n[EndSkill] przy pełnym HP, na koniec tury odzyskuje <style="highlight">15</style> SP i następnej tury zyskuje 1 [Enhancement]<style="highlight"></style>
704. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 잃은 체력의 (<style="highlight">3</style> + 최대 공명 수)% 만큼 회복 (스킬 당 최대 30%)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal (<style="highlight">3</style> + highest Reson.)% of the missing HP on self (max 30% per Skill)
   PL: [OnSucceedAttack] leczy własne brakujące HP o (<style="highlight">3</style> + najwyższy Rezonans)% (maks. 30% na Umiejętność)
705. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태면 다음 턴에 [Reduction] 1, <style="highlight">가장 높은 공명 속성의 취약을 1</style> 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120811].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction], [TabExplain]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] If target is in Staggered, Low Morale, or Panic states, inflict 1 [Reduction] <style="highlight">and Fragility[TabExplain] against the Affinity of the highest Reson.</style> next turn
   PL: [OnSucceedAttack] jeżeli cel jest Oszołomiony, w Niskim Moralu lub w Panice, następnej tury nakłada 1 [Reduction] <style="highlight">i 1 Kruchości[TabExplain] odpowiadającej Afiniczności z najwyższym Rezonansem</style>
706. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 크리스마스 악몽
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].name ; dataList[id=2120821].levelList[level=3].name ; dataList[id=2120821].levelList[level=4].name
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 아늑한 침대
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].abName ; dataList[id=2120821].levelList[level=3].abName ; dataList[id=2120821].levelList[level=4].abName
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 체력 10 회복\n[EndSkill] 자신의 체력이 최대치면, 턴 종료시 정신력을 10 회복하고 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [EndSkill], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Heal 10 HP on self\n[EndSkill] At max HP, heal 10 SP at Turn End and gain 1 [Enhancement] next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] odzyskuje 10 HP\n[EndSkill] przy pełnym HP, na koniec tury odzyskuje 10 SP i następnej tury zyskuje 1 [Enhancement]
709. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2120821].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2120821].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2120821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태면 다음 턴에 [Reduction] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">대상의 정신력이 0 미만이면, 0 미만의 정신력 1 당 피해량 +1% (최대 45%)</style>\n[BeforeAttack] 자신의 체력 10 회복\n[EndSkill] 자신의 체력이 최대치면, 턴 종료시 정신력을 <style="highlight">15</style> 회복하고 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=3].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [EndSkill], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">If target has less than 0 SP, deal +1% damage for every SP value below 0 (max 45%)</style>\n[BeforeAttack] Heal 10 HP on self\n[EndSkill] At max HP, heal <style="highlight">15</style> SP at Turn End and gain 1 [Enhancement] next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">jeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)</style>\n[BeforeAttack] odzyskuje 10 HP\n[EndSkill] przy pełnym HP, na koniec tury odzyskuje <style="highlight">15</style> SP i następnej tury zyskuje 1 [Enhancement]
714. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 잃은 체력의 (2 + 최대 공명 수)% 만큼 회복 (스킬 당 최대 30%)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal (2 + highest Reson.)% of the missing HP (max 30% per Skill)
   PL: [OnSucceedAttack] leczy własne brakujące HP o (2 + najwyższy Rezonans)% (maks. 30% na Umiejętność)
715. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2120821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태면 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 702 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n대상의 정신력이 0 미만이면, 0 미만의 정신력 1 당 피해량 +1% (최대 45%)\n[BeforeAttack] 자신의 체력 10 회복\n[EndSkill] 자신의 체력이 최대치면, 턴 종료시 정신력을 <style="highlight">20</style> 회복하고 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [EndSkill], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\nIf target has less than 0 SP, deal +1% damage for every SP value below 0 (max 45%)\n[BeforeAttack] Heal 10 HP on self\n[EndSkill] At max HP, heal <style="highlight">20</style> SP at Turn End and gain 1 [Enhancement] next turn
   PL: [CantIdentify]\nAtakuje losowy cel\njeżeli SP celu jest niższe niż 0, zadaje +1% obrażeń za każdy 1 SP poniżej 0 (maks. 45%)\n[BeforeAttack] odzyskuje 10 HP\n[EndSkill] przy pełnym HP, na koniec tury odzyskuje <style="highlight">20</style> SP i następnej tury zyskuje 1 [Enhancement]
718. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 잃은 체력의 (<style="highlight">3</style> + 최대 공명 수)% 만큼 회복 (스킬 당 최대 30%)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 704 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태면 다음 턴에 [Reduction] 1, <style="highlight">가장 높은 공명 속성의 취약을 2</style> 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120821].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction], [TabExplain]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] If target is in Staggered, Low Morale, or Panic states, inflict 1 [Reduction] <style="highlight">and 2 Fragility[TabExplain] against the Affinity of the highest Reson.</style> next turn
   PL: [OnSucceedAttack] jeżeli cel jest Oszołomiony, w Niskim Moralu lub w Panice, następnej tury nakłada 1 [Reduction] <style="highlight">i 2 Kruchości[TabExplain] odpowiadającej Afiniczności z najwyższym Rezonansem</style>
720. [Pasywka E.G.O — nazwa] 잠들지 못하는 밤
   źródło: Passive_Ego.json :: dataList[id=2120811].name
   limit: do 40 znaków
   EN: Insomniac Night
   PL: Noc bez Snu
721. [Pasywka E.G.O — opis] 전투 시작시 흐트러짐, 사기저하, 패닉 상태인 적의 수만큼 모든 적에게 각각 [AttackDown] 1 또는 [DefenseDown] 1 부여. (턴 당 최대 2회)\n- 동일한 효과를 갖는 E.G.O 기프트와 중첩하여 발동되지 않음.
   źródło: Passive_Ego.json :: dataList[id=2120811].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDown], [DefenseDown]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Combat Start: against all enemies, inflict 1 [AttackDown] or 1 [DefenseDown] to all enemies (# of enemies in Staggered, Low Morale, or Panic states) times. (2 times per turn)\n- Effect does not stack with E.G.O Gifts with the same effect.
   PL: na początku walki nakłada na wszystkich wrogów po 1 [AttackDown] lub 1 [DefenseDown] (tyle razy, ile wynosi liczba wrogów Oszołamionych, w Niskim Moralu lub w Panice). (maks. 2 razy na turę)\n- nie kumuluje się z Prezentami E.G.O o tym samym efekcie.

## E.G.O [21209] Unbrilliant Glory (눈부시지 않은 영광) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21209`

722. [Karta E.G.O — nazwa] 눈부시지 않은 영광
   źródło: Egos.json :: dataList[id=21209].name
   limit: do 40 znaków
   EN: Unbrilliant Glory
   PL: Nieoślepiająca Chwała
723. [Karta E.G.O — opis] 그레고르 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21209].desc
   limit: do 120 znaków
   EN: Gregor’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Gregor
724. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 눈부시지 않은 영광 - 유수(流水)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120911].levelList[level=1].name ; dataList[id=2120911].levelList[level=3].name ; dataList[id=2120911].levelList[level=4].name
   limit: do 40 znaków
   EN: Unbrilliant Glory - Flowing
   PL: Nieoślepiająca Chwała - Przepływ
725. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 무에나
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120911].levelList[level=1].abName ; dataList[id=2120911].levelList[level=3].abName ; dataList[id=2120911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Młynar
   PL: Młynar
726. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [CantDuel]\n전투에서 처음 사용시 필요한 E.G.O 자원이 분노 1, 나태 2, 오만 1 감소\n[MlynarWaiting]이 1 이상이면, 눈부시지 않은 영광 - 광휘(光輝)로 발동됨\n이 스킬은 적에게 적중하지 않고, 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndSkill] 정신력 25 회복\n[EndSkill] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120911].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [MlynarWaiting], [EndSkill], [AttackUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantDuel]\nWhen used for the first time in an Encounter, consume 1 fewer Wrath, 2 fewer Sloth, and 1 fewer Pride E.G.O resources.\nAt 1+ [MlynarWaiting], activate <noparse>Unbrilliant Glory - Incandescence</noparse> instead\nThis Skill does not hit an enemy, does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndSkill] Heal 25 SP\n[EndSkill] Gain 1 [AttackUp] next turn
   PL: [CantDuel]\nprzy pierwszym użyciu w walce wymagane zasoby E.G.O są niższe o 1 Gniew, 2 Lenistwo i 1 Pychę\nprzy 1+ [MlynarWaiting] zamiast tego wywołuje „Nieoślepiająca Chwała - Żar"\nta Umiejętność nie trafia wrogów, nie uruchamia Umiejętności Obrony, a zewnętrzne efekty nie mogą ponownie jej użyć\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndSkill] odzyskuje 25 SP\n[EndSkill] następnej tury zyskuje 1 [AttackUp]
727. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [CantDuel]\n전투에서 처음 사용시 필요한 E.G.O 자원이 분노 1, 나태 2, 오만 1 감소\n[MlynarWaiting]이 1 이상이면, 눈부시지 않은 영광 - 광휘(光輝)로 발동됨\n이 스킬은 적에게 적중하지 않고, 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndSkill] 정신력 25 회복\n[EndSkill] 다음 턴에 [AttackUp] <style="highlight">2</style> 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120911].levelList[level=3].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [MlynarWaiting], [EndSkill], [AttackUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantDuel]\nWhen used for the first time in an Encounter, consume 1 fewer Wrath, 2 fewer Sloth, and 1 fewer Pride E.G.O resources.\nAt 1+ [MlynarWaiting], activate <noparse>Unbrilliant Glory - Incandescence</noparse> instead\nThis Skill does not hit an enemy, does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndSkill] Heal 25 SP\n[EndSkill] Gain <style="highlight">2</style> [AttackUp] next turn
   PL: [CantDuel]\nprzy pierwszym użyciu w walce wymagane zasoby E.G.O są niższe o 1 Gniew, 2 Lenistwo i 1 Pychę\nprzy 1+ [MlynarWaiting] zamiast tego wywołuje „Nieoślepiająca Chwała - Żar"\nta Umiejętność nie trafia wrogów, nie uruchamia Umiejętności Obrony, a zewnętrzne efekty nie mogą ponownie jej użyć\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndSkill] odzyskuje 25 SP\n[EndSkill] następnej tury zyskuje <style="highlight">2</style> [AttackUp]
728. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [CantDuel]\n전투에서 처음 사용시 필요한 E.G.O 자원이 분노 1, 나태 2, 오만 1 감소\n[MlynarWaiting]이 1 이상이면, 눈부시지 않은 영광 - 광휘(光輝)로 발동됨\n이 스킬은 적에게 적중하지 않고, 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndSkill] 정신력 25 회복\n[EndSkill] 다음 턴에 [AttackUp] 2, <style="highlight">[AttackDmgUp] 1</style> 얻음
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120911].levelList[level=4].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [MlynarWaiting], [EndSkill], [AttackUp], [AttackDmgUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantDuel]\nWhen used for the first time in an Encounter, consume 1 fewer Wrath, 2 fewer Sloth, and 1 fewer Pride E.G.O resources.\nAt 1+ [MlynarWaiting], activate <noparse>Unbrilliant Glory - Incandescence</noparse> instead\nThis Skill does not hit an enemy, does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndSkill] Heal 25 SP\n[EndSkill] Gain 2 [AttackUp] <style="highlight">and 1 [AttackDmgUp]</style> next turn
   PL: [CantDuel]\nprzy pierwszym użyciu w walce wymagane zasoby E.G.O są niższe o 1 Gniew, 2 Lenistwo i 1 Pychę\nprzy 1+ [MlynarWaiting] zamiast tego wywołuje „Nieoślepiająca Chwała - Żar"\nta Umiejętność nie trafia wrogów, nie uruchamia Umiejętności Obrony, a zewnętrzne efekty nie mogą ponownie jej użyć\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndSkill] odzyskuje 25 SP\n[EndSkill] następnej tury zyskuje 2 [AttackUp] <style="highlight">i 1 [AttackDmgUp]</style>
729. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 눈부시지 않은 영광 - 광휘(光輝)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].name ; dataList[id=2120912].levelList[level=3].name ; dataList[id=2120912].levelList[level=4].name
   limit: do 50 znaków
   EN: Unbrilliant Glory - Incandescence
   PL: Nieoślepiająca Chwała - Żar
730. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 무에나
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].abName ; dataList[id=2120912].levelList[level=3].abName ; dataList[id=2120912].levelList[level=4].abName
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[MlynarWaiting]이 40이면, 합 가능으로 변경됨\n[WhenUse] [MlynarWaiting]이 40이면, 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않고 합 위력 +20\n\n[BeforeAttack] [MlynarWaiting]을 전부 소모하고 아래 효과 적용 (모든 수치는 소수점 버림)\n- (소모한 수치 / 20) 만큼 사용한 E.G.O 자원을 1개씩 반환 (오만, 분노 순으로 반환)\n- (소모한 수치 / 10) 만큼 가중치 증가 (최대 4)\n- (소모한 수치 / 10) 만큼 [DefenseUp] 얻음 (턴당 1회)\n- 40 소모했다면, 4번째로 사용할 코인의 피해량 +50%, [Protection] 2 얻음 (턴당 1회)\n\n[BeforeAttack] 메인 타겟의 [Combustion]과 [Vibration]의 합 8 당 피해량 +5% (최대 25%)\n[EndSkill] 이 스킬의 피해로 흐트러졌거나 사망한 대상 1명당 정신력 5 회복 (최대 25)\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndBattle] 이 스킬로 [MlynarWaiting]을 40 소모하지 못했다면, 다음 턴에 조작 패널에서 가장 왼쪽의 스킬 슬롯 [Aggro] 4 증가 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].desc
   limit: do 1350 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [MlynarWaiting], [WhenUse], [BeforeAttack], [DefenseUp], [Protection], [Combustion], [Vibration], [EndSkill], [EndBattle], [Aggro]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Protection] = 보호 / Protection; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor …
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nAt 40 [MlynarWaiting], becomes Clashable\n[WhenUse] At 40 [MlynarWaiting], until this Skill ends, this unit cannot be Staggered from taking damage, and gains Clash Power +20\n\n[BeforeAttack] Consume all [MlynarWaiting] and gain the following effects(all of them rounded down):\n- For every (Stack consumed / 20), recuperate 1 E.G.O resource (in the following order: Pride, then Wrath)\n- For every (Stack consumed / 10), gain +1 Atk Weight (max 4)\n- For every (Stack consumed / 10), gain [DefenseUp] (once per turn)\n- If 40 Stack was consumed, the 4th Coin deals +50% damage, and this unit gains 2 [Protection] (once per turn)\n\n[BeforeAttack] Deal +5% damage for every 8 ([Combustion] + [Vibration]) on the main target (max 25%)\n[EndSkill] Heal 5 SP for every target that was Staggered or killed due to this Skill's damage (max 25)\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndBattle] If this Skill did not consume 40 [MlynarWaiting], the leftmost Skill Slot on the Dashboard gains +4 [Aggro] next turn (once per turn)
   PL: [CantDuel]\nzewnętrzne efekty nie mogą ponownie użyć tej Umiejętności\nprzy 40 [MlynarWaiting] staje się zdolna do Starcia\n[WhenUse] przy 40 [MlynarWaiting], do końca tej Umiejętności ta jednostka nie zostaje Oszołamiona przez obrażenia i zyskuje Moc Walki +20\n\n[BeforeAttack] zużywa całe [MlynarWaiting] i zyskuje następujące efekty (wszystkie wartości zaokrąglone w dół)\n- za każde (zużyta wartość / 20) odzyskuje po 1 zasobu E.G.O (w kolejności: Pycha, potem Gniew)\n- za każde (zużyta wartość / 10) zyskuje +1 Wagi Ataku (maks. 4)\n- za każde (zużyta wartość / 10) zyskuje [DefenseUp] (1 raz na turę)\n- jeżeli zużyto 40, 4. użyta Moneta zadaje +50% obrażeń, a ta jednostka zyskuje 2 [Protection] (1 raz na turę)\n\n[BeforeAttack] zadaje +5% obrażeń za każde 8 (suma [Combustion] i [Vibration]) na celu głównym (maks. 25%)\n[EndSkill] odzyskuje 5 SP za każdego celu Oszołamionego lub pokonanego obrażeniami tej Umiejętności (maks. 25)\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndBattle] jeżeli ta Umiejętność nie zużyła 40 [MlynarWaiting], następnej tury skrajna lewa Umiejętność na Pulpicie zyskuje 4 [Aggro] (1 raz na turę)
732. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] (소모한 [MlynarWaiting] 수치 / 10) - 1만큼 이 코인 재사용 (최대 3회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MlynarWaiting]
   znaczenie tagów: [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard
   EN: Reuse this Coin (([MlynarWaiting] Stack consumed / 10) - 1) times (3 times max)
   PL: ponownie używa tej Monety ((zużyta wartość [MlynarWaiting] / 10) - 1) razy (maks. 3 razy)
734. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
736. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] 마지막에 사용하는 코인이고, 대상의 [Vibration] 위력이 15 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [UnBrokenCoinOnSucceedAttack] If this is the final Coin, and if target has 15+ [Vibration] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli to ostatnia Moneta i Siła [Vibration] celu wynosi 15+, wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
737. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 6 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인을 4회 사용했으면, 대상의 [Vibration]만큼 나태 피해를 줌 (최대 5)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=1].coinlist[#0].coindescs[#5].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] If this Coin was used 4 times, deal Sloth damage equal to [Vibration] on target (max 5)
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta Moneta została użyta 4 razy, zadaje obrażenia Lenistwa równe wartości [Vibration] celu (maks. 5)
738. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[MlynarWaiting]이 40이면, 합 가능으로 변경됨\n[WhenUse] [MlynarWaiting]이 40이면, 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않고 합 위력 +20\n\n[BeforeAttack] [MlynarWaiting]을 전부 소모하고 아래 효과 적용 (모든 수치는 소수점 버림)\n- (소모한 수치 / 20) 만큼 사용한 E.G.O 자원을 1개씩 반환 (오만, 분노 순으로 반환)\n- (소모한 수치 / 10) 만큼 가중치 증가 (최대 4)\n- (소모한 수치 / 10) 만큼 [DefenseUp] 얻음 (턴당 1회)\n- 40 소모했다면, 4번째로 사용할 코인의 피해량 +<style="highlight">80</style>%, [Protection] 2 얻음 (턴당 1회)\n\n[BeforeAttack] 메인 타겟의 [Combustion]과 [Vibration]의 합 8 당 피해량 +5% (최대 25%)\n[EndSkill] 이 스킬의 피해로 흐트러졌거나 사망한 대상 1명당 정신력 5 회복 (최대 25)\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndBattle] 이 스킬로 [MlynarWaiting]을 40 소모하지 못했다면, 다음 턴에 조작 패널에서 가장 왼쪽의 스킬 슬롯 [Aggro] 4 증가 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].desc
   limit: do 1350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [MlynarWaiting], [WhenUse], [BeforeAttack], [DefenseUp], [Protection], [Combustion], [Vibration], [EndSkill], [EndBattle], [Aggro]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Protection] = 보호 / Protection; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor …
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nAt 40 [MlynarWaiting], becomes Clashable\n[WhenUse] At 40 [MlynarWaiting], until this Skill ends, this unit cannot be Staggered from taking damage, and gains Clash Power +20\n\n[BeforeAttack] Consume all [MlynarWaiting] and gain the following effects(all of them rounded down):\n- For every (Stack consumed / 20), recuperate 1 E.G.O resource (in the following order: Pride, then Wrath)\n- For every (Stack consumed / 10), gain +1 Atk Weight (max 4)\n- For every (Stack consumed / 10), gain [DefenseUp] (once per turn)\n- If 40 Stack was consumed, the 4th Coin deals +<style="highlight">80</style>% damage, and this unit gains 2 [Protection] (once per turn)\n\n[BeforeAttack] Deal +5% damage for every 8 ([Combustion] + [Vibration]) on the main target (max 25%)\n[EndSkill] Heal 5 SP for every target that was Staggered or killed due to this Skill's damage (max 25)\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndBattle] If this Skill did not consume 40 [MlynarWaiting], the leftmost Skill Slot on the Dashboard gains +4 [Aggro] next turn (once per turn)
   PL: [CantDuel]\nzewnętrzne efekty nie mogą ponownie użyć tej Umiejętności\nprzy 40 [MlynarWaiting] staje się zdolna do Starcia\n[WhenUse] przy 40 [MlynarWaiting], do końca tej Umiejętności ta jednostka nie zostaje Oszołamiona przez obrażenia i zyskuje Moc Walki +20\n\n[BeforeAttack] zużywa całe [MlynarWaiting] i zyskuje następujące efekty (wszystkie wartości zaokrąglone w dół)\n- za każde (zużyta wartość / 20) odzyskuje po 1 zasobu E.G.O (w kolejności: Pycha, potem Gniew)\n- za każde (zużyta wartość / 10) zyskuje +1 Wagi Ataku (maks. 4)\n- za każde (zużyta wartość / 10) zyskuje [DefenseUp] (1 raz na turę)\n- jeżeli zużyto 40, 4. użyta Moneta zadaje +<style="highlight">80</style>% obrażeń, a ta jednostka zyskuje 2 [Protection] (1 raz na turę)\n\n[BeforeAttack] zadaje +5% obrażeń za każde 8 (suma [Combustion] i [Vibration]) na celu głównym (maks. 25%)\n[EndSkill] odzyskuje 5 SP za każdego celu Oszołamionego lub pokonanego obrażeniami tej Umiejętności (maks. 25)\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndBattle] jeżeli ta Umiejętność nie zużyła 40 [MlynarWaiting], następnej tury skrajna lewa Umiejętność na Pulpicie zyskuje 4 [Aggro] (1 raz na turę)
739. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] (소모한 [MlynarWaiting] 수치 / 10) - 1만큼 이 코인 재사용 (최대 3회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [MlynarWaiting]
   znaczenie tagów: [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard
   EN: Reuse this Coin (([MlynarWaiting] Stack consumed / 10) - 1) times (3 times max)<style="highlight"></style>
   PL: ponownie używa tej Monety ((zużyta wartość [MlynarWaiting] / 10) - 1) razy (maks. 3 razy)<style="highlight"></style>
740. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] <style="highlight">[OnStartCoin] 이 코인이 파괴되지 않았고, 공격 대상이 3명 이상이면, 마지막에 사용할 코인의 피해량 +10% (집중 전투인 경우, 부위를 대상 1명으로 취급)</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]
   EN: <style="highlight">[OnStartCoin] If this Coin isn't Cracked, and if it targets 3+ enemies, the final Coin to be used deals +10% damage (for Focused Encounters, each Part counts as 1 target)</style>
   PL: <style="highlight">[OnStartCoin] jeżeli ta Moneta nie została zniszczona i atakuje 3+ wrogów, ostatnia używana Moneta zadaje +10% obrażeń (w walkach skupionych każda Część liczy się jako 1 cel)</style>
741. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
742. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]<style="highlight"></style>
743. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 6 — opis] [UnBrokenCoinOnSucceedAttack] 마지막에 사용하는 코인이고, 대상의 [Vibration] 위력이 15 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#5].desc ; dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#5].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [UnBrokenCoinOnSucceedAttack] If this is the final Coin, and if target has 15+ [Vibration] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli to ostatnia Moneta i Siła [Vibration] celu wynosi 15+, wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
744. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 7 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인을 4회 사용했으면, 대상의 [Vibration]만큼 나태 피해를 줌 (최대 5)<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=3].coinlist[#0].coindescs[#6].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] If this Coin was used 4 times, deal Sloth damage equal to [Vibration] on target (max 5)<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta Moneta została użyta 4 razy, zadaje obrażenia Lenistwa równe wartości [Vibration] celu (maks. 5)<style="highlight"></style>
745. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[MlynarWaiting]이 40이면, 합 가능으로 변경됨\n[WhenUse] [MlynarWaiting]이 40이면, 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않고 합 위력 +20\n\n[BeforeAttack] [MlynarWaiting]을 전부 소모하고 아래 효과 적용 (모든 수치는 소수점 버림)\n- (소모한 수치 / 20) 만큼 사용한 E.G.O 자원을 1개씩 반환 (오만, 분노 순으로 반환)\n- (소모한 수치 / 10) 만큼 가중치 증가 (최대 4)\n- (소모한 수치 / 10) 만큼 [DefenseUp] 얻음 (턴당 1회)\n- 40 소모했다면, 4번째로 사용할 코인의 피해량 +<style="highlight">100</style>%, [Protection] 2 얻음 (턴당 1회)\n\n[BeforeAttack] 메인 타겟의 [Combustion]과 [Vibration]의 합 8 당 피해량 +5% (최대 25%)\n[EndSkill] 이 스킬의 피해로 흐트러졌거나 사망한 대상 1명당 정신력 5 회복 (최대 25)\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndBattle] 이 스킬로 [MlynarWaiting]을 40 소모하지 못했다면, 다음 턴에 조작 패널에서 가장 왼쪽의 스킬 슬롯 [Aggro] 4 증가 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=4].desc
   limit: do 1350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [MlynarWaiting], [WhenUse], [BeforeAttack], [DefenseUp], [Protection], [Combustion], [Vibration], [EndSkill], [EndBattle], [Aggro]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Protection] = 보호 / Protection; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor …
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nAt 40 [MlynarWaiting], becomes Clashable\n[WhenUse] At 40 [MlynarWaiting], until this Skill ends, this unit cannot be Staggered from taking damage, and gains Clash Power +20\n\n[BeforeAttack] Consume all [MlynarWaiting] and gain the following effects(all of them rounded down):\n- For every (Stack consumed / 20), recuperate 1 E.G.O resource (in the following order: Pride, then Wrath)\n- For every (Stack consumed / 10), gain +1 Atk Weight (max 4)\n- For every (Stack consumed / 10), gain [DefenseUp] (once per turn)\n- If 40 Stack was consumed, the 4th Coin deals +<style="highlight">100</style>% damage, and this unit gains 2 [Protection] (once per turn)\n\n[BeforeAttack] Deal +5% damage for every 8 ([Combustion] + [Vibration]) on the main target (max 25%)\n[EndSkill] Heal 5 SP for every target that was Staggered or killed due to this Skill's damage (max 25)\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndBattle] If this Skill did not consume 40 [MlynarWaiting], the leftmost Skill Slot on the Dashboard gains +4 [Aggro] next turn (once per turn)
   PL: [CantDuel]\nzewnętrzne efekty nie mogą ponownie użyć tej Umiejętności\nprzy 40 [MlynarWaiting] staje się zdolna do Starcia\n[WhenUse] przy 40 [MlynarWaiting], do końca tej Umiejętności ta jednostka nie zostaje Oszołamiona przez obrażenia i zyskuje Moc Walki +20\n\n[BeforeAttack] zużywa całe [MlynarWaiting] i zyskuje następujące efekty (wszystkie wartości zaokrąglone w dół)\n- za każde (zużyta wartość / 20) odzyskuje po 1 zasobu E.G.O (w kolejności: Pycha, potem Gniew)\n- za każde (zużyta wartość / 10) zyskuje +1 Wagi Ataku (maks. 4)\n- za każde (zużyta wartość / 10) zyskuje [DefenseUp] (1 raz na turę)\n- jeżeli zużyto 40, 4. użyta Moneta zadaje +<style="highlight">100</style>% obrażeń, a ta jednostka zyskuje 2 [Protection] (1 raz na turę)\n\n[BeforeAttack] zadaje +5% obrażeń za każde 8 (suma [Combustion] i [Vibration]) na celu głównym (maks. 25%)\n[EndSkill] odzyskuje 5 SP za każdego celu Oszołamionego lub pokonanego obrażeniami tej Umiejętności (maks. 25)\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndBattle] jeżeli ta Umiejętność nie zużyła 40 [MlynarWaiting], następnej tury skrajna lewa Umiejętność na Pulpicie zyskuje 4 [Aggro] (1 raz na turę)
746. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnStartCoin] 이 코인이 파괴되지 않았고, 공격 대상이 3명 이상이면, 마지막에 사용할 코인의 피해량 +<style="highlight">20</style>% (집중 전투인 경우, 부위를 대상 1명으로 취급)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]
   EN: [OnStartCoin] If this Coin isn't Cracked, and if it targets 3+ enemies, the final Coin to be used deals +<style="highlight">20</style>% damage (for Focused Encounters, each Part counts as 1 target)
   PL: [OnStartCoin] jeżeli ta Moneta nie została zniszczona i atakuje 3+ wrogów, ostatnia używana Moneta zadaje +<style="highlight">20</style>% obrażeń (w walkach skupionych każda Część liczy się jako 1 cel)
747. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 7 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인을 4회 사용했으면, 대상의 [Vibration]만큼 나태 피해를 줌 (최대 <style="highlight">10</style>)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120912].levelList[level=4].coinlist[#0].coindescs[#6].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] If this Coin was used 4 times, deal Sloth damage equal to [Vibration] on target (max <style="highlight">10</style>)
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta Moneta została użyta 4 razy, zadaje obrażenia Lenistwa równe wartości [Vibration] celu (maks. <style="highlight">10</style>)
748. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 눈부시지 않은 영광 - 유수(流水)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].name ; dataList[id=2120921].levelList[level=3].name ; dataList[id=2120921].levelList[level=4].name
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 무에나
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].abName ; dataList[id=2120921].levelList[level=3].abName ; dataList[id=2120921].levelList[level=4].abName
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] [MlynarWaiting]이 40이면, 기본 위력 +1\n\n[BeforeAttack] [MlynarWaiting]을 전부 소모하고 아래 효과 적용 (모든 수치는 소수점 버림)\n- (소모한 수치 / 10) 만큼 [DefenseUp] 얻음 (턴당 1회)\n- 40 소모했다면, 마지막 코인의 피해량 +110%, [Protection] 2 얻음 (턴당 1회)\n\n[BeforeAttack] 메인 타겟의 [Combustion]과 [Vibration]의 합 6 당 피해량 +3% (최대 15%)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -4 (최대 -16)\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndBattle] 이 스킬로 [MlynarWaiting]을 40 소모했다면, 다음 턴에 조작 패널에서 가장 왼쪽의 스킬 슬롯 [Aggro] 8 증가 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [MlynarWaiting], [BeforeAttack], [DefenseUp], [Protection], [Combustion], [Vibration], [EndSkill], [EndBattle], [Aggro]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Protection] = 보호 / Protection; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor …
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] At 40 [MlynarWaiting], Base Power +1\n\n[BeforeAttack] Consume all [MlynarWaiting] and gain the following effects(all of them rounded down):\n- Gain (Stack consumed / 10) [DefenseUp] (once per turn)\n- If 40 Stack was consumed, the final Coin deals +110% damage and this unit gains 2 [Protection] (once per turn)\n\n[BeforeAttack] Deal +3% damage for every 6 ([Combustion] + [Vibration]) on the main target (max 15%)\n[BeforeAttack] Base Power -4 for every Cracked Coin (max -16)\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndBattle] If 40 [MlynarWaiting] was consumed by this Skill, the leftmost Skill Slot on the Dashboard gains +8 [Aggro] next turn (once per turn)
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] przy 40 [MlynarWaiting] Moc Bazowa +1\n\n[BeforeAttack] zużywa całe [MlynarWaiting] i zyskuje następujące efekty (wszystkie wartości zaokrąglone w dół)\n- zyskuje (zużyta wartość / 10) [DefenseUp] (1 raz na turę)\n- jeżeli zużyto 40, ostatnia Moneta zadaje +110% obrażeń, a ta jednostka zyskuje 2 [Protection] (1 raz na turę)\n\n[BeforeAttack] zadaje +3% obrażeń za każde 6 (suma [Combustion] i [Vibration]) na celu głównym (maks. 15%)\n[BeforeAttack] -4 do Mocy Bazowej za każdą zniszczoną Monetę (maks. -16)\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndBattle] jeżeli ta Umiejętność zużyła 40 [MlynarWaiting], następnej tury skrajna lewa Umiejętność na Pulpicie zyskuje 8 [Aggro] (1 raz na turę)
751. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2120921].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2120921].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2120921].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=2120921].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL: [OnSucceedAttack] Nakłada 5 [Combustion]
756. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 4, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Vibration] 위력이 15 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=1].coinlist[#3].coindescs[#3].desc ; dataList[id=2120921].levelList[level=3].coinlist[#3].coindescs[#3].desc ; dataList[id=2120921].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [UnBrokenCoinOnSucceedAttack] If target has 15+ [Vibration] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli Siła [Vibration] celu wynosi 15+, wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
758. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">공격 대상이 3명 이상일 때, 1~3코인이 파괴되지 않고 적중시 마지막 코인의 피해량 +25% (코인당 1회 발동, 집중 전투인 경우, 부위를 대상 1명으로 취급)</style>\n[WhenUse] [MlynarWaiting]이 40이면, 기본 위력 +1\n\n[BeforeAttack] [MlynarWaiting]을 전부 소모하고 아래 효과 적용 (모든 수치는 소수점 버림)\n- (소모한 수치 / 10) 만큼 [DefenseUp] 얻음 (턴당 1회)\n- 40 소모했다면, 마지막 코인의 피해량 +<style="highlight">130</style>%, 보호 2 얻음 (턴당 1회)\n\n[BeforeAttack] 메인 타겟의 [Combustion]과 [Vibration]의 합 6 당 피해량 +3% (최대 15%)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -4 (최대 -16)\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndBattle] 이 스킬로 [MlynarWaiting]을 40 소모했다면, 다음 턴에 조작 패널에서 가장 왼쪽의 스킬 슬롯 [Aggro] 8 증가 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=3].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WhenUse], [MlynarWaiting], [BeforeAttack], [DefenseUp], [Combustion], [Vibration], [EndSkill], [EndBattle], [Aggro], [Protection]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">When attacking 3+ targets: If the Coins 1~3 hit without Cracking, the final Coin deals +25% damage (once per Coin; in Focused Encounters, each Part counts as 1 target)</style>\n[WhenUse] At 40 [MlynarWaiting], Base Power +1\n\n[BeforeAttack] Consume all [MlynarWaiting] and gain the following effects(all of them rounded down):\n- Gain (Stack consumed / 10) [DefenseUp] (once per turn)\n- If 40 Stack was consumed, the final Coin deals +<style="highlight">130</style>% damage and this unit gains 2 [Protection] (once per turn)\n\n[BeforeAttack] Deal +3% damage for every 6 ([Combustion] + [Vibration]) on the main target (max 15%)\n[BeforeAttack] Base Power -4 for every Cracked Coin (max -16)\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndBattle] If 40 [MlynarWaiting] was consumed by this Skill, the leftmost Skill Slot on the Dashboard gains +8 [Aggro] next turn (once per turn)
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">przy ataku 3+ celów: jeżeli Monety 1~3 trafiły bez zniszczenia, ostatnia Moneta zadaje +25% obrażeń (1 raz na Monetę; w walkach skupionych każda Część liczy się jako 1 cel)</style>\n[WhenUse] przy 40 [MlynarWaiting] Moc Bazowa +1\n\n[BeforeAttack] zużywa całe [MlynarWaiting] i zyskuje następujące efekty (wszystkie wartości zaokrąglone w dół)\n- zyskuje (zużyta wartość / 10) [DefenseUp] (1 raz na turę)\n- jeżeli zużyto 40, ostatnia Moneta zadaje +<style="highlight">130</style>% obrażeń, a ta jednostka zyskuje 2 [Protection] (1 raz na turę)\n\n[BeforeAttack] zadaje +3% obrażeń za każde 6 (suma [Combustion] i [Vibration]) na celu głównym (maks. 15%)\n[BeforeAttack] -4 do Mocy Bazowej za każdą zniszczoną Monetę (maks. -16)\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndBattle] jeżeli ta Umiejętność zużyła 40 [MlynarWaiting], następnej tury skrajna lewa Umiejętność na Pulpicie zyskuje 8 [Aggro] (1 raz na turę)
759. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=2120921].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 5 [Combustion]<style="highlight"></style>
760. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Vibration] 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=2120921].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 5 [Vibration]<style="highlight"></style>
761. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n공격 대상이 3명 이상일 때, 1~3코인이 파괴되지 않고 적중시 마지막 코인의 피해량 +<style="highlight">30</style>% (코인당 1회 발동, 집중 전투인 경우, 부위를 대상 1명으로 취급)\n[WhenUse] [MlynarWaiting]이 40이면, 기본 위력 +1\n\n[BeforeAttack] [MlynarWaiting]을 전부 소모하고 아래 효과 적용 (모든 수치는 소수점 버림)\n- (소모한 수치 / 10) 만큼 [DefenseUp] 얻음 (턴당 1회)\n- 40 소모했다면, 마지막 코인의 피해량 +<style="highlight">160</style>%, 보호 2 얻음 (턴당 1회)\n\n[BeforeAttack] 메인 타겟의 [Combustion]과 [Vibration]의 합 6 당 피해량 +3% (최대 15%)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -4 (최대 -16)\n[EndSkill] [MlynarWaiting] 1 얻음\n[EndBattle] 이 스킬로 [MlynarWaiting]을 40 소모했다면, 다음 턴에 조작 패널에서 가장 왼쪽의 스킬 슬롯 [Aggro] 8 증가 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=4].desc
   limit: do 1080 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WhenUse], [MlynarWaiting], [BeforeAttack], [DefenseUp], [Combustion], [Vibration], [EndSkill], [EndBattle], [Aggro], [Protection]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: [CantIdentify]\nTargets randomly\nIf there are 3+ targets: If the Coins 1~3 hit without Cracking, the final Coin deals +<style="highlight">30</style>% damage (once per Coin; in Focused Encounters, each Part counts as 1 target)\n[WhenUse] At 40 [MlynarWaiting], Base Power +1\n\n[BeforeAttack] Consume all [MlynarWaiting] and gain the following effects(all of them rounded down):\n- Gain (Stack consumed / 10) [DefenseUp] (once per turn)\n- If 40 Stack was consumed, the final Coin deals +<style="highlight">160</style>% damage and this unit gains 2 [Protection] (once per turn)\n\n[BeforeAttack] Deal +3% damage for every 6 ([Combustion] + [Vibration]) on the main target (max 15%)\n[BeforeAttack] Base Power -4 for every Cracked Coin (max -16)\n[EndSkill] Gain 1 [MlynarWaiting]\n[EndBattle] If 40 [MlynarWaiting] was consumed by this Skill, the leftmost Skill Slot on the Dashboard gains +8 [Aggro] next turn (once per turn)
   PL: [CantIdentify]\nAtakuje losowy cel\nprzy ataku 3+ celów: jeżeli Monety 1~3 trafiły bez zniszczenia, ostatnia Moneta zadaje +<style="highlight">30</style>% obrażeń (1 raz na Monetę; w walkach skupionych każda Część liczy się jako 1 cel)\n[WhenUse] przy 40 [MlynarWaiting] Moc Bazowa +1\n\n[BeforeAttack] zużywa całe [MlynarWaiting] i zyskuje następujące efekty (wszystkie wartości zaokrąglone w dół)\n- zyskuje (zużyta wartość / 10) [DefenseUp] (1 raz na turę)\n- jeżeli zużyto 40, ostatnia Moneta zadaje +<style="highlight">160</style>% obrażeń, a ta jednostka zyskuje 2 [Protection] (1 raz na turę)\n\n[BeforeAttack] zadaje +3% obrażeń za każde 6 (suma [Combustion] i [Vibration]) na celu głównym (maks. 15%)\n[BeforeAttack] -4 do Mocy Bazowej za każdą zniszczoną Monetę (maks. -16)\n[EndSkill] zyskuje 1 [MlynarWaiting]\n[EndBattle] jeżeli ta Umiejętność zużyła 40 [MlynarWaiting], następnej tury skrajna lewa Umiejętność na Pulpicie zyskuje 8 [Aggro] (1 raz na turę)
762. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
763. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2120921].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Pasywka E.G.O — nazwa] 협객
   źródło: Passive_Ego.json :: dataList[id=2120911].name
   limit: do 40 znaków
   EN: Wanderer
   PL: Wierny Wojownik
767. [Pasywka E.G.O — opis] 아래 조건 만족 시 [MlynarWaiting] 얻음\n- 자신의 체력 피해 3 당 1 얻음\n- 자신의 보호막 피해 5 당 1 얻음\n- 본인을 제외한 아군이 흐트러지면, 한 명당 10 얻음\n- 본인을 제외한 아군이 사망하면, 한 명당 20 얻음\n\n턴 시작 시 피해로 인한 흐트러짐 상태일 때, [MlynarWaiting]이 40이면, 해당 턴 동안 모든 내성을 2로 고정하고 자신의 흐트러짐을 해제 (전투당 1회, 강제 흐트러짐 제외)
   źródło: Passive_Ego.json :: dataList[id=2120911].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [MlynarWaiting]
   znaczenie tagów: [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard
   EN: Gain [MlynarWaiting] when meeting one of the following conditions:\n- Gain 1 for every 3 HP damage taken\n- Gain 1 for every 5 Shield HP damage taken\n- Gain 10 per Staggered ally when other allies become Staggered\n- Gain 20 per dead ally when other allies are killed\n\nTurn Start: if this unit is Staggered due to damage, and if this unit has 40+ [MlynarWaiting], fix all of this unit's Resistance values to 2 for the turn and recover from Stagger (once per Encounter; excluding forced Staggers)
   PL: zyskuje [MlynarWaiting] przy spełnieniu jednego z poniższych warunków\n- zyskuje 1 za każde 3 otrzymanych obrażeń HP\n- zyskuje 1 za każde 5 otrzymanych obrażeń Tarczy\n- zyskuje 10 za każdego sojusznika innego niż ta jednostka, który zostaje Oszołamiony\n- zyskuje 20 za każdego sojusznika innego niż ta jednostka, który zostaje pokonany\n\nna początku tury, jeżeli ta jednostka jest Oszołamiona przez obrażenia i ma 40+ [MlynarWaiting], na czas tej tury ustala wartość wszystkich jej Odporności na 2 i zdejmuje z siebie Oszołomienie (1 raz na walkę; z wyłączeniem wymuszonego Oszołomienia)

## E.G.O [21210] Move-in Reg. (입주 신고) — Gregor
- postać: Gregor (그레고르) · ID E.G.O: `21210`

768. [Karta E.G.O — nazwa] 입주 신고
   źródło: Egos.json :: dataList[id=21210].name
   limit: do 40 znaków
   EN: Move-in Reg.
   PL: Zgłoszenie Zamieszkowania
769. [Karta E.G.O — opis] 그레고르 전용 EGO 장비
   źródło: Egos.json :: dataList[id=21210].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 입주 신고
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].name ; dataList[id=2121011].levelList[level=3].name ; dataList[id=2121011].levelList[level=4].name
   (powtórzenie elementu 768 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] Kqe-1j-23
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].abName ; dataList[id=2121011].levelList[level=3].abName ; dataList[id=2121011].levelList[level=4].abName
   limit: do 40 znaków
   EN: Kqe-1j-23
   PL: Kqe-1j-23
772. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 아래 조건 만족 시 코인 위력 +1 (최대 3)\n- 메인 타겟의 [Combustion] 위력 6당\n- (자신의 [Charge] 위력 - 1)만큼\n[BeforeAttack] (자신의 [Charge] 위력 - 1)만큼 이 스킬로 부여하는 [Combustion] <noparse>위력 증가</noparse> (최대 2)\n[BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 7)\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 15 소모하여, 소모한 충전 횟수당 피해량 +1% (최대 15%)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Combustion], [Charge], [BeforeAttack]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Gain Coin Power based on the following conditions (max 3):\n- Coin Power +1 for every 6 [Combustion] Potency on the main target\n- Gain Coin Power equal to ([Charge] Potency on self - 1)\n[BeforeAttack] This Skill inflicts +([Charge] Potency on self - 1) more [Combustion] Potency (max 2)\n[BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 7)\n[BeforeAttack] Consume up to 15 [Charge] Count and deal +1% damage for every [Charge] Count consumed (max 15%)
   PL: Moc Monety +1 przy spełnieniu poniższych warunków (maks. 3)\n- za każde 6 Siły [Combustion] na celu głównym\n- tyle, ile wynosi (Siła [Charge] tej jednostki - 1)\n[BeforeAttack] ta Umiejętność nakłada dodatkowo tyle Siły [Combustion], ile wynosi (Siła [Charge] tej jednostki - 1) (maks. 2)\n[BeforeAttack] zyskuje +(najwyższy Rezonans + 1) Licznika [Charge] (maks. 7)\n[BeforeAttack] zużywa maks. 15 Licznika [Charge] i zadaje +1% obrażeń za każdy zużyty Licznik [Charge] (maks. 15%)\n[EndSkill] jeżeli efekty przed atakiem zużyły 15 Licznika [Charge], zyskuje +5 Licznika [Charge]
773. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [IDMicroChip]이나 [Binding]이 있으면, [Combustion] 횟수 2 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2121011].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2121011].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [IDMicroChip], [Binding], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IDMicroChip] = 주민등록 마이크로칩 / Resident Reg. Microchip; [Binding] = 속박 / Bind; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has [IDMicroChip] or [Binding],  inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] jeżeli cel ma [IDMicroChip] lub [Binding], nakłada +2 Licznika [Combustion]
775. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [IDMicroChip] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [IDMicroChip]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IDMicroChip] = 주민등록 마이크로칩 / Resident Reg. Microchip
   EN: [OnSucceedAttack] Inflict 1 [IDMicroChip]
   PL: [OnSucceedAttack] nakłada 1 [IDMicroChip]
776. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]
777. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 아래 조건 만족 시 코인 위력 +1 (최대 3)\n- 메인 타겟의 [Combustion] 위력 6당\n- (자신의 [Charge] 위력 - 1)만큼\n[BeforeAttack] (자신의 [Charge] 위력 - 1)만큼 이 스킬로 부여하는 [Combustion] <noparse>위력 증가</noparse> (최대 2)\n[BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 7)\n<style="highlight">- 자신의 [Charge] 횟수가 3 이하면, 추가로 3 증가</style>\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 15 소모하여, 소모한 충전 횟수당 피해량 +<style="highlight">2</style>% (최대 <style="highlight">30</style>%)\n<style="highlight">[EndSkill] 공격 시작 전 효과로 [Charge] 횟수를 15 소모했으면, 자신의 [Charge] 횟수 5 증가</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=3].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [Combustion], [Charge], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Gain Coin Power based on the following conditions (max 3):\n- Coin Power +1 for every 6 [Combustion] Potency on the main target\n- Gain Coin Power equal to ([Charge] Potency on self - 1)\n[BeforeAttack] This Skill inflicts +([Charge] Potency on self - 1) more [Combustion] Potency (max 2)\n[BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 7)\n<style="highlight">- At 3 or fewer [Charge] Count, gain 3 more [Charge] Count</style>\n[BeforeAttack] Consume up to 15 [Charge] Count and deal +<style="highlight">2</style>% damage for every [Charge] Count consumed (max <style="highlight">30</style>%)\n<style="highlight">[EndSkill] If the Before Attack effects consumed 15 [Charge] Count, gain +5 [Charge] Count</style>
   PL: Moc Monety +1 przy spełnieniu poniższych warunków (maks. 3)\n- za każde 6 Siły [Combustion] na celu głównym\n- tyle, ile wynosi (Siła [Charge] tej jednostki - 1)\n[BeforeAttack] ta Umiejętność nakłada dodatkowo tyle Siły [Combustion], ile wynosi (Siła [Charge] tej jednostki - 1) (maks. 2)\n[BeforeAttack] zyskuje +(najwyższy Rezonans + 1) Licznika [Charge] (maks. 7)\n<style="highlight">- jeżeli Licznik [Charge] tej jednostki wynosi 3 lub mniej, dodatkowo zyskuje 3</style>\n[BeforeAttack] zużywa maks. 15 Licznika [Charge] i zadaje +<style="highlight">2</style>% obrażeń za każdy zużyty Licznik [Charge] (maks. <style="highlight">30</style>%)\n<style="highlight">[EndSkill] jeżeli efekty przed atakiem zużyły 15 Licznika [Charge], zyskuje +5 Licznika [Charge]</style>
778. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Charge] 횟수 2 증가</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttack] Gain +2 [Charge] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2</style>
780. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [IDMicroChip] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [IDMicroChip]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IDMicroChip] = 주민등록 마이크로칩 / Resident Reg. Microchip
   EN: [OnSucceedAttack] Inflict 1 [IDMicroChip]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 1 [IDMicroChip]<style="highlight"></style>
781. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=2121011].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]<style="highlight"></style>
782. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 아래 조건 만족 시 코인 위력 +1 (최대 3)\n- 메인 타겟의 [Combustion] 위력 6당\n- (자신의 [Charge] 위력 - 1)만큼\n[BeforeAttack] (자신의 [Charge] 위력 - 1)만큼 이 스킬로 부여하는 [Combustion] <noparse>위력 증가</noparse> (최대 2)\n[BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 7)\n- 자신의 [Charge] 횟수가 3 이하면, 추가로 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 15 소모하여, 소모한 충전 횟수당 피해량 +<style="highlight">3</style>% (최대 <style="highlight">45</style>%)\n[EndSkill] 공격 시작 전 효과로 [Charge] 횟수를 15 소모했으면, 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=4].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [Combustion], [Charge], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Gain Coin Power based on the following conditions (max 3):\n- Coin Power +1 for every 6 [Combustion] Potency on the main target\n- Gain Coin Power equal to ([Charge] Potency on self - 1)\n[BeforeAttack] This Skill inflicts +([Charge] Potency on self - 1) more [Combustion] Potency (max 2)\n[BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 7)\n- At 3 or fewer [Charge] Count, gain 3 more [Charge] Count\n[BeforeAttack] Consume up to 15 [Charge] Count and deal +<style="highlight">3</style>% damage for every [Charge] Count consumed (max <style="highlight">45</style>%)\n[EndSkill] If the Before Attack effects consumed 15 [Charge] Count, gain +5 [Charge] Count
   PL: Moc Monety +1 przy spełnieniu poniższych warunków (maks. 3)\n- za każde 6 Siły [Combustion] na celu głównym\n- tyle, ile wynosi (Siła [Charge] tej jednostki - 1)\n[BeforeAttack] ta Umiejętność nakłada dodatkowo tyle Siły [Combustion], ile wynosi (Siła [Charge] tej jednostki - 1) (maks. 2)\n[BeforeAttack] zyskuje +(najwyższy Rezonans + 1) Licznika [Charge] (maks. 7)\n- jeżeli Licznik [Charge] tej jednostki wynosi 3 lub mniej, dodatkowo zyskuje 3\n[BeforeAttack] zużywa maks. 15 Licznika [Charge] i zadaje +<style="highlight">3</style>% obrażeń za każdy zużyty Licznik [Charge] (maks. <style="highlight">45</style>%)\n[EndSkill] jeżeli efekty przed atakiem zużyły 15 Licznika [Charge], zyskuje +5 Licznika [Charge]
783. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2<style="highlight"></style>
785. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [IDMicroChip] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121011].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [IDMicroChip]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IDMicroChip] = 주민등록 마이크로칩 / Resident Reg. Microchip
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [IDMicroChip]
   PL: [OnSucceedAttack] nakłada <style="highlight">2</style> [IDMicroChip]
786. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 입주 신고
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=1].name ; dataList[id=2121021].levelList[level=3].name ; dataList[id=2121021].levelList[level=4].name
   (powtórzenie elementu 768 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] Kqe-1j-23
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=1].abName ; dataList[id=2121021].levelList[level=3].abName ; dataList[id=2121021].levelList[level=4].abName
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n아래 조건 만족 시 코인 위력 +1 (최대 3)\n- 메인 타겟의 [Combustion] 위력 6당\n- (자신의 [Charge] 위력 - 1)만큼\n[BeforeAttack] (최대 공명 수 + 3)만큼 자신의 [Charge] 횟수 증가 (최대 10)\n[BeforeAttack] 피해량 + (자신의 [Charge] 위력 + 횟수 - 1)% (최대 20%)\n[EnemyKill] 자신의 [Charge] 횟수 4 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Combustion], [Charge], [BeforeAttack], [EnemyKill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [CantIdentify]\nTargets randomly\nGain Coin Power based on the following conditions (max 3):\n- Coin Power +1 for every 6 [Combustion] Potency on the main target\n- Gain Coin Power equal to ([Charge] Potency on self - 1)\n[BeforeAttack] Gain +(highest Reson. + 3) [Charge] Count (max 10)\n[BeforeAttack] Deal +([Charge] Potency + Count - 1)% damage (max 20%)\n[EnemyKill] Gain +4 [Charge] Count
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Monety +1 przy spełnieniu poniższych warunków (maks. 3)\n- za każde 6 Siły [Combustion] na celu głównym\n- tyle, ile wynosi (Siła [Charge] tej jednostki - 1)\n[BeforeAttack] zyskuje +(najwyższy Rezonans + 3) Licznika [Charge] (maks. 10)\n[BeforeAttack] zadaje +(Siła [Charge] tej jednostki + Licznik - 1)% obrażeń (maks. 20%)\n[EnemyKill] zyskuje +4 Licznika [Charge]
789. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [IDMicroChip] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2121021].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 775 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2121021].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2121021].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n아래 조건 만족 시 코인 위력 +1 (최대 3)\n- 메인 타겟의 [Combustion] 위력 6당\n- (자신의 [Charge] 위력 - 1)만큼\n[BeforeAttack] (최대 공명 수 + 3)만큼 자신의 [Charge] 횟수 증가 (최대 10)\n[BeforeAttack] 피해량 + (자신의 [Charge] 위력 + 횟수 - 1) x <style="highlight">2</style>% (최대 <style="highlight">40</style>%)\n[EnemyKill]\n- 자신의 [Charge] 횟수 4 증가\n<style="highlight">- 다음 턴에 [AttackDmgUp] 1 얻음 (턴당 1회)</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=3].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Combustion], [Charge], [BeforeAttack], [EnemyKill], [AttackDmgUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EnemyKill] = [적 처치 시] / [On Kill]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantIdentify]\nTargets randomly\nGain Coin Power based on the following conditions (max 3):\n- Coin Power +1 for every 6 [Combustion] Potency on the main target\n- Gain Coin Power equal to ([Charge] Potency on self - 1)\n[BeforeAttack] Gain +(highest Reson. + 3) [Charge] Count (max 10)\n[BeforeAttack] Deal +(([Charge] Potency + Count - 1) x <style="highlight">2</style>)% damage (max <style="highlight">40</style>%)\n[EnemyKill]\n- Gain +4 [Charge] Count\n<style="highlight">- Gain 1 [AttackDmgUp] next turn (once per turn)</style>
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Monety +1 przy spełnieniu poniższych warunków (maks. 3)\n- za każde 6 Siły [Combustion] na celu głównym\n- tyle, ile wynosi (Siła [Charge] tej jednostki - 1)\n[BeforeAttack] zyskuje +(najwyższy Rezonans + 3) Licznika [Charge] (maks. 10)\n[BeforeAttack] zadaje +((Siła [Charge] tej jednostki + Licznik - 1) x <style="highlight">2</style>)% obrażeń (maks. <style="highlight">40</style>%)\n[EnemyKill]\n- zyskuje +4 Licznika [Charge]\n<style="highlight">- następnej tury zyskuje 1 [AttackDmgUp] (1 raz na turę)</style>
793. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] <style="highlight">[OnStartCoin] 자신의 [Charge] 횟수 최대 8 소모</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnStartCoin] Consume up to 8 [Charge] Count</style>
   PL: <style="highlight">[OnStartCoin] zużywa maks. 8 Licznika [Charge]</style>
795. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 이 코인에서 [Charge] 횟수를 소모했으면, 이 코인 최종 피해량의 (소모한 충전 횟수 x 5)%만큼 질투 피해 (최소 5%, 최대 40%)</style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttack] If this Coin consumed [Charge] Count, deal Envy damage equal to ([Charge] Count consumed x 5)% of this Coin's final damage (min 5%, max 40%)</style>
   PL: <style="highlight">[OnSucceedAttack] jeżeli ta Moneta zużyła Licznik [Charge], zadaje obrażenia Zazdrości równe (zużyty Licznik [Charge] x 5)% końcowych obrażeń tej Monety (min. 5%, maks. 40%)</style>
796. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n아래 조건 만족 시 코인 위력 +1 (최대 3)\n- 메인 타겟의 [Combustion] 위력 6당\n- (자신의 [Charge] 위력 - 1)만큼\n[BeforeAttack] (최대 공명 수 + 3)만큼 자신의 [Charge] 횟수 증가 (최대 10)\n[BeforeAttack] 피해량 + (자신의 [Charge] 위력 + 횟수 - 1) x <style="highlight">3</style>% (최대 <style="highlight">60</style>%)\n[EnemyKill]\n- 자신의 [Charge] 횟수 4 증가\n- 다음 턴에 [AttackDmgUp] 1 얻음 (턴당 1회)
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Combustion], [Charge], [BeforeAttack], [EnemyKill], [AttackDmgUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EnemyKill] = [적 처치 시] / [On Kill]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantIdentify]\nTargets randomly\nGain Coin Power based on the following conditions (max 3):\n- Coin Power +1 for every 6 [Combustion] Potency on the main target\n- Gain Coin Power equal to ([Charge] Potency on self - 1)\n[BeforeAttack] Gain +(highest Reson. + 3) [Charge] Count (max 10)\n[BeforeAttack] Deal +(([Charge] Potency + Count - 1) x <style="highlight">3</style>)% damage (max <style="highlight">60</style>%)\n[EnemyKill]\n- Gain +4 [Charge] Count\n- Gain 1 [AttackDmgUp] next turn (once per turn)
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Monety +1 przy spełnieniu poniższych warunków (maks. 3)\n- za każde 6 Siły [Combustion] na celu głównym\n- tyle, ile wynosi (Siła [Charge] tej jednostki - 1)\n[BeforeAttack] zyskuje +(najwyższy Rezonans + 3) Licznika [Charge] (maks. 10)\n[BeforeAttack] zadaje +((Siła [Charge] tej jednostki + Licznik - 1) x <style="highlight">3</style>)% obrażeń (maks. <style="highlight">60</style>%)\n[EnemyKill]\n- zyskuje +4 Licznika [Charge]\n- następnej tury zyskuje 1 [AttackDmgUp] (1 raz na turę)
797. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o <style="highlight">3</style>
798. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [IDMicroChip] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 785 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnStartCoin] 자신의 [Charge] 횟수 최대 8 소모<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: [OnStartCoin] Consume up to 8 [Charge] Count<style="highlight"></style>
   PL: [OnStartCoin] zużywa maks. 8 Licznika [Charge]<style="highlight"></style>
800. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 이 코인에서 [Charge] 횟수를 소모했으면, 이 코인 최종 피해량의 (소모한 충전 횟수 x 5)%만큼 질투 피해 (최소 5%, 최대 40%)<style="highlight"></style>
   źródło: Skills_Ego_Personality-12.json :: dataList[id=2121021].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] If this Coin consumed [Charge] Count, deal Envy damage equal to ([Charge] Count consumed x 5)% of this Coin's final damage (min 5%, max 40%)<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli ta Moneta zużyła Licznik [Charge], zadaje obrażenia Zazdrości równe (zużyty Licznik [Charge] x 5)% końcowych obrażeń tej Monety (min. 5%, maks. 40%)<style="highlight"></style>
801. [Pasywka E.G.O — nazwa] 전입 신고 처리
   źródło: Passive_Ego.json :: dataList[id=2121011].name
   limit: do 40 znaków
   EN: Processing Transfer Reg
   PL: Przetwarzanie Zgłoszenia Zamieszkowania
802. [Pasywka E.G.O — opis] 최대 공명 수가 3 이상이면, 스킬 적중 시 메인 타겟에게 다음 턴에 [Binding] 1 부여 (턴당 1회)\n\n자신의 [Charge] 위력이 3 이상이면, 자신이 [Charge] 횟수를 얻거나 소모하는 기본 스킬 및 적에게 [Combustion] 위력 또는 횟수를 부여하는 기본 스킬 피해량 +10%
   źródło: Passive_Ego.json :: dataList[id=2121011].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [Charge], [Combustion]
   znaczenie tagów: [Binding] = 속박 / Bind; [Charge] = 충전 / Charge; [Combustion] = 화상 / Burn
   EN: At 3+ highest Reson.: On Hit using a Skill, inflict 1 [Binding] next turn on the main target (once per turn)\n\nAt 3+ [Charge] Potency, the following Base Skills deal +10% damage:\n- Base Skills that gain or consume [Charge] Count\n- Base Skills that inflict [Combustion] Potency or Count on the enemy
   PL: przy najwyższym Rezonansie 3+: przy trafieniu Umiejętnością, następnej tury nakłada 1 [Binding] na cel główny (1 raz na turę)\n\nprzy 3+ Siły [Charge] następujące Podstawowe Umiejętności zadają +10% obrażeń:\n- Podstawowe Umiejętności zyskujące lub zużywające Licznik [Charge]\n- Podstawowe Umiejętności nakładające Siłę lub Licznik [Combustion] na wrogów

## E.G.O (dodatkowe): Passive_Ego
- plik gry: `Passive_Ego.json`

803. [E.G.O (dodatkowe) [50001] — nazwa] 매지컬 아르카나
   źródło: Passive_Ego.json :: dataList[id=50001].name
   limit: do 40 znaków
   EN: Magical Arcana
   PL: Magiczna Arcana
804. [E.G.O (dodatkowe) [50001] — opis] 마법소녀 인격 또는 마법소녀 E.G.O 출격 인원 수가 일정 수 이상이면 아래 효과 발동 (인격, E.G.O 중복 적용 가능)\n(2) 아군 마법소녀 인격 또는 마법소녀 E.G.O의 스킬 피해량 +10%
   źródło: Passive_Ego.json :: dataList[id=50001].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Activate the following effects based on the number of "Magical Girl" Identities or "Magical Girl" E.G.O on the field (Identities and E.G.O are counted together)\n(2) Allied "Magical Girl" Identity's or allied "Magical Girl" E.G.O's Skills deal +10% damage
   PL: — opis] wywołuje poniższe efekty w zależności od liczby Tożsamości „Magiczna Dziewczynka" lub E.G.O „Magiczna Dziewczynka" na polu (Tożsamości i E.G.O liczone łącznie)\n(2) Umiejętności sojuszniczych Tożsamości „Magiczna Dziewczynka" lub sojuszniczego E.G.O „Magiczna Dziewczynka" zadają +10% obrażeń
805. [E.G.O (dodatkowe) [50001] — podsumowanie] (2) 마법소녀 인격, EGO의 스킬 피해량 +10%
   źródło: Passive_Ego.json :: dataList[id=50001].summary
   limit: do 120 znaków
   EN: (2) Magical Girl Identities / E.G.O deal +10% damage using Skills
   PL: — podsumowanie] (2) Tożsamości/E.G.O „Magiczna Dziewczynka" zadają +10% obrażeń Umiejętnościami
806. [E.G.O (dodatkowe) [50002] — nazwa] 매지컬 아르카나
   źródło: Passive_Ego.json :: dataList[id=50002].name
   (powtórzenie elementu 803 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [E.G.O (dodatkowe) [50002] — opis] (3) 모든 아군의 빼기 코인 스킬 피해량 +10%\n'눈물로 벼려낸 검' E.G.O 스킬로 메인 타겟인 적에게 공격 종료시, [DespairKnightEGOAlly] 1 부여 (턴당 1회)
   źródło: Passive_Ego.json :: dataList[id=50002].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [DespairKnightEGOAlly]
   znaczenie tagów: [DespairKnightEGOAlly] = 잊혀진 기사의 검 / Sword of a Forgotten Knight
   EN: (3) All allies' Minus Coin Skills deal +10% damage\nAt Attack End against the enemy main target of "The Sword Sharpened with Tears" E.G.O Skill, inflict 1 [DespairKnightEGOAlly] (once per turn)
   PL: — opis] (3) Umiejętności sojuszników z Monetą Minus zadają +10% obrażeń\nna koniec ataku na wroga będącego celem głównym Umiejętności E.G.O „The Sword Sharpened with Tears", nakłada 1 [DespairKnightEGOAlly] (1 raz na turę)
808. [E.G.O (dodatkowe) [50002] — podsumowanie] (3) 모든 아군 빼기 코인 스킬 피해량 +10%, '눈물로 벼려낸 검' 공격 종료시, [DespairKnightEGOAlly] 1 부여
   źródło: Passive_Ego.json :: dataList[id=50002].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [DespairKnightEGOAlly]
   znaczenie tagów: [DespairKnightEGOAlly] = 잊혀진 기사의 검 / Sword of a Forgotten Knight
   EN: (3) All allies' Minus Coin Skills deal +10% damage\nAttack End of "The Sword Sharpened with Tears": Inflict 1 [DespairKnightEGOAlly]
   PL: — podsumowanie] (3) Umiejętności sojuszników z Monetą Minus zadają +10% obrażeń\nna koniec ataku „The Sword Sharpened with Tears", nakłada 1 [DespairKnightEGOAlly]
809. [E.G.O (dodatkowe) [50003] — nazwa] 4번째 성냥불
   źródło: Passive_Ego.json :: dataList[id=50003].name
   limit: do 40 znaków
   EN: 4th Match Flame
   PL: 4. Płomyk Zapałki
810. [E.G.O (dodatkowe) [50003] — opis] [SynergyActivationConditions]\n다음 [SynergyActivationConditions_ForthMatchFlame]을 만족한 4번째 성냥불 E.G.O가\n편성된 수에 따라 아래 효과 발동 (전투에 참여하지 않은 인격 포함)\n\n[SynergyActivationEffect]\n(2) 편성 창에 편성된 [PersonalityCombustion] 수가 3/5/7/10명 이상이면,\n4번째 성냥불 E.G.O의 피해량 20/40/60/80% 증가\n- 전투에 참여하지 않은 인격 포함\n- 해당 E.G.O 스킬의 공격 가중치보다 낮은 대상 1당, 피해량 +20%
   źródło: Passive_Ego.json :: dataList[id=50003].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [SynergyActivationConditions], [SynergyActivationConditions_ForthMatchFlame], [SynergyActivationEffect], [PersonalityCombustion]
   znaczenie tagów: [SynergyActivationConditions] = [발동 조건] / [Activation Conditions]; [SynergyActivationConditions_ForthMatchFlame] = 시너지 발동 조건 / Synergy Activation Condition; [SynergyActivationEffect] = [발동 효과] / [Activation Effects]; [PersonalityCombustion] = 화상 인격 / Burn ID
   EN: [SynergyActivationConditions]\nActivate the [SynergyActivationEffect] based on the number of equipped 4th Match Flame E.G.O that meet the conditions stipulated in [SynergyActivationConditions_ForthMatchFlame] (includes Identities not on the field)\n\n[SynergyActivationEffect]\n(2) If 3+/5+/7+/10+ [PersonalityCombustion]s are equipped in the Team Loadout, 4th Match Flame E.G.O deals +20%/+40%/+60%/+80% damage\n- Includes Identities not on the field\n- Deal +20% damage for every excess Atk Weight beyond the # of actual targets
   PL: — opis] [SynergyActivationConditions]\nwywołuje [SynergyActivationEffect] w zależności od liczby wyposażonych E.G.O „4. Płomyk Zapałki" spełniających warunki z [SynergyActivationConditions_ForthMatchFlame] (wliczając Tożsamości nieuczestniczące w walce)\n\n[SynergyActivationEffect]\n(2) jeżeli w Oknie Składu wyposażono 3/5/7/10 lub więcej [PersonalityCombustion], E.G.O „4. Płomyk Zapałki" zadaje +20%/+40%/+60%/+80% obrażeń\n- wliczając Tożsamości nieuczestniczące w walce\n- zadaje +20% obrażeń za każdego 1 celu poniżej Wagi Ataku tej Umiejętności E.G.O
811. [E.G.O (dodatkowe) [50003] — podsumowanie] (2) 4번째 성냥불 E.G.O 스킬 피해량 증가[TabExplain]
   źródło: Passive_Ego.json :: dataList[id=50003].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: (2) 4th Match Flame E.G.O deals more damage
   PL: — podsumowanie] (2) Umiejętności E.G.O „4. Płomyk Zapałki" zadają więcej obrażeń[TabExplain]
812. [E.G.O (dodatkowe) [50004] — nazwa] 4번째 성냥불
   źródło: Passive_Ego.json :: dataList[id=50004].name
   (powtórzenie elementu 809 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [E.G.O (dodatkowe) [50004] — opis] (3) 4번째 성냥불 E.G.O 스킬 공격 종료 시, 적중한 모든 타겟의 [BurningMatch] 횟수가 1 증가하고 적중한 대상에게 25만큼 [BurningMatch] 위력을 무작위로 나누어 부여 (각 E.G.O마다 턴당 1회 발동)
   źródło: Passive_Ego.json :: dataList[id=50004].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [BurningMatch]
   znaczenie tagów: [BurningMatch] = 4번째 성냥불 / 4th Match Flame
   EN: (3) At 4th Match Flame E.G.O Skill Attack End, inflict +1 [BurningMatch] Count on all targets hit and randomly inflict 25 [BurningMatch] Potency between targets hit (once per turn per E.G.O)
   PL: — opis] (3) na koniec ataku Umiejętności E.G.O „4. Płomyk Zapałki", zwiększa Licznik [BurningMatch] wszystkich trafionych celów o 1 i losowo rozdziela 25 Siły [BurningMatch] między trafionych celów (uruchamia się 1 raz na turę na każde E.G.O)
814. [E.G.O (dodatkowe) [50004] — podsumowanie] (3) 4번째 성냥불 E.G.O 스킬 공격 종료 시, 적중한 타겟에게 [BurningMatch] 부여
   źródło: Passive_Ego.json :: dataList[id=50004].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurningMatch]
   znaczenie tagów: [BurningMatch] = 4번째 성냥불 / 4th Match Flame
   EN: (3) At 4th Match Flame E.G.O Skill Attack End, inflict [BurningMatch] on targets hit
   PL: — podsumowanie] (3) na koniec ataku Umiejętności E.G.O „4. Płomyk Zapałki", nakłada [BurningMatch] na trafione cele
