# Paczka AI P76 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 12/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P76_3c_przeciwnicy_i_anomalie_cz12.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P76_3c_przeciwnicy_i_anomalie_cz12.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [bossraid] Umiejętności wrogów / Anomalii — Skills_Abnormality-BossRaid
- grupa rozdziału/trybu: `bossraid` · plik: `Skills_Abnormality-BossRaid.json`

1. [Umiejętność wroga [501308] (ulepszenie 1) — nazwa] 어떤 산범들의 살이든 가르리
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].name
   limit: do 60 znaków
   EN: No Tiger's Flesh Shall Be Left Uncloven
   PL: No Tiger's Flesh Shall Be Left Uncloven
2. [Umiejętność wroga [501308] (ulepszenie 1) — opis] [Laceration]이 가장 많은 적을 대상으로 함\n<color=#ff6000><mark color=#ff000040><b><u>속도와 상관없이 이 스킬과 합을 할 수 있음</color></mark></b></u>\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 3)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>이 스킬은 [Breath]을 소모하지 않고 반드시 스킬 코인이 앞면으로 결정되고 크리티컬로 적중함</color></mark></b></u>\n[BeforeAttack] 자신의 [Breath] 2당 크리티컬 피해량 +30% (최대 120%)\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Laceration], [WhenUse], [WinDuel], [Breath], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy that has the most [Laceration]\n<color=#ff6000><mark color=#ff000040><b><u>Can Clash with this Skill regardless of Speed</color></mark></b></u>\n[WhenUse] Cannot be Staggered from taking damage until this Skill ends\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>This Skill always flips Head, hits Critically, and does not consume [Breath] Count</color></mark></b></u>\n[BeforeAttack] Deal +30% damage on Critical Hit for every 2 [Breath] on self (max 120%)\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: cel: wróg z największą liczbą [Laceration]\n<color=#ff6000><mark color=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[WhenUse] nie przechodzi w Oszołamienie od otrzymanych obrażeń do zakończenia tej Umiejętności\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 3)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>ta Umiejętność zawsze wyrzuca Awers, trafia krytycznie i nie zużywa Licznika [Breath]</u></b></mark></color>\n[BeforeAttack] zadaje +30% obrażeń przy trafieniu krytycznym za każde 2 [Breath] tej jednostki (maks. 120%)\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
3. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
4. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
5. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [OnSucceedAttack] uruchamia [Laceration] celu 1 raz. Cel traci 1 Licznika [Laceration]
6. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
9. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
10. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 메인 타겟의 [Laceration]이 10 이상이면, 이 코인이 적중한 대상의 [Laceration] 횟수 8 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If the main target has 10+ [Laceration], inflict +8 [Laceration] Count on targets hit by this Coin
   PL: [OnSucceedAttack] jeżeli główny cel ma 10+ [Laceration], trafione tą Monetą cele zyskują +8 Licznika [Laceration]
14. [Umiejętność wroga [501308] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 8 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501308].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +8 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +8 Licznika [Laceration]
15. [Umiejętność wroga [501309] (ulepszenie 1) — nazwa] 본국검[살] - 가다듬기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501309].levelList[level=1].name
   limit: do 70 znaków
   EN: Sword of the Homeland [Sal] - Reassume Stance
   PL: Sword of the Homeland [Sal] - Reassume Stance
16. [Umiejętność wroga [501309] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 감소</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501309].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [SupportProtect], [SuperCoin], [StartDuel], [EndSkill]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SupportProtect] = 원호 방어 / Assist Defense; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Unaffected by [ChoiSwordsmanship]\nIf target's Skill is [SupportProtect] Exclusive Skill, convert into [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>Lose 3 [ChoiSwordsmanship]</color></mark></b></u>\n- If target's Skill is [SupportProtect] Exclusive Skill, this effect does not activate\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>On Hit as an Unopposed Attack, or On Hit against target that used [SupportProtect] Exclusive Skill, gain 2 [ChoiSwordsmanship]</color></mark></b></u>
   PL: nie podlega wpływowi [ChoiSwordsmanship]\njeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], zmienia się w [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>traci 3 [ChoiSwordsmanship]</u></b></mark></color>\n- jeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], ten efekt nie uruchamia się\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przy trafieniu jako Atak Jednostronny albo przy trafieniu celu, który użył Umiejętności wyłącznie dla [SupportProtect], zyskuje 2 [ChoiSwordsmanship]</u></b></mark></color>
17. [Umiejętność wroga [501310] (ulepszenie 1) — nazwa] 본국검[살] - 벼리기
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501310].levelList[level=1].name
   limit: do 60 znaków
   EN: Sword of the Homeland [Sal] - Swordhoning
   PL: Sword of the Homeland [Sal] - Swordhoning
18. [Umiejętność wroga [501310] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 얻음</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 감소</color></mark></b></u>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501310].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [SupportProtect], [SuperCoin], [StartDuel], [EndSkill]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SupportProtect] = 원호 방어 / Assist Defense; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Unaffected by [ChoiSwordsmanship]\nIf target's Skill is [SupportProtect] Exclusive Skill, convert into [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>Gain 3 [ChoiSwordsmanship]</color></mark></b></u>\n- If target's Skill is [SupportProtect] Exclusive Skill, this effect does not activate\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>On Hit as an Unopposed Attack, or On Hit against target that used [SupportProtect] Exclusive Skill, lose 2 [ChoiSwordsmanship]</color></mark></b></u>
   PL: nie podlega wpływowi [ChoiSwordsmanship]\njeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], zmienia się w [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>zyskuje 3 [ChoiSwordsmanship]</u></b></mark></color>\n- jeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], ten efekt nie uruchamia się\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przy trafieniu jako Atak Jednostronny albo przy trafieniu celu, który użył Umiejętności wyłącznie dla [SupportProtect], traci 2 [ChoiSwordsmanship]</u></b></mark></color>
19. [Umiejętność wroga [501901] (ulepszenie 1) — nazwa] 이연참
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501901].levelList[level=1].name
   limit: do 40 znaków
   EN: Double Slash
   PL: Double Slash
20. [Umiejętność wroga [501901] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)
   PL: Końcowa Moc +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. 2)
21. [Umiejętność wroga [501901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] nakłada 2 [Vibration]
22. [Umiejętność wroga [501901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
23. [Umiejętność wroga [501902] (ulepszenie 1) — nazwa] 삼연격
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501902].levelList[level=1].name
   limit: do 40 znaków
   EN: Triple Slash
   PL: Triple Slash
24. [Umiejętność wroga [501902] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501902].levelList[level=1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Umiejętność wroga [501902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada +2 Licznika [Vibration]
26. [Umiejętność wroga [501902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 1 [Vibration] i +2 Licznika [Vibration]
27. [Umiejętność wroga [501902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
28. [Umiejętność wroga [501903] (ulepszenie 1) — nazwa] 이연참-폭[爆]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501903].levelList[level=1].name
   limit: do 40 znaków
   EN: Double Slash - Blast [爆]
   PL: Double Slash - Blast [爆]
29. [Umiejętność wroga [501903] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 4)\n[DefeatDuel] [BulletPropellant] 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501903].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [DefeatDuel], [BulletPropellant]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 4)\n[DefeatDuel] Lose 1 [BulletPropellant]
   PL: Końcowa Moc +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. 4)\n[DefeatDuel] traci 1 [BulletPropellant]
30. [Umiejętność wroga [501903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność wroga [501903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellant]
   PL: zużywa 1 [BulletPropellant]
32. [Umiejętność wroga [501903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 3 [Combustion] i zwiększa Licznik [Combustion] o 2
33. [Umiejętność wroga [501903] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501903].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 2
34. [Umiejętność wroga [501904] (ulepszenie 1) — nazwa] 삼연격-폭[爆]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].name
   limit: do 40 znaków
   EN: Triple Slash - Blast [爆]
   PL: Triple Slash - Blast [爆]
35. [Umiejętność wroga [501904] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 4)\n[DefeatDuel] [BulletPropellant] 1 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 2
40. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność wroga [501904] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501904].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [VibrationExplosion] 2 razy, po czym zmniejsza Licznik [Vibration] celu o 2
43. [Umiejętność wroga [501905] (ulepszenie 1) — nazwa] 폭쇄참 [爆碎斬]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].name
   limit: do 40 znaków
   EN: Blasting Shatterslash [爆碎斬]
   PL: Blasting Shatterslash [爆碎斬]
44. [Umiejętność wroga [501905] (ulepszenie 1) — opis] [Prey_leiheng]을 보유한 대상을 우선으로 지정\n<color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n대상의 [Combustion]과 [Vibration]의 합 6당 코인 위력 +1 (최대 3)\n[DefeatDuel] 자신의 정신력 10 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Prey_leiheng], [Combustion], [Vibration], [DefeatDuel]
   znaczenie tagów: [Prey_leiheng] = 사냥감 / Prey; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets that have [Prey_leiheng]\n<color=#ff6000><mark=#ff000040><b><u>Can clash with this Skill regardless of Speed</u></b></mark></color>\nCoin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 3)\n[DefeatDuel] Lose 10 SP
   PL: priorytet: cele z [Prey_leiheng]\n<color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\nMoc Monety +1 za każde 6 (suma [Combustion] i [Vibration] celu) (maks. 3)\n[DefeatDuel] traci 10 SP
45. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] nakłada 3 [Combustion]
48. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 4 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Vibration] and +4 [Vibration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Vibration] i zwiększa Licznik [Vibration] o 4
50. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL: [OnSucceedAttack] nakłada +3 Licznika [Combustion]
53. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada +3 Licznika [Vibration]
54. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 2, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [Switch_Vibration], przekształcając je w [VibrationIgnition]
55. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 3, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 3, efekt 3 — opis] <color=#ff6000><mark=#ff000040><b><u>이 코인 효과로 [BulletPropellant]을 소모하였다면, 피해량 +50%</u></b></mark></color>
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: <color=#ff6000><mark=#ff000040><b><u>If this unit spent [BulletPropellant] due to this Coin's effect, deal +50% damage</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka zużyła [BulletPropellant] efektem tej Monety, zadaje +50% obrażeń</u></b></mark></color>
58. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +3 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 3 [Combustion] i zwiększa Licznik [Combustion] o 3
59. [Umiejętność wroga [501905] (ulepszenie 1) — moneta 3, efekt 5 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501905].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> uruchamia [VibrationExplosion] 2 razy, po czym zmniejsza Licznik [Vibration] celu o 2
60. [Umiejętność wroga [501906] (ulepszenie 1) — nazwa] 쾌도난마 [快刀亂麻]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].name
   limit: do 40 znaków
   EN: Tanglecleaver [快刀亂麻]
   PL: Tanglecleaver [快刀亂麻]
61. [Umiejętność wroga [501906] (ulepszenie 1) — opis] [Prey_leiheng]을 보유한 대상을 우선으로 지정\n<color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음</u></b></mark></color>\n[WhenUse] [BattleSense]을 전부 소모. 소모한 수치가\n- 10 이상이면, 10당 공격 가중치 +1 (최대 2)\n- 25일 경우, 메인 타겟의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 5)\n[DefeatDuel] [Paralysis] 1 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않으며, <color=#ff6000><mark=#ff000040><b><u>[Combustion] 위력과 횟수, [Vibration] 위력과 횟수 부여량이 절반으로 감소</u></b></mark></color> (다른 효과로 증가되는 수치 제외)\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].desc
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Prey_leiheng], [WhenUse], [BattleSense], [Combustion], [Vibration], [DefeatDuel], [Paralysis], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [Prey_leiheng] = 사냥감 / Prey; [WhenUse] = [사용시] / [On Use]; [BattleSense] = 저력 [底力] / Inner Strength [底力]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: Prioritizes targets that have [Prey_leiheng]\n<color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed; this unit does not become Staggered before it uses this Skill</u></b></mark></color>\n[WhenUse] Consume all [BattleSense] Stack on self. If this unit consumed...\n- ... 10+ Stacks, gain Atk Weight +1 for every 10 Stack consumed (max 2)\n- ... 25 Stacks, Final Power +1 for every 4 (sum of [Combustion] and [Vibration] on the main target) (max 5)\n[DefeatDuel] Gain 1 [Paralysis]\n[DefeatDuel] Deal -80% damage; this Skill's damage cannot Stagger the target; <color=#ff6000><mark=#ff000040><b><u>inflict only half the Potency and Count for both [Combustion] and [Vibration] inflicted by this Skill</u></b></mark></color> (unless raised by other effects)\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)\n[EndSkill] Ends this turn
   PL: priorytet: cele z [Prey_leiheng]\n<color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności</u></b></mark></color>\n[WhenUse] zużywa wszystkie Liczniki [BattleSense] jednostki. jeżeli zużyto...\n- ...10+ Liczników, Waga Ataku +1 za każde 10 zużytych Liczników (maks. 2)\n- ...25 Liczników, Końcowa Moc +1 za każde 4 (suma [Combustion] i [Vibration] głównego celu) (maks. 5)\n[DefeatDuel] zyskuje 1 [Paralysis]\n[DefeatDuel] zadaje o 80% mniej obrażeń; obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; <color=#ff6000><mark=#ff000040><b><u>nakłada tylko połowę Siły i Liczników [Combustion] oraz [Vibration] nakładanych tą Umiejętnością</u></b></mark></color> (poza wartościami zwiększonymi przez inne efekty)\n[EndSkill] [FullReload] (1 raz na turę)\n- jeżeli jednostka ma [BulletPropellantSpecial], zamiast tego [ReloadKeepAmmo] (1 raz na turę)\n[EndSkill] kończy tę turę
62. [Umiejętność wroga [501906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność wroga [501906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 전부 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Spend all [BulletPropellant]
   PL: zużywa cały [BulletPropellant]
64. [Umiejętność wroga [501906] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 소모한 [BulletPropellant]만큼 [Combustion] 부여, [Combustion] 횟수 증가, [Vibration] 부여, [Vibration] 횟수 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletPropellant], [Combustion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletPropellant] = 호표탄 / Tigermark Round; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Combustion], [Combustion] Count, [Vibration], and [Vibration] Count by [BulletPropellant] spent
   PL: [OnSucceedAttack] nakłada [Combustion], Licznik [Combustion], [Vibration] i Licznik [Vibration] w wartości zużytego [BulletPropellant]
65. [Umiejętność wroga [501906] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [501906] (ulepszenie 1) — moneta 1, efekt 5 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> [VibrationExplosion] 3회. 대상의 [Vibration] 횟수 3 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501906].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> Trigger [VibrationExplosion] 3 times; then, reduce target's [Vibration] Count by 3
   PL: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> uruchamia [VibrationExplosion] 3 razy, po czym zmniejsza Licznik [Vibration] celu o 3
67. [Umiejętność wroga [501907] (ulepszenie 1) — nazwa] 초절맹호살격난참 [超絕猛虎殺擊亂斬]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].name
   limit: do 80 znaków
   EN: Savage Tigerslayer's Perfected Flurry of Blades [超絕猛虎殺擊亂斬]
   PL: Savage Tigerslayer's Perfected Flurry of Blades [超絕猛虎殺擊亂斬]
68. [Umiejętność wroga [501907] (ulepszenie 1) — opis] [Prey_leiheng]을 보유한 대상을 우선으로 지정\n<color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음</u></b></mark></color>\n[WhenUse] [BattleSense]을 전부 소모. 소모한 수치가\n- 10 이상이면, 10당 공격 가중치 +1 (최대 4)\n- 25 이상이면, 메인 타겟의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 6)\n- 50일 경우, 코인 위력 +1, 피해량 +50%\n[DefeatDuel] [Paralysis] 6 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않으며, <color=#ff6000><mark=#ff000040><b><u>[Combustion] 위력과 횟수, [Vibration] 위력과 횟수 부여량이 절반으로 감소</u></b></mark></color> (다른 효과로 증가되는 수치 제외)\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Prey_leiheng], [WhenUse], [BattleSense], [Combustion], [Vibration], [DefeatDuel], [Paralysis], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [Prey_leiheng] = 사냥감 / Prey; [WhenUse] = [사용시] / [On Use]; [BattleSense] = 저력 [底力] / Inner Strength [底力]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: Prioritizes targets that have [Prey_leiheng]\n<color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed; this unit does not become Staggered before it uses this Skill</u></b></mark></color>\n[WhenUse] Consume all [BattleSense] Stack on self. If this unit consumed...\n- ... 10+ Stacks, gain Atk Weight +1 for every 10 Stack consumed (max 4)\n- ... 25+ Stacks, Final Power +1 for every 4 (sum of [Combustion] and [Vibration] on the main target) (max 6)\n- ... 50 Stacks, Coin Power +1 and deal +50% damage\n[DefeatDuel] Gain 6 [Paralysis]\n[DefeatDuel] Deal -80% damage; this Skill's damage cannot Stagger the target; <color=#ff6000><mark=#ff000040><b><u>inflict only half the Potency and Count for both [Combustion] and [Vibration] inflicted by this Skill</u></b></mark></color> (unless raised by other effects)\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)\n[EndSkill] Ends this turn
   PL: priorytet: cele z [Prey_leiheng]\n<color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności</u></b></mark></color>\n[WhenUse] zużywa wszystkie Liczniki [BattleSense] jednostki. jeżeli zużyto...\n- ...10+ Liczników, Waga Ataku +1 za każde 10 zużytych Liczników (maks. 4)\n- ...25+ Liczników, Końcowa Moc +1 za każde 4 (suma [Combustion] i [Vibration] głównego celu) (maks. 6)\n- ...50 Liczników, Moc Monety +1 i zadaje +50% obrażeń\n[DefeatDuel] zyskuje 6 [Paralysis]\n[DefeatDuel] zadaje o 80% mniej obrażeń; obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu; <color=#ff6000><mark=#ff000040><b><u>nakłada tylko połowę Siły i Liczników [Combustion] oraz [Vibration] nakładanych tą Umiejętnością</u></b></mark></color> (poza wartościami zwiększonymi przez inne efekty)\n[EndSkill] [FullReload] (1 raz na turę)\n- jeżeli jednostka ma [BulletPropellantSpecial], zamiast tego [ReloadKeepAmmo] (1 raz na turę)\n[EndSkill] kończy tę turę
69. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 6 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL: [OnSucceedAttack] nakłada 6 [Combustion]
72. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 6 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +6 [Combustion] Count
   PL: [OnSucceedAttack] nakłada +6 Licznika [Combustion]
75. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 3, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL: [OnSucceedAttack] nakłada 6 [Vibration]
78. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 4, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 6 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +6 [Vibration] Count
   PL: [OnSucceedAttack] nakłada +6 Licznika [Vibration]
81. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 5, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 5, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#4].coindescs[#2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 6, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#5].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 6, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#5].coindescs[#1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [501907] (ulepszenie 1) — moneta 6, efekt 3 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> [VibrationExplosion] 5회. 대상의 [Vibration] 횟수 5 감소
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501907].levelList[level=1].coinlist[#5].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> Trigger [VibrationExplosion] 5 times; then, reduce target's [Vibration] Count by 5
   PL: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> uruchamia [VibrationExplosion] 5 razy, po czym zmniejsza Licznik [Vibration] celu o 5
87. [Umiejętność wroga [501908] (ulepszenie 1) — nazwa] 천퇴성도 장전
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501908].levelList[level=1].name
   limit: do 50 znaków
   EN: Reloading Tiantui Star's Blade
   PL: Reloading Tiantui Star's Blade
88. [Umiejętność wroga [501908] (ulepszenie 1) — opis] [DuelCounter]\n[DefeatDuel] [BulletPropellant] 1 감소\n[EndBattle] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501908].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DefeatDuel], [BulletPropellant], [EndBattle], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BulletPropellant] = 호표탄 / Tigermark Round; [EndBattle] = [턴 종료 시] / [Turn End]; [FullReload] = 재장전 / Reload; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [ReloadKeepAmmo] = 재장전 - 잔탄 유지 / Reload - Tactical
   EN: [DuelCounter]\n[DefeatDuel] Lose 1 [BulletPropellant]\n[EndBattle] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)
   PL: [DuelCounter]\n[DefeatDuel] traci 1 [BulletPropellant]\n[EndBattle] [FullReload] (1 raz na turę)\n- jeżeli jednostka ma [BulletPropellantSpecial], zamiast tego [ReloadKeepAmmo] (1 raz na turę)
89. [Umiejętność wroga [501908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność wroga [501908] (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501908].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność wroga [501908] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501908].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność wroga [501908] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=501908].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Umiejętność wroga [502001] (ulepszenie 1) — nazwa] 맹호표탄 지원
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=502001].levelList[level=1].name
   limit: do 40 znaków
   EN: Savage Tigermark Support
   PL: Savage Tigermark Support
94. [Umiejętność wroga [502001] (ulepszenie 1) — opis] [EndBattle] 뇌횡에게 [BulletPropellantSpecial] 6 부여\n[EndBattle] [DisengageCombat]
   źródło: Skills_Abnormality-BossRaid.json :: dataList[id=502001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle], [BulletPropellantSpecial], [DisengageCombat]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [DisengageCombat] = 전투 이탈 / Escape Battle
   EN: [EndBattle] Give 6 [BulletPropellantSpecial] to Lei Heng\n[EndBattle] [DisengageCombat]
   PL: [EndBattle] nakłada 6 [BulletPropellantSpecial] na Lei Heng\n[EndBattle] [DisengageCombat]

## [cultivation] Wróg / część: Enemies-cultivation
- plik gry: `Enemies-cultivation.json`

95. [[cultivation] Wróg / część [1247] — nazwa] 웨이
   źródło: Enemies-cultivation.json :: dataList[id=1247].name
   limit: do 40 znaków
   EN: Wei
   PL: Wei
96. [[cultivation] Wróg / część [1247] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=1247].desc
   limit: do 120 znaków
   EN: Core
   PL: Core
97. [[cultivation] Wróg / część [1272] — nazwa] 진 - 취수야객
   źródło: Enemies-cultivation.json :: dataList[id=1272].name
   limit: do 60 znaków
   EN: True Night Drifter of the Drunken Palm
   PL: True Night Drifter of the Drunken Palm
98. [[cultivation] Wróg / część [1272] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=1272].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [[cultivation] Wróg / część [90215] — nazwa] 흑수 - 사 : 은격
   źródło: Enemies-cultivation.json :: dataList[id=90215].name
   limit: do 50 znaków
   EN: Heishou Pack - Si : Veilstriker
   PL: Heishou Pack - Si : Veilstriker
100. [[cultivation] Wróg / część [90215] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=90215].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [[cultivation] Wróg / część [90216] — nazwa] 흑수 - 사 : 음격
   źródło: Enemies-cultivation.json :: dataList[id=90216].name
   limit: do 50 znaków
   EN: Heishou Pack - Si : Shadestriker
   PL: Heishou Pack - Si : Shadestriker
102. [[cultivation] Wróg / część [90216] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=90216].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [[cultivation] Wróg / część [91023] — nazwa] 흑수 - 사 : 잠격
   źródło: Enemies-cultivation.json :: dataList[id=91023].name
   limit: do 50 znaków
   EN: Heishou Pack - Si : Depthstriker
   PL: Heishou Pack - Si : Depthstriker
104. [[cultivation] Wróg / część [91023] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=91023].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [[cultivation] Wróg / część [1286] — nazwa] 취수야객
   źródło: Enemies-cultivation.json :: dataList[id=1286].name
   limit: do 50 znaków
   EN: Night Drifter of the Drunken Palm
   PL: Night Drifter of the Drunken Palm
106. [[cultivation] Wróg / część [1286] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=1286].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [[cultivation] Wróg / część [1287] — nazwa] 싱클레어
   źródło: Enemies-cultivation.json :: dataList[id=1287].name
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair
108. [[cultivation] Wróg / część [1287] — opis] 본체
   źródło: Enemies-cultivation.json :: dataList[id=1287].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [cultivation] Umiejętności wrogów / Anomalii — Skills_Abnormality-cultivation
- grupa rozdziału/trybu: `cultivation` · plik: `Skills_Abnormality-cultivation.json`

109. [Umiejętność wroga [124701] (ulepszenie 1) — nazwa] 철마쇄(鐵馬碎)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124701].levelList[level=1].name
   limit: do 40 znaków
   EN: Ironsteed Trample
   PL: Ironsteed Trample
110. [Umiejętność wroga [124701] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Vibration]의 합이 6 이상이라면, 기본 위력 +3\n[DefeatDuel] 대상의 [Vibration] 위력 2 감소
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124701].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Vibration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ ([Burst] + [Vibration]), Base Power +3\n[DefeatDuel] Reduce target's [Vibration] Potency by 2
   PL: [WhenUse] jeżeli cel ma 6+ (suma [Burst] i [Vibration]), Moc Bazowa +3\n[DefeatDuel] zmniejsza Siłę [Vibration] celu o 2
111. [Umiejętność wroga [124701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] nakłada 1 [Burst]
112. [Umiejętność wroga [124701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] nakłada +1 Licznika [Burst]
113. [Umiejętność wroga [124702] (ulepszenie 1) — nazwa] 파도쇄(破蹈碎)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124702].levelList[level=1].name
   limit: do 40 znaków
   EN: Rupturing Trample
   PL: Rupturing Trample
114. [Umiejętność wroga [124702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Vibration]의 합 4 당, 기본 위력 +2 (최대 4)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Base Power +2 for every 4 ([Burst] + [Vibration]) on target (max 4)
   PL: [WhenUse] Moc Bazowa +2 za każde 4 (suma [Burst] i [Vibration] celu) (maks. 4)
115. [Umiejętność wroga [124702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada +3 Licznika [Burst]
116. [Umiejętność wroga [124702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Umiejętność wroga [124702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] nakłada 2 [Burst]
118. [Umiejętność wroga [124702] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124702].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność wroga [124703] (ulepszenie 1) — nazwa] 마진분쇄(馬陣粉碎)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124703].levelList[level=1].name
   limit: do 40 znaków
   EN: Line-Crushing Cavalry Charge
   PL: Line-Crushing Cavalry Charge
120. [Umiejętność wroga [124703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Vibration]의 합이 6 이상이라면, 기본 위력 +2\n[WhenUse] 자신의 정신력이 -30 이하라면 코인이 뒷면으로 고정됨\n[DefeatDuel] 대상의 [Vibration] 위력 2 감소
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124703].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Vibration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ ([Burst] + [Vibration]), Base Power +2\n[WhenUse] At -30 or lower SP, this unit's Coins always flip Tails\n[DefeatDuel] Reduce target's [Vibration] Potency by 2
   PL: [WhenUse] jeżeli cel ma 6+ (suma [Burst] i [Vibration]), Moc Bazowa +2\n[WhenUse] przy SP równym -30 lub niższym wszystkie Monety tej jednostki zawsze wypadają jako Rewers\n[DefeatDuel] zmniejsza Siłę [Vibration] celu o 2
121. [Umiejętność wroga [124703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 8 부여, [Burst] 횟수 5 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 8 [Burst] and +5 [Burst] Count
   PL: [OnSucceedAttack] nakłada 8 [Burst] i zwiększa Licznik [Burst] o 5
122. [Umiejętność wroga [124704] (ulepszenie 1) — nazwa] 격쇄참(擊碎斬)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].name
   limit: do 40 znaków
   EN: Trample and Decapitate
   PL: Trample and Decapitate
123. [Umiejętność wroga [124704] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Vibration]의 합 4 당, 기본 위력 +2 (최대 4)\n- 대상의 [Burst]과 [Vibration]의 합이 15 이상이라면 빼기 코인 위력 +1
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Base Power +2 for every 4 ([Burst] + [Vibration]) on target (max 4)\n- At 15+ ([Burst] + [Vibration]) on target, Minus Coin Power +1
   PL: [WhenUse] Moc Bazowa +2 za każde 4 (suma [Burst] i [Vibration] celu) (maks. 4)\n- jeżeli cel ma 15+ (suma [Burst] i [Vibration]), Moc Monet Minus +1
124. [Umiejętność wroga [124704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [124704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] nakłada +1 Licznika [Vibration]
126. [Umiejętność wroga [124704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada +2 Licznika [Burst]
127. [Umiejętność wroga [124704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność wroga [124704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1.
129. [Umiejętność wroga [124705] (ulepszenie 1) — nazwa] 더러운 뱀들이… 뭉개주지…
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].name
   limit: do 60 znaków
   EN: Filthy snakes... I'll crush you all...
   PL: Filthy snakes... I'll crush you all...
130. [Umiejętność wroga [124705] (ulepszenie 1) — opis] [WhenUse] 메인 타겟 대상의 [Burst]과 [Vibration]의 합 4 당, 기본 위력 +2 (최대 4)\n[DefeatDuel] 기본 위력 8 감소\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Vibration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +2 for every 4 ([Burst] + [Vibration]) on the main target (max 4)\n[DefeatDuel] Base Power -8\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Bazowa +2 za każde 4 (suma [Burst] i [Vibration] głównego celu) (maks. 4)\n[DefeatDuel] Moc Bazowa -8\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
131. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Burst]
133. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Vibration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Vibration]
135. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [124705] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 서브 타겟에게 다음 턴에 [SweptAwayWei] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124705].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SweptAwayWei]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SweptAwayWei] = 휩쓸림 / Galestruck
   EN: [OnSucceedAttack] Inflict [SweptAwayWei] against sub-targets next turn
   PL: [OnSucceedAttack] nakłada [SweptAwayWei] celom drugorzędnym w następnej turze
140. [Umiejętność wroga [124706] (ulepszenie 1) — nazwa] 분마천진(奔馬穿陣)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].name
   limit: do 40 znaków
   EN: Swiftsteed Linebreaker
   PL: Swiftsteed Linebreaker
141. [Umiejętność wroga [124706] (ulepszenie 1) — opis] [WhenUse] 메인 타겟 대상의 [Burst]과 [Vibration]의 합 4 당, 기본 위력 +2 (최대 6)\n[DefeatDuel] 기본 위력 5 감소\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Vibration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +2 for every 4 ([Burst] + [Vibration]) on the main target (max 6)\n[DefeatDuel] Base Power -5\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Bazowa +2 za każde 4 (suma [Burst] i [Vibration] głównego celu) (maks. 6)\n[DefeatDuel] Moc Bazowa -5\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
142. [Umiejętność wroga [124706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [124706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 메인 타겟이라면 [Vibration] 5 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If it's the main target, inflict +5 [Vibration]
   PL: [OnSucceedAttack] jeżeli to główny cel, nakłada +5 [Vibration]
144. [Umiejętność wroga [124706] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 서브 타겟 1명에게 [Vibration] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Vibration] against 1 sub-target
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Vibration] 1 celowi drugorzędnemu
145. [Umiejętność wroga [124706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [124706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność wroga [124706] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 서브 타겟에게 다음 턴에 [SweptAwayWei] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124706].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [SweptAwayWei]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [SweptAwayWei] = 휩쓸림 / Galestruck
   EN: [UnBrokenCoinOnSucceedAttack] Inflict [SweptAwayWei] against sub-targets next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada [SweptAwayWei] celom drugorzędnym w następnej turze
148. [Umiejętność wroga [124707] (ulepszenie 1) — nazwa] 이 앞을 지나갈 순 없다…!
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].name
   limit: do 40 znaków
   EN: You Shall Not Pass...!
   PL: You Shall Not Pass...!
149. [Umiejętność wroga [124707] (ulepszenie 1) — opis] [Vibration] 위력이 가장 적은 적을 타겟팅 함\n[WhenUse] 대상에게 [Vibration]이 없으면, 기본 위력 -5\n[BeforeAttack] 대상에게 [Vibration]이 없으면, 피해량 90% 감소\n[DefeatDuel] 기본 위력 4 감소\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [WhenUse], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes the target with the least [Vibration] Potency\n[WhenUse] If target does not have [Vibration], Base Power -5\n[BeforeAttack] If target does not have [Vibration], deal -90% damage\n[DefeatDuel] Base Power -4\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cel z najniższą Siłą [Vibration]\n[WhenUse] jeżeli cel nie ma [Vibration], Moc Bazowa -5\n[BeforeAttack] jeżeli cel nie ma [Vibration], zadaje o 90% mniej obrażeń\n[DefeatDuel] Moc Bazowa -4\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
150. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Umiejętność wroga [124707] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124707].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność wroga [124708] (ulepszenie 1) — nazwa] 광마열공충(狂馬裂空衝)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].name
   limit: do 40 znaków
   EN: Mad Steed's Voidrender
   PL: Mad Steed's Voidrender
159. [Umiejętność wroga [124708] (ulepszenie 1) — opis] 자신의 잃은 HP 1% 당 피해량 +1% (최대 80%)\n[BeforeAttack] 자신의 체력이 50% 이하라면 가중치 추가로 2 증가\n[BeforeAttack] 자신에게 [LegStrengthHorse]가 없다면, 이 스킬의 피해량 + 120%, 다음 턴에 [Vulnerable] 2를 얻음\n[DefeatDuel] 기본 위력 12 감소\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [LegStrengthHorse], [Vulnerable], [DefeatDuel]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [LegStrengthHorse] = 각력【오】 / Strider【Wu】; [Vulnerable] = 취약 / Fragile; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +1% damage for every 1% missing HP on self (max 80%)\n[BeforeAttack] At 50% or less HP, gain +2 more Atk Weight\n[BeforeAttack] If this unit does not have [LegStrengthHorse], this Skill deals +120% damage; then, gain 2 [Vulnerable] next turn\n[DefeatDuel] Base Power -12\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: zadaje +1% obrażeń za każde 1% brakującego HP jednostki (maks. 80%)\n[BeforeAttack] przy HP równym 50% lub mniej dodatkowo Waga Ataku +2\n[BeforeAttack] jeżeli jednostka nie ma [LegStrengthHorse], ta Umiejętność zadaje +120% obrażeń, a następnie zyskuje 2 [Vulnerable] w następnej turze\n[DefeatDuel] Moc Bazowa -12\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
160. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] nakłada 5 [Burst]
162. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 5 부여, [Burst] 횟수 5 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Burst] and +5 [Burst] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [Burst] i zwiększa Licznik [Burst] o 5
163. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] nakłada 5 [Vibration]
165. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 5 부여, [Vibration] 횟수 5 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Vibration] and +5 [Vibration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [Vibration] i zwiększa Licznik [Vibration] o 5
166. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Umiejętność wroga [124708] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=124708].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1.
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1.
171. [Umiejętność wroga [127201] (ulepszenie 1) — nazwa] 전선참(前旋斬)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127201].levelList[level=1].name
   limit: do 40 znaków
   EN: Frontal Swirl (前旋斬)
   PL: Frontal Swirl (前旋斬)
172. [Umiejętność wroga [127201] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)\n[WhenUse] [SipOfAlcoholJin] 1 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127201].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SipOfAlcoholJin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞)
   EN: [WhenUse] Coin Power +1 for every 5 [Laceration] on target (max 2)\n[WhenUse] Gain 1 [SipOfAlcoholJin]
   PL: [WhenUse] Moc Monety +1 za każde 5 [Laceration] celu (maks. 2)\n[WhenUse] zyskuje 1 [SipOfAlcoholJin]
173. [Umiejętność wroga [127201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
174. [Umiejętność wroga [127201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada +2 Licznika [Laceration]
175. [Umiejętność wroga [127202] (ulepszenie 1) — nazwa] 인도주(咽道酒)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127202].levelList[level=1].name
   limit: do 60 znaków
   EN: Way of the Open-throat Chugging (咽道酒)
   PL: Way of the Open-throat Chugging (咽道酒)
176. [Umiejętność wroga [127202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)\n[WhenUse] [SipOfAlcoholJin] 1 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127202].levelList[level=1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [127202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada +1 Licznika [Laceration]
178. [Umiejętność wroga [127202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
179. [Umiejętność wroga [127202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 5+ [Laceration], inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], nakłada +2 Licznika [Laceration]
180. [Umiejętność wroga [127203] (ulepszenie 1) — nazwa] 낙주(落酒)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].name
   limit: do 40 znaków
   EN: Waterfall (落酒)
   PL: Waterfall (落酒)
181. [Umiejętność wroga [127203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [DrunkBlood] 당, 기본 위력 +1 (최대 2)\n[WinDuel] [SipOfAlcoholJin] 1 얻음\n[DefeatDuel] [SipOfAlcoholJin] 2 감소
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DrunkBlood], [WinDuel], [SipOfAlcoholJin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DrunkBlood] = 혈주(血注) / Bloodpour (血注); [WinDuel] = [합 승리시] / [Clash Win]; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞); [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] Base Power +1 for every [DrunkBlood] Count on target (max 2)\n[WinDuel] Gain 1 [SipOfAlcoholJin]\n[DefeatDuel] Lose 2 [SipOfAlcoholJin]
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1\n[WhenUse] Moc Bazowa +1 za każdy Licznik [DrunkBlood] celu (maks. 2)\n[WinDuel] zyskuje 1 [SipOfAlcoholJin]\n[DefeatDuel] traci 2 [SipOfAlcoholJin]
182. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [127203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +3 Licznika [Laceration]
189. [Umiejętność wroga [127204] (ulepszenie 1) — nazwa] 취(取)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127204].levelList[level=1].name
   limit: do 40 znaków
   EN: Drunklaim (取)
   PL: Drunklaim (取)
190. [Umiejętność wroga [127204] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5 당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [DrunkBlood] 당, 기본 위력 +1 (최대 2)\n[WhenUse] [SipOfAlcoholJin]이 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127204].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DrunkBlood], [SipOfAlcoholJin], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DrunkBlood] = 혈주(血注) / Bloodpour (血注); [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞); [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 5 [Laceration] on target (max 2)\n[WhenUse] Base Power +1 for every [DrunkBlood] on target (max 2)\n[WhenUse] At 3+ [SipOfAlcoholJin], convert all Coins to [SuperCoin]s\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Monety +1 za każde 5 [Laceration] celu (maks. 2)\n[WhenUse] Moc Bazowa +1 za każde [DrunkBlood] celu (maks. 2)\n[WhenUse] przy 3+ [SipOfAlcoholJin] wszystkie Monety zmieniają się w [SuperCoin]y\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
191. [Umiejętność wroga [127204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [127204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [127204] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 20%)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +1% damage for every ([Laceration] + [Laceration] Count) on the target (max 20%)
   PL: zadaje +1% obrażeń za każde ([Laceration] + Licznik [Laceration]) celu (maks. 20%)
194. [Umiejętność wroga [127204] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [SipOfAlcoholJin]이 3 이상이면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127204].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SipOfAlcoholJin]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞)
   EN: [OnSucceedAttack] If this unit has 3+ [SipOfAlcoholJin], reuse this Skill once (once per Skill)
   PL: [OnSucceedAttack] jeżeli jednostka ma 3+ [SipOfAlcoholJin], używa tej Umiejętności ponownie 1 raz (1 raz na Umiejętność)
195. [Umiejętność wroga [127205] (ulepszenie 1) — nazwa] 진진종참(眞鎭終斬)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127205].levelList[level=1].name
   limit: do 50 znaków
   EN: True Decapitation Deathblow (眞鎭終斬)
   PL: True Decapitation Deathblow (眞鎭終斬)
196. [Umiejętność wroga [127205] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 6 당, 코인 위력 +5 (최대 10)\n[WhenUse] 메인 대상에게 [DrunkBlood]가 있으면, 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127205].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DrunkBlood], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DrunkBlood] = 혈주(血注) / Bloodpour (血注); [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +5 for every 6 [Laceration] on target (max 10)\n[WhenUse] If target has [DrunkBlood], convert all Coins to [SuperCoin]s\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Monety +5 za każde 6 [Laceration] celu (maks. 10)\n[WhenUse] jeżeli główny cel ma [DrunkBlood], wszystkie Monety zmieniają się w [SuperCoin]y\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
197. [Umiejętność wroga [127205] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 100%)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +1% damage for every ([Laceration] + [Laceration] Count) on the target (max 100%)
   PL: zadaje +1% obrażeń za każde ([Laceration] + Licznik [Laceration]) celu (maks. 100%)
198. [Umiejętność wroga [127205] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상의 [DrunkBlood] 당 피해량 +10% (최대 50%)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DrunkBlood]
   znaczenie tagów: [DrunkBlood] = 혈주(血注) / Bloodpour (血注)
   EN: Deal +10% damage for every [DrunkBlood] on target (max 50%)
   PL: zadaje +10% obrażeń za każde [DrunkBlood] celu (maks. 50%)
199. [Umiejętność wroga [127205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [SipOfAlcoholJin] 2 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SipOfAlcoholJin]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞)
   EN: [OnSucceedAttack] Gain 2 [SipOfAlcoholJin]
   PL: [OnSucceedAttack] zyskuje 2 [SipOfAlcoholJin]
200. [Umiejętność wroga [127205] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상의 ([DrunkBlood] 수치 x 5)만큼 색욕 피해를 줌 (최대 25)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127205].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DrunkBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DrunkBlood] = 혈주(血注) / Bloodpour (血注)
   EN: [OnSucceedAttack] Deal ([DrunkBlood] on target x 5) Lust damage (max 25)
   PL: [OnSucceedAttack] zadaje ([DrunkBlood] celu x 5) obrażeń Żądzy (maks. 25)
201. [Umiejętność wroga [127206] (ulepszenie 1) — nazwa] 취고(醉靠)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127206].levelList[level=1].name
   limit: do 40 znaków
   EN: Intoxicated Leaning (醉靠)
   PL: Intoxicated Leaning (醉靠)
202. [Umiejętność wroga [127206] (ulepszenie 1) — opis] [WhenUse] 자신의 [SipOfAlcoholJin]당 보호막 10 얻음 (최대 50)\n[WhenUse] 대상에게 [DrunkBlood] 가 있으면 [Laceration] 5 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127206].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SipOfAlcoholJin], [DrunkBlood], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞); [DrunkBlood] = 혈주(血注) / Bloodpour (血注); [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain 10 Shield for every [SipOfAlcoholJin] on self (max 50)\n[WhenUse] If target has [DrunkBlood], inflict 5 [Laceration]
   PL: [WhenUse] zyskuje 10 Tarczy za każde [SipOfAlcoholJin] jednostki (maks. 50)\n[WhenUse] jeżeli cel ma [DrunkBlood], nakłada 5 [Laceration]
203. [Umiejętność wroga [127207] (ulepszenie 1) — nazwa] 취회공(醉回攻)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127207].levelList[level=1].name
   limit: do 50 znaków
   EN: Drunken Returning Strike (醉回攻)
   PL: Drunken Returning Strike (醉回攻)
204. [Umiejętność wroga [127207] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [SipOfAlcoholJin]당 피해량 +20% (최대 100%)\n[WhenUse] 대상에게 [DrunkBlood]가 있으면, 피해량 +50%
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127207].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [SipOfAlcoholJin], [DrunkBlood]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞); [DrunkBlood] = 혈주(血注) / Bloodpour (血注)
   EN: [DuelCounter]\n[WhenUse] Deal +20% damage for every [SipOfAlcoholJin] on self (max 100%)\n[WhenUse] If target has [DrunkBlood], deal +50% damage
   PL: [DuelCounter]\n[WhenUse] zadaje +20% obrażeń za każde [SipOfAlcoholJin] jednostki (maks. 100%)\n[WhenUse] jeżeli cel ma [DrunkBlood], zadaje +50% obrażeń
205. [Umiejętność wroga [127207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashResistDown] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 2 [SlashResistDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [SlashResistDown] w następnej turze
206. [Umiejętność wroga [127207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 ([DrunkBlood] 수치 x 5)만큼 색욕 피해를 줌 (최대 25)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [127208] (ulepszenie 1) — nazwa] 진 - 진진종참(眞-眞鎭終斬)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].name
   limit: do 70 znaków
   EN: Ultimate True Decapitation Deathblow (眞-眞鎭終斬)
   PL: Ultimate True Decapitation Deathblow (眞-眞鎭終斬)
208. [Umiejętność wroga [127208] (ulepszenie 1) — opis] 가시춘을 타겟으로 함\n[CantChangeTarget]\n[WhenUse] 자신의 속도가 대상보다 높으면 코인 위력 +1\n[WhenUse] 자신의 [SipOfAlcoholJin] 당, 다음 턴에 [AttackUp] 1, [Agility] 1 획득 (최대 3)\n[WinDuel] 공격 가중치 7 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [SipOfAlcoholJin], [AttackUp], [Agility], [WinDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞); [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Prioritizes Jia Xichun\n[CantChangeTarget]\n[WhenUse] If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain 1 [AttackUp] and 1 [Agility] next turn for every [SipOfAlcoholJin] on self (max 3)\n[WinDuel] Gain +7 Atk Weight
   PL: priorytet: Jia Xichun\n[CantChangeTarget]\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, Moc Monety +1\n[WhenUse] zyskuje 1 [AttackUp] i 1 [Agility] w następnej turze za każde [SipOfAlcoholJin] jednostki (maks. 3)\n[WinDuel] Waga Ataku +7
209. [Umiejętność wroga [127208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [127208] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 100%)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 197 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [127208] (ulepszenie 1) — moneta 1, efekt 3 — opis] 대상의 [DrunkBlood] 당 피해량 +10% (최대 50%)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [127208] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Laceration]
213. [Umiejętność wroga [127208] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 ([DrunkBlood] 수치 x 10)만큼 색욕 피해를 줌 (최대 50)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127208].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [DrunkBlood]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [DrunkBlood] = 혈주(血注) / Bloodpour (血注)
   EN: [UnBrokenCoinOnSucceedAttack] Deal ([DrunkBlood] on target x 10) Lust damage (max 50)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje ([DrunkBlood] celu x 10) obrażeń Żądzy (maks. 50)
214. [Umiejętność wroga [127209] (ulepszenie 1) — nazwa] 낙취참(落醉斬)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127209].levelList[level=1].name
   limit: do 50 znaków
   EN: Drunken Decapitation Bladefall (落醉斬)
   PL: Drunken Decapitation Bladefall (落醉斬)
215. [Umiejętność wroga [127209] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 5 당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 속도가 대상보다 높으면 코인 위력 +1
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127209].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Base Power +1 for every 5 [Breath] on self (max 2)\n[WhenUse] If this unit's Speed is faster than the target's, Coin Power +1
   PL: [WhenUse] Moc Bazowa +1 za każde 5 [Breath] jednostki (maks. 2)\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, Moc Monety +1
216. [Umiejętność wroga [127209] (ulepszenie 1) — moneta 1, efekt 1 — opis] 진 - 진진종참(眞-眞鎭終斬)의 피해량 + 20%
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Ultimate True Decapitation Deathblow (眞-眞鎭終斬) deals +20% damage
   PL: Ultimate True Decapitation Deathblow (眞-眞鎭終斬) zadaje +20% obrażeń
217. [Umiejętność wroga [127209] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 이 코인 재사용 (최대 5회)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127209].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin (5 times max)
   PL: [CriticalOnSucceedAttack] używa Monety ponownie (maks. 5 razy)
218. [Umiejętność wroga [127210] (ulepszenie 1) — nazwa] 취영보(醉影步)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127210].levelList[level=1].name
   limit: do 40 znaków
   EN: Drunken Shadowwalking (醉影步)
   PL: Drunken Shadowwalking (醉影步)
219. [Umiejętność wroga [127210] (ulepszenie 1) — opis] [WhenUse] 현재 생존한 아군 2명 당 기본 위력 +6 (최대 12)\n[OnSucceedEvade] [Breath] 3 얻음\n[EndBattle] [Breath] 횟수 2 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=127210].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OnSucceedEvade], [Breath], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Base Power +6 for every 2 surviving ally (max 12)\n[OnSucceedEvade] Gain 3 [Breath]\n[EndBattle] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Bazowa +6 za każde 2 żyjące sojuszniki (maks. 12)\n[OnSucceedEvade] zyskuje 3 [Breath]\n[EndBattle] zyskuje +2 Licznika [Breath]
220. [Umiejętność wroga [9102506] (ulepszenie 1) — nazwa] 진진종참
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102506].levelList[level=1].name
   limit: do 40 znaków
   EN: True Decapitation Deathblow
   PL: True Decapitation Deathblow
221. [Umiejętność wroga [9102506] (ulepszenie 1) — opis] [StartBattle] 이 스킬이 종료되기 전까지 체력이 1 이하가 되지 않음.\n[WhenUse] [AttackUp] 10 얻음\n[WhenUse] [Enhancement] 5 얻음\n[WhenUse] [AttackDmgUp] 10 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102506].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [AttackUp], [Enhancement], [AttackDmgUp], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] HP does not drop below 1 before this Skill ends.\n[WhenUse] Gain 10 [AttackUp]\n[WhenUse] Gain 5 [Enhancement]\n[WhenUse] Gain 10 [AttackDmgUp]\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [StartBattle] HP nie spada poniżej 1 do zakończenia tej Umiejętności.\n[WhenUse] zyskuje 10 [AttackUp]\n[WhenUse] zyskuje 5 [Enhancement]\n[WhenUse] zyskuje 10 [AttackDmgUp]\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
222. [Umiejętność wroga [9102506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [9102506] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상의 ([Laceration] + [Laceration] 횟수)당 피해량 +1% (최대 100%)
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 197 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność wroga [9102506] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [SipOfAlcohol] 5 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102506].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SipOfAlcohol]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SipOfAlcohol] = 한 모금 / Swig
   EN: [OnSucceedAttack] Gain 5 [SipOfAlcohol]
   PL: [OnSucceedAttack] zyskuje 5 [SipOfAlcohol]
225. [Umiejętność wroga [9102601] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102601].levelList[level=1].name
   limit: do 40 znaków
   EN: Downward Slam
   PL: Downward Slam
226. [Umiejętność wroga [9102601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [9102602] (ulepszenie 1) — nazwa] 연속 휘두르기
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102602].levelList[level=1].name
   limit: do 40 znaków
   EN: Stick Combo
   PL: Stick Combo
228. [Umiejętność wroga [9102602] (ulepszenie 1) — opis] [WinDuel] 피해량 +30%
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Deal +30% damage
   PL: [WinDuel] zadaje +30% obrażeń
229. [Umiejętność wroga [9102603] (ulepszenie 1) — nazwa] 세차게 휘두르기
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102603].levelList[level=1].name
   limit: do 40 znaków
   EN: Powerful Swing
   PL: Powerful Swing
230. [Umiejętność wroga [9102603] (ulepszenie 1) — opis] [WinDuel] [Enhancement] 1 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Enhancement]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WinDuel] Gain 1 [Enhancement]
   PL: [WinDuel] zyskuje 1 [Enhancement]
231. [Umiejętność wroga [9102603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL: [OnSucceedAttackHead] nakłada 1 [Burst]
232. [Umiejętność wroga [9102603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [9102603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [9102604] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102604].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL: Counter
235. [Umiejętność wroga [9102605] (ulepszenie 1) — nazwa] 성장
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].name
   limit: do 40 znaków
   EN: Growth
   PL: Growth
236. [Umiejętność wroga [9102605] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
237. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Burst] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +2 Licznika [Burst]
239. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Burst]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Burst]
241. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Burst] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +3 Licznika [Burst]
243. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 피해량 +20%
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal +20% damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje +20% obrażeń
245. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność wroga [9102605] (ulepszenie 1) — moneta 5, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 피해량 +50%
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=9102605].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal +50% damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje +50% obrażeń
247. [Umiejętność wroga [115905] (ulepszenie 1) — nazwa] 부령술(符靈術) - 사기 폭주
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].name
   limit: do 50 znaków
   EN: Spirit Talisman School - Vilerage
   PL: Spirit Talisman School - Vilerage
248. [Umiejętność wroga [115905] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 4당, 최종 위력 +1 (최대 4)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해, 효과로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 4 [Burst] on target (max 4)\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Końcowa Moc +1 za każde 4 [Burst] celu (maks. 4)\n[DefeatDuel] zadaje o 50% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
249. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [OnSucceedAttack] Inflict 10 [OminousTalisman]
   PL: [OnSucceedAttack] nakłada 10 [OminousTalisman]
252. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [OminousTalisman] 10 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [115905] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [OminousTalisman] 전부 소모
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115905].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [OminousTalisman]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [OminousTalisman] = 불길한 부적 / Omen Talisman
   EN: [UnBrokenCoinOnSucceedAttack] Remove all [OminousTalisman] on target
   PL: [UnBrokenCoinOnSucceedAttack] usuwa cały [OminousTalisman] celu
257. [Umiejętność wroga [115706] (ulepszenie 1) — nazwa] 이야..
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115706].levelList[level=1].name
   limit: do 40 znaków
   EN: Oh, damn...
   PL: Oh, damn...
258. [Umiejętność wroga [115706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [115706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
260. [Umiejętność wroga [115707] (ulepszenie 1) — nazwa] 이런 병정 놀이 같은..
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115707].levelList[level=1].name
   limit: do 50 znaków
   EN: What is this foolish pretend-fight?
   PL: What is this foolish pretend-fight?
261. [Umiejętność wroga [115707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
262. [Umiejętność wroga [115708] (ulepszenie 1) — nazwa] ...
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].name
   limit: do 40 znaków
   EN: ...
   PL: ...
263. [Umiejętność wroga [115708] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)\n[DefeatDuel] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] If target has 3+ types of negative effects, Base Power +1\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)\n[DefeatDuel] Gain 1 [Vulnerable]
   PL: [WhenUse] jeżeli cel ma 3+ rodzaje negatywnych efektów, Moc Bazowa +1\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)\n[DefeatDuel] zyskuje 1 [Vulnerable]
264. [Umiejętność wroga [115708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność wroga [115708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [115708] (ulepszenie 1) — moneta 1, efekt 3 — opis] 정신력 5 피해
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   EN: Deal 5 SP damage
   PL: zadaje 5 obrażeń SP
267. [Umiejętność wroga [115708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [115708] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [115708] (ulepszenie 1) — moneta 2, efekt 3 — opis] 정신력 5 피해
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115708].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [115709] (ulepszenie 1) — nazwa] 애들 장난하나?
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115709].levelList[level=1].name
   limit: do 40 znaków
   EN: What's this Child's Play?
   PL: What's this Child's Play?
271. [Umiejętność wroga [115709] (ulepszenie 1) — opis] [WhenUse] 정신력 15 회복\n[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115709].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 15 SP\n[WhenUse] If target has 3+ types of negative effects, Base Power +1
   PL: [WhenUse] przywraca 15 SP\n[WhenUse] jeżeli cel ma 3+ rodzaje negatywnych efektów, Moc Bazowa +1
272. [Umiejętność wroga [115709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [115709] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-cultivation.json :: dataList[id=115709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [cultivation] Umiejętności wrogów / Anomalii — Skills_Enemy-cultivation
- grupa rozdziału/trybu: `cultivation` · plik: `Skills_Enemy-cultivation.json`

274. [Umiejętność wroga [9021501] (ulepszenie 1) — nazwa] 신장수(伸長手)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021501].levelList[level=1].name
   limit: do 40 znaków
   EN: Elongating Palm
   PL: Elongating Palm
275. [Umiejętność wroga [9021501] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021501].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on target) (max 2)\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monety +1 za każde 10 (suma [Breath] jednostki i [Burst] celu) (maks. 2)\n[WhenUse] nakłada +2 Licznika [Breath]
276. [Umiejętność wroga [9021501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL: [OnSucceedAttack] zyskuje 4 [Breath]
277. [Umiejętność wroga [9021501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [BurstPoison], inflict +2 [Burst] Count
   PL: [OnSucceedAttack] jeżeli cel ma [BurstPoison], nakłada +2 Licznika [Burst]
278. [Umiejętność wroga [9021502] (ulepszenie 1) — nazwa] 사관완(蛇貫腕)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021502].levelList[level=1].name
   limit: do 40 znaków
   EN: Puncturing Serpent Arm
   PL: Puncturing Serpent Arm
279. [Umiejętność wroga [9021502] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 8 당 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 8 ([Breath] on self + [Burst] on target) (max 3)
   PL: [WhenUse] Moc Monety +1 za każde 8 (suma [Breath] jednostki i [Burst] celu) (maks. 3)
280. [Umiejętność wroga [9021502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [9021502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność wroga [9021502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 2 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [BurstPoison], inflict 2 [Burst]
   PL: [OnSucceedAttack] jeżeli cel ma [BurstPoison], nakłada 2 [Burst]
283. [Umiejętność wroga [9021503] (ulepszenie 1) — nazwa] 은격관사(隱擊貫蛇)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021503].levelList[level=1].name
   limit: do 40 znaków
   EN: Serpent's Concealed Puncture
   PL: Serpent's Concealed Puncture
284. [Umiejętność wroga [9021503] (ulepszenie 1) — opis] 자신에게 [SnakeStance], 대상에게 [BurstPoison]이 있다면 합 불가 스킬이 됨\n자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 4 당 코인 위력 +1 (최대 10)\n[WinDuel] [Burst] 횟수 2, 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021503].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [SnakeStance], [BurstPoison], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm; [BurstPoison] = 주살【독】 / Deathrite【Venom】; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit has [SnakeStance] and target has [BurstPoison], this Skill becomes an Unclashable Skill\nCoin Power +1 for every 4 ([Breath] on self + [Burst] on target) (max 10)\n[WinDuel] Inflict +2 [Burst] Count and gain +2 [Breath] Count
   PL: jeżeli jednostka ma [SnakeStance], a cel [BurstPoison], Umiejętność staje się Umiejętnością bez Starcia\nMoc Monety +1 za każde 4 (suma [Breath] jednostki i [Burst] celu) (maks. 10)\n[WinDuel] nakłada +2 Licznika [Burst] i zyskuje +2 Licznika [Breath]
285. [Umiejętność wroga [9021503] (ulepszenie 1) — moneta 1, efekt 1 — opis] 자신의 [SnakeStance]당, 피해량 +25% (최대 50%)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SnakeStance]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm
   EN: Deal +25% damage for every [SnakeStance] on self (max 50%)
   PL: zadaje +25% obrażeń za każde [SnakeStance] jednostki (maks. 50%)
286. [Umiejętność wroga [9021503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [SnakeStance]당 [BurstPoison] 3 소모 (턴 당 최대 5)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SnakeStance], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SnakeStance] = 사완 / Serpent Arm; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Consume 3 [BurstPoison] for every [SnakeStance] on self (max 5 per turn)
   PL: [OnSucceedAttack] zużywa 3 [BurstPoison] za każde [SnakeStance] jednostki (maks. 5 na turę)
287. [Umiejętność wroga [9021503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 8 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 8 [Burst]
   PL: [OnSucceedAttack] nakłada 8 [Burst]
288. [Umiejętność wroga [9021503] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [BurstPoison] 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021503].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Inflict [BurstPoison] next turn
   PL: [OnSucceedAttack] nakłada [BurstPoison] w następnej turze
289. [Umiejętność wroga [9021504] (ulepszenie 1) — nazwa] 기회를 보지
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021504].levelList[level=1].name
   limit: do 40 znaków
   EN: Eyeing for a Chance
   PL: Eyeing for a Chance
290. [Umiejętność wroga [9021504] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] [SnakeStance] 3 얻음 (스킬당 1회)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021504].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Burst], [SnakeStance]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [SnakeStance] = 사완 / Serpent Arm
   EN: [CanDuelGuard]\n[WhenUse] Coin Power +1 for every 4 [Burst] on target (max 2)\n[WhenUse] Gain 3 [SnakeStance] (once per Skill)
   PL: [CanDuelGuard]\n[WhenUse] Moc Monety +1 za każde 4 [Burst] celu (maks. 2)\n[WhenUse] zyskuje 3 [SnakeStance] (1 raz na Umiejętność)
291. [Umiejętność wroga [9021504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Umiejętność wroga [9021601] (ulepszenie 1) — nazwa] 신장완(伸長腕)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021601].levelList[level=1].name
   limit: do 40 znaków
   EN: Elongating Arm
   PL: Elongating Arm
293. [Umiejętność wroga [9021601] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021601].levelList[level=1].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [9021601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Umiejętność wroga [9021601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [9021602] (ulepszenie 1) — nazwa] 사감완(蛇噛腕)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021602].levelList[level=1].name
   limit: do 40 znaków
   EN: Gnawing Serpent Arm
   PL: Gnawing Serpent Arm
297. [Umiejętność wroga [9021602] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 8 당 코인 위력 +1 (최대 3)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021602].levelList[level=1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [9021602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [9021602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność wroga [9021602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 1 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [BurstPoison], inflict +1 [Burst] Count
   PL: [OnSucceedAttack] jeżeli cel ma [BurstPoison], nakłada +1 Licznika [Burst]
301. [Umiejętność wroga [9021603] (ulepszenie 1) — nazwa] 음격관사(陰擊貫蛇)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].name
   limit: do 40 znaków
   EN: Serpent's Shadowed Puncture
   PL: Serpent's Shadowed Puncture
302. [Umiejętność wroga [9021603] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 8 당 코인 위력 +1 (최대 4)\n[WinDuel] [Burst] 횟수 2 증가\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 8 ([Breath] on self + [Burst] on target) (max 4)\n[WinDuel] Inflict +2 [Burst] Count\n[WinDuel] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monety +1 za każde 8 (suma [Breath] jednostki i [Burst] celu) (maks. 4)\n[WinDuel] nakłada +2 Licznika [Burst]\n[WinDuel] zyskuje +2 Licznika [Breath]
303. [Umiejętność wroga [9021603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [9021603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [BurstPoison] 부여 (스킬당 1회)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Inflict [BurstPoison] next turn (once per Skill)
   PL: [OnSucceedAttack] nakłada [BurstPoison] w następnej turze (1 raz na Umiejętność)
305. [Umiejętność wroga [9021603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [9021603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신에게 [SnakeStance]이 있으면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SnakeStance]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SnakeStance] = 사완 / Serpent Arm
   EN: [OnSucceedAttack] If this unit has [SnakeStance], Reuse this Coin once (once per Skill)
   PL: [OnSucceedAttack] jeżeli jednostka ma [SnakeStance], używa Monety ponownie 1 raz (1 raz na Umiejętność)
307. [Umiejętność wroga [9021603] (ulepszenie 1) — moneta 2, efekt 3 — opis] - 재사용 코인의 피해량 -70%
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021603].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: - The Reused Coin deals -70% damage
   PL: - używana ponownie Moneta zadaje o 70% mniej obrażeń
308. [Umiejętność wroga [9021604] (ulepszenie 1) — nazwa] 기회를 찾지
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021604].levelList[level=1].name
   limit: do 40 znaków
   EN: Observe for a Chance
   PL: Observe for a Chance
309. [Umiejętność wroga [9021604] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] [SnakeStance] 3 얻음 (스킬당 1회)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021604].levelList[level=1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [9021604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9021604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [9102301] (ulepszenie 1) — nazwa] 변형신완(變形伸腕)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102301].levelList[level=1].name
   limit: do 40 znaków
   EN: Mutated Elongating Arm
   PL: Mutated Elongating Arm
312. [Umiejętność wroga [9102301] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)\n[WinDuel] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102301].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on target) (max 2)\n[WinDuel] Gain +3 [Breath] Count
   PL: [WhenUse] Moc Monety +1 za każde 10 (suma [Breath] jednostki i [Burst] celu) (maks. 2)\n[WinDuel] zyskuje +3 Licznika [Breath]
313. [Umiejętność wroga [9102301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność wroga [9102301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność wroga [9102301] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102301].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [9102301] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 자신에게 [Breath]이 10 이상 있으면, [SnakeStance] 1 얻고 코인 1회 재사용 (스킬당 1회, 턴 당 [SnakeStance] 최대 획득량: 2)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102301].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath], [SnakeStance]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise; [SnakeStance] = 사완 / Serpent Arm
   EN: [CriticalOnSucceedAttack] If this unit has 10+ [Breath], gain 1 [SnakeStance] and Reuse Coin once (once per Skill; can gain up to 2 [SnakeStance] per turn)
   PL: [CriticalOnSucceedAttack] jeżeli jednostka ma 10+ [Breath], zyskuje 1 [SnakeStance] i używa Monety ponownie 1 raz (1 raz na Umiejętność; maks. 2 zyskanych [SnakeStance] na turę)
317. [Umiejętność wroga [9102302] (ulepszenie 1) — nazwa] 사신장완(蛇伸長腕)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].name
   limit: do 40 znaków
   EN: Elongating Serpent Arm
   PL: Elongating Serpent Arm
318. [Umiejętność wroga [9102302] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 8 당 코인 위력 +1 (최대 3)\n[BeforeAttack] 자신에게 [SnakeStance]이 있으면, 공격 가중치 2 증가\n- [WideAreaRampage] 스킬이 됨.\n- 같은 대상을 공격했을 경우, 대상의 [Burst] 횟수가 2 이하면, [Burst] 횟수 1 증가, [BurstPoison] 1 소모\n[WinDuel] 모든 대상에게 [Burst] 횟수 1 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Burst], [BeforeAttack], [SnakeStance], [WideAreaRampage], [BurstPoison], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [SnakeStance] = 사완 / Serpent Arm; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [BurstPoison] = 주살【독】 / Deathrite【Venom】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 8 ([Breath] on self + [Burst] on target) (max 3)\n[BeforeAttack] If this unit has [SnakeStance], gain +2 Atk Weight\n- Becomes a [WideAreaRampage] Skill\n- When attacking the same target, if target has 2 or fewer [Burst] Count, inflict +1 [Burst] Count and consume 1 [BurstPoison]\n[WinDuel] Inflict +1 [Burst] Count on all targets
   PL: [WhenUse] Moc Monety +1 za każde 8 (suma [Breath] jednostki i [Burst] celu) (maks. 3)\n[BeforeAttack] jeżeli jednostka ma [SnakeStance], Waga Ataku +2\n- staje się Umiejętnością [WideAreaRampage].\n- przy atakowaniu tego samego celu, jeżeli cel ma 2 lub mniej Liczników [Burst], nakłada +1 Licznika [Burst] i zużywa 1 [BurstPoison]\n[WinDuel] nakłada +1 Licznika [Burst] wszystkim celom
319. [Umiejętność wroga [9102302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność wroga [9102302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Umiejętność wroga [9102302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Umiejętność wroga [9102302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność wroga [9102302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [9102302] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstPoison]이 있으면, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102302].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność wroga [9102303] (ulepszenie 1) — nazwa] 사첨관극(蛇尖貫極)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102303].levelList[level=1].name
   limit: do 40 znaków
   EN: Serpent's Keenlance
   PL: Serpent's Keenlance
326. [Umiejętność wroga [9102303] (ulepszenie 1) — opis] 자신에게 [SnakeStance], 대상에게 [BurstPoison]이 있다면 합 불가 스킬이 됨\n[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 4 당 코인 위력 +1 (최대 10)\n[WinDuel] [Burst] 횟수 2, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102303].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [SnakeStance], [BurstPoison], [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm; [BurstPoison] = 주살【독】 / Deathrite【Venom】; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit has [SnakeStance] and target has [BurstPoison], this Skill becomes an Unclashable Skill\n[WhenUse] Coin Power +1 for every 4 ([Breath] on self + [Burst] on target) (max 10)\n[WinDuel] Inflict +2 [Burst] Count and gain +3 [Breath] Count
   PL: jeżeli jednostka ma [SnakeStance], a cel [BurstPoison], Umiejętność staje się Umiejętnością bez Starcia\n[WhenUse] Moc Monety +1 za każde 4 (suma [Breath] jednostki i [Burst] celu) (maks. 10)\n[WinDuel] nakłada +2 Licznika [Burst] i zyskuje +3 Licznika [Breath]
327. [Umiejętność wroga [9102303] (ulepszenie 1) — moneta 1, efekt 1 — opis] 자신에게 [SnakeStance]이 있으면, 피해량 +100%
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SnakeStance]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm
   EN: If this unit has [SnakeStance], deal +100% damage
   PL: jeżeli jednostka ma [SnakeStance], zadaje +100% obrażeń
328. [Umiejętność wroga [9102303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [SnakeStance]당 [BurstPoison] 5 소모 (턴 당 1회)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SnakeStance], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SnakeStance] = 사완 / Serpent Arm; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Consume 5 [BurstPoison] for every [SnakeStance] on self (once per turn)
   PL: [OnSucceedAttack] zużywa 5 [BurstPoison] za każde [SnakeStance] jednostki (1 raz na turę)
329. [Umiejętność wroga [9102303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 10 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 10 [Burst]
   PL: [OnSucceedAttack] nakłada 10 [Burst]
330. [Umiejętność wroga [9102303] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [BurstPoison] 부여
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102303].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Umiejętność wroga [9102304] (ulepszenie 1) — nazwa] 기회를 노리지
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102304].levelList[level=1].name
   limit: do 40 znaków
   EN: Wait for a Chance
   PL: Wait for a Chance
332. [Umiejętność wroga [9102304] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 3)\n[WhenUse] [SnakeStance] 3 얻음 (스킬당 1회)
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102304].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Burst], [SnakeStance]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [SnakeStance] = 사완 / Serpent Arm
   EN: [CanDuelGuard]\n[WhenUse] Coin Power +1 for every 4 [Burst] on target (max 3)\n[WhenUse] Gain 3 [SnakeStance] (once per Skill)
   PL: [CanDuelGuard]\n[WhenUse] Moc Monety +1 za każde 4 [Burst] celu (maks. 3)\n[WhenUse] zyskuje 3 [SnakeStance] (1 raz na Umiejętność)
333. [Umiejętność wroga [9102304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-cultivation.json :: dataList[id=9102304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [cultivation] Pasywka wroga: Passives_Abnormality-cultivation
- plik gry: `Passives_Abnormality-cultivation.json`

334. [[cultivation] Pasywka wroga [124701] — nazwa] 전 흑수 - 오 필두
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124701].name
   limit: do 40 znaków
   EN: Former Heishou - Wu Adept
   PL: Former Heishou - Wu Adept
335. [[cultivation] Pasywka wroga [124701] — opis] 스테이지 시작 시 정신력이 -15로 감소하고, [LegStrengthHorse] 3, [CrazyWei] 1 얻음\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -50% (소수점 버림)\n\n자신의 [SuperCoin]이 파괴된 채 적중시, 대상의 [Burst] 효과를 발동하지 않음 (횟수 차감 없음)\n\n흐트러진 적에게 피해량 +50%
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124701].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [LegStrengthHorse], [CrazyWei], [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [SuperCoin]
   znaczenie tagów: [LegStrengthHorse] = 각력【오】 / Strider【Wu】; [CrazyWei] = 광폭화 / Berserking; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Encounter Start: reset this unit's SP to -15 and gain 3 [LegStrengthHorse] and 1 [CrazyWei]\nTake -50% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] (rounded down)\n\nIf this unit hits with a Cracked [SuperCoin], it does not activate the target's [Burst] effect (does not consume Count either)\n\nDeal +50% damage against Staggered enemies
   PL: Początek walki: SP tej jednostki zostaje ustalone na -15, zyskuje 3 [LegStrengthHorse] i 1 [CrazyWei]\notrzymuje o 50% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] (zaokrąglane w dół)\n\nprzy trafieniu rozbitym [SuperCoin]em nie uruchamia efektu [Burst] celu (nie zużywa też jego Licznika)\n\nzadaje +50% obrażeń Oszołomionym wrogom
336. [[cultivation] Pasywka wroga [124702] — nazwa] 짓밟아서… 으깨드리겠습니다
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124702].name
   limit: do 60 znaków
   EN: I will trample... and crush you to mulch
   PL: I will trample... and crush you to mulch
337. [[cultivation] Pasywka wroga [124702] — opis] 자신에게 [LegStrengthHorse]가 있으면, [VibrationExplosion]을 적중 시킬 때 마다 대상이 메인 타겟이면 [ConcussionWei]을 1 부여함
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124702].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [LegStrengthHorse], [VibrationExplosion], [ConcussionWei]
   znaczenie tagów: [LegStrengthHorse] = 각력【오】 / Strider【Wu】; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [ConcussionWei] = 뇌진탕 / Concussion
   EN: If this unit has [LegStrengthHorse], inflict 1 [ConcussionWei] against the main target when this unit triggers [VibrationExplosion] against the main target
   PL: jeżeli jednostka ma [LegStrengthHorse], nakłada 1 [ConcussionWei] na główny cel za każdym razem, gdy uruchamia na nim [VibrationExplosion]
338. [[cultivation] Pasywka wroga [124703] — nazwa] 혼비중천(魂飛中天)
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124703].name
   limit: do 40 znaków
   EN: Soul Lost in Daylight (魂飛中天)
   PL: Soul Lost in Daylight (魂飛中天)
339. [[cultivation] Pasywka wroga [124703] — opis] 자신에게 [LegStrengthHorse]가 있으면, [Vibration]이 없는 대상에게 [VibrationExplosion] 효과가 있는 코인 적중시 [ReboundWei] 1 획득 ([ReboundWei]이 최댓값이라면 획득하지 않음)\n\n턴 종료 시 자신의 [ReboundWei]이 최댓값이라면 전부 소모하고 다음 턴에 [LegStrengthHorse]1 감소
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124703].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [LegStrengthHorse], [Vibration], [VibrationExplosion], [ReboundWei]
   znaczenie tagów: [LegStrengthHorse] = 각력【오】 / Strider【Wu】; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [ReboundWei] = 반동 / Recoiling
   EN: If this unit has [LegStrengthHorse], gain 1 [ReboundWei] when hitting with a Skill that triggers [VibrationExplosion] against targets without [Vibration] (does not gain any [ReboundWei] if its Stack is already maxed)\n\nTurn End: if this unit's [ReboundWei] Stack is maxed, consume all of it; then, lose 1 [LegStrengthHorse] next turn
   PL: jeżeli jednostka ma [LegStrengthHorse], zyskuje 1 [ReboundWei] przy trafieniu Umiejętnością uruchamiającą [VibrationExplosion] na celach bez [Vibration] (nie zyskuje [ReboundWei], jeżeli Licznik osiągnął maksimum)\n\nna koniec tury, jeżeli Licznik [ReboundWei] jednostki osiągnął maksimum, zużywa go cały, a następnie traci 1 [LegStrengthHorse] w następnej turze
340. [[cultivation] Pasywka wroga [124704] — nazwa] 그 더러운 비늘 하나 남지 않도록…
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124704].name
   limit: do 70 znaków
   EN: I'll scrape every filthy scale off your skin...
   PL: I'll scrape every filthy scale off your skin...
341. [[cultivation] Pasywka wroga [124704] — opis] 턴 시작 시 자신의 속도 2 당 [AttackUp] 1 얻음 (최대 2)\n자신의 속도가 5 이상이면, 추가로 [SlashDamageUp] 1, [HitDamageUp] 1 얻음
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124704].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [SlashDamageUp], [HitDamageUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: Turn Start: gain 1 [AttackUp] for every 2 Speed this unit has (max 2)\nAt 5+ Speed, gain 1 [SlashDamageUp] and 1 [HitDamageUp] as well
   PL: na Początku tury zyskuje 1 [AttackUp] za każde 2 Szybkości tej jednostki (maks. 2)\nprzy Szybkości 5+ dodatkowo zyskuje 1 [SlashDamageUp] i 1 [HitDamageUp]
342. [[cultivation] Pasywka wroga [124705] — nazwa] 감히 이곳이 어디라고…!
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124705].name
   limit: do 40 znaków
   EN: Intrepid trespasser...!
   PL: Intrepid trespasser...!
343. [[cultivation] Pasywka wroga [124705] — opis] 합에서 졌을 경우 합을 진행했던 대상의 코인이 더하기 코인이라면 대상의 정신력 5 회복 시키거나, 빼기 코인이라면 대상의 정신력 5 감소 시키고(정신력이 -40 이하라면 이 효과를 받지 않음) 대상이 사용했던 스킬 속성의 E.G.O 자원 +2. (턴 당 3회 발동)\n- 해당 스킬이 분노 혹은 탐식 속성 스킬이라면 가장 부족한 E.G.O 자원 추가로 +2.
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124705].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Clash Lose: if the target's Coin was a Plus Coin, target heals 5 SP; if the target's Coin was a Minus Coin, target loses 5 SP (does not activate if the target's SP is at -40 or less). Then, give 2 E.G.O resources to the Affinity of the Skill the target used (3 times per turn)\n- If the Skill's Affinity was Wrath or Gluttony, give 2 E.G.O resources of the least-owned Affinities as well
   PL: po przegranej w Starciu: jeżeli Moneta celu była Monetą Plus, cel przywraca 5 SP; jeżeli była Monetą Minus, cel traci 5 SP (nie uruchamia się, jeżeli SP celu wynosi -40 lub mniej), a następnie daje 2 zasoby E.G.O Afinności Umiejętności użytej przez cel (3 razy na turę)\n- jeżeli Afinnością Umiejętności był Gniew albo Obżarstwo, dodatkowo daje 2 zasoby E.G.O Afinności, których ma najmniej
344. [[cultivation] Pasywka wroga [127201] — nazwa] 그간의 피해
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127201].name
   limit: do 40 znaków
   EN: Damage Taken
   PL: Damage Taken
345. [[cultivation] Pasywka wroga [127201] — opis] 전투 중 피해를 입었을 때, 해당 턴동안 가하는 피해량 +20%\n전투 중 합 패배시 해당 스킬로부터 받는 피해량 +15%
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127201].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When taking damage during the combat phase: +20% damage for the turn\nDuring the combat phase: On Clash Lose, take +15% damage from the Skill
   PL: przy otrzymaniu obrażeń podczas fazy walki: +20% zadawanych obrażeń w tej turze\npodczas fazy walki: po przegranej w Starciu otrzymuje +15% obrażeń od tej Umiejętności
346. [[cultivation] Pasywka wroga [127202] — nazwa] 만취 수행
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127202].name
   limit: do 40 znaków
   EN: Plastered Training
   PL: Plastered Training
347. [[cultivation] Pasywka wroga [127202] — opis] 자신의 잃은 체력 1%당 가하는 피해량 +2% (최대 100%)
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127202].desc
   limit: do 120 znaków
   EN: Deal +2% damage for every 1% missing HP on self (max 100%)
   PL: zadaje +2% obrażeń za każde 1% brakującego HP jednostki (maks. 100%)
348. [[cultivation] Pasywka wroga [127203] — nazwa] 술과 함께라면 아무것도 두려울 것이 없지
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127203].name
   limit: do 80 znaków
   EN: I've got nothing to fear with a bottle of wine by my side
   PL: I've got nothing to fear with a bottle of wine by my side
349. [[cultivation] Pasywka wroga [127203] — opis] 턴 시작 시 자신의 [SipOfAlcoholJin]이 최대 값이라면 2 소모하고 [DrunkAwakening]을 획득함
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127203].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SipOfAlcoholJin], [DrunkAwakening]
   znaczenie tagów: [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞); [DrunkAwakening] = 정신 각성 / Mental Awakening
   EN: Turn Start: at max [SipOfAlcoholJin] Stack, consume 2 of its Stack and gain [DrunkAwakening]
   PL: na Początku tury, jeżeli Licznik [SipOfAlcoholJin] osiągnął maksimum, zużywa 2 Liczniki i zyskuje [DrunkAwakening]
350. [[cultivation] Pasywka wroga [127204] — nazwa] 취수야객
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127204].name
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [[cultivation] Pasywka wroga [127204] — opis] 스테이지 시작 시 정신력이 10으로 증가함\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -50% (소수점 버림)\n\n수감자에게 받는 피해량 -30%\n\n전 턴에 [SipOfAlcoholJin]을 2 이상 얻었다면 턴 시작 시 자신의 잃은 체력 10%당 정신력 5 회복 (최대 40)\n\n페이즈 변환 시 자신이 흐트러짐 상태라면 해제함
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127204].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [SipOfAlcoholJin]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [SipOfAlcoholJin] = 한 모금(眞) / Swig (眞)
   EN: Encounter Start: reset this unit's SP to 10\nTake -50% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] (rounded down)\n\nTake -30% damage from Sinners\n\nIf this unit gained 2 or more [SipOfAlcoholJin] last turn, heal 5 SP for every 10% missing HP at Turn Start (max 40)\n\nWhen entering a new phase, if this unit is Staggered, recover from Stagger
   PL: Początek walki: SP tej jednostki zostaje ustalone na 10\notrzymuje o 50% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] (zaokrąglane w dół)\n\notrzymuje o 30% mniej obrażeń od Grzeszników\n\njeżeli w poprzedniej turze jednostka zyskała 2 lub więcej [SipOfAlcoholJin], na Początku tury przywraca 5 SP za każde 10% brakującego HP (maks. 40)\n\nprzy wejściu w nową fazę, jeżeli jednostka jest w Oszołamieniu, dochodzi do siebie z Oszołamienia
352. [[cultivation] Pasywka wroga [127205] — nazwa] 혈적성하(血滴成河)
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127205].name
   limit: do 40 znaków
   EN: River of Blooddrops (血滴成河)
   PL: River of Blooddrops (血滴成河)
353. [[cultivation] Pasywka wroga [127205] — opis] 턴 종료 시 [Laceration]이 10 이상인 적이 한 명이라도 있을 경우 발동함\n[Laceration]을 가지고 있는 적에게 [Laceration] 5 당 [DrunkBlood]를 1 부여함 (적 당 3회)
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=127205].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DrunkBlood]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DrunkBlood] = 혈주(血注) / Bloodpour (血注)
   EN: Activates if at least 1 enemy has 10+ [Laceration] at Turn End\nAgainst enemies with [Laceration], inflict 1 [DrunkBlood] for every 5 [Laceration] they have (3 times per enemy)
   PL: uruchamia się na koniec tury, jeżeli co najmniej 1 wróg ma 10+ [Laceration]\nna wrogach z [Laceration] nakłada 1 [DrunkBlood] za każde 5 [Laceration] wroga (3 razy na wroga)
354. [[cultivation] Pasywka wroga [124801] — nazwa] 대련 종료
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124801].name
   limit: do 40 znaków
   EN: Sparring Complete
   PL: Sparring Complete
355. [[cultivation] Pasywka wroga [124801] — opis] 자신의 체력이 20% 미만으로 감소하면, 전투 종료
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124801].desc
   limit: do 120 znaków
   EN: Ends Encounter when this unit's HP drops below 20%
   PL: kończy walkę, gdy HP tej jednostki spadnie poniżej 20%
356. [[cultivation] Pasywka wroga [124901] — nazwa] 회로 반전
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124901].name
   limit: do 40 znaków
   EN: Reversed Circuitry
   PL: Reversed Circuitry
357. [[cultivation] Pasywka wroga [124901] — opis] 턴 시작시 자신의 [Charge] 횟수가 10 미만이면, 자신의 최대 체력의 5%를 소모하여 [Charge] 횟수 5 얻음\n턴 종료시 자신의 [Charge] 횟수가 15 이상이면, [Charge] 횟수를 5 소모하여 자신의 최대 체력의 5% 회복
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=124901].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Turn Start: at less than 10 [Charge] Count, consume 5% HP on self to gain +5 [Charge] Count\nTurn End: at 15+ [Charge] Count, consume 5 [Charge] Count to heal 5% HP on self
   PL: na Początku tury, jeżeli Licznik [Charge] jest niższy niż 10, zużywa 5% HP, aby zyskać +5 Licznika [Charge]\nna koniec tury przy 15+ Licznikach [Charge] zużywa 5 Liczników [Charge], aby przywrócić 5% HP jednostki
358. [[cultivation] Pasywka wroga [125001] — nazwa] 조금 내려놓은 짐
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125001].name
   limit: do 40 znaków
   EN: Slightly Relieved Burdens
   PL: Slightly Relieved Burdens
359. [[cultivation] Pasywka wroga [125001] — opis] 턴 시작시 정신력 5 회복\n턴 시작시 자신의 정신력이 20 이상이면, [Enhancement] 1 얻음
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: heal 5 SP\nTurn Start: at 20+ SP, gain 1 [Enhancement]
   PL: na Początku tury przywraca 5 SP\nna Początku tury przy SP równym 20 lub więcej zyskuje 1 [Enhancement]
360. [[cultivation] Pasywka wroga [125002] — nazwa] 책임의 무게
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125002].name
   limit: do 40 znaków
   EN: Burden of Responsibility
   PL: Burden of Responsibility
361. [[cultivation] Pasywka wroga [125002] — opis] 이번 전투에서 자신의 체력이 최대 체력의 절반 이하가 되면, 다음 턴부터 매 턴 [AttackDmgUp] 2 얻음
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125002].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: If this unit's HP drops below 50% or less in this Encounter, starting from the next turn, gain 2 [AttackDmgUp] every turn
   PL: w tej walce, gdy HP tej jednostki spadnie do 50% Maks. HP lub mniej, od następnej tury zyskuje 2 [AttackDmgUp] co turę
362. [[cultivation] Pasywka wroga [125101] — nazwa] 공포정치
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125101].name
   limit: do 40 znaków
   EN: Rule by Fear
   PL: Rule by Fear
363. [[cultivation] Pasywka wroga [125101] — opis] 대상의 정신력이 0 미만이면, 0보다 낮은 정신력 1 당 가하는 피해량 +3%
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125101].desc
   limit: do 150 znaków
   EN: If the target has less than 0 SP: deal even more damage the further the target's SP is from 0 (+3% damage per 1 SP)
   PL: jeżeli SP celu jest niższe niż 0: zadaje tym więcej obrażeń, im dalej SP celu od 0 (+3% obrażeń za każde 1 SP)
364. [[cultivation] Pasywka wroga [125102] — nazwa] 재밌을 것 같지 않나?
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125102].name
   limit: do 50 znaków
   EN: It's going to be so much fun, hmm?
   PL: It's going to be so much fun, hmm?
365. [[cultivation] Pasywka wroga [125102] — opis] 모든 대상이 부정적인 효과를 얻을 때마다, [AttackUp] 1, [DefenseUp] 1 얻음
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] every time any target gains a negative effect
   PL: zyskuje 1 [AttackUp] i 1 [DefenseUp] za każdym razem, gdy dowolny cel zyskuje negatywny efekt
366. [[cultivation] Pasywka wroga [125103] — nazwa] 비틀린 의지
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125103].name
   limit: do 40 znaków
   EN: Twisted Determination
   PL: Twisted Determination
367. [[cultivation] Pasywka wroga [125103] — opis] 합 승리 시, 정신력 5 회복\n합 패배 시, [Enhancement] 1 얻음
   źródło: Passives_Abnormality-cultivation.json :: dataList[id=125103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: On Clash Win, heal 5 SP\nOn Clash Lose, gain 1 [Enhancement]
   PL: po wygranej w Starciu przywraca 5 SP\npo przegranej w Starciu zyskuje 1 [Enhancement]

## [cultivation] Pasywka wroga: Passives_Enemy-cultivation
- plik gry: `Passives_Enemy-cultivation.json`

368. [[cultivation] Pasywka wroga [9021501] — nazwa] 기회는 지금
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9021501].name
   limit: do 40 znaków
   EN: Now's Our Chance
   PL: Now's Our Chance
369. [[cultivation] Pasywka wroga [9021501] — opis] 턴동안 자신이 [BurstPoison]을 소모 시켜 수치를 0으로 만들었으면, 다음 턴에 [PenetrateDamageUp] 1 얻음 (최대 2)
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9021501].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [BurstPoison], [PenetrateDamageUp]
   znaczenie tagów: [BurstPoison] = 주살【독】 / Deathrite【Venom】; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: For a turn, if this unit reduced the target's [BurstPoison] down to 0 Stack, gain 1 [PenetrateDamageUp] next turn (max 2)
   PL: w ciągu tury, jeżeli jednostka zredukowała Licznik [BurstPoison] celu do 0, zyskuje 1 [PenetrateDamageUp] w następnej turze (maks. 2)
370. [[cultivation] Pasywka wroga [9021502] — nazwa] 사독(蛇毒)
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9021502].name
   limit: do 40 znaków
   EN: Snake Venom
   PL: Snake Venom
371. [[cultivation] Pasywka wroga [9021502] — opis] 대상에게 [BurstPoison]이 있으면, 자신의 [SnakeStance]당 가하는 피해량 +2.5% (최대 7.5%)
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9021502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstPoison], [SnakeStance]
   znaczenie tagów: [BurstPoison] = 주살【독】 / Deathrite【Venom】; [SnakeStance] = 사완 / Serpent Arm
   EN: If target has [BurstPoison], deal +2.5% damage for every [SnakeStance] on self (max 7.5%)
   PL: jeżeli cel ma [BurstPoison], zadaje +2.5% obrażeń za każde [SnakeStance] jednostki (maks. 7.5%)
372. [[cultivation] Pasywka wroga [9102301] — nazwa] 약점이 보인다
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102301].name
   limit: do 40 znaków
   EN: I See Your Weakness
   PL: I See Your Weakness
373. [[cultivation] Pasywka wroga [9102301] — opis] [WideAreaRampage] 공격을 할 때, 같은 대상을 공격했다면 피해량 +20%, 부여하는 [Burst] 위력 혹은 [Burst] 횟수 +1
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102301].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [WideAreaRampage], [Burst]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Burst] = 파열 / Rupture
   EN: When using an [WideAreaRampage] attack, when attacking the same target, deal +20% damage and inflict +1 more [Burst] Potency or Count
   PL: przy ataku [WideAreaRampage], atakując tego samego celu, zadaje +20% obrażeń i nakłada o 1 więcej Siły albo Licznika [Burst]
374. [[cultivation] Pasywka wroga [9102302] — nazwa] 기회가 보인다
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102302].name
   limit: do 40 znaków
   EN: I Spy an Opportunity
   PL: I Spy an Opportunity
375. [[cultivation] Pasywka wroga [9102302] — opis] 턴동안 자신이 [BurstPoison]을 소모 시켜 수치를 0으로 만들었으면, 다음 턴에 [PenetrateDamageUp] 1 얻음 (최대 2)
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102302].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [[cultivation] Pasywka wroga [9102303] — nazwa] 사극독(蛇極毒)
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102303].name
   limit: do 40 znaków
   EN: Snake Deathvenom
   PL: Snake Deathvenom
377. [[cultivation] Pasywka wroga [9102303] — opis] 대상에게 [BurstPoison]이 있으면, 자신의 [SnakeStance]당 가하는 피해량 +5% (최대 15%)
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102303].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstPoison], [SnakeStance]
   znaczenie tagów: [BurstPoison] = 주살【독】 / Deathrite【Venom】; [SnakeStance] = 사완 / Serpent Arm
   EN: If target has [BurstPoison], deal +5% damage for every [SnakeStance] on self (max 15%)
   PL: jeżeli cel ma [BurstPoison], zadaje +5% obrażeń za każde [SnakeStance] jednostki (maks. 15%)
378. [[cultivation] Pasywka wroga [9102601] — nazwa] 각오
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102601].name
   limit: do 40 znaków
   EN: Determination
   PL: Determination
379. [[cultivation] Pasywka wroga [9102601] — opis] 흐트러짐이 풀릴 때, [Enhancement] 1 얻음
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: When recovering from Stagger, gain 1 [Enhancement]
   PL: gdy dochodzi do siebie z Oszołamienia, zyskuje 1 [Enhancement]
380. [[cultivation] Pasywka wroga [9102602] — nazwa] 수업의 성과
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102602].name
   limit: do 40 znaków
   EN: Fruits of Education
   PL: Fruits of Education
381. [[cultivation] Pasywka wroga [9102602] — opis] 스테이지 입장 시, 수업으로 얻는 지/용/인의 합에 비례하여 [StudyStatSinclair] 획득
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102602].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [StudyStatSinclair]
   znaczenie tagów: [StudyStatSinclair] = 알에서 나오기 위한 몸부림 / Thrashing to Hatch
   EN: Upon entering the Stage, gain [StudyStatSinclair] based on the sum of Zhi, Yong, and Ren gained from classes
   PL: przy wejściu na etap zyskuje [StudyStatSinclair] zależnie od sumy Zhi, Yong i Ren zdobytych na zajęciach
382. [[cultivation] Pasywka wroga [9102603] — nazwa] 내면에 귀를 기울인다면…
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102603].name
   limit: do 60 znaków
   EN: If I lend my ear to the inner self...
   PL: If I lend my ear to the inner self...
383. [[cultivation] Pasywka wroga [9102603] — opis] 턴 시작 시, 흐트러짐 상태면 흐트러짐 해제하고 [StudySignSinclair] 획득(전투 당 1회)\n- 이후 모든 스킬 사용 시, 파괴 불가 코인으로 변경됨
   źródło: Passives_Enemy-cultivation.json :: dataList[id=9102603].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StudySignSinclair]
   znaczenie tagów: [StudySignSinclair] = 어느 표지 / A Sign
   EN: Turn Start: if this unit is Staggered, recover from Stagger; then, gain [StudySignSinclair] (once per Encounter)\n- Every Skill used after this activates becomes Unbreakable Coins
   PL: na Początku tury, jeżeli jednostka jest w Oszołamieniu, dochodzi do siebie z Oszołamienia, a następnie zyskuje [StudySignSinclair] (1 raz na walkę)\n- każda Umiejętność użyta po uruchomieniu tego efektu ma Niezniszczalne Monety

## [exme] Wróg / część: Enemies-exme
- plik gry: `Enemies-exme.json`

384. [[exme] Wróg / część [1448] — nazwa] 추노꾼 - 제압
   źródło: Enemies-exme.json :: dataList[id=1448].name
   limit: do 40 znaków
   EN: Ch'unokkun - Incapacitate
   PL: Ch'unokkun - Incapacitate
385. [[exme] Wróg / część [1448] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=1448].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [[exme] Wróg / część [1449] — nazwa] 추노꾼 - 포박
   źródło: Enemies-exme.json :: dataList[id=1449].name
   limit: do 40 znaków
   EN: Ch'unokkun - Bind
   PL: Ch'unokkun - Bind
387. [[exme] Wróg / część [1449] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=1449].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [[exme] Wróg / część [1450] — nazwa] 섬광 현상 - 임경업
   źródło: Enemies-exme.json :: dataList[id=1450].name
   limit: do 50 znaków
   EN: Flash Phenomenon - Im Gyeong-eop
   PL: Flash Phenomenon - Im Gyeong-eop
389. [[exme] Wróg / część [1450] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=1450].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [[exme] Wróg / część [1452] — nazwa] 차가운 N사 2등급 직원
   źródło: Enemies-exme.json :: dataList[id=1452].name
   limit: do 40 znaków
   EN: Icy N Corp. Class 2 Staff
   PL: Icy N Corp. Class 2 Staff
391. [[exme] Wróg / część [1452] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=1452].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [[exme] Wróg / część [1453] — nazwa] 조용한 N사 2등급 직원
   źródło: Enemies-exme.json :: dataList[id=1453].name
   limit: do 50 znaków
   EN: Reticent N Corp. Class 2 Staff
   PL: Reticent N Corp. Class 2 Staff
393. [[exme] Wróg / część [1453] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=1453].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [[exme] Wróg / część [91057] — nazwa] 원망하는 검계 살수
   źródło: Enemies-exme.json :: dataList[id=91057].name
   limit: do 40 znaków
   EN: Hateful Blade Lineage Salsu
   PL: Hateful Blade Lineage Salsu
395. [[exme] Wróg / część [91057] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=91057].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [[exme] Wróg / część [91058] — nazwa] 한 서린 검계 살수
   źródło: Enemies-exme.json :: dataList[id=91058].name
   limit: do 50 znaków
   EN: Resentful Blade Lineage Salsu
   PL: Resentful Blade Lineage Salsu
397. [[exme] Wróg / część [91058] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=91058].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [[exme] Wróg / część [1451] — nazwa] 심상 속 임경업
   źródło: Enemies-exme.json :: dataList[id=1451].name
   limit: do 40 znaków
   EN: Imagined Im Gyeong-eop
   PL: Imagined Im Gyeong-eop
399. [[exme] Wróg / część [1451] — opis] 본체
   źródło: Enemies-exme.json :: dataList[id=1451].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [exme] Umiejętności wrogów / Anomalii — Skills_Abnormality-exme
- grupa rozdziału/trybu: `exme` · plik: `Skills_Abnormality-exme.json`

400. [Umiejętność wroga [144801] (ulepszenie 1) — nazwa] 오랏줄 죄기
   źródło: Skills_Abnormality-exme.json :: dataList[id=144801].levelList[level=1].name
   limit: do 40 znaków
   EN: Constricting Ohra Bonds
   PL: Constricting Ohra Bonds
401. [Umiejętność wroga [144801] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n- 대상보다 속도가 빠르면, 자신의 [Breath] 횟수 1 추가 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144801].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Base Power +1\n[WhenUse] Gain +3 [Breath] Count\n- If this unit's Speed is faster than the target's, gain an additional +1 [Breath] Count
   PL: [WhenUse] przy 6+ (suma [Breath] jednostki i [Laceration] celu), Moc Bazowa +1\n[WhenUse] nakłada +3 Licznika [Breath]\n- jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, dodatkowo nakłada +1 Licznika [Breath]
402. [Umiejętność wroga [144801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [144801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność wroga [144801] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ScratchesHurt] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144801].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScratchesHurt]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScratchesHurt] = 찢긴 상처 / Avulsion Wound
   EN: [OnSucceedAttack] Inflict 1 [ScratchesHurt] next turn
   PL: [OnSucceedAttack] nakłada 1 [ScratchesHurt] w następnej turze
405. [Umiejętność wroga [144802] (ulepszenie 1) — nazwa] 힘줄 베기
   źródło: Skills_Abnormality-exme.json :: dataList[id=144802].levelList[level=1].name
   limit: do 40 znaków
   EN: Hamstringing
   PL: Hamstringing
406. [Umiejętność wroga [144802] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 마지막 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 3 증가\n[WhenUse] 대상보다 속도가 빠르면, [Breath] 3 얻음
   źródło: Skills_Abnormality-exme.json :: dataList[id=144802].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Base Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] If this unit's Speed is faster than the target's, convert the final Coin into [SuperCoin]\n[WhenUse] Gain 2 [Breath] and +3 [Breath] Count\n[WhenUse] If this unit's Speed is faster than the target's, gain 3 [Breath]
   PL: [WhenUse] Moc Bazowa +1 za każde 6 (suma [Breath] jednostki i [Laceration] celu) (maks. 2)\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, ostatnia Moneta zmienia się w [SuperCoin]\n[WhenUse] zyskuje 2 [Breath] i nakłada +3 Licznika [Breath]\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, zyskuje 3 [Breath]
407. [Umiejętność wroga [144802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada +3 Licznika [Laceration]
408. [Umiejętność wroga [144802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] nakłada 1 [Laceration]
409. [Umiejętność wroga [144802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ScratchesHurt] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScratchesHurt]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScratchesHurt] = 찢긴 상처 / Avulsion Wound
   EN: [OnSucceedAttack] Inflict 2 [ScratchesHurt] next turn
   PL: [OnSucceedAttack] nakłada 2 [ScratchesHurt] w następnej turze
410. [Umiejętność wroga [144803] (ulepszenie 1) — nazwa] 찢어베기
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].name
   limit: do 40 znaków
   EN: Avulsion Slash
   PL: Avulsion Slash
411. [Umiejętność wroga [144803] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [SuperCoin], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] If this unit's Speed is faster than the target's, convert all Coins into [SuperCoin]s\n[WhenUse] Gain 3 [Breath]\n[WinDuel] Gain 2 [Breath]
   PL: [WhenUse] Moc Monety +1 za każde 6 (suma [Breath] jednostki i [Laceration] celu) (maks. 2)\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, wszystkie Monety zmieniają się w [SuperCoin]y\n[WhenUse] zyskuje 3 [Breath]\n[WinDuel] zyskuje 2 [Breath]
412. [Umiejętność wroga [144803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Umiejętność wroga [144803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 1 [Laceration]
   PL: [CriticalOnSucceedAttack] nakłada 1 [Laceration]
414. [Umiejętność wroga [144803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [144803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [144803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ScratchesHurt] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [144803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [ScratchesHurt] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [ScratchesHurt]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [ScratchesHurt] = 찢긴 상처 / Avulsion Wound
   EN: [CriticalOnSucceedAttack] Inflict 1 [ScratchesHurt] next turn
   PL: [CriticalOnSucceedAttack] nakłada 1 [ScratchesHurt] w następnej turze
418. [Umiejętność wroga [144804] (ulepszenie 1) — nazwa] 낙인찍기
   źródło: Skills_Abnormality-exme.json :: dataList[id=144804].levelList[level=1].name
   limit: do 40 znaków
   EN: Branding
   PL: Branding
419. [Umiejętność wroga [144804] (ulepszenie 1) — opis] [TiedRope]이 부여된 대상 우선 공격\n대상보다 속도가 빠르면, 속도 차이 1당 피해량 +25% (최대 100%)\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=144804].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [TiedRope], [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [TiedRope] = 포박 / Trussed; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: Prioritizes target that has [TiedRope]\nIf this unit's Speed is faster than the target's, deal +25% damage for every Speed difference (max 100%)\n[WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)
   PL: priorytet: cel z [TiedRope]\njeżeli Szybkość jednostki jest wyższa niż Szybkość celu, zadaje +25% obrażeń za każdą 1 różnicę Szybkości (maks. 100%)\n[WhenUse] Moc Monety +1 za każde 6 (suma [Breath] jednostki i [Laceration] celu) (maks. 2)
420. [Umiejętność wroga [144804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Umiejętność wroga [144804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [144804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Umiejętność wroga [144805] (ulepszenie 1) — nazwa] 도주 차단
   źródło: Skills_Abnormality-exme.json :: dataList[id=144805].levelList[level=1].name
   limit: do 40 znaków
   EN: Escape Cutoff
   PL: Escape Cutoff
424. [Umiejętność wroga [144805] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 기본 위력 +1 (최대 2)\n[WhenUse] [Breath] 3 얻음\n[WinDuel] [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144805].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [Laceration], [WinDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n[WhenUse] Base Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] Gain 3 [Breath]\n[WinDuel] Gain +3 [Breath] Count
   PL: [DuelCounter]\n[WhenUse] Moc Bazowa +1 za każde 6 (suma [Breath] jednostki i [Laceration] celu) (maks. 2)\n[WhenUse] zyskuje 3 [Breath]\n[WinDuel] nakłada +3 Licznika [Breath]
425. [Umiejętność wroga [144805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [144805] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ScratchesHurt] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144805].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [144901] (ulepszenie 1) — nazwa] 제압
   źródło: Skills_Abnormality-exme.json :: dataList[id=144901].levelList[level=1].name
   limit: do 40 znaków
   EN: Trammel
   PL: Trammel
428. [Umiejętność wroga [144901] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n- 대상보다 속도가 빠르면, 자신의 [Breath] 횟수 1 추가 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144901].levelList[level=1].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność wroga [144901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [144901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność wroga [144901] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144901].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
432. [Umiejętność wroga [144902] (ulepszenie 1) — nazwa] 숨통옥죄기
   źródło: Skills_Abnormality-exme.json :: dataList[id=144902].levelList[level=1].name
   limit: do 40 znaków
   EN: Choke Hold
   PL: Choke Hold
433. [Umiejętność wroga [144902] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 마지막 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가\n[WhenUse] 대상보다 속도가 빠르면, [Breath] 3 얻음
   źródło: Skills_Abnormality-exme.json :: dataList[id=144902].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Base Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] If this unit's Speed is faster than the target's, convert the final Coin into [SuperCoin]\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count\n[WhenUse] If this unit's Speed is faster than the target's, gain 3 [Breath]
   PL: [WhenUse] Moc Bazowa +1 za każde 6 (suma [Breath] jednostki i [Laceration] celu) (maks. 2)\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, ostatnia Moneta zmienia się w [SuperCoin]\n[WhenUse] zyskuje 2 [Breath] i nakłada +2 Licznika [Breath]\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, zyskuje 3 [Breath]
434. [Umiejętność wroga [144902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność wroga [144902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [144902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
437. [Umiejętność wroga [144903] (ulepszenie 1) — nazwa] 추쇄집행
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].name
   limit: do 40 znaków
   EN: Hunter's Scouring
   PL: Hunter's Scouring
438. [Umiejętność wroga [144903] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [144903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [144903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 2 [Laceration]
   PL: [CriticalOnSucceedAttack] nakłada 2 [Laceration]
441. [Umiejętność wroga [144903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Umiejętność wroga [144903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [144903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 이번 턴과 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Binding] this turn and next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Binding] w tej i następnej turze
444. [Umiejętność wroga [144903] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] ([Binding] 수치 x 20)% 확률로 [TiedRope] 부여\n- 대상이 흐트러짐 상태라면, 확정 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144903].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Binding], [TiedRope]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [TiedRope] = 포박 / Trussed
   EN: [OnSucceedAttack] ([Binding] x 20)% chance to inflict [TiedRope]\n- If target is Staggered, this effect is inflicted without fail
   PL: [OnSucceedAttack] nakłada [TiedRope] z szansą ([Binding] x 20)%\n- jeżeli cel jest w Oszołamieniu, nakłada bezwarunkowo
445. [Umiejętność wroga [144904] (ulepszenie 1) — nazwa] 낙인찍기
   źródło: Skills_Abnormality-exme.json :: dataList[id=144904].levelList[level=1].name
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność wroga [144904] (ulepszenie 1) — opis] [TiedRope]이 부여된 대상 우선 공격\n대상보다 속도가 빠르면, 속도 차이 1당 피해량 +25% (최대 100%)\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=144904].levelList[level=1].desc
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [144904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność wroga [144904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność wroga [144904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [144905] (ulepszenie 1) — nazwa] 퇴로 차단
   źródło: Skills_Abnormality-exme.json :: dataList[id=144905].levelList[level=1].name
   limit: do 40 znaków
   EN: Route Cutoff
   PL: Route Cutoff
451. [Umiejętność wroga [144905] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 기본 위력 +1 (최대 2)\n[WhenUse] [Breath] 3 얻음\n[WinDuel] [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=144905].levelList[level=1].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [144905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [144905] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=144905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [145201] (ulepszenie 1) — nazwa] 모서리 찍기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145201].levelList[level=1].name
   limit: do 40 znaków
   EN: Briefcase Corner Point
   PL: Briefcase Corner Point
455. [Umiejętność wroga [145201] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 1 얻음 (턴당 1회)\n대상의 [Laceration]과 [Vibration]의 합 6이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-exme.json :: dataList[id=145201].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Agility], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 1 [Agility] next turn (once per turn)\nIf target has 6+ ([Laceration] + [Vibration]), Base Power +1
   PL: [WhenUse] zyskuje 1 [Agility] w następnej turze (1 raz na turę)\njeżeli cel ma 6+ (suma [Laceration] i [Vibration]), Moc Bazowa +1
456. [Umiejętność wroga [145201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LensmanNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LensmanNail] = 고정 못 / Pinning Nail
   EN: [OnSucceedAttack] Inflict 1 [LensmanNail]
   PL: [OnSucceedAttack] nakłada 1 [LensmanNail]
457. [Umiejętność wroga [145201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [145201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność wroga [145201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [145202] (ulepszenie 1) — nazwa] 무게 싣기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].name
   limit: do 40 znaków
   EN: Weighted Bash
   PL: Weighted Bash
461. [Umiejętność wroga [145202] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n대상의 [Laceration]과 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Agility], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 [Agility] next turn (once per turn)\nCoin Power +1 for every 6 ([Laceration] on target + [Vibration] on target) (max 2)
   PL: [WhenUse] zyskuje 2 [Agility] w następnej turze (1 raz na turę)\nMoc Monety +1 za każde 6 (suma [Laceration] i [Vibration] celu) (maks. 2)
462. [Umiejętność wroga [145202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [145202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] nakłada 1 [Vibration]
464. [Umiejętność wroga [145202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność wroga [145202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność wroga [145202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
467. [Umiejętność wroga [145203] (ulepszenie 1) — nazwa] 피사체 고정
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].name
   limit: do 40 znaków
   EN: Enframe Subject
   PL: Enframe Subject
468. [Umiejętność wroga [145203] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vibration], [WhenUse], [SuperCoin]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Coin Power +1 for every 6 ([Laceration] on target + [Vibration] on target) (max 2)\n[WhenUse] If this unit's Speed is faster than the target's, convert all Coins into [SuperCoin]s
   PL: Moc Monety +1 za każde 6 (suma [Laceration] i [Vibration] celu) (maks. 2)\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, wszystkie Monety zmieniają się w [SuperCoin]y
469. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LensmanNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LensmanNail] = 고정 못 / Pinning Nail
   EN: [OnSucceedAttack] Inflict 2 [LensmanNail]
   PL: [OnSucceedAttack] nakłada 2 [LensmanNail]
470. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Paralysis] w następnej turze
475. [Umiejętność wroga [145203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [EndCoin] 다음 턴에 [TakePicture] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [TakePicture]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [TakePicture] = 정보 취득 / Intelligence Gathering
   EN: [EndCoin] Inflict 1 [TakePicture] next turn
   PL: [EndCoin] nakłada 1 [TakePicture] w następnej turze
476. [Umiejętność wroga [145204] (ulepszenie 1) — nazwa] 순간포착
   źródło: Skills_Abnormality-exme.json :: dataList[id=145204].levelList[level=1].name
   limit: do 40 znaków
   EN: Snapshot
   PL: Snapshot
477. [Umiejętność wroga [145204] (ulepszenie 1) — opis] [DuelCounter]\n대상의 [Laceration]과 [Vibration]의 합 4당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-exme.json :: dataList[id=145204].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [Laceration], [Vibration], [WhenUse], [SuperCoin]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [DuelCounter]\nBase Power +1 for every 4 ([Laceration] on target + [Vibration] on target) (max 2)\n[WhenUse] If this unit's Speed is faster than the target's, convert all Coins into [SuperCoin]s
   PL: [DuelCounter]\nMoc Bazowa +1 za każde 4 (suma [Laceration] i [Vibration] celu) (maks. 2)\n[WhenUse] jeżeli Szybkość jednostki jest wyższa niż Szybkość celu, wszystkie Monety zmieniają się w [SuperCoin]y
478. [Umiejętność wroga [145204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDown] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [AttackDown] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [AttackDown] w następnej turze
479. [Umiejętność wroga [145204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność wroga [145204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EndCoin] 다음 턴에 [TakePicture] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność wroga [145301] (ulepszenie 1) — nazwa] 철판 강타
   źródło: Skills_Abnormality-exme.json :: dataList[id=145301].levelList[level=1].name
   limit: do 40 znaków
   EN: Steel Plate Slam
   PL: Steel Plate Slam
482. [Umiejętność wroga [145301] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 1 얻음 (턴당 1회)\n대상의 [Laceration]과 [Vibration]의 합 6이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-exme.json :: dataList[id=145301].levelList[level=1].desc
   (powtórzenie elementu 455 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Umiejętność wroga [145301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Umiejętność wroga [145301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Umiejętność wroga [145301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Umiejętność wroga [145301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [145302] (ulepszenie 1) — nazwa] 못머리 치기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].name
   limit: do 40 znaków
   EN: Nailhead Strike
   PL: Nailhead Strike
488. [Umiejętność wroga [145302] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n대상의 [Laceration]과 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].desc
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Umiejętność wroga [145302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność wroga [145302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność wroga [145302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Umiejętność wroga [145302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Umiejętność wroga [145302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [145303] (ulepszenie 1) — nazwa] 초점 교정
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].name
   limit: do 40 znaków
   EN: Focus Recompose
   PL: Focus Recompose
495. [Umiejętność wroga [145303] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [LensmanNail] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność wroga [145303] (ulepszenie 1) — moneta 3, efekt 3 — opis] [EndCoin] 다음 턴에 [TakePicture] 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145303].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [TakePicture]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [TakePicture] = 정보 취득 / Intelligence Gathering
   EN: [EndCoin] Inflict [TakePicture] next turn
   PL: [EndCoin] nakłada [TakePicture] w następnej turze
503. [Umiejętność wroga [145304] (ulepszenie 1) — nazwa] 순간포착
   źródło: Skills_Abnormality-exme.json :: dataList[id=145304].levelList[level=1].name
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność wroga [145304] (ulepszenie 1) — opis] [DuelCounter]\n대상의 [Laceration]과 [Vibration]의 합 4당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상보다 속도가 빠르면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-exme.json :: dataList[id=145304].levelList[level=1].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Umiejętność wroga [145304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDown] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność wroga [145304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność wroga [145304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EndCoin] 다음 턴에 [TakePicture] 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność wroga [145001] (ulepszenie 1) — nazwa] 소 가르기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145001].levelList[level=1].name
   limit: do 40 znaków
   EN: Oxsplitter
   PL: Oxsplitter
509. [Umiejętność wroga [145001] (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145001].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain 3 [Breath]\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)
   PL: [WhenUse] zyskuje 3 [Breath]\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)
510. [Umiejętność wroga [145001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Umiejętność wroga [145001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [CriticalOnSucceedAttack] nakłada +2 Licznika [Laceration]
512. [Umiejętność wroga [145002] (ulepszenie 1) — nazwa] 곰 가르기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145002].levelList[level=1].name
   limit: do 40 znaków
   EN: Bearsplitter
   PL: Bearsplitter
513. [Umiejętność wroga [145002] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 6 이상이면, 모든 코인이 [SuperCoin]이 됨\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145002].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +3 [Breath] Count\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] At 6+ [Breath], convert all Coins into [SuperCoin]s\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] nakłada +3 Licznika [Breath]\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] przy 6+ [Breath] wszystkie Monety zmieniają się w [SuperCoin]y\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
514. [Umiejętność wroga [145002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność wroga [145002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 3 [Laceration]
   PL: [CriticalOnSucceedAttack] nakłada 3 [Laceration]
516. [Umiejętność wroga [145003] (ulepszenie 1) — nazwa] 곰 허리 끊기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145003].levelList[level=1].name
   limit: do 40 znaków
   EN: Bearspine Breaker
   PL: Bearspine Breaker
517. [Umiejętność wroga [145003] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 7 이상이면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +20%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145003].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Laceration], [ChoiSwordsmanship], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], deal +40% damage on Critical Hit\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>At 7+ [ChoiSwordsmanship], convert all Coins into [SuperCoin]s and deal +20% damage on Critical Hit</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] przy 8+ [Breath] zadaje +40% obrażeń przy trafieniu krytycznym\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>przy 7+ [ChoiSwordsmanship] wszystkie Monety zmieniają się w [SuperCoin]y i zadaje +20% obrażeń przy trafieniu krytycznym</u></b></mark></color>\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
518. [Umiejętność wroga [145003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 1 [SlashResistDown] this turn and next turn
   PL: [OnSucceedAttack] nakłada 1 [SlashResistDown] w tej i następnej turze
519. [Umiejętność wroga [145003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 3
520. [Umiejętność wroga [145005] (ulepszenie 1) — nazwa] 본국검범 - 살 베기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145005].levelList[level=1].name
   limit: do 60 znaków
   EN: Swordform of the Homeland - Sal's Sundering
   PL: Swordform of the Homeland - Sal's Sundering
521. [Umiejętność wroga [145005] (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145005].levelList[level=1].desc
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [145005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność wroga [145005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność wroga [145005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [145006] (ulepszenie 1) — nazwa] 범 사냥
   źródło: Skills_Abnormality-exme.json :: dataList[id=145006].levelList[level=1].name
   limit: do 40 znaków
   EN: Tiger Hunt
   PL: Tiger Hunt
526. [Umiejętność wroga [145006] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 6 이상이면, 모든 코인이 [SuperCoin]이 됨\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145006].levelList[level=1].desc
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność wroga [145006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność wroga [145006] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145006].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [145006] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145006].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [145007] (ulepszenie 1) — nazwa] 범 가르기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145007].levelList[level=1].name
   limit: do 40 znaków
   EN: Tigersplitter
   PL: Tigersplitter
531. [Umiejętność wroga [145007] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 3 이하면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +20%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145007].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Laceration], [ChoiSwordsmanship], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], deal +40% damage on Critical Hit\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>At 3 or fewer [ChoiSwordsmanship], convert all Coins into [SuperCoin]s and deal +20% damage on Critical Hit</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] przy 8+ [Breath] zadaje +40% obrażeń przy trafieniu krytycznym\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>przy 3 lub mniej [ChoiSwordsmanship] wszystkie Monety zmieniają się w [SuperCoin]y i zadaje +20% obrażeń przy trafieniu krytycznym</u></b></mark></color>\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
532. [Umiejętność wroga [145007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 2
533. [Umiejętność wroga [145007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Umiejętność wroga [145007] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145007].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność wroga [145007] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145007].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność wroga [145009] (ulepszenie 1) — nazwa] 본국검[살] - 가다듬기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145009].levelList[level=1].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [145009] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n조력자와 [CantDuel]\n수감자를 대상으로 우선 지정함\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 감소</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-exme.json :: dataList[id=145009].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [CantDuel], [SupportProtect], [SuperCoin], [StartDuel], [EndSkill]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [CantDuel] = [합 불가능] / [Unclashable]; [SupportProtect] = 원호 방어 / Assist Defense; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Unaffected by [ChoiSwordsmanship]\n[CantDuel] with Assist Units\nPrioritizes Sinners\nIf target's Skill is [SupportProtect] Exclusive Skill, convert into [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>Lose 3 [ChoiSwordsmanship]</color></mark></b></u>\n- If target's Skill is [SupportProtect] Exclusive Skill, this effect does not activate\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>On Hit as an Unopposed Attack, or On Hit against target that used [SupportProtect] Exclusive Skill, gain 2 [ChoiSwordsmanship]</color></mark></b></u>
   PL: nie podlega wpływowi [ChoiSwordsmanship]\n[CantDuel] z jednostkami wsparcia\npriorytet: Grzesznicy\njeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], zmienia się w [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>traci 3 [ChoiSwordsmanship]</u></b></mark></color>\n- jeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], ten efekt nie uruchamia się\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przy trafieniu jako Atak Jednostronny albo przy trafieniu celu, który użył Umiejętności wyłącznie dla [SupportProtect], zyskuje 2 [ChoiSwordsmanship]</u></b></mark></color>
538. [Umiejętność wroga [145010] (ulepszenie 1) — nazwa] 본국검[살] - 벼리기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145010].levelList[level=1].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Umiejętność wroga [145010] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n조력자와 [CantDuel]\n수감자를 대상으로 우선 지정함\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 얻음</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 감소</color></mark></b></u>
   źródło: Skills_Abnormality-exme.json :: dataList[id=145010].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [CantDuel], [SupportProtect], [SuperCoin], [StartDuel], [EndSkill]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [CantDuel] = [합 불가능] / [Unclashable]; [SupportProtect] = 원호 방어 / Assist Defense; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Unaffected by [ChoiSwordsmanship]\n[CantDuel] with Assist Units\nPrioritizes Sinners\nIf target's Skill is [SupportProtect] Exclusive Skill, convert into [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>Gain 3 [ChoiSwordsmanship]</color></mark></b></u>\n- If target's Skill is [SupportProtect] Exclusive Skill, this effect does not activate\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>On Hit as an Unopposed Attack, or On Hit against target that used [SupportProtect] Exclusive Skill, lose 2 [ChoiSwordsmanship]</color></mark></b></u>
   PL: nie podlega wpływowi [ChoiSwordsmanship]\n[CantDuel] z jednostkami wsparcia\npriorytet: Grzesznicy\njeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], zmienia się w [SuperCoin]\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>zyskuje 3 [ChoiSwordsmanship]</u></b></mark></color>\n- jeżeli Umiejętność celu jest Umiejętnością wyłącznie dla [SupportProtect], ten efekt nie uruchamia się\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przy trafieniu jako Atak Jednostronny albo przy trafieniu celu, który użył Umiejętności wyłącznie dla [SupportProtect], traci 2 [ChoiSwordsmanship]</u></b></mark></color>
540. [Umiejętność wroga [145011] (ulepszenie 1) — nazwa] 본국궁[살] - 살 날리기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].name
   limit: do 60 znaków
   EN: Bow of the Homeland [Sal] - Arrowloose
   PL: Bow of the Homeland [Sal] - Arrowloose
541. [Umiejętność wroga [145011] (ulepszenie 1) — opis] <color=#ff6000><mark color=#ff000040><b><u>[Laceration]이 가장 많은 적을 대상으로 함</color></mark></b></u>\n[ChoiSwordsmanship]의 영향을 받지 않음\n[WhenUse] 자신의 [Breath] 위력 3 소모하여 최종 위력 +2
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Laceration], [ChoiSwordsmanship], [WhenUse], [Breath]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <color=#ff6000><mark color=#ff000040><b><u>Targets the enemy that has the most [Laceration]</color></mark></b></u>\nUnaffected by [ChoiSwordsmanship]\n[WhenUse] Consume 3 [Breath] Potency on self to gain Final Power +2
   PL: <color=#ff6000><mark color=#ff000040><b><u>cel: wróg z największą liczbą [Laceration]</u></b></mark></color>\nnie podlega wpływowi [ChoiSwordsmanship]\n[WhenUse] zużywa 3 Siły [Breath] jednostki, aby zyskać Końcową Moc +2
542. [Umiejętność wroga [145011] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Umiejętność wroga [145011] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +4 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 4
544. [Umiejętność wroga [145011] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 흐트러짐 손상 10
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Raise Stagger Threshold by 10
   PL: [UnBrokenCoinOnSucceedAttack] podnosi Próg Oszołomienia o 10
545. [Umiejętność wroga [145011] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Binding] w następnej turze
546. [Umiejętność wroga [145011] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Vulnerable] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145011].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Vulnerable]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Vulnerable]
547. [Umiejętność wroga [145012] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Abnormality-exme.json :: dataList[id=145012].levelList[level=1].name
   limit: do 40 znaków
   EN: Guardform
   PL: Guardform
548. [Umiejętność wroga [145012] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n[StartBattle] [Breath] 5 얻음, 자신의 [Breath] 횟수 5 증가\n[WhenUse] 다음 턴에 [CriticalDamageUp] 2 얻음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145012].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [ChoiSwordsmanship], [StartBattle], [Breath], [WhenUse], [CriticalDamageUp]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up
   EN: Unaffected by [ChoiSwordsmanship]\n[StartBattle] Gain 5 [Breath] and +5 [Breath] Count\n[WhenUse] Gain 2 [CriticalDamageUp] next turn
   PL: nie podlega wpływowi [ChoiSwordsmanship]\n[StartBattle] zyskuje 5 [Breath] i +5 Licznika [Breath]\n[WhenUse] zyskuje 2 [CriticalDamageUp] w następnej turze
549. [Umiejętność wroga [145013] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-exme.json :: dataList[id=145013].levelList[level=1].name
   limit: do 40 znaków
   EN: Counterform
   PL: Counterform
550. [Umiejętność wroga [145013] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n[StartBattle] [Breath] 5 얻음, 자신의 [Breath] 횟수 5 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145013].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [ChoiSwordsmanship], [StartBattle], [Breath]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: Unaffected by [ChoiSwordsmanship]\n[StartBattle] Gain 5 [Breath] and +5 [Breath] Count
   PL: nie podlega wpływowi [ChoiSwordsmanship]\n[StartBattle] zyskuje 5 [Breath] i +5 Licznika [Breath]
551. [Umiejętność wroga [145013] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145013].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność wroga [145013] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145013].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność wroga [145101] (ulepszenie 1) — nazwa] 소 가르기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145101].levelList[level=1].name
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [145101] (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145101].levelList[level=1].desc
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [145101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [145101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność wroga [145102] (ulepszenie 1) — nazwa] 곰 가르기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145102].levelList[level=1].name
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność wroga [145102] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 6 이상이면, 모든 코인이 [SuperCoin]이 됨\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145102].levelList[level=1].desc
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność wroga [145102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność wroga [145102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [145103] (ulepszenie 1) — nazwa] 곰 허리 끊기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145103].levelList[level=1].name
   (powtórzenie elementu 516 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność wroga [145103] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChoiSwordsmanship]이 6을 초과하면, 초과하는 값만큼 <noparse>최종 위력 증가</noparse> (최대 3)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 7 이상이면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +20%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145103].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Laceration], [ChoiSwordsmanship], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], deal +40% damage on Critical Hit\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] At more than 6 [ChoiSwordsmanship], gain Final Power for every excess [ChoiSwordsmanship] Stack (max 3)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>At 7+ [ChoiSwordsmanship], convert all Coins into [SuperCoin]s and deal +20% damage on Critical Hit</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] przy 8+ [Breath] zadaje +40% obrażeń przy trafieniu krytycznym\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] przy więcej niż 6 [ChoiSwordsmanship] zyskuje Końcową Moc za każdy nadmiarowy Licznik [ChoiSwordsmanship] (maks. 3)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>przy 7+ [ChoiSwordsmanship] wszystkie Monety zmieniają się w [SuperCoin]y i zadaje +20% obrażeń przy trafieniu krytycznym</u></b></mark></color>\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
563. [Umiejętność wroga [145103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność wroga [145103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Umiejętność wroga [145104] (ulepszenie 1) — nazwa] 산군도 이 칼끝 아래 두동강나리
   źródło: Skills_Abnormality-exme.json :: dataList[id=145104].levelList[level=1].name
   limit: do 60 znaków
   EN: Even Sanguns Shall Be Cleft Under This Sword
   PL: Even Sanguns Shall Be Cleft Under This Sword
566. [Umiejętność wroga [145104] (ulepszenie 1) — opis] [Laceration]이 가장 많은 적을 대상으로 함\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 [ChoiSwordsmanship]이 6을 초과하면, 초과하는 값당 최종 위력 +2 (최대 6)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>이 스킬은 [Breath] 횟수를 소모하지 않고 반드시 스킬 코인이 앞면으로 결정되고 크리티컬로 적중함</color></mark></b></u>\n[BeforeAttack] 자신의 [ChoiSwordsmanship] 2당 크리티컬 피해량 +20% (최대 80%)\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145104].levelList[level=1].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Laceration], [WhenUse], [ChoiSwordsmanship], [WinDuel], [Breath], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy that has the most [Laceration]\n[WhenUse] Cannot be Staggered from taking damage until this Skill ends\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)\n[WhenUse] At more than 6 [ChoiSwordsmanship], gain Final Power +2 for every excess [ChoiSwordsmanship] Stack (max 6)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>This Skill always flips Head, hits Critically, and does not consume [Breath] Count</color></mark></b></u>\n[BeforeAttack] Deal +20% damage on Critical Hit for every 2 [ChoiSwordsmanship] on self (max 80%)\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: cel: wróg z największą liczbą [Laceration]\n[WhenUse] nie przechodzi w Oszołamienie od otrzymanych obrażeń do zakończenia tej Umiejętności\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 3)\n[WhenUse] przy więcej niż 6 [ChoiSwordsmanship] zyskuje Końcową Moc +2 za każdy nadmiarowy Licznik [ChoiSwordsmanship] (maks. 6)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>ta Umiejętność zawsze wyrzuca Awers, trafia krytycznie i nie zużywa Licznika [Breath]</u></b></mark></color>\n[BeforeAttack] zadaje +20% obrażeń przy trafieniu krytycznym za każde 2 [ChoiSwordsmanship] tej jednostki (maks. 80%)\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
567. [Umiejętność wroga [145104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność wroga [145104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인의 최종 피해량의 (자신의 [Breath] X 10)%만큼 참격 피해 (최대 100%)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Deal (([Breath] on self x 10)% of this Coin's final damage) Slash damage (max 100%)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Cięcia równe ([Breath] tej jednostki x 10)% końcowych obrażeń tej Monety (maks. 100%)
569. [Umiejętność wroga [145104] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인의 최종 피해량의 (대상의 [Laceration] X 10)%만큼 색욕 피해 (최대 100%)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145104].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Deal (([Laceration] on target x 10)% of this Coin's final damage) Lust damage (max 100%)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Żądzy równe ([Laceration] celu x 10)% końcowych obrażeń tej Monety (maks. 100%)
570. [Umiejętność wroga [145104] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145104].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [145105] (ulepszenie 1) — nazwa] 본국검범 - 살 베기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145105].levelList[level=1].name
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność wroga [145105] (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-exme.json :: dataList[id=145105].levelList[level=1].desc
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [145105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Umiejętność wroga [145105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [145105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność wroga [145106] (ulepszenie 1) — nazwa] 범 사냥
   źródło: Skills_Abnormality-exme.json :: dataList[id=145106].levelList[level=1].name
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność wroga [145106] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 6 이상이면, 모든 코인이 [SuperCoin]이 됨\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145106].levelList[level=1].desc
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [145106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność wroga [145106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność wroga [145106] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145106].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [145107] (ulepszenie 1) — nazwa] 범 가르기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145107].levelList[level=1].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [145107] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 크리티컬 피해량 +40%\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 [ChoiSwordsmanship]이 3 이하면, 모든 코인이 [SuperCoin]으로 변경되고 크리티컬 피해량 +20%</color></mark></b></u>\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145107].levelList[level=1].desc
   (powtórzenie elementu 531 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [145107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność wroga [145107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Umiejętność wroga [145107] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145107].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [145107] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [SlashResistDown] 1 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145107].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność wroga [145108] (ulepszenie 1) — nazwa] 어떤 산범들의 살이든 가르리
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność wroga [145108] (ulepszenie 1) — opis] [Laceration]이 가장 많은 적을 대상으로 함\n<color=#ff6000><mark color=#ff000040><b><u>속도와 상관없이 이 스킬과 합을 할 수 있음</color></mark></b></u>\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 대상의 [Laceration] 4당 최종 위력 +1 (최대 3)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>이 스킬은 [Breath]을 소모하지 않고 반드시 스킬 코인이 앞면으로 결정되고 크리티컬로 적중함</color></mark></b></u>\n[BeforeAttack] 자신의 [Breath] 2당 크리티컬 피해량 +20% (최대 80%)\n[DefeatDuel]\n- 피해량 -80%\n- 크리티컬이 발동하지 않음\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Laceration], [WhenUse], [WinDuel], [Breath], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy that has the most [Laceration]\n<color=#ff6000><mark color=#ff000040><b><u>Can Clash with this Skill regardless of Speed</color></mark></b></u>\n[WhenUse] Cannot be Staggered from taking damage until this Skill ends\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>This Skill always flips Head, hits Critically, and does not consume [Breath] Count</color></mark></b></u>\n[BeforeAttack] Deal +20% damage on Critical Hit for every 2 [Breath] on self (max 80%)\n[DefeatDuel]\n- Deal -80% damage\n- Does not hit Critically\n- Damage dealt by this Skill cannot Stagger the target
   PL: cel: wróg z największą liczbą [Laceration]\n<color=#ff6000><mark color=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[WhenUse] nie przechodzi w Oszołamienie od otrzymanych obrażeń do zakończenia tej Umiejętności\n[WhenUse] Końcowa Moc +1 za każde 4 [Laceration] celu (maks. 3)\n[WinDuel] <color=#ff6000><mark color=#ff000040><b><u>ta Umiejętność zawsze wyrzuca Awers, trafia krytycznie i nie zużywa Licznika [Breath]</u></b></mark></color>\n[BeforeAttack] zadaje +20% obrażeń przy trafieniu krytycznym za każde 2 [Breath] tej jednostki (maks. 80%)\n[DefeatDuel]\n- zadaje o 80% mniej obrażeń\n- nie trafia krytycznie\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
589. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 메인 타겟의 [Laceration]이 10 이상이면, 이 코인이 적중한 대상의 [Laceration] 횟수 8 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [145108] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 8 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145108].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [145109] (ulepszenie 1) — nazwa] 본국검[살] - 가다듬기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145109].levelList[level=1].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [145109] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n조력자와 [CantDuel]\n수감자를 대상으로 우선 지정함\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 감소</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-exme.json :: dataList[id=145109].levelList[level=1].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [145110] (ulepszenie 1) — nazwa] 본국검[살] - 벼리기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145110].levelList[level=1].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność wroga [145110] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n조력자와 [CantDuel]\n수감자를 대상으로 우선 지정함\n대상의 스킬이 [SupportProtect] 전용 스킬인 경우, [SuperCoin]이 됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanship] 3 얻음</color></mark></b></u>\n- 대상의 스킬이 [SupportProtect] 전용 스킬인 경우 이 효과가 발동하지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>일방 공격이거나 [SupportProtect] 전용 스킬을 사용한 대상에게 적중한 경우, [ChoiSwordsmanship] 2 감소</color></mark></b></u>
   źródło: Skills_Abnormality-exme.json :: dataList[id=145110].levelList[level=1].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [145111] (ulepszenie 1) — nazwa] 본국궁[살] - 살 날리기
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].name
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność wroga [145111] (ulepszenie 1) — opis] <color=#ff6000><mark color=#ff000040><b><u>[Laceration]이 가장 많은 적을 대상으로 함</color></mark></b></u>\n[ChoiSwordsmanship]의 영향을 받지 않음\n[WhenUse] 자신의 [Breath] 위력 3 소모하여 최종 위력 +2
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].desc
   (powtórzenie elementu 541 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [145111] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [145111] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [145111] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 흐트러짐 손상 10
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność wroga [145111] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność wroga [145111] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Vulnerable] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145111].levelList[level=1].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [145112] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Abnormality-exme.json :: dataList[id=145112].levelList[level=1].name
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [145112] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n[StartBattle] [Breath] 5 얻음, 자신의 [Breath] 횟수 5 증가\n[WhenUse] 다음 턴에 [CriticalDamageUp] 2 얻음
   źródło: Skills_Abnormality-exme.json :: dataList[id=145112].levelList[level=1].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [145113] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-exme.json :: dataList[id=145113].levelList[level=1].name
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [145113] (ulepszenie 1) — opis] [ChoiSwordsmanship]의 영향을 받지 않음\n[StartBattle] [Breath] 5 얻음, 자신의 [Breath] 횟수 5 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145113].levelList[level=1].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność wroga [145113] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-exme.json :: dataList[id=145113].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [145113] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-exme.json :: dataList[id=145113].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [exme] Umiejętności wrogów / Anomalii — Skills_Enemy-exme
- grupa rozdziału/trybu: `exme` · plik: `Skills_Enemy-exme.json`

618. [Umiejętność wroga [9105701] (ulepszenie 1) — nazwa] 격세
   źródło: Skills_Enemy-exme.json :: dataList[id=9105701].levelList[level=1].name
   limit: do 40 znaków
   EN: Striker’s Stance
   PL: Striker’s Stance
619. [Umiejętność wroga [9105701] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 기본 위력 +1\n[WhenUse] [Breath] 2 얻음\n[DefeatDuel] [Breath] 3 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105701].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 6+ [Breath], Base Power +1\n[WhenUse] Gain 2 [Breath]\n[DefeatDuel] Gain 3 [Breath]
   PL: [WhenUse] przy 6+ [Breath] Moc Bazowa +1\n[WhenUse] zyskuje 2 [Breath]\n[DefeatDuel] zyskuje 3 [Breath]
620. [Umiejętność wroga [9105701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-exme.json :: dataList[id=9105701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [9105702] (ulepszenie 1) — nazwa] 자법
   źródło: Skills_Enemy-exme.json :: dataList[id=9105702].levelList[level=1].name
   limit: do 40 znaków
   EN: Acupuncture
   PL: Acupuncture
622. [Umiejętność wroga [9105702] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 기본 위력 +2\n[DefeatDuel] [Breath] 5 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 8+ [Breath], Base Power +2\n[DefeatDuel] Gain 5 [Breath]
   PL: [WhenUse] przy 8+ [Breath] Moc Bazowa +2\n[DefeatDuel] zyskuje 5 [Breath]
623. [Umiejętność wroga [9105702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-exme.json :: dataList[id=9105702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [9105702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-exme.json :: dataList[id=9105702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [9105702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedAttack] Gain 1 [SlashDamageUp] next turn
   PL: [OnSucceedAttack] zyskuje 1 [SlashDamageUp] w następnej turze
626. [Umiejętność wroga [9105703] (ulepszenie 1) — nazwa] 연참
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].name
   limit: do 40 znaków
   EN: Slash Series
   PL: Slash Series
627. [Umiejętność wroga [9105703] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 4당, 기본 위력 +1 (최대 5)\n[DefeatDuel] 기본 위력 13 감소\n[DefeatDuel] 이 스킬로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [Breath] 전부 소모
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Base Power +1 for every 4 [Breath] on self (max 5)\n[DefeatDuel] Base Power -13\n[DefeatDuel] This Skill cannot Stagger the target\n[EndSkill] Consume all [Breath] on self
   PL: [WhenUse] Moc Bazowa +1 za każde 4 [Breath] jednostki (maks. 5)\n[DefeatDuel] Moc Bazowa -13\n[DefeatDuel] ta Umiejętność nie Oszołomi celu\n[EndSkill] zużywa cały [Breath] jednostki
628. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Breath] 4 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 4 [Breath] next turn
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 4 [Breath] w następnej turze
630. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration]
632. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +70%
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +70% damage on Critical Hit
   PL: zadaje +70% obrażeń przy trafieniu krytycznym
634. [Umiejętność wroga [9105703] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-exme.json :: dataList[id=9105703].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +2 Licznika [Laceration]
635. [Umiejętność wroga [9105704] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-exme.json :: dataList[id=9105704].levelList[level=1].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [9105704] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-exme.json :: dataList[id=9105704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 6+ [Breath], Base Power +1
   PL: [WhenUse] przy 6+ [Breath] Moc Bazowa +1
637. [Umiejętność wroga [9105704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL: [OnSucceedAttack] zyskuje 5 [Breath]
638. [Umiejętność wroga [9105801] (ulepszenie 1) — nazwa] 격세
   źródło: Skills_Enemy-exme.json :: dataList[id=9105801].levelList[level=1].name
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [9105801] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 기본 위력 +1\n[WhenUse] [Breath] 2 얻음\n[DefeatDuel] [Breath] 3 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105801].levelList[level=1].desc
   (powtórzenie elementu 619 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [9105801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-exme.json :: dataList[id=9105801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [9105802] (ulepszenie 1) — nazwa] 자법
   źródło: Skills_Enemy-exme.json :: dataList[id=9105802].levelList[level=1].name
   (powtórzenie elementu 621 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność wroga [9105802] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 8 이상이면, 기본 위력 +2\n[DefeatDuel] [Breath] 5 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105802].levelList[level=1].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [9105802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-exme.json :: dataList[id=9105802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [9105802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-exme.json :: dataList[id=9105802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [9105802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 625 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność wroga [9105803] (ulepszenie 1) — nazwa] 연참
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].name
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność wroga [9105803] (ulepszenie 1) — opis] 대상의 체력이 50% 미만이면, 최종 위력 +2\n[WhenUse] 자신의 [Breath] 4당, 기본 위력 +1 (최대 5)\n[DefeatDuel] 기본 위력 13 감소\n[DefeatDuel] 이 스킬로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [Breath] 전부 소모
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If target is at less than 50% HP, Final Power +2\n[WhenUse] Base Power +1 for every 4 [Breath] on self (max 5)\n[DefeatDuel] Base Power -13\n[DefeatDuel] This Skill cannot Stagger the target\n[EndSkill] Consume all [Breath] on self
   PL: jeżeli HP celu jest niższe niż 50%, Końcowa Moc +2\n[WhenUse] Moc Bazowa +1 za każde 4 [Breath] jednostki (maks. 5)\n[DefeatDuel] Moc Bazowa -13\n[DefeatDuel] ta Umiejętność nie Oszołomi celu\n[EndSkill] zużywa cały [Breath] jednostki
648. [Umiejętność wroga [9105803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [9105803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Umiejętność wroga [9105803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność wroga [9105803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność wroga [9105803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [9105803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Enemy-exme.json :: dataList[id=9105803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL: [CriticalOnSucceedAttack] podnosi Próg Oszołomienia o 20% zadanych obrażeń
654. [Umiejętność wroga [9105804] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-exme.json :: dataList[id=9105804].levelList[level=1].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [9105804] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-exme.json :: dataList[id=9105804].levelList[level=1].desc
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność wroga [9105804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_Enemy-exme.json :: dataList[id=9105804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [exme] Pasywka wroga: Passives_Abnormality-exme
- plik gry: `Passives_Abnormality-exme.json`

657. [[exme] Pasywka wroga [145004] — nazwa] 지끈거리는 기억
   źródło: Passives_Abnormality-exme.json :: dataList[id=145004].name
   limit: do 40 znaków
   EN: Headsplitting Memory
   PL: Headsplitting Memory
658. [[exme] Pasywka wroga [145004] — opis] 합 패배 시 [RegretSCorp] 1 얻음 (턴당 1회)
   źródło: Passives_Abnormality-exme.json :: dataList[id=145004].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RegretSCorp]
   znaczenie tagów: [RegretSCorp] = 지끈거리는 기억 / Headsplitting Memory
   EN: On Clash Lose, gain 1 [RegretSCorp] (once per turn)
   PL: po przegranej w Starciu zyskuje 1 [RegretSCorp] (1 raz na turę)
659. [[exme] Pasywka wroga [144804] — nazwa] 추노꾼
   źródło: Passives_Abnormality-exme.json :: dataList[id=144804].name
   limit: do 40 znaków
   EN: Ch'unokkun
   PL: Ch'unokkun
660. [[exme] Pasywka wroga [144804] — opis] 대상에게 [TiedRope]을 부여하는데 성공했으면, [TiedWithRope] 얻음
   źródło: Passives_Abnormality-exme.json :: dataList[id=144804].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TiedRope], [TiedWithRope]
   znaczenie tagów: [TiedRope] = 포박 / Trussed; [TiedWithRope] = 압송 채비 / Prisoner Transport Arrangements
   EN: If this unit inflicted [TiedRope] on target, gain [TiedWithRope]
   PL: jeżeli jednostka nałożyła [TiedRope] na cel, zyskuje [TiedWithRope]
661. [[exme] Pasywka wroga [144804] — tekst klimatyczny] S사의 금기 사냥꾼은 크게 어사와 추노꾼으로 나뉜다.\n어사는 조정에 속한 자들로, 대개 단독으로 움직인다. 신분을 감추고 암행하며, 금기를 어긴 자들을 추적한다.\n추노꾼은 해결사 사무소와 같이 저마다 패거리를 만든다. 이들에게 어떤 노비를, 어떤 낙인을 쫓아야 하는지 명령이나 의뢰가 하달되면, 각 패거리의 방식으로 추쇄를 시작한다. 그러한 추노에는 예도 격도 없다.
   źródło: Passives_Abnormality-exme.json :: dataList[id=144804].flavor
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n
   EN: S Corp. commands two sorts of Taboo Hunters: The Royal Censors and the Ch'unokkuns.\nAgents of the Royal Court, the Royal Censors generally operate alone, moving undercover to pursue those who have dared to break the Taboo of Salpippyeo.\nCh'unokkuns, much like Fixer Offices, form bands within their own ranks. Once an order or a contract to hunt down a Branded is bestowed upon them, each band hunts its mark in the manner preferred by the band. The hunt for Nobi knows neither honor nor dignity.
   PL: Korporacja S wydaje polecenia dwóm rodzajom Łowców Tabu: Królewskim Cenzorom i Ch'unokkunom.\nCenzorzy, należący do dworu królewskiego, poruszają się na ogół samotnie — w ukryciu tropią tych, którzy ośmielili się złamać Tabu Salpippyeo.\nCh'unokkunowie, niczym biura fixerów, tworzą własne zgrupowania. Gdy otrzymają rozkaz albo zlecenie polowania na Oznaczonego, każde zgrupowanie rusza na obławy po swojemu. Polowanie na Nobi nie zna ani honoru, ani godności.
662. [[exme] Pasywka wroga [144801] — nazwa] 추쇄건[推刷巾]
   źródło: Passives_Abnormality-exme.json :: dataList[id=144801].name
   limit: do 40 znaków
   EN: Scouring Hunterband [推刷巾]
   PL: Scouring Hunterband [推刷巾]
663. [[exme] Pasywka wroga [144801] — opis] 대상의 [Binding] 1당, 가하는 피해량 +5% (최대 15%)
   źródło: Passives_Abnormality-exme.json :: dataList[id=144801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Deal +5% damage for every 1 [Binding] on target (max 15%)
   PL: zadaje +5% obrażeń za każdy 1 [Binding] celu (maks. 15%)
664. [[exme] Pasywka wroga [144801] — tekst klimatyczny] 눈을 가렸다고 해서 보이지 않는 것은 아니다.\nQ사의 특이점으로 만들어진 이 천은 안대와 이마띠를 비롯한 여러 형태로 가공되어, 동부 전역에 널리 퍼져있다. 그렇기에 동부에서는 머리나 얼굴에 천을 두른 해결사나 회사의 직원들을 볼 수 있다.\n그 역할은 도시의 선글라스나 바이저, 전투용 의안과 동일하다. 실시간으로 상대의 정보를 읽어내고, 시야를 보조하며, 상황을 분석해 준다. 때로는 멀리 떨어진 동료와 통신할 수도 있다.
   źródło: Passives_Abnormality-exme.json :: dataList[id=144801].flavor
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To cover the eyes is not to be blind.\nThese fabrics, created using Q Corp.'s Singularity, are fashioned into many forms, such as blindfolds and headbands, and are commonly used throughout the East. It is not unusual to see Fixers and employees of corporate entities in the East covering their heads and faces with these products.\nThe fabrics serve the same function as sunglasses, visors, and combat prosthetic eyes found elsewhere in the City. They scan the target's information in real time, augment the wearer's vision, and provide tactical analysis. At times, they can also serve as a means of communication with distant allies.
   PL: Zasłonić oczy nie znaczy nie widzieć.\nTe tkaniny, stworzone dzięki Singularności korporacji Q, przetwarzane są w rozmaite formy — od opasek na oczy po opaski na czoło — i powszechnie używane na całym Wschodzie. Niczego dziwnego, że na Wschodzie fixerzy i pracownicy korporacji owijają głowę i twarz tymi wyrobami.\nPełnią tę samą funkcję co okulary przeciwsłoneczne, wizery i bojowe protezy oczu w innych częściach Miasta: odczytują w czasie rzeczywistym dane celu, wspomagają widzenie noszącego i analizują sytuację. Niekiedy służą też jako środek łączności z dalekimi sojusznikami.
665. [[exme] Pasywka wroga [144802] — nazwa] 흔적 추적
   źródło: Passives_Abnormality-exme.json :: dataList[id=144802].name
   limit: do 40 znaków
   EN: Tracking Traces
   PL: Tracking Traces
666. [[exme] Pasywka wroga [144802] — opis] 합 승리 시 대상의 [ScratchesHurt] 수치 1당, [Breath] 2 얻음
   źródło: Passives_Abnormality-exme.json :: dataList[id=144802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ScratchesHurt], [Breath]
   znaczenie tagów: [ScratchesHurt] = 찢긴 상처 / Avulsion Wound; [Breath] = 호흡 / Poise
   EN: On Clash Win, gain 2 [Breath] for every [ScratchesHurt] on target
   PL: po wygranej w Starciu zyskuje 2 [Breath] za każdy Licznik [ScratchesHurt] celu
667. [[exme] Pasywka wroga [144803] — nazwa] 오랏줄 걸기
   źródło: Passives_Abnormality-exme.json :: dataList[id=144803].name
   limit: do 40 znaków
   EN: Throwing the Ohra Bond
   PL: Throwing the Ohra Bond
668. [[exme] Pasywka wroga [144803] — opis] 공격 적중 시 대상이 흐트러짐 상태에 빠지면, 다음 턴에 [Binding] 2 부여 (턴당 1회)
   źródło: Passives_Abnormality-exme.json :: dataList[id=144803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: On Hit, if target is Staggered, inflict 2 [Binding] next turn (once per turn)
   PL: przy trafieniu, jeżeli cel wpada w Oszołamienie, nakłada 2 [Binding] w następnej turze (1 raz na turę)
669. [[exme] Pasywka wroga [144805] — nazwa] 명령 수행
   źródło: Passives_Abnormality-exme.json :: dataList[id=144805].name
   limit: do 40 znaków
   EN: Undertake Orders
   PL: Undertake Orders
670. [[exme] Pasywka wroga [144805] — opis] 이번 전투 동안 [SlaveHunersPower] 얻음
   źródło: Passives_Abnormality-exme.json :: dataList[id=144805].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SlaveHunersPower]
   znaczenie tagów: [SlaveHunersPower] = 압송 명령 / Prisoner Transport Order
   EN: Gain [SlaveHunersPower] for this Encounter
   PL: zyskuje [SlaveHunersPower] na czas tej walki
671. [[exme] Pasywka wroga [145201] — nazwa] 정렬된 정보
   źródło: Passives_Abnormality-exme.json :: dataList[id=145201].name
   limit: do 40 znaków
   EN: Arranged Information
   PL: Arranged Information
672. [[exme] Pasywka wroga [145201] — opis] 적에게 [TakePicture]를 부여했으면, 정신력 10 회복
   źródło: Passives_Abnormality-exme.json :: dataList[id=145201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TakePicture]
   znaczenie tagów: [TakePicture] = 정보 취득 / Intelligence Gathering
   EN: If this unit inflicted [TakePicture] on an enemy, heal 10 SP
   PL: jeżeli jednostka nałożyła [TakePicture] na wroga, przywraca 10 SP
673. [[exme] Pasywka wroga [145202] — nazwa] 견고한 못질
   źródło: Passives_Abnormality-exme.json :: dataList[id=145202].name
   limit: do 40 znaków
   EN: Firm Nailing
   PL: Firm Nailing
674. [[exme] Pasywka wroga [145202] — opis] 적에게 [VibrationExplosion] 시, 대상의 [LensmanNail] 수치만큼 흐트러짐 손상을 입힘
   źródło: Passives_Abnormality-exme.json :: dataList[id=145202].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [LensmanNail]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [LensmanNail] = 고정 못 / Pinning Nail
   EN: On triggering [VibrationExplosion] on an enemy, raise target's Stagger Threshold by [LensmanNail] Stack
   PL: przy uruchomieniu [VibrationExplosion] na wrogu podnosi Próg Oszołomienia celu o Licznik [LensmanNail]
675. [[exme] Pasywka wroga [145204] — nazwa] 명령 수행
   źródło: Passives_Abnormality-exme.json :: dataList[id=145204].name
   (powtórzenie elementu 669 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [[exme] Pasywka wroga [145204] — opis] 이번 전투 동안 [LensmanPower] 얻음
   źródło: Passives_Abnormality-exme.json :: dataList[id=145204].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LensmanPower]
   znaczenie tagów: [LensmanPower] = 조사 명령 / Investigation Order
   EN: Gain [LensmanPower] for this Encounter
   PL: zyskuje [LensmanPower] na czas tej walki
677. [[exme] Pasywka wroga [145001] — nazwa] 본국검술[살] - 대환도
   źródło: Passives_Abnormality-exme.json :: dataList[id=145001].name
   limit: do 70 znaków
   EN: Swordplay of the Homeland [Sal] - Great Hwando
   PL: Swordplay of the Homeland [Sal] - Great Hwando
678. [[exme] Pasywka wroga [145001] — opis] 스테이지 시작시 [ChoiSwordsmanship] 5 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>3턴 마다 자신의 본국태세를 변경함</color></mark></b></u>\n\n턴 종료시 보호막을 보유한 상태면, 다음 턴에 [Breath] 5, [Breath] 횟수 2 얻음\n\n아래 조건 만족 시 ‘본국궁 - 살 날리기’가 포함된 패턴을 사용함\n- 2턴 연속으로 모든 합에서 졌을 시 (일방 공격은 체크하지 않음) \n- 흐트러진 다음 턴\n- 사기저하 및 패닉 시
   źródło: Passives_Abnormality-exme.json :: dataList[id=145001].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [Breath]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [Breath] = 호흡 / Poise
   EN: Encounter Start: Gain 5 [ChoiSwordsmanship]\n\n<color=#ff6000><mark color=#ff000040><b><u>Assume a different Battleform of the Homeland every 3 turns</color></mark></b></u>\n\nTurn End: If this unit has Shield, gain 5 [Breath] and +2 [Breath] Count next turn\n\nWhen the following conditions are met, use a pattern that includes the "Bow of the Homeland - Arrowloose" Skill\n- When this unit lost all Clashes for 2 turns in a row (does not check for Unopposed Attacks)\n- In the turn after the turn in which this unit spent in Stagger\n- When in Low Morale or Panic
   PL: Początek walki: zyskuje 5 [ChoiSwordsmanship]\n\n<color=#ff6000><mark color=#ff000040><b><u>co 3 tury zmienia Formę Bojową Ojczyzny</u></b></mark></color>\n\nna koniec tury, jeżeli jednostka ma Tarczę, zyskuje 5 [Breath] i +2 Licznika [Breath] w następnej turze\n\nprzy spełnieniu poniższych warunków używa wzorca zawierającego Umiejętność „Bow of the Homeland - Arrowloose”\n- po przegraniu wszystkich Starć przez 2 tury z rzędu (Ataki Jednostronne nie są sprawdzane)\n- w turze następującej po turze spędzonej w Oszołamieniu\n- przy Niskim Morale albo w Panice
679. [[exme] Pasywka wroga [145001] — tekst klimatyczny] S사에서 전승되는 본국검 또한 살·피·뼈, 세 갈래로 나뉜다.\n그중에는 산군과 같은 거대한 존재를 베어내기 위한 검술도 전해진다.\n그러한 검술을 온전히 펼치기 위해서는, 그에 걸맞은 거대한 환도가 필요하다.
   źródło: Passives_Abnormality-exme.json :: dataList[id=145001].flavor
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Sword of the Homeland, S Corp.'s traditional art of swordsmanship, is also divided into three branches: Sal, Pi, and Ppyeo.\nWithin their teachings exist techniques to hew and cleave through creatures of colossal stature such as Sanguns.\nTo perform them in full, a swordsman must wield a great hwando capable of bearing the strain of the techniques.
   PL: Sztuka miecza Ojczyzny, przekazywana w korporacji S, także dzieli się na trzy gałęzie: Sal, Pi i Ppyeo.\nWśród jej nauk przekazywane są techniki służące do rąbania potężnych stworzeń, takich jak Sanguny.\nAby rozwinąć je w pełni, szermierz musi dzierżyć wielkie hwando, zdolne znieść ciężar tych technik.
680. [[exme] Pasywka wroga [145002] — nazwa] 두정갑[살] - 철벽
   źródło: Passives_Abnormality-exme.json :: dataList[id=145002].name
   limit: do 60 znaków
   EN: Dujeong Brigandine [Sal] - Iron Bulwark
   PL: Dujeong Brigandine [Sal] - Iron Bulwark
681. [[exme] Pasywka wroga [145002] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -30% (소수점 버림)\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨\n\n스테이지 첫 등장 시 [ChoiSwordsmanshipShield] 5 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>[ChoiSwordsmanshipShield]이 소멸되었으면 전투 종료</color></mark></b></u>
   źródło: Passives_Abnormality-exme.json :: dataList[id=145002].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [PanicChangeLock], [ChoiSwordsmanshipShield]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [ChoiSwordsmanshipShield] = 두정갑[살] / Dujeong Brigandine [Sal]
   EN: Take -30% damage from [Combustion], [Laceration], [Vibration], [Burst], [Sinking] (rounded down)\n\nGain the effects of [PanicChangeLock]; If this unit is Panicked at Turn End, reset SP to 45\n\nUpon entering the Encounter for the first time, gain 5 [ChoiSwordsmanshipShield]\n\n<color=#ff6000><mark color=#ff000040><b><u>When [ChoiSwordsmanshipShield] expires, end Encounter</color></mark></b></u>
   PL: otrzymuje o 30% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] (zaokrąglane w dół)\n\nkorzysta z efektu [PanicChangeLock]; jeżeli na koniec tury jednostka jest w Panice, SP wraca do 45\n\nprzy pierwszym pojawieniu się w walce zyskuje 5 [ChoiSwordsmanshipShield]\n\n<color=#ff6000><mark color=#ff000040><b><u>po wygaśnięciu [ChoiSwordsmanshipShield] kończy walkę</u></b></mark></color>
682. [[exme] Pasywka wroga [145002] — tekst klimatyczny] 동부의 기승갑은 ‘장착’한다기보다 ‘탑승’하는 개념에 가까운 무구이며, S사의 두정갑 또한 그러한 기승갑의 일종이다.\nR사의 파워드 아머 슈트나 서부 기사들의 풀 플레이트 아머와 같이 두정갑은 사용자의 공방 능력을 비약적으로 끌어올린다.\n다만, 이처럼 뛰어난 성능을 지닌 갑주는 쉽게 보급되지 않는다. 또한 저마다 조작법이 다르고, 작동에는 별도의 연료가 필요하다는 제약 또한 따른다.\n그럼에도 확실한 것은 파워드 아머 슈트와 풀 플레이트 아머, 그리고 여타 기승갑들이 그러했듯, 두정갑이 제공하는 확장된 사거리와 강화된 출력에 탑승자가 익숙해지는 순간, 전장에서의 살상력이 비약적으로 상승한다는 점이다.
   źródło: Passives_Abnormality-exme.json :: dataList[id=145002].flavor
   limit: do 1030 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Eastern Warstride Armors are not so much "equipped" as they are "piloted." S Corp.'s Dujeong Brigandine is one example of such armor.\nMuch like R Corp.'s Powered Armor Suit and the Full Plate Armor used by the Knights of the West, the Dujeong Brigandine greatly augments the user's offensive and defensive combat capabilities.\nYet these advantages do not mean that armors of such potency are readily supplied for combat personnel. Each unit has its own unique controls and comes with the limitation of requiring separate fuels.\nWhat remains certain, however, is that, as with all the aforementioned armors, once a rider has familiarized himself with the Dujeong Brigandine's extended reach and heightened power output, he becomes a machine of war that strides across battlefields with the promise of slaughter.
   PL: Wschodnie Pancerze Kroku Wojny to zbroje, którymi raczej się „pilotuje”, niż które się “zakłada” — i Dujeong Brigandine korporacji S należy do tej kategorii.\nTak jak Skafander Pancerza Wspomaganego korporacji R albo Pełna Zbroja Płytowa rycerzy Zachodu, Dujeong Brigandine radykalnie wzmacnia zdolności użytkownika — zarówno ofensywne, jak i defensywne.\nJednak pancerzy o takiej mocy nie rozdaje się łatwo. Każdy ma własną, niepowtarzalną obsługę, a do działania wymaga oddzielnego paliwa.\nPewne jest natomiast to, że — jak w przypadku wszystkich ww. zbroi — gdy pilot oswoi się z rozszerzonym zasięgiem i podniesioną mocą wyjściową Dujeong Brigandine, staje się maszyną wojenną kroczącą przez pola bitew z obietnicą rzezi.
683. [[exme] Pasywka wroga [145003] — nazwa] 단련하는 무예
   źródło: Passives_Abnormality-exme.json :: dataList[id=145003].name
   limit: do 40 znaków
   EN: Martial Arts of Perseverance
   PL: Martial Arts of Perseverance
684. [[exme] Pasywka wroga [145003] — opis] 합 승리시 [Breath] 횟수 2 증가 (턴당 2회)\n\n자신의 스킬이 적중한 대상의 [Laceration] 위력이 5 미만이면, 공격 종료시 대상에게 [Laceration] 1 부여, [Laceration] 횟수 2 증가 (스킬당 1회, 턴당 2회, 메인 타겟 우선 적용)
   źródło: Passives_Abnormality-exme.json :: dataList[id=145003].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Laceration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: On Clash Win, gain +2 [Breath] Count (2 times per turn)\n\nIf the target this unit's Skill hit has less than 5 [Laceration] Potency, inflict 1 [Laceration] and +2 [Laceration] Count at Attack End (once per Skill, 2 times per turn, prioritize the main target)
   PL: po wygranej w Starciu nakłada +2 Licznika [Breath] (2 razy na turę)\n\njeżeli Siła [Laceration] celu trafionego Umiejętnością jednostki jest niższa niż 5, na koniec Ataku nakłada 1 [Laceration] i +2 Licznika [Laceration] (1 raz na Umiejętność, 2 razy na turę, priorytet: główny cel)
685. [[exme] Pasywka wroga [145003] — tekst klimatyczny] ‘누군가는 재능이 없어 노력한다. 다른 누군가는 재능이 있으면서도 노력하지 않는다.’\n‘결국 제일검의 이름을 받는 것은 재능을 타고난 자라고, 모두가 말했다.’\n‘하지만 상관없다. 언젠가 이 검이 구름과 맞닿을 때까지, 나는 그저 단련할 뿐.’
   źródło: Passives_Abnormality-exme.json :: dataList[id=145003].flavor
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'There are those who persevere in training for lack of talent. Then there are those blessed with talent, only to let it rust.'\n'All men say that the title of Apex Blade can only be seized by the gifted.'\n'It matters not. Until the day comes for this blade of mine to rise high enough to meet the clouds, I shall persevere in honing my prowess.'
   PL: 'Są tacy, którzy trenują, bo brakuje im talentu. Są i tacy obdarzeni talentem, którzy jednak go nie rozwijają.'\n'Wszyscy powtarzali, że tytuł Najwyższego Ostrza może zdobyć tylko ten, kto się nim urodził.'\n'Ale to bez znaczenia. Aż przyjdzie dzień, gdy to ostrze wzniesie się tak wysoko, by dotknąć chmur, będę jedynie wytrwale honować swój fach.'
686. [[exme] Pasywka wroga [145005] — nazwa] 육참
   źródło: Passives_Abnormality-exme.json :: dataList[id=145005].name
   limit: do 40 znaków
   EN: Yield My Flesh
   PL: Yield My Flesh
687. [[exme] Pasywka wroga [145005] — opis] 김삿갓에게 가하는 크리티컬 피해량 +20%, 받는 크리티컬 피해량 +20%
   źródło: Passives_Abnormality-exme.json :: dataList[id=145005].desc
   limit: do 120 znaków
   EN: Deal and take +20% damage on Critical Hit against and from Bamboo-hatted Kim
   PL: zadaje i otrzymuje +20% obrażeń przy trafieniu krytycznym w starciu z Kimem w Bambusowym Kapeluszu
688. [[exme] Pasywka wroga [145005] — tekst klimatyczny] “살을 취해주마.”
   źródło: Passives_Abnormality-exme.json :: dataList[id=145005].flavor
   limit: do 120 znaków
   EN: "This flesh, I claim."
   PL: "To ciało biorę."
689. [[exme] Pasywka wroga [145006] — nazwa] 현상된 기억
   źródło: Passives_Abnormality-exme.json :: dataList[id=145006].name
   limit: do 40 znaków
   EN: Developed Memories
   PL: Developed Memories
690. [[exme] Pasywka wroga [145006] — opis] 스테이지 등장시, [PhotoTransitionChoi] 3 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>턴 시작 시 [PhotoTransitionChoi]이 0이면, 퇴각하고 맵이 변경됨</color></mark></b></u>\n\n복귀 시 퇴각한 턴 만큼 본국태세에 따라 [ChoiSwordsmanship]을 얻거나 잃음\n- [ChoiSwordsmanshipOne]: 얻음\n- [ChoiSwordsmanshipMany]: 잃음
   źródło: Passives_Abnormality-exme.json :: dataList[id=145006].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [PhotoTransitionChoi], [ChoiSwordsmanship], [ChoiSwordsmanshipOne], [ChoiSwordsmanshipMany]
   znaczenie tagów: [PhotoTransitionChoi] = 기억 전환 / Memory Transition; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [ChoiSwordsmanshipOne] = 본국태세 - 곰 사냥 / Battleform of the Homeland - Bearhunt; [ChoiSwordsmanshipMany] = 본국태세 - 범 사냥 / Battleform of the Homeland - Tigerhunt
   EN: Upon entering the Encounter, gain 3 [PhotoTransitionChoi]\n\n<color=#ff6000><mark color=#ff000040><b><u>Turn Start: At 0 [PhotoTransitionChoi] Stack, Retreat and transition into a different location</color></mark></b></u>\n\nWhen Returning to the field, based on current Battleform of the Homeland, gain or lose [ChoiSwordsmanship]\n- When in [ChoiSwordsmanshipOne]: Gain Stack\n- When in [ChoiSwordsmanshipMany]: Lose Stack
   PL: przy pojawieniu się w walce zyskuje 3 [PhotoTransitionChoi]\n\n<color=#ff6000><mark color=#ff000040><b><u>na Początku tury, jeżeli Licznik [PhotoTransitionChoi] wynosi 0, wycofuje się, a mapa ulega zmianie</u></b></mark></color>\n\nprzy powrocie na pole walki zyskuje albo traci [ChoiSwordsmanship] zależnie od bieżącej Formy Bojowej Ojczyzny\n- w [ChoiSwordsmanshipOne]: zyskuje Liczniki\n- w [ChoiSwordsmanshipMany]: traci Liczniki
691. [[exme] Pasywka wroga [145007] — nazwa] 어긋난 기억
   źródło: Passives_Abnormality-exme.json :: dataList[id=145007].name
   limit: do 40 znaków
   EN: Mismatched Memories
   PL: Mismatched Memories
692. [[exme] Pasywka wroga [145007] — opis] 턴 시작 시 아래 효과 적용\n- [ChoiSwordsmanshipOne]이고, [ChoiSwordsmanship] 수치가 5 미만이면,\n(5 - [ChoiSwordsmanship] 수치)만큼 <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u>을 얻음\n- [ChoiSwordsmanshipMany]이고, [ChoiSwordsmanship] 수치가 5 초과면,\n초과하는 값만큼 <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u>을 얻음
   źródło: Passives_Abnormality-exme.json :: dataList[id=145007].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanshipOne], [ChoiSwordsmanship], [Vulnerable], [ChoiSwordsmanshipMany]
   znaczenie tagów: [ChoiSwordsmanshipOne] = 본국태세 - 곰 사냥 / Battleform of the Homeland - Bearhunt; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [Vulnerable] = 취약 / Fragile; [ChoiSwordsmanshipMany] = 본국태세 - 범 사냥 / Battleform of the Homeland - Tigerhunt
   EN: Turn Start: Gain the following effects:\n- When in [ChoiSwordsmanshipOne]: At less than 5 [ChoiSwordsmanship] Stack, gain (5 - [ChoiSwordsmanship] Stack) <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u>\n- When in [ChoiSwordsmanshipMany]: At more than 5 [ChoiSwordsmanship] Stack, gain <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u> equal to surplus [ChoiSwordsmanship] Stack past 5
   PL: na Początku tury stosowane są następujące efekty:\n- w [ChoiSwordsmanshipOne], jeżeli Licznik [ChoiSwordsmanship] jest niższy niż 5, zyskuje (5 - Licznik [ChoiSwordsmanship]) <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</u></b></mark></color>\n- w [ChoiSwordsmanshipMany], jeżeli Licznik [ChoiSwordsmanship] przekracza 5, zyskuje <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</u></b></mark></color> równe nadmiarowi Licznika [ChoiSwordsmanship] ponad 5
693. [[exme] Pasywka wroga [145101] — nazwa] 본국검술[살] - 살과 살 가르기
   źródło: Passives_Abnormality-exme.json :: dataList[id=145101].name
   limit: do 80 znaków
   EN: Swordplay of the Homeland [Sal] - Rend Flesh from Flesh
   PL: Swordplay of the Homeland [Sal] - Rend Flesh from Flesh
694. [[exme] Pasywka wroga [145101] — opis] 스테이지 시작시 [ChoiSwordsmanship] 5 얻음\n\n3턴 마다 자신의 본국태세를 변경함\n\n참격 속성 스킬이 적중했으면, [Breath] 위력 1 얻음 (스킬당 1회)\n\n아래 조건 만족 시 ‘본국궁 - 살 날리기’가 포함된 패턴을 사용함\n- 2턴 연속으로 모든 합에서 졌을 시 (일방 공격은 체크하지 않음) \n- 흐트러진 다음 턴\n- 사기저하 및 패닉 시\n\n턴 시작시 자신의 [ChoiSwordsmanship] 수치가 최솟값이거나 최댓값일 때 강력한 스킬을 사용함\n전 턴에 ‘본국궁 - 살 날리기’를 사용했으면, 자신의 [ChoiSwordsmanship] 수치와 상관없이 강력한 스킬을 사용함\n자신의 체력이 55% 이하면, 자신의 [ChoiSwordsmanship] 수치와 상관없이 강력한 스킬을 사용함 (전투당 1회)
   źródło: Passives_Abnormality-exme.json :: dataList[id=145101].desc
   limit: do 940 znaków
   tokeny: zachowaj dokładnie: \n, [ChoiSwordsmanship], [Breath]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [Breath] = 호흡 / Poise
   EN: Encounter Start: Gain 5 [ChoiSwordsmanship]\n\nAssume a different Battleform of the Homeland every 3 turns\n\nOn Hit using a Slash Skill, gain 1 [Breath] Potency (once per Skill)\n\nWhen the following conditions are met, use a pattern that includes the "Bow of the Homeland - Arrowloose" Skill\n- When this unit lost all Clashes for 2 turns in a row (does not check for Unopposed Attacks)\n- Turn after Stagger\n- When in Low Morale or Panic\n\nTurn Start: At Min or Max [ChoiSwordsmanship] Stacks, use a powerful Skill\nIf this unit used the "Bow of the Homeland - Arrowloose" Skill in the last turn, use a powerful Skill regardless of [ChoiSwordsmanship] Stack on self\nAt 55% or lower HP, use a powerful Skill regardless of [ChoiSwordsmanship] Stack on self
   PL: Początek walki: zyskuje 5 [ChoiSwordsmanship]\n\nco 3 tury zmienia Formę Bojową Ojczyzny\n\nprzy trafieniu Umiejętnością Cięcia zyskuje 1 Siły [Breath] (1 raz na Umiejętność)\n\nprzy spełnieniu poniższych warunków używa wzorca zawierającego Umiejętność „Bow of the Homeland - Arrowloose”\n- po przegraniu wszystkich Starć przez 2 tury z rzędu (Ataki Jednostronne nie są sprawdzane)\n- w turze po Oszołamieniu\n- przy Niskim Morale albo w Panice\n\nna Początku tury, jeżeli Licznik [ChoiSwordsmanship] jednostki osiąga minimum albo maksimum, używa potężnej Umiejętności\njeżeli w poprzedniej turze użyto Umiejętności „Bow of the Homeland - Arrowloose”, używa potężnej Umiejętności niezależnie od Licznika [ChoiSwordsmanship]\nprzy HP równym 55% lub mniej używa potężnej Umiejętności niezależnie od Licznika [ChoiSwordsmanship]
695. [[exme] Pasywka wroga [145101] — tekst klimatyczny] 살 당파에서 사용하는 본국검은 죽이는 것에 그 본질을 두지 않는다.\n피가 흐르고 뼈가 드러나도록, 베고 또 베어 대적자의 살점을 떨구는 것. 그것이 '살'의 본국검이다.
   źródło: Passives_Abnormality-exme.json :: dataList[id=145101].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Sword of the Homeland passed down in the Sal Court Circle is not, at its heart, an art of killing.\nTo cut and cut again until blood runs dry and the bone is laid bare—that is the essence of this art that strips the opponent's flesh into ribbons.\nThat is the Sword of the Homeland practiced by "Sal."
   PL: Miecz Ojczyzny przekazywany w Kręgu Dworskim Sal nie jest, w swej istocie, sztuką zabijania.\nCiąć i ciąć dalej, dopóki krew nie spłynie, a kość nie obnaży się — to sedno sztuki, która obdziera ciało przeciwnika w pasy.\nTak praktykuje miecz Ojczyzny „Sal”.
696. [[exme] Pasywka wroga [145104] — nazwa] 본국검술[살] - 태세 변경
   źródło: Passives_Abnormality-exme.json :: dataList[id=145104].name
   limit: do 70 znaków
   EN: Swordplay of the Homeland [Sal] - Shift Battleform
   PL: Swordplay of the Homeland [Sal] - Shift Battleform
697. [[exme] Pasywka wroga [145104] — opis] <color=#ff6000><mark color=#ff000040><b><u>턴 시작시 자신의 본국태세에 따라 [ChoiSwordsmanship] 2를 얻거나 잃음 (1턴은 발동하지 않음)</color></mark></b></u>\n- [ChoiSwordsmanshipOne]: 얻음\n- [ChoiSwordsmanshipMany]: 잃음\n\n질투 속성 스킬을 장착한 턴에는 [ChoiSwordsmanship] 수치 조정 효과에 영향을 받지 않고 <color=#ff6000><mark color=#ff000040><b><u>다음 턴에 [ChoiSwordsmanship]을 5로 초기화함</color></mark></b></u>
   źródło: Passives_Abnormality-exme.json :: dataList[id=145104].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChoiSwordsmanship], [ChoiSwordsmanshipOne], [ChoiSwordsmanshipMany]
   znaczenie tagów: [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal]; [ChoiSwordsmanshipOne] = 본국태세 - 곰 사냥 / Battleform of the Homeland - Bearhunt; [ChoiSwordsmanshipMany] = 본국태세 - 범 사냥 / Battleform of the Homeland - Tigerhunt
   EN: <color=#ff6000><mark color=#ff000040><b><u>Turn Start: Gain or lose 2 [ChoiSwordsmanship] Stack based on Battleform of the Homeland on self (does not activate in the first turn of the Encounter)</color></mark></b></u>\n- [ChoiSwordsmanshipOne]: Gain Stack\n- [ChoiSwordsmanshipMany]: Lose Stack\n\nIn the turn where this unit equipped Envy Skills, this unit will not be affected by [ChoiSwordsmanship] Stack adjustment effects, and will <color=#ff6000><mark color=#ff000040><b><u>reset [ChoiSwordsmanship] Stack to 5 next turn</color></mark></b></u>
   PL: <color=#ff6000><mark color=#ff000040><b><u>na Początku tury zyskuje albo traci 2 Liczniki [ChoiSwordsmanship] zależnie od Formy Bojowej Ojczyzny (nie uruchamia się w pierwszej turze walki)</u></b></mark></color>\n- w [ChoiSwordsmanshipOne]: zyskuje Liczniki\n- w [ChoiSwordsmanshipMany]: traci Liczniki\n\nw turze, w której jednostka wyposażyła Umiejętności Zawiści, nie podlega efektom korekty Licznika [ChoiSwordsmanship] i <color=#ff6000><mark color=#ff000040><b><u>resetuje Licznik [ChoiSwordsmanship] do 5 w następnej turze</u></b></mark></color>
698. [[exme] Pasywka wroga [145105] — nazwa] 두정갑[살] - 태산
   źródło: Passives_Abnormality-exme.json :: dataList[id=145105].name
   limit: do 60 znaków
   EN: Dujeong Brigandine [Sal] - Great Mountain
   PL: Dujeong Brigandine [Sal] - Great Mountain
699. [[exme] Pasywka wroga [145105] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -30% (소수점 버림)\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨\n\n턴 시작 시 아래 효과 적용\n\n- [ChoiSwordsmanshipOne]이고, [ChoiSwordsmanship] 수치가 5 미만이면,\n(5 - [ChoiSwordsmanship] 수치)만큼 <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u>을 얻음\n\n- [ChoiSwordsmanshipMany]이고, [ChoiSwordsmanship] 수치가 5 초과면,\n초과하는 값만큼 <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u>을 얻음
   źródło: Passives_Abnormality-exme.json :: dataList[id=145105].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [PanicChangeLock], [ChoiSwordsmanshipOne], [ChoiSwordsmanship], [Vulnerable], [ChoiSwordsmanshipMany]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [ChoiSwordsmanshipOne] = 본국태세 - 곰 사냥 / Battleform of the Homeland - Bearhunt; [ChoiSwordsmanship] = 본국검술[살] / Swordplay of the Homeland [Sal] …
   EN: Take -30% damage from [Combustion], [Laceration], [Vibration], [Burst], [Sinking] (rounded down)\n\nGain the effects of [PanicChangeLock]; If this unit is Panicked at Turn End, reset SP to 45\n\nTurn Start: Gain the following effects:\n\n- When in [ChoiSwordsmanshipOne]: At less than 5 [ChoiSwordsmanship] Stack, gain (5 - [ChoiSwordsmanship] Stack) <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u>\n\n- When in [ChoiSwordsmanshipMany]: At more than 5 [ChoiSwordsmanship] Stack, gain <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</color></mark></b></u> equal to surplus [ChoiSwordsmanship] Stack past 5
   PL: otrzymuje o 30% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] (zaokrąglane w dół)\n\nkorzysta z efektu [PanicChangeLock]; jeżeli na koniec tury jednostka jest w Panice, SP wraca do 45\n\nna Początku tury stosowane są następujące efekty:\n\n- w [ChoiSwordsmanshipOne], jeżeli Licznik [ChoiSwordsmanship] jest niższy niż 5, zyskuje (5 - Licznik [ChoiSwordsmanship]) <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</u></b></mark></color>\n\n- w [ChoiSwordsmanshipMany], jeżeli Licznik [ChoiSwordsmanship] przekracza 5, zyskuje <color=#ff6000><mark color=#ff000040><b><u>[Vulnerable]</u></b></mark></color> równe nadmiarowi Licznika [ChoiSwordsmanship] ponad 5
700. [[exme] Pasywka wroga [145105] — tekst klimatyczny] S사의 기본적인 두정갑을 기반으로, 살·피·뼈, 세 당파는 저마다의 사상에 맞춘 두정갑을 만들어냈다.\n옛이야기에 따르면 ‘살’은 언제나 살생의 첫 시작을 열어왔다. 그들은 누구보다 앞서 적의 살을 가른다.\n‘피’는 살이 갈라질 때마다 흘러나오는 피를 받아 내고, 그 피를 이용해 전투의 지속성을 보완한다.\n‘뼈’는 살생의 마무리를 맡는다. 마디와 마디를 끊어 무릎을 꿇리고, 끝내 적의 목뼈를 베어 삶을 끝낸다.
   źródło: Passives_Abnormality-exme.json :: dataList[id=145105].flavor
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The three Court Circles of Sal, Pi, and Ppyeo each remade the standard Dujeong Brigandine of S Corp. into forms suited to their own doctrines.\nThe olden tales say that the "Sal" has ever been the first to spearhead a slaughter, eager to cleave the enemy's flesh before any other.\nThe "Pi" harvests the blood that spills forth from each opened flesh wound and turns it into endurance on the battlefield.\nThe "Ppyeo" takes the close of a slaughter. They part one joint from the other, bringing the enemy to their knees. Then, a blade through the neckbone finishes the collective act of killing.
   PL: Trzy Kręgi Dworskie — Sal, Pi i Ppyeo — przekształciły bazowe Dujeong Brigandine korporacji S, nadając im formę zgodną z własnymi doktrynami.\nWedług starych opowieści „Sal” zawsze wytyczało początek rzezi, kładąc ciosy na ciele wroga wcześniej niż ktokolwiek inny.\n„Pi” zbiera krew wypływającą z każdej rozwartej rany i zamienia ją w wytrwałość na polu bitwy.\n„Ppyeo” finalizuje zabijanie: rozbijając staw od stawu, przygina wroga do kolan, po czym ostrze przez kość szyi kresuje zbiorowy akt zabijania.
701. [[exme] Pasywka wroga [146101] — nazwa] 흩어지는 기억
   źródło: Passives_Abnormality-exme.json :: dataList[id=146101].name
   limit: do 40 znaków
   EN: Scattering Memories
   PL: Scattering Memories
702. [[exme] Pasywka wroga [146101] — opis] 사망 시, 가장 적은 수량의 E.G.O 자원 +1
   źródło: Passives_Abnormality-exme.json :: dataList[id=146101].desc
   limit: do 120 znaków
   EN: On death, give +1 E.G.O resource of the least-owned Affinity
   PL: przy śmierci daje +1 zasób E.G.O Afinności, której ma najmniej
703. [[exme] Pasywka wroga [146101] — podsumowanie] 사망 시, E.G.O 자원 획득
   źródło: Passives_Abnormality-exme.json :: dataList[id=146101].summary
   limit: do 120 znaków
   EN: Give E.G.O resource on death
   PL: daje zasób E.G.O przy śmierci
704. [[exme] Pasywka wroga [146001] — nazwa] 장소형 뒤틀림: 현상소
   źródło: Passives_Abnormality-exme.json :: dataList[id=146001].name
   limit: do 50 znaków
   EN: Location-type Distortion: Photo Lab
   PL: Wypaczenie typu Lokalizacja: Ciemnia
705. [[exme] Pasywka wroga [146001] — opis] 이 유닛은 사망하지 않고, 자신을 메인 타겟 대상으로 한 스킬 피해만 적용되며, 그 외의 피해를 받지 않음 \n\n속도가 1로 고정됨\n\n스테이지 등장 후 턴 시작시, [PhotoTransitionChoiCamera]을 3 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 체력이 1이 되거나 턴 시작시 [PhotoTransitionChoiCamera]이 0이면</color></mark></b></u>, 아래 효과 적용\n- N사 2등급 직원과 자신을 소멸 시킴\n- 임경업을 복귀시킴\n- 맵을 변경함
   źródło: Passives_Abnormality-exme.json :: dataList[id=146001].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [PhotoTransitionChoiCamera]
   znaczenie tagów: [PhotoTransitionChoiCamera] = 기억 전환 / Memory Transition
   EN: This unit cannot be killed, and does not take any damage from sources other than Skill damage from Skills attacking this unit as the main target\n\nThis unit's Speed is fixed to 1\n\nTurn Start after entering the Encounter: Gain 3 [PhotoTransitionChoiCamera]\n\n<color=#ff6000><mark color=#ff000040><b><u>If this unit's HP reaches 1, or if [PhotoTransitionChoiCamera] reaches 0 Stack at Turn Start</color></mark></b></u>, activate the following:\n- Remove self and N Corp. Class 2 Staff from the Encounter\n- Return Im Gyeong-eop to the Encounter\n- Move the battle to a different location
   PL: ta jednostka nie może zostać pokonana i otrzymuje wyłącznie obrażenia od Umiejętności atakujących ją jako cel główny; inne obrażenia jej nie szkodzą\n\nSzybkość zostaje ustalona na 1\n\nna Początku tury po pojawieniu się w walce zyskuje 3 [PhotoTransitionChoiCamera]\n\n<color=#ff6000><mark color=#ff000040><b><u>jeżeli HP jednostki osiąga 1 albo Licznik [PhotoTransitionChoiCamera] spada do 0 na Początku tury</u></b></mark></color>, stosowane są następujące efekty:\n- usuwa siebie i N Corp. Class 2 Staff z walki\n- przywraca Im Gyeong-eop do walki\n- przenosi walkę do innej lokalizacji
706. [[exme] Pasywka wroga [146002] — nazwa] 기억에서 기록으로
   źródło: Passives_Abnormality-exme.json :: dataList[id=146002].name
   limit: do 40 znaków
   EN: From Memory to Record
   PL: From Memory to Record
707. [[exme] Pasywka wroga [146002] — opis] S사에서 N사로 돌아온 턴이면, 전투 시작 시 모든 수감자들의 정신력 15 회복
   źródło: Passives_Abnormality-exme.json :: dataList[id=146002].desc
   limit: do 140 znaków
   EN: Combat Start: If the battlefield has returned from S Corp. to N Corp. this turn, heal 15 SP for all Sinners
   PL: Początek walki: jeżeli pole bitwy wróciło w tej turze z korporacji S do korporacji N, wszystkie Grzeszniki przywracają 15 SP

## [exme] Pasywka wroga: Passives_Enemy-exme
- plik gry: `Passives_Enemy-exme.json`

708. [[exme] Pasywka wroga [9105701] — nazwa] 살수본위
   źródło: Passives_Enemy-exme.json :: dataList[id=9105701].name
   limit: do 40 znaków
   EN: Bearing of a Salsu
   PL: Bearing of a Salsu
709. [[exme] Pasywka wroga [9105701] — opis] 자신의 [Breath] 횟수가 1이면, [Breath] 횟수가 감소하지 않는 대신 자신의 체력 10 감소 (이 효과로 흐트러지지 않고, 체력이 1 미만이 되지 않음)\n\n기본 스킬의 크리티컬 피해량이 (자신의 잃은 체력 비율 / 2)만큼 증가함 (최대 50%)
   źródło: Passives_Enemy-exme.json :: dataList[id=9105701].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 1 [Breath] Count, lose 10 HP instead of losing [Breath] Count (this effect cannot Stagger this unit and does not drop this unit's HP below 1)\n\nDeal +(missing HP percentage on self / 2) damage on Critical Hit using Base Skills (max 50%)
   PL: przy 1 Liczniku [Breath] zamiast tracić Licznik [Breath] traci 10 HP (ten efekt nie Oszołomi jednostki i nie obniży jej HP poniżej 1)\n\nUmiejętnościami bazowymi zadaje +((procent brakującego HP jednostki) / 2) obrażeń przy trafieniu krytycznym (maks. 50%)
710. [[exme] Pasywka wroga [9105702] — nazwa] 함께 쉬었던 숨
   źródło: Passives_Enemy-exme.json :: dataList[id=9105702].name
   limit: do 40 znaków
   EN: A Breath Taken Together
   PL: A Breath Taken Together
711. [[exme] Pasywka wroga [9105702] — opis] 자신의 스킬 및 코인 효과로 [Breath] 위력을 얻을 때, [Breath]이 없거나 [Breath] 위력이 가장 낮은 아군 1명에게 [Breath] 1 부여 (턴당 최대 5회)\n\n턴 시작 시 전장에 김삿갓이 있으면, [SlashDamageUp] 1 얻고 자신의 [Laceration] 횟수 2 증가
   źródło: Passives_Enemy-exme.json :: dataList[id=9105702].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [SlashDamageUp], [Laceration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [Laceration] = 출혈 / Bleed
   EN: When gaining [Breath] Potency using this unit's own Skills and Coin effects, apply 1 [Breath] on an ally that does not have [Breath] or has the lowest [Breath] Potency (5 times per turn)\n\nTurn Start: If Bamboo-hatted Kim is on the field, gain 1 [SlashDamageUp] and +2 [Laceration] Count
   PL: zyskując Siłę [Breath] efektami własnych Umiejętności i Monet, nakłada 1 [Breath] sojusznikowi bez [Breath] albo z najniższą Siłą [Breath] (maks. 5 razy na turę)\n\nna Początku tury, jeżeli Kim w Bambusowym Kapeluszu jest na polu walki, zyskuje 1 [SlashDamageUp] i nakłada +2 Licznika [Laceration]
712. [[exme] Pasywka wroga [9105703] — nazwa] 지끈거리는 기억
   źródło: Passives_Enemy-exme.json :: dataList[id=9105703].name
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [[exme] Pasywka wroga [9105703] — opis] 합 패배 시 [RegretSCorp] 1 얻음
   źródło: Passives_Enemy-exme.json :: dataList[id=9105703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RegretSCorp]
   znaczenie tagów: [RegretSCorp] = 지끈거리는 기억 / Headsplitting Memory
   EN: On Clash Lose, gain 1 [RegretSCorp]
   PL: po przegranej w Starciu zyskuje 1 [RegretSCorp]
714. [[exme] Pasywka wroga [9105704] — nazwa] 마지막 숨
   źródło: Passives_Enemy-exme.json :: dataList[id=9105704].name
   limit: do 40 znaków
   EN: The Last Breath
   PL: The Last Breath
715. [[exme] Pasywka wroga [9105704] — opis] 자신이 사망했으면, 다음 턴 시작 시 모든 검계 소속 아군에게 [Breath] 5 부여, [Breath] 횟수 2 증가\n\n턴 시작 시 [Breath] 위력이 20 이상이면, 맨 왼쪽 슬롯에 ‘연참’ 장착
   źródło: Passives_Enemy-exme.json :: dataList[id=9105704].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: If this unit is defeated, apply 5 [Breath] and +2 [Breath] Count on all Blade Lineage allies at the next Turn Start\n\nTurn Start: At 20+ [Breath] Potency, equip "Slash Series" on the leftmost Slot
   PL: jeżeli jednostka zostanie pokonana, na następnym Początku tury nakłada 5 [Breath] i +2 Licznika [Breath] wszystkim sojusznikom z Linii Miecza\n\nna Początku tury przy 20+ Siły [Breath] wyposaża „Slash Series” w skrajnie lewy Slot
716. [[exme] Pasywka wroga [9105804] — nazwa] 마지막 숨
   źródło: Passives_Enemy-exme.json :: dataList[id=9105804].name
   (powtórzenie elementu 714 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [[exme] Pasywka wroga [9105804] — opis] 자신이 사망했으면, 다음 턴 시작 시 모든 검계 소속 아군에게 [Breath] 5 부여, [Breath] 횟수 2 증가\n\n턴 시작 시 [Breath] 위력이 20 이상이면, 맨 왼쪽 슬롯에 ‘연참’ 장착
   źródło: Passives_Enemy-exme.json :: dataList[id=9105804].desc
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [fools] Wróg / część: Enemies-fools
- plik gry: `Enemies-fools.json`

718. [[fools] Wróg / część [8999] — nazwa] 꼬미와 베르길리우스?
   źródło: Enemies-fools.json :: dataList[id=8999].name
   limit: do 40 znaków
   EN: Kkomi and Vergilius?
   PL: Kkomi and Vergilius?
719. [[fools] Wróg / część [8999] — opis] 본체
   źródło: Enemies-fools.json :: dataList[id=8999].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [fools] Umiejętności wrogów / Anomalii — Skills_fools
- grupa rozdziału/trybu: `fools` · plik: `Skills_fools.json`

720. [Umiejętność wroga [899901] (ulepszenie 1) — nazwa] 사탕 줘.
   źródło: Skills_fools.json :: dataList[id=899901].levelList[level=1].name
   limit: do 40 znaków
   EN: Gimme Candy.
   PL: Gimme Candy.
721. [Umiejętność wroga [899901] (ulepszenie 1) — opis] [CandyForCharon]을 가진 대상 우선 공격\n[EndSkill] 대상에게 [CandyForCharon]이 없다면, [CandyForCharon]을 부여함
   źródło: Skills_fools.json :: dataList[id=899901].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CandyForCharon], [EndSkill]
   znaczenie tagów: [CandyForCharon] = 사탕? / Candy?; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with [CandyForCharon]\n[EndSkill] If the target does not have [CandyForCharon], inflict [CandyForCharon]
   PL: priorytet: cele z [CandyForCharon]\n[EndSkill] jeżeli cel nie ma [CandyForCharon], nakłada [CandyForCharon]
722. [Umiejętność wroga [899901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_fools.json :: dataList[id=899901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność wroga [899901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [CandyForCharon]이 있으면, 대상은 다음 턴 흐트러짐 상태가 됨.
   źródło: Skills_fools.json :: dataList[id=899901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CandyForCharon]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CandyForCharon] = 사탕? / Candy?
   EN: [OnSucceedAttack] If target has [CandyForCharon], the target becomes Staggered next turn.
   PL: [OnSucceedAttack] jeżeli cel ma [CandyForCharon], w następnej turze wpada w Oszołamienie.
724. [Umiejętność wroga [899902] (ulepszenie 1) — nazwa] 없어. 사탕.
   źródło: Skills_fools.json :: dataList[id=899902].levelList[level=1].name
   limit: do 40 znaków
   EN: No Candy.
   PL: No Candy.
725. [Umiejętność wroga [899903] (ulepszenie 1) — nazwa] 너희들…
   źródło: Skills_fools.json :: dataList[id=899903].levelList[level=1].name
   limit: do 40 znaków
   EN: You...
   PL: You...
726. [Umiejętność wroga [899903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_fools.json :: dataList[id=899903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [899903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_fools.json :: dataList[id=899903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [899904] (ulepszenie 1) — nazwa] …꼬미가, 화났어.
   źródło: Skills_fools.json :: dataList[id=899904].levelList[level=1].name
   limit: do 40 znaków
   EN: ... Kkomi's angry.
   PL: ... Kkomi's angry.
729. [Umiejętność wroga [899904] (ulepszenie 1) — opis] [BeforeAttack] [CandyForCharon]을 가진 인격 수만큼 공격 가중치 증가\n[WhenUse] [CandyForCharon]을 가진 인격 수만큼 합 위력이 증가
   źródło: Skills_fools.json :: dataList[id=899904].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [CandyForCharon], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [CandyForCharon] = 사탕? / Candy?; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] Gain Atk Weight equal to number of enemies with [CandyForCharon]\n[WhenUse] Gain Clash Power equal to the number of enemies with [CandyForCharon]
   PL: [BeforeAttack] zyskuje Wagę Ataku równą liczbie wrogów z [CandyForCharon]\n[WhenUse] zyskuje Moc Starcia równą liczbie wrogów z [CandyForCharon]
730. [Umiejętność wroga [899904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_fools.json :: dataList[id=899904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [899904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_fools.json :: dataList[id=899904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [899905] (ulepszenie 1) — nazwa] 부릉부릉
   źródło: Skills_fools.json :: dataList[id=899905].levelList[level=1].name
   limit: do 40 znaków
   EN: Vroom-Vroom
   PL: Vroom-Vroom
733. [Umiejętność wroga [899905] (ulepszenie 1) — opis] [WhenUse] [CandyForCharon]을 가진 인격 수만큼 합 위력이 증가\n[CandyForCharon]을 가진 인격 수만큼 피해량 +10% (최대 100%)
   źródło: Skills_fools.json :: dataList[id=899905].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [CandyForCharon]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CandyForCharon] = 사탕? / Candy?
   EN: [WhenUse] Gain Clash Power equal to the number of Identities with [CandyForCharon]\nDeal +10% damage for every Identity with [CandyForCharon] (max 100%)
   PL: [WhenUse] zyskuje Moc Starcia równą liczbie Tożsamości z [CandyForCharon]\nzadaje +10% obrażeń za każdą Tożsamość z [CandyForCharon] (maks. 100%)
734. [Umiejętność wroga [899906] (ulepszenie 1) — nazwa] 때렸어. 꼬미를
   źródło: Skills_fools.json :: dataList[id=899906].levelList[level=1].name
   limit: do 40 znaków
   EN: You hit Kkomi.
   PL: You hit Kkomi.
735. [Umiejętność wroga [899906] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [ParryingResultUp] 2, [Agility] 2 얻음
   źródło: Skills_fools.json :: dataList[id=899906].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ParryingResultUp], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 2 [ParryingResultUp] and 2 [Agility] next turn
   PL: [WhenUse] zyskuje 2 [ParryingResultUp] i 2 [Agility] w następnej turze

## [fools] Pasywka wroga: Passives_fools
- plik gry: `Passives_fools.json`

736. [[fools] Pasywka wroga [899901] — nazwa] 사탕 있어?
   źródło: Passives_fools.json :: dataList[id=899901].name
   limit: do 40 znaków
   EN: Got Candy?
   PL: Got Candy?
737. [[fools] Pasywka wroga [899901] — opis] 편성 순서가 가장 빠른 인격 순서로 [CandyForCharon]이 없는 적 1명에게 턴 시작 시 [CandyForCharon]을 부여함
   źródło: Passives_fools.json :: dataList[id=899901].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CandyForCharon]
   znaczenie tagów: [CandyForCharon] = 사탕? / Candy?
   EN: Turn Start: in Deployment Order, inflict [CandyForCharon] against 1 enemy without [CandyForCharon]
   PL: na Początku tury nakłada [CandyForCharon] na 1 wroga bez [CandyForCharon], według kolejności rozmieszczenia
738. [[fools] Pasywka wroga [899902] — nazwa] 붉은 기운
   źródło: Passives_fools.json :: dataList[id=899902].name
   limit: do 40 znaków
   EN: The Red Aura
   PL: The Red Aura
739. [[fools] Pasywka wroga [899902] — opis] 스테이지 시작 시, 베르길리우스가 스테이지동안 유지되는 보호막 일정량 얻음\n보호막이 사라지면, 해당 턴 종료됨
   źródło: Passives_fools.json :: dataList[id=899902].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Encounter Start: Vergilius gains a certain amount of Shield that lasts for the duration of the Encounter\nTurn ends when the Shield is broken
   PL: Początek walki: Vergilius zyskuje pewną ilość Tarczy utrzymującej się przez tę walkę\ntura kończy się, gdy Tarcza zostaje złamana
740. [[fools] Pasywka wroga [899903] — nazwa] 부릉부릉. 화났어
   źródło: Passives_fools.json :: dataList[id=899903].name
   limit: do 40 znaków
   EN: Vroom-vroom. Angry now
   PL: Vroom-vroom. Angry now
741. [[fools] Pasywka wroga [899903] — opis] 보호막이 소모되면, 패턴 변경됨\n- 속도가 20으로 고정됨\n- 체력 피해를 더 이상 받지 않음
   źródło: Passives_fools.json :: dataList[id=899903].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Shield is depleted, gains a new pattern\n- Fix Speed to 20\n- No longer takes any HP damage
   PL: po zużyciu Tarczy przybiera nowy wzorzec\n- Szybkość zostaje ustalona na 20\n- nie otrzymuje już żadnych obrażeń HP

## [hidden] Wróg / część: Enemies-hidden
- plik gry: `Enemies-hidden.json`

742. [[hidden] Wróg / część [124301] — nazwa] 본체
   źródło: Enemies-hidden.json :: dataList[id=124301].name
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [[hidden] Wróg / część [124301] — opis] 베르길리우스
   źródło: Enemies-hidden.json :: dataList[id=124301].desc
   limit: do 120 znaków
   EN: Vergilius
   PL: Vergilius
744. [[hidden] Wróg / część [124302] — nazwa] 꼬미
   źródło: Enemies-hidden.json :: dataList[id=124302].name
   limit: do 40 znaków
   EN: Kkomi
   PL: Kkomi
745. [[hidden] Wróg / część [124302] — opis] 꼬미
   źródło: Enemies-hidden.json :: dataList[id=124302].desc
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mirror] Umiejętności wrogów / Anomalii — Skills_Abnormality_Mirror
- grupa rozdziału/trybu: `mirror` · plik: `Skills_Abnormality_Mirror.json`

746. [Umiejętność wroga [808202] (ulepszenie 1) — nazwa] 깊은 찌르기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808202].levelList[level=1].name
   limit: do 40 znaków
   EN: Deep Thrust
   PL: Deep Thrust
747. [Umiejętność wroga [808202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 6 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Bleed next turn
   PL: [OnSucceedAttack] nakłada 6 Krwawienia w następnej turze
748. [Umiejętność wroga [808203] (ulepszenie 1) — nazwa] 쥐어짐
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808203].levelList[level=1].name
   limit: do 40 znaków
   EN: The Gripping
   PL: The Gripping
749. [Umiejętność wroga [808203] (ulepszenie 1) — opis] [StartBattle] 다음 턴동안 대상을 주시함
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gazes into the target for the next turn
   PL: [StartBattle] przez następną turę przygląda się celowi
750. [Umiejętność wroga [808204] (ulepszenie 1) — nazwa] 광소
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808204].levelList[level=1].name
   limit: do 40 znaków
   EN: Cackle
   PL: Cackle
751. [Umiejętność wroga [808204] (ulepszenie 1) — opis] [WhenUse] 대상에게 정신피해 10
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Deal 10 SP damage
   PL: [WhenUse] zadaje 10 obrażeń SP
752. [Umiejętność wroga [808204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Attack Power Up next turn
   PL: [OnSucceedAttack] zyskuje 1 Wzrost Mocy Ataku w następnej turze
753. [Umiejętność wroga [808205] (ulepszenie 1) — nazwa] 죄악을 꿰뚫는 못
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808205].levelList[level=1].name
   limit: do 40 znaków
   EN: Sin-skewering Nail
   PL: Sin-skewering Nail
754. [Umiejętność wroga [808205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 N Corp’s Nails next turn
   PL: [OnSucceedAttack] nakłada 1 N Corp's Nails w następnej turze
755. [Umiejętność wroga [808205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 754 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Umiejętność wroga [808205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 754 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Umiejętność wroga [808206] (ulepszenie 1) — nazwa] 정화
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808206].levelList[level=1].name
   limit: do 40 znaków
   EN: Purify
   PL: Purify
758. [Umiejętność wroga [808206] (ulepszenie 1) — opis] [WhenUse] 대상 체력이 30%미만이면 스킬 위력 +2
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808206].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target’s HP is below 30%, Skill Power +2
   PL: [WhenUse] jeżeli HP celu jest niższe niż 30%, Moc Umiejętności +2
759. [Umiejętność wroga [808206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] N사의 못 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 N Corp’s Nails
   PL: [OnSucceedAttack] nakłada 1 N Corp's Nails
760. [Umiejętność wroga [808206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] N사의 못 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 759 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Umiejętność wroga [808206] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] N사의 못 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808206].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 759 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Umiejętność wroga [808206] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상에게 N사의 못이 5이상 있으면, 흐트러짐 상태로 만들고 N사의 못을 없앰
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808206].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ N Corp’s Nails, Stagger them and remove the Nails
   PL: [OnSucceedAttack] jeżeli cel ma 5+ N Corp's Nails, Oszołomi go i je usuwa
763. [Umiejętność wroga [808208] (ulepszenie 1) — nazwa] 처단할지어다!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808208].levelList[level=1].name
   limit: do 40 znaków
   EN: I Shall Claim Your Life!
   PL: I Shall Claim Your Life!
764. [Umiejętność wroga [808208] (ulepszenie 1) — opis] [DefeatDuel] 흐트러짐 상태가 됨
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808208].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] User becomes Staggered
   PL: [DefeatDuel] użytkownik wpada w Oszołamienie
765. [Umiejętność wroga [808208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상을 흐트러짐 상태로 만들고, 다음 턴에 취약 10 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target and inflict 10 Fragile next turn
   PL: [OnSucceedAttack] Oszołomi cel i nakłada 10 Wrażliwości w następnej turze
766. [Umiejętność wroga [808210] (ulepszenie 1) — nazwa] 가소로워
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808210].levelList[level=1].name
   limit: do 40 znaków
   EN: You Are Nothing
   PL: You Are Nothing
767. [Umiejętność wroga [808210] (ulepszenie 1) — opis] [OnSucceedEvade] 대상에게 정신피해 5
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808210].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Deal 5 SP damage
   PL: [OnSucceedEvade] zadaje 5 obrażeń SP
768. [Umiejętność wroga [808301] (ulepszenie 1) — nazwa] 첫 사람의 날개
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808301].levelList[level=1].name
   limit: do 40 znaków
   EN: Protoplast’s Wings
   PL: Protoplast's Wings
769. [Umiejętność wroga [808302] (ulepszenie 1) — nazwa] 첫 사람의 날개
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808302].levelList[level=1].name
   (powtórzenie elementu 768 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [808303] (ulepszenie 1) — nazwa] 무구한 날개짓
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].name
   limit: do 40 znaków
   EN: Innocent Flutters
   PL: Innocent Flutters
771. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] nakłada 1 Spętania w następnej turze
772. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 1 Paraliżu w następnej turze
773. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [808303] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808303].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Umiejętność wroga [808304] (ulepszenie 1) — nazwa] 부러진 날개
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808304].levelList[level=1].name
   limit: do 40 znaków
   EN: Broken Wings
   PL: Broken Wings
780. [Umiejętność wroga [808304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [808304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Umiejętność wroga [808304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [808304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [808305] (ulepszenie 1) — nazwa] 부러진 날개
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808305].levelList[level=1].name
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [808305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [808305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [808305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [808305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność wroga [808306] (ulepszenie 1) — nazwa] 격노한 날개짓
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808306].levelList[level=1].name
   limit: do 40 znaków
   EN: Enraged Flutters
   PL: Enraged Flutters
790. [Umiejętność wroga [808307] (ulepszenie 1) — nazwa] 고결한 정화
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].name
   limit: do 40 znaków
   EN: Noble Purification
   PL: Noble Purification
791. [Umiejętność wroga [808307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Fragile next turn
   PL: [OnSucceedAttack] nakłada 1 Wrażliwości w następnej turze
792. [Umiejętność wroga [808307] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed next turn
   PL: [OnSucceedAttack] nakłada 2 Krwawienia w następnej turze
793. [Umiejętność wroga [808307] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność wroga [808307] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [808307] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [808307] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808307].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [808308] (ulepszenie 1) — nazwa] 영예로운 쥐어짐
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808308].levelList[level=1].name
   limit: do 40 znaków
   EN: Honorable Grip
   PL: Honorable Grip
798. [Umiejętność wroga [808308] (ulepszenie 1) — opis] [WhenUse] 대상의 체력이 30%미만이면 피해량 +100%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808308].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target’s HP is below 30%, +100% Damage
   PL: [WhenUse] jeżeli HP celu jest niższe niż 30%, +100% obrażeń
799. [Umiejętność wroga [808308] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 체력이 30% 미만이면 즉시 처치하고, 체력을 30 회복\n다음 턴에 공격 위력 증가를 2 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808308].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target’s HP is below 30%, kill them and heal 30 HP\nGain 2 Attack Power Up next turn
   PL: [OnSucceedAttackHead] jeżeli HP celu jest niższe niż 30%, zabija go i przywraca 30 HP\nzyskuje 2 Wzrost Mocy Ataku w następnej turze
800. [Umiejętność wroga [808309] (ulepszenie 1) — nazwa] 참회하라!!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808309].levelList[level=1].name
   limit: do 40 znaków
   EN: Repent!!
   PL: Repent!!
801. [Umiejętność wroga [808309] (ulepszenie 1) — opis] [WhenUse] 대상의 체력이 30%미만이면 피해량 +100%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808309].levelList[level=1].desc
   (powtórzenie elementu 798 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [808309] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808309].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Fragile next turn
   PL: [OnSucceedAttack] nakłada 5 Wrażliwości w następnej turze
803. [Umiejętność wroga [808309] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808309].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed next turn
   PL: [OnSucceedAttack] nakłada 5 Krwawienia w następnej turze
804. [Umiejętność wroga [808310] (ulepszenie 1) — nazwa] 온전한 살덩이
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808310].levelList[level=1].name
   limit: do 40 znaków
   EN: Peerless Flesh
   PL: Peerless Flesh
805. [Umiejętność wroga [808401] (ulepszenie 1) — nazwa] 손뼉치기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808401].levelList[level=1].name
   limit: do 40 znaków
   EN: Clap
   PL: Clap
806. [Umiejętność wroga [808401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Attack Power Down next turn
   PL: [OnSucceedAttack] nakłada 1 Spadek Mocy Ataku w następnej turze
807. [Umiejętność wroga [808402] (ulepszenie 1) — nazwa] 강한 손뼉치기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808402].levelList[level=1].name
   limit: do 40 znaków
   EN: Powerful Clap
   PL: Powerful Clap
808. [Umiejętność wroga [808402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 위력 감소 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Attack Power Down next turn
   PL: [OnSucceedAttackHead] nakłada 3 Spadek Mocy Ataku w następnej turze
809. [Umiejętność wroga [808403] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808403].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Whip
   PL: Tail Whip
810. [Umiejętność wroga [808403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [808403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Fragile next turn
   PL: [OnSucceedAttackHead] nakłada 3 Wrażliwości w następnej turze
812. [Umiejętność wroga [808404] (ulepszenie 1) — nazwa] 주머니 압박
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808404].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressing Sac
   PL: Pressing Sac
813. [Umiejętność wroga [808404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL: [OnSucceedAttack] nakłada 3 Spętania w następnej turze
814. [Umiejętność wroga [808405] (ulepszenie 1) — nazwa] 혈사포
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808405].levelList[level=1].name
   limit: do 40 znaków
   EN: Blood Cannon
   PL: Blood Cannon
815. [Umiejętność wroga [808405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed
   PL: [OnSucceedAttack] nakłada 5 Krwawienia
816. [Umiejętność wroga [808405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 20 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 20 Bleed
   PL: [OnSucceedAttackHead] nakłada 20 Krwawienia
817. [Umiejętność wroga [808406] (ulepszenie 1) — nazwa] 종혈
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808406].levelList[level=1].name
   limit: do 40 znaków
   EN: Clotting
   PL: Clotting
818. [Umiejętność wroga [808406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 30 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 30 Bleed
   PL: [OnSucceedAttackHead] nakłada 30 Krwawienia
819. [Umiejętność wroga [808501] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808501].levelList[level=1].name
   limit: do 40 znaków
   EN: Claw
   PL: Claw
820. [Umiejętność wroga [808501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed next turn
   PL: [OnSucceedAttack] nakłada 2 Krwawienia w następnej turze.
821. [Umiejętność wroga [808502] (ulepszenie 1) — nazwa] 등압
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808502].levelList[level=1].name
   limit: do 40 znaków
   EN: Constant Voltage
   PL: Constant Voltage
822. [Umiejętność wroga [808502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 1 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture next turn
   PL: [OnSucceedAttack] nakłada 1 Rozdarcia w następnej turze.
823. [Umiejętność wroga [808503] (ulepszenie 1) — nazwa] 등압추격
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808503].levelList[level=1].name
   limit: do 40 znaków
   EN: Electromotive Pursuit
   PL: Electromotive Pursuit
824. [Umiejętność wroga [808503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 1 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [808503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 4 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Rupture next turn
   PL: [OnSucceedAttackHead] nakłada 4 Rozdarcia w następnej turze.
826. [Umiejętność wroga [808504] (ulepszenie 1) — nazwa] 하울링
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808504].levelList[level=1].name
   limit: do 40 znaków
   EN: Howl
   PL: Howl
827. [Umiejętność wroga [808504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL: [OnSucceedAttack] nakłada 2 Spętania w następnej turze.
828. [Umiejętność wroga [808504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 수비 위력 감소 4 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Defense Power Down
   PL: [OnSucceedAttackHead] nakłada 4 Spadek Mocy Obrony.
829. [Umiejętność wroga [808505] (ulepszenie 1) — nazwa] 전격 하울링
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808505].levelList[level=1].name
   limit: do 40 znaków
   EN: Electrified Howl
   PL: Electrified Howl
830. [Umiejętność wroga [808505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 3 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Rupture next turn
   PL: [OnSucceedAttackHead] nakłada 3 Rozdarcia w następnej turze.
831. [Umiejętność wroga [808506] (ulepszenie 1) — nazwa] 피뢰
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808506].levelList[level=1].name
   limit: do 40 znaków
   EN: Lightning Rod
   PL: Lightning Rod
832. [Umiejętność wroga [808506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture next turn
   PL: [OnSucceedAttack] nakłada 2 Rozdarcia w następnej turze.
833. [Umiejętność wroga [808506] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 파열 5 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture next turn
   PL: [OnSucceedAttackHead] nakłada 5 Rozdarcia w następnej turze.
834. [Umiejętność wroga [808507] (ulepszenie 1) — nazwa] 적뢰
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808507].levelList[level=1].name
   limit: do 40 znaków
   EN: Red Bolts
   PL: Red Bolts
835. [Umiejętność wroga [808507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 10 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Rupture next turn
   PL: [OnSucceedAttack] nakłada 10 Rozdarcia w następnej turze.
836. [Umiejętność wroga [808508] (ulepszenie 1) — nazwa] 하울링
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808508].levelList[level=1].name
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [808508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL: [OnSucceedAttack] nakłada 2 Spętania w następnej turze
838. [Umiejętność wroga [808508] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 수비 위력 감소 4 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808508].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 828 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [808601] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808601].levelList[level=1].name
   limit: do 40 znaków
   EN: Bite
   PL: Bite
840. [Umiejętność wroga [808601] (ulepszenie 1) — opis] [WhenUse] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 2 Self-charge\n[DefeatDuel] Lose 1 Self-charge
   PL: [WhenUse] zyskuje 2 Samoładowania\n[DefeatDuel] zużywa 1 Samoładowanie
841. [Umiejętność wroga [808601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여, 출혈 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed and +2 Bleed Count
   PL: [OnSucceedAttack] nakłada 3 Krwawienia i zwiększa Licznik Krwawienia o 2
842. [Umiejętność wroga [808602] (ulepszenie 1) — nazwa] 꼬리찌르기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808602].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Poke
   PL: Tail Poke
843. [Umiejętność wroga [808602] (ulepszenie 1) — opis] [WhenUse] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808602].levelList[level=1].desc
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [808602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여, 출혈 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 841 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [808602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 837 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [808603] (ulepszenie 1) — nazwa] 감아 조이기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808603].levelList[level=1].name
   limit: do 40 znaków
   EN: Wrapping Coil
   PL: Wrapping Coil
847. [Umiejętność wroga [808603] (ulepszenie 1) — opis] [WhenUse] 자가 충전 2 얻음\n[DefeatDuel] 자가 충전 1 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808603].levelList[level=1].desc
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [808603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile
   PL: [OnSucceedAttack] nakłada 2 Wrażliwości
849. [Umiejętność wroga [808603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bind next turn
   PL: [OnSucceedAttackHead] nakłada 2 Spętania w następnej turze
850. [Umiejętność wroga [808604] (ulepszenie 1) — nazwa] 전류 주입
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808604].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Load
   PL: Electric Load
851. [Umiejętność wroga [808604] (ulepszenie 1) — opis] [WhenUse] 자가 충전 1 얻음\n대상에게 마비가 있다면 피해량 +10%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Self-charge\nDeal +10% damage to targets with Paralyze
   PL: [WhenUse] zyskuje 1 Samoładowanie\nzadaje +10% obrażeń celom z Paraliżem
852. [Umiejętność wroga [808604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL: [OnSucceedAttack] nakłada 3 Paraliżu
853. [Umiejętność wroga [808605] (ulepszenie 1) — nazwa] 전기 방류
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808605].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Release
   PL: Electric Release
854. [Umiejętność wroga [808605] (ulepszenie 1) — opis] [WhenUse] 자가 충전 1 얻음\n대상에게 마비가 있다면 피해량 +10%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808605].levelList[level=1].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność wroga [808605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 852 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność wroga [808606] (ulepszenie 1) — nazwa] 전기 방출
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808606].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Discharge
   PL: Electric Discharge
857. [Umiejętność wroga [808606] (ulepszenie 1) — opis] [WhenUse] 자가 충전 1 얻음\n대상에게 마비가 있다면 피해량 +20%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Self-charge\nDeal +20% damage to targets with Paralyze
   PL: [WhenUse] zyskuje 1 Samoładowanie\nzadaje +20% obrażeń celom z Paraliżem
858. [Umiejętność wroga [808606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność wroga [808606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze
   PL: [OnSucceedAttack] nakłada 5 Paraliżu
860. [Umiejętność wroga [808607] (ulepszenie 1) — nazwa] 초고압 전기 방출
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808607].levelList[level=1].name
   limit: do 50 znaków
   EN: High-voltage Electric Discharge
   PL: High-voltage Electric Discharge
861. [Umiejętność wroga [808607] (ulepszenie 1) — opis] 가지고 있는 자가 충전 전부 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808607].levelList[level=1].desc
   limit: do 120 znaków
   EN: Spend all Self-charge
   PL: zużywa całe Samoładowanie
862. [Umiejętność wroga [808607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność wroga [808607] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 축전 상태일 때, 최종 피해량의 40%만큼 고정 피해
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808607].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Capacitor, deal 40% of damage dealt as fixed damage
   PL: [OnSucceedAttack] jeżeli cel ma Kondensator, zadaje 40% zadanych obrażeń jako obrażenia stałe
864. [Umiejętność wroga [808607] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마비 3, 축전 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808607].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze and 1 Capacitor
   PL: [OnSucceedAttack] nakłada 3 Paraliżu i 1 Kondensator
865. [Umiejętność wroga [808608] (ulepszenie 1) — nazwa] 똬리틀기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808608].levelList[level=1].name
   limit: do 40 znaków
   EN: Coil Up
   PL: Coil Up
866. [Umiejętność wroga [808608] (ulepszenie 1) — opis] 이 스킬이 슬롯에 있을 때 머리 부위 현재 체력만큼 보호막 얻음.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808608].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this skill is on a slot, gain Shield by the head's current HP
   PL: gdy ta Umiejętność jest na Slocie, zyskuje Tarczę równą aktualnemu HP głowy.
867. [Umiejętność wroga [808609] (ulepszenie 1) — nazwa] 꿈틀거리는 머리
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808609].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Head
   PL: Wriggling Head
868. [Umiejętność wroga [808609] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n[WhenUse] 자가 충전 2 소모\n[DefeatDuel] 자가 충전 2 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808609].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy with the least HP\n[WhenUse] Spend 2 Self-charge\n[DefeatDuel] Lose 2 Self-charge
   PL: priorytet: wróg z najniższym HP\n[WhenUse] zużywa 2 Samoładowania\n[DefeatDuel] zużywa 2 Samoładowania
869. [Umiejętność wroga [808609] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808609].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 852 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [808610] (ulepszenie 1) — nazwa] 꿈틀거리는 꼬리
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808610].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Tail
   PL: Wriggling Tail
871. [Umiejętność wroga [808610] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n[WhenUse] 자가 충전 2 소모\n[DefeatDuel] 자가 충전 3 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808610].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the enemy with the least HP\n[WhenUse] Spend 2 Self-charge\n[DefeatDuel] Lose 3 Self-charge
   PL: priorytet: wróg z najniższym HP\n[WhenUse] zużywa 2 Samoładowania\n[DefeatDuel] zużywa 3 Samoładowania
872. [Umiejętność wroga [808610] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808610].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 852 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Umiejętność wroga [808701] (ulepszenie 1) — nazwa] 침울한 신음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808701].levelList[level=1].name
   limit: do 40 znaków
   EN: Gloomy Moan
   PL: Gloomy Moan
874. [Umiejętność wroga [808701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL: [OnSucceedAttack] nakłada 3 Zatonięcia
875. [Umiejętność wroga [808702] (ulepszenie 1) — nazwa] 몰아치는 침잠
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808702].levelList[level=1].name
   limit: do 40 znaków
   EN: Raging Withdrawal
   PL: Raging Withdrawal
876. [Umiejętność wroga [808702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL: [OnSucceedAttack] nakłada +2 Licznika Zatonięcia
877. [Umiejętność wroga [808702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 874 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność wroga [808703] (ulepszenie 1) — nazwa] 슬픔의 반동
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808703].levelList[level=1].name
   limit: do 40 znaków
   EN: Sorrowful Recoil
   PL: Sorrowful Recoil
879. [Umiejętność wroga [808703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count
   PL: [OnSucceedAttack] nakłada +3 Licznika Rozdarcia
880. [Umiejętność wroga [808703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL: [OnSucceedAttack] nakłada 2 Rozdarcia
881. [Umiejętność wroga [808704] (ulepszenie 1) — nazwa] 슬픔의 격류
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808704].levelList[level=1].name
   limit: do 40 znaków
   EN: Sorrowful Torrent
   PL: Sorrowful Torrent
882. [Umiejętność wroga [808704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL: [OnSucceedAttack] nakłada +2 Licznika Rozdarcia
883. [Umiejętność wroga [808704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL: [OnSucceedAttack] nakłada 3 Rozdarcia
884. [Umiejętność wroga [808704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL: [OnSucceedAttackHead] nakłada 2 Rozdarcia
885. [Umiejętność wroga [808705] (ulepszenie 1) — nazwa] 무언가를 찾는 울음소리
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808705].levelList[level=1].name
   limit: do 40 znaków
   EN: Cries Seeking Something
   PL: Cries Seeking Something
886. [Umiejętność wroga [808705] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 낡은 우산 소환
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Spawn an Old Umbrella next turn
   PL: [WhenUse] przywołuje Old Umbrella w następnej turze
887. [Umiejętność wroga [808705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Sinking
   PL: [OnSucceedAttack] nakłada 5 Zatonięcia
888. [Umiejętność wroga [808705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 낡은 우산 수만큼 가하는 피해량 +15%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal +15% damage for each Old Umbrella
   PL: [OnSucceedAttackHead] zadaje +15% obrażeń za każdy Old Umbrella
889. [Umiejętność wroga [808706] (ulepszenie 1) — nazwa] 기다림
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808706].levelList[level=1].name
   limit: do 40 znaków
   EN: Waiting
   PL: Waiting
890. [Umiejętność wroga [808706] (ulepszenie 1) — opis] [StartBattle] 모든 적 정신력 -20
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] All enemies lose 20 SP
   PL: [StartBattle] wszyscy wrogowie tracą 20 SP
891. [Umiejętność wroga [808801] (ulepszenie 1) — nazwa] 흩뿌려지는 슬픔
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808801].levelList[level=1].name
   limit: do 40 znaków
   EN: Scattering Sorrow
   PL: Scattering Sorrow
892. [Umiejętność wroga [808801] (ulepszenie 1) — opis] [EndSkill] 모든 적의 파열 횟수 2, 침잠 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Inflict +2 Rupture Count and +2 Sinking Count to all enemies
   PL: [EndSkill] nakłada +2 Licznika Rozdarcia i +2 Licznika Zatonięcia wszystkim wrogom
893. [Umiejętność wroga [808901] (ulepszenie 1) — nazwa] 얽혀가는 부적
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808901].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangling Talisman
   PL: Entangling Talisman
894. [Umiejętność wroga [808901] (ulepszenie 1) — opis] [WhenUse] 대상에게 얽혀온 저주 부적 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 2 Entangled Curse Talisman
   PL: [WhenUse] nakłada 2 Splątane Talizmany Przekleństwa
895. [Umiejętność wroga [808901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 2 부여. 파열 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture and +2 Rupture Count next turn
   PL: [OnSucceedAttack] nakłada 2 Rozdarcia i +2 Licznika Rozdarcia w następnej turze
896. [Umiejętność wroga [808902] (ulepszenie 1) — nazwa] 쌓여가는 저주
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808902].levelList[level=1].name
   limit: do 40 znaków
   EN: Cumulating Curse
   PL: Cumulating Curse
897. [Umiejętność wroga [808902] (ulepszenie 1) — opis] [WhenUse] 대상에게 얽혀온 저주 부적 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 1 Entangled Curse Talisman
   PL: [WhenUse] nakłada 1 Splątany Talizman Przekleństwa
898. [Umiejętność wroga [808902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 가지고 있는 얽혀온 저주 부적 만큼 얽혀온 저주 부적 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Entangled Curse Talisman by target's Entangled Curse Talisman
   PL: [OnSucceedAttack] nakłada tyle Splątanych Talizmanów Przekleństwa, ile ich posiada cel
899. [Umiejętność wroga [808902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture next turn
   PL: [OnSucceedAttackHead] nakłada 5 Rozdarcia w następnej turze
900. [Umiejętność wroga [808902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 2 부여. 다음 턴에 파열 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture and +2 Rupture Count next turn
   PL: [OnSucceedAttackHead] nakłada 2 Rozdarcia i +2 Licznika Rozdarcia w następnej turze
901. [Umiejętność wroga [808903] (ulepszenie 1) — nazwa] 누구도 울지 않도록
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808903].levelList[level=1].name
   limit: do 40 znaków
   EN: So That No One Will Cry
   PL: So That No One Will Cry
902. [Umiejętność wroga [808903] (ulepszenie 1) — opis] [EndBattle] 다시 붙여진 저주 부적 전부 소멸
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Remove all Reattached Curse Talisman
   PL: [EndBattle] usuwa wszystkie Ponownie Przyklejone Talizmany Przekleństwa
903. [Umiejętność wroga [808903] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808903].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 5 Paraliżu w następnej turze
904. [Umiejętność wroga [808903] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 속박 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808903].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Bind next turn
   PL: [OnSucceedAttackHead] nakłada 5 Spętania w następnej turze
905. [Umiejętność wroga [808904] (ulepszenie 1) — nazwa] 이전하는 부적
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808904].levelList[level=1].name
   limit: do 40 znaków
   EN: Transferring Talisman
   PL: Transferring Talisman
906. [Umiejętność wroga [808904] (ulepszenie 1) — opis] [WhenUse] 대상의 얽혀온 저주 부적 을 전부 소멸. 소멸시킨만큼 다시 붙여진 저주 부적 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808904].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Remove all Entangled Curse Talisman from target; Gain the same amount of Reattached Curse Talisman
   PL: [WhenUse] usuwa wszystkie Splątane Talizmany Przekleństwa celu. zyskuje tyle Ponownie Przyklejonych Talizmanów Przekleństwa, ile ich usunął.
907. [Umiejętność wroga [808905] (ulepszenie 1) — nazwa] 복제되는 저주
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808905].levelList[level=1].name
   limit: do 40 znaków
   EN: Proliferating Curse
   PL: Proliferating Curse
908. [Umiejętność wroga [808905] (ulepszenie 1) — opis] [WhenUse] 대상이 가지고 있는 얽혀온 저주 부적 만큼 얽혀온 저주 부적 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=808905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict Entangled Curse Talisman by target's Entangled Curse Talisman
   PL: [WhenUse] nakłada tyle Splątanych Talizmanów Przekleństwa, ile ich posiada cel
909. [Umiejętność wroga [809001] (ulepszenie 1) — nazwa] 취하고 싶나?
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809001].levelList[level=1].name
   limit: do 40 znaków
   EN: Wanna Get Drunk?
   PL: Wanna Get Drunk?
910. [Umiejętność wroga [809001] (ulepszenie 1) — opis] 합 진행 시 고양 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809001].levelList[level=1].desc
   limit: do 120 znaków
   EN: In a clash, give 1 Morale Boost
   PL: podczas Starcia nakłada 1 Uniesienia
911. [Umiejętność wroga [809001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여, 진동 횟수 2 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Tremor and +2 Tremor Count
   PL: [OnSucceedAttack] nakłada 5 Wstrząsu i zwiększa Licznik Wstrząsu o 2
912. [Umiejętność wroga [809002] (ulepszenie 1) — nazwa] 나눠 마시자!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809002].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Share the Drink!
   PL: Let's Share the Drink!
913. [Umiejętność wroga [809002] (ulepszenie 1) — opis] 합 진행 시 고양 2 부여\n[WhenUse] 체력 5% 회복
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: In a clash, give 2 Morale Boost\n[WhenUse] Heal 5% HP
   PL: podczas Starcia nakłada 2 Uniesienia\n[WhenUse] przywraca 5% HP
914. [Umiejętność wroga [809002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 837 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [809003] (ulepszenie 1) — nazwa] 남은건 이것 뿐이네!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809003].levelList[level=1].name
   limit: do 40 znaków
   EN: This is All I Got!
   PL: This is All I Got!
916. [Umiejętność wroga [809003] (ulepszenie 1) — opis] 합 진행 시 고양 2 부여\n진동을 가진 대상 우선 공격
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a clash, give 2 Morale Boost\nPrioritizes enemies with Tremor
   PL: podczas Starcia nakłada 2 Uniesienia\npriorytet: wrogowie z Wstrząsem
917. [Umiejętność wroga [809003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 진동 횟수만큼 진동 폭발
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst by target's Tremor Count
   PL: [OnSucceedAttack] uruchamia Wyładowanie Wstrząsu tyle razy, ile wynosi Licznik Wstrząsu celu
918. [Umiejętność wroga [809004] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809004].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Have This!
   PL: I'll Have This!
919. [Umiejętność wroga [809004] (ulepszenie 1) — opis] [CantDuel]\n대상 변경 불가.\n고양 을 가진 대상 우선 공격\n대상에게 취기 가 없다면, 합 위력 +5
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809004].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nCannot be redirected\nPrioritizes enemies with Morale Boost\nIf target has no Tipsy, Clash Power +5
   PL: [CantDuel]\nnie można przekierować.\npriorytet: wrogowie z Uniesieniem\njeżeli cel nie ma Pijackiego Nastroju, Moc Starcia +5
920. [Umiejętność wroga [809004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 고양을 가지고 있다면, 고양 만큼 피해량 +10%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Morale Boost, deal +10% damage for each Count
   PL: [OnSucceedAttack] jeżeli cel ma Uniesienie, zadaje +10% obrażeń za każdy Licznik
921. [Umiejętność wroga [809004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 취기 를 가지고 있다면, 주는 피해가 0이 되고 자신의 체력 -50
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Tipsy, deal 0 damage, and user loses 50 HP
   PL: [OnSucceedAttack] jeżeli cel ma Pijacki Nastrój, zadaje 0 obrażeń, a użytkownik traci 50 HP
922. [Umiejętność wroga [809004] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 고양 혹은 취기 전부 소모 시킴
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809004].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove all Morale Boost or Tipsy
   PL: [OnSucceedAttack] usuwa całe Uniesienie albo Pijacki Nastrój
923. [Umiejętność wroga [809005] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809005].levelList[level=1].name
   (powtórzenie elementu 918 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
