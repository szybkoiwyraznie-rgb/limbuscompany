# Paczka AI P86 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 22/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P86_3c_przeciwnicy_i_anomalie_cz22.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P86_3c_przeciwnicy_i_anomalie_cz22.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [twth] Umiejętności wrogów / Anomalii — Skills_Abnormality-twth
- grupa rozdziału/trybu: `twth` · plik: `Skills_Abnormality-twth.json`

1. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
2. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
3. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 5, efekt 2 — opis] <color=#ff6000><mark=#ff000040><b><u>이 코인은 모든 대상에게 적중</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>
   EN: <color=#ff6000><mark=#ff000040><b><u>This Coin hits all targets</u></b></mark></color>
   PL:
4. [Umiejętność wroga [500604] (ulepszenie 1) — nazwa] 크리틱
   źródło: Skills_Abnormality-twth.json :: dataList[id=500604].levelList[level=1].name
   limit: do 40 znaków
   EN: Critique
   PL:
5. [Umiejętność wroga [500604] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse]\n- 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 합 위력 +2 (최대 12)\n- 전장의 <color=#ff6000><mark=#ff000040><b><u>아군 야수파 스튜던트 1명당</u></b></mark></color> 피해량 +12.5% (최대 50%)\n- 대상에게 <color=#ff6000><mark=#ff000040><b><u>[IntenseColors]가 있으면,</u></b></mark></color> 합 위력 +6, 피해량 +200%\n· 대상이 [IntenseColors]를 보유한 상태에서 <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착했으면,</u></b></mark></color> 대신 합 위력 +6, 피해량 -90%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=500604].levelList[level=1].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [WhenUse], [IntenseColors], [Sinking], [DefeatDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [IntenseColors] = 강렬한 색채 / Palette Vibrante; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CantChangeTarget]\n[WhenUse]\n- Clash Power +2 <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on target (max 12)\n- Deal +12.5% damage <color=#ff6000><mark=#ff000040><b><u>for every allied Fauvist Student of the Ring</u></b></mark></color> on the field (max 50%)\n- <color=#ff6000><mark=#ff000040><b><u>If target has [IntenseColors], </u></b></mark></color>Clash Power +6 and deal +200% damage\n· <color=#ff6000><mark=#ff000040><b><u>If target has equipped Defense Skills</u></b></mark></color> while having [IntenseColors], Clash Power +6 and deal -90% damage; instead. Damage from this Skill does not Stagger the target; On Hit, does not trigger [Sinking] effects on the target\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
6. [Umiejętność wroga [500604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Umiejętność wroga [500604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이 코인 재사용 (최대 2회)\n- 합 패배 후 적중 시, 대신 이 코인 재사용 (최대 1회)\n- 대상이 수비 스킬 장착 시, 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=500604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Reuse this Coin (max 2 times)\n- On Hit after losing a Clash, Reuse this Coin (max once instead)\n- Does not trigger if target has equipped Defense Skills
   PL:
8. [Umiejętność wroga [500604] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=500604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL:
9. [Umiejętność wroga [500604] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=500604].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +2 [Sinking] Count
   PL:
10. [Umiejętność wroga [500704] (ulepszenie 1) — nazwa] 영감의 전율
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].name
   limit: do 40 znaków
   EN: The Thrill of Inspiration
   PL:
11. [Umiejętność wroga [500704] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 최종 위력 +1, 피해량 +10% (각각 최대 6, 60%)\n[WinDuel]\n- 각 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 피해량 +10% (최대 60%, 대상 별로 판정)\n[DefeatDuel]\n- 피해량 -75%\n- 이 스킬의 효과로 부여하는 [BearClawWound], [EagleClawWound] 수치가 1/3으로 감소 (소수점 올림)\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [WinDuel], [DefeatDuel], [BearClawWound], [EagleClawWound], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]; [Sinking] = 침잠 / Sinking
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse] Final Power +1 and deal +10% damage <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on the main target (max 6 and 60% respectively)\n[WinDuel]\n- Deal +10% damage <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on each target (max 60% against each target)\n[DefeatDuel]\n- Deal -75% damage\n- Inflict 2/3 less Stacks of [BearClawWound] and [EagleClawWound] with this Skill's effect (rounded up)\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
12. [Umiejętność wroga [500704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność wroga [500704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration] and +3 [Laceration] Count
   PL:
14. [Umiejętność wroga [500704] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking] and +3 [Sinking] Count
   PL:
15. [Umiejętność wroga [500704] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[BearClawWound] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [BearClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 9 [BearClawWound]</u></b></mark></color>
   PL:
16. [Umiejętność wroga [500704] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[EagleClawWound] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [EagleClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 9 [EagleClawWound]</u></b></mark></color>
   PL:
17. [Umiejętność wroga [500704] (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[BoldBrushstrokes] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=500704].levelList[level=1].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [BoldBrushstrokes]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoldBrushstrokes] = 과감한 터치 / Touche Hardie
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 1 [BoldBrushstrokes]</u></b></mark></color>
   PL:
18. [Umiejętność wroga [500705] (ulepszenie 1) — nazwa] 당신의 피부 아래 맥동하는 붉은 색감을 거칠게.
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].name
   limit: do 70 znaków
   EN: Burst Forth the Pulsing Crimson under Your Skin.
   PL:
19. [Umiejętność wroga [500705] (ulepszenie 1) — opis] [WideAreaRampage]\n[IntenseColors]를 보유한 대상을 우선으로 지정\n대상의 수비 스킬을 발동시키지 않음 (합 가능 수비 제외)\n속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 최종 위력 +1 (최대 6)\n- 메인 타겟에게 <color=#ff6000><mark=#ff000040><b><u>[IntenseColors]가 있으면,</u></b></mark></color> 합 위력 +6\n- 대상에게 <color=#ff6000><mark=#ff000040><b><u>[IntenseColors]가 있으면,</u></b></mark></color> 피해량 +200%\n(대상 별로 판정)\n· 타겟 중 [IntenseColors]를 보유한 상태에서 <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착한 대상</u></b></mark></color>에게는, 대신 피해량 -90%\n[WinDuel]\n- 각 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 피해량 +10% (최대 60%, 대상 별로 판정)\n[DefeatDuel]\n- [AttackDmgDown] 5, [Paralysis] 5 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].desc
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [IntenseColors], [WhenUse], [WinDuel], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [IntenseColors] = 강렬한 색채 / Palette Vibrante; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking …
   EN: [WideAreaRampage]\nPrioritizes targets that have [IntenseColors]\nThis Skill does not trigger Defense Skills (excluding Clashable Guard)\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Final Power +1 <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on the main target (max 6)\n- <color=#ff6000><mark=#ff000040><b><u>If the main target has [IntenseColors],</u></b></mark></color> Clash Power +6\n- <color=#ff6000><mark=#ff000040><b><u>If target has [IntenseColors],</u></b></mark></color> deal +200% damage (against each target separately)\n· <color=#ff6000><mark=#ff000040><b><u>If target has equipped Defense Skills</u></b></mark></color> while having [IntenseColors], deal -90% damage instead\n[WinDuel]\n- Deal +10% damage <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect on target</u></b></mark></color> (max 60%, against each target separately)\n[DefeatDuel]\n- Gain 5 [AttackDmgDown] and 5 [Paralysis]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target\n[EndSkill] End this turn
   PL:
20. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL:
22. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
24. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL:
26. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Umiejętność wroga [500705] (ulepszenie 1) — moneta 5, efekt 2 — opis] <color=#ff6000><mark=#ff000040><b><u>이 코인은 모든 대상에게 적중</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=500705].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [twth] Umiejętności wrogów / Anomalii — Skills_Enemy-twth
- grupa rozdziału/trybu: `twth` · plik: `Skills_Enemy-twth.json`

30. [Umiejętność wroga [9104301] (ulepszenie 1) — nazwa] 야만스러운 타격
   źródło: Skills_Enemy-twth.json :: dataList[id=9104301].levelList[level=1].name
   limit: do 40 znaków
   EN: Wildstroke
   PL:
31. [Umiejętność wroga [9104301] (ulepszenie 1) — opis] [WhenUse] 대상에게 [BearClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-twth.json :: dataList[id=9104301].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BearClawWound], [Laceration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target does not have [BearClawWound], Clash Power +1\n[WhenUse] If target has 6+ ([Laceration] + [Sinking]), Coin Power +1
   PL:
32. [Umiejętność wroga [9104301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
33. [Umiejętność wroga [9104301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
34. [Umiejętność wroga [9104302] (ulepszenie 1) — nazwa] 신속한 데생
   źródło: Skills_Enemy-twth.json :: dataList[id=9104302].levelList[level=1].name
   limit: do 40 znaków
   EN: Dessin Rapide
   PL:
35. [Umiejętność wroga [9104302] (ulepszenie 1) — opis] [WhenUse] 대상에게 [BearClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 찢긴 색채가 5 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104302].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BearClawWound], [Laceration], [Sinking], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target does not have [BearClawWound], Clash Power +1\n[WhenUse] If target has 6+ ([Laceration] + [Sinking]), Coin Power +1\n[WhenUse] If target has 5+ Mauled Color, convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
36. [Umiejętność wroga [9104302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność wroga [9104302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [9104302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
39. [Umiejętność wroga [9104303] (ulepszenie 1) — nazwa] 야수파 - 칠하고 펼쳐내기
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].name
   limit: do 50 znaków
   EN: Le Fauvisme - Paint and Unfurl
   PL:
40. [Umiejętność wroga [9104303] (ulepszenie 1) — opis] 대상의 찢긴 색채 3당, 피해량 +10% (최대 30%)\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 체력이 50% 미만이거나, 대상의 찢긴 색채가 5 이상이면, 3코인이 추가되며 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Sinking], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +10% damage for every 3 Mauled Color on target (max 30%)\n[WhenUse] If target has 6+ ([Laceration] + [Sinking]), Coin Power +1\n[WhenUse] At less than 50% HP, or if target has 5+ Mauled Color, use Coin 3 an additional time and convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
41. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
42. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność wroga [9104303] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [BearClawWound] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104303].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BearClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [OnSucceedAttack] Inflict 1 [BearClawWound]
   PL:
48. [Umiejętność wroga [9104304] (ulepszenie 1) — nazwa] 덧댐
   źródło: Skills_Enemy-twth.json :: dataList[id=9104304].levelList[level=1].name
   limit: do 40 znaków
   EN: Gusset
   PL:
49. [Umiejętność wroga [9104304] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상에게 [BearClawWound]가 있으면 최종 위력 +2
   źródło: Skills_Enemy-twth.json :: dataList[id=9104304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [BearClawWound]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [DuelCounter]\n[WhenUse] If target has [BearClawWound], Final Power +2
   PL:
50. [Umiejętność wroga [9104304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [9104401] (ulepszenie 1) — nazwa] 야만스러운 타격
   źródło: Skills_Enemy-twth.json :: dataList[id=9104401].levelList[level=1].name
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [9104401] (ulepszenie 1) — opis] [WhenUse] 대상에게 [BearClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-twth.json :: dataList[id=9104401].levelList[level=1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [9104401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Umiejętność wroga [9104401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność wroga [9104402] (ulepszenie 1) — nazwa] 신속한 데생
   źródło: Skills_Enemy-twth.json :: dataList[id=9104402].levelList[level=1].name
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [9104402] (ulepszenie 1) — opis] [WhenUse] 대상에게 [BearClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 찢긴 색채가 5 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104402].levelList[level=1].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [9104402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
58. [Umiejętność wroga [9104402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [9104402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
60. [Umiejętność wroga [9104403] (ulepszenie 1) — nazwa] 야수파 - 칠하고 펼쳐내기
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].name
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [9104403] (ulepszenie 1) — opis] 대상의 찢긴 색채 3당, 피해량 +10% (최대 30%)\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 체력이 50% 미만이거나, 대상의 찢긴 색채가 5 이상이면, 3코인이 추가되며 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Umiejętność wroga [9104403] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [BearClawWound] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104403].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Umiejętność wroga [9104404] (ulepszenie 1) — nazwa] 덧댐
   źródło: Skills_Enemy-twth.json :: dataList[id=9104404].levelList[level=1].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [9104404] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상에게 [BearClawWound]가 있으면 최종 위력 +2
   źródło: Skills_Enemy-twth.json :: dataList[id=9104404].levelList[level=1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Umiejętność wroga [9104404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Umiejętność wroga [9104501] (ulepszenie 1) — nazwa] 작품 준비
   źródło: Skills_Enemy-twth.json :: dataList[id=9104501].levelList[level=1].name
   limit: do 40 znaków
   EN: Artwork Preparation
   PL:
73. [Umiejętność wroga [9104501] (ulepszenie 1) — opis] [WhenUse] 대상에게 [EagleClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-twth.json :: dataList[id=9104501].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EagleClawWound], [Laceration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target does not have [EagleClawWound], Clash Power +1\n[WhenUse] If target has 6+ ([Laceration] + [Sinking]), Coin Power +1
   PL:
74. [Umiejętność wroga [9104501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
75. [Umiejętność wroga [9104501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność wroga [9104502] (ulepszenie 1) — nazwa] 신속한 표현
   źródło: Skills_Enemy-twth.json :: dataList[id=9104502].levelList[level=1].name
   limit: do 40 znaków
   EN: Brisk Expression
   PL:
77. [Umiejętność wroga [9104502] (ulepszenie 1) — opis] [WhenUse] 대상에게 [EagleClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 찢긴 색채가 5 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104502].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EagleClawWound], [Laceration], [Sinking], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target does not have [EagleClawWound], Clash Power +1\n[WhenUse] If target has 6+ ([Laceration] + [Sinking]), Coin Power +1\n[WhenUse] If target has 5+ Mauled Color, convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
78. [Umiejętność wroga [9104502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
79. [Umiejętność wroga [9104502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Umiejętność wroga [9104502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신에게 [Agility]이 있다면 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Enemy-twth.json :: dataList[id=9104502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] If this unit has [Agility], Reuse this Coin (once per Skill)
   PL:
81. [Umiejętność wroga [9104503] (ulepszenie 1) — nazwa] 작업 마무리
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].name
   limit: do 40 znaków
   EN: Finishing Touch
   PL:
82. [Umiejętność wroga [9104503] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 체력이 50% 미만이거나 대상의 찢긴 색채가 5 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Sinking], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)\n[WhenUse] At less than 50% HP, or if target has 5+ Mauled Color, convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
83. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
84. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność wroga [9104503] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 자신에게 [Agility]이 있다면 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Enemy-twth.json :: dataList[id=9104503].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność wroga [9104504] (ulepszenie 1) — nazwa] 부분 수정
   źródło: Skills_Enemy-twth.json :: dataList[id=9104504].levelList[level=1].name
   limit: do 40 znaków
   EN: Partial Rework
   PL:
91. [Umiejętność wroga [9104504] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상에게 [EagleClawWound]가 있으면 합 위력 +2
   źródło: Skills_Enemy-twth.json :: dataList[id=9104504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [EagleClawWound]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [DuelCounter]\n[WhenUse] If target has [EagleClawWound], Clash Power +2
   PL:
92. [Umiejętność wroga [9104504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EagleClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [OnSucceedAttack] Inflict 2 [EagleClawWound]
   PL:
93. [Umiejętność wroga [9104504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność wroga [9104601] (ulepszenie 1) — nazwa] 작품 준비
   źródło: Skills_Enemy-twth.json :: dataList[id=9104601].levelList[level=1].name
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [9104601] (ulepszenie 1) — opis] [WhenUse] 대상에게 [EagleClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-twth.json :: dataList[id=9104601].levelList[level=1].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność wroga [9104601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
97. [Umiejętność wroga [9104601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Umiejętność wroga [9104602] (ulepszenie 1) — nazwa] 신속한 표현
   źródło: Skills_Enemy-twth.json :: dataList[id=9104602].levelList[level=1].name
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Umiejętność wroga [9104602] (ulepszenie 1) — opis] [WhenUse] 대상에게 [EagleClawWound]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 찢긴 색채가 5 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104602].levelList[level=1].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność wroga [9104602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Umiejętność wroga [9104602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Umiejętność wroga [9104602] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신에게 [Agility]이 있다면 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Enemy-twth.json :: dataList[id=9104602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Umiejętność wroga [9104603] (ulepszenie 1) — nazwa] 작업 마무리
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].name
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność wroga [9104603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 체력이 50% 미만이거나 대상의 찢긴 색채가 5 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].desc
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Umiejętność wroga [9104603] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 자신에게 [Agility]이 있다면 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Enemy-twth.json :: dataList[id=9104603].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Umiejętność wroga [9104604] (ulepszenie 1) — nazwa] 부분 수정
   źródło: Skills_Enemy-twth.json :: dataList[id=9104604].levelList[level=1].name
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Umiejętność wroga [9104604] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상에게 [EagleClawWound]가 있으면 합 위력 +2
   źródło: Skills_Enemy-twth.json :: dataList[id=9104604].levelList[level=1].desc
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność wroga [9104604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Umiejętność wroga [9104604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9104604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Umiejętność wroga [9103401] (ulepszenie 1) — nazwa] 목표 포착
   źródło: Skills_Enemy-twth.json :: dataList[id=9103401].levelList[level=1].name
   limit: do 40 znaków
   EN: Target Sighted
   PL:
117. [Umiejętność wroga [9103401] (ulepszenie 1) — opis] 대상에게 [IndexPrescriptTargetToPersonality]이 있으면, 합 위력 +1, 피해량 +10%\n자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 대상에게 [IndexPrescriptTargetToPersonality]이 있거나 [BlessingOfIndexPrescriptEnemy]가 6 이상이면, 이 스킬의 마지막 코인이 [SuperCoin]이 됨\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103401].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality], [Breath], [Sinking], [WhenUse], [BlessingOfIndexPrescriptEnemy], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [IndexPrescriptTargetToPersonality], Clash Power +1 and deal +10% damage\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[WhenUse] At 6+ [BlessingOfIndexPrescriptEnemy], or if target has [IndexPrescriptTargetToPersonality], convert the final Coin of this Skill into [SuperCoin]\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
118. [Umiejętność wroga [9103401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność wroga [9103401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [9103402] (ulepszenie 1) — nazwa] 지령이 향하는 곳
   źródło: Skills_Enemy-twth.json :: dataList[id=9103402].levelList[level=1].name
   limit: do 50 znaków
   EN: To Where the Prescript Points
   PL:
121. [Umiejętność wroga [9103402] (ulepszenie 1) — opis] 대상에게 [IndexPrescriptTargetToPersonality]이 있으면, 합 위력 +1, 피해량 +20%\n자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 3)\n[WhenUse] 대상에게 [IndexPrescriptTargetToPersonality]이 있거나 [BlessingOfIndexPrescriptEnemy]가 6 이상이면, 이 스킬의 마지막 코인이 [SuperCoin]이 됨\n[WhenUse] [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103402].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality], [Breath], [Sinking], [WhenUse], [BlessingOfIndexPrescriptEnemy], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [IndexPrescriptTargetToPersonality], Clash Power +1 and deal +20% damage\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 3)\n[WhenUse] At 6+ [BlessingOfIndexPrescriptEnemy], or if target has [IndexPrescriptTargetToPersonality], convert the final Coin of this Skill into [SuperCoin]\n[WhenUse] Gain 3 [Breath] and +3 [Breath] Count\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
122. [Umiejętność wroga [9103402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL:
123. [Umiejętność wroga [9103402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność wroga [9103402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [9103403] (ulepszenie 1) — nazwa] 지령 수행
   źródło: Skills_Enemy-twth.json :: dataList[id=9103403].levelList[level=1].name
   limit: do 40 znaków
   EN: Undertake Prescript
   PL:
126. [Umiejętność wroga [9103403] (ulepszenie 1) — opis] 대상에게 [IndexPrescriptTargetToPersonality]이 있으면, 합 위력 +2, 피해량 +25%\n자신의 [Breath]과 대상의 [Sinking]의 합 6당 최종 위력 +1 (최대 3)\n[WhenUse] [BlessingOfIndexPrescriptEnemy]가 3 이상이면, 코인 위력 +1\n[WhenUse] 대상에게 [IndexPrescriptTargetToPersonality]이 있거나 [BlessingOfIndexPrescriptEnemy]가 6 이상이면, 모든 코인이 [SuperCoin]이 됨\n[WhenUse] [Breath] 4 얻음, 자신의 [Breath] 횟수 3 증가\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103403].levelList[level=1].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality], [Breath], [Sinking], [WhenUse], [BlessingOfIndexPrescriptEnemy], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [IndexPrescriptTargetToPersonality], Clash Power +2 and deal +25% damage\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 3)\n[WhenUse] At 3+ [BlessingOfIndexPrescriptEnemy], Coin Power +1\n[WhenUse] At 6+ [BlessingOfIndexPrescriptEnemy], or if target has [IndexPrescriptTargetToPersonality], convert all Coins of this Skill into [SuperCoin]\n[WhenUse] Gain 4 [Breath] and +3 [Breath] Count\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
127. [Umiejętność wroga [9103403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność wroga [9103403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Umiejętność wroga [9103403] (ulepszenie 1) — moneta 3, efekt 1 — opis] 자신의 [BlessingOfIndexPrescriptEnemy] 1당 피해량 +5% (최대 45%)
   źródło: Skills_Enemy-twth.json :: dataList[id=9103403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Deal +5% damage for every [BlessingOfIndexPrescriptEnemy] on self (max 45%)
   PL:
130. [Umiejętność wroga [9103403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9103403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +2 [Sinking] Count
   PL:
131. [Umiejętność wroga [9103501] (ulepszenie 1) — nazwa] 목표 포착
   źródło: Skills_Enemy-twth.json :: dataList[id=9103501].levelList[level=1].name
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [9103501] (ulepszenie 1) — opis] 대상에게 [IndexPrescriptTargetToPersonality]이 있으면, 합 위력 +1, 피해량 +10%\n자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 대상에게 [IndexPrescriptTargetToPersonality]이 있거나 [BlessingOfIndexPrescriptEnemy]가 6 이상이면, 이 스킬의 마지막 코인이 [SuperCoin]이 됨\n[WhenUse] [Breath] 1 얻음, 자신의 [Breath] 횟수 3 증가\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103501].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality], [Breath], [Sinking], [WhenUse], [BlessingOfIndexPrescriptEnemy], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [IndexPrescriptTargetToPersonality], Clash Power +1 and deal +10% damage\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[WhenUse] At 6+ [BlessingOfIndexPrescriptEnemy], or if target has [IndexPrescriptTargetToPersonality], convert the final Coin of this Skill into [SuperCoin]\n[WhenUse] Gain 1 [Breath] and +3 [Breath] Count\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
133. [Umiejętność wroga [9103501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [9103501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9103501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking] and +2 [Sinking] Count
   PL:
135. [Umiejętność wroga [9103502] (ulepszenie 1) — nazwa] 지령이 향하는 곳
   źródło: Skills_Enemy-twth.json :: dataList[id=9103502].levelList[level=1].name
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [9103502] (ulepszenie 1) — opis] 대상에게 [IndexPrescriptTargetToPersonality]이 있으면, 합 위력 +1, 피해량 +20%\n자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 3)\n[WhenUse] 대상에게 [IndexPrescriptTargetToPersonality]이 있거나 [BlessingOfIndexPrescriptEnemy]가 6 이상이면, 이 스킬의 마지막 코인이 [SuperCoin]이 됨\n[WhenUse] [Breath] 4 얻음, 자신의 [Breath] 횟수 2 증가\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103502].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality], [Breath], [Sinking], [WhenUse], [BlessingOfIndexPrescriptEnemy], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [IndexPrescriptTargetToPersonality], Clash Power +1 and deal +20% damage\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 3)\n[WhenUse] At 6+ [BlessingOfIndexPrescriptEnemy], or if target has [IndexPrescriptTargetToPersonality], convert the final Coin of this Skill into [SuperCoin]\n[WhenUse] Gain 4 [Breath] and +2 [Breath] Count\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
137. [Umiejętność wroga [9103502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [9103502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [9103502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9103502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 134 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [9103503] (ulepszenie 1) — nazwa] 지령 수행
   źródło: Skills_Enemy-twth.json :: dataList[id=9103503].levelList[level=1].name
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [9103503] (ulepszenie 1) — opis] 대상에게 [IndexPrescriptTargetToPersonality]이 있으면, 합 위력 +2, 피해량 +25%\n자신의 [Breath]과 대상의 [Sinking]의 합 6당 최종 위력 +1 (최대 3)\n[WhenUse] [BlessingOfIndexPrescriptEnemy]가 3 이상이면, 코인 위력 +1\n[WhenUse] 대상에게 [IndexPrescriptTargetToPersonality]이 있거나 [BlessingOfIndexPrescriptEnemy]가 6 이상이면, 모든 코인이 [SuperCoin]이 됨\n[WhenUse] [Breath] 3 얻음, 자신의 [Breath] 횟수 4 증가\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103503].levelList[level=1].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality], [Breath], [Sinking], [WhenUse], [BlessingOfIndexPrescriptEnemy], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has [IndexPrescriptTargetToPersonality], Clash Power +2 and deal +25% damage\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 3)\n[WhenUse] At 3+ [BlessingOfIndexPrescriptEnemy], Coin Power +1\n[WhenUse] At 6+ [BlessingOfIndexPrescriptEnemy], or if target has [IndexPrescriptTargetToPersonality], convert all Coins of this Skill into [SuperCoin]\n[WhenUse] Gain 3 [Breath] and +4 [Breath] Count\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL:
142. [Umiejętność wroga [9103503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Enemy-twth.json :: dataList[id=9103503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [9103503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-twth.json :: dataList[id=9103503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność wroga [9103503] (ulepszenie 1) — moneta 3, efekt 1 — opis] 자신의 [BlessingOfIndexPrescriptEnemy] 1당 피해량 +5% (최대 45%)
   źródło: Skills_Enemy-twth.json :: dataList[id=9103503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [9103503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-twth.json :: dataList[id=9103503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +3 [Sinking] Count
   PL:

## [twth] Pasywka wroga: Passives_Abnormality-twth
- plik gry: `Passives_Abnormality-twth.json`

146. [[twth] Pasywka wroga [142201] — nazwa] 약지 야수파 도슨트
   źródło: Passives_Abnormality-twth.json :: dataList[id=142201].name
   limit: do 40 znaków
   EN: The Ring's Docent of Fauvism
   PL:
147. [[twth] Pasywka wroga [142201] — opis] 턴 시작 시 아군 약지 야수파 스튜던트 1명당 <color=#ff6000><mark=#ff000040><b><u>[Protection] 2 얻음</u></b></mark></color>\n- 이번 전투에서 ‘크리틱’을 사용하였다면 이후 턴부터는 효과가 강화되어, 대신 [Protection] 2 얻고 정신력 5 회복\n(정신력이 -15 미만이면, 정신력 회복 효과가 2배로 적용)\n- 아군 약지 야수파 스튜던트가 없으면, 대신 [Vulnerable] 2 얻고 정신력 0까지 감소\n\n공격 가중치가 1인 스킬로 피격받기 직전에 다른 아군 스튜던트가 있으면,\n대상이 <color=#ff6000><mark=#ff000040><b><u>공격을 대신 받도록 함 (턴당 2회, 조력자 제외)</u></b></mark></color>\n\n‘크리틱’을 사용한 턴 종료 시 이번 전투에서 사망한 아군 약지 야수파 스튜던트가 있으면, 그 자리를 <color=#ff6000><mark=#ff000040><b><u>동일한 스튜던트를 불러와 다시 채움</u></b></mark></color>\n- 이 효과로 등장한 스튜던트는 매턴 시작 시, 이번 전투 동안 사망한 아군 수만큼 [Vulnerable], [AttackDown] 얻음 (각각 최대 10)
   źródło: Passives_Abnormality-twth.json :: dataList[id=142201].desc
   limit: do 1130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Protection], [Vulnerable], [AttackDown]
   znaczenie tagów: [Protection] = 보호 / Protection; [Vulnerable] = 취약 / Fragile; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Gain 2 [Protection]</u></b></mark></color> for every allied Fauvist Student of the Ring\n- If this unit used "Critique" in this Encounter, gain 2 [Protection] and heal 5 SP instead starting from the next turn\n(At lower than -15 SP, double the SP-healing effect)\n- If there are no allied Fauvist Students of the Ring, gain 2 [Vulnerable] and reduce this unit's SP down to 0 instead\n\nImmediately Before Getting Hit by a Skill that has 1 Atk Weight, if there is an allied Student of the Ring, <color=#ff6000><mark=#ff000040><b><u>have the said unit take the attack instead (2 times per turn, excluding Assist Units)</u></b></mark></color>\n\nTurn End of the turn this unit used "Critique": If an allied Fauvist Student of the Ring was defeated in this Encounter, <color=#ff6000><mark=#ff000040><b><u>refill its vacancy with the same Student unit</u></b></mark></color>\n- Every Turn Start: The Student that refilled the vacancy due to this effect gains (# of allies defeated in this Encounter) [Vulnerable] and [AttackDown] (max 10 each)
   PL:
148. [[twth] Pasywka wroga [142201] — podsumowanie] 피격받기 직전, 다른 아군 스튜던트가 공격 대신 받게 함
   źródło: Passives_Abnormality-twth.json :: dataList[id=142201].summary
   limit: do 120 znaków
   EN: Immediately before getting hit, force an allied Student to take the hit instead
   PL:
149. [[twth] Pasywka wroga [142202] — nazwa] 지도 편달
   źródło: Passives_Abnormality-twth.json :: dataList[id=142202].name
   limit: do 40 znaków
   EN: Mentorship
   PL:
150. [[twth] Pasywka wroga [142202] — opis] 턴 시작 시 아군 약지 야수파 스튜던트에게\n각 대상이 생존한 턴 수(현재 턴 포함)만큼\n[AttackUp], [DefenseUp]를 무작위로 섞어 부여 (최대 5)\n\n흐트러진 아군 스튜던트가 있으면, <color=#ff6000><mark=#ff000040><b><u>턴 종료 시 대상의 흐트러짐을 해제</u></b></mark></color>\n- 이 효과로 흐트러짐이 해제된 스튜던트는 다음 턴에 한하여 모든 공격 내성과 속성 내성이 취약으로 변경됨\n\n패닉 상태인 스튜던트가 있으면, 턴 종료 시 대상의 정신력을 45까지 회복
   źródło: Passives_Abnormality-twth.json :: dataList[id=142202].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: Randomly apply [AttackUp] and [DefenseUp] to allied Fauvist Students of the Ring equal to the number of turns (including the current turn) each unit has survived, respectively (max 5)\n\nTurn End: If an allied Student is Staggered, <color=#ff6000><mark=#ff000040><b><u>recover them from Stagger</u></b></mark></color>\n- All Attack Type and Affinity Resistance for the Students who recovered from Stagger due to this effect becomes "Fatal" for the next turn\n\nTurn End: If a Student is in Panic, heal their SP up to 45
   PL:
151. [[twth] Pasywka wroga [142203] — nazwa] 야수파 - 야성적인 색채
   źródło: Passives_Abnormality-twth.json :: dataList[id=142203].name
   limit: do 50 znaków
   EN: Le Fauvisme - Couleurs Sauvages
   PL:
152. [[twth] Pasywka wroga [142203] — opis] 전투 종료 시 [BearClawWound], [EagleClawWound], [BoldBrushstrokes]를\n전부 보유한 수감자에게 <color=#ff6000><mark=#ff000040><b><u>다음 턴에 [IntenseColors] 1 부여</u></b></mark></color>\n- 대상이 보유한 [BearClawWound], [EagleClawWound]가\n각각 3/6/9 이상이면, 대신 2/3/4 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=142203].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BearClawWound], [EagleClawWound], [BoldBrushstrokes], [IntenseColors]
   znaczenie tagów: [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]; [BoldBrushstrokes] = 과감한 터치 / Touche Hardie; [IntenseColors] = 강렬한 색채 / Palette Vibrante
   EN: Combat End: <color=#ff6000><mark=#ff000040><b><u>Inflict 1 [IntenseColors] next turn</u></b></mark></color> to Sinners that have [BearClawWound], [EagleClawWound], and [BoldBrushstrokes] simultaneously\n- If target has 3+/6+/9+ [BearClawWound] and [EagleClawWound] each, inflict 2/3/4 [IntenseColors] instead (amount inflicted is based on the effect that has the least Stack)
   PL:
153. [[twth] Pasywka wroga [142203] — podsumowanie] 강렬한 색채 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=142203].summary
   limit: do 120 znaków
   EN: Inflict Palette Vibrante
   PL:
154. [[twth] Pasywka wroga [142203] — tekst klimatyczny] ‘동물의 생김새에는 저마다의 목적이 있죠. 그중에서도 우리가 야수라 부르는 것들이 가지는 야성을 깨워내고 표출해내는 것이 바로 야수파입니다.’
   źródło: Passives_Abnormality-twth.json :: dataList[id=142203].flavor
   limit: do 240 znaków
   EN: 'Intrinsic in the outward appearance of each animal is a distinct purpose. And we les Fauves are the ones who awaken and express the ferity of those that we call wild beasts among them.'
   PL:
155. [[twth] Pasywka wroga [142204] — nazwa] 인생이 담긴 야수탈
   źródło: Passives_Abnormality-twth.json :: dataList[id=142204].name
   limit: do 50 znaków
   EN: Casque de Fauve - Empreinte Vitale
   PL:
156. [[twth] Pasywka wroga [142204] — opis] [PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 20으로 변경됨\n\n<color=#ff6000><mark=#ff000040><b><u>체력이 70% 이하면, 페이즈 변경</u></b></mark></color>\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- 해당 턴 시작 시, [FaubismWolfMask] 얻고 정신력 45까지 회복
   źródło: Passives_Abnormality-twth.json :: dataList[id=142204].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PanicChangeLock], [FaubismWolfMask]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [FaubismWolfMask] = 야수파 - 마스크 드 루 / Le Fauvisme - Masque de Loup
   EN: Gain the effects of [PanicChangeLock]\nTurn End: If this unit is in Panic, reset SP to 20\n\n<color=#ff6000><mark=#ff000040><b><u>At 70%- HP, gain a new pattern</u></b></mark></color>\n- Remove all effects other than those exclusive to this unit\n- First Turn Start of the new pattern: Gain [FaubismWolfMask] and heal up to 45 SP
   PL:
157. [[twth] Pasywka wroga [142301] — nazwa] 약지 야수파 도슨트 루포
   źródło: Passives_Abnormality-twth.json :: dataList[id=142301].name
   limit: do 70 znaków
   EN: Rufo, a Docent of The Ring's School of Fauvism
   PL:
158. [[twth] Pasywka wroga [142301] — opis] 강력한 공격을 사용하는 턴의 속도 최솟값, 최댓값 +15\n\n일방 공격으로 받는 피해량 -30%\n일방 공격으로 가하는 피해량 +30%\n- 해당 슬롯의 [Aggro]가 2 이상이면, 수치 1당 이 효과로 증가하는 피해량이 5%씩 감소 (최소 0%)\n\n합 패배 시, [AttackDmgUp] 1 얻음 (턴당 최대 5)\n- 턴 종료 시 또는 스킬을 사용하여 수감자에게 공격 적중 시, 해당 스킬의 공격 종료 시점에 이 효과로 얻은 [AttackDmgUp]가 소멸됨
   źródło: Passives_Abnormality-twth.json :: dataList[id=142301].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [Aggro], [AttackDmgUp]
   znaczenie tagów: [Aggro] = 도발치 / Aggro; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: In the turn this unit uses a powerful attack, Min & Max Speed +15\n\nTake -30% damage from Unopposed Attacks\nDeal +30% damage with Unopposed Attacks\n- If the Slot targeted by this unit's Unopposed Attack has 2+ [Aggro], reduce the increased damage from this effect by 5% per [Aggro] Stack (min 0%)\n\nOn Clash Lose, gain 1 [AttackDmgUp] (5 per turn)\n- At Turn End, or at Attack End of a Skill that hit a Sinner, the [AttackDmgUp] effect gained with this effect expires
   PL:
159. [[twth] Pasywka wroga [142301] — podsumowanie] 일방 공격으로 받는 피해량 감소, 일방 공격으로 가하는 피해량 증가\n합 패배 시, 피해량 증가 얻음
   źródło: Passives_Abnormality-twth.json :: dataList[id=142301].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take less damage and deal more damage with Unopposed Attacks\nOn Clash Lose, gain Damage Up
   PL:
160. [[twth] Pasywka wroga [142302] — nazwa] 야수파 - 마스크 드 루 : 일깨워지는 야성
   źródło: Passives_Abnormality-twth.json :: dataList[id=142302].name
   limit: do 80 znaków
   EN: Le Fauvisme - Masque de Loup : Résurgence de la Sauvagerie
   PL:
161. [[twth] Pasywka wroga [142302] — opis] 턴 시작 시, <color=#ff6000><mark=#ff000040><b><u>[Protection] 8 얻음</u></b></mark></color>\n- 보유한 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 수만큼</u></b></mark></color> 턴 시작 시 획득하는 수치가 2 감소\n- ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’ <color=#ff6000><mark=#ff000040><b><u>합 패배 시,</u></b></mark></color> 이 효과가 다음 턴에 한하여 <color=#ff6000><mark=#ff000040><b><u>[Vulnerable] 2 얻는 효과</u></b></mark></color>로 변경됨\n\n스킬 코인으로 <color=#ff6000><mark=#ff000040><b><u>피격받을 때마다 방어 레벨이 1씩 증가</u></b></mark></color> (턴당 최대 20)\n- 턴 종료 시, 이 효과로 얻은 방어 레벨이 소멸됨\n- ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’ <color=#ff6000><mark=#ff000040><b><u>합 패배 시,</u></b></mark></color> 이 효과가 다음 턴에 한하여 스킬 코인으로 피격받을 때마다 <color=#ff6000><mark=#ff000040><b><u>방어 레벨이 1씩 감소</u></b></mark></color>하는 효과로 변경됨 (최대 20, 해당 턴 종료 시 효과 소멸됨)
   źródło: Passives_Abnormality-twth.json :: dataList[id=142302].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Protection], [Vulnerable]
   znaczenie tagów: [Protection] = 보호 / Protection; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Gain 8 [Protection]</u></b></mark></color>\n- Gain 2 fewer [Protection] at Turn Start <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect on this unit</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>On Clash Lose using "Burst Forth the Pulsing Crimson under Your Skin" Skill, gain 2 [Vulnerable] from this effect instead</u></b></mark></color> for the next turn\n\n<color=#ff6000><mark=#ff000040><b><u>Gain 1 Defense Level each time this unit is hit</u></b></mark></color> by a Skill Coin (max 20 per turn)\n- Turn End: Defense Level gained due to this effect expires\n- <color=#ff6000><mark=#ff000040><b><u>On Clash Lose using "Burst Forth the Pulsing Crimson under Your Skin" Skill, lose 1 Defense Level each time this unit is hit by a Skill Coin instead</u></b></mark></color> for the next turn (max 20; expires at Turn End)
   PL:
162. [[twth] Pasywka wroga [142302] — podsumowanie] 피격 시, 방어 레벨이 증가\n이전 턴에 특정 스킬 합 패배 시, 대신 방어 레벨이 감소
   źródło: Passives_Abnormality-twth.json :: dataList[id=142302].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit, gain Defense Level\nIf this unit lost a Clash using a certain Skill, lose Defense Level instead
   PL:
163. [[twth] Pasywka wroga [142303] — nazwa] 야수파 - 야성적인 색채
   źródło: Passives_Abnormality-twth.json :: dataList[id=142303].name
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [[twth] Pasywka wroga [142303] — opis] 전투 종료 시 [BearClawWound], [EagleClawWound], [BoldBrushstrokes]를\n전부 보유한 수감자에게 <color=#ff6000><mark=#ff000040><b><u>다음 턴에 [IntenseColors] 1 부여</u></b></mark></color>\n- 대상이 보유한 [BearClawWound], [EagleClawWound]가\n각각 3/6/9 이상이면, 대신 2/3/4 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=142303].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [[twth] Pasywka wroga [142303] — podsumowanie] 강렬한 색채 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=142303].summary
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [[twth] Pasywka wroga [142303] — tekst klimatyczny] ‘동물의 생김새에는 저마다의 목적이 있죠. 그중에서도 우리가 야수라 부르는 것들이 가지는 야성을 깨워내고 표출해내는 것이 바로 야수파입니다.’
   źródło: Passives_Abnormality-twth.json :: dataList[id=142303].flavor
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [[twth] Pasywka wroga [142304] — nazwa] 야수파 - 물감 주입 극한치
   źródło: Passives_Abnormality-twth.json :: dataList[id=142304].name
   limit: do 60 znaków
   EN: Le Fauvisme - Maximum Paint Tolerance Dose
   PL:
168. [[twth] Pasywka wroga [142304] — opis] [PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 30으로 변경됨\n\n<color=#ff6000><mark=#ff000040><b><u>체력이 35% 이하</u></b></mark></color>면, <color=#ff6000><mark=#ff000040><b><u>[FaubismWolfMask]가\n[FaubismWolfMaskBlooded]로 변경되고 정신력 45까지 회복</u></b></mark></color>
   źródło: Passives_Abnormality-twth.json :: dataList[id=142304].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PanicChangeLock], [FaubismWolfMask], [FaubismWolfMaskBlooded]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [FaubismWolfMask] = 야수파 - 마스크 드 루 / Le Fauvisme - Masque de Loup; [FaubismWolfMaskBlooded] = 야수파 - 마스크 드 루 앙상글랑테 / Le Fauvisme - Masque de Loup Ensanglanté
   EN: Gain the effects of [PanicChangeLock]\nTurn End: If this unit is in Panic, reset SP to 30\n\n<color=#ff6000><mark=#ff000040><b><u>At 35%- HP, convert [FaubismWolfMask] into [FaubismWolfMaskBlooded], and heal up to 45 SP</u></b></mark></color>
   PL:
169. [[twth] Pasywka wroga [142401] — nazwa] 예술의 흔적
   źródło: Passives_Abnormality-twth.json :: dataList[id=142401].name
   limit: do 40 znaków
   EN: Remnant of Art
   PL:
170. [[twth] Pasywka wroga [142401] — opis] 사망 시, 가장 적은 수량의 E.G.O 자원 +2
   źródło: Passives_Abnormality-twth.json :: dataList[id=142401].desc
   limit: do 120 znaków
   EN: On death, give +2 E.G.O resource of the least-owned Affinity
   PL:
171. [[twth] Pasywka wroga [142401] — podsumowanie] 사망 시, E.G.O 자원 획득
   źródło: Passives_Abnormality-twth.json :: dataList[id=142401].summary
   limit: do 120 znaków
   EN: Give E.G.O resource on death
   PL:
172. [[twth] Pasywka wroga [500601] — nazwa] 사영전투
   źródło: Passives_Abnormality-twth.json :: dataList[id=500601].name
   limit: do 40 znaków
   EN: Reflectrial
   PL:
173. [[twth] Pasywka wroga [500601] — opis] 동일한 대상과의 합 횟수가 10 이상이 되면, 합 위력이 현재 (합 횟수/10)만큼 무작위로 증가 또는 감소 (소수점 버림)\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]의 위력이 최대 30까지 누적되고 횟수는 최대 10까지 누적됨
   źródło: Passives_Abnormality-twth.json :: dataList[id=500601].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: At 10+ Clashes against the same enemy, randomly gain or lose Clash Power by (Clash Count/10) in a Clash (rounded down)\n\nMax Potency cap for [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]: 30\nMax Count cap for [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]: 10
   PL:
174. [[twth] Pasywka wroga [500602] — nazwa] 약지 야수파 도슨트
   źródło: Passives_Abnormality-twth.json :: dataList[id=500602].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [[twth] Pasywka wroga [500602] — opis] 턴 시작 시 아군 약지 야수파 스튜던트 1명당 <color=#ff6000><mark=#ff000040><b><u>[Protection] 2 얻음</u></b></mark></color>\n- 이번 전투에서 ‘크리틱’을 사용하였다면 이후 턴부터는 효과가 강화되어, 대신 [Protection] 2 얻고 정신력 5 회복\n(정신력이 -15 미만이면, 정신력 회복 효과가 2배로 적용)\n- 아군 약지 야수파 스튜던트가 없으면, 대신 [Vulnerable] 2 얻고 정신력 0까지 감소\n\n공격 가중치가 1인 스킬로 피격받기 직전에 다른 아군 스튜던트가 있으면,\n대상에게 <color=#ff6000><mark=#ff000040><b><u>[Protection] 2를 부여하고 대상이 공격을 대신 받도록 함 (턴당 2회)</u></b></mark></color>\n\n‘크리틱’을 사용한 턴 종료 시 이번 전투에서 사망한 아군 약지 야수파 스튜던트가 있으면, 그 자리를 <color=#ff6000><mark=#ff000040><b><u>동일한 스튜던트를 불러와 다시 채움</u></b></mark></color>\n- 이 효과로 등장한 스튜던트는 매턴 시작 시, 이번 전투 동안 사망한 아군 수만큼 [Vulnerable], [AttackDown] 얻음 (각각 최대 10)
   źródło: Passives_Abnormality-twth.json :: dataList[id=500602].desc
   limit: do 1150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Protection], [Vulnerable], [AttackDown]
   znaczenie tagów: [Protection] = 보호 / Protection; [Vulnerable] = 취약 / Fragile; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Gain 2 [Protection]</u></b></mark></color> for every allied Fauvist Student of the Ring\n- If this unit used "Critique" in this Encounter, gain 2 [Protection] and heal 5 SP instead starting from the next turn\n(At lower than -15 SP, double the SP-healing effect)\n- If there are no allied Fauvist Students of the Ring, gain 2 [Vulnerable] and reduce this unit's SP down to 0 instead\n\nImmediately Before Getting Hit by a Skill that has 1 Atk Weight, if there is an allied Student of the Ring, <color=#ff6000><mark=#ff000040><b><u>apply 2 [Protection] on that unit; then, have the said unit take the attack instead (2 times per turn)</u></b></mark></color>\n\nTurn End of the turn this unit used "Critique": If an allied Fauvist Student of the Ring was defeated in this Encounter, <color=#ff6000><mark=#ff000040><b><u>refill its vacancy with the same Student unit</u></b></mark></color>\n- Every Turn Start: The Student that refilled the vacancy due to this effect gains (# of allies defeated in this Encounter) [Vulnerable] and [AttackDown] (max 10 each)
   PL:
176. [[twth] Pasywka wroga [500602] — podsumowanie] 피격받기 직전, 다른 아군 스튜던트가 공격 대신 받게 함
   źródło: Passives_Abnormality-twth.json :: dataList[id=500602].summary
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [[twth] Pasywka wroga [500603] — nazwa] 지도 편달
   źródło: Passives_Abnormality-twth.json :: dataList[id=500603].name
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [[twth] Pasywka wroga [500603] — opis] 턴 시작 시 아군 약지 야수파 스튜던트에게\n각 대상이 생존한 턴 수(현재 턴 포함)만큼\n[AttackUp], [DefenseUp]를 무작위로 섞어 부여 (최대 5)\n\n흐트러진 아군 스튜던트가 있으면, <color=#ff6000><mark=#ff000040><b><u>턴 종료 시 대상의 흐트러짐을 해제</u></b></mark></color>\n- 이 효과로 흐트러짐이 해제된 스튜던트는 다음 턴에 한하여 모든 공격 내성과 속성 내성이 취약으로 변경됨\n\n패닉 상태인 스튜던트가 있으면, 턴 종료 시 대상의 정신력을 45까지 회복
   źródło: Passives_Abnormality-twth.json :: dataList[id=500603].desc
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [[twth] Pasywka wroga [500604] — nazwa] 야수파 - 야성적인 색채
   źródło: Passives_Abnormality-twth.json :: dataList[id=500604].name
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [[twth] Pasywka wroga [500604] — opis] 전투 종료 시 [BearClawWound], [EagleClawWound], [BoldBrushstrokes]를\n전부 보유한 수감자에게 <color=#ff6000><mark=#ff000040><b><u>다음 턴에 [IntenseColors] 1 부여</u></b></mark></color>\n- 대상이 보유한 [BearClawWound], [EagleClawWound]가\n각각 3/6/9 이상이면, 대신 2/3/4 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=500604].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [[twth] Pasywka wroga [500604] — podsumowanie] 강렬한 색채 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=500604].summary
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [[twth] Pasywka wroga [500604] — tekst klimatyczny] ‘동물의 생김새에는 저마다의 목적이 있죠. 그중에서도 우리가 야수라 부르는 것들이 가지는 야성을 깨워내고 표출해내는 것이 바로 야수파입니다.’
   źródło: Passives_Abnormality-twth.json :: dataList[id=500604].flavor
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [[twth] Pasywka wroga [500605] — nazwa] 인생이 담긴 야수탈
   źródło: Passives_Abnormality-twth.json :: dataList[id=500605].name
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [[twth] Pasywka wroga [500605] — opis] [PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 45로 변경됨\n\n<color=#ff6000><mark=#ff000040><b><u>체력이 70% 이하면, 페이즈 변경</u></b></mark></color>\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- 전장에 있는 모든 수감자에게 <color=#ff6000><mark=#ff000040><b><u>[Laceration] 8, [Laceration] 횟수 8, [Sinking] 8, [Sinking] 횟수 8</u></b></mark></color> 부여\n- 해당 턴 시작 시, [FaubismWolfMask] 얻고 정신력 45까지 회복
   źródło: Passives_Abnormality-twth.json :: dataList[id=500605].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PanicChangeLock], [Laceration], [Sinking], [FaubismWolfMask]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [FaubismWolfMask] = 야수파 - 마스크 드 루 / Le Fauvisme - Masque de Loup
   EN: Gain the effects of [PanicChangeLock]\nTurn End: If this unit is in Panic, reset SP to 45\n\n<color=#ff6000><mark=#ff000040><b><u>At 70%- HP, gain a new pattern</u></b></mark></color>\n- Remove all effects other than those exclusive to this unit\n- Inflict <color=#ff6000><mark=#ff000040><b><u>8 [Laceration], +8 [Laceration] Count, 8 [Sinking], and +8 [Sinking] Count</u></b></mark></color> on all Sinners on the field\n- First Turn Start of the new pattern: Gain [FaubismWolfMask] and heal up to 45 SP
   PL:
185. [[twth] Pasywka wroga [500701] — nazwa] 사영전투
   źródło: Passives_Abnormality-twth.json :: dataList[id=500701].name
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [[twth] Pasywka wroga [500701] — opis] 동일한 대상과의 합 횟수가 10 이상이 되면, 합 위력이 현재 (합 횟수/10)만큼 무작위로 증가 또는 감소 (소수점 버림)\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]의 위력이 최대 30까지 누적되고 횟수는 최대 10까지 누적됨
   źródło: Passives_Abnormality-twth.json :: dataList[id=500701].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [[twth] Pasywka wroga [500702] — nazwa] 약지 야수파 도슨트 루포
   źródło: Passives_Abnormality-twth.json :: dataList[id=500702].name
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [[twth] Pasywka wroga [500702] — opis] 강력한 공격을 사용하는 턴의 속도 최솟값, 최댓값 +15\n\n일방 공격으로 받는 피해량 -50%\n일방 공격으로 가하는 피해량 +50%\n- 해당 슬롯의 [Aggro]가 2 이상이면, 수치 1당 이 효과로 증가하는 피해량이 5%씩 감소 (최소 0%)\n\n합 패배 시, [AttackDmgUp] 1 얻음 (턴당 최대 5)\n- 턴 종료 시 또는 스킬을 사용하여 수감자에게 공격 적중 시, 해당 스킬의 공격 종료 시점에 이 효과로 얻은 [AttackDmgUp]가 소멸됨
   źródło: Passives_Abnormality-twth.json :: dataList[id=500702].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [Aggro], [AttackDmgUp]
   znaczenie tagów: [Aggro] = 도발치 / Aggro; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: In the turn this unit uses a powerful attack, Min & Max Speed +15\n\nTake -50% damage from Unopposed Attacks\nDeal +50% damage with Unopposed Attacks\n- If the Slot targeted by this unit's Unopposed Attack has 2+ [Aggro], reduce the increased damage from this effect by 5% per [Aggro] Stack (min 0%)\n\nOn Clash Lose, gain 1 [AttackDmgUp] (5 per turn)\n- At Turn End, or at Attack End of a Skill that hit a Sinner, the [AttackDmgUp] effect gained with this effect expires
   PL:
189. [[twth] Pasywka wroga [500702] — podsumowanie] 일방 공격으로 받는 피해량 감소, 일방 공격으로 가하는 피해량 증가\n합 패배 시, 피해량 증가 얻음
   źródło: Passives_Abnormality-twth.json :: dataList[id=500702].summary
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [[twth] Pasywka wroga [500703] — nazwa] 야수파 - 마스크 드 루 : 일깨워지는 야성
   źródło: Passives_Abnormality-twth.json :: dataList[id=500703].name
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [[twth] Pasywka wroga [500703] — opis] 턴 시작 시, <color=#ff6000><mark=#ff000040><b><u>[Protection] 10 얻음</u></b></mark></color>\n- 보유한 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 수만큼</u></b></mark></color> 턴 시작 시 획득하는 수치가 1 감소\n- ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’ <color=#ff6000><mark=#ff000040><b><u>합 패배 시,</u></b></mark></color> 이 효과가 다음 턴에 한하여 <color=#ff6000><mark=#ff000040><b><u>[Vulnerable] 2 얻는 효과</u></b></mark></color>로 변경됨\n\n스킬 코인으로 <color=#ff6000><mark=#ff000040><b><u>피격받을 때마다 방어 레벨이 1씩 증가</u></b></mark></color> (턴당 최대 20)\n- 턴 종료 시, 이 효과로 얻은 방어 레벨이 소멸됨\n- ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’ <color=#ff6000><mark=#ff000040><b><u>합 패배 시,</u></b></mark></color> 이 효과가 다음 턴에 한하여 스킬 코인으로 피격받을 때마다 <color=#ff6000><mark=#ff000040><b><u>방어 레벨이 1씩 감소</u></b></mark></color>하는 효과로 변경됨 (최대 20, 해당 턴 종료 시 효과 소멸됨)
   źródło: Passives_Abnormality-twth.json :: dataList[id=500703].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Protection], [Vulnerable]
   znaczenie tagów: [Protection] = 보호 / Protection; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Gain 10 [Protection]</u></b></mark></color>\n- Gain 1 fewer [Protection] at Turn Start <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect on this unit</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>On Clash Lose using "Burst Forth the Pulsing Crimson under Your Skin" Skill, gain 2 [Vulnerable] from this effect instead</u></b></mark></color> for the next turn\n\n<color=#ff6000><mark=#ff000040><b><u>Gain 1 Defense Level each time this unit is hit</u></b></mark></color> by a Skill Coin (max 20 per turn)\n- Turn End: Defense Level gained due to this effect expires\n- <color=#ff6000><mark=#ff000040><b><u>On Clash Lose using "Burst Forth the Pulsing Crimson under Your Skin" Skill, lose 1 Defense Level each time this unit is hit by a Skill Coin instead</u></b></mark></color> for the next turn (max 20; expires at Turn End)
   PL:
192. [[twth] Pasywka wroga [500703] — podsumowanie] 피격 시, 방어 레벨이 증가\n이전 턴에 특정 스킬 합 패배 시, 대신 방어 레벨이 감소
   źródło: Passives_Abnormality-twth.json :: dataList[id=500703].summary
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [[twth] Pasywka wroga [500704] — nazwa] 야수파 - 야성적인 색채
   źródło: Passives_Abnormality-twth.json :: dataList[id=500704].name
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [[twth] Pasywka wroga [500704] — opis] 전투 종료 시 [BearClawWound], [EagleClawWound], [BoldBrushstrokes]를\n전부 보유한 수감자에게 <color=#ff6000><mark=#ff000040><b><u>다음 턴에 [IntenseColors] 1 부여</u></b></mark></color>\n- 대상이 보유한 [BearClawWound], [EagleClawWound]가\n각각 3/6/9 이상이면, 대신 2/3/4 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=500704].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [[twth] Pasywka wroga [500704] — podsumowanie] 강렬한 색채 부여
   źródło: Passives_Abnormality-twth.json :: dataList[id=500704].summary
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [[twth] Pasywka wroga [500704] — tekst klimatyczny] ‘동물의 생김새에는 저마다의 목적이 있죠. 그중에서도 우리가 야수라 부르는 것들이 가지는 야성을 깨워내고 표출해내는 것이 바로 야수파입니다.’
   źródło: Passives_Abnormality-twth.json :: dataList[id=500704].flavor
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [[twth] Pasywka wroga [500705] — nazwa] 야수파 - 물감 주입 극한치
   źródło: Passives_Abnormality-twth.json :: dataList[id=500705].name
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [[twth] Pasywka wroga [500705] — opis] [PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 45로 변경됨\n\n<color=#ff6000><mark=#ff000040><b><u>체력이 35% 이하</u></b></mark></color>면, <color=#ff6000><mark=#ff000040><b><u>[FaubismWolfMask]가\n[FaubismWolfMaskBlooded]로 변경되고 정신력 45까지 회복</u></b></mark></color>
   źródło: Passives_Abnormality-twth.json :: dataList[id=500705].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PanicChangeLock], [FaubismWolfMask], [FaubismWolfMaskBlooded]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [FaubismWolfMask] = 야수파 - 마스크 드 루 / Le Fauvisme - Masque de Loup; [FaubismWolfMaskBlooded] = 야수파 - 마스크 드 루 앙상글랑테 / Le Fauvisme - Masque de Loup Ensanglanté
   EN: Gain the effects of [PanicChangeLock]\nTurn End: If this unit is in Panic, reset SP to 45\n\n<color=#ff6000><mark=#ff000040><b><u>At 35%- HP, convert [FaubismWolfMask] into [FaubismWolfMaskBlooded], and heal up to 45 SP</u></b></mark></color>
   PL:

## [twth] Pasywka wroga: Passives_Enemy-twth
- plik gry: `Passives_Enemy-twth.json`

199. [[twth] Pasywka wroga [9104301] — nazwa] 강렬한 원색 - 루주
   źródło: Passives_Enemy-twth.json :: dataList[id=9104301].name
   limit: do 50 znaków
   EN: Intense Primary Color - Rouge
   PL:
200. [[twth] Pasywka wroga [9104301] — opis] 공격 적중 전 대상에게 [Laceration]이 없었으면, 대상의 [Laceration] 횟수 3 증가 (적 별로 턴당 1회)
   źródło: Passives_Enemy-twth.json :: dataList[id=9104301].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Before hitting, if target does not have [Laceration], inflict +3 [Laceration] Count (once per turn per enemy)
   PL:
201. [[twth] Pasywka wroga [9104302] — nazwa] 야수파 - 마스크 드 시앵
   źródło: Passives_Enemy-twth.json :: dataList[id=9104302].name
   limit: do 50 znaków
   EN: Le Fauvisme - Masque de Chien
   PL:
202. [[twth] Pasywka wroga [9104302] — opis] 적에게 스킬 적중 시 대상에게 [BearClawWound] 1 부여\n\n[BearClawWound]를 4 부여 할 때마다, 다음 턴에 [Enhancement] 1 얻음 (턴당 2회)
   źródło: Passives_Enemy-twth.json :: dataList[id=9104302].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [BearClawWound], [Enhancement]
   znaczenie tagów: [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: On Hit with a Skill, inflict 1 [BearClawWound]\n\nGain 1 [Enhancement] next turn for every 4 [BearClawWound] inflicted (2 times per turn)
   PL:
203. [[twth] Pasywka wroga [9104302] — tekst klimatyczny] “시작은 하나의 동물로.”\n“점차 예술과 야성을 탐구해 갈수록, 그 위에 다른 짐승을 더해가죠.”
   źródło: Passives_Enemy-twth.json :: dataList[id=9104302].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "The first step is always but a single animal."\n\n"And with every quest for art and ferity, another beast is layered atop the previous specimen.'"
   PL:
204. [[twth] Pasywka wroga [9104303] — nazwa] 차오르는 영감
   źródło: Passives_Enemy-twth.json :: dataList[id=9104303].name
   limit: do 40 znaków
   EN: Welling Inspiration
   PL:
205. [[twth] Pasywka wroga [9104303] — opis] 자신 혹은 아군이 피격 시 다음 턴에 [AttackUp] 1 얻음 (스킬당 1회, 턴당 최대 3)
   źródło: Passives_Enemy-twth.json :: dataList[id=9104303].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: When this unit or an ally is hit, gain 1 [AttackUp] next turn (once per Skill, 3 times per turn)
   PL:
206. [[twth] Pasywka wroga [9104304] — nazwa] 마지막 붓질
   źródło: Passives_Enemy-twth.json :: dataList[id=9104304].name
   limit: do 40 znaków
   EN: Final Brushstroke
   PL:
207. [[twth] Pasywka wroga [9104304] — opis] 사망 시, 무작위 적 2명에게 [BearClawWound] 3 부여
   źródło: Passives_Enemy-twth.json :: dataList[id=9104304].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BearClawWound]
   znaczenie tagów: [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: When this unit is killed, inflict 3 [BearClawWound] on 2 random enemies
   PL:
208. [[twth] Pasywka wroga [9104501] — nazwa] 강렬한 원색 - 블뢰
   źródło: Passives_Enemy-twth.json :: dataList[id=9104501].name
   limit: do 40 znaków
   EN: Intense Primary Color - Bleu
   PL:
209. [[twth] Pasywka wroga [9104501] — opis] 공격 적중 전 대상에게 [Sinking]이 없었으면, 대상의 [Sinking] 횟수 3 증가 (적 별로 턴당 1회)
   źródło: Passives_Enemy-twth.json :: dataList[id=9104501].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Before hitting, if target does not have [Sinking], inflict +3 [Sinking] Count (once per turn per enemy)
   PL:
210. [[twth] Pasywka wroga [9104502] — nazwa] 야수파 - 마스크 드 셰브르-이부
   źródło: Passives_Enemy-twth.json :: dataList[id=9104502].name
   limit: do 50 znaków
   EN: Le Fauvisme - Masque de Chèvre-Hibou
   PL:
211. [[twth] Pasywka wroga [9104502] — opis] 적에게 스킬 적중 시 대상에게 [EagleClawWound] 1 부여\n- 자신에게 [Agility]이 있으면 [EagleClawWound] 부여량 +1\n\n[EagleClawWound]를 4 부여 할 때마다, 다음 턴에 [Agility] 1 얻음 (턴당 2회)
   źródło: Passives_Enemy-twth.json :: dataList[id=9104502].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [EagleClawWound], [Agility]
   znaczenie tagów: [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]; [Agility] = 신속 / Haste
   EN: On Hit with a Skill, inflict 1 [EagleClawWound]\n- If this unit has [Agility], inflict 1 additional [EagleClawWound]\n\nGain 1 [Agility] next turn for every 4 [EagleClawWound] inflicted (2 times per turn)
   PL:
212. [[twth] Pasywka wroga [9104502] — tekst klimatyczny] “자신만의 고유한 정체성을 드러내는 하나의 야수. 저희는 그 야수를 예술의 기본으로 삼고 자부심을 품습니다. 그러니 야수파 안에서 특정 짐승이 유행한다고 해서, 자신의 정체성이 되는 야수를 바꾸진 않죠.”\n”하지만 간혹 그 정체성을 휙휙 바꿔가며 줏대 없이 야수를 갈아타는 놈들도 있다던데… 흠.”
   źródło: Passives_Enemy-twth.json :: dataList[id=9104502].flavor
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "There are beasts that fall in and out of vogue within the School of Fauvism, yes—but a true artist must take fierce pride in that single animal as the underdrawing which best represents their unique self."\n\n"Despite this wisdom, however, there are some who flit from beast to beast, as though the self is nothing more than a costume to be worn and discarded... Hm"
   PL:
213. [[twth] Pasywka wroga [9104503] — nazwa] 재빠른 표현
   źródło: Passives_Enemy-twth.json :: dataList[id=9104503].name
   limit: do 40 znaków
   EN: Alacritous Expression
   PL:
214. [[twth] Pasywka wroga [9104503] — opis] 대상보다 속도가 빠르면, 합 위력 +1
   źródło: Passives_Enemy-twth.json :: dataList[id=9104503].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's, Clash Power +1
   PL:
215. [[twth] Pasywka wroga [9104504] — nazwa] 마지막 붓질
   źródło: Passives_Enemy-twth.json :: dataList[id=9104504].name
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [[twth] Pasywka wroga [9104504] — opis] 사망 시, 무작위 적 2명에게 [EagleClawWound] 3 부여
   źródło: Passives_Enemy-twth.json :: dataList[id=9104504].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EagleClawWound]
   znaczenie tagów: [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: When this unit is killed, inflict 3 [EagleClawWound] on 2 random enemies
   PL:
217. [[twth] Pasywka wroga [9103401] — nazwa] 쪽지로 전해진 지령
   źródło: Passives_Enemy-twth.json :: dataList[id=9103401].name
   limit: do 50 znaków
   EN: Prescript Delivered on Paper Slips
   PL:
218. [[twth] Pasywka wroga [9103401] — opis] 턴 시작 시\n- 자신의 [BlessingOfIndexPrescriptEnemy] 수치에 따라 [IndexPrescriptEnemy_0]/[IndexPrescriptEnemy_1]/[IndexPrescriptEnemy_2]/[IndexPrescriptEnemy_3] 얻음 \n- 무작위 수감자 1명에게 [IndexPrescriptTargetToPersonality] 부여\n(집중 전투일 경우, 우선 공격함)
   źródło: Passives_Enemy-twth.json :: dataList[id=9103401].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [IndexPrescriptEnemy_0], [IndexPrescriptEnemy_1], [IndexPrescriptEnemy_2], [IndexPrescriptEnemy_3], [IndexPrescriptTargetToPersonality]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptEnemy_0] = 지령[쪽지] I / Prescript: [Paper Slip] I; [IndexPrescriptEnemy_1] = 지령[쪽지] II / Prescript: [Paper Slip] II; [IndexPrescriptEnemy_2] = 지령[쪽지] III / Prescript: [Paper Slip] III; [IndexPrescriptEnemy_3] = 지령[쪽지] IV / Prescript: [Paper Slip] IV; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index
   EN: Turn Start:\n- Gain [IndexPrescriptEnemy_0]/[IndexPrescriptEnemy_1]/[IndexPrescriptEnemy_2]/[IndexPrescriptEnemy_3] based on [BlessingOfIndexPrescriptEnemy] Stack on self\n- Inflict [IndexPrescriptTargetToPersonality] to a random Sinner (in Focused Encounters, attacks prioritize the Sinner that has [IndexPrescriptTargetToPersonality])
   PL:
219. [[twth] Pasywka wroga [9103401] — tekst klimatyczny] “지령이 여러 방식으로 전달된다는 것을 아시는 분도 있을 겁니다.  그중에서 쪽지로 전달받는 지령이 가장 일반적이며, 이를 선호하는 사람들이 많습니다.”
   źródło: Passives_Enemy-twth.json :: dataList[id=9103401].flavor
   limit: do 220 znaków
   EN: "Some of you may already be aware that the Prescripts are delivered through various means. Of these, the Paper Slip is the most commonplace—and the most preferred by many."
   PL:
220. [[twth] Pasywka wroga [9103402] — nazwa] 지령의 뜻
   źródło: Passives_Enemy-twth.json :: dataList[id=9103402].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL:
221. [[twth] Pasywka wroga [9103402] — opis] 이번 턴에 [IndexPrescript_Base]을 수행했으면,\n턴 종료 시 정신력 5 회복, [BlessingOfIndexPrescriptEnemy] 2 얻음 (턴당 1회)\n- [IndexPrescriptEnemy_2]을 보유 중이거나 [IndexPrescript_Base] 수행 시 타겟에게\n[IndexPrescriptTargetToPersonality]이 있으면, 대신 정신력 10 회복, [BlessingOfIndexPrescriptEnemy] 3 얻음\n\n이번 턴에 [IndexPrescript_Base]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexEnemy] 10 얻음\n- [BlessingOfIndexPrescriptEnemy] 6 미만이면, 턴 종료 시 [BlessingOfIndexPrescriptEnemy] 1 얻음 \n- [BlessingOfIndexPrescriptEnemy] 9면, [KarmaOfIndexEnemy]를 얻지 않음
   źródło: Passives_Enemy-twth.json :: dataList[id=9103402].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescript_Base], [BlessingOfIndexPrescriptEnemy], [IndexPrescriptEnemy_2], [IndexPrescriptTargetToPersonality], [KarmaOfIndexEnemy]
   znaczenie tagów: [IndexPrescript_Base] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptEnemy_2] = 지령[쪽지] III / Prescript: [Paper Slip] III; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [KarmaOfIndexEnemy] = 카르마 / Karmic Consequence
   EN: Turn End: If [IndexPrescript_Base] was executed this turn, heal 5 SP and gain 2 [BlessingOfIndexPrescriptEnemy] (once per turn)\n- If this unit has [IndexPrescriptEnemy_2], or if target has [IndexPrescriptTargetToPersonality] when this unit is executing [IndexPrescript_Base], heal 10 SP and gain 3 [BlessingOfIndexPrescriptEnemy] instead\n\nTurn End: If [IndexPrescript_Base] was not executed this turn, gain 10 [KarmaOfIndexEnemy]\n- At less than 6 [BlessingOfIndexPrescriptEnemy], gain 1 [BlessingOfIndexPrescriptEnemy]\n- At 9 [BlessingOfIndexPrescriptEnemy], does not gain [KarmaOfIndexEnemy]
   PL:
222. [[twth] Pasywka wroga [9103402] — tekst klimatyczny] “그렇다면 지령의 전달 방식… 그 종류는 몇 가지나 있을까요? 그리고 여러 형태의 지령은 하나로부터 나오는 걸까요? 아니면 전달 방식마다 다른 주체가 존재하는 걸까요?”\n“그걸 탐구하는 것이 저희 검지 연구회가 하는 일입니다. 가입하시겠어요?”
   źródło: Passives_Enemy-twth.json :: dataList[id=9103402].flavor
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Then the question we must ask is: How many forms might the Prescripts take? Do they all flow from a single origin, or are there distinct entities behind each?"\n\n"Unraveling these mysteries is the purpose of the Society for the Research of the Index. Now, would you like to join us and explore the answers together?"
   PL:
223. [[twth] Pasywka wroga [9103403] — nazwa] 수행자의 검
   źródło: Passives_Enemy-twth.json :: dataList[id=9103403].name
   limit: do 40 znaków
   EN: Proselyte's Blade
   PL:
224. [[twth] Pasywka wroga [9103403] — opis] [BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%\n\n[IndexPrescriptTargetToPersonality]을 보유한 대상에게 적중 시,\n[Breath] 1 얻고 [Sinking] 1 부여 (턴당 1회)\n- [BlessingOfIndexPrescriptEnemy] 3당, 턴당 발동 가능한 횟수 +1 (최대 2)
   źródło: Passives_Enemy-twth.json :: dataList[id=9103403].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [IndexPrescriptTargetToPersonality], [Breath], [Sinking]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking
   EN: Deal +2.5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] on self (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage against all targets instead\n\nOn Hit against [IndexPrescriptTargetToPersonality], gain 1 [Breath] and inflict 1 [Sinking] (once per turn)\n- Increases the number of times this effect can trigger per turn by 1 for every 3 [BlessingOfIndexPrescriptEnemy] (max 2)
   PL:
225. [[twth] Pasywka wroga [9103403] — tekst klimatyczny] 보잘것없어 보이는 평범한 검.\n이 검은 지령을 따라가며 수행하는 지령의 내용과 어디선가 나타나는 전령들의 도움, 그리고 대행자들의 사사를 통해 점차 개성을 가진 검으로 완성되어 간다.
   źródło: Passives_Enemy-twth.json :: dataList[id=9103403].flavor
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A modest blade, unassuming and unworthy of note.\nYet in following the Prescript—the fulfilling of its directives, the aid of Messengers that emerge from unseen places, the teachings of the Proxies—is it slowly perfected into a weapon imbued with a singular uniqueness.
   PL:

## [walpu10] Wróg / część: Enemies-walpu10
- plik gry: `Enemies-walpu10.json`

226. [[walpu10] Wróg / część [1580] — nazwa] 살바도르
   źródło: Enemies-walpu10.json :: dataList[id=1580].name
   limit: do 40 znaków
   EN: Salvador
   PL:
227. [[walpu10] Wróg / część [1580] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1580].desc
   limit: do 120 znaków
   EN: Core
   PL:
228. [[walpu10] Wróg / część [1581] — nazwa] 유나
   źródło: Enemies-walpu10.json :: dataList[id=1581].name
   limit: do 40 znaków
   EN: Yuna
   PL:
229. [[walpu10] Wróg / część [1581] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1581].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [[walpu10] Wróg / część [1582] — nazwa] 필립
   źródło: Enemies-walpu10.json :: dataList[id=1582].name
   limit: do 40 znaków
   EN: Philip
   PL:
231. [[walpu10] Wróg / część [1582] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1582].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [[walpu10] Wróg / część [1583] — nazwa] 오스카
   źródło: Enemies-walpu10.json :: dataList[id=1583].name
   limit: do 40 znaków
   EN: Oscar
   PL:
233. [[walpu10] Wróg / część [1583] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1583].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [[walpu10] Wróg / część [1584] — nazwa] 파멜리
   źródło: Enemies-walpu10.json :: dataList[id=1584].name
   limit: do 40 znaków
   EN: Pameli
   PL:
235. [[walpu10] Wróg / część [1584] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1584].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [[walpu10] Wróg / część [1585] — nazwa] 파멜라
   źródło: Enemies-walpu10.json :: dataList[id=1585].name
   limit: do 40 znaków
   EN: Pamela
   PL:
237. [[walpu10] Wróg / część [1585] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1585].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [[walpu10] Wróg / część [1586] — nazwa] 필립
   źródło: Enemies-walpu10.json :: dataList[id=1586].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [[walpu10] Wróg / część [1586] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1586].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [[walpu10] Wróg / część [1587] — nazwa] 불안정 개화 E.G.O::밀랍날개
   źródło: Enemies-walpu10.json :: dataList[id=1587].name
   limit: do 60 znaków
   EN: Volatile Effloresced E.G.O::Waxen Pinion
   PL:
241. [[walpu10] Wróg / część [1587] — opis] 본체
   źródło: Enemies-walpu10.json :: dataList[id=1587].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu10] Umiejętności wrogów / Anomalii — Skills_Abnormality-walpu10
- grupa rozdziału/trybu: `walpu10` · plik: `Skills_Abnormality-walpu10.json`

242. [Umiejętność wroga [158001] (ulepszenie 1) — nazwa] 의뢰 처리
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158001].levelList[level=1].name
   limit: do 40 znaków
   EN: Handle Request
   PL:
243. [Umiejętność wroga [158001] (ulepszenie 1) — opis] [BeforeAttack] 정신력 10 회복\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158001].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [BeforeAttack] Heal 10 SP\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
244. [Umiejętność wroga [158001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [158001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
246. [Umiejętność wroga [158001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [158001] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ResultEnhancement]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [UnBrokenCoinOnSucceedAttack] Gain 1 [ResultEnhancement] next turn
   PL:
248. [Umiejętność wroga [158002] (ulepszenie 1) — nazwa] 여명의 섬광
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158002].levelList[level=1].name
   limit: do 40 znaków
   EN: Flash of Sunup
   PL:
249. [Umiejętność wroga [158002] (ulepszenie 1) — opis] [WhenUse] 자신의 [DawnOfficeStigmaSOne]이 15 이상이면, 스킬의 2코인이 [SuperCoin]으로 1개 추가됨
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DawnOfficeStigmaSOne], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaSOne] = 새벽불 / Light of Daybreak; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] At 15+ [DawnOfficeStigmaSOne], this Skill gains an extra Coin 2 as an [SuperCoin]
   PL:
250. [Umiejętność wroga [158002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [158002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
252. [Umiejętność wroga [158002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
253. [Umiejętność wroga [158002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
254. [Umiejętność wroga [158003] (ulepszenie 1) — nazwa] 노을빛 검
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].name
   limit: do 40 znaków
   EN: Sunset Blade
   PL:
255. [Umiejętność wroga [158003] (ulepszenie 1) — opis] [WhenUse] 자신의 [DawnOfficeStigmaSOne]이 15 이상이면, 아래 효과 적용\n- 스킬의 3코인이 [SuperCoin]으로 1개 추가됨\n- 추가된 코인의 적중시 [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DawnOfficeStigmaSOne], [SuperCoin], [VibrationExplosion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaSOne] = 새벽불 / Light of Daybreak; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [WhenUse] At 15+ [DawnOfficeStigmaSOne], apply the following effects:\n- Gains an extra Coin 3 as an [SuperCoin]\n- On Hit using the extra Coin, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
256. [Umiejętność wroga [158003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL:
257. [Umiejętność wroga [158003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [158003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [158003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność wroga [158003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [158004] (ulepszenie 1) — nazwa] 새벽을 가르는 검
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].name
   limit: do 40 znaków
   EN: Dawnsplitter
   PL:
262. [Umiejętność wroga [158004] (ulepszenie 1) — opis] [WhenUse] 자신의 [DawnOfficeStigmaSOne] 10당 최종 위력 +1, 피해량 +10%\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DawnOfficeStigmaSOne], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaSOne] = 새벽불 / Light of Daybreak; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 and deal +10% damage for every 10 [DawnOfficeStigmaSOne] on self\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
263. [Umiejętność wroga [158004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [158004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL:
265. [Umiejętność wroga [158004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [158004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
267. [Umiejętność wroga [158004] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 1회 발동, [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158004].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Combustion] on target once. Target loses 1 [Combustion] Count
   PL:
268. [Umiejętność wroga [158005] (ulepszenie 1) — nazwa] 새벽녘
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].name
   limit: do 40 znaków
   EN: Crack of Dawn
   PL:
269. [Umiejętność wroga [158005] (ulepszenie 1) — opis] [WhenUse] 지정된 대상 수 1명당 피해량 +20% (최대 60%)\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 최대 체력의 (모든 타겟의 [Combustion] 위력의 합 x 2)% 만큼 체력 회복 (최대 30%)\n[EndSkill] 자신의 [DawnOfficeStigmaSOne]과 [Combustion] 전부 소모
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [EndSkill], [Combustion], [DawnOfficeStigmaSOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn; [DawnOfficeStigmaSOne] = 새벽불 / Light of Daybreak
   EN: [WhenUse] Deal +20% damage for every target (max 60%)\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n[EndSkill] Heal (total sum of [Combustion] Potency on all targets x 2)% HP (max 30%)\n[EndSkill] Consume all [DawnOfficeStigmaSOne] and [Combustion] on self
   PL:
270. [Umiejętność wroga [158005] (ulepszenie 1) — tekst klimatyczny] 연기전쟁의 치열했던 여러 전장 중 한 곳. 그곳에서 어느 결전 병기의 남은 날개 한 쌍을 공간과 함께 녹여 자르며 새벽의 끝을 알리던 기술.\n\n“하… 죽을 뻔했군…”\n“이봐. 저 괴물을… 해치워 줄 수… 있겠나?”
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At one of the countless raging battlefields of the Smoke War, this very technique melted down and cleaved through a certain decisive weapon's last pair of wings and the space it inhabited, heralding the dawn's end.\n\n"Hah... That almost killed me...!"\n"Lady, do you think... you can finish that monster off?"
   PL:
271. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL:
273. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL:
274. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 2 times
   PL:
277. [Umiejętność wroga [158005] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 2회 발동
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158005].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Combustion] on the target 2 times
   PL:
278. [Umiejętność wroga [158006] (ulepszenie 1) — nazwa] 수호자
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158006].levelList[level=1].name
   limit: do 40 znaków
   EN: Guardian
   PL:
279. [Umiejętność wroga [158006] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [SupportProtect]를 1 얻음\n[StartBattle] 자신의 최대 체력의 20%만큼 보호막을 얻음\n[StartBattle] [Combustion]을 보유한 적의 수만큼 [Protection]를 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158006].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [SupportProtect], [Combustion], [Protection]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [Combustion] = 화상 / Burn; [Protection] = 보호 / Protection
   EN: [CanDuelGuard]\n[StartBattle] Gain 1 [SupportProtect]\n[StartBattle] Gain Shield equal to 20% of max HP\n[StartBattle] Gain [Protection] equal to number of enemies that have [Combustion]
   PL:
280. [Umiejętność wroga [158006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [158007] (ulepszenie 1) — nazwa] 아지랑이
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158007].levelList[level=1].name
   limit: do 40 znaków
   EN: Heat Haze
   PL:
282. [Umiejętność wroga [158007] (ulepszenie 1) — opis] [DuelCounter]\n[SupportProtect] 전용 스킬\n[WhenUse] [DawnOfficeStigmaSOne] 5 얻음\n[WhenUse] 모든 아군 정신력 6 상승
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158007].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SupportProtect], [WhenUse], [DawnOfficeStigmaSOne]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaSOne] = 새벽불 / Light of Daybreak
   EN: [DuelCounter]\n[SupportProtect] exclusive Skill\n[WhenUse] Gain 5 [DawnOfficeStigmaSOne]\n[WhenUse] All allies heal 6 SP
   PL:
283. [Umiejętność wroga [158007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL:
284. [Umiejętność wroga [158007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
285. [Umiejętność wroga [158101] (ulepszenie 1) — nazwa] 의뢰 처리
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158101].levelList[level=1].name
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność wroga [158101] (ulepszenie 1) — opis] [BeforeAttack] 정신력 10 회복\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158101].levelList[level=1].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [158101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Umiejętność wroga [158101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [158101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność wroga [158101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [PlusCoinValueUp] 1 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [PlusCoinValueUp]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: [UnBrokenCoinOnSucceedAttack] Gain 1 [PlusCoinValueUp] next turn
   PL:
291. [Umiejętność wroga [158102] (ulepszenie 1) — nazwa] 나비 베기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].name
   limit: do 40 znaków
   EN: Butterfly Slash
   PL:
292. [Umiejętność wroga [158102] (ulepszenie 1) — opis] [WhenUse] [DawnOfficeStigmaYOne] 6 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DawnOfficeStigmaYOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaYOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: [WhenUse] Gain 6 [DawnOfficeStigmaYOne]
   PL:
293. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 3, efekt 1 — opis] 자신의 [DawnOfficeStigmaYOne] 10당 이 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DawnOfficeStigmaYOne]
   znaczenie tagów: [DawnOfficeStigmaYOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: Reuse this Coin once for every 10 [DawnOfficeStigmaYOne] on self (max 2 times per Skill)
   PL:
297. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [158102] (ulepszenie 1) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158102].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [ReUseOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
300. [Umiejętność wroga [158103] (ulepszenie 1) — nazwa] 사출
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].name
   limit: do 40 znaków
   EN: Eject
   PL:
301. [Umiejętność wroga [158103] (ulepszenie 1) — opis] [WhenUse] [DawnOfficeStigmaYOne] 8 얻음\n[WhenUse] 자신의 [DawnOfficeStigmaYOne] 10당 최종 위력 +1\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DawnOfficeStigmaYOne], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaYOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 8 [DawnOfficeStigmaYOne]\n[WhenUse] Final Power +1 for every 10 [DawnOfficeStigmaYOne] on self\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
302. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 1회 발동, [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 3, efekt 2 — opis] 자신의 [DawnOfficeStigmaYOne] 10당 이 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [158103] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 1회 발동, [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158103].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [158104] (ulepszenie 1) — nazwa] 사출 - 정오
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].name
   limit: do 40 znaków
   EN: Eject - High Noon
   PL:
312. [Umiejętność wroga [158104] (ulepszenie 1) — opis] [WideAreaRampage]\n[WhenUse] 지정된 타겟수 1명당 피해량 +20% (최대 60%)\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 모든 대상에게 [VibrationIgnition]로 [Switch_Vibration]\n[EndSkill] 최대 체력의 모든 타겟의 [Combustion] 위력의 합만큼 체력 회복 (최대 15%)\n[EndSkill] 최대 체력의 자신의 [Combustion] 위력만큼 체력 회복 (최대 15%)\n[EndSkill] 자신의 [DawnOfficeStigmaYOne]과 [Combustion] 전부 소모
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [WhenUse], [DefeatDuel], [BeforeAttack], [VibrationIgnition], [Switch_Vibration], [EndSkill], [Combustion], [DawnOfficeStigmaYOne]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn …
   EN: [WideAreaRampage]\n[WhenUse] Deal +20% damage for every target (max 60%)\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] Trigger [Switch_Vibration] on all targets into [VibrationIgnition]\n[EndSkill] Heal (total sum of [Combustion] Potency on all targets)% HP (max 15%)\n[EndSkill] Heal ([Combustion] Potency on self)% HP (max 15%)\n[EndSkill] Consume all [DawnOfficeStigmaYOne] and [Combustion] on self
   PL:
313. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 2 — opis] 자신의 [DawnOfficeStigmaYOne] 10당 이 코인 1회 재사용 (스킬당 최대 2회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 3 — opis] - 재사용 시, 이 코인은 모든 공격 대상에게 적중함
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   EN: - On Reuse, this Coin hits all targets of the attack
   PL:
320. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
321. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 5 — opis] [ReUseOnSucceedAttack]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack]
   PL:
322. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 6 — opis] - [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: - [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 2 times
   PL:
323. [Umiejętność wroga [158104] (ulepszenie 1) — moneta 3, efekt 7 — opis] - [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 2회 발동
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158104].levelList[level=1].coinlist[#2].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: - [UnBrokenCoinOnSucceedAttack] Activate [Combustion] on the target 2 times
   PL:
324. [Umiejętność wroga [158105] (ulepszenie 1) — nazwa] 낙인
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158105].levelList[level=1].name
   limit: do 40 znaków
   EN: Stigmatize
   PL:
325. [Umiejętność wroga [158105] (ulepszenie 1) — opis] <color=#ff6000><mark color=#ff000040><b><u>턴 시작시 보유했던 자신의 [DawnOfficeStigmaYOne] 10당 피격 시 이 스킬 1회 재사용 (최대 2회)</color></mark></b></u>\n[StartBattle] [DawnOfficeStigmaYOne] 2당 최종 위력 +1 (최대 5)\n[StartBattle] [Combustion]을 보유한 적의 수만큼 [DefenseUp]를 얻음\n[WhenUse] 자신의 [DawnOfficeStigmaYOne] 10당 부정적인 효과 부여량 +1
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158105].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [DawnOfficeStigmaYOne], [StartBattle], [Combustion], [DefenseUp], [WhenUse]
   znaczenie tagów: [DawnOfficeStigmaYOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [StartBattle] = [전투 시작시] / [Combat Start]; [Combustion] = 화상 / Burn; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WhenUse] = [사용시] / [On Use]
   EN: <color=#ff6000><mark color=#ff000040><b><u>When hit, Reuse this Skill once for every 10 [DawnOfficeStigmaYOne] on self at Turn Start (max 2 times)</color></mark></b></u>\n[StartBattle] Final Power +1 for every 2 [DawnOfficeStigmaYOne] (max 5)\n[StartBattle] Gain [DefenseUp] equal to the number of enemies that have [Combustion]\n[WhenUse] Inflict +1 more negative effect for every 10 [DawnOfficeStigmaYOne] on self
   PL:
326. [Umiejętność wroga [158105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [158105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność wroga [158105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
329. [Umiejętność wroga [158105] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność wroga [158106] (ulepszenie 1) — nazwa] 연계
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158106].levelList[level=1].name
   limit: do 40 znaków
   EN: Seconded Offensive
   PL:
331. [Umiejętność wroga [158106] (ulepszenie 1) — opis] [WhenUse] 자신의 [DawnOfficeStigmaYOne] 1당 피해량 +2%, 10당 최종 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158106].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DawnOfficeStigmaYOne]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DawnOfficeStigmaYOne] = 불꽃나비의 관 / Fire Butterfly Coffin
   EN: [WhenUse]\n- Deal +2% damage for every [DawnOfficeStigmaYOne] on self\n- Final Power +1 for every 10 [DawnOfficeStigmaYOne] on self (max 3)
   PL:
332. [Umiejętność wroga [158106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Umiejętność wroga [158106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [158201] (ulepszenie 1) — nazwa] 의뢰 처리
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158201].levelList[level=1].name
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [158201] (ulepszenie 1) — opis] [BeforeAttack] 자신의 정신력 20 회복\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158201].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [BeforeAttack] Heal 20 SP\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
336. [Umiejętność wroga [158201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Umiejętność wroga [158201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [158201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność wroga [158201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [158202] (ulepszenie 1) — nazwa] 노을빛 검
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158202].levelList[level=1].name
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność wroga [158202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 4당 최종 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] Final Power +1 for every 4 [Combustion] on target (max 3)
   PL:
342. [Umiejętność wroga [158202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność wroga [158202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [158202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Umiejętność wroga [158203] (ulepszenie 1) — nazwa] 낙인
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158203].levelList[level=1].name
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Umiejętność wroga [158203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 4당 최종 위력 +1 (최대 2)\n[BeforeAttack] 정신력 15 회복\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158203].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 4 [Combustion] on target (max 2)\n[BeforeAttack] Heal 15 SP\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
347. [Umiejętność wroga [158203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [158203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Combustion]
   PL:
349. [Umiejętność wroga [158203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [158203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 2회 발동, [Combustion] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Combustion] on target 2 times. Target loses 2 [Combustion] Count
   PL:
351. [Umiejętność wroga [158204] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158204].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL:
352. [Umiejętność wroga [158204] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 4당 최종 위력 +1 (최대 3)\n<color=#ff6000><mark color=#ff000040><b><u>[OnSucceedEvade] 자신의 최대 체력의 15%만큼 회복</color></mark></b></u>
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158204].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Combustion], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] Final Power +1 for every 4 [Combustion] on target (max 3)\n<color=#ff6000><mark color=#ff000040><b><u>[OnSucceedEvade] Heal 15% HP</color></mark></b></u>
   PL:
353. [Umiejętność wroga [158301] (ulepszenie 1) — nazwa] 쾌속 찌르기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158301].levelList[level=1].name
   limit: do 40 znaków
   EN: High-speed Stabbing
   PL:
354. [Umiejętność wroga [158301] (ulepszenie 1) — opis] [WhenUse] 자신의 [WalpuTenWedgeOffice]가 3이면, 합 위력 +1\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WalpuTenWedgeOffice], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WalpuTenWedgeOffice] = 쐐기 사무소 / Wedge Office; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 3 [WalpuTenWedgeOffice], Clash Power +1\n[WinDuel] Gain +2 [Breath] Count
   PL:
355. [Umiejętność wroga [158301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
356. [Umiejętność wroga [158301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Umiejętność wroga [158301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
358. [Umiejętność wroga [158302] (ulepszenie 1) — nazwa] 섬광의 창
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158302].levelList[level=1].name
   limit: do 40 znaków
   EN: Sparking Spear
   PL:
359. [Umiejętność wroga [158302] (ulepszenie 1) — opis] [WhenUse] 자신의 [WalpuTenWedgeOffice]가 3이면, 합 위력 +2\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WalpuTenWedgeOffice], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WalpuTenWedgeOffice] = 쐐기 사무소 / Wedge Office; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 3 [WalpuTenWedgeOffice], Clash Power +2\n[WinDuel] Gain +2 [Breath] Count
   PL:
360. [Umiejętność wroga [158302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL:
361. [Umiejętność wroga [158302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +1 [Vibration] Count
   PL:
362. [Umiejętność wroga [158302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
363. [Umiejętność wroga [158303] (ulepszenie 1) — nazwa] 꿰뚫기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].name
   limit: do 40 znaków
   EN: Transpierce
   PL:
364. [Umiejętność wroga [158303] (ulepszenie 1) — opis] 피해량 +(<color=#ff6000><mark color=#ff000040><b><u>대상의 현재 체력 비율</color></mark></b></u> - 50)% (최대 50%, 최소 0%)\n크리티컬 피해량 +(자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 x 2.5)% (최대 50%)\n[WhenUse] 자신의 [WalpuTenWedgeOffice]가 3이면, 합 위력 +6\n[WinDuel] [Breath] 2 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Breath], [Vibration], [WhenUse], [WalpuTenWedgeOffice], [WinDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [WalpuTenWedgeOffice] = 쐐기 사무소 / Wedge Office; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Deal +(<color=#ff6000><mark color=#ff000040><b><u>current HP percentage on target</color></mark></b></u> - 50)% damage (max 50%, min 0%)\nDeal +(([Breath] Potency on self + [Vibration] Potency on target) x 2.5)% damage on Critical Hit (max 50%)\n[WhenUse] At 3 [WalpuTenWedgeOffice], Clash Power +6\n[WinDuel] Gain 2 [Breath] and +3 [Breath] Count
   PL:
365. [Umiejętność wroga [158303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność wroga [158303] (ulepszenie 1) — moneta 1, efekt 2 — opis] <color=#ff6000><mark color=#ff000040><b><u>대상이 [Switch_Vibration]이나 [FusionVibration] 상태면,</color></mark></b></u> 이 코인 피해량 +50%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: <color=#ff6000><mark color=#ff000040><b><u>If target is in [Switch_Vibration] or [FusionVibration] states,</color></mark></b></u> this Coin deals +50% damage
   PL:
367. [Umiejętność wroga [158303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL:
368. [Umiejętność wroga [158303] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 2 부여 (턴당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 2 [PenetrateTakeDamageUp] (once per turn)
   PL:
369. [Umiejętność wroga [158303] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [OnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]
   PL:
370. [Umiejętność wroga [158303] (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158303].levelList[level=1].coinlist[#0].coindescs[#5].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (once per Skill)
   PL:
371. [Umiejętność wroga [158304] (ulepszenie 1) — nazwa] 쐐기 대형 전개
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].name
   limit: do 40 znaków
   EN: Assume Wedge Formation
   PL:
372. [Umiejętność wroga [158304] (ulepszenie 1) — opis] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +30%\n[WhenUse]\n- 자신의 [Breath] 횟수 3 증가\n- 자신을 제외한 <color=#ff6000><mark color=#ff000040><b><u>행동 가능한 쐐기 사무소 소속 아군 수만큼 공격 가중치 증가</color></mark></b></u> (최대 2)\n[EndSkill]\n- 자신의 [WalpuTenComboWedge] 25 소모\n- (사용하지 못한 코인 갯수 x 5)만큼 다음 턴에 [WalpuTenComboWedge] 얻음\n- 자신을 제외한 쐐기 사무소 소속 아군에게 다음 턴에 [PenetrateResultUp] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [EndSkill], [WalpuTenComboWedge], [PenetrateResultUp], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [WalpuTenComboWedge] = 승기 / Momentum; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: Deal +30% damage for every excess Atk Weight beyond the # of actual targets\n[WhenUse]\n- Gain +3 [Breath] Count\n- <color=#ff6000><mark color=#ff000040><b><u>Gain Atk Weight equal to the number of other non-immobilized "Wedge Office[TabExplain]" allies</color></mark></b></u> (max 2)\n[EndSkill]\n- Consume 25 [WalpuTenComboWedge] on self\n- Gain [WalpuTenComboWedge] next turn equal to (# of Coins that weren't used x 5)\n- Apply 1 [PenetrateResultUp] next turn to other "Wedge Office[TabExplain]" allies
   PL:
373. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ComboSkill] : 쐐기 사무소 해결사 파멜라
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ComboSkill], [TabExplain]
   znaczenie tagów: [ComboSkill] = 연 / Joint Combo
   EN: [ComboSkill]: Wedge Office[TabExplain] Fixer Pamela
   PL:
374. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 1, efekt 2 — opis] - 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: - Deal +30% damage
   PL:
375. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 1, efekt 3 — opis] - 마지막 코인 적중시 [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [Vibration]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: - On final Coin Hit, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
376. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
377. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [ComboSkill] : 쐐기 사무소 해결사 파멜리
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ComboSkill], [TabExplain]
   znaczenie tagów: [ComboSkill] = 연 / Joint Combo
   EN: [ComboSkill]: Wedge Office[TabExplain] Fixer Pameli
   PL:
378. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 2, efekt 2 — opis] - 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 2, efekt 3 — opis] - 마지막 코인 적중시 [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +30% damage on Critical Hit
   PL:
382. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność wroga [158304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
384. [Umiejętność wroga [158305] (ulepszenie 1) — nazwa] 숨고르기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158305].levelList[level=1].name
   limit: do 40 znaków
   EN: Catch Breath
   PL:
385. [Umiejętność wroga [158305] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 3당, 코인 위력 +1 (최대 2)\n[OnSucceedEvade]\n- [Breath] 2 얻음 (턴 당 3회)\n- 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n[EndBattle] 다음 턴에 [PenetrateResultUp] 1, [PenetrateDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158305].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [OnSucceedEvade], [Agility], [EndBattle], [PenetrateResultUp], [PenetrateDamageUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Agility] = 신속 / Haste; [EndBattle] = [턴 종료 시] / [Turn End]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [WhenUse] Coin Power +1 for every 3 [Breath] Potency on self (max 2)\n[OnSucceedEvade]\n- Gain 2 [Breath] (3 times per turn)\n- Gain 2 [Agility] next turn (once per turn)\n[EndBattle] Gain 1 [PenetrateResultUp] and 1 [PenetrateDamageUp] next turn (once per turn)
   PL:
386. [Umiejętność wroga [158306] (ulepszenie 1) — nazwa] 물러서도록
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].name
   limit: do 40 znaków
   EN: Step Aside.
   PL:
387. [Umiejętność wroga [158306] (ulepszenie 1) — opis] [DuelCounter]\n원호방어 전용 스킬\n[WhenUse] 자신의 잃은 체력 20%당 합 위력 +1 (최대 4)\n[WhenUse]\n- [SupportProtect]한 대상 아군과 자신의 정신력 5 회복\n- 최대 체력의 15%만큼 보호막 얻음 (턴당 1회)\n- [Protection] 2 얻음 (턴당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [SupportProtect], [Protection], [TabExplain]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [SupportProtect] = 원호 방어 / Assist Defense; [Protection] = 보호 / Protection
   EN: [DuelCounter]\nAssist Defense[TabExplain] exclusive Skill\n[WhenUse] Clash Power +1 for every 20% missing HP on self (max 4)\n[WhenUse]\n- This unit and the ally this unit used [SupportProtect] on heal 5 SP\n- Gain Shield equal to 15% of this unit's max HP (once per turn)\n- Gain 2 [Protection] (once per turn)
   PL:
388. [Umiejętność wroga [158306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [158306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [158306] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność wroga [158306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [158306] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [158306] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158306].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność wroga [158401] (ulepszenie 1) — nazwa] 격돌
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158401].levelList[level=1].name
   limit: do 40 znaków
   EN: Collision
   PL:
395. [Umiejętność wroga [158401] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 3)\n[WhenUse] [Breath] 2 얻음\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: 쐐기 사무소 해결사 파멜라</color></mark></b></u> (턴당 1회)\n- [WalpuTenBattleFieldKnow] 1 얻음\n- 마지막 코인 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158401].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [WalpuTenBattleFieldKnow], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max 3)\n[WhenUse] Gain 2 [Breath]\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: Wedge Office[TabExplain] Fixer Pamela</color></mark></b></u> (once per turn)\n- Gain 1 [WalpuTenBattleFieldKnow]\n- Reuse the final Coin (once per Skill)
   PL:
396. [Umiejętność wroga [158401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność wroga [158401] (ulepszenie 1) — moneta 2, efekt 1 — opis] 자신의 [WalpuTenBattleFieldKnow] 1당, 피해량 +5% (최대 20%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WalpuTenBattleFieldKnow]
   znaczenie tagów: [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis
   EN: Deal +5% damage for every [WalpuTenBattleFieldKnow] on self (max 20%)
   PL:
398. [Umiejętność wroga [158401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność wroga [158401] (ulepszenie 1) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] [WalpuTenWedgeMarkSilver] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158401].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [WalpuTenWedgeMarkSilver]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [WalpuTenWedgeMarkSilver] = 은색 표식[쐐기] / Silver Mark [Wedge]
   EN: [ReUseOnSucceedAttack] Inflict 1 [WalpuTenWedgeMarkSilver]
   PL:
400. [Umiejętność wroga [158402] (ulepszenie 1) — nazwa] 여세를 몰아
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158402].levelList[level=1].name
   limit: do 50 znaków
   EN: Riding the Tide of the Offensive
   PL:
401. [Umiejętność wroga [158402] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158402].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor
   EN: [WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 3 [Breath]
   PL:
402. [Umiejętność wroga [158402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [158402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność wroga [158402] (ulepszenie 1) — moneta 3, efekt 1 — opis] 자신의 [WalpuTenBattleFieldKnow] 1당, 피해량 +5% (최대 20%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność wroga [158402] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158402].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
406. [Umiejętność wroga [158403] (ulepszenie 1) — nazwa] 창 휩쓸기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].name
   limit: do 40 znaków
   EN: Speared Sweep
   PL:
407. [Umiejętność wroga [158403] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: 쐐기 사무소 해결사 파멜라</color></mark></b></u> (턴당 1회)\n- [WalpuTenBattleFieldKnow] 1 얻음\n- 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [WalpuTenBattleFieldKnow], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: Wedge Office[TabExplain] Fixer Pamela</color></mark></b></u> (once per turn)\n- Gain 1 [WalpuTenBattleFieldKnow]\n- Deal +30% damage
   PL:
408. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL:
409. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 4, efekt 1 — opis] 자신의 [WalpuTenBattleFieldKnow] 1당, 피해량 +10% (최대 40%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WalpuTenBattleFieldKnow]
   znaczenie tagów: [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis
   EN: Deal +10% damage for every [WalpuTenBattleFieldKnow] on self (max 40%)
   PL:
411. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 4, efekt 2 — opis] 대상의 [Vibration] 위력 1당, 피해량 +2% (최대 20%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal +2% damage for every 1 [Vibration] Potency on target (max 20%)
   PL:
412. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 4, efekt 3 — opis] <color=#ff6000><mark color=#ff000040><b><u>대상이 [Switch_Vibration]이나 [FusionVibration] 상태면</color></mark></b></u>, 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: <color=#ff6000><mark color=#ff000040><b><u>If target is in [Switch_Vibration] or [FusionVibration] states,</color></mark></b></u> deal +30% damage
   PL:
413. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 4, efekt 4 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [158403] (ulepszenie 1) — moneta 4, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158403].levelList[level=1].coinlist[#3].coindescs[#4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL:
415. [Umiejętność wroga [158404] (ulepszenie 1) — nazwa] 빠르고 확실하게 꿰뚫어주마
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Run You Through Quick & True
   PL:
416. [Umiejętność wroga [158404] (ulepszenie 1) — opis] 대상의 [WalpuTenWedgeMarkSilver] 1당, 합 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[WhenUse] 모든 코인이 [SuperCoin]이 됨\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: 쐐기 사무소 해결사 파멜라</color></mark></b></u> (턴당 1회)\n- [WalpuTenBattleFieldKnow] 1 얻음\n- 피해량 +30%\n[EndSkill] 대상의 [WalpuTenWedgeMarkSilver] 전부 소모
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WalpuTenWedgeMarkSilver], [WhenUse], [Breath], [Vibration], [SuperCoin], [ComboSkill], [WalpuTenBattleFieldKnow], [EndSkill], [TabExplain]
   znaczenie tagów: [WalpuTenWedgeMarkSilver] = 은색 표식[쐐기] / Silver Mark [Wedge]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [ComboSkill] = 연 / Joint Combo; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Clash Power +1 for every [WalpuTenWedgeMarkSilver] on target (max 5)\n[WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[WhenUse] Convert all Coins into [SuperCoin]s\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: Wedge Office[TabExplain] Fixer Pamela</color></mark></b></u> (once per turn)\n- Gain 1 [WalpuTenBattleFieldKnow]\n- Deal +30% damage\n[EndSkill] Consume all [WalpuTenWedgeMarkSilver] on target
   PL:
417. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 1 — opis] 자신의 [WalpuTenBattleFieldKnow] 1당, 피해량 +10% (최대 40%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상의 [Vibration] 위력 1당, 피해량 +2% (최대 40%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal +2% damage for every 1 [Vibration] Potency on target (max 40%)
   PL:
421. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 3 — opis] <color=#ff6000><mark color=#ff000040><b><u>대상이 [Switch_Vibration]이나 [FusionVibration] 상태면</color></mark></b></u>, 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Reuse this Coin (once per Skill)
   PL:
423. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 5 — opis] [ReUseOnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [ReUseOnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]
   PL:
424. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 6 — opis] [ReUseOnSucceedAttack] 이 코인 최종 피해량의 (대상의 [WalpuTenWedgeMarkSilver] x 10)%만큼 관통 피해 (최대 50%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#5].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [WalpuTenWedgeMarkSilver]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [WalpuTenWedgeMarkSilver] = 은색 표식[쐐기] / Silver Mark [Wedge]
   EN: [ReUseOnSucceedAttack] Deal Pierce damage equal to ([WalpuTenWedgeMarkSilver] on target x 10)% of this Coin's final damage (max 50%)
   PL:
425. [Umiejętność wroga [158404] (ulepszenie 1) — moneta 3, efekt 7 — opis] [ReUseOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158404].levelList[level=1].coinlist[#2].coindescs[#6].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [ReUseOnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL:
426. [Umiejętność wroga [158405] (ulepszenie 1) — nazwa] 숨고르기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158405].levelList[level=1].name
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [158405] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력이 6이상이면, 코인 위력 +1\n[OnSucceedEvade] [Breath] 2 얻음 (스킬당 1회)\n[OnSucceedEvade] 다음 턴에 [Agility] 1 얻음 (턴당 1회)\n[EndBattle] 다음 턴에 [PenetrateResultUp] 1 얻음 (턴당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158405].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [OnSucceedEvade], [Agility], [EndBattle], [PenetrateResultUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Agility] = 신속 / Haste; [EndBattle] = [턴 종료 시] / [Turn End]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: [WhenUse] At 6+ [Breath] Potency, Coin Power +1\n[OnSucceedEvade] Gain 2 [Breath] (once per Skill)\n[OnSucceedEvade] Gain 1 [Agility] next turn (once per turn)\n[EndBattle] Gain 1 [PenetrateResultUp] next turn (once per turn)
   PL:
428. [Umiejętność wroga [158501] (ulepszenie 1) — nazwa] 격돌
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158501].levelList[level=1].name
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność wroga [158501] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 3)\n[WhenUse] [Breath] 4 얻음\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: 쐐기 사무소 해결사 파멜리</color></mark></b></u> (턴당 1회)\n- [WalpuTenBattleFieldKnow] 1 얻음\n- 마지막 코인 재사용 (스킬당 1회)\n[WinDuel] 다음 턴에 [PenetrateDamageUp] 1 얻음 (턴당 1회)\n[BeforeAttack] 자신의 [WalpuTenBattleFieldKnow] 1당, 마지막 코인의 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158501].levelList[level=1].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [WalpuTenBattleFieldKnow], [WinDuel], [PenetrateDamageUp], [BeforeAttack], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max 3)\n[WhenUse] Gain 4 [Breath]\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: Wedge Office[TabExplain] Fixer Pameli</color></mark></b></u> (once per turn)\n- Gain 1 [WalpuTenBattleFieldKnow]\n- Reuse the final Coin (once per Skill)\n[WinDuel] Gain 1 [PenetrateDamageUp] next turn (once per turn)\n[BeforeAttack] The final Coin gains Final Power +1 for every [WalpuTenBattleFieldKnow] on self (max 2)
   PL:
430. [Umiejętność wroga [158501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność wroga [158501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [ReUseOnSucceedAttack] [WalpuTenWedgeMarkGold] 1 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [WalpuTenWedgeMarkGold]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [WalpuTenWedgeMarkGold] = 금색 표식[쐐기] / Golden Mark [Wedge]
   EN: [ReUseOnSucceedAttack] Inflict 1 [WalpuTenWedgeMarkGold]
   PL:
432. [Umiejętność wroga [158502] (ulepszenie 1) — nazwa] 빈틈 노리기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158502].levelList[level=1].name
   limit: do 40 znaków
   EN: Gap Strike
   PL:
433. [Umiejętność wroga [158502] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 3)\n[WhenUse] [Breath] 3 얻음\n[WinDuel] 대상에게 [Vibration] 1 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n[BeforeAttack] 자신의 [WalpuTenBattleFieldKnow] 1당, 마지막 코인의 최종 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158502].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Vibration], [WinDuel], [VibrationExplosion], [BeforeAttack], [WalpuTenBattleFieldKnow]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max 3)\n[WhenUse] Gain 3 [Breath]\n[WinDuel] Inflict 1 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n[BeforeAttack] The final Coin gains Final Power +1 for every [WalpuTenBattleFieldKnow] on self (max 3)
   PL:
434. [Umiejętność wroga [158502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność wroga [158502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [158503] (ulepszenie 1) — nazwa] 창 휩쓸기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].name
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność wroga [158503] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: 쐐기 사무소 해결사 파멜리</color></mark></b></u> (턴당 1회)\n- [WalpuTenBattleFieldKnow] 1 얻음\n- 피해량 +40%\n[WinDuel] 대상에게 [Vibration] 2 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n[BeforeAttack] 자신의 [WalpuTenBattleFieldKnow] 1당, 마지막 코인의 최종 위력 +1 (최대 4)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [WalpuTenBattleFieldKnow], [WinDuel], [VibrationExplosion], [BeforeAttack], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: Wedge Office[TabExplain] Fixer Pameli</color></mark></b></u> (once per turn)\n- Gain 1 [WalpuTenBattleFieldKnow]\n- Deal +40% damage\n[WinDuel] Inflict 2 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n[BeforeAttack] The final Coin gains Final Power +1 for every [WalpuTenBattleFieldKnow] on self (max 4)
   PL:
438. [Umiejętność wroga [158503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [158503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [158503] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 [Vibration] 위력 1당, 피해량 +2% (최대 20%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność wroga [158503] (ulepszenie 1) — moneta 3, efekt 2 — opis] <color=#ff6000><mark color=#ff000040><b><u>대상이 [Switch_Vibration]이나 [FusionVibration] 상태면</color></mark></b></u>, 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Umiejętność wroga [158503] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [158503] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158503].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [158504] (ulepszenie 1) — nazwa] 빈틈 없이 확실하게 꿰뚫어주지
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].name
   limit: do 50 znaków
   EN: My Spear Will Puncture You True.
   PL:
445. [Umiejętność wroga [158504] (ulepszenie 1) — opis] 대상의 [WalpuTenWedgeMarkGold] 1당, 합 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[WhenUse] 모든 코인이 [SuperCoin]이 됨\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: 쐐기 사무소 해결사 파멜리</color></mark></b></u> (턴당 1회)\n- [WalpuTenBattleFieldKnow] 1 얻음\n- 피해량 +30%\n[WinDuel] 대상에게 [Vibration] 4 부여하고 [VibrationExplosion]\n[BeforeAttack] 자신의 [WalpuTenBattleFieldKnow]과 대상의 [WalpuTenWedgeMarkGold]의 합 1당, 마지막 코인의 최종 위력 +1 (최대 8)\n[EndSkill] 대상의 [WalpuTenWedgeMarkGold] 전부 소모
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WalpuTenWedgeMarkGold], [WhenUse], [Breath], [Vibration], [SuperCoin], [ComboSkill], [WalpuTenBattleFieldKnow], [WinDuel], [VibrationExplosion], [BeforeAttack], [EndSkill], [TabExplain]
   znaczenie tagów: [WalpuTenWedgeMarkGold] = 금색 표식[쐐기] / Golden Mark [Wedge]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [ComboSkill] = 연 / Joint Combo; [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win] …
   EN: Clash Power +1 for every [WalpuTenWedgeMarkGold] on target (max 5)\n[WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[WhenUse] Convert all Coins into [SuperCoin]s\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>[ComboSkill]: Wedge Office[TabExplain] Fixer Pameli</color></mark></b></u> (once per turn)\n- Gain 1 [WalpuTenBattleFieldKnow]\n- Deal +30% damage\n[WinDuel] Inflict 4 [Vibration] on target, then trigger [VibrationExplosion]\n[BeforeAttack] The final Coin gains +([WalpuTenBattleFieldKnow] on self + [WalpuTenWedgeMarkGold] on target) Final Power (max 8)\n[EndSkill] Consume all [WalpuTenWedgeMarkGold] on target
   PL:
446. [Umiejętność wroga [158504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [158504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność wroga [158504] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 [Vibration] 위력 1당, 피해량 +2% (최대 40%)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność wroga [158504] (ulepszenie 1) — moneta 3, efekt 2 — opis] <color=#ff6000><mark color=#ff000040><b><u>대상이 [Switch_Vibration]이나 [FusionVibration] 상태면</color></mark></b></u>, 피해량 +30%
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [158504] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [158504] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158504].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [158505] (ulepszenie 1) — nazwa] 숨고르기
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158505].levelList[level=1].name
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [158505] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력이 6이상이면, 코인 위력 +1\n[OnSucceedEvade] [Breath] 3 얻음 (스킬당 1회)\n[OnSucceedEvade] 다음 턴에 [Agility] 1 얻음 (턴당 1회)\n[EndBattle] 다음 턴에 [PenetrateResultUp] 1 얻음 (턴당 1회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158505].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [OnSucceedEvade], [Agility], [EndBattle], [PenetrateResultUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Agility] = 신속 / Haste; [EndBattle] = [턴 종료 시] / [Turn End]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: [WhenUse] At 6+ [Breath] Potency, Coin Power +1\n[OnSucceedEvade] Gain 3 [Breath] (once per Skill)\n[OnSucceedEvade] Gain 1 [Agility] next turn (once per turn)\n[EndBattle] Gain 1 [PenetrateResultUp] next turn (once per turn)
   PL:
454. [Umiejętność wroga [158601] (ulepszenie 1) — nazwa] 후회
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].name
   limit: do 40 znaków
   EN: Rue
   PL:
455. [Umiejętność wroga [158601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 4당 최종 위력 +2 (최대 4)\n[BeforeAttack] <color=#ff6000><mark color=#ff000040><b><u>자신의 정신력이 20/40 이상이면</color></mark></b></u>, 피해량 +50%/+100%\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Combustion], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +2 for every 4 [Combustion] on target (max 4)\n[BeforeAttack] <color=#ff6000><mark color=#ff000040><b><u>At 20+/40+ SP,</color></mark></b></u> deal +50%/+100% damage\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target
   PL:
456. [Umiejętność wroga [158601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Umiejętność wroga [158601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [158601] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Vibration]
   PL:
459. [Umiejętność wroga [158601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [158601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 2회 발동, [Combustion] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [158601] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회, [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158601].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL:
462. [Umiejętność wroga [158701] (ulepszenie 1) — nazwa] 서글픈 노을
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158701].levelList[level=1].name
   limit: do 40 znaków
   EN: Rueful Eventide
   PL:
463. [Umiejętność wroga [158701] (ulepszenie 1) — opis] [WhenUse] 자신의 정신력이 40 이상이면, 다음 턴에 [ParryingResultUp] 1 얻음\n[BeforeAttack] 정신력 10 회복
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ParryingResultUp], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] At 40+ SP, gain 1 [ParryingResultUp] next turn\n[BeforeAttack] Heal 10 SP
   PL:
464. [Umiejętność wroga [158701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
465. [Umiejętność wroga [158701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność wroga [158702] (ulepszenie 1) — nazwa] 깃털 방패
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158702].levelList[level=1].name
   limit: do 40 znaków
   EN: Feather Shield
   PL:
467. [Umiejętność wroga [158702] (ulepszenie 1) — opis] [WhenUse] [Protection] 2 얻음\n- <color=#ff6000><mark color=#ff000040><b><u>대상에게 [Combustion]이 있으면</color></mark></b></u>, 추가로 2 얻음\n[WhenUse] 자신의 정신력이 30 이상이면, 다음 턴에 [DefenseUp] 2 얻음
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158702].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Protection], [Combustion], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection; [Combustion] = 화상 / Burn; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain 2 [Protection]\n- <color=#ff6000><mark color=#ff000040><b><u>If target has [Combustion]</color></mark></b></u>, gain 2 additional [Protection]\n[WhenUse] At 30+ SP, gain 2 [DefenseUp] next turn
   PL:
468. [Umiejętność wroga [158702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL:
469. [Umiejętność wroga [158702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność wroga [158703] (ulepszenie 1) — nazwa] 이글거리는 검
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].name
   limit: do 40 znaków
   EN: Searing Sword
   PL:
471. [Umiejętność wroga [158703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 6당 최종 위력 +1 (최대 2)\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 자신의 정신력이 40/45 이상이면, 공격 가중치 +1/+2
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [DefeatDuel], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] Final Power +1 for every 6 [Combustion] on target (max 2)\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] At 40+/45+ SP, gain +1/+2 Atk Weight
   PL:
472. [Umiejętność wroga [158703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność wroga [158703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Combustion] Count
   PL:
474. [Umiejętność wroga [158703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [158703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 6 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL:
476. [Umiejętność wroga [158703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [158703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [PhilipWax] 3 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [PhilipWax]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [PhilipWax] = 불확실한 슬픔의 감정 / Emotion of Uncertain Sorrow
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [PhilipWax]
   PL:
478. [Umiejętność wroga [158704] (ulepszenie 1) — nazwa] 맹렬한 돌진
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158704].levelList[level=1].name
   limit: do 40 znaków
   EN: Fierce Charge
   PL:
479. [Umiejętność wroga [158704] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 6당 최종 위력 +1 (최대 2)\n[BeforeAttack] 대상의 [Combustion] 2당 피해량 +2% (최대 30%)\n[EndSkill] 1코인 재사용 횟수만큼 정신력 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158704].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Final Power +1 for every 6 [Combustion] on target (max 2)\n[BeforeAttack] Deal +2% damage for every 2 [Combustion] on target (max 30%)\n[EndSkill] Lose (# of Coin 1 Reused) SP
   PL:
480. [Umiejętność wroga [158704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność wroga [158704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 이 코인 재사용 (스킬당 최대 2회)
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse this Coin (2 times per Skill)
   PL:
482. [Umiejętność wroga [158704] (ulepszenie 1) — moneta 1, efekt 3 — opis] [ReUseOnSucceedAttack] 대상의 [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158704].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: [ReUseOnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
483. [Umiejętność wroga [158704] (ulepszenie 1) — moneta 1, efekt 4 — opis] [ReUseOnSucceedAttack] [PhilipWax] 2 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158704].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [PhilipWax]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [PhilipWax] = 불확실한 슬픔의 감정 / Emotion of Uncertain Sorrow
   EN: [ReUseOnSucceedAttack] Inflict 2 [PhilipWax]
   PL:
484. [Umiejętność wroga [158705] (ulepszenie 1) — nazwa] 타오르는 일격
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158705].levelList[level=1].name
   limit: do 40 znaków
   EN: Blazing Strike
   PL:
485. [Umiejętność wroga [158705] (ulepszenie 1) — opis] <color=#ff6000><mark color=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</color></mark></b></u>\n이 스킬을 장착한 턴에 <color=#ff6000><mark color=#ff000040><b><u>공격 스킬로 피격 시, [ResultReduction] 2 얻음</color></mark></b></u> (스킬당 1회. 턴당 최대 3회)\n[WhenUse] 메인 타겟의 [Combustion] 4당 최종 위력 +2 (최대 4)\n[BeforeAttack] 자신의 정신력이 20/40 이상이면, 피해량 +50%/+100%\n[DefeatDuel]\n- 피해량 -80%\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158705].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ResultReduction], [WhenUse], [Combustion], [BeforeAttack], [DefeatDuel], [EndSkill]
   znaczenie tagów: [ResultReduction] = 위력 감소 / Power Down; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <color=#ff6000><mark color=#ff000040><b><u>Can Clash with this Skill regardless of Speed</color></mark></b></u>\nDuring the turn this unit has this Skill equipped, <color=#ff6000><mark color=#ff000040><b><u>gain 2 [ResultReduction] when hit by Attack Skills</color></mark></b></u> (once per Skill; 3 times per turn)\n[WhenUse] Final Power +2 for every 4 [Combustion] on the main target (max 4)\n[BeforeAttack] At 20+/40+ SP, deal +50%/+100% damage\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n[EndSkill] End this turn
   PL:
486. [Umiejętność wroga [158705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [158705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion]
   PL:
488. [Umiejętność wroga [158705] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Combustion] 2회 발동, [Combustion] 횟수 2 감소
   źródło: Skills_Abnormality-walpu10.json :: dataList[id=158705].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu10] Pasywka wroga: Passives_Abnormality-walpu10
- plik gry: `Passives_Abnormality-walpu10.json`

489. [[walpu10] Pasywka wroga [158001] — nazwa] 새벽 사무소 - 수호자
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158001].name
   limit: do 40 znaków
   EN: Dawn Office - Guardian
   PL:
490. [[walpu10] Pasywka wroga [158001] — opis] 턴 시작시 남은 체력 비율이 가장 적은 아군에게 [Protection] 2 부여\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 남은 체력이 30% 이하면,</color></mark></b></u> 같은 소속 아군의 스킬 3 적중 시 대상 적에게 ‘여명의 섬광’ 사용 (턴당 1회)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158001].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Turn Start: Apply 2 [Protection] to the ally that has the lowest remaining HP percentage\n\n<color=#ff6000><mark color=#ff000040><b><u>At 30%- HP,</color></mark></b></u> when an ally from the same faction hits using Skill 3, use the "Flash of Sunup" Skill against the targeted enemy (once per turn)
   PL:
491. [[walpu10] Pasywka wroga [158002] — nazwa] 모르겐포이어[스티그마 공방]
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158002].name
   limit: do 50 znaków
   EN: Morgenfeuer [Stigma Workshop]
   PL:
492. [[walpu10] Pasywka wroga [158002] — opis] 스테이지 첫 등장 시 [DawnOfficeStigmaSOne] 0 얻음\n\n아래 조건 만족 시 [DawnOfficeStigmaSOne] 얻음\n- 기본 스킬 적중시 3 얻음 (스킬당 1회)\n· <noparse>새벽 사무소</noparse> - 수호자 패시브로 사용하는 ‘여명의 섬광’이면, 1 추가로 얻음\n· 대상에게 [Combustion]이 있으면, 1 추가로 얻음\n- (자신이 보유한 [Combustion] 발동으로 인한 피해/2) 만큼 얻음\n\n[DawnOfficeStigmaSOne]이 30이면, 강력한 스킬을 사용함\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 스킬 적중시 대상에게 [Combustion]이 있으면, 해당 스킬 마지막 코인 최종 피해량의 30%만큼 흐트러짐 피해</color></mark></b></u>\n- 파괴된 코인에는 해당 효과가 발동하지 않음
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158002].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [DawnOfficeStigmaSOne], [Combustion]
   znaczenie tagów: [DawnOfficeStigmaSOne] = 새벽불 / Light of Daybreak; [Combustion] = 화상 / Burn
   EN: Upon entering the Encounter for the first time: Gain 0 [DawnOfficeStigmaSOne]\n\nGain [DawnOfficeStigmaSOne] when the following conditions are met:\n- On Hit using Base Skills: Gain 3 Stacks (once per Skill)\n · If the said Skill is "Flash of Sunup" used via the <noparse>Dawn Office</noparse> - <noparse>Guardian</noparse> Passive, gain 1 additional Stack\n · If target has [Combustion], gain 1 more\n- Gain Stacks equal to (damage taken from [Combustion] activation on self / 2)\n\nAt 30 [DawnOfficeStigmaSOne], use a powerful Skill\n\n<color=#ff6000><mark color=#ff000040><b><u>On Hit using this unit's Skills, if target has [Combustion], raise target's Stagger Threshold by 30% of the final damage dealt by the said Skill's final Coin</color></mark></b></u>\n- This effect does not activate on Cracked Coins
   PL:
493. [[walpu10] Pasywka wroga [158002] — tekst klimatyczny] A+급의 공방 무기. 해결사로서 처음 일을 시작했을 때부터 연기전쟁과 그 이후까지. 새벽녘의 해결사의 손에서 휘둘러진 검. 새벽녘의 해결사가 실적을 쌓을 때마다 스티그마 공방의 유명세는 높아졌고, 그에 대한 보답으로 스티그마 공방에서 몇 번이고 그를 위해 이 검을 개량해 주었다. 쌓여온 관록과도 같이, 이 검 또한 단조되고 개선되어 왔다. 그렇게 한때 S급이라는 평가를 받았던 무기였지만, 새벽녘의 해결사가 일선에서 물러나 다음 세대를 가르치는 사이, 필연적으로 모르겐포이어의 열기는 식어가고, 날 끝은 무뎌져 갔다.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158002].flavor
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An A+ class Workshop weapon that has remained a constant companion of its wielder, <i>the Fixer at the Crack of Dawn</i>, since his first days as a Fixer through the Smoke War and its fallout. Every contract successfully carried out by the Fixer added to Stigma Workshop's fame, and as a show of gratitude, they repeatedly upgraded and expanded the weapon's capabilities. Just as the Fixer's seasoned renown was built up over time, this blade, too, was forged, remade, and sharpened by the years. \nMorgenfeuer, once regarded as an S-class weapon, inevitably lost its fervor and edge in the twilight years of the Fixer at the Crack of Dawn as he withdrew from the front lines of the Fixer business in favor of teaching the next generation.
   PL:
494. [[walpu10] Pasywka wroga [158003] — nazwa] 스티그마 공방 무기
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158003].name
   limit: do 40 znaków
   EN: Stigma Workshop Weaponry
   PL:
495. [[walpu10] Pasywka wroga [158003] — opis] 자신의 스킬로 [Combustion]을 부여할 때, 부여하는 [Combustion] 위력 및 횟수 수치 +1\n- 자신의 스킬이 적중한 적의 [Combustion] 횟수가 3 미만이면, 대상의 [Combustion] 횟수 1 증가
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158003].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit inflicts [Combustion] using its Skills, inflict +1 more [Combustion] Potency and Count\n- If an enemy hit by this unit's Skills has fewer than 3 [Combustion] Count, inflict +1 [Combustion] Count on the target
   PL:
496. [[walpu10] Pasywka wroga [158004] — nazwa] 새벽녘의 해결사
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158004].name
   limit: do 50 znaków
   EN: The Fixer at the Crack of Dawn
   PL:
497. [[walpu10] Pasywka wroga [158004] — opis] 모든 수감자가 정신력 20 회복 (전투당 1회, 빼기 코인 인격은 감소로 적용)\n\n[Combustion] 효과로 받는 피해량 -50% (소수점 버림)\n- 체력이 50% 미만이면, 효과가 강화 되어, [Combustion] 효과로 받는 피해량 -75%\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158004].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [PanicChangeLock]
   znaczenie tagów: [Combustion] = 화상 / Burn; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: All Sinners heal 20 SP (once per Encounter; Minus Coin Identities lose SP instead)\n\nTake -50% damage from [Combustion] (rounded down)\n- At lower than 50% HP, this effect is enhanced and this unit takes -75% damage from [Combustion]\n\nApply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 45
   PL:
498. [[walpu10] Pasywka wroga [158101] — nazwa] 새벽 사무소 - 선배
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158101].name
   limit: do 40 znaków
   EN: Dawn Office - Seonbae
   PL:
499. [[walpu10] Pasywka wroga [158101] — opis] 턴 시작시 속도가 빠른 아군에게 [ParryingResultUp] 2 부여\n- 속도가 동일하면, 필립, 살바도르, 유나 순으로 부여함\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 남은 체력이 30% 이하면,</color></mark></b></u> 같은 소속 아군의 스킬 3 적중 시 대상 적에게 ‘<noparse>연계</noparse>’ 사용 (턴당 1회)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158101].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, <noparse>, </noparse>, \n, [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: Apply 2 [ParryingResultUp] to the ally with the fastest Speed\n- If Speed is equal, prioritize Philip, Salvador, then Yuna\n\n<color=#ff6000><mark color=#ff000040><b><u>At 30%- HP,</color></mark></b></u> when an ally from the same faction hits using Skill 3, use "<noparse>Seconded Offensive</noparse>" against the targeted enemy (once per turn)
   PL:
500. [[walpu10] Pasywka wroga [158102] — nazwa] 포이어팔터[스티그마 공방]
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158102].name
   limit: do 50 znaków
   EN: Feuerfalter [Stigma Workshop]
   PL:
501. [[walpu10] Pasywka wroga [158102] — opis] 스테이지 첫 등장 시 [DawnOfficeStigmaYOne] 0 얻음\n\n아래 조건 만족 시 [DawnOfficeStigmaYOne] 얻음\n- 기본 스킬 적중시 3 얻음 (스킬당 1회)\n· <noparse>새벽 사무소</noparse> - 선배 패시브로 사용하는 ‘<noparse>연계</noparse>’이면, 1 추가로 얻음\n· 대상에게 [Combustion]이 있으면, 1 추가로 얻음\n- (자신이 보유한 [Combustion] 발동으로 인한 피해/2) 만큼 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>[DawnOfficeStigmaYOne]이 30이면, 강력한 스킬을 사용함</color></mark></b></u>
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158102].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [DawnOfficeStigmaYOne], [Combustion]
   znaczenie tagów: [DawnOfficeStigmaYOne] = 불꽃나비의 관 / Fire Butterfly Coffin; [Combustion] = 화상 / Burn
   EN: Upon entering the Encounter for the first time: Gain 0 [DawnOfficeStigmaYOne]\n\nGain [DawnOfficeStigmaYOne] when the following conditions are met:\n- On Hit using Base Skills: Gain 3 Stacks (once per Skill)\n · If the said Skill is "<noparse>Seconded Offensive</noparse>" used via the <noparse>Dawn Office</noparse> - Seonbae Passive, gain 1 additional Stack\n · If target has [Combustion], gain 1 more\n- Gain Stacks equal to (damage taken from [Combustion] activation on self / 2)\n\n<color=#ff6000><mark color=#ff000040><b><u>At 30 [DawnOfficeStigmaYOne], use a powerful Skill</color></mark></b></u>
   PL:
502. [[walpu10] Pasywka wroga [158102] — tekst klimatyczny] 캐리어 또는 악기 케이스와 같이 생긴 이 무기를 쓰는 이유는 명확하다. 첫 번째는 일상에 녹아들기 위함이다. 전투에서 활용하기 어렵고 복잡한 유형의 무기는 오히려 그 비효율성 때문에 무기로 인식되지 않을 확률이 높다.\n두 번째는 캐리어의 모양, 그 자체로 인해 생기는 수납력이다. 그렇기에 무언가를 담는 형태의 무기는 제뱌찌 협회에서 적극적으로 사용한다.\n다만, 이러한 장점과 별개로 공방 장비를 쓰는 이들 사이에서 평가는 좋지 않다. 이 무기를 다루기 위해 투자한 시간을 다른 무기에 쏟았다면, 더 강해졌을 것이라거나, 겉멋이나 든 요즘 해결사들이 쓰는 장비라는 말을 종종 들을 수 있다. \n이러한 까다로운 장비를 들고 있는 사람을 만났을 때, 그 사람이 고등급 해결사, 혹은 직책 높은 조직원이라는 것은… 역설적이게도 다른 의미를 가진다. 그렇기에 공방에서 이 장비의 명칭은 캐리어가 아닌 관, 코핀으로 불리고 있다. 그리고 관에는 으레 나비가 따라붙는다.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158102].flavor
   limit: do 1730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The appeal of a weapon shaped like a suitcase or a musical instrument case is clear enough.\n\nFirst, the user may blend into the cover of daily life without raising alarm. Though arms of this sort are unwieldy and complicated to make use of in battle, that perceived shortcoming makes them less likely to be recognized as tools of killing.\n\nSecondly, weapons fashioned into the form of a case afford storage capacity. Container-shaped arms, for example, are actively used by the Fixers of the Devyat' Association.\n\nSuch convenience, however, does not automatically win favors from those who elect Workshop gear as their weapon of choice. The common opinion is that anyone who invests so much time in mastering this sort of weaponry would be better served by training with something else—in fact, the user would often hear snide remarks from other combatants, ranging from "Fixers these days" to "showy and pretentious."\n\nBut should one let this reputation for impracticality drop one's guard when facing an opponent armed with such a finicky piece of equipment, especially if they happen to be a high-ranking Fixer or a Syndicate officer, one will find that the laughable "containers" or "cases" carry quite a different weight—a weight grave enough for any Workshop worth its name to call them "coffins." And coffins, as a matter of fact, have a way of inviting butterflies.
   PL:
503. [[walpu10] Pasywka wroga [158103] — nazwa] 스티그마 공방 무기
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158103].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [[walpu10] Pasywka wroga [158103] — opis] 자신의 스킬로 [Combustion]을 부여할 때, 부여하는 [Combustion] 위력 및 횟수 수치 +1\n- 자신의 스킬이 적중한 적의 [Combustion] 횟수가 3 미만이면, 대상의 [Combustion] 횟수 1 증가
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158103].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [[walpu10] Pasywka wroga [158104] — nazwa] 고독한 해결사
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158104].name
   limit: do 40 znaków
   EN: The Lone Fixer
   PL:
506. [[walpu10] Pasywka wroga [158104] — opis] <color=#ff6000><mark color=#ff000040><b><u>턴 종료시 다른 아군이 없으면 [LoneFixer]를 얻음</color></mark></b></u>\n\n[Combustion] 효과로 받는 피해량 -50% (소수점 버림)\n- 체력이 50% 미만이면, 효과가 강화 되어, [Combustion] 효과로 받는 피해량 -75%\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158104].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [LoneFixer], [Combustion], [PanicChangeLock]
   znaczenie tagów: [LoneFixer] = 고독한 해결사 / The Lone Fixer; [Combustion] = 화상 / Burn; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: <color=#ff6000><mark color=#ff000040><b><u>Turn End: If there are no other allies remaining on the field, gain [LoneFixer]</color></mark></b></u>\n\nTake -50% damage from [Combustion] (rounded down)\n- At lower than 50% HP, this effect is enhanced and this unit takes -75% damage from [Combustion]\n\nApply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 45
   PL:
507. [[walpu10] Pasywka wroga [158104] — tekst klimatyczny] “고독이 뭔지 알아? 소중했던 사람이 멀리 떠나버려서, 더 이상 함께 점심을 먹을 수 없다는 거. 나한텐 그게 고독이더라고. 되도록… 필립, 너는 고독이라는 걸 이해할 일이 없었으면 좋겠네.”
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158104].flavor
   limit: do 330 znaków
   EN: "Do you know what loneliness is? It's when someone you held dear has gone far away, and you can't sit down to lunch with them anymore. That's what loneliness means to me, anyway. I just hope... that you never have to find out what it feels like, Philip."
   PL:
508. [[walpu10] Pasywka wroga [158201] — nazwa] 스티그마 공방 무기
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158201].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [[walpu10] Pasywka wroga [158201] — opis] 자신의 스킬로 [Combustion]을 부여할 때, 부여하는 [Combustion] 위력 및 횟수 수치 +1\n- 자신의 스킬이 적중한 적의 [Combustion] 횟수가 3 미만이면, 대상의 [Combustion] 횟수 1 증가
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158201].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [[walpu10] Pasywka wroga [158202] — nazwa] 격정
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158202].name
   limit: do 40 znaków
   EN: Passion
   PL:
511. [[walpu10] Pasywka wroga [158202] — opis] <color=#ff6000><mark color=#ff000040><b><u>자신의 정신력이 20/40 이상이면,</color></mark></b></u> 코인 위력이 1/2씩 증가
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158202].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>
   EN: <color=#ff6000><mark color=#ff000040><b><u>At 20+/40+ SP,</color></mark></b></u> Coin Power +1/+2
   PL:
512. [[walpu10] Pasywka wroga [158203] — nazwa] 새벽 사무소 - 신입
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158203].name
   limit: do 40 znaków
   EN: Dawn Office - Rookie
   PL:
513. [[walpu10] Pasywka wroga [158203] — opis] [Combustion] 효과로 받는 피해량 -40% (소수점 버림)\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨\n\n체력이 0이 되면…
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158203].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [PanicChangeLock]
   znaczenie tagów: [Combustion] = 화상 / Burn; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Take -40% damage from [Combustion] (rounded down)\n\nApply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 45\n\nWhen HP reaches 0...
   PL:
514. [[walpu10] Pasywka wroga [158301] — nazwa] 불굴
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158301].name
   limit: do 40 znaków
   EN: Unrelenting
   PL:
515. [[walpu10] Pasywka wroga [158301] — opis] <color=#ff6000><mark color=#ff000040><b><u>이번 전투에서 체력이 0이 되는 피해를 받았을 때,</color></mark></b></u> 다음 효과가 발동 (전투당 1회)\n- 해당 피해를 받지 않고 해당 턴 동안 체력이 1 미만으로 감소하지 않음\n- 턴 종료 시, 최대 체력의 50%만큼 체력 회복\n- 이 효과가 발동되었으면, 이번 전투 동안 받는 피해량 -20%
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158301].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: <color=#ff6000><mark color=#ff000040><b><u>In this Encounter, when this unit takes damage that brings its HP down to 0,</color></mark></b></u> apply the following effects (once per Encounter):\n- Nullify that damage; then, this unit's HP cannot drop below 1 for the turn\n- Turn End: Heal 50% HP\n- If this effect was activated, take -20% damage for this Encounter
   PL:
516. [[walpu10] Pasywka wroga [158302] — nazwa] 쐐기 사무소
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158302].name
   limit: do 40 znaków
   EN: Wedge Office
   PL:
517. [[walpu10] Pasywka wroga [158302] — opis] 스테이지 첫 등장 시, 아래 효과 적용\n- 정신력 45 회복\n- 모든 쐐기 사무소 소속 아군에게 [WalpuTenWedgeOffice] 3 부여\n\n턴 시작 시 <color=#ff6000><mark color=#ff000040><b><u>흐트러짐 상태인 아군이 있으면</color></mark></b></u> 쐐기 사무소 대표 오스카가 [SupportProtect] 2 얻음 (자신 제외)\n<color=#ff6000><mark color=#ff000040><b><u>전투 중 아군이 흐트러지면</color></mark></b></u>, 쐐기 사무소 대표 오스카가 [SupportProtect] 1 얻음 (턴당 1회, 상시 체크)\n- 위 두 효과로 [SupportProtect] 획득 시 쐐기 사무소 대표 오스카가 흐트러짐 상태면, 흐트러짐을 해제 (강제 흐트러짐 제외)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158302].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WalpuTenWedgeOffice], [SupportProtect], [TabExplain]
   znaczenie tagów: [WalpuTenWedgeOffice] = 쐐기 사무소 / Wedge Office; [SupportProtect] = 원호 방어 / Assist Defense
   EN: Upon entering the Encounter for the first time, activate the following effects:\n- Heal 45 SP\n- Apply 3 [WalpuTenWedgeOffice] to all Wedge Office[TabExplain] allies\n\nTurn Start: <color=#ff6000><mark color=#ff000040><b><u>If an ally is Staggered,</color></mark></b></u> Wedge Office[TabExplain] Rep Oscar gains 2 [SupportProtect] (excluding self)\n<color=#ff6000><mark color=#ff000040><b><u>When an ally becomes Staggered during combat,</color></mark></b></u> Wedge Office[TabExplain] Rep Oscar gains 1 [SupportProtect] (once per turn; checked continuously)\n- If Wedge Office[TabExplain] Rep Oscar is Staggered when gaining [SupportProtect] from the above two effects, recover from Stagger (excluding forced Staggers)
   PL:
518. [[walpu10] Pasywka wroga [158303] — nazwa] 쐐기 원호
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158303].name
   limit: do 40 znaków
   EN: Assistance of the Wedge
   PL:
519. [[walpu10] Pasywka wroga [158303] — opis] 자신을 포함한 아군이 아래 조건 만족시, [WalpuTenComboWedge] 1 얻음 (조건별로 캐릭터당 턴당 1회)\n해당 캐릭터가 쐐기 사무소 소속이면, 대신 [WalpuTenComboWedge] 2 얻음\n- 스킬 사용시\n- 합 승리시\n- 자신의 기본 스킬로 [VibrationExplosion] 발생시
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158303].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WalpuTenComboWedge], [VibrationExplosion], [TabExplain]
   znaczenie tagów: [WalpuTenComboWedge] = 승기 / Momentum; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When an ally, including this unit, meets the following conditions, gain 1 [WalpuTenComboWedge] (once per condition per character per turn)\nIf the said character is in "Wedge Office[TabExplain]", gain 2 [WalpuTenComboWedge] instead\n- On Skill Use\n- On Clash Win\n- When triggering [VibrationExplosion] using Base Skills
   PL:
520. [[walpu10] Pasywka wroga [158303] — tekst klimatyczny] 대부분의 해결사 사무소는 협력을 통해 서로의 부족함을 보완한다.\n그중에서도 호흡이 잘 맞는 사무소들은 더 많은 정보를 교류하고 신뢰를 쌓아 형제처럼 지내기도 한다.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158303].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Most Fixer Offices work together to make up for one another's shortcomings.\n\nSome Offices, however, find themselves so perfectly in sync that their partnership grows into something more. As they exchange information and forge deeper bonds of trust, they may eventually come to regard one another as siblings.
   PL:
521. [[walpu10] Pasywka wroga [158304] — nazwa] 쐐기식 창술
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158304].name
   limit: do 40 znaków
   EN: Wedge-style Spearmanship
   PL:
522. [[walpu10] Pasywka wroga [158304] — opis] [VibrationExplosion]로 가하는 흐트러짐 피해량 +10%\n턴 시작 시 [PenetrateResultUp], [PenetrateDamageUp] 1 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>현재 체력 비율이 50% 이상이거나 보호막을 보유한 대상에게 가하는 피해량 +20%</color></mark></b></u>\n\n기본 스킬로 피해를 줄 때 대상의 방어 레벨이 적중한 스킬의 공격 레벨보다 높으면, 수치 차이 1당 피해량 +2% (최대 30%)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158304].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [VibrationExplosion], [PenetrateResultUp], [PenetrateDamageUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: +10% to Stagger Threshold raised by [VibrationExplosion]\nTurn Start: Gain 1 [PenetrateResultUp] and [PenetrateDamageUp]\n\n<color=#ff6000><mark color=#ff000040><b><u>Deal +20% damage to targets at 50%+ current HP and targets that have Shield</color></mark></b></u>\n\nWhen dealing damage using Base Skills, if the target's Defense Level is higher than the Offense Level of the Skill that hit, deal +2% damage for every 1 Level of difference (max 30%)
   PL:
523. [[walpu10] Pasywka wroga [158304] — tekst klimatyczny] 창끝을 날카롭게 가는 것만으로는 관통력을 높이는 데 한계가 있고, 특허 받은 합금이나 유적에서 발견되는 재료로 만든 창은 어지간한 사무소의 몇년치 예산과 맞먹는다. 반면 주변에 흐르는 바람을 무기에 휘감는 기술은, 다루는 공방이 많고 들어가는 값에 비해 관통력 또한 뛰어나다.\n\n쐐기 사무소의 창도 이러한 기술을 다루는 공방에서 만들어졌다. 이는 회전을 적극적으로 섞는 쐐기 사무소의 창술과 합쳐져, 여태껏 수많은 적을 꿰뚫었다.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158304].flavor
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is only so much piercing power to be gained from sharpening a spearhead. Spears forged from Patented alloys or rare materials recovered from the Ruins may offer greater results, but their price can rival several years' worth of an ordinary Fixer Office's budget. A far more economical approach is to harness the surrounding currents of wind and coil them around the weapon, granting it formidable piercing power at a fraction of the cost. The technique is well-established, with many Workshops offering their own implementations.\n\nWedge Office's spears are the handiwork of one such Workshop. Combined with the Office's distinctive spearwork, which makes masterful use of twisting and rotational movements, these weapons have run countless foes through.
   PL:
524. [[walpu10] Pasywka wroga [158401] — nazwa] 쐐기 박기
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158401].name
   limit: do 40 znaków
   EN: Wedge Drive
   PL:
525. [[walpu10] Pasywka wroga [158401] — opis] 아래 조건 중 하나라도 만족하면 [WalpuTenBattleFieldKnow] 1 얻음 (턴당 1회)\n- 전투 중 적이 사망했거나 흐트러짐 상태가 될 경우\n- <color=#ff6000><mark color=#ff000040><b><u>부정적인 효과가 4종류 이상 있는 대상에게 공격 적중 시</color></mark></b></u>\n- [WalpuTenWedgeMarkSilver]가 있는 대상에게 공격 적중 시\n\n관통 스킬로 마지막 코인 적중 시 메인 타겟에게 [WalpuTenWedgeMarkGold] 1 부여 (스킬당 1회)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158401].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WalpuTenBattleFieldKnow], [WalpuTenWedgeMarkSilver], [WalpuTenWedgeMarkGold]
   znaczenie tagów: [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis; [WalpuTenWedgeMarkSilver] = 은색 표식[쐐기] / Silver Mark [Wedge]; [WalpuTenWedgeMarkGold] = 금색 표식[쐐기] / Golden Mark [Wedge]
   EN: When any of the following conditions are met, gain 1 [WalpuTenBattleFieldKnow] (once per turn)\n- When an enemy is defeated or becomes Staggered during combat\n- <color=#ff6000><mark color=#ff000040><b><u>On Hit against a target that has 4 or more types of negative effect</color></mark></b></u>\n- On Hit against a target that has [WalpuTenWedgeMarkSilver]\n\nOn final Coin Hit using Pierce Skills, inflict 1 [WalpuTenWedgeMarkGold] on the main target (once per Skill)
   PL:
526. [[walpu10] Pasywka wroga [158402] — nazwa] 도시의 사냥꾼
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158402].name
   limit: do 40 znaków
   EN: Hunters of the City
   PL:
527. [[walpu10] Pasywka wroga [158402] — opis] 스테이지 첫 등장시, 정신력 45 회복\n\n턴 종료 시 자신의 [Breath] 위력이 10 이상이면, 다음 턴에 [Agility] 1 얻음\n\n자신의 [Breath] 위력이 20을 초과했으면, 기본 스킬로 가하는 크리티컬 피해량 +(초과한 수치)% (최대 25%)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158402].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: Upon entering the Encounter for the first time, heal 45 SP\n\nTurn End: At 10+ [Breath] Potency, gain 1 [Agility] next turn\n\nAt 20+ [Breath] Potency, Base Skills deal +(excess Potency)% damage on Critical Hit (max 25%)
   PL:
528. [[walpu10] Pasywka wroga [158402] — tekst klimatyczny] 도시의 밤거리는 언제나 비열하고 야만적인 것들로 우글거린다.\n인생 역전을 노리는 쥐들부터 복수를 꿈꾸는 뒷골목 주민, 이권을 다투는 조직들과 손가락 그리고 청소부까지.\n그렇기에 밤에 이루어지는 의뢰는 대개 보수가 높음에도 인기가 없다.\n하지만 그런 심야의 의뢰를 기회로 여기는 자들도 있다.\n뛰어난 상황 판단 능력과 우환을 남기지 않는 신속하고 빈틈없는 마무리.\n그 두 가지를 무기로 쐐기 사무소는 매번 살아남아 높은 보수를 챙겨 왔다.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158402].flavor
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The streets of the City are never short of vile and savage company after dark. Rats desperate to turn their lives around, denizens of the Backstreets harboring dreams of revenge, Syndicates and Fingers embroiled in struggles over their interests... and, of course, the Sweepers.\n\nFor all the fortunes to be made from working after sundown, few Fixers are eager to accept such contracts. There are, however, those who find their greatest opportunities precisely where others dare not tread.\n\nThe discernment to read any situation with remarkable precision. The swiftness and thoroughness to bring a job to its conclusion without inviting further trouble. With these two qualities as its greatest assets, Wedge Office has weathered every contract and walked away with the handsome compensation that follows.
   PL:
529. [[walpu10] Pasywka wroga [158501] — nazwa] 쐐기 박기
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158501].name
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [[walpu10] Pasywka wroga [158501] — opis] 합 시작 시 [WalpuTenBattleFieldKnow] 1 얻음 (턴당 1회)\n\n관통 스킬로 마지막 코인 적중 시 메인 타겟에게 [WalpuTenWedgeMarkSilver] 1 부여 (스킬당 1회)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158501].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WalpuTenBattleFieldKnow], [WalpuTenWedgeMarkSilver]
   znaczenie tagów: [WalpuTenBattleFieldKnow] = 전장 파악 / Field Analysis; [WalpuTenWedgeMarkSilver] = 은색 표식[쐐기] / Silver Mark [Wedge]
   EN: Clash Start: Gain 1 [WalpuTenBattleFieldKnow] (once per turn)\n\nOn Pierce Skill final Coin Hit, inflict 1 [WalpuTenWedgeMarkSilver] on the main target (once per Skill)
   PL:
531. [[walpu10] Pasywka wroga [158502] — nazwa] 도시의 사냥꾼
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158502].name
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [[walpu10] Pasywka wroga [158502] — opis] 스테이지 첫 등장시, 정신력 45 회복\n\n턴 종료 시 자신의 [Breath] 위력이 10 이상이면, 다음 턴에 [Agility] 1 얻음\n\n자신의 [Breath] 위력이 20을 초과했으면, 기본 스킬로 가하는 크리티컬 피해량 +(초과한 수치)% (최대 25%)
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158502].desc
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [[walpu10] Pasywka wroga [158502] — tekst klimatyczny] 도시의 밤거리는 언제나 비열하고 야만적인 것들로 우글거린다.\n인생 역전을 노리는 쥐들부터 복수를 꿈꾸는 뒷골목 주민, 이권을 다투는 조직들과 손가락 그리고 청소부까지.\n그렇기에 밤에 이루어지는 의뢰는 대개 보수가 높음에도 인기가 없다.\n하지만 그런 심야의 의뢰를 기회로 여기는 자들도 있다.\n뛰어난 상황 판단 능력과 우환을 남기지 않는 신속하고 빈틈없는 마무리.\n그 두 가지를 무기로 쐐기 사무소는 매번 살아남아 높은 보수를 챙겨 왔다.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158502].flavor
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [[walpu10] Pasywka wroga [158601] — nazwa] 스티그마 공방 무기
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158601].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [[walpu10] Pasywka wroga [158601] — opis] 자신의 스킬로 [Combustion]을 부여할 때, 부여하는 [Combustion] 위력 및 횟수 수치 +1\n- 자신의 스킬이 적중한 적의 [Combustion] 횟수가 3 미만이면, 대상의 [Combustion] 횟수 1 증가
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158601].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [[walpu10] Pasywka wroga [158602] — nazwa] 격정
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158602].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [[walpu10] Pasywka wroga [158602] — opis] <color=#ff6000><mark color=#ff000040><b><u>자신의 정신력이 20/40 이상이면</color></mark></b></u>, 코인 위력이 1/2씩 증가\n\n<color=#ff6000><mark color=#ff000040><b><u>체력이 50% 이하면</color></mark></b></u>, 최종 위력 +1
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: <color=#ff6000><mark color=#ff000040><b><u>At 20+/40+ SP,</color></mark></b></u> Coin Power +1/+2\n\n<color=#ff6000><mark color=#ff000040><b><u>At 50%- HP,</color></mark></b></u> Final Power +1
   PL:
538. [[walpu10] Pasywka wroga [158603] — nazwa] 새벽 사무소 - 신입
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158603].name
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [[walpu10] Pasywka wroga [158603] — opis] 스테이지 첫 등장시, 정신력 45 회복\n[Combustion] 효과로 받는 피해량 -40% (소수점 버림)\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨\n\n체력이 10이 되면…
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158603].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [PanicChangeLock]
   znaczenie tagów: [Combustion] = 화상 / Burn; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Upon entering the Encounter for the first time, heal 45 SP\nTake -40% damage from [Combustion] (rounded down)\n\nApply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, change SP to 45\n\nAt 10 HP...
   PL:
540. [[walpu10] Pasywka wroga [158701] — nazwa] 격정
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158701].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [[walpu10] Pasywka wroga [158701] — opis] 턴 종료시 흐트러짐 상태가 아니라면 모든 적에게 [Combustion] 2 부여\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 정신력이 20/40/45 이상이면</color></mark></b></u>, 최종 위력이 1/2/3씩 증가\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 체력이 50% 이하면</color></mark></b></u>, 최종 위력 +1
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158701].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn End: If this unit is not Staggered, inflict 2 [Combustion] on all enemies\n\n<color=#ff6000><mark color=#ff000040><b><u>At 20+/40+/45+ SP,</color></mark></b></u> Final Power +1/+2/+3\n\n<color=#ff6000><mark color=#ff000040><b><u>At 50%- HP,</color></mark></b></u> Final Power +1
   PL:
542. [[walpu10] Pasywka wroga [158702] — nazwa] 불안정한 자아의 껍질
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158702].name
   limit: do 40 znaków
   EN: Unstable Shell of Ego
   PL:
543. [[walpu10] Pasywka wroga [158702] — opis] 피격 시 공격자에게 [Combustion]을 부여하는 [PhilipShield] 상태와 공격 적중 시 대상에게 [Combustion]을 부여하는 [PhilipSword] 상태가 반복됨\n\n[PhilipReady]가 0이면, ‘타오르는 일격’을 사용함\n- 해당 턴 종료 후 다음 턴에 다시 [PhilipReady] 4 얻음
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158702].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [PhilipShield], [PhilipSword], [PhilipReady], [TabExplain]
   znaczenie tagów: [Combustion] = 화상 / Burn; [PhilipShield] = 깃털 방패 / Feather Shield; [PhilipSword] = 이글거리는 검 / Searing Sword; [PhilipReady] = 타오르는 일격 준비 / Readying Blazing Strike
   EN: Regularly shifts between [PhilipShield] and [PhilipSword] modes, inflicting [Combustion] after taking hits and upon attacking, respectively.\n\nAt 0 [PhilipReady], use "Blazing[TabExplain] Strike"\n- Gain 4 [PhilipReady] again next turn after the end of the turn this unit used "Blazing[TabExplain] Strike"
   PL:
544. [[walpu10] Pasywka wroga [158703] — nazwa] 불안정 개화 E.G.O::밀랍날개
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158703].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [[walpu10] Pasywka wroga [158703] — opis] 스테이지 첫 등장시 정신력 45로 시작하고, [PhilipPower] 얻음\n\n[Combustion] 효과로 받는 피해량 -50% (소수점 버림)\n- 체력이 50% 미만이면, 효과가 강화 되어, [Combustion] 효과로 받는 피해량 -75%\n\n[PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158703].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [PhilipPower], [Combustion], [PanicChangeLock]
   znaczenie tagów: [PhilipPower] = 슬픔과 함께 일어설 수 있는 길 / Getting Back on One's Feet Amid Sadness; [Combustion] = 화상 / Burn; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Upon entering the Encounter for the first time, enter with 45 SP and gain [PhilipPower]\n\nTake -50% damage from [Combustion] (rounded down)\n- At lower than 50% HP, this effect is enhanced and this unit takes -75% damage from [Combustion]\n\nApply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 45
   PL:
546. [[walpu10] Pasywka wroga [158703] — tekst klimatyczny] 날아오를 하늘을 아직 정하지 못한 어중간한 날개.
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158703].flavor
   limit: do 120 znaków
   EN: Half-formed wings, yet to choose the skies in which they shall soar.
   PL:
547. [[walpu10] Pasywka wroga [158704] — nazwa] 정해진 결말
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158704].name
   limit: do 40 znaków
   EN: The Conclusion Prewritten
   PL:
548. [[walpu10] Pasywka wroga [158704] — opis] 체력이 10이 되면…
   źródło: Passives_Abnormality-walpu10.json :: dataList[id=158704].desc
   limit: do 120 znaków
   EN: At 10 HP...
   PL:

## [walpu2] Wróg / część: Enemies-walpu2
- plik gry: `Enemies-walpu2.json`

549. [[walpu2] Wróg / część [8147] — nazwa] 녹빛 여명 - 의문 - α
   źródło: Enemies-walpu2.json :: dataList[id=8147].name
   limit: do 40 znaków
   EN: Dawn of Green - Doubt - α
   PL:
550. [[walpu2] Wróg / część [8147] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=8147].desc
   limit: do 120 znaków
   EN: Enemy Unit
   PL:
551. [[walpu2] Wróg / część [8148] — nazwa] 녹빛 여명 - 의문 - β
   źródło: Enemies-walpu2.json :: dataList[id=8148].name
   limit: do 40 znaków
   EN: Dawn of Green - Doubt - β
   PL:
552. [[walpu2] Wróg / część [8148] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=8148].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [[walpu2] Wróg / część [8149] — nazwa] 녹빛 여명 - 의문 - γ
   źródło: Enemies-walpu2.json :: dataList[id=8149].name
   limit: do 40 znaków
   EN: Dawn of Green - Doubt - γ
   PL:
554. [[walpu2] Wróg / część [8149] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=8149].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [[walpu2] Wróg / część [8150] — nazwa] 녹빛 여명 - 의문 - δ
   źródło: Enemies-walpu2.json :: dataList[id=8150].name
   limit: do 40 znaków
   EN: Dawn of Green - Doubt - δ
   PL:
556. [[walpu2] Wróg / część [8150] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=8150].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [[walpu2] Wróg / część [814701] — nazwa] 몸통
   źródło: Enemies-walpu2.json :: dataList[id=814701].name
   limit: do 40 znaków
   EN: Body
   PL:
558. [[walpu2] Wróg / część [814701] — opis] 부위
   źródło: Enemies-walpu2.json :: dataList[id=814701].desc
   limit: do 120 znaków
   EN: Part
   PL:
559. [[walpu2] Wróg / część [814801] — nazwa] 몸통
   źródło: Enemies-walpu2.json :: dataList[id=814801].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [[walpu2] Wróg / część [814801] — opis] 부위
   źródło: Enemies-walpu2.json :: dataList[id=814801].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [[walpu2] Wróg / część [814901] — nazwa] 몸통
   źródło: Enemies-walpu2.json :: dataList[id=814901].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [[walpu2] Wróg / część [814901] — opis] 부위
   źródło: Enemies-walpu2.json :: dataList[id=814901].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [[walpu2] Wróg / część [815001] — nazwa] 몸통
   źródło: Enemies-walpu2.json :: dataList[id=815001].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [[walpu2] Wróg / część [815001] — opis] 부위
   źródło: Enemies-walpu2.json :: dataList[id=815001].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [[walpu2] Wróg / część [90106] — nazwa] 녹빛 여명 - 의문 - α
   źródło: Enemies-walpu2.json :: dataList[id=90106].name
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [[walpu2] Wróg / część [90106] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=90106].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [[walpu2] Wróg / część [90107] — nazwa] 녹빛 여명 - 의문 - β
   źródło: Enemies-walpu2.json :: dataList[id=90107].name
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [[walpu2] Wróg / część [90107] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=90107].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [[walpu2] Wróg / część [90108] — nazwa] 녹빛 여명 - 의문 - γ
   źródło: Enemies-walpu2.json :: dataList[id=90108].name
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [[walpu2] Wróg / część [90108] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=90108].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [[walpu2] Wróg / część [90109] — nazwa] 녹빛 여명 - 의문 - δ
   źródło: Enemies-walpu2.json :: dataList[id=90109].name
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [[walpu2] Wróg / część [90109] — opis] 적 잡몹
   źródło: Enemies-walpu2.json :: dataList[id=90109].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu2] Umiejętności wrogów / Anomalii — Skills_Enemy-walpu2
- grupa rozdziału/trybu: `walpu2` · plik: `Skills_Enemy-walpu2.json`

573. [Umiejętność wroga [814701] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814701].levelList[level=1].name
   limit: do 40 znaków
   EN: Stab
   PL:
574. [Umiejętność wroga [814701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여. 대상에게 출혈이 있으면 출혈 횟수 1 추가 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed. If target has Bleed, inflict +1 Bleed Count
   PL:
575. [Umiejętność wroga [814702] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814702].levelList[level=1].name
   limit: do 40 znaków
   EN: Pin Down
   PL:
576. [Umiejętność wroga [814702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed Count
   PL:
577. [Umiejętność wroga [814702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
578. [Umiejętność wroga [814703] (ulepszenie 1) — nazwa] 고통
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814703].levelList[level=1].name
   limit: do 40 znaków
   EN: Pain
   PL:
579. [Umiejętność wroga [814703] (ulepszenie 1) — opis] 출혈이 있는 대상 우선 공격
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814703].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes enemies with Bleed
   PL:
580. [Umiejętność wroga [814703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 10%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, deal 10% of damage dealt as bonus damage
   PL:
581. [Umiejętność wroga [814703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 10%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [814703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈만큼 출혈 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Bleed by Bleed on target
   PL:
583. [Umiejętność wroga [814704] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814704].levelList[level=1].name
   limit: do 40 znaków
   EN: Defend
   PL:
584. [Umiejętność wroga [814704] (ulepszenie 1) — opis] 보호막 체력이 있을 때, 피격 시 다음 턴에 출혈 2 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814704].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this unit has Shield HP, inflict 2 Bleed next turn On Hit
   PL:
585. [Umiejętność wroga [814801] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814801].levelList[level=1].name
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [814801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여. 대상에게 출혈이 있으면 출혈 횟수 2 추가 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed. If target has Bleed, inflict +2 Bleed Count
   PL:
587. [Umiejętność wroga [814802] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814802].levelList[level=1].name
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność wroga [814802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność wroga [814802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed
   PL:
590. [Umiejętność wroga [814803] (ulepszenie 1) — nazwa] 고통
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].name
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [814803] (ulepszenie 1) — opis] 출혈이 있는 대상 우선 공격\n자신의 공격으로 대상을 처치했다면, 정신력이 가장 낮은 적 정신력 10 감소.
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritizes targets with Bleed\nWhen this unit defeats the target with an attack, enemy with the lowest SP loses 10 SP.
   PL:
592. [Umiejętność wroga [814803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 10%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [814803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 대상의 출혈만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Target loses (Bleed on target) SP
   PL:
594. [Umiejętność wroga [814803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 10%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [814803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 대상의 출혈만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność wroga [814803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈만큼 출혈 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność wroga [814804] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814804].levelList[level=1].name
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [814901] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814901].levelList[level=1].name
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [814901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여. 대상에게 출혈이 있으면 출혈 횟수 2 추가 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [814902] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814902].levelList[level=1].name
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [814902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL:
602. [Umiejętność wroga [814902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [814903] (ulepszenie 1) — nazwa] 고통
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].name
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność wroga [814903] (ulepszenie 1) — opis] 출혈이 있는 대상 우선 공격\n자신의 공격으로 대상을 처치했다면, 정신력이 가장 낮은 적 정신력 10 감소.\n자신의 공격으로 대상을 처치했다면, 다른 대상에게 재사용.
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritizes targets with Bleed\nWhen this unit defeats the target with an attack, enemy with the lowest SP loses 10 SP.\nWhen this unit defeats the target with an attack, reuse Skill on a different target.
   PL:
605. [Umiejętność wroga [814903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, deal 20% of damage dealt as bonus damage
   PL:
606. [Umiejętność wroga [814903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 출혈만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses (Bleed on target) SP
   PL:
607. [Umiejętność wroga [814903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [814903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 출혈만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [814903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈만큼 출혈 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność wroga [814903] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 출혈이 10 이상이라면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814903].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 10+ Bleed, Reuse this Coin once
   PL:
611. [Umiejętność wroga [814904] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-walpu2.json :: dataList[id=814904].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL:
612. [Umiejętność wroga [815001] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815001].levelList[level=1].name
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [815001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여. 대상에게 출혈이 있으면 출혈 횟수 2 추가 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed. If target has Bleed, inflict +2 Bleed Count
   PL:
614. [Umiejętność wroga [815001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 횟수 2 증가
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Bleed Count
   PL:
615. [Umiejętność wroga [815001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
616. [Umiejętność wroga [815001] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 출혈 횟수 2 증가
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [815002] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815002].levelList[level=1].name
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [815002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 601 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [815002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [815002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [815003] (ulepszenie 1) — nazwa] 고통
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].name
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [815003] (ulepszenie 1) — opis] 출혈이 있는 대상 우선 공격\n자신의 공격으로 대상을 처치했다면, 정신력이 가장 낮은 적 정신력 15 감소.\n자신의 공격으로 대상을 처치했다면, 다른 대상에게 재사용.
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritizes targets with Bleed\nWhen this unit defeats the target with an attack, enemy with the lowest SP loses 15 SP.\nWhen this unit defeats the target with an attack, reuse Skill on a different target.
   PL:
623. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] (대상의 출혈/2)만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses (Bleed on target/2) SP
   PL:
625. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] (대상의 출혈/2)만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈이 있다면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] (대상의 출혈/2)만큼 정신력 피해
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈만큼 출혈 부여
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [815003] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 출혈이 7 이상이라면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815003].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 7+ Bleed, Reuse this Coin once
   PL:
631. [Umiejętność wroga [815004] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-walpu2.json :: dataList[id=815004].levelList[level=1].name
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu4] Wróg / część: Enemies-walpu4
- plik gry: `Enemies-walpu4.json`

632. [[walpu4] Wróg / część [8363] — nazwa] 이해의 과실
   źródło: Enemies-walpu4.json :: dataList[id=8363].name
   limit: do 40 znaków
   EN: Fruit of Understanding
   PL:
633. [[walpu4] Wróg / część [8363] — opis] 적 잡몹
   źródło: Enemies-walpu4.json :: dataList[id=8363].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [[walpu4] Wróg / część [8364] — nazwa] 이해의 과실
   źródło: Enemies-walpu4.json :: dataList[id=8364].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [[walpu4] Wróg / część [8364] — opis] 적 잡몹
   źródło: Enemies-walpu4.json :: dataList[id=8364].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [[walpu4] Wróg / część [8365] — nazwa] 이해의 과실
   źródło: Enemies-walpu4.json :: dataList[id=8365].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [[walpu4] Wróg / część [8365] — opis] 적 잡몹
   źródło: Enemies-walpu4.json :: dataList[id=8365].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [[walpu4] Wróg / część [8366] — nazwa] 사랑을 주소서
   źródło: Enemies-walpu4.json :: dataList[id=8366].name
   limit: do 40 znaków
   EN: Grant Us Love
   PL:
639. [[walpu4] Wróg / część [8366] — opis] 적 잡몹
   źródło: Enemies-walpu4.json :: dataList[id=8366].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [[walpu4] Wróg / część [836602] — nazwa] 왼팔
   źródło: Enemies-walpu4.json :: dataList[id=836602].name
   limit: do 40 znaków
   EN: Left Arm
   PL:
641. [[walpu4] Wróg / część [836602] — opis] 적 잡몹
   źródło: Enemies-walpu4.json :: dataList[id=836602].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [[walpu4] Wróg / część [836603] — nazwa] 오른팔
   źródło: Enemies-walpu4.json :: dataList[id=836603].name
   limit: do 40 znaków
   EN: Right Arm
   PL:
643. [[walpu4] Wróg / część [836603] — opis] 적 잡몹
   źródło: Enemies-walpu4.json :: dataList[id=836603].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu4] Umiejętności wrogów / Anomalii — Skills_Abnormality-walpu4
- grupa rozdziału/trybu: `walpu4` · plik: `Skills_Abnormality-walpu4.json`

644. [Umiejętność wroga [836301] (ulepszenie 1) — nazwa] 이해
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836301].levelList[level=1].name
   limit: do 40 znaków
   EN: Understanding
   PL:
645. [Umiejętność wroga [836301] (ulepszenie 1) — opis] 대상의 정신력이 10 이하면 합 위력 +1\n[WhenUse] [VioletUnderstand] 1 얻음
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [VioletUnderstand]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [VioletUnderstand] = 이해 / Understanding
   EN: If target has 10- SP, Clash Power +1\n[WhenUse] Gain 1 [VioletUnderstand]
   PL:
646. [Umiejętność wroga [836301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MentalCrack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MentalCrack] = 정신 균열 / Mental Fracture
   EN: [OnSucceedAttack] Inflict 1 [MentalCrack]
   PL:
647. [Umiejętność wroga [836302] (ulepszenie 1) — nazwa] 인지
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836302].levelList[level=1].name
   limit: do 40 znaków
   EN: Perception
   PL:
648. [Umiejętność wroga [836302] (ulepszenie 1) — opis] 대상의 정신력이 10 이하면 합 위력 +1\n[WhenUse] [VioletUnderstand] 2 얻음
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [VioletUnderstand]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [VioletUnderstand] = 이해 / Understanding
   EN: If target has 10- SP, Clash Power +1\n[WhenUse] Gain 2 [VioletUnderstand]
   PL:
649. [Umiejętność wroga [836302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VioletTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VioletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VioletTakeDamageUp] = 질투 취약 / Envy Fragility
   EN: [OnSucceedAttack] Inflict 1 [VioletTakeDamageUp]
   PL:
650. [Umiejętność wroga [836302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność wroga [836303] (ulepszenie 1) — nazwa] 구원
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836303].levelList[level=1].name
   limit: do 40 znaków
   EN: Salvation
   PL:
652. [Umiejętność wroga [836303] (ulepszenie 1) — opis] 대상의 정신력이 10 이하면 합 위력 +1\n[WhenUse] [VioletUnderstand] 1 얻음
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836303].levelList[level=1].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [836303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VioletTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Umiejętność wroga [836303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [836304] (ulepszenie 1) — nazwa] 이해 불능
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836304].levelList[level=1].name
   limit: do 40 znaków
   EN: What is Incomprehensible
   PL:
656. [Umiejętność wroga [836304] (ulepszenie 1) — opis] [WhenUse] [VioletUnderstand] 2 얻음
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [VioletUnderstand]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [VioletUnderstand] = 이해 / Understanding
   EN: [WhenUse] Gain 2 [VioletUnderstand]
   PL:
657. [Umiejętność wroga [836305] (ulepszenie 1) — nazwa] 붕괴
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836305].levelList[level=1].name
   limit: do 40 znaków
   EN: Decay
   PL:
658. [Umiejętność wroga [836305] (ulepszenie 1) — opis] [CantDuel]\n[EndSkill] 사망
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\n[EndSkill] Dies
   PL:
659. [Umiejętność wroga [836305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [VioletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VioletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VioletTakeDamageUp] = 질투 취약 / Envy Fragility
   EN: [OnSucceedAttack] Inflict 2 [VioletTakeDamageUp] next turn
   PL:
660. [Umiejętność wroga [836305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 피해를 10 ~ 14 입힘
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10~14 SP damage
   PL:
661. [Umiejętność wroga [836601] (ulepszenie 1) — nazwa] 자비
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836601].levelList[level=1].name
   limit: do 40 znaków
   EN: Mercy
   PL:
662. [Umiejętność wroga [836601] (ulepszenie 1) — opis] 대상의 정신력이 20 이하면 합 위력 +1
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836601].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has 20- SP, Clash Power +1
   PL:
663. [Umiejętność wroga [836601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VioletTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność wroga [836601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność wroga [836602] (ulepszenie 1) — nazwa] 사랑
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836602].levelList[level=1].name
   limit: do 40 znaków
   EN: Love
   PL:
666. [Umiejętność wroga [836602] (ulepszenie 1) — opis] 대상의 정신력이 20 이하면 합 위력 +1
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836602].levelList[level=1].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność wroga [836602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VioletTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność wroga [836602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność wroga [836603] (ulepszenie 1) — nazwa] 점멸하는 이해의 문자
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836603].levelList[level=1].name
   limit: do 50 znaków
   EN: Flickering Glyphs of Understanding
   PL:
670. [Umiejętność wroga [836603] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]
   PL:
671. [Umiejętność wroga [836603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [836603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność wroga [836604] (ulepszenie 1) — nazwa] 점멸하는 이해의 문자
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836604].levelList[level=1].name
   (powtórzenie elementu 669 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność wroga [836604] (ulepszenie 1) — opis] 대상의 정신력이 20 이하면 합 위력 +1
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836604].levelList[level=1].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność wroga [836604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VioletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VioletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VioletTakeDamageUp] = 질투 취약 / Envy Fragility
   EN: [OnSucceedAttack] Inflict 2 [VioletTakeDamageUp]
   PL:
676. [Umiejętność wroga [836604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 1 부여
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [836605] (ulepszenie 1) — nazwa] 이해 불능
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836605].levelList[level=1].name
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Umiejętność wroga [836605] (ulepszenie 1) — opis] [WhenUse] [Protection] 2 얻음
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [WhenUse] Gain 2 [Protection]
   PL:
679. [Umiejętność wroga [836606] (ulepszenie 1) — nazwa] 쇄도하는 안식의 팔
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836606].levelList[level=1].name
   limit: do 40 znaków
   EN: Rushing Arms of Rest
   PL:
680. [Umiejętność wroga [836606] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836606].levelList[level=1].desc
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [836606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 100 피해
   źródło: Skills_Abnormality-walpu4.json :: dataList[id=836606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 100 HP damage
   PL:

## [walpu4] Pasywka wroga: Passives_Abnormality-walpu4
- plik gry: `Passives_Abnormality-walpu4.json`

682. [[walpu4] Pasywka wroga [836301] — nazwa] BLACK 피해
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836301].name
   limit: do 40 znaków
   EN: BLACK Damage
   PL:
683. [[walpu4] Pasywka wroga [836301] — opis] 이 유닛이 피해를 입힐 때, 정신력 1 ~ 3 피해
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836301].desc
   limit: do 120 znaków
   EN: When this unit deals damage, it also deals 1~3 SP damage
   PL:
684. [[walpu4] Pasywka wroga [836401] — nazwa] 이해의 과실
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836401].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [[walpu4] Pasywka wroga [836401] — opis] 이 유닛은 일정 턴 뒤에 자멸함
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836401].desc
   limit: do 120 znaków
   EN: This unit self-terminates after a certain number of turns passes
   PL:
686. [[walpu4] Pasywka wroga [836402] — nazwa] 이해의 과실
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836402].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [[walpu4] Pasywka wroga [836402] — opis] 이 유닛은 일정 턴 뒤에 자멸함
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836402].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [[walpu4] Pasywka wroga [836403] — nazwa] 이해의 과실
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836403].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [[walpu4] Pasywka wroga [836403] — opis] 이 유닛은 일정 턴 뒤에 자멸함
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836403].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [[walpu4] Pasywka wroga [836601] — nazwa] 침식
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836601].name
   limit: do 40 znaków
   EN: Corrosion
   PL:
691. [[walpu4] Pasywka wroga [836601] — opis] 턴 종료 시, 모든 적에게 3의 피해를 입힘
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836601].desc
   limit: do 120 znaków
   EN: Turn End: Deal 3 damage to all enemies
   PL:
692. [[walpu4] Pasywka wroga [836302] — nazwa] 붕괴 임박
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836302].name
   limit: do 40 znaków
   EN: Imminent Decay
   PL:
693. [[walpu4] Pasywka wroga [836302] — opis] 이 유닛은 일정 턴 뒤에 자멸함
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836302].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [[walpu4] Pasywka wroga [836602] — nazwa] 팔 부위 패시브
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836602].name
   limit: do 40 znaków
   EN: Passive for the Arm Part
   PL:
695. [[walpu4] Pasywka wroga [836602] — opis] 팔 부위 파괴 시 특정 스킬 사용 불가
   źródło: Passives_Abnormality-walpu4.json :: dataList[id=836602].desc
   limit: do 120 znaków
   EN: Break the Arm to disable certain Skills
   PL:

## [walpu5] Wróg / część: Enemies-walpu5
- plik gry: `Enemies-walpu5.json`

696. [[walpu5] Wróg / część [90178] — nazwa] 위협적인 톱니 신도
   źródło: Enemies-walpu5.json :: dataList[id=90178].name
   limit: do 40 znaków
   EN: Threatening Gear Worshipper
   PL:
697. [[walpu5] Wróg / część [90178] — opis] 적 잡몹
   źródło: Enemies-walpu5.json :: dataList[id=90178].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [[walpu5] Wróg / część [90179] — nazwa] 기민한 톱니 신도
   źródło: Enemies-walpu5.json :: dataList[id=90179].name
   limit: do 40 znaków
   EN: Nimble Gear Worshipper
   PL:
699. [[walpu5] Wróg / część [90179] — opis] 적 잡몹
   źródło: Enemies-walpu5.json :: dataList[id=90179].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [[walpu5] Wróg / część [90180] — nazwa] 저돌적인 톱니 광신도
   źródło: Enemies-walpu5.json :: dataList[id=90180].name
   limit: do 40 znaków
   EN: Aggressive Gear Fanatic
   PL:
701. [[walpu5] Wróg / część [90180] — opis] 적 잡몹
   źródło: Enemies-walpu5.json :: dataList[id=90180].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu5] Umiejętności wrogów / Anomalii — Skills_Enemy-walpu5
- grupa rozdziału/trybu: `walpu5` · plik: `Skills_Enemy-walpu5.json`

702. [Umiejętność wroga [9017801] (ulepszenie 1) — nazwa] 톱니가 이끄는 대로
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017801].levelList[level=1].name
   limit: do 40 znaków
   EN: Guidance of the Gears
   PL:
703. [Umiejętność wroga [9017801] (ulepszenie 1) — opis] [WhenUse] [Smoke] 2 얻음
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Smoke]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Smoke] = 연기 / Smoke
   EN: [WhenUse] Gain 2 [Smoke]
   PL:
704. [Umiejętność wroga [9017801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Smoke] 횟수 1 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Gain +1 [Smoke] Count
   PL:
705. [Umiejętność wroga [9017802] (ulepszenie 1) — nazwa] 고기 톱니: 멈추기
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017802].levelList[level=1].name
   limit: do 40 znaków
   EN: Meat Gear: Stop
   PL:
706. [Umiejętność wroga [9017802] (ulepszenie 1) — opis] [WhenUse] [Smoke] 4 얻음, 자신의 [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Smoke]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Smoke] = 연기 / Smoke
   EN: [WhenUse] Gain 4 [Smoke] and +2 [Smoke] Count
   PL:
707. [Umiejętność wroga [9017802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 2 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Inflict 2 [Smoke]
   PL:
708. [Umiejętność wroga [9017802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 1 [Paralysis] next turn
   PL:
709. [Umiejętność wroga [9017802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Smoke] 2 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [9017802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 708 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [9017803] (ulepszenie 1) — nazwa] 증기
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017803].levelList[level=1].name
   limit: do 40 znaków
   EN: Vapour
   PL:
712. [Umiejętność wroga [9017803] (ulepszenie 1) — opis] 대상의 [Smoke] 3당, 합 위력 +1 (최대 2)\n자신의 [Smoke] 3당, 피해량 +10% (최대 20%)\n[WhenUse] 자신의 [Smoke]가 10이면, 코인 위력 +2\n[EndSkill] 자신의 [Smoke] 전부 소모
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017803].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Smoke], [WhenUse], [EndSkill]
   znaczenie tagów: [Smoke] = 연기 / Smoke; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Clash Power +1 for every 3 [Smoke] on the target (max 2)\nDeal +10% damage for every 3 [Smoke] on self (max 20%)\n[WhenUse] At 10 [Smoke], Coin Power +2\n[EndSkill] Consume all [Smoke] on self
   PL:
713. [Umiejętność wroga [9017803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 3 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Inflict 3 [Smoke]
   PL:
714. [Umiejętność wroga [9017803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Smoke] 3 당, 코인 재사용 (최대 3회 발동)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Reuse Coin for every 3 [Smoke] on the target (3 times max)
   PL:
715. [Umiejętność wroga [9017804] (ulepszenie 1) — nazwa] 회피 명령
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017804].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade Order
   PL:
716. [Umiejętność wroga [9017804] (ulepszenie 1) — opis] [OnSucceedEvade] [Smoke] 3 얻음, [Smoke] 횟수 1 증가\n[OnSucceedEvade] 자신의 [Smoke]가 10이면, 다음 턴에 [ParryingResultUp] 1, [Protection] 3 얻음 (턴 당 1회)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017804].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Smoke], [ParryingResultUp], [Protection]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Smoke] = 연기 / Smoke; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [Protection] = 보호 / Protection
   EN: [OnSucceedEvade] Gain 3 [Smoke] and +1 [Smoke] Count\n[OnSucceedEvade] At 10 [Smoke], gain 1 [ParryingResultUp] and 3 [Protection] next turn (once per turn)
   PL:
717. [Umiejętność wroga [9017901] (ulepszenie 1) — nazwa] 톱니를 따라
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017901].levelList[level=1].name
   limit: do 40 znaków
   EN: Guided by Gears
   PL:
718. [Umiejętność wroga [9017901] (ulepszenie 1) — opis] [WhenUse] [Smoke] 2 얻음.
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Smoke]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Smoke] = 연기 / Smoke
   EN: [WhenUse] Gain 2 [Smoke]
   PL:
719. [Umiejętność wroga [9017901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Smoke] 횟수 1 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 704 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [9017902] (ulepszenie 1) — nazwa] 고기 톱니: 부여잡기
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017902].levelList[level=1].name
   limit: do 40 znaków
   EN: Meat Gear: Grapple
   PL:
721. [Umiejętność wroga [9017902] (ulepszenie 1) — opis] [WhenUse] [Smoke] 4 얻음, 자신의 [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017902].levelList[level=1].desc
   (powtórzenie elementu 706 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [9017902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 횟수 1 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Inflict +1 [Smoke] Count
   PL:
723. [Umiejętność wroga [9017902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 1 [Binding] next turn
   PL:
724. [Umiejętność wroga [9017902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Smoke] 횟수 1 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [9017902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność wroga [9017903] (ulepszenie 1) — nazwa] 기습 명령
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017903].levelList[level=1].name
   limit: do 40 znaków
   EN: Assault Order
   PL:
727. [Umiejętność wroga [9017903] (ulepszenie 1) — opis] 대상의 [Smoke] 3당, 합 위력 +1 (최대 2)\n자신의 [Smoke] 3당, 피해량 +10% (최대 20%)\n[WhenUse] 자신의 [Smoke]가 10이면, 코인 위력 +2\n[EndSkill] 자신의 [Smoke] 전부 소모
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017903].levelList[level=1].desc
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [9017903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Inflict +2 [Smoke] Count
   PL:
729. [Umiejętność wroga [9017903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Smoke] 3 당, 코인 재사용 (최대 3회 발동)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 714 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [9017904] (ulepszenie 1) — nazwa] 회피 명령
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017904].levelList[level=1].name
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [9017904] (ulepszenie 1) — opis] [OnSucceedEvade] [Smoke] 3 얻음, [Smoke] 횟수 1 증가\n[OnSucceedEvade] 자신의 [Smoke]가 10이면, 다음 턴에 [ParryingResultUp] 1, [Protection] 3 얻음 (턴 당 1회)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9017904].levelList[level=1].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [9018001] (ulepszenie 1) — nazwa] 고기 톱니: 명령
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018001].levelList[level=1].name
   limit: do 40 znaków
   EN: Meat Gear: Command
   PL:
733. [Umiejętność wroga [9018001] (ulepszenie 1) — opis] [WhenUse] [Smoke] 3 얻음, 자신의 [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Smoke]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Smoke] = 연기 / Smoke
   EN: [WhenUse] Gain 3 [Smoke] and +2 [Smoke] Count
   PL:
734. [Umiejętność wroga [9018001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 3 부여, [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Inflict 3 [Smoke] and +2 [Smoke] Count
   PL:
735. [Umiejętność wroga [9018002] (ulepszenie 1) — nazwa] 생각 톱니: 수급
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018002].levelList[level=1].name
   limit: do 40 znaków
   EN: Thought Gear: Collect
   PL:
736. [Umiejętność wroga [9018002] (ulepszenie 1) — opis] [WhenUse] [Smoke] 4 얻음, 자신의 [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018002].levelList[level=1].desc
   (powtórzenie elementu 706 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [9018002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 4 부여, [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Inflict 4 [Smoke] and +2 [Smoke] Count
   PL:
738. [Umiejętność wroga [9018002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 708 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność wroga [9018003] (ulepszenie 1) — nazwa] 고기 톱니: 제한
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018003].levelList[level=1].name
   limit: do 40 znaków
   EN: Meat Gear: Restrict
   PL:
740. [Umiejętność wroga [9018003] (ulepszenie 1) — opis] 대상의 [Smoke] 3당, 코인 위력 +1\n자신의 [Smoke] 3당, 피해량 +10%\n이 스킬에서 코인 재사용 시 자신의 [Smoke] 3 소모\n[WhenUse] 자신의 [Smoke]가 10이면, 코인 위력 +1
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018003].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Smoke], [WhenUse]
   znaczenie tagów: [Smoke] = 연기 / Smoke; [WhenUse] = [사용시] / [On Use]
   EN: Coin Power +1 for every 3 [Smoke] on the target\nDeal +10% damage for every 3 [Smoke] on self\nConsume 3 [Smoke] on self every time this Skill Reuses Coin\n[WhenUse] At 10 [Smoke], Coin Power +1
   PL:
741. [Umiejętność wroga [9018003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 횟수 1 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [9018003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Smoke] 5 당, 코인 재사용 (최대 2회 발동)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Smoke]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Smoke] = 연기 / Smoke
   EN: [OnSucceedAttack] Reuse Coin for every 5 [Smoke] on the target (2 times max)
   PL:
743. [Umiejętność wroga [9018004] (ulepszenie 1) — nazwa] 생각 톱니: 해제
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018004].levelList[level=1].name
   limit: do 40 znaków
   EN: Thought Gear: Remove
   PL:
744. [Umiejętność wroga [9018004] (ulepszenie 1) — opis] 대상의 [Smoke] 3당, 합 위력 +1\n자신의 [Smoke] 3당, 피해량 +20%\n[WhenUse] 자신의 [Smoke]가 10이면, 코인 위력 +2\n[EndSkill] 자신의 [Smoke] 전부 소모
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018004].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Smoke], [WhenUse], [EndSkill]
   znaczenie tagów: [Smoke] = 연기 / Smoke; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Clash Power +1 for every 3 [Smoke] on the target\nDeal +20% damage for every 3 [Smoke] on self\n[WhenUse] At 10 [Smoke], Coin Power +2\n[EndSkill] Consume all [Smoke] on self
   PL:
745. [Umiejętność wroga [9018004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Smoke] 3 부여
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 713 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Umiejętność wroga [9018004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Smoke] 횟수 2 증가
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność wroga [9018004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Smoke] 3 당, 코인 재사용 (최대 3회 발동)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 714 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Umiejętność wroga [9018005] (ulepszenie 1) — nazwa] 생각 톱니: 증기
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018005].levelList[level=1].name
   limit: do 40 znaków
   EN: Thought Gear: Vapour
   PL:
749. [Umiejętność wroga [9018005] (ulepszenie 1) — opis] [WhenUse] [Smoke] 5 얻음, [Smoke] 횟수 2 증가\n[WhenUse] 자신의 [Smoke]가 10이면, 다음 턴에 [PlusCoinValueUp] 2, [Protection] 3 얻음 (턴 당 1회)
   źródło: Skills_Enemy-walpu5.json :: dataList[id=9018005].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Smoke], [PlusCoinValueUp], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Smoke] = 연기 / Smoke; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [Protection] = 보호 / Protection
   EN: [WhenUse] Gain 5 [Smoke] and +2 [Smoke] Count\n[WhenUse] At 10 [Smoke], gain 2 [PlusCoinValueUp] and 3 [Protection] next turn (once per turn)
   PL:

## [walpu5] Pasywka wroga: Passives_Enemy-walpu5
- plik gry: `Passives_Enemy-walpu5.json`

750. [[walpu5] Pasywka wroga [9017801] — nazwa] 뭉게뭉게
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017801].name
   limit: do 40 znaków
   EN: Puffy Brume
   PL:
751. [[walpu5] Pasywka wroga [9017801] — opis] 자신에게 있는 [Smoke]의 효과로 받는 피해량이 증가하지 않고 대신 가하는 피해량이 증가함.
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Smoke]
   znaczenie tagów: [Smoke] = 연기 / Smoke
   EN: Instead of taking more damage due to [Smoke] on self, inflict more damage.
   PL:
752. [[walpu5] Pasywka wroga [9017802] — nazwa] 내연기관
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017802].name
   limit: do 40 znaków
   EN: Internal Combustion Engine
   PL:
753. [[walpu5] Pasywka wroga [9017802] — opis] [Smoke]를 얻을 때, 추가로 1 얻음
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Smoke]
   znaczenie tagów: [Smoke] = 연기 / Smoke
   EN: When gaining [Smoke], gain 1 additional [Smoke]
   PL:
754. [[walpu5] Pasywka wroga [9017803] — nazwa] 고기 톱니
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017803].name
   limit: do 40 znaków
   EN: Meat Gear
   PL:
755. [[walpu5] Pasywka wroga [9017803] — opis] 전투 중 가장 먼저 적중하는 코인의 피해량 +10%
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017803].desc
   limit: do 120 znaków
   EN: The first Coin to connect in an Encounter deals +10% damage
   PL:
756. [[walpu5] Pasywka wroga [9017804] — nazwa] 생각 톱니
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017804].name
   limit: do 40 znaków
   EN: Thought Gear
   PL:
757. [[walpu5] Pasywka wroga [9017804] — opis] 회피 스킬 사용시 기본 위력 +1
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017804].desc
   limit: do 120 znaków
   EN: On Evade Skill Use: Base Power +1
   PL:
758. [[walpu5] Pasywka wroga [9017805] — nazwa] 내연기관 이상
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017805].name
   limit: do 60 znaków
   EN: Internal Combustion Engine Malfunction
   PL:
759. [[walpu5] Pasywka wroga [9017805] — opis] 흐트러짐 상태가 되면, 자신의 [Smoke] 전부 소모
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9017805].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Smoke]
   znaczenie tagów: [Smoke] = 연기 / Smoke
   EN: When Staggered, lose all [Smoke] on self
   PL:
760. [[walpu5] Pasywka wroga [9018001] — nazwa] 고기 톱니: 강화
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9018001].name
   limit: do 40 znaków
   EN: Meat Gear: Enhance
   PL:
761. [[walpu5] Pasywka wroga [9018001] — opis] 자신을 제외한 아군이 있다면, 턴 시작 시 모든 아군에게 [ParryingResultUp] 1, [AttackDmgUp] 2 부여 (대상당 최대 2번 적용)\n자신을 제외한 아군이 없다면, 턴 시작 시 [Smoke] 8 얻음
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9018001].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [ParryingResultUp], [AttackDmgUp], [Smoke]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [Smoke] = 연기 / Smoke
   EN: If there are other surviving allies, apply 1 [ParryingResultUp] and 2 [AttackDmgUp] to all allies (2 times for each ally)\nIf ther eare no other surviving allies, gain 8 [Smoke] at Turn Start
   PL:
762. [[walpu5] Pasywka wroga [9018002] — nazwa] 생각 톱니: 지연
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9018002].name
   limit: do 40 znaków
   EN: Thought Gear: Delay
   PL:
763. [[walpu5] Pasywka wroga [9018002] — opis] 이 캐릭터가 살아있으면 턴 종료 시 적이 생성되지 않는다.
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9018002].desc
   limit: do 120 znaków
   EN: If this unit is alive, no enemies are generated at Turn End.
   PL:
764. [[walpu5] Pasywka wroga [9018003] — nazwa] 생각 톱니: 위해
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9018003].name
   limit: do 40 znaków
   EN: Thought Gear: Risk
   PL:
765. [[walpu5] Pasywka wroga [9018003] — opis] 수비 스킬 사용시 수비 스킬의 기본 위력 +1
   źródło: Passives_Enemy-walpu5.json :: dataList[id=9018003].desc
   limit: do 120 znaków
   EN: On Defensive Skill Use: Defensive Skill Base Power +1
   PL:

## [walpu6] Wróg / część: Enemies-walpu6
- plik gry: `Enemies-walpu6.json`

766. [[walpu6] Wróg / część [1223] — nazwa] 절망의 기사
   źródło: Enemies-walpu6.json :: dataList[id=1223].name
   limit: do 40 znaków
   EN: The Knight of Despair
   PL:
767. [[walpu6] Wróg / część [1223] — opis] 적 잡몹
   źródło: Enemies-walpu6.json :: dataList[id=1223].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [[walpu6] Wróg / część [122301] — nazwa] 몸통
   źródło: Enemies-walpu6.json :: dataList[id=122301].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [[walpu6] Wróg / część [122301] — opis] 절기 부위
   źródło: Enemies-walpu6.json :: dataList[id=122301].desc
   limit: do 120 znaków
   EN: KoD Part
   PL:
770. [[walpu6] Wróg / część [1224] — nazwa] 잊혀진 기사의 검
   źródło: Enemies-walpu6.json :: dataList[id=1224].name
   limit: do 40 znaków
   EN: Sword of a Forgotten Knight
   PL:
771. [[walpu6] Wróg / część [1224] — opis] 적 잡몹
   źródło: Enemies-walpu6.json :: dataList[id=1224].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [[walpu6] Wróg / część [122401] — nazwa] 몸통
   źródło: Enemies-walpu6.json :: dataList[id=122401].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [[walpu6] Wróg / część [122401] — opis] 절기 칼 부위
   źródło: Enemies-walpu6.json :: dataList[id=122401].desc
   limit: do 120 znaków
   EN: KoD Sword Part
   PL:
774. [[walpu6] Wróg / część [1225] — nazwa] 마음을 부수는 검
   źródło: Enemies-walpu6.json :: dataList[id=1225].name
   limit: do 40 znaków
   EN: Heart-breaking Sword
   PL:
775. [[walpu6] Wróg / część [1225] — opis] 적 잡몹
   źródło: Enemies-walpu6.json :: dataList[id=1225].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [[walpu6] Wróg / część [122501] — nazwa] 몸통
   źródło: Enemies-walpu6.json :: dataList[id=122501].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [[walpu6] Wróg / część [122501] — opis] 절기 칼 부위
   źródło: Enemies-walpu6.json :: dataList[id=122501].desc
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [[walpu6] Wróg / część [1226] — nazwa] 마음을 찢는 검
   źródło: Enemies-walpu6.json :: dataList[id=1226].name
   limit: do 40 znaków
   EN: Heart-tearing Sword
   PL:
779. [[walpu6] Wróg / część [1226] — opis] 적 잡몹
   źródło: Enemies-walpu6.json :: dataList[id=1226].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [[walpu6] Wróg / część [122601] — nazwa] 몸통
   źródło: Enemies-walpu6.json :: dataList[id=122601].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [[walpu6] Wróg / część [122601] — opis] 절기 칼 부위
   źródło: Enemies-walpu6.json :: dataList[id=122601].desc
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [[walpu6] Wróg / część [1227] — nazwa] 마음을 꿰뚫는 검
   źródło: Enemies-walpu6.json :: dataList[id=1227].name
   limit: do 40 znaków
   EN: Heart-piercing Sword
   PL:
783. [[walpu6] Wróg / część [1227] — opis] 적 잡몹
   źródło: Enemies-walpu6.json :: dataList[id=1227].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [[walpu6] Wróg / część [122701] — nazwa] 몸통
   źródło: Enemies-walpu6.json :: dataList[id=122701].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [[walpu6] Wróg / część [122701] — opis] 절기 칼 부위
   źródło: Enemies-walpu6.json :: dataList[id=122701].desc
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu6] Umiejętności wrogów / Anomalii — Skills_Abnormality-walpu6
- grupa rozdziału/trybu: `walpu6` · plik: `Skills_Abnormality-walpu6.json`

786. [Umiejętność wroga [122301] (ulepszenie 1) — nazwa] 쏟아지는 절망
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122301].levelList[level=1].name
   limit: do 40 znaków
   EN: Cascading Despair
   PL:
787. [Umiejętność wroga [122301] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Sinking]이 4 이상 있으면, 코인 위력 +1\n[WinDuel] 남은 코인 갯수 만큼 [ColdBlackTear] 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122301].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel], [ColdBlackTear]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [WhenUse] If target has 4+ [Sinking], Coin Power +1\n[WinDuel] Inflict [ColdBlackTear] equal to the # of remaining Coins
   PL:
788. [Umiejętność wroga [122301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność wroga [122301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL:
790. [Umiejętność wroga [122301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [122302] (ulepszenie 1) — nazwa] 날카로운 눈물
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].name
   limit: do 40 znaków
   EN: Sharp Teardrops
   PL:
792. [Umiejętność wroga [122302] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Sinking]이 4 이상 있으면, 코인 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 기본 위력 +1\n[WinDuel] 남은 코인 갯수 만큼 [ColdBlackTear] 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel], [ColdBlackTear]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [WhenUse] If target has 4+ [Sinking], Coin Power +1\n[WhenUse] If target has 20 or higher SP, Base Power +1\n[WinDuel] Inflict [ColdBlackTear] equal to the # of remaining Coins
   PL:
793. [Umiejętność wroga [122302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność wroga [122302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [122302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [122302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [122302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [122302] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122302].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [122303] (ulepszenie 1) — nazwa] 흐르는 절망 어린 눈물
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].name
   limit: do 40 znaków
   EN: River of Despairing Tears
   PL:
800. [Umiejętność wroga [122303] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4 당 기본 위력 +1 (최대 2)\n[WhenUse] 대상에게 [ColdBlackTear]이 1 이상 있다면, 코인 위력 +1\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [ColdBlackTear], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 for every 4 [Sinking] on target (max 2)\n[WhenUse] If target has 1+ [ColdBlackTear], Coin Power +1\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL:
801. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ColdBlackTear]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [ColdBlackTear]
   PL:
803. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 802 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 802 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 802 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [122303] (ulepszenie 1) — moneta 5, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122303].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 802 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [122304] (ulepszenie 1) — nazwa] 나누자 무뎌지는 슬픔
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122304].levelList[level=1].name
   limit: do 40 znaków
   EN: Shared Sorrow, Dulled
   PL:
812. [Umiejętność wroga [122304] (ulepszenie 1) — opis] [WhenUse] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ColdBlackTear]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [WhenUse] Inflict 1 [ColdBlackTear]
   PL:
813. [Umiejętność wroga [122304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [ColdBlackTear]이 3 이상 있다면, [Vulnerable] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ColdBlackTear], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target has 3+ [ColdBlackTear], inflict 1 [Vulnerable]
   PL:
814. [Umiejętność wroga [122305] (ulepszenie 1) — nazwa] 거세게 쏟아지는 텅 빈 절망
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122305].levelList[level=1].name
   limit: do 50 znaków
   EN: Violent Cascade of Hollow Despair
   PL:
815. [Umiejętność wroga [122305] (ulepszenie 1) — opis] [ColdBlackTear]이 가장 많은 대상을 우선 공격함\n[WhenUse] 메인 대상에게 [ColdBlackTear]이 5 이상 있다면, 코인 위력 +5
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122305].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [ColdBlackTear], [WhenUse]
   znaczenie tagów: [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears; [WhenUse] = [사용시] / [On Use]
   EN: Prioritizes targets with the most [ColdBlackTear]\n[WhenUse] If the main target has 5+ [ColdBlackTear], Coin Power +5
   PL:
816. [Umiejętność wroga [122305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [122305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 최대 체력의 ([ColdBlackTear] 수치 x 6)%만큼 고정 피해를 주고, 대상의 모든 [ColdBlackTear] 제거
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ColdBlackTear]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [UnBrokenCoinOnSucceedAttack] Deal fixed damage equal to ([ColdBlackTear] Stack on target x 6)% of target's max HP, then remove all [ColdBlackTear] on target
   PL:
818. [Umiejętność wroga [122306] (ulepszenie 1) — nazwa] 아르카나 티어 앤 피어스
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].name
   limit: do 40 znaków
   EN: Arcana: Tear and Pierce
   PL:
819. [Umiejętność wroga [122306] (ulepszenie 1) — opis] 아르카나[TabExplain] 슬레이브를 사용하는 적이 있고, 자신에게 [CollapsedPride]가 없으면 사용함
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [CollapsedPride]
   znaczenie tagów: [CollapsedPride] = 무너져 내린 긍지 / Crumbled Pride
   EN: Uses this Skill when an enemy uses Arcana[TabExplain] Slave, and when this unit does not have [CollapsedPride]\nCounterattacks only Arcana Slave
   PL:
820. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [ColdBlackTear] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ColdBlackTear]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [OnSucceedAttack] Inflict 2 [ColdBlackTear]
   PL:
822. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ColdBlackTear]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [OnSucceedAttack] Inflict 1 [ColdBlackTear]
   PL:
824. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [ColdBlackTear] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [122306] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 대상의 최대 체력의 ([ColdBlackTear] 수치 x 6)%만큼 고정 피해를 주고, 대상의 모든 [ColdBlackTear] 제거 (내성 무시)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122306].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ColdBlackTear]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [OnSucceedAttack] Deal fixed damage equal to ([ColdBlackTear] Stack on target x 6)% of target's max HP, then remove all [ColdBlackTear] on target (ignores Resistances)
   PL:
830. [Umiejętność wroga [122401] (ulepszenie 1) — nazwa] 빛바랜 믿음
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122401].levelList[level=1].name
   limit: do 40 znaków
   EN: Faded Faith
   PL:
831. [Umiejętność wroga [122401] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122401].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Clash Power +1 for every 4 [Sinking] on target (max 2)\n[WhenUse] If target has 10 or higher SP, Base Power +1\n[WhenUse] If target has 20 or higher SP, Coin Power +1
   PL:
832. [Umiejętność wroga [122401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [122401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [122402] (ulepszenie 1) — nazwa] 닳아버린 긍지
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122402].levelList[level=1].name
   limit: do 40 znaków
   EN: Weathered Pride
   PL:
835. [Umiejętność wroga [122402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122402].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [122402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [122402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [122402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [122403] (ulepszenie 1) — nazwa] 끝없는 절망
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122403].levelList[level=1].name
   limit: do 40 znaków
   EN: Endless Despair
   PL:
840. [Umiejętność wroga [122403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122403].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność wroga [122403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [122403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [122403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [122403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [122404] (ulepszenie 1) — nazwa] 눈물로 벼려낸 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122404].levelList[level=1].name
   limit: do 40 znaków
   EN: Sword Sharpened with Tears
   PL:
846. [Umiejętność wroga [122404] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +5 (최대 10)\n[WhenUse] 대상에게 [ColdBlackTear]이 있다면, 최종 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122404].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [ColdBlackTear]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [WhenUse] Coin Power +5 for every 6 [Sinking] on target (max 10)\n[WhenUse] If target has [ColdBlackTear], Final Power +1
   PL:
847. [Umiejętność wroga [122404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 6 이상이라면, 다음 턴에 [DefenseDown] (대상의 [Sinking]수치 / 10)만큼 부여 (소수점 버림)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] If target has 6+ [Sinking], inflict ([Sinking] on target / 10) [DefenseDown] next turn (rounded down)
   PL:
848. [Umiejętność wroga [122405] (ulepszenie 1) — nazwa] 비통이 맺힌 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122405].levelList[level=1].name
   limit: do 40 znaków
   EN: Sword Laced with Grief
   PL:
849. [Umiejętność wroga [122405] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +3 (최대 6)\n[WhenUse] 대상의 [ColdBlackTear] 1당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122405].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [ColdBlackTear]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [WhenUse] Coin Power +3 for every 6 [Sinking] on target (max 6)\n[WhenUse] Base Power +1 for every [ColdBlackTear] Count on target (max 3)
   PL:
850. [Umiejętność wroga [122405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność wroga [122405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 최대 체력의 (스킬 위력)%만큼 추가 우울 피해를 줌 (최대 30)\n- 대상에게 [ColdBlackTear]이 2 이상 있을 경우 한번 더 추가 우울 피해를 줌
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack], [ColdBlackTear]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears
   EN: [UnBrokenCoinOnSucceedAttack] Deal bonus Gloom damage equal to (Skill Power)% of target's max HP (max 30)\n- If target has 2+ [ColdBlackTear], deal bonus Gloom damage again
   PL:
852. [Umiejętność wroga [122501] (ulepszenie 1) — nazwa] 빛바랜 믿음
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122501].levelList[level=1].name
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Umiejętność wroga [122501] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122501].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność wroga [122501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność wroga [122501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność wroga [122502] (ulepszenie 1) — nazwa] 닳아버린 긍지
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122502].levelList[level=1].name
   (powtórzenie elementu 834 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność wroga [122502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122502].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Umiejętność wroga [122502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność wroga [122502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność wroga [122502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [122503] (ulepszenie 1) — nazwa] 끝없는 절망
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122503].levelList[level=1].name
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność wroga [122503] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122503].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność wroga [122503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność wroga [122503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność wroga [122503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Umiejętność wroga [122503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Umiejętność wroga [122504] (ulepszenie 1) — nazwa] 눈물로 벼려낸 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122504].levelList[level=1].name
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Umiejętność wroga [122504] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +5 (최대 10)\n[WhenUse] 대상에게 [ColdBlackTear]이 있다면, 최종 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122504].levelList[level=1].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Umiejętność wroga [122504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 6 이상이라면, 다음 턴에 [DefenseDown] (대상의 [Sinking]수치 / 10)만큼 부여 (소수점 버림)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [122505] (ulepszenie 1) — nazwa] 비통이 맺힌 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122505].levelList[level=1].name
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność wroga [122505] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +3 (최대 6)\n[WhenUse] 대상의 [ColdBlackTear] 1당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122505].levelList[level=1].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Umiejętność wroga [122505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Umiejętność wroga [122505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 최대 체력의 (스킬 위력)%만큼 추가 우울 피해를 줌 (최대 30)\n- 대상에게 [ColdBlackTear]이 2 이상 있을 경우 한번 더 추가 우울 피해를 줌
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Umiejętność wroga [122601] (ulepszenie 1) — nazwa] 빛바랜 믿음
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122601].levelList[level=1].name
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Umiejętność wroga [122601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122601].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Umiejętność wroga [122601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Umiejętność wroga [122601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność wroga [122602] (ulepszenie 1) — nazwa] 닳아버린 긍지
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122602].levelList[level=1].name
   (powtórzenie elementu 834 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Umiejętność wroga [122602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122602].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Umiejętność wroga [122602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Umiejętność wroga [122602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Umiejętność wroga [122602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Umiejętność wroga [122603] (ulepszenie 1) — nazwa] 끝없는 절망
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122603].levelList[level=1].name
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Umiejętność wroga [122603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122603].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Umiejętność wroga [122603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Umiejętność wroga [122603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Umiejętność wroga [122603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność wroga [122603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Umiejętność wroga [122604] (ulepszenie 1) — nazwa] 눈물로 벼려낸 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122604].levelList[level=1].name
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Umiejętność wroga [122604] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +5 (최대 10)\n[WhenUse] 대상에게 [ColdBlackTear]이 있다면, 최종 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122604].levelList[level=1].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Umiejętność wroga [122604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 6 이상이라면, 다음 턴에 [DefenseDown] (대상의 [Sinking]수치 / 10)만큼 부여 (소수점 버림)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Umiejętność wroga [122605] (ulepszenie 1) — nazwa] 비통이 맺힌 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122605].levelList[level=1].name
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Umiejętność wroga [122605] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +3 (최대 6)\n[WhenUse] 대상의 [ColdBlackTear] 1당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122605].levelList[level=1].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Umiejętność wroga [122605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Umiejętność wroga [122605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 최대 체력의 (스킬 위력)%만큼 추가 우울 피해를 줌 (최대 30)\n- 대상에게 [ColdBlackTear]이 2 이상 있을 경우 한번 더 추가 우울 피해를 줌
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Umiejętność wroga [122701] (ulepszenie 1) — nazwa] 빛바랜 믿음
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122701].levelList[level=1].name
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Umiejętność wroga [122701] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122701].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Umiejętność wroga [122701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność wroga [122701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Umiejętność wroga [122702] (ulepszenie 1) — nazwa] 닳아버린 긍지
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122702].levelList[level=1].name
   (powtórzenie elementu 834 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Umiejętność wroga [122702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122702].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność wroga [122702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Umiejętność wroga [122702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Umiejętność wroga [122702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność wroga [122703] (ulepszenie 1) — nazwa] 끝없는 절망
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122703].levelList[level=1].name
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Umiejętność wroga [122703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 4당 합 위력 +1 (최대 2)\n[WhenUse] 대상의 정신력이 10 이상이라면, 기본 위력 +1\n[WhenUse] 대상의 정신력이 20 이상이라면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122703].levelList[level=1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność wroga [122703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność wroga [122703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Umiejętność wroga [122703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność wroga [122703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Umiejętność wroga [122704] (ulepszenie 1) — nazwa] 눈물로 벼려낸 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122704].levelList[level=1].name
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność wroga [122704] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +5 (최대 10)\n[WhenUse] 대상에게 [ColdBlackTear]이 있다면, 최종 위력 +1
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122704].levelList[level=1].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Umiejętność wroga [122704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 6 이상이라면, 다음 턴에 [DefenseDown] (대상의 [Sinking]수치 / 10)만큼 부여 (소수점 버림)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Umiejętność wroga [122705] (ulepszenie 1) — nazwa] 비통이 맺힌 검
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122705].levelList[level=1].name
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [122705] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 6당 코인 위력 +3 (최대 6)\n[WhenUse] 대상의 [ColdBlackTear] 1당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122705].levelList[level=1].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Umiejętność wroga [122705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Umiejętność wroga [122705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 최대 체력의 (스킬 위력)%만큼 추가 우울 피해를 줌 (최대 30)\n- 대상에게 [ColdBlackTear]이 2 이상 있을 경우 한번 더 추가 우울 피해를 줌
   źródło: Skills_Abnormality-walpu6.json :: dataList[id=122705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu6] Pasywka wroga: Passives_Abnormality-walpu6
- plik gry: `Passives_Abnormality-walpu6.json`

918. [[walpu6] Pasywka wroga [122301] — nazwa] 절망의 기사
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122301].name
   (powtórzenie elementu 766 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [[walpu6] Pasywka wroga [122301] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -50% (소수점 버림)\n자신의 [SuperCoin]이 파괴된 채 적중시, 대상의 [Sinking] 효과를 발동하지 않음 (횟수 차감하지 않음)
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122301].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [SuperCoin]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Takes -50% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] (rounded down)\nIf this unit hits with a Cracked [SuperCoin], it does not activate the target's [Sinking] effect (does not consume Count either)
   PL:
920. [[walpu6] Pasywka wroga [122302] — nazwa] 흐르는 무력한 눈물
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122302].name
   limit: do 40 znaków
   EN: River of Helpless Tears
   PL:
921. [[walpu6] Pasywka wroga [122302] — opis] 턴 시작 시 필드에 있는 검 중 [HelplessTear]을 지니고 있는 검이 하나도 없다면, 임의의 검 1개에게 [HelplessTear] 부여 (턴 당 1회, [HelplessTear]이 있는 검이 있는 경우 발동하지 않음)
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122302].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [HelplessTear]
   znaczenie tagów: [HelplessTear] = 무력한 눈물 / Helpless Tears
   EN: Turn Start: if none of the swords on the field have [HelplessTear], apply [HelplessTear] to 1 random sword (once per turn; does not activate if a sword has [HelplessTear])
   PL:
922. [[walpu6] Pasywka wroga [122303] — nazwa] 볼품없는 긍지
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122303].name
   limit: do 40 znaków
   EN: Hollow Pride
   PL:
923. [[walpu6] Pasywka wroga [122303] — opis] 첫번째 흐트러짐 이후 턴 종료 시 [ColdBlackTear]을 5 이상 가지고 있는 수감자가 있다면 다음 턴에 광역기를 사용함\n첫번째 흐트러짐 이후 턴 종료 시 모든 수감자에게 [ColdBlackTear]이 있다면, 다음 턴에 [SignOfDespair]를 획득함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122303].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [ColdBlackTear], [SignOfDespair]
   znaczenie tagów: [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears; [SignOfDespair] = 절망의 가호 / Blessing of Despair
   EN: Turn End after getting Staggered for the first time: if there is a Sinner with 5+ [ColdBlackTear], uses an AoE Skill next turn\nTurn End after getting Staggered for the first time: if all Sinners have [ColdBlackTear], gain [SignOfDespair] next turn
   PL:
924. [[walpu6] Pasywka wroga [122304] — nazwa] 나눠가지는 슬픔
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122304].name
   limit: do 40 znaków
   EN: Shared Sorrow
   PL:
925. [[walpu6] Pasywka wroga [122304] — opis] 처음 흐트러졌을 경우 다음 턴에 흐트러짐을 해제하고, 매 턴마다 [Protection] 10과 보호막 500 얻음\n다음 턴에 잊혀진 기사의 검을 소환함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122304].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: When Staggered for the first time, recover from Stagger next turn; then, gain 10 [Protection] and 500 Shield every turn\nSummon a Forgotten Knight's Sword next turn
   PL:
926. [[walpu6] Pasywka wroga [122305] — nazwa] 닳디 닳은 기사
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122305].name
   limit: do 40 znaków
   EN: Weathered Knight
   PL:
927. [[walpu6] Pasywka wroga [122305] — opis] 검이 자신에게 꽂힐 때 마다 매 턴마다 얻는 [Protection]를 3, 보호막을 100 감소하고, [CollapsedPride]를 1 얻음\n자신의 [CollapsedPride]가 3일 경우 [Protection]와 보호막을 더 이상 얻지 않고 다음 턴에 흐트러짐 상태가 되고 [WornOutKnight]를 얻음
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122305].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [CollapsedPride], [WornOutKnight]
   znaczenie tagów: [Protection] = 보호 / Protection; [CollapsedPride] = 무너져 내린 긍지 / Crumbled Pride; [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight
   EN: Every time a sword pierces this unit, gain 1 [CollapsedPride], and [Protection] gained every turn is reduced by 3 while Shield HP gained every turn is reduced by 100\nAt 3 [CollapsedPride], this unit no longer gains [Protection] and Shield every turn, and instead becomes Staggered next turn and gains [WornOutKnight]
   PL:
928. [[walpu6] Pasywka wroga [122306] — nazwa] 하나 남은 정의
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122306].name
   limit: do 40 znaków
   EN: One Last Justice
   PL:
929. [[walpu6] Pasywka wroga [122306] — opis] 자신에게 [WornOutKnight]가 있는 상태로 아르카나[TabExplain] 슬레이브 적중시, 체력이 5% 미만으로 떨어지지 않고, 턴 종료 시 자결함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122306].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [WornOutKnight], [TabExplain]
   znaczenie tagów: [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight
   EN: When this unit is hit by ARCANA[TabExplain] SLAVE while it has [WornOutKnight]: does not lose HP below 5%, and kills itself at Turn End
   PL:
930. [[walpu6] Pasywka wroga [122307] — nazwa] 나눠가지는 슬픔
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122307].name
   (powtórzenie elementu 924 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [[walpu6] Pasywka wroga [122307] — opis] 처음 흐트러졌을 경우 다음 턴에 흐트러짐을 해제하고, 매 턴마다 [Protection] 10과 보호막 500 얻음\n다음 턴에 마음을 부수는 검, 마음을 찢는 검, 마음을 꿰뚫는 검을 소환함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122307].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: When Staggered for the first time, recover from Stagger next turn; then, gain 10 [Protection] and 500 Shield every turn\nSummon Heart-breaking Sword, Heart-tearing Sword, and Heart-piercing Sword next turn
   PL:
932. [[walpu6] Pasywka wroga [122308] — nazwa] 하나 남은 정의
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122308].name
   (powtórzenie elementu 928 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [[walpu6] Pasywka wroga [122308] — opis] 자신에게 [WornOutKnight]가 있고 체력이 600 미만인 상태로 아르카나[TabExplain] 슬레이브 적중시, 체력이 5% 미만으로 떨어지지 않고, 턴 종료 시 자결함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122308].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [WornOutKnight], [TabExplain]
   znaczenie tagów: [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight
   EN: When this unit is hit by ARCANA[TabExplain] SLAVE while it has [WornOutKnight] and is at less than 600 HP: does not lose HP below 5%, and kills itself at Turn End
   PL:
934. [[walpu6] Pasywka wroga [122401] — nazwa] 절망을 찌르는 검
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122401].name
   limit: do 40 znaków
   EN: Despair-piercing Sword
   PL:
935. [[walpu6] Pasywka wroga [122401] — opis] [HelplessTear]이 있는 검이 체력이 0이 되면, 절망의 기사에게 꽂힘
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [HelplessTear], [TabExplain]
   znaczenie tagów: [HelplessTear] = 무력한 눈물 / Helpless Tears
   EN: If a sword with [HelplessTear] reaches 0 HP, it stabs the Knight of Despair[TabExplain]
   PL:
936. [[walpu6] Pasywka wroga [122402] — nazwa] 잊혀진 기사의 검
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122402].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [[walpu6] Pasywka wroga [122402] — opis] 자신의 [SuperCoin]이 파괴된 채 적중시, 대상의 [Sinking] 효과를 발동하지 않음
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122402].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [SuperCoin], [Sinking]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking
   EN: If this unit hits with a Cracked [SuperCoin], it does not activate the target's [Sinking] effect
   PL:
938. [[walpu6] Pasywka wroga [122403] — nazwa] 칼 끝이 향하는 건 보호해 주지 못한 모든 이들
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122403].name
   limit: do 80 znaków
   EN: The Sword Points Toward Those Who Could Not be Protected
   PL:
939. [[walpu6] Pasywka wroga [122403] — opis] [ChasingArcana]를 지닌 적이 있다면, 그 대상을 우선 타겟 지정함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122403].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChasingArcana]
   znaczenie tagów: [ChasingArcana] = 영창 - 아르카나 슬레이브 / Chanting - Arcana Slave
   EN: If there is an enemy with [ChasingArcana], prioritizes that unit
   PL:
940. [[walpu6] Pasywka wroga [122404] — nazwa] 휴식
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122404].name
   limit: do 40 znaków
   EN: Respite
   PL:
941. [[walpu6] Pasywka wroga [122404] — opis] [HelplessTear]이 없는 상태에서 체력이 1 미만으로 감소하지 않음.\n턴 종료 시 [HelplessTear]이 없는 상태에서 체력이 1일 경우, 체력을 최대로 회복함
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122404].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [HelplessTear]
   znaczenie tagów: [HelplessTear] = 무력한 눈물 / Helpless Tears
   EN: This unit's HP does not drop below 1 when it does not have [HelplessTear]\nTurn End: if this unit's HP drops to 1 when it does not have [HelplessTear], heals back to full HP
   PL:
942. [[walpu6] Pasywka wroga [122405] — nazwa] 절망을 찌르는 검
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122405].name
   (powtórzenie elementu 934 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [[walpu6] Pasywka wroga [122405] — opis] [HelplessTear]이 있는 검이 체력이 0이 되면, 절망의 기사에게 꽂히고, 다음 턴에 임의의 검 1개에게 자신의 물리 내성 중 취약인 내성을 똑같이 취약으로 바꿈
   źródło: Passives_Abnormality-walpu6.json :: dataList[id=122405].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [HelplessTear], [TabExplain]
   znaczenie tagów: [HelplessTear] = 무력한 눈물 / Helpless Tears
   EN: If a sword with [HelplessTear] reaches 0 HP, it stabs the Knight of Despair[TabExplain]; then, transfers its Fatal Resistance value to 1 other random Sword next turn
   PL:

## [walpu8] Wróg / część: Enemies-walpu8
- plik gry: `Enemies-walpu8.json`

944. [[walpu8] Wróg / część [1366] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1366].name
   limit: do 40 znaków
   EN: BongBong [Orange]
   PL:
945. [[walpu8] Wróg / część [1366] — opis] 여명 시련 - 무리 이동 준비 1
   źródło: Enemies-walpu8.json :: dataList[id=1366].desc
   limit: do 120 znaków
   EN: Dawn Ordeal - Swarm Movement Prep 1
   PL:
946. [[walpu8] Wróg / część [136601] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136601].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [[walpu8] Wróg / część [136601] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136601].desc
   limit: do 120 znaków
   EN: BongBong [Orange] Body
   PL:
948. [[walpu8] Wróg / część [1367] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1367].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [[walpu8] Wróg / część [1367] — opis] 여명 시련 - 무리 이동 준비 2
   źródło: Enemies-walpu8.json :: dataList[id=1367].desc
   limit: do 120 znaków
   EN: Dawn Ordeal - Swarm Movement Prep 2
   PL:
950. [[walpu8] Wróg / część [136701] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136701].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [[walpu8] Wróg / część [136701] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136701].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [[walpu8] Wróg / część [1368] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1368].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [[walpu8] Wróg / część [1368] — opis] 여명 시련 - 무리 이동 준비 3
   źródło: Enemies-walpu8.json :: dataList[id=1368].desc
   limit: do 120 znaków
   EN: Dawn Ordeal - Swarm Movement Prep 3
   PL:
954. [[walpu8] Wróg / część [136801] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136801].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [[walpu8] Wróg / część [136801] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136801].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [[walpu8] Wróg / część [1369] — nazwa] 큥큥이[오렌지맛 착즙기]
   źródło: Enemies-walpu8.json :: dataList[id=1369].name
   limit: do 50 znaków
   EN: BunBun [Juicy Squeezer - Orange]
   PL:
957. [[walpu8] Wróg / część [1369] — opis] 어스름 시련
   źródło: Enemies-walpu8.json :: dataList[id=1369].desc
   limit: do 120 znaków
   EN: Ordeal of Dusk
   PL:
958. [[walpu8] Wróg / część [136901] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136901].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [[walpu8] Wróg / część [136901] — opis] 큥큥이[오렌지맛 착즙기] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=136901].desc
   limit: do 120 znaków
   EN: BunBun [Juicy Squeezer - Orange] Body
   PL:
960. [[walpu8] Wróg / część [1370] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1370].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [[walpu8] Wróg / część [1370] — opis] 여명 시련 - 무리 이동 준비 1
   źródło: Enemies-walpu8.json :: dataList[id=1370].desc
   (powtórzenie elementu 945 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [[walpu8] Wróg / część [137001] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137001].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [[walpu8] Wróg / część [137001] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137001].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [[walpu8] Wróg / część [1371] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1371].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [[walpu8] Wróg / część [1371] — opis] 여명 시련 - 무리 이동 준비 2
   źródło: Enemies-walpu8.json :: dataList[id=1371].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [[walpu8] Wróg / część [137101] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137101].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [[walpu8] Wróg / część [137101] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137101].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [[walpu8] Wróg / część [1372] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1372].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [[walpu8] Wróg / część [1372] — opis] 여명 시련 - 무리 이동 준비 3
   źródło: Enemies-walpu8.json :: dataList[id=1372].desc
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [[walpu8] Wróg / część [137201] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137201].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [[walpu8] Wróg / część [137201] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137201].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [[walpu8] Wróg / część [1373] — nazwa] 큥큥이[오렌지맛 착즙기]
   źródło: Enemies-walpu8.json :: dataList[id=1373].name
   (powtórzenie elementu 956 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [[walpu8] Wróg / część [1373] — opis] 어스름 시련
   źródło: Enemies-walpu8.json :: dataList[id=1373].desc
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [[walpu8] Wróg / część [137301] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137301].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [[walpu8] Wróg / część [137301] — opis] 큥큥이[오렌지맛 착즙기] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137301].desc
   (powtórzenie elementu 959 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [[walpu8] Wróg / część [1374] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1374].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [[walpu8] Wróg / część [1374] — opis] 여명 시련 - 무리 이동 준비 1
   źródło: Enemies-walpu8.json :: dataList[id=1374].desc
   (powtórzenie elementu 945 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [[walpu8] Wróg / część [137401] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137401].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [[walpu8] Wróg / część [137401] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137401].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [[walpu8] Wróg / część [1375] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1375].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [[walpu8] Wróg / część [1375] — opis] 여명 시련 - 무리 이동 준비 2
   źródło: Enemies-walpu8.json :: dataList[id=1375].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
982. [[walpu8] Wróg / część [137501] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137501].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [[walpu8] Wróg / część [137501] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137501].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [[walpu8] Wróg / część [1376] — nazwa] 뀽뀽이[오렌지맛]
   źródło: Enemies-walpu8.json :: dataList[id=1376].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [[walpu8] Wróg / część [1376] — opis] 여명 시련 - 무리 이동 준비 3
   źródło: Enemies-walpu8.json :: dataList[id=1376].desc
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [[walpu8] Wróg / część [137601] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137601].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [[walpu8] Wróg / część [137601] — opis] 뀽뀽이[오렌지맛] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137601].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [[walpu8] Wróg / część [1377] — nazwa] 큥큥이[오렌지맛 착즙기]
   źródło: Enemies-walpu8.json :: dataList[id=1377].name
   (powtórzenie elementu 956 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [[walpu8] Wróg / część [1377] — opis] 어스름 시련
   źródło: Enemies-walpu8.json :: dataList[id=1377].desc
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [[walpu8] Wróg / część [137701] — nazwa] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137701].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [[walpu8] Wróg / część [137701] — opis] 큥큥이[오렌지맛 착즙기] 몸통
   źródło: Enemies-walpu8.json :: dataList[id=137701].desc
   (powtórzenie elementu 959 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu8] Umiejętności wrogów / Anomalii — Skills_Abnormality-walpu8
- grupa rozdziału/trybu: `walpu8` · plik: `Skills_Abnormality-walpu8.json`

992. [Umiejętność wroga [136601] (ulepszenie 1) — nazwa] 달려들기
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136601].levelList[level=1].name
   limit: do 40 znaków
   EN: Pounce
   PL:
993. [Umiejętność wroga [136601] (ulepszenie 1) — opis] 체력 비율이 가장 높은 대상 우선 공격\n[WhenUse] 대상에게 [Laceration]이 4이상 있으면, 기본 위력 +1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136601].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Prioritizes targets with the highest HP percentage\n[WhenUse] If target has 4+ [Laceration], Base Power +1
   PL:
994. [Umiejętność wroga [136601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Umiejętność wroga [136602] (ulepszenie 1) — nazwa] 깨물어 먹기
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136602].levelList[level=1].name
   limit: do 40 znaków
   EN: Gnawing Gobble
   PL:
996. [Umiejętność wroga [136602] (ulepszenie 1) — opis] 체력 비율이 가장 높은 대상 우선 공격\n[WhenUse] 대상에게 [Laceration]이 4이상 있으면, 기본 위력 +1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136602].levelList[level=1].desc
   (powtórzenie elementu 993 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Umiejętność wroga [136602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있을 경우, 다음 턴에 [PenetrateResistDown] 2 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [PenetrateResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [PenetrateResistDown] = 관통 내성 약화 / Pierce Resist Down
   EN: [OnSucceedAttack] If target has [Laceration], Inflict 2 [PenetrateResistDown] next turn
   PL:
998. [Umiejętność wroga [136602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Umiejętność wroga [136603] (ulepszenie 1) — nazwa] 오렌지맛 버블 보충
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136603].levelList[level=1].name
   limit: do 50 znaków
   EN: Orange-flavored Bubble Supplement
   PL:
1000. [Umiejętność wroga [136603] (ulepszenie 1) — opis] 체력 비율이 가장 높은 대상 우선 공격\n[WhenUse] 대상에게 [Laceration]이 4이상 있으면, 코인 위력 +1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136603].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Prioritizes targets with the highest HP percentage\n[WhenUse] If target has 4+ [Laceration], Coin Power +1
   PL:
1001. [Umiejętność wroga [136603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Umiejętność wroga [136603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1003. [Umiejętność wroga [136603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Umiejętność wroga [136604] (ulepszenie 1) — nazwa] 버블 풍미 더하기
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].name
   limit: do 40 znaków
   EN: Add a Note of Bubbly Flavor
   PL:
1005. [Umiejętność wroga [136604] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)
   PL:
1006. [Umiejętność wroga [136604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있을 경우, 다음 턴에 [PenetrateResistDown] 2 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 997 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [Umiejętność wroga [136604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Umiejętność wroga [136604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [Umiejętność wroga [136604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1010. [Umiejętność wroga [136604] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1011. [Umiejętność wroga [136605] (ulepszenie 1) — nazwa] 무리 이동
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136605].levelList[level=1].name
   limit: do 40 znaków
   EN: Herd Migration
   PL:
1012. [Umiejętność wroga [136605] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Binding] 2 부여\n[EndBattle] 자신의 [RunHallway]소멸 후 [NextHallway] 발동
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136605].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Binding], [EndBattle], [RunHallway], [NextHallway]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Binding] = 속박 / Bind; [EndBattle] = [턴 종료 시] / [Turn End]; [RunHallway] = 무리 이동 준비 / Preparing Herd Migration; [NextHallway] = 무리 이주 / Herd Relocation
   EN: [OnSucceedEvade] Inflict 2 [Binding] next turn\n[EndBattle] [RunHallway] expires; then, activate [NextHallway]
   PL:
1013. [Umiejętność wroga [136901] (ulepszenie 1) — nazwa] 씹어 먹기
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136901].levelList[level=1].name
   limit: do 40 znaków
   EN: Chomping Gobble
   PL:
1014. [Umiejętność wroga [136901] (ulepszenie 1) — opis] 속도가 가장 낮은 대상 우선 공격\n[WhenUse] 대상에게 [Laceration]이 4이상 있으면, 기본 위력 +1\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136901].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Prioritizes targets with the slowest Speed\n[WhenUse] If target has 4+ [Laceration], Base Power +1\n[BeforeAttack] Base Power -1 for every Cracked Coin
   PL:
1015. [Umiejętność wroga [136901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1016. [Umiejętność wroga [136901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +3 [Laceration] Count
   PL:
1017. [Umiejętność wroga [136902] (ulepszenie 1) — nazwa] 중형 오렌지 버블 채우기
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].name
   limit: do 50 znaków
   EN: Filling a Medium-sized Orange Bubble
   PL:
1018. [Umiejętność wroga [136902] (ulepszenie 1) — opis] 속도가 가장 낮은 대상 우선 공격\n[WhenUse] 대상에게 [Laceration]이 4이상 있으면, 코인 위력 +1\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Prioritizes targets with the slowest Speed\n[WhenUse] If target has 4+ [Laceration], Coin Power +1\n[BeforeAttack] Base Power -1 for every Cracked Coin
   PL:
1019. [Umiejętność wroga [136902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Umiejętność wroga [136902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Umiejętność wroga [136902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1022. [Umiejętność wroga [136902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Umiejętność wroga [136902] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136902].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL:
1024. [Umiejętność wroga [136903] (ulepszenie 1) — nazwa] 더 진하고 더 많이
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].name
   limit: do 40 znaków
   EN: More Potent, More Plentiful
   PL:
1025. [Umiejętność wroga [136903] (ulepszenie 1) — opis] 속도가 가장 낮은 대상 우선 공격\n[WhenUse] 대상의 [Laceration] 3당, 코인 위력 +1 (최대 2)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Prioritizes targets with the slowest Speed\n[WhenUse] Coin Power +1 for every 3 [Laceration] on target (max 2)\n[BeforeAttack] Base Power -1 for every Cracked Coin
   PL:
1026. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +4 [Laceration] Count
   PL:
1028. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1032. [Umiejętność wroga [136903] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateResistDown] 2 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136903].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateResistDown] = 관통 내성 약화 / Pierce Resist Down
   EN: [OnSucceedAttack] Inflict 2 [PenetrateResistDown] next turn
   PL:
1033. [Umiejętność wroga [136904] (ulepszenie 1) — nazwa] 뀽뀽이 번식을 위한 사료 포식
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].name
   limit: do 60 znaków
   EN: Feed Consumption for BongBong Procreation
   PL:
1034. [Umiejętność wroga [136904] (ulepszenie 1) — opis] 속도가 가장 낮은 대상 우선 공격\n[WhenUse] 대상의 [Laceration] 3당, 코인 위력 +1 (최대 2)\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -1
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].desc
   (powtórzenie elementu 1025 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1036. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1038. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1039. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1040. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1042. [Umiejętność wroga [136904] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136904].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Umiejętność wroga [136905] (ulepszenie 1) — nazwa] 무리 이동
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136905].levelList[level=1].name
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Umiejętność wroga [136905] (ulepszenie 1) — opis] [CanDuelGuard]\n[EndBattle] 자신의 [RunHallway]소멸 후 ‘자신’과 ‘자신이 소환한 완전 식품’에게 [NextHallway] 발동
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136905].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [EndBattle], [RunHallway], [NextHallway]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [EndBattle] = [턴 종료 시] / [Turn End]; [RunHallway] = 무리 이동 준비 / Preparing Herd Migration; [NextHallway] = 무리 이주 / Herd Relocation
   EN: [CanDuelGuard]\n[EndBattle] [RunHallway] expires; then, activate [NextHallway] for 'self' and 'The Perfect Food summoned by self'
   PL:
1045. [Umiejętność wroga [136905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-walpu8.json :: dataList[id=136905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [walpu8] Pasywka wroga: Passives_Abnormality-walpu8
- plik gry: `Passives_Abnormality-walpu8.json`

1046. [[walpu8] Pasywka wroga [136601] — nazwa] 방황하는 시련
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136601].name
   limit: do 40 znaków
   EN: Wandering Ordeal
   PL:
1047. [[walpu8] Pasywka wroga [136601] — opis] 등장 시 [RunHallway]를 1~3 얻음\n턴 시작 시 [RunHallway]가 0이면, ‘무리 이동’ 스킬 사용\n(흐트러짐 상태 일 시, 흐트러짐 상태를 해제하고 발동)\n\n전투에 ‘큥큥이’가 있으면, 해당 패시브 발동하지 않음
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136601].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [RunHallway]
   znaczenie tagów: [RunHallway] = 무리 이동 준비 / Preparing Herd Migration
   EN: Upon entry, gain 1~3 [RunHallway]\nTurn Start: At 0 [RunHallway], use 'Herd Migration'\n(If this unit is Staggered, recover from Stagger when this effect triggers)\n\nIf 'BunBun' is on the battlefield, this passive does not activate
   PL:
1048. [[walpu8] Pasywka wroga [136601] — tekst klimatyczny] ‘시련은 환상체와 사뭇 다르다. 시련은 이 회사 깊은 곳에서 흐르는 인류의 꿈에서 무작위적으로 끌어올려진 강렬한 트라우마들의 표상이다.’
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136601].flavor
   limit: do 260 znaków
   EN: 'Ordeals are quite distinct from Abnormalities—they are vivid representations of intense traumas, dredged up at random from humanity's dreams that course through the farthest depths of this company.'
   PL:
1049. [[walpu8] Pasywka wroga [136602] — nazwa] 입맛 저격
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136602].name
   limit: do 40 znaków
   EN: Tailored for the Palate
   PL:
1050. [[walpu8] Pasywka wroga [136602] — opis] 대상의 약점,  취약 속성(내성 1 초과)으로 공격 적중 시, 다음 턴에 [Binding] 1 부여 (스킬당 1회)
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136602].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: On Attack Hit against a target with a damage type the target is "Weak" or "Fatal" (Resistance > 1) to, inflict 1 [Binding] next turn (once per Skill)
   PL:
1051. [[walpu8] Pasywka wroga [136602] — tekst klimatyczny] ‘이렇게 맛있는 음료 이름이 왜 뀽뀽이일까요?’
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136602].flavor
   limit: do 120 znaków
   EN: "How could such a flavorful beverage end up being called BongBong?"
   PL:
1052. [[walpu8] Pasywka wroga [136603] — nazwa] 맛의 비밀
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136603].name
   limit: do 40 znaków
   EN: The Secret of Taste
   PL:
1053. [[walpu8] Pasywka wroga [136603] — opis] 자신을 처치한 대상에게 [PumpkinJelly] 1 부여
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136603].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PumpkinJelly]
   znaczenie tagów: [PumpkinJelly] = 오렌지맛 뀽뀽이 / BongBong Orange
   EN: Inflict 1 [PumpkinJelly] on the target that killed this unit
   PL:
1054. [[walpu8] Pasywka wroga [136901] — nazwa] 방황하는 시련
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136901].name
   (powtórzenie elementu 1046 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [[walpu8] Pasywka wroga [136901] — opis] 스테이지 시작 시 [RunHallway] 3 얻음\n턴 시작 시 [RunHallway]가 0이면, ‘무리 이동’ 스킬 사용\n(흐트러짐 상태 일 시, 흐트러짐 상태를 해제하고 발동)\n\n전투 중 ‘자신이 소환한 뀽뀽이’ 이외 남은 ‘뀽뀽이’가 없는 경우\n‘무리 이동’의 스킬 효과가 발동하지 않으며, 다음 턴 [RunHallway] 3 얻음
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136901].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [RunHallway]
   znaczenie tagów: [RunHallway] = 무리 이동 준비 / Preparing Herd Migration
   EN: Encounter Start: Gain 3 [RunHallway]\nTurn Start: At 0 [RunHallway], use 'Herd Migration'\n(If this unit is Staggered, recover from Stagger when this effect triggers)\n\nIf there are no BongBongs left on the battlefield except for "BongBongs spawned by this unit", the Skill effects of 'Herd Migration' do not trigger, and this unit gains 3 [RunHallway] next turn
   PL:
1056. [[walpu8] Pasywka wroga [136901] — tekst klimatyczny] ‘저 희끄무레한 연기 속에서 시련이란 것들이 튀어나오는데… 저 연기는 대체 뭔가요, 팀장님!’
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136901].flavor
   limit: do 160 znaków
   EN: "These Ordeal things keep popping out from that murky-white smoke... just what is that smoke supposed to be, Captain?!"
   PL:
1057. [[walpu8] Pasywka wroga [136902] — nazwa] 이어지는 시련
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136902].name
   limit: do 40 znaków
   EN: Lasting Ordeal
   PL:
1058. [[walpu8] Pasywka wroga [136902] — opis] 퇴각 후 4턴이 지나면, ‘자신’과 ‘자신이 소환한 뀽뀽이’가 등장 가능한 수만큼 전투 복귀. 이후 [RunHallway] 3 얻음\n\n자신이 복귀하려할 때 전투 인원이 꽉 찼으면, 무작위 뀽뀽이 1개체를 퇴각 시키고 자신만 전투 복귀
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136902].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [RunHallway]
   znaczenie tagów: [RunHallway] = 무리 이동 준비 / Preparing Herd Migration
   EN: Once 4 turns pass after this unit Retreats, this unit and all available "BongBongs spawned by this unit" Return to the battlefield. Then, gain 3 [RunHallway]\n\nIf all available combat participant spots are filled, Retreat a random BongBong unit and Return to the battlefield.
   PL:
1059. [[walpu8] Pasywka wroga [136903] — nazwa] 취약한 오렌지 버블
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136903].name
   limit: do 40 znaków
   EN: Fragile Orange Bubble
   PL:
1060. [[walpu8] Pasywka wroga [136903] — opis] 일방 공격으로 피격 시 받는 피해 +100%\n<color=#ff6000><mark color=#ff000040><b><u>탄환을 소모하는 스킬</color></mark></b></u>과 합 진행 시 합 위력 -3, 공격 스킬의 모든 코인이 일반 코인으로 변경됨.
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136903].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: When hit by Unopposed Attacks, take +100% damage\nWhen clashing against <color=#ff6000><mark color=#ff000040><b><u>Skills that spend Ammo</color></mark></b></u>, Clash Power -3 and convert all Coins on its Attack Skills to Regular Coins.
   PL:
1061. [[walpu8] Pasywka wroga [136903] — tekst klimatyczny] ‘아직 가공되지 않은 탄산을 품고 있는 버블은 맛있지만 강력한 산성을 띠니 다들 조심해. 작은 뀽뀽이들의 톡 쏘는 버블 탄산이면 몰라도, 저 정도로 큰 큥큥이들이 가지고 있는 원액을 뒤집어 썼다간 온몸이 녹아내릴 테니까.’
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136903].flavor
   limit: do 380 znaków
   EN: "I know those carbonated bubbles are tasty, but be careful around them, okay? They're unprocessed and highly acidic. Sure, a few spatters of little BongBongs' pop bubbles might not be so dangerous, but getting doused in the undiluted fluid of those massive BunBuns'll melt you guys into a puddle."
   PL:
1062. [[walpu8] Pasywka wroga [136904] — nazwa] 식품 생산
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136904].name
   limit: do 40 znaków
   EN: Food Production
   PL:
1063. [[walpu8] Pasywka wroga [136904] — opis] 적 처치 시 뀽뀽이 1개체 소환\n턴 종료 시 [RunHallway] 수치가 0이면, 다음 턴에 ‘뀽뀽이’를 가능한 만큼 소환
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136904].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [RunHallway]
   znaczenie tagów: [RunHallway] = 무리 이동 준비 / Preparing Herd Migration
   EN: On Kill, summon 1 BongBong\nTurn End: At 0 [RunHallway] Stack, summon as many BongBongs as possible next turn
   PL:
1064. [[walpu8] Pasywka wroga [136904] — tekst klimatyczny] ‘이런 탄산 제조법은 비밀이래요. 그들만의 레시피가 있다는 거죠.’
   źródło: Passives_Abnormality-walpu8.json :: dataList[id=136904].flavor
   limit: do 130 znaków
   EN: "Apparently, they've got this special, top-secret carbonation formula. Like an in-house recipe."
   PL:

## [x1p1c1] Wróg / część: Enemies-x1p1c1
- plik gry: `Enemies-x1p1c1.json`

1065. [[x1p1c1] Wróg / część [1365] — nazwa] 뽕이황쩨
   źródło: Enemies-x1p1c1.json :: dataList[id=1365].name
   limit: do 40 znaków
   EN: Da Boingy Empworoar
   PL:
1066. [[x1p1c1] Wróg / część [1365] — opis] 거대 봉이
   źródło: Enemies-x1p1c1.json :: dataList[id=1365].desc
   limit: do 120 znaków
   EN: Huge Bongy
   PL:
1067. [[x1p1c1] Wróg / część [136501] — nazwa] 몸통
   źródło: Enemies-x1p1c1.json :: dataList[id=136501].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1068. [[x1p1c1] Wróg / część [136501] — opis] 부위
   źródło: Enemies-x1p1c1.json :: dataList[id=136501].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1069. [[x1p1c1] Wróg / część [91039] — nazwa] 봉이 벌레
   źródło: Enemies-x1p1c1.json :: dataList[id=91039].name
   limit: do 40 znaków
   EN: Bongybug
   PL:
1070. [[x1p1c1] Wróg / część [91039] — opis] 1장 G사 직원(ver.봉이)
   źródło: Enemies-x1p1c1.json :: dataList[id=91039].desc
   limit: do 120 znaków
   EN: Chapter 1 G Corp. Staff (ver. Bongy)
   PL:
1071. [[x1p1c1] Wróg / część [91040] — nazwa] 봉이 경호단
   źródło: Enemies-x1p1c1.json :: dataList[id=91040].name
   limit: do 40 znaków
   EN: Bongyguard
   PL:
1072. [[x1p1c1] Wróg / część [91040] — opis] 2장 경비원 (ver.봉이)
   źródło: Enemies-x1p1c1.json :: dataList[id=91040].desc
   limit: do 120 znaków
   EN: Chapter 2 Security Guard (ver. Bongy)
   PL:
1073. [[x1p1c1] Wróg / część [91041] — nazwa] 봉이 요원
   źródło: Enemies-x1p1c1.json :: dataList[id=91041].name
   limit: do 40 znaków
   EN: Bongy Security
   PL:
1074. [[x1p1c1] Wróg / część [91041] — opis] 3장 K사 직원(ver.봉이)
   źródło: Enemies-x1p1c1.json :: dataList[id=91041].desc
   limit: do 120 znaków
   EN: Chapter 3 K Corp. Staff (ver. Bongy)
   PL:
1075. [[x1p1c1] Wróg / część [1384] — nazwa] 봉이 벌레
   źródło: Enemies-x1p1c1.json :: dataList[id=1384].name
   (powtórzenie elementu 1069 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1076. [[x1p1c1] Wróg / część [1384] — opis] 1장 G사 직원(ver.봉이)
   źródło: Enemies-x1p1c1.json :: dataList[id=1384].desc
   (powtórzenie elementu 1070 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1077. [[x1p1c1] Wróg / część [138401] — nazwa] 몸통
   źródło: Enemies-x1p1c1.json :: dataList[id=138401].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1078. [[x1p1c1] Wróg / część [138401] — opis] 부위
   źródło: Enemies-x1p1c1.json :: dataList[id=138401].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1079. [[x1p1c1] Wróg / część [1385] — nazwa] 봉이 경호단
   źródło: Enemies-x1p1c1.json :: dataList[id=1385].name
   (powtórzenie elementu 1071 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1080. [[x1p1c1] Wróg / część [1385] — opis] 2장 경비원 (ver.봉이)
   źródło: Enemies-x1p1c1.json :: dataList[id=1385].desc
   (powtórzenie elementu 1072 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1081. [[x1p1c1] Wróg / część [138501] — nazwa] 몸통
   źródło: Enemies-x1p1c1.json :: dataList[id=138501].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1082. [[x1p1c1] Wróg / część [138501] — opis] 부위
   źródło: Enemies-x1p1c1.json :: dataList[id=138501].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1083. [[x1p1c1] Wróg / część [1386] — nazwa] 봉이 요원
   źródło: Enemies-x1p1c1.json :: dataList[id=1386].name
   (powtórzenie elementu 1073 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1084. [[x1p1c1] Wróg / część [1386] — opis] 3장 K사 직원(ver.봉이)
   źródło: Enemies-x1p1c1.json :: dataList[id=1386].desc
   (powtórzenie elementu 1074 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1085. [[x1p1c1] Wróg / część [138601] — nazwa] 몸통
   źródło: Enemies-x1p1c1.json :: dataList[id=138601].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1086. [[x1p1c1] Wróg / część [138601] — opis] 부위
   źródło: Enemies-x1p1c1.json :: dataList[id=138601].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1087. [[x1p1c1] Wróg / część [1387] — nazwa] 거짓 봉이
   źródło: Enemies-x1p1c1.json :: dataList[id=1387].name
   limit: do 40 znaków
   EN: False Bongy
   PL:
1088. [[x1p1c1] Wróg / część [1387] — opis] 거대 봉이
   źródło: Enemies-x1p1c1.json :: dataList[id=1387].desc
   (powtórzenie elementu 1066 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [[x1p1c1] Wróg / część [138701] — nazwa] 몸통
   źródło: Enemies-x1p1c1.json :: dataList[id=138701].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1090. [[x1p1c1] Wróg / część [138701] — opis] 부위
   źródło: Enemies-x1p1c1.json :: dataList[id=138701].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [x1p1c1] Umiejętności wrogów / Anomalii — Skills_Abnormality-x1p1c1
- grupa rozdziału/trybu: `x1p1c1` · plik: `Skills_Abnormality-x1p1c1.json`

1091. [Umiejętność wroga [136501] (ulepszenie 1) — nazwa] 꼬!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136501].levelList[level=1].name
   limit: do 40 znaków
   EN: Cluck!
   PL:
1092. [Umiejętność wroga [136501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1093. [Umiejętność wroga [136501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL:
1094. [Umiejętność wroga [136501] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136501].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [Umiejętność wroga [136502] (ulepszenie 1) — nazwa] 꾸꼬!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].name
   limit: do 40 znaków
   EN: Cluckcoo!
   PL:
1096. [Umiejętność wroga [136502] (ulepszenie 1) — opis] [WideAreaRampage]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WideAreaRampage]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: [WideAreaRampage]
   PL:
1097. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1098. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 3 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 SP damage
   PL:
1099. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Vibration]
   PL:
1100. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1101. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 3 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1098 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1102. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 1099 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1103. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1104. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 3 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1098 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1105. [Umiejętność wroga [136502] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136502].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 1099 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1106. [Umiejętność wroga [136503] (ulepszenie 1) — nazwa] 뽀꼭!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].name
   limit: do 40 znaków
   EN: Bawkcoo!
   PL:
1107. [Umiejętność wroga [136503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1108. [Umiejętność wroga [136503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 1093 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1109. [Umiejętność wroga [136503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1110. [Umiejętność wroga [136503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1111. [Umiejętność wroga [136503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1093 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1112. [Umiejętność wroga [136503] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136503].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1113. [Umiejętność wroga [136504] (ulepszenie 1) — nazwa] 뿌꼭꼬!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136504].levelList[level=1].name
   limit: do 40 znaków
   EN: Bawkkawkcoo!
   PL:
1114. [Umiejętność wroga [136504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1115. [Umiejętność wroga [136504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
1116. [Umiejętność wroga [136504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Paralysis]
   PL:
1117. [Umiejętność wroga [136505] (ulepszenie 1) — nazwa] 뽕꼬뽀꽁!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].name
   limit: do 40 znaków
   EN: Bawkkawkcluckcoo!
   PL:
1118. [Umiejętność wroga [136505] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 50% 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL:
1119. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1120. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 1 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Paralysis]
   PL:
1121. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 정신력 3 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal 3 SP damage
   PL:
1122. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1123. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 1 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1124. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] 정신력 3 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 1121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1125. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1126. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 1 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1127. [Umiejętność wroga [136505] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttackHead] 정신력 3 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136505].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 1121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1128. [Umiejętność wroga [136506] (ulepszenie 1) — nazwa] 꾸꾹!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136506].levelList[level=1].name
   limit: do 40 znaków
   EN: Khhcluck!
   PL:
1129. [Umiejętność wroga [136506] (ulepszenie 1) — opis] [CanDuelGuard]\n[WinDuel] 정신력 5 피해
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[WinDuel] Deal 5 SP damage
   PL:
1130. [Umiejętność wroga [136506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=136506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1131. [Umiejętność wroga [138701] (ulepszenie 1) — nazwa] 끄!
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138701].levelList[level=1].name
   limit: do 40 znaków
   EN: Kgh!
   PL:
