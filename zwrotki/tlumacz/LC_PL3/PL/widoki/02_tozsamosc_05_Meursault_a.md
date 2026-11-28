# Grzesznik #05: Meursault — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Meursault** (뫼르소) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #05: Meursault (뫼르소)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 뫼르소
   źródło: Characters.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Meursault
   PL:
2. [Akta więźnia — nazwa] 뫼르소
   źródło: IntroduceCharacter.json :: dataList[id=뫼르소].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: IntroduceCharacter.json :: dataList[id=뫼르소].description
   limit: do 120 znaków
   EN: Wants clear and concise commands, requiring no judgement on his part.
   PL: Wymaga jasnych i krótkich poleceń, niezostawiających mu pola do własnego osądu.

## [0] LCB Sinner — Meursault — LCB 수감자
- ID Tożsamości: `10501` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 90 · szybkość: 1–2 / 1–2 / 2–3 / 2–3
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10501].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10501].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10501].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 뫼르소의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10501].desc
   limit: do 120 znaków
   EN: Meursault’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 원, 투
   źródło: Skills.json :: dataList[id=1050101].levelList[level=1].name ; dataList[id=1050101].levelList[level=2].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Un, Deux
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
12. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 주먹꽂기
   źródło: Skills.json :: dataList[id=1050102].levelList[level=1].name ; dataList[id=1050102].levelList[level=2].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 6 · monety: 1 (+9)
   limit: do 40 znaków
   EN: Nailing Fist
   PL:
14. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1050102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
15. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 수비 위력 증가 3 얻음
   źródło: Skills.json :: dataList[id=1050102].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Defense Power Up next turn
   PL:
16. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연격
   źródło: Skills.json :: dataList[id=1050103].levelList[level=3].name ; dataList[id=1050103].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Des Coups
   PL:
17. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [WhenUse] 다음 턴에 보호 3 얻음
   źródło: Skills.json :: dataList[id=1050103].levelList[level=3].desc ; dataList[id=1050103].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Protection next turn
   PL:
18. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050103].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +2 [Vibration] Count
   PL:
19. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
23. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050104].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL:
24. [Pasywka bojowa (od ulepszenia 1, posiadane 2× Sloth) — nazwa] 각오
   źródło: Passives.json :: dataList[id=1050101].name
   limit: do 40 znaków
   EN: Staunchness
   PL:
25. [Pasywka bojowa (od ulepszenia 1, posiadane 2× Sloth) — opis] 전투 시작 시 자신의 체력이 50% 미만이면 보호 1을 얻음
   źródło: Passives.json :: dataList[id=1050101].desc
   limit: do 120 znaków
   EN: At less than 50% HP, gain 1 Protection at the start of the combat phase.
   PL:
26. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 등뒤 받쳐주기
   źródło: Passives.json :: dataList[id=1050121].name
   limit: do 40 znaków
   EN: Backup
   PL:
27. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 최대 체력이 가장 높은 아군 1명 공격 스킬로 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1050121].desc
   limit: do 120 znaków
   EN: 1 ally with the highest Max HP takes -10% damage from attack skills.
   PL:
28. [Kwestia głosowa [get_10501_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=get_10501_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
29. [Kwestia głosowa [get_10501_1] (Identity Acquisition)] 뫼르소. 그렇게 불러주시겠습니까, 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=get_10501_1].dlg
   limit: do 120 znaków
   EN: Meursault. Please refer to me as such, Manager.
   PL:
30. [Kwestia głosowa [lobby_morning_10501_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=lobby_morning_10501_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
31. [Kwestia głosowa [lobby_morning_10501_1] (Morning Greeting)] 정해진 시간에 기상하는 것은 사칙에 명시된 내용입니다. 관리자님을 포함한 대다수의 수감자들은 이 사실을 모르는 것 같군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=lobby_morning_10501_1].dlg
   limit: do 190 znaków
   EN: The company rules say that its employees are to get up at designated hours. It appears most Sinners are unaware of this fact, and so are you.
   PL:
32. [Kwestia głosowa [lobby_noon_10501_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=lobby_noon_10501_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
33. [Kwestia głosowa [lobby_noon_10501_1] (Afternoon Greeting)] 점심시간에는 무얼 하냐고 물으신다면… 무엇을 해야 하는지 규정된 바는 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=lobby_noon_10501_1].dlg
   limit: do 120 znaków
   EN: If you ask me how I intend to spend my afternoon… No rules state what to do.
   PL:
34. [Kwestia głosowa [lobby_night_10501_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=lobby_night_10501_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
35. [Kwestia głosowa [lobby_night_10501_1] (Evening Greeting)] 구태여 좋냐 안 좋냐를 따지자면 밤보다는 낮을 선호하는 편입니다. 보이지 않을수록 이해가 어렵기 때문입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=lobby_night_10501_1].dlg
   limit: do 200 znaków
   EN: If I had to compare the times of day against each other, I prefer day to night. Darkness obscures vision, and what is hard to see is hard to understand.
   PL:
36. [Kwestia głosowa [smalltalk_10501_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=smalltalk_10501_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
37. [Kwestia głosowa [smalltalk_10501_1] (Chatter #1)] 저한테 무슨 볼일이라도 있으신 겁니까, 관리자님? 귀책되어야 할 사유가 있다면, 분명하게 말씀해주시는 게 좋습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=smalltalk_10501_1].dlg
   limit: do 130 znaków
   EN: Do you have any business with me, Manager? If there is a particular reason, do make it clear.
   PL:
38. [Kwestia głosowa [smalltalk_10501_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=smalltalk_10501_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
39. [Kwestia głosowa [smalltalk_10501_2] (Chatter #2)] 다들 제게 평소에 웃고 다니라고 하더군요. 관리자님께서도 그걸 원하시는 겁니까?
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=smalltalk_10501_2].dlg
   limit: do 120 znaków
   EN: People suggest that I smile more often. Do you want that as well, Manager?
   PL:
40. [Kwestia głosowa [smalltalk_10501_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=smalltalk_10501_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
41. [Kwestia głosowa [smalltalk_10501_3] (Chatter #3)] …자꾸만 말을 거시는군요. 관리자님의 규정에서는 그렇게 명시되어 있는 겁니까?
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=smalltalk_10501_3].dlg
   limit: do 120 znaków
   EN: …You continue to speak with me. Are you encouraged by the rules to do so?
   PL:
42. [Kwestia głosowa [neglect_10501_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=neglect_10501_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
43. [Kwestia głosowa [neglect_10501_1] (Idle)] 복귀하실 때까지 기다리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=neglect_10501_1].dlg
   limit: do 120 znaków
   EN: I shall wait here until you return.
   PL:
44. [Kwestia głosowa [formation_10501_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=formation_10501_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
45. [Kwestia głosowa [formation_10501_1] (Deployment)] 네, 원하신다면.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=formation_10501_1].dlg
   limit: do 120 znaków
   EN: Yes, if that is what you want.
   PL:
46. [Kwestia głosowa [battleentry_10501_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battleentry_10501_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
47. [Kwestia głosowa [battleentry_10501_1] (Stage Entry)] 규정이라면. 따르겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battleentry_10501_1].dlg
   limit: do 120 znaków
   EN: If the rules say so.
   PL:
48. [Kwestia głosowa [battle_select_10501_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_select_10501_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
49. [Kwestia głosowa [battle_select_10501_1] (Viewed in Battle)] 무슨 문제라도 있으십니까, 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_select_10501_1].dlg
   limit: do 120 znaków
   EN: Is there a problem, Manager?
   PL:
50. [Kwestia głosowa [battle_endcommand_10501_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_endcommand_10501_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
51. [Kwestia głosowa [battle_endcommand_10501_1] (Commencing Attack)] 규정에 따라, 실행합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_endcommand_10501_1].dlg
   limit: do 120 znaków
   EN: I shall execute the order according to the rules.
   PL:
52. [Kwestia głosowa [battle_enemy_break_10501_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_enemy_break_10501_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
53. [Kwestia głosowa [battle_enemy_break_10501_1] (Enemy Stagger)] 다음 판단을 부탁합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_enemy_break_10501_1].dlg
   limit: do 120 znaków
   EN: I am awaiting your next order.
   PL:
54. [Kwestia głosowa [battle_break_10501_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_break_10501_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
55. [Kwestia głosowa [battle_break_10501_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_break_10501_1].dlg
   limit: do 120 znaków
   EN: Ugh!
   PL:
56. [Kwestia głosowa [battle_kill_10501_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_kill_10501_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
57. [Kwestia głosowa [battle_kill_10501_1] (Enemy Killed)] 규정대로.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_kill_10501_1].dlg
   limit: do 120 znaków
   EN: Done accordingly.
   PL:
58. [Kwestia głosowa [battle_allydead_10501_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_allydead_10501_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
59. [Kwestia głosowa [battle_allydead_10501_1] (Ally Death)] 규정대로 부탁드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_allydead_10501_1].dlg
   limit: do 120 znaków
   EN: Please take care of this by the rules.
   PL:
60. [Kwestia głosowa [choice_success_p_10501_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=choice_success_p_10501_2].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
61. [Kwestia głosowa [choice_success_p_10501_2] (Check Passed)] 해냈다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=choice_success_p_10501_2].dlg
   limit: do 120 znaków
   EN: I made it.
   PL:
62. [Kwestia głosowa [choice_fail_n_10501_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=choice_fail_n_10501_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
63. [Kwestia głosowa [choice_fail_n_10501_1] (Check Failed)] 실패했군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=choice_fail_n_10501_1].dlg
   limit: do 120 znaków
   EN: I failed.
   PL:
64. [Kwestia głosowa [battle_clear_10501_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_clear_10501_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
65. [Kwestia głosowa [battle_clear_10501_1] (Victory Cry)] 그저 명령대로 행한 것일 뿐.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_clear_10501_1].dlg
   limit: do 120 znaków
   EN: I simply followed orders.
   PL:
66. [Kwestia głosowa [battle_clear_ex_10501_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_clear_ex_10501_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
67. [Kwestia głosowa [battle_clear_ex_10501_1] (Extra Conditions Fulfilled)] 마땅히 했어야 할 일에 칭찬은 불필요한 과정입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_clear_ex_10501_1].dlg
   limit: do 120 znaków
   EN: It’s what should have been done; compliments are redundant.
   PL:
68. [Kwestia głosowa [battle_defeat_10501_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_defeat_10501_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
69. [Kwestia głosowa [battle_defeat_10501_1] (Defeat Wail)] 전략을 다시 재고해보시길.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LCB_10501.json :: dataList[id=battle_defeat_10501_1].dlg
   limit: do 120 znaków
   EN: I implore you to revise the strategy.
   PL:

## [00] Liu Assoc. South Section 6 — Meursault — 남부 리우 협회 6과
- ID Tożsamości: `10502` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

70. [Karta Tożsamości — tytuł] 남부 리우 협회\n6과
   źródło: Personalities.json :: dataList[id=10502].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 6
   PL:
71. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10502].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10502].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Karta Tożsamości — opis] 뫼르소의 두번째 인격
   źródło: Personalities.json :: dataList[id=10502].desc
   limit: do 120 znaków
   EN: Meursault’s 2nd Identity
   PL:
74. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 돌파
   źródło: Skills.json :: dataList[id=1050201].levelList[level=1].name ; dataList[id=1050201].levelList[level=2].name ; dataList[id=1050201].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Assault
   PL:
75. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Burn
   PL:
76. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL:
78. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn
   PL:
80. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 진각
   źródło: Skills.json :: dataList[id=1050202].levelList[level=1].name ; dataList[id=1050202].levelList[level=2].name ; dataList[id=1050202].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Stalwart Stance
   PL:
81. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 무작위 적 2명에게 화상 2 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict 2 Burn on 2 random enemies
   PL:
84. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 무작위 적 2명에게 화상 3 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict 3 Burn on 2 random enemies
   PL:
86. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연무 붕권
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].name ; dataList[id=1050203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Perfected Death Fist
   PL:
87. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 3 부여
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Burn
   PL:
88. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 3 증가
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1050203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Burn Count
   PL:
89. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 무작위 적 2명에게 화상 3 부여
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1050203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 화상 위력이 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050203].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 5+ Burn, Coin Power +1
   PL:
91. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050204].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 태산
   źródło: Passives.json :: dataList[id=1050201].name
   limit: do 40 znaków
   EN: Great Mountain
   PL:
93. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 피격 시 무작위 대상에게 화상 1 부여 (최대 4회)
   źródło: Passives.json :: dataList[id=1050201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked, inflict 1 Burn on a random enemy.\n(Up to 4 times)
   PL:
94. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 마찰 타격점
   źródło: Passives.json :: dataList[id=1050221].name
   limit: do 40 znaków
   EN: Friction Point
   PL:
95. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 낮은 아군 1명 화상 부여 값 +1
   źródło: Passives.json :: dataList[id=1050221].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed inflicts +1 Burn.
   PL:
96. [Kwestia głosowa [get_10502_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=get_10502_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Kwestia głosowa [get_10502_1] (Identity Acquisition)] 불꽃이 필요하신 거라면 피워드립니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=get_10502_1].dlg
   limit: do 120 znaków
   EN: If it is fire you need, then I will provide it.
   PL:
98. [Kwestia głosowa [lobby_morning_10502_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=lobby_morning_10502_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Kwestia głosowa [lobby_morning_10502_1] (Morning Greeting)] 때가 되어서 자연스럽게 눈이 떠진 것뿐입니다. 그러니 제 기상 시간에 대해 감탄하실 필요는 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=lobby_morning_10502_1].dlg
   limit: do 130 znaków
   EN: My eyes opened because it was time to wake up. There is no need to be amazed by how early I rise.
   PL:
100. [Kwestia głosowa [lobby_noon_10502_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=lobby_noon_10502_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Kwestia głosowa [lobby_noon_10502_1] (Afternoon Greeting)] 남는 시간에는 다른 이들의 훈련을 도와주고 있습니다. 처음엔 한 명이었는데 어느새 일과가 되어버렸더군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=lobby_noon_10502_1].dlg
   limit: do 190 znaków
   EN: In my spare time, I help others with their training. I only did it for one person at first, but as time went on, it became a regular routine.
   PL:
102. [Kwestia głosowa [lobby_night_10502_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=lobby_night_10502_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Kwestia głosowa [lobby_night_10502_1] (Evening Greeting)] 어두운 게 싫으시다면 주위를 밝혀드릴 수 있습니다. 제 불꽃은 6과에서 제일 밝은 불꽃입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=lobby_night_10502_1].dlg
   limit: do 130 znaków
   EN: I can brighten your surroundings if you dislike the dark. My fire is the brightest in Section 6.
   PL:
104. [Kwestia głosowa [smalltalk_10502_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Kwestia głosowa [smalltalk_10502_1] (Chatter #1)] 만약 일이 잘 풀리지 않는다면… 엉킨 부분을 찬찬히 살펴보면 됩니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_1].dlg
   limit: do 120 znaków
   EN: If things are not going well… you start by carefully examining the problem.
   PL:
106. [Kwestia głosowa [smalltalk_10502_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Kwestia głosowa [smalltalk_10502_2] (Chatter #2)] 말이 없어서 답답하다는 평가를 자주 듣습니다. 부정적인 요인은 아니므로, 구태여 고칠 노력은 하지 않고 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_2].dlg
   limit: do 180 znaków
   EN: Others often assess my infrequency of speech as stifling. As it is not a negative factor, I do not make an active effort to rectify it.
   PL:
108. [Kwestia głosowa [smalltalk_10502_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Kwestia głosowa [smalltalk_10502_3] (Chatter #3)] 때가 되어서 이곳으로 왔고, 관리자님을 만난 것처럼… 때가 된다면 황금가지 역시 찾을 수 있을 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_3].dlg
   limit: do 150 znaków
   EN: I arrived here and met you because it was time… Similarly, we will find the Golden Bough when the right time comes.
   PL:
110. [Kwestia głosowa [smalltalk_10502_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
111. [Kwestia głosowa [smalltalk_10502_4] (Post-Uptie Chat 1)] 지금까지의 관리 경험으로 미루어 보건대, 관리자님 정도라면 막힘없이 불꽃을 피워낼 수 있을 것입니다. 원하신다면…
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_4].dlg
   limit: do 170 znaków
   EN: Judging from the managerial experience so far, someone of your caliber should be able to create a flame with ease. If you want…
   PL:
112. [Kwestia głosowa [smalltalk_10502_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
113. [Kwestia głosowa [smalltalk_10502_5] (Post-Uptie Chat 2)] 기억을 잃은 것에 연연해하지 마시길. 관리자님이라면 자연스러운 순간에 찾아낼 수 있을 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=smalltalk_10502_5].dlg
   limit: do 150 znaków
   EN: Don’t let your loss of memory distract you too much. I am certain the moment of recovery will come naturally.
   PL:
114. [Kwestia głosowa [neglect_10502_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=neglect_10502_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Kwestia głosowa [neglect_10502_1] (Idle)] 급한 일이 생긴 거라면, 떠나셔도 됩니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=neglect_10502_1].dlg
   limit: do 120 znaków
   EN: You may leave me if you’re urgently needed.
   PL:
116. [Kwestia głosowa [gacksung_10502_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=gacksung_10502_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
117. [Kwestia głosowa [gacksung_10502_1] (Uptying)] 더욱 진한 불꽃이 되도록 정진하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=gacksung_10502_1].dlg
   limit: do 120 znaków
   EN: I will strive to become a keener flame.
   PL:
118. [Kwestia głosowa [formation_10502_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=formation_10502_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Kwestia głosowa [formation_10502_1] (Deployment)] 불꽃을 바라신다면.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=formation_10502_1].dlg
   limit: do 120 znaków
   EN: If it’s a fire you wish for.
   PL:
120. [Kwestia głosowa [battleentry_10502_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battleentry_10502_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Kwestia głosowa [battleentry_10502_1] (Stage Entry)] 이 불꽃이 필요하시다면.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battleentry_10502_1].dlg
   limit: do 120 znaków
   EN: If you need this fire of mine.
   PL:
122. [Kwestia głosowa [battle_select_10502_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_select_10502_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Kwestia głosowa [battle_select_10502_1] (Viewed in Battle)] 잘 풀리지 않고 있습니까?
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_select_10502_1].dlg
   limit: do 120 znaków
   EN: Is it not progressing well?
   PL:
124. [Kwestia głosowa [battle_endcommand_10502_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_endcommand_10502_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Kwestia głosowa [battle_endcommand_10502_1] (Commencing Attack)] 제 불을 따라오십시오.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_endcommand_10502_1].dlg
   limit: do 120 znaków
   EN: Follow my fire.
   PL:
126. [Kwestia głosowa [battle_enemy_break_10502_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_enemy_break_10502_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Kwestia głosowa [battle_enemy_break_10502_1] (Enemy Stagger)] 잘 풀린 것 같습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_enemy_break_10502_1].dlg
   limit: do 120 znaków
   EN: It seems to have gone well.
   PL:
128. [Kwestia głosowa [battle_break_10502_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_break_10502_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Kwestia głosowa [battle_break_10502_1] (Staggered)] 읏!
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_break_10502_1].dlg
   limit: do 120 znaków
   EN: Nkh!
   PL:
130. [Kwestia głosowa [battle_kill_10502_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_kill_10502_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Kwestia głosowa [battle_kill_10502_1] (Enemy Killed)] 자연스러운 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_kill_10502_1].dlg
   limit: do 120 znaków
   EN: A natural outcome.
   PL:
132. [Kwestia głosowa [battle_allydead_10502_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_allydead_10502_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Kwestia głosowa [battle_allydead_10502_1] (Ally Death)] 더 진한 불꽃이었다면…
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_allydead_10502_1].dlg
   limit: do 120 znaków
   EN: If only the fire were more intense…
   PL:
134. [Kwestia głosowa [choice_success_p_10502_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=choice_success_p_10502_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Kwestia głosowa [choice_success_p_10502_2] (Check Passed)] 길을 밝힐 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=choice_success_p_10502_2].dlg
   limit: do 120 znaków
   EN: I lit the path as required.
   PL:
136. [Kwestia głosowa [choice_fail_n_10502_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=choice_fail_n_10502_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Kwestia głosowa [choice_fail_n_10502_1] (Check Failed)] 불꽃도 흔들릴 때가 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=choice_fail_n_10502_1].dlg
   limit: do 120 znaków
   EN: Fires are susceptible to sudden gusts.
   PL:
138. [Kwestia głosowa [battle_clear_10502_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_clear_10502_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Kwestia głosowa [battle_clear_10502_1] (Victory Cry)] 타격점이 분명하게 보이더군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_clear_10502_1].dlg
   limit: do 120 znaków
   EN: I was able to see where to strike.
   PL:
140. [Kwestia głosowa [battle_clear_ex_10502_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_clear_ex_10502_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Kwestia głosowa [battle_clear_ex_10502_1] (Extra Conditions Fulfilled)] 네, 이번 불꽃은 저도 마음에 들었습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_clear_ex_10502_1].dlg
   limit: do 120 znaków
   EN: Yes, I was fond of the fire I managed to ignite now.
   PL:
142. [Kwestia głosowa [battle_defeat_10502_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_defeat_10502_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Kwestia głosowa [battle_defeat_10502_1] (Defeat Wail)] 괜찮습니다. 문제점을 파악했습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_LiuAsso6_10502.json :: dataList[id=battle_defeat_10502_1].dlg
   limit: do 120 znaków
   EN: It’s alright. I’ve grasped the problem.
   PL:

## [000] W Corp. L2 Cleanup Agent — Meursault — W사 2등급 정리 요원
- ID Tożsamości: `10503` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

144. [Karta Tożsamości — tytuł] W사 2등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10503].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L2\nCleanup Agent
   PL:
145. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10503].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10503].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Karta Tożsamości — opis] 뫼르소의 세번째 인격
   źródło: Personalities.json :: dataList[id=10503].desc
   limit: do 120 znaków
   EN: Meursault’s 3rd Identity
   PL:
148. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 절단
   źródło: Skills.json :: dataList[id=1050301].levelList[level=1].name ; dataList[id=1050301].levelList[level=2].name ; dataList[id=1050301].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Rip
   PL:
149. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 참격 보호 1 얻음
   źródło: Skills.json :: dataList[id=1050301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Slash Protection
   PL:
150. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 참격 보호 2 얻음
   źródło: Skills.json :: dataList[id=1050301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Slash Protection
   PL:
151. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1050301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Charge Count
   PL:
152. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 참격 보호 2 얻음\n자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1050301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Slash Protection\nGain +3 Charge Count
   PL:
153. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].name ; dataList[id=1050302].levelList[level=2].name ; dataList[id=1050302].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Energy Cycle
   PL:
154. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL:
155. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
157. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1050302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
158. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 3을 소모하여 참격 취약 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1050302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 3 Charge Count to inflict 2 Slash Fragility
   PL:
159. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 충전 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050302].levelList[level=4].desc
   limit: do 120 znaków
   EN: If at 5+ Charge Count, Coin Power +1
   PL:
160. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
161. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 에너지 교류
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].name ; dataList[id=1050303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Energy Current
   PL:
163. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 2 Charge Count to inflict 2 Defense Level Down
   PL:
164. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 충전 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050303].levelList[level=4].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050304].levelList[level=1].name ; dataList[id=1050304].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+5)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain +2 Charge Count
   PL:
170. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 견뎌내기
   źródło: Passives.json :: dataList[id=1050301].name
   limit: do 40 znaków
   EN: Enduring Spirit
   PL:
171. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 피격 시 충전 횟수 1 증가 (최대 6회)
   źródło: Passives.json :: dataList[id=1050301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked, gain +1 Charge Count.\n(Up to 6 times)
   PL:
172. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Envy) — nazwa] 묵묵함
   źródło: Passives.json :: dataList[id=1050321].name
   limit: do 40 znaków
   EN: Taciturn
   PL:
173. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Envy) — opis] 속도가 가장 낮은 아군 1명 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1050321].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed inflicts +1 Rupture.
   PL:
174. [Kwestia głosowa [get_10503_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=get_10503_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Kwestia głosowa [get_10503_1] (Identity Acquisition)] 목적지를 말씀해주신다면, 안내해드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=get_10503_1].dlg
   limit: do 120 znaków
   EN: Tell me your destination, and I’ll guide you there.
   PL:
176. [Kwestia głosowa [lobby_morning_10503_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=lobby_morning_10503_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Kwestia głosowa [lobby_morning_10503_1] (Morning Greeting)] 이해가 되지 않는 것은 많지만, 그중 하나가 지각을 하는 자들입니다. 회사에서 요구하는 기본적인 소양이라고 생각합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=lobby_morning_10503_1].dlg
   limit: do 210 znaków
   EN: There are many things I fail to comprehend, and those who are late to work are one of them. I believe timely arrival is a basic requirement for an employee to meet.
   PL:
178. [Kwestia głosowa [lobby_noon_10503_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=lobby_noon_10503_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Kwestia głosowa [lobby_noon_10503_1] (Afternoon Greeting)] 이 시간대에는 햇빛을 쬐곤 합니다. 햇빛을 아무 때나 볼 수 있다는 것이 낯선 탓이었을 수도 있겠군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=lobby_noon_10503_1].dlg
   limit: do 200 znaków
   EN: I often expose myself to sunlight at this hour. It may be attributed to the fact that the nature of my occupation prevented me from seeing it frequently.
   PL:
180. [Kwestia głosowa [lobby_night_10503_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=lobby_night_10503_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [lobby_night_10503_1] (Evening Greeting)] 저와 대화하는 걸 즐겨하는 이는 드뭅니다. 그렇지 않은 관리자님은 유별난 사람이겠군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=lobby_night_10503_1].dlg
   limit: do 120 znaków
   EN: Few people enjoy conversing with me. That would make you a strange one, Manager.
   PL:
182. [Kwestia głosowa [smalltalk_10503_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [smalltalk_10503_1] (Chatter #1)] 시체들을 보는 건 익숙합니다. 그것이 유쾌하다는 뜻은 아니지만.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_1].dlg
   limit: do 120 znaków
   EN: I am familiar with dead bodies. Familiarity does not assure pleasantness, however.
   PL:
184. [Kwestia głosowa [smalltalk_10503_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [smalltalk_10503_2] (Chatter #2)] 돈키호테는 W사에 입사한 것이 자랑스럽다고 하더군요. 조금 신기했습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_2].dlg
   limit: do 120 znaków
   EN: Don Quixote says she is proud to have joined W Corp. I found that rather curious.
   PL:
186. [Kwestia głosowa [smalltalk_10503_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [smalltalk_10503_3] (Chatter #3)] 만약 워프 열차를 이용하신다면 미리 말씀 주셔도 괜찮습니다, 관리자님의 파편은 제가 모아드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_3].dlg
   limit: do 140 znaków
   EN: If you’re ever taking a WARP train, you may let me know, Manager. I will personally pick up your pieces.
   PL:
188. [Kwestia głosowa [smalltalk_10503_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [smalltalk_10503_4] (Post-Uptie Chat 1)] 누군가와 공감한다는 것이 그렇게 중요한 일이었다면… 사규에 명시되었어야 했을 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_4].dlg
   limit: do 160 znaków
   EN: If it is actually that important to empathize with others… they should have stated as much in the company guidelines.
   PL:
190. [Kwestia głosowa [smalltalk_10503_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [smalltalk_10503_5] (Post-Uptie Chat 2)] W사는 유독 퇴사자가 많은 기업이었습니다. 그들의 마지막 모습은 항상 눈물과 침 범벅이더군요. 구태여 이해하려는 노력은 하지 않았습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=smalltalk_10503_5].dlg
   limit: do 250 znaków
   EN: W Corp. saw particularly many resignations. The quitting employees always had copious amounts of tears and saliva about their faces. I did not make an active effort to comprehend their behavior.
   PL:
192. [Kwestia głosowa [neglect_10503_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=neglect_10503_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [neglect_10503_1] (Idle)] 제시간에만 돌아오시길.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=neglect_10503_1].dlg
   limit: do 120 znaków
   EN: Do make sure to return in time.
   PL:
194. [Kwestia głosowa [gacksung_10503_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=gacksung_10503_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [gacksung_10503_1] (Uptying)] 승진은… 익숙합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=gacksung_10503_1].dlg
   limit: do 120 znaków
   EN: Promotions… That, I am used to.
   PL:
196. [Kwestia głosowa [formation_10503_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=formation_10503_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [formation_10503_1] (Deployment)] 네, 목적지를 향해.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=formation_10503_1].dlg
   limit: do 120 znaków
   EN: Understood, I’ll get you to your destination.
   PL:
198. [Kwestia głosowa [battleentry_10503_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battleentry_10503_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [battleentry_10503_1] (Stage Entry)] 목적지까지 가기 위하여.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battleentry_10503_1].dlg
   limit: do 120 znaków
   EN: Onto our destination.
   PL:
200. [Kwestia głosowa [battle_select_10503_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_select_10503_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [battle_select_10503_1] (Viewed in Battle)] 여전히 유별난 사람이시군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_select_10503_1].dlg
   limit: do 120 znaków
   EN: You are certainly a peculiar individual.
   PL:
202. [Kwestia głosowa [battle_endcommand_10503_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_endcommand_10503_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [battle_endcommand_10503_1] (Commencing Attack)] 방해물을 제거합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_endcommand_10503_1].dlg
   limit: do 120 znaków
   EN: Removing obstacles.
   PL:
204. [Kwestia głosowa [battle_enemy_break_10503_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_enemy_break_10503_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Kwestia głosowa [battle_enemy_break_10503_1] (Enemy Stagger)] 그다지 유쾌하진 않군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_enemy_break_10503_1].dlg
   limit: do 120 znaków
   EN: I am not particularly amused.
   PL:
206. [Kwestia głosowa [battle_break_10503_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_break_10503_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Kwestia głosowa [battle_break_10503_1] (Staggered)] 흡!
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_break_10503_1].dlg
   limit: do 120 znaków
   EN: Hmpfh!
   PL:
208. [Kwestia głosowa [battle_kill_10503_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_kill_10503_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Kwestia głosowa [battle_kill_10503_1] (Enemy Killed)] 모을 필요는 없겠군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_kill_10503_1].dlg
   limit: do 120 znaków
   EN: I won’t have to collect these remains.
   PL:
210. [Kwestia głosowa [battle_allydead_10503_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_allydead_10503_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Kwestia głosowa [battle_allydead_10503_1] (Ally Death)] 파편은 나중에 모으겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_allydead_10503_1].dlg
   limit: do 120 znaków
   EN: I’ll collect their remains later.
   PL:
212. [Kwestia głosowa [choice_success_p_10503_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=choice_success_p_10503_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Kwestia głosowa [choice_success_p_10503_2] (Check Passed)] 규정대로 했을 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=choice_success_p_10503_2].dlg
   limit: do 120 znaków
   EN: I merely followed the procedures.
   PL:
214. [Kwestia głosowa [choice_fail_n_10503_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=choice_fail_n_10503_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Kwestia głosowa [choice_fail_n_10503_1] (Check Failed)] 규정에 없던 내용이군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=choice_fail_n_10503_1].dlg
   limit: do 120 znaków
   EN: This was not in the procedures.
   PL:
216. [Kwestia głosowa [battle_clear_10503_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_clear_10503_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Kwestia głosowa [battle_clear_10503_1] (Victory Cry)] 이곳의 시체들은 더 단단하군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_clear_10503_1].dlg
   limit: do 120 znaków
   EN: The corpses here are more durable than what I work with.
   PL:
218. [Kwestia głosowa [battle_clear_ex_10503_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_clear_ex_10503_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Kwestia głosowa [battle_clear_ex_10503_1] (Extra Conditions Fulfilled)] 다들 알맞은 파편으로 조각났군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_clear_ex_10503_1].dlg
   limit: do 120 znaków
   EN: All of them have been segmented into adequate pieces.
   PL:
220. [Kwestia głosowa [battle_defeat_10503_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_defeat_10503_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Kwestia głosowa [battle_defeat_10503_1] (Defeat Wail)] 익숙해지는 과정일 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Wcorp_10503.json :: dataList[id=battle_defeat_10503_1].dlg
   limit: do 120 znaków
   EN: It’s a necessary step for familiarization.
   PL:

## [000] N Corp. Großhammer — Meursault — N사 큰 망치
- ID Tożsamości: `10504` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 99 · szybkość: 2–4 / 2–4 / 3–5 / 3–5
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

222. [Karta Tożsamości — tytuł] N사\n큰 망치
   źródło: Personalities.json :: dataList[id=10504].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nGroßhammer
   PL:
223. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10504].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10504].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Karta Tożsamości — opis] 뫼르소의 네번째 인격
   źródło: Personalities.json :: dataList[id=10504].desc
   limit: do 120 znaków
   EN: Meursault’s 4th Identity
   PL:
226. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 꿰뚫기
   źródło: Skills.json :: dataList[id=1050401].levelList[level=1].name ; dataList[id=1050401].levelList[level=2].name ; dataList[id=1050401].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 5 · monety: 2 (+1)
   limit: do 40 znaków
   EN: Drive
   PL:
227. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user’s Stagger Threshold by 30% of damage dealt
   PL:
228. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 60%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user’s Stagger Threshold by 60% of damage dealt
   PL:
230. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 60%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n자신의 체력이 50%미만일 때, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1050401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\nAt less than 50% HP, Coin Power +2
   PL:
232. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 죄를 씻어내노라
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].name ; dataList[id=1050402].levelList[level=2].name ; dataList[id=1050402].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 6 · monety: 2 (+3)
   limit: do 40 znaków
   EN: You Are Cleansed of Sin
   PL:
233. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 3 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Nails
   PL:
234. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 못 3 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].coinlist[#0].coindescs[#0].summary ; dataList[id=1050402].levelList[level=2].coinlist[#0].coindescs[#0].summary
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL:
236. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 못이 5 이상 있으면, 다음 턴에 속박 2, 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Nails, inflict 2 Bind and 1 Attack Power Down next turn
   PL:
237. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 6 증가
   źródło: Skills.json :: dataList[id=1050402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Aggro to this Skill Slot next turn
   PL:
238. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 못이 5 이상 있으면, 다음 턴에 속박 2, 공격 위력 감소 2 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Nails, inflict 2 Bind and 2 Attack Power Down next turn
   PL:
239. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 이단 말살
   źródło: Skills.json :: dataList[id=1050403].levelList[level=3].name ; dataList[id=1050403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 8 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Annihilate Heretics
   PL:
240. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 못 2 부여
   źródło: Skills.json :: dataList[id=1050403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Nails next turn
   PL:
241. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1050403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 50% of damage dealt
   PL:
242. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 6 증가
   źródło: Skills.json :: dataList[id=1050403].levelList[level=4].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복\n 대상의 못 1당 체력 회복량 +3%
   źródło: Skills.json :: dataList[id=1050403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 50% of damage dealt\nHP Heal +3% for each of target's Nails
   PL:
244. [Obrona (ulepszenie 1) — nazwa] 어리석도다...!
   źródło: Skills.json :: dataList[id=1050404].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 15 · monety: 1 (−5)
   limit: do 40 znaków
   EN: Foolishness…!
   PL:
245. [Obrona (ulepszenie 1) — opis] [StartBattle] 보호 1을 얻음\n체력이 50% 미만이면 최종 위력 + 2
   źródło: Skills.json :: dataList[id=1050404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 1 Protection\nAt less than 50% HP, Final Power +2
   PL:
246. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Wrath) — nazwa] 집념의 망치
   źródło: Passives.json :: dataList[id=1050401].name
   limit: do 40 znaków
   EN: Obsessive Hammer
   PL:
247. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Wrath) — opis] 전투 시작 시 체력이 50% 미만이면, 자신에게 부여된 부정적인 효과 중 1개를 제거하고, 광신 1, 공격 위력 증가 1, 보호 3을 얻음
   źródło: Passives.json :: dataList[id=1050401].desc
   limit: do 180 znaków
   EN: When below 50% HP, remove 1 negative status effect and gain 1 Fanatic, 1 Attack Power Up, and 3 Protection at the start of the combat phase.
   PL:
248. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 으뜸 영광
   źródło: Passives.json :: dataList[id=1050421].name
   limit: do 40 znaków
   EN: Highest Honor
   PL:
249. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 현재 체력이 가장 낮은 아군 1명이 체력이 50% 미만이면 공격 위력 증가 1, 보호 1을 얻음. 대상이 N사 광신도면 광신 1을 추가로 얻음
   źródło: Passives.json :: dataList[id=1050421].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply 1 Attack Power Up and 1 Protection to the ally with the least HP below 50%.\nIf the ally is an 'N Corp. Fanatic', also apply 1 Fanatic.
   PL:
250. [Kwestia głosowa [get_10504_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=get_10504_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [get_10504_1] (Identity Acquisition)] 쥐는 자의 망치는 이곳에 있나니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=get_10504_1].dlg
   limit: do 120 znaków
   EN: Here is the hammer of the One Who Grips.
   PL:
252. [Kwestia głosowa [lobby_morning_10504_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=lobby_morning_10504_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [lobby_morning_10504_1] (Morning Greeting)] 육체를 바르게 하기에 적합한 시간입니다. 귀하께서도 집회에 참여하여 마음을 씻어내는 것이 어떠한지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=lobby_morning_10504_1].dlg
   limit: do 160 znaków
   EN: The time is ripe to discipline the body. I suggest that you participate in the gathering as well to help cleanse your mind.
   PL:
254. [Kwestia głosowa [lobby_noon_10504_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=lobby_noon_10504_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [lobby_noon_10504_1] (Afternoon Greeting)] 이 시간에 귀하를 마주칠 줄은 미처 모르고 있었습니다. 근무에 고충이 있다면, 본인에게 언제든 말씀하시기를.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=lobby_noon_10504_1].dlg
   limit: do 170 znaków
   EN: I did not anticipate encountering you at this hour. If you have any woes regarding your work, please don’t hesitate to inform me.
   PL:
256. [Kwestia głosowa [lobby_night_10504_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=lobby_night_10504_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [lobby_night_10504_1] (Evening Greeting)] 귀하는 침소에 일찍 들어 육신을 보존하소서. 본인은 지금부터… 쥐여져야 하므로.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=lobby_night_10504_1].dlg
   limit: do 180 znaków
   EN: I suggest you retire to bed early so that you may preserve your strength. As for myself… there is a matter that needs me to be gripped.
   PL:
258. [Kwestia głosowa [smalltalk_10504_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [smalltalk_10504_1] (Chatter #1)] 쥐는 자를 보필하는 것은 으뜸 영광입니다. 본인은, 아직도 지명의 순간을 잊지 않고 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_1].dlg
   limit: do 150 znaków
   EN: It is one’s highest honor to aid the One Who Grips. I still have not forgotten the moment I was appointed as such.
   PL:
260. [Kwestia głosowa [smalltalk_10504_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [smalltalk_10504_2] (Chatter #2)] 이 못이 궁금하시군요. 이것은 N사의 경험 통조림을 만드는데 쓰입니다. 자세한 사용 방법은… 직접 현장을 찾으심이.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_2].dlg
   limit: do 210 znaków
   EN: So you are curious about this nail. This one is used to manufacture N Corp’s canned experiences. As for its use… You would do well to see where it’s used yourself.
   PL:
262. [Kwestia głosowa [smalltalk_10504_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [smalltalk_10504_3] (Chatter #3)] 이 가면은 쥐는 자께서 하사해주신 것입니다. 과거에 쓰던 것은 이 생명수의 관을 가리기에 부적절해진 터라.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_3].dlg
   limit: do 180 znaków
   EN: This mask has been bestowed upon me by the One Who Grips. The one I wore in the past could no longer conceal the tubes carrying lifefluid.
   PL:
264. [Kwestia głosowa [smalltalk_10504_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [smalltalk_10504_4] (Post-Uptie Chat 1)] …최근에 쥐는 자께서 눈 여겨 보시는 자가 있는 것 같습니다. 못의 자질이 있다던가. 귀하께서 인선을 하실 때의 판단을 알고 싶습니다. 혜안을 나누어주시옵소서.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_4].dlg
   limit: do 290 znaków
   EN: …It seems that there is someone recently holding the attention of the One Who Grips. It involves something about the potential to serve as a Nail. I would like to know how you determine who to appoint. Please share your wisdom.
   PL:
266. [Kwestia głosowa [smalltalk_10504_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [smalltalk_10504_5] (Post-Uptie Chat 2)] 저는 단 한 명의 못을 위한 망치일 뿐입니다. 쥐는 자께서는 못의 씨앗인 그 자를 가르치라 하시지만… 아니. 쥐는 자의 뜻이 그렇다면, 따를 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=smalltalk_10504_5].dlg
   limit: do 260 znaków
   EN: I am but a Hammer, serving a single Nail. Although the One Who Grips insists that I teach that disciple, a seed with the bearings of a Nail… Nay. If the One Who Grips instructs, then I am to follow.
   PL:
268. [Kwestia głosowa [neglect_10504_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=neglect_10504_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [neglect_10504_1] (Idle)] 망치는 언제나 그 자리에, 쥐일 때를 기다리고 있으므로.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=neglect_10504_1].dlg
   limit: do 120 znaków
   EN: The hammer always waits in place, ready to be gripped.
   PL:
270. [Kwestia głosowa [gacksung_10504_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=gacksung_10504_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [gacksung_10504_1] (Uptying)] 인정 받기에는 아직 미력하나, 귀하의 뜻이 그러하다면.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=gacksung_10504_1].dlg
   limit: do 140 znaków
   EN: Though I believe myself to be ever too puny to deserve such recognition, I will accept if you insist.
   PL:
272. [Kwestia głosowa [formation_10504_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=formation_10504_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [formation_10504_1] (Deployment)] 이곳에 있나니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=formation_10504_1].dlg
   limit: do 120 znaków
   EN: I am here.
   PL:
274. [Kwestia głosowa [battleentry_10504_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battleentry_10504_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [battleentry_10504_1] (Stage Entry)] 흙으로도 돌아가지 못 하리라.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battleentry_10504_1].dlg
   limit: do 120 znaków
   EN: They shan’t rest beneath the earth.
   PL:
276. [Kwestia głosowa [battle_select_10504_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_select_10504_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [battle_select_10504_1] (Viewed in Battle)] 말씀을 받드오니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_select_10504_1].dlg
   limit: do 120 znaków
   EN: I heed your words.
   PL:
278. [Kwestia głosowa [battle_endcommand_10504_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_endcommand_10504_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battle_endcommand_10504_1] (Commencing Attack)] 참회하게 되리라.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_endcommand_10504_1].dlg
   limit: do 120 znaków
   EN: You shall repent.
   PL:
280. [Kwestia głosowa [battle_enemy_break_10504_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_enemy_break_10504_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [battle_enemy_break_10504_1] (Enemy Stagger)] 무가치한 저항일 뿐이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_enemy_break_10504_1].dlg
   limit: do 120 znaków
   EN: A worthless resistance.
   PL:
282. [Kwestia głosowa [battle_break_10504_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_break_10504_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [battle_break_10504_1] (Staggered)] 신앙이 빈약하군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_break_10504_1].dlg
   limit: do 120 znaków
   EN: Such feeble faith.
   PL:
284. [Kwestia głosowa [battle_kill_10504_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_kill_10504_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Kwestia głosowa [battle_kill_10504_1] (Enemy Killed)] 이단을 정화했다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_kill_10504_1].dlg
   limit: do 120 znaków
   EN: The heretic has been purged.
   PL:
286. [Kwestia głosowa [battle_dead_10504_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_dead_10504_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
287. [Kwestia głosowa [battle_dead_10504_1] (Death)] 망치는… 그대들을 계속 쫓을 것이다…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_dead_10504_1].dlg
   limit: do 120 znaków
   EN: The hammer… shall pursue you to the end…
   PL:
288. [Kwestia głosowa [choice_success_p_10504_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=choice_success_p_10504_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Kwestia głosowa [choice_success_p_10504_2] (Check Passed)] 쥐는 자께서 성공을 명하셨으므로.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=choice_success_p_10504_2].dlg
   limit: do 120 znaków
   EN: For the One Who Grips had ordered me to succeed.
   PL:
290. [Kwestia głosowa [choice_fail_n_10504_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=choice_fail_n_10504_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Kwestia głosowa [choice_fail_n_10504_1] (Check Failed)] 본인이 미력하였기에.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=choice_fail_n_10504_1].dlg
   limit: do 120 znaków
   EN: It was the fault of my inability.
   PL:
292. [Kwestia głosowa [battle_clear_10504_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_clear_10504_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Kwestia głosowa [battle_clear_10504_1] (Victory Cry)] 쥐는 자께서 만족하셨다면, 그것으로 족합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_clear_10504_1].dlg
   limit: do 120 znaków
   EN: If the One Who Grips is satisfied, that is enough for me.
   PL:
294. [Kwestia głosowa [battle_clear_ex_10504_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_clear_ex_10504_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Kwestia głosowa [battle_clear_ex_10504_1] (Extra Conditions Fulfilled)] 쥐는 자께 완벽한 승리를 바치리라.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_clear_ex_10504_1].dlg
   limit: do 120 znaków
   EN: I devote this superb victory to the One Who Grips.
   PL:
296. [Kwestia głosowa [battle_defeat_10504_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_defeat_10504_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Kwestia głosowa [battle_defeat_10504_1] (Defeat Wail)] 모든 것은… 미력한 본인의 죄…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Ncorp_10504.json :: dataList[id=battle_defeat_10504_1].dlg
   limit: do 120 znaków
   EN: It is all… the fault of my weakness…
   PL:

## [00] Rosespanner Workshop Fixer — Meursault — 장미스패너 공방 해결사
- ID Tożsamości: `10505` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 76 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor, Charge

298. [Karta Tożsamości — tytuł] 장미스패너 공방\n해결사
   źródło: Personalities.json :: dataList[id=10505].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rosespanner Workshop Fixer
   PL:
299. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10505].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10505].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Karta Tożsamości — opis] 뫼르소의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10505].desc
   limit: do 120 znaków
   EN: Meursault’s 5th Identity
   PL:
302. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 떠맡은 업무 처리
   źródło: Skills.json :: dataList[id=1050501].levelList[level=1].name ; dataList[id=1050501].levelList[level=2].name ; dataList[id=1050501].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Saddled Tasks
   PL:
303. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
304. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL:
305. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1050501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 진동 횟수가 5 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1050501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 5+ [Vibration] Count, Coin Power +2
   PL:
307. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 강제 휴식
   źródło: Skills.json :: dataList[id=1050502].levelList[level=1].name ; dataList[id=1050502].levelList[level=2].name ; dataList[id=1050502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Forced Break
   PL:
308. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
309. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Vibration]이 5 이상 있을 때 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has 5+ [Vibration], inflict 1 Attack Power Down next turn
   PL:
310. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1050502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 진동 횟수가 7 이상이면, 최종 위력 +1
   źródło: Skills.json :: dataList[id=1050502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 7+ [Vibration] Count, Final Power +1
   PL:
313. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 마무리 가속
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].name ; dataList[id=1050503].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Finishing Runup
   PL:
314. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +1 Charge Count
   PL:
315. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1050503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL:
317. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1050503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1050503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]\n[VibrationExplosion] 시 진동 횟수 3 감소, 충전 횟수를 전부 소모하여 (소모한 충전 횟수 X 5)% 만큼 [VibrationExplosion]의 흐트러짐 피해량이 증가함 (최대 50%)
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nWhen triggering [VibrationExplosion], reduce [Vibration] Count by 3, then spend all Charge Count to further raise Stagger Threshold by (Charge Count x 5)% (Max 50%)
   PL:
321. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — podsumowanie] [OnSucceedAttack] [VibrationExplosion]. 진동 횟수 3 감소. 충전 횟수를 소모하여 흐트러짐 피해량이 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#3].coindescs[#0].summary ; dataList[id=1050503].levelList[level=4].coinlist[#3].coindescs[#0].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 3; Spend Charge Count to further raise Stagger Threshold
   PL:
322. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 진동 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050503].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 10+ [Vibration] Count, Coin Power +1
   PL:
323. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050504].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — nazwa] 만성 피로
   źródło: Passives.json :: dataList[id=1050501].name
   limit: do 40 znaków
   EN: Chronic Fatigue
   PL:
325. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — opis] 대상의 진동 이 5 이상이면 대상의 합 위력 -1\n흐트러짐 상태가 해제될 때 최대 체력의 5%만큼 체력 회복
   źródło: Passives.json :: dataList[id=1050501].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a clash, the opponent has -1 Clash Power if they have 5+ Tremor.\nWhen recovering from Stagger, heal 5% of Max HP.
   PL:
326. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 권고 휴직
   źródło: Passives.json :: dataList[id=1050521].name
   limit: do 40 znaków
   EN: Leave by Suggestion
   PL:
327. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 속도가 가장 빠른 아군 1명이 진동 이 부여된 적과 합 진행 시 적의 합 위력 -1
   źródło: Passives.json :: dataList[id=1050521].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed lowers the Clash Power of opponents that have Tremor by 1
   PL:
328. [Kwestia głosowa [get_10505_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=get_10505_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Kwestia głosowa [get_10505_1] (Identity Acquisition)] 음… 새로운 업무는 좌측에… 아, 호출이시군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=get_10505_1].dlg
   limit: do 120 znaków
   EN: Hm… You can place new assignments on the left— Ah, you called for me.
   PL:
330. [Kwestia głosowa [lobby_morning_10505_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=lobby_morning_10505_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Kwestia głosowa [lobby_morning_10505_1] (Morning Greeting)] …아침… 입니까? 이상하군요. 아직 퇴근을 누르지 않았는데.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=lobby_morning_10505_1].dlg
   limit: do 120 znaków
   EN: …Is it… morning? C’est étrange. I do not remember clocking out.
   PL:
332. [Kwestia głosowa [lobby_noon_10505_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=lobby_noon_10505_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Kwestia głosowa [lobby_noon_10505_1] (Afternoon Greeting)] 잠시… 눈 붙이겠습니다. 점심 식사는 먼저… 하십시오…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=lobby_noon_10505_1].dlg
   limit: do 120 znaków
   EN: Allow me… to nap for a moment. You can… have your lunch first…
   PL:
334. [Kwestia głosowa [lobby_night_10505_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=lobby_night_10505_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Kwestia głosowa [lobby_night_10505_1] (Evening Greeting)] 야간은 보통 외근입니다. 아, 저는 아까 눈을 붙여두어 괜찮습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=lobby_night_10505_1].dlg
   limit: do 140 znaków
   EN: My evenings are mostly occupied with outdoor assignments. Ah, I had my rest earlier today, so it’s fine.
   PL:
336. [Kwestia głosowa [smalltalk_10505_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Kwestia głosowa [smalltalk_10505_1] (Chatter #1)] 말씀하신 작업은 처리해 두었습니다. 총 네 분의 일감이 남아있어서, 다음 요청이 있으시다면 그 후에… 가능합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_1].dlg
   limit: do 230 znaków
   EN: I have taken care of the task you told me. I currently have assignments from four people, so if you have another request to make… It will have to wait until I’m done with these.
   PL:
338. [Kwestia głosowa [smalltalk_10505_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Kwestia głosowa [smalltalk_10505_2] (Chatter #2)] 퇴근… 하지 않은 지 조금 오래되었군요. 하지만, 부탁하신 일이 끝나지 않았으니 어쩔 수 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_2].dlg
   limit: do 170 znaków
   EN: It has… been quite some time since I clocked out last. However, I cannot leave while the work I’ve been entrusted with isn’t done.
   PL:
340. [Kwestia głosowa [smalltalk_10505_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Kwestia głosowa [smalltalk_10505_3] (Chatter #3)] 이 음료… 말입니까. 아뇨, 그다지 좋아하지는 않습니다. 피로를 단시간에 풀 수 있는 방법이 이것밖에 없을 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_3].dlg
   limit: do 180 znaków
   EN: You’re… curious about this drink, I see. No, it’s not my preference. It simply is the only method I have to relieve exhaustion quickly.
   PL:
342. [Kwestia głosowa [smalltalk_10505_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Kwestia głosowa [smalltalk_10505_4] (Post-Uptie Chat 1)] 일감을… 대신 처리해 주신다는 말씀이십니까?\n잘 이해가 되지 않는군요. 이것은 제게 맡겨진 일입니다. 나눌 필요는 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_4].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You’ll… do some of my work for me?\nI do not understand. These assignments are my responsibility. There is no need to share my burden.
   PL:
344. [Kwestia głosowa [smalltalk_10505_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Kwestia głosowa [smalltalk_10505_5] (Post-Uptie Chat 2)] 처음부터 이렇게 일이 많지는 않았습니다. 다만, 다른 분들이 일을 맡기셨고, 저는 그걸 할 수 있었을 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=smalltalk_10505_5].dlg
   limit: do 150 znaków
   EN: The workload wasn’t always this heavy. When others left their work to me, I simply proved capable of handling it.
   PL:
346. [Kwestia głosowa [neglect_10505_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=neglect_10505_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Kwestia głosowa [neglect_10505_1] (Idle)] ……. (조금 코고는 소리)
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=neglect_10505_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ……\n(He’s snoring softly)
   PL:
348. [Kwestia głosowa [gacksung_10505_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=gacksung_10505_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Kwestia głosowa [gacksung_10505_1] (Uptying)] 음. 연봉 인상입니까. 알겠습니다. 그럼 저는 남은 일을 끝내야 해서…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=gacksung_10505_1].dlg
   limit: do 120 znaków
   EN: Hm. You’re giving me a raise. Entendu. Pardon me then, as I have tasks to take care of…
   PL:
350. [Kwestia głosowa [formation_10505_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=formation_10505_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Kwestia głosowa [formation_10505_1] (Deployment)] 제가 필요하시군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=formation_10505_1].dlg
   limit: do 120 znaków
   EN: I see you need me.
   PL:
352. [Kwestia głosowa [battleentry_10505_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battleentry_10505_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Kwestia głosowa [battleentry_10505_1] (Stage Entry)] 외근, 시작합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battleentry_10505_1].dlg
   limit: do 120 znaków
   EN: Engaging in external assignment.
   PL:
354. [Kwestia głosowa [battle_select_10505_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_select_10505_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Kwestia głosowa [battle_select_10505_1] (Viewed in Battle)] 요청이라도 있으십니까.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_select_10505_1].dlg
   limit: do 120 znaków
   EN: I presume you have a request.
   PL:
356. [Kwestia głosowa [battle_endcommand_10505_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_endcommand_10505_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Kwestia głosowa [battle_endcommand_10505_1] (Commencing Attack)] 그렇게 하죠.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_endcommand_10505_1].dlg
   limit: do 120 znaków
   EN: Entendu, will do.
   PL:
358. [Kwestia głosowa [battle_enemy_break_10505_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_enemy_break_10505_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Kwestia głosowa [battle_enemy_break_10505_1] (Enemy Stagger)] 일이 끝나갈 조짐이 보이는군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_enemy_break_10505_1].dlg
   limit: do 120 znaków
   EN: The assignment is steadily approaching completion.
   PL:
360. [Kwestia głosowa [battle_break_10505_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_break_10505_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Kwestia głosowa [battle_break_10505_1] (Staggered)] 헉.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_break_10505_1].dlg
   limit: do 120 znaków
   EN: Gasp.
   PL:
362. [Kwestia głosowa [battle_kill_10505_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_kill_10505_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Kwestia głosowa [battle_kill_10505_1] (Enemy Killed)] 하나 마무리했습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_kill_10505_1].dlg
   limit: do 120 znaków
   EN: One has been taken care of.
   PL:
364. [Kwestia głosowa [battle_dead_10505_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_dead_10505_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Kwestia głosowa [battle_dead_10505_1] (Death)] 아… 잠시… 쉬겠습니다…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_dead_10505_1].dlg
   limit: do 120 znaków
   EN: Ah… Allow me… to rest for a moment…
   PL:
366. [Kwestia głosowa [choice_success_p_10505_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=choice_success_p_10505_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Kwestia głosowa [choice_success_p_10505_2] (Check Passed)] 정시 퇴근… 가능할 것 같군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=choice_success_p_10505_2].dlg
   limit: do 120 znaków
   EN: It appears I… will be able to leave work on time.
   PL:
368. [Kwestia głosowa [choice_fail_n_10505_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=choice_fail_n_10505_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Kwestia głosowa [choice_fail_n_10505_1] (Check Failed)] 야근은 확정… 이군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=choice_fail_n_10505_1].dlg
   limit: do 120 znaków
   EN: That has confirmed that I… will have overtime.
   PL:
370. [Kwestia głosowa [battle_clear_10505_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_clear_10505_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Kwestia głosowa [battle_clear_10505_1] (Victory Cry)] 완료했습니다. 사무소로 돌아가겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_clear_10505_1].dlg
   limit: do 120 znaków
   EN: Assignment complete. I’ll be returning to the office.
   PL:
372. [Kwestia głosowa [battle_clear_ex_10505_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_clear_ex_10505_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Kwestia głosowa [battle_clear_ex_10505_1] (Extra Conditions Fulfilled)] 완료했습니다. …현장 퇴근 말씀이십니까. 알겠습니다. 후우…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_clear_ex_10505_1].dlg
   limit: do 120 znaków
   EN: Assignment complete. …You mean that I can go home today. Entendu. Ouf…
   PL:
374. [Kwestia głosowa [battle_defeat_10505_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_defeat_10505_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Kwestia głosowa [battle_defeat_10505_1] (Defeat Wail)] 일이… 꼬였군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Kcorp_10505.json :: dataList[id=battle_defeat_10505_1].dlg
   limit: do 120 znaków
   EN: Things… have gotten complicated.
   PL:

## [000] R Corp. 4th Pack Rhino — Meursault — R사 제 4무리 코뿔소팀
- ID Tożsamości: `10506` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 95 · szybkość: 2–4 / 2–4 / 3–5 / 3–5
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Bleed

376. [Karta Tożsamości — tytuł] R사 제 4무리\n코뿔소팀
   źródło: Personalities.json :: dataList[id=10506].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nRhino
   PL:
377. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10506].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10506].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Karta Tożsamości — opis] 뫼르소의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10506].desc
   limit: do 120 znaków
   EN: Meursault’s 6th Identity
   PL:
380. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 육중한 충돌
   źródło: Skills.json :: dataList[id=1050601].levelList[level=1].name ; dataList[id=1050601].levelList[level=2].name ; dataList[id=1050601].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Weighty Bash
   PL:
381. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 충전 횟수가 10 이상이면, 최종 위력 + 1
   źródło: Skills.json :: dataList[id=1050601].levelList[level=1].desc
   limit: do 120 znaków
   EN: At 10+ Charge Count, Final Power +1
   PL:
382. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL:
383. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 충전 횟수가 10 이상이면, 최종 위력 + 1\n속도가 7 이상이면, 피해량 +25%
   źródło: Skills.json :: dataList[id=1050601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 10+ Charge Count, Final Power +1\nAt 7+ Speed, deal +25% Damage
   PL:
384. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL:
385. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 충전 횟수가 10 이상이면, 최종 위력 + 2\n속도가 7 이상이면, 피해량 +25%\n[WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050601].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: At 10+ Charge Count, Final Power +2\nAt 7+ Speed, deal +25% Damage\n[WhenUse] Gain +2 Charge Count
   PL:
386. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 부수기
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].name ; dataList[id=1050602].levelList[level=2].name ; dataList[id=1050602].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Demolish
   PL:
387. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +4 Charge Count
   PL:
388. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL:
389. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1050602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1050602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL:
390. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 속도가 7 이상이면, 이 스킬에서 증가시키는 출혈 횟수 +1
   źródło: Skills.json :: dataList[id=1050602].levelList[level=2].desc
   limit: do 120 znaków
   EN: At 7+ Speed, inflict +1 Bleed Count with this skill
   PL:
391. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 속도가 7 이상이면, 이 스킬에서 증가시키는 출혈 횟수 +1\n[WhenUse] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: At 7+ Speed, inflict +1 Bleed Count with this Skill\n[WhenUse] Gain +4 Charge Count
   PL:
392. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 코뿔소 돌진
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].name ; dataList[id=1050603].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 6 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Rhino Ram
   PL:
394. [Umiejętność 3 (×1) (ulepszenie 1) — opis] [WhenUse] 충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 10+ Charge Count, Coin Power +1
   PL:
395. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 2 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1050603].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 2 Charge Count; Inflict +1 Bleed Count
   PL:
397. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 충전 횟수 3 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=1050603].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 3 Charge Count; Inflict +1 Bleed Count
   PL:
398. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 2 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1050603].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 충전 횟수 3 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=1050603].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 충전 횟수가 10 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1050603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 10+ Charge Count, Coin Power +2
   PL:
402. [Obrona (ulepszenia 1,4) — nazwa] 생체 전류 감응
   źródło: Skills.json :: dataList[id=1050604].levelList[level=1].name ; dataList[id=1050604].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Bioelectricity Induction
   PL:
403. [Obrona (ulepszenie 1) — opis] [WhenUse] 보호막이 있는동안 피격 시 충전 횟수 1 증가 (턴 당 최대 10)
   źródło: Skills.json :: dataList[id=1050604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If attacked while shielded, gain +1 Charge Count (Max 10 per turn)
   PL:
404. [Obrona (ulepszenie 4) — opis] [WhenUse] 보호막이 있는동안 피격 시 충전 횟수 2 증가 (턴 당 최대 10)
   źródło: Skills.json :: dataList[id=1050604].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If attacked while shielded, gain +2 Charge Count (Max 10 per turn)
   PL:
405. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] rrR-#4 슈트 가압 가동
   źródło: Passives.json :: dataList[id=1050601].name
   limit: do 50 znaków
   EN: Activate rrR-#4 Suit Pressurization
   PL:
406. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] 턴 종료 시 충전 횟수 5당 다음 턴의 속도 최대 값 +2 (최대 6)
   źródło: Passives.json :: dataList[id=1050601].desc
   limit: do 120 znaków
   EN: At the end of the turn, Max Speed +2 (Capped at 6) per 5 Charge Count next turn.
   PL:
407. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 기동 훈련
   źródło: Passives.json :: dataList[id=1050621].name
   limit: do 40 znaków
   EN: Maneuver Training
   PL:
408. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 턴 종료 시 충전 횟수가 가장 높은 아군 1명이 충전 횟수 5당 다음 턴의 속도 최대 값 +1 (최대 3)
   źródło: Passives.json :: dataList[id=1050621].desc
   limit: do 170 znaków
   EN: At the end of the turn, 1 ally that has the highest Charge Count gains Max Speed +1 (Capped at 3) per 5 Charge Count next turn
   PL:
409. [Kwestia głosowa [get_10506_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=get_10506_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Kwestia głosowa [get_10506_1] (Identity Acquisition)] 준비되었습니다. 제가 앞장서도록 하죠.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=get_10506_1].dlg
   limit: do 120 znaków
   EN: I'm ready. Let me take the vanguard.
   PL:
411. [Kwestia głosowa [lobby_morning_10506_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=lobby_morning_10506_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Kwestia głosowa [lobby_morning_10506_1] (Morning Greeting)] 아침에 깨어날 때마다 다시 부화한 느낌이 듭니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=lobby_morning_10506_1].dlg
   limit: do 120 znaków
   EN: Every morning, I feel as though I am newly hatched.
   PL:
413. [Kwestia głosowa [lobby_noon_10506_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=lobby_noon_10506_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [lobby_noon_10506_1] (Afternoon Greeting)] 낮이군요. 기동 훈련을 수행할 시간입니다. 식사는, 간단하게 해결해 두었습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=lobby_noon_10506_1].dlg
   limit: do 120 znaków
   EN: It's afternoon—time for maneuver training. As for lunch, I had something simple.
   PL:
415. [Kwestia głosowa [lobby_night_10506_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=lobby_night_10506_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [lobby_night_10506_1] (Evening Greeting)] 밤이면 선별되었던 날들이 떠오릅니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=lobby_night_10506_1].dlg
   limit: do 120 znaków
   EN: Nighttime brings back memories of my selection.
   PL:
417. [Kwestia głosowa [smalltalk_10506_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [smalltalk_10506_1] (Chatter #1)] 이 슈트… 말씀이십니까. 죄송하지만, 이것은 저희 코뿔소 팀 외에는 사용할 수 없는 슈트입니다.\n무게도 문제지만, 생체전류와 감응해야 하기 때문에 별도의 시술 없이는 움직이지도 못하시게 될 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This suit...? I'm sorry, but only the Rhino Team can use this suit.\nYou won't be able to lift a finger without a special procedure allowing your bioelectricity to be detected by the suit, much less endure the suit's weight.
   PL:
419. [Kwestia głosowa [smalltalk_10506_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [smalltalk_10506_2] (Chatter #2)] 저희는 전투의 가장 앞을 담당합니다. 협력하는 이들을 위해, 모든 것을 튕겨내고 상대의 전열을 무너뜨리죠.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_2].dlg
   limit: do 130 znaków
   EN: We are vanguards of the battlefield. We defend those who work with us and disrupt the enemy lines.
   PL:
421. [Kwestia głosowa [smalltalk_10506_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [smalltalk_10506_3] (Chatter #3)] 훈련이 너무 잦아 보일 수 있겠지만… 모두 필요한 것입니다. 언제, 어디에 투입될지 모르기 때문입니다.\n…하지만 훈련에 적극 참여하는 자들이 드물긴 하군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_3].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The training may appear excessively frequent... yet it is all necessary. Unforeseen deployment may happen at any time.\n...Not many of them appear enthusiastic, however.
   PL:
423. [Kwestia głosowa [smalltalk_10506_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [smalltalk_10506_4] (Post-Uptie Chat 1)] 전투 경험이 떨어지는 경우는 솔직히, 많이 없습니다. 일단 R사에 입사하게 되면, 그 경험은 질리도록 쌓기 때문이죠…\n다시 떠올리고 싶진 않군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_4].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To be frank, not many are lacking in combat experience. Joining R Corp. means that you'll soon have plenty of it, that's why...\nI don't wish to recall them, however.
   PL:
425. [Kwestia głosowa [smalltalk_10506_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [smalltalk_10506_5] (Post-Uptie Chat 2)] 제가 저를 부수고 터트리는 경험은, 굉장히 불쾌한 경험입니다. 저는 그 필요성을 익히 알고 있기 때문에, 이해했지만…\n당신은 가능하면 경험하지 않았으면 좋겠군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=smalltalk_10506_5].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Breaking and bursting myself is an awfully unpleasant experience. I do understand its necessity, however...\nI hope you won't ever experience it yourself.
   PL:
427. [Kwestia głosowa [neglect_10506_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=neglect_10506_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [neglect_10506_1] (Idle)] 간단한 근력 운동을 하고 있기 좋은 시간이군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=neglect_10506_1].dlg
   limit: do 120 znaków
   EN: This seems like a good time to do some anaerobic exercise.
   PL:
429. [Kwestia głosowa [gacksung_10506_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=gacksung_10506_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [gacksung_10506_1] (Uptying)] 알겠습니다. 지원해주신 만큼, 확실한 전투 결과를 가져다 드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=gacksung_10506_1].dlg
   limit: do 120 znaków
   EN: Understood. I will bring you results that are as good as your support.
   PL:
431. [Kwestia głosowa [formation_10506_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=formation_10506_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [formation_10506_1] (Deployment)] 투입이군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=formation_10506_1].dlg
   limit: do 120 znaków
   EN: Deployment.
   PL:
433. [Kwestia głosowa [battleentry_10506_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battleentry_10506_1].desc
   limit: do 120 znaków
   EN: Entry
   PL:
434. [Kwestia głosowa [battleentry_10506_1] (Entry)] 슈트 가압… 실시.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battleentry_10506_1].dlg
   limit: do 120 znaków
   EN: Commencing... suit pressurization.
   PL:
435. [Kwestia głosowa [battle_select_10506_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_select_10506_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [battle_select_10506_1] (Viewed in Battle)] 이곳은 위험합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_select_10506_1].dlg
   limit: do 120 znaków
   EN: It's not safe here.
   PL:
437. [Kwestia głosowa [battle_endcommand_10506_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_endcommand_10506_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [battle_endcommand_10506_1] (Commencing Attack)] 흐읍!
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_endcommand_10506_1].dlg
   limit: do 120 znaków
   EN: Haah!
   PL:
439. [Kwestia głosowa [battle_enemy_break_10506_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_enemy_break_10506_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Kwestia głosowa [battle_enemy_break_10506_1] (Enemy Stagger)] 전열이 무너졌군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_enemy_break_10506_1].dlg
   limit: do 120 znaków
   EN: Their lines are broken.
   PL:
441. [Kwestia głosowa [battle_break_10506_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_break_10506_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [battle_break_10506_1] (Staggered)] 으음…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_break_10506_1].dlg
   limit: do 120 znaków
   EN: Hnnh...
   PL:
443. [Kwestia głosowa [battle_kill_10506_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_kill_10506_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [battle_kill_10506_1] (Enemy Killed)] 생명활동의 정지를 확인했다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_kill_10506_1].dlg
   limit: do 120 znaków
   EN: Confirming cessation of biological activity.
   PL:
445. [Kwestia głosowa [battle_dead_10506_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_dead_10506_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [battle_dead_10506_1] (Death)] 아… 다시 선별과정을 거쳐야 하는 것인가…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_dead_10506_1].dlg
   limit: do 120 znaków
   EN: Ah... must I repeat the selection process...?
   PL:
447. [Kwestia głosowa [choice_success_p_10506_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=choice_success_p_10506_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [choice_success_p_10506_2] (Check Passed)] 선별된 저의 성과입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=choice_success_p_10506_2].dlg
   limit: do 120 znaków
   EN: Selecting me brings success.
   PL:
449. [Kwestia głosowa [choice_fail_n_10506_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=choice_fail_n_10506_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [choice_fail_n_10506_1] (Check Failed)] 이런 상황은… 예측 못했군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=choice_fail_n_10506_1].dlg
   limit: do 120 znaków
   EN: I did not anticipate... this outcome.
   PL:
451. [Kwestia głosowa [battle_clear_10506_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_clear_10506_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Kwestia głosowa [battle_clear_10506_1] (Victory Cry)] 나쁘지 않은 결과 입니다. 오늘 부족했던 점은 훈련으로 충당하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_clear_10506_1].dlg
   limit: do 120 znaków
   EN: An adequate result. I will make up for the mistakes today with additional training.
   PL:
453. [Kwestia głosowa [battle_clear_ex_10506_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_clear_ex_10506_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Kwestia głosowa [battle_clear_ex_10506_1] (Extra Conditions Fulfilled)] 부족함이 없는 결과군요. 부화장의 엄격한 선별이 맺은 결실입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_clear_ex_10506_1].dlg
   limit: do 130 znaków
   EN: A flawless result. An outcome made possible by the rigorous selection process of the Hatchery.
   PL:
455. [Kwestia głosowa [battle_defeat_10506_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_defeat_10506_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Kwestia głosowa [battle_defeat_10506_1] (Defeat Wail)] 전투 경험이… 부족했군요… 다시 부화장으로 보내질테죠…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Rcorp_10506.json :: dataList[id=battle_defeat_10506_1].dlg
   limit: do 120 znaków
   EN: I lacked... combat experience... I will be sent back to the Hatchery, then...
   PL:

## [00] The Middle Little Brother — Meursault — 중지 작은 아우
- ID Tożsamości: `10507` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

457. [Karta Tożsamości — tytuł] 중지\n작은 아우
   źródło: Personalities.json :: dataList[id=10507].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Middle\nLittle Brother
   PL:
458. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10507].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10507].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Karta Tożsamości — opis] 뫼르소의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10507].desc
   limit: do 120 znaków
   EN: Meursault’s 7th Identity
   PL:
461. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 기억한다
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=1].name ; dataList[id=1050701].levelList[level=2].name ; dataList[id=1050701].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: We Remember
   PL:
462. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
463. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [DefeatDuel] 다음 턴에 질투 피해량 증가 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=2].desc ; dataList[id=1050701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 1 Envy DMG Up next turn
   PL:
465. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
466. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 의리 사슬
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].name ; dataList[id=1050702].levelList[level=2].name ; dataList[id=1050702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Chains of Loyalty
   PL:
468. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 질투 위력 증가 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].desc ; dataList[id=1050702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Envy Power Up to 2 allies adjacent to this unit on the Dashboard.
   PL:
469. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 질투 위력 증가 1 부여\n해당 슬롯에서 선택한 스킬이 질투 속성이면 추가로 질투 피해량 증가 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Envy Power Up to 2 allies adjacent to this unit on the Dashboard\nApply 1 Envy DMG Up as well when selecting Envy affinity Skills from the affected Skill Slots
   PL:
474. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 새긴다
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].name ; dataList[id=1050703].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Recording
   PL:
475. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 질투 공명이 4 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].desc
   limit: do 120 znaków
   EN: At 4+ Envy Reson., Coin Power +1
   PL:
476. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 앙갚음 대상 이면, 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Vengeance Mark, inflict 1 Plus Coin Drop next turn
   PL:
477. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 앙갚음 대상 이면, 다음 턴에 질투 취약 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Vengeance Mark, inflict 1 Envy Fragility next turn
   PL:
478. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 질투 공명이 4 이상이면 코인 위력 +1\n질투 완전 공명이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 4+ Envy Reson., Coin Power +1\nAt 6+ Envy A-Reson., Coin Power +1
   PL:
479. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 앙갚음 대상 이면, 다음 턴에 질투 취약 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Vengeance Mark, inflict 2 Envy Fragility next turn
   PL:
480. [Obrona (ulepszenia 1,4) — nazwa] 배로 갚기
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=1].name ; dataList[id=1050704].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Multifold Retribution
   PL:
481. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Obrona (ulepszenie 4) — opis] 질투 공명이 4 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=4].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 의리
   źródło: Passives.json :: dataList[id=1050701].name
   limit: do 40 znaków
   EN: Loyalty
   PL:
487. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] - 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 최종 위력 1 증가\n- 자신 이외의 중지 인격이 생존해있으면, 매 턴 종료 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1050701].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Final Power +1\n- If there is another surviving ally from the Middle, heal 6 SP at every Turn End
   PL:
488. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 의리
   źródło: Passives.json :: dataList[id=1050711].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] - 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 최종 위력 1 증가\n- 자신 이외의 중지 인격이 생존해있으면, 매 턴 종료 시 자신과 정신력이 가장 낮은 중지 인격 1명의 매 턴 종료 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1050711].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Final Power +1\n- If there is another surviving ally from the Middle other than this unit, this unit and the surviving ally from the Middle with the least SP both heal 6 SP at every Turn End
   PL:
490. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 한 식구
   źródło: Passives.json :: dataList[id=1050721].name
   limit: do 40 znaków
   EN: One Family
   PL:
491. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 정신력이 가장 낮은 아군 1명이 자신과 동일한 소속의 캐릭터가 생존해있는 경우, 턴 종료 시 정신력 10 회복
   źródło: Passives.json :: dataList[id=1050721].desc
   limit: do 130 znaków
   EN: The 1 ally with the least SP heals 10 SP at Turn End if there is another ally from the same Faction
   PL:
492. [Kwestia głosowa [get_10507_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=get_10507_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Kwestia głosowa [get_10507_1] (Identity Acquisition)] 뫼르소입니다. 작은 형님을 보필하고 있습니다. 이상입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=get_10507_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I am Meursault. I aid the Big Brother in his endeavors.\nThat is all.
   PL:
494. [Kwestia głosowa [lobby_morning_10507_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=lobby_morning_10507_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Kwestia głosowa [lobby_morning_10507_1] (Morning Greeting)] 일어나셨습니까. 함께 거실로 가시죠. 다른 아우들과 형님, 누님께서 이야기를 나누고 싶어하십니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=lobby_morning_10507_1].dlg
   limit: do 180 znaków
   EN: Good morning. Let us head to the living room together. My fellow junior Brothers, senior Brothers, and Sisters want to have a chat with you.
   PL:
496. [Kwestia głosowa [lobby_noon_10507_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=lobby_noon_10507_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Kwestia głosowa [lobby_noon_10507_1] (Afternoon Greeting)] 특별히 바깥 활동이 예정되어 있지 않으시다면, 남아 있는 식구들과 식사를 하시죠. 함께 떠들며 식사하는 것은 중지의 중요한 일과입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=lobby_noon_10507_1].dlg
   limit: do 220 znaków
   EN: If you have no particular outdoor activities scheduled, then join the other remaining family for a meal. It is important that the Middle always dine and chat together.
   PL:
498. [Kwestia głosowa [lobby_night_10507_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=lobby_night_10507_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Kwestia głosowa [lobby_night_10507_1] (Evening Greeting)] 저는… 형님께서 호출하셔서, 사업장에 가보아야 합니다. 형님과 나누는 술자리에 빠질 수는 없죠. 그것은 규율입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=lobby_night_10507_1].dlg
   limit: do 210 znaków
   EN: I... have been summoned by a senior Brother and must visit our site of business. I can not 'flake' on a drinking night with my senior Brothers. That is the rule.
   PL:
500. [Kwestia głosowa [smalltalk_10507_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Kwestia głosowa [smalltalk_10507_1] (Chatter #1)] 저희 아우들 사이에 서열은 없습니다. 그런 것이 중요하지도 않습니다. 형님을 보좌하며 서로가 밀어주고 당겨준다. 그뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_1].dlg
   limit: do 260 znaków
   EN: Us junior Brothers do not concern ourselves with seniority amongst ourselves. It is a detail of very little significance. All we wish to do is to support each other and our senior Brothers, and no more.
   PL:
502. [Kwestia głosowa [smalltalk_10507_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Kwestia głosowa [smalltalk_10507_2] (Chatter #2)] 식구 안에서 일어나는 사소한 실수. 그 실수를 나서서 덮어주는 것은 제 사소한 즐거움입니다. 그것이 의리라고 배웠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_2].dlg
   limit: do 200 znaków
   EN: Little mistakes may occur within a family. It is my little joy to sweep such little mistakes under the rug. I have been taught that that is true loyalty.
   PL:
504. [Kwestia głosowa [smalltalk_10507_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Kwestia głosowa [smalltalk_10507_3] (Chatter #3)] 이 사슬에는 결속과 연결이라는 의미가 깃들어있다고 합니다. 저희 모두, 같은 사슬에 연결되어 운명을 함께 하며 같은 것을 짊어지고 책임지는 것입니다.\n그 사슬을 벗을 필요도, 벗을 수도 없고, 벗으려는 자도 필요없겠지요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_3].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: These chains represent solidarity and connection. Together, we who are bound by the same chain bear the responsibilities hand in hand. We will face our destinies and share the weight together.\nWe have no need to remove these chains. We have no means to remove these chains. And we have no need for those who intend to remove these chains.
   PL:
506. [Kwestia głosowa [smalltalk_10507_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Kwestia głosowa [smalltalk_10507_4] (Post-Uptie Chat 1)] 앙갚음 장부에는 많은 것들이 쓰여있습니다. 동료가 죽었을 때의 복수법부터… 걷다가 발을 밟혔을 때 되갚음까지. 이번에 행할 것은… 3조 1항…
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_4].dlg
   limit: do 280 znaków
   EN: Many things are written in The Book of Vengeance. From instructions for avenging a Brother's death to instructions for avenging getting our foot stepped on in the streets. This time, I will refer to Title 3, Section 1...
   PL:
508. [Kwestia głosowa [smalltalk_10507_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Kwestia głosowa [smalltalk_10507_5] (Post-Uptie Chat 2)] 중지는 반드시 되돌려 줍니다. 우리 사람이 아니라면, 그 어떠한 일에도 사소함이란 있을 수 없는 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=smalltalk_10507_5].dlg
   limit: do 140 znaków
   EN: The Middle always pays their debts. There are no 'little mistakes', unless the mistake is from one of us.
   PL:
510. [Kwestia głosowa [neglect_10507_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=neglect_10507_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Kwestia głosowa [neglect_10507_1] (Idle)] 혼자만 있는 건… 익숙치 않군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=neglect_10507_1].dlg
   limit: do 120 znaków
   EN: I am not used to... being on my lonesome.
   PL:
512. [Kwestia głosowa [gacksung_10507_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=gacksung_10507_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Kwestia głosowa [gacksung_10507_1] (Uptying)] 어디서 무슨 일이라도 당했습니까? 이리 와서 자세히 설명해 보시죠. 장부에 적어두어 반드시 갚아드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=gacksung_10507_1].dlg
   limit: do 220 znaków
   EN: Has something happened to you? Please, come here and tell me what transpired, in full detail. I will add it to the Book of Vengeance so that this offense may be avenged.
   PL:
514. [Kwestia głosowa [formation_10507_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=formation_10507_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Kwestia głosowa [formation_10507_1] (Deployment)] 형님과 누님들을 위해.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=formation_10507_1].dlg
   limit: do 120 znaków
   EN: For my senior Brothers and Sisters.
   PL:
516. [Kwestia głosowa [battleentry_10507_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battleentry_10507_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Kwestia głosowa [battleentry_10507_1] (Stage Entry)] 몸을 풀어두죠.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battleentry_10507_1].dlg
   limit: do 120 znaków
   EN: I will conduct a warm-up exercise.
   PL:
518. [Kwestia głosowa [battle_select_10507_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_select_10507_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Kwestia głosowa [battle_select_10507_1] (Viewed in Battle)] 장부를 읽고 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_select_10507_1].dlg
   limit: do 120 znaków
   EN: I am reading the Book.
   PL:
520. [Kwestia głosowa [battle_endcommand_10507_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_endcommand_10507_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Kwestia głosowa [battle_endcommand_10507_1] (Commencing Attack)] 되갚아주마.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_endcommand_10507_1].dlg
   limit: do 120 znaków
   EN: Vengeance comes for you.
   PL:
522. [Kwestia głosowa [battle_enemy_break_10507_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_enemy_break_10507_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Kwestia głosowa [battle_enemy_break_10507_1] (Enemy Stagger)] 그 정도 각오로 우리 식구를 건드렸나.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_enemy_break_10507_1].dlg
   limit: do 120 znaków
   EN: You should have prepared for retribution when you slighted a member of our family.
   PL:
524. [Kwestia głosowa [battle_break_10507_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_break_10507_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Kwestia głosowa [battle_break_10507_1] (Staggered)] 큭.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_break_10507_1].dlg
   limit: do 120 znaków
   EN: Kgh.
   PL:
526. [Kwestia głosowa [battle_kill_10507_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_kill_10507_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Kwestia głosowa [battle_kill_10507_1] (Enemy Killed)] 되갚았습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_kill_10507_1].dlg
   limit: do 120 znaków
   EN: Vengeance has been executed.
   PL:
528. [Kwestia głosowa [battle_dead_10507_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_dead_10507_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Kwestia głosowa [battle_dead_10507_1] (Death)] 나로… 끝나지는 않…을 것이다… 중지는 기억한다…
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_dead_10507_1].dlg
   limit: do 120 znaków
   EN: I won't... Be the last... of us... The Middle... Remembers...
   PL:
530. [Kwestia głosowa [choice_success_p_10507_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=choice_success_p_10507_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Kwestia głosowa [choice_success_p_10507_2] (Check Passed)] 음, 가능했군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=choice_success_p_10507_2].dlg
   limit: do 120 znaków
   EN: Hm. I have done it.
   PL:
532. [Kwestia głosowa [choice_fail_n_10507_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=choice_fail_n_10507_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Kwestia głosowa [choice_fail_n_10507_1] (Check Failed)] …저보다 적합한 식구가 해줄 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=choice_fail_n_10507_1].dlg
   limit: do 120 znaków
   EN: ... A family member better suited for this job will take over.
   PL:
534. [Kwestia głosowa [battle_clear_10507_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_clear_10507_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Kwestia głosowa [battle_clear_10507_1] (Victory Cry)] 처리했으니, 장부에서 한 줄 그어도 되겠군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_clear_10507_1].dlg
   limit: do 120 znaków
   EN: This has been taken care of. We can cross that out from the Book of Vengeance.
   PL:
536. [Kwestia głosowa [battle_clear_ex_10507_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_clear_ex_10507_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Kwestia głosowa [battle_clear_ex_10507_1] (Extra Conditions Fulfilled)] 앙갚음 장부대로 받은 것을 돌려주었습니다. 이것이 가족을 건드렸을 때의 결과입니다. 기억하셔야 합니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_clear_ex_10507_1].dlg
   limit: do 210 znaków
   EN: Conditions as written on the Book of Vengeance have been fulfilled. This is what happens when one lays their hands upon a member of our family. Do not forget that.
   PL:
538. [Kwestia głosowa [battle_defeat_10507_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_defeat_10507_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Kwestia głosowa [battle_defeat_10507_1] (Defeat Wail)] 괜찮습니다. 저들의 만행은 장부에 적혔습니다… 중지는 기억합니다. 그러니 기필코 식구들이 나설겁니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_MiddleFinger_10507.json :: dataList[id=battle_defeat_10507_1].dlg
   limit: do 190 znaków
   EN: It is all right. Their crimes are now written in the Book of Vengeance... The Middle remembers. The family will now come to claim their vengeance.
   PL:

## [000] Blade Lineage Mentor — Meursault — 검계 우두머리
- ID Tożsamości: `10508` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise

540. [Karta Tożsamości — tytuł] 검계\n우두머리
   źródło: Personalities.json :: dataList[id=10508].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nMentor
   PL:
541. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10508].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10508].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Karta Tożsamości — opis] 뫼르소의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10508].desc
   limit: do 120 znaków
   EN: Meursault’s 8th Identity
   PL:
544. [Umiejętność 1 (×3) (ulepszenia 1–4) — nazwa] 발검
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].name ; dataList[id=1050801].levelList[level=2].name ; dataList[id=1050801].levelList[level=3].name ; dataList[id=1050801].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Draw of the Sword
   PL:
545. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
546. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL:
547. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier1] 1 부여 (최대 2회)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BladeResultUpTier1], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier1] = 본국검 - 세법 전수 / Sword of the Homeland - Rending; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[StartBattle] Apply 1 [BladeResultUpTier1] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)\n</style>[WhenUse] Gain +2 [Breath] Count
   PL:
549. [Umiejętność 1 (×3) (ulepszenia 2–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050801].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL:
550. [Umiejętność 1 (×3) (ulepszenia 2–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050801].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1050801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Umiejętność 1 (×3) (ulepszenie 3) — opis] [StartBattle_Force] <color=#EBCAA2>자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier1] 1 부여 (최대 2회)</color>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#EBCAA2>, </color>, \n, [StartBattle_Force], [BladeResultUpTier1], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle_Force] = [전투 시작시] / [Combat Start]; [BladeResultUpTier1] = 본국검 - 세법 전수 / Sword of the Homeland - Rending; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [StartBattle_Force] <color=#EBCAA2>Apply 1 [BladeResultUpTier1] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)</color>\n[WhenUse] Gain +2 [Breath] Count
   PL:
552. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 5 이상이면 코인 위력 +1</style>\n[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier1] 1 부여 (최대 2회)\n<style="highlight">- 검계 조직원이 6명 이상 전투에 참여했으면, 대신 2 부여</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [StartBattle], [BladeResultUpTier1], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier1] = 본국검 - 세법 전수 / Sword of the Homeland - Rending; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 5+ [Breath], Coin Power +1</style>\n[StartBattle] Apply 1 [BladeResultUpTier1] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)\n<style="highlight">- If there are 6 or more allied Blade Lineage Identities in the Encounter, apply 2 instead</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
553. [Umiejętność 2 (×2) (ulepszenia 1–4) — nazwa] 자법
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].name ; dataList[id=1050802].levelList[level=2].name ; dataList[id=1050802].levelList[level=3].name ; dataList[id=1050802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Acupuncture
   PL:
554. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL:
555. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 3 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 3 [Breath]
   PL:
556. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
557. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier2] 1 부여 (최대 2회)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BladeResultUpTier2], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier2] = 본국검 - 자법 전수 / Sword of the Homeland - Penetrating; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[StartBattle] Apply 1 [BladeResultUpTier2] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)</style>\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL:
558. [Umiejętność 2 (×2) (ulepszenia 2–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050802].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL:
559. [Umiejętność 2 (×2) (ulepszenia 2–3) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +40%
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1050802].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +40% Damage on Critical Hit
   PL:
560. [Umiejętność 2 (×2) (ulepszenie 3) — opis] [StartBattle_Force] <color=#EBCAA2>자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier2] 1 부여 (최대 2회)</color>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#EBCAA2>, </color>, \n, [StartBattle_Force], [BladeResultUpTier2], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [StartBattle_Force] = [전투 시작시] / [Combat Start]; [BladeResultUpTier2] = 본국검 - 자법 전수 / Sword of the Homeland - Penetrating; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [StartBattle_Force] <color=#EBCAA2>Apply 1 [BladeResultUpTier2] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)</color>\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL:
561. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 7 이상이면 코인 위력 +1</style>\n[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier2] 1 부여 (최대 2회)\n<style="highlight">- 검계 조직원이 6명 이상 전투에 참여했으면, 대신 2 부여</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=4].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [StartBattle], [BladeResultUpTier2], [WhenUse], [WinDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier2] = 본국검 - 자법 전수 / Sword of the Homeland - Penetrating; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">At 7+ [Breath], Coin Power +1</style>\n[StartBattle] Apply 1 [BladeResultUpTier2] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)\n<style="highlight">- If there are 6 or more allied Blade Lineage Identities in the Encounter, apply 2 instead</style>\n[WhenUse] Gain +3 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL:
562. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +60%
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +60% Damage on Critical Hit
   PL:
563. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 육참
   źródło: Skills_personality-05.json :: dataList[id=1050803].levelList[level=3].name ; dataList[id=1050803].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 20 · monety: 1 (−8)
   limit: do 40 znaków
   EN: Yield My Flesh
   PL:
564. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WinDuel] [Breath] 5 얻음\n[DefeatDuel] 피격 후 골단 스킬 사용\n[CriticalActivated] 호흡 위력 1당 크리티컬 피해량 +2% (최대 50%)\n크리티컬 피해량 +15%\n 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)
   źródło: Skills_personality-05.json :: dataList[id=1050803].levelList[level=3].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [Breath], [DefeatDuel], [CriticalActivated]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [CriticalActivated] = [크리티컬 발동 시] / [On Crit]
   EN: [WhenUse] Gain +3 Aggro to this Skill Slot next turn\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WinDuel] Gain 5 [Breath]\n[DefeatDuel] After getting hit, use 'To Claim Their Bones' Skill\n[CriticalActivated] Deal +2% damage on Critical Hit for every Poise Potency on self (Max 50%)\n+15% Damage on Critical Hit\nDeal +0.5% damage per 1% missing HP on self (Max 25%)
   PL:
565. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WinDuel] [Breath] 5 얻음\n[DefeatDuel] 피격 후 골단 스킬 사용\n[CriticalActivated] 호흡 위력 1당 크리티컬 피해량 +3% (최대 75%)\n크리티컬 피해량 +30%\n 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)
   źródło: Skills_personality-05.json :: dataList[id=1050803].levelList[level=4].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [Breath], [DefeatDuel], [CriticalActivated]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [CriticalActivated] = [크리티컬 발동 시] / [On Crit]
   EN: [WhenUse] Gain +3 Aggro to this Skill Slot next turn\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WinDuel] Gain 5 [Breath]\n[DefeatDuel] After getting hit, use 'To Claim Their Bones' Skill\n[CriticalActivated] Deal +3% damage on Critical Hit for every Poise Potency on self (Max 75%)\n+30% Damage on Critical Hit\nDeal +0.5% damage per 1% missing HP on self (Max 25%)
   PL:
566. [Obrona (ulepszenia 1,4) — nazwa] 살주
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=1].name ; dataList[id=1050804].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Overthrow
   PL:
567. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 참격 위력 증가 1을 얻음 (최대 1회)
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Slash Power Up next turn (1 time max)
   PL:
568. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050804].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
569. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 참격 위력 증가 1을 얻음 (최대 1회)\n<style="highlight">잃은 체력 1% 당 피해량 0.5% 증가 (최대 25%)</style>
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Slash Power Up next turn (1 time max)\n<style="highlight">Deal +0.5% damage for every 1% missing HP on self (Max 25%)</style>
   PL:
570. [Obrona (ulepszenia 1,4) — nazwa] 골단
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].name ; dataList[id=1050805].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 4 · monety: 4 (+4)
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL:
571. [Obrona (ulepszenie 1) — opis] [BeforeAttack] 자신의 [Breath]이 10 이상이면 공격 가중치 +1\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 호흡 위력 1당  크리티컬 피해량 + 2% (최대 50%)\n크리티컬 피해량 +20%\n자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Breath], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] At 10+ [Breath], Atk Weight +1\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WhenUse] Deal +2% damage on Critical Hit for every Poise Potency on self (Max 50%)\n+20% Damage on Critical Hit\nDeal +0.5% damage per 1% missing HP on self (Max 25%)
   PL:
572. [Obrona (ulepszenia 1,4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1050805].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
573. [Obrona (ulepszenia 1,4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].coinlist[#3].coindescs[#1].desc ; dataList[id=1050805].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze next turn
   PL:
574. [Obrona (ulepszenie 4) — opis] <style="highlight">[BeforeAttack] 자신의 [Breath] 7당 공격 가중치 +1 (최대 2)</style>\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 호흡 위력 1당  크리티컬 피해량 + 2% (최대 50%)\n크리티컬 피해량 +<style="highlight">30</style>%\n자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)\n<style="highlight">타겟이 1명이면, 피해량 +100% (집중 전투에서는 부위로 판정)</style>
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Breath], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">[BeforeAttack] For every 7 [Breath] on self, Atk Weight +1 (Max +2)</style>\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WhenUse] Deal +2% damage on Critical Hit for every Poise Potency on self (Max 50%)\n+<style="highlight">30</style>% Damage on Critical Hit\nDeal +0.5% damage for every 1% missing HP on self (Max 25%)\n<style="highlight">If this Skill targets only a single enemy, deal +100% damage (In Focused Encounters, a single Part)</style>
   PL:
575. [Pasywka bojowa (od ulepszenia 1) — nazwa] 추모
   źródło: Passives.json :: dataList[id=1050802].name
   limit: do 40 znaków
   EN: In Memoriam
   PL:
576. [Pasywka bojowa (od ulepszenia 1) — opis] 자신을 제외한 검계 조직원이 3명 이상 사망한 경우\n- 자신의 스킬, 코인 효과로 호흡 위력, 횟수를 얻을 때, 호흡 위력, 횟수 1 추가 증가\n- 검계 조직원이 5명 이상 사망한 경우, 대신 2 증가\n- 전투 시작 시 자신에게 [SwordPlayOfTheHomeland] 부여
   źródło: Passives.json :: dataList[id=1050802].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [SwordPlayOfTheHomeland]
   znaczenie tagów: [SwordPlayOfTheHomeland] = 본국검술 / Swordplay of the Homeland
   EN: When 3 or more other Blade Lineage allies are defeated:\n- When gaining Poise Potency/Count using this unit's own Skills and Coin effects: Gain 1 more of each\n- When 5 or more other Blade Lineage allies are defeated, gain 2 more of each instead\n- Combat Start: Apply [SwordPlayOfTheHomeland] on self
   PL:
577. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 본국검술
   źródło: Passives.json :: dataList[id=1050801].name
   limit: do 40 znaków
   EN: Swordplay of the Homeland
   PL:
578. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)\n\n자신의 스킬, 코인 효과로 [Breath] 위력, 횟수를 얻을 때, 자신을 제외한 [Breath]이 없거나, 가장 낮은 검계 인격 2명의 [Breath] 위력, 횟수 1 증가\n- 전투에 참여한 검계 조직원이 6명 이상이면, 대신 2 증가
   źródło: Passives.json :: dataList[id=1050801].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn (once per Encounter)\n\nWhen this unit gains [Breath] Potency/Count using its own Skill or Coin effects: Give 1 [Breath] Potency and +1 [Breath] Count to 2 other Blade Lineage allies that have no [Breath] or have the least [Breath]\n- If there are 6 or more Blade Lineage allies participating in this Encounter, give 2 [Breath] Potency and +2 [Breath] Count instead
   PL:
579. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — nazwa] 본국검술
   źródło: Passives.json :: dataList[id=1050811].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)\n\n자신의 스킬, 코인 효과로 [Breath] 위력, 횟수를 얻을 때, 자신을 제외한 [Breath]이 없거나, 가장 낮은 검계 인격 2명의 [Breath] 위력, 횟수 1 증가\n- 전투에 참여한 검계 조직원이 6명 이상이면, 대신 2 증가\n\n<style="highlight">전투 시작 시 자신을 제외한 검계 조직원에게 [SwordPlayOfTheHomeland] 부여</style>
   źródło: Passives.json :: dataList[id=1050811].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [SwordPlayOfTheHomeland]
   znaczenie tagów: [Breath] = 호흡 / Poise; [SwordPlayOfTheHomeland] = 본국검술 / Swordplay of the Homeland
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn (once per Encounter)\n\nWhen this unit gains [Breath] Potency/Count using its own Skill or Coin effects: Give 1 [Breath] Potency and +1 [Breath] Count to 2 other Blade Lineage allies that have no [Breath] or have the least [Breath]\n- If there are 6 or more Blade Lineage allies participating in this Encounter, give 2 [Breath] Potency and +2 [Breath] Count instead\n\n<style="highlight">Combat Start: Apply [SwordPlayOfTheHomeland] buff to all other Blade Lineage allies</style>
   PL:
581. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 본국검술
   źródło: Passives.json :: dataList[id=1050821].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] 전투 시작 시 [Breath]을 가장 많이 보유한 아군 1명의 참격 속성 스킬의 크리티컬 피해량 +15%
   źródło: Passives.json :: dataList[id=1050821].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Combat Start: 1 ally that has the most [Breath] deals +15% damage on Critical Hit using Slash Skills
   PL:
583. [Kwestia głosowa [get_10508_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=get_10508_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [get_10508_1] (Identity Acquisition)] 착수하지 않는 겁니까. 음. 돌을 던질 수밖에 없는 형국이군요, 우리는.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=get_10508_1].dlg
   limit: do 120 znaków
   EN: We are not placing our stone here, then? Mm, then the tides drive us to resign.
   PL:
585. [Kwestia głosowa [lobby_morning_10508_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=lobby_morning_10508_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [lobby_morning_10508_1] (Morning Greeting)] 아침은 이르게 시작하는 것이 좋다. 생각해야 할 것도, 행동해야 할 것도 많으니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=lobby_morning_10508_1].dlg
   limit: do 120 znaków
   EN: A morning must start early. There is much to process and much to do.
   PL:
587. [Kwestia głosowa [lobby_noon_10508_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=lobby_noon_10508_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [lobby_noon_10508_1] (Afternoon Greeting)] 일정이 비어있다면, 한 국 어떻겠는가. 잠시 생각을 체계화할 시간이 필요해서.\n우리가 정착할 곳을 찾기 위한 고민이 필요하므로.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=lobby_noon_10508_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Would you join me for a round of baduk if there is a vacancy in your schedule? I require some time to systemize my thoughts.\nI must contemplate where I may find our new home.
   PL:
589. [Kwestia głosowa [lobby_night_10508_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=lobby_night_10508_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [lobby_night_10508_1] (Evening Greeting)] 달빛이 강할 때는 주의하는 편이 좋다. 몸에 베인 상처들을 바깥으로 내보이는 것은 좋지 않으니까.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=lobby_night_10508_1].dlg
   limit: do 130 znaków
   EN: Always remain watchful under a bright moonlight. One must keep their wounds and scars out of sight.
   PL:
591. [Kwestia głosowa [smalltalk_10508_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [smalltalk_10508_1] (Chatter #1)] 검을 다룰 때는 망설이지 않아야 한다. 망설임이 있다는 것은… 곧 검을 그만큼 덜 다루어봤다는 의미가 되니, 연습에 매진하도록.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_1].dlg
   limit: do 200 znaków
   EN: Do not hesitate when wielding a blade, for hesitation is a sign of an underdeveloped familiarity with the blade. Train yourself to reach greater heights.
   PL:
593. [Kwestia głosowa [smalltalk_10508_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [smalltalk_10508_2] (Chatter #2)] 바둑은 상대를 앞에 두고 어떻게 싸울 것인가를 살피기에 적합한 놀이다.\n수를 쌓아가면, 그 안에 상대가 무슨 생각을 하는지도 자연히 읽히지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_2].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One can learn the opponent's strategies by playing a game of baduk with them.\nThe further the game progresses, the more moves the opponent makes, the easier it becomes to read them.
   PL:
595. [Kwestia głosowa [smalltalk_10508_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [smalltalk_10508_3] (Chatter #3)] 곧 큰 난이 벌어질 것만 같다. 나는 호위를 부탁받은 몸이니, 끝까지 지키려 하겠으나… 어쩌면, S사에서 설 자리를 잃게 될지도 모르겠지.\n지켜야할 그 분이나, 나와 친우들도.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_3].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I expect that turmoil shall visit us soon. I have been tasked with the role of a protector, so I shall do my duty to the bitter end. \n...Yet I foresee that my fellows, the one I must protect, and I may lose my place at S Corp.
   PL:
597. [Kwestia głosowa [smalltalk_10508_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [smalltalk_10508_4] (Post-Uptie Chat 1)] 역마의 삶을 살 것이라 누군가 말했을 땐 코웃음을 쳤으나… 이제는 정말, 떠돌이의 삶을 살게 되겠군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_4].dlg
   limit: do 210 znaków
   EN: When someone had once told me that I would live the life of a vagrant, I had scoffed at the notion. ... I suppose I shall truly live a life of a wanderer, now.
   PL:
599. [Kwestia głosowa [smalltalk_10508_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [smalltalk_10508_5] (Post-Uptie Chat 2)] 살을 찢고, 뼈를 절단한다. 그 말은 곧, 한 번 검을 내려칠 때 뼈까지 갈라낼 정도로 집중을 해야 한다는 의미다.\n직접 보고, 몸에 새기도록.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=smalltalk_10508_5].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tear the flesh and hew the bones. In other words, one must maintain utmost focus until the blade cleaves clean through the bones. I will demonstrate, and you will learn.
   PL:
601. [Kwestia głosowa [neglect_10508_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=neglect_10508_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [neglect_10508_1] (Idle)] …음. 초읽기를 시작하지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=neglect_10508_1].dlg
   limit: do 120 znaków
   EN: ... Mm. I will start the countdown.
   PL:
603. [Kwestia głosowa [gacksung_10508_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=gacksung_10508_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [gacksung_10508_1] (Uptying)] 얼마나 자객을 보내든, 결국 내게는 반상 앞의 한 수일 뿐이다.\n아직 나의 한 수는 끝나지 않았는데… 응수할텐가?
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=gacksung_10508_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No matter how many assassins they send, they are nothing before me but the placement of a single stone in a game of baduk.\nMy play has yet to flourish... will you respond nevertheless?
   PL:
605. [Kwestia głosowa [formation_10508_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=formation_10508_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [formation_10508_1] (Deployment)] 화점에 두지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=formation_10508_1].dlg
   limit: do 120 znaków
   EN: I place my stone at a flower point.
   PL:
607. [Kwestia głosowa [battleentry_10508_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battleentry_10508_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [battleentry_10508_1] (Stage Entry)] 착수.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battleentry_10508_1].dlg
   limit: do 120 znaków
   EN: My play.
   PL:
609. [Kwestia głosowa [battle_select_10508_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_select_10508_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [battle_select_10508_1] (Viewed in Battle)] 훈수는, 금기다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_select_10508_1].dlg
   limit: do 120 znaków
   EN: I will not accept any unsolicited advice.
   PL:
611. [Kwestia głosowa [battle_endcommand_10508_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_endcommand_10508_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [battle_endcommand_10508_1] (Commencing Attack)] 벤다면, 사활을 건다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_endcommand_10508_1].dlg
   limit: do 120 znaków
   EN: If you will cut... then wager your life on it.
   PL:
613. [Kwestia głosowa [battle_enemy_break_10508_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_enemy_break_10508_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [battle_enemy_break_10508_1] (Enemy Stagger)] 살을 베어내고,
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_enemy_break_10508_1].dlg
   limit: do 120 znaków
   EN: Yield the flesh.
   PL:
615. [Kwestia głosowa [battle_break_10508_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_break_10508_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [battle_break_10508_1] (Staggered)] 자충… 수인가.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_break_10508_1].dlg
   limit: do 120 znaków
   EN: A defeat of my own making...
   PL:
617. [Kwestia głosowa [battle_kill_10508_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_kill_10508_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Kwestia głosowa [battle_kill_10508_1] (Enemy Killed)] 뼈를 깎는다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_kill_10508_1].dlg
   limit: do 120 znaków
   EN: To claim the bones.
   PL:
619. [Kwestia głosowa [battle_dead_10508_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_dead_10508_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Kwestia głosowa [battle_dead_10508_1] (Death)] 아… 친우들을 볼 면목이… 없군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_dead_10508_1].dlg
   limit: do 120 znaków
   EN: Ah... how will I stand tall before my... fellows...?
   PL:
621. [Kwestia głosowa [choice_success_p_10508_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=choice_success_p_10508_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Kwestia głosowa [choice_success_p_10508_2] (Check Passed)] 묘수로군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=choice_success_p_10508_2].dlg
   limit: do 120 znaków
   EN: A wise move.
   PL:
623. [Kwestia głosowa [choice_fail_n_10508_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=choice_fail_n_10508_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Kwestia głosowa [choice_fail_n_10508_1] (Check Failed)] 악수로군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=choice_fail_n_10508_1].dlg
   limit: do 120 znaków
   EN: A witless move.
   PL:
625. [Kwestia głosowa [battle_clear_10508_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_clear_10508_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Kwestia głosowa [battle_clear_10508_1] (Victory Cry)] 치열했으나, 좋은 끝내기였다. 이제 우리의 활로를 찾을 수 있겠군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_clear_10508_1].dlg
   limit: do 130 znaków
   EN: The endgame of this match was close yet conclusive. We may now freely seek the path to our survival.
   PL:
627. [Kwestia głosowa [battle_clear_ex_10508_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_clear_ex_10508_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Kwestia głosowa [battle_clear_ex_10508_1] (Extra Conditions Fulfilled)] 승부수가 먹혀들었군. 판세는 완벽히 우리에게 있었다. 정착지를 찾을 때까지, 이 기세를 잃지 않기를.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_clear_ex_10508_1].dlg
   limit: do 160 znaków
   EN: My stratagem worked, and the tide of this battle was in our favor. Let this tide continue until we find us a new home.
   PL:
629. [Kwestia głosowa [battle_defeat_10508_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_defeat_10508_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Kwestia głosowa [battle_defeat_10508_1] (Defeat Wail)] 패착이 있었나. 이렇게 몸에 칼자국이 하나 더 새겨지는군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_SwordGroup_10508.json :: dataList[id=battle_defeat_10508_1].dlg
   limit: do 120 znaków
   EN: I must have made a losing move. Thus I yield my flesh to another scar.
   PL:

## [00] Dead Rabbits Boss — Meursault — 데드레빗츠 보스
- ID Tożsamości: `10509` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 76 · szybkość: 3–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Rupture

631. [Karta Tożsamości — tytuł] 데드레빗츠\n보스
   źródło: Personalities.json :: dataList[id=10509].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dead Rabbits\nBoss
   PL:
632. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10509].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10509].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Karta Tożsamości — opis] 뫼르소의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10509].desc
   limit: do 120 znaków
   EN: Meursault’s 9th Identity
   PL:
635. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 배트치기
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=1].name ; dataList[id=1050901].levelList[level=2].name ; dataList[id=1050901].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Bat Strike
   PL:
636. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL:
637. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Burst]이 5 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +1
   PL:
638. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
639. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Burst]이 5 이상이면 코인 위력 +<style="highlight">2</style>
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +<style="highlight">2</style>
   PL:
640. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 내려박기
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=1].name ; dataList[id=1050902].levelList[level=2].name ; dataList[id=1050902].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Smackdown
   PL:
641. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050902].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 6 이상이면 [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1050902].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 6+ [Burst], inflict 2 [AttackDown]
   PL:
643. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuel] Inflict +2 [Burst] Count
   PL:
644. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1</style>\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] If target has 6+ [Burst], Coin Power +1</style>\n[WinDuel] Inflict +2 [Burst] Count
   PL:
645. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 4 이상이면 [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 4+ [Burst], inflict 2 [AttackDown]
   PL:
646. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 쏟아내기
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].name ; dataList[id=1050903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Relentless
   PL:
647. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1\n[WinDuel] [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1\n[WinDuel] Inflict 2 [AttackDown]
   PL:
648. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1050903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL:
649. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 6 이상이면, 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1050903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 6+ [Burst], inflict 2 [AttackDown] next turn
   PL:
650. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Burst]이 3 이상이면 합 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1\n[WinDuel] [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: <style="highlight">[WhenUse] If target has 3+ [Burst], Clash Power +1</style>\n[WhenUse] If target has 6+ [Burst], Coin Power +1\n[WinDuel] Inflict 2 [AttackDown]
   PL:
651. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills_personality-05.json :: dataList[id=1050904].levelList[level=1].name ; dataList[id=1050904].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Counter
   PL:
652. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050904].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050904].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
653. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — nazwa] 시간 벌기
   źródło: Passives.json :: dataList[id=1050901].name
   limit: do 40 znaków
   EN: Buy Time
   PL:
654. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — opis] [Burst]이 있는 대상과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1050901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Clash Power +1 in a Clash against targets that have [Burst]
   PL:
655. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — podsumowanie] [Burst]이 있는 대상과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1050901].summary
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Glut.) — nazwa] 시간 벌기
   źródło: Passives.json :: dataList[id=1050911].name
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Glut.) — opis] [Burst]이 있는 대상과 합 진행 시 합 위력 +1\n대상의 [Burst] 횟수가 5 이상이면, 합 위력 +2
   źródło: Passives.json :: dataList[id=1050911].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Clash Power +1 against targets that have [Burst]\nClash Power +2 if the target has 5+ [Burst] Count
   PL:
658. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 내가 책임진다
   źródło: Passives.json :: dataList[id=1050921].name
   limit: do 40 znaków
   EN: My Responsibility
   PL:
659. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 속도가 가장 빠른 아군 1명이 [Burst]이 6 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여 (적 1명 당 턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1050921].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: When 1 ally with the fastest Speed hits an enemy that has 6+ [Burst], inflict 1 [AttackDown] (3 times per enemy per turn)
   PL:
660. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — podsumowanie] [Burst]이 6 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여
   źródło: Passives.json :: dataList[id=1050921].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Inflict 1 [AttackDown] On Hit against targets that have 6+ [Burst]
   PL:
661. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Glut.) — nazwa] 내가 책임진다
   źródło: Passives.json :: dataList[id=1050931].name
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Glut.) — opis] 속도가 가장 빠른 아군 1명이 [Burst]이 3 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여 (적 1명 당 턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1050931].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: When 1 ally with the fastest Speed hits an enemy that has 3+ [Burst], inflict 1 [AttackDown] (3 times per enemy per turn)
   PL:
663. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Glut.) — podsumowanie] [Burst]이 3 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여
   źródło: Passives.json :: dataList[id=1050931].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Inflict 1 [AttackDown] On Hit against targets that have 3+ [Burst]
   PL:
664. [Kwestia głosowa [get_10509_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=get_10509_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Kwestia głosowa [get_10509_1] (Identity Acquisition)] 비가 추적추적 내리는데…\n이런 날 누가 찾아올 줄은 몰랐군. 술에 절은 개인가?
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=get_10509_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... I was not expecting any guests on such a drizzling day. \nWhat are you, a hound drenched in alcohol?
   PL:
666. [Kwestia głosowa [lobby_morning_10509_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=lobby_morning_10509_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Kwestia głosowa [lobby_morning_10509_1] (Morning Greeting)] 해가 떴군. 오늘도 각자 맡은 담당 거리로 나간다. 관리할 걸 관리하고, 가져올 것을 가져온다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=lobby_morning_10509_1].dlg
   limit: do 140 znaków
   EN: The sun has risen. Work your respective streets. Manage what needs managing, take what's there to take.
   PL:
668. [Kwestia głosowa [lobby_noon_10509_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=lobby_noon_10509_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Kwestia głosowa [lobby_noon_10509_1] (Afternoon Greeting)] 점심은… 그래. 오늘 보호비를 걷을 예정이었던 펍으로 가지. 예정 보호비에서 식비 수준의 금액을 절감해주는 방향으로 말하면 서로에게 이득이 되겠군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=lobby_noon_10509_1].dlg
   limit: do 260 znaków
   EN: For lunch... yes. We will head to the pub that owes us protection fee. It will be for the benefit of us all if we give them a discount on the protection fee equal to the amount of food we consume there.
   PL:
670. [Kwestia głosowa [lobby_night_10509_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=lobby_night_10509_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Kwestia głosowa [lobby_night_10509_1] (Evening Greeting)] 밤거리는 다툼을 나누기 좋은 환경이다. 싸움을 준비해라. 우리의 지역을 좀먹는 놈들을 처리하지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=lobby_night_10509_1].dlg
   limit: do 170 znaków
   EN: Streets during the night are ripe for conflict. Prepare for battle; we will clear the streets of those who leech on our territory.
   PL:
672. [Kwestia głosowa [smalltalk_10509_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Kwestia głosowa [smalltalk_10509_1] (Chatter #1)] 항간에… 우리 데드레빗츠가 주변 갱단답지 않게 친절하다는 소문이 돌더군. 이해가 되지 않는다.\n보호비를 걷고서 진짜 보호해주는 갱단은 드물다고 하던가. 출혈 없이 더 많은 미래 소득을 발생시키기 위해서는 당연한 행동 아닌가.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_1].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Word on the street is that... us Dead Rabbits are 'kind' for a gang. I fail to understand this perspective.\nThey say that not many gangs actually protect those they extort protection money from. Odd. I merely see this as a wise business decision to protect our future assets without unnecessary bloodshed.
   PL:
674. [Kwestia głosowa [smalltalk_10509_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Kwestia głosowa [smalltalk_10509_2] (Chatter #2)] 최근에 식구가 되고 싶다고 굴러들어 온 녀석이 있었지. 시궁창 냄새가 나지 않는 걸 보아서는 갱과는 거리가 먼 곳 출신 같은데.\n…눈에는 독기가 서려있더군. 써먹어보고, 쓸모 있으면 데려갈 생각이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_2].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A new recruit joined our ranks. He did not smell like the gutters, so I do not understand what someone who hasn't spent much time in the streets is doing out here.\nBut his eyes... I saw venom in his eyes. I intend to let him stay with us as long as he is useful.
   PL:
676. [Kwestia głosowa [smalltalk_10509_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Kwestia głosowa [smalltalk_10509_3] (Chatter #3)] 싸움이 시작되기 전에 던지는 스카프는, 우리 데드레빗츠의 유구한 전통이다. 토끼의 귀 모양으로 묶은 이 스카프가 적에게 뛰어드는 것을 표현했지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_3].dlg
   limit: do 220 znaków
   EN: It is an old tradition of the Dead Rabbits to throw our scarves before a fight. This scarf, tied like a rabbit's ears, symbolizes our zeal as we hop our way into battle.
   PL:
678. [Kwestia głosowa [smalltalk_10509_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Kwestia głosowa [smalltalk_10509_4] (Post-Uptie Chat 1)] 시간이… 많이 지나갔군. 이럴 때 다른 갱과 시비가 벌어진 건 이득이라고 볼 수 있다.\n보호비를 바치는 녀석들의 시간보단, 그런 걸 무수히 뺏어온 다른 갱의 것을 한 번에 흡수하는게 효율적이니까.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A lot of... time has passed. A conflict with a different gang will be a benefit to our organization.\nIt is more efficient to take the time of those who have been extorting times of others for a long while than it is to collect protection fees.
   PL:
680. [Kwestia głosowa [smalltalk_10509_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Kwestia głosowa [smalltalk_10509_5] (Post-Uptie Chat 2)] 히스클리프… 라고 했나? 쓸만하게 싸우는군. 굳이 느낀 점을 말하자면, 존재 가치를 증명하기 위해 필요 이상으로 날뛴다는 느낌인가.\n…생각보다 오래 보고 지내겠군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=smalltalk_10509_5].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heathcliff... was it? Not bad. I did notice that he may be overcompensating for something, however. It was as though he wanted to prove that his existence was worth it.\n... I suppose I will be seeing him for longer than I expected.
   PL:
682. [Kwestia głosowa [neglect_10509_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=neglect_10509_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Kwestia głosowa [neglect_10509_1] (Idle)] 느긋하게 보내라. 시간은 결국… 언젠가 벌 수 있으니까.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=neglect_10509_1].dlg
   limit: do 120 znaków
   EN: Always take things slow. Time... can always be made again.
   PL:
684. [Kwestia głosowa [gacksung_10509_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=gacksung_10509_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Kwestia głosowa [gacksung_10509_1] (Uptying)] 슬슬 시간을 채워넣을 때가 됐군. 분수를 모르고 골목에 돌아다니는 갱도 보인다. 시간을 벌 때군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=gacksung_10509_1].dlg
   limit: do 200 znaków
   EN: We will soon have to make time. Quite opportune that there are other gangs roaming our streets. I see this as a perfect opportunity to make some extra time.
   PL:
686. [Kwestia głosowa [formation_10509_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=formation_10509_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Kwestia głosowa [formation_10509_1] (Deployment)] 시간을 벌러 갈 시간이군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=formation_10509_1].dlg
   limit: do 120 znaków
   EN: Time to make some... time.
   PL:
688. [Kwestia głosowa [battleentry_10509_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battleentry_10509_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Kwestia głosowa [battleentry_10509_1] (Stage Entry)] 데드레빗츠의 시간이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battleentry_10509_1].dlg
   limit: do 120 znaków
   EN: It's the Dead Rabbits' time.
   PL:
690. [Kwestia głosowa [battle_select_10509_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_select_10509_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Kwestia głosowa [battle_select_10509_1] (Viewed in Battle)] 지금은 시간이 많지 않다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_select_10509_1].dlg
   limit: do 120 znaków
   EN: I do not have much time at this moment.
   PL:
692. [Kwestia głosowa [battle_endcommand_10509_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_endcommand_10509_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Kwestia głosowa [battle_endcommand_10509_1] (Commencing Attack)] 후드려 패주지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_endcommand_10509_1].dlg
   limit: do 120 znaków
   EN: I will thrash them.
   PL:
694. [Kwestia głosowa [battle_enemy_break_10509_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_enemy_break_10509_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Kwestia głosowa [battle_enemy_break_10509_1] (Enemy Stagger)] 뇌진탕인가. 토끼들이 보일 거다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_enemy_break_10509_1].dlg
   limit: do 120 znaków
   EN: Are you hallucinating rabbits? You must be concussed.
   PL:
696. [Kwestia głosowa [battle_break_10509_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_break_10509_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Kwestia głosowa [battle_break_10509_1] (Staggered)] 흠…
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_break_10509_1].dlg
   limit: do 120 znaków
   EN: Hm...
   PL:
698. [Kwestia głosowa [battle_kill_10509_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_kill_10509_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Kwestia głosowa [battle_kill_10509_1] (Enemy Killed)] 필요 없는 시간은 가져가지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_kill_10509_1].dlg
   limit: do 120 znaków
   EN: I will take what surplus time you have.
   PL:
700. [Kwestia głosowa [battle_dead_10509_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_dead_10509_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Kwestia głosowa [battle_dead_10509_1] (Death)] 이런 날도… 온다고 생각했지… 마지막까지… 느긋하게…
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_dead_10509_1].dlg
   limit: do 120 znaków
   EN: I knew... that this day would come... I will take it slow... to my last breath...
   PL:
702. [Kwestia głosowa [choice_success_p_10509_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=choice_success_p_10509_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Kwestia głosowa [choice_success_p_10509_2] (Check Passed)] 시간 문제였다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=choice_success_p_10509_2].dlg
   limit: do 120 znaków
   EN: It was but a matter of time.
   PL:
704. [Kwestia głosowa [choice_fail_n_10509_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=choice_fail_n_10509_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Kwestia głosowa [choice_fail_n_10509_1] (Check Failed)] 내가 책임지도록 하지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=choice_fail_n_10509_1].dlg
   limit: do 120 znaków
   EN: I will take responsibility for this.
   PL:
706. [Kwestia głosowa [battle_clear_10509_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_clear_10509_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Kwestia głosowa [battle_clear_10509_1] (Victory Cry)] 생각보다 얻어들인 시간은 적지만, 이 항쟁으로 흡수한 세력이 생긴 건 이득이군. 좀 더 영향력이 커질 것이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_clear_10509_1].dlg
   limit: do 190 znaków
   EN: Though we haven't bought much time from this conflict, we have successfully absorbed their forces into our fold. Our sphere of influence grows.
   PL:
708. [Kwestia głosowa [battle_clear_ex_10509_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_clear_ex_10509_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Kwestia głosowa [battle_clear_ex_10509_1] (Extra Conditions Fulfilled)] 흠… 잘 싸웠군. 새로 들어온 놈도 마음에 든다. 앞으로는 굴러들어오는 놈도 적극적으로 받아들이기로 하지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_clear_ex_10509_1].dlg
   limit: do 160 znaków
   EN: Hm... well fought. I quite like our new recruit as well. I suppose we can start accepting more applicants that come our way.
   PL:
710. [Kwestia głosowa [battle_defeat_10509_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_defeat_10509_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Kwestia głosowa [battle_defeat_10509_1] (Defeat Wail)] 시간을 벌기만 할 수는 없지. 종종 뺏기기도 하는 법이다. …괜찮다. 시계의 모든 시간만 뺏기지 않으면 된다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_DeadRabbit_10509.json :: dataList[id=battle_defeat_10509_1].dlg
   limit: do 170 znaków
   EN: Sometimes we end up losing time. ... This is fine. As long as there is some time remaining in our watch... we will be all right.
   PL:

## [000] Dieci Assoc. South Section 4 Director — Meursault — 남부 디에치 협회 4과 부장
- ID Tożsamości: `10510` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

712. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과 부장
   źródło: Personalities.json :: dataList[id=10510].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4 Director
   PL:
713. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10510].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10510].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Karta Tożsamości — opis] 뫼르소의 열번째 인격
   źródło: Personalities.json :: dataList[id=10510].desc
   limit: do 120 znaków
   EN: Meursault’s 10th Identity
   PL:
716. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 학업 정진
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=1].name ; dataList[id=1051001].levelList[level=2].name ; dataList[id=1051001].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Studious Dedication
   PL:
717. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] x 최대 체력의 3%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard]
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Discard]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: Gain ([KnowledgeExplored] x 3% of Max HP) Shield if this Skill is Discarded\n[WhenUse] [Discard] 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL:
718. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
719. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] x 최대 체력의 <style="highlight">4%</style>)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard]\n<style="highlight">[WhenUse] [KnowledgeExplored]이 2 이상이면, 합 위력 +1\n[WinDuel] [KnowledgeTraining] 2 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=2].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [WhenUse], [Discard], [WinDuel], [KnowledgeTraining]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [WinDuel] = [합 승리시] / [Clash Win]; [KnowledgeTraining] = 지식 단련 / Erudition
   EN: Gain ([KnowledgeExplored] x <style="highlight">4%</style> of Max HP) Shield if this Skill is Discarded\n[WhenUse] [Discard] 1 Skill of the lowest rank in all of this unit's Skill Slots\n<style="highlight">[WhenUse] At 2+ [KnowledgeExplored], Clash Power +1\n[WinDuel] Gain 2 [KnowledgeTraining] (once per turn)</style>
   PL:
720. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL:
721. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] x 최대 체력의 <style="highlight">5%</style>)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard]\n<style="highlight">[WhenUse] ([KnowledgeExplored] - 1)만큼 합 위력이 증가 (최대 2)</style>\n[WinDuel] [KnowledgeTraining] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [WhenUse], [Discard], [WinDuel], [KnowledgeTraining]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [WinDuel] = [합 승리시] / [Clash Win]; [KnowledgeTraining] = 지식 단련 / Erudition
   EN: Gain ([KnowledgeExplored] x <style="highlight">5%</style> of Max HP) Shield if this Skill is Discarded\n[WhenUse] [Discard] 1 Skill of the lowest rank in all of this unit's Skill Slots\n<style="highlight">[WhenUse] Gain ([KnowledgeExplored] - 1) Clash Power (max 2)</style>\n[WinDuel] Gain 2 [KnowledgeTraining] (once per turn)
   PL:
722. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 배움의 시간
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=1].name ; dataList[id=1051002].levelList[level=2].name ; dataList[id=1051002].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Moment of Erudition
   PL:
723. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] 자신에게 [KnowledgeExplored]만큼 [KnowledgeTraining] 부여\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 등급이 낮은 순으로 [Discard]
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [KnowledgeExplored], [KnowledgeTraining], [WhenUse], [Discard]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [KnowledgeExplored] = 탐구한 지식 / Insight; [KnowledgeTraining] = 지식 단련 / Erudition; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [StartBattle] Gain [KnowledgeTraining] equal to [KnowledgeExplored] on self\n[WhenUse] [Discard] 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots
   PL:
724. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to [KnowledgeExplored]
   PL:
725. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[KnowledgeExplored] 1당 피해량 +3% (최대 9%)</style>\n<style="highlight">[StartBattle] 무작위 아군 하나와</style> 자신에게 [KnowledgeExplored]만큼 [KnowledgeTraining] 부여 <style="highlight">([Discard]을 사용하는 아군 중 [KnowledgeTraining]이 낮은 아군에게 우선 적용)</style>\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 등급이 낮은 순으로 [Discard]\n<style="highlight">[WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=2].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [StartBattle], [KnowledgeTraining], [Discard], [WhenUse], [Sinking]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [StartBattle] = [전투 시작시] / [Combat Start]; [KnowledgeTraining] = 지식 단련 / Erudition; [Discard] = 버림 / Discard; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">Deal +3% damage for every [KnowledgeExplored] on self (max 9%)</style>\n[StartBattle] Apply [KnowledgeTraining] equal to [KnowledgeExplored] on self <style="highlight"> to a random ally</style> and on self <style="highlight">(prioritizes allies with [Discard] that has the least [KnowledgeTraining])</style>\n[WhenUse] [Discard] 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n<style="highlight">[WhenUse] If target has 6+ [Sinking], Coin Power +1</style>
   PL:
726. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to [KnowledgeExplored]<style="highlight"></style>
   PL:
727. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [KnowledgeExplored] 1당 피해량 <style="highlight">+5%</style> (최대 <style="highlight">15%</style>)\n[StartBattle] 무작위 아군 <style="highlight">둘</style>과 자신에게 [KnowledgeExplored]만큼 [KnowledgeTraining] 부여 ([Discard]을 사용하는 아군 중 [KnowledgeTraining]이 낮은 아군에게 우선 적용)\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 등급이 낮은 순으로 [Discard]\n<style="highlight">[WhenUse] 대상의 [Sinking] 6당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=4].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [StartBattle], [KnowledgeTraining], [Discard], [WhenUse], [Sinking]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [StartBattle] = [전투 시작시] / [Combat Start]; [KnowledgeTraining] = 지식 단련 / Erudition; [Discard] = 버림 / Discard; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: Deal <style="highlight">+5%</style> damage for every [KnowledgeExplored] on self (max <style="highlight">15%</style>)\n[StartBattle] Apply [KnowledgeTraining] equal to [KnowledgeExplored] on self <style="highlight">to 2 random allies</style> and on self (prioritizes allies with [Discard] that has the least [KnowledgeTraining])\n[WhenUse] [Discard] 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Sinking] on target (max 2)</style>
   PL:
728. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] <style="highlight">([KnowledgeExplored] x 2)</style>만큼 [Sinking] 부여
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to <style="highlight">([KnowledgeExplored] x 2)</style>
   PL:
729. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 지식 전소
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=3].name ; dataList[id=1051003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Scorch Knowledge
   PL:
730. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [KnowledgeExplored] 1당 피해량 +3% (최대 18%)\n[WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1\n[BeforeAttack] 자신의 [KnowledgeTraining]을 전부 소모하여 그 수치의 절반만큼 [KnowledgeExplored]을 추가로 얻음 (소수점 버림)\n[EndSkill] [KnowledgeExplored]이 4 이상이면, 1로 초기화 (이 스킬로 적 처치 시, 3으로 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Sinking], [BeforeAttack], [KnowledgeTraining], [EndSkill]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [KnowledgeTraining] = 지식 단련 / Erudition; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +3% damage for every [KnowledgeExplored] on self (max 18%)\n[WhenUse] If target has 6+ [Sinking], Coin Power +1\n[BeforeAttack] Consume all [KnowledgeTraining] on self and gain half of that value as additional [KnowledgeExplored] (rounded down)\n[EndSkill] At 4+ [KnowledgeExplored], reset value to 1 (if this Skill defeats an enemy, reset value to 3 instead)
   PL:
731. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 위력과 [Sinking] 횟수를 합하여 [KnowledgeExplored]만큼 무작위로 부여
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Inflict [Sinking] Potency/Count equal to [KnowledgeExplored] value against the target (how much of that [Sinking] is Potency or Count is randomly determined)
   PL:
732. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [KnowledgeExplored] 1당 피해량 <style="highlight">+5%</style> (최대 <style="highlight">45%</style>)\n<style="highlight">[WhenUse] 대상의 [Sinking] 6당, 코인 위력 +1 (최대 2)</style>\n[BeforeAttack] 자신의 [KnowledgeTraining]을 전부 소모하여 그 <style="highlight">수치만큼</style> [KnowledgeExplored]을 추가로 얻음\n[EndSkill] [KnowledgeExplored]이 4 이상이면, 1로 초기화 (이 스킬로 적 처치 시, 3으로 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [WhenUse], [Sinking], [BeforeAttack], [KnowledgeTraining], [EndSkill]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [KnowledgeTraining] = 지식 단련 / Erudition; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal <style="highlight">+5%</style> damage for every [KnowledgeExplored] (max <style="highlight">45%</style>)\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Sinking] on target (max 2)</style>\n[BeforeAttack] Consume all [KnowledgeTraining] on self and gain <style="highlight">the same value</style> as additional [KnowledgeExplored]\n[EndSkill] At 4+ [KnowledgeExplored], reset value to 1 (if this Skill defeats an enemy, reset value to 3 instead)
   PL:
733. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 위력과 [Sinking] 횟수를 합하여 [KnowledgeExplored]만큼 무작위로 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Inflict [Sinking] Potency/Count equal to [KnowledgeExplored] value against the target (how much of that [Sinking] is Potency or Count is randomly determined)<style="highlight"></style>
   PL:
734. [Obrona (ulepszenia 1,4) — nazwa] 탐구 몰입
   źródło: Skills_personality-05.json :: dataList[id=1051004].levelList[level=1].name ; dataList[id=1051004].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Fixated Study
   PL:
735. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 [Discard]
   źródło: Skills_personality-05.json :: dataList[id=1051004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Discard]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [WhenUse] [Discard] 1 Skill of the highest rank in all of this unit's Skill Slots
   PL:
736. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 [Discard]\n<style="highlight">[WhenUse] 다음 턴에 이 슬롯이 도발치 6을 얻음</style>
   źródło: Skills_personality-05.json :: dataList[id=1051004].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Discard]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [WhenUse] [Discard] 1 Skill of the highest rank in all of this unit's Skill Slots\n<style="highlight">[WhenUse] Gain +6 Aggro to this Skill Slot next turn</style>
   PL:
737. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Gloom) — nazwa] 자율 학습 지시
   źródło: Passives.json :: dataList[id=1051001].name
   limit: do 40 znaków
   EN: Study Hall
   PL:
738. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Gloom) — opis] 자신을 제외한 아군이 스킬을 버릴 때마다 대상과 자신에게 [KnowledgeTraining] 1을 부여 (스킬 당 1회, 턴 당 3회)\n턴 종료 시, 자신을 제외하고 스킬을 버린 아군의 수만큼 다음 턴에 관통 피해량 증가, 타격 피해량 증가 얻음 (최대 3)
   źródło: Passives.json :: dataList[id=1051001].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeTraining]
   znaczenie tagów: [KnowledgeTraining] = 지식 단련 / Erudition
   EN: Every time another ally Discards a Skill, apply 1 [KnowledgeTraining] to the ally and self (once per Skill, 3 times per turn)\nTurn End: next turn, gain Pierce DMG Up and Blunt DMG Up equal to the number of other allies that Discarded Skills (max 3)
   PL:
739. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 성실한 배움
   źródło: Passives.json :: dataList[id=1051021].name
   limit: do 40 znaków
   EN: Diligent Learning
   PL:
740. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 최대 체력이 가장 높은 아군 1명이 스킬을 버릴 때, 해당 인격 최대 체력의 (5 x 버린 스킬의 등급)% 만큼 보호막을 얻음 (턴 당 1회)\n[KnowledgeExplored]이 있는 경우, 보호막 수치가 1.5배로 적용됨
   źródło: Passives.json :: dataList[id=1051021].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: When 1 ally with the highest max HP Discards a Skill, gain (5 x Discarded Skill rank)% of the max HP as Shield (once per turn)\nIf the unit has [KnowledgeExplored], multiply the above Shield value by 1.5
   PL:
741. [Kwestia głosowa [get_10510_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=get_10510_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Kwestia głosowa [get_10510_1] (Identity Acquisition)] 음, 이번 야간자율학습은 누구도 빠지지 않았군. 휘발된 지식을 다시 채우는 것도 좋지만, 새로운 지식을 배우는 것도 잊지 말도록.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=get_10510_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mm, good. No one is absent from tonight's late-night studies session.\nRemember not only to refill what you have burned but also to add new knowledge into your repositories.
   PL:
743. [Kwestia głosowa [lobby_morning_10510_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=lobby_morning_10510_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Kwestia głosowa [lobby_morning_10510_1] (Morning Greeting)] 아침이군. 미적거리지 말고 눈을 뜬 후에 가볍게 몸을 움직여라.\n머리와 몸이 완전히 깨어났다면 바깥으로 나가 빛을 쬐고, 그 뒤 지식을 탐구하는 것이 좋다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=lobby_morning_10510_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It is morning. Do not linger in bed; open your eyes, move your body, and stir awake.\nOnce you are awake in both body and mind, go outside and take in the light. It is best that you begin your studies after the aforementioned routine.
   PL:
745. [Kwestia głosowa [lobby_noon_10510_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=lobby_noon_10510_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Kwestia głosowa [lobby_noon_10510_1] (Afternoon Greeting)] 벌써 점심 시간인가. 이 시간에 너무 배부르게 먹는 것은 잠을 불러오곤 하지.\n어느 정도의 공복감은 집중력을 향상시킨다. 이후 일정이 있다면 기억해두는 편이 좋겠군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=lobby_noon_10510_1].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Already lunchtime, is it? Remember: overfeeding oneself is likely to invite sleep at too early an hour.\nA certain level of hunger enhances focus. Keep that in mind if you have any endeavors scheduled later today.
   PL:
747. [Kwestia głosowa [lobby_night_10510_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=lobby_night_10510_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Kwestia głosowa [lobby_night_10510_1] (Evening Greeting)] 곧 거두어진 아이들의 취침 시간이군. 수면은 눈 뜨고 보았던 것을 복습하는 중요한 학습행위니 방해되지 않게 정숙하는 것을 권장한다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=lobby_night_10510_1].dlg
   limit: do 310 znaków
   EN: The children must sleep soon. It is recommended that we maintain a degree of silence, for 'sleep' is an important part of the educational regimen in which the brain processes and reviews the knowledge that was gathered during the waking hours.
   PL:
749. [Kwestia głosowa [smalltalk_10510_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Kwestia głosowa [smalltalk_10510_1] (Chatter #1)] 시선을 더욱 가까이 붙여라. 열쇠와 달리 우리는 주먹으로 더듬어 지식을 취하는 자들이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_1].dlg
   limit: do 160 znaków
   EN: Hold your gaze closer. We are not like the Keys; we are those who claim our knowledge through contact with our fists.
   PL:
751. [Kwestia głosowa [smalltalk_10510_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Kwestia głosowa [smalltalk_10510_2] (Chatter #2)] 하나 협회의 해결사 시험 외에도, 별도로 치뤄지는 디에치 협회 내의 지식 시험은 지속 가능한 동기 부여로 작동하고 있다.\n시험을 통해 지식을 쌓다보면 언젠가 성자님을 알현하게 될 것이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_2].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Association's Knowledge Exams are additional, constant motivators separate from the exams conducted by the Hana Association.\nGrow your knowledge. Use exams to motivate and push yourselves further. Only then shall you one day be permitted an audience with the Saints.
   PL:
753. [Kwestia głosowa [smalltalk_10510_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Kwestia głosowa [smalltalk_10510_3] (Chatter #3)] 남부 디에치 협회가 목숨을 다해 지켜야 하는 성물은, 아주 깊은 유적에서 발견되었다고 기록되어 있다.\n이는 북부나 동부, 본부인 서부에서 수호하는 성물도 마찬가지일 테지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_3].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Records say that the Holy Relic, which we must protect with our lives, was discovered in the abyssal depths of the Ruins.\nIt is likely that the Holy Relics in the North, the East, or our headquarters in the West are also from the Ruins.
   PL:
755. [Kwestia głosowa [smalltalk_10510_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Kwestia głosowa [smalltalk_10510_4] (Post-Uptie Chat 1)] 지식이 휘발되어 강력한 물리력으로 변환되는 현상에 대해 묻는건가…\n음, 그것에 대해 지금으로서는 내가 아무것도 모른다는 것을 알고 있다. 어쩌면 이전의 나는 알았을지도. 하지만 그 또한 불분명할 뿐.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_4].dlg
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I see. You are inquiring me about the phenomenon through which the burning of knowledge directly translates to powerful physical force.\nMm, I am well-aware that I am unaware of its exact mechanisms. Perhaps my past self held knowledge that may be an answer to your query, but I am also unaware of the veracity of that statement.
   PL:
757. [Kwestia głosowa [smalltalk_10510_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Kwestia głosowa [smalltalk_10510_5] (Post-Uptie Chat 2)] 지식을 축적해두는 것은 살아가기 위한 양분을 쌓아두는 것과 같다. 이는 거둬진 자의 천성이자 법칙이니, 지식을 새로이 쌓는 것을 게을리해선 안된다.\n탐구하기 싫어하는 아이들에게 해주었던 말이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=smalltalk_10510_5].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To gather knowledge is equivalent to scrounging nutrients for survival. Do not idle before erudition, for to scrounge is the nature and the rule of the adopted.\nI have told as such to the children who have refused to study.
   PL:
759. [Kwestia głosowa [neglect_10510_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=neglect_10510_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Kwestia głosowa [neglect_10510_1] (Idle)] 이곳에 온 이유를 잊었는가. 잊었다면 다시 탐구해야한다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=neglect_10510_1].dlg
   limit: do 120 znaków
   EN: Have you forgotten why you have come here? Then learn it again.
   PL:
761. [Kwestia głosowa [gacksung_10510_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=gacksung_10510_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Kwestia głosowa [gacksung_10510_1] (Uptying)] 주먹에 휘감긴 이 광휘의 천은 켜켜이 쌓아온 지식의 무게를 발하여 너를 깨부술지니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=gacksung_10510_1].dlg
   limit: do 200 znaków
   EN: Thus from this brilliant fabric radiates the weight of layers upon layers of knowledge; now, my fists wreathed in its full weight, shall smite you down.
   PL:
763. [Kwestia głosowa [formation_10510_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=formation_10510_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Kwestia głosowa [formation_10510_1] (Deployment)] 주먹으로 매만지며 탐구할 순간.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=formation_10510_1].dlg
   limit: do 120 znaków
   EN: Let my fist be the conduit through which I attain knowledge.
   PL:
765. [Kwestia głosowa [battleentry_10510_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battleentry_10510_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Kwestia głosowa [battleentry_10510_1] (Stage Entry)] 디에치의 교리에 따라 행할 뿐.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battleentry_10510_1].dlg
   limit: do 120 znaków
   EN: I merely do as the doctrine of the Dieci dictates.
   PL:
767. [Kwestia głosowa [battle_select_10510_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_select_10510_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Kwestia głosowa [battle_select_10510_1] (Viewed in Battle)] 질문은 끝나고 따로 받겠다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_select_10510_1].dlg
   limit: do 120 znaków
   EN: Questions must wait until this task is completed.
   PL:
769. [Kwestia głosowa [battle_endcommand_10510_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_endcommand_10510_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Kwestia głosowa [battle_endcommand_10510_1] (Commencing Attack)] 이 또한 지식이 되도록.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_endcommand_10510_1].dlg
   limit: do 120 znaków
   EN: Let this become knowledge as well.
   PL:
771. [Kwestia głosowa [battle_enemy_break_10510_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_enemy_break_10510_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Kwestia głosowa [battle_enemy_break_10510_1] (Enemy Stagger)] 앎은 영원하지 않으니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_enemy_break_10510_1].dlg
   limit: do 120 znaków
   EN: To know is not eternal.
   PL:
773. [Kwestia głosowa [battle_break_10510_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_break_10510_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Kwestia głosowa [battle_break_10510_1] (Staggered)] 음…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_break_10510_1].dlg
   limit: do 120 znaków
   EN: Mm...
   PL:
775. [Kwestia głosowa [battle_kill_10510_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_kill_10510_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Kwestia głosowa [battle_kill_10510_1] (Enemy Killed)] …무지에서 도피하지 말라.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_kill_10510_1].dlg
   limit: do 120 znaków
   EN: ... Thus, turn not from ignorance.
   PL:
777. [Kwestia głosowa [battle_dead_10510_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_dead_10510_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Kwestia głosowa [battle_dead_10510_1] (Death)] 가장 당연한 순간이… 내게도 왔군…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_dead_10510_1].dlg
   limit: do 120 znaków
   EN: The moment of inevitability claims me... as well...
   PL:
779. [Kwestia głosowa [choice_success_p_10510_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=choice_success_p_10510_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Kwestia głosowa [choice_success_p_10510_2] (Check Passed)] 이번 선택은 옳았다. 그러나 다음에도 옳을지는 모르는 것이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=choice_success_p_10510_2].dlg
   limit: do 130 znaków
   EN: This was a correct choice. However, this has no bearing on the accuracy of my subsequent choices.
   PL:
781. [Kwestia głosowa [choice_fail_n_10510_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=choice_fail_n_10510_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Kwestia głosowa [choice_fail_n_10510_1] (Check Failed)] 어쩌면 이미 잊혀진 지식이었던가. 틀림은 당연한 결과지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=choice_fail_n_10510_1].dlg
   limit: do 120 znaków
   EN: Perhaps the knowledge was already lost. This outcome was inevitable.
   PL:
783. [Kwestia głosowa [battle_clear_10510_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_clear_10510_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Kwestia głosowa [battle_clear_10510_1] (Victory Cry)] 어떤 지식을 잊었는지부터 생각해야겠군. 승리의 기쁨은 그 뒤에 만끽해도 늦지 않는다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_clear_10510_1].dlg
   limit: do 120 znaków
   EN: I must review what knowledge I have lost in this battle. Celebration can wait.
   PL:
785. [Kwestia głosowa [battle_clear_ex_10510_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_clear_ex_10510_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Kwestia głosowa [battle_clear_ex_10510_1] (Extra Conditions Fulfilled)] 전투를 통해 잊은 것과 배운 것을 살피고, 다시 지식을 쌓아 디에치의 일을 해결할 뿐이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_clear_ex_10510_1].dlg
   limit: do 190 znaków
   EN: I merely review all that I have learned and forgotten from this battle. Once ready, I will continue to complete the Dieci Association's tasks.
   PL:
787. [Kwestia głosowa [battle_defeat_10510_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_defeat_10510_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Kwestia głosowa [battle_defeat_10510_1] (Defeat Wail)] 패배했으나, 여기서도 지식을 얻을 수 있을 것이다. 그러니 남은 것은 그 앎을 바탕으로 승리하는 것 뿐이군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Dieci_10510.json :: dataList[id=battle_defeat_10510_1].dlg
   limit: do 130 znaków
   EN: We will gain new knowledge as a consequence of this defeat. Hone it to forge our next victory.
   PL:

## [000] Cinq Assoc. West Section 3 — Meursault — 서부 섕크 협회 3과
- ID Tożsamości: `10511` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

789. [Karta Tożsamości — tytuł] 서부 섕크 협회\n3과
   źródło: Personalities.json :: dataList[id=10511].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nWest Section 3
   PL:
790. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10511].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10511].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Karta Tożsamości — opis] 뫼르소의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10511].desc
   limit: do 120 znaków
   EN: Meursault’s 11th Identity
   PL:
793. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 알레
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=1].name ; dataList[id=1051101].levelList[level=2].name ; dataList[id=1051101].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Allez
   PL:
794. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=1].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1051101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
796. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 속도가 대상보다 3 이상 높으면 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력을 부여하지 않고 적중시 [Burst] 횟수를 소모하지 않음\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=2].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency with its effects, but does not consume [Burst] Count On Hit\n[WhenUse] Gain +2 [Breath] Count
   PL:
797. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 3 당 코인 위력 +1. 최대 2)\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력을 부여하지 않고 적중시 [Burst] 횟수를 소모하지 않음\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 3 Speed difference; max 2)\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency with its effects, but does not consume [Burst] Count On Hit\n[WhenUse] Gain +2 [Breath] Count
   PL:
799. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 빠르면 대상과의 속도 차이만큼 [Burst] 부여 (최대 3)
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If this unit's Speed is faster than the target's, inflict [Burst] equal to their Speed difference (max 3)
   PL:
800. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 팡트
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].name ; dataList[id=1051102].levelList[level=2].name ; dataList[id=1051102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Fente
   PL:
801. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +2 [Breath] Count
   PL:
802. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1051102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 자신의 속도가 대상보다 3 이상 높으면 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력, [Burst] 횟수를 부여하지 않고, 적중 시 [Burst] 횟수를 소모하지 않음\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=2].desc ; dataList[id=1051102].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency or Count with its effects, but does not consume [Burst] Count On Hit\n[WinDuel] Gain +2 [Breath] Count
   PL:
806. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict +2 [Burst] Count
   PL:
807. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
808. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[Burst]을 부여하지 않은 경우, 부여하는 [Burst] 위력, 횟수 1 당 크리티컬 피해량 +5%</style>
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: <style="highlight">If this unit does not inflict [Burst], +5% Damage on Critical Hit for every [Burst] Potency and Count it would have inflicted</style>
   PL:
809. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 4 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]<style="highlight"></style>
   PL:
810. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict +2 [Burst] Count<style="highlight"></style>
   PL:
811. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 살뤼
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].name ; dataList[id=1051103].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Salut
   PL:
812. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 적중 시 [Burst] 횟수를 소모하지 않음\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [ConcentratedAttackMeursault]가 있으면 추가로 호흡 5 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel], [Breath], [ConcentratedAttackMeursault]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not consume [Burst] Count On Hit\n[WinDuel] Gain 5 [Breath]\n- If target has [ConcentratedAttackMeursault], gain 5 additional [Breath]
   PL:
813. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [WinDuelAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1051103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] The final Coin deals +10% damage
   PL:
814. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [WinDuelAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1051103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 813 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 해당 슬롯의 [ConcentratedAttackMeursault] 1 당 피해량 +10%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ConcentratedAttackMeursault]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Deal +10% damage for every [ConcentratedAttackMeursault] on the Slot
   PL:
816. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 3)</style>\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 적중 시 [Burst] 횟수를 소모하지 않음\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [ConcentratedAttackMeursault]가 있으면 추가로 호흡 5 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [Breath], [ConcentratedAttackMeursault]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 3)</style>\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not consume [Burst] Count On Hit\n[WinDuel] Gain 5 [Breath]\n- If target has [ConcentratedAttackMeursault], gain 5 additional [Breath]
   PL:
818. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 해당 슬롯의 [ConcentratedAttackMeursault] 1 당 피해량 <style="highlight">+20%</style>
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ConcentratedAttackMeursault]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Deal <style="highlight">+20%</style> damage for every [ConcentratedAttackMeursault] on the Slot
   PL:
819. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">- 대상의 [Burst] 1 당 크리티컬 피해량 +2% (최대 30%)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: <style="highlight">- Deal +2% Damage on Critical Hit for every [Burst] on target (max 30%)</style>
   PL:
820. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[EndSkill] 이 코인으로 대상을 처치하거나 부위를 파괴했으면, 무작위 대상에게 스킬 1회 재사용 (재사용 시 발동하지 않음)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">[EndSkill] If this Coin defeated the target or destroyed the Part, Reuse this Skill once against a random target (does not activate on Reuse)</style>
   PL:
821. [Obrona (ulepszenia 1,4) — nazwa] 데팡시브
   źródło: Skills_personality-05.json :: dataList[id=1051104].levelList[level=1].name ; dataList[id=1051104].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Défensive
   PL:
822. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 속도가 공격자보다 3 이상 높으면, 코인 위력 +2
   źródło: Skills_personality-05.json :: dataList[id=1051104].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's by 3 or more, Coin Power +2
   PL:
823. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride, posiadane 2× Glut.) — nazwa] 결투 생방송
   źródło: Passives.json :: dataList[id=1051101].name
   limit: do 40 znaków
   EN: Duel Livestream
   PL:
824. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride, posiadane 2× Glut.) — opis] 턴 종료시 자신의 [Breath] 위력 3 마다, 다음 턴에 [Agility] 1 얻음 (최대 2)\n기본 스킬로 공격 적중 시,  다음 턴에 [ConcentratedAttackMeursault] 부여. (스킬당 1회 부여)
   źródło: Passives.json :: dataList[id=1051101].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [ConcentratedAttackMeursault]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Gain 1 [Agility] next turn for every 3 [Breath] Potency on self at Turn End (max 2)\nOn Hit using Base Skills: Inflict [ConcentratedAttackMeursault] next turn (once per Skill)
   PL:
825. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride, posiadane 2× Glut.) — podsumowanie] 턴 종료시 자신의 호흡 횟수에 비례해 다음 턴에 신속 얻음. 기본 공격 적중시 다음 턴에 [ConcentratedAttackMeursault] 부여
   źródło: Passives.json :: dataList[id=1051101].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [ConcentratedAttackMeursault], [Agility], [Breath]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise
   EN: Turn End: Gain [Agility] based on [Breath] Count on self. On Hit using a Base Skill, inflict [ConcentratedAttackMeursault] next turn
   PL:
826. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Pride, posiadane 2× Glut.) — nazwa] 결투 생방송
   źródło: Passives.json :: dataList[id=1051111].name
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Pride, posiadane 2× Glut.) — opis] 턴 종료시 자신의 [Breath] 위력 3 마다, 다음 턴에 [Agility] 1 얻음 (최대 2)\n기본 스킬로 공격 적중 시, 다음 턴에 [ConcentratedAttackMeursault] 부여. (스킬당 1회 부여)\n<style="highlight">[ConcentratedAttackMeursault]가 부여된 슬롯을 공격하여 대상을 처치하거나 부위를 파괴했으면, 정신력 7 회복</style>
   źródło: Passives.json :: dataList[id=1051111].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Agility], [ConcentratedAttackMeursault]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Gain 1 [Agility] next turn for every 3 [Breath] Potency on self at Turn End (max 2)\nOn Hit using Base Skills: Inflict [ConcentratedAttackMeursault] next turn (once per Skill)\n<style="highlight">If this unit attacked the Slot that has [ConcentratedAttackMeursault] and defeated its owner or broke the Part, heal 7 SP</style>
   PL:
828. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Pride, posiadane 2× Glut.) — podsumowanie] 턴 종료시 자신의 호흡 횟수에 비례해 다음 턴에 신속 얻음. 기본 공격 적중시 다음 턴에 [ConcentratedAttackMeursault] 부여. 대상을 처치하면 정신력을 회복함
   źródło: Passives.json :: dataList[id=1051111].summary
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [ConcentratedAttackMeursault], [Agility], [Breath]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise
   EN: Turn End: Gain [Agility] based on [Breath] Count on self. On Hit using a Base Skill, inflict [ConcentratedAttackMeursault] next turn. Heals SP On Kill
   PL:
829. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 한 발 더 빠르게
   źródło: Passives.json :: dataList[id=1051121].name
   limit: do 40 znaków
   EN: One Step Ahead
   PL:
830. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 속도가 가장 빠른 아군 1명이 합 승리시 다음 턴에 신속 1을 얻음(턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1051121].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: The fastest ally, on Clash Win, gains 1 [Agility] next turn (2 times per turn)
   PL:
831. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — podsumowanie] 속도가 가장 빠른 아군이 합 승리시 다음 턴에 신속 얻음
   źródło: Passives.json :: dataList[id=1051121].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: The fastest ally, on Clash Win, gains 1 [Agility] next turn
   PL:
832. [Kwestia głosowa [get_10511_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=get_10511_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Kwestia głosowa [get_10511_1] (Identity Acquisition)] 금일 인터뷰는 여기까지 받겠습니다. 자세한 것은 서부 섕크 협회 홍보부로.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=get_10511_1].dlg
   limit: do 160 znaków
   EN: Today's interview ends here. Please refer any further questions to the Cinq Association West's Public Relations Department.
   PL:
834. [Kwestia głosowa [lobby_morning_10511_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=lobby_morning_10511_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Kwestia głosowa [lobby_morning_10511_1] (Morning Greeting)] 좋은 아침입니다. 이 시간은 본래 협회의 아침 운동 시간이기에… 자세한 인터뷰는 긴 시간을 요구하니, 가능하면 운동 후에.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=lobby_morning_10511_1].dlg
   limit: do 340 znaków
   EN: Good morning. This time of day is normally reserved for the Association’s morning workout sessions. As an interview may require a significant amount of time and undivided attention, I would like to request we table it until after the exercise has been completed.
   PL:
836. [Kwestia głosowa [lobby_noon_10511_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=lobby_noon_10511_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Kwestia głosowa [lobby_noon_10511_1] (Afternoon Greeting)] 당신은 점심식사를 거르시는 것입니까. 커리큘럼에 대한 이야기가 세시간 십사분이 경과하는 시점에서 다른 분들은 모두 식사를 이유로 자리를 뜨셨습니다만…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=lobby_noon_10511_1].dlg
   limit: do 230 znaków
   EN: Will you not join them for lunch? At the three-hour-and-fourteen-minute mark of our discussion regarding our curriculum, everyone else has left the interview for lunch, so...
   PL:
838. [Kwestia głosowa [lobby_night_10511_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=lobby_night_10511_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Kwestia głosowa [lobby_night_10511_1] (Evening Greeting)] 밤에는 특별히 방송을 하지 않습니다. 시청자 다수가 요구하는 사항이지만, 개인의 사생활을 방송하여 어떤 이득이 있는지 현재로서는 파악하기 어렵습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=lobby_night_10511_1].dlg
   limit: do 290 znaków
   EN: I do not broadcast at nighttime. Though a non-significant portion of my current viewership has requested such scheduling, it is difficult to yet determine what benefits could be gained from broadcasting one's private life.
   PL:
840. [Kwestia głosowa [smalltalk_10511_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Kwestia głosowa [smalltalk_10511_1] (Chatter #1)] 결투 생방송 말씀이십니까. 그것은 개인의 홍보를 목적으로 하기보단, 결투에 쓰이는 검법과 자세를 다수의 익명에게 검토 받는 것에 목적이 있습니다.\n익명의 인물들이 내놓는 차가운 시선은 객관화에 도움이 됩니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_1].dlg
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You must be referring to live broadcasts of my duels. Their purpose has less to do with self-promotion, and more to do with allowing an anonymous group of evaluators to analyze my techniques and form.\nThe cold, uncaring gaze of the anonymous masses is beneficial to gaining an objective perspective of oneself.
   PL:
842. [Kwestia głosowa [smalltalk_10511_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Kwestia głosowa [smalltalk_10511_2] (Chatter #2)] 서부의 협회라 한들, 섕크는 본질적으로 같습니다. 결투를 통해 상대를 무릎 꿇리거나 처분한다. 그뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_2].dlg
   limit: do 220 znaków
   EN: Every Cinq, regardless of its branch, is the same in its core. Defeat your foe via a duel and either bring them to their knees or execute them. Such is its simplicity.
   PL:
844. [Kwestia głosowa [smalltalk_10511_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Kwestia głosowa [smalltalk_10511_3] (Chatter #3)] 생방송으로 찾아오는 의뢰의 지분이 높다는 것과 그것의 편리함은 부정할 수 없겠습니다.\n들리는 소식에 의하면, 남부에서는 뒷골목의 고용주를 찾기 위해 순찰을 돌기도 한다고 합니다. …음, 확실히 비효율적이겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_3].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The undeniable truth is that a significant portion of contracts are issued due to publicity garnered via live broadcasts, and that they offer a degree of convenience.\nIt has also been said that the southern branch often patrols the Backstreets to uncover new prospective clients. ... Mm. Such a method appears to be quite inefficient.
   PL:
846. [Kwestia głosowa [smalltalk_10511_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Kwestia głosowa [smalltalk_10511_4] (Post-Uptie Chat 1)] 눈으로 쫓기 힘든 것은 당연한 것입니다. 그렇게 될 수 있도록 단련하기 때문에.\n생방송 다시보기를 시청하신다면, 화면을 멈춰가며 자세를 분석하실 수 있으니 추천드립니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_4].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It is no surprise that my movements cannot easily be tracked by the naked eye. That was the precise purpose of the training, after all.\nRevisiting previous broadcasts is recommended for those who wish to pause the feed in order to closely analyze the form.
   PL:
848. [Kwestia głosowa [smalltalk_10511_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Kwestia głosowa [smalltalk_10511_5] (Post-Uptie Chat 2)] 외우피의 공증은 확인되었다. 결투 상대의 동의도 확인했다. 죽음을 두고 겨룰 것인가, 아니면 승패를 위한 결투인가?\n마지막 대답이 끝나면, 즉시 검을 들겠다. 고민은 충분히 하도록.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=smalltalk_10511_5].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Öufi Association has notarized this activity, and the opponent's agreement is in place. Will this duel be to the death, or merely determine the better swordsman?\nIt will commence once the reply is given. You may have as much time as you wish to think this over.
   PL:
850. [Kwestia głosowa [neglect_10511_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=neglect_10511_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Kwestia głosowa [neglect_10511_1] (Idle)] …아, 지금 시간이 났습니다. 마저 인터뷰를 진행하도록 하겠습니다. 섕크 듀엘 교본 110페이지부터였습니까?
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=neglect_10511_1].dlg
   limit: do 170 znaków
   EN: ... Ah, this may be a good time to continue the interview. Shall we continue from page one-hundred-ten of the Cinq dueling manual?
   PL:
852. [Kwestia głosowa [gacksung_10511_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=gacksung_10511_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Kwestia głosowa [gacksung_10511_1] (Uptying)] 잠시. 지금부터 결투의 모습을 보여드리겠습니다. 인터뷰는 그 후에.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=gacksung_10511_1].dlg
   limit: do 140 znaków
   EN: A moment, please. You will now observe a demonstration of a duel; the interview may resume afterward.
   PL:
854. [Kwestia głosowa [formation_10511_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=formation_10511_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Kwestia głosowa [formation_10511_1] (Deployment)] 의뢰로군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=formation_10511_1].dlg
   limit: do 120 znaków
   EN: A contract, then.
   PL:
856. [Kwestia głosowa [battleentry_10511_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battleentry_10511_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Kwestia głosowa [battleentry_10511_1] (Stage Entry)] 해오던 대로 방송을 켜겠다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battleentry_10511_1].dlg
   limit: do 120 znaków
   EN: This will be broadcast as always.
   PL:
858. [Kwestia głosowa [battle_select_10511_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_select_10511_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Kwestia głosowa [battle_select_10511_1] (Viewed in Battle)] 집중중이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_select_10511_1].dlg
   limit: do 120 znaków
   EN: Currently focused.
   PL:
860. [Kwestia głosowa [battle_endcommand_10511_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_endcommand_10511_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Kwestia głosowa [battle_endcommand_10511_1] (Commencing Attack)] 아따크.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_endcommand_10511_1].dlg
   limit: do 120 znaków
   EN: Attaque.
   PL:
862. [Kwestia głosowa [battle_enemy_break_10511_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_enemy_break_10511_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Kwestia głosowa [battle_enemy_break_10511_1] (Enemy Stagger)] 다시. 결투는 끝나지 않았다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_enemy_break_10511_1].dlg
   limit: do 120 znaków
   EN: Again. This duel is not over.
   PL:
864. [Kwestia głosowa [battle_break_10511_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_break_10511_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Kwestia głosowa [battle_break_10511_1] (Staggered)] 흠. 롱뻬.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_break_10511_1].dlg
   limit: do 120 znaków
   EN: Hm. Rompre.
   PL:
866. [Kwestia głosowa [battle_kill_10511_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_kill_10511_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Kwestia głosowa [battle_kill_10511_1] (Enemy Killed)] 좋은 결투였다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_kill_10511_1].dlg
   limit: do 120 znaków
   EN: A good match.
   PL:
868. [Kwestia głosowa [battle_dead_10511_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_dead_10511_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Kwestia głosowa [battle_dead_10511_1] (Death)] 모자랐… 군. 이 패배를… 영상으로 돌려본다면… 공부가…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_dead_10511_1].dlg
   limit: do 120 znaków
   EN: So that... wasn't enough... Perhaps this defeat could be... reviewed... in a video...
   PL:
870. [Kwestia głosowa [choice_success_p_10511_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=choice_success_p_10511_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Kwestia głosowa [choice_success_p_10511_2] (Check Passed)] 이런 식으로 해결하면 됩니다. 시청자분들.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=choice_success_p_10511_2].dlg
   limit: do 120 znaków
   EN: This is how to handle one such situation, viewers.
   PL:
872. [Kwestia głosowa [choice_fail_n_10511_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=choice_fail_n_10511_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Kwestia głosowa [choice_fail_n_10511_1] (Check Failed)] 시청자 중에, 이것의 해결법을 아는 자가…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=choice_fail_n_10511_1].dlg
   limit: do 120 znaków
   EN: Is there anyone among my viewers who knows the answer...?
   PL:
874. [Kwestia głosowa [battle_clear_10511_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_clear_10511_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Kwestia głosowa [battle_clear_10511_1] (Victory Cry)] 평소와 같은 일과였습니다. 잠깐의 위기, 결과적인 승리. 볼 거리가 적어진 점은 익명의 시청자들에게 다소 안타까운 일이겠습니다만.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_clear_10511_1].dlg
   limit: do 260 znaków
   EN: There was nothing out of the ordinary in terms of today's schedule. A momentary crisis followed by a conclusive victory. It is unfortunate that the anonymous masses will not have much material to chew on.
   PL:
876. [Kwestia głosowa [battle_clear_ex_10511_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_clear_ex_10511_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Kwestia głosowa [battle_clear_ex_10511_1] (Extra Conditions Fulfilled)] 압도했습니다. 제 기존 검술보다 한층 더 향상된 기술을 쓸 수 있었다고 생각합니다. 시청자의 수가 대폭 증가하겠군요.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_clear_ex_10511_1].dlg
   limit: do 200 znaków
   EN: An overwhelming victory. I believe that my skills with the blade have grown much since my previous attempt. This will surely result in increased viewership.
   PL:
878. [Kwestia głosowa [battle_defeat_10511_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_defeat_10511_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Kwestia głosowa [battle_defeat_10511_1] (Defeat Wail)] 이런 패배는 상정한 적 없습니다. 하지만, 패배의 이유를 저장된 영상을 관찰하며 복기할 수 있으니 나쁜 수확은 아닐 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Cinq_10511.json :: dataList[id=battle_defeat_10511_1].dlg
   limit: do 230 znaków
   EN: Such defeat was not an expected outcome. However, as the reason for this defeat may be reviewed and analyzed, it can be said that this skirmish has yielded a net positive result.
   PL:

## [000] The Thumb East Capo IIII — Meursault — 동부 엄지 카포IIII
- ID Tożsamości: `10512` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Burn, Tremor

880. [Karta Tożsamości — tytuł] 동부 엄지\n카포IIII
   źródło: Personalities.json :: dataList[id=10512].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Thumb\nEast Capo IIII
   PL:
881. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10512].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10512].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Karta Tożsamości — opis] 뫼르소의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10512].desc
   limit: do 120 znaków
   EN: Meursault’s 12th Identity
   PL:
884. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 이연참-폭[爆]
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].name ; dataList[id=1051201].levelList[level=2].name ; dataList[id=1051201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Double Slash - Blast [爆]
   PL:
885. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellantAlly]
   PL:
886. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
887. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
888. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max 2)</style>
   PL:
889. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Vibration]</style>
   PL:
890. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellantAlly]<style="highlight"></style>
   PL:
891. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL:
892. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL:
893. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max <style="highlight">3</style>)
   PL:
894. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 891 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL:
896. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL:
897. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 삼연격-폭[爆]
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].name ; dataList[id=1051202].levelList[level=2].name ; dataList[id=1051202].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Triple Slash - Blast [爆]
   PL:
898. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 886 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
903. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL:
904. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].desc
   (powtórzenie elementu 888 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 889 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 891 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 892 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL:
911. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count<style="highlight"></style>
   PL:
912. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 4 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
913. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max <style="highlight">4</style>)
   PL:
914. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 891 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 895 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL:
918. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+2</style> [Combustion] Count
   PL:
919. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
920. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 쾌도난마 [快刀亂麻]
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].name ; dataList[id=1051203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Tanglecleaver [快刀亂麻]
   PL:
921. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BulletPropellantSpecialAlly]이 있으면, '초절맹호살격난참'으로 발동됨\n- [BeforeUse] [BulletPropellantSpecialAlly]이 없으면 발동 취소\n메인 타겟 대상의 [Combustion]과 [Vibration]의 합이 8 이상이면, 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellantSpecialAlly], [BeforeUse], [Combustion], [Vibration]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [BeforeUse] = [사용전] / [Before Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: If this unit has [BulletPropellantSpecialAlly], activate 'Savage Tigerslayer's Perfected Flurry of Blades' instead\n- [BeforeUse] If this unit does not have [BulletPropellantSpecialAlly], cancel activation\nIf the main target has 8+ ([Combustion] + [Vibration]), Coin Power +1
   PL:
922. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
924. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
925. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
927. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
928. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] 이 코인 효과로 [BulletPropellantAlly]을 소모하였다면, 피해량 +20%
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: If this unit spent [BulletPropellantAlly] due to this Coin's effect, deal +20% damage
   PL:
930. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL:
931. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantAlly] 소모 시, 효과 1회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantAlly], activate the above effect once more
   PL:
932. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BulletPropellantSpecialAlly]이 있으면, '초절맹호살격난참'으로 발동됨\n- [BeforeUse] [BulletPropellantSpecialAlly]이 없으면 발동 취소\n메인 타겟 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 8당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletPropellantSpecialAlly], [BeforeUse], [Combustion], [Vibration]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [BeforeUse] = [사용전] / [Before Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: If this unit has [BulletPropellantSpecialAlly], activate 'Savage Tigerslayer's Perfected Flurry of Blades' instead\n- [BeforeUse] If this unit does not have [BulletPropellantSpecialAlly], cancel activation\n<style="highlight">Coin Power +1 for every 8 ([Combustion] + [Vibration]) on the main target, (max 2)</style>
   PL:
933. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL:
935. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Combustion]
   PL:
936. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Vibration] Count
   PL:
938. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Combustion] Count
   PL:
939. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 890 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 이 코인 효과로 [BulletPropellantAlly]을 소모하였다면, 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: If this unit spent [BulletPropellantAlly] due to this Coin's effect, deal <style="highlight">+50%</style> damage
   PL:
941. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]<style="highlight"></style>
   PL:
942. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantAlly] 소모 시, 효과 <style="highlight">2</style>회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantAlly], activate the above effect <style="highlight">2</style> more times
   PL:
943. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 초절맹호살격난참 [超絕猛虎殺擊亂斬]
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].name ; dataList[id=1051205].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 5 (+3)
   limit: do 80 znaków
   EN: Savage Tigerslayer's Perfected Flurry of Blades [超絕猛虎殺擊亂斬]
   PL:
944. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 합이 8 이상이면, 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: If the main target has 8+ ([Combustion] + [Vibration]), Coin Power +1
   PL:
945. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 923 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 926 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellantSpecialAlly]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: Spend 1 [BulletPropellantSpecialAlly]
   PL:
948. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 924 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
950. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 5, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 930 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 5, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantSpecialAlly] 소모 시, 효과 1회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#4].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantSpecialAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantSpecialAlly], activate the above effect once more
   PL:
954. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 8당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">Coin Power +1 for every 8 ([Combustion] + [Vibration]) on the main target (max 2)</style>
   PL:
955. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 934 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 937 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletPropellantSpecialAlly]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: Spend 1 [BulletPropellantSpecialAlly]<style="highlight"></style>
   PL:
958. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 938 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 5, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 941 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 5, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantSpecialAlly] 소모 시, 효과 <style="highlight">2</style>회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#4].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantSpecialAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantSpecialAlly], activate the above effect <style="highlight">2</style> more times
   PL:
964. [Obrona (ulepszenia 1,4) — nazwa] 끓어오르는군.
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=1].name ; dataList[id=1051204].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: I'm Burning Up.
   PL:
965. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n메인 타겟 대상의 [Combustion]과 [Vibration]의 합이 4 이상이면, 최종 위력 +1\n[BulletPropellantAlly] 또는 [BulletPropellantSpecialAlly]이 0이면, 합 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [Combustion], [Vibration], [BulletPropellantAlly], [BulletPropellantSpecialAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [DuelCounter]\nIf the main target has 4+ ([Combustion] + [Vibration]), Final Power +1\nIf [BulletPropellantAlly] (or [BulletPropellantSpecialAlly]) is at 0, Clash Power +1
   PL:
966. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가 (턴당 2회)
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count (2 times per turn)
   PL:
967. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n메인 타겟 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 4당, 최종 위력 +1 (최대 2)</style>\n[BulletPropellantAlly] 또는 [BulletPropellantSpecialAlly]이 0이면, 합 위력 <style="highlight">+2</style>
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [Combustion], [Vibration], [BulletPropellantAlly], [BulletPropellantSpecialAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [DuelCounter]\n<style="highlight">Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max 2)</style>\nIf [BulletPropellantAlly] (or [BulletPropellantSpecialAlly]) is at 0, Clash Power <style="highlight">+2</style>
   PL:
968. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)</style>
   PL:
969. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count (2 times per turn)<style="highlight"></style>
   PL:
970. [Pasywka bojowa (od ulepszenia 1) — nazwa] 삽시호 [揷翅虎]
   źródło: Passives.json :: dataList[id=1051202].name
   limit: do 40 znaków
   EN: Chachihu [揷翅虎]
   PL:
971. [Pasywka bojowa (od ulepszenia 1) — opis] 상시 적용 : [BulletPropellantAlly] 12개 보유\n\n[BulletPropellantAlly], [BulletPropellantSpecialAlly]을 소모하는 코인을 굴릴 때, 해당 특수 탄환이 없는 경우에도 공격을 취소하지 않는 대신 해당 코인의 적중 시 [Combustion] 부여, [Combustion] 횟수 증가 효과가 발동하지 않음\n\n이번 전투에서 처음으로 수비 스킬을 장착하였거나 [BulletPropellantAlly]을 전부 사용, 또는 흐트러졌다면, 해당 턴 종료 시 [BulletPropellantSpecialAlly] 8발을 장전하고 [IrritationAlly] 1 얻음 (전투당 1회)\n- 흐트러짐 상태에서 효과 발동 시, 흐트러짐 상태 해제 (강제 흐트러짐 제외)\n- [BulletPropellantAlly]이 남아있으면 전부 소멸\n- 자신이 소모한 [BulletPropellantAlly]과 [BulletPropellantSpecialAlly]의 합이 8 이상이면, [IrritationAlly]이 [HugeIrritationAlly]으로 변경\n\n[BulletPropellantSpecialAlly]의 마지막 탄환을 소모하는 기본 공격 스킬을 사용할 경우,\n- 공격 시작 전 공격 가중치 +2\n- 다음 턴에 [BeastEyesAlly] 1 얻음
   źródło: Passives.json :: dataList[id=1051202].desc
   limit: do 1390 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellantAlly], [BulletPropellantSpecialAlly], [Combustion], [IrritationAlly], [HugeIrritationAlly], [BeastEyesAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [Combustion] = 화상 / Burn; [IrritationAlly] = 천퇴성[天退星] / Tiantui Star [天退星]; [HugeIrritationAlly] = 신(心) - 천퇴성[天退星] / Shin (心) - Tiantui Star [天退星]; [BeastEyesAlly] = 오버히트 / Overheat
   EN: Always Active: begin Encounters with 12 [BulletPropellantAlly]\n\nWhen flipping a Coin that consumes [BulletPropellantAlly] or [BulletPropellantSpecialAlly]: while not having those 'Unique Ammo' does not cancel this unit's attacks, the Coin's On Hit "inflict [Combustion]" and "inflict [Combustion] Count" effects do not activate\n\nIf this unit equipped Defense Skills for the first time in this Encounter, or if this unit spent all of his [BulletPropellantAlly], or if this unit is Staggered: at the end of that turn, reload 8 [BulletPropellantSpecialAlly] and gain 1 [IrritationAlly] (once per Encounter)\n- If this effect activates while this unit is Staggered, recover from Stagger (excluding forced Staggers)\n- Remove all [BulletPropellantAlly] if this unit has any leftover [BulletPropellantAlly]\n- At 8+ (sum of [BulletPropellantAlly] and [BulletPropellantSpecialAlly] spent), convert [IrritationAlly] to [HugeIrritationAlly]\n\nWhen this unit uses a Base Attack Skill that spends the final Round of [BulletPropellantSpecialAlly]...\n- Gain Atk Weight +2 before attacking\n- Gain 1 [BeastEyesAlly] next turn
   PL:
972. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 천퇴성도 [天退星刀]
   źródło: Passives.json :: dataList[id=1051201].name
   limit: do 40 znaków
   EN: Tiantui Star's Blade [天退星刀]
   PL:
973. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] [BulletPropellantAlly] 보유 시,\n- 1 이상이면 '쾌도난마'의 모든 코인이 [SuperCoin]으로 변경\n- [BulletPropellantAlly]을 소모하는 스킬 코인 위력 +1 (소모 가능한 만큼만 적용)\n\n[BulletPropellantSpecialAlly] 보유 시,\n- 1 이상이면 기본 공격 스킬의 모든 코인이 [SuperCoin]으로 변경\n- 0 이면 기본 공격 스킬의 특수 탄환을 소모할 수 있는 코인이 [SuperCoin]으로 변경\n- [BulletPropellantSpecialAlly]을 소모하는 스킬 코인 위력 +2 (소모 가능한 만큼만 적용)
   źródło: Passives.json :: dataList[id=1051201].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellantAlly], [SuperCoin], [BulletPropellantSpecialAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: When this unit has [BulletPropellantAlly]:\n- At 1+ [BulletPropellantAlly], convert all Coins of 'Tanglecleaver' into [SuperCoin]s\n- Skill Coins that spend [BulletPropellantAlly] gain +1 Power (activates only as long as the Coin has Rounds left to spend)\n\nWhen this unit has [BulletPropellantSpecialAlly]:\n- At 1+ [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills to [SuperCoin]s\n- At 0 [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills that spend 'Unique Ammo' to [SuperCoin]s\n- Skill Coins that spend [BulletPropellantSpecialAlly] gain +2 Power (activates only as long as the Coin has Rounds left to spend)
   PL:
974. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — nazwa] 천퇴성도 [天退星刀]
   źródło: Passives.json :: dataList[id=1051211].name
   (powtórzenie elementu 972 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — opis] [BulletPropellantAlly] 보유 시,\n- 1 이상이면 '쾌도난마'의 모든 코인이 [SuperCoin]으로 변경\n- [BulletPropellantAlly]을 소모하는 스킬 코인 위력 +1, <style="highlight">피해량 +10%</style> (소모 가능한 만큼만 적용)\n\n[BulletPropellantSpecialAlly] 보유 시,\n- 1 이상이면 기본 공격 스킬의 모든 코인이 [SuperCoin]으로 변경\n- 0 이면 기본 공격 스킬의 특수 탄환을 소모할 수 있는 코인이 [SuperCoin]으로 변경\n- [BulletPropellantSpecialAlly]을 소모하는 스킬 코인 위력 +2, <style="highlight">피해량 +30%, 해당 코인으로 적중 시 부여하는 [Combustion] 위력과 [Combustion] 횟수 부여값 +2</style> (소모 가능한 만큼만 적용)
   źródło: Passives.json :: dataList[id=1051211].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletPropellantAlly], [SuperCoin], [BulletPropellantSpecialAlly], [Combustion]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [Combustion] = 화상 / Burn
   EN: When this unit has [BulletPropellantAlly]:\n- At 1+ [BulletPropellantAlly], convert all Coins of 'Tanglecleaver' into [SuperCoin]s\n- Skill Coins that spend [BulletPropellantAlly] gain +1 Power <style="highlight">and deal +10% damage</style> (activates only as long as the Coin has Rounds left to spend)\n\nWhen this unit has [BulletPropellantSpecialAlly]:\n- At 1+ [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills to [SuperCoin]s\n- At 0 [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills that spend 'Unique Ammo' to [SuperCoin]s\n- Skill Coins that spend [BulletPropellantSpecialAlly] gain +2 Power, <style="highlight">deal +30% damage, and inflict +2 more [Combustion] Potency and [Combustion] Count On Hit with those Coins</style> (activates only as long as the Coin has Rounds left to spend)
   PL:
976. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 맹호의 도약
   źródło: Passives.json :: dataList[id=1051221].name
   limit: do 40 znaków
   EN: Savage Tiger's Lunge
   PL:
977. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 [Bullet]을 소모하는 스킬 사용 시 대상보다 속도가 3 이상 높다면, 가하는 피해량 +(대상과의 속도 차이 x 2)% (최대 10%)\n([Bullet]이 없으면 적용되지 않음. 단, [Bullet] 버프는 보유하였으나 수치가 0인 경우에는 효과가 적용됨)
   źródło: Passives.json :: dataList[id=1051221].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When 1 ally with the fastest Speed uses a Skill that spends [Bullet], if their Speed is faster than the target's by 3 or more, deal +(Speed difference × 2)% more damage (max 10%).\n(This effect does not activate if the affected unit lacks the [Bullet] buff entirely. However, it will activate if they have the [Bullet] buff, even if they have 0 rounds left)
   PL:
978. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Sloth) — nazwa] 맹호의 도약
   źródło: Passives.json :: dataList[id=1051231].name
   (powtórzenie elementu 976 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 [Bullet]을 소모하는 스킬 사용 시 대상보다 속도가 3 이상 높다면, 가하는 피해량 +(대상과의 속도 차이 x <style="highlight">3</style>)% (최대 <style="highlight">15%</style>)\n([Bullet]이 없으면 적용되지 않음. 단, [Bullet] 버프는 보유하였으나 수치가 0인 경우에는 효과가 적용됨)
   źródło: Passives.json :: dataList[id=1051231].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When 1 ally with the fastest Speed uses a Skill that spends [Bullet], if their Speed is faster than the target's by 3 or more, deal +(Speed difference × <style="highlight">3</style>)% more damage (max <style="highlight">15%</style>).\n(This effect does not activate if the affected unit lacks the [Bullet] buff entirely. However, it will activate if they have the [Bullet] buff, even if they have 0 rounds left)
   PL:
980. [Kwestia głosowa [get_10512_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=get_10512_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Kwestia głosowa [get_10512_1] (Identity Acquisition)] 세 번은 곱씹어보고 내게 말 붙이길 권장하지. 혓바닥을 잡아 뜯는 건 오늘은 그만 하고 싶군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=get_10512_1].dlg
   limit: do 130 znaków
   EN: Think it over three times, hard, before talking to me. I have ripped out enough tongues today.
   PL:
982. [Kwestia głosowa [lobby_morning_10512_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=lobby_morning_10512_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Kwestia głosowa [lobby_morning_10512_1] (Morning Greeting)] 준비된 자부터 아침보고를 시작해라. '준비',라고 말하는 것엔 항상 말했듯 여러가지의 절차를 포함한다.\n목적과 방식, 과정과 결과… 그리고 모든 것을 아우르는 예의. 갖추지 않은 자는 목숨 또한 갖출 필요가 없는 것으로 인지하겠다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=lobby_morning_10512_1].dlg
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Commence morning reports, starting from whoever is ready. And as I have said many times in the past, the state of being 'ready' entails various steps and procedures: purpose, method, process, outcome... and, most importantly, the all-encompassing adherence to manners. Those who are not 'ready' based on this criterion will be deemed unworthy of life.
   PL:
984. [Kwestia głosowa [lobby_noon_10512_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=lobby_noon_10512_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Kwestia głosowa [lobby_noon_10512_1] (Afternoon Greeting)] 정오가 되었는데도 이것들을 치우지 않았나. 분명 중요한 상담이 있으니 처리를 해 두라 일렀을 텐데.\n…흠, 허드렛일을 할 것도 죽어버렸나. 어쩔 수 없지. 상담에서는 기세도 중요할테니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=lobby_noon_10512_1].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's noon, and the trash is still here... I remember insisting that these must be cleaned up, as I expect to welcome an important client here.\n... Hm, no one left for the clean-up either, I see. I suppose intimidation factors can also be significant elements in these consultations.
   PL:
986. [Kwestia głosowa [lobby_night_10512_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=lobby_night_10512_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [Kwestia głosowa [lobby_night_10512_1] (Evening Greeting)] 야밤에 나를 찾는 것은 예의에 어긋난다고 생각하지 않나. 나와 시선을 맞출 정도의 위치라 하더라도…\n그렇군. 당신이라면 이 늦은 시각에도 응당 모시는 것이 예의에 맞을 것이다. 결례를 사과하지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=lobby_night_10512_1].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you not think that it is quite unmannerly to visit me so late into the night? Even if your station grants you the right to look me right in the eyes...\n... I see. Then the manners would dictate that you deserve to be welcomed here at this hour. I apologize for my discourtesy.
   PL:
988. [Kwestia głosowa [smalltalk_10512_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Kwestia głosowa [smalltalk_10512_1] (Chatter #1)] 사씨 가문에서 의뢰가 올 줄은 알고 있었지만, 이렇게 직접 높은 자리의 사람을 마주하게 될 줄은 몰랐군.\n독대를 요청했다고 들어, 어느 정도의 위치를 가진 자라고는 파악할 수 있었지만… 흠, 그것도 당신이 올 줄은.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_1].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A contract from the Shi family was expected, but a visitation from someone of such distinguished rank... was not.\nI could deduce by the fact that this individual requested a private meeting that it would be one with an esteemed position, but... hm. I certainly did not expect you.
   PL:
990. [Kwestia głosowa [smalltalk_10512_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [Kwestia głosowa [smalltalk_10512_2] (Chatter #2)] 치아 두 개를 담근 레드 와인은 이 순간과의 좋은 마리아주다. 예술품에 가깝다고 할 수 있지.\n…흠. 최근에 거미집에 다녀왔더니 혼잣말이 방정맞아졌나. 예술 같은 단어를 입에 올리는군. 앉은 자리에 맞는 말을 써야… 엄지의 카포, 일테지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_2].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Red wine with two freshly pulled teeth makes for a good pairing, a <i>mariage</i> with this particular circumstance. Almost like a work of art.\n... Hm. It seems that my recent visit to the House of Spiders has affected my speech. To use words like 'art'... is not befitting the Capo of the Thumb.
   PL:
992. [Kwestia głosowa [smalltalk_10512_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Kwestia głosowa [smalltalk_10512_3] (Chatter #3)] 호표탄 하나가 이 최고급 시가 세 개의 가치와 맞먹는다. 전탄을 소모해서 참격을 가할 땐 휴미더에 든 시가 모두를 날려버린다는 생각도 들지만…\n간혹, 시가 한 다스보다 가치로운 상대를 만날 때도 있으니, 아끼는 것이 더 가치 없는 일이지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_3].dlg
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The value of a single Tigermark Round is equivalent to the value of three of these premium cigars. Slashing at my foe by consuming every ammunition in its chambers is like losing an entire humidor's worth of cigars, yet...\n... sometimes, a good fight is worth more than a bundle of cigars. I would be remiss to let this chance pass in favor of frugality.
   PL:
994. [Kwestia głosowa [smalltalk_10512_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_4].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Kwestia głosowa [smalltalk_10512_4] (Post-Uptie Chat 1)] …총알값 아까울 놈은 아니군. 아끼지 않고 휘둘러 주겠다. 흔치 않게… 조금, 들뜨는 마음이 드는군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_4].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... I see that you are worth the cost of my ammunition. Prepare to face my unmitigated might.\nThis 'excitement'... what a rare sensation.
   PL:
996. [Kwestia głosowa [smalltalk_10512_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_5].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Kwestia głosowa [smalltalk_10512_5] (Post-Uptie Chat 2)] 호랑이를 잡으려 했나. 그렇다면 물어 뜯겨 죽는 각오 정도는 상응했겠지.\n나, 뫼르소. 엄지의 카포이자 동부십검 중 하나. 전력으로 상대하마.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=smalltalk_10512_5].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One mustn't embark on a tiger hunt without preparing to be mauled by its teeth. I presume that you feel ready, then?\nI am Meursault. Capo of the Thumb, one of the Ten Blades of the East. I will now meet you in battle with all my might.
   PL:
998. [Kwestia głosowa [neglect_10512_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=neglect_10512_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Kwestia głosowa [neglect_10512_1] (Idle)] 그래, 네가 할 말이 있다 해도 내게 직접 말을 걸지 않은 건 현명한 처사다. 너보다 높은, 그러나 나보단 낮은 자를 통하도록.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=neglect_10512_1].dlg
   limit: do 190 znaków
   EN: It was an astute decision on your end to not address me directly. Find a superior of yours who is inferior to my station to relay your message.
   PL:
1000. [Kwestia głosowa [gacksung_10512_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=gacksung_10512_1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1001. [Kwestia głosowa [gacksung_10512_1] (Uptying)] 이 천퇴성도의 이름을 감추어야 한다는 점은 다소 아쉽지만… 날개 돋은 듯한 호랑이의 포효소리를 내비칠 수 있으니, 이 정도로 만족하지.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=gacksung_10512_1].dlg
   limit: do 240 znaków
   EN: The fact that the name of Tiantui Star's blade must remain hidden is a shame, indeed... but here, that want is fulfilled by another—that I may roar like a winged tiger. This sates me.
   PL:
1002. [Kwestia głosowa [formation_10512_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=formation_10512_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1003. [Kwestia głosowa [formation_10512_1] (Deployment)] 걸맞는 곳이여야 할 거다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=formation_10512_1].dlg
   limit: do 120 znaków
   EN: You best hope that this task is worthy of my presence.
   PL:
1004. [Kwestia głosowa [battleentry_10512_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battleentry_10512_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Kwestia głosowa [battleentry_10512_1] (Stage Entry)] 사냥감인가. 몸이… 끓어오르는군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battleentry_10512_1].dlg
   limit: do 120 znaków
   EN: Off to hunt, then? Oh, good... I'm burning up.
   PL:
1006. [Kwestia głosowa [battle_select_10512_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_select_10512_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [Kwestia głosowa [battle_select_10512_1] (Viewed in Battle)] …너는 위아래가 없군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_select_10512_1].dlg
   limit: do 120 znaków
   EN: ... The concept of manners must be alien to you.
   PL:
1008. [Kwestia głosowa [battle_endcommand_10512_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_endcommand_10512_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [Kwestia głosowa [battle_endcommand_10512_1] (Commencing Attack)] 받아볼텐가.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_endcommand_10512_1].dlg
   limit: do 120 znaków
   EN: Are you ready?
   PL:
1010. [Kwestia głosowa [battle_enemy_break_10512_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_enemy_break_10512_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1011. [Kwestia głosowa [battle_enemy_break_10512_1] (Enemy Stagger)] 이것밖에 못하나?
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_enemy_break_10512_1].dlg
   limit: do 120 znaków
   EN: Is this really your best?
   PL:
1012. [Kwestia głosowa [battle_break_10512_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_break_10512_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1013. [Kwestia głosowa [battle_break_10512_1] (Staggered)] 크흐… 다소, 즐겁군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_break_10512_1].dlg
   limit: do 120 znaków
   EN: Keh... Why, that's quite good.
   PL:
1014. [Kwestia głosowa [battle_kill_10512_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_kill_10512_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1015. [Kwestia głosowa [battle_kill_10512_1] (Enemy Killed)] 그렇게 서 있으면, 목이 떨어질 수 밖에.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_kill_10512_1].dlg
   limit: do 120 znaków
   EN: Standing around as you did is what cost you your head.
   PL:
1016. [Kwestia głosowa [battle_dead_10512_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_dead_10512_1].desc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1017. [Kwestia głosowa [battle_dead_10512_1] (Death)] 후… 씨바…
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_dead_10512_1].dlg
   limit: do 120 znaków
   EN: Puff... motherfucker...
   PL:
1018. [Kwestia głosowa [choice_success_p_10512_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=choice_success_p_10512_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Kwestia głosowa [choice_success_p_10512_2] (Check Passed)] 의뢰여야 했을 거다. 부탁이었다면 팔 두 짝을 뽑을테니.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=choice_success_p_10512_2].dlg
   limit: do 140 znaków
   EN: This better have been a contract. I may have to remove both of your arms if it was an insolent request.
   PL:
1020. [Kwestia głosowa [choice_fail_n_10512_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=choice_fail_n_10512_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Kwestia głosowa [choice_fail_n_10512_1] (Check Failed)] …의뢰 실패 비용으로, 네 목숨은 건드리지 않겠다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=choice_fail_n_10512_1].dlg
   limit: do 120 znaków
   EN: ... I will not be taking your life. As a compensation for failing this mission.
   PL:
1022. [Kwestia głosowa [battle_clear_10512_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_clear_10512_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Kwestia głosowa [battle_clear_10512_1] (Victory Cry)] 영, 맥이 없군. 겨우 이 정도의 작자들이었나. 네 상관의 이름과 위치를 대라. 그놈 목까지 들고 가지 않으면, 수지타산이 맞지 않다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_clear_10512_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Disappointing. Is this really your best?\nGive me the name and the location of your superior. I must claim their head to make this worth the effort.
   PL:
1024. [Kwestia głosowa [battle_clear_ex_10512_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_clear_ex_10512_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1025. [Kwestia głosowa [battle_clear_ex_10512_1] (Extra Conditions Fulfilled)] 나를 들뜨게 만드는 일은 많지 않지만… 이번엔 그 귀중한 경우의 수에 들어맞았군. 잘 놀다 간다. 회수하지 않은 탄피는… 팁이다.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_clear_ex_10512_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are not many things in this world that excite me. However... this is one of those rare cases.\nI enjoyed this dance. Keep any bullet casings I missed—consider them a tip.
   PL:
1026. [Kwestia głosowa [battle_defeat_10512_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_defeat_10512_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Kwestia głosowa [battle_defeat_10512_1] (Defeat Wail)] 단도직입적으로 묻겠다… 내 목숨을 살릴 만한 방도는 없나. 혹은, 그에 상응하는 금액을 말해라.\n…없다면, 하. 목을 내놓아야겠군.
   źródło: PersonalityVoiceDlg/Voice_Meursault_Thumb_10512.json :: dataList[id=battle_defeat_10512_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Let me be straightforward. Is there any means by which I may survive this encounter? Or, if a monetary compensation would suffice, then provide a number.\n... If not, then... hah. It seems that I must lose my head.
   PL:
