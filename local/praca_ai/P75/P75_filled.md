# Paczka AI P75 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 11/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P75_3c_przeciwnicy_i_anomalie_cz11.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P75_3c_przeciwnicy_i_anomalie_cz11.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c9p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c9p3
- grupa rozdziału/trybu: `a1c9p3` · plik: `Skills_Abnormality-a1c9p3.json`

1. [Umiejętność wroga [133103] (ulepszenie 1) — nazwa] 재료획득 - 피로 목욕하는 오브제
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].name
   limit: do 60 znaków
   EN: Gather Ingredient - Blood-bathed Objet
   PL: Gather Ingredient - Blood-bathed Objet
2. [Umiejętność wroga [133103] (ulepszenie 1) — opis] 신체관극을 대상으로 우선 지정함\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes Corpus Theaters\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: Corpus Theaters\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
3. [Umiejętność wroga [133103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
4. [Umiejętność wroga [133103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 Licznika [Laceration]
5. [Umiejętność wroga [133103] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Laceration]
6. [Umiejętność wroga [133103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Umiejętność wroga [133103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Inflict 1 [ResultReduction] next turn
   PL: [OnSucceedAttack] nakłada 1 [ResultReduction] w następnej turze
8. [Umiejętność wroga [133103] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133103].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultEnhancement]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [OnSucceedAttack] Gain 1 [ResultEnhancement] next turn
   PL: [OnSucceedAttack] zyskuje 1 [ResultEnhancement] w następnej turze
9. [Umiejętność wroga [133104] (ulepszenie 1) — nazwa] 티비아의 멜로디 - 해체된 것이 해체되지 않은 것을 해체하는 것
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].name
   limit: do 90 znaków
   EN: Tibia's Melody - Anatomization of the Unanatomized by the Anatomized
   PL: Tibia's Melody - Anatomization of the Unanatomized by the Anatomized
10. [Umiejętność wroga [133104] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 피해량이 60%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [MineTheRings] 소멸
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [MineTheRings]
   znaczenie tagów: [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: During the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -60% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [MineTheRings] expires
   PL: w turze, w której ta jednostka ma wyposażoną tę Umiejętność, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nza każdego celu zabitego tą Umiejętnością przywraca 15 SP\n[StartBattle] zyskuje 4 [Protection]\n[WhenUse] zadaje +3% obrażeń za każde 6 łącznie ([Laceration] głównego celu + [Laceration] celu dodatkowego) (maks. 30%)\n[DefeatDuel] zadaje o 60% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EndSkill] [MineTheRings] wygasa
11. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 SP damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 5 obrażeń SP
13. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP (once per Skill)
   PL: [OnSucceedAttack] przywraca 5 SP jednostki (1 raz na Umiejętność)
14. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
16. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 1 [Protection] next turn (once per Skill)
   PL: [OnSucceedAttack] zyskuje 1 [Protection] w następnej turze (1 raz na Umiejętność)
17. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [AttackDmgDown] w następnej turze
19. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn (once per Skill)
   PL: [OnSucceedAttack] zyskuje 1 [AttackDmgUp] w następnej turze (1 raz na Umiejętność)
20. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność wroga [133104] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133104].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
22. [Umiejętność wroga [133105] (ulepszenie 1) — nazwa] 우린 피와 살을 사랑해요
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133105].levelList[level=1].name
   limit: do 60 znaków
   EN: Oh, How We Love the Flesh and the Blood
   PL: Oh, How We Love the Flesh and the Blood
23. [Umiejętność wroga [133105] (ulepszenie 1) — opis] 약지 제자 - 알비나를 대상으로 우선 지정함\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>[AttackDmgDown] 4 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [AttackDmgDown]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: Prioritizes The Ring Apprentice - Albina\n[DefeatDuel] Gain <color=#ff6000><mark=#ff000040><b><u>4 [AttackDmgDown]</u></b></mark></color>
   PL: priorytet: The Ring Apprentice - Albina\n[DefeatDuel] zyskuje <color=#ff6000><mark=#ff000040><b><u>4 [AttackDmgDown]</u></b></mark></color>
24. [Umiejętność wroga [133105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Umiejętność wroga [133105] (ulepszenie 1) — moneta 1, efekt 2 — opis] 이 코인은 체력 피해를 입히지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin does not deal HP damage
   PL: ta Moneta nie zadaje obrażeń HP
26. [Umiejętność wroga [133105] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133105].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [133105] (ulepszenie 1) — moneta 1, efekt 4 — opis] - 대상이 아군이면 이 효과를 대신하여 다음 턴까지 [AttackUp] 6 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133105].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: - If target is an ally, apply 6 [AttackUp] instead of the effect above
   PL: - jeżeli cel jest sojusznikiem, zamiast efektu powyżej nakłada 6 [AttackUp] do następnej tury
28. [Umiejętność wroga [133106] (ulepszenie 1) — nazwa] 전시회 주최
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133106].levelList[level=1].name
   limit: do 40 znaków
   EN: Curating the Exhibition
   PL: Curating the Exhibition
29. [Umiejętność wroga [133106] (ulepszenie 1) — opis] [StartBattle] <color=#ff6000><mark=#ff000040><b><u>[SupportProtect] 2 얻음</u></b></mark></color>\n[WhenUse] 공격자의 공격 종료 전까지 공격자가 보유한 [Laceration] 횟수가 감소하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133106].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [SupportProtect], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>Gain 2 [SupportProtect]</u></b></mark></color>\n[WhenUse] The attacker does not lose [Laceration] Count before Attack End
   PL: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>zyskuje 2 [SupportProtect]</u></b></mark></color>\n[WhenUse] atakujący nie traci Licznika [Laceration] przed końcem Ataku
30. [Umiejętność wroga [133107] (ulepszenie 1) — nazwa] 반달리즘은 사절이랍니다
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133107].levelList[level=1].name
   limit: do 50 znaków
   EN: Please. Vandalism is Prohibited.
   PL: Please. Vandalism is Prohibited.
31. [Umiejętność wroga [133107] (ulepszenie 1) — opis] [DuelCounter]\n[SupportProtect] 전용 스킬\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 1 얻음\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133107].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SupportProtect], [WhenUse], [Protection], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[SupportProtect] exclusive Skill\nCannot be Staggered before using this Skill\n[WhenUse] Gain 1 [Protection]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [DuelCounter]\nUmiejętność wyłącznie dla [SupportProtect]\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[WhenUse] zyskuje 1 [Protection]\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
32. [Umiejętność wroga [133107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
33. [Umiejętność wroga [133107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 1 [Protection] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Protection] w następnej turze
34. [Umiejętność wroga [133107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Umiejętność wroga [133107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność wroga [133108] (ulepszenie 1) — nazwa] 폐장 - 설치미술 제 1호 ‘당신들이 흩뿌린 살과 뼈가 객석이 되어’
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133108].levelList[level=1].name
   limit: do 110 znaków
   EN: Closing Time - Installation Art no. 1: Your Flesh and Bones as the Gallery's Seats
   PL: Closing Time - Installation Art no. 1: Your Flesh and Bones as the Gallery's Seats
37. [Umiejętność wroga [133108] (ulepszenie 1) — opis] [CantDuel]\n레벨이 높은 적을 대상으로 우선 지정함\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 대상의 [Laceration] 8당, 코인 위력 +1 (최대 2)\n[EndSkill] 턴 종료
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133108].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Laceration], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\nPrioritizes enemy with the highest level\nThis Skill does not trigger Defense Skills\n[WhenUse] Coin Power +1 for every 8 [Laceration] on target (max 2)\n[EndSkill] End this turn
   PL: [CantDuel]\npriorytet: wróg z najwyższym poziomem\nta Umiejętność nie uruchamia Umiejętności obrony\n[WhenUse] Moc Monety +1 za każde 8 [Laceration] celu (maks. 2)\n[EndSkill] kończy tę turę
38. [Umiejętność wroga [133108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 현재 체력이 최대 체력의 60% 미만이면, 체력 피해 대신 정신력 피해를 입힘
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At less than 60% HP, deal SP damage instead of HP damage
   PL: [OnSucceedAttack] przy HP niższym niż 60%, zadaje obrażenia SP zamiast obrażeń HP
39. [Umiejętność wroga [133108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태로 만들고 다음 턴에 [LivingSpecimenTheRings]으로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [LivingSpecimenTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenTheRings] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Stagger target and turn target into [LivingSpecimenTheRings] next turn</u></b></mark></color>
   PL: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Oszołomi cel i przekształci go w [LivingSpecimenTheRings] w następnej turze</u></b></mark></color>
40. [Umiejętność wroga [133601] (ulepszenie 1) — nazwa] 도축 - 갈비뼈
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133601].levelList[level=1].name
   limit: do 40 znaków
   EN: Butcher - Ribs
   PL: Butcher - Ribs
41. [Umiejętność wroga [133601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
42. [Umiejętność wroga [133601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
43. [Umiejętność wroga [133601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność wroga [133601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność wroga [133602] (ulepszenie 1) — nazwa] 회전분쇄
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133602].levelList[level=1].name
   limit: do 40 znaków
   EN: Rotator Crush
   PL: Rotator Crush
46. [Umiejętność wroga [133602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133602].levelList[level=1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność wroga [133602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
48. [Umiejętność wroga [133602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
49. [Umiejętność wroga [133602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Agility] w następnej turze
50. [Umiejętność wroga [133603] (ulepszenie 1) — nazwa] 힘줄파열
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133603].levelList[level=1].name
   limit: do 40 znaków
   EN: Tendon Tear
   PL: Tendon Tear
51. [Umiejętność wroga [133603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)
   PL: [WhenUse] Moc Monety +1 za każde 4 [Laceration] celu (maks. 2)
52. [Umiejętność wroga [133603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL: [OnSucceedAttack] nakłada 6 [Laceration]
53. [Umiejętność wroga [133603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Umiejętność wroga [133603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność wroga [133603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [133604] (ulepszenie 1) — nazwa] 파시아 식사 시간이야
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Eat, Fascia
   PL: Time to Eat, Fascia
57. [Umiejętność wroga [133604] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
58. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Laceration]
60. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Laceration]
62. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] zadaje 5 obrażeń SP
64. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 10 회복
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 SP on self
   PL: [OnSucceedAttack] przywraca 10 SP jednostki
65. [Umiejętność wroga [133604] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [HumanFleshTheRings] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133604].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HumanFleshTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HumanFleshTheRings] = 생체 재료 / Corpus Ingredient
   EN: [OnSucceedAttack] Gain 1 [HumanFleshTheRings]
   PL: [OnSucceedAttack] zyskuje 1 [HumanFleshTheRings]
66. [Umiejętność wroga [133605] (ulepszenie 1) — nazwa] 억압당한 육체의 해방
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].name
   limit: do 50 znaków
   EN: Liberation of the Repressed Flesh
   PL: Liberation of the Repressed Flesh
67. [Umiejętność wroga [133605] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 피해량이 60%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [BoneBladeTheRings] 소멸
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [BoneBladeTheRings]
   znaczenie tagów: [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: During the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -60% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [BoneBladeTheRings] expires
   PL: w turze, w której ta jednostka ma wyposażoną tę Umiejętność, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nza każdego celu zabitego tą Umiejętnością przywraca 15 SP\n[StartBattle] zyskuje 4 [Protection]\n[WhenUse] zadaje +3% obrażeń za każde 6 łącznie ([Laceration] głównego celu + [Laceration] celu dodatkowego) (maks. 30%)\n[DefeatDuel] zadaje o 60% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EndSkill] [BoneBladeTheRings] wygasa
68. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność wroga [133605] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133605].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność wroga [133606] (ulepszenie 1) — nazwa] 시작된 전시회
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133606].levelList[level=1].name
   limit: do 40 znaków
   EN: The Exhibition Begins
   PL: The Exhibition Begins
80. [Umiejętność wroga [133606] (ulepszenie 1) — opis] [StartBattle] <color=#ff6000><mark=#ff000040><b><u>[SupportProtect] 1 얻음</u></b></mark></color>\n[StartBattle] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [SupportProtect], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [Agility] = 신속 / Haste
   EN: [StartBattle] <color=#ff6000><mark=#ff000040><b><u> Gain 1 [SupportProtect]</u></b></mark></color>\n[StartBattle] Gain 1 [Agility] next turn
   PL: [StartBattle] <color=#ff6000><mark=#ff000040><b><u> zyskuje 1 [SupportProtect]</u></b></mark></color>\n[StartBattle] zyskuje 1 [Agility] w następnej turze
81. [Umiejętność wroga [133607] (ulepszenie 1) — nazwa] 반달리즘은 사절이야
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133607].levelList[level=1].name
   limit: do 50 znaków
   EN: You there. Vandalism is Prohibited.
   PL: You there. Vandalism is Prohibited.
82. [Umiejętność wroga [133607] (ulepszenie 1) — opis] [DuelCounter]\n[SupportProtect] 전용 스킬\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 1 얻음\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133607].levelList[level=1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [133607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [133607] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133607].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [133607] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133607].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [133607] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133607].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [132701] (ulepszenie 1) — nazwa] 짓밟기
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132701].levelList[level=1].name
   limit: do 40 znaków
   EN: Stomping
   PL: Stomping
88. [Umiejętność wroga [132701] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 4+ [Laceration], Coin Power +1
   PL: jeżeli cel ma 4+ [Laceration], Moc Monety +1
89. [Umiejętność wroga [132701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
90. [Umiejętność wroga [132701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność wroga [132701] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132701].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność wroga [132701] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132701].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ReinforcedTattooSpider], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] If this unit has [ReinforcedTattooSpider], inflict 2 [Paralysis]
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta jednostka ma [ReinforcedTattooSpider], nakłada 2 [Paralysis]
93. [Umiejętność wroga [132702] (ulepszenie 1) — nazwa] 걷어차기
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132702].levelList[level=1].name
   limit: do 40 znaków
   EN: Punting
   PL: Punting
94. [Umiejętność wroga [132702] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132702].levelList[level=1].desc
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [132702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 5
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 5
96. [Umiejętność wroga [132702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Umiejętność wroga [132703] (ulepszenie 1) — nazwa] 원한 스탬핑
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].name
   limit: do 40 znaków
   EN: Stamp of Vengeance
   PL: Stamp of Vengeance
98. [Umiejętność wroga [132703] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 기본 위력 +1 (최대 3)\n[EndSkill] 자신의 [ResentmentSpider]을 전부 소모하고, [DaughterEducationSpider] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [EndSkill], [ResentmentSpider], [DaughterEducationSpider]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [ResentmentSpider] = 중지 - 원한 / The Middle - Grudge; [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: Base Power +1 for every 3 [Laceration] on target (max 3)\n[EndSkill] Consume all [ResentmentSpider] on self and gain 1 [DaughterEducationSpider]
   PL: Moc Bazowa +1 za każde 3 [Laceration] celu (maks. 3)\n[EndSkill] zużywa wszystkie [ResentmentSpider] jednostki i zyskuje 1 [DaughterEducationSpider]
99. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration]
105. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Umiejętność wroga [132703] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132703].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Umiejętność wroga [132704] (ulepszenie 1) — nazwa] 고작 이거에 부서지지 말라고!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].name
   limit: do 60 znaków
   EN: Don't Let Somethin' Like This Break Ya!
   PL: Don't Let Somethin' Like This Break Ya!
109. [Umiejętność wroga [132704] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 추가 타격 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ReinforcedTattooSpider]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 5 Blunt bonus damage On Coin Hit
   PL: [WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], zadaje 5 dodatkowych obrażeń Uderzeniem przy trafieniu Monety
110. [Umiejętność wroga [132704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Umiejętność wroga [132704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding]
   PL: [OnSucceedAttack] nakłada 2 [Binding]
112. [Umiejętność wroga [132704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Umiejętność wroga [132704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 10 dodatkowych obrażeń Uderzeniem
114. [Umiejętność wroga [132704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Umiejętność wroga [132704] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132704].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Paralysis]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Paralysis]
116. [Umiejętność wroga [132705] (ulepszenie 1) — nazwa] 규칙 위반
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132705].levelList[level=1].name
   limit: do 40 znaków
   EN: Rule Violation
   PL: Rule Violation
117. [Umiejętność wroga [132705] (ulepszenie 1) — opis] 피격 시 자신의 [ReinforcedTattooSpider] 1당 이 스킬 1회 재사용 (최대 1회)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132705].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [ReinforcedTattooSpider], [WhenUse], [Laceration]
   znaczenie tagów: [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: When hit, Reuse this Skill once for every [ReinforcedTattooSpider] on self (1 time max)\n[WhenUse] If this unit has [ReinforcedTattooSpider], On Coin Hit, inflict +1 [Laceration] Count
   PL: przy otrzymaniu trafienia używa tej Umiejętności ponownie raz za każde [ReinforcedTattooSpider] jednostki (do 1 razu)\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], przy trafieniu Monety nakłada 1 Licznika [Laceration]
118. [Umiejętność wroga [132705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność wroga [132705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 회복 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 10
   PL: [OnSucceedAttack] obniża Próg Oszołomienia użytkownika o 10
120. [Umiejętność wroga [132706] (ulepszenie 1) — nazwa] 포장 하나 뜯는다!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].name
   limit: do 50 znaków
   EN: Gonna Unbox a Layer of Packaging!
   PL: Gonna Unbox a Layer of Packaging!
121. [Umiejętność wroga [132706] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 추가 타격 피해 10\n[EndSkill] [MiddleFatherSwordOne]이 [MiddleFatherSwordTwo] 상태가 됨
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [ReinforcedTattooSpider], [EndSkill], [MiddleFatherSwordOne], [MiddleFatherSwordTwo]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [EndSkill] = [공격 종료시] / [Attack End]; [MiddleFatherSwordOne] = 봉인된 검 / Sealed Sword; [MiddleFatherSwordTwo] = 1단계 봉인 해제 / First Seal Removed
   EN: [CantChangeTarget]\n[WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Blunt bonus damage on Coin Hit\n[EndSkill] [MiddleFatherSwordOne] becomes [MiddleFatherSwordTwo]
   PL: [CantChangeTarget]\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], zadaje 10 dodatkowych obrażeń Uderzeniem przy trafieniu Monety\n[EndSkill] [MiddleFatherSwordOne] zmienia się w [MiddleFatherSwordTwo]
122. [Umiejętność wroga [132706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Umiejętność wroga [132706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność wroga [132706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [132706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [132706] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Umiejętność wroga [132706] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132706].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność wroga [132707] (ulepszenie 1) — nazwa] 짓밟기
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132707].levelList[level=1].name
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Umiejętność wroga [132707] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 다음 턴에 [ParryingResultUp] 1 얻음 (턴당 2회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132707].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [ParryingResultUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: If target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[DefeatDuel] Gain 1 [ParryingResultUp] next turn (2 times per turn)
   PL: jeżeli cel ma 4+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], nakłada 1 [Laceration] przy trafieniu Monety\n[DefeatDuel] zyskuje 1 [ParryingResultUp] w następnej turze (2 razy na turę)
130. [Umiejętność wroga [132707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Umiejętność wroga [132707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [132707] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132707].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność wroga [132707] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132707].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [132708] (ulepszenie 1) — nazwa] 걷어차기
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132708].levelList[level=1].name
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [132708] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 다음 턴에 [VioletDamageUp] 1 얻음 (턴당 2회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132708].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [VioletDamageUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: If target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[DefeatDuel] Gain 1 [VioletDamageUp] next turn (2 times per turn)
   PL: jeżeli cel ma 4+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], nakłada 1 [Laceration] przy trafieniu Monety\n[DefeatDuel] zyskuje 1 [VioletDamageUp] w następnej turze (2 razy na turę)
136. [Umiejętność wroga [132708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 10
137. [Umiejętność wroga [132708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [132709] (ulepszenie 1) — nazwa] 원한 스탬핑
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].name
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [132709] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 기본 위력 +1 (최대 3)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[EndSkill] 자신의 [ResentmentSpider]을 전부 소모하고, [DaughterEducationSpider] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [EndSkill], [ResentmentSpider], [DaughterEducationSpider]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [EndSkill] = [공격 종료시] / [Attack End]; [ResentmentSpider] = 중지 - 원한 / The Middle - Grudge; [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: Base Power +1 for every 3 [Laceration] on target (max 3)\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[EndSkill] Consume all [ResentmentSpider] on self and gain 1 [DaughterEducationSpider]
   PL: Moc Bazowa +1 za każde 3 [Laceration] celu (maks. 3)\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], nakłada 1 [Laceration] przy trafieniu Monety\n[EndSkill] zużywa wszystkie [ResentmentSpider] jednostki i zyskuje 1 [DaughterEducationSpider]
140. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Laceration]
146. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność wroga [132709] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132709].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [132710] (ulepszenie 1) — nazwa] 후끈해지지 않나?!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].name
   limit: do 40 znaków
   EN: Are Ya Feelin' the Heat?!
   PL: Are Ya Feelin' the Heat?!
150. [Umiejętność wroga [132710] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 추가 타격 피해 10\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Blunt bonus damage On Coin Hit\n[BeforeAttack] At 50% or less HP, deal +40% damage
   PL: [WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], zadaje 10 dodatkowych obrażeń Uderzeniem przy trafieniu Monety\n[BeforeAttack] przy HP równym 50% lub mniej zadaje +40% obrażeń
151. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] nakłada 2 [Combustion]
153. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 추가 타격 피해 15
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 15 dodatkowych obrażeń Uderzeniem
157. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność wroga [132710] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132710].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Paralysis]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Paralysis]
160. [Umiejętność wroga [132711] (ulepszenie 1) — nazwa] 규칙 위반
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132711].levelList[level=1].name
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Umiejętność wroga [132711] (ulepszenie 1) — opis] 피격 시 <color=#ff6000><mark=#ff000040><b><u>자신의 [ReinforcedTattooSpider] 1당 이 스킬 1회 재사용</u></b></mark></color> (최대 1회)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132711].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ReinforcedTattooSpider], [WhenUse], [Laceration], [BeforeAttack]
   znaczenie tagów: [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: When hit, <color=#ff6000><mark=#ff000040><b><u>Reuse this Skill once for every [ReinforcedTattooSpider] on self</u></b></mark></color> (1 time max)\n[WhenUse] If this unit has [ReinforcedTattooSpider], On Coin Hit, inflict +1 [Laceration] Count\n[BeforeAttack] At 50% or less HP, deal +40% damage
   PL: przy otrzymaniu trafienia <color=#ff6000><mark=#ff000040><b><u>używa tej Umiejętności ponownie raz za każde [ReinforcedTattooSpider] jednostki</u></b></mark></color> (do 1 razu)\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], przy trafieniu Monety nakłada 1 Licznika [Laceration]\n[BeforeAttack] przy HP równym 50% lub mniej zadaje +40% obrażeń
162. [Umiejętność wroga [132711] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Umiejętność wroga [132711] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 회복 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [132712] (ulepszenie 1) — nazwa] 두번째 포장지까지 벗기게 되는군.
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].name
   limit: do 70 znaków
   EN: Looks Like I Gotta Unbox the Second Layer, too.
   PL: Looks Like I Gotta Unbox the Second Layer, too.
165. [Umiejętność wroga [132712] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 추가 타격 피해 10\n[EndSkill] [MiddleFatherSwordTwo] 상태가 [MiddleFatherSwordThree] 상태가 됨
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [ReinforcedTattooSpider], [EndSkill], [MiddleFatherSwordTwo], [MiddleFatherSwordThree]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [EndSkill] = [공격 종료시] / [Attack End]; [MiddleFatherSwordTwo] = 1단계 봉인 해제 / First Seal Removed; [MiddleFatherSwordThree] = 2단계 봉인 해제 / Second Seal Removed
   EN: [CantChangeTarget]\n[WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Blunt bonus damage on Coin Hit\n[EndSkill] [MiddleFatherSwordTwo] becomes [MiddleFatherSwordThree]
   PL: [CantChangeTarget]\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], zadaje 10 dodatkowych obrażeń Uderzeniem przy trafieniu Monety\n[EndSkill] [MiddleFatherSwordTwo] zmienia się w [MiddleFatherSwordThree]
166. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [132712] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132712].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 5 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 5 [Vulnerable]
174. [Umiejętność wroga [132801] (ulepszenie 1) — nazwa] 몸 좀 풀어볼까?
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].name
   limit: do 40 znaków
   EN: Time for Some Warm-up!
   PL: Time for Some Warm-up!
175. [Umiejętność wroga [132801] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면 기본 위력 +2\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 5+ [Laceration], Base Power +2\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: jeżeli cel ma 5+ [Laceration], Moc Bazowa +2\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
176. [Umiejętność wroga [132801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 3 dodatkowe obrażenia Uderzeniem
177. [Umiejętność wroga [132801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [132801] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [132801] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 3 Blunt bonus damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 3 dodatkowe obrażenia Uderzeniem
180. [Umiejętność wroga [132801] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132801].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ReinforcedTattooSpiderDaughter], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] If this unit has [ReinforcedTattooSpiderDaughter], inflict 2 [Binding]
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughter], nakłada 2 [Binding]
181. [Umiejętność wroga [132802] (ulepszenie 1) — nazwa] 욜라 패기
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].name
   limit: do 40 znaków
   EN: Totally Badass Ass-kicking
   PL: Totally Badass Ass-kicking
182. [Umiejętność wroga [132802] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면 기본 위력 +2\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 코인 적중시 [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughter]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos
   EN: If target has 5+ [Laceration], Base Power +2\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughter], inflict 2 [Laceration] On Coin Hit
   PL: jeżeli cel ma 5+ [Laceration], Moc Bazowa +2\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughter], nakłada 2 [Laceration] przy trafieniu Monety
183. [Umiejętność wroga [132802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 5 dodatkowych obrażeń Uderzeniem
184. [Umiejętność wroga [132802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [132802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [132802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [132802] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [GotACompliment]가 4 이상이면, 이 코인 3회 재사용
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132802].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GotACompliment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GotACompliment] = 칭찬 받았다! / I Got Praised!
   EN: [OnSucceedAttack] At 4+ [GotACompliment], Reuse this Coin 3 times
   PL: [OnSucceedAttack] przy 4+ [GotACompliment], używa Monety ponownie 3 razy
188. [Umiejętność wroga [132803] (ulepszenie 1) — nazwa] 해결사 배 가르기!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132803].levelList[level=1].name
   limit: do 40 znaków
   EN: Fixer Disemboweling!
   PL: Fixer Disemboweling!
189. [Umiejętność wroga [132803] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpider] 상태일 때 열선[TabExplain] 효과가 적용됨\n대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[EndSkill] 자신의 [GotACompliment]가 2 이상이면, 다음 턴에 [VioletDamageUp] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132803].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpider], [TabExplain], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughter], [EndSkill], [GotACompliment], [VioletDamageUp]
   znaczenie tagów: [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [EndSkill] = [공격 종료시] / [Attack End]; [GotACompliment] = 칭찬 받았다! / I Got Praised!; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpider] state, this Skill activates its Thermal Blade effects\nIf target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughter], inflict +1 [Laceration] Count On Coin Hit\n[EndSkill] At 2+ [GotACompliment], gain 1 [VioletDamageUp] next turn
   PL: Umiejętność termicznego ostrza.\nw stanie [HeatingWireOnSpider] ta Umiejętność uruchamia swoje efekty termicznego ostrza\njeżeli cel ma 4+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughter], przy trafieniu Monety nakłada 1 Licznika [Laceration]\n[EndSkill] przy 2+ [GotACompliment], zyskuje 1 [VioletDamageUp] w następnej turze
190. [Umiejętność wroga [132803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [132803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [132804] (ulepszenie 1) — nazwa] 십자난무!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].name
   limit: do 40 znaków
   EN: Crossing Dervish!
   PL: Crossing Dervish!
193. [Umiejętność wroga [132804] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpider] 상태일 때 열선[TabExplain] 효과가 적용됨\n대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpider], [TabExplain], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughter], [DefeatDuel]
   znaczenie tagów: [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpider] state, this Skill activates its Thermal Blade effects\nIf target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughter], inflict +1 [Laceration] Count On Coin Hit\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: Umiejętność termicznego ostrza.\nw stanie [HeatingWireOnSpider] ta Umiejętność uruchamia swoje efekty termicznego ostrza\njeżeli cel ma 4+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughter], przy trafieniu Monety nakłada 1 Licznika [Laceration]\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
194. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 Blunt bonus damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 5 dodatkowych obrażeń Uderzeniem
202. [Umiejętność wroga [132804] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132804].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Umiejętność wroga [132805] (ulepszenie 1) — nazwa] 바이올렛 브레이크 슬램!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].name
   limit: do 40 znaków
   EN: Violet~ Breaking Slam!
   PL: Violet~ Breaking Slam!
204. [Umiejętność wroga [132805] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpider] 상태일 때 열선[TabExplain] 효과가 적용됨\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[WhenUse] 자신의 체력이 40% 이하일 때, 피해량 +60%\n[WhenUse] 자신의 [GotACompliment]가 5 이상이면, 코인 적중시 50% 확률로 [Paralysis] 1 부여\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [ResentmentSpiderDaughter]을 전부 소모하고, [GotACompliment] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpider], [TabExplain], [WhenUse], [ReinforcedTattooSpiderDaughter], [Laceration], [GotACompliment], [Paralysis], [DefeatDuel], [EndSkill], [ResentmentSpiderDaughter]
   znaczenie tagów: [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [Laceration] = 출혈 / Bleed; [GotACompliment] = 칭찬 받았다! / I Got Praised!; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpider] state, this Skill activates its Thermal Blade effects\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughter], inflict +1 [Laceration] Count On Coin Hit\n[WhenUse] At 40% or less HP, deal +60% damage\n[WhenUse] At 5+ [GotACompliment], 50% chance to inflict 1 [Paralysis] On Coin Hit\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[EndSkill] Consume all [ResentmentSpiderDaughter] on self and gain 1 [GotACompliment]
   PL: Umiejętność termicznego ostrza.\nw stanie [HeatingWireOnSpider] ta Umiejętność uruchamia swoje efekty termicznego ostrza\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughter], przy trafieniu Monety nakłada 1 Licznika [Laceration]\n[WhenUse] przy HP równym 40% lub mniej zadaje +60% obrażeń\n[WhenUse] przy 5+ [GotACompliment], przy trafieniu Monety nakłada 1 [Paralysis] z szansą 50%\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EndSkill] zużywa wszystkie [ResentmentSpiderDaughter] jednostki i zyskuje 1 [GotACompliment]
205. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Raise Stagger Threshold by 5
   PL: [UnBrokenCoinOnSucceedAttack] podnosi Próg Oszołomienia o 5
214. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [132805] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132805].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [132806] (ulepszenie 1) — nazwa] 가만 안둬
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132806].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Get You Back for This...!
   PL: I'll Get You Back for This...!
217. [Umiejętność wroga [132806] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpider] 상태일 때 열선[TabExplain] 효과가 적용됨\n피격 시 <color=#ff6000><mark=#ff000040><b><u>자신의 [ReinforcedTattooSpiderDaughter] 1당 이 스킬 1회 재사용</u></b></mark></color> (최대 2회)\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 코인 적중시 [Laceration] 1 부여\n[WhenUse] 자신의 체력이 40% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132806].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HeatingWireOnSpider], [TabExplain], [ReinforcedTattooSpiderDaughter], [WhenUse], [Laceration]
   znaczenie tagów: [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpider] state, this Skill activates its Thermal Blade effects\nWhen Hit, <color=#ff6000><mark=#ff000040><b><u>Reuse this Skill once for every [ReinforcedTattooSpiderDaughter] on self</u></b></mark></color> (2 times max)\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughter], inflict 1 [Laceration] On Coin Hit\n[WhenUse] At 40% or less HP, deal +40% damage
   PL: Umiejętność termicznego ostrza.\nw stanie [HeatingWireOnSpider] ta Umiejętność uruchamia swoje efekty termicznego ostrza\nprzy otrzymaniu trafienia <color=#ff6000><mark=#ff000040><b><u>używa tej Umiejętności ponownie raz za każde 1 [ReinforcedTattooSpiderDaughter] jednostki</u></b></mark></color> (do 2 razy)\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughter], nakłada 1 [Laceration] przy trafieniu Monety\n[WhenUse] przy HP równym 40% lub mniej zadaje +40% obrażeń
218. [Umiejętność wroga [132806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [132806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] nakłada 1 [Laceration]
220. [Umiejętność wroga [132806] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 회복 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132806].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [134101] (ulepszenie 1) — nazwa] 짓밟기!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134101].levelList[level=1].name
   limit: do 40 znaków
   EN: Stomping!
   PL: Stomping!
222. [Umiejętność wroga [134101] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 다음 턴에 [SkillPowerUp] 1 얻음 (턴당 2회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134101].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [SkillPowerUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [SkillPowerUp] = 기본 위력 증가 / Base Power Up
   EN: If target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[DefeatDuel] Gain 1 [SkillPowerUp] next turn (2 times per turn)
   PL: jeżeli cel ma 4+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], nakłada 1 [Laceration] przy trafieniu Monety\n[DefeatDuel] zyskuje 1 [SkillPowerUp] w następnej turze (2 razy na turę)
223. [Umiejętność wroga [134101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
224. [Umiejętność wroga [134101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność wroga [134101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [134101] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134101].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [134102] (ulepszenie 1) — nazwa] 걷어차기!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134102].levelList[level=1].name
   limit: do 40 znaków
   EN: Punting!
   PL: Punting!
228. [Umiejętność wroga [134102] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 다음 턴에 [VioletDamageUp] 1 얻음 (턴당 2회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134102].levelList[level=1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [134102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 15
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 15
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 15
230. [Umiejętność wroga [134102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 15
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [134103] (ulepszenie 1) — nazwa] 즉결 처형 스탬핑!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].name
   limit: do 60 znaków
   EN: Stamp of Complete and Total Extermination!
   PL: Stamp of Complete and Total Extermination!
232. [Umiejętność wroga [134103] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 기본 위력 +1 (최대 3)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[EndSkill] 자신의 [ResentmentSpider]을 전부 소모하고, [DaughterEducationSpider] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].desc
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [Laceration]
239. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Laceration]
241. [Umiejętność wroga [134103] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134103].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [134104] (ulepszenie 1) — nazwa] 슬슬 녹아 죽을 차례다
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Melt Away and Die
   PL: Time to Melt Away and Die
243. [Umiejętność wroga [134104] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 추가 참격 피해 10\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Slash bonus damage On Coin Hit\n[BeforeAttack] At 50% or less HP, deal +40% damage
   PL: [WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], zadaje 10 dodatkowych obrażeń Cięciem przy trafieniu Monety\n[BeforeAttack] przy HP równym 50% lub mniej zadaje +40% obrażeń
244. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL: [OnSucceedAttack] nakłada 4 [Combustion]
246. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 추가 참격 피해 15
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 Slash bonus damage
   PL: [OnSucceedAttack] zadaje 15 dodatkowych obrażeń Cięciem
250. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [134104] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134104].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [134105] (ulepszenie 1) — nazwa] 규칙 위반!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134105].levelList[level=1].name
   limit: do 40 znaków
   EN: Rule Violation!
   PL: Rule Violation!
254. [Umiejętność wroga [134105] (ulepszenie 1) — opis] 피격 시 <color=#ff6000><mark=#ff000040><b><u>자신의 [ReinforcedTattooSpider] 1당 이 스킬 1회 재사용</u></b></mark></color> (최대 1회)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134105].levelList[level=1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [134105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [134105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 회복 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [134106] (ulepszenie 1) — nazwa] 레바테인 - 여기까지 꺼내는 것도 오랜만이군!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].name
   limit: do 90 znaków
   EN: Lævateinn - Been a While Since I Had to Unbox the Whole Thing!
   PL: Lævateinn - Been a While Since I Had to Unbox the Whole Thing!
258. [Umiejętność wroga [134106] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 추가 참격 피해 10\n[EndSkill] [MiddleFatherSwordThree] 상태가 [MiddleFatherSwordFour]이 됨
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [ReinforcedTattooSpider], [EndSkill], [MiddleFatherSwordThree], [MiddleFatherSwordFour]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [EndSkill] = [공격 종료시] / [Attack End]; [MiddleFatherSwordThree] = 2단계 봉인 해제 / Second Seal Removed; [MiddleFatherSwordFour] = 레바테인 / Lævateinn
   EN: [CantChangeTarget]\n[WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Slash bonus damage on Coin Hit\n[EndSkill] [MiddleFatherSwordThree] becomes [MiddleFatherSwordFour]
   PL: [CantChangeTarget]\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpider], zadaje 10 dodatkowych obrażeń Cięciem przy trafieniu Monety\n[EndSkill] [MiddleFatherSwordThree] zmienia się w [MiddleFatherSwordFour]
259. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 Slash bonus damage
   PL: [OnSucceedAttack] zadaje 10 dodatkowych obrażeń Cięciem
261. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [134106] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134106].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 10 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 10 [Vulnerable]
267. [Umiejętność wroga [134107] (ulepszenie 1) — nazwa] 배떼지를 갈라주지
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Gut Ya Like a Fish
   PL: I'll Gut Ya Like a Fish
268. [Umiejętność wroga [134107] (ulepszenie 1) — opis] [BeforeUse] 자신의 정신력 10 감소\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[DefeatDuel] 다음 턴에 [SkillPowerUp] 1 얻음 (턴당 2회)\n[BeforeAttack] (이 스킬의 코인 수 x 2)만큼 [Combustion] 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [DefeatDuel], [SkillPowerUp], [BeforeAttack], [Combustion]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [SkillPowerUp] = 기본 위력 증가 / Base Power Up; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn
   EN: [BeforeUse] Lose 10 SP\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] Gain 1 [SkillPowerUp] next turn (2 times per turn)\n[BeforeAttack] Gain (# of Coins in this Skill x 2) [Combustion]
   PL: [BeforeUse] traci 10 SP\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[DefeatDuel] zyskuje 1 [SkillPowerUp] w następnej turze (2 razy na turę)\n[BeforeAttack] zyskuje (liczba Monet tej Umiejętności x 2) [Combustion]
269. [Umiejętność wroga [134107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [134107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 흐트러짐 손상 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Raise Stagger Threshold by 10
   PL: [UnBrokenCoinOnSucceedAttack] podnosi Próg Oszołomienia o 10
271. [Umiejętność wroga [134107] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [134107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [134107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 10 [Combustion] i 2 Licznika [Combustion]
274. [Umiejętność wroga [134108] (ulepszenie 1) — nazwa] 칼빵 [레바테인]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].name
   limit: do 40 znaków
   EN: Gut Stab [Lævateinn]
   PL: Gut Stab [Lævateinn]
275. [Umiejętność wroga [134108] (ulepszenie 1) — opis] [BeforeUse] 자신의 정신력 10 감소\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%\n[BeforeAttack] (이 스킬의 코인 수 x 2)만큼 [Combustion] 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [DefeatDuel], [BeforeAttack], [Combustion]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn
   EN: [BeforeUse] Lose 10 SP\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] At 50%- HP, deal +40% damage\n[BeforeAttack] Gain (# of Coins in this Skill x 2) [Combustion]
   PL: [BeforeUse] traci 10 SP\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[BeforeAttack] przy HP równym 50% lub mniej zadaje +40% obrażeń\n[BeforeAttack] zyskuje (liczba Monet tej Umiejętności x 2) [Combustion]
276. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 10 Blunt bonus damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 10 dodatkowych obrażeń Uderzeniem
278. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion]
   PL: [OnSucceedAttack] nakłada 10 [Combustion]
282. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 4 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +4 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Combustion]
284. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność wroga [134108] (ulepszenie 1) — moneta 5, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134108].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Combustion]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Combustion]
286. [Umiejętność wroga [134109] (ulepszenie 1) — nazwa] ...즉결처형[레바테인]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].name
   limit: do 70 znaków
   EN: ... Complete and Total Extermination [Lævateinn]
   PL: ... Complete and Total Extermination [Lævateinn]
287. [Umiejętność wroga [134109] (ulepszenie 1) — opis] [BeforeUse] 자신의 정신력 10 감소\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +60%\n[BeforeAttack] (이 스킬의 코인 수 x 2)만큼 [Combustion] 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [DefeatDuel], [BeforeAttack], [Combustion]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn
   EN: [BeforeUse] Lose 10 SP\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] At 50%- HP, deal +60% damage\n[BeforeAttack] Gain (# of Coins in this Skill x 2) [Combustion]
   PL: [BeforeUse] traci 10 SP\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[BeforeAttack] przy HP równym 50% lub mniej zadaje +60% obrażeń\n[BeforeAttack] zyskuje (liczba Monet tej Umiejętności x 2) [Combustion]
288. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL: [OnSucceedAttack] nakłada 5 [Combustion]
290. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Combustion]
292. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 10 Slash bonus damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 10 dodatkowych obrażeń Cięciem
293. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 5, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 관통 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 10 Pierce bonus damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 10 dodatkowych obrażeń Przebiciem
300. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 5, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#4].coindescs[#2].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Umiejętność wroga [134109] (ulepszenie 1) — moneta 5, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134109].levelList[level=1].coinlist[#4].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ReinforcedTattooSpider], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] If this unit has [ReinforcedTattooSpider], inflict 5 [Paralysis]
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta jednostka ma [ReinforcedTattooSpider], nakłada 5 [Paralysis]
302. [Umiejętność wroga [134110] (ulepszenie 1) — nazwa] 규칙 위반!!
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134110].levelList[level=1].name
   limit: do 40 znaków
   EN: Rule Violation!!
   PL: Rule Violation!!
303. [Umiejętność wroga [134110] (ulepszenie 1) — opis] 피격 시 자신의 [ReinforcedTattooSpider] 1당 이 스킬 1회 재사용 (최대 1회)\n[BeforeUse] 자신의 정신력 10 감소\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%\n[BeforeAttack] (이 스킬의 코인 수 x 2)만큼 [Combustion] 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134110].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [ReinforcedTattooSpider], [BeforeUse], [BeforeAttack], [Combustion]
   znaczenie tagów: [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [BeforeUse] = [사용전] / [Before Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn
   EN: When Hit, Reuse this Skill once for every [ReinforcedTattooSpider] on self (1 time max)\n[BeforeUse] Lose 10 SP\n[BeforeAttack] At 50% or less HP, deal +40% damage\n[BeforeAttack] Gain (# of Coins in this Skill x 2) [Combustion]
   PL: przy otrzymaniu trafienia używa tej Umiejętności ponownie raz za każde [ReinforcedTattooSpider] jednostki (do 1 razu)\n[BeforeUse] traci 10 SP\n[BeforeAttack] przy HP równym 50% lub mniej zadaje +40% obrażeń\n[BeforeAttack] zyskuje (liczba Monet tej Umiejętności x 2) [Combustion]
304. [Umiejętność wroga [134110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność wroga [134110] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134110].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Combustion]
306. [Umiejętność wroga [133901] (ulepszenie 1) — nazwa] 황제의 주먹
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133901].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Fist
   PL: The Emperor's Fist
307. [Umiejętność wroga [133901] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 1개당, 피해량 +20% (최대 100%)\n대상의 [OffenseBug] 2당, 피해량 +10%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133901].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OffenseBug]
   znaczenie tagów: [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: Deal +20% damage for every type of negative effect on target (max 100%)\nDeal +10% damage for every 2 [OffenseBug] on target
   PL: zadaje +20% obrażeń za każdy typ negatywnych efektów celu (maks. 100%)\nzadaje +10% obrażeń za każde 2 [OffenseBug] celu
308. [Umiejętność wroga [133901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여, 2 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 Potency and +2 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] nakłada 2 Siły i 2 Licznika losowego statusu spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]
309. [Umiejętność wroga [133901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여, 2 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [133902] (ulepszenie 1) — nazwa] 황제의 채찍과 주먹
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Whip & Fist
   PL: The Emperor's Whip & Fist
311. [Umiejętność wroga [133902] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 1개당, 피해량 +20% (최대 100%)\n대상의 [OffenseBug] 2당, 피해량 +10%\n[DefeatDuel] 피해량 80% 감소, 해당 피해로 흐트러짐이 발생하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [OffenseBug], [DefeatDuel]
   znaczenie tagów: [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +20% damage for every type of negative effect on target (max 100%)\nDeal +10% damage for every 2 [OffenseBug] on target\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: zadaje +20% obrażeń za każdy typ negatywnych efektów celu (maks. 100%)\nzadaje +10% obrażeń za każde 2 [OffenseBug] celu\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
312. [Umiejętność wroga [133902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność wroga [133902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 3 부여, 3 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 Potency and +3 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] nakłada 3 Siły i 3 Licznika losowego statusu spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]
314. [Umiejętność wroga [133902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność wroga [133902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 3 부여, 3 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [133902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [133902] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133902].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 5 [Breath] and +3 [Breath] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 5 [Breath] i 3 Licznika [Breath]
318. [Umiejętność wroga [133903] (ulepszenie 1) — nazwa] 황제의 포식
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133903].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Devouring
   PL: The Emperor's Devouring
319. [Umiejętność wroga [133903] (ulepszenie 1) — opis] [WhenUse] 합을 진행한 스킬의 <color=#ff6000><mark color=#ff000040><b><u>[SuperCoin] 1개당, 기본 위력 + 10</color></mark></b></u>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [WhenUse], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] <color=#ff6000><mark color=#ff000040><b><u>Base Power +10 for every [SuperCoin] on the Skill</color></mark></b></u> this unit Clashed with
   PL: [WhenUse] <color=#ff6000><mark color=#ff000040><b><u>Moc Bazowa +10 za każdy [SuperCoin] Umiejętności</u></b></mark></color>, z którą stoczono Starcie
320. [Umiejętność wroga [133903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ExtractCoin]
   znaczenie tagów: [ExtractCoin] = 적출 코인 / Excision Coin
   EN: [ExtractCoin]
   PL: [ExtractCoin]
321. [Umiejętność wroga [133903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 이로운 효과 모두 흡수
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Absorb all positive effects from the target
   PL: [UnBrokenCoinOnSucceedAttack] absorbuje wszystkie pozytywne efekty celu
322. [Umiejętność wroga [133903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark color=#ff000040><b><u>[OffenseBug] 절반 감소</color></mark></b></u> (소수점 버림)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [OnSucceedAttack], [OffenseBug]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: [OnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>Halve the [OffenseBug] Stack on target</color></mark></b></u> (rounded down)
   PL: [OnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>zmniejsza Licznik [OffenseBug] celu o połowę</u></b></mark></color> (zaokrąglając w dół)
323. [Umiejętność wroga [133903] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상의 부정적인 효과 모두 흡수\n- 해당 효과 발동 후 자신에게 [DefenseBug]이 없으면, 다음 턴에 [ResultReduction] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133903].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [DefenseBug], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseBug] = 방어 해충[바퀴] / Protecting Pest [Roaches]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Absorb all negative effects from the target\n- After activating the above effect, if this unit does not have [DefenseBug], gain 2 [ResultReduction] next turn
   PL: [OnSucceedAttack] absorbuje wszystkie negatywne efekty celu\n- po uruchomieniu powyższego efektu, jeżeli ta jednostka nie ma [DefenseBug], zyskuje 2 [ResultReduction] w następnej turze
324. [Umiejętność wroga [133904] (ulepszenie 1) — nazwa] 황제의 태형
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133904].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Flogging
   PL: The Emperor's Flogging
325. [Umiejętność wroga [133904] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 1개당, 피해량 +20% (최대 100%)\n대상의 [OffenseBug] 2당, 피해량 +10%\n[WhenUse] 자신의 [Charge] 횟수 10 증가\n[StartDuel] 자신의 [Charge] 횟수 5 감소\n[DefeatDuel] 피해량 80% 감소, 해당 피해로 흐트러짐이 발생하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133904].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [OffenseBug], [WhenUse], [Charge], [StartDuel], [DefeatDuel]
   znaczenie tagów: [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]; [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [StartDuel] = [합 시작 시] / [Clash Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +20% damage for every type of negative effect on target (max 100%)\nDeal +10% damage for every 2 [OffenseBug] on target\n[WhenUse] Gain +10 [Charge] Count\n[StartDuel] Lose 5 [Charge] Count\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: zadaje +20% obrażeń za każdy typ negatywnych efektów celu (maks. 100%)\nzadaje +10% obrażeń za każde 2 [OffenseBug] celu\n[WhenUse] zyskuje 10 Licznika [Charge]\n[StartDuel] traci 5 Licznika [Charge]\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
326. [Umiejętność wroga [133904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [133904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 3 부여, 3 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność wroga [133904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Umiejętność wroga [133904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수를 모두 소모하여 + 피해량 (소모한 [Charge] 횟수 x 20)%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Consume all [Charge] Count on self and deal +([Charge] Count consumed x 20)% damage
   PL: [OnSucceedAttack] zużywa wszystkie Liczniki [Charge] jednostki i zadaje +(zużyte Liczniki [Charge] x 20)% obrażeń
330. [Umiejętność wroga [133905] (ulepszenie 1) — nazwa] 바퀴행진
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133905].levelList[level=1].name
   limit: do 40 znaków
   EN: March of Roaches
   PL: March of Roaches
331. [Umiejętność wroga [133905] (ulepszenie 1) — opis] 대상의 [OffenseBug] 2당, 피해량 +10%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OffenseBug]
   znaczenie tagów: [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: Deal +10% damage for every 2 [OffenseBug] on target
   PL: zadaje +10% obrażeń za każde 2 [OffenseBug] celu
332. [Umiejętność wroga [133905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [OffenseBug] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OffenseBug]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: [OnSucceedAttack] Inflict 2 [OffenseBug]
   PL: [OnSucceedAttack] nakłada 2 [OffenseBug]
333. [Umiejętność wroga [133905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [OffenseBug] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [133905] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [OffenseBug] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OffenseBug]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: [OnSucceedAttack] Inflict 3 [OffenseBug]
   PL: [OnSucceedAttack] nakłada 3 [OffenseBug]
335. [Umiejętność wroga [133906] (ulepszenie 1) — nazwa] 황제의 울림
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133906].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Quaking
   PL: The Emperor's Quaking
336. [Umiejętność wroga [133906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] nakłada 5 [Vibration]
337. [Umiejętność wroga [133906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [133906] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133906].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Vibration]
339. [Umiejętność wroga [133906] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 무작위 [Vibration]으로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133906].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into a random [Vibration] type
   PL: [OnSucceedAttack] uruchamia [Switch_Vibration], przekształcając je w losowy [Vibration]
340. [Umiejętność wroga [133906] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133906].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion]; następnie zmniejsza Licznik [Vibration] celu o 1
341. [Umiejętność wroga [133907] (ulepszenie 1) — nazwa] 황제의 적출
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Excision
   PL: The Emperor's Excision
342. [Umiejętność wroga [133907] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 1개당, 피해량 +20% (최대 100%)\n대상의 [OffenseBug] 2당, 피해량 +10%\n[WhenUse] 합을 진행한 스킬의 <color=#ff6000><mark color=#ff000040><b><u>[SuperCoin] 1개당, 기본 위력 + 20</color></mark></b></u>\n[DefeatDuel] 피해량 80% 감소, 해당 피해로 흐트러짐이 발생하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [OffenseBug], [WhenUse], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +20% damage for every type of negative effect on target (max 100%)\nDeal +10% damage for every 2 [OffenseBug] on target\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>Base Power +20 for every [SuperCoin] on the Skill</color></mark></b></u> this unit Clashed with\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: zadaje +20% obrażeń za każdy typ negatywnych efektów celu (maks. 100%)\nzadaje +10% obrażeń za każde 2 [OffenseBug] celu\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>Moc Bazowa +20 za każdy [SuperCoin] Umiejętności</u></b></mark></color>, z którą stoczono Starcie\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
343. [Umiejętność wroga [133907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [133907] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 3 부여, 3 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Umiejętność wroga [133907] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [AttackDown] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [AttackDown]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [AttackDown]
346. [Umiejętność wroga [133907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Umiejętność wroga [133907] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 3 부여, 3 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [133907] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [DefenseDown] 5 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133907].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [DefenseDown]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [DefenseDown]
349. [Umiejętność wroga [133908] (ulepszenie 1) — nazwa] 황제의 만찬
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Feast
   PL: The Emperor's Feast
350. [Umiejętność wroga [133908] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 1개당, 피해량 +20% (최대 100%)\n대상의 [OffenseBug] 2당, 피해량 +10%\n[WhenUse] 합을 진행한 스킬의 <color=#ff6000><mark color=#ff000040><b><u>[SuperCoin] 1개당, 기본 위력 + 20</color></mark></b></u>\n[DefeatDuel] 피해량 80% 감소, 해당 피해로 흐트러짐이 발생하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].desc
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Umiejętność wroga [133908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [133908] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 보호막 제거
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Remove target's Shield
   PL: [UnBrokenCoinOnSucceedAttack] usuwa Tarczę celu
353. [Umiejętność wroga [133908] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność wroga [133908] (ulepszenie 1) — moneta 2, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność wroga [133908] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 본체와 부위 최대 체력의 25% 만큼 체력 회복
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133908].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] The Core and the Part both heal 25% of their respective max HP
   PL: [UnBrokenCoinOnSucceedAttack] przywraca Korpusowi i Części po 25% ich Maks. HP
356. [Umiejętność wroga [133909] (ulepszenie 1) — nazwa] ‘…아들, 심장을 노려야지’
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].name
   limit: do 60 znaków
   EN: 'Son, don't forget to go for the heart.'
   PL: 'Son, don't forget to go for the heart.'
357. [Umiejętność wroga [133909] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse] [Breath] 10 얻음, 자신의 [Breath] 횟수 4 증가\n[WinDuel] [Breath] 10 얻음\n[DefeatDuel] 피해량 80% 감소하고, 크리티컬이 발동하지 않음.\n해당 피해로 흐트러짐이 발생하지 않음\n[DefeatDuel] 다음 턴에 [Vulnerable] 5 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [Breath], [WinDuel], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [CantChangeTarget]\n[WhenUse] Gain 10 [Breath] and +4 [Breath] Count\n[WinDuel] Gain 10 [Breath]\n[DefeatDuel] Deal -80% damage and does not hit Critically\nDamage dealt by this Skill cannot Stagger the target\n[DefeatDuel] Gain 5 [Vulnerable] next turn
   PL: [CantChangeTarget]\n[WhenUse] zyskuje 10 [Breath] i 4 Licznika [Breath]\n[WinDuel] zyskuje 10 [Breath]\n[DefeatDuel] zadaje o 80% mniej obrażeń i nie zadaje trafienia krytycznego.\nobrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[DefeatDuel] zyskuje 5 [Vulnerable] w następnej turze
358. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 5 부여, 2 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 Potency and +2 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: [OnSucceedAttack] nakłada 5 Siły i 2 Licznika losowego statusu spośród [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]
360. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 대상의 최대 체력 25% 만큼 오만 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal Pride damage equal to 25% of target's max HP
   PL: [CriticalOnSucceedAttack] zadaje obrażenia Pychy równe 25% Maks. HP celu
361. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 5 부여, 2 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] 대상의 최대 체력 25% 만큼 오만 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 5 부여, 2 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 대상의 최대 체력 25% 만큼 오만 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 5 부여, 2 횟수 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Umiejętność wroga [133909] (ulepszenie 1) — moneta 4, efekt 3 — opis] [CriticalOnSucceedAttack] 대상의 최대 체력 25% 만큼 오만 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133909].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Umiejętność wroga [133910] (ulepszenie 1) — nazwa] 황제의 방패
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133910].levelList[level=1].name
   limit: do 40 znaków
   EN: The Emperor's Shield
   PL: The Emperor's Shield
371. [Umiejętność wroga [133910] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>지정한 대상에게 이번 턴 동안 공격 스킬로 받는 피해 50% 감소</u></b></mark></color>\n[WinDuel] 다음 턴에 [Binding] 3 부여\n[DefeatDuel] 대상의 정신력 15 회복
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133910].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WinDuel], [Binding], [DefeatDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Binding] = 속박 / Bind; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <color=#ff6000><mark=#ff000040><b><u>For this turn, take -50% damage from the targeted unit's Attack Skills</u></b></mark></color>\n[WinDuel] Inflict 3 [Binding] next turn\n[DefeatDuel] Target heals 15 SP
   PL: <color=#ff6000><mark=#ff000040><b><u>w tej turze otrzymuje o 50% mniej obrażeń od Umiejętności ataku wskazanej jednostki</u></b></mark></color>\n[WinDuel] nakłada 3 [Binding] w następnej turze\n[DefeatDuel] cel przywraca 15 SP
372. [Umiejętność wroga [133910] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133910].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność wroga [134502] (ulepszenie 1) — nazwa] 해체
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].name
   limit: do 40 znaków
   EN: Anatomize
   PL: Anatomize
374. [Umiejętność wroga [134502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
375. [Umiejętność wroga [134502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność wroga [134502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Umiejętność wroga [134502] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność wroga [134502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność wroga [134502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność wroga [134502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [134503] (ulepszenie 1) — nazwa] 재료획득 - 피로 목욕하는 오브제
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność wroga [134503] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność wroga [134503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność wroga [134503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność wroga [134503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność wroga [134503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [134503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [134503] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134503].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [134504] (ulepszenie 1) — nazwa] 티비아의 멜로디 - 해체된 것이 해체되지 않은 것을 해체하는 것
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [134504] (ulepszenie 1) — opis] [CantChangeTarget]\n이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 피해량이 60%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[DefeatDuel] [MineTheRings] 소멸\n[EndSkill] [MineTheRings] 소멸
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [MineTheRings], [EndSkill]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose] …
   EN: [CantChangeTarget]\nDuring the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -60% damage and damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] [MineTheRings] expires\n[EndSkill] [MineTheRings] expires
   PL: [CantChangeTarget]\nw turze, w której ta jednostka ma wyposażoną tę Umiejętność, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nza każdego celu zabitego tą Umiejętnością przywraca 15 SP\n[StartBattle] zyskuje 4 [Protection]\n[WhenUse] zadaje +3% obrażeń za każde 6 łącznie ([Laceration] głównego celu + [Laceration] celu dodatkowego) (maks. 30%)\n[DefeatDuel] zadaje o 60% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[DefeatDuel] [MineTheRings] wygasa\n[EndSkill] [MineTheRings] wygasa
391. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność wroga [134504] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134504].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [134508] (ulepszenie 1) — nazwa] 폐장 - 설치미술 제 1호 ‘당신들이 흩뿌린 살과 뼈가 객석이 되어’
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134508].levelList[level=1].name
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [134508] (ulepszenie 1) — opis] [CantDuel]\n레벨이 높은 적을 대상으로 우선 지정함\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 대상의 [Laceration] 8당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134508].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Laceration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [CantDuel]\nPrioritizes enemy with the highest level\nThis Skill does not trigger Defense Skills\n[WhenUse] Coin Power +1 for every 8 [Laceration] on target (max 2)
   PL: [CantDuel]\npriorytet: wróg z najwyższym poziomem\nta Umiejętność nie uruchamia Umiejętności obrony\n[WhenUse] Moc Monety +1 za każde 8 [Laceration] celu (maks. 2)
404. [Umiejętność wroga [134508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 현재 체력이 최대 체력의 60% 미만이면, 체력 피해 대신 정신력 피해를 입힘
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność wroga [134508] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태로 만들고 [LivingSpecimenTheRings]으로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134508].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [LivingSpecimenTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenTheRings] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Stagger target and turn target into [LivingSpecimenTheRings]</u></b></mark></color>
   PL: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Oszołomi cel i przekształci go w [LivingSpecimenTheRings]</u></b></mark></color>
406. [Umiejętność wroga [134605] (ulepszenie 1) — nazwa] 억압당한 육체의 해방
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].name
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność wroga [134605] (ulepszenie 1) — opis] [CantChangeTarget]\n이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 피해량이 60%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[DefeatDuel] [BoneBladeTheRings] 소멸\n[EndSkill] [BoneBladeTheRings] 소멸
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [BoneBladeTheRings], [EndSkill]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose] …
   EN: [CantChangeTarget]\nDuring the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -60% damage and damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] [BoneBladeTheRings] expires\n[EndSkill] [BoneBladeTheRings] expires
   PL: [CantChangeTarget]\nw turze, w której ta jednostka ma wyposażoną tę Umiejętność, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nza każdego celu zabitego tą Umiejętnością przywraca 15 SP\n[StartBattle] zyskuje 4 [Protection]\n[WhenUse] zadaje +3% obrażeń za każde 6 łącznie ([Laceration] głównego celu + [Laceration] celu dodatkowego) (maks. 30%)\n[DefeatDuel] zadaje o 60% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[DefeatDuel] [BoneBladeTheRings] wygasa\n[EndSkill] [BoneBladeTheRings] wygasa
408. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [134605] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134605].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [132210] (ulepszenie 1) — nazwa] 극 공간참 - 절연[空間斬 - 絕緣]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132210].levelList[level=1].name
   limit: do 70 znaków
   EN: Uttermost Rend Space - String Severance [空間斬 - 絕緣]
   PL: Uttermost Rend Space - String Severance [空間斬 - 絕緣]
420. [Umiejętność wroga [132210] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬 종료시까지 흐트러짐 상태가 되지 않음\n[WhenUse] 자신의 정신력이 20 이상이면 망을 3개 생성, 최종 위력 +10\n[EndSkill] 이 스킬에서 망을 생성했으면, 정신력 -20\n[WinDuel] [SlashDamageUp] 2 얻음\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132210].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EndSkill], [WinDuel], [SlashDamageUp], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [WinDuel] = [합 승리시] / [Clash Win]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed; this unit cannot be Staggered until this Skill ends\n[WhenUse] At 20+ SP, generate 3 Mang. Final Power +10\n[EndSkill] If this Skill generated Mang, lose 20 SP\n[WinDuel] Gain 2 [SlashDamageUp]\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie do końca tej Umiejętności\n[WhenUse] przy SP równym 20 lub więcej tworzy 3 Mang. Moc Końcowa +10\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 20 SP\n[WinDuel] zyskuje 2 [SlashDamageUp]\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
421. [Umiejętność wroga [132210] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132210].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [132210] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132210].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +100% Damage on Critical Hit
   PL: zadaje +100% obrażeń przy trafieniu krytycznym
423. [Umiejętność wroga [132210] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[PhantomIncision]을 모두 소모</u></b></mark></color>하여, 각 피격자의 최대 체력의 (소모값)% 만큼 체력 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132210].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Consume all [PhantomIncision] on target</u></b></mark></color> and deal ([PhantomIncision] consumed)% HP damage against each target hit, respectively
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zużywa wszystkie [PhantomIncision] celu</u></b></mark></color> i zadaje każdemu trafionemu celowi obrażenia HP równe (zużyte [PhantomIncision])% Maks. HP
424. [Umiejętność wroga [132211] (ulepszenie 1) — nazwa] 확정된 상대
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132211].levelList[level=1].name
   limit: do 40 znaków
   EN: Destinated Opponent
   PL: Destinated Opponent
425. [Umiejętność wroga [132211] (ulepszenie 1) — opis] [SojiAbiBuffOne], [SojiAbiBuffTwo], [SojiAbiBuffThree] 중 <color=#ff6000><mark=#ff000040><b><u>대응되는 버프를 보유한 대상만 합 가능</u></b></mark></color>\n이 스킬은 수비 스킬을 발동시키지 않음\n\n[DefeatDuel] [Vulnerable] 1 얻음\n[DefeatDuel] 대상의 [SojiAbiBuffOne], [SojiAbiBuffTwo], [SojiAbiBuffThree] 소멸\n\n[OnDirectAttack] 최종 위력 +10
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132211].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SojiAbiBuffOne], [SojiAbiBuffTwo], [SojiAbiBuffThree], [DefeatDuel], [Vulnerable], [OnDirectAttack]
   znaczenie tagów: [SojiAbiBuffOne] = 계명(雞鳴) / Dawn's First Crow (雞鳴); [SojiAbiBuffTwo] = 일입(日入) / The Sun's Descent (日入); [SojiAbiBuffThree] = 황혼(黃昏) / Eventide Glow (黃昏); [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: <color=#ff6000><mark=#ff000040><b><u>Only targets with the corresponding buff</u></b></mark></color> among [SojiAbiBuffOne], [SojiAbiBuffTwo], or [SojiAbiBuffThree] can Clash with this Skill\nThis Skill does not trigger the target's Defense Skill\n\n[DefeatDuel] Gain 1 [Vulnerable]\n[DefeatDuel] Remove [SojiAbiBuffOne], [SojiAbiBuffTwo], [SojiAbiBuffThree] from target\n\n[OnDirectAttack] Final Power +10
   PL: <color=#ff6000><mark=#ff000040><b><u>tylko cele posiadające odpowiadający bonus</u></b></mark></color> spośród [SojiAbiBuffOne], [SojiAbiBuffTwo] i [SojiAbiBuffThree] mogą stoczyć Starcie z tą Umiejętnością\nta Umiejętność nie uruchamia Umiejętności obrony celu\n\n[DefeatDuel] zyskuje 1 [Vulnerable]\n[DefeatDuel] usuwa [SojiAbiBuffOne], [SojiAbiBuffTwo] i [SojiAbiBuffThree] celu\n\n[OnDirectAttack] Moc Końcowa +10
426. [Umiejętność wroga [132212] (ulepszenie 1) — nazwa] 미래를 막지 못했군 - 잔흔참[殘痕斬]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132212].levelList[level=1].name
   limit: do 80 znaków
   EN: You Have Failed to Stop the Future - Scartrail Slash [殘痕斬]
   PL: You Have Failed to Stop the Future - Scartrail Slash [殘痕斬]
427. [Umiejętność wroga [132212] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬 종료시까지 흐트러짐 상태가 되지 않음\n[StartBattle] 이번 턴에 수비 스킬을 장착한 적 1명당 [AttackDmgDown] 1 얻음 (최대 5)\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132212].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackDmgDown], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgDown] = 피해량 감소 / Damage Down; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered until this Skill ends\n[StartBattle] Gain 1 [AttackDmgDown] for every enemy that has equipped Defense Skill this turn (max 5)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie do końca tej Umiejętności\n[StartBattle] zyskuje 1 [AttackDmgDown] za każdego wroga, który w tej turze wyposażył Umiejętność obrony (maks. 5)\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
428. [Umiejętność wroga [132212] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 <color=#ff6000><mark=#ff000040><b><u>[SojiAbiBuffOne], [SojiAbiBuffTwo], [SojiAbiBuffThree]이 있으면,</u></b></mark></color> (이 코인 최종 위력) x 5의 오만 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132212].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [SojiAbiBuffOne], [SojiAbiBuffTwo], [SojiAbiBuffThree]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SojiAbiBuffOne] = 계명(雞鳴) / Dawn's First Crow (雞鳴); [SojiAbiBuffTwo] = 일입(日入) / The Sun's Descent (日入); [SojiAbiBuffThree] = 황혼(黃昏) / Eventide Glow (黃昏)
   EN: [OnSucceedAttack] If target has <color=#ff6000><mark=#ff000040><b><u>[SojiAbiBuffOne], [SojiAbiBuffTwo], or [SojiAbiBuffThree],</u></b></mark></color> deal (this Coin's Final Power x 5) Pride damage to target
   PL: [OnSucceedAttack] jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>[SojiAbiBuffOne], [SojiAbiBuffTwo] albo [SojiAbiBuffThree]</u></b></mark></color>, zadaje mu obrażenia Pychy równe (Moc Końcowa tej Monety x 5)
429. [Umiejętność wroga [132213] (ulepszenie 1) — nazwa] 이연 - 잔[二連 - 殘]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132213].levelList[level=1].name
   limit: do 50 znaków
   EN: Twinslash - Echoshear [二連 - 殘]
   PL: Twinslash - Echoshear [二連 - 殘]
430. [Umiejętność wroga [132213] (ulepszenie 1) — opis] [DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132213].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target
   PL: [DefeatDuel] zadaje o 80% mniej końcowych obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
431. [Umiejętność wroga [132213] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132213].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [132213] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttackHead] 이 코인 재사용 (스킬 당 1회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132213].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttackHead]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]
   EN: [CriticalOnSucceedAttackHead] Reuse this Coin (once per Skill)
   PL: [CriticalOnSucceedAttackHead] używa Monety ponownie (1 raz na Umiejętność)
433. [Umiejętność wroga [132214] (ulepszenie 1) — nazwa] 필연쇄[必然殺]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132214].levelList[level=1].name
   limit: do 40 znaków
   EN: Inevitable Termination [必然殺]
   PL: Inevitable Termination [必然殺]
434. [Umiejętność wroga [132214] (ulepszenie 1) — opis] [EndSkill] 대상이 사망했거나 흐트러지면 이 스킬 재사용 (턴 당 3회)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132214].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Reuse this Skill if target is defeated or Staggered (3 times per turn)
   PL: [EndSkill] jeżeli cel zginął albo przeszedł w Oszołamienie, używa tej Umiejętności ponownie (3 razy na turę)
435. [Umiejętność wroga [132215] (ulepszenie 1) — nazwa] 132215
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132215].levelList[level=1].name
   limit: do 40 znaków
   EN: 132215
   PL: 132215
436. [Umiejętność wroga [132215] (ulepszenie 1) — opis] 사용하지 않는 스킬
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132215].levelList[level=1].desc
   limit: do 120 znaków
   EN: UNUSED SKILL
   PL: UNUSED SKILL
437. [Umiejętność wroga [133701] (ulepszenie 1) — nazwa] 이 손으로 대신…
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133701].levelList[level=1].name
   limit: do 50 znaków
   EN: Let These Hands be the Proxy...
   PL: Let These Hands be the Proxy...
438. [Umiejętność wroga [133701] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 정신력 3 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133701].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Final Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[WhenUse] Gain +2 [Breath] Count\n[EndSkill] Lose 3 SP
   PL: Moc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[WhenUse] zyskuje 2 Licznika [Breath]\n[EndSkill] traci 3 SP
439. [Umiejętność wroga [133701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] nakłada 2 [Sinking]
440. [Umiejętność wroga [133701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Sinking]
441. [Umiejętność wroga [133702] (ulepszenie 1) — nazwa] 파헤치고, 파헤치겠어요
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133702].levelList[level=1].name
   limit: do 40 znaków
   EN: Disembowel, Eviscerate...
   PL: Disembowel, Eviscerate...
442. [Umiejętność wroga [133702] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 있거나, [IndexPrescriptTargetToPersonality]이면,</u></b></mark></color> 마지막 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -50%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[WhenUse] [Breath] 2 얻음\n[EndSkill] 정신력 3 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133702].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [Sinking], [StartBattle], [PressureOfPrescript], [IndexPrescriptTargetToPersonality], [SuperCoin], [DefeatDuel], [WhenUse], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [PressureOfPrescript] = 압박감 / Onus; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use] …
   EN: Final Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [PressureOfPrescript], or if target has [IndexPrescriptTargetToPersonality]</u></b></mark></color>, convert the final Coin to [SuperCoin]\n[DefeatDuel] Deal -50% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[WhenUse] Gain 2 [Breath]\n[EndSkill] Lose 3 SP
   PL: Moc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [PressureOfPrescript] albo cel ma [IndexPrescriptTargetToPersonality]</u></b></mark></color>, ostatnia Moneta zmienia się w [SuperCoin]\n[DefeatDuel] zadaje o 50% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[WhenUse] zyskuje 2 [Breath]\n[EndSkill] traci 3 SP
443. [Umiejętność wroga [133702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] nakłada 1 [Sinking]
444. [Umiejętność wroga [133702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [133702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Sinking]
446. [Umiejętność wroga [133703] (ulepszenie 1) — nazwa] 대행: 새기기
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133703].levelList[level=1].name
   limit: do 40 znaków
   EN: Procuration: Engrave
   PL: Procuration: Engrave
447. [Umiejętność wroga [133703] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 있거나, [IndexPrescriptTargetToPersonality]이면,</u></b></mark></color> 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[IndexPrescriptTargetToPersonality]이면, 피해량 +50%</u></b></mark></color>\n[WhenUse] [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n[DefeatDuel] 피해량 -80%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[EndSkill] 정신력 6 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133703].levelList[level=1].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [Sinking], [StartBattle], [PressureOfPrescript], [IndexPrescriptTargetToPersonality], [SuperCoin], [WhenUse], [DefeatDuel], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [PressureOfPrescript] = 압박감 / Onus; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose] …
   EN: Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [PressureOfPrescript], or if target has [IndexPrescriptTargetToPersonality]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s\n[WhenUse]<color=#ff6000><mark=#ff000040><b><u>If the target has [IndexPrescriptTargetToPersonality], deal +50% damage</u></b></mark></color>\n[WhenUse] Gain 3 [Breath] and +3 [Breath] Count\n[DefeatDuel] Deal -80% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] Lose 6 SP
   PL: Moc Monety +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [PressureOfPrescript] albo cel ma [IndexPrescriptTargetToPersonality]</u></b></mark></color>, wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y\n[WhenUse]<color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [IndexPrescriptTargetToPersonality], zadaje +50% obrażeń</u></b></mark></color>\n[WhenUse] zyskuje 3 [Breath] i 3 Licznika [Breath]\n[DefeatDuel] zadaje o 80% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[EndSkill] traci 6 SP
448. [Umiejętność wroga [133703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking]
449. [Umiejętność wroga [133703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Sinking]
450. [Umiejętność wroga [133704] (ulepszenie 1) — nazwa] 대행: 말살
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].name
   limit: do 40 znaków
   EN: Procuration: Annihilate
   PL: Procuration: Annihilate
451. [Umiejętność wroga [133704] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도와 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[IndexPrescriptTargetToPersonality]이면, 피해량 +100%</u></b></mark></color>\n[DefeatDuel] [ResultReduction] 3, [Paralysis] 4 얻음\n[DefeatDuel] 피해량 -90%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[EndSkill] 정신력 15 감소\n[EndSkill] [PressureOfPrescript] 전부 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [IndexPrescriptTargetToPersonality], [DefeatDuel], [ResultReduction], [Paralysis], [Sinking], [EndSkill], [PressureOfPrescript]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [PressureOfPrescript] = 압박감 / Onus
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If the target has [IndexPrescriptTargetToPersonality], deal +100% damage</u></b></mark></color>\n[DefeatDuel] Gain 3 [ResultReduction] and 4 [Paralysis]\n[DefeatDuel] Deal -90% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] Lose 15 SP\n[EndSkill] Consume all [PressureOfPrescript]
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [IndexPrescriptTargetToPersonality], zadaje +100% obrażeń</u></b></mark></color>\n[DefeatDuel] zyskuje 3 [ResultReduction] i 4 [Paralysis]\n[DefeatDuel] zadaje o 90% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[EndSkill] traci 15 SP\n[EndSkill] zużywa wszystkie [PressureOfPrescript]
452. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Sinking]
454. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność wroga [133704] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133704].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [133705] (ulepszenie 1) — nazwa] 대행: 말살 - 본망[本望]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].name
   limit: do 80 znaków
   EN: Procuration: Annihilation - Mang of Immanent Yearning [本望]
   PL: Procuration: Annihilation - Mang of Immanent Yearning [本望]
461. [Umiejętność wroga [133705] (ulepszenie 1) — opis] [WhenUse] <color=#ff6000><mark=#ff000040><b><u>정신력이 0 이상이면, 망 1개 생성</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +20%, 최종 위력과 코인 위력 각각 +2</u></b></mark></color>\n[EndSkill] 정신력 15 감소\n[EndSkill] 망을 생성했으면, 정신력 20 소모\n[EndSkill] [PressureOfPrescript] 전부 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [EndSkill], [PressureOfPrescript]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [PressureOfPrescript] = 압박감 / Onus
   EN: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>At 0+ SP, generate 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Deal +20% damage, Final Power +2, Coin Power +2</u></b></mark></color>\n[EndSkill] Lose 15 SP\n[EndSkill] If this Skill generated 1 Mang, lose 20 SP\n[EndSkill] Consume all [PressureOfPrescript]
   PL: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>przy SP równym 0 lub więcej tworzy 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>zadaje +20% obrażeń, Moc Końcowa +2 i Moc Monety +2</u></b></mark></color>\n[EndSkill] traci 15 SP\n[EndSkill] jeżeli ta Umiejętność utworzyła 1 Mang, traci 20 SP\n[EndSkill] zużywa wszystkie [PressureOfPrescript]
462. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność wroga [133705] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133705].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność wroga [133706] (ulepszenie 1) — nazwa] 모든 것을 듣고, 모든 것을 바라고, 모든 것을 이 손으로…
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].name
   limit: do 70 znaków
   EN: Hear all. Hope all. With these Hands, all will...
   PL: Hear all. Hope all. With these Hands, all will...
473. [Umiejętność wroga [133706] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>료슈를 지정하며 대상 변경 불가</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>망 1개 생성</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +20%, 최종 위력과 코인 위력 각각 +2</u></b></mark></color>\n[EndSkill] 정신력 15 감소\n[EndSkill] 망을 생성했으면, 정신력 20 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <color=#ff6000><mark=#ff000040><b><u>Targets Ryōshū and cannot change target</u></b></mark></color>\n[WhenUse]<color=#ff6000><mark=#ff000040><b><u>Generate 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Deal +20% damage, Final Power +2, Coin Power +2</u></b></mark></color>\n[EndSkill] Lose 15 SP\n[EndSkill] If this Skill generated 1 Mang, lose 20 SP
   PL: <color=#ff6000><mark=#ff000040><b><u>wskazuje Ryōshū i nie może zmienić celu</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>tworzy 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>zadaje +20% obrażeń, Moc Końcowa +2 i Moc Monety +2</u></b></mark></color>\n[EndSkill] traci 15 SP\n[EndSkill] jeżeli ta Umiejętność utworzyła 1 Mang, traci 20 SP
474. [Umiejętność wroga [133706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [133706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność wroga [133706] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [133706] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność wroga [133706] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133706].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność wroga [133801] (ulepszenie 1) — nazwa] 수[守]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133801].levelList[level=1].name
   limit: do 40 znaków
   EN: Defend [守]
   PL: Defend [守]
480. [Umiejętność wroga [133801] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 자신의 [Breath] 횟수 4 증가\n- 이 스킬을 사용하는 슬롯에 메인 타겟으로 지정된 공격 스킬이 있으면 이 효과로 얻는 [Breath] 횟수 2 감소\n\n[WinDuel] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133801].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [Breath], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[StartBattle] Gain +4 [Breath] Count\n- If the Skill Slot using this Skill is a main target of an Attack Skill, gain 2 fewer [Breath] Count from this effect\n\n[WinDuel] Gain +1 [Breath] Count
   PL: [CanDuelGuard]\n[StartBattle] zyskuje 4 Licznika [Breath]\n- jeżeli w slocie tej Umiejętności wskazany jest cel główny Umiejętności ataku, ten efekt daje o 2 mniej Licznika [Breath]\n\n[WinDuel] zyskuje 1 Licznika [Breath]
481. [Umiejętność wroga [133801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność wroga [133802] (ulepszenie 1) — nazwa] 반[反]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133802].levelList[level=1].name
   limit: do 40 znaków
   EN: Reflect [反]
   PL: Reflect [反]
483. [Umiejętność wroga [133802] (ulepszenie 1) — opis] [DuelCounter]\n[DefeatDuel] 자신의 [Breath] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DefeatDuel], [Breath]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Breath] = 호흡 / Poise
   EN: [DuelCounter]\n[DefeatDuel] Lose 1 [Breath] Count
   PL: [DuelCounter]\n[DefeatDuel] traci 1 Licznika [Breath]
484. [Umiejętność wroga [133802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [Breath]
485. [Umiejętność wroga [133803] (ulepszenie 1) — nazwa] 무명섬[無名閃]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133803].levelList[level=1].name
   limit: do 40 znaków
   EN: Unnamed Cut [無名閃]
   PL: Unnamed Cut [無名閃]
486. [Umiejętność wroga [133803] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +50% Damage on Critical Hit
   PL: zadaje +50% obrażeń przy trafieniu krytycznym
487. [Umiejętność wroga [133804] (ulepszenie 1) — nazwa] 연쇄참[連鎖斬]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133804].levelList[level=1].name
   limit: do 40 znaków
   EN: Chainslash [連鎖斬]
   PL: Chainslash [連鎖斬]
488. [Umiejętność wroga [133804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp] next turn
   PL: [OnSucceedAttack] nakłada 1 [SlashTakeDamageUp] w następnej turze
489. [Umiejętność wroga [133805] (ulepszenie 1) — nazwa] 이격[二擊]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133805].levelList[level=1].name
   limit: do 40 znaków
   EN: Twinstrike [二擊]
   PL: Twinstrike [二擊]
490. [Umiejętność wroga [133805] (ulepszenie 1) — opis] [WinDuel] [DicipleLittleFinger] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133805].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [DicipleLittleFinger]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: [WinDuel] Gain 1 [DicipleLittleFinger]
   PL: [WinDuel] zyskuje 1 [DicipleLittleFinger]
491. [Umiejętność wroga [133805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 1 Licznika [Breath]
492. [Umiejętność wroga [133805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] zyskuje 2 [Breath]
493. [Umiejętność wroga [133806] (ulepszenie 1) — nazwa] 삼격[三擊]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133806].levelList[level=1].name
   limit: do 40 znaków
   EN: Triplestrike [三擊]
   PL: Triplestrike [三擊]
494. [Umiejętność wroga [133806] (ulepszenie 1) — opis] [WinDuel] [DicipleLittleFinger] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133806].levelList[level=1].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność wroga [133806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Umiejętność wroga [133806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] zyskuje 1 [Breath]
497. [Umiejętność wroga [133806] (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133806].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +30% Damage on Critical Hit
   PL: zadaje +30% obrażeń przy trafieniu krytycznym
498. [Umiejętność wroga [133807] (ulepszenie 1) — nazwa] 낙성일살[落星一殺]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133807].levelList[level=1].name
   limit: do 40 znaków
   EN: Fallstar Slayer [落星一殺]
   PL: Fallstar Slayer [落星一殺]
499. [Umiejętność wroga [133807] (ulepszenie 1) — opis] 속도에 관계없이 이 스킬과 합을 할 수 있음\n자신의 [DicipleLittleFinger] 1 당 피해량 +1%\n[WhenUse] 자신의 [DicipleLittleFinger] 10 당 코인 위력 +1\n[DefeatDuel] 피해량이 80% 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133807].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DicipleLittleFinger], [WhenUse], [DefeatDuel]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\nDeal +1% damage for every [DicipleLittleFinger] on self\n[WhenUse] Coin Power +1 for every 10 [DicipleLittleFinger] on self\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nzadaje +1% obrażeń za każdy [DicipleLittleFinger] jednostki\n[WhenUse] Moc Monety +1 za każde 10 [DicipleLittleFinger] jednostki\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
500. [Umiejętność wroga [133807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [133807] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133807].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność wroga [133807] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 최종 피해량만큼 참격 피해
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133807].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal Slash damage equal to this Coin's final damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Cięcia równe końcowym obrażeniom tej Monety
503. [Umiejętność wroga [133808] (ulepszenie 1) — nazwa] 공간참 - 청[空間斬 - 靑]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].name
   limit: do 50 znaków
   EN: Rend Space - Azureslash [空間斬 - 靑]
   PL: Rend Space - Azureslash [空間斬 - 靑]
504. [Umiejętność wroga [133808] (ulepszenie 1) — opis] 자신의 [DicipleLittleFinger] 1 당 피해량 +1%\n[WhenUse] 자신의 [DicipleLittleFinger] 10 당 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [DicipleLittleFinger], [WhenUse]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade; [WhenUse] = [사용시] / [On Use]
   EN: Deal +1% damage for every [DicipleLittleFinger] on self\n[WhenUse] Coin Power +1 for every 10 [DicipleLittleFinger] on self
   PL: zadaje +1% obrażeń za każdy [DicipleLittleFinger] jednostki\n[WhenUse] Moc Monety +1 za każde 10 [DicipleLittleFinger] jednostki
505. [Umiejętność wroga [133808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność wroga [133808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność wroga [133808] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność wroga [133808] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność wroga [133808] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133808].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Umiejętność wroga [134701] (ulepszenie 1) — nazwa] 무게를 실어 내려쳐, 몸을 무너뜨리고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134701].levelList[level=1].name
   limit: do 60 znaków
   EN: Slam Down with Weight, Topple the Body
   PL: Slam Down with Weight, Topple the Body
511. [Umiejętność wroga [134701] (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 2)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +20%\n- 타격 무기가 아닐 경우, 피해량 -10%\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134701].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [WhenUse], [Breath]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 2)\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +20% damage\n- Non-Blunt weapons deal -10% damage\n[WhenUse] Gain +1 [Breath] Count
   PL: Moc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 2)\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +20% obrażeń\n- broń niebędąca Uderzeniem zadaje o 10% mniej obrażeń\n[WhenUse] zyskuje 1 Licznika [Breath]
512. [Umiejętność wroga [134701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Umiejętność wroga [134702] (ulepszenie 1) — nazwa] 끝을 세워, 심지까지 밀어 넣고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134702].levelList[level=1].name
   limit: do 60 znaków
   EN: Lay Vertical The End, Insert Up to the Wick
   PL: Lay Vertical The End, Insert Up to the Wick
514. [Umiejętność wroga [134702] (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 2)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +20%\n- 관통 무기가 아닐 경우, 피해량 -10%\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134702].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [WhenUse], [Breath]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 2)\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +20% damage\n- Non-Pierce weapons deal -10% damage\n[WhenUse] Gain +1 [Breath] Count
   PL: Moc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 2)\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +20% obrażeń\n- broń niebędąca Przebiciem zadaje o 10% mniej obrażeń\n[WhenUse] zyskuje 1 Licznika [Breath]
515. [Umiejętność wroga [134702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność wroga [134702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność wroga [134703] (ulepszenie 1) — nazwa] 날을 눕혀, 숨결이 갈라지듯 잘라내고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134703].levelList[level=1].name
   limit: do 80 znaków
   EN: Lay the Blade on its Side, Slice Like a Severed Breath
   PL: Lay the Blade on its Side, Slice Like a Severed Breath
518. [Umiejętność wroga [134703] (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 2)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +20%\n- 참격 무기가 아닐 경우, 피해량 -10%\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134703].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [WhenUse], [Breath]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 2)\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +20% damage\n- Non-Slash weapons deal -10% damage\n[WhenUse] Gain +1 [Breath] Count
   PL: Moc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 2)\nefekty zależą od typu ataku używanej broni\n- broń Cięcia zadaje +20% obrażeń\n- broń niebędąca Cięciem zadaje o 10% mniej obrażeń\n[WhenUse] zyskuje 1 Licznika [Breath]
519. [Umiejętność wroga [134703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Umiejętność wroga [134703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Umiejętność wroga [134704] (ulepszenie 1) — nazwa] 휘둘러 떨어뜨려, 땅과 하나로 만들며
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134704].levelList[level=1].name
   limit: do 60 znaków
   EN: Swing to Fell, Have it Meet the Ground
   PL: Swing to Fell, Have it Meet the Ground
522. [Umiejętność wroga [134704] (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 2)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +30%\n- 타격 무기가 아닐 경우, 피해량 -15%\n[StartBattle] 다음 효과 누적 적용\n- [UnlockBuff_Rien2]면, 마지막 코인이 [SuperCoin]으로 변경됨\n- [UnlockBuff_Rien3]면, 이 스킬로 합 승리 시 10만큼 흐트러짐 회복\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134704].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [StartBattle], [UnlockBuff_Rien2], [SuperCoin], [UnlockBuff_Rien3], [WhenUse], [Breath]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 2)\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +30% damage\n- Non-Blunt weapons deal -15% damage\n[StartBattle] Gain the following effects (effects are cumulative)\n- At [UnlockBuff_Rien2], convert the final Coin to [SuperCoin]\n- At [UnlockBuff_Rien3], on Clash Win with this Skill, lower user's Stagger Threshold by 10\n[WhenUse] Gain 2 [Breath]
   PL: Moc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 2)\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +30% obrażeń\n- broń niebędąca Uderzeniem zadaje o 15% mniej obrażeń\n[StartBattle] zyskuje następujące efekty (efekty się kumulują)\n- jeżeli jednostka ma [UnlockBuff_Rien2], ostatnia Moneta zmienia się w [SuperCoin]\n- jeżeli jednostka ma [UnlockBuff_Rien3], po wygranej w Starciu tą Umiejętnością obniża Próg Oszołomienia użytkownika o 10\n[WhenUse] zyskuje 2 [Breath]
523. [Umiejętność wroga [134704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 [Sinking]
524. [Umiejętność wroga [134704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [134704] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134704].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 Licznika [Sinking]
526. [Umiejętność wroga [134705] (ulepszenie 1) — nazwa] 점 하나를 겨눠, 안쪽에서 울리며
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134705].levelList[level=1].name
   limit: do 60 znaków
   EN: Aim Toward a Point, Let it Echo Within
   PL: Aim Toward a Point, Let it Echo Within
527. [Umiejętność wroga [134705] (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 2)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +30%\n- 관통 무기가 아닐 경우, 피해량 -15%\n[StartBattle] 다음 효과 누적 적용\n- [UnlockBuff_Rien2]면, 마지막 코인이 [SuperCoin]으로 변경됨\n- [UnlockBuff_Rien3]면, 이 스킬로 합 승리 시 다음 턴에 [ResultReduction] 1 부여\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134705].levelList[level=1].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [StartBattle], [UnlockBuff_Rien2], [SuperCoin], [UnlockBuff_Rien3], [ResultReduction], [WhenUse], [Breath]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [ResultReduction] = 위력 감소 / Power Down; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 2)\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +30% damage\n- Non-Pierce weapons deal -15% damage\n[StartBattle] Gain the following effects (effects are cumulative)\n- At [UnlockBuff_Rien2], convert the final Coin to [SuperCoin]\n- At [UnlockBuff_Rien3], on Clash Win with this Skill, inflict 1 [ResultReduction] next turn\n[WhenUse] Gain 2 [Breath]
   PL: Moc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 2)\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +30% obrażeń\n- broń niebędąca Przebiciem zadaje o 15% mniej obrażeń\n[StartBattle] zyskuje następujące efekty (efekty się kumulują)\n- jeżeli jednostka ma [UnlockBuff_Rien2], ostatnia Moneta zmienia się w [SuperCoin]\n- jeżeli jednostka ma [UnlockBuff_Rien3], po wygranej w Starciu tą Umiejętnością nakłada 1 [ResultReduction] w następnej turze\n[WhenUse] zyskuje 2 [Breath]
528. [Umiejętność wroga [134705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [134705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Sinking]
530. [Umiejętność wroga [134705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność wroga [134705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność wroga [134706] (ulepszenie 1) — nazwa] 결을 낮게 깔아, 남은 것을 벗겨내고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134706].levelList[level=1].name
   limit: do 60 znaków
   EN: Carve at a Low Slant, Peel What Remains
   PL: Carve at a Low Slant, Peel What Remains
533. [Umiejętność wroga [134706] (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 2)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +30%\n- 참격 무기가 아닐 경우, 피해량 -15%\n[StartBattle] 다음 효과 누적 적용\n- [UnlockBuff_Rien2]면, 마지막 코인이 [SuperCoin]으로 변경됨\n- [UnlockBuff_Rien3]면, 이 스킬로 합 승리 시 다음 턴에 [ResultEnhancement] 1 얻음\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134706].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [StartBattle], [UnlockBuff_Rien2], [SuperCoin], [UnlockBuff_Rien3], [ResultEnhancement], [WhenUse], [Breath]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [ResultEnhancement] = 위력 증가 / Power Up; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 2)\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +30% damage\n- Non-Slash weapons deal -15% damage\n[StartBattle] Gain the following effects (effects are cumulative)\n- At [UnlockBuff_Rien2], convert the final Coin to [SuperCoin]\n- At [UnlockBuff_Rien3], on Clash Win with this Skill, gain 1 [ResultEnhancement] next turn\n[WhenUse] Gain 2 [Breath]
   PL: Moc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 2)\nefekty zależą od typu ataku używanej broni\n- broń Cięcia zadaje +30% obrażeń\n- broń niebędąca Cięciem zadaje o 15% mniej obrażeń\n[StartBattle] zyskuje następujące efekty (efekty się kumulują)\n- jeżeli jednostka ma [UnlockBuff_Rien2], ostatnia Moneta zmienia się w [SuperCoin]\n- jeżeli jednostka ma [UnlockBuff_Rien3], po wygranej w Starciu tą Umiejętnością zyskuje 1 [ResultEnhancement] w następnej turze\n[WhenUse] zyskuje 2 [Breath]
534. [Umiejętność wroga [134706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność wroga [134706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność wroga [134706] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134706].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [134706] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134706].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność wroga [134707] (ulepszenie 1) — nazwa] 소리를 부수고, 생각을 납작하게 짓이겨라
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134707].levelList[level=1].name
   limit: do 60 znaków
   EN: Destroy the Sound, Crush Flat the Thought
   PL: Destroy the Sound, Crush Flat the Thought
539. [Umiejętność wroga [134707] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +50%\n- 타격 무기가 아닐 경우, 피해량 -25%\n[StartBattle] 다음 효과 누적 적용\n- [UnlockBuff_Rien2]면, 3,4번째 코인이 [SuperCoin]으로 변경됨\n- [UnlockBuff_Rien3]면, 이 스킬로 합 승리 시 15만큼 흐트러짐 피해\n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134707].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [UnlockBuff_Rien2], [SuperCoin], [UnlockBuff_Rien3], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Can Clash with this Skill regardless of Speed\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +50% damage\n- Non-Blunt weapons deal -25% damage\n[StartBattle] Gain the following effects (effects are cumulative)\n- At [UnlockBuff_Rien2], convert the 3rd and 4th Coins to [SuperCoin]s\n- At [UnlockBuff_Rien3], on Clash Win with this Skill, raise target's Stagger Threshold by 15\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +50% obrażeń\n- broń niebędąca Uderzeniem zadaje o 25% mniej obrażeń\n[StartBattle] zyskuje następujące efekty (efekty się kumulują)\n- jeżeli jednostka ma [UnlockBuff_Rien2], 3. i 4. Moneta zmieniają się w [SuperCoin]y\n- jeżeli jednostka ma [UnlockBuff_Rien3], po wygranej w Starciu tą Umiejętnością podnosi Próg Oszołomienia celu o 15\n[WhenUse] zyskuje 2 [Breath] i 2 Licznika [Breath]
540. [Umiejętność wroga [134707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking]
541. [Umiejętność wroga [134707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Umiejętność wroga [134707] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134707].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 2 [Breath]
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 2 [Breath]
543. [Umiejętność wroga [134707] (ulepszenie 1) — moneta 4, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134707].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain +2 [Breath] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 2 Licznika [Breath]
544. [Umiejętność wroga [134708] (ulepszenie 1) — nazwa] 고요의 중심을 찌르고, 기억을 꿰뚫어라
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134708].levelList[level=1].name
   limit: do 70 znaków
   EN: Stab the Silence's Heart, Penetrate the Memory
   PL: Stab the Silence's Heart, Penetrate the Memory
545. [Umiejętność wroga [134708] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +50%\n- 관통 무기가 아닐 경우, 피해량 -25%\n[StartBattle] 다음 효과 누적 적용\n- [UnlockBuff_Rien2]면, 3,4번째 코인이 [SuperCoin]으로 변경됨\n- [UnlockBuff_Rien3]면, 이 스킬로 합 승리 시 다음 턴에 [AttackDmgUp] 1 얻음\n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134708].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [UnlockBuff_Rien2], [SuperCoin], [UnlockBuff_Rien3], [AttackDmgUp], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [AttackDmgUp] = 피해량 증가 / Damage Up; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Can Clash with this Skill regardless of Speed\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +50% damage\n- Non-Pierce weapons deal -25% damage\n[StartBattle] Gain the following effects (effects are cumulative)\n- At [UnlockBuff_Rien2], convert the 3rd and 4th Coins to [SuperCoin]s\n- At [UnlockBuff_Rien3], on Clash Win with this Skill, gain 1 [AttackDmgUp] next turn\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +50% obrażeń\n- broń niebędąca Przebiciem zadaje o 25% mniej obrażeń\n[StartBattle] zyskuje następujące efekty (efekty się kumulują)\n- jeżeli jednostka ma [UnlockBuff_Rien2], 3. i 4. Moneta zmieniają się w [SuperCoin]y\n- jeżeli jednostka ma [UnlockBuff_Rien3], po wygranej w Starciu tą Umiejętnością zyskuje 1 [AttackDmgUp] w następnej turze\n[WhenUse] zyskuje 2 [Breath] i 2 Licznika [Breath]
546. [Umiejętność wroga [134708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Umiejętność wroga [134708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność wroga [134708] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134708].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność wroga [134708] (ulepszenie 1) — moneta 4, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134708].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność wroga [134709] (ulepszenie 1) — nazwa] 날카롭게 벼린 비밀로, 형태를 베어내라
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134709].levelList[level=1].name
   limit: do 50 znaków
   EN: With Tempered Secret, Cut the Form
   PL: With Tempered Secret, Cut the Form
551. [Umiejętność wroga [134709] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +50%\n- 참격 무기가 아닐 경우, 피해량 -25%\n[StartBattle] 다음 효과 누적 적용\n- [UnlockBuff_Rien2]면, 마지막 코인이 [SuperCoin]으로 변경됨\n- [UnlockBuff_Rien3]면, 이 스킬로 합 승리 시 최종 위력 +2\n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134709].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [UnlockBuff_Rien2], [SuperCoin], [UnlockBuff_Rien3], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Can Clash with this Skill regardless of Speed\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +50% damage\n- Non-Slash weapons deal -25% damage\n[StartBattle] Gain the following effects (effects are cumulative)\n- At [UnlockBuff_Rien2], convert the final Coin to [SuperCoin]\n- At [UnlockBuff_Rien3], on Clash Win with this Skill, Final Power +2\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nefekty zależą od typu ataku używanej broni\n- broń Cięcia zadaje +50% obrażeń\n- broń niebędąca Cięciem zadaje o 25% mniej obrażeń\n[StartBattle] zyskuje następujące efekty (efekty się kumulują)\n- jeżeli jednostka ma [UnlockBuff_Rien2], ostatnia Moneta zmienia się w [SuperCoin]\n- jeżeli jednostka ma [UnlockBuff_Rien3], po wygranej w Starciu tą Umiejętnością zyskuje Moc Końcową +2\n[WhenUse] zyskuje 2 [Breath] i 2 Licznika [Breath]
552. [Umiejętność wroga [134709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność wroga [134709] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134709].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [134709] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134709].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [134709] (ulepszenie 1) — moneta 4, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134709].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [134710] (ulepszenie 1) — nazwa] 부족한 것을 세 번 채워넣는다
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134710].levelList[level=1].name
   limit: do 50 znaków
   EN: Fill Three Times What is Wanting
   PL: Fill Three Times What is Wanting
557. [Umiejętność wroga [134710] (ulepszenie 1) — opis] [DuelCounter]\n\n[BeforeUse] 공격 스킬 9종 중 무작위 스킬로 발동됨\n- 사용되지 않은 스킬이 있으면, 해당 스킬 우선으로 발동
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134710].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [BeforeUse]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [BeforeUse] = [사용전] / [Before Use]
   EN: [DuelCounter]\n\n[BeforeUse] Activates as one of the 9 Attack Skills, randomly selected\n- Prioritizes Skills that haven't been used yet
   PL: [DuelCounter]\n\n[BeforeUse] uruchamia się jako jedna z 9 Umiejętności ataku, wybierana losowo\n- priorytet: Umiejętności, które nie zostały jeszcze użyte
558. [Umiejętność wroga [134710] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134710].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność wroga [134710] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134710].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność wroga [134711] (ulepszenie 1) — nazwa] Furioso-Replica
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134711].levelList[level=1].name
   limit: do 40 znaków
   EN: Furioso-Replica
   PL: Furioso-Replica
561. [Umiejętność wroga [134711] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n- 합 위력 +5 (<color=#ff6000><mark=#ff000040><b><u>자신의 [KarmaOfIndexRien] 10당 1씩 감소, 최소 0</u></b></mark></color>)\n[WhenUse] 정신력이 0 이상이면, 망 1개 생성\n- 피해량이 40%만큼 증가하고 최종 위력 +4\n[WinDuel] \n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 3, [Binding] 1, [Vulnerable] 1 부여\n[DefeatDuel] \n- [AttackDmgDown] 4, [Paralysis] 9 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 20만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134711].levelList[level=1].desc
   limit: do 930 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien] = 카르마 / Karmic Consequence; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 3 [Breath] and +3 [Breath] Count\n- Clash Power +5 (<color=#ff6000><mark=#ff000040><b><u>Clash Power gained is reduced by 1 for every 10 [KarmaOfIndexRien] on self, down to 0</u></b></mark></color>)\n[WhenUse] At 0+ SP, generate 1 Mang\n- Deal +40% damage; Final Power +4\n\n[WinDuel]\n- Gain 3 [Breath] and +3 [Breath] Count\n- Attack End: Inflict 3 [Laceration], 1 [Binding], and 1 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Gain 4 [AttackDmgDown] and 9 [Paralysis]\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 20 SP\n[EndSkill] End this turn
   PL: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>ta Umiejętność nie uruchamia Umiejętności obrony celu</u></b></mark></color>\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- zyskuje 3 [Breath] i 3 Licznika [Breath]\n- Moc Starcia +5 (<color=#ff6000><mark=#ff000040><b><u>zyskiwana Moc Starcia maleje o 1 za każde 10 [KarmaOfIndexRien] jednostki, do 0</u></b></mark></color>)\n[WhenUse] przy SP równym 0 lub więcej tworzy 1 Mang\n- zadaje +40% obrażeń; Moc Końcowa +4\n\n[WinDuel]\n- zyskuje 3 [Breath] i 3 Licznika [Breath]\n- na koniec Ataku nakłada 3 [Laceration], 1 [Binding] i 1 [Vulnerable] w następnej turze wszystkim celom trafionym przez tę jednostkę\n[DefeatDuel]\n- zyskuje 4 [AttackDmgDown] i 9 [Paralysis]\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 20 SP\n[EndSkill] kończy tę turę
562. [Umiejętność wroga [134711] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność wroga [134711] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność wroga [134711] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134711].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Reuse this Coin (7 times max)</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>używa Monety ponownie (do 7 razy)</u></b></mark></color>
565. [Umiejętność wroga [134711] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134711].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność wroga [134801] (ulepszenie 1) — nazwa] 무게를 실어 내려쳐, 몸을 무너뜨리고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134801].levelList[level=1].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność wroga [134801] (ulepszenie 1) — opis] 타격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +30%\n- 타격 무기가 아닐 경우, 피해량 -15%\n[WhenUse] [Breath] 1 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134801].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexRien_2Phase], [WhenUse], [Breath]
   znaczenie tagów: [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Blunt weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Blunt weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Blunt weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +30% damage\n- Non-Blunt weapons deal -15% damage\n[WhenUse] Gain 1 [Breath] and +1 [Breath] Count
   PL: broń Uderzenia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +30% obrażeń\n- broń niebędąca Uderzeniem zadaje o 15% mniej obrażeń\n[WhenUse] zyskuje 1 [Breath] i 1 Licznika [Breath]
568. [Umiejętność wroga [134801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność wroga [134801] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134801].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność wroga [134802] (ulepszenie 1) — nazwa] 끝을 세워, 심지까지 밀어 넣고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134802].levelList[level=1].name
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [134802] (ulepszenie 1) — opis] 관통 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +30%\n- 관통 무기가 아닐 경우, 피해량 -15%\n[WhenUse] [Breath] 1 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134802].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexRien_2Phase], [WhenUse], [Breath]
   znaczenie tagów: [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Pierce weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Pierce weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Pierce weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +30% damage\n- Non-Pierce weapons deal -15% damage\n[WhenUse] Gain 1 [Breath] and +1 [Breath] Count
   PL: broń Przebicia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +30% obrażeń\n- broń niebędąca Przebiciem zadaje o 15% mniej obrażeń\n[WhenUse] zyskuje 1 [Breath] i 1 Licznika [Breath]
572. [Umiejętność wroga [134802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [134802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Umiejętność wroga [134802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [134802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność wroga [134803] (ulepszenie 1) — nazwa] 날을 눕혀, 숨결이 갈라지듯 잘라내고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134803].levelList[level=1].name
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność wroga [134803] (ulepszenie 1) — opis] 참격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +30%\n- 참격 무기가 아닐 경우, 피해량 -15%\n[WhenUse] [Breath] 1 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134803].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexRien_2Phase], [WhenUse], [Breath]
   znaczenie tagów: [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Slash weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Slash weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Slash weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +30% damage\n- Non-Slash weapons deal -15% damage\n[WhenUse] Gain 1 [Breath] and +1 [Breath] Count
   PL: broń Cięcia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Cięcia zadaje +30% obrażeń\n- broń niebędąca Cięciem zadaje o 15% mniej obrażeń\n[WhenUse] zyskuje 1 [Breath] i 1 Licznika [Breath]
578. [Umiejętność wroga [134803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność wroga [134803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność wroga [134803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [134803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [134804] (ulepszenie 1) — nazwa] 휘둘러 떨어뜨려, 땅과 하나로 만들며
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134804].levelList[level=1].name
   (powtórzenie elementu 521 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [134804] (ulepszenie 1) — opis] 타격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +40%\n- 타격 무기가 아닐 경우, 피해량 -20%\n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 1 증가\n[WinDuel] 15만큼 흐트러짐 회복\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 발동하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134804].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Blunt weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Blunt weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Blunt weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +40% damage\n- Non-Blunt weapons deal -20% damage\n[WhenUse] Gain 2 [Breath] and +1 [Breath] Count\n[WinDuel] Lower user's Stagger Threshold by 15\n- At 75+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: broń Uderzenia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +40% obrażeń\n- broń niebędąca Uderzeniem zadaje o 20% mniej obrażeń\n[WhenUse] zyskuje 2 [Breath] i 1 Licznika [Breath]\n[WinDuel] obniża Próg Oszołomienia użytkownika o 15\n- przy 75+ [KarmaOfIndexRien_2Phase], ten efekt nie uruchamia się
584. [Umiejętność wroga [134804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] nakłada 4 [Sinking]
585. [Umiejętność wroga [134804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [134804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność wroga [134804] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134804].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność wroga [134805] (ulepszenie 1) — nazwa] 점 하나를 겨눠, 안쪽에서 울리며
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].name
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność wroga [134805] (ulepszenie 1) — opis] 관통 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +40%\n- 관통 무기가 아닐 경우, 피해량 -20%\n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 1 증가\n[WinDuel] 다음 턴에 [ResultReduction] 2 부여\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 발동하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel], [ResultReduction]
   znaczenie tagów: [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [ResultReduction] = 위력 감소 / Power Down
   EN: Pierce weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Pierce weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Pierce weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +40% damage\n- Non-Pierce weapons deal -20% damage\n[WhenUse] Gain 2 [Breath] and +1 [Breath] Count\n[WinDuel] Inflict 2 [ResultReduction] next turn\n- At 75+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: broń Przebicia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +40% obrażeń\n- broń niebędąca Przebiciem zadaje o 20% mniej obrażeń\n[WhenUse] zyskuje 2 [Breath] i 1 Licznika [Breath]\n[WinDuel] nakłada 2 [ResultReduction] w następnej turze\n- przy 75+ [KarmaOfIndexRien_2Phase], ten efekt nie uruchamia się
590. [Umiejętność wroga [134805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [134805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [134805] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [134805] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [134805] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134805].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [134806] (ulepszenie 1) — nazwa] 결을 낮게 깔아, 남은 것을 벗겨내고
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].name
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność wroga [134806] (ulepszenie 1) — opis] 참격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n[UnlockBuff_Base] 단계 1당 최종 위력 +1 (최대 3)\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +40%\n- 참격 무기가 아닐 경우, 피해량 -20%  \n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 1 증가\n[WinDuel] 다음 턴에 [ResultEnhancement] 2 얻음\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 발동하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [KarmaOfIndexRien_2Phase], [UnlockBuff_Base], [WhenUse], [Breath], [WinDuel], [ResultEnhancement]
   znaczenie tagów: [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [UnlockBuff_Base] = 해금 / Unlock; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: Slash weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Slash weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Slash weapons appear even less frequently\nFinal Power +1 for every [UnlockBuff_Base] stage (max 3)\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +40% damage\n- Non-Pierce weapons deal -20% damage\n[WhenUse] Gain 2 [Breath] and +1 [Breath] Count\n[WinDuel] Gain 2 [ResultEnhancement] next turn\n- At 75+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: broń Cięcia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nMoc Końcowa +1 za każdy Etap [UnlockBuff_Base] (maks. 3)\nefekty zależą od typu ataku używanej broni\n- broń Cięcia zadaje +40% obrażeń\n- broń niebędąca Cięciem zadaje o 20% mniej obrażeń\n[WhenUse] zyskuje 2 [Breath] i 1 Licznika [Breath]\n[WinDuel] zyskuje 2 [ResultEnhancement] w następnej turze\n- przy 75+ [KarmaOfIndexRien_2Phase], ten efekt nie uruchamia się
597. [Umiejętność wroga [134806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [134806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [134806] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [134806] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [134806] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134806].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [134807] (ulepszenie 1) — nazwa] 소리를 부수고, 생각을 납작하게 짓이겨라
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].name
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [134807] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 타격 스킬 또는 료슈가 아니면</u></b></mark></color>, 코인 위력 +2, 피해량 +50%\n- 타격 스킬 또는 료슈에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n\n타격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +60%\n- 타격 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 25만큼 흐트러짐 피해\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].desc
   limit: do 1130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Blunt Skill or a non-Ryōshū unit</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Blunt Skill or Ryōshū:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nBlunt weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Blunt weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Blunt weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +60% damage\n- Non-Blunt weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Raise target's Stagger Threshold by 25\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli ta jednostka ma [BlackNightmare]:\n- wszystkie Monety zmieniają się w [SuperCoin]y\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli przeciwnik w Starciu nie używa Umiejętności Uderzenia i nie jest Ryōshū</u></b></mark></color>, Moc Monety +2 i zadaje +50% obrażeń\n- po przegranej w Starciu z Umiejętnością Uderzenia albo z Ryōshū:\n  - Moc Monety -2 i zadaje o 50% mniej obrażeń\n  - obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n\nbroń Uderzenia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +60% obrażeń\n- broń niebędąca Uderzeniem zadaje o 30% mniej obrażeń\n[WhenUse] zyskuje 3 [Breath] i 2 Licznika [Breath]\n[WinDuel] podnosi Próg Oszołomienia celu o 25\n- przy 150+ [KarmaOfIndexRien_2Phase], ten efekt nie uruchamia się
604. [Umiejętność wroga [134807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [134807] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność wroga [134807] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [134807] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [134807] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [134807] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134807].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność wroga [134808] (ulepszenie 1) — nazwa] 고요의 중심을 찌르고, 기억을 꿰뚫어라
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].name
   limit: do 70 znaków
   EN: Stab the Heart of Silence, Penetrate the Memory
   PL: Stab the Heart of Silence, Penetrate the Memory
611. [Umiejętność wroga [134808] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 관통 스킬 또는 료슈가 아니면</u></b></mark></color>, 코인 위력 +2, 피해량 +50%\n- 관통 스킬 또는 료슈에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n\n관통 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +60%\n- 관통 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 [AttackDmgUp] 2 얻음\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].desc
   limit: do 1130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel], [AttackDmgUp]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Pierce Skill or a non-Ryōshū unit</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Pierce Skill or Ryōshū:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nPierce weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Pierce weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Pierce weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +60% damage\n- Non-Pierce weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Gain 2 [AttackDmgUp] next turn\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli ta jednostka ma [BlackNightmare]:\n- wszystkie Monety zmieniają się w [SuperCoin]y\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli przeciwnik w Starciu nie używa Umiejętności Przebicia i nie jest Ryōshū</u></b></mark></color>, Moc Monety +2 i zadaje +50% obrażeń\n- po przegranej w Starciu z Umiejętnością Przebicia albo z Ryōshū:\n  - Moc Monety -2 i zadaje o 50% mniej obrażeń\n  - obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n\nbroń Przebicia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +60% obrażeń\n- broń niebędąca Przebiciem zadaje o 30% mniej obrażeń\n[WhenUse] zyskuje 3 [Breath] i 2 Licznika [Breath]\n[WinDuel] zyskuje 2 [AttackDmgUp] w następnej turze\n- przy 150+ [KarmaOfIndexRien_2Phase], ten efekt nie uruchamia się
612. [Umiejętność wroga [134808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [134808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 3 [Breath]
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 3 [Breath]
614. [Umiejętność wroga [134808] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [134808] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność wroga [134808] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [134808] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134808].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [134809] (ulepszenie 1) — nazwa] 날카롭게 벼린 비밀로, 형태를 베어내라
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].name
   limit: do 50 znaków
   EN: With Tempered Secret, Sever the Form
   PL: With Tempered Secret, Sever the Form
619. [Umiejętność wroga [134809] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 참격 스킬 또는 료슈가 아니면,</u></b></mark></color> 코인 위력 +2, 피해량 +50%\n- 참격 스킬 또는 료슈에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n\n참격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +60%\n- 참격 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 최종 위력 +3\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].desc
   limit: do 1100 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Slash Skill or a non-Ryōshū unit</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Slash Skill or Ryōshū:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nSlash weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Slash weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Slash weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +60% damage\n- Non-Slash weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Final Power +3\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli ta jednostka ma [BlackNightmare]:\n- wszystkie Monety zmieniają się w [SuperCoin]y\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli przeciwnik w Starciu nie używa Umiejętności Cięcia i nie jest Ryōshū</u></b></mark></color>, Moc Monety +2 i zadaje +50% obrażeń\n- po przegranej w Starciu z Umiejętnością Cięcia albo z Ryōshū:\n  - Moc Monety -2 i zadaje o 50% mniej obrażeń\n  - obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n\nbroń Cięcia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], częstotliwość maleje\n- przy 150+ [KarmaOfIndexRien_2Phase], częstotliwość maleje dodatkowo\nefekty zależą od typu ataku używanej broni\n- broń Cięcia zadaje +60% obrażeń\n- broń niebędąca Cięciem zadaje o 30% mniej obrażeń\n[WhenUse] zyskuje 3 [Breath] i 2 Licznika [Breath]\n[WinDuel] Moc Końcowa +3\n- przy 150+ [KarmaOfIndexRien_2Phase], ten efekt nie uruchamia się
620. [Umiejętność wroga [134809] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [134809] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain +3 [Breath] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 3 Licznika [Breath]
622. [Umiejętność wroga [134809] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [134809] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [134809] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [134809] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134809].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [134810] (ulepszenie 1) — nazwa] 딸, 기억해? 이번 건 아마 너만 받아낼 수 있을 거야
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].name
   limit: do 90 znaków
   EN: Remember This, Sweetheart? Only You Can Clash Against This Move.
   PL: Remember This, Sweetheart? Only You Can Clash Against This Move.
627. [Umiejętność wroga [134810] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>료슈 이외의 대상이 합 불가능\n- 료슈는 속도와 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n일방 공격 시, 코인 위력 +2, 피해량 +50%\n[DefeatDuel]\n- 코인 위력 -2, 피해량 -50%\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndBattle] <color=#ff6000><mark=#ff000040><b><u>합에서 패배했으면, [BurningWoundRien] 1 얻음</u></b></mark></color>\n- [BlackNightmare] 관련 특수 효과가 있는 스킬 3종이 이번 턴 동안 전부 합에서 패배했으면, 대신 2 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [Sinking], [EndBattle], [BurningWoundRien], [BlackNightmare]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Sinking] = 침잠 / Sinking; [EndBattle] = [턴 종료 시] / [Turn End]; [BurningWoundRien] = 이글거리는 상처 / Sizzling Wound; [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts
   EN: <color=#ff6000><mark=#ff000040><b><u>Only Ryōshū can Clash against this Skill</u></b></mark></color>\n- Ryōshū can Clash with this Skill regardless of Speed\nOn Unopposed Attack, Coin Power +2 and deal +50% damage\n\n[DefeatDuel]\n- Coin Power -2 and deal -50% damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\n[EndBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit lost the Clash, gain 1 [BurningWoundRien]</u></b></mark></color>\n- If all 3 Skills with [BlackNightmare]-related unique effects lost the Clash this turn, gain 2 [BurningWoundRien] instead
   PL: <color=#ff6000><mark=#ff000040><b><u>tylko Ryōshū może stoczyć Starcie z tą Umiejętnością\n- Ryōshū może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\nprzy nieprzeciwstawianym ataku Moc Monety +2 i zadaje +50% obrażeń\n\n[DefeatDuel]\n- Moc Monety -2 i zadaje o 50% mniej obrażeń\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n\n[EndBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka przegrała Starcie, zyskuje 1 [BurningWoundRien]</u></b></mark></color>\n- jeżeli wszystkie 3 Umiejętności ze specjalnymi efektami [BlackNightmare] przegrały Starcie w tej turze, zamiast tego zyskuje 2 [BurningWoundRien]
628. [Umiejętność wroga [134810] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność wroga [134810] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [134810] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność wroga [134810] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [134810] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność wroga [134810] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134810].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność wroga [134811] (ulepszenie 1) — nazwa] Furioso [Crescendo]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134811].levelList[level=1].name
   limit: do 40 znaków
   EN: Furioso [Crescendo]
   PL: Furioso [Crescendo]
635. [Umiejętność wroga [134811] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 6 얻음, 자신의 [Breath] 횟수 6 증가\n- 합 위력 +10 (<color=#ff6000><mark=#ff000040><b><u>자신의 [KarmaOfIndexRien_2Phase] 20당 1씩 감소</u></b></mark></color>)\n[WhenUse] 정신력이 0 이상이면, 망 2개 생성\n- 피해량이 70%만큼 증가하고 최종 위력 +6\n[WinDuel]\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 4, [Binding] 2, [Vulnerable] 2 부여\n[DefeatDuel] \n- [AttackDmgDown] 6, [Paralysis] 9 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 25만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134811].levelList[level=1].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien_2Phase], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 6 [Breath] and +6 [Breath] Count\n- Clash Power +10 (<color=#ff6000><mark=#ff000040><b><u>Clash Power gained is reduced by 1 for every 20 [KarmaOfIndexRien_2Phase] on self</u></b></mark></color>)\n[WhenUse] At 0+ SP, generate 2 Mangs\n- Deal +70% damage; Final Power +6\n\n[WinDuel]\n- Attack End: Inflict 4 [Laceration], 2 [Binding], and 2 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Gain 6 [AttackDmgDown] and 9 [Paralysis]\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 25 SP\n[EndSkill] End this turn
   PL: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>ta Umiejętność nie uruchamia Umiejętności obrony celu</u></b></mark></color>\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- zyskuje 6 [Breath] i 6 Licznika [Breath]\n- Moc Starcia +10 (<color=#ff6000><mark=#ff000040><b><u>zyskiwana Moc Starcia maleje o 1 za każde 20 [KarmaOfIndexRien_2Phase] jednostki</u></b></mark></color>)\n[WhenUse] przy SP równym 0 lub więcej tworzy 2 Mang\n- zadaje +70% obrażeń; Moc Końcowa +6\n\n[WinDuel]\n- na koniec Ataku nakłada 4 [Laceration], 2 [Binding] i 2 [Vulnerable] w następnej turze wszystkim celom trafionym przez tę jednostkę\n[DefeatDuel]\n- zyskuje 6 [AttackDmgDown] i 9 [Paralysis]\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 25 SP\n[EndSkill] kończy tę turę
636. [Umiejętność wroga [134811] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134811].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [134811] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność wroga [134811] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134811].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [134811] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134811].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [134812] (ulepszenie 1) — nazwa] Furioso [Lacrimosa-Crescendo]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134812].levelList[level=1].name
   limit: do 50 znaków
   EN: Furioso [Lacrimosa-Crescendo]
   PL: Furioso [Lacrimosa-Crescendo]
641. [Umiejętność wroga [134812] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n<color=#ff6000><mark=#ff000040><b><u>- 료슈의 기본 E.G.O와 합 진행 시, 합 위력 -20</u></b></mark></color>\n[WhenUse]\n- [Breath] 9 얻음, 자신의 [Breath] 횟수 9 증가\n- 합 위력 +15 (자신의 [KarmaOfIndexRien_2Phase] 20당 1씩 감소)\n[WhenUse] 정신력이 0 이상이면, 망 3개 생성\n- 피해량이 100%만큼 증가하고 최종 위력 +12\n[WinDuel]\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 5, [Binding] 3, [Vulnerable] 3 부여\n[DefeatDuel] \n- [AttackDmgDown] 8, [Paralysis] 9 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음  \n[EndSkill] 망을 생성했으면, 정신력 30만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134812].levelList[level=1].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien_2Phase], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n<color=#ff6000><mark=#ff000040><b><u>- When Clashing against Ryōshū's base E.G.O, Clash Power -20</u></b></mark></color>\n\n[WhenUse]\n- Gain 9 [Breath] and +9 [Breath] Count\n- Clash Power +15 (Clash Power gained is reduced by 1 for every 20 [KarmaOfIndexRien_2Phase] on self)\n[WhenUse] At 0+ SP, generate 3 Mangs\n- Deal +100% damage; Final Power +12\n\n[WinDuel]\n- Attack End: Inflict 5 [Laceration], 3 [Binding], and 3 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Gain 8 [AttackDmgDown] and 9 [Paralysis]\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 30 SP\n[EndSkill] End this turn
   PL: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>ta Umiejętność nie uruchamia Umiejętności obrony celu</u></b></mark></color>\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n<color=#ff6000><mark=#ff000040><b><u>- podczas Starcia z bazowym E.G.O Ryōshū Moc Starcia -20</u></b></mark></color>\n\n[WhenUse]\n- zyskuje 9 [Breath] i 9 Licznika [Breath]\n- Moc Starcia +15 (zyskiwana Moc Starcia maleje o 1 za każde 20 [KarmaOfIndexRien_2Phase] jednostki)\n[WhenUse] przy SP równym 0 lub więcej tworzy 3 Mang\n- zadaje +100% obrażeń; Moc Końcowa +12\n\n[WinDuel]\n- na koniec Ataku nakłada 5 [Laceration], 3 [Binding] i 3 [Vulnerable] w następnej turze wszystkim celom trafionym przez tę jednostkę\n[DefeatDuel]\n- zyskuje 8 [AttackDmgDown] i 9 [Paralysis]\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; przy trafieniu nie uruchamia [Sinking] celu\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 30 SP\n[EndSkill] kończy tę turę
642. [Umiejętność wroga [134812] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134812].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [134812] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134812].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [134812] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134812].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [134812] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=134812].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność wroga [132216] (ulepszenie 1) — nazwa] 원망[怨望]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132216].levelList[level=1].name
   limit: do 40 znaków
   EN: Resentment [怨望]
   PL: Resentment [怨望]
647. [Umiejętność wroga [132216] (ulepszenie 1) — opis] [StartBattle] 이 스킬을 사용하는 슬롯에 메인 타겟으로 지정된 공격 스킬이 있으면 자신의 [Breath] 위력 10 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132216].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: [StartBattle] If the Skill Slot using this Skill is a main target of an Attack Skill, lose 10 [Breath] Potency
   PL: [StartBattle] jeżeli w slocie tej Umiejętności wskazany jest cel główny Umiejętności ataku, traci 10 Siły [Breath]
648. [Umiejętność wroga [132217] (ulepszenie 1) — nazwa] 비망[非望]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132217].levelList[level=1].name
   limit: do 40 znaków
   EN: Futility [非望]
   PL: Futility [非望]
649. [Umiejętność wroga [132217] (ulepszenie 1) — opis] [StartBattle] 이 스킬을 사용하는 슬롯에 메인 타겟으로 지정된 공격 스킬이 있으면 자신의 정신력 5 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132217].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] If the Skill Slot using this Skill is a main target of an Attack Skill, lose 5 SP
   PL: [StartBattle] jeżeli w slocie tej Umiejętności wskazany jest cel główny Umiejętności ataku, traci 5 SP
650. [Umiejętność wroga [132218] (ulepszenie 1) — nazwa] 낙망[落望]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132218].levelList[level=1].name
   limit: do 40 znaków
   EN: Dismay [落望]
   PL: Dismay [落望]
651. [Umiejętność wroga [132218] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] [Reduction] 3 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132218].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [DefeatDuel], [Reduction]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] Gain 3 [Reduction]</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] zyskuje 3 [Reduction]</u></b></mark></color>
652. [Umiejętność wroga [132218] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132218].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Gain 1 [Vulnerable]
   PL: [OnSucceedAttack] zyskuje 1 [Vulnerable]
653. [Umiejętność wroga [132219] (ulepszenie 1) — nazwa] 당신이 원망스러워, 하지만...
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132219].levelList[level=1].name
   limit: do 40 znaków
   EN: I resent you so. But...
   PL: I resent you so. But...
654. [Umiejętność wroga [132219] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] [Vulnerable] 2 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132219].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [DefeatDuel], [Vulnerable]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] Gain 2 [Vulnerable]</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] zyskuje 2 [Vulnerable]</u></b></mark></color>
655. [Umiejętność wroga [132219] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=132219].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p3] Pasywka wroga: Passives_Abnormality-a1c9p3
- plik gry: `Passives_Abnormality-a1c9p3.json`

656. [[a1c9p3] Pasywka wroga [133303] — nazwa] 아이언메이든- 재세동
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133303].name
   limit: do 40 znaków
   EN: Iron Maiden - Defibrillation
   PL: Iron Maiden - Defibrillation
657. [[a1c9p3] Pasywka wroga [133303] — opis] 흐트러짐 상태가 되면, 흐트러짐 상태를 해제하고 이번 턴을 종료함 (전투당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133303].desc
   limit: do 120 znaków
   EN: When Staggered, recover from Stagger and end this turn (once per Encounter)
   PL: gdy przejdzie w Oszołamienie, dochodzi do siebie z Oszołamienia i kończy tę turę (1 raz na walkę)
658. [[a1c9p3] Pasywka wroga [133101] — nazwa] 제 모든 신체 요소는 이미 티비아에
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133101].name
   limit: do 60 znaków
   EN: All of My Corpus has been Given to Tibia
   PL: All of My Corpus has been Given to Tibia
659. [[a1c9p3] Pasywka wroga [133101] — opis] [Combustion], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력 피해량 -30%\n[Laceration]로 받는 피해량 -50%\n\n턴 시작 시, 흐트러짐 상태면 흐트러짐 해제. 이후 [CrimsonTakeDamageUp] 2 얻고 다음 턴까지 ‘설치 미술 제 3호 ‘간이늑골’’ 사용 불가능 (전투당 1회)\n\n턴 종료 시 자신의 [Combustion] 4당, 다음 턴에 [DefenseDown] 1 얻음 (최대 15)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133101].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [Burst], [Sinking], [Laceration], [CrimsonTakeDamageUp], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Take -30% HP, SP damage from [Combustion], [Burst], and [Sinking]; -30% to Stagger Threshold raised by [Vibration]\nTake -50% damage from [Laceration]\n\nTurn Start: If this unit is Staggered, recover from Stagger. Afterward, gain 2 [CrimsonTakeDamageUp] and becomes unable to use 'Installation Art no. 3: Improvised Ribcage' until next turn (once per Encounter)\n\nTurn End: Gain 1 [DefenseDown] next turn for every 4 [Combustion] on self (max 15)
   PL: otrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Burst] i [Sinking]; otrzymuje o 30% mniej wzrostu Próg Oszołomienia od [Vibration]\notrzymuje o 50% mniej obrażeń od [Laceration]\n\nna Początku tury, jeżeli jest w Oszołamieniu, dochodzi do siebie z Oszołamienia. następnie zyskuje 2 [CrimsonTakeDamageUp] i do następnej tury nie może użyć „Installation Art no. 3: Improvised Ribcage” (1 raz na walkę)\n\nna koniec tury zyskuje 1 [DefenseDown] w następnej turze za każde 4 [Combustion] jednostki (maks. 15)
660. [[a1c9p3] Pasywka wroga [133102] — nazwa] 신체중심미술
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133102].name
   limit: do 40 znaków
   EN: Corpus-centric Art
   PL: Corpus-centric Art
661. [[a1c9p3] Pasywka wroga [133102] — opis] 등장 시 정신력 30 회복\n\n공격 스킬 적중 시 부정적인 효과를 부여하고 동시에 긍정적인 효과를 얻으면, 공격 종료 시 정신력 4 회복\n- 이 효과로 정신력 회복 시 자신의 정신력이 최대면 다음 턴에 [ResultEnhancement] 1 얻음 (턴당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133102].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [ResultEnhancement]
   znaczenie tagów: [ResultEnhancement] = 위력 증가 / Power Up
   EN: When this unit enters the Encounter, heal 30 SP\n\nOn Hit with Attack Skill: If this unit inflicts negative effect and gains beneficial effect simultaneously, heal 4 SP at Attack End\n- If this unit is at max SP when healing SP with the above effect, gain 1 [ResultEnhancement] next turn (once per turn)
   PL: przy pojawieniu się przywraca 30 SP\n\nprzy trafieniu Umiejętnością ataku, jeżeli jednostka nakłada negatywny efekt i jednocześnie zyskuje pozytywny efekt, na koniec Ataku przywraca 4 SP\n- jeżeli przy przywracaniu SP tym efektem jednostka ma Maks. SP, zyskuje 1 [ResultEnhancement] w następnej turze (1 raz na turę)
662. [[a1c9p3] Pasywka wroga [133102] — tekst klimatyczny] 현장에서 상대의 뼈와 근육을 재료로 삼아 전투를 조형하고, 그 과정이 이어질수록 작은 뼛조각마저 정교한 무기가 되어가는 미술.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133102].flavor
   limit: do 260 znaków
   EN: A form of art that sculpts and exhibits artworks using bones and muscles as the material. Each act of creation incorporates even the tiniest of bone shards into the artist's intricately-crafted weapon.
   PL: Sztuka, która rzeźbi i eksponuje dzieła, używając kości i mięśni jako materiału. Każdy akt tworzenia włącza nawet najdrobniejsze odłamki kości w misternie rzeźbioną broń artysty.
663. [[a1c9p3] Pasywka wroga [133103] — nazwa] 재료는 언제나 현장에서 수급하고 가공하는 것이 미학
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133103].name
   limit: do 90 znaków
   EN: The Aesthetics of Harvesting and Trimming the Ingredient On-site
   PL: The Aesthetics of Harvesting and Trimming the Ingredient On-site
664. [[a1c9p3] Pasywka wroga [133103] — opis] 스킬 종료 시 자신의 스킬로 피해를 줬으면, 대상 하나당 [HumanBoneTheRings] 30, [HumanBloodTheRings] 1 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133103].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [HumanBoneTheRings], [HumanBloodTheRings]
   znaczenie tagów: [HumanBoneTheRings] = 생체 재료(뼈) / Corpus Ingredient (Bones); [HumanBloodTheRings] = 생체 재료(피) / Corpus Ingredient (Blood)
   EN: After using a Skill, gain 30 [HumanBoneTheRings] and 1 [HumanBloodTheRings] for every target damaged by this unit's Skill
   PL: po zakończeniu Umiejętności, jeżeli jednostka zadała obrażenia Umiejętnością, zyskuje 30 [HumanBoneTheRings] i 1 [HumanBloodTheRings] za każdego trafionego celu
665. [[a1c9p3] Pasywka wroga [133104] — nazwa] 일생의 작품 티비아
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133104].name
   limit: do 40 znaków
   EN: Magnum Opus: Tibia
   PL: Magnum Opus: Tibia
666. [[a1c9p3] Pasywka wroga [133104] — opis] 턴 종료시 [HumanBoneTheRings]가 206이고 [HumanBloodTheRings]가 5면 각각 수치만큼 감소하고 [MineTheRings] 1 얻음\n\n턴 시작시 [MineTheRings]가 있으면, 이번 턴에 강력한 공격 사용\n\n강력한 공격 사용 전에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음</u></b></mark></color> (스킬당 1회. 턴당 최대 3회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133104].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HumanBoneTheRings], [HumanBloodTheRings], [MineTheRings], [PlusCoinValueDown], [ResultReduction]
   znaczenie tagów: [HumanBoneTheRings] = 생체 재료(뼈) / Corpus Ingredient (Bones); [HumanBloodTheRings] = 생체 재료(피) / Corpus Ingredient (Blood); [MineTheRings] = 작품명: 티비아 / Artwork: Tibia; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down
   EN: Turn End: At 206 [HumanBoneTheRings] and 5 [HumanBloodTheRings], reduce the Stack of each effect equal to those numbers respectively and gain 1 [MineTheRings]\n\nTurn Start: If this unit has [MineTheRings], use a powerful attack this turn\n\n<color=#ff6000><mark=#ff000040><b><u>When hit by an Attack Skill before using the powerful attack, gain 1 [PlusCoinValueDown] and 1 [ResultReduction]</u></b></mark></color> (once per Skill; max 3 times per turn)
   PL: na koniec tury przy 206 [HumanBoneTheRings] i 5 [HumanBloodTheRings] zmniejsza Licznik każdego z tych efektów o odpowiednią wartość i zyskuje 1 [MineTheRings]\n\nna Początku tury, jeżeli ta jednostka ma [MineTheRings], używa w tej turze potężnego ataku\n\n<color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku przed użyciem potężnego ataku, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction]</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)
667. [[a1c9p3] Pasywka wroga [133104] — tekst klimatyczny] 자신의 모든 육체를 쏟아붓고 깎아내어 완성한 역작, 티비아
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133104].flavor
   limit: do 180 znaków
   EN: Tibia, the work of the artist's life, completed by breaking his own corpus and pouring his blood to the last drop—in the most literal sense.
   PL: Tibia — dzieło życia artysty, ukończone przez połamanie własnego ciała i przelanie krwi do ostatniej kropli — w najbardziej dosłownym tego słowa znaczeniu.
668. [[a1c9p3] Pasywka wroga [133105] — nazwa] 만족스러운 예술
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133105].name
   limit: do 50 znaków
   EN: Artwork Pleasing to the Senses
   PL: Artwork Pleasing to the Senses
669. [[a1c9p3] Pasywka wroga [133105] — opis] [MineTheRings] 소멸 시 아래 대상의 정신력을 30 회복하고 다음 턴에 아래 대상이 [AttackUp] 2, [DefenseUp] 2 얻음\n- 약지 아비 - 칼리스토\n- 약지 제자 - 알비나\n- 신체관극[TabExplain]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133105].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [MineTheRings], [AttackUp], [DefenseUp], [TabExplain]
   znaczenie tagów: [MineTheRings] = 작품명: 티비아 / Artwork: Tibia; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: When [MineTheRings] expires, the following units heal 30 SP and gain 2 [AttackUp] and 2 [DefenseUp] next turn:\n- The Ring Nursefather - Callisto\n- The Ring Apprentice - Albina\n- Corpus Theater[TabExplain]
   PL: gdy [MineTheRings] wygasają, wymienione niżej jednostki przywracają 30 SP i zyskują 2 [AttackUp] i 2 [DefenseUp] w następnej turze:\n- The Ring Nursefather - Callisto\n- The Ring Apprentice - Albina\n- Corpus Theater[TabExplain]
670. [[a1c9p3] Pasywka wroga [133106] — nazwa] 제자의 전시를 잠시 감상해 볼까요
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133106].name
   limit: do 70 znaków
   EN: Allow Me to Briefly Enjoy My Pupil's Exhibition
   PL: Allow Me to Briefly Enjoy My Pupil's Exhibition
671. [[a1c9p3] Pasywka wroga [133106] — opis] 자신에게 [SupportProtect]가 있으면, <color=#ff6000><mark=#ff000040><b><u>합 시작 시 [SupportProtect] 1 감소</u></b></mark></color> (스킬당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133106].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [SupportProtect]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense
   EN: If this unit has [SupportProtect], <color=#ff6000><mark=#ff000040><b><u>lose 1 [SupportProtect] on Clash Start</u></b></mark></color> (once per Skill)
   PL: jeżeli ta jednostka ma [SupportProtect], <color=#ff6000><mark=#ff000040><b><u>na początku Starcia traci 1 [SupportProtect]</u></b></mark></color> (1 raz na Umiejętność)
672. [[a1c9p3] Pasywka wroga [133107] — nazwa] 신체극복
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133107].name
   limit: do 40 znaków
   EN: Transcend the Corpus
   PL: Transcend the Corpus
673. [[a1c9p3] Pasywka wroga [133107] — opis] 자신의 체력이 50% 미만인 경우, 흐트러짐 상태를 해제하고 이번 턴을 종료함\n- 이 효과가 발동한 다음 턴 시작 시 마지막 스킬 슬롯에 ‘폐장 - 설치미술 제 1호 ‘당신들이 흩뿌린 살과 뼈가 객석이 되어’’ 장착
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133107].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At less than 50% HP, recover from Stagger and end this turn\n- Following the activation of this effect, equip 'Closing Time - Installation Art no. 1: Your Flesh and Bones as the Gallery's Seats' on this unit's last Skill Slot at the start of the next turn
   PL: przy HP niższym niż 50% dochodzi do siebie z Oszołamienia i kończy tę turę\n- po uruchomieniu tego efektu wyposaża „Closing Time - Installation Art no. 1: Your Flesh and Bones as the Gallery's Seats” na ostatnim slocie Umiejętności tej jednostki na początku następnej tury
674. [[a1c9p3] Pasywka wroga [133109] — nazwa] 뛰어다니는 관객은 의자에 앉아 감상하시죠
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133109].name
   limit: do 60 znaków
   EN: Please, Do Stop Running and Be Seated
   PL: Please, Do Stop Running and Be Seated
675. [[a1c9p3] Pasywka wroga [133109] — opis] 턴 종료 시 속도가 가장 빠른 수감자 및 조력자에게 다음 턴에 [RedemptionTheRings] 부여
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133109].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [RedemptionTheRings]
   znaczenie tagów: [RedemptionTheRings] = 재료가 떨어지는 상처 / Ingredient-shedding Wound
   EN: Turn End: Inflict [RedemptionTheRings] next turn to the Sinner and Assist Unit with the fastest Speed
   PL: na koniec tury nakłada [RedemptionTheRings] w następnej turze Grzesznikowi i jednostce wsparcia z najwyższą Szybkością
676. [[a1c9p3] Pasywka wroga [133201] — nazwa] 구속
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133201].name
   limit: do 40 znaków
   EN: Bondage
   PL: Bondage
677. [[a1c9p3] Pasywka wroga [133201] — opis] 신체관극과 연결된 캐릭터에게 아래의 효과가 적용됨\n- 행동 불가능 상태가 됨\n- 버프, 체력, 정신력이 갱신되지 않음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133201].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply the following effects to the unit tethered to Corpus Theater:\n- Become 'immobilized'\n- This unit's buffs, HP, and SP cannot be changed
   PL: nakłada następujące efekty na jednostkę powiązaną z Corpus Theater:\n- przechodzi w stan „unieruchomienia”\n- bonusy, HP i SP tej jednostki nie mogą się zmieniać
678. [[a1c9p3] Pasywka wroga [133202] — nazwa] 재료 수확
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133202].name
   limit: do 40 znaków
   EN: Ingredient Harvest
   PL: Ingredient Harvest
679. [[a1c9p3] Pasywka wroga [133202] — opis] 신체관극이 약지 아비에게 처치되면, 연결된 캐릭터는 전투 불가 상태가 됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133202].desc
   limit: do 150 znaków
   EN: If Corpus Theater is destroyed by the Ring Nursefather, the tethered unit becomes unavailable for the Encounter
   PL: jeżeli Corpus Theater zostanie zniszczone przez The Ring Nursefather, powiązana jednostka staje się niedostępna w tej walce
680. [[a1c9p3] Pasywka wroga [133203] — nazwa] 예술로부터의 생존
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133203].name
   limit: do 40 znaków
   EN: Escape from the Art
   PL: Escape from the Art
681. [[a1c9p3] Pasywka wroga [133203] — opis] 신체관극이 약지 아비 외 다른 캐릭터에게 처치되면, 아래의 효과가 발동됨\n- 다음 턴에 연결된 캐릭터가 전투에 복귀하고 정신력이 10 미만이면, 정신력이 10이 됨\n- 약지 아비와 약지 제자의 정신력 10 감소\n- 모든 E.G.O 자원 2개씩 획득
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133203].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If Corpus Theater is destroyed by units other than the Ring Nursefather, activate the following effects:\n- The tethered unit returns to battle next turn; if the unit is at less than 10 SP, heal SP to 10\n- The Ring Nursefather and The Ring Apprentice lose 10 SP\n- Gain 2 E.G.O Resource for all Affinities
   PL: jeżeli Corpus Theater zostanie zniszczone przez jednostkę inną niż The Ring Nursefather, uruchamiają się następujące efekty:\n- powiązana jednostka wraca do walki w następnej turze; jeżeli ma mniej niż 10 SP, przywraca SP do 10\n- The Ring Nursefather i The Ring Apprentice tracą 10 SP\n- zyskuje po 2 zasobów E.G.O każdej Afinności
682. [[a1c9p3] Pasywka wroga [133204] — nazwa] 가연성 소재
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133204].name
   limit: do 40 znaków
   EN: Flammable Material
   PL: Flammable Material
683. [[a1c9p3] Pasywka wroga [133204] — opis] [Combustion]으로 받는 피해가 2배가 됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133204].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Take x2 damage from [Combustion]
   PL: otrzymuje 2x obrażeń od [Combustion]
684. [[a1c9p3] Pasywka wroga [133601] — nazwa] 재료가 된 육체의 맥동
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133601].name
   limit: do 70 znaków
   EN: The Pulse and Beat of Corpus-turned-Ingredient
   PL: The Pulse and Beat of Corpus-turned-Ingredient
685. [[a1c9p3] Pasywka wroga [133601] — opis] [Combustion], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%\n[Laceration]로 받는 피해량 -50%\n\n턴 종료 시 자신의 [Combustion] 4당, 다음 턴에 [DefenseDown] 1 얻음 (최대 15)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133601].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [Burst], [Sinking], [Laceration], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Take -30% HP, SP damage from [Combustion], [Burst], and [Sinking]; -30% to Stagger Threshold raised by [Vibration]\nTake -50% damage from [Laceration]\n\nTurn End: Gain 1 [DefenseDown] next turn for every 4 [Combustion] on self (max 15)
   PL: otrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Burst] i [Sinking]; otrzymuje o 30% mniej wzrostu Próg Oszołomienia od [Vibration]\notrzymuje o 50% mniej obrażeń od [Laceration]\n\nna koniec tury zyskuje 1 [DefenseDown] w następnej turze za każde 4 [Combustion] jednostki (maks. 15)
686. [[a1c9p3] Pasywka wroga [133601] — tekst klimatyczny] 알비나의 피와 살로 만들어진 파시아.\n뇌만 남은 알비나와, 뇌만 없는 파시아.\n어떤 존재가 진정한 육체를 소유하고 있는가에 대한 질문을 던진다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133601].flavor
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fascia is made of Albina's flesh and blood.\nNow, Albina has only the brain, while Fascia lacks only the brain.\nFood for thought: Which of them possesses the true corpus?
   PL: Fascia została stworzona z ciała i krwi Albiny.\nAlbina ma teraz tylko mózg, a Fascia brakuje tylko mózgu.\nPytanie do przemyślenia: która z nich posiada prawdziwe ciało?
687. [[a1c9p3] Pasywka wroga [133602] — nazwa] 신체파
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133602].name
   limit: do 40 znaków
   EN: Corporism
   PL: Corporism
688. [[a1c9p3] Pasywka wroga [133602] — opis] 공격 스킬 적중 시 부정적인 효과를 부여하고 동시에 긍정적인 효과를 얻으면, 정신력 4 회복\n- 이 효과로 정신력 회복 시 자신의 정신력이 최대면 다음 턴에 [Agility] 1 얻음 (턴당 2회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133602].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: On Hit with Attack Skills: If this unit inflicts negative effect and gains beneficial effect simultaneously, heal 4 SP\n- If this unit is at max SP when healing SP with the above effect, gain 1 [Agility] next turn (2 times per turn)
   PL: przy trafieniu Umiejętnościami ataku, jeżeli jednostka nakłada negatywny efekt i jednocześnie zyskuje pozytywny efekt, przywraca 4 SP\n- jeżeli przy przywracaniu SP tym efektem jednostka ma Maks. SP, zyskuje 1 [Agility] w następnej turze (2 razy na turę)
689. [[a1c9p3] Pasywka wroga [133603] — nazwa] 소중한 작품 파시아
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133603].name
   limit: do 40 znaków
   EN: Fascia, My Precious Artwork
   PL: Fascia, My Precious Artwork
690. [[a1c9p3] Pasywka wroga [133603] — opis] 턴 종료 시 [HumanFleshTheRings]가 2면, 다음 턴에 [HumanFleshTheRings] 소멸 후 [BoneBladeTheRings] 얻음\n\n턴 시작 시 [BoneBladeTheRings]가 있으면, 이번 턴에 강력한 공격 사용\n\n강력한 공격 사용 전에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음</u></b></mark></color> (스킬당 1회. 턴당 최대 3회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133603].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HumanFleshTheRings], [BoneBladeTheRings], [PlusCoinValueDown], [ResultReduction]
   znaczenie tagów: [HumanFleshTheRings] = 생체 재료 / Corpus Ingredient; [BoneBladeTheRings] = 작품명: 파시아 / Artwork: Fascia; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down
   EN: Turn End: At 2 [HumanFleshTheRings], remove [HumanFleshTheRings] and gain [BoneBladeTheRings] next turn\n\nTurn Start: If this unit has [BoneBladeTheRings], use a powerful attack this turn\n\n<color=#ff6000><mark=#ff000040><b><u>When hit by an Attack Skill before using the powerful attack, gain 1 [PlusCoinValueDown] and 1 [ResultReduction]</u></b></mark></color> (once per Skill; max 3 times per turn)
   PL: na koniec tury przy 2 [HumanFleshTheRings], w następnej turze usuwa [HumanFleshTheRings] i zyskuje [BoneBladeTheRings]\n\nna Początku tury, jeżeli ta jednostka ma [BoneBladeTheRings], używa w tej turze potężnego ataku\n\n<color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku przed użyciem potężnego ataku, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction]</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)
691. [[a1c9p3] Pasywka wroga [133604] — nazwa] 갤러리에서는 갤러리만의 감상 규칙이 있는 법
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133604].name
   limit: do 70 znaków
   EN: Visitors Must Respect the Rules of the Gallery
   PL: Visitors Must Respect the Rules of the Gallery
692. [[a1c9p3] Pasywka wroga [133604] — opis] 자신에게 [SupportProtect]가 있으면, <color=#ff6000><mark=#ff000040><b><u>합 시작 시 [SupportProtect] 1 감소</u></b></mark></color> (스킬당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133604].desc
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [[a1c9p3] Pasywka wroga [133606] — nazwa] 마에스트로님의 앞에서 작품으로 증명해 보이겠어
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133606].name
   limit: do 80 znaków
   EN: With this Artwork, I will Prove Myself before the Maestro
   PL: With this Artwork, I will Prove Myself before the Maestro
694. [[a1c9p3] Pasywka wroga [133606] — opis] 약지 아비 등장 시 자신의 정신력이 20미만이면, 정신력이 20이 됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133606].desc
   limit: do 120 znaków
   EN: At less than 20 SP when the Ring Nursefather enters the Encounter, heal SP to 20
   PL: jeżeli przy pojawieniu się The Ring Nursefather jednostka ma mniej niż 20 SP, przywraca SP do 20
695. [[a1c9p3] Pasywka wroga [132701] — nazwa] 원한 문신 [<s>큰 형님</s>]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132701].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: Vengeance Tattoos [<s>Great Brother</s>]
   PL: Vengeance Tattoos [<s>Great Brother</s>]
696. [[a1c9p3] Pasywka wroga [132701] — opis] [Combustion], [Laceration], [Vibration], [Burst]로 받는 피해량 -30% (소수점 버림)\n받는 흐트러짐 피해량 - 50% (소수점 버림)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132701].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture
   EN: Takes -30% damage from [Combustion], [Laceration], [Vibration], and [Burst] (rounded down)\n-50% to the amount of Stagger Threshold raised (rounded down)
   PL: otrzymuje o 30% mniej obrażeń od [Combustion], [Laceration], [Vibration] i [Burst] (zaokrąglając w dół)\notrzymuje o 50% mniej wzrostu Próg Oszołomienia (zaokrąglając w dół)
697. [[a1c9p3] Pasywka wroga [132702] — nazwa] 앙갚음 장부
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132702].name
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL: The Book of Vengeance
698. [[a1c9p3] Pasywka wroga [132702] — opis] 스테이지 시작시 모든 수감자와 LCD 캐릭터에게 [VengeanceBookSpider]를 부여함\n\n이번 턴 적중한 스킬 수가 3개를 초과 했으면, 초과된 스킬 수만큼 다음 턴에 [ReinforcedTattooSpider] 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132702].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [VengeanceBookSpider], [ReinforcedTattooSpider]
   znaczenie tagów: [VengeanceBookSpider] = 앙갚음 장부 / The Book of Vengeance; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]
   EN: Encounter Start: Inflict [VengeanceBookSpider] on all Sinners and LCD units\n\nIf this unit hit with more than 3 Skills this turn, gain 1 [ReinforcedTattooSpider] next turn for every excess Skill that hit
   PL: Początek walki: nakłada [VengeanceBookSpider] wszystkim Grzesznikom i jednostkom LCD\n\njeżeli w tej turze trafiono więcej niż 3 Umiejętnościami, zyskuje 1 [ReinforcedTattooSpider] w następnej turze za każdą nadwyżkową Umiejętność, która trafiła
699. [[a1c9p3] Pasywka wroga [132703] — nazwa] 딸램 교육
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132703].name
   limit: do 40 znaków
   EN: My Daughter's Education
   PL: My Daughter's Education
700. [[a1c9p3] Pasywka wroga [132703] — opis] 합 승리시 [DaughterEducationSpider] 1 얻음\n\n스킬 적중시 [DaughterEducationSpider] 1 얻음 (스킬당 1회, 파괴된 코인일 경우 얻지 않음)\n\n턴의 가장 처음 사용하는 스킬의 합 승리시 [DaughterEducationSpider]을 1 추가로 얻고, 해당 스킬의 코인 위력 +1
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132703].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [DaughterEducationSpider]
   znaczenie tagów: [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: On Clash Win, gain 1 [DaughterEducationSpider]\n\nOn Hit with a Skill, gain 1 [DaughterEducationSpider] (once per Skill; this effect does not activate for Cracked Coins)\n\nOn Clash Win with the first-used Skill in a turn, gain 1 more [DaughterEducationSpider] and the Skill gains Coin Power +1
   PL: po wygranej w Starciu zyskuje 1 [DaughterEducationSpider]\n\nprzy trafieniu Umiejętnością zyskuje 1 [DaughterEducationSpider] (1 raz na Umiejętność; ten efekt nie uruchamia się dla Rozbitych Monet)\n\npo wygranej w Starciu pierwszą używaną w turze Umiejętnością zyskuje dodatkowe 1 [DaughterEducationSpider], a ta Umiejętność zyskuje Moc Monety +1
701. [[a1c9p3] Pasywka wroga [132704] — nazwa] 원한
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132704].name
   limit: do 40 znaków
   EN: Resentment
   PL: Resentment
702. [[a1c9p3] Pasywka wroga [132704] — opis] 스킬 2회 피격 시 [ResentmentSpider] 1 얻음, [DaughterEducationSpider] 1 감소 (피격 횟수는 누적됨)\n\n자신의 [ResentmentSpider]이 최댓값이면 강력한 공격을 사용함\n\n턴 종료시 자신의 체력이 80%, 60%, 40% 미만이면, [ResentmentSpider] 최댓값으로 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132704].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [ResentmentSpider], [DaughterEducationSpider]
   znaczenie tagów: [ResentmentSpider] = 중지 - 원한 / The Middle - Grudge; [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: When hit by 2 Skills, gain 1 [ResentmentSpider] and lose 1 [DaughterEducationSpider] (number of hits taken is always tracked)\n\nAt max [ResentmentSpider] Stack, use a powerful attack\n\nTurn End: At less than 80% / 60% / 40% HP, max out this unit's [ResentmentSpider] Stack
   PL: przy otrzymaniu trafień 2 Umiejętnościami zyskuje 1 [ResentmentSpider] i traci 1 [DaughterEducationSpider] (liczba otrzymanych trafień jest zawsze śledzona)\n\nprzy Maks. Liczniku [ResentmentSpider] używa potężnego ataku\n\nna koniec tury przy HP niższym niż 80% / 60% / 40% zyskuje [ResentmentSpider] do Maksimum
703. [[a1c9p3] Pasywka wroga [132706] — nazwa] ???
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132706].name
   limit: do 40 znaków
   EN: ???
   PL: ???
704. [[a1c9p3] Pasywka wroga [132706] — opis] ???
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132706].desc
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [[a1c9p3] Pasywka wroga [134101] — nazwa] 원한 문신 최고 출력… 레바테인 봉인 해제다!
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134101].name
   limit: do 70 znaków
   EN: Vengeance Tattoos Max Output... Unseal Lævateinn!
   PL: Vengeance Tattoos Max Output... Unseal Lævateinn!
706. [[a1c9p3] Pasywka wroga [134101] — opis] [MiddleFatherSwordFour] 해방 시 [MiddleFatherGuts]을 얻음\n\n[MosesRedBreathCharge]을 보유한 캐릭터를 타겟팅함
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134101].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFatherSwordFour], [MiddleFatherGuts], [MosesRedBreathCharge]
   znaczenie tagów: [MiddleFatherSwordFour] = 레바테인 / Lævateinn; [MiddleFatherGuts] = 초근성 / Ridiculous Grit; [MosesRedBreathCharge] = 깊은 숨 - 붉은색 / Deep Breath - Red
   EN: When [MiddleFatherSwordFour] is unsealed, this unit gains [MiddleFatherGuts]\n\nTargets the unit with [MosesRedBreathCharge]
   PL: gdy [MiddleFatherSwordFour] zostaje uwolniona, ta jednostka zyskuje [MiddleFatherGuts]\n\nwskazuje jednostkę posiadającą [MosesRedBreathCharge]
707. [[a1c9p3] Pasywka wroga [132801] — nazwa] 이렇게 하면 되는거죠 아빠!
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132801].name
   limit: do 50 znaków
   EN: Am I doing this right, Papa?!
   PL: Am I doing this right, Papa?!
708. [[a1c9p3] Pasywka wroga [132801] — opis] 스테이지 시작시 [HeatingWireOffSpider]를 가지고 시작함\n\n턴 시작 시 자신이 보유한 [GotACompliment]가 3 이상이면 해당 턴 동안 [HeatingWireOnSpider]으로 바뀌고, [Laceration]을 부여하는 스킬로 [Combustion]을 추가로 부여함\n\n턴 종료시 자신이 보유한 [GotACompliment]가 3 미만이면 [HeatingWireOnSpider]이 [HeatingWireOffSpider]로 전환됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132801].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOffSpider], [GotACompliment], [HeatingWireOnSpider], [Laceration], [Combustion]
   znaczenie tagów: [HeatingWireOffSpider] = 열선 OFF / Thermal Blades OFF; [GotACompliment] = 칭찬 받았다! / I Got Praised!; [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: Begins Encounter with [HeatingWireOffSpider]\n\nTurn Start: At 3+ [GotACompliment], gain [HeatingWireOnSpider] for the turn and also inflict [Combustion] with Skills that inflict [Laceration]\n\nTurn End: At less than 3 [GotACompliment], convert this unit's [HeatingWireOnSpider] to [HeatingWireOffSpider]
   PL: rozpoczyna walkę z [HeatingWireOffSpider]\n\nna Początku tury, przy 3+ [GotACompliment], na czas tej tury zyskuje [HeatingWireOnSpider], a Umiejętności nakładające [Laceration] nakładają dodatkowo [Combustion]\n\nna koniec tury, przy mniej niż 3 [GotACompliment], [HeatingWireOnSpider] jednostki zmienia się w [HeatingWireOffSpider]
709. [[a1c9p3] Pasywka wroga [132801] — tekst klimatyczny] ‘아빠는 늘 칭찬해 주고 만화책도 사줘서 좋아.’
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132801].flavor
   limit: do 120 znaków
   EN: 'I like my papa because he always praises me and buys me comic books.'
   PL: 'Lubię tatę, bo zawsze mnie chwali i kupuje mi komiksy.'
710. [[a1c9p3] Pasywka wroga [132802] — nazwa] 중지식 문신
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132802].name
   limit: do 40 znaków
   EN: The Middle Styled Tattoos
   PL: The Middle Styled Tattoos
711. [[a1c9p3] Pasywka wroga [132802] — opis] 이번 턴 적중한 스킬 수가 2개를 초과했으면, 초과된 스킬 수만큼 다음 턴에 [ReinforcedTattooSpiderDaughter] 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132802].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [ReinforcedTattooSpiderDaughter]
   znaczenie tagów: [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos
   EN: If this unit hit with more than 2 Skills, gain 1 [ReinforcedTattooSpiderDaughter] next turn for every excess Skill that hit
   PL: jeżeli w tej turze trafiono więcej niż 2 Umiejętnościami, zyskuje 1 [ReinforcedTattooSpiderDaughter] w następnej turze za każdą nadwyżkową trafioną Umiejętność
712. [[a1c9p3] Pasywka wroga [132802] — tekst klimatyczny] “나도 언젠간 중지에서 가족으로 인정받고, 누님이랑 형님들이랑 계속 같이 살 수 있는 거야?”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132802].flavor
   limit: do 160 znaków
   EN: 'Will the bigger Sisters and Brothers of the Middle accept me as their family one day, so I can continue to live with them?'
   PL: 'Czy duże Siostry i Bracia z The Middle uznają mnie kiedyś za rodzinę, żebym mogła dalej żyć razem z nimi?'
713. [[a1c9p3] Pasywka wroga [132803] — nazwa] 칭찬은 키라도 춤추게 한다
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132803].name
   limit: do 50 znaków
   EN: Praise is the Wind in Her Sail
   PL: Praise is the Wind in Her Sail
714. [[a1c9p3] Pasywka wroga [132803] — opis] 합 승리시 [GotACompliment] 1 얻음\n\n스킬 적중시 [GotACompliment] 1 얻음 (스킬당 1회, 파괴된 코인일 경우 얻지 않음)\n\n턴의 가장 처음 사용하는 스킬의 합 승리시 [GotACompliment]를 1 추가로 얻고, 해당 스킬의 코인 위력 +1
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132803].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [GotACompliment]
   znaczenie tagów: [GotACompliment] = 칭찬 받았다! / I Got Praised!
   EN: On Clash Win, gain 1 [GotACompliment]\n\nOn Hit with a Skill, gain 1 [GotACompliment] (once per Skill; this effect does not activate for Cracked Coins)\n\nOn Clash Win with the first-used Skill in a turn, gain 1 more [GotACompliment] and the Skill gains Coin Power +1
   PL: po wygranej w Starciu zyskuje 1 [GotACompliment]\n\nprzy trafieniu Umiejętnością zyskuje 1 [GotACompliment] (1 raz na Umiejętność; ten efekt nie uruchamia się dla Rozbitych Monet)\n\npo wygranej w Starciu pierwszą używaną w turze Umiejętnością zyskuje dodatkowe 1 [GotACompliment], a ta Umiejętność zyskuje Moc Monety +1
715. [[a1c9p3] Pasywka wroga [132804] — nazwa] 중지는 반드시 갚는 거라 했어
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132804].name
   limit: do 60 znaków
   EN: I'm pretty sure the Middle never forgets
   PL: I'm pretty sure the Middle never forgets
716. [[a1c9p3] Pasywka wroga [132804] — opis] 스킬 2회 피격 시 [ResentmentSpiderDaughter] 1 얻음, [GotACompliment] 1 감소 (피격 횟수는 누적됨)\n\n자신의 [ResentmentSpiderDaughter]이 최댓값이면 강력한 공격을 사용함\n\n턴 종료시 자신의 체력이 80%, 60%, 40% 미만이면, [ResentmentSpiderDaughter] 최댓값으로 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132804].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [ResentmentSpiderDaughter], [GotACompliment]
   znaczenie tagów: [ResentmentSpiderDaughter] = 중지 - 원한 / The Middle - Grudge; [GotACompliment] = 칭찬 받았다! / I Got Praised!
   EN: When hit by 2 Skills, gain 1 [ResentmentSpiderDaughter] and lose 1 [GotACompliment] (number of hits taken is always tracked)\n\nAt max [ResentmentSpiderDaughter] Stack, use a powerful attack\n\nTurn End: At less than 80% / 60% / 40% HP, max out this unit's [ResentmentSpiderDaughter] Stack
   PL: przy otrzymaniu trafień 2 Umiejętnościami zyskuje 1 [ResentmentSpiderDaughter] i traci 1 [GotACompliment] (liczba otrzymanych trafień jest zawsze śledzona)\n\nprzy Maks. Liczniku [ResentmentSpiderDaughter] używa potężnego ataku\n\nna koniec tury przy HP niższym niż 80% / 60% / 40% zyskuje [ResentmentSpiderDaughter] do Maksimum
717. [[a1c9p3] Pasywka wroga [134201] — nazwa] 이렇게 하면 되는거죠 아빠!
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134201].name
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [[a1c9p3] Pasywka wroga [134201] — opis] 스테이지 시작시 [HeatingWireOffSpider]를 가지고 시작함\n\n턴 시작 시 자신이 보유한 [GotACompliment]가 3 이상이면 해당 턴 동안 [HeatingWireOnSpider]으로 바뀌고, [Laceration]을 부여하는 스킬로 [Combustion]을 추가로 부여함\n\n턴 종료시 자신이 보유한 [GotACompliment]가 3 미만이면 [HeatingWireOnSpider]이 [HeatingWireOffSpider]로 전환됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134201].desc
   (powtórzenie elementu 708 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [[a1c9p3] Pasywka wroga [134202] — nazwa] 저거... 욜라 위험해보이는데?
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134202].name
   limit: do 50 znaków
   EN: Whoa... That looks mad dangerous!
   PL: Whoa... That looks mad dangerous!
720. [[a1c9p3] Pasywka wroga [134202] — opis] 중지 아비가 [MiddleFatherSwordFour] 보유 시, [HeatingWireOffSpider] 상태가 되지 않음\n\n[MosesRedBreathCharge]을 보유한 캐릭터를 타겟팅함
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134202].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFatherSwordFour], [HeatingWireOffSpider], [MosesRedBreathCharge]
   znaczenie tagów: [MiddleFatherSwordFour] = 레바테인 / Lævateinn; [HeatingWireOffSpider] = 열선 OFF / Thermal Blades OFF; [MosesRedBreathCharge] = 깊은 숨 - 붉은색 / Deep Breath - Red
   EN: If the Middle Nursefather has [MiddleFatherSwordFour], does not enter [HeatingWireOffSpider] state\n\nTargets the unit with [MosesRedBreathCharge]
   PL: jeżeli The Middle Nursefather ma [MiddleFatherSwordFour], nie wchodzi w stan [HeatingWireOffSpider]\n\nwskazuje jednostkę posiadającą [MosesRedBreathCharge]
721. [[a1c9p3] Pasywka wroga [134202] — tekst klimatyczny] 그녀의 동물적인 직감과 선천적인 전투 센스가 본능적으로 말하고 있다. 저게 뭔지는 몰라도, 당하면 반드시 죽는다고.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134202].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The combination of her animalistic instincts and battle experience is screaming at her in unison:\nWhatever that red thing is, if she can't stop that attack from going off, it <b>will</b> kill.
   PL: Połączenie jej zwierzęcej intuicji i wrodzonego wyczucia walki krzyczy w niej jednym głosem:\ncokolwiek to czerwone jest, jeżeli nie powstrzyma tego ataku, on na pewno zabije.
722. [[a1c9p3] Pasywka wroga [132601] — nazwa] 고된 전투
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132601].name
   limit: do 40 znaków
   EN: Grueling Battle
   PL: Grueling Battle
723. [[a1c9p3] Pasywka wroga [132601] — opis] 최대 체력의 20%가 감소한 상태로 전투를 시작\n스테이지 시작 시 3턴간 [ResultReduction] 2 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132601].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [ResultReduction]
   znaczenie tagów: [ResultReduction] = 위력 감소 / Power Down
   EN: Begins battle with 20% missing HP\nFor the first 3 turns of the Encounter, gain 2 [ResultReduction]
   PL: rozpoczyna walkę z 20% brakującego HP\nprzez pierwsze 3 tury walki zyskuje 2 [ResultReduction]
724. [[a1c9p3] Pasywka wroga [132601] — tekst klimatyczny] 특색과의 전투는 그를 분명 강하게 만들었을것이다.\n살아남아 그 경험을 양분으로 삼을수만 있다면
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132601].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Meeting a Color Fixer in battle is doubtless an experience that will elevate his skills to the next level.\nIf he survives this battle, that is.
   PL: Spotkanie z Fixerem Koloru w walce to niewątpliwie doświadczenie, które podniesie jego umiejętności na wyższy poziom.\no ile przeżyje tę walkę.
725. [[a1c9p3] Pasywka wroga [132602] — nazwa] 무너져가는 자세
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132602].name
   limit: do 40 znaków
   EN: Crumbling Form
   PL: Crumbling Form
726. [[a1c9p3] Pasywka wroga [132602] — opis] [DuelEdge] 수치에 따라 다음 효과를 얻음 (중복 적용)\n- 수치 1당 부여된 대상에게 가하는 피해량 +10%, 받는 피해량 +10%\n- 3 이상이면, 부여된 대상과 합 진행 시 합 위력 +1\n- 5 이상이면, 부여된 대상과 합 진행 시 기본 위력 +1\n- 7 이상이면, 부여된 대상과 합 진행 시 코인 위력 +1\n- 10 이상이면, 부여된 대상과 합 진행 시 최종 위력 +1
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132602].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdge]
   znaczenie tagów: [DuelEdge] = 결투 고조 / The Duel Escalates
   EN: Gain the following effects based on the target's [DuelEdge] Stack\n- For every Stack, deal +10% damage against and take -10% damage from the target with [DuelEdge]\n- At 3+ Stack, in a Clash against targets with [DuelEdge], gain Clash Power +1\n- At 5+ Stack, in a Clash against targets with [DuelEdge], gain Base Power +1\n- At 7+ Stack, in a Clash against targets with [DuelEdge], gain Coin Power +1\n- At 10+ Stack, in a Clash against targets with [DuelEdge], gain Final Power +1
   PL: zyskuje następujące efekty w zależności od Licznika [DuelEdge] celu\n- za każdy Licznik zadaje +10% obrażeń i otrzymuje o 10% mniej obrażeń od celu z [DuelEdge]\n- przy 3+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Starcia +1\n- przy 5+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Bazowa +1\n- przy 7+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Monety +1\n- przy 10+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Końcowa +1
727. [[a1c9p3] Pasywka wroga [132603] — nazwa] 필사의 분전
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132603].name
   limit: do 40 znaków
   EN: Desperate Struggle
   PL: Desperate Struggle
728. [[a1c9p3] Pasywka wroga [132603] — opis] 엄지 아비가 참전한 이후부터 패시브‘사냥 표식’을 사용하지 않으며, 다음 효과가 추가됨\n- 정신력이 30미만인 경우 정신력이 30으로 회복\n- 턴 시작 시 [SupportProtect] 3 얻음\n<color=#ff6000><mark=#ff000040><b><u>- 속도에 관계없이 합을 할 수 있음\n- 베르길리우스와 우선으로 합을 진행</u></b></mark></color>\n- 엄지 아비가 합에서 승리하면, 해당 공격 종료 시 '콜피 소타니'로 일방 공격 (턴당 2회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132603].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SupportProtect]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense
   EN: After the Thumb Nursefather enters the field, deactivate the "Hunter's Mark" Passive and gain the following effects instead:\n- At less than 30 SP, heal up to 30 SP\n- Turn Start: Gain 3 [SupportProtect]\n<color=#ff6000><mark=#ff000040><b><u>- Can Clash regardless of Speed\n- Prioritize Clashing against Vergilius</u></b></mark></color>\n- When the Thumb Nursefather wins a Clash, and uses an Attack against the target, follow up with "Colpi Sottani" as an Unopposed Attack against the same target (2 times per turn)
   PL: od momentu, gdy The Thumb Nursefather wejdzie na pole bitwy, nie używa Pasywu „Hunter's Mark”, a zamiast tego zyskuje następujące efekty:\n- przy mniej niż 30 SP przywraca SP do 30\n- na Początku tury zyskuje 3 [SupportProtect]\n<color=#ff6000><mark=#ff000040><b><u>- może stoczyć Starcie niezależnie od Szybkości\n- priorytet: Starcie z Vergiliusem</u></b></mark></color>\n- gdy The Thumb Nursefather wygra Starcie i użyje Ataku na cel, następuje po nim „Colpi Sottani” jako nieprzeciwstawiany atak na tego samego celu (2 razy na turę)
729. [[a1c9p3] Pasywka wroga [132603] — tekst klimatyczny] ‘지금이라면, 죽일 수 있지 않을까.’\n\n잠에 든 스승을 보며, 루치오는 항상 같은 상념에 빠졌다.\n그 생각을 행동으로 옮기지 않는 것은, 이미 학습된 공포와 뒷골목에서 자신을 데려와 준 은혜 때문이었다.\n하지만 쌓여버린 원한이 너무나 깊다. 진심을 다해 명령을 따르겠다 말하면서도 루치오는 다짐했다.\n이 전투가 끝나면 반드시 죽이자. 남은 눈 하나까지 베고 찔러 죽여버리자.\n온몸에 멍이 든 소년의 눈에 처음으로 생기가 돌기 시작했다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132603].flavor
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'Maybe I can kill her now. Maybe this is my chance.'\n\nOnce again, the same contemplation comes to seize Lucio as he looms over his master, who lies fast asleep.\nBut this impulse remains an unactioned thought, for he had both fear born from experience and gratitude for his deliverance from the Backstreets.\nYet, his resentment runs too deep. Lucio makes a promise with himself, even as he swears utter fealty without a trace of deception:\n'Once this battle is behind us, I will kill her. I will gouge out her other eye and stab and slash at her, again and again, until she no longer moves.'\nFor the first time, fire burns in the eyes of the boy whose body is covered in bruises.
   PL: 'Może właśnie teraz mógłbym ją zabić. Może to jest moja szansa.'\n\nTen sam gnuśny nurt myśli ogarnia Lucio za każdym razem, gdy nachyla się nad śpiącą mistrzynią.\nPozostaje on jednak jedynie myślą — bo chłopaka trzyma strach wyuczony ze doświadczenia i wdzięczność za wyciągnięcie go z Zaułków.\nA jednak jego uraza jest zbyt głęboka. Lucio ślubuje sam sobie — nawet gdy bez śladu fałszu przysięga wierność rozkazom:\n„Kiedy ta walka się skończy, zabiję ją. Wyłupię jej pozostałe oko i będę ją kłuć i ciąć raz za razem, aż przestanie się ruszać.”\nPo raz pierwszy w oczach chłopca pokrytego siniakami zapłonął ogień.
730. [[a1c9p3] Pasywka wroga [132604] — nazwa] 사냥 표식
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132604].name
   limit: do 40 znaków
   EN: Hunter's Mark
   PL: Hunter's Mark
731. [[a1c9p3] Pasywka wroga [132604] — opis] 무작위 적 1명을 지정하여, 속도를 1로 만들고 모든 스킬의 타겟으로 지정한다\n이후 4턴마다 발동한다
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132604].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Randomly select an enemy, reduce their Speed to 1, and target it with all of this unit's Skills\nActivates every 4 turns after the initial activation
   PL: wskazuje losowego wroga, ustala jego Szybkość na 1 i wskazuje go celom wszystkich Umiejętności\nuruchamia się co 4 tury po pierwszym uruchomieniu
732. [[a1c9p3] Pasywka wroga [132606] — nazwa] 듀엘로 디스페라토
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132606].name
   limit: do 40 znaków
   EN: Duello Disperato
   PL: Duello Disperato
733. [[a1c9p3] Pasywka wroga [132606] — opis] 합 종료 시 합을 진행한 대상에게 [DuelEdge] 1 부여\n[DuelEdge]를 가진 대상과 합 진행 시 대상의 [DuelEdge] 수치 1당, 정신력 2 증가 (최대 10)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132606].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdge]
   znaczenie tagów: [DuelEdge] = 결투 고조 / The Duel Escalates
   EN: After Clashing, inflict 1 [DuelEdge] against the target this unit Clashed against\nIn a Clash against targets with [DuelEdge], heal 2 SP for every [DuelEdge] Stack on target (max 10)
   PL: po rozegraniu Starcia nakłada 1 [DuelEdge] celowi, z którym stoczyło Starcie\npodczas Starcia z celami posiadającymi [DuelEdge], przywraca 2 SP za każdy Licznik [DuelEdge] celu (maks. 10)
734. [[a1c9p3] Pasywka wroga [131401] — nazwa] 예지안
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131401].name
   limit: do 40 znaków
   EN: The Eye of Precognition
   PL: The Eye of Precognition
735. [[a1c9p3] Pasywka wroga [131401] — opis] 스테이지 등장 시, [FutureEyeOn] 30 얻음\n[FutureEyeOn] 수치가 0이 되면, [FutureEyeOn]이 [FutureEyeOff]로 변경됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131401].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [FutureEyeOn], [FutureEyeOff]
   znaczenie tagów: [FutureEyeOn] = 예지안 / Eye of Precognition; [FutureEyeOff] = 예지안 과열 / Eye of Precognition - Overheat
   EN: When this unit enters the Encounter, gain 30 [FutureEyeOn]\nAt 0 [FutureEyeOn] Stack, convert [FutureEyeOn] to [FutureEyeOff]
   PL: przy pojawieniu się w walce zyskuje 30 [FutureEyeOn]\ngdy Licznik [FutureEyeOn] spadnie do 0, [FutureEyeOn] zmienia się w [FutureEyeOff]
736. [[a1c9p3] Pasywka wroga [131401] — tekst klimatyczny] 오딘의 눈이라 불린 이 유물은, 사실 세 갈래로 쪼개진 어떤 유물의 파편 중 하나다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131401].flavor
   limit: do 140 znaków
   EN: This Relic, known as the Eye of Odin, is but a third of a whole Relic that was broken into three parts.
   PL: Ta Relikwia, znana jako Oko Odyna, to zaledwie jedna trzecia całej Relikwii, która została rozbita na trzy części.
737. [[a1c9p3] Pasywka wroga [131402] — nazwa] 가속하는 미래
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131402].name
   limit: do 40 znaków
   EN: Accelerating Future
   PL: Accelerating Future
738. [[a1c9p3] Pasywka wroga [131402] — opis] 합 진행 시 <color=#ff6000><mark=#ff000040><b><u>매 합마다 자신에게 [LookingFuture] 1 부여</u></b></mark></color>\n[LookingFuture]는 턴당 (턴 시작 시 보유한 [FutureEyeOn]/3)까지 얻을 수 있음\n[FutureEyeOn]이 있을 때, <color=#ff6000><mark=#ff000040><b><u>일방공격을 당하거나 합 패배 시 ‘예지’ 스킬 발동</u></b></mark></color>
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131402].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [LookingFuture], [FutureEyeOn]
   znaczenie tagów: [LookingFuture] = 가속하는 미래 / Accelerating Future; [FutureEyeOn] = 예지안 / Eye of Precognition
   EN: In a Clash, <color=#ff6000><mark=#ff000040><b><u>gain 1 [LookingFuture] with every Clash</u></b></mark></color>\nCan gain up to ([FutureEyeOn] Stack at Turn Start / 3) [LookingFuture] per turn\nWhile this unit has [FutureEyeOn], <color=#ff6000><mark=#ff000040><b><u>getting attacked by Unopposed Attacks or losing a Clash activates the "Precognition" Skill</u></b></mark></color>
   PL: podczas Starcia <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [LookingFuture] przy każdym Starciu</u></b></mark></color>\nmoże zyskać do ([FutureEyeOn] na Początku tury / 3) [LookingFuture] na turę\ndopóki ta jednostka ma [FutureEyeOn], <color=#ff6000><mark=#ff000040><b><u>otrzymanie nieprzeciwstawianego ataku albo przegrana w Starciu uruchamia Umiejętność „Precognition”</u></b></mark></color>
739. [[a1c9p3] Pasywka wroga [131402] — tekst klimatyczny] “맞대고 부딪힐수록 이 검은 가열되고, 내가 본 미래에 도달할 때까지 가속할 거다.”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131402].flavor
   limit: do 140 znaków
   EN: "The more we clash, the hotter my sword will become... and accelerate to bring us to the future I foresaw."
   PL: "Im więcej starć, tym bardziej rozgrzewa się ten miecz... i przyspiesza, by zawieść nas w przyszłość, którą ujrzałem."
740. [[a1c9p3] Pasywka wroga [131408] — nazwa] 과부하
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131408].name
   limit: do 40 znaków
   EN: Overloaded
   PL: Overloaded
741. [[a1c9p3] Pasywka wroga [131408] — opis] 다음 조건에 따라 [FutureEyeOn] 감소\n- [LookingFuture]를 얻지 못하면, 매 합마다 [FutureEyeOn] 1 감소\n- 일방 공격을 당할 시 [FutureEyeOn] 1 감소\n- 합 패배 시 [FutureEyeOn] 3 감소
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131408].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [FutureEyeOn], [LookingFuture]
   znaczenie tagów: [FutureEyeOn] = 예지안 / Eye of Precognition; [LookingFuture] = 가속하는 미래 / Accelerating Future
   EN: The following causes this unit to lose [FutureEyeOn] Stack:\n- If this unit fails to gain [LookingFuture], lose 1 [FutureEyeOn] with every Clash\n- When this unit is attacked by an Unopposed Attack, lose 1 [FutureEyeOn]\n- On Clash Lose, lose 3 [FutureEyeOn]
   PL: następujące okoliczności powodują utratę Licznika [FutureEyeOn]:\n- jeżeli jednostka nie zyska [LookingFuture], traci 1 [FutureEyeOn] przy każdym Starciu\n- przy otrzymaniu nieprzeciwstawianego ataku traci 1 [FutureEyeOn]\npo przegranej w Starciu traci 3 [FutureEyeOn]
742. [[a1c9p3] Pasywka wroga [131408] — tekst klimatyczny] ‘눈이 지끈거리며 뜨거워지고, 시야가 붉어진다’
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131408].flavor
   limit: do 120 znaków
   EN: 'The eye's heating up, its socket is starting to ache, and my vision is turning red.'
   PL: 'Oko się nagrzewa, oczodół zaczyna boleć, a pole widzenia robi się czerwone.'
743. [[a1c9p3] Pasywka wroga [131405] — nazwa] 팔레르모 스파다
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131405].name
   limit: do 40 znaków
   EN: La Spada di Palermo
   PL: La Spada di Palermo
744. [[a1c9p3] Pasywka wroga [131405] — opis] 메인 타겟의 화상 1당, 보호막에 입히는 피해량 15% 증가 (최대 300%)\n스킬 사용 시 대상의 공격 스킬이 참격 혹은 관통 속성이면, 합 위력 +1\n자신의 스킬 효과로 [VibrationExplosion]이 발동되었다면, 다음 턴 [AttackDmgUp] 2 얻음 (턴당 3회)\n자신의 스킬 효과로 크리티컬이 발동되었다면, 정신력 5 회복
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131405].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [AttackDmgUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Deal +15% more damage against Shields for every Burn on the main target (max 300%)\nOn Skill Use, if target's Attack Skill is either a Slash or a Pierce Skill, Clash Power +1\nIf this unit's Skill effects triggered [VibrationExplosion], gain 2 [AttackDmgUp] next turn (3 times per turn)\nIf this unit hit Critically with its Skill effects, heal 5 SP
   PL: zadaje o 15% więcej obrażeń Tarczom za każdy punkt Podpalenia głównego celu (maks. 300%)\nprzy użyciu Umiejętności, jeżeli Umiejętność ataku celu jest Umiejętnością Cięcia albo Przebicia, Moc Starcia +1\njeżeli efekty Umiejętności tej jednostki uruchomiły [VibrationExplosion], zyskuje 2 [AttackDmgUp] w następnej turze (3 razy na turę)\njeżeli efekty Umiejętności tej jednostki zadały trafienie krytyczne, przywraca 5 SP
745. [[a1c9p3] Pasywka wroga [131404] — nazwa] 보냐텔리 가문의 수치
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131404].name
   limit: do 50 znaków
   EN: The Shame of Famiglia Bognatelli
   PL: The Shame of Famiglia Bognatelli
746. [[a1c9p3] Pasywka wroga [131404] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%\n[AccelBullet]이 1 이상이면, [AccelBullet]을 소모하는 스킬의 피해량 +30%, 보호막에 입히는 피해량 +150%\n[AccelBullet] 소모한 수치 1당, [Breath] 4 얻음\n[AccelBullet]을 소모하는 코인을 굴릴 때, 가속탄이 없는 경우에도 공격을 취소하지 않음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131404].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [AccelBullet], [Breath]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [AccelBullet] = 가속탄 / Acceleration Round; [Breath] = 호흡 / Poise
   EN: Take -30% HP, SP damage from [Combustion], [Laceration], [Burst], [Sinking]; -30% to Stagger Threshold raised by [Vibration]\nAt 1+ [AccelBullet], Skills that spend [AccelBullet] deal +30% damage and deal +150% damage against Shields\nGain 4 [Breath] for every [AccelBullet] spent\nWhen flipping a Coin that spends [AccelBullet], does not cancel the attack even if this unit does not have Acceleration Round
   PL: otrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Laceration], [Burst] i [Sinking]; otrzymuje o 30% mniej wzrostu Próg Oszołomienia od [Vibration]\nprzy 1+ [AccelBullet], Umiejętności zużywające [AccelBullet] zadają +30% obrażeń i zadają +150% obrażeń Tarczom\nzyskuje 4 [Breath] za każdy zużyty [AccelBullet]\nprzy rzucie Monety zużywającej [AccelBullet] nie przerywa ataku, nawet jeżeli jednostka nie ma Acceleration Round
747. [[a1c9p3] Pasywka wroga [131404] — tekst klimatyczny] “팔레르모를 전수 받고, 가보까지 계승 받았음에도 이런 추태를 보이다니.”\n“네가 물려 받은 유물과 검은, 네 불명예스러운 잔향이 배어 있으니 회수하지 않겠다.”\n“언더보스로 승격한지 사흘 만에 파면 당한 건 발렌치나, 네가 유일할 테지.”\n“너는 가문의 수치다. 보냐텔리는 너에게서 사랑을 거두겠다.”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131404].flavor
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "You were an inheritor of the Palermitan style and a wielder of our family heirloom—you had every privilege one could ever hope for. How dare you embarrass yourself like this?"\n"We'll let you keep the Relic and the sword, for they have been defiled by your dishonorable stench."\n"To be promoted to the station of a Sottocapo, an Underboss... only to be ousted in a mere 3 days. No one else has suffered such pathetic humiliation apart from you, Valencina."\n"You are the shame of our family. La Famiglia Bognatelli withdraws its love from you."
   PL: "Byłeś dziedzicem stylu Palermo i posiadaczem pamiątki rodzinnego domu — miałeś wszystko, o czym można marzyć. Jak śmiesz tak sprofanować się?"\n"Pozwolimy ci zatrzymać Relikwię i miecz, bo nasiąkły twoją plugawą wonią hańby."\n"Awansować na Sottocapo, podbossa... i oblać się po zaledwie 3 dniach. Nikt oprócz ciebie, Valencina, nie poniósł tak żałosnej hańby."\n"Jesteś hańbą naszej rodziny. La Famiglia Bognatelli odbiera tobie swoją miłość."
748. [[a1c9p3] Pasywka wroga [131409] — nazwa] 신(心) - 발렌치나
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131409].name
   limit: do 40 znaków
   EN: Shin (心) - Valencina
   PL: Shin (心) - Valencina
749. [[a1c9p3] Pasywka wroga [131409] — opis] 피격 시 혹은 ‘엄지 제자 - 루치오’가 전투 불능이 되면, 다음 턴에 [ObsessionAndGreed] 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131409].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [ObsessionAndGreed]
   znaczenie tagów: [ObsessionAndGreed] = 신(心) - 발렌치나 / Shin (心) - Valencina
   EN: When hit, or when "The Thumb Apprentice - Lucio" is defeated, gain [ObsessionAndGreed] next turn
   PL: przy otrzymaniu trafienia albo gdy „The Thumb Apprentice - Lucio” zostaje pokonany, zyskuje [ObsessionAndGreed] w następnej turze
750. [[a1c9p3] Pasywka wroga [131409] — tekst klimatyczny] “후… 결국 그 광신도 놈이 짜 놓은 작전대로 들어가서 깽판을 치면 된다는 건데… 이런다고 진짜 티켓이 돌아오는 거 맞아?”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131409].flavor
   limit: do 230 znaków
   EN: "*sigh* Okay. So, you're saying we can get Ticket back by going in and wrecking the place according to that fanatic's plan... Is this really going to bring Ticket back to us?"
   PL: "*wzdycha* Dobrze. Czyli mówisz, że możemy odzyskać Ticket, wchodząc i robiąc dewastację według planu tego fanatyka... Czy to naprawdę przywróci nam Ticket?"
751. [[a1c9p3] Pasywka wroga [131406] — nazwa] 루치오. 이 쓸모없는 것
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131406].name
   limit: do 50 znaków
   EN: Lucio, you useless little shit!
   PL: Lucio, you useless little shit!
752. [[a1c9p3] Pasywka wroga [131406] — opis] ‘엄지 제자 - 루치오’가 전투 불능이 되면, 패시브 ‘사냥 시간’이 발동
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131406].desc
   limit: do 120 znaków
   EN: When "The Thumb Apprentice - Lucio" is defeated, activate "Time to Hunt" Passive
   PL: gdy „The Thumb Apprentice - Lucio” zostaje pokonany, uruchamia się Pasyw „Time to Hunt”
753. [[a1c9p3] Pasywka wroga [131410] — nazwa] 사냥 시간
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131410].name
   limit: do 40 znaków
   EN: Time to Hunt
   PL: Time to Hunt
754. [[a1c9p3] Pasywka wroga [131410] — opis] 턴 시작 시 흐트러짐 상태면 흐트러짐을 해제\n\n무작위 수감자 1명을 지정하여, [TeachersPrey]을 부여\n- 이후 4턴마다 1번씩 발동\n- 스킬 ‘처분’으로 대상을 처치할 시 다음 턴에 다시 발동
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131410].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [TeachersPrey]
   znaczenie tagów: [TeachersPrey] = 사냥 표적 / Game Target
   EN: Turn Start: If this unit is Staggered, recover from Stagger\n\nSelect a random Sinner and inflict [TeachersPrey]\n- Activates every 4 turns after the initial activation\n- If this unit kills the target with the Skill "Disposal," activate it again next turn
   PL: na Początku tury, jeżeli jest w Oszołamieniu, dochodzi do siebie z Oszołamienia\n\nwskazuje losowego Grzesznika i nakłada [TeachersPrey]\n- uruchamia się co 4 tury po pierwszym uruchomieniu\n- jeżeli zabije cel Umiejętnością „Disposal”, uruchamia się ponownie w następnej turze
755. [[a1c9p3] Pasywka wroga [131410] — tekst klimatyczny] 팔레르모는 보냐텔리 가문의 성향을 그대로 빼닮은 검술이다.\n하나의 사냥감을 집요하게 노려, 사냥하고 해체한다. 은밀함은 배제한다. 명예롭고 당당하게, 모두의 시선 앞에서 상대를 죽인다.\n그 화려한 검술은 수많은 영예를 낳았고, 보냐텔리 가문을 뒷골목의 7대 명문가로 만들었다.\n팔레르모를 완전히 터득한 발렌치나는 연기전쟁에서 수많은 장교와 베테랑 병사들의 목을 떨구며 연기전쟁의 영웅 중 한 명이 되었다.\n하지만 누가 예상이나 했을까. 그 명성이 그녀의 발목을 잡을 줄이야.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=131410].flavor
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Palermitan Style has much in common with the originator of the sword technique—La Famiglia Bognatelli.\nBoth the Famiglia and the sword style are renowned for relentlessly focusing on a single prey during a hunt, which is concluded with a Coup de Grâce that may as well be called a dissection. These executions are not carried out in the shadows, but instead, proudly put on display for all to behold.\nThe spectacular and formidable sword style has granted the Famiglia much honor and prestige, eventually securing them a place among the Sette Famiglie of the Backstreets.\nValencina, a master of the Palermitan Style, used it to hunt and execute many officers and so-called battle-hardened soldiers during the Smoke War, becoming a veritable "War Hero."\nIronically, no one could have imagined her fall would sink as low as her fame once soared.
   PL: Styl Palermo ma wiele wspólnego z jego źródłem — La Famiglia Bognatelli.\nZarówno Famiglia, jak i ten styl szermierki słyną z bezlitosnego skupienia na pojedynczej zdobyczy podczas polowania, które kończy Coup de Grâce — można by rzec: sekcja. Te egzekucje nie odbywają się w cieniu, lecz dumnie, na oczach wszystkich.\nTa wspaniała i potężna sztuka miecza przyniosła Famiglii wiele honorów, zapewniając jej miejsce wśród Sette Famiglie Zaułków.\nValencina, mistrzyni Stylu Palermo, używała go, by polować i tracić wielu oficerów i tzw. zahartowanych w boju żołnierzy podczas Wojny Dymów, stając się prawdziwą „Bohaterką Wojny”.\nIroncznie — nikt nie przypuszczał, że jej upadek będzie tak głęboki, jak wysoko wzniósła się jej sława.
756. [[a1c9p3] Pasywka wroga [134501] — nazwa] 제 모든 신체 요소는 이미 티비아에
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134501].name
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [[a1c9p3] Pasywka wroga [134501] — opis] [Combustion], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%\n[Laceration]로 받는 피해량 -50%\n\n턴 시작 시, 흐트러짐 상태면 흐트러짐 해제. 이후 [CrimsonTakeDamageUp] 2 얻음 (전투당 1회)\n\n턴 종료 시 자신의 [Combustion] 4당, 다음 턴에 [DefenseDown] 1 얻음 (최대 15)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134501].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [Burst], [Sinking], [Laceration], [CrimsonTakeDamageUp], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Take -30% HP, SP damage from [Combustion], [Burst], and [Sinking]; -30% to Stagger Threshold raised by [Vibration]\nTake -50% damage from [Laceration]\n\nTurn Start: If this unit is Staggered, recover from Stagger. Afterward, gain 2 [CrimsonTakeDamageUp] (once per Encounter)\n\nTurn End: Gain 1 [DefenseDown] next turn for every 4 [Combustion] on self (max 15)
   PL: otrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Burst] i [Sinking]; otrzymuje o 30% mniej wzrostu Próg Oszołomienia od [Vibration]\notrzymuje o 50% mniej obrażeń od [Laceration]\n\nna Początku tury, jeżeli jest w Oszołamieniu, dochodzi do siebie z Oszołamienia. następnie zyskuje 2 [CrimsonTakeDamageUp] (1 raz na walkę)\n\nna koniec tury zyskuje 1 [DefenseDown] w następnej turze za każde 4 [Combustion] jednostki (maks. 15)
758. [[a1c9p3] Pasywka wroga [134501] — tekst klimatyczny] 거미집의 존재 이유이자, 손가락이 그토록 기다려 온 걸작이 곧 완성될 것 같군요.\n황금가지는 흥미로운 물건이지만, 사실 작품을 완성하는 데 필요한 재료는 아니었답니다.\n림버스 컴퍼니라는 회사를 적으로 돌리면서까지 가져온 이유는 여전히 모르겠지만… \n결과가 확실하니 이 난잡한 과정도 납득할 수 밖에 없네요.\n이 모든 상황은 뤼엔… 아니, 그자가 신봉하는 신이 원한 것.\n신이라 불리는 존재의 사랑을 한몸에 받는다면, 그것은 과연 축복일까요, 아니면 저주일까요. 후훗.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134501].flavor
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Soon, the masterpiece shall be completed—the raison d'être of the House of Spiders.\nThe Golden Boughs are... interesting objet, to be sure, but the fact remains that they are not essential to the perfection of the masterpiece.\nI doubt if it was truly necessary to seize them and risk making an enemy out of Limbus Company... although I do admit these sloppy dance steps did, in the end, come together to form a rather acceptable finale.\nIn any case, this series of circumstances we find ourselves in was Rien's desire—or more precisely, the pleasure of the so-called god he puts his faith in.\nOne must wonder, however... Is it a blessing or a curse to be so compellingly <i>loved</i> by such a thing referred to as "god"? Fuhuhu...
   PL: Wkrótce arcydzieło zostanie ukończone — raison d'être Domu Pająków.\nZłote Gałęzie to... ciekawe obiekty, nie zaprzeczam, lecz fakt pozostaje faktem: nie są one niezbędne do doskonałości arcydzieła.\nWątpię, czy naprawdę trzeba było je przejąć, ryzykując, że Limbus Company stanie się naszym wrogiem... choć przyznaję, że te chaotyczne kroki taneczne ułożyły się w końcu w całkiem znośne zakończenie.\nTak czy inaczej, ta seria okoliczności, w której się znaleźliśmy, była pragnieniem Riena — a ściślej, przyjemnością tzw. boga, w którego on wierzy.\nTrzeba się jednak zastanowić... Czy to błogosławieństwo, czy przekleństwo — być tak namownie kochanym przez coś, co zwie się „bogiem”? Fuhuhu...
759. [[a1c9p3] Pasywka wroga [134502] — nazwa] 신체파
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134502].name
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [[a1c9p3] Pasywka wroga [134502] — opis] 공격 스킬 적중 시 부정적인 효과를 부여하고 동시에 긍정적인 효과를 얻으면, 공격 종료 시 정신력 4 회복\n- 이 효과로 정신력 회복 시 자신의 정신력이 최대면 다음 턴에 [ResultEnhancement] 1 얻음 (턴당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134502].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [ResultEnhancement]
   znaczenie tagów: [ResultEnhancement] = 위력 증가 / Power Up
   EN: On Hit with Attack Skills: If this unit inflicts negative effect and gains positive effect simultaneously, heal 4 SP at Attack End\n- If this unit is at max SP when healing SP with the above effect, gain 1 [ResultEnhancement] next turn (once per turn)
   PL: przy trafieniu Umiejętnościami ataku, jeżeli jednostka nakłada negatywny efekt i jednocześnie zyskuje pozytywny efekt, na koniec Ataku przywraca 4 SP\n- jeżeli przy przywracaniu SP tym efektem jednostka ma Maks. SP, zyskuje 1 [ResultEnhancement] w następnej turze (1 raz na turę)
761. [[a1c9p3] Pasywka wroga [134506] — nazwa] 제자의 전시를 잠시 감상해 볼까요
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134506].name
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [[a1c9p3] Pasywka wroga [134506] — opis] 자신에게 [SupportProtect]가 있으면, <color=#ff6000><mark=#ff000040><b><u>합 시작 시 [SupportProtect] 1 감소</u></b></mark></color> (스킬당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134506].desc
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [[a1c9p3] Pasywka wroga [134509] — nazwa] 좋은 소재는 좋은 육체로부터
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134509].name
   limit: do 60 znaków
   EN: Healthy Corpus Leads to Healthy Ingredient
   PL: Healthy Corpus Leads to Healthy Ingredient
764. [[a1c9p3] Pasywka wroga [134509] — opis] 이 캐릭터는 레벨이 가장 높은 수감자 및 조력자에게 가하는 피해량이 150% 증가하고 우선 공격함
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134509].desc
   limit: do 150 znaków
   EN: This unit deals +150% damage to the Sinner and Assist Unit with the highest level and prioritizes attacking them
   PL: ta jednostka zadaje +150% obrażeń Grzesznikowi i jednostce wsparcia o najwyższym poziomie i priorytet: atakowanie ich
765. [[a1c9p3] Pasywka wroga [134509] — tekst klimatyczny] “하지만 예술적인 감각이 어느 정도 무르익었다면, 가장 뛰어난 신체를 먼저 노리는 게 좋답니다.”\n“좋은 신체에서 떨어진 살점과 뼛조각을 베이스로, 작품의 스케일을 크게 잡을 수 있거든요.”\n“기대되지 않나요, 알비나?”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134509].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "But once you have reached a certain level of mastery, it is best to aim for the most robust corpus among your ingredients."\n"You see, a healthy corpus may provide ample pieces of muscles and bones to broaden the scope and scale of the artwork."\n"Such exciting prospects, yes, dear Albina?"
   PL: "Ale kiedy twój zmysł artystyczny dojrzeje do pewnego poziomu, najlepiej celować najpierw w najbardziej wytrzymałe ciało spośród materiałów."\n"Zdrowe ciało daje przecież obfite kawałki mięśni i kości, na których można rozciągnąć zakres i skalę dzieła."\n"Podniecające perspektywy, prawda, droga Albina?"
766. [[a1c9p3] Pasywka wroga [134510] — nazwa] 일생의 작품 티비아
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134510].name
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [[a1c9p3] Pasywka wroga [134510] — opis] 턴 종료시 [HumanBoneTheRings]가 206이고 [HumanBloodTheRings]가 5면 각각 수치만큼 감소하고 [MineTheRings] 1 얻음\n\n턴 시작시 [MineTheRings]가 있으면, 이번 턴에 강력한 공격 사용\n\n강력한 공격 사용 전에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음</u></b></mark></color> (스킬당 1회. 턴당 최대 3회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134510].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HumanBoneTheRings], [HumanBloodTheRings], [MineTheRings], [PlusCoinValueDown], [ResultReduction]
   znaczenie tagów: [HumanBoneTheRings] = 생체 재료(뼈) / Corpus Ingredient (Bones); [HumanBloodTheRings] = 생체 재료(피) / Corpus Ingredient (Blood); [MineTheRings] = 작품명: 티비아 / Artwork: Tibia; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down
   EN: Turn End: At 206 [HumanBoneTheRings] and 5 [HumanBloodTheRings], reduce Stack of each effect equal to those numbers and gain 1 [MineTheRings]\n\nTurn Start: If this unit has [MineTheRings], use a powerful attack this turn\n\n<color=#ff6000><mark=#ff000040><b><u>When hit by an Attack Skill before using the powerful attack, gain 1 [PlusCoinValueDown] and 1 [ResultReduction]</u></b></mark></color> (once per Skill; max 3 times per turn)
   PL: na koniec tury przy 206 [HumanBoneTheRings] i 5 [HumanBloodTheRings] zmniejsza Licznik każdego z tych efektów o odpowiednią wartość i zyskuje 1 [MineTheRings]\n\nna Początku tury, jeżeli ta jednostka ma [MineTheRings], używa w tej turze potężnego ataku\n\n<color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku przed użyciem potężnego ataku, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction]</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)
768. [[a1c9p3] Pasywka wroga [134510] — tekst klimatyczny] 자신의 모든 육체를 쏟아붓고 깎아내어 완성한 역작, 티비아
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134510].flavor
   (powtórzenie elementu 667 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [[a1c9p3] Pasywka wroga [134604] — nazwa] 갤러리에서는 갤러리만의 감상 규칙이 있는 법
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134604].name
   (powtórzenie elementu 691 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [[a1c9p3] Pasywka wroga [134604] — opis] 자신에게 [SupportProtect]가 있으면, <color=#ff6000><mark=#ff000040><b><u>합 시작 시 [SupportProtect] 1 감소</u></b></mark></color> (스킬당 1회)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134604].desc
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [[a1c9p3] Pasywka wroga [134605] — nazwa] 재료선정
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134605].name
   limit: do 40 znaków
   EN: Ingredient Selection
   PL: Ingredient Selection
772. [[a1c9p3] Pasywka wroga [134605] — opis] 이 캐릭터는 레벨이 가장 낮은 수감자 및 조력자를 우선 공격함
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134605].desc
   limit: do 120 znaków
   EN: This character prioritizes attacking the Sinner and Assist Unit with the lowest level
   PL: ta jednostka priorytet: atakowanie Grzesznika i jednostki wsparcia o najniższym poziomie
773. [[a1c9p3] Pasywka wroga [134605] — tekst klimatyczny] “제일 약한 사람의 근육과 뼈부터 꺼내야겠어.”\n“보잘것없는 재료일 테지만, 그렇게 하나씩 작품을 만들고 전시하다 보면 더 좋은 재료도 얻을 수 있을 거야.”\n“기대되지 않니, 파시아?”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134605].flavor
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "I'll harvest the muscles and bones of the weakest one first."\n"The ingredients might not cut it, but I'll be able to harvest better ones as I craft and display more artworks."\n"What an exciting prospect, right, dear Fascia?"
   PL: "Zacznę od wyjęcia mięśni i kości najsłabszego."\n"Materiał może być niewielki, ale tworząc i eksponując dzieła jedno po drugim, zdobędę lepsze."\n"Podniecające perspektywy, prawda, droga Fascia?"
774. [[a1c9p3] Pasywka wroga [132218] — nazwa] 132218
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132218].name
   limit: do 40 znaków
   EN: 132218
   PL: 132218
775. [[a1c9p3] Pasywka wroga [132214] — nazwa] 미래 잔상
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132214].name
   limit: do 40 znaków
   EN: Afterimage of the Future
   PL: Afterimage of the Future
776. [[a1c9p3] Pasywka wroga [132214] — opis] 특정 턴마다 '확정된 상대' 스킬 사용\n<color=#ff6000><mark=#ff000040><b><u>공격 대상으로 지정된 대상만 해당 스킬에 합 가능</u></b></mark></color>\n\n자신의 '확정된 상대' 스킬이 합에서 패배하면, 36 ~ 60의 고정 피해 받음\n\n전투 종료시 자신이 이번 턴에 사용한 <color=#ff6000><mark=#ff000040><b><u>모든 '확정된 상대' 스킬이 합에서 패배</u></b></mark></color>했다면, 다음 턴에 [Vulnerable] 1 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132214].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Every few turns, use the "Destinated Opponent" Skill\n<color=#ff6000><mark=#ff000040><b><u>Only the target of this unit's attack can Clash with the said Skill Slot</u></b></mark></color>\n\nIf this unit's "Destinated Opponent" Skill loses a Clash, take 36 ~ 60 fixed damage\n\nCombat End: <color=#ff6000><mark=#ff000040><b><u>If every "Destinated Opponent" Skill this unit used in this turn lost a Clash</u></b></mark></color>, gain 1 [Vulnerable] next turn
   PL: co kilka tur używa Umiejętności „Destinated Opponent”\n<color=#ff6000><mark=#ff000040><b><u>tylko cel wskazany atakiem może stoczyć Starcie z tym slocie Umiejętności</u></b></mark></color>\n\njeżeli Umiejętność „Destinated Opponent” tej jednostki przegra Starcie, otrzymuje 36~60 stałych obrażeń\n\nna koniec walki: <color=#ff6000><mark=#ff000040><b><u>jeżeli wszystkie Umiejętności „Destinated Opponent” użyte przez tę jednostkę w tej turze przegrały Starcie</u></b></mark></color>, zyskuje 1 [Vulnerable] w następnej turze
777. [[a1c9p3] Pasywka wroga [132217] — nazwa] 132217
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132217].name
   limit: do 40 znaków
   EN: 132217
   PL: 132217
778. [[a1c9p3] Pasywka wroga [132219] — nazwa] 천살성상[天殺星傷]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132219].name
   limit: do 50 znaków
   EN: Tiansha Star's Bladewound [天殺星傷]
   PL: Tiansha Star's Bladewound [天殺星傷]
779. [[a1c9p3] Pasywka wroga [132219] — opis] 스테이지 시작시, [LvDownLittleFingerBossTwo], [TimeEntangleUnstable] 4 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132219].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LvDownLittleFingerBossTwo], [TimeEntangleUnstable]
   znaczenie tagów: [LvDownLittleFingerBossTwo] = 천살성상[天殺星傷] / Tiansha Star's Bladewound [天殺星傷]; [TimeEntangleUnstable] = 폭주 - 잔상 얽힘 / Paroxysm - Afterimage Entanglement
   EN: Encounter Start: Gain [LvDownLittleFingerBossTwo] and 4 [TimeEntangleUnstable]
   PL: Początek walki: zyskuje [LvDownLittleFingerBossTwo] i 4 [TimeEntangleUnstable]
780. [[a1c9p3] Pasywka wroga [132222] — nazwa] 새벽에서 황혼까지
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132222].name
   limit: do 40 znaków
   EN: From Dawn till Dusk
   PL: From Dawn till Dusk
781. [[a1c9p3] Pasywka wroga [132222] — opis] 턴 시작시 정신력이 0 이상이면, [SojiAbiAgeFuture] 1 얻음\n0보다 높은 정신력 2당, [SojiAbiAgeFuture] 1 얻음\n\n턴 시작시 정신력이 0 미만이면, [SojiAbiAgePast] 1 얻음\n0보다 낮은 정신력 2당, [SojiAbiAgePast] 1 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132222].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [SojiAbiAgeFuture], [SojiAbiAgePast]
   znaczenie tagów: [SojiAbiAgeFuture] = 순행 - 연민 / Forward Flow - Compassion; [SojiAbiAgePast] = 역행 - 미움 / Backward Flow - Bitterness
   EN: Turn Start: At 0+ SP, gain 1 [SojiAbiAgeFuture]\nGain 1 [SojiAbiAgeFuture] for every 2 SP above 0\n\nTurn Start: At less than 0 SP, gain 1 [SojiAbiAgePast]\nGain 1 [SojiAbiAgePast] for every 2 SP below 0
   PL: na Początku tury, przy SP równym 0 lub więcej, zyskuje 1 [SojiAbiAgeFuture]\nzyskuje 1 [SojiAbiAgeFuture] za każde 2 SP powyżej 0\n\nna Początku tury, przy SP niższym niż 0, zyskuje 1 [SojiAbiAgePast]\nzyskuje 1 [SojiAbiAgePast] za każde 2 SP poniżej 0
782. [[a1c9p3] Pasywka wroga [132222] — tekst klimatyczny] 과거와 현재, 미래가 하나로 겹쳐지며 시간의 구분은 의미를 잃고, 어린 시절이든 세월을 보낸 어느 시점이든, 모든 때는 한곳으로 불려 와진다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132222].flavor
   limit: do 290 znaków
   EN: The past, the present, the future—the myriad moments converge together, rendering the distinction of time meaningless. Youthful and aged selves alike are pulled into the here and now from every point along the continuum of time.
   PL: Przeszłość, teraźniejszość i przyszłość — niezliczone momenty zlewają się w jedno, odbierając podziałowi czasu znaczenie. Młode i stare „ja” w jednakowym stopniu są ściągnięte w tu i teraz z każdego punktu kontinuum czasu.
783. [[a1c9p3] Pasywka wroga [132223] — nazwa] 시공간 잔상 분열
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132223].name
   limit: do 50 znaków
   EN: Spacetime Afterimage Collapse
   PL: Spacetime Afterimage Collapse
784. [[a1c9p3] Pasywka wroga [132223] — opis] 턴 종료시, 이번 턴 시작시와의 정신력 차이 5당 [TimeEntangleUnstable] 1 증가 (턴당 최대 5 증가)\n누적으로 피해 100을 받을 때마다 [TimeEntangleUnstable] 1 감소 (보호막 피해 포함)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132223].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [TimeEntangleUnstable]
   znaczenie tagów: [TimeEntangleUnstable] = 폭주 - 잔상 얽힘 / Paroxysm - Afterimage Entanglement
   EN: Turn End: Gain 1 [TimeEntangleUnstable] for every 5 SP difference between this unit's current SP and SP at Turn Start (max 5 per turn)\n\nFor every 100 damage taken cumulatively, lose 1 [TimeEntangleUnstable] (including Shield damage)
   PL: na koniec tury zyskuje 1 [TimeEntangleUnstable] za każde 5 różnicy między aktualnym SP tej jednostki a SP na Początku tury (maks. 5 na turę)\ntraci 1 [TimeEntangleUnstable] za każde 100 obrażeń otrzymanych łącznie (w tym obrażenia Tarczy)
785. [[a1c9p3] Pasywka wroga [132223] — tekst klimatyczny] ‘나를 감싼 잔상들이 한 꺼풀씩 벗겨질 때마다 상실과 후련함이 동시에 찾아와’
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132223].flavor
   limit: do 190 znaków
   EN: 'The afterimages that have long wrapped me in their folds are stripped away, layer by layer... and I am left standing in both loss and liberation.'
   PL: 'Pozostające, które od dawna owijały mnie w swoje fałdy, są zdejmowane warstwa po warstwie... a ja pozostaję stojąca i w stratzie, i w wyzwoleniu.'
786. [[a1c9p3] Pasywka wroga [133701] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133701].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL: Will of the Prescript
787. [[a1c9p3] Pasywka wroga [133701] — opis] 스테이지 시작 시, 최대 체력의 20%만큼 보호막 얻음 (이번 전투 동안 유지)\n\n턴 시작 시\n- [UnlockBuff_Base] 단계에 따라 [IndexPrescript_Base_2nd] 얻음\n- 무작위 적에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함 (특정 패턴 제외)\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133701].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [IndexPrescript_Base_2nd], [IndexPrescriptTargetToPersonality], [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_Base_2nd] = 지령 / Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Encounter Start: Gain Shield equal to 20% of max HP (remains throughout this Encounter)\n\nTurn Start:\n- Gain [IndexPrescript_Base_2nd] based on [UnlockBuff_Base] stage on self\n- Inflict [IndexPrescriptTargetToPersonality] to a random enemy and prioritize attacking that enemy (excluding certain pattern)\n\nDeal +2.5% damage to [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage to all targets instead
   PL: Początek walki: zyskuje Tarczę równą 20% Maks. HP (utrzymuje się przez tę walkę)\n\nna Początku tury:\n- zyskuje [IndexPrescript_Base_2nd] zależnie od Etapu [UnlockBuff_Base] jednostki\n- nakłada [IndexPrescriptTargetToPersonality] losowemu wrogowi i priorytet: atakowanie tego wroga (poza określonym wzorcem)\n\nzadaje +2.5% obrażeń [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 20%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +30% obrażeń wszystkim celom
788. [[a1c9p3] Pasywka wroga [133702] — nazwa] 지령 수행
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133702].name
   limit: do 40 znaków
   EN: Undertake Prescript
   PL: Undertake Prescript
789. [[a1c9p3] Pasywka wroga [133702] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 15 회복, ([UnlockBuff_Base] 단계+1)만큼 [BlessingOfIndexPrescriptEnemy] 얻음 (턴당 1회)\n\n이번 턴에 [IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [PressureOfPrescript] 1, [KarmaOfIndexStudent] 10 얻음\n- [UnlockBuff_Base] 단계가 2 미만이면, 턴 종료 시 [BlessingOfIndexPrescriptEnemy] 1 얻음\n- [BlessingOfIndexPrescriptEnemy]가 9면, [KarmaOfIndexStudent]를 얻지 않음\n\n- [PressureOfPrescript]을 얻을 때마다 그 수치만큼 [EsteemNeeds]를 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133702].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescript_Base_2nd], [UnlockBuff_Base], [BlessingOfIndexPrescriptEnemy], [PressureOfPrescript], [KarmaOfIndexStudent], [EsteemNeeds]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [UnlockBuff_Base] = 해금 / Unlock; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [PressureOfPrescript] = 압박감 / Onus; [KarmaOfIndexStudent] = 카르마 / Karmic Consequence; [EsteemNeeds] = 인정 욕구 / Desire for Acknowledgement
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 15 SP and gain [BlessingOfIndexPrescriptEnemy] by ([UnlockBuff_Base] stage + 1) (once per turn)\n\nTurn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 1 [PressureOfPrescript] and 10 [KarmaOfIndexStudent]\n- If this unit's [UnlockBuff_Base] stage is below 2, gain 1 [BlessingOfIndexPrescriptEnemy]\n- At 9 [BlessingOfIndexPrescriptEnemy], does not gain [KarmaOfIndexStudent]\n\n- Gain [EsteemNeeds] equal to [PressureOfPrescript] gained every time this unit gains [PressureOfPrescript]
   PL: na koniec tury: jeżeli w tej turze wykonano [IndexPrescript_Base_2nd], przywraca 15 SP i zyskuje (Etap [UnlockBuff_Base] + 1) [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\nna koniec tury: jeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd], zyskuje 1 [PressureOfPrescript] i 10 [KarmaOfIndexStudent]\n- jeżeli Etap [UnlockBuff_Base] tej jednostki jest niższy niż 2, na koniec tury zyskuje 1 [BlessingOfIndexPrescriptEnemy]\n- przy 9 [BlessingOfIndexPrescriptEnemy] nie zyskuje [KarmaOfIndexStudent]\n\n- zyskuje [EsteemNeeds] równe zyskanym [PressureOfPrescript], za każdym razem, gdy ta jednostka zyskuje [PressureOfPrescript]
790. [[a1c9p3] Pasywka wroga [133703] — nazwa] 해금
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133703].name
   limit: do 40 znaków
   EN: Unlock
   PL: Unlock
791. [[a1c9p3] Pasywka wroga [133703] — opis] 턴 종료 시 [BlessingOfIndexPrescriptEnemy]가 6/9거나 체력이 80%/60% 이하면,\n- [UnlockBuff_2]/[UnlockBuff_3] 얻음\n- 정신력이 45로 증가\n- 보유한 [PressureOfPrescript] 전부 소모, 흐트러짐 해제\n\n체력 조건으로 [UnlockBuff_Base] 획득 시\n- (증가한 정신력/15)만큼 [KarmaOfIndexStudent] 얻음\n- [BlessingOfIndexPrescriptEnemy]가 6/9 미만이면, 6/9로 변경\n증가한 수치 1당 다음 턴 시작 시 [DefenseDown] 1, [KarmaOfIndexStudent] 2 얻음\n\n강력한 공격을 사용하는 턴의 속도 최솟값, 최댓값 +10
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133703].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [UnlockBuff_2], [UnlockBuff_3], [PressureOfPrescript], [UnlockBuff_Base], [KarmaOfIndexStudent], [DefenseDown]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_2] = 해금 - II / Unlock - II; [UnlockBuff_3] = 해금 - III / Unlock - III; [PressureOfPrescript] = 압박감 / Onus; [UnlockBuff_Base] = 해금 / Unlock; [KarmaOfIndexStudent] = 카르마 / Karmic Consequence; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn End: At 6/9 [BlessingOfIndexPrescriptEnemy] or at 80%-/60%- HP,\n- Gain [UnlockBuff_2]/[UnlockBuff_3]\n- Heal to 45 SP\n- Consume all [PressureOfPrescript] and recover from Stagger\n\nIf [UnlockBuff_Base] was gained based on HP conditional above,\n- Gain [KarmaOfIndexStudent] by (sum of healed SP / 15)\n- Increase [BlessingOfIndexPrescriptEnemy] to 6/9 if this unit had less than 6/9 [BlessingOfIndexPrescriptEnemy]; gain 1 [DefenseDown] and 2 [KarmaOfIndexStudent] next turn for every [BlessingOfIndexPrescriptEnemy] gained\n\nMin & Max Speed +10 in the turn this unit uses its powerful attack
   PL: na koniec tury, przy 6/9 [BlessingOfIndexPrescriptEnemy] albo przy HP równym 80%/60% lub mniej:\n- zyskuje [UnlockBuff_2]/[UnlockBuff_3]\n- przywraca SP do 45\n- zużywa wszystkie [PressureOfPrescript] i dochodzi do siebie z Oszołamienia\n\njeżeli [UnlockBuff_Base] zostało uzyskane dzięki warunkowi HP opisanemu powyżej:\n- zyskuje (przywrócone SP / 15) [KarmaOfIndexStudent]\n- jeżeli jednostka miała mniej niż 6/9 [BlessingOfIndexPrescriptEnemy], zwiększa [BlessingOfIndexPrescriptEnemy] do 6/9; za każdy zyskany [BlessingOfIndexPrescriptEnemy] zyskuje 1 [DefenseDown] i 2 [KarmaOfIndexStudent] w następnej turze\n\nMin. i Maks. Szybkość +10 w turze użycia potężnego ataku
792. [[a1c9p3] Pasywka wroga [133704] — nazwa] 개화 E.G.O::대행
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133704].name
   limit: do 50 znaków
   EN: Effloresced E.G.O::Procuration
   PL: Effloresced E.G.O::Procuration
793. [[a1c9p3] Pasywka wroga [133704] — opis] 이번 전투 동안 개화[TabExplain] E.G.O::대행 상태로 전투를 진행함\n- 스테이지 시작 시, [UnlockBuff_1], [BlessingOfIndexPrescriptEnemy] 3 얻음\n- 해당 상태 동안 내성 변경, [Blandishment_Enemy] 얻음\n- 정신력이 0 미만으로 내려가지 않음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133704].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [UnlockBuff_1], [BlessingOfIndexPrescriptEnemy], [Blandishment_Enemy]
   znaczenie tagów: [UnlockBuff_1] = 해금 - I / Unlock - I; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [Blandishment_Enemy] = 당연한 믿음 / Faith Beyond Question
   EN: For this Encounter, maintain Effloresced[TabExplain] E.G.O::Procuration state\n- Encounter Start: Gain [UnlockBuff_1] and 3 [BlessingOfIndexPrescriptEnemy]\n- Gain [Blandishment_Enemy] and a different set of Resistance values while in this state\n- SP does not drop below 0
   PL: w tej walce utrzymuje stan Effloresced[TabExplain] E.G.O::Procuration\n- Początek walki: zyskuje [UnlockBuff_1] i 3 [BlessingOfIndexPrescriptEnemy]\n- w tym stanie zyskuje [Blandishment_Enemy] i inny zestaw wartości Odporności\n- SP nie spada poniżej 0
794. [[a1c9p3] Pasywka wroga [133705] — nazwa] 몰입
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133705].name
   limit: do 40 znaków
   EN: Concentration
   PL: Concentration
795. [[a1c9p3] Pasywka wroga [133705] — opis] [UnlockBuff_3]을 얻으면 다음 효과 적용\n- [Blandishment_Shin_Enemy], 최대 체력의 50%만큼 보호막 얻음 (이번 전투 동안 유지)\n- [PressureOfPrescript]이 [PressureOfPrescript_2nd]으로 변경되고, 최대로 증가\n- 턴 시작 시 [PressureOfPrescript_2nd] 1 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133705].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_3], [Blandishment_Shin_Enemy], [PressureOfPrescript], [PressureOfPrescript_2nd]
   znaczenie tagów: [UnlockBuff_3] = 해금 - III / Unlock - III; [Blandishment_Shin_Enemy] = 신(心) - 소라 / Shin (心) - Sora; [PressureOfPrescript] = 압박감 / Onus; [PressureOfPrescript_2nd] = 극심한 압박감 / Extreme Onus
   EN: At [UnlockBuff_3], apply the following effects:\n- [Blandishment_Shin_Enemy], gain Shield equal to 50% of max HP (lasts for the rest of this Encounter)\n- Intensify [PressureOfPrescript] to [PressureOfPrescript_2nd] and max out its Stack\n- Turn Start: Gain 1 [PressureOfPrescript_2nd]
   PL: przy uzyskaniu [UnlockBuff_3] obowiązują następujące efekty:\n- zyskuje [Blandishment_Shin_Enemy] i Tarczę równą 50% Maks. HP (utrzymuje się przez resztę tej walki)\n- [PressureOfPrescript] zmienia się w [PressureOfPrescript_2nd] i osiąga maksimum\n- na Początku tury zyskuje 1 [PressureOfPrescript_2nd]
796. [[a1c9p3] Pasywka wroga [133801] — nazwa] 정검[整劍]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133801].name
   limit: do 40 znaków
   EN: The Orthodox Blade [整劍]
   PL: The Orthodox Blade [整劍]
797. [[a1c9p3] Pasywka wroga [133801] — opis] 스테이지 시작시 [DicipleLittleFinger] 50을 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DicipleLittleFinger]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: Encounter Start: gain 50 [DicipleLittleFinger]
   PL: Początek walki: zyskuje 50 [DicipleLittleFinger]
798. [[a1c9p3] Pasywka wroga [133802] — nazwa] 별의 이름을 받기 위한 수행
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133802].name
   limit: do 60 znaków
   EN: Training to Inherit the Name of a Star
   PL: Training to Inherit the Name of a Star
799. [[a1c9p3] Pasywka wroga [133802] — opis] 공격 스킬 종료시, 각 대상에게 (크리티컬로 적중한 참격 코인 개수 x 10)만큼 참격 피해 (해당 피해로는 흐트러지지 않음)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133802].desc
   limit: do 180 znaków
   EN: Attack Skill End: Deal (# of Slash Coins that hit Critically x 10) Slash damage against each target (cannot be Staggered due to this damage)
   PL: koniec Umiejętności ataku: zadaje każdemu celowi obrażenia Cięcia równe (liczba Monet Cięcia trafiających krytycznie x 10) (te obrażenia nie powodują Oszołamienia)
800. [[a1c9p3] Pasywka wroga [133803] — nazwa] 정신일도
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133803].name
   limit: do 40 znaków
   EN: Singular Focus of the Mind
   PL: Singular Focus of the Mind
801. [[a1c9p3] Pasywka wroga [133803] — opis] [Breath] 위력이 최대 25로 제한됨\n25를 초과하여 얻는 [Breath] 위력은 [DicipleLittleFinger]로 전환됨\n\n[DicipleLittleFinger]가 감소할 때마다 그 수치만큼 [Fugacious]을 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133803].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [DicipleLittleFinger], [Fugacious]
   znaczenie tagów: [Breath] = 호흡 / Poise; [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade; [Fugacious] = 검의 길 / Way of the Blade
   EN: This unit's [Breath] Potency is capped at 25\nAny excess [Breath] Potency gained past 25 will be converted to [DicipleLittleFinger]\n\nGain [Fugacious] equal to [DicipleLittleFinger] lost every time this unit loses [DicipleLittleFinger] Stack
   PL: Siła [Breath] tej jednostki jest ograniczona do 25\nnadmierna Siła [Breath] uzyskana ponad 25 jest przekształcana w [DicipleLittleFinger]\n\nzyskuje tyle [Fugacious], ile utraconych [DicipleLittleFinger], za każdym razem, gdy ta jednostka traci Licznik [DicipleLittleFinger]
802. [[a1c9p3] Pasywka wroga [133804] — nazwa] 정념[靜念]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133804].name
   limit: do 40 znaków
   EN: Tranquility [靜念]
   PL: Tranquility [靜念]
803. [[a1c9p3] Pasywka wroga [133804] — opis] 자신에게 [DicipleLittleFinger]가 있으면 아래 효과 적용\n- 정신력이 0 미만으로 감소하지 않음. 0 미만이었으면 0이 됨\n- 받는 정신력 피해가 우울 피해로 전환됨 (기본 정신력 증감조건 제외)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133804].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [DicipleLittleFinger]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: If this unit has [DicipleLittleFinger], gain the following effects:\n- SP does not drop below 0; if it was below 0, recover to 0\n- Convert any SP damage taken into Gloom damage (save for SP changes due to "Base factors increasing/decreasing Sanity")
   PL: jeżeli ta jednostka ma [DicipleLittleFinger], obowiązują następujące efekty:\n- SP nie spada poniżej 0; jeżeli było niższe niż 0, wraca do 0\n- otrzymywane obrażenia SP są przekształcane w obrażenia Zauły (poza zmianami SP wynikającymi z „bazowych warunków zmiany Poczucia”)
804. [[a1c9p3] Pasywka wroga [133805] — nazwa] 은혜
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133805].name
   limit: do 40 znaków
   EN: Grace
   PL: Grace
805. [[a1c9p3] Pasywka wroga [133805] — opis] 료슈 외 대상과 합을 진행할 때, 합 위력 -2\n료슈 외 대상에게 받는 피해량 -20%
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133805].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a Clash against targets that aren't Ryōshū, Clash Power -2\nTake -20% damage from targets other than Ryōshū
   PL: podczas Starcia z celami innymi niż Ryōshū Moc Starcia -2\notrzymuje o 20% mniej obrażeń od celów innych niż Ryōshū
806. [[a1c9p3] Pasywka wroga [133901] — nazwa] 황제의 백성
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133901].name
   limit: do 40 znaków
   EN: The Emperor's Subjects
   PL: The Emperor's Subjects
807. [[a1c9p3] Pasywka wroga [133901] — opis] 턴 시작 시 [DefenseBug]를 50 얻음 (턴당 얻는 수치 3 감소, 최대 20 감소)\n- 자신에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking]이 있으면,\n<color=#ff6000><mark=#ff000040><b><u>위력을 무작위로 감소시키고, 감소된 수치만큼 [DefenseBug] 감소</u></b></mark></color>\n- 해당 효과의 위력이 1이고 횟수가 2 이상이면, 대신 횟수 감소\n\n전투 중 <color=#ff6000><mark=#ff000040><b><u>[DefenseBug]가 모두 감소되면,</u></b></mark></color> 다음 턴에 아래 효과 적용\n- [DefenseBug] 대신 [DefenseDown] 10 얻음\n- 적에게 가장 부족한 속성의 E.G.O 자원 3종을 2개씩 생성\n- 턴 종료 시 자신의 부정적인 효과 모두 제거. [DefenseBug] 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133901].desc
   limit: do 870 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefenseBug], [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [DefenseDown]
   znaczenie tagów: [DefenseBug] = 방어 해충[바퀴] / Protecting Pest [Roaches]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: Gain 50 [DefenseBug] (Gain 3 fewer [DefenseBug] with every subsequent turn; max reduction 20)\n- If this unit has [Combustion], [Laceration], [Vibration], [Burst], or [Sinking], <color=#ff6000><mark=#ff000040><b><u>reduce their Potency by a random value; then, lose the same Stacks of [DefenseBug] as that random value</u></b></mark></color>\n- If the above effects are at 1 Potency but has 2+ Count, reduce their Count instead\n\n<color=#ff6000><mark=#ff000040><b><u>If all [DefenseBug] was lost</u></b></mark></color> during the combat phase, gain the following effects next turn:\n- Gain 10 [DefenseDown] instead of gaining [DefenseBug]\n- Generate 2 E.G.O resources for each of the 3 least-owned Affinities\n- Turn End: Remove all negative effects from this unit and start gaining [DefenseBug] again
   PL: na Początku tury zyskuje 50 [DefenseBug] (każda kolejna tura daje o 3 mniej [DefenseBug]; maks. zmniejszenie 20)\n- jeżeli ta jednostka ma [Combustion], [Laceration], [Vibration], [Burst] albo [Sinking],\n<color=#ff6000><mark=#ff000040><b><u>zmniejsza ich Siłę o losową wartość; następnie traci tyle Liczników [DefenseBug], ile wynosiła ta losowa wartość</u></b></mark></color>\n- jeżeli powyższe efekty mają Siłę 1, a Licznik 2 lub więcej, zamiast tego zmniejsza ich Licznik\n\n<color=#ff6000><mark=#ff000040><b><u>jeżeli w fazie walki wszystkie [DefenseBug] zostały utracone</u></b></mark></color>, w następnej turze obowiązują następujące efekty:\n- zamiast zyskiwać [DefenseBug], zyskuje 10 [DefenseDown]\n- generuje po 2 zasobów E.G.O dla każdej z 3 Afinności, których jednostka ma najmniej\n- na koniec tury usuwa wszystkie negatywne efekty tej jednostki i od nowa zaczyna zyskiwać [DefenseBug]
808. [[a1c9p3] Pasywka wroga [133901] — tekst klimatyczny] 어느 곳에서나 어느 순간에나, 그들은 면과 면이 만나는 선으로부터 기어 나온다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133901].flavor
   limit: do 120 znaków
   EN: They crawl out unheralded from betwixt all the lines that form where walls meet.
   PL: Pełzną niepostrzeżenie spod wszystkich linii, które powstają tam, gdzie spotykają się ściany.
809. [[a1c9p3] Pasywka wroga [133902] — nazwa] 황제의 망토
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133902].name
   limit: do 40 znaków
   EN: The Emperor's Mantle
   PL: The Emperor's Mantle
810. [[a1c9p3] Pasywka wroga [133902] — opis] 턴 시작 시 ([DefenseBug] x 40)만큼 보호막 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133902].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseBug]
   znaczenie tagów: [DefenseBug] = 방어 해충[바퀴] / Protecting Pest [Roaches]
   EN: Turn Start: Gain ([DefenseBug] x 40) Shield
   PL: na Początku tury zyskuje Tarczę równą ([DefenseBug] x 40)
811. [[a1c9p3] Pasywka wroga [133902] — tekst klimatyczny] 바퀴벌레들의 군집은, 황제 단 하나만을 위해 움직인다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133902].flavor
   limit: do 120 znaków
   EN: The Legion of Roaches moves for no one but its Emperor.
   PL: Legion Karaluchów porusza się tylko dla jednego — swojego Cesarza.
812. [[a1c9p3] Pasywka wroga [133903] — nazwa] 황제의 군세
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133903].name
   limit: do 40 znaków
   EN: The Emperor's Legion
   PL: The Emperor's Legion
813. [[a1c9p3] Pasywka wroga [133903] — opis] - 합 승리 시 대상에게 [OffenseBug] 3 부여\n- 스킬 적중 시 대상에게 [OffenseBug] 1 부여
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133903].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OffenseBug]
   znaczenie tagów: [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: - On Clash Win, inflict 3 [OffenseBug] on target\n- On Hit with a Skill, inflict 1 [OffenseBug] on target
   PL: - po wygranej w Starciu nakłada 3 [OffenseBug] celowi\n- przy trafieniu Umiejętnością nakłada 1 [OffenseBug] celowi
814. [[a1c9p3] Pasywka wroga [133903] — tekst klimatyczny] 파고들고 스며들고 침투하여, 갉아내고 뜯어내고 포식한다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133903].flavor
   limit: do 120 znaków
   EN: Rip, seep, trickle, carve, tear, devour.
   PL: Podgryzać, wsiąkać, przesiąkać, wyżłabiać, drzeć, pożerać.
815. [[a1c9p3] Pasywka wroga [133904] — nazwa] 황제의 피
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133904].name
   limit: do 40 znaków
   EN: The Emperor's Blood
   PL: The Emperor's Blood
816. [[a1c9p3] Pasywka wroga [133904] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -50%\n해당 피해로는 흐트러짐이 발생하지 않음\n본체 잃은 체력 25%당, 턴 시작 시 [ResultReduction] 2 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133904].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [ResultReduction]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [ResultReduction] = 위력 감소 / Power Down
   EN: Take -50% HP, SP damage from [Combustion], [Laceration], [Burst], and [Sinking]; -50% to Stagger Threshold raised by [Vibration]\nCannot be Staggered due to this damage\nTurn Start: Gain 2 [ResultReduction] for every 25% missing HP on the Core
   PL: otrzymuje o 50% mniej obrażeń HP i SP od [Combustion], [Laceration], [Burst] i [Sinking]; otrzymuje o 50% mniej wzrostu Próg Oszołomienia od [Vibration]\nte obrażenia nie powodują Oszołamienia\nna Początku tury zyskuje 2 [ResultReduction] za każde 25% brakującego HP Korpusu
817. [[a1c9p3] Pasywka wroga [133904] — tekst klimatyczny] ‘모든 것에 적응하고 무뎌진다’
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133904].flavor
   limit: do 120 znaków
   EN: 'Become dulled and inured to all things.'
   PL: 'Tępieje i przyzwyczaja się do wszystkiego.'
818. [[a1c9p3] Pasywka wroga [133905] — nazwa] 뜯겨진 포장지
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133905].name
   limit: do 40 znaków
   EN: The Unwrapped Present
   PL: The Unwrapped Present
819. [[a1c9p3] Pasywka wroga [133905] — opis] 정신력과 무관하게 코인 확률이 50%로 고정\n\n<color=#ff6000><mark=#ff000040><b><u>수감자와의 합에서 승리 시,</u></b></mark></color> 정신력 5 감소, 수감자에게 가하는 피해량 -40%\n\n<color=#ff6000><mark=#ff000040><b><u>사기저하 또는 패닉 상태가 되면,</u></b></mark></color> [ParryingResultDown], [ResultReduction] 얻음\n패닉 상태 해제 시 [ResultReduction] 2 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133905].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ParryingResultDown], [ResultReduction]
   znaczenie tagów: [ParryingResultDown] = 합 위력 감소 / Clash Power Down; [ResultReduction] = 위력 감소 / Power Down
   EN: This unit's SP value cannot affect the outcome of Coin flips, which is fixed to 50-50\n\n<color=#ff6000><mark=#ff000040><b><u>On Clash Win against Sinners,</u></b></mark></color> lose 5 SP and deal -40% damage against them\n\n<color=#ff6000><mark=#ff000040><b><u>When in Low Morale or Panic states</u></b></mark></color>, gain [ParryingResultDown] and [ResultReduction]\nWhen recovering from Panic, gain 2 [ResultReduction]
   PL: wartość SP tej jednostki nie wpływa na wynik rzutów Monet, które są z góry ustalone na 50-50\n\n<color=#ff6000><mark=#ff000040><b><u>po wygranej w Starciu z Grzesznikami</u></b></mark></color> traci 5 SP i zadaje o 40% mniej obrażeń Grzesznikom\n\n<color=#ff6000><mark=#ff000040><b><u>gdy jest w stanie Niskiego Morale albo Paniki</u></b></mark></color>, zyskuje [ParryingResultDown] i [ResultReduction]\ngdy wychodzi z Paniki, zyskuje 2 [ResultReduction]
820. [[a1c9p3] Pasywka wroga [133905] — tekst klimatyczny] ‘하지만 이게 정말 다 뜯어진 걸까?’
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133905].flavor
   limit: do 120 znaków
   EN: 'Are there really no more wrappings underneath?'
   PL: 'Czy naprawdę nic już nie zostało pod spodem?'
821. [[a1c9p3] Pasywka wroga [133906] — nazwa] 황제의 진노
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133906].name
   limit: do 40 znaków
   EN: The Emperor's Wrath
   PL: The Emperor's Wrath
822. [[a1c9p3] Pasywka wroga [133906] — opis] 체력이 50%가 되거나 흐트러짐 상태가 되면, 자신에게 걸린 부정적인 효과와 흐트러짐 상태를 해제하고 패턴이 변경됨\n이후 다음 효과 적용\n- 정신력이 0이 됨\n- [DefenseBug] 50 얻음\n- 패시브‘황제의 군세’를 통한 [OffenseBug] 부여량이 2배로 증가함
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=133906].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseBug], [OffenseBug]
   znaczenie tagów: [DefenseBug] = 방어 해충[바퀴] / Protecting Pest [Roaches]; [OffenseBug] = 공격 해충[바퀴] / Hurting Pest [Roaches]
   EN: At 50% HP, or when Staggered, recover from Stagger and remove all negative effects on this unit and gain a new pattern\nThen, gain the following effects:\n- Reset SP to 0\n- Gain 50 [DefenseBug]\n- Double the amount of [OffenseBug] inflicted by the Passive "The Emperor's Legion"
   PL: przy 50% HP albo przy przejściu w Oszołamienie dochodzi do siebie z Oszołamienia, usuwa wszystkie negatywne efekty i przybiera nowy wzorzec\nnastępnie obowiązują następujące efekty:\n- SP wraca do 0\n- zyskuje 50 [DefenseBug]\n- ilość nakładanych przez Pasyw „The Emperor's Legion” [OffenseBug] rośnie dwukrotnie
823. [[a1c9p3] Pasywka wroga [134701] — nazwa] 검지 아비 뤼엔
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134701].name
   limit: do 40 znaków
   EN: Rien, The Index Nursefather
   PL: Rien, The Index Nursefather
824. [[a1c9p3] Pasywka wroga [134701] — opis] <color=#ff6000><mark=#ff000040><b><u>일방 공격으로 받는 피해량 -50%</u></b></mark></color>\n[Vibration], [Burst], [Sinking]으로 받는 피해량 -50%\n[UnlockBuff_Base]으로 정신력 회복 시 정신력이 0 미만이면, 정신력을 0까지 회복\n\n스테이지 시작 시, [BurningWoundRien_Mask] 얻음\n\n체력이 55% 이하면, 페이즈 변경\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- [StackRienSpecialSkill] 0으로 초기화
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134701].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Vibration], [Burst], [Sinking], [UnlockBuff_Base], [BurningWoundRien_Mask], [StackRienSpecialSkill]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [UnlockBuff_Base] = 해금 / Unlock; [BurningWoundRien_Mask] = 뤼엔의 가면 / Rien's Mask; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: <color=#ff6000><mark=#ff000040><b><u>Take -50% damage from Unopposed Attacks</u></b></mark></color>\nTake -50% damage from [Vibration], [Burst], and [Sinking]\nWhen healing SP from [UnlockBuff_Base], if this unit's SP is below 0, heal up to 0 SP\n\nEncounter Start: Gain [BurningWoundRien_Mask]\n\nAt 55% HP, gain a new pattern\n- Remove all effects other than those exclusive to this unit\n- Reset [StackRienSpecialSkill] Stack to 0
   PL: <color=#ff6000><mark=#ff000040><b><u>otrzymuje o 50% mniej obrażeń od Ataków Jednostronnych</u></b></mark></color>\notrzymuje o 50% mniej obrażeń od [Vibration], [Burst] i [Sinking]\ngdy przywraca SP dzięki [UnlockBuff_Base], jeżeli SP jednostki jest niższe niż 0, przywraca SP do 0\n\nPoczątek walki: zyskuje [BurningWoundRien_Mask]\n\nprzy 55% HP przybiera nowy wzorzec\n- usuwa wszystkie efekty inne niż własne tej jednostki\n- zeruje Licznik [StackRienSpecialSkill] do 0
825. [[a1c9p3] Pasywka wroga [134701] — tekst klimatyczny] 지령이 말한 대로 그때를 기다렸다고.\n딸이 나가도 기다리고 기다렸지.\n\n그러다 림버스 컴퍼니에서 연락이 왔고 뒷문이 열려있더구나.\n그리고 단말기가 울려서 딸을 데리러 가야 할 때가 되었다는 것을 알았지.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134701].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I waited for "the moment" as the Prescript told me to.\nEven after my darling daughter left, I waited.\n\nAnd after a while, I was contacted by Limbus Company, and saw that the Backdoor was open.\nThat's when the device beeped and let me know that it was finally time to bring my daughter home.
   PL: Czekałem na „ten moment”, jak nakazywał Prescript.\nCzekałem i czekałem, nawet gdy moja córeczka wyszła.\n\nPóźniej odezwało się Limbus Company, a tylne wejście było otwarte.\nI wtedy urządzenie zameldowało, że nadszedł czas, by zabrać córkę do domu.
826. [[a1c9p3] Pasywka wroga [134702] — nazwa] 신탁 단말기 [카두세우스]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134702].name
   limit: do 40 znaków
   EN: Oracle Device [Caduceus]
   PL: Oracle Device [Caduceus]
827. [[a1c9p3] Pasywka wroga [134702] — opis] <color=#ff6000><mark=#ff000040><b><u>코인마다 무기가 무작위로 정해지며 특수 효과 적용</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\n공격 스킬 사용 시, [StackRienSpecialSkill] 1 얻음 (최대 9)\n- 스킬별 1회 획득 가능 (동일한 스킬로 2를 초과하여 얻을 수 없음)\n\n<color=#ff6000><mark=#ff000040><b><u>턴 시작 시 [StackRienSpecialSkill]가 9면, 강력한 스킬 사용</u></b></mark></color>\n- 첫 사용 후 공격 종료 시, [Shin_Rien] 얻음\n- 스킬 종류별 [StackRienSpecialSkill] 획득 여부 초기화\n- 속도 최솟값, 최댓값 +25\n- 턴 종료 시 다음 턴에, [Vulnerable] 1, [ResultReduction] 2 얻음\n\n다섯 번째 턴 시작 시, [StackRienSpecialSkill]가 9 미만이면, 9까지 증가하고 (증가한 수치 x 5)만큼 [KarmaOfIndexRien] 얻음\n- 이후 네 턴마다 이 효과 발동
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134702].desc
   limit: do 1140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RienWeapon01Hatchet], [RienWeapon02Stiletto], [RienWeapon03Greatsword], [RienWeapon04Rapier], [RienWeapon05Sledgehammer], [RienWeapon06Ultragreatsword], [RienWeapon07Lance], [RienWeapon08Chain], [RienWeapon09Scythe], [StackRienSpecialSkill], [Shin_Rien], [Vulnerable], [ResultReduction], [KarmaOfIndexRien]
   znaczenie tagów: [RienWeapon01Hatchet] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [RienWeapon02Stiletto] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [RienWeapon03Greatsword] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [RienWeapon04Rapier] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [RienWeapon05Sledgehammer] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [RienWeapon06Ultragreatsword] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a greatsword...; [RienWeapon07Lance] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [RienWeapon08Chain] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: <color=#ff6000><mark=#ff000040><b><u>A random weapon is assigned to every Coin. Each weapon has a unique effect.</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\nWhen using an Attack Skill, gain 1 [StackRienSpecialSkill] (max 9)\n- Can be gained once per Skill; does not gain Stack from the same Skill twice\n\n<color=#ff6000><mark=#ff000040><b><u>Turn Start: At 9 [StackRienSpecialSkill] Stacks, use a powerful Skill</u></b></mark></color>\n- Attack End: After using the powerful Skill for the first time, gain [Shin_Rien]\n- Reset the per-Skill [StackRienSpecialSkill] cap\n- Min & Max Speed +25\n- Turn End: Gain 1 [Vulnerable] and 2 [ResultReduction] next turn\n\nTurn 5 Start: At less than 9 [StackRienSpecialSkill], bring its Stack to 9; then, gain (Stack gained x 5) [KarmaOfIndexRien]\n- Then, activate this effect every 4 turns
   PL: <color=#ff6000><mark=#ff000040><b><u>każdej Monecie przypisywana jest losowa broń, z unikalnym efektem</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\nprzy użyciu Umiejętności ataku zyskuje 1 [StackRienSpecialSkill] (maks. 9)\n- można zyskać 1 raz na Umiejętność (nie można zyskać 2 razy tą samą Umiejętnością)\n\n<color=#ff6000><mark=#ff000040><b><u>na Początku tury przy 9 Licznikach [StackRienSpecialSkill] używa potężnej Umiejętności</u></b></mark></color>\n- na koniec Ataku, po pierwszym użyciu potężnej Umiejętności, zyskuje [Shin_Rien]\n- zeruje limit zyskiwania [StackRienSpecialSkill] per Umiejętność\n- Min. i Maks. Szybkość +25\n- na koniec tury zyskuje 1 [Vulnerable] i 2 [ResultReduction] w następnej turze\n\nna Początku 5. tury, jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, podnosi go do 9 i zyskuje (zyskane Liczniki x 5) [KarmaOfIndexRien]\n- potem uruchamia ten efekt co 4 tury
828. [[a1c9p3] Pasywka wroga [134702] — tekst klimatyczny] 단말기 안에는 특이점과 유사한 기술을 이용해 형태와 질량을 변동시킬 수 있는, 금속 같은 액체가 들어 있다.\n이 액체는 단말기가 수령한 지령에 따라 모습을 바꾸며, 살해 대상의 정보와 주어진 제한 시간에 맞춰 무기로 변환된다.\n어느 날에는 지나치게 작은 단검이 배정되어 다른 무기로 바뀌기를 기다렸지만, 살해 제한 시간이 다가올 때까지 쓸만한 무기가 나오지 않았다. 결국, 마지막까지 기다려 나온 것이 포크였기에, 그 포크로 대상을 죽여야만 했다.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134702].flavor
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A vial of what looks like liquid metal capable of changing its shape and mass, its qualities almost like those of Singularities, swishes inside the Device.\nThe form the fluid takes is contingent on the Prescript the Device receives. The weapons it produces depend on the information regarding the target and the time limit given to carry out the assassination.\nOne day, as he received a dagger too small for the task, he elected to wait until it produced a different weapon. However, despite the approaching deadline, it refused to provide him a proper weapon; he had no choice but to kill his target with a fork.
   PL: Wewnątrz urządzenia chlupocze ciecz jak płynny metal, zdolna zmieniać kształt i masę, niemal jak Singularności.\nForma, jaką przyjmuje ciecz, zależy od Prescriptu, który urządzenie otrzyma. Broń, którą produkuje, zależy od informacji o celu i limitu czasu na zabójstwo.\nPewnego dnia, gdy dostał sztylet zbyt mały do tego zadania, postanowił poczekać, aż urządzenie wyprodukuje inną broń. Mimo zbliżającego się terminu ta jednak nie dała mu porządnej broni — musiał więc zabić cel widelcem.
829. [[a1c9p3] Pasywka wroga [134703] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134703].name
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [[a1c9p3] Pasywka wroga [134703] — opis] 턴 시작 시,\n- [UnlockBuff_Base] 단계에 따라 [IndexPrescript_Base_2nd] 얻음\n- 료슈를 제외한 무작위 수감자에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함\n<color=#ff6000><mark=#ff000040><b><u>- [IndexPrescriptTargetToPersonality]에게 사용하는 스킬의 코인이 전부 [SuperCoin]으로 변경됨</u></b></mark></color>\n· [IndexPrescriptTargetToPersonality]이 사망하거나 대상을 공격하지 못하게 될 경우,\n<color=#ff6000><mark=#ff000040><b><u>사용하지 않은 나머지 스킬을 료슈 제외 무작위 수감자 한 명에게 사용\n(현재 체력이 가장 낮은 대상 우선)</u></b></mark></color>\n· 다른 모든 수감자 사망 시, 료슈에게 부여\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134703].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [UnlockBuff_Base], [IndexPrescript_Base_2nd], [IndexPrescriptTargetToPersonality], [SuperCoin], [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_Base_2nd] = 지령 / Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Turn Start:\n- Gain [IndexPrescript_Base_2nd] based on [UnlockBuff_Base] stage on self\n- Apply [IndexPrescriptTargetToPersonality] against a random non-Ryōshū Sinner, and prioritize attacking them\n<color=#ff6000><mark=#ff000040><b><u>- When using a Skill against [IndexPrescriptTargetToPersonality], convert all Coins on that Skill to [SuperCoin]s</u></b></mark></color>\n· If [IndexPrescriptTargetToPersonality] is killed, or if this unit can no longer attack that target, <color=#ff6000><mark=#ff000040><b><u>use the remaining Skills against a random non-Ryōshū Sinner (prioritizes targets with the least current HP)</u></b></mark></color>\n· When all other Sinners are killed, apply it to Ryōshū\n\nDeal +2.5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage against all targets
   PL: na Początku tury:\n- zyskuje [IndexPrescript_Base_2nd] zależnie od Etapu [UnlockBuff_Base] jednostki\n- nakłada [IndexPrescriptTargetToPersonality] losowemu Grzesznikowi (innemu niż Ryōshū) i priorytet: atakowanie go\n<color=#ff6000><mark=#ff000040><b><u>- przy użyciu Umiejętności na [IndexPrescriptTargetToPersonality] wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y</u></b></mark></color>\n· jeżeli [IndexPrescriptTargetToPersonality] zginie albo jednostka nie może już zaatakować tego celu, <color=#ff6000><mark=#ff000040><b><u>używa pozostałych Umiejętności na losowym Grzeszniku (innym niż Ryōshū) (priorytet: cele z najmniejszym aktualnym HP)</u></b></mark></color>\n· gdy wszyscy pozostali Grzesznicy zginą, nakłada go Ryōshū\n\nzadaje +2.5% obrażeń [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 20%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +30% obrażeń wszystkim celom
831. [[a1c9p3] Pasywka wroga [134703] — tekst klimatyczny] 제가 가족을 꾸리길 원하십니까. \n\n“당신 같은 남편을 어쩜 이렇게 운명적으로 만날 수 있었을까요.”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134703].flavor
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you wish me to raise a family?\n\n"It must've been fate that brought us together. To think that I'd ever meet a husband like you..."
   PL: Czy pragniesz, bym założył rodzinę?\n\n"To musiał być los, który nas połączył. Kto by pomyślał, że poznam męża takiego jak ty..."
832. [[a1c9p3] Pasywka wroga [134704] — nazwa] 지령 수행
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134704].name
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [[a1c9p3] Pasywka wroga [134704] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 10 회복, [BlessingOfIndexPrescriptEnemy] 3 얻음 (턴당 1회)\n\n이번 턴에<color=#ff6000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexRien] 8 얻고,\n[IndexPrescriptTargetToPersonality]이었던 수감자가 다음 턴에 [ParryingResultUp] 1 얻음</u></b></mark></color>\n- [UnlockBuff_Base]이 없으면, 턴 종료 시 [BlessingOfIndexPrescriptEnemy] 1 얻음\n- [BlessingOfIndexPrescriptEnemy]가 9면, [KarmaOfIndexRien]를 얻지 않음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134704].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptEnemy], [KarmaOfIndexRien], [IndexPrescriptTargetToPersonality], [ParryingResultUp], [UnlockBuff_Base]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexRien] = 카르마 / Karmic Consequence; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [UnlockBuff_Base] = 해금 / Unlock
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 10 SP and gain 3 [BlessingOfIndexPrescriptEnemy] (once per turn)\n\n<color=#ff6000><mark=#ff000040><b><u>Turn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 8 [KarmaOfIndexRien], and the Sinner who had [IndexPrescriptTargetToPersonality] gains 1 [ParryingResultUp] next turn</u></b></mark></color>\n- If this unit does not have [UnlockBuff_Base], gain 1 [BlessingOfIndexPrescriptEnemy] at Turn End\n- At 9 [BlessingOfIndexPrescriptEnemy], does not gain [KarmaOfIndexRien]
   PL: na koniec tury: jeżeli w tej turze wykonano [IndexPrescript_Base_2nd], przywraca 10 SP i zyskuje 3 [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\n<color=#ff6000><mark=#ff000040><b><u>na koniec tury: jeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd], zyskuje 8 [KarmaOfIndexRien], a Grzesznik, który miał [IndexPrescriptTargetToPersonality], zyskuje 1 [ParryingResultUp] w następnej turze</u></b></mark></color>\n- jeżeli jednostka nie ma [UnlockBuff_Base], na koniec tury zyskuje 1 [BlessingOfIndexPrescriptEnemy]\n- przy 9 [BlessingOfIndexPrescriptEnemy] nie zyskuje [KarmaOfIndexRien]
834. [[a1c9p3] Pasywka wroga [134704] — tekst klimatyczny] 제가 가족을 잃기를 원하십니까.\n\n“여보. 잠시 북부에 좀 다녀올게.”\n“아, 오후에 택배가 오기로 했으니 대신 받아줄 수 있겠니, 딸?”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134704].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you wish me to lose my family?\n\n"Honey, I gotta take a quick trip up north today."\n"Ah, also—hey, buddy. I'm expecting a package this afternoon, so would you be a dear and pick it up for me, sweetheart?"
   PL: Czy pragniesz, bym stracił rodzinę?\n\n"Kochanie, wybieram się dziś na chwilę na północ."\n"A, tak — hej, kolego. Oczekuję dziś po południu przesyłki, więc byłbyś wspaniały i odebrałbyś ją za mnie, kochanie?"
835. [[a1c9p3] Pasywka wroga [134705] — nazwa] 해금
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134705].name
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [[a1c9p3] Pasywka wroga [134705] — opis] 턴 종료 시 [BlessingOfIndexPrescriptEnemy]가 3/6/9거나 체력이 95%/85%/75% 이하면,\n- [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3] 얻음\n\n첫 번째 턴 종료 시 [UnlockBuff_Base] 단계가 1 미만이면, [UnlockBuff_Rien1] 얻음\n네 번째 턴 종료 시 [UnlockBuff_Base] 단계가 2 미만이면, [UnlockBuff_Rien2] 얻음\n\n체력 또는 턴 조건으로 [UnlockBuff_Base] 시,\n- [BlessingOfIndexPrescriptEnemy]가 3/6/9 미만이면, 3/6/9로 변경,\n증가한 수치 1당 다음 턴 시작 시 [KarmaOfIndexRien] 10 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134705].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [UnlockBuff_Rien1], [UnlockBuff_Rien2], [UnlockBuff_Rien3], [UnlockBuff_Base], [KarmaOfIndexRien]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_Rien1] = 해금 - I / Unlock - I; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [UnlockBuff_Base] = 해금 / Unlock; [KarmaOfIndexRien] = 카르마 / Karmic Consequence
   EN: Turn End: At 3/6/9 [BlessingOfIndexPrescriptEnemy] or at 95%-/85%-/75%- HP,- Gain [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3]\n\nTurn 1 End: At lower than [UnlockBuff_Base] stage 1, gain [UnlockBuff_Rien1]\nTurn 4 End: At lower than [UnlockBuff_Base] stage 2, gain [UnlockBuff_Rien2]\n\nWhen [UnlockBuff_Base] is activated due to HP or Turn conditionals:\n- At less than 3/6/9 [BlessingOfIndexPrescriptEnemy] Stack, raise them to 3/6/9\nGain 10 [KarmaOfIndexRien] at the next Turn Start for every Stack gained
   PL: na koniec tury, przy 3/6/9 [BlessingOfIndexPrescriptEnemy] albo przy HP równym 95%/85%/75% lub mniej:\n- zyskuje [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3]\n\nna koniec 1. tury, jeżeli Etap [UnlockBuff_Base] jest niższy niż 1, zyskuje [UnlockBuff_Rien1]\nna koniec 4. tury, jeżeli Etap [UnlockBuff_Base] jest niższy niż 2, zyskuje [UnlockBuff_Rien2]\n\ngdy [UnlockBuff_Base] zostaje uzyskane dzięki warunkowi HP lub tury:\n- jeżeli jednostka ma mniej niż 3/6/9 Liczników [BlessingOfIndexPrescriptEnemy], podnosi je do 3/6/9\nzyskuje 10 [KarmaOfIndexRien] na następnym Początku tury za każdy zyskany Licznik
837. [[a1c9p3] Pasywka wroga [134705] — tekst klimatyczny] “지령을 따라가다 보면 닫힌 것들이 풀리기 마련.”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134705].flavor
   limit: do 120 znaków
   EN: "Following the Prescripts is to unlock what is locked."
   PL: "Idąc za Prescriptem, otwiera się to, co zamknięte."
838. [[a1c9p3] Pasywka wroga [134801] — nazwa] 아비 뤼엔 [모조품]
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134801].name
   limit: do 40 znaków
   EN: Rien, the Father [Imitation]
   PL: Rien, the Father [Imitation]
839. [[a1c9p3] Pasywka wroga [134801] — opis] <color=#ff6000><mark=#ff000040><b><u>일방 공격으로 받는 피해량 -75%</u></b></mark></color>\n[Vibration], [Burst], [Sinking]으로 받는 피해량 -75%\n[UnlockBuff_Base]으로 정신력 회복 시 정신력이 15 미만이면, 정신력을 15까지 회복\n\n체력이 55% 이하가 되어 페이즈 변경 시, 다음 효과 적용\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- [StackRienSpecialSkill] 0으로 초기화\n- [IndexPrescript_RienSecondPhase] 얻음\n- [BurningWoundRien_Mask]이 [BurningWoundRien]로 변경\n- [KarmaOfIndexRien]가 [KarmaOfIndexRien_2Phase]로 변경되고 10 얻음\n- [Shin_Rien]이 없으면 즉시 얻음\n\n체력이 25% 이하면 패턴이 변경되어 특정 스킬이 더욱 강력해짐
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134801].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Vibration], [Burst], [Sinking], [UnlockBuff_Base], [StackRienSpecialSkill], [IndexPrescript_RienSecondPhase], [BurningWoundRien_Mask], [BurningWoundRien], [KarmaOfIndexRien], [KarmaOfIndexRien_2Phase], [Shin_Rien]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [UnlockBuff_Base] = 해금 / Unlock; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]; [IndexPrescript_RienSecondPhase] = 지령[단말기] - 경고 / Prescript: [Device] - Warning; [BurningWoundRien_Mask] = 뤼엔의 가면 / Rien's Mask; [BurningWoundRien] = 이글거리는 상처 / Sizzling Wound …
   EN: <color=#ff6000><mark=#ff000040><b><u>Take -75% damage from Unopposed Attacks</u></b></mark></color>\nTake -75% damage from [Vibration], [Burst], and [Sinking]\nWhen healing SP from [UnlockBuff_Base], if this unit's SP is below 15, heal up to 15 SP\n\nWhen this unit enters a new phase at 55% HP, gain the following effects:\n- Remove all effects other than those exclusive to this unit\n- Reset [StackRienSpecialSkill] Stack to 0\n- Gain [IndexPrescript_RienSecondPhase]\n- Convert [BurningWoundRien_Mask] to [BurningWoundRien]\n- Convert [KarmaOfIndexRien] to [KarmaOfIndexRien_2Phase]; then gain 10 Stacks of that effect\n- If this unit does not have [Shin_Rien], immediately gain that effect\n\nAt 25% or lower HP, gain a new pattern and greatly enhance a certain Skill
   PL: <color=#ff6000><mark=#ff000040><b><u>otrzymuje o 75% mniej obrażeń od Ataków Jednostronnych</u></b></mark></color>\notrzymuje o 75% mniej obrażeń od [Vibration], [Burst] i [Sinking]\ngdy przywraca SP dzięki [UnlockBuff_Base], jeżeli SP jednostki jest niższe niż 15, przywraca SP do 15\n\ngdy ta jednostka wchodzi w nową fazę przy 55% HP, zyskuje następujące efekty:\n- usuwa wszystkie efekty inne niż własne tej jednostki\n- zeruje Licznik [StackRienSpecialSkill] do 0\n- zyskuje [IndexPrescript_RienSecondPhase]\n- [BurningWoundRien_Mask] zmienia się w [BurningWoundRien]\n- [KarmaOfIndexRien] zmienia się w [KarmaOfIndexRien_2Phase]; następnie zyskuje 10 Liczników tego efektu\n- jeżeli jednostka nie ma [Shin_Rien], natychmiast go zyskuje\n\nprzy HP równym 25% lub mniej przybiera nowy wzorzec i znacznie wzmacnia określoną Umiejętność
840. [[a1c9p3] Pasywka wroga [134801] — tekst klimatyczny] 누군가를 따라해야 하는 것만 같았고 그게 누군지 몰라 지령을 의심하고 거스를 뻔했지만, 뒤늦게 자신이 누구를 닮게 되었는지 깨닫고, 지령의 뜻을 받아들여 완성된 거짓 아비.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134801].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Once, he harbored a suspicion that he was being shaped into an imitation of someone; he doubted the Will and nearly defied it, for he did not know whom he was to mimic. Only when it was too late did he understand its intent and come to accept the Prescript's will.\nOnly then was the false father completed.
   PL: Kiedyś trawiło go podejrzenie, że jest formowany na kogoś naśladowcę; wątpił w Wolę i prawie jej się sprzeciwił, bo nie wiedział, kogo ma naśladować. Dopiero, gdy było już za późno, zrozumiał jej zamiar i przyjął wolę Prescriptu.\nDopiero wtedy ukończono fałszywego ojca.
841. [[a1c9p3] Pasywka wroga [134802] — nazwa] 신탁 단말기 [카두세우스] - 완전 해금
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134802].name
   limit: do 60 znaków
   EN: Oracle Device [Caduceus] - Full Unlock
   PL: Oracle Device [Caduceus] - Full Unlock
842. [[a1c9p3] Pasywka wroga [134802] — opis] <color=#ff6000><mark=#ff000040><b><u>코인마다 무기가 무작위로 정해지며 특수 효과 적용</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\n공격 스킬 사용 시, [StackRienSpecialSkill] 1 얻음 (최대 9)\n- 스킬별 1회 획득 가능 (동일한 스킬로 2 이상 획득 불가)\n- 특수 패턴에서만 사용하는 스킬로는 얻지 않음\n\n턴 시작 시 [StackRienSpecialSkill]가 9면, 강력한 스킬 사용\n- 스킬 종류별 [StackRienSpecialSkill] 획득 여부 초기화\n- 속도 최솟값, 최댓값 +25\n- 턴 종료 시 다음 턴에, [Vulnerable] 2, [ResultReduction] 3 얻음\n\n페이즈가 변경된 턴부터 효과 발동\n- 네 턴마다 [StackRienSpecialSkill]가 9 미만이면,\n9까지 증가하고 (증가한 수치 x 5)만큼 [KarmaOfIndexRien_2Phase] 얻음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134802].desc
   limit: do 1240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RienWeapon01Hatchet2phase], [RienWeapon02Stiletto2phase], [RienWeapon03Greatsword2phase], [RienWeapon04Rapier2phase], [RienWeapon05Sledgehammer2phase], [RienWeapon06Ultragreatsword2phase], [RienWeapon07Lance2phase], [RienWeapon08Chain2phase], [RienWeapon09Scythe2phase], [StackRienSpecialSkill], [Vulnerable], [ResultReduction], [KarmaOfIndexRien_2Phase]
   znaczenie tagów: [RienWeapon01Hatchet2phase] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [RienWeapon02Stiletto2phase] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [RienWeapon03Greatsword2phase] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [RienWeapon04Rapier2phase] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [RienWeapon05Sledgehammer2phase] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [RienWeapon06Ultragreatsword2phase] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a great sword...; [RienWeapon07Lance2phase] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [RienWeapon08Chain2phase] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: <color=#ff6000><mark=#ff000040><b><u>A random weapon is assigned to every Coin. Each weapon has a unique effect.</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\nWhen using an Attack Skill, gain 1 [StackRienSpecialSkill] (max 9)\n- Can be gained once per Skill; does not gain Stack from the same Skill twice\n- Does not gain Stack from a Skill used only in a special pattern\n\nTurn Start: At 9 [StackRienSpecialSkill] Stacks, use a powerful Skill\n- Reset the per-Skill [StackRienSpecialSkill] cap\n- Min & Max Speed +25\n- Turn End: Gain 2 [Vulnerable] and 3 [ResultReduction] next turn\n\nActivate the following, starting from the turn in which the phase changed\n- Every 4 turns, at less than 9 [StackRienSpecialSkill], bring its Stack to 9; then, gain (Stack gained x 5) [KarmaOfIndexRien_2Phase]
   PL: <color=#ff6000><mark=#ff000040><b><u>każdej Monecie przypisywana jest losowa broń, z unikalnym efektem</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\nprzy użyciu Umiejętności ataku zyskuje 1 [StackRienSpecialSkill] (maks. 9)\n- można zyskać 1 raz na Umiejętność (nie można zyskać 2 razy tą samą Umiejętnością)\n- nie zyskuje za Umiejętności używane wyłącznie w specjalnym wzorcu\n\nna Początku tury przy 9 Licznikach [StackRienSpecialSkill] używa potężnej Umiejętności\n- zeruje limit zyskiwania [StackRienSpecialSkill] per Umiejętność\n- Min. i Maks. Szybkość +25\n- na koniec tury zyskuje 2 [Vulnerable] i 3 [ResultReduction] w następnej turze\n\nuruchamia następujący efekt od tury, w której zmieniła się faza\n- co 4 tury, jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, podnosi go do 9 i zyskuje (zyskane Liczniki x 5) [KarmaOfIndexRien_2Phase]
843. [[a1c9p3] Pasywka wroga [134802] — tekst klimatyczny] 전파를 통해 지령을 보내는 도시의 신, 헤르메스가 선사한 최고의 무기이자 저주.
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134802].flavor
   limit: do 160 znaków
   EN: An unparalleled weapon and a curse bestowed by Hermes, a god of the City whose Prescripts are distributed by radio waves.
   PL: Najlepsza broń i przekleństwo podarowane przez Hermesa, boga Miasta, którego Prescripty rozsyłane są falami radiowymi.
844. [[a1c9p3] Pasywka wroga [134803] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134803].name
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [[a1c9p3] Pasywka wroga [134803] — opis] 턴 시작 시,\n- 료슈를 제외한 무작위 수감자에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함\n<color=#ff6000><mark=#ff000040><b><u>- [IndexPrescriptTargetToPersonality]에게 사용하는 스킬의 코인이 전부 [SuperCoin]으로 변경됨</u></b></mark></color>\n· [IndexPrescriptTargetToPersonality]이 사망하거나 대상을 공격하지 못하게 될 경우,<color=#ff6000><mark=#ff000040><b><u>사용하지 않은 나머지 스킬을 료슈 제외 무작위 수감자 한 명에게 사용 (현재 체력이 가장 낮은 대상 우선, 체력 1인 경우 제외)</u></b></mark></color>\n· 다른 모든 수감자 사망 시, 료슈에게 부여\n- [BlessingOfIndexPrescriptEnemy]만큼 [Protection] 얻음 (최대 9)\n<color=#ff6000><mark=#ff000040><b><u>· [KarmaOfIndexRien_2Phase] 20당, 1 감소</u></b></mark></color>\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +5% (최대 40%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +50%\n\n페이즈가 변경된 턴부터 효과 발동\n- 두 턴마다 [BlackNightmare] 얻음.\n- [BlackNightmare]을 얻을 때 [StackRienSpecialSkill]가 9 미만이면, 특수 패턴 발동
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134803].desc
   limit: do 1360 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescriptTargetToPersonality], [SuperCoin], [BlessingOfIndexPrescriptEnemy], [Protection], [KarmaOfIndexRien_2Phase], [BlackNightmare], [StackRienSpecialSkill]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [Protection] = 보호 / Protection; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: Turn Start:\n- Apply [IndexPrescriptTargetToPersonality] against a random non-Ryōshū Sinner, and prioritize attacking them\n<color=#ff6000><mark=#ff000040><b><u>- When using a Skill against [IndexPrescriptTargetToPersonality], convert all Coins on that Skill to [SuperCoin]s</u></b></mark></color>\n· If [IndexPrescriptTargetToPersonality] is killed, or if this unit can no longer attack that target, <color=#ff6000><mark=#ff000040><b><u>use the remaining Skills against a random non-Ryōshū Sinner (prioritizes targets with the least current HP, unless they have 1 HP)</u></b></mark></color>\n· When all other Sinners are killed, apply it to Ryōshū\n- Gain [Protection] equal to [BlessingOfIndexPrescriptEnemy] (max 9)\n<color=#ff6000><mark=#ff000040><b><u>· Lose 1 Stack for every 20 [KarmaOfIndexRien_2Phase]</u></b></mark></color>\n\nDeal +5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 40%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +50% damage against all targets\n\nStarting from the first turn after the phase change, activate the following effects:\n- Gain [BlackNightmare] every 2 turns.\n- When gaining [BlackNightmare], if this unit has fewer than 9 [StackRienSpecialSkill] Stack, activate a unique pattern
   PL: na Początku tury:\n- nakłada [IndexPrescriptTargetToPersonality] losowemu Grzesznikowi (innemu niż Ryōshū) i priorytet: atakowanie go\n<color=#ff6000><mark=#ff000040><b><u>- przy użyciu Umiejętności na [IndexPrescriptTargetToPersonality] wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y</u></b></mark></color>\n· jeżeli [IndexPrescriptTargetToPersonality] zginie albo jednostka nie może już zaatakować tego celu, <color=#ff6000><mark=#ff000040><b><u>używa pozostałych Umiejętności na losowym Grzeszniku (innym niż Ryōshū) (priorytet: cele z najmniejszym aktualnym HP, z wyjątkiem celów z 1 HP)</u></b></mark></color>\n· gdy wszyscy pozostali Grzesznicy zginą, nakłada go Ryōshū\n- zyskuje [Protection] równy [BlessingOfIndexPrescriptEnemy] (maks. 9)\n<color=#ff6000><mark=#ff000040><b><u>· traci 1 Licznika za każde 20 [KarmaOfIndexRien_2Phase]</u></b></mark></color>\n\nzadaje +5% obrażeń [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 40%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +50% obrażeń wszystkim celom\n\nuruchamia następujące efekty od pierwszej tury po zmianie fazy:\n- zyskuje [BlackNightmare] co 2 tury.\n- przy zyskiwaniu [BlackNightmare], jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, uruchamia specjalny wzorzec
846. [[a1c9p3] Pasywka wroga [134803] — tekst klimatyczny] 가족을 꾸렸습니다.\n\n“당신은 지금 이곳에 있으면 안될 텐데.”\n“아직 작업이 한창이다. 무엇보다 섬세하고 아름답게 장식하고 있거든.”\n“…네놈, 설마 지령을 거스를 셈인가.”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134803].flavor
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I raised a family.\n\n"You're not supposed to be here right now."\n"My work is still much underway, and I'd like to carve them up in peace so they can attain the most exquisite beauty I can sculpt."\n"... Don't tell me, are you here to defy the Prescript?"
   PL: Założyłem rodzinę.\n\n"Nie powinnaś tu teraz być."\n"Moja praca wciąż trwa, a chciałbym w spokoju rzeźbić je, by osiągnęły najdoskonalszą piękność, jaką potrafię wyrzeźbić."\n"... Nie mów, że przyszedłeś sprzeciwiać się Prescriptowi."
847. [[a1c9p3] Pasywka wroga [134804] — nazwa] 지령 수행
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134804].name
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [[a1c9p3] Pasywka wroga [134804] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 15 회복, [BlessingOfIndexPrescriptEnemy] 1 얻음 (턴당 1회)\n\n이번 턴에 <color=#ff6000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexRien_2Phase] 10 얻고 [BlessingOfIndexPrescriptEnemy] 1 잃음,\n[IndexPrescriptTargetToPersonality]이었던 수감자가 다음 턴에 [ParryingResultUp] 2 얻음</u></b></mark></color>\n- 강력한 스킬을 사용한 턴일 경우, 대신 [KarmaOfIndexRien_2Phase] 15 얻고 [BlessingOfIndexPrescriptEnemy] 3 잃음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134804].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptEnemy], [KarmaOfIndexRien_2Phase], [IndexPrescriptTargetToPersonality], [ParryingResultUp]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 15 SP and gain 1 [BlessingOfIndexPrescriptEnemy] (once per turn)\n\n<color=#ff6000><mark=#ff000040><b><u>Turn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 10 [KarmaOfIndexRien_2Phase], lose 1 [BlessingOfIndexPrescriptEnemy], and the Sinner who had [IndexPrescriptTargetToPersonality] gains 2 [ParryingResultUp] next turn</u></b></mark></color>\n- If this unit used a powerful Skill this turn, gain 15 [KarmaOfIndexRien_2Phase] and lose 3 [BlessingOfIndexPrescriptEnemy] instead
   PL: na koniec tury: jeżeli w tej turze wykonano [IndexPrescript_Base_2nd], przywraca 15 SP i zyskuje 1 [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\n<color=#ff6000><mark=#ff000040><b><u>na koniec tury: jeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd], zyskuje 10 [KarmaOfIndexRien_2Phase], traci 1 [BlessingOfIndexPrescriptEnemy], a Grzesznik, który miał [IndexPrescriptTargetToPersonality], zyskuje 2 [ParryingResultUp] w następnej turze</u></b></mark></color>\n- jeżeli w tej turze użyto potężnej Umiejętności, zamiast tego zyskuje 15 [KarmaOfIndexRien_2Phase] i traci 3 [BlessingOfIndexPrescriptEnemy]
849. [[a1c9p3] Pasywka wroga [134804] — tekst klimatyczny] 가족을… 잃었습니다.\n \n“가지마…”\n“이대로 가지마… 아빠…  우리… 살려줘…”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=134804].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I... lost my family.\n\n"Don't go..."\n"Don't go... Not... like this... Daddy... Please... help us..."
   PL: Straciłem... rodzinę.\n \n"Nie odchodź..."\n"Nie odchodź... Nie... tak... Tato... Proszę... ratuj nas..."
850. [[a1c9p3] Pasywka wroga [132224] — nazwa] 마지막 전투
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132224].name
   limit: do 40 znaków
   EN: The Final Battle
   PL: The Final Battle
851. [[a1c9p3] Pasywka wroga [132224] — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고 아래 효과를 적용 (전투 당 1회)\n- 체력을 최대로 회복하고, 자신의 해제 가능한 모든 부정적인 효과를 해제\n- 이번 전투 동안 [Vulnerable] 1을 얻고, [TimeEntangleUnstable]이 1로 고정됨.\n- 매 턴 종료시 (현재 턴 수 x 10)만큼 고정 피해 받음\n- 이후 턴을 종료하고, 패턴이 강화됨
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132224].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [TimeEntangleUnstable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [TimeEntangleUnstable] = 폭주 - 잔상 얽힘 / Paroxysm - Afterimage Entanglement
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage and apply the following effects (once per Encounter):\n- Heal max HP and remove all removable negative effects from this unit\n- For this Encounter, gain 1 [Vulnerable] and fix [TimeEntangleUnstable] to 1. Take (# of current turn x 10) fixed damage at the end of every turn\n- Afterward, end turn and the attack pattern becomes empowered
   PL: w tej walce, gdy ta jednostka otrzyma obrażenia sprowadzające jej HP do 0, niweluje te obrażenia i nakłada następujące efekty (1 raz na walkę):\n- przywraca Maks. HP i usuwa wszystkie usuwalne negatywne efekty tej jednostki\n- w tej walce zyskuje 1 [Vulnerable], a Licznik [TimeEntangleUnstable] zostaje ustalony na 1. otrzymuje (aktualna liczba tur x 10) stałych obrażeń na koniec każdej tury\n- następnie kończy turę, a wzorzec ataku zostaje wzmocniony
852. [[a1c9p3] Pasywka wroga [132224] — tekst klimatyczny] “당신은 잊었고, 나는 모든 걸 기억하게 됐어.”
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=132224].flavor
   limit: do 120 znaków
   EN: "You have been made to forget all, and I to remember all."
   PL: "Ciebie zmuszono do zapomnienia wszystkiego, a mnie — do zapamiętania wszystkiego."
853. [[a1c9p3] Pasywka wroga [137801] — nazwa] 관찰
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137801].name
   limit: do 40 znaków
   EN: Observation
   PL: Observation
854. [[a1c9p3] Pasywka wroga [137801] — opis] 스테이지 시작 시, 모든 적에게 [ObservedPerson] 1을 부여하고\n[ObservedPerson]가 적용된 인원 수만큼 [Breath] 위력을 얻고 [Breath] 횟수 증가\n\n턴 시작 시, [ObservedPerson]를 보유하지 않은 대상에게 [ObservedPerson] 1 부여\n\n대상의 [ObservedPerson] 10당 스킬로 부여하는 [Vibration] 위력, [Vibration] 횟수 부여량 +1 (최대 3)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137801].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [ObservedPerson], [Breath], [Vibration]
   znaczenie tagów: [ObservedPerson] = 피관찰자 / Subject of Observation; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor
   EN: Encounter Start: Apply 1 [ObservedPerson] on all enemies; then, gain [Breath] Potency and Count equal to the number of units with [ObservedPerson]\n\nTurn Start: Apply 1 [ObservedPerson] against targets without [ObservedPerson]\n\nFor every 10 [ObservedPerson] on the target, inflict +1 more [Vibration] Potency and Count with this unit's Skills (max 3)
   PL: Początek walki: nakłada 1 [ObservedPerson] wszystkim wrogom; następnie zyskuje Siłę i Liczniki [Breath] równe liczbie jednostek z [ObservedPerson]\n\nna Początku tury nakłada 1 [ObservedPerson] celom, które nie mają [ObservedPerson]\n\nza każde 10 [ObservedPerson] celu nakłada o 1 więcej Siły i Liczników [Vibration] Umiejętnościami tej jednostki (maks. 3)
855. [[a1c9p3] Pasywka wroga [137802] — nazwa] 적응
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137802].name
   limit: do 40 znaków
   EN: Adaptation
   PL: Adaptation
856. [[a1c9p3] Pasywka wroga [137802] — opis] 자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 횟수 1 추가로 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>턴 시작 시, 직전 턴에 자신에게 가장 많은 피해를 입힌 수감자에게 [ResultReduction] 3, [ObservedPerson] 5 부여\n- 대상의 [ObservedPerson]가 30이면, 대신 [ResultReduction] 5 부여</u></b></mark></color>
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137802].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [ObservedPerson], [ResultReduction]
   znaczenie tagów: [Breath] = 호흡 / Poise; [ObservedPerson] = 피관찰자 / Subject of Observation; [ResultReduction] = 위력 감소 / Power Down
   EN: Gain 1 [Breath] Potency every time this unit inflicts damage with Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain 1 additional [Breath] Potency with every hit\n\nGain +1 [Breath] Count every time this unit takes damage from a Sinner's Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain +1 additional [Breath] Count with every hit taken\n\n<color=#ff6000><mark=#ff000040><b><u>Turn Start: Inflict 3 [ResultReduction] and 5 [ObservedPerson] to the Sinner who dealt the most damage to this unit in the previous turn\n- If the target has 30 [ObservedPerson], inflict 5 [ResultReduction] instead</u></b></mark></color>
   PL: zyskuje 1 Siły [Breath] za każdym razem, gdy zadaje obrażenia efektami Umiejętności ataku (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowe 1 Siły [Breath] przy każdym trafieniu\n\nzyskuje 1 Licznika [Breath] za każdym razem, gdy otrzymuje obrażenia od efektów Umiejętności ataku Grzesznika (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowe 1 Licznika [Breath] przy każdym otrzymanym trafieniu\n\n<color=#ff6000><mark=#ff000040><b><u>na Początku tury nakłada 3 [ResultReduction] i 5 [ObservedPerson] Grzesznikowi, który zadał tej jednostce najwięcej obrażeń w poprzedniej turze\n- jeżeli cel ma 30 [ObservedPerson], zamiast tego nakłada 5 [ResultReduction]</u></b></mark></color>
857. [[a1c9p3] Pasywka wroga [137803] — nazwa] 방어기제
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137803].name
   limit: do 40 znaków
   EN: Defense Mechanism
   PL: Defense Mechanism
858. [[a1c9p3] Pasywka wroga [137803] — opis] 턴 시작 시, <color=#ff6000><mark=#ff000040><b><u>잃은 체력의 30%만큼 보호막을 얻음 (최대 체력의 25%를 초과하여 얻을 수 없음)</u></b></mark></color>\n- [Combustion] 상태일 경우, ([Combustion] 횟수 x 1.5)%만큼 보호막 수치가 대폭 감소\n- 보호막이 [Burst] 효과 피해를 100% 추가로 받음\n\n턴 종료 시 이 효과로 얻은 보호막이 파괴되었다면, 파괴된 횟수에 비례하여 이번 전투 동안 턴 시작 시 [DefenseDown] 1 얻음 (최대 5)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137803].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Burst], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Gain Shield equal to 30% of missing HP (Shield HP cannot exceed 25% of the max HP)</u></b></mark></color>\n- If this unit has [Combustion], lose ([Combustion] Count x 1.5)% Shield HP\n- Shield takes +100% damage from [Burst] effects\n\nTurn End: If the Shield gained due to this effect is destroyed, for the rest of this Encounter, gain 1 [DefenseDown] at Turn Start for every instance the Shield has been destroyed (max 5)
   PL: na Początku tury <color=#ff6000><mark=#ff000040><b><u>zyskuje Tarczę równą 30% brakującego HP (HP Tarczy nie może przekroczyć 25% Maks. HP)</u></b></mark></color>\n- jeżeli jednostka ma [Combustion], traci ([Combustion] Licznik x 1.5)% HP Tarczy\n- Tarcza otrzymuje +100% obrażeń od efektów [Burst]\n\nna koniec tury, jeżeli Tarcza zyskana dzięki temu efektowi została zniszczona, przez resztę tej walki na Początku tury zyskuje 1 [DefenseDown] za każde jej zniszczenie (maks. 5)
859. [[a1c9p3] Pasywka wroga [137804] — nazwa] 확증편향
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137804].name
   limit: do 40 znaków
   EN: Confirmation Bias
   PL: Confirmation Bias
860. [[a1c9p3] Pasywka wroga [137804] — opis] 턴 종료 시, <color=#ff6000><mark=#ff000040><b><u>수감자의 정신력을 10만큼 빼앗음</u></b></mark></color> (최대 3명, 정신력이 높은 순으로 적용, 동일한 대상에게 중첩 적용되지 않음\n(호엔하임이 패닉 상태에서는 발동하지 않음)\n\n<color=#ff6000><mark=#ff000040><b><u>자신의 정신력이 15 미만으로 내려가지 않음</u></b></mark></color>
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137804].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: Turn End: <color=#ff6000><mark=#ff000040><b><u>Siphon 10 SP from Sinners</u></b></mark></color> (max 3 Sinners in descending order of SP; does not apply cumulatively on the same target)\n(Does not activate if Hohenheim is Panicked)\n\n<color=#ff6000><mark=#ff000040><b><u>This unit's SP does not drop below 15</u></b></mark></color>
   PL: na koniec tury <color=#ff6000><mark=#ff000040><b><u> wysysa 10 SP od Grzeszników</u></b></mark></color> (maks. 3 Grzeszników, w kolejności od najwyższego SP; nie kumuluje się na tym samym celu)\n(nie uruchamia się, gdy Hohenheim jest w Panice)\n\n<color=#ff6000><mark=#ff000040><b><u>SP tej jednostki nie spada poniżej 15</u></b></mark></color>
861. [[a1c9p3] Pasywka wroga [137805] — nazwa] 가설 정립
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137805].name
   limit: do 40 znaków
   EN: Establish Hypothesis
   PL: Establish Hypothesis
862. [[a1c9p3] Pasywka wroga [137805] — opis] 세 번째 턴이 되면 패턴이 변경되어 강력한 스킬을 사용할 준비를 시작함.\n이후에는 턴 종료 시 [Breath] 횟수가 30 이상이 되었을 때, 위 효과가 발동\n\n강력한 스킬 준비 단계 동안 체력 피해를 입지 않았으면, 해당 스킬의 파괴력이 크게 증가함 (보호막 피해는 적용되지 않음)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137805].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On Turn 3: Gains a new pattern and prepares to use a powerful Skill.\nAfter Turn 3 is over: The above effect activates when this unit has 30+ [Breath] Count at Turn End\n\nIf this unit did not take any HP damage during the preparation period before using the powerful Skill, greatly enhance the Skill (does not count damages taken by Shield HP)
   PL: w 3. turze przybiera nowy wzorzec i zaczyna przygotowywać potężną Umiejętność.\nod tury po 3. turze: powyższy efekt uruchamia się na koniec tury, gdy Licznik [Breath] tej jednostki wynosi 30 lub więcej\n\njeżeli podczas przygotowywania potężnej Umiejętności jednostka nie otrzyma obrażeń HP, mocno wzmacnia tę Umiejętność (nie liczy obrażeń otrzymanych przez HP Tarczy)
863. [[a1c9p3] Pasywka wroga [137806] — nazwa] 부적응
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137806].name
   limit: do 40 znaków
   EN: Maladaptation
   PL: Maladaptation
864. [[a1c9p3] Pasywka wroga [137806] — opis] 선택지에 의하여 약화된 경우, 「적응」 패시브가 다음 효과로 변경 적용됨\n\n자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 횟수 1 추가로 얻음\n\n크리티컬 피해량이 증가하거나 감소하지 않음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137806].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [ObservedPerson]
   znaczenie tagów: [Breath] = 호흡 / Poise; [ObservedPerson] = 피관찰자 / Subject of Observation
   EN: When weakened due to a Choice Event, this Passive replaces 「Adaptation」\n\nGain 1 [Breath] Potency every time this unit inflicts damage with Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain 1 additional [Breath] Potency with every hit; however, reduce the target's [ObservedPerson] by 3\n\nGain +1 [Breath] Count every time this unit takes damage from a Sinner's Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain +1 additional [Breath] Count with every hit taken; however, reduce the target's [ObservedPerson] by 3\n\nCritical damage does not increase or decrease
   PL: gdy zostanie osłabiona przez Zdarzenie Wyboru, ten Pasyw zastępuje „Adaptation”\n\nzyskuje 1 Siły [Breath] za każdym razem, gdy zadaje obrażenia efektami Umiejętności ataku (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowe 1 Siły [Breath] przy każdym trafieniu, ale zmniejsza [ObservedPerson] celu o 3\n\nzyskuje 1 Licznika [Breath] za każdym razem, gdy otrzymuje obrażenia od efektów Umiejętności ataku Grzesznika (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowe 1 Licznika [Breath] przy każdym otrzymanym trafieniu, ale zmniejsza [ObservedPerson] celu o 3\n\nobrażenia krytyczne nie rosną ani nie maleją
865. [[a1c9p3] Pasywka wroga [137807] — nazwa] 엉성한 방어기제
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137807].name
   limit: do 40 znaków
   EN: Inadequate Defense Mechanism
   PL: Inadequate Defense Mechanism
866. [[a1c9p3] Pasywka wroga [137807] — opis] 선택지에 의하여 약화된 경우, 「방어기제」 패시브가 다음 효과로 변경 적용됨\n\n턴 시작 시, 잃은 체력의 15%만큼 보호막을 얻음 (최대 체력의 5%를 초과하여 얻을 수 없음)\n- [Combustion] 상태일 경우, ([Combustion] 횟수 x 2)%만큼 보호막 수치가 대폭 감소\n- 보호막이 [Burst] 효과 피해를 150% 추가로 받음\n\n턴 종료 시 이 효과로 얻은 보호막이 파괴되었다면, 파괴된 횟수에 비례하여 이번 전투 동안 턴 시작 시 [DefenseDown] 2 얻음 (최대 10)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137807].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Burst], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When weakened due to a Choice Event, this Passive replaces 「Defense Mechanism」\n\nTurn Start: Gain Shield equal to 15% of missing HP (Shield HP cannot exceed 5% of the max HP)\n- If this unit has [Combustion], lose ([Combustion] Count x 2)% Shield HP\n- Shield takes +150% damage from [Burst] effects\n\nTurn End: If the Shield gained due to this effect is destroyed, for the rest of this Encounter, gain 2 [DefenseDown] at Turn Start for every instance the Shield has been destroyed (max 10)
   PL: gdy zostanie osłabiona przez Zdarzenie Wyboru, ten Pasyw zastępuje „Defense Mechanism”\n\nna Początku tury zyskuje Tarczę równą 15% brakującego HP (HP Tarczy nie może przekroczyć 5% Maks. HP)\n- jeżeli jednostka ma [Combustion], traci ([Combustion] Licznik x 2)% HP Tarczy\n- Tarcza otrzymuje +150% obrażeń od efektów [Burst]\n\nna koniec tury, jeżeli Tarcza zyskana dzięki temu efektowi została zniszczona, przez resztę tej walki na Początku tury zyskuje 2 [DefenseDown] za każde jej zniszczenie (maks. 10)
867. [[a1c9p3] Pasywka wroga [137808] — nazwa] 자기 의심
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137808].name
   limit: do 40 znaków
   EN: Self-doubt
   PL: Self-doubt
868. [[a1c9p3] Pasywka wroga [137808] — opis] 선택지에 의하여 약화된 경우, 「확증편향」 패시브가 다음 효과로 변경 적용됨\n\n턴 시작 시, <color=#ff6000><mark=#ff000040><b><u>[Vulnerable] 3 얻고</u></b></mark></color> 자신의 정신력이 15만큼 감소\n턴 종료 시, 자신보다 정신력이 높은 대상의 정신력을 5만큼 빼앗음 (최대 3명, 정신력이 높은 순으로 적용, 동일한 대상에게 중첩 적용되지 않음)\n(호엔하임이 패닉 상태에서는 발동하지 않음)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137808].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: When weakened due to a Choice Event, this Passive replaces 「Confirmation Bias」\n\nTurn Start: <color=#ff6000><mark=#ff000040><b><u>Gain 3 [Vulnerable]</u></b></mark></color> and lose 15 SP\nTurn End: Siphon 5 SP from targets with higher SP than this unit (max 3 targets; in descending order of SP; cannot stack on the same target)\n(Does not activate if Hohenheim is Panicked)
   PL: gdy zostanie osłabiona przez Zdarzenie Wyboru, ten Pasyw zastępuje „Confirmation Bias”\n\nna Początku tury <color=#ff6000><mark=#ff000040><b><u>zyskuje 3 [Vulnerable]</u></b></mark></color> i traci 15 SP\nna koniec tury wysysa 5 SP od celów z wyższym SP niż ta jednostka (maks. 3 cele; w kolejności od najwyższego SP; nie kumuluje się na tym samym celu)\n(nie uruchamia się, gdy Hohenheim jest w Panice)
869. [[a1c9p3] Pasywka wroga [137809] — nazwa] 적응
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137809].name
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [[a1c9p3] Pasywka wroga [137809] — opis] 자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 횟수 1 추가로 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>턴 시작 시, 직전 턴에 자신에게 가장 많은 피해를 입힌 수감자에게 [ResultReduction] 3, [ObservedPerson] 5 부여\n- 대상의 [ObservedPerson]가 30이면, 대신 [ResultReduction] 5 부여</u></b></mark></color>
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137809].desc
   (powtórzenie elementu 856 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [[a1c9p3] Pasywka wroga [137810] — nazwa] 방어기제
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137810].name
   (powtórzenie elementu 857 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [[a1c9p3] Pasywka wroga [137810] — opis] 턴 시작 시, <color=#ff6000><mark=#ff000040><b><u>잃은 체력의 30%만큼 보호막을 얻음 (최대 체력의 25%를 초과하여 얻을 수 없음)</u></b></mark></color>\n- [Combustion] 상태일 경우, ([Combustion] 횟수 x 1.5)%만큼 보호막 수치가 대폭 감소\n- 보호막이 [Burst] 효과 피해를 100% 추가로 받음\n\n턴 종료 시 이 효과로 얻은 보호막이 파괴되었다면, 파괴된 횟수에 비례하여 이번 전투 동안 턴 시작 시 [DefenseDown] 1 얻음 (최대 5)
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137810].desc
   (powtórzenie elementu 858 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [[a1c9p3] Pasywka wroga [137811] — nazwa] 부적응
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137811].name
   (powtórzenie elementu 863 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [[a1c9p3] Pasywka wroga [137811] — opis] 선택지에 의하여 약화된 경우, 「적응」 패시브가 다음 효과로 변경 적용됨\n\n자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 횟수 1 추가로 얻음\n\n크리티컬 피해량이 증가하거나 감소하지 않음
   źródło: Passives_Abnormality-a1c9p3.json :: dataList[id=137811].desc
   (powtórzenie elementu 864 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [bossraid] Umiejętności wrogów / Anomalii — Skills_Abnormality-BossRaid
- grupa rozdziału/trybu: `bossraid` · plik: `Skills_Abnormality-BossRaid.json`

875. [Umiejętność wroga [500101] (ulepszenie 1) — nazwa] 주먹질
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500101].levelList[level=1].name
   limit: do 40 znaków
   EN: Punching
   PL: Punching
876. [Umiejętność wroga [500101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 3
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 3 dodatkowe obrażenia Uderzeniem
877. [Umiejętność wroga [500101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 3
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 876 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność wroga [500101] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis]
   PL: [OnSucceedAttack] nakłada 3 [Paralysis]
879. [Umiejętność wroga [500102] (ulepszenie 1) — nazwa] 발길질
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500102].levelList[level=1].name
   limit: do 40 znaków
   EN: Kicking
   PL: Kicking
880. [Umiejętność wroga [500102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 5
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 5 dodatkowych obrażeń Uderzeniem
881. [Umiejętność wroga [500102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 5
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 880 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Umiejętność wroga [500102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 3 [Paralysis] w następnej turze
883. [Umiejętność wroga [500103] (ulepszenie 1) — nazwa] 되갚기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500103].levelList[level=1].name
   limit: do 40 znaków
   EN: Payback
   PL: Payback
884. [Umiejętność wroga [500103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 5 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 5 SP
   PL: [OnSucceedAttack] cel traci 5 SP
885. [Umiejętność wroga [500104] (ulepszenie 1) — nazwa] 뒤통수 조심!
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500104].levelList[level=1].name
   limit: do 40 znaków
   EN: Watch Your Back!
   PL: Watch Your Back!
886. [Umiejętność wroga [500104] (ulepszenie 1) — opis] 대상의 정신력이 0 미만인 경우, 코인 위력 +3
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500104].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has less than 0 SP, Coin Power +3
   PL: jeżeli SP celu jest niższe niż 0, Moc Monety +3
887. [Umiejętność wroga [500104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 10 회복
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność wroga [500104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2, [Reduction] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 2 [Binding] and 2 [Reduction] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] i 2 [Reduction] w następnej turze
889. [Umiejętność wroga [500104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 20 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 20 SP
   PL: [OnSucceedAttack] cel traci 20 SP
890. [Umiejętność wroga [500105] (ulepszenie 1) — nazwa] 다들 집합
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500105].levelList[level=1].name
   limit: do 40 znaków
   EN: Assemble
   PL: Assemble
891. [Umiejętność wroga [500105] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 아군 2명 소환
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Summon 2 allies next turn
   PL: [StartBattle] przywołuje 2 sojuszników w następnej turze
892. [Umiejętność wroga [500106] (ulepszenie 1) — nazwa] 내 몸에 새겨봐라
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500106].levelList[level=1].name
   limit: do 40 znaków
   EN: Make this Memorable
   PL: Make this Memorable
893. [Umiejętność wroga [500107] (ulepszenie 1) — nazwa] 내 헤어쿠포오오오온!!!
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500107].levelList[level=1].name
   limit: do 40 znaków
   EN: MY HAIR COUPOOOOOOOOOOONS!!!
   PL: MY HAIR COUPOOOOOOOOOOONS!!!
894. [Umiejętność wroga [500107] (ulepszenie 1) — opis] [DefeatDuel] 최종 피해량이 30%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500107].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -30% final damage and damage dealt by this Skill cannot Stagger the target
   PL: [DefeatDuel] zadaje o 30% mniej końcowych obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
895. [Umiejętność wroga [500107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 흐트러짐 손상 30
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Raise Stagger Threshold by 30
   PL: [UnBrokenCoinOnSucceedAttack] podnosi Próg Oszołomienia o 30
896. [Umiejętność wroga [500107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Paralysis] w następnej turze
897. [Umiejętność wroga [500107] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [RicardoBookRaid] 5 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500107].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [OnSucceedAttack] Reduce [RicardoBookRaid] on target by 5
   PL: [OnSucceedAttack] zmniejsza [RicardoBookRaid] celu o 5
898. [Umiejętność wroga [500108] (ulepszenie 1) — nazwa] 고통 새기기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500108].levelList[level=1].name
   limit: do 40 znaków
   EN: Promised Suffering
   PL: Promised Suffering
899. [Umiejętność wroga [500108] (ulepszenie 1) — opis] [RicardoBookRaid]의 수치가 가장 높은 대상을 우선 지정\n[WhenUse] 대상의 <color=#ff6000><mark=#ff000040><b><u>[RicardoBookRaid]이 3 이상이면,</u></b></mark></color>\n이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500108].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RicardoBookRaid], [WhenUse], [SuperCoin]
   znaczenie tagów: [RicardoBookRaid] = 장부에 적힘 / Written in the Book; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Prioritizes targets that have the highest [RicardoBookRaid] Stack\n[WhenUse] If target has <color=#ff6000><mark=#ff000040><b><u>3+ [RicardoBookRaid],</u></b></mark></color> convert all Coins on this Skill to [SuperCoin]s
   PL: priorytet: cele z najwyższym Licznikiem [RicardoBookRaid]\n[WhenUse] jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>3+ [RicardoBookRaid]</u></b></mark></color>,\nwszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y
900. [Umiejętność wroga [500108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] this turn and next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w tej i następnej turze
901. [Umiejętność wroga [500108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność wroga [500108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (대상이 보유한 [RicardoBookRaid] x 3)만큼 타격 추가 피해
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [OnSucceedAttack] Inflict ([RicardoBookRaid] on target x 3) Blunt bonus damage
   PL: [OnSucceedAttack] zadaje ([RicardoBookRaid] celu x 3) dodatkowych obrażeń Uderzeniem
903. [Umiejętność wroga [500108] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [RicardoBookRaid] 3 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500108].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [OnSucceedAttack] Reduce [RicardoBookRaid] on target by 3
   PL: [OnSucceedAttack] zmniejsza [RicardoBookRaid] celu o 3
904. [Umiejętność wroga [500109] (ulepszenie 1) — nazwa] 장난이 길었군
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500109].levelList[level=1].name
   limit: do 40 znaków
   EN: Enough Games
   PL: Enough Games
905. [Umiejętność wroga [500109] (ulepszenie 1) — opis] [StartBattle] 정신력 20 회복\n[EndBattle] 다음 턴에 [Enhancement] 5 얻음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500109].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [EndBattle], [Enhancement]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [StartBattle] Heal 20 SP\n[EndBattle] Gain 5 [Enhancement] next turn
   PL: [StartBattle] przywraca 20 SP\n[EndBattle] zyskuje 5 [Enhancement] w następnej turze
906. [Umiejętność wroga [500110] (ulepszenie 1) — nazwa] 전원, 처형이다!!!
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500110].levelList[level=1].name
   limit: do 50 znaków
   EN: COMPLETE AND TOTAL EXTERMINATION!!!
   PL: COMPLETE AND TOTAL EXTERMINATION!!!
907. [Umiejętność wroga [500110] (ulepszenie 1) — opis] [DefeatDuel] 최종 피해량이 30%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500110].levelList[level=1].desc
   (powtórzenie elementu 894 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność wroga [500110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Umiejętność wroga [500110] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [RicardoBookRaid] 1당 최대 체력의 3% 피해
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500110].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [UnBrokenCoinOnSucceedAttack] Deal damage equal to 3% of target's max HP for every [RicardoBookRaid] on target
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia równe 3% Maks. HP celu za każde [RicardoBookRaid] celu
910. [Umiejętność wroga [500110] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [RicardoBookRaid] 10 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500110].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [OnSucceedAttack] Reduce [RicardoBookRaid] on target by 10
   PL: [OnSucceedAttack] zmniejsza [RicardoBookRaid] celu o 10
911. [Umiejętność wroga [500111] (ulepszenie 1) — nazwa] 우리 식구들이었군
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500111].levelList[level=1].name
   limit: do 40 znaków
   EN: Ah, You Were One of the Fam
   PL: Ah, You Were One of the Fam
912. [Umiejętność wroga [500111] (ulepszenie 1) — opis] [StartBattle] 모든 중지 소속 유닛의 정신력 10 회복
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500111].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] All of The Middle-faction units heal 10 SP
   PL: [StartBattle] wszystkie jednostki frakcji Środkowego przywracają 10 SP
913. [Umiejętność wroga [500112] (ulepszenie 1) — nazwa] 날 속인거냐!!!
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500112].levelList[level=1].name
   limit: do 40 znaków
   EN: TRICKED ME, DID YOU??!!
   PL: TRICKED ME, DID YOU??!!
914. [Umiejętność wroga [500112] (ulepszenie 1) — opis] [StartBattle] 정신력 20 감소\n[StartBattle] [AttackUp] 6 얻음\n[StartBattle] [Vulnerable] 4 얻음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500112].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackUp], [Vulnerable]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Vulnerable] = 취약 / Fragile
   EN: [StartBattle] Lose 20 SP\n[StartBattle] Gain 6 [AttackUp]\n[StartBattle] Gain 4 [Vulnerable]
   PL: [StartBattle] traci 20 SP\n[StartBattle] zyskuje 6 [AttackUp]\n[StartBattle] zyskuje 4 [Vulnerable]
915. [Umiejętność wroga [500112] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500112].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Umiejętność wroga [500113] (ulepszenie 1) — nazwa] 원한 곱씹기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500113].levelList[level=1].name
   limit: do 40 znaków
   EN: Swear Vengeance
   PL: Swear Vengeance
917. [Umiejętność wroga [500113] (ulepszenie 1) — opis] [EndBattle] 다음 턴에 [AttackUp] 3 얻음\n- 이 스킬을 사용하는 슬롯을 <color=#ff6000><mark=#ff000040><b><u>메인 타겟으로 지정한 공격 스킬이 있으면,</u></b></mark></color>\n이 효과로 얻는 [AttackUp] 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500113].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [EndBattle], [AttackUp]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [EndBattle] Gain 3 [AttackUp] next turn\n- If the Slot using this Skill <color=#ff6000><mark=#ff000040><b><u>is a main target of an Attack Skill</u></b></mark></color>, gain 1 less [AttackUp] Stack from this effect
   PL: [EndBattle] zyskuje 3 [AttackUp] w następnej turze\n- jeżeli Slot używający tej Umiejętności <color=#ff6000><mark=#ff000040><b><u>jest głównym celem Umiejętności ataku</u></b></mark></color>, zyskuje o 1 mniej Licznika [AttackUp] z tego efektu
918. [Umiejętność wroga [500114] (ulepszenie 1) — nazwa] 즉결 처형이다!
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500114].levelList[level=1].name
   limit: do 70 znaków
   EN: IMMEDIATE, COMPLETE, AND TOTAL EXTERMINATION!
   PL: IMMEDIATE, COMPLETE, AND TOTAL EXTERMINATION!
919. [Umiejętność wroga [500114] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [RicardoBookRaid] 1당 최대 체력의 1% 피해
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500114].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [OnSucceedAttack] Deal damage equal to 1% of target's max HP for every [RicardoBookRaid] on target
   PL: [OnSucceedAttack] zadaje obrażenia równe 1% Maks. HP celu za każde [RicardoBookRaid] celu
920. [Umiejętność wroga [500114] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [RicardoBookRaid] 1당 최대 체력의 1% 피해
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500114].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 919 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność wroga [500114] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [RicardoBookRaid] 1당 최대 체력의 1% 피해
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500114].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 919 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność wroga [500115] (ulepszenie 1) — nazwa] 시험은 끝났다
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500115].levelList[level=1].name
   limit: do 40 znaków
   EN: No More Tests
   PL: No More Tests
923. [Umiejętność wroga [500115] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [HitDamageUp] 3 얻음\n[WhenUse] 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[RicardoBookRaid]이 5 이상이면,</u></b></mark></color>\n이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500115].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [HitDamageUp], [RicardoBookRaid], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [RicardoBookRaid] = 장부에 적힘 / Written in the Book; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Gain 3 [HitDamageUp] next turn\n[WhenUse] If the main target has <color=#ff6000><mark=#ff000040><b><u>5+ [RicardoBookRaid]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s
   PL: [WhenUse] zyskuje 3 [HitDamageUp] w następnej turze\n[WhenUse] jeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>5+ [RicardoBookRaid]</u></b></mark></color>, wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y
924. [Umiejętność wroga [500116] (ulepszenie 1) — nazwa] 형님의 자비
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500116].levelList[level=1].name
   limit: do 40 znaków
   EN: Mercy of the Big Brother
   PL: Mercy of the Big Brother
925. [Umiejętność wroga [500116] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500116].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność wroga [500116] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상의 [RicardoBookRaid] 10 감소</u></b></mark></color>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500116].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [RicardoBookRaid]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RicardoBookRaid] = 장부에 적힘 / Written in the Book
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Reduce [RicardoBookRaid] on target by 10</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zmniejsza [RicardoBookRaid] celu o 10</u></b></mark></color>
927. [Umiejętność wroga [500116] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상을 흐트러짐 상태로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500116].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Stagger target</u></b></mark></color>
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Oszołomi cel</u></b></mark></color>
928. [Umiejętność wroga [500301] (ulepszenie 1) — nazwa] 기회 잡기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500301].levelList[level=1].name
   limit: do 40 znaków
   EN: Seize ya Chance
   PL: Seize ya Chance
929. [Umiejętność wroga [500301] (ulepszenie 1) — opis] [BeforeHit] 대상의 [MiddleFingerBook] 수치당, 보호막 5 얻음 (턴 당 1회, 최대 50)\n[WhenUse] 대상의 [MiddleFingerBook] 수치가 5 이상이면, 기본 위력 +3, [DefenseDown] 4 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500301].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeHit], [MiddleFingerBook], [WhenUse], [DefenseDown]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [BeforeHit] Gain 5 Shield for every [MiddleFingerBook] on the target (once per turn; max 50)\n[WhenUse] If target has 5+ [MiddleFingerBook], Base Power +3; inflict 4 [DefenseDown]
   PL: [BeforeHit] zyskuje 5 Tarczy za każdy [MiddleFingerBook] celu (1 raz na turę; maks. 50)\n[WhenUse] jeżeli cel ma 5+ [MiddleFingerBook], Moc Bazowa +3; nakłada 4 [DefenseDown]
930. [Umiejętność wroga [500401] (ulepszenie 1) — nazwa] 배로 갚기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=500401].levelList[level=1].name
   limit: do 40 znaków
   EN: Multifold Retribution
   PL: Multifold Retribution
931. [Umiejętność wroga [501203] (ulepszenie 1) — nazwa] 곰 허리 끊기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501203].levelList[level=1].name
   limit: do 40 znaków
   EN: Bearspine Breaker
   PL: Bearspine Breaker
932. [Umiejętność wroga [501203] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 7 이상이면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +100%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501203].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Laceration], [ChoiSwordsmanship], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], deal +40% damage on Critical Hit\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>At 7+ [ChoiSwordsmanship], convert all Coins into [SuperCoin]s and deal +100% damage on Critical Hit</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] przy 8+ [Breath] zadaje +40% obrażeń przy trafieniu krytycznym\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>przy 7+ [ChoiSwordsmanship] wszystkie Monety zmieniają się w [SuperCoin]y i zadaje +100% obrażeń przy trafieniu krytycznym</u></b></mark></color>\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
933. [Umiejętność wroga [501203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 1 [SlashResistDown] this turn and next turn
   PL: [OnSucceedAttack] nakłada 1 [SlashResistDown] w tej i następnej turze
934. [Umiejętność wroga [501203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 3
935. [Umiejętność wroga [501207] (ulepszenie 1) — nazwa] 범 가르기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501207].levelList[level=1].name
   limit: do 40 znaków
   EN: Tigersplitter
   PL: Tigersplitter
936. [Umiejętność wroga [501207] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 3 이하면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +100%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501207].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Laceration], [ChoiSwordsmanship], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], deal +40% damage on Critical Hit\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>At 3 or fewer [ChoiSwordsmanship], convert all Coins into [SuperCoin]s and deal +100% damage on Critical Hit</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] przy 8+ [Breath] zadaje +40% obrażeń przy trafieniu krytycznym\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>przy 3 lub mniej [ChoiSwordsmanship] wszystkie Monety zmieniają się w [SuperCoin]y i zadaje +100% obrażeń przy trafieniu krytycznym</u></b></mark></color>\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
937. [Umiejętność wroga [501207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 2
938. [Umiejętność wroga [501207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 937 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Umiejętność wroga [501207] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501207].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
940. [Umiejętność wroga [501207] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501207].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 933 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Umiejętność wroga [501209] (ulepszenie 1) — nazwa] 본국검[살] - 가다듬기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501209].levelList[level=1].name
   limit: do 70 znaków
   EN: Sword of the Homeland [Sal] - Reassume Stance
   PL: Sword of the Homeland [Sal] - Reassume Stance
942. [Umiejętność wroga [501209] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 감소</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501209].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [SupportProtect], [SuperCoin], [StartDuel], [EndSkill]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SupportProtect] = 원호 방어 / Assist Defense; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Unaffected by [ChoiSwordsmanship]\nIf target's Skill is [SupportProtect] Exclusive Skill, convert into [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>Lose 3 [ChoiSwordsmanship]</color></mark></b></u>\n- If target's Skill is [SupportProtect] Exclusive Skill, this effect does not activate\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>On Hit as an Unopposed Attack, or On Hit against target that used [SupportProtect] Exclusive Skill, gain 2 [ChoiSwordsmanship]</color></mark></b></u>
   PL: nie podlega wpływowi [ChoiSwordsmanship]\njeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], zmienia się w [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>traci 3 [ChoiSwordsmanship]</u></b></mark></color>\n- jeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], ten efekt nie uruchamia się\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przy trafieniu jako Atak Jednostronny albo przy trafieniu celu, który użył Umiejętności wyłącznie dla [SupportProtect], zyskuje 2 [ChoiSwordsmanship]</u></b></mark></color>
943. [Umiejętność wroga [501210] (ulepszenie 1) — nazwa] 본국검[살] - 벼리기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501210].levelList[level=1].name
   limit: do 60 znaków
   EN: Sword of the Homeland [Sal] - Swordhoning
   PL: Sword of the Homeland [Sal] - Swordhoning
944. [Umiejętność wroga [501210] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 얻음</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 감소</color></mark></b></u>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501210].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [SupportProtect], [SuperCoin], [StartDuel], [EndSkill]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SupportProtect] = 원호 방어 / Assist Defense; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Unaffected by [ChoiSwordsmanship]\nIf target's Skill is [SupportProtect] Exclusive Skill, convert into [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>Gain 3 [ChoiSwordsmanship]</color></mark></b></u>\n- If target's Skill is [SupportProtect] Exclusive Skill, this effect does not activate\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>On Hit as an Unopposed Attack, or On Hit against target that used [SupportProtect] Exclusive Skill, lose 2 [ChoiSwordsmanship]</color></mark></b></u>
   PL: nie podlega wpływowi [ChoiSwordsmanship]\njeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], zmienia się w [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>zyskuje 3 [ChoiSwordsmanship]</u></b></mark></color>\n- jeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], ten efekt nie uruchamia się\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przy trafieniu jako Atak Jednostronny albo przy trafieniu celu, który użył Umiejętności wyłącznie dla [SupportProtect], traci 2 [ChoiSwordsmanship]</u></b></mark></color>
945. [Umiejętność wroga [501303] (ulepszenie 1) — nazwa] 곰 허리 끊기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501303].levelList[level=1].name
   (powtórzenie elementu 931 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Umiejętność wroga [501303] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChoiSwordsmanship]이 6을 초과하면, 초과하는 값만큼 <noparse>최종 위력 증가</noparse> (최대 3)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 7 이상이면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +100%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501303].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Laceration], [ChoiSwordsmanship], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], deal +40% damage on Critical Hit\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] At more than 6 [ChoiSwordsmanship], gain Final Power for every excess [ChoiSwordsmanship] Stack (max 3)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>At 7+ [ChoiSwordsmanship], convert all Coins into [SuperCoin]s and deal +100% damage on Critical Hit</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] przy 8+ [Breath] zadaje +40% obrażeń przy trafieniu krytycznym\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] przy więcej niż 6 [ChoiSwordsmanship] zyskuje Końcową Moc za każdy nadmiarowy Licznik [ChoiSwordsmanship] (maks. 3)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>przy 7+ [ChoiSwordsmanship] wszystkie Monety zmieniają się w [SuperCoin]y i zadaje +100% obrażeń przy trafieniu krytycznym</u></b></mark></color>\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
947. [Umiejętność wroga [501303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 933 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Umiejętność wroga [501303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 934 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Umiejętność wroga [501304] (ulepszenie 1) — nazwa] 산군도 이 칼끝 아래 두동강나리
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501304].levelList[level=1].name
   limit: do 60 znaków
   EN: Even Sanguns Shall Be Cleft Under This Sword
   PL: Even Sanguns Shall Be Cleft Under This Sword
950. [Umiejętność wroga [501304] (ulepszenie 1) — opis] [Laceration]이 가장 많은 적을 대상으로 함\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 [ChoiSwordsmanship]이 6을 초과하면, 초과하는 값당 최종 위력 +2 (최대 6)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>이 스킬은 [Breath] 횟수를 소모하지 않고 반드시 스킬 코인이 앞면으로 결정되고 크리티컬로 적중함</color></mark></b></u>\n[BeforeAttack] 자신의 [ChoiSwordsmanship] 2당 크리티컬 피해량 +30% (최대 120%)\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501304].levelList[level=1].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Laceration], [WhenUse], [ChoiSwordsmanship], [WinDuel], [Breath], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy that has the most [Laceration]\n[WhenUse] Cannot be Staggered from taking damage until this Skill ends\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)\n[WhenUse] At more than 6 [ChoiSwordsmanship], gain Final Power +2 for every excess [ChoiSwordsmanship] Stack (max 6)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>This Skill always flips Head, hits Critically, and does not consume [Breath] Count</color></mark></b></u>\n[BeforeAttack] Deal +30% damage on Critical Hit for every 2 [ChoiSwordsmanship] on self (max 120%)\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: cel: wróg z największą liczbą [Laceration]\n[WhenUse] nie przechodzi w Oszołamienie od otrzymanych obrażeń do zakończenia tej Umiejętności\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 3)\n[WhenUse] przy więcej niż 6 [ChoiSwordsmanship] zyskuje Końcową Moc +2 za każdy nadmiarowy Licznik [ChoiSwordsmanship] (maks. 6)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>ta Umiejętność zawsze wyrzuca Awers, trafia krytycznie i nie zużywa Licznika [Breath]</u></b></mark></color>\n[BeforeAttack] zadaje +30% obrażeń przy trafieniu krytycznym za każde 2 [ChoiSwordsmanship] tej jednostki (maks. 120%)\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
951. [Umiejętność wroga [501304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność wroga [501304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인의 최종 피해량의 (자신의 [Breath] X 10)%만큼 참격 피해 (최대 100%)
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Deal (([Breath] on self x 10)% of this Coin's final damage) Slash damage (max 100%)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Cięcia równe ([Breath] tej jednostki x 10)% końcowych obrażeń tej Monety (maks. 100%)
953. [Umiejętność wroga [501304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인의 최종 피해량의 (대상의 [Laceration] X 10)%만큼 색욕 피해 (최대 100%)
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Deal (([Laceration] on target x 10)% of this Coin's final damage) Lust damage (max 100%)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Żądzy równe ([Laceration] celu x 10)% końcowych obrażeń tej Monety (maks. 100%)
954. [Umiejętność wroga [501304] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501304].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [OnSucceedAttack] uruchamia [Laceration] celu 1 raz. Cel traci 1 Licznika [Laceration]
955. [Umiejętność wroga [501307] (ulepszenie 1) — nazwa] 범 가르기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501307].levelList[level=1].name
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Umiejętność wroga [501307] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 3 이하면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +100%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501307].levelList[level=1].desc
   (powtórzenie elementu 936 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Umiejętność wroga [501307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 937 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Umiejętność wroga [501307] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501307].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 937 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Umiejętność wroga [501307] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501307].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Umiejętność wroga [501307] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501307].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 933 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
