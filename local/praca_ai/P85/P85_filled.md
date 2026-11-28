# Paczka AI P85 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 21/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P85_3c_przeciwnicy_i_anomalie_cz21.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P85_3c_przeciwnicy_i_anomalie_cz21.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [refraction6] Wróg / część: Enemies_Refraction6
- plik gry: `Enemies_Refraction6.json`

1. [[refraction6] Wróg / część [9571] — nazwa] 굴절된 매화침
   źródło: Enemies_Refraction6.json :: dataList[id=9571].name
   limit: do 40 znaków
   EN: Refracted Flower-burying Pin
   PL: Refracted Flower-burying Pin
2. [[refraction6] Wróg / część [9571] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9571].desc
   limit: do 120 znaków
   EN: Core
   PL: Core
3. [[refraction6] Wróg / część [957101] — nazwa] 매화침
   źródło: Enemies_Refraction6.json :: dataList[id=957101].name
   limit: do 40 znaków
   EN: Flower-burying Pin
   PL: Flower-burying Pin
4. [[refraction6] Wróg / część [957101] — opis] 부위
   źródło: Enemies_Refraction6.json :: dataList[id=957101].desc
   limit: do 120 znaków
   EN: Part
   PL: Część
5. [[refraction6] Wróg / część [9550] — nazwa] 굴절된 소지 아비 - 시오미 요루
   źródło: Enemies_Refraction6.json :: dataList[id=9550].name
   limit: do 70 znaków
   EN: The Refracted Pinky Nursefather - Shiomi Yoru
   PL: The Refracted Pinky Nursefather - Shiomi Yoru
6. [[refraction6] Wróg / część [9550] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9550].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [[refraction6] Wróg / część [9554] — nazwa] 굴절된 약지 아비 - 칼리스토
   źródło: Enemies_Refraction6.json :: dataList[id=9554].name
   limit: do 60 znaków
   EN: The Refracted Ring Nursefather - Callisto
   PL: The Refracted Ring Nursefather - Callisto
8. [[refraction6] Wróg / część [9554] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9554].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
9. [[refraction6] Wróg / część [9555] — nazwa] 굴절된 약지 제자 - 알비나
   źródło: Enemies_Refraction6.json :: dataList[id=9555].name
   limit: do 60 znaków
   EN: The Refracted Ring Apprentice - Albina
   PL: The Refracted Ring Apprentice - Albina
10. [[refraction6] Wróg / część [9555] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9555].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [[refraction6] Wróg / część [9551] — nazwa] 굴절된 검지 아비 - 뤼엔
   źródło: Enemies_Refraction6.json :: dataList[id=9551].name
   limit: do 60 znaków
   EN: The Refracted Index Nursefather - Rien
   PL: The Refracted Index Nursefather - Rien
12. [[refraction6] Wróg / część [9551] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9551].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [[refraction6] Wróg / część [9552] — nazwa] 굴절된 검지 아비 - 뤼엔
   źródło: Enemies_Refraction6.json :: dataList[id=9552].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [[refraction6] Wróg / część [9552] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9552].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [[refraction6] Wróg / część [9553] — nazwa] 굴절된 뒤틀린 호엔하임
   źródło: Enemies_Refraction6.json :: dataList[id=9553].name
   limit: do 50 znaków
   EN: Refracted Distorted Hohenheim
   PL: Refracted Distorted Hohenheim
16. [[refraction6] Wróg / część [9553] — opis] 본체
   źródło: Enemies_Refraction6.json :: dataList[id=9553].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction6] Umiejętności wrogów / Anomalii — Skills_Abnormality_Refraction6
- grupa rozdziału/trybu: `refraction6` · plik: `Skills_Abnormality_Refraction6.json`

17. [Umiejętność wroga [956301] (ulepszenie 1) — nazwa] 난격
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956301].levelList[level=1].name
   limit: do 40 znaków
   EN: Fluttering Havoc
   PL: Fluttering Havoc
18. [Umiejętność wroga [956301] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Combustion]과 [Laceration]의 합 8당 합 위력 +1 (최대 3)\n- 자신의 [Breath] 6당 피해량 +5% (최대 20%)\n- [Breath] 2 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956301].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [Laceration], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise
   EN: [WhenUse]\n- Clash Power +1 for every 8 ([Combustion] + [Laceration]) on target (max 3)\n- Deal +5% damage for every 6 [Breath] on self (max 20%)\n- Gain 2 [Breath]
   PL: [WhenUse]\n- Moc Starcia +1 za każde 8 ([Combustion] + [Laceration]) na celu (maks. 3)\n- zadaje +5% obrażeń za każde 6 [Breath] na sobie (maks. 20%)\n- zyskuje 2 [Breath]
19. [Umiejętność wroga [956301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
20. [Umiejętność wroga [956301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
21. [Umiejętność wroga [956301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1
22. [Umiejętność wroga [956301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
23. [Umiejętność wroga [956302] (ulepszenie 1) — nazwa] 분쇄
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956302].levelList[level=1].name
   limit: do 40 znaków
   EN: Pulverization
   PL: Pulverization
24. [Umiejętność wroga [956302] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Combustion]과 [Laceration]의 합 8당 합 위력 +1 (최대 3)\n- 자신의 [Breath] 6당 피해량 +5% (최대 20%)\n- [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956302].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [Laceration], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise
   EN: [WhenUse]\n- Clash Power +1 for every 8 ([Combustion] + [Laceration]) on target (max 3)\n- Deal +5% damage for every 6 [Breath] on self (max 20%)\n- Gain +2 [Breath] Count
   PL: [WhenUse]\n- Moc Starcia +1 za każde 8 ([Combustion] + [Laceration]) na celu (maks. 3)\n- zadaje +5% obrażeń za każde 6 [Breath] na sobie (maks. 20%)\n- zwiększa Licznik [Breath] o 2
25. [Umiejętność wroga [956302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
26. [Umiejętność wroga [956302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [956302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność wroga [956302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Umiejętność wroga [956303] (ulepszenie 1) — nazwa] 태동 시작
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956303].levelList[level=1].name
   limit: do 40 znaków
   EN: The Quickening
   PL: The Quickening
30. [Umiejętność wroga [956303] (ulepszenie 1) — opis] [CantDuel], [CantChangeTarget]\n이 공격 스킬이 가하는 피해는 0이 됨\n[WhenUse] 이번 턴 동안 모든 피해를 받지 않음\n[EndSkill] 스테이지 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956303].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [WhenUse], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel], [CantChangeTarget]\nThis Attack Skill deals 0 damage\n[WhenUse] Does not take damage for this turn\n[EndSkill] End the Encounter
   PL: [CantDuel], [CantChangeTarget]\nta Umiejętność ataku zadaje 0 obrażeń\n[WhenUse] w tej turze nie otrzymuje obrażeń\n[EndSkill] kończy walkę
31. [Umiejętność wroga [956303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
32. [Umiejętność wroga [956304] (ulepszenie 1) — nazwa] 나생 - 회귀
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956304].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangled Life - Regression
   PL: Entangled Life - Regression
33. [Umiejętność wroga [956304] (ulepszenie 1) — opis] 이 스킬과 합을 진행한 스킬의 <color=#ff6000><mark=#ff000040><b><u>공격 유형, 속성 유형</u></b></mark></color>이 다가오는 과거에 영향을 끼침\n- 2스테이지의 적들이 [HeatedWingScalesExplain] 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956304].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HeatedWingScalesExplain]
   znaczenie tagów: [HeatedWingScalesExplain] = 달궈진 비늘 가루 / Incandescent Scale Dust
   EN: <color=#ff6000><mark=#ff000040><b><u>Attack Type and Affinity</u></b></mark></color> of Skills that Clashed with this Skill affect the impending Past\n- Enemy units of Stage 2 gain [HeatedWingScalesExplain]
   PL: <color=#ff6000><mark=#ff000040><b><u>Typ Ataku i Atrybut</u></b></mark></color> Umiejętności, które przeprowadziły z tą Umiejętnością Starcie, wpływają na nadchodzącą Przeszłość\n- wrogowie 2. stadium zyskują [HeatedWingScalesExplain]
34. [Umiejętność wroga [956304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Umiejętność wroga [956305] (ulepszenie 1) — nazwa] 나생 - 현현
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956305].levelList[level=1].name
   limit: do 50 znaków
   EN: Entangled Life - Manifestation
   PL: Entangled Life - Manifestation
36. [Umiejętność wroga [956305] (ulepszenie 1) — opis] 이 스킬과 합을 진행한 스킬의 <color=#ff6000><mark=#ff000040><b><u>공격 유형, 속성 유형</u></b></mark></color>이 다가오는 현재에 영향을 끼침\n- 3스테이지의 적들이 [TransparentWingScalesExplain] 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956305].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TransparentWingScalesExplain]
   znaczenie tagów: [TransparentWingScalesExplain] = 예리한 비늘 가루 / Acuate Scale Dust
   EN: <color=#ff6000><mark=#ff000040><b><u>Attack Type and Affinity</u></b></mark></color> of Skills that Clashed with this Skill affect the impending Present\n- Enemy units of Stage 3 gain [TransparentWingScalesExplain]
   PL: <color=#ff6000><mark=#ff000040><b><u>Typ Ataku i Atrybut</u></b></mark></color> Umiejętności, które przeprowadziły z tą Umiejętnością Starcie, wpływają na nadchodzącą Teraźniejszość\n- wrogowie 3. stadium zyskują [TransparentWingScalesExplain]
37. [Umiejętność wroga [956305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [956306] (ulepszenie 1) — nazwa] 나생 - 도래
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956306].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangled Life - Advent
   PL: Entangled Life - Advent
39. [Umiejętność wroga [956306] (ulepszenie 1) — opis] 이 스킬과 합을 진행한 스킬의 <color=#ff6000><mark=#ff000040><b><u>공격 유형, 속성 유형</u></b></mark></color>이 다가오는 미래에 영향을 끼침\n- 4스테이지의 적들이 [RustedWingScalesExplain] 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956306].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RustedWingScalesExplain]
   znaczenie tagów: [RustedWingScalesExplain] = 녹슨 비늘 가루 / Rusted Scale Dust
   EN: <color=#ff6000><mark=#ff000040><b><u>Attack Type and Affinity</u></b></mark></color> of Skills that Clashed with this Skill affect the impending Future\n- Enemy units of Stage 4 gain [RustedWingScalesExplain]
   PL: <color=#ff6000><mark=#ff000040><b><u>Typ Ataku i Atrybut</u></b></mark></color> Umiejętności, które przeprowadziły z tą Umiejętnością Starcie, wpływają na nadchodzącą Przyszłość\n- wrogowie 4. stadium zyskują [RustedWingScalesExplain]
40. [Umiejętność wroga [956306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Umiejętność wroga [956401] (ulepszenie 1) — nazwa] 우화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956401].levelList[level=1].name
   limit: do 40 znaków
   EN: Eclosion
   PL: Eclosion
42. [Umiejętność wroga [956401] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n이 공격 스킬이 가하는 피해는 0이 됨\n[EndSkill] 스테이지 종료\n- 보호막이 파괴되었으면, 대신 다음 턴이 시작되어 <color=#ff6000><mark=#ff000040><b><u>특수한 선택지</u></b></mark></color>가 등장하고 이후 스테이지 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956401].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantDuel], [CantChangeTarget], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel][CantChangeTarget]\nThis Attack Skill deals 0 damage\n[EndSkill] End the Encounter\n- If the Shield is broken, proceed to the next turn instead and <color=#ff6000><mark=#ff000040><b><u>face a unique Choice Event</u></b></mark></color> before the Encounter ends
   PL: [CantDuel][CantChangeTarget]\nta Umiejętność ataku zadaje 0 obrażeń\n[EndSkill] kończy walkę\n- jeżeli Tarcza została zniszczona, zamiast tego rozpoczyna się następna tura, pojawia się <color=#ff6000><mark=#ff000040><b><u>unikatowy Wybór</u></b></mark></color>, a następnie walka się kończy
43. [Umiejętność wroga [956401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność wroga [956501] (ulepszenie 1) — nazwa] 우화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956501].levelList[level=1].name
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność wroga [956501] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n이 공격 스킬이 가하는 피해는 0이 됨\n[EndSkill] 스테이지 종료\n- 보호막이 파괴되었으면, 대신 다음 턴이 시작되어 <color=#ff6000><mark=#ff000040><b><u>특수한 선택지</u></b></mark></color>가 등장하고 이후 스테이지 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956501].levelList[level=1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Umiejętność wroga [956501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność wroga [956601] (ulepszenie 1) — nazwa] 우화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956601].levelList[level=1].name
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Umiejętność wroga [956601] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n이 공격 스킬이 가하는 피해는 0이 됨\n[EndSkill] 스테이지 종료\n- 보호막이 파괴되었으면, 대신 다음 턴이 시작되어 <color=#ff6000><mark=#ff000040><b><u>특수한 선택지</u></b></mark></color>가 등장하고 이후 스테이지 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956601].levelList[level=1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Umiejętność wroga [956601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Umiejętność wroga [956701] (ulepszenie 1) — nazwa] 난격
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956701].levelList[level=1].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [956701] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Combustion]과 [Laceration]의 합 8당 합 위력 +1 (최대 3)\n- 자신의 [Breath] 8당 피해량 +10% (최대 30%)\n- [Breath] 2 얻음\n- 체력이 66%/33% 미만이면, 마지막/모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956701].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [Laceration], [Breath], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse]\n- Clash Power +1 for every 8 ([Combustion] on target + [Laceration] on target) (max 3)\n- Deal +10% damage for every 8 [Breath] on self (max 30%)\n- Gain 2 [Breath]\n- At less than 66% HP, convert the final Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s
   PL: [WhenUse]\n- Moc Starcia +1 za każde 8 ([Combustion] + [Laceration]) na celu (maks. 3)\n- zadaje +10% obrażeń za każde 8 [Breath] na sobie (maks. 30%)\n- zyskuje 2 [Breath]\n- przy poniżej 66% HP ostatnia moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y
52. [Umiejętność wroga [956701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [956701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Umiejętność wroga [956701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność wroga [956701] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956701].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [956702] (ulepszenie 1) — nazwa] 분쇄
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956702].levelList[level=1].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [956702] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Combustion]과 [Laceration]의 합 8당 합 위력 +1 (최대 3)\n- 자신의 [Breath] 8당 피해량 +10% (최대 30%)\n- [Breath] 횟수 2 증가\n- 체력이 66%/33% 미만이면, 마지막/모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956702].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [Laceration], [Breath], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse]\n- Clash Power +1 for every 8 ([Combustion] + [Laceration]) on target (max 3)\n- Deal +10% damage for every 8 [Breath] on self (max 30%)\n- Gain +2 [Breath] Count\n- At less than 66% HP, convert the final Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s
   PL: [WhenUse]\n- Moc Starcia +1 za każde 8 ([Combustion] + [Laceration]) na celu (maks. 3)\n- zadaje +10% obrażeń za każde 8 [Breath] na sobie (maks. 30%)\n- zwiększa Licznik [Breath] o 2\n- przy poniżej 66% HP ostatnia moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y
58. [Umiejętność wroga [956702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [956702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność wroga [956702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [956702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność wroga [956703] (ulepszenie 1) — nazwa] 요란
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].name
   limit: do 40 znaków
   EN: Chaotic Turmoil
   PL: Chaotic Turmoil
63. [Umiejętność wroga [956703] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Combustion]과 [Laceration]의 합 6당 합 위력 +1 (최대 6)\n- 자신의 [Breath] 6당 합 위력 +1 (최대 3)\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>[ResultReduction] 2, [AttackDmgDown] 2</u></b></mark></color> 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Combustion], [Laceration], [Breath], [DefeatDuel], [ResultReduction], [AttackDmgDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [WhenUse]\n- Clash Power +1 for every 6 ([Combustion] + [Laceration]) on target (max 6)\n- Clash Power +1 for every 6 [Breath] on self (max 3)\n[DefeatDuel]\nGain <color=#ff6000><mark=#ff000040><b><u>2 [ResultReduction] and 2[AttackDmgDown]</u></b></mark></color>
   PL: [WhenUse]\n- Moc Starcia +1 za każde 6 ([Combustion] + [Laceration]) na celu (maks. 6)\n- Moc Starcia +1 za każde 6 [Breath] na sobie (maks. 3)\n[DefeatDuel]\nzyskuje <color=#ff6000><mark=#ff000040><b><u>2 [ResultReduction] i 2 [AttackDmgDown]</u></b></mark></color>
64. [Umiejętność wroga [956703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność wroga [956703] (ulepszenie 1) — moneta 1, efekt 2 — opis] 잃은 체력 33%당 이 코인 1회 재사용 (최대 2회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Reuse this Coin once for every 33% missing HP (max 2 times)
   PL: ponownie używa tej monety 1 raz za każde 33% brakującego HP (maks. 2 razy)
66. [Umiejętność wroga [956703] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Umiejętność wroga [956703] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Umiejętność wroga [956703] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956703].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
69. [Umiejętność wroga [956704] (ulepszenie 1) — nazwa] 단야
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956704].levelList[level=1].name
   limit: do 40 znaków
   EN: Temper and Cast
   PL: Temper and Cast
70. [Umiejętność wroga [956704] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 대상의 [Combustion] 6당 합 위력 +1 (최대 6)\n- 체력이 66%/33% 미만이면, 두 번째/모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956704].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Clash Power +1 for every 6 [Combustion] on target (max 6)\n- At less than 66% HP, convert the second Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s\n[DefeatDuel] Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Starcia +1 za każde 6 [Combustion] na celu (maks. 6)\n- przy poniżej 66% HP druga moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y\n[DefeatDuel] do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
71. [Umiejętność wroga [956704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion] and +1 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 1 [Combustion] i zwiększa Licznik [Combustion] o 1
72. [Umiejętność wroga [956704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Combustion] 1회 발동</u></b></mark></color>시키고 [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Activate [Combustion] on target once</u></b></mark></color>. Target loses 1 [Combustion] Count
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>aktywuje [Combustion] na celu 1 raz</u></b></mark></color>, cel traci 1 Licznik [Combustion]
73. [Umiejętność wroga [956705] (ulepszenie 1) — nazwa] 소훼
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].name
   limit: do 40 znaków
   EN: Immolation
   PL: Immolation
74. [Umiejętność wroga [956705] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 메인 타겟의 [Combustion] 6당 합 위력 +1 (최대 6)\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +([StackPastActivate] x 2)%</u></b></mark></color> (최대 60%)\n- 체력이 66%/33% 미만이면, 두 번째/모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Combustion], [StackPastActivate], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [StackPastActivate] = 과거 상태 / In the Past; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Clash Power +1 for every 6 [Combustion] on the main target (max 6)\n- <color=#ff6000><mark=#ff000040><b><u>Deal +([StackPastActivate] x 2)% damage</u></b></mark></color> (max 60%)\n- At less than 66% HP, convert the second Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s\n[DefeatDuel] Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Starcia +1 za każde 6 [Combustion] na głównym celu (maks. 6)\n- zadaje <color=#ff6000><mark=#ff000040><b><u>+([StackPastActivate] x 2)% obrażeń</u></b></mark></color> (maks. 60%)\n- przy poniżej 66% HP druga moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y\n[DefeatDuel] do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
75. [Umiejętność wroga [956705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 2
76. [Umiejętność wroga [956705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]
77. [Umiejętność wroga [956705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność wroga [956705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Combustion] 2회 발동</u></b></mark></color>시키고 [Combustion] 횟수 2 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Activate [Combustion] on target 2 times</u></b></mark></color>. Target loses 2 [Combustion] Count
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>aktywuje [Combustion] na celu 2 razy</u></b></mark></color>, cel traci 2 Liczniki [Combustion]
79. [Umiejętność wroga [956705] (ulepszenie 1) — moneta 3, efekt 3 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[Combustion] 1회 발동</u></b></mark></color>시키고 [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956705].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [Combustion]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Combustion] = 화상 / Burn
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, activate [Combustion] on the main target once</u></b></mark></color>. Target loses 1 [Combustion] Count
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color>, aktywuje na głównym celu <color=#ff6000><mark=#ff000040><b><u>[Combustion] 1 raz</u></b></mark></color>, cel traci 1 Licznik [Combustion]
80. [Umiejętność wroga [956706] (ulepszenie 1) — nazwa] 겁화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].name
   limit: do 40 znaków
   EN: Kalpāgni
   PL: Kalpāgni
81. [Umiejętność wroga [956706] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 메인 타겟의 [Combustion] 6당 최종 위력 +1 (최대 6)\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +([StackPastActivate] x 4)%</u></b></mark></color> (최대 120%)\n[WinDuel] [StackPastActivate] 5 얻음\n[DefeatDuel]\n- [StackPastActivate] 절반으로 감소 (소수점 버림)\n- [AttackDmgDown] 2, [Paralysis] 4 얻음\n- 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Combustion], [StackPastActivate], [WinDuel], [DefeatDuel], [AttackDmgDown], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [StackPastActivate] = 과거 상태 / In the Past; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Final Power +1 for every 6 [Combustion] on the main target (max 6)\n- <color=#ff6000><mark=#ff000040><b><u>Deal +([StackPastActivate] x 4)% damage</u></b></mark></color> (max 120%)\n[WinDuel] Gain 5 [StackPastActivate]\n[DefeatDuel]\n- Halve [StackPastActivate] (rounded down)\n- Gain 2 [AttackDmgDown] and 4 [Paralysis] \n- Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Końcowa +1 za każde 6 [Combustion] na głównym celu (maks. 6)\n- zadaje <color=#ff6000><mark=#ff000040><b><u>+([StackPastActivate] x 4)% obrażeń</u></b></mark></color> (maks. 120%)\n[WinDuel] zyskuje 5 [StackPastActivate]\n[DefeatDuel]\n- zmniejsza [StackPastActivate] o połowę (zaokrąglone w dół)\n- zyskuje 2 [AttackDmgDown] i 4 [Paralysis]\n- do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
82. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Combustion] 1회 발동</u></b></mark></color>시키고 [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Combustion] 2회 발동</u></b></mark></color>시키고 [Combustion] 횟수 2 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność wroga [956706] (ulepszenie 1) — moneta 4, efekt 3 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, 대상의 <color=#ff6000><mark=#ff000040><b><u>[Combustion] 1회 발동</u></b></mark></color>시키고 [Combustion] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956706].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [Combustion]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Combustion] = 화상 / Burn
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, activate [Combustion] on target once</u></b></mark></color>. Target loses 1 [Combustion] Count
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color>, aktywuje na celu <color=#ff6000><mark=#ff000040><b><u>[Combustion] 1 raz</u></b></mark></color>, cel traci 1 Licznik [Combustion]
91. [Umiejętność wroga [956707] (ulepszenie 1) — nazwa] 무상
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956707].levelList[level=1].name
   limit: do 40 znaków
   EN: Anitya
   PL: Anitya
92. [Umiejętność wroga [956707] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 자신의 [Breath] 6당 합 위력 +1, 피해량 +10% (각각 최대 6, 60%)\n- 체력이 66%/33% 미만이면, 두 번째/모든 코인이 [SuperCoin]으로 변경됨\n[BeforeAttack] [Breath] 2 얻음, [Breath] 횟수 2 증가\n[DefeatDuel] 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956707].levelList[level=1].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [SuperCoin], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Clash Power +1 and deal +10% damage for every 6 [Breath] on self (max 6 and 60%, respectively)\n- At less than 66% HP, convert the second Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s\n[BeforeAttack] Gain 2 [Breath] and +2 [Breath] Count\n[DefeatDuel] Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Starcia +1 i zadaje +10% obrażeń za każde 6 [Breath] na sobie (maks. odpowiednio 6 i 60%)\n- przy poniżej 66% HP druga moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y\n[BeforeAttack] zyskuje 2 [Breath] i zwiększa Licznik [Breath] o 2\n[DefeatDuel] do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
93. [Umiejętność wroga [956707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음, [Breath] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] and +1 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 1 [Breath] i zwiększa Licznik [Breath] o 1
94. [Umiejętność wroga [956707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 대상에게 <color=#ff6000><mark=#ff000040><b><u>(자신의 [Breath]/2)만큼 오만 피해</u></b></mark></color>를 입히고 [Breath] 횟수 1 감소 (소수점 버림)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal ([Breath] on self / 2) Pride damage on target</u></b></mark></color> and lose 1 [Breath] Count (rounded down)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje celowi <color=#ff6000><mark=#ff000040><b><u>(połowę własnego [Breath]) obrażeń Pychy</u></b></mark></color> i traci 1 Licznik [Breath] (zaokrąglone w dół)
95. [Umiejętność wroga [956708] (ulepszenie 1) — nazwa] 천공
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].name
   limit: do 40 znaków
   EN: Skypiercer
   PL: Skypiercer
96. [Umiejętność wroga [956708] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 자신의 [Breath] 6당 합 위력 +1, 피해량 +10% (각각 최대 6, 60%)\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +([StackPresentActivate] x 2)%</u></b></mark></color> (최대 60%)\n- 체력이 66%/33% 미만이면, 두 번째/모든 코인이 [SuperCoin]으로 변경됨\n[BeforeAttack] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[DefeatDuel] 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Breath], [StackPresentActivate], [SuperCoin], [BeforeAttack], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [StackPresentActivate] = 현재 상태 / In the Present; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Clash Power +1 and deal +10% damage for every 6 [Breath] on self (max 6 and 60%, respectively)\n- <color=#ff6000><mark=#ff000040><b><u>Deal +([StackPresentActivate] x 2)% damage</u></b></mark></color> (max 60%)\n- At less than 66% HP, convert the second Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s\n[BeforeAttack] Gain 3 [Breath] and +2 [Breath] Count\n[DefeatDuel] Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Starcia +1 i zadaje +10% obrażeń za każde 6 [Breath] na sobie (maks. odpowiednio 6 i 60%)\n- zadaje <color=#ff6000><mark=#ff000040><b><u>+([StackPresentActivate] x 2)% obrażeń</u></b></mark></color> (maks. 60%)\n- przy poniżej 66% HP druga moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y\n[BeforeAttack] zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 2\n[DefeatDuel] do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
97. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
98. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>피해량 +(자신의 [Breath] 횟수)%</u></b></mark></color> (최대 50%)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal +([Breath] Count on self)% damage</u></b></mark></color> (max 50%)
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje +(Licznik [Breath] na sobie)% obrażeń</u></b></mark></color> (maks. 50%)
101. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 3, efekt 3 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>피해량 +(자신의 [Breath] 횟수)%</u></b></mark></color> (최대 30%)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [Breath]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Breath] = 호흡 / Poise
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, deal +([Breath] Count on self)% damage</u></b></mark></color> (max 30%)
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color> zadaje <color=#ff6000><mark=#ff000040><b><u>+(Licznik [Breath] na sobie)% obrażeń</u></b></mark></color> (maks. 30%)
102. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>피해량 +(자신의 [Breath] x 2)%</u></b></mark></color> (최대 100%)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal +([Breath] on self x 2)% damage</u></b></mark></color> (max 100%)
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje +([Breath] na sobie x 2)% obrażeń</u></b></mark></color> (maks. 100%)
104. [Umiejętność wroga [956708] (ulepszenie 1) — moneta 4, efekt 3 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>피해량 +(자신의 [Breath])%</u></b></mark></color> (최대 50%)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956708].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [Breath]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Breath] = 호흡 / Poise
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, deal +([Breath] on self)% damage</u></b></mark></color> (max 50%)
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color> zadaje <color=#ff6000><mark=#ff000040><b><u>+([Breath] na sobie)% obrażeń</u></b></mark></color> (maks. 50%)
105. [Umiejętność wroga [956709] (ulepszenie 1) — nazwa] 파사
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956709].levelList[level=1].name
   limit: do 40 znaków
   EN: Smite the Wicked
   PL: Smite the Wicked
106. [Umiejętność wroga [956709] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 자신의 [Breath] 6당 최종 위력 +1, 피해량 +20% (각각 최대 6, 120%)\n- [Breath] 4 얻음, [Breath] 횟수 4 증가\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +([StackPresentActivate] x 4)% (최대 120%)</u></b></mark></color>\n[BeforeAttack] 자신의 [Breath] 위력이 20을 초과하면 초과되는 [Breath]을 최대 20까지 소모하여, 피해량 +(소모한 수치 x 5)% (최대 100%)\n- 합 패배 시, 발동하지 않음\n[WinDuel] [StackPresentActivate] 5 얻음\n[DefeatDuel]\n- [StackPresentActivate] 절반으로 감소 (소수점 버림)\n- [AttackDmgDown] 2, [Paralysis] 1 얻음\n- 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음\n[EndSkill] 대상이 사망하였다면, 이 스킬을 체력이 가장 높은 대상에게 재사용 (턴당 1회)\n- 합 패배 시, 발동하지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956709].levelList[level=1].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Breath], [StackPresentActivate], [BeforeAttack], [WinDuel], [DefeatDuel], [AttackDmgDown], [Paralysis], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [StackPresentActivate] = 현재 상태 / In the Present; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Paralysis] = 마비 / Paralyze …
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Final Power +1 and deal +20% damage for every 6 [Breath] on self (max 6 and 120%, respectively)\n- Gain 4 [Breath] and +4 [Breath] Count\n- <color=#ff6000><mark=#ff000040><b><u>Deal +([StackPresentActivate] x 4)% damage (max 120%)</u></b></mark></color>\n[BeforeAttack] If this unit has 20+ [Breath] Potency, consume up to 20 surplus [Breath] Potency past 20 to deal +([Breath] consumed x 5)% damage (max 100%)\n- On Clash Lose, this effect does not activate\n[WinDuel] Gain 5 [StackPresentActivate]\n[DefeatDuel]\n- Halve [StackPresentActivate] (rounded down)\n- Gain 2 [AttackDmgDown] and 1 [Paralysis]\n- Target cannot be Staggered until this Skill's Attack End\n[EndSkill] If target is killed, Reuse this Skill on the target that has the highest HP (once per turn)\n- On Clash Lose, this effect does not activate
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Końcowa +1 i zadaje +20% obrażeń za każde 6 [Breath] na sobie (maks. odpowiednio 6 i 120%)\n- zyskuje 4 [Breath] i zwiększa Licznik [Breath] o 4\n- zadaje <color=#ff6000><mark=#ff000040><b><u>+([StackPresentActivate] x 4)% obrażeń (maks. 120%)</u></b></mark></color>\n[BeforeAttack] jeżeli Siła [Breath] tej jednostki przekracza 20, zużywa nadwyżkową Siłę [Breath] ponad 20 (do maks. 20), zadając +(zużyte [Breath] x 5)% obrażeń (maks. 100%)\n- nie aktywuje się w razie przegranej Starcia\n[WinDuel] zyskuje 5 [StackPresentActivate]\n[DefeatDuel]\n- zmniejsza [StackPresentActivate] o połowę (zaokrąglone w dół)\n- zyskuje 2 [AttackDmgDown] i 1 [Paralysis]\n- do końca Ataku tą Umiejętnością cel nie może być Oszołamiony\n[EndSkill] jeżeli cel zginął, ponownie używa tej Umiejętności na celu z najwyższym HP (1 raz na turę)\n- nie aktywuje się w razie przegranej Starcia
107. [Umiejętność wroga [956709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Umiejętność wroga [956709] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상의 <color=#ff6000><mark=#ff000040><b><u>관통 내성이 약점(1.5) 미만이면, 약점(1.5)으로 취급</u></b></mark></color>\n- 합 패배 시, 발동하지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: <color=#ff6000><mark=#ff000040><b><u>If target's Pierce Resist. is below "Weak" (1.5), treat is as Weak (1.5)</u></b></mark></color>\n- On Clash Lose, this effect does not activate
   PL: jeżeli <color=#ff6000><mark=#ff000040><b><u>Odporność na Przebicie celu jest niższa niż „słaba" (1.5), traktuje ją jako „słabą" (1.5)</u></b></mark></color>\n- nie aktywuje się w razie przegranej Starcia
109. [Umiejętność wroga [956709] (ulepszenie 1) — moneta 1, efekt 3 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>이 코인 피해량의 50%만큼 추가 관통 피해</u></b></mark></color>를 입힘
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956709].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, deal +(50% of this Coin's damage)% bonus Pierce damage</u></b></mark></color>
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color> zadaje <color=#ff6000><mark=#ff000040><b><u>dodatkowe obrażenia Przebicia równe 50% obrażeń tej monety</u></b></mark></color>
110. [Umiejętność wroga [956710] (ulepszenie 1) — nazwa] 부식
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956710].levelList[level=1].name
   limit: do 40 znaków
   EN: Corrosive Disintegration
   PL: Corrosive Disintegration
111. [Umiejętność wroga [956710] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 대상의 [Laceration] 6당 합 위력 +1 (최대 6)\n- 체력이 66%/33% 미만이면, 두 번째/모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956710].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- Clash Power +1 for every 6 [Laceration] on target (max 6)\n- At less than 66% HP, convert the second Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s\n[DefeatDuel] Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Starcia +1 za każde 6 [Laceration] na celu (maks. 6)\n- przy poniżej 66% HP druga moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y\n[DefeatDuel] do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
112. [Umiejętność wroga [956710] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956710].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration] and +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 1 [Laceration] i zwiększa Licznik [Laceration] o 1
113. [Umiejętność wroga [956710] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Laceration] 1회 발동</u></b></mark></color>시키고 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956710].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Activate [Laceration] on target once</u></b></mark></color>. Target loses 1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>aktywuje [Laceration] na celu 1 raz</u></b></mark></color>, cel traci 1 Licznik [Laceration]
114. [Umiejętność wroga [956711] (ulepszenie 1) — nazwa] 후멸
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956711].levelList[level=1].name
   limit: do 40 znaków
   EN: Rotting Annihilation
   PL: Rotting Annihilation
115. [Umiejętność wroga [956711] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n이 스킬과 합을 진행하는 동안 <color=#ff6000><mark=#ff000040><b><u>메인 타겟의 [Laceration] 횟수가 1 미만으로 내려가지 않음</u></b></mark></color>\n[WhenUse]\n- 메인 타겟의 [Laceration] 6당 합 위력 +1 (최대 6)\n- 피해량 +([StackFutureActivate] x 2)% (최대 60%)\n- 체력이 66%/33% 미만이면, 두 번째/모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956711].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Laceration], [WhenUse], [StackFutureActivate], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [StackFutureActivate] = 미래 상태 / In the Future; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\nWhile Clashing with this Skill, <color=#ff6000><mark=#ff000040><b><u>the main target's [Laceration] Count does not drop below 1</u></b></mark></color>\n[WhenUse]\n- Clash Power +1 for every 6 [Laceration] on the main target (max 6)\n- Deal +([StackFutureActivate] x 2)% damage (max 60%)\n- At less than 66% HP, convert the second Coin into [SuperCoin]\n- At less than 33% HP, convert all Coins into [SuperCoin]s\n[DefeatDuel] Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\ndopóki toczy Starcie z tą Umiejętnością, <color=#ff6000><mark=#ff000040><b><u>Licznik [Laceration] głównego celu nie spada poniżej 1</u></b></mark></color>\n[WhenUse]\n- Moc Starcia +1 za każde 6 [Laceration] na głównym celu (maks. 6)\n- zadaje +([StackFutureActivate] x 2)% obrażeń (maks. 60%)\n- przy poniżej 66% HP druga moneta zmienia się w [SuperCoin]\n- przy poniżej 33% HP wszystkie monety zmieniają się w [SuperCoin]y\n[DefeatDuel] do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
116. [Umiejętność wroga [956711] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 2
117. [Umiejętność wroga [956711] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Laceration] 2회 발동</u></b></mark></color>시키고 [Laceration] 횟수 2 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Activate [Laceration] on target 2 times</u></b></mark></color>. Target loses 2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>aktywuje [Laceration] na celu 2 razy</u></b></mark></color>, cel traci 2 Liczniki [Laceration]
118. [Umiejętność wroga [956711] (ulepszenie 1) — moneta 2, efekt 2 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[Laceration] 1회 발동</u></b></mark></color>시키고 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956711].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [Laceration]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Laceration] = 출혈 / Bleed
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, activate [Laceration] on the main target once</u></b></mark></color>. Target loses 1 [Laceration] Count
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color>, aktywuje na głównym celu <color=#ff6000><mark=#ff000040><b><u>[Laceration] 1 raz</u></b></mark></color>, cel traci 1 Licznik [Laceration]
119. [Umiejętność wroga [956712] (ulepszenie 1) — nazwa] 혈화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].name
   limit: do 40 znaków
   EN: Bloodflower
   PL: Bloodflower
120. [Umiejętność wroga [956712] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n이 스킬과 합을 진행하는 동안 <color=#ff6000><mark=#ff000040><b><u>메인 타겟의 [Laceration] 횟수가 1 미만으로 내려가지 않음</u></b></mark></color>\n[WhenUse]\n- 메인 타겟의 [Laceration] 6당 최종 위력 +1 (최대 6)\n- 피해량 +([StackFutureActivate] x 4)% (최대 120%)\n[WinDuel] [StackFutureActivate] 5 얻음\n[DefeatDuel]\n- [StackFutureActivate] 절반으로 감소 (소수점 버림)\n- [AttackDmgDown] 2, [Paralysis] 2 얻음\n- 이 스킬의 공격 종료시까지 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Laceration], [WhenUse], [StackFutureActivate], [WinDuel], [DefeatDuel], [AttackDmgDown], [Paralysis]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [StackFutureActivate] = 미래 상태 / In the Future; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\nWhile Clashing with this Skill, <color=#ff6000><mark=#ff000040><b><u>the main target's [Laceration] Count does not drop below 1</u></b></mark></color>\n[WhenUse]\n- Final Power +1 for every 6 [Laceration] on the main target (max 6)\n- Deal +([StackFutureActivate] x 4)% damage (max 120%)\n[WinDuel] Gain 5 [StackFutureActivate]\n[DefeatDuel]\n- Halve [StackFutureActivate] (rounded down)\n- Gain 2 [AttackDmgDown] and 2 [Paralysis]\n- Target cannot be Staggered until this Skill's Attack End
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\ndopóki toczy Starcie z tą Umiejętnością, <color=#ff6000><mark=#ff000040><b><u>Licznik [Laceration] głównego celu nie spada poniżej 1</u></b></mark></color>\n[WhenUse]\n- Moc Końcowa +1 za każde 6 [Laceration] na głównym celu (maks. 6)\n- zadaje +([StackFutureActivate] x 4)% obrażeń (maks. 120%)\n[WinDuel] zyskuje 5 [StackFutureActivate]\n[DefeatDuel]\n- zmniejsza [StackFutureActivate] o połowę (zaokrąglone w dół)\n- zyskuje 2 [AttackDmgDown] i 2 [Paralysis]\n- do końca Ataku tą Umiejętnością cel nie może być Oszołamiony
121. [Umiejętność wroga [956712] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Umiejętność wroga [956712] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 1 [Laceration] i zwiększa Licznik [Laceration] o 2
123. [Umiejętność wroga [956712] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność wroga [956712] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i 3 Licznika [Laceration]
125. [Umiejętność wroga [956712] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[Laceration] 2회 발동</u></b></mark></color>시키고 [Laceration] 횟수 2 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [956712] (ulepszenie 1) — moneta 2, efekt 4 — opis] [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>체력이 33% 미만</u></b></mark></color>이면, 대상의 <color=#ff6000><mark=#ff000040><b><u>[Laceration] 1회 발동</u></b></mark></color>시키고 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956712].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [Laceration]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [Laceration] = 출혈 / Bleed
   EN: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>At less than 33% HP, activate [Laceration] on target once</u></b></mark></color>. Target loses 1 [Laceration] Count
   PL: [DefeatDuelAttack]\n<color=#ff6000><mark=#ff000040><b><u>przy poniżej 33% HP</u></b></mark></color>, aktywuje na celu <color=#ff6000><mark=#ff000040><b><u>[Laceration] 1 raz</u></b></mark></color>, cel traci 1 Licznik [Laceration]
127. [Umiejętność wroga [956801] (ulepszenie 1) — nazwa] 역린지화[逆鱗之禍]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].name
   limit: do 50 znaków
   EN: Wrath of the Inverted Scale [逆鱗之禍]
   PL: Wrath of the Inverted Scale [逆鱗之禍]
128. [Umiejętność wroga [956801] (ulepszenie 1) — opis] 이 스킬은 <color=#ff6000><mark=#ff000040><b><u>메인 타겟으로 피격</u></b></mark></color> 시에만 발동\n[WhenUse] 자신이 보유한 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 모두 소모</u></b></mark></color>. 소모한 만큼 마지막 코인 재사용 (최대 5회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [YesdragonSelfRefraction]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: This Skill activates only when <color=#ff6000><mark=#ff000040><b><u>the "Inverted Scale" Part is hit as the main target</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Consume all [YesdragonSelfRefraction]</u></b></mark></color> on self and Reuse the final Coin (# of Stacks consumed) times (max 5 times)
   PL: ta Umiejętność aktywuje się tylko gdy <color=#ff6000><mark=#ff000040><b><u>część „Inverted Scale" zostanie trafiona jako główny cel</u></b></mark></color>\n[WhenUse] zużywa <color=#ff6000><mark=#ff000040><b><u>wszystkie własne [YesdragonSelfRefraction]</u></b></mark></color> i ponownie używa ostatniej monety (liczba zużytych Stosów) razy (maks. 5)
129. [Umiejętność wroga [956801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [956801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] zadaje 5 obrażeń SP
131. [Umiejętność wroga [956801] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EnemyKill] 메인 타겟 처치 시, 해당 스킬이 [WideAreaRampage]로 변경됨
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [WideAreaRampage]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: [EnemyKill] Upon killing the main target, apply the [WideAreaRampage] effect on this Skill
   PL: [EnemyKill] po zabiciu głównego celu, nadaje tej Umiejętności efekt [WideAreaRampage]
132. [Umiejętność wroga [956801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność wroga [956801] (ulepszenie 1) — moneta 2, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음. [WideAreaRampage]가 되었다면, 해당 효과 비활성화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WideAreaRampage]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: This Coin damages only the main target. If [WideAreaRampage] is applied, this Coin damages all targets
   PL: ta moneta zadaje obrażenia tylko głównemu celowi. jeżeli aktywny jest [WideAreaRampage], ta moneta zadaje obrażenia wszystkim celom
134. [Umiejętność wroga [956801] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956801].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
135. [Umiejętność wroga [956802] (ulepszenie 1) — nazwa] 섬뢰[閃雷]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956802].levelList[level=1].name
   limit: do 40 znaków
   EN: Levinflash [閃雷]
   PL: Levinflash [閃雷]
136. [Umiejętność wroga [956802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] nakłada 2 [Burst]
137. [Umiejętność wroga [956802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [956803] (ulepszenie 1) — nazwa] 용성[龍聲]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956803].levelList[level=1].name
   limit: do 40 znaków
   EN: Roar of the Dragon [龍聲]
   PL: Roar of the Dragon [龍聲]
139. [Umiejętność wroga [956803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
140. [Umiejętność wroga [956803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
141. [Umiejętność wroga [956803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
142. [Umiejętność wroga [956804] (ulepszenie 1) — nazwa] 낙침[落針]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956804].levelList[level=1].name
   limit: do 40 znaków
   EN: The Descending Pin [落針]
   PL: The Descending Pin [落針]
143. [Umiejętność wroga [956804] (ulepszenie 1) — opis] [WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 2당</u></b></mark></color>, 기본 위력 +1\n[WhenUse] 대상에게 [Binding] 혹은 [Paralysis]가 있으면, 기본 위력 +2\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>다음 턴에 <noparse>매화침</noparse> 소환</u></b></mark></color>\n[DefeatDuel] 대상의 정신력 5 회복\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u><noparse>매화침</noparse>을 소환하지 않으며</u></b></mark></color>, 머리 부위가 <color=#ff6000><mark=#ff000040><b><u>고정 피해</u></b></mark></color>를 받음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956804].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, <noparse>, </noparse>, \n, [WhenUse], [YesdragonSelfRefraction], [Binding], [Paralysis], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [Binding] = 속박 / Bind; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 <color=#ff6000><mark=#ff000040><b><u>for every 2 [YesdragonSelfRefraction]</u></b></mark></color> on self\n[WhenUse] If target has [Binding] or [Paralysis], Base Power +2\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Spawn "Flower-burying Pin" next turn</u></b></mark></color>\n[DefeatDuel] Heal 5 SP on target\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>Does not spawn "Flower-burying Pin"</u></b></mark></color>, and the head takes <color=#ff6000><mark=#ff000040><b><u>fixed damage</u></b></mark></color>
   PL: [WhenUse] Moc Bazowa +1 <color=#ff6000><mark=#ff000040><b><u>za każde 2 [YesdragonSelfRefraction]</u></b></mark></color> na sobie\n[WhenUse] jeżeli cel ma [Binding] lub [Paralysis], Moc Bazowa +2\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>przyzywa "<noparse>Flower-burying Pin</noparse>" w następnej turze</u></b></mark></color>\n[DefeatDuel] odnawia celowi 5 Poczytalności\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>nie przyzywa "<noparse>Flower-burying Pin</noparse>"</u></b></mark></color>, a głowa otrzymuje <color=#ff6000><mark=#ff000040><b><u>stałe obrażenia</u></b></mark></color>
144. [Umiejętność wroga [956804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 [Burst] i 2 Licznika [Burst]
145. [Umiejętność wroga [956805] (ulepszenie 1) — nazwa] 용권[龍卷]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956805].levelList[level=1].name
   limit: do 40 znaków
   EN: Draconic Vortex [龍卷]
   PL: Draconic Vortex [龍卷]
146. [Umiejętność wroga [956805] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 [Binding] 혹은 [Paralysis]가 있으면, 코인 위력 +1\n[DefeatDuel] 메인 타겟에게 <color=#ff6000><mark=#ff000040><b><u>[YesdragonWind] 부여</u></b></mark></color>
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956805].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Binding], [Paralysis], [DefeatDuel], [YesdragonWind]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]; [YesdragonWind] = 변덕스러운 자비 / Capricious Mercy
   EN: [WhenUse] If the main target has [Binding] or [Paralysis], Coin Power +1\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>Apply [YesdragonWind]</u></b></mark></color> on the main target
   PL: [WhenUse] jeżeli główny cel ma [Binding] lub [Paralysis], Moc Monet +1\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>nakłada [YesdragonWind]</u></b></mark></color> na główny cel
147. [Umiejętność wroga [956805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Burst]
148. [Umiejętność wroga [956805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] nakłada 2 [Burst]
149. [Umiejętność wroga [956805] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956805].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [956806] (ulepszenie 1) — nazwa] 적우[積雨]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].name
   limit: do 40 znaków
   EN: Gathering Rain [積雨]
   PL: Gathering Rain [積雨]
151. [Umiejętność wroga [956806] (ulepszenie 1) — opis] [WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 1당</u></b></mark></color>, 기본 위력 +1\n[WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 5 이상이면</u></b></mark></color>, 코인 위력 +1, 가중치 +1\n[DefeatDuel] 피해량이 80%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [YesdragonSelfRefraction], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 <color=#ff6000><mark=#ff000040><b><u>for every [YesdragonSelfRefraction]</u></b></mark></color> on self\n[WhenUse] If this unit has <color=#ff6000><mark=#ff000040><b><u>5+ [YesdragonSelfRefraction]</u></b></mark></color>, Coin Power +1 and gain +1 Atk Weight\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Bazowa +1 <color=#ff6000><mark=#ff000040><b><u>za każdy [YesdragonSelfRefraction]</u></b></mark></color> na sobie\n[WhenUse] jeżeli ta jednostka ma <color=#ff6000><mark=#ff000040><b><u>5+ [YesdragonSelfRefraction]</u></b></mark></color>, Moc Monet +1 i Waga Ataku +1\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
152. [Umiejętność wroga [956806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Umiejętność wroga [956806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [956806] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Burst]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Burst]
155. [Umiejętność wroga [956806] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [956806] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction]이 5 이상이면, 이 코인 재사용</u></b></mark></color> (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [YesdragonSelfRefraction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: [OnSucceedAttack] If this unit has <color=#ff6000><mark=#ff000040><b><u>5+ [YesdragonSelfRefraction], Reuse this Coin</u></b></mark></color> (once per Skill)
   PL: [OnSucceedAttack] jeżeli ta jednostka ma <color=#ff6000><mark=#ff000040><b><u>5+ [YesdragonSelfRefraction], ponownie używa tej monety</u></b></mark></color> (1 raz na Umiejętność)
157. [Umiejętność wroga [956806] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956806].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Burst] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +2 Licznika [Burst]
158. [Umiejętność wroga [956807] (ulepszenie 1) — nazwa] 낙뢰[落雷]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956807].levelList[level=1].name
   limit: do 40 znaków
   EN: Levinfall [落雷]
   PL: Levinfall [落雷]
159. [Umiejętność wroga [956807] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n<color=#ff6000><mark=#ff000040><b><u><noparse>매화침</noparse>을 타겟으로 지정</u></b></mark></color>\n<noparse>매화침</noparse>이 사망했을 경우 해당 스킬이 취소됨
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956807].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, <noparse>, </noparse>, </u>, </b>, </mark>, </color>, \n, [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantDuel][CantChangeTarget] \n<color=#ff6000><mark=#ff000040><b><u>Targets "Flower-burying Pin"</u></b></mark></color>\nIf "Flower-burying Pin" is destroyed, cancel this Skill
   PL: [CantDuel][CantChangeTarget]\n<color=#ff6000><mark=#ff000040><b><u>wskazuje "<noparse>Flower-burying Pin</noparse>" jako cel</u></b></mark></color>\njeżeli "<noparse>Flower-burying Pin</noparse>" zginie, ta Umiejętność zostaje anulowana
160. [Umiejętność wroga [956807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst] and +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 5 [Burst] i zwiększa Licznik [Burst] o 3
161. [Umiejętność wroga [956807] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 50% 확률로 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956807].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] 50% chance to inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttack] 50% szans na nałożenie 1 [Paralysis] w następnej turze
162. [Umiejętność wroga [956901] (ulepszenie 1) — nazwa] 용지첨[龍之櫼]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956901].levelList[level=1].name
   limit: do 40 znaków
   EN: The Dragon's Wedge [龍之櫼]
   PL: The Dragon's Wedge [龍之櫼]
163. [Umiejętność wroga [956901] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 <color=#ff6000><mark=#ff000040><b><u>[DragonLanceRefraction] 1 얻음</u></b></mark></color>\n[DefeatDuel] 전투 시작 시 효과가 취소됨. 다음 턴에 [Endurance] 3 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956901].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CanDuelGuard], [StartBattle], [DragonLanceRefraction], [DefeatDuel], [Endurance]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [DragonLanceRefraction] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: [CanDuelGuard]\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>Gain 1 [DragonLanceRefraction]</u></b></mark></color> next turn\n[DefeatDuel] Cancel the Combat Start effect. Gain 3 [Endurance] next turn
   PL: [CanDuelGuard]\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [DragonLanceRefraction]</u></b></mark></color> w następnej turze\n[DefeatDuel] anuluje efekt z początku walki. zyskuje 3 [Endurance] w następnej turze
164. [Umiejętność wroga [956901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność wroga [956902] (ulepszenie 1) — nazwa] 역린지화[逆鱗之禍]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].name
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność wroga [956902] (ulepszenie 1) — opis] [WhenUse] 자신이 보유한 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 모두 소모</u></b></mark></color>. 소모한 만큼 마지막 코인 재사용 (최대 5회)\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [YesdragonSelfRefraction], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>Consume all [YesdragonSelfRefraction]</u></b></mark></color> on self and Reuse the final Coin (# of Stacks consumed) times (max 5 times)\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] zużywa <color=#ff6000><mark=#ff000040><b><u>wszystkie własne [YesdragonSelfRefraction]</u></b></mark></color> i ponownie używa ostatniej monety (liczba zużytych Stosów) razy (maks. 5)\n[DefeatDuel] zadaje o 50% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
167. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EnemyKill] 메인 타겟 처치 시, 해당 스킬이 [WideAreaRampage]로 변경됨
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 2, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음. [WideAreaRampage]가 되었다면, 해당 효과 비활성화
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [956902] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956902].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [CondensedBloodRefraction]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [CondensedBloodRefraction] = 용혈[龍血] / Dragon's Blood [龍血]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [CondensedBloodRefraction]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [CondensedBloodRefraction]
174. [Umiejętność wroga [956903] (ulepszenie 1) — nazwa] 섬뢰[閃雷]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].name
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Umiejętność wroga [956903] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 정신력이 35 미만이면, 기본 위력 +1\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If the main target has less than 35 SP, Base Power +1\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli główny cel ma poniżej 35 Poczytalności, Moc Bazowa +1\n[DefeatDuel] zadaje o 50% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
176. [Umiejętność wroga [956903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [956903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [956903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [CondensedBloodRefraction]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [CondensedBloodRefraction] = 용혈[龍血] / Dragon's Blood [龍血]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [CondensedBloodRefraction] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +1 Licznika [CondensedBloodRefraction]
179. [Umiejętność wroga [956903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [956903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [956903] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956903].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Paralysis] w następnej turze
182. [Umiejętność wroga [956904] (ulepszenie 1) — nazwa] 용성[龍聲]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].name
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [956904] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 정신력이 35 미만이면, 코인 위력 +1\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If the main target has less than 35 SP, Coin Power +1\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli główny cel ma poniżej 35 Poczytalności, Moc Monet +1\n[DefeatDuel] zadaje o 50% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
184. [Umiejętność wroga [956904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [956904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 SP damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 5 obrażeń SP
186. [Umiejętność wroga [956904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [956904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [956904] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956904].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [CondensedBloodRefraction]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [CondensedBloodRefraction] = 용혈[龍血] / Dragon's Blood [龍血]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [CondensedBloodRefraction] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +2 Licznika [CondensedBloodRefraction]
189. [Umiejętność wroga [956905] (ulepszenie 1) — nazwa] 낙침[落針]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956905].levelList[level=1].name
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność wroga [956905] (ulepszenie 1) — opis] [WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 2당</u></b></mark></color>, 기본 위력 +1\n[WhenUse] 대상에게 [Binding] 혹은 [Paralysis]가 있으면, 기본 위력 +2\n[WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 5 이상이면</u></b></mark></color>, 코인 위력 +1\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>다음 턴에 <noparse>매화침</noparse> 소환</u></b></mark></color>\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u><noparse>매화침</noparse>을 소환하지 않음</u></b></mark></color>
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956905].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, <noparse>, </noparse>, \n, [WhenUse], [YesdragonSelfRefraction], [Binding], [Paralysis], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [Binding] = 속박 / Bind; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 <color=#ff6000><mark=#ff000040><b><u>for every 2 [YesdragonSelfRefraction]</u></b></mark></color> on self\n[WhenUse] If target has [Binding] or [Paralysis], Base Power +2\n[WhenUse] If this unit has <color=#ff6000><mark=#ff000040><b><u>5+ [YesdragonSelfRefraction]</u></b></mark></color>, Coin Power +1\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Spawn "Flower-burying Pin" next turn</u></b></mark></color>\n[DefeatDuel]<color=#ff6000><mark=#ff000040><b><u>Does not spawn "Flower-burying Pin"</u></b></mark></color>
   PL: [WhenUse] Moc Bazowa +1 <color=#ff6000><mark=#ff000040><b><u>za każde 2 [YesdragonSelfRefraction]</u></b></mark></color> na sobie\n[WhenUse] jeżeli cel ma [Binding] lub [Paralysis], Moc Bazowa +2\n[WhenUse] jeżeli ta jednostka ma <color=#ff6000><mark=#ff000040><b><u>5+ [YesdragonSelfRefraction]</u></b></mark></color>, Moc Monet +1\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>przyzywa "<noparse>Flower-burying Pin</noparse>" w następnej turze</u></b></mark></color>\n[DefeatDuel]<color=#ff6000><mark=#ff000040><b><u>nie przyzywa "<noparse>Flower-burying Pin</noparse>"</u></b></mark></color>
191. [Umiejętność wroga [956905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [956905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [956906] (ulepszenie 1) — nazwa] 용권[龍卷]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].name
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [956906] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 [Binding] 혹은 [Paralysis]가 있으면, 코인 위력 +1
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Binding], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind; [Paralysis] = 마비 / Paralyze
   EN: [WhenUse] If the main target has [Binding] or [Paralysis], Coin Power +1
   PL: [WhenUse] jeżeli główny cel ma [Binding] lub [Paralysis], Moc Monet +1
195. [Umiejętność wroga [956906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [956906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [CondensedBloodRefraction] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CondensedBloodRefraction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CondensedBloodRefraction] = 용혈[龍血] / Dragon's Blood [龍血]
   EN: [OnSucceedAttack] Inflict +1 [CondensedBloodRefraction] Count
   PL: [OnSucceedAttack] nakłada +1 Licznika [CondensedBloodRefraction]
197. [Umiejętność wroga [956906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [956906] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [CondensedBloodRefraction] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [956906] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [956906] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [CondensedBloodRefraction] 횟수 1 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956906].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [956907] (ulepszenie 1) — nazwa] 적우[積雨]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].name
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność wroga [956907] (ulepszenie 1) — opis] [WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 1당</u></b></mark></color>, 기본 위력 +1\n[WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction] 5 이상이면</u></b></mark></color>, 코인 위력 +1, 가중치 +1\n[DefeatDuel] 피해량이 80%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 <color=#ff6000><mark=#ff000040><b><u>[YesdragonSelfRefraction]이 5 이상이면, 이 코인 재사용</u></b></mark></color> (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [956907] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956907].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [CondensedBloodRefraction]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [CondensedBloodRefraction] = 용혈[龍血] / Dragon's Blood [龍血]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [CondensedBloodRefraction]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [CondensedBloodRefraction]
211. [Umiejętność wroga [956908] (ulepszenie 1) — nazwa] 낙뢰[落雷]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956908].levelList[level=1].name
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [956908] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n<color=#ff6000><mark=#ff000040><b><u><noparse>매화침</noparse>을 타겟으로 지정</u></b></mark></color>\n<noparse>매화침</noparse>이 사망했을 경우 해당 스킬이 취소됨
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956908].levelList[level=1].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [956908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność wroga [956908] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 50% 확률로 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956908].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [956909] (ulepszenie 1) — nazwa] 용루성도[龍淚成濤]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].name
   limit: do 50 znaków
   EN: Tides Born of Dragon's Tears [龍淚成濤]
   PL: Tides Born of Dragon's Tears [龍淚成濤]
216. [Umiejętność wroga [956909] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 자신의 <color=#ff6000><mark=#ff000040><b><u>[DragonLanceRefraction] 수치 1당</u></b></mark></color>, 코인 위력 +1, 가중치 +1\n- [DragonLanceRefraction]이 최댓값이면, 추가로 피해량 +100%\n[DefeatDuel] 피해량이 80%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음\n[DefeatDuel] 다음 턴까지 [Vulnerable] 3 얻음\n[EndSkillAll] [DragonLanceRefraction] 수치가 1로 감소함
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [DragonLanceRefraction], [DefeatDuel], [Vulnerable], [EndSkillAll]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DragonLanceRefraction] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>For every [DragonLanceRefraction] on self</u></b></mark></color>, Coin Power +1 and gain +1 Atk Weight\n- If [DragonLanceRefraction] is at max Stack, deal +100% additional damage\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] Gain 3 [Vulnerable] until the next Turn End\n[EndSkillAll] Reduce [DragonLanceRefraction] Stack to 1
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] do końca tej Umiejętności ta jednostka nie może być Oszołamiona obrażeniami\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>za każdy własny [DragonLanceRefraction]</u></b></mark></color>, Moc Monet +1 i Waga Ataku +1\n- jeżeli [DragonLanceRefraction] osiągnie maks. Stosów, zadaje dodatkowo +100% obrażeń\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[DefeatDuel] zyskuje 3 [Vulnerable] do końca następnej tury\n[EndSkillAll] zmniejsza Stosy [DragonLanceRefraction] do 1
217. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [956909] (ulepszenie 1) — moneta 5, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [CondensedBloodRefraction] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=956909].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [957001] (ulepszenie 1) — nazwa] 자천멸오[自穿滅汚]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957001].levelList[level=1].name
   limit: do 60 znaków
   EN: Impale the Self, Impurity to Purge [自穿滅汚]
   PL: Impale the Self, Impurity to Purge [自穿滅汚]
228. [Umiejętność wroga [957001] (ulepszenie 1) — opis] [CantDuel] [CantIdentify]\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>홍옥의 체력이 1이면 피해량이 0이 되며</u></b></mark></color>, 코인 효과가 발동하지 않음\n[EndSkill] 이 캐릭터 사망
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957001].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantDuel], [CantIdentify], [WhenUse], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel] [CantIdentify]\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If Crimson Jade is at 1 HP, deal 0 damage</u></b></mark></color>, and Coin effects do not trigger\n[EndSkill] This unit dies
   PL: [CantDuel] [CantIdentify]\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli Crimson Jade ma 1 HP, zadaje 0 obrażeń</u></b></mark></color>, a efekty monet nie aktywują się\n[EndSkill] ta jednostka ginie
229. [Umiejętność wroga [957001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 5 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +5 [Burst] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Burst] o 5
230. [Umiejętność wroga [957001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [957001] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957001].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność wroga [957001] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957001].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [957101] (ulepszenie 1) — nazwa] 용의 기운을 머금은 바늘
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957101].levelList[level=1].name
   limit: do 50 znaków
   EN: Spirit-bearing Pin of the Dragon
   PL: Spirit-bearing Pin of the Dragon
234. [Umiejętność wroga [957101] (ulepszenie 1) — opis] [CanDuelGuard]\n[WinDuel] 대상에게 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WinDuel], [Vulnerable]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WinDuel] = [합 승리시] / [Clash Win]; [Vulnerable] = 취약 / Fragile
   EN: [CanDuelGuard]\n[WinDuel] Inflict 1 [Vulnerable] on target
   PL: [CanDuelGuard]\n[WinDuel] nakłada 1 [Vulnerable] na cel
235. [Umiejętność wroga [957101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=957101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Umiejętność wroga [955110] (ulepszenie 1) — nazwa] Furioso-Replica
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955110].levelList[level=1].name
   limit: do 40 znaków
   EN: Furioso-Replica
   PL: Furioso-Replica
237. [Umiejętność wroga [955110] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n- 합 위력 +5 (<color=#ff6000><mark=#ff000040><b><u>자신의 [KarmaOfIndexRien] 8당 1씩 감소, 최소 0</u></b></mark></color>)\n[WhenUse] 정신력이 0 이상이면, 망 1개 생성\n- 피해량이 20%만큼 증가하고 최종 위력 +3\n[WinDuel] \n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 3, [Binding] 1, [Vulnerable] 1 부여\n[DefeatDuel]\n- [AttackDmgDown] 4, [Paralysis] 9 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 20만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955110].levelList[level=1].desc
   limit: do 930 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien] = 카르마 / Karmic Consequence; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 3 [Breath] and +3 [Breath] Count\n- Clash Power +5 (<color=#ff6000><mark=#ff000040><b><u>Clash Power gained is reduced by 1 for every 8 [KarmaOfIndexRien] on self, down to 0</u></b></mark></color>)\n[WhenUse] At 0+ SP, generate 1 Mang\n- Deal +20% damage; Final Power +3\n[WinDuel]\n- Gain 3 [Breath] and +3 [Breath] Count\n- Attack End: Inflict 3 [Laceration], 1 [Binding], and 1 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Gain 4 [AttackDmgDown] and 9 [Paralysis]\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 20 SP\n[EndSkill] End this turn
   PL: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>ta Umiejętność nie aktywuje Umiejętności obronnych celu</u></b></mark></color>\nmoże przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 3\n- Moc Starcia +5 (<color=#ff6000><mark=#ff000040><b><u>maleje o 1 za każde 8 [KarmaOfIndexRien] na tej jednostce, do minimum 0</u></b></mark></color>)\n[WhenUse] przy Poczytalności 0 lub wyższej, tworzy 1 Mang\n- zadaje +20% obrażeń; Moc Końcowa +3\n[WinDuel]\n- zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 3\n- po zakończeniu ataku nakłada na wszystkie trafione cele, w następnej turze, 3 [Laceration], 1 [Binding] i 1 [Vulnerable]\n[DefeatDuel]\n- zyskuje 4 [AttackDmgDown] i 9 [Paralysis]\n- obrażenia z tej Umiejętności nie Oszołamiają celu; przy trafieniu nie aktywuje [Sinking] na celu\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 20 Poczytalności\n[EndSkill] kończy tę turę
238. [Umiejętność wroga [955110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Umiejętność wroga [955110] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955110].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [955110] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955110].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Reuse this Coin (max 7 times)</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>ponownie używa tej monety (maks. 7 razy)</u></b></mark></color>
241. [Umiejętność wroga [955110] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955110].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Sinking]
242. [Umiejętność wroga [955207] (ulepszenie 1) — nazwa] 소리를 부수고, 생각을 납작하게 짓이겨라
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].name
   limit: do 60 znaków
   EN: Destroy the Sound, Crush Flat the Thought
   PL: Destroy the Sound, Crush Flat the Thought
243. [Umiejętność wroga [955207] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 타격 스킬이 아니면</u></b></mark></color>, 코인 위력 +2, 피해량 +50%\n- 타격 스킬에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중시 대상의 [Sinking] 효과가 발동하지 않음\n\n타격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +60%\n- 타격 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 25만큼 흐트러짐 피해\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].desc
   limit: do 1100 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Blunt Skill</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Blunt Skill:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nBlunt weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Blunt weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Blunt weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +60% damage\n- Non-Blunt weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Raise target's Stagger Threshold by 25\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli ta jednostka ma [BlackNightmare]:\n- wszystkie monety zmieniają się w [SuperCoin]y\n- <color=#ff6000><mark=#ff000040><b><u>gdy toczy Starcie z Umiejętnością inną niż Uderzenie</u></b></mark></color>, Moc Monet +2 i zadaje +50% obrażeń\n- przy przegranej Starcia z Umiejętnością Uderzenia:\n  - Moc Monet -2 i zadaje -50% obrażeń\n  - obrażenia z tej Umiejętności nie Oszołamiają celu; przy trafieniu nie aktywuje [Sinking] na celu\n\nbroń Uderzenia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], broń Uderzenia pojawia się rzadziej\n- przy 150+ [KarmaOfIndexRien_2Phase], broń Uderzenia pojawia się jeszcze rzadziej\nefekty zależą od typu ataku używanej broni\n- broń Uderzenia zadaje +60% obrażeń\n- broń innego typu zadaje -30% obrażeń\n[WhenUse] zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 2\n[WinDuel] podnosi Próg Oszołomienia celu o 25\n- przy 150+ [KarmaOfIndexRien_2Phase], ten efekt nie aktywuje się
244. [Umiejętność wroga [955207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking]
245. [Umiejętność wroga [955207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Sinking]
246. [Umiejętność wroga [955207] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [955207] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 2 [Breath]
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 2 [Breath]
248. [Umiejętność wroga [955207] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [955207] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955207].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain +2 [Breath] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 2 Licznika [Breath]
250. [Umiejętność wroga [955208] (ulepszenie 1) — nazwa] 고요의 중심을 찌르고, 기억을 꿰뚫어라
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].name
   limit: do 70 znaków
   EN: Stab the Heart of Silence, Penetrate the Memory
   PL: Stab the Heart of Silence, Penetrate the Memory
251. [Umiejętność wroga [955208] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 관통 스킬이 아니면</u></b></mark></color>, 코인 위력 +2, 피해량 +50%\n- 관통 스킬에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중시 대상의 [Sinking] 효과가 발동하지 않음\n\n관통 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +60%\n- 관통 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 [AttackDmgUp] 2 얻음\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel], [AttackDmgUp]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Pierce Skill</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Pierce Skill:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nPierce weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Pierce weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Pierce weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +60% damage\n- Non-Pierce weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Gain 2 [AttackDmgUp] next turn\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli ta jednostka ma [BlackNightmare]:\n- wszystkie monety zmieniają się w [SuperCoin]y\n- <color=#ff6000><mark=#ff000040><b><u>gdy toczy Starcie z Umiejętnością inną niż Przebicie</u></b></mark></color>, Moc Monet +2 i zadaje +50% obrażeń\n- przy przegranej Starcia z Umiejętnością Przebicia:\n  - Moc Monet -2 i zadaje -50% obrażeń\n  - obrażenia z tej Umiejętności nie Oszołamiają celu; przy trafieniu nie aktywuje [Sinking] na celu\n\nbroń Przebicia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], broń Przebicia pojawia się rzadziej\n- przy 150+ [KarmaOfIndexRien_2Phase], broń Przebicia pojawia się jeszcze rzadziej\nefekty zależą od typu ataku używanej broni\n- broń Przebicia zadaje +60% obrażeń\n- broń innego typu zadaje -30% obrażeń\n[WhenUse] zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 2\n[WinDuel] zyskuje 2 [AttackDmgUp] w następnej turze\n- przy 150+ [KarmaOfIndexRien_2Phase], ten efekt nie aktywuje się
252. [Umiejętność wroga [955208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [955208] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 3 [Breath]
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 3 [Breath]
254. [Umiejętność wroga [955208] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [955208] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [955208] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [955208] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955208].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [955209] (ulepszenie 1) — nazwa] 날카롭게 벼린 비밀로, 형태를 베어내라
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].name
   limit: do 50 znaków
   EN: With Tempered Secret, Sever the Form
   PL: With Tempered Secret, Sever the Form
259. [Umiejętność wroga [955209] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 참격 스킬이 아니면,</u></b></mark></color> 코인 위력 +2, 피해량 +50%\n- 참격 스킬에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중시 대상의 [Sinking] 효과가 발동하지 않음\n\n참격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +60%\n- 참격 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 최종 위력 +3\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Slash Skill</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Slash Skill:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nSlash weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Slash weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Slash weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +60% damage\n- Non-Slash weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Final Power +3\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli ta jednostka ma [BlackNightmare]:\n- wszystkie monety zmieniają się w [SuperCoin]y\n- <color=#ff6000><mark=#ff000040><b><u>gdy toczy Starcie z Umiejętnością inną niż Ścięcie</u></b></mark></color>, Moc Monet +2 i zadaje +50% obrażeń\n- przy przegranej Starcia z Umiejętnością Ścięcia:\n  - Moc Monet -2 i zadaje -50% obrażeń\n  - obrażenia z tej Umiejętności nie Oszołamiają celu; przy trafieniu nie aktywuje [Sinking] na celu\n\nbroń Ścięcia pojawia się częściej\n- przy 75+ [KarmaOfIndexRien_2Phase], broń Ścięcia pojawia się rzadziej\n- przy 150+ [KarmaOfIndexRien_2Phase], broń Ścięcia pojawia się jeszcze rzadziej\nefekty zależą od typu ataku używanej broni\n- broń Ścięcia zadaje +60% obrażeń\n- broń innego typu zadaje -30% obrażeń\n[WhenUse] zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 2\n[WinDuel] Moc Końcowa +3\n- przy 150+ [KarmaOfIndexRien_2Phase], ten efekt nie aktywuje się
260. [Umiejętność wroga [955209] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [955209] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain +3 [Breath] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 3 Licznika [Breath]
262. [Umiejętność wroga [955209] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność wroga [955209] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
264. [Umiejętność wroga [955209] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność wroga [955209] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955209].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [955210] (ulepszenie 1) — nazwa] Furioso [Crescendo]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955210].levelList[level=1].name
   limit: do 40 znaków
   EN: Furioso [Crescendo]
   PL: Furioso [Crescendo]
267. [Umiejętność wroga [955210] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 6 얻음, 자신의 [Breath] 횟수 6 증가\n- 합 위력 +10 (<color=#ff6000><mark=#ff000040><b><u>자신의 [KarmaOfIndexRien_2Phase] 8당 1씩 감소</u></b></mark></color>)\n[WhenUse] 정신력이 0 이상이면, 망 2개 생성\n- 피해량이 40%만큼 증가하고 최종 위력 +5\n[WinDuel]\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 4, [Binding] 2, [Vulnerable] 2 부여\n[DefeatDuel]\n- [AttackDmgDown] 6, [Paralysis] 9 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 25만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955210].levelList[level=1].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien_2Phase], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 6 [Breath] and +6 [Breath] Count\n- Clash Power +10 (<color=#ff6000><mark=#ff000040><b><u>Clash Power gained is reduced by 1 for every 8 [KarmaOfIndexRien_2Phase] on self</u></b></mark></color>)\n[WhenUse] At 0+ SP, generate 2 Mangs\n- Deal +40% damage; Final Power +5\n[WinDuel]\n- Attack End: Inflict 4 [Laceration], 2 [Binding], and 2 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Gain 6 [AttackDmgDown] and 9 [Paralysis]\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 25 SP\n[EndSkill] End this turn
   PL: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>ta Umiejętność nie aktywuje Umiejętności obronnych celu</u></b></mark></color>\nmoże przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- zyskuje 6 [Breath] i zwiększa Licznik [Breath] o 6\n- Moc Starcia +10 (<color=#ff6000><mark=#ff000040><b><u>maleje o 1 za każde 8 [KarmaOfIndexRien_2Phase] na tej jednostce</u></b></mark></color>)\n[WhenUse] przy Poczytalności 0 lub wyższej, tworzy 2 Mangi\n- zadaje +40% obrażeń; Moc Końcowa +5\n[WinDuel]\n- po zakończeniu ataku nakłada na wszystkie trafione cele, w następnej turze, 4 [Laceration], 2 [Binding] i 2 [Vulnerable]\n[DefeatDuel]\n- zyskuje 6 [AttackDmgDown] i 9 [Paralysis]\n- obrażenia z tej Umiejętności nie Oszołamiają celu; przy trafieniu nie aktywuje [Sinking] na celu\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 25 Poczytalności\n[EndSkill] kończy tę turę
268. [Umiejętność wroga [955210] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955210].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [955210] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955210].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [955210] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955210].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Umiejętność wroga [955210] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955210].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [955211] (ulepszenie 1) — nazwa] Furioso [Lacrimosa-Crescendo]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955211].levelList[level=1].name
   limit: do 50 znaków
   EN: Furioso [Lacrimosa-Crescendo]
   PL: Furioso [Lacrimosa-Crescendo]
273. [Umiejętność wroga [955211] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 9 얻음, 자신의 [Breath] 횟수 9 증가\n- 합 위력 +15 (자신의 [KarmaOfIndexRien_2Phase] 8당 1씩 감소)\n[WhenUse] 정신력이 0 이상이면, 망 3개 생성\n- 피해량이 60%만큼 증가하고 최종 위력 +8\n[WinDuel]\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 5, [Binding] 3, [Vulnerable] 3 부여\n[DefeatDuel]\n- [AttackDmgDown] 8, [Paralysis] 9 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중시 대상의 [Sinking] 효과가 발동하지 않음  \n[EndSkill] 망을 생성했으면, 정신력 30만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955211].levelList[level=1].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien_2Phase], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 9 [Breath] and +9 [Breath] Count\n- Clash Power +15 (Clash Power gained is reduced by 1 for every 8 [KarmaOfIndexRien_2Phase] on self)\n[WhenUse] At 0+ SP, generate 3 Mangs\n- Deal +60% damage; Final Power +8\n[WinDuel]\n- Attack End: Inflict 5 [Laceration], 3 [Binding], and 3 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Gain 8 [AttackDmgDown] and 9 [Paralysis]\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 30 SP\n[EndSkill] End this turn
   PL: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>ta Umiejętność nie aktywuje Umiejętności obronnych celu</u></b></mark></color>\nmoże przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- zyskuje 9 [Breath] i zwiększa Licznik [Breath] o 9\n- Moc Starcia +15 (maleje o 1 za każde 8 [KarmaOfIndexRien_2Phase] na tej jednostce)\n[WhenUse] przy Poczytalności 0 lub wyższej, tworzy 3 Mangi\n- zadaje +60% obrażeń; Moc Końcowa +8\n[WinDuel]\n- po zakończeniu ataku nakłada na wszystkie trafione cele, w następnej turze, 5 [Laceration], 3 [Binding] i 3 [Vulnerable]\n[DefeatDuel]\n- zyskuje 8 [AttackDmgDown] i 9 [Paralysis]\n- obrażenia z tej Umiejętności nie Oszołamiają celu; przy trafieniu nie aktywuje [Sinking] na celu\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 30 Poczytalności\n[EndSkill] kończy tę turę
274. [Umiejętność wroga [955211] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność wroga [955211] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955211].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Umiejętność wroga [955211] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955211].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [955211] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955211].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność wroga [955601] (ulepszenie 1) — nazwa] 막아줘
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955601].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't Let Them Hurt Me
   PL: Don't Let Them Hurt Me
279. [Umiejętność wroga [955601] (ulepszenie 1) — opis] [CanDuelGuard]\n이번 전투에서 사망한 아군 1명당, 최종 위력 -4
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard
   EN: [CanDuelGuard]\nFinal Power -4 for every ally defeated in this Encounter
   PL: [CanDuelGuard]\nMoc Końcowa -4 za każdego pokonanego sojusznika w tej walce
280. [Umiejętność wroga [955601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [955602] (ulepszenie 1) — nazwa] 놀아줘!
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955602].levelList[level=1].name
   limit: do 40 znaków
   EN: Play With Me!
   PL: Play With Me!
282. [Umiejętność wroga [955602] (ulepszenie 1) — opis] 이번 전투에서 사망한 아군 1명당, 최종 위력 +1, 피해량 +5%\n[DefeatDuel] 기본 위력 7 감소\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955602].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 and deal +5% damage for every ally defeated in this Encounter\n[DefeatDuel] Base Power -7\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: Moc Końcowa +1 i zadaje +5% obrażeń za każdego pokonanego sojusznika w tej walce\n[DefeatDuel] Moc Bazowa -7\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
283. [Umiejętność wroga [955602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [955602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność wroga [955602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Inflict 1 [ResultReduction] next turn
   PL: [OnSucceedAttack] nakłada 1 [ResultReduction] w następnej turze
286. [Umiejętność wroga [955603] (ulepszenie 1) — nazwa] 이얍!
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955603].levelList[level=1].name
   limit: do 40 znaków
   EN: Hyah!
   PL: Hyah!
287. [Umiejętność wroga [955603] (ulepszenie 1) — opis] 이번 전투에서 사망한 아군 1명당, 최종 위력 +1, 피해량 +10%\n[DefeatDuel] 기본 위력 8 감소\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955603].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 and deal +10% damage for every ally defeated in this Encounter\n[DefeatDuel] Base Power -8\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: Moc Końcowa +1 i zadaje +10% obrażeń za każdego pokonanego sojusznika w tej walce\n[DefeatDuel] Moc Bazowa -8\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
288. [Umiejętność wroga [955603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [955603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność wroga [955604] (ulepszenie 1) — nazwa] 인형 좋아해?
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955604].levelList[level=1].name
   limit: do 40 znaków
   EN: Do You Like Dolls?
   PL: Do You Like Dolls?
291. [Umiejętność wroga [955604] (ulepszenie 1) — opis] 이번 전투에서 사망한 아군 1명당, 최종 위력 +1, 피해량 +5%\n[DefeatDuel] 기본 위력 10 감소\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955604].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 and deal +5% damage for every ally defeated in this Encounter\n[DefeatDuel] Base Power -10\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: Moc Końcowa +1 i zadaje +5% obrażeń za każdego pokonanego sojusznika w tej walce\n[DefeatDuel] Moc Bazowa -10\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
292. [Umiejętność wroga [955604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Umiejętność wroga [955604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [955604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 2 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Inflict 2 [ResultReduction] next turn
   PL: [OnSucceedAttack] nakłada 2 [ResultReduction] w następnej turze
295. [Umiejętność wroga [955605] (ulepszenie 1) — nazwa] 난 가위를 낼게, 너는?
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955605].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Go fer Scissors. How 'Bout You?
   PL: Ja Graję Nożyczki. A Ty?
296. [Umiejętność wroga [955605] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>일방 공격이거나 합 패배 시, 피해량 +300%</u></b></mark></color>\n[StartDuel] <color=#ff6000><mark=#ff000040><b><u>대상에게 [ResultReduction]가 있으면, 합 위력 +20</u></b></mark></color>\n[WinDuel] 공격 대상의 수비 스킬을 발동시키지 않음\n[WinDuel] 이 스킬을 종료하고 대상에게 ‘네가 이겼어’ 사용함
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955605].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartDuel], [ResultReduction], [WinDuel]
   znaczenie tagów: [StartDuel] = [합 시작 시] / [Clash Start]; [ResultReduction] = 위력 감소 / Power Down; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <color=#ff6000><mark=#ff000040><b><u>If this Skill is an Unopposed Attack, or if this Skill loses a Clash, deal +300% damage</u></b></mark></color>\n[StartDuel] <color=#ff6000><mark=#ff000040><b><u>If target has [ResultReduction], Clash Power +20</u></b></mark></color>\n[WinDuel] This Skill does not trigger the target's Defense Skill\n[WinDuel] End this Skill and use "You Win..." on the target
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli to atak bez kontr lub ta Umiejętność przegrywa Starcie, zadaje +300% obrażeń</u></b></mark></color>\n[StartDuel] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [ResultReduction], Moc Starcia +20</u></b></mark></color>\n[WinDuel] ta Umiejętność nie aktywuje Umiejętności obronnej celu\n[WinDuel] kończy tę Umiejętność i używa na celu „You Win..."
297. [Umiejętność wroga [955605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [955605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [955605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność wroga [955605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 4 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Laceration] and +4 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 4
301. [Umiejętność wroga [955606] (ulepszenie 1) — nazwa] 네가 이겼어
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955606].levelList[level=1].name
   limit: do 40 znaków
   EN: You Win...
   PL: You Win...
302. [Umiejętność wroga [955606] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 공격이 적중하지 않음\n[WhenUse] 대상에게 다음 턴에 [AttackUp] 2 부여\n[EndSkill] 현재 체력이 가장 낮은 수감자 2명의 체력을 (이 코인의 최종 위력 x 5)만큼 회복
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955606].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [AttackUp], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- Its attack does not hit\n[WhenUse] Apply 2 [AttackUp] on target next turn\n[EndSkill] Heal (this Coin's Final Power x 5) HP for 2 Sinners that have the lowest current HP
   PL: [CantDuel]\nta Umiejętność ma następujące właściwości:\n- nie aktywuje Umiejętności obronnych\n- jej atak nie trafia\n[WhenUse] nakłada 2 [AttackUp] na cel w następnej turze\n[EndSkill] przywraca (Moc Końcowa tej monety x 5) HP dwóm Grzesznikom z najniższym aktualnym HP
303. [Umiejętność wroga [955607] (ulepszenie 1) — nazwa] 영원히 같이 놀자~!
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955607].levelList[level=1].name
   limit: do 50 znaków
   EN: Let's Play Together Forever~!
   PL: Let's Play Together Forever~!
304. [Umiejętność wroga [955607] (ulepszenie 1) — opis] 이 스킬은 수비 스킬을 발동시키지 않고, 속도와 상관없이 합을 할 수 있음\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착한 대상에게는 피해량 -90%</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[StartDuel] 최종 위력 +20</u></b></mark></color>\n[WinDuel] 피해량 +100%\n[DefeatDuel] 피해량이 90%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[DefeatDuel] 다음 턴에 모든 부위가 흐트러짐 상태가 됨\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955607].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [StartDuel], [WinDuel], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StartDuel] = [합 시작 시] / [Clash Start]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: This Skill does not trigger Defense Skills, and can be Clashed with regardless of Speed\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Deal -90% damage against targets that have equipped Defense Skills</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[StartDuel] Final Power +20</u></b></mark></color>\n[WinDuel] Deal +100% damage\n[DefeatDuel] Deal -90% damage and damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] All Parts become Staggered next turn\n[EndSkill] End this turn
   PL: ta Umiejętność nie aktywuje Umiejętności obronnych i można ją przeprowadzić w Starcie niezależnie od Szybkości\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>zadaje o 90% mniej obrażeń celom z wyposażoną Umiejętnością obronną</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[StartDuel] Moc Końcowa +20</u></b></mark></color>\n[WinDuel] zadaje +100% obrażeń\n[DefeatDuel] zadaje o 90% mniej obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[DefeatDuel] w następnej turze wszystkie Części przechodzą w Oszołamienie\n[EndSkill] kończy tę turę
305. [Umiejętność wroga [955607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [955607] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955607].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność wroga [955607] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955607].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [955607] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 6 부여, [Laceration] 횟수 5 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955607].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 6 [Laceration] and +5 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 6 [Laceration] i zwiększa Licznik [Laceration] o 5
309. [Umiejętność wroga [955401] (ulepszenie 1) — nazwa] 설치 미술 제 3호 ‘간이늑골’
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955401].levelList[level=1].name
   limit: do 60 znaków
   EN: Installation Art no. 3: Improvised Ribcage
   PL: Sztuka Instalacji nr 3: Improwizowana Klatka Piersiowa
310. [Umiejętność wroga [955401] (ulepszenie 1) — opis] [CantDuel]\n레벨이 높은 적 우선 지정\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 대상의 [Laceration] 8당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955401].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Laceration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [CantDuel]\nPrioritizes enemy with the highest level\nThis Skill does not trigger Defense Skills\n[WhenUse] Coin Power +1 for every 8 [Laceration] on target (max 2)
   PL: [CantDuel]\npriorytet: wróg o najwyższym poziomie\nta Umiejętność nie aktywuje Umiejętności obronnych\n[WhenUse] Moc Monet +1 za każde 8 [Laceration] na celu (maks. 2)
311. [Umiejętność wroga [955401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 피해 대신 정신력 피해를 입힘
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal SP damage instead of HP damage
   PL: [OnSucceedAttack] zadaje obrażenia SP zamiast obrażeń HP
312. [Umiejętność wroga [955401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 정신력 15 회복
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 15 SP on self
   PL: [OnSucceedAttack] przywraca 15 SP jednostki
313. [Umiejętność wroga [955401] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태로 만들고 다음 턴에 [LivingSpecimenTheRings]으로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955401].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [LivingSpecimenTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenTheRings] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Stagger target and turn target into [LivingSpecimenTheRings] next turn</u></b></mark></color>
   PL: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>oszołomia cel i w następnej turze zamienia go w [LivingSpecimenTheRings]</u></b></mark></color>
314. [Umiejętność wroga [955404] (ulepszenie 1) — nazwa] 티비아의 멜로디 - 해체된 것이 해체되지 않은 것을 해체하는 것
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].name
   limit: do 90 znaków
   EN: Tibia's Melody - Anatomization of the Unanatomized by the Anatomized
   PL: Tibia's Melody - Anatomization of the Unanatomized by the Anatomized
315. [Umiejętność wroga [955404] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 피해량이 90%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [MineTheRings] 소멸
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [MineTheRings]
   znaczenie tagów: [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: During the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: Heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -90% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [MineTheRings] expires
   PL: w turze, w której ta jednostka ma wyposażoną tę Umiejętność, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>przy trafieniu Umiejętnością ataku</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nza każdego celu zabitego tą Umiejętnością przywraca 15 Poczytalności\n[StartBattle] zyskuje 4 [Protection]\n[WhenUse] zadaje +3% obrażeń za każde 6 ([Laceration] na głównym celu + [Laceration] na celu drugorzędnym) (maks. 30%)\n[DefeatDuel] zadaje o 90% mniej obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] [MineTheRings] wygasa
316. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 SP damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 5 obrażeń SP
318. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP (once per Skill)
   PL: [OnSucceedAttack] przywraca 5 SP jednostki (1 raz na Umiejętność)
319. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
321. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 1 [Protection] next turn (once per Skill)
   PL: [OnSucceedAttack] zyskuje 1 [Protection] w następnej turze (1 raz na Umiejętność)
322. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [AttackDmgDown] w następnej turze
324. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn (once per Skill)
   PL: [OnSucceedAttack] zyskuje 1 [AttackDmgUp] w następnej turze (1 raz na Umiejętność)
325. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Umiejętność wroga [955404] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955404].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
327. [Umiejętność wroga [955001] (ulepszenie 1) — nazwa] 절명[絶命]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955001].levelList[level=1].name
   limit: do 40 znaków
   EN: Deathedge [絶命]
   PL: Deathedge [絶命]
328. [Umiejętność wroga [955001] (ulepszenie 1) — opis] 이 스킬은 대상의 수비 스킬을 발동시키지 않음\n현재 체력 비율이 가장 낮은 대상 공격
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955001].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Skill does not trigger the target's Defense Skill\nPrioritizes the target with the lowest current HP percentage
   PL: ta Umiejętność nie aktywuje Umiejętności obronnej celu\npriorytet: cel z najniższym procentem aktualnego HP
329. [Umiejętność wroga [955001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 잃은 체력 1%당 [PhantomIncision] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict 1 [PhantomIncision] for every 1% missing HP on target
   PL: [OnSucceedAttack] nakłada 1 [PhantomIncision] za każde 1% brakującego HP celu
330. [Umiejętność wroga [955001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [PhantomIncision]을 모두 소모하여, 최대 체력의 (소모값)% 만큼 체력 피해
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Consume all [PhantomIncision] on target and deal ([PhantomIncision] consumed)% HP damage
   PL: [OnSucceedAttack] zużywa wszystkie [PhantomIncision] na celu i zadaje (zużyta wartość)% obrażeń HP
331. [Umiejętność wroga [955505] (ulepszenie 1) — nazwa] 억압당한 육체의 해방
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].name
   limit: do 50 znaków
   EN: Liberation of the Repressed Flesh
   PL: Liberation of the Repressed Flesh
332. [Umiejętność wroga [955505] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 피해량이 90%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [BoneBladeTheRings] 소멸
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [BoneBladeTheRings]
   znaczenie tagów: [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: During the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: Heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -90% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [BoneBladeTheRings] expires
   PL: w turze, w której ta jednostka ma wyposażoną tę Umiejętność, zyskuje 1 [PlusCoinValueDown] i 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>przy trafieniu Umiejętnością ataku</u></b></mark></color> (1 raz na Umiejętność; maks. 3 razy na turę)\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nza każdego celu zabitego tą Umiejętnością przywraca 15 Poczytalności\n[StartBattle] zyskuje 4 [Protection]\n[WhenUse] zadaje +3% obrażeń za każde 6 ([Laceration] na głównym celu + [Laceration] na celu drugorzędnym) (maks. 30%)\n[DefeatDuel] zadaje o 90% mniej obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] [BoneBladeTheRings] wygasa
333. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność wroga [955505] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Refraction6.json :: dataList[id=955505].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [refraction6] Pasywka wroga: Passives_Abnormality_Refraction6
- plik gry: `Passives_Abnormality_Refraction6.json`

344. [[refraction6] Pasywka wroga [956301] — nazwa] 태동
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956301].name
   limit: do 40 znaków
   EN: Quickening of the Unborn
   PL: Quickening of the Unborn
345. [[refraction6] Pasywka wroga [956301] — opis] 스테이지 시작 시, 최대 체력의 1.3%만큼 보호막을 얻음\n체력이 90% 미만으로 내려가지 않음\n\n세 번째 턴 종료 전에 보호막이 파괴되면,\n해당 턴이 즉시 종료되고, 다음 턴에 <color=#ff6000><mark=#ff000040><b><u>특수 패턴</u></b></mark></color> 발동\n\n스킬 ‘태동 시작’ 공격 종료 시, 스테이지 전투가 종료됨
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956301].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: Encounter Start: Gain 1.3% HP as Shield\nHP does not fall below 90%\n\nIf this unit's Shield is broken before the end of Turn 3,\nEnd the turn immediately and activate <color=#ff6000><mark=#ff000040><b><u>a unique pattern</u></b></mark></color> next turn\n\nAt Attack End of "The Quickening" Skill: End the Encounter
   PL: na początku walki zyskuje Tarczę równą 1.3% HP\nHP nie spada poniżej 90%\n\njeżeli Tarcza tej jednostki pęknie przed końcem 3. tury,\ntura natychmiast się kończy, a w następnej turze aktywuje się <color=#ff6000><mark=#ff000040><b><u>unikatowy wzorzec</u></b></mark></color>\n\npo zakończeniu ataku Umiejętności „The Quickening": kończy walkę
346. [[refraction6] Pasywka wroga [956401] — nazwa] 우화 - 전생
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956401].name
   limit: do 40 znaków
   EN: Eclosion - Life That Was
   PL: Eclosion - Life That Was
347. [[refraction6] Pasywka wroga [956401] — opis] 속도가 1로 고정되고 체력이 1 미만으로 감소하지 않음\n등장 이후 첫 번째 턴 시작 시, 보호막 333 얻음\n\n스킬 ‘우화’ 공격 종료 시, 스테이지 전투가 종료됨\n- 보호막이 파괴되었으면, 대신 다음 턴이 시작되어 <color=#ff6000><mark=#ff000040><b><u>특수한 선택지</u></b></mark></color>가 등장하고 이후 스테이지 종료
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956401].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: Fix this unit's Speed to 1; this unit's HP does not drop below 1\nFirst Turn Start after entering the Encounter: Gain 333 Shield\n\nAt Attack End of the Skill "Eclosion", end Encounter\n- If the Shield is broken, proceed to the next turn instead and <color=#ff6000><mark=#ff000040><b><u>face a unique Choice Event</u></b></mark></color> before the Encounter ends
   PL: Szybkość tej jednostki jest stała (1); HP tej jednostki nie spada poniżej 1\npierwszy początek tury po pojawieniu się w walce: zyskuje 333 Tarczy\n\npo zakończeniu ataku Umiejętności „Eclosion" kończy walkę\n- jeżeli Tarcza została zniszczona, zamiast tego rozpoczyna się następna tura, pojawia się <color=#ff6000><mark=#ff000040><b><u>unikatowy Wybór</u></b></mark></color>, a następnie walka się kończy
348. [[refraction6] Pasywka wroga [956402] — nazwa] 단조의 세월
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956402].name
   limit: do 40 znaków
   EN: Time of Forging
   PL: Time of Forging
349. [[refraction6] Pasywka wroga [956402] — opis] [HeatedWingScales]의 효과가 4배로 적용\n\nE.G.O 스킬로 받는 피해량 +100%
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956402].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [HeatedWingScales]
   znaczenie tagów: [HeatedWingScales] = 달궈진 비늘 가루 / Incandescent Scale Dust
   EN: Quadruple the effects of [HeatedWingScales]\n\nTake +100% damage from E.G.O Skills
   PL: efekty [HeatedWingScales] działają z czterokrotną siłą\n\notrzymuje +100% obrażeń z Umiejętności E.G.O
350. [[refraction6] Pasywka wroga [956501] — nazwa] 우화 - 금생
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956501].name
   limit: do 40 znaków
   EN: Eclosion - Life That Is
   PL: Eclosion - Life That Is
351. [[refraction6] Pasywka wroga [956501] — opis] 속도가 1로 고정되고 체력이 1 미만으로 감소하지 않음\n등장 이후 첫 번째 턴 시작 시, 보호막 333 얻음\n\n스킬 ‘우화’ 공격 종료 시, 스테이지 전투가 종료됨\n- 보호막이 파괴되었으면, 대신 다음 턴이 시작되어 <color=#ff6000><mark=#ff000040><b><u>특수한 선택지</u></b></mark></color>가 등장하고 이후 스테이지 종료
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956501].desc
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [[refraction6] Pasywka wroga [956502] — nazwa] 찰나의 일순
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956502].name
   limit: do 40 znaków
   EN: Kṣaṇa of Circumvolution
   PL: Kṣaṇa of Circumvolution
353. [[refraction6] Pasywka wroga [956502] — opis] [TransparentWingScales]의 효과가 4배로 적용\n\nE.G.O 스킬로 받는 피해량 +100%
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [TransparentWingScales]
   znaczenie tagów: [TransparentWingScales] = 예리한 비늘 가루 / Acuate Scale Dust
   EN: Quadruple the effects of [TransparentWingScales]\n\nTake +100% damage from E.G.O Skills
   PL: efekty [TransparentWingScales] działają z czterokrotną siłą\n\notrzymuje +100% obrażeń z Umiejętności E.G.O
354. [[refraction6] Pasywka wroga [956601] — nazwa] 우화 - 내생
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956601].name
   limit: do 40 znaków
   EN: Eclosion - Life That Will Be
   PL: Eclosion - Life That Will Be
355. [[refraction6] Pasywka wroga [956601] — opis] 속도가 1로 고정되고 체력이 1 미만으로 감소하지 않음\n등장 이후 첫 번째 턴 시작 시, 보호막 333 얻음\n\n스킬 ‘우화’ 공격 종료 시, 스테이지 전투가 종료됨\n- 보호막이 파괴되었으면, 대신 다음 턴이 시작되어 <color=#ff6000><mark=#ff000040><b><u>특수한 선택지</u></b></mark></color>가 등장하고 이후 스테이지 종료
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956601].desc
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [[refraction6] Pasywka wroga [956602] — nazwa] 억겁의 산화
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956602].name
   limit: do 40 znaków
   EN: Erosion of Kalpas
   PL: Erosion of Kalpas
357. [[refraction6] Pasywka wroga [956602] — opis] [RustedWingScales]의 효과가 4배로 적용\n\nE.G.O 스킬로 받는 피해량 +100%
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [RustedWingScales]
   znaczenie tagów: [RustedWingScales] = 녹슨 비늘 가루 / Rusted Scale Dust
   EN: Quadruple the effects of [RustedWingScales]\n\nTake +100% damage from E.G.O Skills
   PL: efekty [RustedWingScales] działają z czterokrotną siłą\n\notrzymuje +100% obrażeń z Umiejętności E.G.O
358. [[refraction6] Pasywka wroga [9567010] — nazwa] 과거 [過去]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567010].name
   limit: do 40 znaków
   EN: Past [過去]
   PL: Past [過去]
359. [[refraction6] Pasywka wroga [9567010] — opis] [StackPastActivate]면, 다음 효과가 적용됨\n- 수감자에게 피격받을 때마다 대상 수감자에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가\n- 스킬 ‘겁화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPastActivate]/2)만큼 정신력 피해 입힘 (소수점 버림)’ 효과 추가\n- 턴 시작 시 [Combustion] 위력과 횟수 합이 10 이상인 모든 수감자에게 [TakeHpHealReduce] 5, [CrimsonTakeDamageUp] 3 부여
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567010].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [StackPastActivate], [Combustion], [TakeHpHealReduce], [CrimsonTakeDamageUp]
   znaczenie tagów: [StackPastActivate] = 과거 상태 / In the Past; [Combustion] = 화상 / Burn; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: When [StackPastActivate], gain the following effects:\n- When hit by Sinners, inflict 1 [Combustion] and +1 [Combustion] Count on the\nattacking Sinner\n- Skill "Kalpāgni" gains Final Power +2 and its final Coin gains "On Hit,\ninflict ([StackPastActivate] Stack / 2) SP damage (rounded down)" effect\n- Turn Start: Inflict 5 [TakeHpHealReduce] and 3 [CrimsonTakeDamageUp] on all Sinners who have 10+ ([Combustion] Potency + [Combustion] Count)
   PL: gdy aktywny jest [StackPastActivate], zyskuje następujące efekty:\n- za każdym razem gdy otrzymuje trafienie od Grzesznika, nakłada na atakującego Grzesznika 1 [Combustion] i zwiększa Licznik [Combustion] o 1\n- Umiejętność „Kalpāgni" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu zadaje (Stos [StackPastActivate]/2) obrażeń Poczytalności (zaokrąglone w dół)"\n- na początku tury nakłada 5 [TakeHpHealReduce] i 3 [CrimsonTakeDamageUp] na wszystkich Grzeszników z sumą (Moc [Combustion] + Licznik [Combustion]) 10 lub wyższą
360. [[refraction6] Pasywka wroga [9567011] — nazwa] 과거 [過去]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567011].name
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [[refraction6] Pasywka wroga [9567011] — opis] [StackPastActivate]면, 다음 효과가 적용됨\n<mark=#000000AA>- <color=#ff9000><s></color>수감자에게 피격받을 때마다 대상 수감자에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가<color=#ff0000></s></color></mark>\n- 스킬 ‘겁화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPastActivate]/2)만큼 정신력 피해 입힘 (소수점 버림)’ 효과 추가\n- 턴 시작 시 [Combustion] 위력과 횟수 합이 10 이상인 모든 수감자에게 [TakeHpHealReduce] 5, [CrimsonTakeDamageUp] 3 부여
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567011].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#ff9000>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackPastActivate], [Combustion], [TakeHpHealReduce], [CrimsonTakeDamageUp]
   znaczenie tagów: [StackPastActivate] = 과거 상태 / In the Past; [Combustion] = 화상 / Burn; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: When [StackPastActivate], gain the following effects:\n<mark=#000000AA>- <color=#ff9000><s></color>When hit by Sinners, inflict 1 [Combustion] and +1 [Combustion] Count on the\nattacking Sinner<color=#ff0000></s></color></mark>\n- Skill "Kalpāgni" gains Final Power +2 and its final Coin gains "On Hit,\ninflict ([StackPastActivate] Stack / 2) SP damage (rounded down)" effect\n- Turn Start: Inflict 5 [TakeHpHealReduce] and 3 [CrimsonTakeDamageUp] on all Sinners who have 10+ ([Combustion] Potency + [Combustion] Count)
   PL: gdy aktywny jest [StackPastActivate], zyskuje następujące efekty:\n<mark=#000000AA>- <color=#ff9000><s></color>za każdym razem gdy otrzymuje trafienie od Grzesznika, nakłada na atakującego\nGrzesznika 1 [Combustion] i zwiększa Licznik [Combustion] o 1<color=#ff0000></s></color></mark>\n- Umiejętność „Kalpāgni" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu zadaje (Stos [StackPastActivate]/2) obrażeń Poczytalności (zaokrąglone w dół)"\n- na początku tury nakłada 5 [TakeHpHealReduce] i 3 [CrimsonTakeDamageUp] na wszystkich Grzeszników z sumą (Moc [Combustion] + Licznik [Combustion]) 10 lub wyższą
362. [[refraction6] Pasywka wroga [9567012] — nazwa] 과거 [過去]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567012].name
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [[refraction6] Pasywka wroga [9567012] — opis] [StackPastActivate]면, 다음 효과가 적용됨\n- 수감자에게 피격받을 때마다 대상 수감자에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가\n<mark=#000000AA>- <color=#ff9000><s></color>스킬 ‘겁화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPastActivate]/2)만큼 정신력 피해 입힘 (소수점 버림)’ 효과 추가<color=#ff0000></s></color></mark>\n- 턴 시작 시 [Combustion] 위력과 횟수 합이 10 이상인 모든 수감자에게 [TakeHpHealReduce] 5, [CrimsonTakeDamageUp] 3 부여
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567012].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#ff9000>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackPastActivate], [Combustion], [TakeHpHealReduce], [CrimsonTakeDamageUp]
   znaczenie tagów: [StackPastActivate] = 과거 상태 / In the Past; [Combustion] = 화상 / Burn; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: When [StackPastActivate], gain the following effects:\n- When hit by Sinners, inflict 1 [Combustion] and +1 [Combustion] Count on the\nattacking Sinner\n<mark=#000000AA>- <color=#ff9000><s></color>Skill "Kalpāgni" gains Final Power +2 and its final Coin gains "On Hit,\ninflict ([StackPastActivate] Stack / 2) SP damage (rounded down)" effect<color=#ff0000></s></color></mark>\n- Turn Start: Inflict 5 [TakeHpHealReduce] and 3 [CrimsonTakeDamageUp] on all Sinners who have 10+ ([Combustion] Potency + [Combustion] Count)
   PL: gdy aktywny jest [StackPastActivate], zyskuje następujące efekty:\n- za każdym razem gdy otrzymuje trafienie od Grzesznika, nakłada na atakującego Grzesznika 1 [Combustion] i zwiększa Licznik [Combustion] o 1\n<mark=#000000AA>- <color=#ff9000><s></color>Umiejętność „Kalpāgni" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu zadaje (Stos\n[StackPastActivate]/2) obrażeń Poczytalności (zaokrąglone w dół)"<color=#ff0000></s></color></mark>\n- na początku tury nakłada 5 [TakeHpHealReduce] i 3 [CrimsonTakeDamageUp] na wszystkich Grzeszników z sumą (Moc [Combustion] + Licznik [Combustion]) 10 lub wyższą
364. [[refraction6] Pasywka wroga [9567013] — nazwa] 과거 [過去]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567013].name
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [[refraction6] Pasywka wroga [9567013] — opis] [StackPastActivate]면, 다음 효과가 적용됨\n- 수감자에게 피격받을 때마다 대상 수감자에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가\n- 스킬 ‘겁화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPastActivate]/2)만큼 정신력 피해 입힘 (소수점 버림)’ 효과 추가\n<mark=#000000AA>- <color=#ff9000><s></color>턴 시작 시 [Combustion] 위력과 횟수 합이 10 이상인 모든 수감자에게 [TakeHpHealReduce] 5, [CrimsonTakeDamageUp] 3 부여<color=#ff0000></s></color></mark>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567013].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#ff9000>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackPastActivate], [Combustion], [TakeHpHealReduce], [CrimsonTakeDamageUp]
   znaczenie tagów: [StackPastActivate] = 과거 상태 / In the Past; [Combustion] = 화상 / Burn; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: When [StackPastActivate], gain the following effects:\n- When hit by Sinners, inflict 1 [Combustion] and +1 [Combustion] Count on the\nattacking Sinner\n- Skill "Kalpāgni" gains Final Power +2 and its final Coin gains "On Hit,\ninflict ([StackPastActivate] Stack / 2) SP damage (rounded down)" effect\n<mark=#000000AA>- <color=#ff9000><s></color>Turn Start: Inflict 5 [TakeHpHealReduce] and 3 [CrimsonTakeDamageUp] on all Sinners who have 10+ ([Combustion] Potency + [Combustion] Count)<color=#ff0000></s></color></mark>
   PL: gdy aktywny jest [StackPastActivate], zyskuje następujące efekty:\n- za każdym razem gdy otrzymuje trafienie od Grzesznika, nakłada na atakującego Grzesznika 1 [Combustion] i zwiększa Licznik [Combustion] o 1\n- Umiejętność „Kalpāgni" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu zadaje (Stos [StackPastActivate]/2) obrażeń Poczytalności (zaokrąglone w dół)"\n<mark=#000000AA>- <color=#ff9000><s></color>na początku tury nakłada 5 [TakeHpHealReduce] i 3 [CrimsonTakeDamageUp] na wszystkich Grzeszników z sumą (Moc [Combustion] + Licznik\n[Combustion]) 10 lub wyższą<color=#ff0000></s></color></mark>
366. [[refraction6] Pasywka wroga [9567020] — nazwa] 현재 [現在]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567020].name
   limit: do 40 znaków
   EN: Present [現在]
   PL: Present [現在]
367. [[refraction6] Pasywka wroga [9567020] — opis] [StackPresentActivate]면, 다음 효과가 적용됨\n- 크리티컬 발동 시 [Breath] 횟수가 감소하지 않으며, 턴 시작 시 (2 + 수감자 수)만큼 [Breath] 얻고 [Breath] 횟수 증가\n- 스킬 ‘파사’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPresentActivate]/2)만큼 흐트러짐 피해 (소수점 버림)’ 효과 추가\n- 적중 시 크리티컬 피해량 +(자신의 [Breath] 위력과 횟수 합 x 2)% (최대 120%, 합 패배 시 수치가 1/3으로 감소)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567020].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n, [StackPresentActivate], [Breath]
   znaczenie tagów: [StackPresentActivate] = 현재 상태 / In the Present; [Breath] = 호흡 / Poise
   EN: When [StackPresentActivate], gain the following effects:\n- Does not lose [Breath] Count On Crit; Turn Start: gain (2 + # of Sinners) [Breath] and [Breath] Count\n- Skill "Smite the Wicked" gains Final Power +2 and its final Coin gains "On Hit, raise Stagger Threshold by ([StackPresentActivate] Stack / 2) (rounded down)" effect\n- On Hit, deal +(([Breath] Potency on self + [Breath] Count on self) x 2)% damage on Critical Hit (max 120%; on Clash Lose, apply only one-third of the effect's full value)
   PL: gdy aktywny jest [StackPresentActivate], zyskuje następujące efekty:\n- przy trafieniu krytycznym nie traci Liczników [Breath]; na początku tury zyskuje (2 + liczba Grzeszników) [Breath] i zwiększa Licznik [Breath]\n- Umiejętność „Smite the Wicked" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu podnosi Próg Oszołomienia o (Stos [StackPresentActivate]/2) (zaokrąglone w dół)"\n- przy trafieniu krytycznym zadaje +((Moc [Breath] na sobie + Licznik [Breath] na sobie) x 2)% obrażeń (maks. 120%; w razie przegranej Starcia stosowana jest tylko 1/3 pełnej wartości efektu)
368. [[refraction6] Pasywka wroga [9567021] — nazwa] 현재 [現在]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567021].name
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [[refraction6] Pasywka wroga [9567021] — opis] [StackPresentActivate]면, 다음 효과가 적용됨\n<mark=#000000AA>- <color=#e5e5e5><s></color>크리티컬 발동 시 [Breath] 횟수가 감소하지 않으며, 턴 시작 시 (2 + 수감자 수)만큼 [Breath] 얻고 [Breath] 횟수 증가<color=#ff0000></s></color></mark>\n- 스킬 ‘파사’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPresentActivate]/2)만큼 흐트러짐 피해 (소수점 버림)’ 효과 추가\n- 적중 시 크리티컬 피해량 +(자신의 [Breath] 위력과 횟수 합 x 2)% (최대 120%, 합 패배 시 수치가 1/3으로 감소)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567021].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#e5e5e5>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackPresentActivate], [Breath]
   znaczenie tagów: [StackPresentActivate] = 현재 상태 / In the Present; [Breath] = 호흡 / Poise
   EN: When [StackPresentActivate], gain the following effects:\n<mark=#000000AA>- <color=#e5e5e5><s></color>Does not lose [Breath] Count On Crit; Turn Start: gain (2 + # of Sinners) [Breath] and [Breath] Count<color=#ff0000></s></color></mark>\n- Skill "Smite the Wicked" gains Final Power +2 and its final Coin gains "On Hit, raise Stagger Threshold by ([StackPresentActivate] Stack / 2) (rounded down)" effect\n- On Hit, deal +(([Breath] Potency on self + [Breath] Count on self) x 2)% damage on Critical Hit (max 120%; on Clash Lose, apply only one-third of the effect's full value)
   PL: gdy aktywny jest [StackPresentActivate], zyskuje następujące efekty:\n<mark=#000000AA>- <color=#e5e5e5><s></color>przy trafieniu krytycznym nie traci Liczników [Breath]; na początku tury zyskuje (2 + liczba Grzeszników) [Breath] i zwiększa Licznik [Breath]<color=#ff0000></s></color></mark>\n- Umiejętność „Smite the Wicked" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu podnosi Próg Oszołomienia o (Stos [StackPresentActivate]/2) (zaokrąglone w dół)"\n- przy trafieniu krytycznym zadaje +((Moc [Breath] na sobie + Licznik [Breath] na sobie) x 2)% obrażeń (maks. 120%; w razie przegranej Starcia stosowana jest tylko 1/3 pełnej wartości efektu)
370. [[refraction6] Pasywka wroga [9567022] — nazwa] 현재 [現在]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567022].name
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [[refraction6] Pasywka wroga [9567022] — opis] [StackPresentActivate]면, 다음 효과가 적용됨\n- 크리티컬 발동 시 [Breath] 횟수가 감소하지 않으며, 턴 시작 시 (2 + 수감자 수)만큼 [Breath] 얻고 [Breath] 횟수 증가\n<mark=#000000AA>- <color=#e5e5e5><s></color>스킬 ‘파사’의 최종 위력 +2, 마지막 코인에 ‘적중 시 [StackPresentActivate]/2)만큼 흐트러짐 피해 (소수점 버림)’ 효과 추가<color=#ff0000></s></color></mark>\n- 적중 시 크리티컬 피해량 +(자신의 [Breath] 위력과 횟수 합 x 2)% (최대 120%, 합 패배 시 수치가 1/3으로 감소)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567022].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#e5e5e5>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackPresentActivate], [Breath]
   znaczenie tagów: [StackPresentActivate] = 현재 상태 / In the Present; [Breath] = 호흡 / Poise
   EN: When [StackPresentActivate], gain the following effects:\n- Does not lose [Breath] Count On Crit; Turn Start: gain (2 + # of Sinners) [Breath] and [Breath] Count\n<mark=#000000AA>- <color=#e5e5e5><s></color>Skill "Smite the Wicked" gains Final Power +2 and its final Coin gains "On Hit, raise Stagger Threshold by ([StackPresentActivate] Stack / 2) (rounded down)" effect<color=#ff0000></s></color></mark>\n- On Hit, deal +(([Breath] Potency on self + [Breath] Count on self) x 2)% damage on Critical Hit (max 120%; on Clash Lose, apply only one-third of the effect's full value)
   PL: gdy aktywny jest [StackPresentActivate], zyskuje następujące efekty:\n- przy trafieniu krytycznym nie traci Liczników [Breath]; na początku tury zyskuje (2 + liczba Grzeszników) [Breath] i zwiększa Licznik [Breath]\n<mark=#000000AA>- <color=#e5e5e5><s></color>Umiejętność „Smite the Wicked" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu podnosi Próg Oszołomienia o (Stos [StackPresentActivate]/2) (zaokrąglone w dół)"<color=#ff0000></s></color></mark>\n- przy trafieniu krytycznym zadaje +((Moc [Breath] na sobie + Licznik [Breath] na sobie) x 2)% obrażeń (maks. 120%; w razie przegranej Starcia stosowana jest tylko 1/3 pełnej wartości efektu)
372. [[refraction6] Pasywka wroga [9567023] — nazwa] 현재 [現在]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567023].name
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [[refraction6] Pasywka wroga [9567023] — opis] [StackPresentActivate]면, 다음 효과가 적용됨\n- 크리티컬 발동 시 [Breath] 횟수가 감소하지 않으며, 턴 시작 시 (2 + 수감자 수)만큼 [Breath] 얻고 [Breath] 횟수 증가\n- 스킬 ‘파사’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackPresentActivate]/2)만큼 흐트러짐 피해 (소수점 버림)’ 효과 추가\n<mark=#000000AA>- <color=#e5e5e5><s></color>적중 시 크리티컬 피해량 +(자신의 [Breath] 위력과 횟수 합 x 2)% (최대 120%, 합 패배 시 수치가 1/3으로 감소)<color=#ff0000></s></color></mark>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567023].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#e5e5e5>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackPresentActivate], [Breath]
   znaczenie tagów: [StackPresentActivate] = 현재 상태 / In the Present; [Breath] = 호흡 / Poise
   EN: When [StackPresentActivate], gain the following effects:\n- Does not lose [Breath] Count On Crit; Turn Start: gain (2 + # of Sinners) [Breath] and [Breath] Count\n- Skill "Smite the Wicked" gains Final Power +2 and its final Coin gains "On Hit, raise Stagger Threshold by ([StackPresentActivate] Stack / 2) (rounded down)" effect\n<mark=#000000AA>- <color=#e5e5e5><s></color>On Hit, deal +(([Breath] Potency on self + [Breath] Count on self) x 2)% damage on Critical Hit (max 120%; on Clash Lose, apply only one-third of the effect's full value)<color=#ff0000></s></color></mark>
   PL: gdy aktywny jest [StackPresentActivate], zyskuje następujące efekty:\n- przy trafieniu krytycznym nie traci Liczników [Breath]; na początku tury zyskuje (2 + liczba Grzeszników) [Breath] i zwiększa Licznik [Breath]\n- Umiejętność „Smite the Wicked" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu podnosi Próg Oszołomienia o (Stos [StackPresentActivate]/2) (zaokrąglone w dół)"\n<mark=#000000AA>- <color=#e5e5e5><s></color>przy trafieniu krytycznym zadaje +((Moc [Breath] na sobie + Licznik [Breath] na sobie) x 2)% obrażeń (maks. 120%; w razie przegranej Starcia stosowana jest tylko 1/3 pełnej wartości efektu)<color=#ff0000></s></color></mark>
374. [[refraction6] Pasywka wroga [9567030] — nazwa] 미래 [未來]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567030].name
   limit: do 40 znaków
   EN: Future [未來]
   PL: Future [未來]
375. [[refraction6] Pasywka wroga [9567030] — opis] [StackFutureActivate]면, 다음 효과가 적용됨\n- 턴 시작 시 모든 수감자의 [Laceration] 횟수가 (3 + 현재 턴 수/2)만큼 증가 (소수점 올림)\n- 스킬 ‘혈화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackFutureActivate] x 3)만큼 자신의 체력 회복’ 효과 추가\n- 자신 또는 수감자에게 [Laceration]이 발동할 때마다 해당 [Laceration] 피해만큼 자신의 체력을 회복 (소수점 버림)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567030].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [StackFutureActivate], [Laceration]
   znaczenie tagów: [StackFutureActivate] = 미래 상태 / In the Future; [Laceration] = 출혈 / Bleed
   EN: When [StackFutureActivate], gain the following effects:\n- Turn Start: All Sinners gain +(3 + # of current turn / 2) [Laceration] Count (rounded up)\n- Skill "Bloodflower" gains Final Power +2 and its final Coin gains "On Hit,\nheal ([StackFutureActivate] Stack x 3) HP on self" effect\n- Whenever [Laceration] activates on self or on Sinners, heal HP equal to the said [Laceration] damage (rounded down)
   PL: gdy aktywny jest [StackFutureActivate], zyskuje następujące efekty:\n- na początku tury wszyscy Grzesznicy zyskują +(3 + numer bieżącej tury/2) Licznika [Laceration] (zaokrąglone w górę)\n- Umiejętność „Bloodflower" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu przywraca sobie (Stos [StackFutureActivate] x 3) HP"\n- za każdym razem gdy [Laceration] aktywuje się na tej jednostce lub na Grzesznikach, przywraca HP równe obrażeniom tego [Laceration] (zaokrąglone w dół)
376. [[refraction6] Pasywka wroga [9567031] — nazwa] 미래 [未來]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567031].name
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [[refraction6] Pasywka wroga [9567031] — opis] [StackFutureActivate]면, 다음 효과가 적용됨\n<mark=#000000AA>- <color=#d93737><s></color>턴 시작 시 모든 수감자의 [Laceration] 횟수가 (3 + 현재 턴 수/2)만큼 증가 (소수점 올림)<color=#ff0000></s></color></mark>\n- 스킬 ‘혈화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackFutureActivate] x 3)만큼 자신의 체력 회복’ 효과 추가\n- 자신 또는 수감자에게 [Laceration]이 발동할 때마다 해당 [Laceration] 피해만큼 자신의 체력을 회복 (소수점 버림)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567031].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#d93737>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackFutureActivate], [Laceration]
   znaczenie tagów: [StackFutureActivate] = 미래 상태 / In the Future; [Laceration] = 출혈 / Bleed
   EN: When [StackFutureActivate], gain the following effects:\n<mark=#000000AA>- <color=#d93737><s></color>Turn Start: All Sinners gain +(3 + # of current turn / 2) [Laceration] Count (rounded up)<color=#ff0000></s></color></mark>\n- Skill "Bloodflower" gains Final Power +2 and its final Coin gains "On Hit,\nheal ([StackFutureActivate] Stack x 3) HP on self" effect\n- Whenever [Laceration] activates on self or on Sinners, heal HP equal to the said [Laceration] damage (rounded down)
   PL: gdy aktywny jest [StackFutureActivate], zyskuje następujące efekty:\n<mark=#000000AA>- <color=#d93737><s></color>na początku tury wszyscy Grzesznicy zyskują +(3 + numer bieżącej\ntury/2) Licznika [Laceration] (zaokrąglone w górę)<color=#ff0000></s></color></mark>\n- Umiejętność „Bloodflower" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu przywraca sobie (Stos [StackFutureActivate] x 3) HP"\n- za każdym razem gdy [Laceration] aktywuje się na tej jednostce lub na Grzesznikach, przywraca HP równe obrażeniom tego [Laceration] (zaokrąglone w dół)
378. [[refraction6] Pasywka wroga [9567032] — nazwa] 미래 [未來]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567032].name
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [[refraction6] Pasywka wroga [9567032] — opis] [StackFutureActivate]면, 다음 효과가 적용됨\n- 턴 시작 시 모든 수감자의 [Laceration] 횟수가 (3 + 현재 턴 수/2)만큼 증가 (소수점 올림)\n<mark=#000000AA>- <color=#d93737><s></color>스킬 ‘혈화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackFutureActivate] x 3)만큼 자신의 체력 회복’ 효과 추가<color=#ff0000></s></color></mark>\n- 자신 또는 수감자에게 [Laceration]이 발동할 때마다 해당 [Laceration] 피해만큼 자신의 체력을 회복 (소수점 버림)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567032].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#d93737>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackFutureActivate], [Laceration]
   znaczenie tagów: [StackFutureActivate] = 미래 상태 / In the Future; [Laceration] = 출혈 / Bleed
   EN: When [StackFutureActivate], gain the following effects:\n- Turn Start: All Sinners gain +(3 + # of current turn / 2) [Laceration] Count (rounded up)\n<mark=#000000AA>- <color=#d93737><s></color>Skill "Bloodflower" gains Final Power +2 and its final Coin gains "On Hit,\nheal ([StackFutureActivate] Stack x 3) HP on self" effect<color=#ff0000></s></color></mark>\n- Whenever [Laceration] activates on self or on Sinners, heal HP equal to the said [Laceration] damage (rounded down)
   PL: gdy aktywny jest [StackFutureActivate], zyskuje następujące efekty:\n- na początku tury wszyscy Grzesznicy zyskują +(3 + numer bieżącej tury/2) Licznika [Laceration] (zaokrąglone w górę)\n<mark=#000000AA>- <color=#d93737><s></color>Umiejętność „Bloodflower" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu\nprzywraca sobie (Stos [StackFutureActivate] x 3) HP"<color=#ff0000></s></color></mark>\n- za każdym razem gdy [Laceration] aktywuje się na tej jednostce lub na Grzesznikach, przywraca HP równe obrażeniom tego [Laceration] (zaokrąglone w dół)
380. [[refraction6] Pasywka wroga [9567033] — nazwa] 미래 [未來]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567033].name
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [[refraction6] Pasywka wroga [9567033] — opis] [StackFutureActivate]면, 다음 효과가 적용됨\n- 턴 시작 시 모든 수감자의 [Laceration] 횟수가 (3 + 현재 턴 수/2)만큼 증가 (소수점 올림)\n- 스킬 ‘혈화’의 최종 위력 +2, 마지막 코인에 ‘적중 시 ([StackFutureActivate] x 3)만큼 자신의 체력 회복’ 효과 추가\n<mark=#000000AA>- <color=#d93737><s></color>자신 또는 수감자에게 [Laceration]이 발동할 때마다 해당 [Laceration] 피해만큼 자신의 체력을 회복 (소수점 버림)<color=#ff0000></s></color></mark>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=9567033].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <mark=#000000AA>, <color=#d93737>, <s>, </color>, <color=#ff0000>, </s>, </mark>, \n, [StackFutureActivate], [Laceration]
   znaczenie tagów: [StackFutureActivate] = 미래 상태 / In the Future; [Laceration] = 출혈 / Bleed
   EN: When [StackFutureActivate], gain the following effects:\n- Turn Start: All Sinners gain +(3 + # of current turn / 2) [Laceration] Count (rounded up)\n- Skill "Bloodflower" gains Final Power +2 and its final Coin gains "On Hit,\nheal ([StackFutureActivate] Stack x 3) HP" effect\n<mark=#000000AA>- <color=#d93737><s></color>Whenever [Laceration] activates on self or on Sinners, heal HP equal to the said [Laceration] damage (rounded down)<color=#ff0000></s></color></mark>
   PL: gdy aktywny jest [StackFutureActivate], zyskuje następujące efekty:\n- na początku tury wszyscy Grzesznicy zyskują +(3 + numer bieżącej tury/2) Licznika [Laceration] (zaokrąglone w górę)\n- Umiejętność „Bloodflower" zyskuje Moc Końcową +2, a jej ostatnia moneta zyskuje efekt „przy trafieniu przywraca sobie (Stos [StackFutureActivate] x 3) HP"\n<mark=#000000AA>- <color=#d93737><s></color>za każdym razem gdy [Laceration] aktywuje się na tej jednostce lub na Grzesznikach, przywraca HP równe\nobrażeniom tego [Laceration] (zaokrąglone w dół)<color=#ff0000></s></color></mark>
382. [[refraction6] Pasywka wroga [956704] — nazwa] 삼세인과 [三世因果]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956704].name
   limit: do 90 znaków
   EN: Causality that Threads the Past, the Present, and the Future [三世因果]
   PL: Causality that Threads the Past, the Present, and the Future [三世因果]
383. [[refraction6] Pasywka wroga [956704] — opis] 동일한 대상과의 합 횟수가 10 이상이 되면, 합 위력이 현재\n(합 횟수/10)만큼 무작위로 증가 또는 감소 (소수점 버림)\n\n스테이지 시작 시,\n- 제 1 구간에 등장한 나생접::고치의 체력으로 전투 시작 (보호막 제외)\n- [StackPastActivate]/[StackPresentActivate]/[StackFutureActivate] 각각 10 얻음\n\n체력이 66%/33% 미만이면, 슬롯 패턴이 변경됨\n- 이번 전투에서 처음으로 체력이 <color=#ff6000><mark=#ff000040><b><u>66%/33% 미만</u></b></mark></color>으로 내려가면,\n다음 턴에 <color=#ff6000><mark=#ff000040><b><u>[StackPastActivate], [StackPresentActivate], [StackFutureActivate]를 각각 10 얻음</u></b></mark></color>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956704].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StackPastActivate], [StackPresentActivate], [StackFutureActivate], [TabExplain]
   znaczenie tagów: [StackPastActivate] = 과거 상태 / In the Past; [StackPresentActivate] = 현재 상태 / In the Present; [StackFutureActivate] = 미래 상태 / In the Future
   EN: At 10+ Clashes against the same target, randomly gain or lose Clash Power by (Clash Count / 10) in a Clash (rounded down)\n\nEncounter Start:\n- Begin Encounter with the same HP as Butterfly[TabExplain] of Entangled Lives::The Pupa (excluding Shield)\n- Gain 10 Stacks each of [StackPastActivate] / [StackPresentActivate] / [StackFutureActivate]\n\nAt less than 66%/33% HP, gain new Slot patterns\n- <color=#ff6000><mark=#ff000040><b><u>When this unit's HP drops below 66%/33%</u></b></mark></color> for the first time in this Encounter, <color=#ff6000><mark=#ff000040><b><u>gain 10 Stacks each of [StackPastActivate], [StackPresentActivate], and [StackFutureActivate]</u></b></mark></color> next turn
   PL: przy 10+ Starciach z tym samym celem, w Starciu Moc Starcia losowo rośnie lub maleje o (liczba Starć/10) (zaokrąglone w dół)\n\nna początku walki:\n- rozpoczyna walkę z HP równym Butterfly[TabExplain] of Entangled Lives::The Pupa (bez Tarczy)\n- zyskuje po 10 Stosów [StackPastActivate] / [StackPresentActivate] / [StackFutureActivate]\n\nprzy poniżej 66%/33% HP zyskuje nowe wzorce slotów\n- gdy HP tej jednostki po raz pierwszy w tej walce spadnie <color=#ff6000><mark=#ff000040><b><u>poniżej 66%/33%</u></b></mark></color>, w następnej turze <color=#ff6000><mark=#ff000040><b><u>zyskuje po 10 Stosów [StackPastActivate], [StackPresentActivate] i [StackFutureActivate]</u></b></mark></color>
384. [[refraction6] Pasywka wroga [956705] — nazwa] 나생의 시간
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956705].name
   limit: do 40 znaków
   EN: Moment of Entangled Lives
   PL: Moment of Entangled Lives
385. [[refraction6] Pasywka wroga [956705] — opis] 턴 시작 시 <color=#ff6000><mark=#ff000040><b><u>가장 높은 수치의 상태가 활성화</u></b></mark></color>되고 특수한 스킬을 사용\n- 수치가 동일하면 상태 유지\n- 비활성화된 상태는 [StackPast]/[StackPresent]/[StackFuture]로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>상태가 변경</u></b></mark></color>되었으면, [TimeGap] 1 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>나생접 환영::과거/현재/미래가 메인 타겟으로 피격받을 때</u></b></mark></color>마다\n나생접::나비가 보유한 [StackPastActivate]/[StackPresentActivate]/[StackFutureActivate] 수치가 감소\n\n<color=#ff6000><mark=#ff000040><b><u>[StackPastActivate]/[StackPresentActivate]/[StackFutureActivate]의 수치가 높아지면,</u></b></mark></color>\n나생접::나비의 스킬 위력과 피해량이 <color=#ff6000><mark=#ff000040><b><u>크게 증가하고</u></b></mark></color>\n부여 및 획득하는 <color=#ff6000><mark=#ff000040><b><u>상태 이상 수치가 크게 증가</u></b></mark></color>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956705].desc
   limit: do 1190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StackPast], [StackPresent], [StackFuture], [TimeGap], [StackPastActivate], [StackPresentActivate], [StackFutureActivate], [TabExplain]
   znaczenie tagów: [StackPast] = 과거 상태 (비활성화) / In the Past (Deactivated); [StackPresent] = 현재 상태 (비활성화) / In the Present (Deactivated); [StackFuture] = 미래 상태 (비활성화) / In the Future (Deactivated); [TimeGap] = 시간 괴리 / Temporal Disjunction; [StackPastActivate] = 과거 상태 / In the Past; [StackPresentActivate] = 현재 상태 / In the Present; [StackFutureActivate] = 미래 상태 / In the Future
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Activate the highest-Stacked state of time</u></b></mark></color> between [StackPastActivate], [StackPresentActivate], and [StackFutureActivate] and use a special Skill\n- If multiple states of time share the highest Stack, the currently active state of time does not change\n- Inactive states of time become [StackPast], [StackPresent], or [StackFuture], respectively\n- When the <color=#ff6000><mark=#ff000040><b><u>currently active state of time changes</u></b></mark></color>, gain 1 [TimeGap]\n\n<color=#ff6000><mark=#ff000040><b><u>Every time Illusory Butterfly[TabExplain] of Entangled Lives::The Past / The Present / The Future are hit as main targets</u></b></mark></color>, Butterfly[TabExplain] of Entangled Lives::Imago loses [StackPastActivate] / [StackPresentActivate] / [StackFutureActivate] Stack\n\n<color=#ff6000><mark=#ff000040><b><u>Higher [StackPastActivate] / [StackPresentActivate] / [StackFutureActivate] Stacks</u></b></mark></color> lead to Butterfly[TabExplain] of Entangled Lives::Imago's Skill Power and damage output becoming <color=#ff6000><mark=#ff000040><b><u>greatly enhanced</u></b></mark></color>, and <color=#ff6000><mark=#ff000040><b><u>greatly increase the amount of status effects it inflicts or gains</u></b></mark></color>
   PL: na początku tury <color=#ff6000><mark=#ff000040><b><u>aktywuje się stan czasu o najwyższej wartości</u></b></mark></color> spośród [StackPastActivate], [StackPresentActivate] i [StackFutureActivate], a jednostka używa specjalnej Umiejętności\n- jeżeli kilka stanów czasu ma najwyższą wartość, aktywny stan czasu pozostaje bez zmian\n- nieaktywne stany czasu zmieniają się odpowiednio w [StackPast], [StackPresent] lub [StackFuture]\n- gdy <color=#ff6000><mark=#ff000040><b><u>aktywny stan czasu ulegnie zmianie</u></b></mark></color>, zyskuje 1 [TimeGap]\n\n<color=#ff6000><mark=#ff000040><b><u>za każdym razem gdy Illusory Butterfly[TabExplain] of Entangled Lives::The Past / The Present / The Future zostaną trafione jako główne cele</u></b></mark></color>, Butterfly[TabExplain] of Entangled Lives::Imago traci Stos [StackPastActivate] / [StackPresentActivate] / [StackFutureActivate]\n\n<color=#ff6000><mark=#ff000040><b><u>wyższe Stosy [StackPastActivate] / [StackPresentActivate] / [StackFutureActivate]</u></b></mark></color> sprawiają, że Moc Umiejętności i obrażenia Butterfly[TabExplain] of Entangled Lives::Imago stają się <color=#ff6000><mark=#ff000040><b><u>znacznie większe</u></b></mark></color>, a <color=#ff6000><mark=#ff000040><b><u>nakładane i otrzymywane wartości statusów znacznie rosną</u></b></mark></color>
386. [[refraction6] Pasywka wroga [956801] — nazwa] 일첨지명[一櫼之命]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956801].name
   limit: do 50 znaków
   EN: Life Hanging on a Wedge [一櫼之命]
   PL: Life Hanging on a Wedge [一櫼之命]
387. [[refraction6] Pasywka wroga [956801] — opis] 스테이지 시작 시 [YesdragonSelfRefraction] 3 얻음\n턴 종료 시 다음 턴에 [YesdragonSelfRefraction] 1 얻음\n‘진노’ 패시브가 발동할 때마다 얻는 [YesdragonSelfRefraction] 1 씩 증가
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956801].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [YesdragonSelfRefraction]
   znaczenie tagów: [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: Encounter Start: Gain 3 [YesdragonSelfRefraction]\nTurn End: Gain 1 [YesdragonSelfRefraction] next turn\nGain +1 more [YesdragonSelfRefraction] from this effect every time the "Thundering Wrath" Passive triggers
   PL: na początku walki zyskuje 3 [YesdragonSelfRefraction]\nna koniec tury zyskuje 1 [YesdragonSelfRefraction] w następnej turze\nza każdym razem gdy pasywka „Thundering Wrath" się aktywuje, z tego efektu zyskuje o 1 [YesdragonSelfRefraction] więcej
388. [[refraction6] Pasywka wroga [956802] — nazwa] 진노[震怒]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956802].name
   limit: do 40 znaków
   EN: Thundering Wrath [震怒]
   PL: Thundering Wrath [震怒]
389. [[refraction6] Pasywka wroga [956802] — opis] 역린 부위가 자신을 메인 타겟 대상으로 한 스킬 피해만 받으며, 그 외의 피해를 받지 않음\n역린 부위 피격 시 다음 턴 스킬 슬롯에서 역린 부위가 사라지며, ‘역린지화’ 스킬로 소모한 [YesdragonSelfRefraction] 수치 1당, [AttackUp] 1, [DefenseDown] 1 얻음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956802].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [YesdragonSelfRefraction], [AttackUp], [DefenseDown]
   znaczenie tagów: [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: The Inverted Scale Part takes damage only from Skills that it is the main target of; does not take damage from any other sources\nWhen the Inverted Scale Part is hit, remove the Inverted Scale Part from the Skill Slots next turn; gain 1 [AttackUp] and 1 [DefenseDown] for every [YesdragonSelfRefraction] Stack consumed by the "Wrath of the Inverted Scale" Skill
   PL: część Inverted Scale otrzymuje obrażenia tylko z Umiejętności, dla których jest głównym celem; nie otrzymuje obrażeń z innych źródeł\ngdy część Inverted Scale zostanie trafiona, znika ze slotów Umiejętności w następnej turze; za każdy Stos [YesdragonSelfRefraction] zużyty przez Umiejętność „Wrath of the Inverted Scale" zyskuje 1 [AttackUp] i 1 [DefenseDown]
390. [[refraction6] Pasywka wroga [956804] — nazwa] 용의 비늘
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956804].name
   limit: do 40 znaków
   EN: Dragon's Scale
   PL: Dragon's Scale
391. [[refraction6] Pasywka wroga [956804] — opis] [Agility]과 [Binding]에 영향 받지 않음.\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 흐트러짐 손상 피해량 -50%
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956804].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Binding], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Agility] = 신속 / Haste; [Binding] = 속박 / Bind; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Unaffected by [Agility] and [Binding]\nTake -50% HP damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]; -50% to Stagger Threshold raised by [Vibration]
   PL: niezależna od [Agility] i [Binding]\notrzymuje -50% obrażeń HP od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]; [Vibration] podnosi Próg Oszołomienia o 50% mniej
392. [[refraction6] Pasywka wroga [956805] — nazwa] 오를 수 없는 하늘
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956805].name
   limit: do 40 znaków
   EN: The Unreachable Heavens
   PL: The Unreachable Heavens
393. [[refraction6] Pasywka wroga [956805] — opis] 스테이지 시작 시 머리 부위가 최대 체력의 100% 만큼 보호막을 얻음\n턴 종료 시 보호막이 사라지지 않음\n보호막이 파괴되면 페이즈가 변경됨
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956805].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Encounter Start: The Head Part gains Shield equal to 100% of this unit's max HP\nDoes not lose Shield at Turn End\nWhen the Shield is broken, enter a new phase
   PL: na początku walki część Head zyskuje Tarczę równą 100% Maks. HP tej jednostki\nna koniec tury nie traci Tarczy\ngdy Tarcza pęknie, rozpoczyna się nowa faza
394. [[refraction6] Pasywka wroga [956901] — nazwa] 더럽혀진 몸
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956901].name
   limit: do 40 znaków
   EN: Tarnished Body
   PL: Tarnished Body
395. [[refraction6] Pasywka wroga [956901] — opis] 모든 부위가 부위 파괴 가능 및 적출 불가 상태로 변경됨\n파괴된 부위는 3턴 뒤 최대 체력의 30%로 <noparse>재생</noparse>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: All Parts become Breakable and Unseverable\nBroken Parts regenerate in 3 turns with 30% HP
   PL: wszystkie Części mogą być zniszczone, ale nie da się ich odciąć\nzniszczone Części po 3 turach <noparse>odrastają</noparse> z 30% HP
396. [[refraction6] Pasywka wroga [956902] — nazwa] 일첨지명[一櫼之命]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956902].name
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [[refraction6] Pasywka wroga [956902] — opis] <noparse>매화첨</noparse> 부위가 파괴되지 않는 동안, 사망하지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956902].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>
   EN: Cannot be killed as long as the Flower-burying Wedge Part isn't broken
   PL: nie może zginąć dopóki część Flower-burying Wedge nie zostanie zniszczona
398. [[refraction6] Pasywka wroga [956903] — nazwa] 부서진 비늘
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956903].name
   limit: do 40 znaków
   EN: Broken Scale
   PL: Broken Scale
399. [[refraction6] Pasywka wroga [956903] — opis] 역린 부위가 파괴될 시, ‘진노’ 패시브가 발동하지 않음.\n역린 부위가 파괴되어 있는 동안 모든 부위에 [AttackUp] 3, [DefenseDown] 6 얻음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956903].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When the Inverted Scale Part is broken, the "Thundering Wrath" Passive does not activate\nWhile the Inverted Scale Part is broken, all Parts gain 3 [AttackUp] and 6 [DefenseDown]
   PL: gdy część Inverted Scale zostanie zniszczona, pasywka „Thundering Wrath" nie aktywuje się\ndopóki część Inverted Scale jest zniszczona, wszystkie Części zyskują 3 [AttackUp] i 6 [DefenseDown]
400. [[refraction6] Pasywka wroga [956904] — nazwa] 파괴된 머리
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956904].name
   limit: do 40 znaków
   EN: Broken Skull
   PL: Broken Skull
401. [[refraction6] Pasywka wroga [956904] — opis] 머리 부위가 파괴되어 있는 동안 매턴 마다 모든 부위에 [Vulnerable] 2 부여
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956904].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: While the Head part is broken, all Parts gain 2 [Vulnerable] every turn
   PL: dopóki część Head jest zniszczona, wszystkie Części zyskują 2 [Vulnerable] co turę
402. [[refraction6] Pasywka wroga [956907] — nazwa] 매화만개[梅花滿開]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956907].name
   limit: do 60 znaków
   EN: Erumpent Flower-burying Efflorescence [梅花滿開]
   PL: Erumpent Flower-burying Efflorescence [梅花滿開]
403. [[refraction6] Pasywka wroga [956907] — opis] 스테이지 시작 시 [YesdragonSelfRefraction] 3 얻음\n턴 종료 시 다음 턴에 [YesdragonSelfRefraction] 1 얻음\n‘진노’ 패시브가 발동할 때마다 얻는 [YesdragonSelfRefraction] 1 씩 증가\n- 역린 부위가 파괴되면, 추가 수치 초기화
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956907].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [YesdragonSelfRefraction]
   znaczenie tagów: [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: Encounter Start: Gain 3 [YesdragonSelfRefraction]\nTurn End: Gain 1 [YesdragonSelfRefraction] next turn\nGain +1 more [YesdragonSelfRefraction] from this effect every time the "Thundering Wrath" Passive triggers\n- When the Inverted Scale is broken, reset the increased [YesdragonSelfRefraction] gain
   PL: na początku walki zyskuje 3 [YesdragonSelfRefraction]\nna koniec tury zyskuje 1 [YesdragonSelfRefraction] w następnej turze\nza każdym razem gdy pasywka „Thundering Wrath" się aktywuje, z tego efektu zyskuje o 1 [YesdragonSelfRefraction] więcej\n- gdy część Inverted Scale zostanie zniszczona, przyrost wartości zostaje zresetowany
404. [[refraction6] Pasywka wroga [956908] — nazwa] 진노[震怒]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956908].name
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [[refraction6] Pasywka wroga [956908] — opis] 역린 부위가 자신을 메인 타겟 대상으로 한 스킬 피해만 받으며, 그 외의 피해를 받지 않음\n역린 부위 피격 시 다음 턴 스킬 슬롯에서 역린 부위가 사라지며, ‘역린지화’ 스킬로 소모한 [YesdragonSelfRefraction] 수치 1당, [AttackUp] 1, [DefenseDown] 1 얻음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=956908].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [[refraction6] Pasywka wroga [957001] — nazwa] 용맥[龍脈]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957001].name
   limit: do 40 znaków
   EN: Dragon's Vein [龍脈]
   PL: Dragon's Vein [龍脈]
407. [[refraction6] Pasywka wroga [957001] — opis] 턴 시작 시 본체의 최대 체력의 300%만큼 보호막을 얻음\n- 공격 스킬 장착 시 해당 패시브 효과 발동하지 않음\n턴 시작 시 흐트러짐 상태이면, 흐트러짐을 해제
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957001].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Gain Shield equal to 300% of the Core's max HP\n- This effect does not trigger when Attack Skills are equipped\nTurn Start: When Staggered, recover from Stagger
   PL: na początku tury zyskuje Tarczę równą 300% Maks. HP Core\n- ten efekt nie aktywuje się gdy wyposażone są Umiejętności ataku\nna początku tury, jeżeli jest Oszołamiona, dochodzi do siebie z Oszołamienia
408. [[refraction6] Pasywka wroga [957002] — nazwa] 흘러나오는 용맥
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957002].name
   limit: do 40 znaków
   EN: The Dragon's Bleeding Vein
   PL: The Dragon's Bleeding Vein
409. [[refraction6] Pasywka wroga [957002] — opis] 피격 시 공격한 대상에게 다음 턴에 [YesdragonPower] 부여\n\n사망한 즉시 모든 수감자에게 [YesdragonPower] 부여
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957002].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [YesdragonPower]
   znaczenie tagów: [YesdragonPower] = 용의 기운[龍氣] / Dragon's Spirit [龍氣]
   EN: When hit, apply [YesdragonPower] on the attacker next turn\n\nOn death, immediately apply [YesdragonPower] on all Sinners
   PL: przy otrzymaniu trafienia nakłada [YesdragonPower] na atakującego w następnej turze\n\nnatychmiast po śmierci nakłada [YesdragonPower] na wszystkich Grzeszników
410. [[refraction6] Pasywka wroga [957003] — nazwa] 회광반조[回光返照]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957003].name
   limit: do 40 znaków
   EN: One Last Radiance [回光返照]
   PL: One Last Radiance [回光返照]
411. [[refraction6] Pasywka wroga [957003] — opis] 이번 턴에 체력이 0이 되는 피해를 받으면, 해당 턴 동안 체력이 1 미만으로 감소하지 않고, 피해로 인한 흐트러짐 상태를 해제함.\n이후 해당 턴 동안 피해로 인해 흐트러지거나 사망하지 않고, 해당 턴의 마지막 순서에 ‘자천멸오’ 스킬을 사용함.
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957003].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain]
   EN: When this unit takes damage that brings its HP down to 0, this unit's HP does not drop below 1 for the turn; recover from Stagger due to damage\nFor the rest of the turn, this unit cannot be Staggered or killed due to damage; then, use "Impale the Self, Impurity[TabExplain] to Purge" at the very end of that turn
   PL: gdy ta jednostka otrzyma obrażenia sprowadzające jej HP do 0, w tej turze jej HP nie spada poniżej 1; dochodzi do siebie z Oszołamienia od obrażeń\nprzez resztę tury ta jednostka nie może zostać Oszołamiona ani zginąć od obrażeń, a na samym końcu tury używa Umiejętności „Impale the Self, Impurity[TabExplain] to Purge"
412. [[refraction6] Pasywka wroga [957004] — nazwa] 고고한 정기
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957004].name
   limit: do 40 znaków
   EN: Lofty Energy
   PL: Lofty Energy
413. [[refraction6] Pasywka wroga [957004] — opis] 이 유닛은 회복과 원호 방어를 받지 않음\n자신을 메인 타겟 대상으로 한 스킬 피해만 받으며, 그 외의 피해를 받지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957004].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain]
   EN: This unit cannot be subject to healing or Assist Defense[TabExplain] effects\nTake damage only from Skills that this unit is the main target of; does not take damage from any other sources
   PL: ta jednostka nie może być leczona ani korzystać z Asysty obronnej[TabExplain]\notrzymuje obrażenia tylko z Umiejętności, dla których jest głównym celem; nie otrzymuje obrażeń z innych źródeł
414. [[refraction6] Pasywka wroga [957006] — nazwa] 굴절된 출구
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957006].name
   limit: do 40 znaków
   EN: Refracted Egress
   PL: Refracted Egress
415. [[refraction6] Pasywka wroga [957006] — opis] 퇴각 불가능
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957006].desc
   limit: do 120 znaków
   EN: Cannot Retreat
   PL: Cannot Retreat
416. [[refraction6] Pasywka wroga [957101] — nazwa] 물귀원주[物歸原主]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957101].name
   limit: do 40 znaków
   EN: Return to Origin [物歸原主]
   PL: Return to Origin [物歸原主]
417. [[refraction6] Pasywka wroga [957101] — opis] 응룡의 ‘낙뢰’ 스킬 피격 시, 바로 사망하며 응룡에게 [YesdragonSelfRefraction] 1 부여
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957101].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [YesdragonSelfRefraction]
   znaczenie tagów: [YesdragonSelfRefraction] = 매화침[埋花針] / Flower-burying Pin [埋花針]
   EN: When hit by Yinglong's "Levinfall" Skill, die instantly and apply 1 [YesdragonSelfRefraction] on Yinglong
   PL: gdy zostanie trafiona Umiejętnością „Levinfall" Yinglonga, natychmiast ginie i nakłada 1 [YesdragonSelfRefraction] na Yinglonga
418. [[refraction6] Pasywka wroga [955101] — nazwa] 검지 아비 뤼엔
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955101].name
   limit: do 40 znaków
   EN: Rien, The Index Nursefather
   PL: Rien, The Index Nursefather
419. [[refraction6] Pasywka wroga [955101] — opis] <color=#ff9000><mark=#ff000040><b><u>일방 공격으로 받는 피해량 -50%</u></b></mark></color>\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -50%\n[UnlockBuff_Base]으로 정신력 회복 시 정신력이 15 미만이면, 정신력을 15까지 회복\n\n스테이지 시작 시, [BurningWoundRien_Mask] 얻고 정신력을 45까지 회복\n\n체력이 55% 이하면, 턴이 종료되고 페이즈 변경\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- [StackRienSpecialSkill] 0으로 초기화
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955101].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [UnlockBuff_Base], [BurningWoundRien_Mask], [StackRienSpecialSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [UnlockBuff_Base] = 해금 / Unlock; [BurningWoundRien_Mask] = 뤼엔의 가면 / Rien's Mask; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: <color=#ff9000><mark=#ff000040><b><u>Take -50% damage from Unopposed Attacks</u></b></mark></color>\nTake -50% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\nWhen healing SP from [UnlockBuff_Base], if this unit's SP is below 15, heal SP up to 15\n\nEncounter Start: Gain [BurningWoundRien_Mask] and heal SP up to 45\n\nAt 55%- HP, end the turn and gain a new pattern\n- Remove all effects other than those exclusive to this unit\n- Change [StackRienSpecialSkill] Stack to 0
   PL: <color=#ff9000><mark=#ff000040><b><u>otrzymuje -50% obrażeń z ataków bez kontr</u></b></mark></color>\notrzymuje -50% obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\ngdy odzyskuje Poczytalność z [UnlockBuff_Base], jeżeli Poczytalność tej jednostki jest poniżej 15, przywraca ją do 15\n\nna początku walki zyskuje [BurningWoundRien_Mask] i przywraca Poczytalność do 45\n\nprzy 55% HP lub mniej, tura się kończy i rozpoczyna się nowy wzorzec\n- usuwa wszystkie efekty inne niż własne tej jednostki\n- zmienia Stos [StackRienSpecialSkill] na 0
420. [[refraction6] Pasywka wroga [955101] — tekst klimatyczny] 지령이 말한 대로 그때를 기다렸다고.\n딸이 나가도 기다리고 기다렸지.\n\n그러다 림버스 컴퍼니에서 연락이 왔고 뒷문이 열려있더구나.\n그리고 단말기가 울려서 딸을 데리러 가야 할 때가 되었다는 것을 알았지.
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955101].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I waited for "the moment" as the Prescript told me to.\nEven after my darling daughter left, I waited.\n\nAnd after a while, I was contacted by Limbus Company, and saw that the Backdoor was open.\nThat's when the device beeped and let me know that it was finally time to bring my daughter home.
   PL: Czekałem na „tamtą chwilę", tak jak nakazywała Preskrypcja.\nCzekałem, nawet gdy moja córeczka odeszła.\n\nPo pewnym czasie skontaktowało się ze mną Limbus Company, a ja zobaczyłem, że tylne drzwi są otwarte.\nWtedy urządzenie zapiszczało i dało mi znać, że przyszedł czas, by przywrócić córkę do domu.
421. [[refraction6] Pasywka wroga [955102] — nazwa] 신탁 단말기 [카두세우스]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955102].name
   limit: do 40 znaków
   EN: Oracle Device [Caduceus]
   PL: Oracle Device [Caduceus]
422. [[refraction6] Pasywka wroga [955102] — opis] <color=#ff9000><mark=#ff000040><b><u>코인마다 무기가 무작위로 정해지며 특수 효과 적용</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\n공격 스킬 사용 시, [StackRienSpecialSkill] 1 얻음 (최대 9)\n- 스킬별 1회 획득 가능 (동일한 스킬로 2를 초과하여 얻을 수 없음)\n\n<color=#ff9000><mark=#ff000040><b><u>턴 시작 시 [StackRienSpecialSkill]가 9면, 강력한 스킬을 사용</u></b></mark></color>\n- 첫 사용 후 공격 종료 시, [Shin_Rien] 얻음\n- 스킬 종류별 [StackRienSpecialSkill] 획득 여부 초기화\n- 속도 최솟값, 최댓값 +15\n- 턴 종료 시 다음 턴에, [Vulnerable] 1, [ResultReduction] 2 얻음\n\n등장 이후 네 번째 턴 시작 시, [StackRienSpecialSkill]가 9 미만이면, 9까지 증가하고 (증가한 수치 x 3)만큼 [KarmaOfIndexRien] 얻음\n- 이후 네 턴마다 이 효과 발동
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955102].desc
   limit: do 1180 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RienWeapon01Hatchet], [RienWeapon02Stiletto], [RienWeapon03Greatsword], [RienWeapon04Rapier], [RienWeapon05Sledgehammer], [RienWeapon06Ultragreatsword], [RienWeapon07Lance], [RienWeapon08Chain], [RienWeapon09Scythe], [StackRienSpecialSkill], [Shin_Rien], [Vulnerable], [ResultReduction], [KarmaOfIndexRien]
   znaczenie tagów: [RienWeapon01Hatchet] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [RienWeapon02Stiletto] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [RienWeapon03Greatsword] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [RienWeapon04Rapier] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [RienWeapon05Sledgehammer] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [RienWeapon06Ultragreatsword] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a greatsword...; [RienWeapon07Lance] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [RienWeapon08Chain] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: <color=#ff9000><mark=#ff000040><b><u>A random weapon is assigned to every Coin. Each weapon has a unique effect.</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\nWhen using an Attack Skill, gain 1 [StackRienSpecialSkill] (max 9)\n- Can be gained once per Skill; does not gain Stack from the same Skill twice\n\n<color=#ff9000><mark=#ff000040><b><u>Turn Start: At 9 [StackRienSpecialSkill] Stacks, use a powerful Skill</u></b></mark></color>\n- Attack End: After using the powerful Skill for the first time, gain [Shin_Rien]\n- Reset the per-Skill [StackRienSpecialSkill] cap\n- Min & Max Speed +15\n- Turn End: Gain 1 [Vulnerable] and 2 [ResultReduction] next turn\n\nTurn 4 Start after entering the field: At less than 9 [StackRienSpecialSkill], bring its Stack to 9; then, gain (Stack gained x 3) [KarmaOfIndexRien]\n- Then, activate this effect every 4 turns
   PL: <color=#ff9000><mark=#ff000040><b><u>każdej monecie przypisywana jest losowa broń; każda broń ma unikatowy efekt.</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\nprzy użyciu Umiejętności ataku zyskuje 1 [StackRienSpecialSkill] (maks. 9)\n- można zdobyć 1 raz na Umiejętność; ta sama Umiejętność nie daje Stosu drugi raz\n\n<color=#ff9000><mark=#ff000040><b><u>na początku tury przy 9 [StackRienSpecialSkill], używa potężnej Umiejętności</u></b></mark></color>\n- po zakończeniu ataku po pierwszym użyciu zyskuje [Shin_Rien]\n- resetuje licznik zdobywania [StackRienSpecialSkill] per Umiejętność\n- Szybkość minimalna i maksymalna +15\n- na koniec tury zyskuje w następnej turze 1 [Vulnerable] i 2 [ResultReduction]\n\nprzy czwartym początku tury po pojawieniu się w walce, jeżeli [StackRienSpecialSkill] jest poniżej 9, podnosi Stos do 9, po czym zyskuje (liczba zdobytych Stosów x 3) [KarmaOfIndexRien]\n- następnie ten efekt aktywuje się co 4 tury
423. [[refraction6] Pasywka wroga [955102] — tekst klimatyczny] 단말기 안에는 특이점과 유사한 기술을 이용해 형태와 질량을 변동시킬 수 있는, 금속 같은 액체가 들어 있다.\n이 액체는 단말기가 수령한 지령에 따라 모습을 바꾸며, 살해 대상의 정보와 주어진 제한 시간에 맞춰 무기로 변환된다.\n어느 날에는 지나치게 작은 단검이 배정되어 다른 무기로 바뀌기를 기다렸지만, 살해 제한 시간이 다가올 때까지 쓸만한 무기가 나오지 않았다. 결국, 마지막까지 기다려 나온 것이 포크였기에, 그 포크로 대상을 죽여야만 했다.
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955102].flavor
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A vial of what looks like liquid metal capable of changing its shape and mass, its qualities almost like those of Singularities, swishes inside the Device.\nThe form the fluid takes is contingent on the Prescript the Device receives. The weapons it produces depend on the information regarding the target and the time limit given to carry out the assassination.\nOne day, as he received a dagger too small for the task, he elected to wait until it produced a different weapon. However, despite the approaching deadline, it refused to provide him a proper weapon; he had no choice but to kill his target with a fork.
   PL: Wewnątrz Urządzenia chlupocze fiolka płynnego metalu zdolnego zmieniać kształt i masę — jego właściwości niemal przypominają Singularności.\nPostać, jaką przybiera płyn, zależy od Preskrypcji otrzymanej przez Urządzenie. Wytwarzana broń zależy od informacji o celu i limitu czasu wyznaczonego na dokonanie zabójstwa.\nPewnego dnia otrzymał sztylet zbyt mały do tego zadania i postanowił zaczekać, aż pojawi się inna broń. Jednak mimo zbliżającego się terminu Urządzenie nie chciało dać mu porządnej broni; nie pozostało mu nic innego, jak zabić cel widelcem.
424. [[refraction6] Pasywka wroga [955103] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955103].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL: Will of the Prescript
425. [[refraction6] Pasywka wroga [955103] — opis] 턴 시작 시,\n- [UnlockBuff_Base] 단계에 따라 [IndexPrescript_Base_2nd] 얻음\n- 무작위 수감자에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함\n<color=#ff9000><mark=#ff000040><b><u>- [IndexPrescriptTargetToPersonality]에게 사용하는 스킬의 코인이 전부 [SuperCoin]으로 변경됨</u></b></mark></color>\n\n공격 시 [IndexPrescriptTargetToPersonality]이 사망하거나 대상을 공격하지 못하게 될 경우,\n<color=#ff9000><mark=#ff000040><b><u>사용하지 않은 나머지 스킬을 무작위 수감자에게 사용\n- 현재 체력이 가장 낮은 대상 우선 (체력이 1인 경우 제외)\n- 무작위로 선택된 수감자가 사망하거나 체력이 1이 될 경우, 다른 수감자에게 반복</u></b></mark></color>\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955103].desc
   limit: do 1080 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [UnlockBuff_Base], [IndexPrescript_Base_2nd], [IndexPrescriptTargetToPersonality], [SuperCoin], [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_Base_2nd] = 지령 / Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Turn Start:\n- Gain [IndexPrescript_Base_2nd] based on [UnlockBuff_Base] stage on self\n- Apply [IndexPrescriptTargetToPersonality] against a random Sinner, and prioritize attacking them\n<color=#ff9000><mark=#ff000040><b><u>- When using a Skill against [IndexPrescriptTargetToPersonality], convert all Coins on that Skill to [SuperCoin]s</u></b></mark></color>\n\nWhen attacking, if [IndexPrescriptTargetToPersonality] is killed, or if this unit can no longer attack that target, <color=#ff9000><mark=#ff000040><b><u>use the remaining Skills against a random Sinner\n- Prioritizes targets with the lowest current HP, unless they have 1 HP\n- When the randomly chosen Sinner is killed, or if the said Sinner's HP is brought down to 1, repeat this effect on another Sinner</u></b></mark></color>\n\nDeal +2.5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage against all targets
   PL: na początku tury:\n- zyskuje [IndexPrescript_Base_2nd] zgodnie ze stopniem [UnlockBuff_Base]\n- nakłada [IndexPrescriptTargetToPersonality] na losowego Grzesznika i atakuje go priorytetowo\n<color=#ff9000><mark=#ff000040><b><u>- monety Umiejętności używanej przeciwko [IndexPrescriptTargetToPersonality] w całości zmieniają się w [SuperCoin]y</u></b></mark></color>\n\njeżeli podczas ataku [IndexPrescriptTargetToPersonality] zginie lub jednostka nie może już zaatakować tego celu, <color=#ff9000><mark=#ff000040><b><u>używa pozostałych, niewykorzystanych Umiejętności na losowego Grzesznika\n- priorytet: cele z najniższym aktualnym HP (poza celami z 1 HP)\n- gdy losowo wybrany Grzesznik zginie lub jego HP spadnie do 1, powtarza ten efekt na innym Grzeszniku</u></b></mark></color>\n\nzadaje +2.5% obrażeń przeciwko [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 20%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +30% obrażeń wszystkim celom
426. [[refraction6] Pasywka wroga [955103] — tekst klimatyczny] 제가 가족을 꾸리길 원하십니까. \n\n“당신 같은 남편을 어쩜 이렇게 운명적으로 만날 수 있었을까요.”
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955103].flavor
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you wish me to raise a family?\n\n"It must've been fate that brought us together. To think that I'd ever meet a husband like you..."
   PL: Chce pan, żebym założyła rodzinę?\n\n„To musiał być los, który nas połączył. Pomyśleć, że mogłam spotkać męża takiego jak ty..."
427. [[refraction6] Pasywka wroga [955104] — nazwa] 지령 수행
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955104].name
   limit: do 40 znaków
   EN: Undertake Prescript
   PL: Undertake Prescript
428. [[refraction6] Pasywka wroga [955104] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 10 회복, [BlessingOfIndexPrescriptEnemy] 3 얻음 (턴당 1회)\n\n이번 턴에<color=#ff9000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexRien] 8 얻음</u></b></mark></color>\n- [UnlockBuff_Base]이 없으면, 턴 종료 시 [BlessingOfIndexPrescriptEnemy] 1 얻음\n- [BlessingOfIndexPrescriptEnemy]가 9면, [KarmaOfIndexRien]를 얻지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955104].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptEnemy], [KarmaOfIndexRien], [UnlockBuff_Base]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexRien] = 카르마 / Karmic Consequence; [UnlockBuff_Base] = 해금 / Unlock
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 10 SP and gain 3 [BlessingOfIndexPrescriptEnemy] (once per turn)\n\n<color=#ff9000><mark=#ff000040><b><u>Turn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 8 [KarmaOfIndexRien]</u></b></mark></color>\n- If this unit does not have [UnlockBuff_Base], gain 1 [BlessingOfIndexPrescriptEnemy] at Turn End\n- At 9 [BlessingOfIndexPrescriptEnemy], does not gain [KarmaOfIndexRien]
   PL: na koniec tury, jeżeli w tej turze wykonano [IndexPrescript_Base_2nd], przywraca 10 Poczytalności i zyskuje 3 [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\n<color=#ff9000><mark=#ff000040><b><u>na koniec tury, jeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd], zyskuje 8 [KarmaOfIndexRien]</u></b></mark></color>\n- jeżeli jednostka nie ma [UnlockBuff_Base], na koniec tury zyskuje 1 [BlessingOfIndexPrescriptEnemy]\n- przy 9 [BlessingOfIndexPrescriptEnemy] nie zyskuje [KarmaOfIndexRien]
429. [[refraction6] Pasywka wroga [955104] — tekst klimatyczny] 제가 가족을 잃기를 원하십니까.\n\n“여보. 잠시 북부에 좀 다녀올게.”\n“아, 오후에 택배가 오기로 했으니 대신 받아줄 수 있겠니, 딸?”
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955104].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you wish me to lose my family?\n\n"Honey, I gotta take a quick trip up north today."\n"Ah, also—hey, buddy. I'm expecting a package this afternoon, so would you be a dear and pick it up for me, sweetheart?"
   PL: Chce pan, żebym stracił rodzinę?\n\n„Kochanie, wybieram się dziś na chwilę na północ."\n„A, i jeszcze — hej, ty. Czekam dziś na paczkę, przyniósłbyś ją za mnie, kochanie?"
430. [[refraction6] Pasywka wroga [955105] — nazwa] 해금
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955105].name
   limit: do 40 znaków
   EN: Unlock
   PL: Unlock
431. [[refraction6] Pasywka wroga [955105] — opis] 턴 종료 시 [BlessingOfIndexPrescriptEnemy]가 3/6/9거나 체력이 95%/85%/75% 이하면,\n- [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3] 얻음\n\n등장 이후 첫 번째 턴 종료 시 [UnlockBuff_Base] 단계가 1 미만이면, [UnlockBuff_Rien1] 얻음\n등장 이후 세 번째 턴 종료 시 [UnlockBuff_Base] 단계가 2 미만이면, [UnlockBuff_Rien2] 얻음\n\n체력 또는 턴 조건으로 [UnlockBuff_Base] 시,\n- [BlessingOfIndexPrescriptEnemy]가 3/6/9 미만이면, 3/6/9로 변경,\n증가한 수치 1당 다음 턴 시작 시 [KarmaOfIndexRien] 5 얻음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955105].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [UnlockBuff_Rien1], [UnlockBuff_Rien2], [UnlockBuff_Rien3], [UnlockBuff_Base], [KarmaOfIndexRien]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_Rien1] = 해금 - I / Unlock - I; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [UnlockBuff_Base] = 해금 / Unlock; [KarmaOfIndexRien] = 카르마 / Karmic Consequence
   EN: Turn End: At 3/6/9 [BlessingOfIndexPrescriptEnemy] or at 95%-/85%-/75%- HP,- Gain [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3]\n\nTurn 1 End after entering the field: At lower than [UnlockBuff_Base] stage 1, gain [UnlockBuff_Rien1]\nTurn 3 End after entering the field: At lower than [UnlockBuff_Base] stage 2, gain [UnlockBuff_Rien2]\n\nWhen [UnlockBuff_Base] is activated due to HP or Turn conditionals:\n- At less than 3/6/9 [BlessingOfIndexPrescriptEnemy] Stack, raise them to 3/6/9\nGain 5 [KarmaOfIndexRien] at the next Turn Start for every Stack gained
   PL: na koniec tury, przy 3/6/9 [BlessingOfIndexPrescriptEnemy] lub przy 95%/85%/75% HP lub mniej, zyskuje [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3]\n\nprzy pierwszym końcu tury od pojawienia się w walce, jeżeli stopień [UnlockBuff_Base] jest niższy niż 1, zyskuje [UnlockBuff_Rien1]\nprzy trzecim końcu tury od pojawienia się w walce, jeżeli stopień [UnlockBuff_Base] jest niższy niż 2, zyskuje [UnlockBuff_Rien2]\n\ngdy [UnlockBuff_Base] aktywuje się przez warunek HP lub tur:\n- jeżeli Stosy [BlessingOfIndexPrescriptEnemy] są poniżej 3/6/9, podnosi je do 3/6/9\nzyskuje 5 [KarmaOfIndexRien] na początku następnej tury za każdy zdobyty Stos
432. [[refraction6] Pasywka wroga [955105] — tekst klimatyczny] “지령을 따라가다 보면 닫힌 것들이 풀리기 마련.”
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955105].flavor
   limit: do 120 znaków
   EN: "Following the Prescripts is to unlock what is locked."
   PL: „Podążanie za Nakazami odblokowuje to, co zamknięte.”
433. [[refraction6] Pasywka wroga [955106] — nazwa] 패닉 변경 불가
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955106].name
   limit: do 40 znaków
   EN: Fixed Panic
   PL: Zablokowana Panika
434. [[refraction6] Pasywka wroga [955106] — opis] [PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 15로 변경됨
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955106].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [PanicChangeLock]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Apply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 15
   PL: nakłada efekt [PanicChangeLock]\nna koniec tury, jeżeli ta jednostka jest w Panice, Poczytalność rośnie do 15
435. [[refraction6] Pasywka wroga [955201] — nazwa] 아비 뤼엔 [모조품]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955201].name
   limit: do 40 znaków
   EN: Rien, the Father [Imitation]
   PL: Rien, the Father [Imitation]
436. [[refraction6] Pasywka wroga [955201] — opis] <color=#ff9000><mark=#ff000040><b><u>일방 공격으로 받는 피해량 -75%</u></b></mark></color>\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -75%\n[UnlockBuff_Base]으로 정신력 회복 시 정신력이 30 미만이면, 정신력을 30까지 회복\n\n체력이 55% 이하가 되어 페이즈 변경 시, 다음 효과 적용\n- 자신의 고유 효과를 제외한 나머지 효과 전부 소멸\n- [StackRienSpecialSkill] 0으로 초기화\n- [IndexPrescript_RienSecondPhase] 얻음\n- [BurningWoundRien_Mask]이 [BurningWoundRien]로 변경\n- [KarmaOfIndexRien]가 [KarmaOfIndexRien_2Phase]로 변경되고 10 얻음\n- [Shin_Rien]이 없으면 즉시 얻음\n\n체력이 25% 이하면 패턴이 변경되어 특정 스킬이 더욱 강력해짐
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955201].desc
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [UnlockBuff_Base], [StackRienSpecialSkill], [IndexPrescript_RienSecondPhase], [BurningWoundRien_Mask], [BurningWoundRien], [KarmaOfIndexRien], [KarmaOfIndexRien_2Phase], [Shin_Rien]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [UnlockBuff_Base] = 해금 / Unlock; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]; [IndexPrescript_RienSecondPhase] = 지령[단말기] - 경고 / Prescript: [Device] - Warning …
   EN: <color=#ff9000><mark=#ff000040><b><u>Take -75% damage from Unopposed Attacks</u></b></mark></color>\nTake -75% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\nWhen healing SP from [UnlockBuff_Base], if this unit's SP is below 30, heal up to 30 SP\n\nWhen this unit enters a new phase at 55% HP, gain the following effects:\n- Remove all effects other than those exclusive to this unit\n- Reset [StackRienSpecialSkill] Stack to 0\n- Gain [IndexPrescript_RienSecondPhase]\n- Convert [BurningWoundRien_Mask] to [BurningWoundRien]\n- Convert [KarmaOfIndexRien] to [KarmaOfIndexRien_2Phase]; then gain 10 Stacks of that effect\n- If this unit does not have [Shin_Rien], immediately gain that effect\n\nAt 25% or lower HP, gain a new pattern and greatly enhance a certain Skill
   PL: <color=#ff9000><mark=#ff000040><b><u>otrzymuje -75% obrażeń z ataków bez kontr</u></b></mark></color>\notrzymuje -75% obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\ngdy odzyskuje Poczytalność z [UnlockBuff_Base], jeżeli Poczytalność tej jednostki jest poniżej 30, przywraca ją do 30\n\ngdy ta jednostka wchodzi w nową fazę przy 55% HP, zyskuje następujące efekty:\n- usuwa wszystkie efekty inne niż własne tej jednostki\n- resetuje Stos [StackRienSpecialSkill] do 0\n- zyskuje [IndexPrescript_RienSecondPhase]\n- zamienia [BurningWoundRien_Mask] w [BurningWoundRien]\n- zamienia [KarmaOfIndexRien] w [KarmaOfIndexRien_2Phase], po czym zyskuje 10 Stosów tego efektu\n- jeżeli ta jednostka nie ma [Shin_Rien], natychmiast go zyskuje\n\nprzy 25% HP lub mniej zyskuje nowy wzorzec i znacznie wzmacnia pewną Umiejętność
437. [[refraction6] Pasywka wroga [955201] — tekst klimatyczny] 누군가를 따라해야 하는 것만 같았고 그게 누군지 몰라 지령을 의심하고 거스를 뻔했지만, 뒤늦게 자신이 누구를 닮게 되었는지 깨닫고, 지령의 뜻을 받아들여 완성된 거짓 아비.
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955201].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Once, he harbored a suspicion that he was being shaped into an imitation of someone; he doubted the Will and nearly defied it, for he did not know whom he was to mimic. Only when it was too late did he understand its intent and come to accept the Prescript's will.\nOnly then was the false father completed.
   PL: Kiedyś podejrzewał, że ma stać się czyimś naśladownictwem; ponieważ nie wiedział, kogo ma odwzorować, zwątpił w Preskrypcję i niemal jej się sprzeciwił. Dopiero gdy było już za późno, zrozumiał jej zamiar i przyjął wolę Preskrypcji.\nDopiero wtedy został ukończony fałszywy ojciec.
438. [[refraction6] Pasywka wroga [955202] — nazwa] 신탁 단말기 [카두세우스] - 완전 해금
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955202].name
   limit: do 60 znaków
   EN: Oracle Device [Caduceus] - Full Unlock
   PL: Oracle Device [Caduceus] - Full Unlock
439. [[refraction6] Pasywka wroga [955202] — opis] <color=#ff9000><mark=#ff000040><b><u>코인마다 무기가 무작위로 정해지며 특수 효과 적용</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\n공격 스킬 사용 시, [StackRienSpecialSkill] 1 얻음 (최대 9)\n- 스킬별 1회 획득 가능 (동일한 스킬로 2를 초과하여 얻을 수 없음)\n- 특수 패턴에서만 사용하는 스킬로는 얻지 않음\n\n턴 시작 시 [StackRienSpecialSkill]가 9면, 강력한 스킬을 사용\n- 스킬 종류별 [StackRienSpecialSkill] 획득 여부 초기화\n- 속도 최솟값, 최댓값 +15\n- 턴 종료 시 다음 턴에, [Vulnerable] 2, [ResultReduction] 3 얻음\n\n페이즈가 변경된 턴부터 효과 발동\n- 세 턴마다 [StackRienSpecialSkill]가 9 미만이면,\n9까지 증가하고 (증가한 수치 x 5)만큼 [KarmaOfIndexRien_2Phase] 얻음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955202].desc
   limit: do 1240 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RienWeapon01Hatchet2phase], [RienWeapon02Stiletto2phase], [RienWeapon03Greatsword2phase], [RienWeapon04Rapier2phase], [RienWeapon05Sledgehammer2phase], [RienWeapon06Ultragreatsword2phase], [RienWeapon07Lance2phase], [RienWeapon08Chain2phase], [RienWeapon09Scythe2phase], [StackRienSpecialSkill], [Vulnerable], [ResultReduction], [KarmaOfIndexRien_2Phase]
   znaczenie tagów: [RienWeapon01Hatchet2phase] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [RienWeapon02Stiletto2phase] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [RienWeapon03Greatsword2phase] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [RienWeapon04Rapier2phase] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [RienWeapon05Sledgehammer2phase] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [RienWeapon06Ultragreatsword2phase] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a great sword...; [RienWeapon07Lance2phase] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [RienWeapon08Chain2phase] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: <color=#ff9000><mark=#ff000040><b><u>A random weapon is assigned to every Coin. Each weapon has a unique effect.</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\nWhen using an Attack Skill, gain 1 [StackRienSpecialSkill] (max 9)\n- Can be gained once per Skill; does not gain Stack from the same Skill twice\n- Does not gain Stack from a Skill used only in a special pattern\n\nTurn Start: At 9 [StackRienSpecialSkill] Stacks, use a powerful Skill\n- Reset the per-Skill [StackRienSpecialSkill] cap\n- Min & Max Speed +15\n- Turn End: Gain 2 [Vulnerable] and 3 [ResultReduction] next turn\n\nActivate the following, starting from the turn in which the phase changed\n- Every 3 turns, at less than 9 [StackRienSpecialSkill], bring its Stack to 9; then, gain (Stack gained x 5) [KarmaOfIndexRien_2Phase]
   PL: <color=#ff9000><mark=#ff000040><b><u>każdej monecie przypisywana jest losowa broń; każda broń ma unikatowy efekt.</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\nprzy użyciu Umiejętności ataku zyskuje 1 [StackRienSpecialSkill] (maks. 9)\n- można zdobyć 1 raz na Umiejętność; ta sama Umiejętność nie daje Stosu drugi raz\n- nie zyskuje Stosu z Umiejętności używanych tylko w specjalnym wzorcu\n\nna początku tury przy 9 [StackRienSpecialSkill], używa potężnej Umiejętności\n- resetuje licznik zdobywania [StackRienSpecialSkill] per Umiejętność\n- Szybkość minimalna i maksymalna +15\n- na koniec tury zyskuje w następnej turze 2 [Vulnerable] i 3 [ResultReduction]\n\nefekt aktywuje się od tury, w której nastąpiła zmiana fazy\n- co 3 tury, jeżeli [StackRienSpecialSkill] jest poniżej 9,\npodnosi Stos do 9, po czym zyskuje (liczba zdobytych Stosów x 5) [KarmaOfIndexRien_2Phase]
440. [[refraction6] Pasywka wroga [955202] — tekst klimatyczny] 전파를 통해 지령을 보내는 도시의 신, 헤르메스가 선사한 최고의 무기이자 저주.
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955202].flavor
   limit: do 160 znaków
   EN: An unparalleled weapon and a curse bestowed by Hermes, a god of the City whose Prescripts are distributed by radio waves.
   PL: Najlepsza broń i przekleństwo podarowane przez Hermesa, boga Miasta, którego Prescripty rozsyłane są falami radiowymi.
441. [[refraction6] Pasywka wroga [955203] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955203].name
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [[refraction6] Pasywka wroga [955203] — opis] 턴 시작 시,\n- 무작위 수감자에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함\n<color=#ff9000><mark=#ff000040><b><u>- [IndexPrescriptTargetToPersonality]에게 사용하는 스킬의 코인이 전부 [SuperCoin]으로 변경됨</u></b></mark></color>\n- [BlessingOfIndexPrescriptEnemy]만큼 [Protection] 얻음 (최대 9)\n<color=#ff9000><mark=#ff000040><b><u>- [KarmaOfIndexRien_2Phase] 20당, 1 감소</u></b></mark></color>\n\n공격 시 [IndexPrescriptTargetToPersonality]이 사망하거나 대상을 공격하지 못하게 될 경우, <color=#ff9000><mark=#ff000040><b><u>사용하지 않은 나머지 스킬을 다른 무작위 수감자 한 명에게 사용\n- 현재 체력이 가장 낮은 대상 우선 (체력 1인 경우 제외)\n- 무작위로 선택된 수감자가 사망하거나 체력이 1이 될 경우, 다른 수감자에게 반복</u></b></mark></color>\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +5% (최대 40%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +50%\n\n페이즈가 변경되고 두 번째 턴부터 효과 발동\n- 턴 시작 시 [BlackNightmare] 얻음.\n· 직전 턴에 강력한 스킬을 사용하였으면, 해당 턴에는 [BlackNightmare] 사라짐
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955203].desc
   limit: do 1420 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescriptTargetToPersonality], [SuperCoin], [BlessingOfIndexPrescriptEnemy], [Protection], [KarmaOfIndexRien_2Phase], [BlackNightmare]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [Protection] = 보호 / Protection; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts
   EN: Turn Start:\n- Apply [IndexPrescriptTargetToPersonality] against a random Sinner, and prioritize attacking them\n<color=#ff9000><mark=#ff000040><b><u>- When using a Skill against [IndexPrescriptTargetToPersonality], convert all Coins on that Skill to [SuperCoin]s</u></b></mark></color>\n- Gain [Protection] equal to [BlessingOfIndexPrescriptEnemy] (max 9)\n<color=#ff9000><mark=#ff000040><b><u>\n- Lose 1 Stack for every 20 [KarmaOfIndexRien_2Phase]</u></b></mark></color>\n\nWhen attacking, if [IndexPrescriptTargetToPersonality] is killed, or if this unit can no longer attack that target, <color=#ff9000><mark=#ff000040><b><u>use the remaining Skills against a random other Sinner\n- Prioritizes targets with the lowest current HP, unless they have 1 HP\n- When the randomly chosen Sinner is killed, or if the said Sinner's HP is brought down to 1, repeat this effect on another Sinner</u></b></mark></color>\n\nDeal +5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 40%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +50% damage against all targets\n\nStarting from the first turn after the phase change, activate the following effects:\n- Turn Start: Gain [BlackNightmare]\n· If this unit used a powerful attack in the previous turn, lose [BlackNightmare] for that turn
   PL: na początku tury:\n- nakłada [IndexPrescriptTargetToPersonality] na losowego Grzesznika i atakuje go priorytetowo\n<color=#ff9000><mark=#ff000040><b><u>- monety Umiejętności używanej przeciwko [IndexPrescriptTargetToPersonality] w całości zmieniają się w [SuperCoin]y</u></b></mark></color>\n- zyskuje [Protection] równy wartości [BlessingOfIndexPrescriptEnemy] (maks. 9)\n<color=#ff9000><mark=#ff000040><b><u>- traci 1 Stos za każde 20 [KarmaOfIndexRien_2Phase]</u></b></mark></color>\n\njeżeli podczas ataku [IndexPrescriptTargetToPersonality] zginie lub jednostka nie może już zaatakować tego celu, <color=#ff9000><mark=#ff000040><b><u>używa pozostałych, niewykorzystanych Umiejętności na innego losowego Grzesznika\n- priorytet: cele z najniższym aktualnym HP (poza celami z 1 HP)\n- gdy losowo wybrany Grzesznik zginie lub jego HP spadnie do 1, powtarza ten efekt na innym Grzeszniku</u></b></mark></color>\n\nzadaje +5% obrażeń przeciwko [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 40%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +50% obrażeń wszystkim celom\n\nefekty aktywują się od pierwszej tury po zmianie fazy:\n- na początku tury zyskuje [BlackNightmare]\n· jeżeli w poprzedniej turze użyto potężnego ataku, w tej turze [BlackNightmare] znika
443. [[refraction6] Pasywka wroga [955203] — tekst klimatyczny] 가족을 꾸렸습니다.\n\n“당신은 지금 이곳에 있으면 안될 텐데.”\n“아직 작업이 한창이다. 무엇보다 섬세하고 아름답게 장식하고 있거든.”\n“…네놈, 설마 지령을 거스를 셈인가.”
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955203].flavor
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I raised a family.\n\n"You're not supposed to be here right now."\n"My work is still much underway, and I'd like to carve them up in peace so they can attain the most exquisite beauty I can sculpt."\n"... Don't tell me, are you here to defy the Prescript?"
   PL: Założyłem rodzinę.\n\n„Nie powinieneś tu być."\n„Moje dzieło wciąż się toczy; chcę złożyć je w spokoju, by mogło osiągnąć najdoskonalsze piękno, jakie zdołam wyrzeźbić."\n„...Nie mów mi, że przyszedłeś przeciwko Preskrypcji."
444. [[refraction6] Pasywka wroga [955204] — nazwa] 지령 수행
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955204].name
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [[refraction6] Pasywka wroga [955204] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 15 회복, [BlessingOfIndexPrescriptEnemy] 1 얻음 (턴당 1회)\n\n이번 턴에 <color=#ff9000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexRien_2Phase] 8 얻고 [BlessingOfIndexPrescriptEnemy] 1 잃음</u></b></mark></color>\n- 강력한 스킬을 사용한 턴일 경우, 대신 [KarmaOfIndexRien_2Phase] 12 얻고 [BlessingOfIndexPrescriptEnemy] 2 잃음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955204].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptEnemy], [KarmaOfIndexRien_2Phase]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 15 SP and gain 1 [BlessingOfIndexPrescriptEnemy] (once per turn)\n\n<color=#ff9000><mark=#ff000040><b><u>Turn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 8 [KarmaOfIndexRien_2Phase] and lose 1 [BlessingOfIndexPrescriptEnemy]</u></b></mark></color>\n- If this unit used a powerful Skill this turn, gain 12 [KarmaOfIndexRien_2Phase] and lose 2 [BlessingOfIndexPrescriptEnemy] instead
   PL: na koniec tury, jeżeli w tej turze wykonano [IndexPrescript_Base_2nd], przywraca 15 Poczytalności i zyskuje 1 [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\n<color=#ff9000><mark=#ff000040><b><u>na koniec tury, jeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd], zyskuje 8 [KarmaOfIndexRien_2Phase] i traci 1 [BlessingOfIndexPrescriptEnemy]</u></b></mark></color>\n- jeżeli w tej turze użyto potężnej Umiejętności, zamiast tego zyskuje 12 [KarmaOfIndexRien_2Phase] i traci 2 [BlessingOfIndexPrescriptEnemy]
446. [[refraction6] Pasywka wroga [955204] — tekst klimatyczny] 가족을… 잃었습니다.\n \n“가지마…”\n“이대로 가지마… 아빠…  우리… 살려줘…”
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955204].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I... lost my family.\n\n"Don't go..."\n"Don't go... Not... like this... Daddy... Please... help us..."
   PL: Rodzina... została... stracona.\n\n„Nie odchodź..."\n„Nie odchodź... Tylko nie... tak... Tato... Prosimy... ratuj nas..."
447. [[refraction6] Pasywka wroga [955205] — nazwa] 패닉 변경 불가
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955205].name
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [[refraction6] Pasywka wroga [955205] — opis] [PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 30으로 변경됨
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955205].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [PanicChangeLock]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Apply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 30
   PL: nakłada efekt [PanicChangeLock]\nna koniec tury, jeżeli ta jednostka jest w Panice, Poczytalność rośnie do 30
449. [[refraction6] Pasywka wroga [955312] — nazwa] 패닉 변경 불가
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955312].name
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [[refraction6] Pasywka wroga [955312] — opis] [PanicChangeLock] 효과가 적용되며, 턴 종료 시 패닉 상태면 정신력이 45로 변경됨
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955312].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [PanicChangeLock]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Apply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, raise SP to 45
   PL: nakłada efekt [PanicChangeLock]\nna koniec tury, jeżeli ta jednostka jest w Panice, Poczytalność rośnie do 45
451. [[refraction6] Pasywka wroga [955601] — nazwa] 술래잡기 시작이야
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955601].name
   limit: do 40 znaków
   EN: Let's Play Tag! Here I Go!
   PL: Let's Play Tag! Here I Go!
452. [[refraction6] Pasywka wroga [955601] — opis] 턴 시작 시 [TagGameBuff]가 없으면, 자신을 제외한 레벨이 가장 낮은 아군 1/2/3명이 3턴 동안 [TagGameBuff]가 됨 (이 효과 발동 횟수에 따라 인원 수가 증가함)\n\n<color=#ff9000><mark=#ff000040><b><u>[TagGameBuff]가 살아있는 상태에서 [TagGameBuff]가 끝났으면</u></b></mark></color>, 아래 효과 발동\n- 모든 수감자가 각자 최대 체력의 40%만큼 고정 체력 피해를 입음\n- 침식/패닉이 가능한 무작위 수감자 1명의 정신력이 -45로 강제 변경됨\n\n[TagGameBuff]가 수감자에 의해 사망했으면, 처치한 수감자는 이번 전투 동안 [ResultEnhancement] 1 얻음 (이 효과는 누적됨)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955601].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TagGameBuff], [ResultEnhancement], [TabExplain]
   znaczenie tagów: [TagGameBuff] = 술래 / "It"; [ResultEnhancement] = 위력 증가 / Power Up
   EN: Turn Start: If there are no [TagGameBuff]s, this unit's 1/2/3 other allies that have the lowest Level become [TagGameBuff] for 3 turns (number of units receiving this effect increases every time this effect activates)\n\n<color=#ff9000><mark=#ff000040><b><u>If [TagGameBuff] effect expires while the unit that had the [TagGameBuff] effect is alive</u></b></mark></color>, gain the following effects:\n- All Sinners take fixed damage equal to 40% HP each\n- Reduce SP to -45 for a random Sinner who can enter E.G.O Corrosion[TabExplain] or Panic\n\nIf a Sinner kills a [TagGameBuff], the said Sinner gains 1 [ResultEnhancement] for the rest of this Encounter (this effect can be gained cumulatively)
   PL: na początku tury, jeżeli nie ma żadnego [TagGameBuff], 1/2/3 sojuszników tej jednostki (poza nią samą) o najniższym poziomie staje się [TagGameBuff] na 3 tury (liczba objętych jednostek rośnie z każdą aktywacją tego efektu)\n\njeżeli <color=#ff9000><mark=#ff000040><b><u>efekt [TagGameBuff] wygaśnie, a jednostka z tym efektem żyje</u></b></mark></color>, aktywują się następujące efekty:\n- wszyscy Grzesznicy otrzymują stałe obrażenia równe 40% własnego HP\n- Poczytalność losowego Grzesznika zdolnego do Erozji E.G.O[TabExplain] lub Paniki zostaje wymuszona na -45\n\njeżeli Grzesznik zabije [TagGameBuff], ten Grzesznik zyskuje 1 [ResultEnhancement] na resztę tej walki (efekt kumuluje się)
453. [[refraction6] Pasywka wroga [955602] — nazwa] 놀아줄래? 놀아줄래? 놀아줄래?
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955602].name
   limit: do 60 znaków
   EN: Will You Play? Will You Play? Will You Play?
   PL: Will You Play? Will You Play? Will You Play?
454. [[refraction6] Pasywka wroga [955602] — opis] 턴 종료 시 살아있는 아군이 자신만 있거나 본체 체력이 50%이하면, 다음 턴에 ‘영원히 같이 놀자~!’를 사용함 (전투당 1회)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955602].desc
   limit: do 190 znaków
   EN: Turn End: If this unit is the only surviving ally, or if the Core is at 50%- HP, use "Let's Play Together Forever~!" next turn (once per Encounter)
   PL: na koniec tury, jeżeli ta jednostka jest jedynym żyjącym sojusznikiem albo HP Core wynosi 50% lub mniej, używa w następnej turze „Let's Play Together Forever~!" (1 raz na walkę)
455. [[refraction6] Pasywka wroga [955603] — nazwa] 끝나버린 놀이
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955603].name
   limit: do 40 znaków
   EN: No More Playtime
   PL: No More Playtime
456. [[refraction6] Pasywka wroga [955603] — opis] 턴 시작 시 인형 부위가 <color=#ff9000><mark=#ff000040><b><u>자신을 제외한 아군 수만큼 [Protection]를 얻음</u></b></mark></color>\n\n인형 부위가 파괴되면 놀아줄래와 남은 아군이 사망함
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955603].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Turn Start: The "Stuffed Toy" Part <color=#ff9000><mark=#ff000040><b><u>gains [Protection] equal to the number of allies excluding this unit</u></b></mark></color>\n\nWhen the "Stuffed Toy" Part is destroyed, Will You Play? and its remaining allies are killed
   PL: na początku tury część „Stuffed Toy" <color=#ff9000><mark=#ff000040><b><u>zyskuje [Protection] równą liczbie sojuszników poza tą jednostką</u></b></mark></color>\n\ngdy część „Stuffed Toy" zostanie zniszczona, Will You Play? i pozostali sojusznicy giną
457. [[refraction6] Pasywka wroga [955604] — nazwa] 애착 인형
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955604].name
   limit: do 40 znaków
   EN: Attachment Plushie
   PL: Attachment Plushie
458. [[refraction6] Pasywka wroga [955604] — opis] <color=#ff9000><mark=#ff000040><b><u>몸통 부위가 받는 체력 피해는 0으로 고정됨</u></b></mark></color>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955604].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>
   EN: <color=#ff9000><mark=#ff000040><b><u>HP damage taken by the Core is fixed at 0</u></b></mark></color>
   PL: <color=#ff9000><mark=#ff000040><b><u>obrażenia HP otrzymywane przez Core są stałe i wynoszą 0</u></b></mark></color>
459. [[refraction6] Pasywka wroga [955401] — nazwa] 제 모든 신체 요소는 이미 티비아에
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955401].name
   limit: do 60 znaków
   EN: All of My Corpus has been Given to Tibia
   PL: All of My Corpus has been Given to Tibia
460. [[refraction6] Pasywka wroga [955401] — opis] [Combustion], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력 피해량 -30%\n[Laceration]로 받는 피해량 -50%\n\n턴 시작 시, 흐트러짐 상태면 흐트러짐 해제. 이후 [CrimsonTakeDamageUp] 2 얻고 다음 턴까지 ‘설치 미술 제 3호 ‘간이늑골’’ 사용 불가능 (전투당 1회)\n\n턴 종료 시 자신의 [Combustion] 4당, 다음 턴에 [DefenseDown] 1 얻음 (최대 15)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955401].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [Burst], [Sinking], [Laceration], [CrimsonTakeDamageUp], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Take -30% HP, SP damage from [Combustion], [Vibration], [Burst], and [Sinking]\nTake -50% damage from [Laceration]\n\nTurn Start: If this unit is Staggered, recover from Stagger. Afterward, gain 2 [CrimsonTakeDamageUp] and becomes unable to use "Installation Art no. 3: Improvised Ribcage" until next turn (once per Encounter)\n\nTurn End: Gain 1 [DefenseDown] next turn for every 4 [Combustion] on self (max 15)
   PL: otrzymuje -30% obrażeń HP i Poczytalności od [Combustion], [Vibration], [Burst] i [Sinking]\notrzymuje -50% obrażeń od [Laceration]\n\nna początku tury, jeżeli jest Oszołamiona, dochodzi do siebie z Oszołamienia. następnie zyskuje 2 [CrimsonTakeDamageUp] i do następnej tury nie może użyć „Installation Art no. 3: Improvised Ribcage" (1 raz na walkę)\n\nna koniec tury za każde 4 [Combustion] na sobie zyskuje 1 [DefenseDown] w następnej turze (maks. 15)
461. [[refraction6] Pasywka wroga [955301] — nazwa] 관찰
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955301].name
   limit: do 40 znaków
   EN: Observation
   PL: Obserwacja
462. [[refraction6] Pasywka wroga [955301] — opis] 스테이지 시작 시, 모든 적에게 [ObservedPerson] 1을 부여하고\n[ObservedPerson]가 적용된 인원 수만큼 [Breath] 위력을 얻고 [Breath] 횟수 증가\n\n턴 시작 시, [ObservedPerson]를 보유하지 않은 대상에게 [ObservedPerson] 1 부여\n\n대상의 [ObservedPerson] 10당 스킬로 부여하는 [Vibration] 위력, [Vibration] 횟수 부여량 +1 (최대 3)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955301].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [ObservedPerson], [Breath], [Vibration]
   znaczenie tagów: [ObservedPerson] = 피관찰자 / Subject of Observation; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor
   EN: Encounter Start: Apply 1 [ObservedPerson] on all enemies; then, gain [Breath] Potency and Count equal to the number of units with [ObservedPerson]\n\nTurn Start: Apply 1 [ObservedPerson] against targets without [ObservedPerson]\n\nFor every 10 [ObservedPerson] on the target, inflict +1 more [Vibration] Potency and Count with this unit's Skills (max 3)
   PL: na początku walki nakłada 1 [ObservedPerson] na wszystkich wrogów, po czym zyskuje Moc [Breath] i Licznik [Breath] równy liczbie jednostek z [ObservedPerson]\n\nna początku tury nakłada 1 [ObservedPerson] na cele bez [ObservedPerson]\n\nza każde 10 [ObservedPerson] na celu Umiejętności tej jednostki nakładają o 1 więcej Mocy [Vibration] i Licznika [Vibration] (maks. 3)
463. [[refraction6] Pasywka wroga [955302] — nazwa] 적응
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955302].name
   limit: do 40 znaków
   EN: Adaptation
   PL: Adaptacja
464. [[refraction6] Pasywka wroga [955302] — opis] 자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 횟수 1 추가로 얻음\n\n<color=#ff9000><mark=#ff000040><b><u>턴 시작 시, 직전 턴에 자신에게 가장 많은 피해를 입힌 수감자에게 [ResultReduction] 3, [ObservedPerson] 5 부여\n- 대상의 [ObservedPerson]가 30이면, 대신 [ResultReduction] 5 부여</u></b></mark></color>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955302].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [ObservedPerson], [ResultReduction]
   znaczenie tagów: [Breath] = 호흡 / Poise; [ObservedPerson] = 피관찰자 / Subject of Observation; [ResultReduction] = 위력 감소 / Power Down
   EN: Gain 1 [Breath] Potency every time this unit inflicts damage with Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain 1 additional [Breath] Potency with every hit\n\nGain +1 [Breath] Count every time this unit takes damage from a Sinner's Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain +1 additional [Breath] Count with every hit taken\n\n<color=#ff9000><mark=#ff000040><b><u>Turn Start: Inflict 3 [ResultReduction] and 5 [ObservedPerson] to the Sinner who dealt the most damage to this unit in the previous turn\n- If the target has 30 [ObservedPerson], inflict 5 [ResultReduction] instead</u></b></mark></color>
   PL: zyskuje 1 Moc [Breath] za każdym razem gdy zadaje obrażenia efektami Umiejętności ataku (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowo 1 Moc [Breath] przy każdym trafieniu\n\nzyskuje +1 Licznik [Breath] za każdym razem gdy otrzymuje obrażenia efektami Umiejętności ataku Grzesznika (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowo +1 Licznik [Breath] przy każdym otrzymanym trafieniu\n\n<color=#ff9000><mark=#ff000040><b><u>na początku tury nakłada 3 [ResultReduction] i 5 [ObservedPerson] na Grzesznika, który w poprzedniej turze zadał tej jednostce najwięcej obrażeń\n- jeżeli cel ma 30 [ObservedPerson], zamiast tego nakłada 5 [ResultReduction]</u></b></mark></color>
465. [[refraction6] Pasywka wroga [955303] — nazwa] 방어기제
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955303].name
   limit: do 40 znaków
   EN: Defense Mechanism
   PL: Mechanizm Obrony
466. [[refraction6] Pasywka wroga [955303] — opis] 턴 시작 시, <color=#ff9000><mark=#ff000040><b><u>잃은 체력의 30%만큼 보호막을 얻음 (최대 체력의 25%를 초과하여 얻을 수 없음)</u></b></mark></color>\n- [Combustion] 상태일 경우, ([Combustion] 횟수 x 1.5)%만큼 보호막 수치가 대폭 감소\n- 보호막이 [Burst] 효과 피해를 100% 추가로 받음\n\n턴 종료 시 이 효과로 얻은 보호막이 파괴되었다면, 파괴된 횟수에 비례하여 이번 전투 동안 턴 시작 시 [DefenseDown] 1 얻음 (최대 5)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955303].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Burst], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: <color=#ff9000><mark=#ff000040><b><u>Gain Shield equal to 30% of missing HP (Shield HP cannot exceed 25% of the max HP)</u></b></mark></color>\n- If this unit has [Combustion], lose ([Combustion] Count x 1.5)% Shield HP\n- Shield takes +100% damage from [Burst] effects\n\nTurn End: If the Shield gained due to this effect is destroyed, for the rest of this Encounter, gain 1 [DefenseDown] at Turn Start for every instance the Shield has been destroyed (max 5)
   PL: na początku tury <color=#ff9000><mark=#ff000040><b><u>zyskuje Tarczę równą 30% brakującego HP (HP Tarczy nie może przekroczyć 25% Maks. HP)</u></b></mark></color>\n- jeżeli ta jednostka ma [Combustion], traci (Licznik [Combustion] x 1.5)% HP Tarczy\n- Tarcza otrzymuje +100% obrażeń z efektów [Burst]\n\nna koniec tury, jeżeli Tarcza zyskana dzięki temu efektowi została zniszczona, przez resztę tej walki na początku tury zyskuje 1 [DefenseDown] za każde zniszczenie Tarczy (maks. 5)
467. [[refraction6] Pasywka wroga [955304] — nazwa] 확증편향
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955304].name
   limit: do 40 znaków
   EN: Confirmation Bias
   PL: Efekt Potwierdzenia
468. [[refraction6] Pasywka wroga [955304] — opis] 턴 종료 시, <color=#ff9000><mark=#ff000040><b><u>수감자의 정신력을 10만큼 빼앗음</u></b></mark></color> (최대 3명, 정신력이 높은 순으로 적용, 동일한 대상에게 중첩 적용되지 않음\n(호엔하임이 패닉 상태에서는 발동하지 않음)\n\n<color=#ff9000><mark=#ff000040><b><u>자신의 정신력이 15 미만으로 내려가지 않음</u></b></mark></color>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955304].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: Turn End: <color=#ff9000><mark=#ff000040><b><u>Siphon 10 SP from Sinners</u></b></mark></color> (max 3 Sinners in descending order of SP; does not apply cumulatively on the same target)\n(Does not activate if Hohenheim is Panicked)\n\n<color=#ff9000><mark=#ff000040><b><u>This unit's SP does not drop below 15</u></b></mark></color>
   PL: na koniec tury <color=#ff9000><mark=#ff000040><b><u>wyssie 10 Poczytalności Grzesznikom</u></b></mark></color> (maks. 3 Grzeszników w kolejności od najwyższej Poczytalności; nie kumuluje się na tym samym celu)\n(nie aktywuje się gdy Hohenheim jest w Panice)\n\n<color=#ff9000><mark=#ff000040><b><u>Poczytalność tej jednostki nie spada poniżej 15</u></b></mark></color>
469. [[refraction6] Pasywka wroga [955305] — nazwa] 가설 정립
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955305].name
   limit: do 40 znaków
   EN: Establish Hypothesis
   PL: Stawianie Hipotezy
470. [[refraction6] Pasywka wroga [955305] — opis] 세 번째 턴이 되면 패턴이 변경되어 강력한 스킬을 사용할 준비를 시작함.\n이후에는 턴 종료 시 [Breath] 횟수가 30 이상이 되었을 때, 위 효과가 발동\n\n강력한 스킬 준비 단계 동안 체력 피해를 입지 않았으면, 해당 스킬의 파괴력이 크게 증가함 (보호막 피해는 적용되지 않음)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955305].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On Turn 3: Gains a new pattern and prepares to use a powerful Skill.\nAfter Turn 3 is over: The above effect activates when this unit has 30+ [Breath] Count at Turn End\n\nIf this unit did not take any HP damage during the preparation period before using the powerful Skill, greatly enhance the Skill (does not count damages taken by Shield HP)
   PL: w 3. turze zyskuje nowy wzorzec i przygotowuje się do użycia potężnej Umiejętności.\npóźniej, na koniec tury, ten efekt aktywuje się gdy Licznik [Breath] tej jednostki wynosi 30 lub więcej\n\njeżeli w okresie przygotowań przed użyciem potężnej Umiejętności ta jednostka nie otrzymała obrażeń HP, Umiejętność zostaje znacznie wzmocniona (obrażenia przyjęte przez HP Tarczy nie liczą się)
471. [[refraction6] Pasywka wroga [955306] — nazwa] 부적응
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955306].name
   limit: do 40 znaków
   EN: Maladaptation
   PL: Maladaptacja
472. [[refraction6] Pasywka wroga [955306] — opis] 선택지에 의하여 약화된 경우, 「적응」 패시브가 다음 효과로 변경 적용됨\n\n자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 횟수 1 추가로 얻음\n\n크리티컬 피해량이 증가하거나 감소하지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955306].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [ObservedPerson]
   znaczenie tagów: [Breath] = 호흡 / Poise; [ObservedPerson] = 피관찰자 / Subject of Observation
   EN: When weakened due to a Choice Event, this Passive replaces 「Adaptation」\n\nGain 1 [Breath] Potency every time this unit inflicts damage with Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain 1 additional [Breath] Potency with every hit; however, reduce the target's [ObservedPerson] by 3\n\nGain +1 [Breath] Count every time this unit takes damage from a Sinner's Attack Skill effects (15 per turn)\n- If the target has 15+ [ObservedPerson], gain +1 additional [Breath] Count with every hit taken; however, reduce the target's [ObservedPerson] by 3\n\nCritical damage does not increase or decrease
   PL: gdy jednostka zostanie osłabiona przez Wybór, ta pasywka zastępuje 「Adaptacja」 następującymi efektami\n\nzyskuje 1 Moc [Breath] za każdym razem gdy zadaje obrażenia efektami Umiejętności ataku (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowo 1 Moc [Breath] przy każdym trafieniu, ale zmniejsza [ObservedPerson] celu o 3\n\nzyskuje +1 Licznik [Breath] za każdym razem gdy otrzymuje obrażenia efektami Umiejętności ataku Grzesznika (maks. 15 na turę)\n- jeżeli cel ma 15+ [ObservedPerson], zyskuje dodatkowo +1 Licznik [Breath] przy każdym otrzymanym trafieniu, ale zmniejsza [ObservedPerson] celu o 3\n\nobrażenia krytyczne nie zwiększają się i nie zmniejszają
473. [[refraction6] Pasywka wroga [955307] — nazwa] 엉성한 방어기제
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955307].name
   limit: do 40 znaków
   EN: Inadequate Defense Mechanism
   PL: Nieadekwatny Mechanizm Obrony
474. [[refraction6] Pasywka wroga [955307] — opis] 선택지에 의하여 약화된 경우, 「방어기제」 패시브가 다음 효과로 변경 적용됨\n\n턴 시작 시, 잃은 체력의 15%만큼 보호막을 얻음 (최대 체력의 5%를 초과하여 얻을 수 없음)\n- [Combustion] 상태일 경우, ([Combustion] 횟수 x 2)%만큼 보호막 수치가 대폭 감소\n- 보호막이 [Burst] 효과 피해를 150% 추가로 받음\n\n턴 종료 시 이 효과로 얻은 보호막이 파괴되었다면, 파괴된 횟수에 비례하여 이번 전투 동안 턴 시작 시 [DefenseDown] 2 얻음 (최대 10)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955307].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Burst], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When weakened due to a Choice Event, this Passive replaces 「Defense Mechanism」\n\nTurn Start: Gain Shield equal to 15% of missing HP (Shield HP cannot exceed 5% of the max HP)\n- If this unit has [Combustion], lose ([Combustion] Count x 2)% Shield HP\n- Shield takes +150% damage from [Burst] effects\n\nTurn End: If the Shield gained due to this effect is destroyed, for the rest of this Encounter, gain 2 [DefenseDown] at Turn Start for every instance the Shield has been destroyed (max 10)
   PL: gdy jednostka zostanie osłabiona przez Wybór, ta pasywka zastępuje 「Mechanizm Obrony」 następującymi efektami\n\nna początku tury zyskuje Tarczę równą 15% brakującego HP (HP Tarczy nie może przekroczyć 5% Maks. HP)\n- jeżeli ta jednostka ma [Combustion], traci (Licznik [Combustion] x 2)% HP Tarczy\n- Tarcza otrzymuje +150% obrażeń z efektów [Burst]\n\nna koniec tury, jeżeli Tarcza zyskana dzięki temu efektowi została zniszczona, przez resztę tej walki na początku tury zyskuje 2 [DefenseDown] za każde zniszczenie Tarczy (maks. 10)
475. [[refraction6] Pasywka wroga [955308] — nazwa] 자기 의심
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955308].name
   limit: do 40 znaków
   EN: Self-doubt
   PL: Samowątpienie
476. [[refraction6] Pasywka wroga [955308] — opis] 선택지에 의하여 약화된 경우, 「확증편향」 패시브가 다음 효과로 변경 적용됨\n\n턴 시작 시, <color=#ff9000><mark=#ff000040><b><u>[Vulnerable] 3 얻고</u></b></mark></color> 자신의 정신력이 15만큼 감소\n턴 종료 시, 자신보다 정신력이 높은 대상의 정신력을 5만큼 빼앗음 (최대 3명, 정신력이 높은 순으로 적용, 동일한 대상에게 중첩 적용되지 않음)\n(호엔하임이 패닉 상태에서는 발동하지 않음)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955308].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff9000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: When weakened due to a Choice Event, this Passive replaces 「Confirmation Bias」\n\nTurn Start: <color=#ff9000><mark=#ff000040><b><u>Gain 3 [Vulnerable]</u></b></mark></color> and lose 15 SP\nTurn End: Siphon 5 SP from targets with higher SP than this unit (max 3 targets; in descending order of SP; cannot stack on the same target)\n(Does not activate if Hohenheim is Panicked)
   PL: gdy jednostka jest osłabiona przez Wybór, ta pasywka zastępuje 「Efekt Potwierdzenia」 następującymi efektami\n\nna początku tury <color=#ff9000><mark=#ff000040><b><u>zyskuje 3 [Vulnerable]</u></b></mark></color> i traci 15 Poczytalności\nna koniec tury wyssie 5 Poczytalności celom z wyższą Poczytalnością niż ta jednostka (maks. 3 cele; w kolejności od najwyższej Poczytalności; nie kumuluje się na tym samym celu)\n(nie aktywuje się gdy Hohenheim jest w Panice)
477. [[refraction6] Pasywka wroga [955309] — nazwa] 적응
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955309].name
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [[refraction6] Pasywka wroga [955309] — opis] 자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, [Breath] 횟수 1 추가로 얻음\n\n<color=#ff9000><mark=#ff000040><b><u>턴 시작 시, 직전 턴에 자신에게 가장 많은 피해를 입힌 수감자에게 [ResultReduction] 3, [ObservedPerson] 5 부여\n- 대상의 [ObservedPerson]가 30이면, 대신 [ResultReduction] 5 부여</u></b></mark></color>
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955309].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [[refraction6] Pasywka wroga [955310] — nazwa] 방어기제
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955310].name
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [[refraction6] Pasywka wroga [955310] — opis] 턴 시작 시, <color=#ff9000><mark=#ff000040><b><u>잃은 체력의 30%만큼 보호막을 얻음 (최대 체력의 25%를 초과하여 얻을 수 없음)</u></b></mark></color>\n- [Combustion] 상태일 경우, ([Combustion] 횟수 x 1.5)%만큼 보호막 수치가 대폭 감소\n- 보호막이 [Burst] 효과 피해를 100% 추가로 받음\n\n턴 종료 시 이 효과로 얻은 보호막이 파괴되었다면, 파괴된 횟수에 비례하여 이번 전투 동안 턴 시작 시 [DefenseDown] 1 얻음 (최대 5)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955310].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [[refraction6] Pasywka wroga [955311] — nazwa] 부적응
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955311].name
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [[refraction6] Pasywka wroga [955311] — opis] 선택지에 의하여 약화된 경우, 「적응」 패시브가 다음 효과로 변경 적용됨\n\n자신의 공격 스킬 효과로 피해를 입힐 때마다 [Breath] 위력 1 얻음 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 위력 1 추가로 얻음\n\n수감자의 공격 스킬 효과로 피해를 받을 때마다 [Breath] 횟수 1 증가 (턴 당 최대 15)\n- 대상의 [ObservedPerson]가 15 이상이면, 대상의 [ObservedPerson] 3을 감소시키는 대신 [Breath] 횟수 1 추가로 얻음\n\n크리티컬 피해량이 증가하거나 감소하지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955311].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [[refraction6] Pasywka wroga [955002] — nazwa] 중첩된 잔상
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955002].name
   limit: do 40 znaków
   EN: Superposed Afterimage
   PL: Superposed Afterimage
484. [[refraction6] Pasywka wroga [955002] — opis] 이 캐릭터가 전투에 등장하면, [TimeEntangleFour] 얻음\n[TimeGapAb]가 없으면, [TimeGapAb]를 ([TimeEntangleDesc] 단계 x  400)만큼 얻음. ([TimeEntangleDesc] 단계 당 1회)\n\n[TimeEntangleDesc] 3, 4단계에서 <color=#ff6000><mark=#ff000040><b><u>[TimeGapAb]를 모두 잃으면 패턴이 변경되고, 다음 턴 동안 흐트러짐</u></b></mark></color>\n\n[TimeEntangleDesc] 2단계에서 <color=#ff6000><mark=#ff000040><b><u>[TimeGapAb]를 모두 잃으면 패턴이 변경됨</u></b></mark></color>\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955002].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TimeEntangleFour], [TimeGapAb], [TimeEntangleDesc], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [TimeEntangleFour] = 4중 잔상 얽힘 / Fourfold Afterimage Entanglement; [TimeGapAb] = 괴리 / Disjunction; [TimeEntangleDesc] = 잔상 얽힘 / Afterimage Entanglement; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Upon entering the Encounter, this unit gains [TimeEntangleFour]\nIf this unit does not have [TimeGapAb], this unit gains [TimeGapAb] equal to ([TimeEntangleDesc] stage x 400) (once per [TimeEntangleDesc] stage)\n\nAt stage 3 and 4 [TimeEntangleDesc], <color=#ff6000><mark=#ff000040><b><u>if this unit loses all [TimeGapAb], the pattern changes and become Staggered for the next turn</u></b></mark></color>\n\nAt stage 2 [TimeEntangleDesc], <color=#ff6000><mark=#ff000040><b><u>if this unit loses all [TimeGapAb], the pattern changes</u></b></mark></color>\n\nTake -30% HP, SP damage from [Combustion], [Laceration], [Burst], and [Sinking]; -30% to Stagger Threshold raised by [Vibration]
   PL: po pojawieniu się w walce ta jednostka zyskuje [TimeEntangleFour]\njeżeli ta jednostka nie ma [TimeGapAb], zyskuje [TimeGapAb] równe (stopień [TimeEntangleDesc] x 400) (1 raz na stopień [TimeEntangleDesc])\n\nna stopniu 3 i 4 [TimeEntangleDesc], <color=#ff6000><mark=#ff000040><b><u>jeżeli ta jednostka straci całą wartość [TimeGapAb], wzorzec się zmienia, a w następnej turze przechodzi w Oszołamienie</u></b></mark></color>\n\nna stopniu 2 [TimeEntangleDesc], <color=#ff6000><mark=#ff000040><b><u>jeżeli ta jednostka straci całą wartość [TimeGapAb], wzorzec się zmienia</u></b></mark></color>\n\notrzymuje -30% obrażeń HP i Poczytalności od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]; [Vibration] podnosi Próg Oszołomienia o 30% mniej
485. [[refraction6] Pasywka wroga [957201] — nazwa] 과거 - 분절 [分節]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957201].name
   limit: do 40 znaków
   EN: The Past - Segmentation [分節]
   PL: The Past - Segmentation [分節]
486. [[refraction6] Pasywka wroga [957201] — opis] 나생접::나비가 보유한 [StackPastActivate] 수치가 표시됨\n\n<color=#ff6000><mark=#ff000040><b><u>메인 타겟으로 피격</u></b></mark></color>받을 때마다\n- 나생접::나비의 [StackPastActivate] -1 (코인당 1회)\n- 자신을 타겟한 수감자의 정신력 10 회복 (수감자별 턴당 1회)\n\n이번 턴에 <color=#ff6000><mark=#ff000040><b><u>메인 타겟으로 피격받지 않았으면,</u></b></mark></color>\n전투 종료 시 나생접::나비의 [StackPastActivate] +5\n- 나생접::나비가 흐트러졌으면, 이 효과가 발동하지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957201].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StackPastActivate], [TabExplain]
   znaczenie tagów: [StackPastActivate] = 과거 상태 / In the Past
   EN: Displays current [StackPastActivate] Stack on Butterfly[TabExplain] of Entangled Lives::Imago\n\nEvery time this unit is <color=#ff6000><mark=#ff000040><b><u>hit as the main target</u></b></mark></color>:\n- Butterfly[TabExplain] of Entangled Lives::Imago loses 1 [StackPastActivate] Stack (once per Coin)\n- The Sinner who attacked this unit heals 10 SP (once per turn per Sinner)\n\nIf this unit <color=#ff6000><mark=#ff000040><b><u>did not get hit as the main target this turn</u></b></mark></color>, Butterfly[TabExplain] of Entangled Lives::Imago gains 5 [StackPastActivate] Stack at Combat End\n- If Butterfly[TabExplain] of Entangled Lives::Imago is Staggered, this effect does not activate
   PL: wyświetla aktualny Stos [StackPastActivate] jednostki Butterfly[TabExplain] of Entangled Lives::Imago\n\nza każdym razem gdy ta jednostka zostanie <color=#ff6000><mark=#ff000040><b><u>trafiona jako główny cel</u></b></mark></color>:\n- Butterfly[TabExplain] of Entangled Lives::Imago traci 1 Stos [StackPastActivate] (1 raz na monetę)\n- Grzesznik, który zaatakował tę jednostkę, przywraca 10 Poczytalności (1 raz na turę na Grzesznika)\n\njeżeli w tej turze ta jednostka <color=#ff6000><mark=#ff000040><b><u>nie została trafiona jako główny cel</u></b></mark></color>, na koniec walki Butterfly[TabExplain] of Entangled Lives::Imago zyskuje 5 Stosów [StackPastActivate]\n- jeżeli Butterfly[TabExplain] of Entangled Lives::Imago jest Oszołamione, ten efekt nie aktywuje się
487. [[refraction6] Pasywka wroga [957202] — nazwa] 과거 - 연기 [緣起]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957202].name
   limit: do 40 znaków
   EN: The Past - Origination [緣起]
   PL: The Past - Origination [緣起]
488. [[refraction6] Pasywka wroga [957202] — opis] 속도가 1로 고정되고 체력이 1 미만으로 감소하지 않음\n\n자신이 체력 피해를 받을 때, 받은 피해의\n절반만큼을 나생접::나비에게 전가함 (소수점 버림)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957202].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain]
   EN: Fix this unit's Speed to 1; this unit's HP does not drop below 1\n\nWhen this unit takes HP damage, transfer half of damage taken to Butterfly[TabExplain] of Entangled Lives::Imago (rounded down)
   PL: Szybkość tej jednostki jest stała (1); HP tej jednostki nie spada poniżej 1\n\ngdy ta jednostka otrzymuje obrażenia HP, połowa otrzymanych obrażeń przenosi się na Butterfly[TabExplain] of Entangled Lives::Imago (zaokrąglone w dół)
489. [[refraction6] Pasywka wroga [957301] — nazwa] 현재 - 분절 [分節]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957301].name
   limit: do 50 znaków
   EN: The Present - Segmentation [分節]
   PL: The Present - Segmentation [分節]
490. [[refraction6] Pasywka wroga [957301] — opis] 나생접::나비가 보유한 [StackPresentActivate] 수치가 표시됨\n\n<color=#ff6000><mark=#ff000040><b><u>메인 타겟으로 피격</u></b></mark></color>받을 때마다\n- 나생접::나비의 [StackPresentActivate] -1 (코인당 1회)\n- 자신을 타겟한 수감자의 정신력 10 회복 (수감자별 턴당 1회)\n\n<color=#ff6000><mark=#ff000040><b><u>이번 턴에 메인 타겟으로 피격받지 않았으면,</u></b></mark></color>\n전투 종료 시 나생접::나비의 [StackPresentActivate] +5\n- 나생접::나비가 흐트러졌으면, 이 효과가 발동하지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957301].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StackPresentActivate], [TabExplain]
   znaczenie tagów: [StackPresentActivate] = 현재 상태 / In the Present
   EN: Displays current [StackPresentActivate] Stack on Butterfly[TabExplain] of Entangled Lives::Imago\n\nEvery time this unit is <color=#ff6000><mark=#ff000040><b><u>hit as the main target</u></b></mark></color>:\n- Butterfly[TabExplain] of Entangled Lives::Imago loses 1 [StackPresentActivate] Stack (once per Coin)\n- The Sinner who attacked this unit heals 10 SP (once per turn per Sinner)\n\nIf this unit <color=#ff6000><mark=#ff000040><b><u>did not get hit as the main target this turn</u></b></mark></color>, Butterfly[TabExplain] of Entangled Lives::Imago gains 5 [StackPresentActivate] Stack at Combat End\n- If Butterfly[TabExplain] of Entangled Lives::Imago is Staggered, this effect does not activate
   PL: wyświetla aktualny Stos [StackPresentActivate] jednostki Butterfly[TabExplain] of Entangled Lives::Imago\n\nza każdym razem gdy ta jednostka zostanie <color=#ff6000><mark=#ff000040><b><u>trafiona jako główny cel</u></b></mark></color>:\n- Butterfly[TabExplain] of Entangled Lives::Imago traci 1 Stos [StackPresentActivate] (1 raz na monetę)\n- Grzesznik, który zaatakował tę jednostkę, przywraca 10 Poczytalności (1 raz na turę na Grzesznika)\n\njeżeli w tej turze ta jednostka <color=#ff6000><mark=#ff000040><b><u>nie została trafiona jako główny cel</u></b></mark></color>, na koniec walki Butterfly[TabExplain] of Entangled Lives::Imago zyskuje 5 Stosów [StackPresentActivate]\n- jeżeli Butterfly[TabExplain] of Entangled Lives::Imago jest Oszołamione, ten efekt nie aktywuje się
491. [[refraction6] Pasywka wroga [957302] — nazwa] 현재 - 연기 [緣起]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957302].name
   limit: do 50 znaków
   EN: The Present - Origination [緣起]
   PL: The Present - Origination [緣起]
492. [[refraction6] Pasywka wroga [957302] — opis] 속도가 1로 고정되고 체력이 1 미만으로 감소하지 않음\n\n자신이 체력 피해를 받을 때, 받은 피해의\n절반만큼을 나생접::나비에게 전가함 (소수점 버림)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957302].desc
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [[refraction6] Pasywka wroga [957401] — nazwa] 미래 - 분절 [分節]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957401].name
   limit: do 50 znaków
   EN: The Future - Segmentation [分節]
   PL: The Future - Segmentation [分節]
494. [[refraction6] Pasywka wroga [957401] — opis] 나생접::나비가 보유한 [StackFutureActivate] 수치가 표시됨\n\n<color=#ff6000><mark=#ff000040><b><u>메인 타겟으로 피격</u></b></mark></color>받을 때마다\n- 나생접::나비의 [StackFutureActivate] -1 (코인당 1회)\n- 자신을 타겟한 수감자의 정신력 10 회복 (수감자별 턴당 1회)\n\n<color=#ff6000><mark=#ff000040><b><u>이번 턴에 메인 타겟으로 피격받지 않았으면,</u></b></mark></color>\n전투 종료 시 나생접::나비의 [StackFutureActivate] +5\n- 나생접::나비가 흐트러졌으면, 이 효과가 발동하지 않음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957401].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StackFutureActivate], [TabExplain]
   znaczenie tagów: [StackFutureActivate] = 미래 상태 / In the Future
   EN: Displays current [StackFutureActivate] Stack on Butterfly[TabExplain] of Entangled Lives::Imago\n\nEvery time this unit is <color=#ff6000><mark=#ff000040><b><u>hit as the main target</u></b></mark></color>:\n- Butterfly[TabExplain] of Entangled Lives::Imago loses 1 [StackFutureActivate] Stack (once per Coin)\n- The Sinner who attacked this unit heals 10 SP (once per turn per Sinner)\n\nIf this unit <color=#ff6000><mark=#ff000040><b><u>did not get hit as the main target this turn</u></b></mark></color>, Butterfly[TabExplain] of Entangled Lives::Imago gains 5 [StackFutureActivate] Stack at Combat End\n- If Butterfly[TabExplain] of Entangled Lives::Imago is Staggered, this effect does not activate
   PL: wyświetla aktualny Stos [StackFutureActivate] jednostki Butterfly[TabExplain] of Entangled Lives::Imago\n\nza każdym razem gdy ta jednostka zostanie <color=#ff6000><mark=#ff000040><b><u>trafiona jako główny cel</u></b></mark></color>:\n- Butterfly[TabExplain] of Entangled Lives::Imago traci 1 Stos [StackFutureActivate] (1 raz na monetę)\n- Grzesznik, który zaatakował tę jednostkę, przywraca 10 Poczytalności (1 raz na turę na Grzesznika)\n\njeżeli w tej turze ta jednostka <color=#ff6000><mark=#ff000040><b><u>nie została trafiona jako główny cel</u></b></mark></color>, na koniec walki Butterfly[TabExplain] of Entangled Lives::Imago zyskuje 5 Stosów [StackFutureActivate]\n- jeżeli Butterfly[TabExplain] of Entangled Lives::Imago jest Oszołamione, ten efekt nie aktywuje się
495. [[refraction6] Pasywka wroga [957402] — nazwa] 미래 - 연기 [緣起]
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957402].name
   limit: do 50 znaków
   EN: The Future - Origination [緣起]
   PL: The Future - Origination [緣起]
496. [[refraction6] Pasywka wroga [957402] — opis] 속도가 1로 고정되고 체력이 1 미만으로 감소하지 않음\n\n자신이 체력 피해를 받을 때, 받은 피해의\n절반만큼을 나생접::나비에게 전가함 (소수점 버림)
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=957402].desc
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [[refraction6] Pasywka wroga [955701] — nazwa] 억제된 힘
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955701].name
   limit: do 40 znaków
   EN: Suppressed Might
   PL: Stłumiona Siła
498. [[refraction6] Pasywka wroga [955701] — opis] 스테이지 등장 시 [MiddleFingerLeashBuff] 얻음
   źródło: Passives_Abnormality_Refraction6.json :: dataList[id=955701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MiddleFingerLeashBuff]
   znaczenie tagów: [MiddleFingerLeashBuff] = 억제된 힘 / Suppressed Might
   EN: Upon entering the Encounter, gain [MiddleFingerLeashBuff]
   PL: po pojawieniu się w walce zyskuje [MiddleFingerLeashBuff]

## [sweep] Wróg / część: Enemies-sweep
- plik gry: `Enemies-sweep.json`

499. [[sweep] Wróg / część [90183] — nazwa] 비열한 삼도끼 사무소 해결사
   źródło: Enemies-sweep.json :: dataList[id=90183].name
   limit: do 50 znaków
   EN: Deceitful Tri-axe Office Fixer
   PL: Deceitful Tri-axe Office Fixer
500. [[sweep] Wróg / część [90183] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90183].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [[sweep] Wróg / część [90184] — nazwa] 억척스러운 표정의 괴한
   źródło: Enemies-sweep.json :: dataList[id=90184].name
   limit: do 40 znaków
   EN: Tough-looking Stranger
   PL: Tough-looking Stranger
502. [[sweep] Wróg / część [90184] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90184].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [[sweep] Wróg / część [90193] — nazwa] 어정쩡한 삼도끼 사무소 해결사
   źródło: Enemies-sweep.json :: dataList[id=90193].name
   limit: do 40 znaków
   EN: Awkward Tri-axe Office Fixer
   PL: Awkward Tri-axe Office Fixer
504. [[sweep] Wróg / część [90193] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90193].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [[sweep] Wróg / część [90194] — nazwa] 날카로운 표정의 괴한
   źródło: Enemies-sweep.json :: dataList[id=90194].name
   limit: do 40 znaków
   EN: Sharp-looking Stranger
   PL: Sharp-looking Stranger
506. [[sweep] Wróg / część [90194] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90194].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [[sweep] Wróg / część [90185] — nazwa] 흑수 - 묘 : 쾌격
   źródło: Enemies-sweep.json :: dataList[id=90185].name
   limit: do 50 znaków
   EN: Heishou Pack - Mao: Featherstriker
   PL: Heishou Pack - Mao: Featherstriker
508. [[sweep] Wróg / część [90185] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90185].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [[sweep] Wróg / część [90186] — nazwa] 흑수 - 묘 : 암격
   źródło: Enemies-sweep.json :: dataList[id=90186].name
   limit: do 50 znaków
   EN: Heishou Pack - Mao: Umbrastriker
   PL: Heishou Pack - Mao: Umbrastriker
510. [[sweep] Wróg / część [90186] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90186].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [[sweep] Wróg / część [90187] — nazwa] 도시의 청소부 A
   źródło: Enemies-sweep.json :: dataList[id=90187].name
   limit: do 40 znaków
   EN: The City's Sweeper A
   PL: The City's Sweeper A
512. [[sweep] Wróg / część [90187] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90187].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [[sweep] Wróg / część [90188] — nazwa] 도시의 청소부 B
   źródło: Enemies-sweep.json :: dataList[id=90188].name
   limit: do 40 znaków
   EN: The City's Sweeper B
   PL: The City's Sweeper B
514. [[sweep] Wróg / część [90188] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90188].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [[sweep] Wróg / część [90189] — nazwa] 도시의 청소부 C
   źródło: Enemies-sweep.json :: dataList[id=90189].name
   limit: do 40 znaków
   EN: The City's Sweeper C
   PL: The City's Sweeper C
516. [[sweep] Wróg / część [90189] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90189].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [[sweep] Wróg / część [90190] — nazwa] 도시의 청소부 D
   źródło: Enemies-sweep.json :: dataList[id=90190].name
   limit: do 40 znaków
   EN: The City's Sweeper D
   PL: The City's Sweeper D
518. [[sweep] Wróg / część [90190] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90190].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [[sweep] Wróg / część [91020] — nazwa] 작은 아우 베르너
   źródło: Enemies-sweep.json :: dataList[id=91020].name
   limit: do 40 znaków
   EN: Little Brother Werner
   PL: Little Brother Werner
520. [[sweep] Wróg / część [91020] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=91020].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [[sweep] Wróg / część [90191] — nazwa] 엄격한 중지 작은 아우
   źródło: Enemies-sweep.json :: dataList[id=90191].name
   limit: do 50 znaków
   EN: Stern Little Brother of the Middle
   PL: Stern Little Brother of the Middle
522. [[sweep] Wróg / część [90191] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90191].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [[sweep] Wróg / część [90192] — nazwa] 든든한 중지 작은 아우
   źródło: Enemies-sweep.json :: dataList[id=90192].name
   limit: do 50 znaków
   EN: Sturdy Little Brother of the Middle
   PL: Sturdy Little Brother of the Middle
524. [[sweep] Wróg / część [90192] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=90192].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [[sweep] Wróg / część [1126] — nazwa] 자로
   źródło: Enemies-sweep.json :: dataList[id=1126].name
   limit: do 40 znaków
   EN: Zilu
   PL: Zilu
526. [[sweep] Wróg / część [1126] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=1126].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [[sweep] Wróg / część [112601] — nazwa] 몸통
   źródło: Enemies-sweep.json :: dataList[id=112601].name
   limit: do 40 znaków
   EN: Body
   PL: Body
528. [[sweep] Wróg / część [112601] — opis] 부위
   źródło: Enemies-sweep.json :: dataList[id=112601].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [[sweep] Wróg / część [1127] — nazwa] 리카르도
   źródło: Enemies-sweep.json :: dataList[id=1127].name
   limit: do 40 znaków
   EN: Ricardo
   PL: Ricardo
530. [[sweep] Wróg / część [1127] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=1127].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [[sweep] Wróg / część [112701] — nazwa] 몸통
   źródło: Enemies-sweep.json :: dataList[id=112701].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [[sweep] Wróg / część [112701] — opis] 부위
   źródło: Enemies-sweep.json :: dataList[id=112701].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [[sweep] Wróg / część [1128] — nazwa] 작은 아우 베르너
   źródło: Enemies-sweep.json :: dataList[id=1128].name
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [[sweep] Wróg / część [1128] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=1128].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [[sweep] Wróg / część [112801] — nazwa] 몸통
   źródło: Enemies-sweep.json :: dataList[id=112801].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [[sweep] Wróg / część [112801] — opis] 부위
   źródło: Enemies-sweep.json :: dataList[id=112801].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [[sweep] Wróg / część [1129] — nazwa] 엄격한 중지 작은 아우
   źródło: Enemies-sweep.json :: dataList[id=1129].name
   (powtórzenie elementu 521 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [[sweep] Wróg / część [1129] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=1129].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [[sweep] Wróg / część [112901] — nazwa] 몸통
   źródło: Enemies-sweep.json :: dataList[id=112901].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [[sweep] Wróg / część [112901] — opis] 부위
   źródło: Enemies-sweep.json :: dataList[id=112901].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [[sweep] Wróg / część [1130] — nazwa] 든든한 중지 작은 아우
   źródło: Enemies-sweep.json :: dataList[id=1130].name
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [[sweep] Wróg / część [1130] — opis] 본체
   źródło: Enemies-sweep.json :: dataList[id=1130].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [[sweep] Wróg / część [113001] — nazwa] 몸통
   źródło: Enemies-sweep.json :: dataList[id=113001].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [[sweep] Wróg / część [113001] — opis] 부위
   źródło: Enemies-sweep.json :: dataList[id=113001].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [tkt] Wróg / część: Enemies-tkt
- plik gry: `Enemies-tkt.json`

545. [[tkt] Wróg / część [90140] — nazwa] 과격한 유로지비 활동단원
   źródło: Enemies-tkt.json :: dataList[id=90140].name
   limit: do 40 znaków
   EN: Aggressive Yurodivy
   PL: Aggressive Yurodivy
546. [[tkt] Wróg / część [90140] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=90140].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [[tkt] Wróg / część [90141] — nazwa] 재빠른 유로지비 활동단원
   źródło: Enemies-tkt.json :: dataList[id=90141].name
   limit: do 40 znaków
   EN: Quick-witted Yurodivy
   PL: Quick-witted Yurodivy
548. [[tkt] Wróg / część [90141] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=90141].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [[tkt] Wróg / część [91017] — nazwa] 20구 유로지비 대장
   źródło: Enemies-tkt.json :: dataList[id=91017].name
   limit: do 50 znaków
   EN: District 20 Yurodiviye Captain
   PL: District 20 Yurodiviye Captain
550. [[tkt] Wróg / część [91017] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=91017].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [[tkt] Wróg / część [90142] — nazwa] T사 2등급 징수직
   źródło: Enemies-tkt.json :: dataList[id=90142].name
   limit: do 50 znaków
   EN: T Corp. Class 2 Collection Staff
   PL: T Corp. Class 2 Collection Staff
552. [[tkt] Wróg / część [90142] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=90142].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [[tkt] Wróg / część [90143] — nazwa] T사 3등급 징수직 - 사살
   źródło: Enemies-tkt.json :: dataList[id=90143].name
   limit: do 60 znaków
   EN: T Corp. Class 3 Collector - Neutralize
   PL: T Corp. Class 3 Collector - Neutralize
554. [[tkt] Wróg / część [90143] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=90143].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [[tkt] Wróg / część [90144] — nazwa] T사 3등급 징수직 - 제압
   źródło: Enemies-tkt.json :: dataList[id=90144].name
   limit: do 50 znaków
   EN: T Corp. Class 3 Collector - Suppress
   PL: T Corp. Class 3 Collector - Suppress
556. [[tkt] Wróg / część [90144] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=90144].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [[tkt] Wróg / część [8277] — nazwa] 시간 살인마
   źródło: Enemies-tkt.json :: dataList[id=8277].name
   limit: do 40 znaków
   EN: The Time Ripper
   PL: The Time Ripper
558. [[tkt] Wróg / część [8277] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=8277].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [[tkt] Wróg / część [827701] — nazwa] 몸통
   źródło: Enemies-tkt.json :: dataList[id=827701].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [[tkt] Wróg / część [827701] — opis] 부위
   źródło: Enemies-tkt.json :: dataList[id=827701].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [[tkt] Wróg / część [8278] — nazwa] 시간 살인마
   źródło: Enemies-tkt.json :: dataList[id=8278].name
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [[tkt] Wróg / część [8278] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=8278].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [[tkt] Wróg / część [827801] — nazwa] 뇌
   źródło: Enemies-tkt.json :: dataList[id=827801].name
   limit: do 40 znaków
   EN: Brain
   PL: Brain
564. [[tkt] Wróg / część [827801] — opis] 부위
   źródło: Enemies-tkt.json :: dataList[id=827801].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [[tkt] Wróg / część [827802] — nazwa] 뇌
   źródło: Enemies-tkt.json :: dataList[id=827802].name
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [[tkt] Wróg / część [827802] — opis] 부위
   źródło: Enemies-tkt.json :: dataList[id=827802].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [[tkt] Wróg / część [827803] — nazwa] 뇌
   źródło: Enemies-tkt.json :: dataList[id=827803].name
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [[tkt] Wróg / część [827803] — opis] 부위
   źródło: Enemies-tkt.json :: dataList[id=827803].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [[tkt] Wróg / część [827804] — nazwa] 뇌
   źródło: Enemies-tkt.json :: dataList[id=827804].name
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [[tkt] Wróg / część [827804] — opis] 부위
   źródło: Enemies-tkt.json :: dataList[id=827804].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [[tkt] Wróg / część [827805] — nazwa] 뇌
   źródło: Enemies-tkt.json :: dataList[id=827805].name
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [[tkt] Wróg / część [827805] — opis] 부위
   źródło: Enemies-tkt.json :: dataList[id=827805].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [[tkt] Wróg / część [8279] — nazwa] 펼쳐진 시간 살인마들
   źródło: Enemies-tkt.json :: dataList[id=8279].name
   limit: do 40 znaków
   EN: Unfolded Time Rippers
   PL: Unfolded Time Rippers
574. [[tkt] Wróg / część [8279] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=8279].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [[tkt] Wróg / część [827901] — nazwa] 몸통
   źródło: Enemies-tkt.json :: dataList[id=827901].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [[tkt] Wróg / część [827901] — opis] 본체
   źródło: Enemies-tkt.json :: dataList[id=827901].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [tkt] Umiejętności wrogów / Anomalii — Skills_Abnormality-tkt
- grupa rozdziału/trybu: `tkt` · plik: `Skills_Abnormality-tkt.json`

577. [Umiejętność wroga [827701] (ulepszenie 1) — nazwa] 겁을 먹었나?
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827701].levelList[level=1].name
   limit: do 40 znaków
   EN: Are You Afraid?
   PL: Are You Afraid?
578. [Umiejętność wroga [827701] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +1\n[DefeatDuel] 자신의 체력이 75% 미만이면, [LimitedTime]을 50 소모하여, [Protection] 1 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827701].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [DefeatDuel], [LimitedTime], [Protection]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [DefeatDuel] = [합 패배] / [Clash Lose]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [Protection] = 보호 / Protection
   EN: When in [TimeAcceleration] state, Clash Power +1\n[DefeatDuel] At 75%- HP, consume 50 [LimitedTime] and gain 1 [Protection] (once per turn)
   PL: w stanie [TimeAcceleration], Moc Starcia +1\n[DefeatDuel] przy 75% HP lub mniej, zużywa 50 [LimitedTime] i zyskuje 1 [Protection] (1 raz na turę)
579. [Umiejętność wroga [827701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
580. [Umiejętność wroga [827701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [827702] (ulepszenie 1) — nazwa] 시간을 죽인 벌
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827702].levelList[level=1].name
   limit: do 40 znaków
   EN: Punishment For Time Killers
   PL: Punishment For Time Killers
582. [Umiejętność wroga [827702] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +2\n[WhenUse] [LimitedTime]이 500 이상이면, 대상의 [Laceration] 횟수 1 증가\n[WhenUse] [LimitedTime]이 300 이상이면, [LimitedTime]을 25 소모하여, 이 스킬에서 부여하는 [Laceration] 위력과 횟수 +1
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827702].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [LimitedTime], [Laceration]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [Laceration] = 출혈 / Bleed
   EN: When in [TimeAcceleration] state, Clash Power +2\n[WhenUse] At 500+ [LimitedTime], inflict +1 [Laceration] Count\n[WhenUse] At 300+ [LimitedTime], consume 25 [LimitedTime] and inflict +1 more [Laceration] Potency and Count with this Skill
   PL: w stanie [TimeAcceleration], Moc Starcia +2\n[WhenUse] przy 500+ [LimitedTime], zwiększa Licznik [Laceration] o 1\n[WhenUse] przy 300+ [LimitedTime], zużywa 25 [LimitedTime] i nakłada o 1 więcej Mocy [Laceration] i Licznika [Laceration] tą Umiejętnością
583. [Umiejętność wroga [827702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
584. [Umiejętność wroga [827702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
585. [Umiejętność wroga [827702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [827703] (ulepszenie 1) — nazwa] 적출
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827703].levelList[level=1].name
   limit: do 40 znaków
   EN: Extraction
   PL: Ekstrakcja
587. [Umiejętność wroga [827703] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 코인 위력 +1\n[WhenUse] 자신의 체력이 75%미만이면, [LimitedTime]을 50소모하여, 합 위력 +2
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827703].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [LimitedTime]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time
   EN: When in [TimeAcceleration] state, Coin Power +1\n[WhenUse] At 75%- HP, consume 50 [LimitedTime] and gain Clash Power +2 (once per turn)
   PL: w stanie [TimeAcceleration], Moc Monet +1\n[WhenUse] przy 75% HP lub mniej, zużywa 50 [LimitedTime] i zyskuje Moc Starcia +2 (1 raz na turę)
588. [Umiejętność wroga [827703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność wroga [827703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [827703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [827703] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827703].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [827704] (ulepszenie 1) — nazwa] 난도질
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827704].levelList[level=1].name
   limit: do 40 znaków
   EN: Mutilate
   PL: Okaleczenie
593. [Umiejętność wroga [827704] (ulepszenie 1) — opis] [WhenUse] 자신의 체력이 75%미만이면, [LimitedTime]을 75 소모하여, 합 위력 +2\n[BeforeAttack] [TimeAcceleration] 상태면, 공격 가중치 1 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827704].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [LimitedTime], [BeforeAttack], [TimeAcceleration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [WhenUse] At 75%- HP, consume 75 [LimitedTime] and gain Clash Power +2\n[BeforeAttack] When in [TimeAcceleration] state, gain +1 Atk Weight
   PL: [WhenUse] przy 75% HP lub mniej, zużywa 75 [LimitedTime] i zyskuje Moc Starcia +2\n[BeforeAttack] w stanie [TimeAcceleration], Waga Ataku +1
594. [Umiejętność wroga [827704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [827704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL: [OnSucceedAttack] nakłada 8 [Laceration]
596. [Umiejętność wroga [827705] (ulepszenie 1) — nazwa] 구원할 시간
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827705].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to be Saved
   PL: Time to be Saved
597. [Umiejętność wroga [827705] (ulepszenie 1) — opis] [CantDuel]\n자신에게 공격 스킬을 사용한 대상에게 다음 턴에 [TimeKillerWatch] 부여\n[StartBattle] [LimitedTime] 200 소모. 다음 턴에 [TimeAcceleration]을 얻음
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827705].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [TimeKillerWatch], [StartBattle], [LimitedTime], [TimeAcceleration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [TimeKillerWatch] = 시간 구제 대상 / Time Relief Entitlement; [StartBattle] = [전투 시작시] / [Combat Start]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [CantDuel]\nInflict [TimeKillerWatch] against the target that used an Attack Skill against this unit\n[StartBattle] Consume 200 [LimitedTime] and gain [TimeAcceleration] next turn
   PL: [CantDuel]\nnakłada [TimeKillerWatch] na cel, który użył Umiejętności ataku przeciwko tej jednostce\n[StartBattle] zużywa 200 [LimitedTime] i zyskuje [TimeAcceleration] w następnej turze
598. [Umiejętność wroga [827706] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827706].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Unik
599. [Umiejętność wroga [827706] (ulepszenie 1) — opis] [WhenUse] [LimitedTime] 100 당, 기본 위력 +1
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [LimitedTime]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time
   EN: [WhenUse] Base Power +1 for every 100 [LimitedTime] on self
   PL: [WhenUse] Moc Bazowa +1 za każde 100 [LimitedTime] na sobie
600. [Umiejętność wroga [827801] (ulepszenie 1) — nazwa] 겁을 먹었나?
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827801].levelList[level=1].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [827801] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +1\n[DefeatDuel] 자신의 체력이 75% 미만이면, [OwnTime]을 50 소모하여, [Protection] 1 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827801].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [DefeatDuel], [OwnTime], [Protection]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [DefeatDuel] = [합 패배] / [Clash Lose]; [OwnTime] = 분담 시간 / Shared Time; [Protection] = 보호 / Protection
   EN: When in [TimeAcceleration] state, Clash Power +1\n[DefeatDuel] At 75%- HP, consume 50 [OwnTime] and gain 1 [Protection] (once per turn)
   PL: w stanie [TimeAcceleration], Moc Starcia +1\n[DefeatDuel] przy 75% HP lub mniej, zużywa 50 [OwnTime] i zyskuje 1 [Protection] (1 raz na turę)
602. [Umiejętność wroga [827801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [827801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność wroga [827802] (ulepszenie 1) — nazwa] 시간을 죽인 벌
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827802].levelList[level=1].name
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [827802] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +2\n[WhenUse] 모든 부위가 보유한 [OwnTime]의 합이 500 이상이면, 대상의 [Laceration] 횟수 1 증가\n[WhenUse] 모든 부위가 보유한 [OwnTime]의 합이 300 이상이면, [OwnTime]을 25 소모하여, 이 스킬에서 부여하는 [Laceration] 위력과 횟수 +1
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827802].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [OwnTime], [Laceration]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time; [Laceration] = 출혈 / Bleed
   EN: When in [TimeAcceleration] state, Clash Power +2\n[WhenUse] At 500+ (sum of [OwnTime] on all Parts), inflict +1 [Laceration] Count\n[WhenUse] At 300+ (sum of [OwnTime] on all Parts), consume 25 [OwnTime] and inflict +1 more [Laceration] Potency and Count with this Skill
   PL: w stanie [TimeAcceleration], Moc Starcia +2\n[WhenUse] przy 500+ (suma [OwnTime] wszystkich Części), zwiększa Licznik [Laceration] o 1\n[WhenUse] przy 300+ (suma [OwnTime] wszystkich Części), zużywa 25 [OwnTime] i nakłada o 1 więcej Mocy [Laceration] i Licznika [Laceration] tą Umiejętnością
606. [Umiejętność wroga [827802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [827802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [827802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [827803] (ulepszenie 1) — nazwa] 적출
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827803].levelList[level=1].name
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność wroga [827803] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 코인 위력 +1\n[WhenUse] 자신의 체력이 75%미만이면, [OwnTime]을 50소모하여, 합 위력 +2
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827803].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [OwnTime]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time
   EN: When in [TimeAcceleration] state, Coin Power +1\n[WhenUse] At 75%- HP, consume 50 [OwnTime] and gain Clash Power +2 (once per turn)
   PL: w stanie [TimeAcceleration], Moc Monet +1\n[WhenUse] przy 75% HP lub mniej, zużywa 50 [OwnTime] i zyskuje Moc Starcia +2 (1 raz na turę)
611. [Umiejętność wroga [827803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [827803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [827803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [827803] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827803].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [827804] (ulepszenie 1) — nazwa] 난도질
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827804].levelList[level=1].name
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność wroga [827804] (ulepszenie 1) — opis] [WhenUse] 자신의 체력이 75%미만이면, [OwnTime]을 75 소모하여, 합 위력 +2\n[BeforeAttack] [TimeAcceleration] 상태면, 공격 가중치 1 증가\n[BeforeAttack] 자신의 체력이 60% 미만이면, [OwnTime]을 10 소모하여, 공격 가중치 1 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827804].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OwnTime], [BeforeAttack], [TimeAcceleration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [WhenUse] At 75%- HP, consume 75 [OwnTime] and gain Clash Power +2\n[BeforeAttack] When in [TimeAcceleration] state, gain +1 Atk Weight\n[BeforeAttack] At 60%- HP, consume 10 [OwnTime] and gain +1 Atk Weight
   PL: [WhenUse] przy 75% HP lub mniej, zużywa 75 [OwnTime] i zyskuje Moc Starcia +2\n[BeforeAttack] w stanie [TimeAcceleration], Waga Ataku +1\n[BeforeAttack] przy 60% HP lub mniej, zużywa 10 [OwnTime] i zyskuje Waga Ataku +1
617. [Umiejętność wroga [827804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [827804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [827805] (ulepszenie 1) — nazwa] 구원할 시간
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827805].levelList[level=1].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [827805] (ulepszenie 1) — opis] [CantDuel]\n자신에게 공격 스킬을 사용한 대상에게 다음 턴에 [TimeKillerWatch] 부여\n[StartBattle] [OwnTime] 200 소모. 다음 턴에 [TimeAcceleration]을 얻음
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827805].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [TimeKillerWatch], [StartBattle], [OwnTime], [TimeAcceleration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [TimeKillerWatch] = 시간 구제 대상 / Time Relief Entitlement; [StartBattle] = [전투 시작시] / [Combat Start]; [OwnTime] = 분담 시간 / Shared Time; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [CantDuel]\nInflict [TimeKillerWatch] against the target that used an Attack Skill against this unit\n[StartBattle] Consume 200 [OwnTime] and gain [TimeAcceleration] next turn
   PL: [CantDuel]\nnakłada [TimeKillerWatch] na cel, który użył Umiejętności ataku przeciwko tej jednostce\n[StartBattle] zużywa 200 [OwnTime] i zyskuje [TimeAcceleration] w następnej turze
621. [Umiejętność wroga [827806] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827806].levelList[level=1].name
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [827806] (ulepszenie 1) — opis] [WhenUse] 모든 부위가 보유한 [OwnTime]의 합 100 당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827806].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [OwnTime]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time
   EN: [WhenUse] Base Power +1 for every 100 sum of [OwnTime] across all Parts (max 3)
   PL: [WhenUse] Moc Bazowa +1 za każde 100 sumy [OwnTime] wszystkich Części (maks. 3)
623. [Umiejętność wroga [827807] (ulepszenie 1) — nazwa] 시간 살인 시간
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827807].levelList[level=1].name
   limit: do 40 znaków
   EN: Timekilling Time
   PL: Czas Zabijania Czasu
624. [Umiejętność wroga [827807] (ulepszenie 1) — opis] [CantDuel]\n자신의 속도를 24로 고정함.\n이번 턴동안 흐트러짐 상태가 되지 않음.\n[WhenUse] 모두의 마지막 남은 [OwnTime] 400 획득 후 소모.
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827807].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [OwnTime]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time
   EN: [CantDuel]\nThis unit's Speed is fixed at 24.\nCannot be Staggered this turn.\n[WhenUse] Takes a total of 400 [OwnTime] from everyone, then consumes it.
   PL: [CantDuel]\nSzybkość tej jednostki jest stała (24).\nw tej turze nie może przejść w Oszołamienie.\n[WhenUse] zabiera łącznie 400 [OwnTime] od wszystkich, po czym je zużywa.
625. [Umiejętność wroga [827807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 시간을 삭제함. 대상의 시간을 삭제시켰다면, 모든 부위가 [OwnTime]을 최대로 회복하고, 다음 턴에 신속, 공격 위력 증가 10을 얻음.
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [OwnTime]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [OwnTime] = 분담 시간 / Shared Time
   EN: [OnSucceedAttack] Erase the target's time. Once this unit erases the target's time, all Parts recover [OwnTime] to their max values and gain 10 Haste and 10 Attack Power Up next turn.
   PL: [OnSucceedAttack] usuwa czas celu. gdy ta jednostka usunie czas celu, wszystkie Części odzyskują [OwnTime] do maksymalnych wartości i zyskują w następnej turze 10 Pośpiechu i 10 Wzrost Mocy Ataku.
626. [Umiejętność wroga [827901] (ulepszenie 1) — nazwa] 째깍
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827901].levelList[level=1].name
   limit: do 40 znaków
   EN: Tick
   PL: Tick
627. [Umiejętność wroga [827901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [827902] (ulepszenie 1) — nazwa] 째-깍
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827902].levelList[level=1].name
   limit: do 40 znaków
   EN: Tock
   PL: Tock
629. [Umiejętność wroga [827902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5이상이면, 합 위력 +1
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 5+ [Laceration], Clash Power +1
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Starcia +1
630. [Umiejętność wroga [827902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność wroga [827902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [827902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność wroga [827903] (ulepszenie 1) — nazwa] 째째깍
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827903].levelList[level=1].name
   limit: do 40 znaków
   EN: Ticktick-Tock
   PL: Ticktick-Tock
634. [Umiejętność wroga [827903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5이상이면, 합 위력 +1
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827903].levelList[level=1].desc
   (powtórzenie elementu 629 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność wroga [827903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [827903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [827903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 화상 5 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Burn
   PL: [OnSucceedAttack] nakłada 5 Podpalenia
638. [Umiejętność wroga [827904] (ulepszenie 1) — nazwa] 깍
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827904].levelList[level=1].name
   limit: do 40 znaków
   EN: Tock
   PL: Tock
639. [Umiejętność wroga [827707] (ulepszenie 1) — nazwa] 이런...
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827707].levelList[level=1].name
   limit: do 40 znaków
   EN: My...
   PL: My...
640. [Umiejętność wroga [827707] (ulepszenie 1) — opis] [DefeatDuel] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827707].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [Vulnerable]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [DefeatDuel] Gain 1 [Vulnerable]
   PL: [DefeatDuel] zyskuje 1 [Vulnerable]
641. [Umiejętność wroga [827707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność wroga [827707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [827708] (ulepszenie 1) — nazwa] 시간이 부족해
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827708].levelList[level=1].name
   limit: do 40 znaków
   EN: Running Out of Time
   PL: Running Out of Time
644. [Umiejętność wroga [827708] (ulepszenie 1) — opis] [DefeatDuel] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827708].levelList[level=1].desc
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [827708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność wroga [827708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność wroga [827708] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827708].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność wroga [827708] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827708].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [827808] (ulepszenie 1) — nazwa] 시간이 필요해!
   źródło: Skills_Abnormality-tkt.json :: dataList[id=827808].levelList[level=1].name
   limit: do 40 znaków
   EN: We Need More Time!
   PL: We Need More Time!

## [tkt] Umiejętności wrogów / Anomalii — Skills_Enemy-tkt
- grupa rozdziału/trybu: `tkt` · plik: `Skills_Enemy-tkt.json`

650. [Umiejętność wroga [9014001] (ulepszenie 1) — nazwa] 방해하지마
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014001].levelList[level=1].name
   limit: do 40 znaków
   EN: Away With You
   PL: Nie Przeszkadzaj
651. [Umiejętność wroga [9014001] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2
652. [Umiejętność wroga [9014001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수만큼 자신의 [Vibration] 횟수 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to [Vibration] Count on target
   PL: [OnSucceedAttack] zyskuje Licznik [Vibration] równy Licznikowi [Vibration] celu
653. [Umiejętność wroga [9014001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
654. [Umiejętność wroga [9014001] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014001].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +2 [Vibration] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Vibration] o 2
655. [Umiejętność wroga [9014002] (ulepszenie 1) — nazwa] 비장의 무기다
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014002].levelList[level=1].name
   limit: do 40 znaków
   EN: My Secret Weapon
   PL: My Secret Weapon
656. [Umiejętność wroga [9014002] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014002].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Umiejętność wroga [9014002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
658. [Umiejętność wroga [9014002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [9014002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [9014002] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014002].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [9014003] (ulepszenie 1) — nazwa] 더러운 시곗줄들!
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014003].levelList[level=1].name
   limit: do 40 znaków
   EN: Filthy Watch Chains!
   PL: Filthy Watch Chains!
662. [Umiejętność wroga [9014003] (ulepszenie 1) — opis] 자신의 [Vibration] 횟수 5당, 합 위력 +1 (최대 2)\n[WhenUse] 자신의 [Vibration]을 [VibrationDistribution]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014003].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [WhenUse], [VibrationDistribution], [Switch_Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: Clash Power +1 for every 5 [Vibration] Count on self (max 2)\n[WhenUse] Trigger [Switch_Vibration] to convert [Vibration] on self to [VibrationDistribution]
   PL: Moc Starcia +1 za każde 5 Liczników [Vibration] na sobie (maks. 2)\n[WhenUse] uruchamia [Switch_Vibration], zamieniając [Vibration] na sobie w [VibrationDistribution]
663. [Umiejętność wroga [9014003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수만큼 [Vibration] 횟수 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] Count equal to [Vibration] Count on self
   PL: [OnSucceedAttack] zyskuje Licznik [Vibration] równy Licznikowi [Vibration] na sobie
664. [Umiejętność wroga [9014003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
665. [Umiejętność wroga [9014004] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014004].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Garda
666. [Umiejętność wroga [9014004] (ulepszenie 1) — opis] [StartBattle] 자신의 [Vibration] 횟수 2배만큼 보호막 체력을 얻음 (최대 20)
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Gain 2 x ([Vibration] Count on self) Shield HP (max 20)
   PL: [StartBattle] zyskuje HP Tarczy równe 2 x (Licznik [Vibration] na sobie) (maks. 20)
667. [Umiejętność wroga [9014101] (ulepszenie 1) — nazwa] 비켜 비켜
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014101].levelList[level=1].name
   limit: do 40 znaków
   EN: Outta My Way
   PL: Outta My Way
668. [Umiejętność wroga [9014101] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014101].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność wroga [9014101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]만큼 자신의 [Vibration] 얻음
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] equal to [Vibration] on target
   PL: [OnSucceedAttack] zyskuje [Vibration] równy [Vibration] celu
670. [Umiejętność wroga [9014101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL: [OnSucceedAttack] nakłada 6 [Vibration]
671. [Umiejętność wroga [9014101] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014101].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [9014102] (ulepszenie 1) — nazwa] 만만치 않을걸?
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014102].levelList[level=1].name
   limit: do 40 znaków
   EN: I'm Pretty Good, You Know
   PL: I'm Pretty Good, You Know
673. [Umiejętność wroga [9014102] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014102].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność wroga [9014102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
675. [Umiejętność wroga [9014102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność wroga [9014102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [9014102] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014102].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Umiejętność wroga [9014103] (ulepszenie 1) — nazwa] 비열한 시곗줄이!
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014103].levelList[level=1].name
   limit: do 40 znaków
   EN: Vile Watch Chains!
   PL: Vile Watch Chains!
679. [Umiejętność wroga [9014103] (ulepszenie 1) — opis] 자신의 [Vibration] 횟수 5당, 합 위력 +1 (최대 2)\n[WhenUse] 자신의 [Vibration]을 [VibrationDistribution]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014103].levelList[level=1].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [9014103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration]만큼 [Vibration] 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] equal to [Vibration] on target
   PL: [OnSucceedAttack] zyskuje [Vibration] równy [Vibration] celu
681. [Umiejętność wroga [9014103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [9014104] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014104].levelList[level=1].name
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Umiejętność wroga [9014104] (ulepszenie 1) — opis] [StartBattle] 자신의 [Vibration] 횟수 2배만큼 보호막 체력을 얻음 (최대 20)
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014104].levelList[level=1].desc
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [9101701] (ulepszenie 1) — nazwa] 양심 없냐?
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101701].levelList[level=1].name
   limit: do 40 znaków
   EN: Have You No Shame?
   PL: Have You No Shame?
685. [Umiejętność wroga [9101701] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +1 [Vibration] Count
   PL: [WhenUse] Zyskuje +1 Licznik [Vibration]
686. [Umiejętność wroga [9101701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
687. [Umiejętność wroga [9101701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Umiejętność wroga [9101702] (ulepszenie 1) — nazwa] 양심 없구나
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101702].levelList[level=1].name
   limit: do 40 znaków
   EN: I See, You Have No Shame
   PL: I See, You Have No Shame
689. [Umiejętność wroga [9101702] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101702].levelList[level=1].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [9101702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Umiejętność wroga [9101702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność wroga [9101703] (ulepszenie 1) — nazwa] 지켜줄 수 있을까?
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101703].levelList[level=1].name
   limit: do 40 znaków
   EN: Can You Protect Them?
   PL: Can You Protect Them?
693. [Umiejętność wroga [9101703] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101703].levelList[level=1].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [9101703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] nakłada 5 [Vibration]
695. [Umiejętność wroga [9101703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 10 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] At 10+ [Vibration] Count on self, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] przy 10+ Licznikach [Vibration] na sobie, uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
696. [Umiejętność wroga [9101703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 위력이 15이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 15+ [Vibration] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli cel ma 15+ Mocy [Vibration], uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
697. [Umiejętność wroga [9101704] (ulepszenie 1) — nazwa] 그 무기 못쓸걸?
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101704].levelList[level=1].name
   limit: do 40 znaków
   EN: Can't Use That Weapon Now
   PL: Can't Use That Weapon Now
698. [Umiejętność wroga [9101704] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101704].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [9101704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność wroga [9101704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [9101704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationCollapse], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationCollapse]
   PL: [OnSucceedAttack] uruchamia [Switch_Vibration] w [VibrationCollapse]
702. [Umiejętność wroga [9101705] (ulepszenie 1) — nazwa] 각오는 되어있겠지?
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101705].levelList[level=1].name
   limit: do 40 znaków
   EN: Ready For A Beating?
   PL: Ready For A Beating?
703. [Umiejętność wroga [9101705] (ulepszenie 1) — opis] [VibrationCollapse]가 있는 대상 우선 공격\n[WhenUse] 자신을 제외한 모든 아군에게 자신의 [Vibration] 횟수만큼 [Vibration] 횟수 부여\n[WhenUse] 자신을 포함한 모든 아군의 [Vibration]을 [VibrationDistribution]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101705].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationCollapse], [WhenUse], [Vibration], [VibrationDistribution], [Switch_Vibration]
   znaczenie tagów: [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: Prioritizes targets with [VibrationCollapse]\n[WhenUse] Apply [Vibration] Count equal to [Vibration] Count on self to all other allies\n[WhenUse] Trigger [Switch_Vibration] on all allies(including this unit) to convert their [Vibration] to [VibrationDistribution]
   PL: priorytet: cele z [VibrationCollapse]\n[WhenUse] nakłada Licznik [Vibration] równy Licznikowi [Vibration] na sobie wszystkim pozostałym sojusznikom\n[WhenUse] uruchamia [Switch_Vibration] na wszystkich sojusznikach (łącznie z tą jednostką), zamieniając ich [Vibration] w [VibrationDistribution]
704. [Umiejętność wroga [9101705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 10 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 10 [Vibration]
   PL: [OnSucceedAttack] nakłada 10 [Vibration]
705. [Umiejętność wroga [9101705] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationEcho]으로 [FusionVibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101705].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationEcho], [FusionVibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [OnSucceedAttack] Trigger [FusionVibration] into [VibrationEcho]
   PL: [OnSucceedAttack] uruchamia [FusionVibration] w [VibrationEcho]
706. [Umiejętność wroga [9101706] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101706].levelList[level=1].name
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność wroga [9101706] (ulepszenie 1) — opis] [StartBattle] 자신의 [Vibration] 횟수 3배만큼 보호막 체력을 얻음 (최대 30)
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Gain 3 x ([Vibration] Count on self) Shield HP (max 30)
   PL: [StartBattle] zyskuje HP Tarczy równe 3 x (Licznik [Vibration] na sobie) (maks. 30)
708. [Umiejętność wroga [9101707] (ulepszenie 1) — nazwa] 대의를 위한 수거
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].name
   limit: do 40 znaków
   EN: For the Greater Good
   PL: For the Greater Good
709. [Umiejętność wroga [9101707] (ulepszenie 1) — opis] [CantDuel]\n[StartBattle] 자신을 제외한 모든 아군의 [Vibration] 횟수 자신이 얻고 모든 아군의 [Vibration] 제거\n[StartBattle] 자신의 [Vibration] 횟수 3당 [AttackUp] 1을 얻음\n[WhenUse] 자신의 [Vibration] 횟수 9 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [Vibration], [AttackUp], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\n[StartBattle] Draw all other allies' [Vibration] Count to self; [Vibration] on all allies expire\n[StartBattle] Gain 1 [AttackUp] for every 3 [Vibration] Count on self\n[WhenUse] Gain 9 [Vibration] Count
   PL: [CantDuel]\n[StartBattle] przenosi Licznik [Vibration] wszystkich pozostałych sojuszników na siebie; [Vibration] wszystkich sojuszników wygasa\n[StartBattle] zyskuje 1 [AttackUp] za każde 3 Liczniki [Vibration] na sobie\n[WhenUse] zyskuje 9 Liczników [Vibration]
710. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 10 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 704 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수당 10%만큼의 추가 나태 피해량 입힘
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Deal 10% bonus Sloth damage for every [Vibration] Count on self
   PL: [OnSucceedAttack] zadaje dodatkowe 10% obrażeń Lenistwa za każdy Licznik [Vibration] na sobie
712. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 4 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +4 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Vibration]
713. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수당 10%만큼의 추가 나태 피해량 입힘
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 소모하여, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Consume 3 [Vibration] Count on self, and trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] zużywa 3 Liczniki [Vibration] na sobie i uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
715. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 소모하여, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 714 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność wroga [9101707] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 소모하여, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt.json :: dataList[id=9101707].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 714 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność wroga [9014201] (ulepszenie 1) — nazwa] 징수 검문
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014201].levelList[level=1].name
   limit: do 40 znaków
   EN: Collection Stop-and-search
   PL: Collection Stop-and-search
718. [Umiejętność wroga [9014201] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014201].levelList[level=1].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [9014201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 4 이상이면, [InterlockingTime_Re] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [InterlockingTime_Re]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [InterlockingTime_Re] = 맞물리는 시간 / Interlocking Time
   EN: [OnSucceedAttack] If target has 4+ [Vibration] Count, inflict 1 [InterlockingTime_Re]
   PL: [OnSucceedAttack] jeżeli cel ma 4+ Liczników [Vibration], nakłada 1 [InterlockingTime_Re]
720. [Umiejętność wroga [9014201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 4 이상이면, [InterlockingTime_Re] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [9014201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +1 [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o 1
722. [Umiejętność wroga [9014202] (ulepszenie 1) — nazwa] 거기 멈춰주시기 바랍니다.
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].name
   limit: do 40 znaków
   EN: Please Stop.
   PL: Please Stop.
723. [Umiejętność wroga [9014202] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수가 4 이상이면, 합 위력 +1
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n[WhenUse] At 4+ [Vibration] Count, Clash Power +1
   PL: [WhenUse] zyskuje +2 Licznika [Vibration]\n[WhenUse] przy 4+ Licznikach [Vibration], Moc Starcia +1
724. [Umiejętność wroga [9014202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 2 [Paralysis] w następnej turze
725. [Umiejętność wroga [9014202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 4 이상이면, [Vibration] 8 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 4+ [Vibration] Count, inflict 8 [Vibration]
   PL: [OnSucceedAttack] przy 4+ Licznikach [Vibration], nakłada 8 [Vibration]
726. [Umiejętność wroga [9014202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +2 [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o 2
727. [Umiejętność wroga [9014202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [9014202] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 4 이상이면, [Vibration] 횟수 8 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014202].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 4+ [Vibration] Count, inflict 8 [Vibration] Count
   PL: [OnSucceedAttack] przy 4+ Licznikach [Vibration], zwiększa własny Licznik [Vibration] o 8
729. [Umiejętność wroga [9014203] (ulepszenie 1) — nazwa] 강제 징수 집행하겠습니다.
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].name
   limit: do 40 znaków
   EN: Enforcing Collections.
   PL: Enforcing Collections.
730. [Umiejętność wroga [9014203] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 5 당, 합 위력 +1 (최대 2)\n[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 수치당 피해량 +10%. (최대 100%)\n[EndSkill] 자신의 [Vibration] 횟수 전부 소모
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Clash Power +1 for every 5 [Vibration] Count on self (max 2)\n[WhenUse] At 5+ [Vibration] Count, deal +10% damage for every [Vibration] Count. (max 100%)\n[EndSkill] Consume all [Vibration] Count on self
   PL: [WhenUse] Moc Starcia +1 za każde 5 Liczników [Vibration] na sobie (maks. 2)\n[WhenUse] przy 5+ Licznikach [Vibration], zadaje +10% obrażeń za każdy Licznik [Vibration]. (maks. 100%)\n[EndSkill] zużywa wszystkie Liczniki [Vibration] na sobie
731. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +2 [Vibration] Count next turn
   PL: [OnSucceedAttack] zyskuje +2 Licznika [Vibration] w następnej turze
732. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration]이 8이상이면, [InterlockingTime_Re] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [InterlockingTime_Re]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [InterlockingTime_Re] = 맞물리는 시간 / Interlocking Time
   EN: [OnSucceedAttack] If target has 8+ [Vibration], inflict 1 [InterlockingTime_Re]
   PL: [OnSucceedAttack] jeżeli cel ma 8+ [Vibration], nakłada 1 [InterlockingTime_Re]
733. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 4 이상이면, [Vibration] 8 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 731 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 4이상이면, [InterlockingTime_Re] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [InterlockingTime_Re]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [InterlockingTime_Re] = 맞물리는 시간 / Interlocking Time
   EN: [OnSucceedAttack] If target has 4+ [Vibration] Count, inflict 1 [InterlockingTime_Re]
   PL: [OnSucceedAttack] jeżeli cel ma 4+ Liczników [Vibration], nakłada 1 [InterlockingTime_Re]
736. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 4 이상이면, [Vibration] 횟수 5 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 4+ [Vibration] Count, inflict 5 [Vibration] Count
   PL: [OnSucceedAttack] przy 4+ Licznikach [Vibration], zwiększa własny Licznik [Vibration] o 5
737. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 7이상이면, [InterlockingTime_Re] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [InterlockingTime_Re]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [InterlockingTime_Re] = 맞물리는 시간 / Interlocking Time
   EN: [OnSucceedAttack] At 7+ [Vibration] Count, inflict 1 [InterlockingTime_Re]
   PL: [OnSucceedAttack] przy 7+ Licznikach [Vibration], nakłada 1 [InterlockingTime_Re]
738. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion]
739. [Umiejętność wroga [9014203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 4이상이면, [VibrationChain]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationChain], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationChain] = 진동 - 사슬 / Tremor - Chain; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] At 4+ [Vibration] Count, trigger [Switch_Vibration] into [VibrationChain]
   PL: [OnSucceedAttack] przy 4+ Licznikach [Vibration], uruchamia [Switch_Vibration] w [VibrationChain]
740. [Umiejętność wroga [9014204] (ulepszenie 1) — nazwa] 시간 대여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014204].levelList[level=1].name
   limit: do 40 znaków
   EN: Borrow Time
   PL: Wypożyczony Czas
741. [Umiejętność wroga [9014204] (ulepszenie 1) — opis] [StartBattle] [Vibration] 횟수를 5 소모하여, 자신의 [TimeRentalTwo] 횟수 3 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vibration], [TimeRentalTwo]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor; [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: [StartBattle] Consume 5 [Vibration] Count and gain +3 [TimeRentalTwo] Count
   PL: [StartBattle] zużywa 5 Liczników [Vibration] i zyskuje +3 Licznika [TimeRentalTwo]
742. [Umiejętność wroga [9014301] (ulepszenie 1) — nazwa] 징수 준비
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014301].levelList[level=1].name
   limit: do 40 znaków
   EN: Prepare To Collect
   PL: Przygotowanie do Zbierania
743. [Umiejętność wroga [9014301] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014301].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność wroga [9014301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 이상이면, [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [Vibration] Count, inflict 3 [Vibration]
   PL: [OnSucceedAttack] przy 3+ Licznikach [Vibration], nakłada 3 [Vibration]
745. [Umiejętność wroga [9014301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +1 [Vibration] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Vibration] o 1
746. [Umiejętność wroga [9014302] (ulepszenie 1) — nazwa] T사제 가속 절단기
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].name
   limit: do 50 znaków
   EN: T Corp. Accelerated Amputator
   PL: Przyspieszony Amputator Korporacji T
747. [Umiejętność wroga [9014302] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Umiejętność wroga [9014302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
749. [Umiejętność wroga [9014302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [Vibration] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict 2 [Vibration]
   PL: nakłada 2 [Vibration]
750. [Umiejętność wroga [9014302] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 726 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [9014302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność wroga [9014302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność wroga [9014303] (ulepszenie 1) — nazwa] 시계 좀 보여주시죠.
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014303].levelList[level=1].name
   limit: do 40 znaków
   EN: Your Timepiece, If You Will.
   PL: Your Timepiece, If You Will.
754. [Umiejętność wroga [9014303] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WinDuel] 자신의 [Vibration] 횟수 3을 소모하여, 자신의 [TimeRentalTwo] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014303].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [WinDuel], [TimeRentalTwo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: [WhenUse] At 5+ [Vibration] Count, Clash Power +1\n[WhenUse] Gain +2 [Vibration] Count\n[WinDuel] Consume 3 [Vibration] Count on self and gain +1 [TimeRentalTwo] Count
   PL: [WhenUse] przy 5+ Licznikach [Vibration], Moc Starcia +1\n[WhenUse] zyskuje +2 Licznika [Vibration]\n[WinDuel] zużywa 3 Liczniki [Vibration] na sobie i zyskuje +1 Licznika [TimeRentalTwo]
755. [Umiejętność wroga [9014303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable] w następnej turze
756. [Umiejętność wroga [9014303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Attack Power Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spadku Mocy Ataku
757. [Umiejętność wroga [9014303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 5 이상이면, [VibrationChain]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationChain], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationChain] = 진동 - 사슬 / Tremor - Chain; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] At 5+ [Vibration] Count, trigger [Switch_Vibration] into [VibrationChain]
   PL: [OnSucceedAttack] przy 5+ Licznikach [Vibration], uruchamia [Switch_Vibration] w [VibrationChain]
758. [Umiejętność wroga [9014304] (ulepszenie 1) — nazwa] 강제 징수 집행하겠습니다.
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].name
   (powtórzenie elementu 729 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Umiejętność wroga [9014304] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n[WhenUse] [Vibration] 횟수 4 당 기본 위력 +1 (최대 3)\n[WinDuel] 자신의 [Vibration] 횟수 5를 소모하여, 자신의 [TimeRentalTwo] 횟수 3 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [WinDuel], [TimeRentalTwo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: [WhenUse] Gain +3 [Vibration] Count\n[WhenUse] Base Power +1 for every 4 [Vibration] Count on self (max 3)\n[WinDuel] Consume 5 [Vibration] Count on self and gain +3 [TimeRentalTwo] Count
   PL: [WhenUse] zyskuje +3 Licznika [Vibration]\n[WhenUse] Moc Bazowa +1 za każde 4 Liczniki [Vibration] na sobie (maks. 3)\n[WinDuel] zużywa 5 Liczników [Vibration] na sobie i zyskuje +3 Licznika [TimeRentalTwo]
760. [Umiejętność wroga [9014304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1을 소모하여, 취약 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume 1 [Vibration] Count on self to inflict 1 Fragile
   PL: [OnSucceedAttack] zużywa 1 Licznik [Vibration] na sobie, by nałożyć 1 Wrażliwości
761. [Umiejętność wroga [9014304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1을 소모하여, [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume 1 [Vibration] Count on self to inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] zużywa 1 Licznik [Vibration] na sobie, by zyskać +3 Licznika [Vibration]
762. [Umiejętność wroga [9014304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1을 소모하여, [Vibration] 8 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume 1 [Vibration] Count on self to inflict 8 [Vibration]
   PL: [OnSucceedAttack] zużywa 1 Licznik [Vibration] na sobie, by nałożyć 8 [Vibration]
763. [Umiejętność wroga [9014304] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 2 소모하여, [VibrationExplosion] 후 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Consume 2 [Vibration] Count on self to trigger [VibrationExplosion]; then, reuse this Coin (1 time max)
   PL: [OnSucceedAttack] zużywa 2 Liczniki [Vibration] na sobie, by uruchomić [VibrationExplosion], po czym ponownie używa tej monety (maks. 1 raz)
764. [Umiejętność wroga [9014304] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 5 소모하여, [TimeAccumulation] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014304].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [TimeAccumulation]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [TimeAccumulation] = 시간 누진 / Time Delay
   EN: [OnSucceedAttack] Consume 5 [Vibration] Count on self to inflict 2 [TimeAccumulation]
   PL: [OnSucceedAttack] zużywa 5 Liczników [Vibration] na sobie, by nałożyć 2 [TimeAccumulation]
765. [Umiejętność wroga [9014305] (ulepszenie 1) — nazwa] 시간 대여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014305].levelList[level=1].name
   (powtórzenie elementu 740 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność wroga [9014305] (ulepszenie 1) — opis] [StartBattle] [Vibration] 횟수 4를 소모하여, 자신의 [TimeRentalTwo] 횟수 3 증가\n[StartBattle] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014305].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Vibration], [TimeRentalTwo]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor; [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: [StartBattle] Consume 4 [Vibration] Count and gain +3 [TimeRentalTwo] Count\n[StartBattle] Gain +2 [Vibration] Count
   PL: [StartBattle] zużywa 4 Liczniki [Vibration] i zyskuje +3 Licznika [TimeRentalTwo]\n[StartBattle] zyskuje +2 Licznika [Vibration]
767. [Umiejętność wroga [9014401] (ulepszenie 1) — nazwa] 징수 준비
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014401].levelList[level=1].name
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Umiejętność wroga [9014401] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014401].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [9014401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 이상이면, [Vibration] 3 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [9014401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 745 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Umiejętność wroga [9014402] (ulepszenie 1) — nazwa] T사제 시간 포박기
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014402].levelList[level=1].name
   limit: do 40 znaków
   EN: T Corp. Time Snare
   PL: T Corp. Time Snare
772. [Umiejętność wroga [9014402] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014402].levelList[level=1].desc
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność wroga [9014402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 소모하여, 다음 턴에 [Paralysis] 2 부여. [Vibration] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Consume 1 [Vibration] Count on self to inflict 2 [Paralysis] next turn. Inflict 2 [Vibration]
   PL: [OnSucceedAttack] zużywa 1 Licznik [Vibration] na sobie, by nałożyć 2 [Paralysis] w następnej turze. nakłada 2 [Vibration]
774. [Umiejętność wroga [9014402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 726 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność wroga [9014402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 소모하여, 다음 턴에 [Paralysis] 2 부여. [Vibration] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [9014403] (ulepszenie 1) — nazwa] 그대로 멈춰주시죠.
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014403].levelList[level=1].name
   limit: do 40 znaków
   EN: Stand Still.
   PL: Stand Still.
777. [Umiejętność wroga [9014403] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WinDuel] 자신의 [Vibration] 횟수 3을 소모하여, 자신의 [TimeRentalTwo] 횟수 1 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014403].levelList[level=1].desc
   (powtórzenie elementu 754 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [9014403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 소모하여, 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume 2 [Vibration] Count on self to inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] zużywa 2 Liczniki [Vibration] na sobie, by nałożyć 2 [Binding] w następnej turze
779. [Umiejętność wroga [9014403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 소모하여, 다음 턴에 [ParryingResultDown] 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [ParryingResultDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [ParryingResultDown] = 합 위력 감소 / Clash Power Down
   EN: [OnSucceedAttack] Consume 2 [Vibration] Count on self to inflict 2 [ParryingResultDown] next turn
   PL: [OnSucceedAttack] zużywa 2 Liczniki [Vibration] na sobie, by nałożyć 1 [ParryingResultDown] w następnej turze
780. [Umiejętność wroga [9014404] (ulepszenie 1) — nazwa] 강제 징수 집행하겠습니다.
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].name
   (powtórzenie elementu 729 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [9014404] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n[WhenUse] [Vibration] 횟수 4 당 기본 위력 +1 (최대 3)\n[WinDuel] 자신의 [Vibration] 횟수 5를 소모하여, 자신의 [TimeRentalTwo] 횟수 3 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].desc
   (powtórzenie elementu 759 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Umiejętność wroga [9014404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1을 소모하여, 취약 1 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [9014404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1을 소모하여, [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [9014404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1을 소모하여, [Vibration] 8 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [9014404] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 2 소모하여, [VibrationExplosion] 후 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [9014404] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 5 소모하여, [TimeAccumulation] 2 부여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014404].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [9014405] (ulepszenie 1) — nazwa] 시간 대여
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014405].levelList[level=1].name
   (powtórzenie elementu 740 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [9014405] (ulepszenie 1) — opis] [StartBattle] [Vibration] 횟수 4를 소모하여, 자신의 [TimeRentalTwo] 횟수 3 증가\n[StartBattle] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-tkt.json :: dataList[id=9014405].levelList[level=1].desc
   (powtórzenie elementu 766 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [tkt] Pasywka wroga: Passives_Abnormality-tkt
- plik gry: `Passives_Abnormality-tkt.json`

789. [[tkt] Pasywka wroga [827701] — nazwa] 구제한 시간
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827701].name
   limit: do 40 znaków
   EN: Rescued Time
   PL: Rescued Time
790. [[tkt] Pasywka wroga [827701] — opis] 전투 시작 시 [LimitedTime] 1000을 보유함
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LimitedTime]
   znaczenie tagów: [LimitedTime] = 빼앗은 시간 / Stolen Time
   EN: Have 1000 [LimitedTime] at the start of the Encounter
   PL: na początku walki posiada 1000 [LimitedTime]
791. [[tkt] Pasywka wroga [827702] — nazwa] 가속 재생 수복
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827702].name
   limit: do 40 znaków
   EN: Accelerated Regeneration
   PL: Accelerated Regeneration
792. [[tkt] Pasywka wroga [827702] — opis] 턴 종료 시 부위 파괴 상태면, 해당 부위가 보유한 시간을 100을 소모하여 다음 턴에 부위 파괴 상태를 해제함.
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827702].desc
   limit: do 140 znaków
   EN: Turn End: If a Part is broken, spend 100 Time from that Part to recover from Part Broken state next turn.
   PL: na koniec tury, jeżeli Część jest zniszczona, zużywa 100 Czasu z tej Części, by w następnej turze wyjść ze stanu zniszczonej Części.
793. [[tkt] Pasywka wroga [827801] — nazwa] 모두의 시간
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827801].name
   limit: do 40 znaków
   EN: Everyone's Time
   PL: Everyone's Time
794. [[tkt] Pasywka wroga [827801] — opis] 체력이 75%가 되면 2페이즈로 전환함. 페이즈 전환 시 정신력을 30까지 회복하고, [LimitedTime]을 모든 부위가 [OwnTime]으로 나눠서 보유함.
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827801].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [LimitedTime], [OwnTime]
   znaczenie tagów: [LimitedTime] = 빼앗은 시간 / Stolen Time; [OwnTime] = 분담 시간 / Shared Time
   EN: At 75% HP, enter the second phase. Upon phase change, recover SP up to 30, and divide the [LimitedTime] between all Parts as [OwnTime].
   PL: przy 75% HP przechodzi do drugiej fazy. przy zmianie fazy przywraca Poczytalność do 30, a [LimitedTime] zostaje podzielone między wszystkie Części jako [OwnTime].
795. [[tkt] Pasywka wroga [827802] — nazwa] 공평한 지출
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827802].name
   limit: do 40 znaków
   EN: Equal Expense
   PL: Equal Expense
796. [[tkt] Pasywka wroga [827802] — opis] 매 턴마다 [EquitableDistribution]를 얻음.
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EquitableDistribution]
   znaczenie tagów: [EquitableDistribution] = 시간 공동 분담 지출 / Joint Time Expenditure
   EN: Turn End: gain [EquitableDistribution].
   PL: na koniec tury: zyskuje [EquitableDistribution].
797. [[tkt] Pasywka wroga [827803] — nazwa] 시간 공동체를 위해
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827803].name
   limit: do 40 znaków
   EN: For the Time Community
   PL: For the Time Community
798. [[tkt] Pasywka wroga [827803] — opis] 턴 시작 시 모든 부위가 [Protection] 5를 얻음.
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Turn Start: All Parts gain 5 [Protection].
   PL: na początku tury wszystkie Części zyskują 5 [Protection].
799. [[tkt] Pasywka wroga [827804] — nazwa] 저 놈 시간부터 가져가!
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827804].name
   limit: do 40 znaków
   EN: Take Theirs First!
   PL: Take Theirs First!
800. [[tkt] Pasywka wroga [827804] — opis] 체력이 60% 미만이 되면, [EquitableDistribution]이 [UnfairDistribution]로 변경됨.
   źródło: Passives_Abnormality-tkt.json :: dataList[id=827804].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EquitableDistribution], [UnfairDistribution]
   znaczenie tagów: [EquitableDistribution] = 시간 공동 분담 지출 / Joint Time Expenditure; [UnfairDistribution] = 내부 분열 / Infighting
   EN: At 60%- HP, convert [EquitableDistribution] into [UnfairDistribution].
   PL: przy 60% HP lub mniej, [EquitableDistribution] zamienia się w [UnfairDistribution].

## [tkt] Pasywka wroga: Passives_Enemy-tkt
- plik gry: `Passives_Enemy-tkt.json`

801. [[tkt] Pasywka wroga [9101701] — nazwa] 모두의 성과
   źródło: Passives_Enemy-tkt.json :: dataList[id=9101701].name
   limit: do 40 znaków
   EN: Collective Achievement
   PL: Collective Achievement
802. [[tkt] Pasywka wroga [9101701] — opis] 자신의 공격 혹은 [VibrationExplosion]로 대상이 흐트러짐 상태가 된다면, 모든 아군의 정신력 10 회복
   źródło: Passives_Enemy-tkt.json :: dataList[id=9101701].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: If the target is Staggered by this unit's Attack or [VibrationExplosion], all allies heal 10 SP
   PL: jeżeli cel staje się Oszołamiony od ataku tej jednostki lub [VibrationExplosion], wszyscy sojusznicy przywracają 10 Poczytalności
803. [[tkt] Pasywka wroga [9014201] — nazwa] 시간 긴급 대출
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014201].name
   limit: do 40 znaków
   EN: Emergency Time Loan
   PL: Emergency Time Loan
804. [[tkt] Pasywka wroga [9014201] — opis] 턴 시작 시 흐트러짐 상태라면, [TimeRentalTwo] 횟수 3 얻음.
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TimeRentalTwo]
   znaczenie tagów: [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: Turn Start: If this unit is staggered, gain +3 [TimeRentalTwo] Count.
   PL: na początku tury, jeżeli ta jednostka jest Oszołamiona, zyskuje +3 Licznika [TimeRentalTwo].
805. [[tkt] Pasywka wroga [9014202] — nazwa] 황금 시간 I
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014202].name
   limit: do 40 znaków
   EN: Golden Time I
   PL: Golden Time I
806. [[tkt] Pasywka wroga [9014202] — opis] 턴 종료 시 체력이 16% ~ 20%사이로 남았을 때, 전체 체력의 60%만큼 즉시 회복. 흐트러짐 상태 해제. (최대 1회)
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014202].desc
   limit: do 180 znaków
   EN: At the end of the turn, if the HP is between 16% and 20%, instantly heal up to 60% of Max HP, and recover from stagger. (One time max)
   PL: na koniec tury, jeżeli HP wynosi od 16% do 20%, natychmiast przywraca 60% Maks. HP i dochodzi do siebie z Oszołamienia. (maks. 1 raz)
807. [[tkt] Pasywka wroga [9014203] — nazwa] 시간반동 I
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014203].name
   limit: do 40 znaków
   EN: Time Recoil I
   PL: Time Recoil I
808. [[tkt] Pasywka wroga [9014203] — opis] 황금 시간 발동 이후, 턴 시작 시 [Vulnerable] 2 얻음
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014203].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: After activating Golden Time, gain 2 [Vulnerable] at the next Turn Start
   PL: po uaktywnieniu Golden Time, zyskuje 2 [Vulnerable] na początku następnej tury
809. [[tkt] Pasywka wroga [9014204] — nazwa] 시간 대여 준비
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014204].name
   limit: do 40 znaków
   EN: Ready to Borrow Time
   PL: Ready to Borrow Time
810. [[tkt] Pasywka wroga [9014204] — opis] 턴 시작 시 [TimeRentalTwo]가 없을 때, 자신의 진동 횟수 5 증가
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014204].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TimeRentalTwo]
   znaczenie tagów: [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: Turn Start: If this unit does not have [TimeRentalTwo], gain +5 Tremor Count
   PL: na początku tury, jeżeli ta jednostka nie ma [TimeRentalTwo], zyskuje +5 Licznika Wstrząsu
811. [[tkt] Pasywka wroga [9014301] — nazwa] 황금 시간 II
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014301].name
   limit: do 40 znaków
   EN: Golden Time II
   PL: Golden Time II
812. [[tkt] Pasywka wroga [9014301] — opis] 턴 종료 시 체력이 10% ~ 20%사이로 남았을 때, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제. (최대 1회)
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014301].desc
   limit: do 180 znaków
   EN: At the end of the turn, if the HP is between 10% and 20%, instantly heal up to 80% of Max HP, and recover from stagger. (One time max)
   PL: na koniec tury, jeżeli HP wynosi od 10% do 20%, natychmiast przywraca 80% Maks. HP i dochodzi do siebie z Oszołamienia. (maks. 1 raz)
813. [[tkt] Pasywka wroga [9014302] — nazwa] 시간반동 II
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014302].name
   limit: do 40 znaków
   EN: Time Recoil II
   PL: Time Recoil II
814. [[tkt] Pasywka wroga [9014302] — opis] 황금 시간 발동 이후, 턴 시작 시 [Vulnerable] 3 얻음
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014302].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: After activating Golden Time, gain 3 [Vulnerable] at the next Turn Start
   PL: po uaktywnieniu Golden Time, zyskuje 3 [Vulnerable] na początku następnej tury
815. [[tkt] Pasywka wroga [9014303] — nazwa] 시간 대여
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014303].name
   (powtórzenie elementu 740 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [[tkt] Pasywka wroga [9014303] — opis] 스테이지 시작 시, [TimeRentalTwo] 횟수 4 증가
   źródło: Passives_Enemy-tkt.json :: dataList[id=9014303].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TimeRentalTwo]
   znaczenie tagów: [TimeRentalTwo] = T사의 시간 대여 / T Corp. Borrowed Time
   EN: Encounter Start: Gain +4 [TimeRentalTwo] Count
   PL: na początku walki: zyskuje +4 Licznika [TimeRentalTwo]

## [tkt-re] Umiejętności wrogów / Anomalii — Skills_Abnormality-tkt-re
- grupa rozdziału/trybu: `tkt-re` · plik: `Skills_Abnormality-tkt-re.json`

817. [Umiejętność wroga [122801] (ulepszenie 1) — nazwa] 겁을 먹었나?
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122801].levelList[level=1].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [122801] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +1\n[DefeatDuel] 자신의 체력이 75% 미만이면, [LimitedTime]을 40 소모하여, [Protection] 1 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122801].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [DefeatDuel], [LimitedTime], [Protection]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [DefeatDuel] = [합 패배] / [Clash Lose]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [Protection] = 보호 / Protection
   EN: When in [TimeAcceleration] state, Clash Power +1\n[DefeatDuel] At 75%- HP, consume 40 [LimitedTime] and gain 1 [Protection] (once per turn)
   PL: w stanie [TimeAcceleration], Moc Starcia +1\n[DefeatDuel] przy 75% HP lub mniej, zużywa 40 [LimitedTime] i zyskuje 1 [Protection] (1 raz na turę)
819. [Umiejętność wroga [122801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [122801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Umiejętność wroga [122802] (ulepszenie 1) — nazwa] 시간을 죽인 벌
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122802].levelList[level=1].name
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [122802] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +2\n[WhenUse] [LimitedTime]이 700 이상이면, 대상의 [Laceration] 횟수 3 증가\n[WhenUse] [LimitedTime]이 500 이상이면, 대상의 [Laceration] 횟수 1 증가\n[WhenUse] [LimitedTime]이 400 이상이면, [LimitedTime]을 20 소모하여, 이 스킬에서 부여하는 [Laceration] 위력과 횟수 +1
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122802].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [LimitedTime], [Laceration]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [Laceration] = 출혈 / Bleed
   EN: When in [TimeAcceleration] state, Clash Power +2\n[WhenUse] At 700+ [LimitedTime], inflict +3 [Laceration] Count\n[WhenUse] At 500+ [LimitedTime], inflict +1 [Laceration] Count\n[WhenUse] At 400+ [LimitedTime], consume 20 [LimitedTime] and inflict +1 more [Laceration] Potency and Count with this Skill
   PL: w stanie [TimeAcceleration], Moc Starcia +2\n[WhenUse] przy 700+ [LimitedTime], zwiększa Licznik [Laceration] celu o 3\n[WhenUse] przy 500+ [LimitedTime], zwiększa Licznik [Laceration] celu o 1\n[WhenUse] przy 400+ [LimitedTime], zużywa 20 [LimitedTime] i nakłada o 1 więcej Mocy [Laceration] i Licznika [Laceration] tą Umiejętnością
823. [Umiejętność wroga [122802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [122802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [122802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [122803] (ulepszenie 1) — nazwa] 적출
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].name
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [122803] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 코인 위력 +1\n[WhenUse] 자신의 체력이 75% 미만이면, [LimitedTime]을 40 소모하여, 합 위력 +2\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [LimitedTime], [DefeatDuel]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: When in [TimeAcceleration] state, Coin Power +1\n[WhenUse] At 75%- HP, consume 40 [LimitedTime] and gain Clash Power +2\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: w stanie [TimeAcceleration], Moc Monet +1\n[WhenUse] przy 75% HP lub mniej, zużywa 40 [LimitedTime] i zyskuje Moc Starcia +2\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
828. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration]
832. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Umiejętność wroga [122803] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122803].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [122804] (ulepszenie 1) — nazwa] 난도질
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122804].levelList[level=1].name
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [122804] (ulepszenie 1) — opis] [WhenUse] 자신의 체력이 75%미만이면, [LimitedTime]을 60 소모하여, 합 위력 +2\n[BeforeAttack] [TimeAcceleration] 상태면, 공격 가중치 1 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122804].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [LimitedTime], [BeforeAttack], [TimeAcceleration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [WhenUse] At 75%- HP, consume 60 [LimitedTime] and gain Clash Power +2\n[BeforeAttack] When in [TimeAcceleration] state, gain +1 Atk Weight
   PL: [WhenUse] przy 75% HP lub mniej, zużywa 60 [LimitedTime] i zyskuje Moc Starcia +2\n[BeforeAttack] w stanie [TimeAcceleration], Waga Ataku +1
838. [Umiejętność wroga [122804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [122804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [122804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność wroga [122804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
842. [Umiejętność wroga [122805] (ulepszenie 1) — nazwa] 구원할 시간
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122805].levelList[level=1].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [122805] (ulepszenie 1) — opis] [CantDuel]\n자신에게 공격 스킬을 사용한 대상에게 다음 턴에 [TimeKillerWatch] 부여\n[StartBattle] [LimitedTime] 200 소모. 다음 턴에 [TimeAcceleration]을 얻음
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122805].levelList[level=1].desc
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [122806] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122806].levelList[level=1].name
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [122806] (ulepszenie 1) — opis] [WhenUse] [LimitedTime] 100 당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122806].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [LimitedTime]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LimitedTime] = 빼앗은 시간 / Stolen Time
   EN: [WhenUse] Base Power +1 for every 100 [LimitedTime] (max 3)
   PL: [WhenUse] Moc Bazowa +1 za każde 100 [LimitedTime] (maks. 3)
846. [Umiejętność wroga [122807] (ulepszenie 1) — nazwa] 이런...
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122807].levelList[level=1].name
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność wroga [122807] (ulepszenie 1) — opis] [DefeatDuel] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122807].levelList[level=1].desc
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [122807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność wroga [122807] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122807].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Umiejętność wroga [122808] (ulepszenie 1) — nazwa] 시간이 부족해
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122808].levelList[level=1].name
   (powtórzenie elementu 643 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność wroga [122808] (ulepszenie 1) — opis] [DefeatDuel] [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122808].levelList[level=1].desc
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Umiejętność wroga [122808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Umiejętność wroga [122808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność wroga [122808] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122808].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność wroga [122808] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122808].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność wroga [122901] (ulepszenie 1) — nazwa] 겁을 먹었나?
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122901].levelList[level=1].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność wroga [122901] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +1\n[DefeatDuel] 자신의 체력이 75% 미만이면, [OwnTime]을 40 소모하여, [Protection] 1 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122901].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [DefeatDuel], [OwnTime], [Protection]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [DefeatDuel] = [합 패배] / [Clash Lose]; [OwnTime] = 분담 시간 / Shared Time; [Protection] = 보호 / Protection
   EN: When in [TimeAcceleration] state, Clash Power +1\n[DefeatDuel] At 75%- HP, consume 40 [OwnTime] and gain 1 [Protection] (once per turn)
   PL: w stanie [TimeAcceleration], Moc Starcia +1\n[DefeatDuel] przy 75% HP lub mniej, zużywa 40 [OwnTime] i zyskuje 1 [Protection] (1 raz na turę)
858. [Umiejętność wroga [122901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność wroga [122901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność wroga [122902] (ulepszenie 1) — nazwa] 시간을 죽인 벌
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122902].levelList[level=1].name
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [122902] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 합 위력 +2\n[WhenUse] 모든 부위가 보유한 [OwnTime]의 합이 600 이상이면, 대상의 [Laceration] 횟수 3 증가\n[WhenUse] 모든 부위가 보유한 [OwnTime]의 합이 500 이상이면, 대상의 [Laceration] 횟수 1 증가\n[WhenUse] 모든 부위가 보유한 [OwnTime]의 합이 400 이상이면, [OwnTime]을 20 소모하여, 이 스킬에서 부여하는 [Laceration] 위력과 횟수 +1
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122902].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [OwnTime], [Laceration]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time; [Laceration] = 출혈 / Bleed
   EN: When in [TimeAcceleration] state, Clash Power +2\n[WhenUse] At 600+ (sum of [OwnTime] on all Parts), inflict +3 [Laceration] Count\n[WhenUse] At 500+ (sum of [OwnTime] on all Parts), inflict +1 [Laceration] Count\n[WhenUse] At 400+ (sum of [OwnTime] on all Parts), consume 20 [OwnTime] and inflict +1 more [Laceration] Potency and Count with this Skill
   PL: w stanie [TimeAcceleration], Moc Starcia +2\n[WhenUse] przy 600+ (suma [OwnTime] wszystkich Części), zwiększa Licznik [Laceration] celu o 3\n[WhenUse] przy 500+ (suma [OwnTime] wszystkich Części), zwiększa Licznik [Laceration] celu o 1\n[WhenUse] przy 400+ (suma [OwnTime] wszystkich Części), zużywa 20 [OwnTime] i nakłada o 1 więcej Mocy [Laceration] i Licznika [Laceration] tą Umiejętnością
862. [Umiejętność wroga [122902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność wroga [122902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność wroga [122902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność wroga [122903] (ulepszenie 1) — nazwa] 적출
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].name
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Umiejętność wroga [122903] (ulepszenie 1) — opis] [TimeAcceleration] 상태면, 코인 위력 +1\n[WhenUse] 자신의 체력이 75% 미만이면, [OwnTime]을 40 소모하여, 합 위력 +2\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [TimeAcceleration], [WhenUse], [OwnTime], [DefeatDuel]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration; [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: When in [TimeAcceleration] state, Coin Power +1\n[WhenUse] At 75%- HP, consume 40 [OwnTime] and gain Clash Power +2\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: w stanie [TimeAcceleration], Moc Monet +1\n[WhenUse] przy 75% HP lub mniej, zużywa 40 [OwnTime] i zyskuje Moc Starcia +2\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
867. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Umiejętność wroga [122903] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122903].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Umiejętność wroga [122904] (ulepszenie 1) — nazwa] 난도질
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122904].levelList[level=1].name
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Umiejętność wroga [122904] (ulepszenie 1) — opis] [WhenUse] 자신의 체력이 75%미만이면, [OwnTime]을 60 소모하여, 합 위력 +2\n[BeforeAttack] [TimeAcceleration] 상태면, 공격 가중치 3 증가\n[BeforeAttack] 자신의 체력이 60% 미만이면, [OwnTime]을 10 소모하여, 공격 가중치 1 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122904].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OwnTime], [BeforeAttack], [TimeAcceleration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [WhenUse] At 75%- HP, consume 60 [OwnTime] and gain Clash Power +2\n[BeforeAttack] When in [TimeAcceleration] state, gain +3 Atk Weight\n[BeforeAttack] At 60%- HP, consume 10 [OwnTime] and gain +1 Atk Weight
   PL: [WhenUse] przy 75% HP lub mniej, zużywa 60 [OwnTime] i zyskuje Moc Starcia +2\n[BeforeAttack] w stanie [TimeAcceleration], Waga Ataku +3\n[BeforeAttack] przy 60% HP lub mniej, zużywa 10 [OwnTime] i zyskuje Waga Ataku +1
877. [Umiejętność wroga [122904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność wroga [122904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Umiejętność wroga [122904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Umiejętność wroga [122904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 841 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Umiejętność wroga [122905] (ulepszenie 1) — nazwa] 구원할 시간
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122905].levelList[level=1].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Umiejętność wroga [122905] (ulepszenie 1) — opis] [CantDuel]\n자신에게 공격 스킬을 사용한 대상에게 다음 턴에 [TimeKillerWatch] 부여\n[StartBattle] [OwnTime] 200 소모. 다음 턴에 [TimeAcceleration]을 얻음)
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122905].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [TimeKillerWatch], [StartBattle], [OwnTime], [TimeAcceleration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [TimeKillerWatch] = 시간 구제 대상 / Time Relief Entitlement; [StartBattle] = [전투 시작시] / [Combat Start]; [OwnTime] = 분담 시간 / Shared Time; [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: [CantDuel]\nInflict [TimeKillerWatch] against the target that used an Attack Skill against this unit\n[StartBattle] Consume 200 [OwnTime] and gain [TimeAcceleration] next turn)
   PL: [CantDuel]\nnakłada [TimeKillerWatch] na cel, który użył Umiejętności ataku przeciwko tej jednostce\n[StartBattle] zużywa 200 [OwnTime] i zyskuje [TimeAcceleration] w następnej turze)
883. [Umiejętność wroga [122906] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122906].levelList[level=1].name
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Umiejętność wroga [122906] (ulepszenie 1) — opis] [WhenUse] 모든 부위가 보유한 [OwnTime]의 합 50 당, 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122906].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [OwnTime]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OwnTime] = 분담 시간 / Shared Time
   EN: [WhenUse] Base Power +1 for every 50 sum of [OwnTime] across all Parts (max 3)
   PL: [WhenUse] Moc Bazowa +1 za każde 50 sumy [OwnTime] wszystkich Części (maks. 3)
885. [Umiejętność wroga [122907] (ulepszenie 1) — nazwa] 시간 살인 시간
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122907].levelList[level=1].name
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Umiejętność wroga [122907] (ulepszenie 1) — opis] [CantDuel]\n자신의 속도를 24로 고정함.\n이번 턴동안 흐트러짐 상태가 되지 않음.\n[WhenUse] 모두의 마지막 남은 [OwnTime] 400 획득 후 소모.
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122907].levelList[level=1].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Umiejętność wroga [122907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 시간을 삭제함. 대상의 시간을 삭제시켰다면, 모든 부위가 [OwnTime]을 최대로 회복하고, 다음 턴에 신속, 공격 위력 증가 10을 얻음.
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 625 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność wroga [122908] (ulepszenie 1) — nazwa] 시간이 필요해!
   źródło: Skills_Abnormality-tkt-re.json :: dataList[id=122908].levelList[level=1].name
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [tkt-re] Umiejętności wrogów / Anomalii — Skills_Enemy-tkt-re
- grupa rozdziału/trybu: `tkt-re` · plik: `Skills_Enemy-tkt-re.json`

889. [Umiejętność wroga [9102401] (ulepszenie 1) — nazwa] 양심 없냐?
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102401].levelList[level=1].name
   (powtórzenie elementu 684 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Umiejętność wroga [9102401] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n[WhenUse] At 5+ [Vibration] Count, Clash Power +1
   PL: [WhenUse] zyskuje +2 Licznika [Vibration]\n[WhenUse] przy 5+ Licznikach [Vibration], Moc Starcia +1
891. [Umiejętność wroga [9102401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Umiejętność wroga [9102401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Umiejętność wroga [9102402] (ulepszenie 1) — nazwa] 양심 없구나
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102402].levelList[level=1].name
   (powtórzenie elementu 688 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Umiejętność wroga [9102402] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102402].levelList[level=1].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Umiejętność wroga [9102402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Umiejętność wroga [9102402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Umiejętność wroga [9102403] (ulepszenie 1) — nazwa] 지켜줄 수 있을까?
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102403].levelList[level=1].name
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Umiejętność wroga [9102403] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102403].levelList[level=1].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność wroga [9102403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Umiejętność wroga [9102403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수가 10 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Umiejętność wroga [9102403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 위력이 15 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 15+ [Vibration] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli cel ma 15+ Mocy [Vibration], uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
902. [Umiejętność wroga [9102404] (ulepszenie 1) — nazwa] 그 무기 못쓸걸?
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102404].levelList[level=1].name
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Umiejętność wroga [9102404] (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +1
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n[WhenUse] At 5+ [Vibration] Count, Clash Power +1
   PL: [WhenUse] zyskuje +3 Licznika [Vibration]\n[WhenUse] przy 5+ Licznikach [Vibration], Moc Starcia +1
904. [Umiejętność wroga [9102404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność wroga [9102404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Umiejętność wroga [9102404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność wroga [9102405] (ulepszenie 1) — nazwa] 각오는 되어있겠지?
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].name
   (powtórzenie elementu 702 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność wroga [9102405] (ulepszenie 1) — opis] [VibrationCollapse]가 있는 대상 우선 공격\n[WhenUse] 자신을 제외한 모든 아군에게 자신의 [Vibration] 횟수만큼 [Vibration] 횟수 부여\n[WhenUse] 자신을 포함한 모든 아군의 [Vibration]을 [VibrationDistribution]로 [Switch_Vibration]\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationCollapse], [WhenUse], [Vibration], [VibrationDistribution], [Switch_Vibration], [DefeatDuel]
   znaczenie tagów: [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [VibrationCollapse]\n[WhenUse] Apply [Vibration] Count equal to [Vibration] Count on self to all other allies\n[WhenUse] Trigger [Switch_Vibration] on all allies(including this unit) to convert their [Vibration] to [VibrationDistribution]\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cele z [VibrationCollapse]\n[WhenUse] nakłada Licznik [Vibration] równy Licznikowi [Vibration] na sobie wszystkim pozostałym sojusznikom\n[WhenUse] uruchamia [Switch_Vibration] na wszystkich sojusznikach (łącznie z tą jednostką), zamieniając ich [Vibration] w [VibrationDistribution]\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
909. [Umiejętność wroga [9102405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność wroga [9102405] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Umiejętność wroga [9102405] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność wroga [9102405] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 10 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Vibration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Vibration]
913. [Umiejętność wroga [9102405] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Umiejętność wroga [9102405] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationEcho]으로 [FusionVibration]
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102405].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [9102406] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102406].levelList[level=1].name
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Umiejętność wroga [9102406] (ulepszenie 1) — opis] [StartBattle] 자신의 [Vibration] 횟수 5배만큼 보호막 체력을 얻음 (최대 60)
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102406].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Gain 5 x ([Vibration] Count on self) Shield HP (max 60)
   PL: [StartBattle] zyskuje HP Tarczy równe 5 x (Licznik [Vibration] na sobie) (maks. 60)
917. [Umiejętność wroga [9102407] (ulepszenie 1) — nazwa] 대의를 위한 수거
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].name
   (powtórzenie elementu 708 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Umiejętność wroga [9102407] (ulepszenie 1) — opis] [CantDuel]\n[StartBattle] 자신을 제외한 모든 아군의 [Vibration] 횟수를 자신이 얻고 모든 아군의 [Vibration] 제거\n[StartBattle] 자신의 [Vibration] 횟수 3당 [AttackUp] 1을 얻음\n[WhenUse] 자신의 [Vibration] 횟수 10 증가
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle], [Vibration], [AttackUp], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\n[StartBattle] Draw all other allies' [Vibration] Count to self; [Vibration] on all allies expire\n[StartBattle] Gain 1 [AttackUp] for every 3 [Vibration] Count on self\n[WhenUse] Gain 10 [Vibration] Count
   PL: [CantDuel]\n[StartBattle] przenosi Licznik [Vibration] wszystkich pozostałych sojuszników na siebie; [Vibration] wszystkich sojuszników wygasa\n[StartBattle] zyskuje 1 [AttackUp] za każde 3 Liczniki [Vibration] na sobie\n[WhenUse] zyskuje 10 Liczników [Vibration]
919. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 10 부여
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 704 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수당 20%만큼의 추가 나태 피해량 입힘
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Deal 20% bonus Sloth damage for every [Vibration] Count on self
   PL: [OnSucceedAttack] zadaje dodatkowe 20% obrażeń Lenistwa za każdy Licznik [Vibration] na sobie
921. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 4 증가
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수당 20%만큼의 추가 나태 피해량 입힘
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 920 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 소모하여, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Consume 1 [Vibration] Count on self, and trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] zużywa 1 Licznik [Vibration] na sobie i uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
924. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 소모하여, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 923 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Umiejętność wroga [9102407] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 소모하여, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-tkt-re.json :: dataList[id=9102407].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 923 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [tkt-re] Pasywka wroga: Passives_Abnormality-tkt-re
- plik gry: `Passives_Abnormality-tkt-re.json`

926. [[tkt-re] Pasywka wroga [122801] — nazwa] 정각
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122801].name
   limit: do 40 znaków
   EN: 'O Clock
   PL: 'O Clock
927. [[tkt-re] Pasywka wroga [122801] — opis] 턴 종료 시 자신의 [LimitedTime]이 60으로 나누어 떨어지면, 다음 턴에 [SlashDamageUp] 2, [PenetrateDamageUp] 2을 얻음
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122801].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [LimitedTime], [SlashDamageUp], [PenetrateDamageUp]
   znaczenie tagów: [LimitedTime] = 빼앗은 시간 / Stolen Time; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Turn End: if this unit's [LimitedTime] is evenly divisible by 60, gain 2 [SlashDamageUp] and 2 [PenetrateDamageUp] next turn
   PL: na koniec tury, jeżeli [LimitedTime] tej jednostki dzieli się bez reszty przez 60, zyskuje w następnej turze 2 [SlashDamageUp] i 2 [PenetrateDamageUp]
928. [[tkt-re] Pasywka wroga [122802] — nazwa] 남겨진 시간
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122802].name
   limit: do 40 znaków
   EN: Remaining Time
   PL: Remaining Time
929. [[tkt-re] Pasywka wroga [122802] — opis] 자신이 [TimeAcceleration] 상태라면, 적 적중시 적에게 피해량의 10%만큼 현재 사용 중인 스킬의 죄악 속성의 피해를 추가로 입힘 (턴 당 2회)
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122802].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [TimeAcceleration]
   znaczenie tagów: [TimeAcceleration] = 시간 가속 / Time Acceleration
   EN: If this unit is in [TimeAcceleration] state, deal 10% of the damage it dealt On Hit as bonus damage in the Skill's Sin Affinity (2 times per turn)
   PL: jeżeli ta jednostka jest w stanie [TimeAcceleration], przy trafieniu zadaje dodatkowo 10% zadanych obrażeń w Atrybucie Grzechu użytej Umiejętności (2 razy na turę)
930. [[tkt-re] Pasywka wroga [122901] — nazwa] 정각
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122901].name
   (powtórzenie elementu 926 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [[tkt-re] Pasywka wroga [122901] — opis] 턴 종료 시 자신의 [LimitedTime] 혹은 [OwnTime]의 합이 60으로 나누어 떨어지면, 다음 턴에 [SlashDamageUp] 2, [PenetrateDamageUp] 2을 얻음
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122901].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [LimitedTime], [OwnTime], [SlashDamageUp], [PenetrateDamageUp]
   znaczenie tagów: [LimitedTime] = 빼앗은 시간 / Stolen Time; [OwnTime] = 분담 시간 / Shared Time; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Turn End: if this unit's [LimitedTime], or the sum of [OwnTime] is evenly divisible by 60, gain 2 [SlashDamageUp] and 2 [PenetrateDamageUp] next turn
   PL: na koniec tury, jeżeli suma [LimitedTime] lub [OwnTime] tej jednostki dzieli się bez reszty przez 60, zyskuje w następnej turze 2 [SlashDamageUp] i 2 [PenetrateDamageUp]
932. [[tkt-re] Pasywka wroga [122902] — nazwa] 시간 초가속
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122902].name
   limit: do 40 znaków
   EN: Time Hyperacceleration
   PL: Time Hyperacceleration
933. [[tkt-re] Pasywka wroga [122902] — opis] 자신이 [EquitableDistribution] 상태라면, 적 적중시 적에게 피해량의 10%만큼 현재 사용 중인 스킬의 죄악 속성의 피해를 추가로 입힘 (턴 당 2회)
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=122902].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [EquitableDistribution]
   znaczenie tagów: [EquitableDistribution] = 시간 공동 분담 지출 / Joint Time Expenditure
   EN: If this unit is in [EquitableDistribution] state, deal 10% of the damage it dealt On Hit as bonus damage in the Skill's Sin Affinity (2 times per turn)
   PL: jeżeli ta jednostka jest w stanie [EquitableDistribution], przy trafieniu zadaje dodatkowo 10% zadanych obrażeń w Atrybucie Grzechu użytej Umiejętności (2 razy na turę)
934. [[tkt-re] Pasywka wroga [123001] — nazwa] 시간 초가속
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=123001].name
   (powtórzenie elementu 932 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [[tkt-re] Pasywka wroga [123001] — opis] 턴 종료 시 자신이 살아있다면, 다음 턴에 랜덤한 시간살인마의 한 부위에 [Protection] 1 부여
   źródło: Passives_Abnormality-tkt-re.json :: dataList[id=123001].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Turn End: if this unit is alive, apply 1 [Protection] next turn to a random Part on The Time Ripper.
   PL: na koniec tury, jeżeli ta jednostka żyje, nakłada 1 [Protection] w następnej turze na losową Część The Time Ripper.

## [tkt-re] Pasywka wroga: Passives_Enemy-tkt-re
- plik gry: `Passives_Enemy-tkt-re.json`

936. [[tkt-re] Pasywka wroga [9102401] — nazwa] 모두를 위해
   źródło: Passives_Enemy-tkt-re.json :: dataList[id=9102401].name
   limit: do 40 znaków
   EN: For Everyone
   PL: For Everyone
937. [[tkt-re] Pasywka wroga [9102401] — opis] [VibrationDistribution] 버프 획득 시 살아있는 아군이 없더라도 무조건 1명 있는 취급함\n만약, 살아있는 아군이 없는 상태로 [VibrationDistribution] 효과를 받았다면 다음 턴에 [Vulnerable] 1 얻음
   źródło: Passives_Enemy-tkt-re.json :: dataList[id=9102401].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationDistribution], [Vulnerable]
   znaczenie tagów: [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [Vulnerable] = 취약 / Fragile
   EN: When gaining [VibrationDistribution], even if there are no surviving allies, behave as though there is 1 other surviving ally\nIf this unit gains [VibrationDistribution] while there are no surviving allies, gain 1 [Vulnerable] next turn
   PL: przy zdobywaniu [VibrationDistribution], nawet gdy nie ma żyjących sojuszników, traktuje tak, jakby był 1 inny żyjący sojusznik\njeżeli ta jednostka zyskuje [VibrationDistribution], gdy nie ma żyjących sojuszników, zyskuje 1 [Vulnerable] w następnej turze

## [twth] Wróg / część: Enemies-twth
- plik gry: `Enemies-twth.json`

938. [[twth] Wróg / część [91034] — nazwa] 지령을 좇는 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=91034].name
   limit: do 60 znaków
   EN: Prescript-chasing Proselyte of the Index
   PL: Prescript-chasing Proselyte of the Index
939. [[twth] Wróg / część [91034] — opis] 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=91034].desc
   limit: do 120 znaków
   EN: The Index Proselyte
   PL: Prozelita The Index
940. [[twth] Wróg / część [91035] — nazwa] 지령을 따르는 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=91035].name
   limit: do 60 znaków
   EN: Prescript-conforming Proselyte of the Index
   PL: Prescript-conforming Proselyte of the Index
941. [[twth] Wróg / część [91035] — opis] 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=91035].desc
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [[twth] Wróg / część [91043] — nazwa] 충동적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91043].name
   limit: do 60 znaków
   EN: Impulsive Fauvist Student of the Ring
   PL: Impulsive Fauvist Student of the Ring
943. [[twth] Wróg / część [91043] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91043].desc
   limit: do 120 znaków
   EN: Fauvist Student
   PL: Fowistyczny Student
944. [[twth] Wróg / część [91044] — nazwa] 본능적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91044].name
   limit: do 60 znaków
   EN: Instinctive Fauvist Student of the Ring
   PL: Instinctive Fauvist Student of the Ring
945. [[twth] Wróg / część [91044] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91044].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [[twth] Wróg / część [91045] — nazwa] 야성적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91045].name
   limit: do 50 znaków
   EN: Feral Fauvist Student of the Ring
   PL: Feral Fauvist Student of the Ring
947. [[twth] Wróg / część [91045] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91045].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [[twth] Wróg / część [91046] — nazwa] 즉흥적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91046].name
   limit: do 60 znaków
   EN: Spontaneous Fauvist Student of the Ring
   PL: Spontaneous Fauvist Student of the Ring
949. [[twth] Wróg / część [91046] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=91046].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
950. [[twth] Wróg / część [1413] — nazwa] 충동적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1413].name
   (powtórzenie elementu 942 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [[twth] Wróg / część [1413] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1413].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [[twth] Wróg / część [141301] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=141301].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [[twth] Wróg / część [141301] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=141301].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [[twth] Wróg / część [1414] — nazwa] 본능적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1414].name
   (powtórzenie elementu 944 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [[twth] Wróg / część [1414] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1414].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [[twth] Wróg / część [141401] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=141401].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [[twth] Wróg / część [141401] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=141401].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [[twth] Wróg / część [1415] — nazwa] 야성적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1415].name
   (powtórzenie elementu 946 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [[twth] Wróg / część [1415] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1415].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [[twth] Wróg / część [141501] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=141501].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [[twth] Wróg / część [141501] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=141501].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [[twth] Wróg / część [1416] — nazwa] 즉흥적인 약지 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1416].name
   (powtórzenie elementu 948 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [[twth] Wróg / część [1416] — opis] 야수파 스튜던트
   źródło: Enemies-twth.json :: dataList[id=1416].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [[twth] Wróg / część [141601] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=141601].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [[twth] Wróg / część [141601] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=141601].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [[twth] Wróg / część [1422] — nazwa] 루포
   źródło: Enemies-twth.json :: dataList[id=1422].name
   limit: do 40 znaków
   EN: Rufo
   PL: Rufo
967. [[twth] Wróg / część [1422] — opis] 야수파 도슨트
   źródło: Enemies-twth.json :: dataList[id=1422].desc
   limit: do 120 znaków
   EN: Fauvist Docent
   PL: Fauvist Docent
968. [[twth] Wróg / część [142201] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=142201].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [[twth] Wróg / część [142201] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=142201].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [[twth] Wróg / część [1423] — nazwa] 루포
   źródło: Enemies-twth.json :: dataList[id=1423].name
   (powtórzenie elementu 966 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [[twth] Wróg / część [1423] — opis] 야수파 도슨트
   źródło: Enemies-twth.json :: dataList[id=1423].desc
   (powtórzenie elementu 967 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [[twth] Wróg / część [142301] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=142301].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [[twth] Wróg / część [142301] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=142301].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [[twth] Wróg / część [1428] — nazwa] 지령을 좇는 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=1428].name
   (powtórzenie elementu 938 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [[twth] Wróg / część [1428] — opis] 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=1428].desc
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [[twth] Wróg / część [142801] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=142801].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [[twth] Wróg / część [142801] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=142801].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [[twth] Wróg / część [1429] — nazwa] 지령을 따르는 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=1429].name
   (powtórzenie elementu 940 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [[twth] Wróg / część [1429] — opis] 검지 수행자
   źródło: Enemies-twth.json :: dataList[id=1429].desc
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [[twth] Wróg / część [142901] — nazwa] 몸통
   źródło: Enemies-twth.json :: dataList[id=142901].name
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [[twth] Wróg / część [142901] — opis] 부위
   źródło: Enemies-twth.json :: dataList[id=142901].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [twth] Umiejętności wrogów / Anomalii — Skills_Abnormality-twth
- grupa rozdziału/trybu: `twth` · plik: `Skills_Abnormality-twth.json`

982. [Umiejętność wroga [142201] (ulepszenie 1) — nazwa] 원색 표현
   źródło: Skills_Abnormality-twth.json :: dataList[id=142201].levelList[level=1].name
   limit: do 40 znaków
   EN: Expression of Primary Colors
   PL: Wyraz Barw Podstawowych
983. [Umiejętność wroga [142201] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-twth.json :: dataList[id=142201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Sinking]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: Final Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)
   PL: Moc Końcowa +1 za każde 6 (suma [Laceration] + [Sinking]) na celu (maks. 2)
984. [Umiejętność wroga [142201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Umiejętność wroga [142201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [EagleClawWound] 1 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EagleClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [OnSucceedAttack] Inflict 1 [EagleClawWound]
   PL: [OnSucceedAttack] nakłada 1 [EagleClawWound]
986. [Umiejętność wroga [142201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 [Sinking]
987. [Umiejętność wroga [142201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [EagleClawWound] 1 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 985 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Umiejętność wroga [142202] (ulepszenie 1) — nazwa] 강렬한 덧칠
   źródło: Skills_Abnormality-twth.json :: dataList[id=142202].levelList[level=1].name
   limit: do 40 znaków
   EN: Vehement Overpainting
   PL: Gwałtowne Przemalowanie
989. [Umiejętność wroga [142202] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-twth.json :: dataList[id=142202].levelList[level=1].desc
   (powtórzenie elementu 983 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Umiejętność wroga [142202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]
991. [Umiejętność wroga [142202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BearClawWound] 1 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BearClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [OnSucceedAttack] Inflict 1 [BearClawWound]
   PL: [OnSucceedAttack] nakłada 1 [BearClawWound]
992. [Umiejętność wroga [142202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Umiejętność wroga [142202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BearClawWound] 1 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 991 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [Umiejętność wroga [142203] (ulepszenie 1) — nazwa] 야수파 - 원초적 전개
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].name
   limit: do 50 znaków
   EN: Le Fauvisme - Déchaînement Primal
   PL: Le Fauvisme - Déchaînement Primal
995. [Umiejętność wroga [142203] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Sinking]의 합 6당, 최종 위력 +1 (최대 3)\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Sinking], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 3)\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL: Moc Końcowa +1 za każde 6 (suma [Laceration] + [Sinking]) na celu (maks. 3)\n[DefeatDuel]\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- przy trafieniu nie aktywuje efektów [Sinking] celu
996. [Umiejętność wroga [142203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Umiejętność wroga [142203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BearClawWound] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BearClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [OnSucceedAttack] Inflict 2 [BearClawWound]
   PL: [OnSucceedAttack] nakłada 2 [BearClawWound]
998. [Umiejętność wroga [142203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 [Sinking] i zwiększa Licznik [Sinking] o 2
999. [Umiejętność wroga [142203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EagleClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [OnSucceedAttack] Inflict 2 [EagleClawWound]
   PL: [OnSucceedAttack] nakłada 2 [EagleClawWound]
1000. [Umiejętność wroga [142203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1001. [Umiejętność wroga [142203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[BoldBrushstrokes] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=142203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [BoldBrushstrokes]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoldBrushstrokes] = 과감한 터치 / Touche Hardie
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 1 [BoldBrushstrokes]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 1 [BoldBrushstrokes]</u></b></mark></color>
1002. [Umiejętność wroga [142204] (ulepszenie 1) — nazwa] 크리틱
   źródło: Skills_Abnormality-twth.json :: dataList[id=142204].levelList[level=1].name
   limit: do 40 znaków
   EN: Critique
   PL: Krytyka
1003. [Umiejętność wroga [142204] (ulepszenie 1) — opis] [CantChangeTarget]\n[WhenUse]\n- 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 합 위력 +2 (최대 12)\n- 대상에게 <color=#ff6000><mark=#ff000040><b><u>[IntenseColors]가 있으면,</u></b></mark></color> 합 위력 +6, 피해량 +100%\n· 대상이 [IntenseColors]를 보유한 상태에서 <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착했으면,</u></b></mark></color> 대신 합 위력 +6, 피해량 -90%\n[DefeatDuel]\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142204].levelList[level=1].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [WhenUse], [IntenseColors], [DefeatDuel], [Sinking]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [IntenseColors] = 강렬한 색채 / Palette Vibrante; [DefeatDuel] = [합 패배] / [Clash Lose]; [Sinking] = 침잠 / Sinking
   EN: [CantChangeTarget]\n[WhenUse]\n- Clash Power +2 <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on target (max 12)\n- <color=#ff6000><mark=#ff000040><b><u>If target has [IntenseColors], </u></b></mark></color>Clash Power +6 and deal +100% damage\n· <color=#ff6000><mark=#ff000040><b><u>If target has equipped Defense Skills</u></b></mark></color> while having [IntenseColors], Clash Power +6 and deal -90% damage instead\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL: [CantChangeTarget]\n[WhenUse]\n- Moc Starcia +2 <color=#ff6000><mark=#ff000040><b><u>za każdy rodzaj negatywnego efektu</u></b></mark></color> na celu (maks. 12)\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [IntenseColors], </u></b></mark></color>Moc Starcia +6 i zadaje +100% obrażeń\n· <color=#ff6000><mark=#ff000040><b><u>jeżeli cel wyposażył Umiejętności obronne</u></b></mark></color> mając [IntenseColors], zamiast tego Moc Starcia +6 i zadaje -90% obrażeń\n[DefeatDuel]\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- przy trafieniu nie aktywuje efektów [Sinking] celu
1004. [Umiejętność wroga [142204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Umiejętność wroga [142204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이 코인 재사용 (최대 2회)\n- 합 패배 후 적중 시, 대신 이 코인 재사용 (최대 1회)\n- 대상이 수비 스킬 장착 시, 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Reuse this Coin (max 2 times)\n- On Hit after losing a Clash, Reuse this Coin (max once instead)\n- Does not trigger if target has equipped Defense Skills
   PL: [OnSucceedAttack] ponownie używa tej monety (maks. 2 razy)\n- przy trafieniu po przegranej Starcia, zamiast tego ponownie używa tej monety (maks. 1 raz)\n- nie aktywuje się jeżeli cel wyposażył Umiejętności obronne
1006. [Umiejętność wroga [142204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [Umiejętność wroga [142204] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142204].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 998 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Umiejętność wroga [142301] (ulepszenie 1) — nazwa] 원색 처리
   źródło: Skills_Abnormality-twth.json :: dataList[id=142301].levelList[level=1].name
   limit: do 50 znaków
   EN: Embellish with Primary Colors
   PL: Embellish with Primary Colors
1009. [Umiejętność wroga [142301] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142301].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Sinking], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)\n[DefeatDuel]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL: Moc Końcowa +1 za każde 6 (suma [Laceration] + [Sinking]) na celu (maks. 2)\n[DefeatDuel]\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- przy trafieniu nie aktywuje efektów [Sinking] celu
1010. [Umiejętność wroga [142301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration]
1011. [Umiejętność wroga [142301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 999 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1012. [Umiejętność wroga [142301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1013. [Umiejętność wroga [142301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [EagleClawWound] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 999 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1014. [Umiejętność wroga [142302] (ulepszenie 1) — nazwa] 격렬한 덧칠
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].name
   limit: do 40 znaków
   EN: Impassioned Overpainting
   PL: Impassioned Overpainting
1015. [Umiejętność wroga [142302] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Sinking]의 합 6당, 최종 위력 +1 (최대 3)\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].desc
   (powtórzenie elementu 995 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1016. [Umiejętność wroga [142302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking]
1017. [Umiejętność wroga [142302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BearClawWound] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 997 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1018. [Umiejętność wroga [142302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Umiejętność wroga [142302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Umiejętność wroga [142302] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BearClawWound] 2 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142302].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 997 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Umiejętność wroga [142303] (ulepszenie 1) — nazwa] 야수파 - 포악한 전개
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].name
   limit: do 50 znaków
   EN: Le Fauvisme - Déchaînement Brutal
   PL: Fowizm - Wybuchowa Furia
1022. [Umiejętność wroga [142303] (ulepszenie 1) — opis] 대상의 [Laceration]과 [Sinking]의 합 6당, 최종 위력 +1 (최대 4)\n[WhenUse] 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 수가 3개 이상이면,</u></b></mark></color> 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel]\n- 피해량 -75%\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Laceration], [Sinking], [WhenUse], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 4)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If target has 3+ types of negative effect,</u></b></mark></color> convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel]\n- Deal -75% damage\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL: Moc Końcowa +1 za każde 6 (suma [Laceration] + [Sinking]) na celu (maks. 4)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma 3+ rodzaje negatywnych efektów,</u></b></mark></color> wszystkie monety tej Umiejętności zmieniają się w [SuperCoin]y\n[DefeatDuel]\n- zadaje o 75% mniej obrażeń\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- przy trafieniu nie aktywuje efektów [Sinking] celu
1023. [Umiejętność wroga [142303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [Umiejętność wroga [142303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BearClawWound] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BearClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [OnSucceedAttack] Inflict 3 [BearClawWound]
   PL: [OnSucceedAttack] nakłada 3 [BearClawWound]
1025. [Umiejętność wroga [142303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
1026. [Umiejętność wroga [142303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [EagleClawWound] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EagleClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [OnSucceedAttack] Inflict 3 [EagleClawWound]
   PL: [OnSucceedAttack] nakłada 3 [EagleClawWound]
1027. [Umiejętność wroga [142303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [Umiejętność wroga [142303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[BoldBrushstrokes] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=142303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1001 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Umiejętność wroga [142304] (ulepszenie 1) — nazwa] 영감의 전율
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].name
   limit: do 40 znaków
   EN: The Thrill of Inspiration
   PL: The Thrill of Inspiration
1030. [Umiejętność wroga [142304] (ulepszenie 1) — opis] 속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 최종 위력 +1, 피해량 +10% (각각 최대 6, 60%)\n[WinDuel]\n- 각 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 피해량 +10% (최대 60%, 대상 별로 판정)\n[DefeatDuel]\n- 피해량 -75%\n- 이 스킬의 효과로 부여하는 [BearClawWound], [EagleClawWound] 수치가 1/3으로 감소 (소수점 올림)\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [WinDuel], [DefeatDuel], [BearClawWound], [EagleClawWound], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]; [Sinking] = 침잠 / Sinking
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse] Final Power +1 and deal +10% damage <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on the main target (max 6 and 60% respectively)\n[WinDuel]\n- Deal +10% damage <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on each target (max 60% against each target)\n[DefeatDuel]\n- Deal -75% damage\n- Inflict 2/3 less Stacks of [BearClawWound] and [EagleClawWound] with this Skill's effect (rounded up)\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target
   PL: może przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] Moc Końcowa +1 i zadaje +10% obrażeń <color=#ff6000><mark=#ff000040><b><u>za każdy rodzaj negatywnego efektu</u></b></mark></color> na głównym celu (maks. odpowiednio 6 i 60%)\n[WinDuel]\n- zadaje +10% obrażeń <color=#ff6000><mark=#ff000040><b><u>za każdy rodzaj negatywnego efektu</u></b></mark></color> na każdym celu (maks. 60% na cel)\n[DefeatDuel]\n- zadaje o 75% mniej obrażeń\n- efekty tej Umiejętności nakładają o 1/3 mniej Stosów [BearClawWound] i [EagleClawWound] (zaokrąglone w górę)\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- przy trafieniu nie aktywuje efektów [Sinking] celu
1031. [Umiejętność wroga [142304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1032. [Umiejętność wroga [142304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration] and +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration] i zwiększa Licznik [Laceration] o 3
1033. [Umiejętność wroga [142304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking] and +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking] i 3 Licznika [Sinking]
1034. [Umiejętność wroga [142304] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[BearClawWound] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [BearClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWound] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 9 [BearClawWound]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 9 [BearClawWound]</u></b></mark></color>
1035. [Umiejętność wroga [142304] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[EagleClawWound] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [EagleClawWound]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EagleClawWound] = 찢긴 색채 [블뢰] / Mauled Color [Bleu]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 9 [EagleClawWound]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 9 [EagleClawWound]</u></b></mark></color>
1036. [Umiejętność wroga [142304] (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[BoldBrushstrokes] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-twth.json :: dataList[id=142304].levelList[level=1].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 1001 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Umiejętność wroga [142305] (ulepszenie 1) — nazwa] 당신의 피부 아래 맥동하는 붉은 색감을 거칠게.
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].name
   limit: do 70 znaków
   EN: Burst Forth the Pulsing Crimson under Your Skin.
   PL: Burst Forth the Pulsing Crimson under Your Skin.
1038. [Umiejętność wroga [142305] (ulepszenie 1) — opis] [WideAreaRampage]\n[IntenseColors]를 보유한 대상을 우선으로 지정\n대상의 수비 스킬을 발동시키지 않음 (합 가능 수비 제외)\n속도와 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 최종 위력 +1 (최대 6)\n- 메인 타겟에게 <color=#ff6000><mark=#ff000040><b><u>[IntenseColors]가 있으면,</u></b></mark></color> 합 위력 +6\n- 대상에게 <color=#ff6000><mark=#ff000040><b><u>[IntenseColors]가 있으면,</u></b></mark></color> 피해량 +100%\n(대상 별로 판정)\n· 타겟 중 [IntenseColors]를 보유한 상태에서 <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착한 대상</u></b></mark></color>에게는, 대신 피해량 -90%\n[WinDuel]\n- 각 대상의 <color=#ff6000><mark=#ff000040><b><u>부정적인 효과 1개당</u></b></mark></color> 피해량 +10% (최대 60%, 대상 별로 판정)\n[DefeatDuel]\n- [AttackDmgDown] 5, [Paralysis] 5 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].desc
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [IntenseColors], [WhenUse], [WinDuel], [DefeatDuel], [AttackDmgDown], [Paralysis], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [IntenseColors] = 강렬한 색채 / Palette Vibrante; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking …
   EN: [WideAreaRampage]\nPrioritizes targets that have [IntenseColors]\nThis Skill does not trigger Defense Skills (excluding Clashable Guard)\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Final Power +1 <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect</u></b></mark></color> on the main target (max 6)\n- <color=#ff6000><mark=#ff000040><b><u>If the main target has [IntenseColors],</u></b></mark></color> Clash Power +6\n- <color=#ff6000><mark=#ff000040><b><u>If target has [IntenseColors],</u></b></mark></color> deal +100% damage (against each target separately)\n· <color=#ff6000><mark=#ff000040><b><u>If target has equipped Defense Skills</u></b></mark></color> while having [IntenseColors], deal -90% damage instead\n[WinDuel]\n- Deal +10% damage <color=#ff6000><mark=#ff000040><b><u>for every type of negative effect on target</u></b></mark></color> (max 60%, against each target separately)\n[DefeatDuel]\n- Gain 5 [AttackDmgDown] and 5 [Paralysis]\n- Damage from this Skill does not Stagger the target\n- On Hit, does not trigger [Sinking] effects on the target\n[EndSkill] End this turn
   PL: [WideAreaRampage]\npriorytet: cele z [IntenseColors]\nta Umiejętność nie aktywuje Umiejętności obronnych (poza obroną z możliwością Starcia)\nmoże przeprowadzić Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- Moc Końcowa +1 <color=#ff6000><mark=#ff000040><b><u>za każdy rodzaj negatywnego efektu</u></b></mark></color> na głównym celu (maks. 6)\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma [IntenseColors],</u></b></mark></color> Moc Starcia +6\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [IntenseColors],</u></b></mark></color> zadaje +100% obrażeń (osobno dla każdego celu)\n· <color=#ff6000><mark=#ff000040><b><u>jeżeli cel wyposażył Umiejętności obronne</u></b></mark></color> mając [IntenseColors], zamiast tego zadaje -90% obrażeń\n[WinDuel]\n- zadaje +10% obrażeń <color=#ff6000><mark=#ff000040><b><u>za każdy rodzaj negatywnego efektu celu</u></b></mark></color> (maks. 60%, osobno dla każdego celu)\n[DefeatDuel]\n- zyskuje 5 [AttackDmgDown] i 5 [Paralysis]\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- przy trafieniu nie aktywuje efektów [Sinking] celu\n[EndSkill] kończy tę turę
1039. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1040. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1042. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Laceration]
1043. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1045. [Umiejętność wroga [142305] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-twth.json :: dataList[id=142305].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
