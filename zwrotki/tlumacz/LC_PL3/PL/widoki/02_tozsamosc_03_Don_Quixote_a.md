# Grzesznik #03: Don Quixote — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Don Quixote** (돈키호테) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #03: Don Quixote (돈키호테)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 돈키호테
   źródło: Characters.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Don Quixote
   PL:
2. [Akta więźnia — nazwa] 돈키호테
   źródło: IntroduceCharacter.json :: dataList[id=돈키호테].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을\n수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자\n열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다.\n전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다.\n본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?)\n역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다.\n원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: IntroduceCharacter.json :: dataList[id=돈키호테].description
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is no Sinner that can outmatch this one's level of passion if we were to measure it.\nAn avid aficionada of all things Fixer, she adorns herself with a variety of Fixer-related merchandise.\nThey won't affect her performance in combat one way or another,\nso there is no need for you to restrict her from keeping her decorations.\nShe is deeply immersed in the role of a righteous Fixer,\nhence the exaggerated mannerisms akin to those of an actor. (Has such a thing ever existed, really?)\nIt's advised to play along with her for a smooth mission.
   PL: Gdyby mierzyć Grzeszników samym zapałem, ta otrzymałaby najwyższą ocenę.\nJest zagorzałą fanką i kolekcjonerką wszystkiego, co związane z Fikserami,\ndlatego obwiesza się pamiątkami po nich od stóp do głów. Nie wpływa to\nszczególnie na walkę, nie ma więc potrzeby jej tego zabraniać.\nSama jest głęboko zatopiona w roli Fiksera sprawiedliwości (czy coś takiego\nw ogóle kiedykolwiek istniało?), stąd przesadna gestykulacja niczym\nu aktorki trzeciej kategorii. Dla sprawnego przebiegu misji lepiej jej przytakiwać.

## [0] LCB Sinner — Don Quixote — LCB 수감자
- ID Tożsamości: `10301` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10301].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10301].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10301].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 돈키호테의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10301].desc
   limit: do 120 znaków
   EN: Don Quixote’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 찌르기
   źródło: Skills.json :: dataList[id=1030101].levelList[level=1].name ; dataList[id=1030101].levelList[level=2].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Joust
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 신속 1 얻음
   źródło: Skills.json :: dataList[id=1030101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Haste next turn
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WinDuel] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 2 Haste next turn
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 모아 찌르기
   źródło: Skills.json :: dataList[id=1030102].levelList[level=1].name ; dataList[id=1030102].levelList[level=2].name ; dataList[id=1030102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Galloping Tilt
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1030102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Attack Power Up next turn
   PL:
13. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills.json :: dataList[id=1030102].levelList[level=2].desc ; dataList[id=1030102].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 2 Attack Power Up next turn
   PL:
14. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1030102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL:
15. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 정의를 위해!
   źródło: Skills.json :: dataList[id=1030103].levelList[level=3].name ; dataList[id=1030103].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 3 (+3)
   limit: do 40 znaków
   EN: For Justice!
   PL:
16. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 속도가 10 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1030103].levelList[level=3].desc ; dataList[id=1030103].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 10+ Speed, Coin Power +2
   PL:
17. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1030103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1030103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 부여
   źródło: Skills.json :: dataList[id=1030103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed count
   PL:
20. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1030104].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
21. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Lust) — nazwa] 정의의 응징
   źródło: Passives.json :: dataList[id=1030101].name
   limit: do 40 znaków
   EN: Righteous Retribution
   PL:
22. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Lust) — opis] 합 승리 시 해당 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030101].desc
   limit: do 120 znaków
   EN: Skills deal +10% damage in a won clash.
   PL:
23. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 응원
   źródło: Passives.json :: dataList[id=1030121].name
   limit: do 40 znaków
   EN: Support
   PL:
24. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 정신력이 가장 높은 아군 1명 관통 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030121].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +10% Pierce damage.
   PL:
25. [Kwestia głosowa [get_10301_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=get_10301_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
26. [Kwestia głosowa [get_10301_1] (Identity Acquisition)] 이 몸의 차례인가? 나는, 돈키호테일세!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=get_10301_1].dlg
   limit: do 120 znaków
   EN: Hath my time come? I am Don Quixote!
   PL:
27. [Kwestia głosowa [lobby_morning_10301_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=lobby_morning_10301_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
28. [Kwestia głosowa [lobby_morning_10301_1] (Morning Greeting)] 하암… 관리자 나리는 참 부지런한 것 같소. 어떻게 이 시간에 눈이 팍 떠진단 말이오…?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=lobby_morning_10301_1].dlg
   limit: do 160 znaków
   EN: Yaaawn… You must be one diligent laborer, Manager Esquire. How on earth do you manage to rouse yourself at this hour…?
   PL:
29. [Kwestia głosowa [lobby_noon_10301_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=lobby_noon_10301_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
30. [Kwestia głosowa [lobby_noon_10301_1] (Afternoon Greeting)] 점심밥은 무엇을 먹을 생각이오? 나는 로쟈씨가 근사한 식당을 알아봤다 해서 엄청나게 기대 중이오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=lobby_noon_10301_1].dlg
   limit: do 160 znaków
   EN: What plans doth you have for a luncheon today? I, for one, eagerly anticipate Señorita Rodya’s choice of “fancy diner”.
   PL:
31. [Kwestia głosowa [lobby_night_10301_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=lobby_night_10301_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
32. [Kwestia głosowa [lobby_night_10301_1] (Evening Greeting)] 오늘따라 별이 밝소. 관리자 나리께서도 별이 보이오?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=lobby_night_10301_1].dlg
   limit: do 120 znaków
   EN: The stars shine bright tonight. Doth you see them as well, Manager Esquire?
   PL:
33. [Kwestia głosowa [smalltalk_10301_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=smalltalk_10301_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
34. [Kwestia głosowa [smalltalk_10301_1] (Chatter #1)] 관리자 나리, 이것좀 구경하시겠소? 내 보물들이오, 흐흐… 한정판인데 어렵게 구했소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=smalltalk_10301_1].dlg
   limit: do 200 znaków
   EN: Manager Esquire, would you lend an eye to these? ‘Tis my trove of treasures, hehe… Some are limited editions which I fought valiantly to lay claim upon!
   PL:
35. [Kwestia głosowa [smalltalk_10301_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=smalltalk_10301_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
36. [Kwestia głosowa [smalltalk_10301_2] (Chatter #2)] 언제나 세상의 정의를 위해 달려 나가는 저 해결사들을 보시오! 너무나 반짝거리지 않소?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=smalltalk_10301_2].dlg
   limit: do 140 znaków
   EN: My, cast your gaze upon those Fixers, sprinting forth to bring about justice! Dazzling, are they not?
   PL:
37. [Kwestia głosowa [smalltalk_10301_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=smalltalk_10301_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
38. [Kwestia głosowa [smalltalk_10301_3] (Chatter #3)] 관리자 나리는 제일 좋아하는 해결사가 누구시오? 배지 나눠드릴 테니 옷에 붙이고 다니시는 게 어떠오?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=smalltalk_10301_3].dlg
   limit: do 160 znaków
   EN: Pray tell, what Fixer is your favorite, Manager Esquire? Would you fancy a pin in their celebration to decorate your attire?
   PL:
39. [Kwestia głosowa [neglect_10301_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=neglect_10301_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
40. [Kwestia głosowa [neglect_10301_1] (Idle)] 관리자 나리!!!!! 나를 두고 어디 간 것이오!!!!!!!!!!!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=neglect_10301_1].dlg
   limit: do 120 znaków
   EN: Manager Esquire!!!!! To where in the world hast thou disappeared!!!!!!!!!!!
   PL:
41. [Kwestia głosowa [formation_10301_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=formation_10301_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
42. [Kwestia głosowa [formation_10301_1] (Deployment)] 달리자! 로시난테!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=formation_10301_1].dlg
   limit: do 120 znaków
   EN: Onward, Rocinante!
   PL:
43. [Kwestia głosowa [battleentry_10301_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battleentry_10301_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
44. [Kwestia głosowa [battleentry_10301_1] (Stage Entry)] 내가 나설 차례인가!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battleentry_10301_1].dlg
   limit: do 120 znaków
   EN: ‘Tis my time to shine!
   PL:
45. [Kwestia głosowa [battle_select_10301_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_select_10301_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
46. [Kwestia głosowa [battle_select_10301_1] (Viewed in Battle)] 나를 지켜보고 있었군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_select_10301_1].dlg
   limit: do 120 znaków
   EN: Thine eyes were upon me!
   PL:
47. [Kwestia głosowa [battle_endcommand_10301_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_endcommand_10301_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
48. [Kwestia głosowa [battle_endcommand_10301_1] (Commencing Attack)] 출진이다!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_endcommand_10301_1].dlg
   limit: do 120 znaków
   EN: To arms!
   PL:
49. [Kwestia głosowa [battle_enemy_break_10301_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_enemy_break_10301_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
50. [Kwestia głosowa [battle_enemy_break_10301_1] (Enemy Stagger)] 생각대로 되었소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_enemy_break_10301_1].dlg
   limit: do 120 znaków
   EN: Just as I foresaw!
   PL:
51. [Kwestia głosowa [battle_break_10301_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_break_10301_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
52. [Kwestia głosowa [battle_break_10301_1] (Staggered)] 앗!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_break_10301_1].dlg
   limit: do 120 znaków
   EN: Ay!
   PL:
53. [Kwestia głosowa [battle_kill_10301_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_kill_10301_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
54. [Kwestia głosowa [battle_kill_10301_1] (Enemy Killed)] 승리했소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_kill_10301_1].dlg
   limit: do 120 znaków
   EN: A triumph!
   PL:
55. [Kwestia głosowa [battle_allydead_10301_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_allydead_10301_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
56. [Kwestia głosowa [battle_allydead_10301_1] (Ally Death)] 관리자 나리, 힘들겠지만 부탁하오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_allydead_10301_1].dlg
   limit: do 120 znaków
   EN: Manager Esquire, I am counting on you to regain our ground!
   PL:
57. [Kwestia głosowa [choice_success_p_10301_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=choice_success_p_10301_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
58. [Kwestia głosowa [choice_success_p_10301_1] (Check Passed)] 굳이 자만하지 않겠소! 역사엔 틀림없이 기록될 테니까!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=choice_success_p_10301_1].dlg
   limit: do 120 znaków
   EN: I shan’t bask in glory! I know history will remember this deed, after all!
   PL:
59. [Kwestia głosowa [choice_fail_n_10301_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=choice_fail_n_10301_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
60. [Kwestia głosowa [choice_fail_n_10301_1] (Check Failed)] 역경을 이겨내야 진정한 영웅인 법. 다음에 다시 가보세!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=choice_fail_n_10301_1].dlg
   limit: do 130 znaków
   EN: A true hero must needs be able to overcome hardship. We shall sally forth once more next time!
   PL:
61. [Kwestia głosowa [battle_clear_10301_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_clear_10301_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
62. [Kwestia głosowa [battle_clear_10301_1] (Victory Cry)] 음음! 정의는 반드시 승리하는 법!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_clear_10301_1].dlg
   limit: do 120 znaków
   EN: Insooth! Justice always prevails!
   PL:
63. [Kwestia głosowa [battle_clear_ex_10301_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_clear_ex_10301_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
64. [Kwestia głosowa [battle_clear_ex_10301_1] (Extra Conditions Fulfilled)] 역시 본인은 위대한 해결사가 될 자질이 있소!!!! 음하하하하!!!!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_clear_ex_10301_1].dlg
   limit: do 120 znaków
   EN: I knew a great Fixer slumbered within me!!!! Mwahahahaha!!!!
   PL:
65. [Kwestia głosowa [battle_defeat_10301_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_defeat_10301_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
66. [Kwestia głosowa [battle_defeat_10301_1] (Defeat Wail)] 크윽… 대가를… 치루게… 될 것이오…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LCB_10301.json :: dataList[id=battle_defeat_10301_1].dlg
   limit: do 120 znaków
   EN: Keugh… They shall… pay… for this…
   PL:

## [000] W Corp. L3 Cleanup Agent — Don Quixote — W사 3등급 정리 요원
- ID Tożsamości: `10302` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

67. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10302].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Agent
   PL:
68. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10302].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10302].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Karta Tożsamości — opis] 돈키호테의 두번째 인격
   źródło: Personalities.json :: dataList[id=10302].desc
   limit: do 120 znaków
   EN: Don Quixote’s 2nd Identity
   PL:
71. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 절단
   źródło: Skills.json :: dataList[id=1030201].levelList[level=1].name ; dataList[id=1030201].levelList[level=2].name ; dataList[id=1030201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Rip
   PL:
72. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1030201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL:
73. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1030201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture
   PL:
74. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1030201].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL:
75. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 충전 횟수가 5 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1030201].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 5+ Charge Count, Coin Power +2
   PL:
76. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1030201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +4 Charge Count
   PL:
77. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도약
   źródło: Skills.json :: dataList[id=1030202].levelList[level=1].name ; dataList[id=1030202].levelList[level=2].name ; dataList[id=1030202].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Leap
   PL:
78. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 취약 1 부여
   źródło: Skills.json :: dataList[id=1030202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Fragile
   PL:
79. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1030202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +4 Charge Count
   PL:
80. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1030202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 취약 2 부여
   źródło: Skills.json :: dataList[id=1030202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1030202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Fragile
   PL:
82. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 충전 횟수가 7 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1030202].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 7+ Charge Count, Coin Power +1
   PL:
83. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 공간 절단
   źródło: Skills.json :: dataList[id=1030203].levelList[level=3].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 1 · monety: 5 (+2)
   limit: do 40 znaków
   EN: Rip Space
   PL:
84. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 충전 횟수 10을 소모하여 코인 위력 +4\n충전 횟수가 10미만인 경우 체력 20% 감소
   źródło: Skills.json :: dataList[id=1030203].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Spend 10 Charge Count to gain +4 Coin Power\nAt less than 10 Charge Count, lose 20% HP
   PL:
85. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 5, efekt 1 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills.json :: dataList[id=1030203].levelList[level=3].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture
   PL:
86. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1030204].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 급속충전
   źródło: Passives.json :: dataList[id=1030201].name
   limit: do 40 znaków
   EN: Quick Recharge
   PL:
88. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 전투 시작 시 이번 턴에 충전 횟수 (우울 공명 수/3)만큼 증가
   źródło: Passives.json :: dataList[id=1030201].desc
   limit: do 120 znaków
   EN: At the start of the combat phase, gain Charge Count by (Gloom Reson. / 3).
   PL:
89. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 꺾인 마음
   źródło: Passives.json :: dataList[id=1030221].name
   limit: do 40 znaków
   EN: Broken Spirit
   PL:
90. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 속도가 가장 높은 아군 1명 첫번째 스킬의 최종 위력 +1
   źródło: Passives.json :: dataList[id=1030221].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed gains +1 final Power for their first skill.
   PL:
91. [Kwestia głosowa [get_10302_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=get_10302_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Kwestia głosowa [get_10302_1] (Identity Acquisition)] 승객 여러분 안녕하시오!!! 내. 가. 도착하였네!!!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=get_10302_1].dlg
   limit: do 120 znaków
   EN: Welcome aboard, dearest passengers!!! I. Have. Arrived!!!
   PL:
93. [Kwestia głosowa [lobby_morning_10302_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=lobby_morning_10302_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Kwestia głosowa [lobby_morning_10302_1] (Morning Greeting)] 새벽을 여는 첫 기차처럼 오늘도 앞을 향해 달려 나가겠소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=lobby_morning_10302_1].dlg
   limit: do 120 znaków
   EN: Like the first train breaking the dawn, I shall rush forth with ever-constant vigor!
   PL:
95. [Kwestia głosowa [lobby_noon_10302_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=lobby_noon_10302_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Kwestia głosowa [lobby_noon_10302_1] (Afternoon Greeting)] 점심도 챙겨주는 회사라니…! 나 여기가 참 좋소! 백날 천날 여기서 계속 있고 싶소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=lobby_noon_10302_1].dlg
   limit: do 160 znaków
   EN: To think that the company provideth midday meals…! I am infatuated! I would remain employed here for eons if I could!
   PL:
97. [Kwestia głosowa [lobby_night_10302_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=lobby_night_10302_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Kwestia głosowa [lobby_night_10302_1] (Evening Greeting)] 나 오늘은 회의 때 필기 진짜 열심히 했소! 이것 보시오, 색깔별로 펜으로 다 예쁘게 꾸몄소! 별도 있고 꽃도 있고…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=lobby_night_10302_1].dlg
   limit: do 220 znaków
   EN: I have done mine utmost to take notes during today’s meeting! Behold, I have utilized a great variety of colors to illuminate the writing! With stars and flowers and…
   PL:
99. [Kwestia głosowa [smalltalk_10302_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Kwestia głosowa [smalltalk_10302_1] (Chatter #1)] 관리자 나리는 W사 열차를 이용해 보신 적이 있소? 없다고 하셨소?! 잠깐… 잠깐 시간을 내주시오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_1].dlg
   limit: do 130 znaków
   EN: Have you ridden one of W Corp’s trains, Manager Esquire? Not once?! Hold it, I… Give me a moment.
   PL:
101. [Kwestia głosowa [smalltalk_10302_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Kwestia głosowa [smalltalk_10302_2] (Chatter #2)] 나중에 우리끼리 기차여행 가는 건 어떨 것 같소, 관리자 나리? 도시락은 내가 준비하겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_2].dlg
   limit: do 120 znaków
   EN: What do you think of going on a train trip together, Manager Esquire? I’ll pack our lunch!
   PL:
103. [Kwestia głosowa [smalltalk_10302_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Kwestia głosowa [smalltalk_10302_3] (Chatter #3)] 혹시 로쟈씨 보지 못하셨소? 아니 글쎄, W사의 역사에 대해 내 친히 설파해주겠다고 약속했는데, 아까부터 보이지가 않소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_3].dlg
   limit: do 210 znaków
   EN: Have you seen Mistress Rodya anywhere? I promised her earlier that I would give her an extensive lecture on the history of W Corp, yet she’s nowhere to be found!
   PL:
105. [Kwestia głosowa [smalltalk_10302_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
106. [Kwestia głosowa [smalltalk_10302_4] (Post-Uptie Chat 1)] 관리자 나리, 계속 코끝에 맴도는 이 비릿한 냄새는 나한테만 나는 것이오? 아니면 계속 공기 중에 퍼져있는 것이오?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_4].dlg
   limit: do 130 znaków
   EN: Manager Esquire, is it just me, or is this metallic odor tingling my nose prevalent in the air?
   PL:
107. [Kwestia głosowa [smalltalk_10302_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
108. [Kwestia głosowa [smalltalk_10302_5] (Post-Uptie Chat 2)] 그거 아시오? 사람은 의외로 쉽게 죽지 않소. 피가 넘쳐흐를 만큼 흐르고 셀 수도 없이 뼈가 부러져도 숨을 쉬고 있소.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=smalltalk_10302_5].dlg
   limit: do 210 znaków
   EN: Did you know that human life is more resilient than it seems? One may still be breathing even after suffering profuse bleeding and breaking most of one’s bones.
   PL:
109. [Kwestia głosowa [neglect_10302_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=neglect_10302_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Kwestia głosowa [neglect_10302_1] (Idle)] 그렇게 해서 W사의 성과가 널리 알려지게 된 것… 응? 관리자 나리?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=neglect_10302_1].dlg
   limit: do 120 znaków
   EN: …and that is how the achievements of W Corp. came to be widely kno— Hm? Manager Esquire?
   PL:
111. [Kwestia głosowa [gacksung_10302_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=gacksung_10302_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
112. [Kwestia głosowa [gacksung_10302_1] (Uptying)] 나도 드디어 중요한 일을 맡게 되는 것이오?!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=gacksung_10302_1].dlg
   limit: do 120 znaków
   EN: Will I finally be given an important task?!
   PL:
113. [Kwestia głosowa [formation_10302_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=formation_10302_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Kwestia głosowa [formation_10302_1] (Deployment)] 출발합니다!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=formation_10302_1].dlg
   limit: do 120 znaków
   EN: Here we go!
   PL:
115. [Kwestia głosowa [battleentry_10302_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battleentry_10302_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Kwestia głosowa [battleentry_10302_1] (Stage Entry)] 기차와 같이 달려 나가겠소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battleentry_10302_1].dlg
   limit: do 120 znaków
   EN: I shall rush ahead as would a train!
   PL:
117. [Kwestia głosowa [battle_select_10302_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_select_10302_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Kwestia głosowa [battle_select_10302_1] (Viewed in Battle)] 나는 언제나 달려 나갈 준비가 되었소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_select_10302_1].dlg
   limit: do 120 znaków
   EN: I’m always ready to speed forward!
   PL:
119. [Kwestia głosowa [battle_endcommand_10302_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_endcommand_10302_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Kwestia głosowa [battle_endcommand_10302_1] (Commencing Attack)] 내 앞을 막을 자는 없소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_endcommand_10302_1].dlg
   limit: do 120 znaków
   EN: None shall stop me!
   PL:
121. [Kwestia głosowa [battle_enemy_break_10302_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_enemy_break_10302_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Kwestia głosowa [battle_enemy_break_10302_1] (Enemy Stagger)] 지금이 기회인 것 같소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_enemy_break_10302_1].dlg
   limit: do 120 znaków
   EN: Now seems to be our chance!
   PL:
123. [Kwestia głosowa [battle_break_10302_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_break_10302_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Kwestia głosowa [battle_break_10302_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_break_10302_1].dlg
   limit: do 120 znaków
   EN: Urk!
   PL:
125. [Kwestia głosowa [battle_kill_10302_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_kill_10302_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Kwestia głosowa [battle_kill_10302_1] (Enemy Killed)] 다음은 어디오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_kill_10302_1].dlg
   limit: do 120 znaków
   EN: Where to next?!
   PL:
127. [Kwestia głosowa [battle_allydead_10302_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_allydead_10302_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Kwestia głosowa [battle_allydead_10302_1] (Ally Death)] 관리자 나리! 끝나고 부탁하오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_allydead_10302_1].dlg
   limit: do 120 znaków
   EN: Manager Esquire! I’ll count on you once this is over!
   PL:
129. [Kwestia głosowa [choice_success_p_10302_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=choice_success_p_10302_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Kwestia głosowa [choice_success_p_10302_1] (Check Passed)] 관리자 나리! 잘한 것 같지 않소?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=choice_success_p_10302_1].dlg
   limit: do 120 znaków
   EN: Manager Esquire! I did a rather impressive job, did I not?
   PL:
131. [Kwestia głosowa [choice_fail_n_10302_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=choice_fail_n_10302_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Kwestia głosowa [choice_fail_n_10302_1] (Check Failed)] 중요한 일이었는데, 미안하오…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=choice_fail_n_10302_1].dlg
   limit: do 120 znaków
   EN: I am terribly sorry, it was vital that I succeed…
   PL:
133. [Kwestia głosowa [battle_clear_10302_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_clear_10302_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Kwestia głosowa [battle_clear_10302_1] (Victory Cry)] 회사의 뛰어난 인재가 바로 여기 있군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_clear_10302_1].dlg
   limit: do 120 znaków
   EN: Now THERE is a valuable asset to the company!
   PL:
135. [Kwestia głosowa [battle_clear_ex_10302_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_clear_ex_10302_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Kwestia głosowa [battle_clear_ex_10302_1] (Extra Conditions Fulfilled)] 이게 바로 소위 말하는 엘리트?! 나 승진시켜주시오, 관리자 나리!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_clear_ex_10302_1].dlg
   limit: do 120 znaków
   EN: Have I become a so-called elite?! Promote me, Manager Esquire!
   PL:
137. [Kwestia głosowa [battle_defeat_10302_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_defeat_10302_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Kwestia głosowa [battle_defeat_10302_1] (Defeat Wail)] 난… 포기하지 않을 것이오…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_WCorp5_10302.json :: dataList[id=battle_defeat_10302_1].dlg
   limit: do 120 znaków
   EN: I… shan’t ever give up…
   PL:

## [00] Shi Assoc. South Section 5 Director — Don Quixote — 남부 시 협회 5과 부장
- ID Tożsamości: `10303` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 69 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

139. [Karta Tożsamości — tytuł] 남부 시 협회\n5과 부장
   źródło: Personalities.json :: dataList[id=10303].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nSouth Section 5 Director
   PL:
140. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10303].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10303].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Karta Tożsamości — opis] 돈키호테의 세번째 인격
   źródło: Personalities.json :: dataList[id=10303].desc
   limit: do 120 znaków
   EN: Don Quixote’s 3rd Identity
   PL:
143. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 숨고르기
   źródło: Skills.json :: dataList[id=1030301].levelList[level=1].name ; dataList[id=1030301].levelList[level=2].name ; dataList[id=1030301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Catch Breath
   PL:
144. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath] next turn
   PL:
145. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] next turn
   PL:
146. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Haste next turn
   PL:
147. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] next turn
   PL:
148. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 이격
   źródło: Skills.json :: dataList[id=1030302].levelList[level=1].name ; dataList[id=1030302].levelList[level=2].name ; dataList[id=1030302].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Dual Strike
   PL:
149. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL:
150. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Haste next turn
   PL:
151. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 체력이 최대 체력의 50%미만일 때 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At less than 50% HP, gain 2 Haste next turn
   PL:
152. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] next turn
   PL:
153. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 체력이 최대 체력의 50%미만일 때 다음 턴에 신속 4 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At less than 50% HP, gain 4 Haste next turn
   PL:
154. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 3 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 3 Haste next turn
   PL:
156. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과호흡
   źródło: Skills.json :: dataList[id=1030303].levelList[level=3].name ; dataList[id=1030303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+21)
   limit: do 40 znaków
   EN: Overbreathe
   PL:
157. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 속도가 10 이상이면, 스킬 위력 +3
   źródło: Skills.json :: dataList[id=1030303].levelList[level=3].desc
   limit: do 120 znaków
   EN: At 10+ Speed, Skill Power +3
   PL:
158. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 속도가 10 이상이면, 스킬 위력 +5
   źródło: Skills.json :: dataList[id=1030303].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 10+ Speed, Skill Power +5
   PL:
159. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1030304].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 마음가짐
   źródło: Passives.json :: dataList[id=1030301].name
   limit: do 40 znaków
   EN: Prepared Mind
   PL:
161. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 다음 턴에 [Agility]을 (분노 공명 수/3)만큼 얻음
   źródło: Passives.json :: dataList[id=1030301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Gain [Agility] by (Wrath Reson. / 3) next turn.
   PL:
162. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 양단
   źródło: Passives.json :: dataList[id=1030321].name
   limit: do 40 znaków
   EN: Divide in Two
   PL:
163. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 속도가 가장 높은 아군 1명 참격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed deals +10% Slash damage.
   PL:
164. [Kwestia głosowa [get_10303_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=get_10303_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Kwestia głosowa [get_10303_1] (Identity Acquisition)] 자, 정의가 찾아왔소! 악인들을 평등한 죽음으로 이끄리라!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=get_10303_1].dlg
   limit: do 120 znaków
   EN: Hurrah, justice hath arrived! I shall drive all villains into equal demise!
   PL:
166. [Kwestia głosowa [lobby_morning_10303_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=lobby_morning_10303_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Kwestia głosowa [lobby_morning_10303_1] (Morning Greeting)] 쉿, 관리자 나리. 기습 훈련 중이었소. 내 발걸음 소리가 들렸소?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=lobby_morning_10303_1].dlg
   limit: do 130 znaków
   EN: Shh, quiet, Manager Esquire. I was practicing mine ambush maneuvers. Could you hear my footsteps?
   PL:
168. [Kwestia głosowa [lobby_noon_10303_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=lobby_noon_10303_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Kwestia głosowa [lobby_noon_10303_1] (Afternoon Greeting)] 난 말이오, 관리자 나리. 세상에 굴복하지 않고 싶소. 눈에 보이는 것보다 하늘엔 더 별이 많은 것처럼 말이오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=lobby_noon_10303_1].dlg
   limit: do 230 znaków
   EN: You see, Manager Esquire, I aspire to persevere through the storms cast by the world. It ought to be worth the turmoil, as there are more stars in the sky than bare eyes can see.
   PL:
170. [Kwestia głosowa [lobby_night_10303_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=lobby_night_10303_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Kwestia głosowa [lobby_night_10303_1] (Evening Greeting)] 밝은 달을 보고 있으니 처음의 열의가 되살아나는 것 같소.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=lobby_night_10303_1].dlg
   limit: do 120 znaków
   EN: I feel the passion from mine youth rekindle when I gaze upon the bright moon.
   PL:
172. [Kwestia głosowa [smalltalk_10303_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Kwestia głosowa [smalltalk_10303_1] (Chatter #1)] 어쩌면, 악인들이 그리 멀리 있는 존재가 아닐지도 모르오. 아, 아무것도 아니오. 못 들은 걸로 하시오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_1].dlg
   limit: do 160 znaków
   EN: Perhaps villains are closer to us than one might have thought. Ah, ‘tis but meaningless rambles. Forget that I spoke.
   PL:
174. [Kwestia głosowa [smalltalk_10303_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Kwestia głosowa [smalltalk_10303_2] (Chatter #2)] 나, 소리 나지 않게 기습하는 법을 훈련하느라 진짜 고생 많이 했소.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_2].dlg
   limit: do 120 znaków
   EN: It did take me tremendous pains to learn to strike one’s foe with nary a sound.
   PL:
176. [Kwestia głosowa [smalltalk_10303_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Kwestia głosowa [smalltalk_10303_3] (Chatter #3)] 응? 내 얼굴이 너무 울적해 보인다는 것이오? 잘못 보셨소. 그냥 생각 좀 하고 있었을 뿐이오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_3].dlg
   limit: do 140 znaków
   EN: Hm? I appear fraught with gloom to the eyes? Surely, you are mistaken. I was merely lost in contemplation.
   PL:
178. [Kwestia głosowa [smalltalk_10303_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Kwestia głosowa [smalltalk_10303_4] (Post-Uptie Chat 1)] 관리자 나리, 난 모든 이들이 나처럼 정의를 위해서만 올곧게 싸우는 줄 알았소. 정치니, 파생 세력이니 하는 건… 내게 너무 어렵소…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_4].dlg
   limit: do 250 znaków
   EN: Manager Esquire, I thought that all men fought righteous battles in the name of justice as I do. All this complication of political intricacies and derived factions… They’re beyond my grasp…
   PL:
180. [Kwestia głosowa [smalltalk_10303_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [smalltalk_10303_5] (Post-Uptie Chat 2)] 중간 관리자 역할은… 정말 마음고생이 심한 직책인 것 같소… 관리자 나리도 늘 이렇게 힘들었소?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=smalltalk_10303_5].dlg
   limit: do 180 znaków
   EN: The task of middle management… is truly an arduous one, especially for the mind… Have you endured this struggle as well, Manager Esquire?
   PL:
182. [Kwestia głosowa [neglect_10303_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=neglect_10303_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [neglect_10303_1] (Idle)] 관리자 나리도 어둠 속에 숨어버린 것이오?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=neglect_10303_1].dlg
   limit: do 120 znaków
   EN: Have you hidden yourself among the shadows?
   PL:
184. [Kwestia głosowa [gacksung_10303_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=gacksung_10303_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [gacksung_10303_1] (Uptying)] 나… 더 힘내보겠소! 지켜봐 주시오, 관리자 나리!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=gacksung_10303_1].dlg
   limit: do 120 znaków
   EN: I… shall exert greater efforts! Watch me, Manager Esquire!
   PL:
186. [Kwestia głosowa [formation_10303_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=formation_10303_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [formation_10303_1] (Deployment)] 악인들을 뒤쫓아서!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=formation_10303_1].dlg
   limit: do 120 znaków
   EN: I shall pursue yon evildoers!
   PL:
188. [Kwestia głosowa [battleentry_10303_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battleentry_10303_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [battleentry_10303_1] (Stage Entry)] 이번엔 어떤 짓을 한 악인들이오?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battleentry_10303_1].dlg
   limit: do 120 znaków
   EN: What vile deeds have those villains done?
   PL:
190. [Kwestia głosowa [battle_select_10303_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_select_10303_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [battle_select_10303_1] (Viewed in Battle)] 기습 준비 중이었는데, 내가 보이시오?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_select_10303_1].dlg
   limit: do 120 znaków
   EN: I was preparing a surprise attack—you were able to detect me?
   PL:
192. [Kwestia głosowa [battle_endcommand_10303_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_endcommand_10303_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [battle_endcommand_10303_1] (Commencing Attack)] 악인들을 해치우세나!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_endcommand_10303_1].dlg
   limit: do 120 znaków
   EN: Let us vanquish these evildoers!
   PL:
194. [Kwestia głosowa [battle_enemy_break_10303_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_enemy_break_10303_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [battle_enemy_break_10303_1] (Enemy Stagger)] 정신 차릴 수 없을 것이오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_enemy_break_10303_1].dlg
   limit: do 120 znaków
   EN: You shan’t be let a moment of clarity!
   PL:
196. [Kwestia głosowa [battle_break_10303_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_break_10303_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [battle_break_10303_1] (Staggered)] 으…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_break_10303_1].dlg
   limit: do 120 znaków
   EN: Ack…
   PL:
198. [Kwestia głosowa [battle_kill_10303_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_kill_10303_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [battle_kill_10303_1] (Enemy Killed)] 처리했소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_kill_10303_1].dlg
   limit: do 120 znaków
   EN: I slew them!
   PL:
200. [Kwestia głosowa [battle_allydead_10303_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_allydead_10303_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [battle_allydead_10303_1] (Ally Death)] 악인을 무찌르고 돌아오겠소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_allydead_10303_1].dlg
   limit: do 120 znaków
   EN: I shall avenge thee and vanquish that villain!
   PL:
202. [Kwestia głosowa [choice_success_p_10303_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=choice_success_p_10303_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [choice_success_p_10303_1] (Check Passed)] 나의 정의에는 결과가 있었소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=choice_success_p_10303_1].dlg
   limit: do 120 znaków
   EN: My justice bore fruit!
   PL:
204. [Kwestia głosowa [choice_fail_n_10303_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=choice_fail_n_10303_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Kwestia głosowa [choice_fail_n_10303_1] (Check Failed)] 굴복하지 않을 것이오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=choice_fail_n_10303_1].dlg
   limit: do 120 znaków
   EN: Nay, I shan’t submit!
   PL:
206. [Kwestia głosowa [battle_clear_10303_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_clear_10303_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Kwestia głosowa [battle_clear_10303_1] (Victory Cry)] 달빛 아래에서 정의가 널리 퍼져나갈 것이오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_clear_10303_1].dlg
   limit: do 120 znaków
   EN: Justice shall flourish under the moonlight!
   PL:
208. [Kwestia głosowa [battle_clear_ex_10303_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_clear_ex_10303_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Kwestia głosowa [battle_clear_ex_10303_1] (Extra Conditions Fulfilled)] 어둠이 캄캄할수록 빛나는 별이 탄생하지! 바로 지금처럼 말이오!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_clear_ex_10303_1].dlg
   limit: do 120 znaków
   EN: On the darkest night, the brightest star is born! Now is one such moment!
   PL:
210. [Kwestia głosowa [battle_defeat_10303_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_defeat_10303_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Kwestia głosowa [battle_defeat_10303_1] (Defeat Wail)] 이제 모르겠소. 달이 저무는데, 정의는 정말 실현되긴 하는 거요?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Shi_10303.json :: dataList[id=battle_defeat_10303_1].dlg
   limit: do 120 znaków
   EN: I am certain no longer. The moon wanes. Is there hope of justice’s fulfillment?
   PL:

## [00] N Corp. Mittelhammer — Don Quixote — N사 중간 망치
- ID Tożsamości: `10304` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Bleed

212. [Karta Tożsamości — tytuł] N사\n중간 망치
   źródło: Personalities.json :: dataList[id=10304].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nMittelhammer
   PL:
213. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10304].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10304].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Karta Tożsamości — opis] 돈키호테의 네번째 인격
   źródło: Personalities.json :: dataList[id=10304].desc
   limit: do 120 znaków
   EN: Don Quixote’s 4th Identity
   PL:
216. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 올곧은 정화
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].name ; dataList[id=1030401].levelList[level=2].name ; dataList[id=1030401].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Rightful Purge
   PL:
217. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 못 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Nails
   PL:
218. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL:
219. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1030401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
221. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 못 2 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Nails
   PL:
223. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
224. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 집행!
   źródło: Skills.json :: dataList[id=1030402].levelList[level=1].name ; dataList[id=1030402].levelList[level=2].name ; dataList[id=1030402].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Enactment!
   PL:
225. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1030402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
226. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] 대상에게 못 이 5 이상 있으면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1030402].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +20% Damage to targets that have 5+ Nails
   PL:
227. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] 대상에게 못 이 5 이상 있으면, 피해량 +30%
   źródło: Skills.json :: dataList[id=1030402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% damage to targets that have 5+ Nails
   PL:
228. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 광적인 심판
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].name ; dataList[id=1030403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Fanatical Judgement
   PL:
229. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Nails
   PL:
230. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 못 1 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1030403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
232. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 대상에게 못 이 5 이상 있으면, 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1030403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 5+ Nails, inflict 1 Attack Power Down next turn
   PL:
233. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 대상에게 못 이 5 이상 있으면, 다음 턴에 마비 2 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1030403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 5+ Nails, inflict 2 Paralyze next turn
   PL:
234. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1030403].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 2 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Nails
   PL:
236. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 못 2 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1030404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Guard
   PL:
238. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — nazwa] 두드릴지라!
   źródło: Passives.json :: dataList[id=1030401].name
   limit: do 40 znaków
   EN: Thou Shalt Hammer!
   PL:
239. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — opis] 못 이 있는 대상에게 부여하는 진동 횟수 +1\n자신에게 광신 이 있으면 부여하는 못 +1
   źródło: Passives.json :: dataList[id=1030401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If the target has Nails, inflict +1 Tremor Count.\nIf this unit is Fanatic, inflict +1 Nails.
   PL:
240. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 맹목의 망치
   źródło: Passives.json :: dataList[id=1030421].name
   limit: do 40 znaków
   EN: Hammer of Zealotry
   PL:
241. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 광신 이 있는 아군 중 정신력이 가장 낮은 아군의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030421].desc
   limit: do 120 znaków
   EN: 1 Fanatic ally that has the least SP deals +10% damage
   PL:
242. [Kwestia głosowa [get_10304_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=get_10304_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Kwestia głosowa [get_10304_1] (Identity Acquisition)] 악을 정화하는 정의의 망치. 본인을 필요로 하는가? 후후후…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=get_10304_1].dlg
   limit: do 120 znaków
   EN: The hammer of justice purgeth evil. Dost thou require mine aid? Fuhuhu…
   PL:
244. [Kwestia głosowa [lobby_morning_10304_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=lobby_morning_10304_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Kwestia głosowa [lobby_morning_10304_1] (Morning Greeting)] …아, 미안하네. 교리에 집중을 하면 다른 건 잘 듣지 못해서. 아침 식사 시간인가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=lobby_morning_10304_1].dlg
   limit: do 170 znaków
   EN: …Ah, mine apologies. I give little heed to other sounds whilst I am focused on the doctrine. Hath the time for breakfast come?
   PL:
246. [Kwestia głosowa [lobby_noon_10304_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=lobby_noon_10304_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Kwestia głosowa [lobby_noon_10304_1] (Afternoon Greeting)] 밤이 되면 정의를 집행하느라 바빠질테지… 지금 남은 걸 읽어둬야만 해…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=lobby_noon_10304_1].dlg
   limit: do 160 znaków
   EN: When the night falleth, I shall be occupied with delivering justice… I must use this time to read the remaining passages…
   PL:
248. [Kwestia głosowa [lobby_night_10304_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=lobby_night_10304_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Kwestia głosowa [lobby_night_10304_1] (Evening Greeting)] …히힉?! 앗, 하… 가면… 벗고 다녀 주면 안되겠는가? 어두워서 무심코 정화할 뻔 했지 않은가…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=lobby_night_10304_1].dlg
   limit: do 180 znaków
   EN: …Heeheek?! Ah, hah… The masque… Will you please unmasque yourself at ordinary times? The dark made me mistake you for a heretic to purge…
   PL:
250. [Kwestia głosowa [smalltalk_10304_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [smalltalk_10304_1] (Chatter #1)] 6장 18절… 그러나 그대와는 내 언약을 세우리니… 히힉! 쥐는 자께서 세우시는 언약… 히히힉!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_1].dlg
   limit: do 140 znaków
   EN: In 6:18… “Yet I shall forge a vow with thee…” Heehee! A vow decreed by the One Who Grips… Heeheeheek!
   PL:
252. [Kwestia głosowa [smalltalk_10304_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [smalltalk_10304_2] (Chatter #2)] 세상에는 너무 악이 많소… 쥐는 자께서 홀몸으로 그들을 전부 정화하시기에는 바쁘심으로, 본인이 도우는 것이오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_2].dlg
   limit: do 170 znaków
   EN: An overabundance of evil prevaileth in the world… As the One Who Grips beeth simply too busy to purge them all alone, I aid her.
   PL:
254. [Kwestia głosowa [smalltalk_10304_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [smalltalk_10304_3] (Chatter #3)] 아아, 이 양피지 말인가. 본인이 직접 필사한 것이오… 책자의 형태로는, 항상 쥐는 자께서 남긴 말씀을 함께 할 수 없지 않소…? 히힉.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_3].dlg
   limit: do 260 znaków
   EN: Ahh, so of this parchment you are curious. I transcribed the text myself… I cannot be in company with the passages of the One Who Grips at all times if they are confined to their tomes, can I…? Heeheeh.
   PL:
256. [Kwestia głosowa [smalltalk_10304_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [smalltalk_10304_4] (Post-Uptie Chat 1)] 이 망치는 내겐 재판봉과도 같소. 악한 자의 심장에… 정의의 심판을 내리는 것이지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_4].dlg
   limit: do 150 znaków
   EN: This hammer beeth like a judge’s gavel to me. With it, I aim for the heart of evil… and deliver judgement upon it.
   PL:
258. [Kwestia głosowa [smalltalk_10304_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [smalltalk_10304_5] (Post-Uptie Chat 2)] 그대가 쥐는 자께서 행하시는 대업을 도우는 자라니, 본인의 마음 또한 든든하네.\n그대와 함께라면, 본인의 정의집행 또한 커다란 발전이 있겠지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=smalltalk_10304_5].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To hear that you aid the One Who Grips in her great task relieveth me.\nWith you, mine own enactment of justice shall make great strides.
   PL:
260. [Kwestia głosowa [neglect_10304_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=neglect_10304_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [neglect_10304_1] (Idle)] 귀한 휴식 시간을 허공으로 날려버릴 수는 없지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=neglect_10304_1].dlg
   limit: do 120 znaków
   EN: I cannot let precious rest go to waste.
   PL:
262. [Kwestia głosowa [gacksung_10304_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=gacksung_10304_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [gacksung_10304_1] (Uptying)] 키힛! 아하하핫! 올곧은…! 정화.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=gacksung_10304_1].dlg
   limit: do 120 znaków
   EN: Keehee! Ahahahah! Upstanding…! Purging.
   PL:
264. [Kwestia głosowa [formation_10304_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=formation_10304_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [formation_10304_1] (Deployment)] …음, 출발하지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=formation_10304_1].dlg
   limit: do 120 znaków
   EN: …Mm, let us advance.
   PL:
266. [Kwestia głosowa [battleentry_10304_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battleentry_10304_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [battleentry_10304_1] (Stage Entry)] 악은 제 형태를 갖추지 못하리라.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battleentry_10304_1].dlg
   limit: do 120 znaków
   EN: Evil shan’t keep its proper form.
   PL:
268. [Kwestia głosowa [battle_select_10304_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_select_10304_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [battle_select_10304_1] (Viewed in Battle)] 하하하핫! 아, 옆에 있었군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_select_10304_1].dlg
   limit: do 120 znaków
   EN: Hahahahah! Ah, you were by the side!
   PL:
270. [Kwestia głosowa [battle_endcommand_10304_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_endcommand_10304_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [battle_endcommand_10304_1] (Commencing Attack)] 꿰뚫어 주겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_endcommand_10304_1].dlg
   limit: do 120 znaków
   EN: I shall pierce thee!
   PL:
272. [Kwestia głosowa [battle_enemy_break_10304_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_enemy_break_10304_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [battle_enemy_break_10304_1] (Enemy Stagger)] (미친 웃음)
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_enemy_break_10304_1].dlg
   limit: do 120 znaków
   EN: *Maniacal Laughter*
   PL:
274. [Kwestia głosowa [battle_break_10304_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_break_10304_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [battle_break_10304_1] (Staggered)] (미친 웃음)
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_break_10304_1].dlg
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Kwestia głosowa [battle_kill_10304_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_kill_10304_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [battle_kill_10304_1] (Enemy Killed)] 제대로 집행했군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_kill_10304_1].dlg
   limit: do 120 znaków
   EN: Rightly executed.
   PL:
278. [Kwestia głosowa [battle_dead_10304_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_dead_10304_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
279. [Kwestia głosowa [battle_dead_10304_1] (Death)] 큭… 아직, 해야할 일이…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_dead_10304_1].dlg
   limit: do 120 znaków
   EN: Krh… There are still—deeds undone…
   PL:
280. [Kwestia głosowa [choice_success_p_10304_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=choice_success_p_10304_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [choice_success_p_10304_1] (Check Passed)] 어려운 일은 아니었네.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=choice_success_p_10304_1].dlg
   limit: do 120 znaków
   EN: ‘Twasn’t a difficult task.
   PL:
282. [Kwestia głosowa [choice_fail_n_10304_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=choice_fail_n_10304_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [choice_fail_n_10304_1] (Check Failed)] …당황스럽군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=choice_fail_n_10304_1].dlg
   limit: do 120 znaków
   EN: …This puzzleth me.
   PL:
284. [Kwestia głosowa [battle_clear_10304_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_clear_10304_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Kwestia głosowa [battle_clear_10304_1] (Victory Cry)] 흠… 이제 휴식 시간인가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_clear_10304_1].dlg
   limit: do 120 znaków
   EN: Hmm… Doth it be time for rest?
   PL:
286. [Kwestia głosowa [battle_clear_ex_10304_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_clear_ex_10304_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Kwestia głosowa [battle_clear_ex_10304_1] (Extra Conditions Fulfilled)] 이 풍경… 정의의 망치가 다녀간 토지는 이토록 아름답구나!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_clear_ex_10304_1].dlg
   limit: do 120 znaków
   EN: This scenery… Oh, how beautiful the lands become once trodden by the hammer of justice!
   PL:
288. [Kwestia głosowa [battle_defeat_10304_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_defeat_10304_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Kwestia głosowa [battle_defeat_10304_1] (Defeat Wail)] 이히히힛… 악을… 정화하기에는… 무력했나.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Ncorp_10304.json :: dataList[id=battle_defeat_10304_1].dlg
   limit: do 120 znaków
   EN: Eheeheehee… Perchance… I was powerless… to purge evil.
   PL:

## [000] Cinq Assoc. South Section 5 Director — Don Quixote — 남부 섕크 협회 5과 부장
- ID Tożsamości: `10305` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 72 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: —

290. [Karta Tożsamości — tytuł] 남부 섕크 협회\n5과 부장
   źródło: Personalities.json :: dataList[id=10305].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nSouth Section 5 Director
   PL:
291. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10305].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10305].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Karta Tożsamości — opis] 돈키호테의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10305].desc
   limit: do 120 znaków
   EN: Don Quixote’s 5th Identity
   PL:
294. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 르미즈
   źródło: Skills.json :: dataList[id=1030501].levelList[level=1].name ; dataList[id=1030501].levelList[level=2].name ; dataList[id=1030501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Remise
   PL:
295. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 속도가 7 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1030501].levelList[level=1].desc
   limit: do 120 znaków
   EN: At 7+ Speed, Coin Power +1
   PL:
296. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [WinDuelAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030501].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttackHead]
   znaczenie tagów: [WinDuelAttackHead] = [합 승리 후 앞면 적중시] / [Heads Hit after Clash Win]
   EN: [WinDuelAttackHead] Inflict 1 Bind next turn
   PL:
297. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 속도가 7 이상이면, 코인 위력 +1\n[WinDuel] 다음 턴에 신속 1을 얻음
   źródło: Skills.json :: dataList[id=1030501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 7+ Speed, Coin Power +1\n[WinDuel] Gain 1 Haste next turn
   PL:
298. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 7 이상이면, 코인 위력 +2\n[WinDuel] 다음 턴에 신속 1을 얻음
   źródło: Skills.json :: dataList[id=1030501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 7+ Speed, Coin Power +2\n[WinDuel] Gain 1 Haste next turn
   PL:
299. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [WinDuelAttack] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] Inflict 1 Bind next turn
   PL:
300. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 플레쉬
   źródło: Skills.json :: dataList[id=1030502].levelList[level=1].name ; dataList[id=1030502].levelList[level=2].name ; dataList[id=1030502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Flèche
   PL:
301. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 신속 1을 얻음
   źródło: Skills.json :: dataList[id=1030502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Haste next turn
   PL:
302. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030502].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bind next turn
   PL:
303. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 신속 2를 얻음
   źródło: Skills.json :: dataList[id=1030502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Haste next turn
   PL:
304. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 신속 2를 얻음\n[WinDuel] 합 횟수에 비례하여 피해량 증가(합 횟수 1 당 +5%. 최대 50%)
   źródło: Skills.json :: dataList[id=1030502].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 2 Haste next turn\n[WinDuel] Deal more damage based on Clash count (+5% per Clash count, Max 50%)
   PL:
305. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL:
306. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 살뤼!
   źródło: Skills.json :: dataList[id=1030503].levelList[level=3].name ; dataList[id=1030503].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 6 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Salut!
   PL:
307. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 10 이상이면, 코인 위력 +2\n[WinDuel] 합 횟수에 비례하여 피해량 증가(합 횟수 1 당 +5%. 최대 50%)
   źródło: Skills.json :: dataList[id=1030503].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 10+ Speed, Coin Power +2\n[WinDuel] Deal more damage based on Clash count (+5% per Clash count, Max 50%)
   PL:
308. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DuelDeclaration_DonQuixote] 부여
   źródło: Skills.json :: dataList[id=1030503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DuelDeclaration_DonQuixote]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DuelDeclaration_DonQuixote] = 결투 선포 - 돈키호테 / Declared Duel - Don Quixote
   EN: [OnSucceedAttack] Inflict [DuelDeclaration_DonQuixote]
   PL:
309. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 10 이상이면, 코인 위력 +3\n[WinDuel] 합 횟수에 비례하여 피해량 증가(합 횟수 1 당 +10%. 최대 100%)
   źródło: Skills.json :: dataList[id=1030503].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 10+ Speed, Coin Power +3\n[WinDuel] Deal more damage based on Clash count (+10% per Clash count, Max 100%)
   PL:
310. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [EnemyKill] 자신의 정신력 15 회복
   źródło: Skills.json :: dataList[id=1030503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal 15 SP
   PL:
311. [Obrona (ulepszenia 1,4) — nazwa] 데팡시브
   źródło: Skills.json :: dataList[id=1030504].levelList[level=1].name ; dataList[id=1030504].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Défensive
   PL:
312. [Obrona (ulepszenia 1,4) — opis] [OnSucceedEvade] 대상의 정신력 3 감소
   źródło: Skills.json :: dataList[id=1030504].levelList[level=1].desc ; dataList[id=1030504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 3 SP
   PL:
313. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 고귀한 결투
   źródło: Passives.json :: dataList[id=1030501].name
   limit: do 40 znaków
   EN: A Noble Duel
   PL:
314. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 모든 아군의 속도가 모든 적보다 높으면, 자신의 피해량이 속도가 가장 느린 적과의 속도 차이에 비례하여 증가 (속도 차이 1 당 6%. 최대 30%)
   źródło: Passives.json :: dataList[id=1030501].desc
   limit: do 280 znaków
   EN: If the Speed of all allies is faster than the Speed of all enemies, this unit deals more damage based on the Speed difference between itself and the slowest enemy (+6% for every point of Speed difference; max 30%)
   PL:
315. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 결투 의뢰
   źródło: Passives.json :: dataList[id=1030521].name
   limit: do 40 znaków
   EN: Dueling Request
   PL:
316. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 모든 아군의 속도가 모든 적보다 높으면, 속도가 가장 빠른 아군의 피해량이 속도가 가장 느린 적과의 속도 차이에 비례하여 증가 (속도 차이 1 당 3%. 최대 15%)
   źródło: Passives.json :: dataList[id=1030521].desc
   limit: do 280 znaków
   EN: If the Speed of all allies is faster than the Speed of all enemies, the fastest ally deals more damage based on the Speed difference between itself and the slowest enemy (+3% for every point of Speed difference; max 15%)
   PL:
317. [Kwestia głosowa [get_10305_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=get_10305_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Kwestia głosowa [get_10305_1] (Identity Acquisition)] 자아! 그대가 나와 결투할 자인가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=get_10305_1].dlg
   limit: do 120 znaków
   EN: Aha! Art thou my partner in duel?!
   PL:
319. [Kwestia głosowa [lobby_morning_10305_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=lobby_morning_10305_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Kwestia głosowa [lobby_morning_10305_1] (Morning Greeting)] 좋은 아침일세! 흐흠, 오늘도 날씨가 화창하군. 어디, 이번엔 산책이라도 나가볼까?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=lobby_morning_10305_1].dlg
   limit: do 130 znaków
   EN: Good morrow! Hmhm, another bright day indeed. Let's see, mayhaps I shall go on a merry stroll?
   PL:
321. [Kwestia głosowa [lobby_noon_10305_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=lobby_noon_10305_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Kwestia głosowa [lobby_noon_10305_1] (Afternoon Greeting)] 음… 역시, 낮이 되니 사람이 붐비는군. 앗! 저기! 다툼인가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=lobby_noon_10305_1].dlg
   limit: do 120 znaków
   EN: Hm... Midday certainly brings out the crowd. Aha! See yonder! A brawl, perhaps?!
   PL:
323. [Kwestia głosowa [lobby_night_10305_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=lobby_night_10305_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Kwestia głosowa [lobby_night_10305_1] (Evening Greeting)] 식사는 했는가? 이 근처에 괜찮은 레스토랑이 있다네! 디너 디저트에 있는 수플레가 맛있지. 함께 가지 않겠는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=lobby_night_10305_1].dlg
   limit: do 190 znaków
   EN: Hast thou supped yet? I have found thee a nice restaurant nearabouts! Their dinner menu features a rather delicious soufflé. Wilt thou accompany me?
   PL:
325. [Kwestia głosowa [smalltalk_10305_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Kwestia głosowa [smalltalk_10305_1] (Chatter #1)] 부지런히 움직여야겠지! 도시에는 언제나 다툼이 있고, 그만큼 대리 결투를 의뢰하는 자가 많으니까!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_1].dlg
   limit: do 140 znaków
   EN: I mustn't dally! The city abounds with conflict, and many seek those that would take up arms in their place!
   PL:
327. [Kwestia głosowa [smalltalk_10305_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Kwestia głosowa [smalltalk_10305_2] (Chatter #2)] 길거리를 산책하며 정신을 환기시키는 것도 업무적으로도 중요한 일일세!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_2].dlg
   limit: do 140 znaków
   EN: Strolling through the streets and taking mine own mind off things is an important part of my profession!
   PL:
329. [Kwestia głosowa [smalltalk_10305_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Kwestia głosowa [smalltalk_10305_3] (Chatter #3)] 장갑을 던지는 것은! 상대를 향한 고귀하고 명예로운 결투선포일세! 결투에 있어서 중요한 절차지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_3].dlg
   limit: do 180 znaków
   EN: To throw down my gauntlet is a dignified and honorable declaration of mine intent to duel! 'Tis an indispensable part of a duel's etiquette.
   PL:
331. [Kwestia głosowa [smalltalk_10305_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Kwestia głosowa [smalltalk_10305_4] (Post-Uptie Chat 1)] 이건 가끔 드는 의문이네만… 어째, 장갑을 맞은 자들은 하나 같이 얼굴을 붉으락푸르락 하더군.\n왜들 그렇게 화를 내는지… 명예롭게 결투를 받아들이지 못하는 심성인가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_4].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prithee, I cannot help but be perplexed… Wherefore do those struck by my gauntlet turn red with fury?\nWhat causeth them to fume, I wonder…? Perhaps their hearts are simply not fit for an honorable duel.
   PL:
333. [Kwestia głosowa [smalltalk_10305_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [smalltalk_10305_5] (Post-Uptie Chat 2)] 부장이라고 해서 다른 협회원들과 다를 바는 없지 않겠나! 실제로! 본인은 그들을 부하라고 부르지도 않지.\n나는 그저, 그들보다 조금 더 많은 경험을 가졌을 뿐이네. 또 모르지 않는가? 새로 들어온 신입이 어떤 결투에서는 나보다 뛰어날지!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=smalltalk_10305_5].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The station of a Director is no different from that of mine associates! In truth, I do not call them my subordinates, even.\nI have but a meager merit in experience, no more. Besides, perchance we may have a newcomer who surpasses my skill in combat!
   PL:
335. [Kwestia głosowa [neglect_10305_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=neglect_10305_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [neglect_10305_1] (Idle)] (콧노래)
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=neglect_10305_1].dlg
   limit: do 120 znaków
   EN: (Hums)
   PL:
337. [Kwestia głosowa [gacksung_10305_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=gacksung_10305_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [gacksung_10305_1] (Uptying)] 음! 인정 받는다는 것은 언제나 명예로운 일이지! 감사를 표하겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=gacksung_10305_1].dlg
   limit: do 120 znaków
   EN: Aha! To be recognized is to be bestowed with honor! I thank thee!
   PL:
339. [Kwestia głosowa [formation_10305_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=formation_10305_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [formation_10305_1] (Deployment)] 결투 의뢰로군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=formation_10305_1].dlg
   limit: do 120 znaków
   EN: Aha, a dueling request!
   PL:
341. [Kwestia głosowa [battleentry_10305_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battleentry_10305_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [battleentry_10305_1] (Stage Entry)] 좁은 곳이 좋겠어…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battleentry_10305_1].dlg
   limit: do 120 znaków
   EN: Perchance a narrow alleyway shall be to my benefit...
   PL:
343. [Kwestia głosowa [battle_select_10305_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_select_10305_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [battle_select_10305_1] (Viewed in Battle)] 결투 중에는 말을 걸지 않는게 좋다만.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_select_10305_1].dlg
   limit: do 120 znaków
   EN: 'Tis ill-advised to speak to me whilst I fight a duel.
   PL:
345. [Kwestia głosowa [battle_endcommand_10305_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_endcommand_10305_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [battle_endcommand_10305_1] (Commencing Attack)] 알레!(Allez!)
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_endcommand_10305_1].dlg
   limit: do 120 znaków
   EN: Allez!
   PL:
347. [Kwestia głosowa [battle_enemy_break_10305_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_enemy_break_10305_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [battle_enemy_break_10305_1] (Enemy Stagger)] 항복하겠는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_enemy_break_10305_1].dlg
   limit: do 120 znaków
   EN: Dost thou surrender?
   PL:
349. [Kwestia głosowa [battle_break_10305_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_break_10305_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [battle_break_10305_1] (Staggered)] 치잇…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_break_10305_1].dlg
   limit: do 120 znaków
   EN: Tsk...
   PL:
351. [Kwestia głosowa [battle_kill_10305_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_kill_10305_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [battle_kill_10305_1] (Enemy Killed)] 유쾌한 결투였네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_kill_10305_1].dlg
   limit: do 120 znaków
   EN: 'Twas a duel most amusing!
   PL:
353. [Kwestia głosowa [battle_dead_10305_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_dead_10305_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [battle_dead_10305_1] (Death)] 아아… 이건, 부끄럽군…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_dead_10305_1].dlg
   limit: do 120 znaków
   EN: Aah... 'Twas... a shameful display...
   PL:
355. [Kwestia głosowa [choice_success_p_10305_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=choice_success_p_10305_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [choice_success_p_10305_2] (Check Passed)] 예술적인 솜씨!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=choice_success_p_10305_2].dlg
   limit: do 120 znaków
   EN: Poetry in motion!
   PL:
357. [Kwestia głosowa [choice_fail_n_10305_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=choice_fail_n_10305_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [choice_fail_n_10305_1] (Check Failed)] 아하, 이거… 미안하군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=choice_fail_n_10305_1].dlg
   limit: do 120 znaków
   EN: Ahh, this was... I beg forgiveness.
   PL:
359. [Kwestia głosowa [battle_clear_10305_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_clear_10305_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_clear_10305_1] (Victory Cry)] 치열한 결투였소! 그대들도 뛰어났네만… 흠, 다음 결투가 더 기다려지는군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_clear_10305_1].dlg
   limit: do 120 znaków
   EN: A fervorous duel! You lot were no slouches, yet... Hm, I eagerly await your next challenge.
   PL:
361. [Kwestia głosowa [battle_clear_ex_10305_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_clear_ex_10305_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [battle_clear_ex_10305_1] (Extra Conditions Fulfilled)] 보람차군! 그대들도 뛰어났네만, 내가 쪼오금 더 나았군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_clear_ex_10305_1].dlg
   limit: do 120 znaków
   EN: Wonderful! You were surpassed by my skill, though only by a little.
   PL:
363. [Kwestia głosowa [battle_defeat_10305_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_defeat_10305_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [battle_defeat_10305_1] (Defeat Wail)] 큭… 심히 치욕스럽군…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Cinq_10305.json :: dataList[id=battle_defeat_10305_1].dlg
   limit: do 120 znaków
   EN: Ugh... How disgraceful...!
   PL:

## [000] The Middle Little Sister — Don Quixote — 중지 작은 아우
- ID Tożsamości: `10306` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 86 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

365. [Karta Tożsamości — tytuł] 중지\n작은 아우
   źródło: Personalities.json :: dataList[id=10306].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Middle\nLittle Sister
   PL:
366. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10306].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10306].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Karta Tożsamości — opis] 돈키호테의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10306].desc
   limit: do 120 znaków
   EN: Don Quixote’s 6th Identity
   PL:
369. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 장부 확인
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=1].name ; dataList[id=1030601].levelList[level=2].name ; dataList[id=1030601].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Checking the Book
   PL:
370. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 자신의 정신력 5 회복
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=2].desc ; dataList[id=1030601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP on self
   PL:
373. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
374. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
375. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 의리 증명
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].name ; dataList[id=1030602].levelList[level=2].name ; dataList[id=1030602].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Proof of Loyalty
   PL:
376. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./3) (Max 4)
   PL:
377. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
378. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 피해량 감소 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1030602].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Damage Down
   PL:
379. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./3) (Max 4)\nIf the highest A-Reson is Envy A-Reson, Gain 50% additional Offense Level to the Offense Level gained by the above effect (rounded down)
   PL:
380. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] (가장 높은 완전 공명 수/2)만큼 이 스킬의 공격 레벨이 1 증가 (최대 6)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)\n전투 참가 가능 수가 7인 이하인 집중 전투에서는 증가하는 공격 레벨이 2배로 적용됨.
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./2) (Max 6)\nIf the highest A-Reson is Envy A-Reson., boost the Offense Level gained by the above effect by 50% (rounded down)\nGain double the Offense Level from the above effects in Focused Encounters with 7 or fewer Participant Limits.
   PL:
381. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량 감소 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Damage Down
   PL:
382. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 정의로운 앙갚음
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].name ; dataList[id=1030603].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: A Just Vengeance
   PL:
383. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./3) (Max 4)\nIf the highest A-Reson is Envy A-Reson, Gain 50% additional 'Offense Level' to the 'Offense Level' gained by the above effect (rounded down)
   PL:
384. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [EndSkill] 대상이 사망하면 정신력이 가장 낮은 아군 1명의 정신력 6 회복
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] If target is defeated, 1 ally with the least SP heals 6 SP
   PL:
388. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] (가장 높은 완전 공명 수/2)만큼 이 스킬의 공격 레벨이 1 증가 (최대 6)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)\n전투 참가 가능 수가 7인 이하인 집중 전투에서는 증가하는 공격 레벨이 2배로 적용됨.
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=4].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Obrona (ulepszenia 1,4) — nazwa] 배로 갚기
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=1].name ; dataList[id=1030604].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Multifold Retribution
   PL:
390. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 3 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 3
   PL:
391. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 3 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Obrona (ulepszenie 4) — opis] [StartBattle] 질투 완전 공명 수의 합이 6 이상이면, 반격 시 '정의로운 앙갚음' 스킬을 사용함.\n변경 시 해당 스킬의 속성이 질투로 변경됨.\n(조작 패널의 왼쪽 슬롯 스킬부터 발동. 턴 당 최대 2회 발동)
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] At 6+ sum of Envy A-Reson., use 'A Just Vengeance' as Counter.\nUpon activating the above effect, the Skill's affinity is changed to Envy.\n(Leftmost 'Multifold Retribution' is activated first. Activates 2 times per turn)
   PL:
393. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 5
   PL:
394. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Obrona (ulepszenia 3–4) — nazwa] 정의로운 앙갚음
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].name ; dataList[id=1030605].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 4 · monety: 4 (+3)
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Obrona (ulepszenie 3) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].desc
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Obrona (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Obrona (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Obrona (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Obrona (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [EndSkill] 대상이 사망하면 정신력이 가장 낮은 아군 1명의 정신력 6 회복
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Obrona (ulepszenie 4) — opis] [StartBattle] (가장 높은 완전 공명 수/2)만큼 이 스킬의 공격 레벨이 1 증가 (최대 6)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)\n전투 참가 가능 수가 6인 이하인 전투에서는 증가하는 공격 레벨이 2배로 적용됨.
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./2) (Max 6)\nIf the highest A-Reson is Envy A-Reson, Gain 50% additional Offense Level to the Offense Level gained by the above effect (rounded down)\nGain double the Offense Level from above effects in encounters with 6 or fewer Participant Limits.
   PL:
402. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — nazwa] 원한 문신
   źródło: Passives.json :: dataList[id=1030601].name
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL:
403. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — opis] - 자신을 포함한 아군이 3번 피격당할 때마다 다음 턴에 질투 피해량 증가 1을 얻음. (최대 5)\n- 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 최종 위력 1 증가
   źródło: Passives.json :: dataList[id=1030601].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Gain 1 Envy DMG Up next turn every time the enemies strike an ally(including this unit) 3 times. (Max 5)\n- Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Final Power +1
   PL:
404. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Envy) — nazwa] 원한 문신
   źródło: Passives.json :: dataList[id=1030611].name
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Envy) — opis] - 자신을 포함한 아군이 3번 피격당할 때마다 다음 턴에 질투 피해량 증가 1을 얻음. (최대 5)\n- 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 코인 위력 1 증가
   źródło: Passives.json :: dataList[id=1030611].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Gain 1 Envy DMG Up next turn every time the enemies strike an ally(including this unit) 3 times. (Max 5)\n- Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Coin Power +1
   PL:
406. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 편 가르기
   źródło: Passives.json :: dataList[id=1030621].name
   limit: do 40 znaków
   EN: Favoritism
   PL:
407. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 최대 체력이 가장 낮은 아군 1명이 자신을 제외한 아군의 피격 횟수 6회마다 다음 턴에 타격 피해량 증가 1을 얻음. (최대 2)
   źródło: Passives.json :: dataList[id=1030621].desc
   limit: do 180 znaków
   EN: 1 ally with the lowest Max HP gains 1 Blunt DMG Up next turn every time the enemies strike an ally(not including this unit) 6 times. (Max 2)
   PL:
408. [Kwestia głosowa [get_10306_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=get_10306_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Kwestia głosowa [get_10306_1] (Identity Acquisition)] 돈키호테요! 중지의 작은 아우이자, 작은 형님의 든든한 수하! 잘 부탁하네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=get_10306_1].dlg
   limit: do 170 znaków
   EN: Call me Don Quixote! A Little Sister of the Middle, and a trusty minion to the Big Brother! Pleased to make thine acquaintance!
   PL:
410. [Kwestia głosowa [lobby_morning_10306_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=lobby_morning_10306_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Kwestia głosowa [lobby_morning_10306_1] (Morning Greeting)] 멋진 아침일세! 오늘 작은 형님께서 어딜 가시는지 알고 있는가? 내게도 알려주게!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=lobby_morning_10306_1].dlg
   limit: do 140 znaków
   EN: 'Tis a wonderful morn! Art thou aware of the goings of the Big Brother today? Share with me such details!
   PL:
412. [Kwestia głosowa [lobby_noon_10306_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=lobby_noon_10306_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Kwestia głosowa [lobby_noon_10306_1] (Afternoon Greeting)] 작은 형님께서 오늘은 외식이라고 하셨네! 그대도 함께 가는가? 심지어 사주신다고 하는군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=lobby_noon_10306_1].dlg
   limit: do 160 znaków
   EN: The Big Brother invites me to dine out together this lunch! Wilt thou be joining us? Marry, he so generously offered to pay!
   PL:
414. [Kwestia głosowa [lobby_night_10306_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=lobby_night_10306_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Kwestia głosowa [lobby_night_10306_1] (Evening Greeting)] 저녁은 파티가 어울리지! 우리의 저녁식사는 언제나 파티 같네! 다들 떠들썩하고, 언제나 재밌는 이야기가 가득하지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=lobby_night_10306_1].dlg
   limit: do 160 znaków
   EN: 'Tis only proper that a party accompanies a dinner! Our dinners are always party-like, full of busy, jovial chatters.
   PL:
416. [Kwestia głosowa [smalltalk_10306_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Kwestia głosowa [smalltalk_10306_1] (Chatter #1)] 중지의 사람과 식구를 건드는 것이야말로 죄악이지. 그것을 몇 배로 되갚아 주는 것이 정의고!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_1].dlg
   limit: do 180 znaków
   EN: True villainy is to bother a member, a family of the Middle! And to smite our two—no, threefold vengeance upon those curs is true justice!
   PL:
418. [Kwestia głosowa [smalltalk_10306_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Kwestia głosowa [smalltalk_10306_2] (Chatter #2)] 우리 작은 형님께서는 머리스타일에 신경을 많이 쓰시는 분일세. 가장 잘 나가는 항구선의… 비싼 가게를 가신다더군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_2].dlg
   limit: do 220 znaków
   EN: Our Big Brother is one who pays much care to styling his hair. It is said that he frequents a... rather boutique hair shop in one of the portships marked by affluence.
   PL:
420. [Kwestia głosowa [smalltalk_10306_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Kwestia głosowa [smalltalk_10306_3] (Chatter #3)] 작은 형님의 강력함은 내가 감히 견주어 볼 깜냥도 되지는 않지만… 그래도 나와 몇 배나 차이가 날지 간혹 궁금해지곤 한다네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_3].dlg
   limit: do 180 znaków
   EN: Though mine strength may be incomparable to the Big Brother's... I must still muse. Is he stronger than I tenfold? A hundredfold? Hm hm!
   PL:
422. [Kwestia głosowa [smalltalk_10306_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Kwestia głosowa [smalltalk_10306_4] (Post-Uptie Chat 1)] 하하, 그러게 우리 사람을 왜 건드렸는가? 자, 이제 죗값을 치르시게나!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_4].dlg
   limit: do 120 znaków
   EN: Ha ha! Wherefore hath thou meddled with one of our own? Now, pay thy price!
   PL:
424. [Kwestia głosowa [smalltalk_10306_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Kwestia głosowa [smalltalk_10306_5] (Post-Uptie Chat 2)] 자, 잘 들여다보게. 이것이… 앙갚음 장부라는 것일세. 정의를 위해 해야할 것들이 적혀있다네.\n여기 그대의 이름이 있지? 지워지길 바라나? 그럼… 그만 죽어야겠군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=smalltalk_10306_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lo! Read it well, for this is the Book of Vengeance. Here are tasks that we must complete to achieve justice.\nBehold, written here is thy name. Wouldst thou like for me to erase it? ... Then thou must perish.
   PL:
426. [Kwestia głosowa [neglect_10306_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=neglect_10306_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Kwestia głosowa [neglect_10306_1] (Idle)] 빈 시간을 활용해서 장부를 정리하는 것이 중요하지. 언젠가 나도 작은 누님… 아니 큰 누님까지 될테니!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=neglect_10306_1].dlg
   limit: do 150 znaków
   EN: 'Tis important to keep the Book organized. For one day I shall rise to become a Big Sister... nay, a Great Sister!
   PL:
428. [Kwestia głosowa [gacksung_10306_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=gacksung_10306_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Kwestia głosowa [gacksung_10306_1] (Uptying)] 작은 형님께서 내게 장부의 처리를 맡기셨네! 하하, 이것 참! 기대에 보답해드려야겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=gacksung_10306_1].dlg
   limit: do 190 znaków
   EN: I have been tasked by the Big Brother himself to carry out this quest for the Book of Vengeance! Haha, heigh-ho! I must live up to his expectations!
   PL:
430. [Kwestia głosowa [formation_10306_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=formation_10306_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Kwestia głosowa [formation_10306_1] (Deployment)] 되갚아줄 상대가 있나보군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=formation_10306_1].dlg
   limit: do 120 znaków
   EN: There be a cur who deserves our vengeance, then?!
   PL:
432. [Kwestia głosowa [battleentry_10306_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battleentry_10306_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Kwestia głosowa [battleentry_10306_1] (Stage Entry)] 본인이 나서지!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battleentry_10306_1].dlg
   limit: do 120 znaków
   EN: Allow me!
   PL:
434. [Kwestia głosowa [battle_select_10306_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_select_10306_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Kwestia głosowa [battle_select_10306_1] (Viewed in Battle)] 아! 작은 형님께서 부르셨나?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_select_10306_1].dlg
   limit: do 120 znaków
   EN: Ah! Hath the Big Brother summoned me?
   PL:
436. [Kwestia głosowa [battle_endcommand_10306_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_endcommand_10306_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Kwestia głosowa [battle_endcommand_10306_1] (Commencing Attack)] 하하! 가세!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_endcommand_10306_1].dlg
   limit: do 120 znaków
   EN: Ha ha! Charge!
   PL:
438. [Kwestia głosowa [battle_enemy_break_10306_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_enemy_break_10306_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Kwestia głosowa [battle_enemy_break_10306_1] (Enemy Stagger)] 정신 차리게, 장부에 따르면 맨정신에 죽여야 하니까.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_enemy_break_10306_1].dlg
   limit: do 120 znaków
   EN: Steel thyself! The Book demands that thy death be carried out in clear mind.
   PL:
440. [Kwestia głosowa [battle_break_10306_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_break_10306_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Kwestia głosowa [battle_break_10306_1] (Staggered)] 아닛…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_break_10306_1].dlg
   limit: do 120 znaków
   EN: No...!
   PL:
442. [Kwestia głosowa [battle_kill_10306_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_kill_10306_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Kwestia głosowa [battle_kill_10306_1] (Enemy Killed)] 이걸로 되갚았군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_kill_10306_1].dlg
   limit: do 120 znaków
   EN: Vengeance hath been executed.
   PL:
444. [Kwestia głosowa [battle_dead_10306_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_dead_10306_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Kwestia głosowa [battle_dead_10306_1] (Death)] 여기서… 끝나다니… 하지만, 중지는 기억할 거다…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_dead_10306_1].dlg
   limit: do 120 znaków
   EN: To end here... is... No. The Middle... will remember...
   PL:
446. [Kwestia głosowa [choice_success_p_10306_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=choice_success_p_10306_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Kwestia głosowa [choice_success_p_10306_2] (Check Passed)] 하! 더 어려운 것 없나?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=choice_success_p_10306_2].dlg
   limit: do 120 znaków
   EN: Hah! Bring forth a real challenge!
   PL:
448. [Kwestia głosowa [choice_fail_n_10306_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=choice_fail_n_10306_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Kwestia głosowa [choice_fail_n_10306_1] (Check Failed)] 본인의 의지가 모자랐나보군…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=choice_fail_n_10306_1].dlg
   limit: do 120 znaków
   EN: Mine conviction must have fallen short...
   PL:
450. [Kwestia głosowa [battle_clear_10306_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_clear_10306_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Kwestia głosowa [battle_clear_10306_1] (Victory Cry)] 마지막까지 잘 갚아줬군! 오늘 저녁에 자랑할 거리가 늘었어!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_clear_10306_1].dlg
   limit: do 120 znaków
   EN: Thus this Vengeance hath been carried out to the end! There is more to boast this evening!
   PL:
452. [Kwestia głosowa [battle_clear_ex_10306_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_clear_ex_10306_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Kwestia głosowa [battle_clear_ex_10306_1] (Extra Conditions Fulfilled)] 어디보자…  그래! 장부의 이쪽 줄을 지우면 되겠군. 본인도 이번에 한몫했으니, 작은 형님께서 흡족해 하시겠어!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_clear_ex_10306_1].dlg
   limit: do 190 znaków
   EN: Let's see... Indeed! This entire row may be crossed out. The Big Brother must be pleased, for I have played a significant part in this quest!
   PL:
454. [Kwestia głosowa [battle_defeat_10306_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_defeat_10306_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Kwestia głosowa [battle_defeat_10306_1] (Defeat Wail)] 중지는 기억하고.. 기록해서… 되갚는다는 것을 잊지 말게나.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_MiddleFinger_10306.json :: dataList[id=battle_defeat_10306_1].dlg
   limit: do 150 znaków
   EN: Lest you forget... The Middle remembers... The Middle records... And Vengeance shall rain down upon thee tenfold.
   PL:

## [00] Lobotomy E.G.O::Lantern — Don Quixote — 로보토미 E.G.O:: 초롱
- ID Tożsamości: `10307` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: wydarzenie 9102 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

456. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n초롱
   źródło: Personalities.json :: dataList[id=10307].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Lantern
   PL:
457. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10307].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10307].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Karta Tożsamości — opis] 돈키호테의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10307].desc
   limit: do 120 znaków
   EN: Don Quixote’s 7th Identity
   PL:
460. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 씹어주겠네!
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=1].name ; dataList[id=1030701].levelList[level=2].name ; dataList[id=1030701].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: I Shall Nibble Thee!
   PL:
461. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict +2 [Burst] Count
   PL:
462. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 1을 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +1 [Aggro] to this Skill Slot next turn
   PL:
463. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
464. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 3를 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL:
465. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 발광 미끼
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].name ; dataList[id=1030702].levelList[level=2].name ; dataList[id=1030702].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Flashing Lure
   PL:
466. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL:
467. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL:
469. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 2를 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn
   PL:
470. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
471. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1030702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
473. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수가 2 이하면, [Burst] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 2 or less [Burst] Count, inflict +2 [Burst] Count
   PL:
474. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 4를 얻음\n[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +4 [Aggro] to this Skill Slot next turn\n[WhenUse] If target has 6+ [Burst], Coin Power +1
   PL:
475. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수가 2 이하면, [Burst] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 2 or less [Burst] Count, inflict +3 [Burst] Count
   PL:
476. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 빙글빙글 냠냠냠!
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].name ; dataList[id=1030703].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Whirlwind Om-Nom-Nom!
   PL:
477. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 3를 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL:
479. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 체력 10 회복.
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 HP.
   PL:
480. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 체력 추가 회복 ([Burst] 1 당 체력 1 회복. 최대 20)
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Heal additional HP based on [Burst] on target (1 HP healed per 1 [Burst]. Max 20)
   PL:
481. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] 자신의 체력이 최대 체력의 50% 미만이면 코인 1회 재사용
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1030703].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   EN: At 50%- HP, reuse Coin once
   PL:
482. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 5를 얻음\n[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +5 [Aggro] to this Skill Slot next turn\n[WhenUse] If target has 6+ [Burst], Coin Power +1
   PL:
483. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 체력 15 회복. 코인 재사용 시 체력 회복량 50% 증가.
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 15 HP. Heal by +50% more HP when reusing Coin.
   PL:
484. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 체력 추가 회복 ([Burst] 1 당 체력 2 회복. 최대 40)
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Heal additional HP based on [Burst] on target (2 HP healed per 1 [Burst]. Max 40)
   PL:
485. [Obrona (ulepszenia 1,4) — nazwa] 들썩이는 이빨
   źródło: Skills_personality-03.json :: dataList[id=1030704].levelList[level=1].name ; dataList[id=1030704].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Chattering Teeth
   PL:
486. [Obrona (ulepszenie 1) — opis] [EndBattle] 남은 보호막 수치만큼 체력 회복 (턴 당 1회. 최대 회복량: 최대 체력의 10%)
   źródło: Skills_personality-03.json :: dataList[id=1030704].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Heal HP equal to remaining Shield HP (Once per turn. Max Heal amount: 10% of Max HP)
   PL:
487. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면 최종 위력 +3\n[EndBattle] 남은 보호막 수치만큼 체력 회복 (턴 당 1회. 최대 회복량: 최대 체력의 10%)
   źródło: Skills_personality-03.json :: dataList[id=1030704].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] If target has 6+ [Burst], Final Power +3\n[EndBattle] Heal HP equal to remaining Shield HP (Once per turn. Max Heal amount: 10% of Max HP)
   PL:
488. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 잘근잘근 냠냠
   źródło: Passives.json :: dataList[id=1030701].name
   limit: do 40 znaków
   EN: Om Nom Nom
   PL:
489. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 자신의 스킬 슬롯에 [Aggro]가 있을 때 합 위력 +1\n명령 페이즈에서 자신을 공격 스킬의 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 4 회복 (환상체인 경우 부위로 판정)
   źródło: Passives.json :: dataList[id=1030701].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: If this unit's Skill Slot has [Aggro], Clash Power +1\nHeal 4 HP every time this unit hits enemies that targeted this unit with an Attack Skill in the Chaining Phase (For Abnormalities, the Parts that targeted this unit with an Attack Skill)
   PL:
490. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 잘근잘근 냠냠
   źródło: Passives.json :: dataList[id=1030711].name
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 자신의 스킬 슬롯에 [Aggro]가 있을 때 합 위력 +1\n명령 페이즈에서 자신을 공격 스킬의 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 6 회복 (환상체인 경우 부위로 판정)
   źródło: Passives.json :: dataList[id=1030711].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: If this unit's Skill Slot has [Aggro], Clash Power +1\nHeal 6 HP every time this unit hits enemies that targeted this unit with an Attack Skill in the Chaining Phase (For Abnormalities, each Part is calculated separately)
   PL:
492. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 초롱초롱
   źródło: Passives.json :: dataList[id=1030721].name
   limit: do 40 znaków
   EN: Illumilantern
   PL:
493. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] [Aggro]가 가장 높은 슬롯을 보유한 아군 1명이 자신을 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 2 회복 ([Aggro]가 없으면 적용되지 않음.)
   źródło: Passives.json :: dataList[id=1030721].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: The ally with the highest [Aggro] Skill Slot heals 2 HP every time they hit an enemy that targets this unit (Does not apply to units without [Aggro])
   PL:
494. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Glut.) — nazwa] 초롱초롱
   źródło: Passives.json :: dataList[id=1030731].name
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Glut.) — opis] [Aggro]가 가장 높은 슬롯을 보유한 아군 1명이 자신을 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 4 회복 ([Aggro]가 없으면 적용되지 않음.)
   źródło: Passives.json :: dataList[id=1030731].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: The ally with the highest [Aggro] Skill Slot heals 4 HP every time they hit an enemy that targets this unit (Does not apply to units without [Aggro])
   PL:
496. [Kwestia głosowa [get_10307_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=get_10307_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Kwestia głosowa [get_10307_1] (Identity Acquisition)] 이렇게 영롱하게 빛나는 초롱을 본 적 있는가? 이 몸과 있으면 어둠이 우리를 피해 도망다닐 것이네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=get_10307_1].dlg
   limit: do 150 znaków
   EN: Have thee ever beheld a Lantern so grossly incandescent? Remain at my side, and darkness shall never consume us!
   PL:
498. [Kwestia głosowa [lobby_morning_10307_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=lobby_morning_10307_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Kwestia głosowa [lobby_morning_10307_1] (Morning Greeting)] 오늘도 에너지를 모아보겠네! 지금은 조용한 이 복도에도, 곧 무슨 일이 벌어질지 무척이나 기대가 되지 않는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=lobby_morning_10307_1].dlg
   limit: do 220 znaków
   EN: Today is another day! Thus I shall toil to gather more energy. Dost thou not find thyself growing delighted at the notion of numerous happenings in this hallway today?
   PL:
500. [Kwestia głosowa [lobby_noon_10307_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=lobby_noon_10307_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Kwestia głosowa [lobby_noon_10307_1] (Afternoon Greeting)] 점심 시간이오, 본인은 그다지 배가 고프진 않지만… 이 조그만 이빨 친구들이 계속해서 들썩거리고 있군, 후후.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=lobby_noon_10307_1].dlg
   limit: do 160 znaków
   EN: 'Tis time for a midday meal. I am far from famished... alas, these little teeth fellows are chattering expectantly. Heh heh.
   PL:
502. [Kwestia głosowa [lobby_night_10307_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=lobby_night_10307_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Kwestia głosowa [lobby_night_10307_1] (Evening Greeting)] 이 시간이야말로 초롱이 빛나기에 제일 탁월한 시간 아니겠나.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=lobby_night_10307_1].dlg
   limit: do 120 znaków
   EN: Verily, is this not the time for the Lantern to shine?
   PL:
504. [Kwestia głosowa [smalltalk_10307_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Kwestia głosowa [smalltalk_10307_1] (Chatter #1)] 관리자 나리, 이것 좀 보시게! 복도 한가운데에 이렇게 예쁜 꽃이 피어있는게 너무 신기하지 않은가? 이렇게 만지니까 막 움직이고… 움찔거리고…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_1].dlg
   limit: do 230 znaków
   EN: Come hither and behold, Manager Esquire! Is it not so fascinating to see such a beaut of a flower in the middle of a hallway? Lo! If I poke it so, it fidgets and twitches...
   PL:
506. [Kwestia głosowa [smalltalk_10307_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Kwestia głosowa [smalltalk_10307_2] (Chatter #2)] 방금!!! 환상체의 탈출을 알리는 경보음이 들리지 않았는가? 빨리 빨리, 비켜 보시게, 이 몸이 나설 차례이니!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_2].dlg
   limit: do 190 znaków
   EN: FIE!!! Didst thou not hear the siren indicating that an Abnormality is on the loose? Make haste, make haste! Make way! 'Tis my chance to shine!
   PL:
508. [Kwestia głosowa [smalltalk_10307_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Kwestia głosowa [smalltalk_10307_3] (Chatter #3)] 이 털옷은 참 따뜻하오. 아 그렇다고 너무 쓰다듬으면 관리자 나리의 손가락, 한두 개 정도 없어질 수 있으니 조심하시는 게 좋을 것이오…!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_3].dlg
   limit: do 160 znaków
   EN: Quite warm it is, this furry garb! Ah, take care not to pet it too much. It may nibble thy finger off. Or fingers...!
   PL:
510. [Kwestia głosowa [smalltalk_10307_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Kwestia głosowa [smalltalk_10307_4] (Post-Uptie Chat 1)] 오티스 나리가 <color=#325339>(팀장이라 해야지!)</color> 에흠, 말해준 것이 있네만… 본인은 미끼 역할을 하는 것에 탁월한 재능이 있는 것 같소! 그러니까 위험한 일이 생기면 곧바로 내 뒤에 숨으시게나.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_4].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#325339>, </color>
   EN: Lady Outis <color=#325339>(It's Captain Outis!)</color> has, ahem, shared aught with me... That I may be quite adept at playing the role of a 'bait'! Quickly hide behind me at the first sign of danger, thou must!
   PL:
512. [Kwestia głosowa [smalltalk_10307_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Kwestia głosowa [smalltalk_10307_5] (Post-Uptie Chat 2)] 이 초롱을 가만히 보고 있으면 말이오, 마음이 참 따땃해지고 좋은 일만 생길 것 같지 않은가?\n비록 이곳이 좋은 일만 생길 리는 없는 곳이라고는 하지만…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=smalltalk_10307_5].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Behold this Lantern for a while. Dost thou not feel the warm heart and good fortune rumbling within thyself?\nEven at a place such as this where good fortune seems so ill-available...
   PL:
514. [Kwestia głosowa [neglect_10307_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=neglect_10307_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Kwestia głosowa [neglect_10307_1] (Idle)] 나리, 어디 계시는가? 이러다 숨어버린 나리를 초롱이 먼저 발견해서 물어버리면 어떡하려고!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=neglect_10307_1].dlg
   limit: do 130 znaków
   EN: To where hast thou gone, Manager Esquire?! Thou mustn't let the Lantern ambush and nibble thee!
   PL:
516. [Kwestia głosowa [gacksung_10307_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=gacksung_10307_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Kwestia głosowa [gacksung_10307_1] (Uptying)] 흥을 주체할 수가 없네, 나리!!! 오늘 이 몸이 더 제압할 악당들은 없는 것인가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=gacksung_10307_1].dlg
   limit: do 130 znaków
   EN: I cannot contain my joy Manager Esquire!!! Prithee, bring forth more villains for me to thrash!
   PL:
518. [Kwestia głosowa [formation_10307_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=formation_10307_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Kwestia głosowa [formation_10307_1] (Deployment)] 나! 훌륭한 미끼 될 수 있소!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=formation_10307_1].dlg
   limit: do 120 znaków
   EN: I! Can be quite the excellent bait, if I do say so myself!
   PL:
520. [Kwestia głosowa [battleentry_10307_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battleentry_10307_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Kwestia głosowa [battleentry_10307_1] (Stage Entry)] 발광할 시간인가!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battleentry_10307_1].dlg
   limit: do 120 znaków
   EN: Ah, my time to flash has come once again!
   PL:
522. [Kwestia głosowa [battle_select_10307_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_select_10307_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Kwestia głosowa [battle_select_10307_1] (Viewed in Battle)] 또 제압할 것이 있는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_select_10307_1].dlg
   limit: do 120 znaków
   EN: Is there aught else to suppress?!
   PL:
524. [Kwestia głosowa [battle_endcommand_10307_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_endcommand_10307_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Kwestia głosowa [battle_endcommand_10307_1] (Commencing Attack)] 잘근잘근 씹어버리겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_endcommand_10307_1].dlg
   limit: do 120 znaków
   EN: I shall chew thee to shreds!
   PL:
526. [Kwestia głosowa [battle_enemy_break_10307_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_enemy_break_10307_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Kwestia głosowa [battle_enemy_break_10307_1] (Enemy Stagger)] 곧 삼켜질 것이오, 기다리시게!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_enemy_break_10307_1].dlg
   limit: do 120 znaków
   EN: Just thee wait! Thou shall be devoured whole posthaste!
   PL:
528. [Kwestia głosowa [battle_break_10307_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_break_10307_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Kwestia głosowa [battle_break_10307_1] (Staggered)] 잠시, 망설인 것 뿐일세.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_break_10307_1].dlg
   limit: do 120 znaków
   EN: ... 'Twas but a moment of hesitation.
   PL:
530. [Kwestia głosowa [battle_kill_10307_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_kill_10307_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Kwestia głosowa [battle_kill_10307_1] (Enemy Killed)] 잘근잘근.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_kill_10307_1].dlg
   limit: do 120 znaków
   EN: Om nom.
   PL:
532. [Kwestia głosowa [battle_dead_10307_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_dead_10307_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Kwestia głosowa [battle_dead_10307_1] (Death)] 본인은… 늘 빛나고 있었는가…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_dead_10307_1].dlg
   limit: do 120 znaków
   EN: So I have always... shone so brightly...
   PL:
534. [Kwestia głosowa [choice_success_p_10307_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=choice_success_p_10307_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Kwestia głosowa [choice_success_p_10307_2] (Check Passed)] 역시 초롱을 따라가면 답이 보이지 않겠는가!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=choice_success_p_10307_2].dlg
   limit: do 120 znaków
   EN: Ah... to follow the Lantern is to walk the path of answers!
   PL:
536. [Kwestia głosowa [choice_fail_n_10307_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=choice_fail_n_10307_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Kwestia głosowa [choice_fail_n_10307_1] (Check Failed)] 답은… 보이지 않았네.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=choice_fail_n_10307_1].dlg
   limit: do 120 znaków
   EN: The answer... yet remains out of sight.
   PL:
538. [Kwestia głosowa [battle_clear_10307_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_clear_10307_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Kwestia głosowa [battle_clear_10307_1] (Victory Cry)] 오늘도, 멋지게 발광하지 않았는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_clear_10307_1].dlg
   limit: do 120 znaków
   EN: Have I not flashed so radiantly today?!
   PL:
540. [Kwestia głosowa [battle_clear_ex_10307_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_clear_ex_10307_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Kwestia głosowa [battle_clear_ex_10307_1] (Extra Conditions Fulfilled)] 역시, 깔끔하게 삼켜버리지 않았나! 호드님에게 칭찬이라도 받으면 좋겠소!!!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_clear_ex_10307_1].dlg
   limit: do 160 znaków
   EN: Thus I have gobbled them up without a trace! I hope Miss Hod finds it within herself to compliment mine achievements!
   PL:
542. [Kwestia głosowa [battle_defeat_10307_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_defeat_10307_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Kwestia głosowa [battle_defeat_10307_1] (Defeat Wail)] 이 이빨들에게 씹히는 건… 어째, 본인이었나 보오.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_LEGO_10307.json :: dataList[id=battle_defeat_10307_1].dlg
   limit: do 120 znaków
   EN: Fie, I was the one to be gobbled up by these very fangs...
   PL:

## [00] Blade Lineage Salsu — Don Quixote — 검계 살수
- ID Tożsamości: `10308` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 73 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise

544. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=10308].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL:
545. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10308].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10308].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Karta Tożsamości — opis] 돈키호테의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10308].desc
   limit: do 120 znaków
   EN: Don Quixote’s 8th Identity
   PL:
548. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발검
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].name ; dataList[id=1030801].levelList[level=2].name ; dataList[id=1030801].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Draw of the Sword
   PL:
549. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].desc ; dataList[id=1030801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
550. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030801].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL:
551. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030801].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 5 이상이면 코인 위력 +1\n</style>[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 5+ [Breath] on self, Coin Power +1\n</style>[WhenUse] Gain +2 [Breath] Count
   PL:
553. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL:
554. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 검궤
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].name ; dataList[id=1030802].levelList[level=2].name ; dataList[id=1030802].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Blade Arc
   PL:
556. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].desc ; dataList[id=1030802].levelList[level=2].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 2 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
558. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 위력을 가장 적게 보유한 아군 1명에게 [Breath] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030802].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 1 ally that either has no [Breath] or has the least [Breath] Potency, apply 2 [Breath]
   PL:
559. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
560. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 7 이상이면 코인 위력 +1\n</style>[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 7+ [Breath] on self, Coin Power +1\n</style>[WhenUse] Gain +2 [Breath] Count
   PL:
561. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 위력을 가장 적게 보유한 아군 1명에게 [Breath] 2 부여\n<style="highlight">대상이 검계 조직원이면 호흡 2 추가 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 1 ally that either has no [Breath] or has the least [Breath] Potency, apply 2 [Breath]\n<style="highlight">If the affected ally is from the Blade Lineage, apply 2 additional [Breath]</style>
   PL:
562. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 잘가시게!
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].name ; dataList[id=1030803].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Fare Thee Well!
   PL:
563. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]
   PL:
564. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +10% damage
   PL:
565. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 횟수를 가장 적게 보유한 아군 2명의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 2 allies that either have no [Breath] or have the least [Breath] Count, apply +2 [Breath] Count
   PL:
567. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [EndSkill] 대상이 사망했으면, 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [SlashDamageUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [EndSkill] If target is defeated, gain 1 [SlashDamageUp] next turn
   PL:
568. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 10 이상이면 코인 위력 +1\n</style>[WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 10+ [Breath] on self, Coin Power +1\n</style>[WhenUse] Gain 5 [Breath]
   PL:
569. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
570. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 횟수를 가장 적게 보유한 아군 2명의 [Breath] 횟수 2 증가.\n<style="highlight">대상이 검계 조직원이면 [Breath] 횟수 2 추가 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 2 allies that either have no [Breath] or have the least [Breath] Count, apply +2 [Breath] Count\n<style="highlight">If the affected ally is from the Blade Lineage, apply 2 additional [Breath] Count</style>
   PL:
571. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [EndSkill] 대상이 사망했으면, <style="highlight">자신과 무작위 아군 1명에게 다음 턴에 [SlashDamageUp] 1 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [SlashDamageUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [EndSkill] If target is defeated, <style="highlight">apply 1 [SlashDamageUp] to self and 1 random other ally next turn</style>
   PL:
572. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-03.json :: dataList[id=1030804].levelList[level=1].name ; dataList[id=1030804].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — nazwa] 함께 쉬는 숨
   źródło: Passives.json :: dataList[id=1030801].name
   limit: do 40 znaków
   EN: Collective Breathing
   PL:
574. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — opis] 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때, [Breath]이 없거나 [Breath] 위력이 가장 낮은 아군 1명에게 [Breath] 1 부여 (최대 3회)
   źródło: Passives.json :: dataList[id=1030801].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When this unit gains [Breath] Potency using its own Skill or Coin effects: Apply 1 [Breath] Potency to 1 ally that either has no [Breath] or has the least [Breath] Potency (max 3 times)
   PL:
575. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — nazwa] 함께 쉬는 숨
   źródło: Passives.json :: dataList[id=1030811].name
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — opis] 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때, [Breath]이 없거나 [Breath] 위력이 가장 낮은 아군 1명에게 [Breath] 1 부여 (최대 5회)
   źródło: Passives.json :: dataList[id=1030811].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When this unit gains [Breath] Potency using its own Skill or Coin effects: Give 1 [Breath] Potency to 1 ally that either has no [Breath] or has the least [Breath] Potency (max 5 times)
   PL:
577. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 밤 산책
   źródło: Passives.json :: dataList[id=1030821].name
   limit: do 40 znaków
   EN: Nightly Stroll
   PL:
578. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] [Breath]을 가장 적게 보유한 아군 1명이 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때 얻는 [Breath] 위력 +1 (최대 2회. [Breath]이 없는 대상에게는 적용되지 않음)
   źródło: Passives.json :: dataList[id=1030821].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: 1 ally that has the least [Breath] gains 1 more [Breath] Potency when gaining [Breath] Potency using its own Skill or Coin effects (max 2 times; does not apply to allies that do not have [Breath])
   PL:
579. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Pride) — nazwa] 밤 산책
   źródło: Passives.json :: dataList[id=1030831].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Pride) — opis] [Breath]을 가장 적게 보유한 아군 1명이 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때 얻는 [Breath] 위력 +2 (최대 2회. [Breath]이 없는 대상에게는 적용되지 않음)
   źródło: Passives.json :: dataList[id=1030831].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: 1 ally that has the least [Breath] gains 2 more [Breath] Potency when gaining [Breath] Potency using its own Skill or Coin effects (max 2 times; does not apply to allies that do not have [Breath])
   PL:
581. [Kwestia głosowa [get_10308_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=get_10308_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [get_10308_1] (Identity Acquisition)] 주도… 라니, 본인은 그런 건 잘 모르네만. 켁, 이거 왜 이렇게 쓴가?!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=get_10308_1].dlg
   limit: do 160 znaków
   EN: The way of... Wine? Drinking etiquette? Forsooth, I am quite unacquainted with that subject. Kaugh, 't-tis quite bitter!
   PL:
583. [Kwestia głosowa [lobby_morning_10308_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=lobby_morning_10308_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [lobby_morning_10308_1] (Morning Greeting)] 좋은 아침일세! 주변이 다소 칙칙하긴 하지만, 흠~ 이 청량한 향취는 좋지 않은가?\n정찰을 하기에도, 이른 아침이 가장 적합하지!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=lobby_morning_10308_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Good morrow to thee! Though the weather may be quite dreary, hm~ This crisp smell of daybreak is quite pleasant, is it not?\n'Tis the perfect time for a reconnaissance, indeed!
   PL:
585. [Kwestia głosowa [lobby_noon_10308_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=lobby_noon_10308_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [lobby_noon_10308_1] (Afternoon Greeting)] 낮에는 검술을 다듬는 시간이 길어서 말일세, 특별히 식사를 하지는 않는 편이지.\n그보다, 정찰에서 무슨 일이 있었는가 하면…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=lobby_noon_10308_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, oft do I forgo a midday meal in favor of honing my skills with a blade.\nForget that, for I must now narrate the events of my reconnaissance!
   PL:
587. [Kwestia głosowa [lobby_night_10308_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=lobby_night_10308_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [lobby_night_10308_1] (Evening Greeting)] 음… 밤에는 술과 함께 식사를 하는 문화가 있다는데, 내게는 잘 안 맞는게 아닌가 싶네… 그저 육전이나 실컷 먹고 싶소만!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=lobby_night_10308_1].dlg
   limit: do 250 znaków
   EN: Mm... I have heard tale of a culture that oft sups alongside an alcoholic beverage, indeed. Yet it ill-fits my temperament... I merely wish to gorge myself on slabs of meaty yukjeon(meat fritter)!
   PL:
589. [Kwestia głosowa [smalltalk_10308_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [smalltalk_10308_1] (Chatter #1)] 본인은 검이나 실컷 휘두루고 싶소! 이런 곳에서 술 마시는 방법이나 공부할 줄은…\n이, 이 말은 오티스 나리께 들어가지 않게 해주시게!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I wish only to twirl and let my blade sing with abandon! Seldom did I expect me to be forced to learn 'the way of wine'... \n... P-prithee, do not let Lady Outis hear of my complaints!
   PL:
591. [Kwestia głosowa [smalltalk_10308_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [smalltalk_10308_2] (Chatter #2)] 병으로 마시나, 잔에 따라서 마시나 결과는 같은 것 아니오? 왜 검 외의 것에 그리도 집착하는지.\n그런 것보다 흑운회, 그 작자들이 뭘 작당하고 있는지 들어야 하지 않겠는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_2].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sip from a bottle, sip from a cup... what difference does it make? It ends up in my gullet all the same. I am befuddled at why any would focus on a subject so irrelevant from the blade.\nFie, I care not for such trifles. Thou must hear of the mischief the Kurokumo Clan is up to.
   PL:
593. [Kwestia głosowa [smalltalk_10308_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [smalltalk_10308_3] (Chatter #3)] 본인이 느끼기엔, 검의 궤적을 따라 무언가를 베는 것은 훌륭한 식사를 하는 것보다 훨씬 즐거운 일인 것 같네!\n막, 손끝에 느껴지는 저항감에 두근두근하지 않는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_3].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tis my belief that to cut something along the arc of my blade is much more satisfying than indulging in a succulent meal!\nThe sensation of that slight resistance as the blade cuts through the mass... 'tis quite exhilarating, wouldst thou not agree?
   PL:
595. [Kwestia głosowa [smalltalk_10308_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [smalltalk_10308_4] (Post-Uptie Chat 1)] 행인이 있을 시간이 아닌데 소란스럽더니… 이런 불청객들이 있지 않았겠는가?\n이 시간에는 아무도 지나다니지 않는 것이 옳으니, 본인이 옳게 해두었지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_4].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I sensed that we may find ourselves a few unwelcome guests! I deduced it from the untimely stirring, indeed.\n'Tis only right that no traveler graces the roads at this time. So I have righted all the wrongs.
   PL:
597. [Kwestia głosowa [smalltalk_10308_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [smalltalk_10308_5] (Post-Uptie Chat 2)] 검술을 다듬으며 공기를 가르는 것과, 가도를 지나며 베어낼 것을 베어내는 일은 크게 다를게 없네.\n기껏해야… 음, 손 끝에 느껴지는 무게의 차이가 있겠군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=smalltalk_10308_5].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To slice through the air as I train myself in the way of blades, and to hew the deserving ones as I walk the path... there is very little difference.\nIf I were to make a distinction... mm, I must say, the only difference is the weight in my hands.
   PL:
599. [Kwestia głosowa [neglect_10308_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=neglect_10308_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [neglect_10308_1] (Idle)] 달빛이 좋군… 검에 상처는 나지 않았나… 후우, 이제 먼지 한 톨도 없군.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=neglect_10308_1].dlg
   limit: do 160 znaków
   EN: 'Tis a moonlight most fair... Hath the battle left nicks in my blade...? Whew, not even a speck of dust remains on its edge.
   PL:
601. [Kwestia głosowa [gacksung_10308_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=gacksung_10308_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [gacksung_10308_1] (Uptying)] 아, 바깥이 소란스러워서 말일세. 잠시 둘러보며 산책이나 해도 되겠는가?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=gacksung_10308_1].dlg
   limit: do 140 znaków
   EN: Ah, 'twas naught but the noise outside. Wouldst thou mind if I should go on a little stroll to investigate?
   PL:
603. [Kwestia głosowa [formation_10308_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=formation_10308_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [formation_10308_1] (Deployment)] 음? 잠시, 이것만 삼키고…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=formation_10308_1].dlg
   limit: do 120 znaków
   EN: Hm? Ah, give me but a moment—I must first swallow this...
   PL:
605. [Kwestia głosowa [battleentry_10308_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battleentry_10308_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [battleentry_10308_1] (Stage Entry)] 뛰어가겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battleentry_10308_1].dlg
   limit: do 120 znaków
   EN: I shall scurry there posthaste!
   PL:
607. [Kwestia głosowa [battle_select_10308_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_select_10308_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [battle_select_10308_1] (Viewed in Battle)] 조금 바쁘네만?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_select_10308_1].dlg
   limit: do 120 znaków
   EN: I am quite busy at the moment!
   PL:
609. [Kwestia głosowa [battle_endcommand_10308_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_endcommand_10308_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [battle_endcommand_10308_1] (Commencing Attack)] 즐겁겠군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_endcommand_10308_1].dlg
   limit: do 120 znaków
   EN: How thrilling!
   PL:
611. [Kwestia głosowa [battle_enemy_break_10308_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_enemy_break_10308_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [battle_enemy_break_10308_1] (Enemy Stagger)] 응? 아하, 빗겨베어버렸군…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_enemy_break_10308_1].dlg
   limit: do 120 znaków
   EN: Hm? Aha, I must not have struck true...
   PL:
613. [Kwestia głosowa [battle_break_10308_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_break_10308_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [battle_break_10308_1] (Staggered)] 으앗!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_break_10308_1].dlg
   limit: do 120 znaków
   EN: Uagh!
   PL:
615. [Kwestia głosowa [battle_kill_10308_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_kill_10308_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [battle_kill_10308_1] (Enemy Killed)] 음, 확실하게 갈라지는 감각이었네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_kill_10308_1].dlg
   limit: do 120 znaków
   EN: Ah, truly! 'Twas a flesh-splitting sensation!
   PL:
617. [Kwestia głosowa [battle_dead_10308_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_dead_10308_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Kwestia głosowa [battle_dead_10308_1] (Death)] 아앗, 하… 그래, 언젠가는… 이렇게 베일 줄도… 알았지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_dead_10308_1].dlg
   limit: do 120 znaków
   EN: Aah, haah... Forsooth, well did I expect to be... hewn... myself.
   PL:
619. [Kwestia głosowa [choice_success_p_10308_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=choice_success_p_10308_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Kwestia głosowa [choice_success_p_10308_2] (Check Passed)] 이보게! 본인이 해냈네~
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=choice_success_p_10308_2].dlg
   limit: do 120 znaków
   EN: Heigh-ho! I have done it~!
   PL:
621. [Kwestia głosowa [choice_fail_n_10308_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=choice_fail_n_10308_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Kwestia głosowa [choice_fail_n_10308_1] (Check Failed)] 으, 으음~ 이렇게 하는게 아니었나…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=choice_fail_n_10308_1].dlg
   limit: do 120 znaków
   EN: Uh-ahm~ I-I suppose I have made a mistake...
   PL:
623. [Kwestia głosowa [battle_clear_10308_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_clear_10308_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Kwestia głosowa [battle_clear_10308_1] (Victory Cry)] 가벼운 산책을 한 기분이네. 이제 돌아가… 면 오티스 나리가 있겠군. 아이고~
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_clear_10308_1].dlg
   limit: do 150 znaków
   EN: 'Twas naught but a quick jaunt indeed. Now I return with a lighter heart to... where Lady Outis awaits. Drat...
   PL:
625. [Kwestia głosowa [battle_clear_ex_10308_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_clear_ex_10308_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Kwestia głosowa [battle_clear_ex_10308_1] (Extra Conditions Fulfilled)] 검을 잔뜩 휘둘러 버렸네! 이정도로 상쾌하고 개운한 기분이면, 그 고리타분한 이야기도 웃으며 들을 수 있겠지!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_clear_ex_10308_1].dlg
   limit: do 190 znaków
   EN: I have swung my blade with abandon! Ah, how refreshing, how exhilarating! Now, I may have enough patience to sit through such interminable lectures!
   PL:
627. [Kwestia głosowa [battle_defeat_10308_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_defeat_10308_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Kwestia głosowa [battle_defeat_10308_1] (Defeat Wail)] 검술에 흠이 있었나보네… 본인이 많이 물러졌나보군. 더 정진하겠네…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_SwordGroup_10308.json :: dataList[id=battle_defeat_10308_1].dlg
   limit: do 120 znaków
   EN: A flaw in my techniques... I must have grown complacent. I shall persevere...
   PL:

## [000] T Corp. Class 3 Collection Staff — Don Quixote — T사 3등급 징수직 직원
- ID Tożsamości: `10309` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 95 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

629. [Karta Tożsamości — tytuł] T사 3등급\n징수직 직원
   źródło: Personalities.json :: dataList[id=10309].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. Class 3\nCollection Staff
   PL:
630. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10309].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10309].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Karta Tożsamości — opis] 돈키호테의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10309].desc
   limit: do 120 znaków
   EN: Don Quixote’s 9th Identity
   PL:
633. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 징수 준비를 하지
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=1].name ; dataList[id=1030901].levelList[level=2].name ; dataList[id=1030901].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Let Us Prepare To Collect
   PL:
634. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL:
635. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
636. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Clash Power +1\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn</style>
   PL:
637. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL:
638. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Vibration] 6 당 합 위력 +1 (최대 2)</style>\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] Gain Clash Power +1 for every 6 [Vibration] on target (max 2)</style>\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL:
639. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 이 스킬 슬롯의 [Aggro] 4 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Aggro]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">[OnSucceedAttack] Gain +4 [Aggro] to this Skill Slot next turn</style>
   PL:
640. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] T사제 가속 절단기
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].name ; dataList[id=1030902].levelList[level=2].name ; dataList[id=1030902].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: T Corp. Accelerated Amputator
   PL:
641. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL:
642. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]을 최대 3 소모\n소모한 [Vibration]만큼 자신의 [Vibration] 횟수 증가
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030902].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume up to 3 [Vibration] on target, and gain the same amount of [Vibration] Count on self
   PL:
643. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
644. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Clash Power +1</style>
   PL:
645. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL:
646. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 이 스킬의 코인 효과로 대상의 [Vibration]을 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Skill's Coin effects consumed [Vibration] on target, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
647. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n[WhenUse] 대상의 [Vibration] <style="highlight">6 당 합 위력 +1 (최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n[WhenUse] <style="highlight">Clash Power +1 for every 6 [Vibration] on target (max 2)</style>
   PL:
648. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]을 최대 3 소모\n(소모한 [Vibration]<style="highlight">x2</style>)만큼 자신의 [Vibration] 횟수 증가\n<style="highlight">다음 턴에 (소모한 [Vibration]-1)만큼 [Binding] 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume up to 3 [Vibration] on target, and gain <style="highlight">double the amount consumed</style> as [Vibration] Count on self\n<style="highlight">Inflict ([Vibration] consumed - 1) [Binding] next turn</style>
   PL:
649. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL:
650. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 이 스킬의 코인 효과로 대상의 [Vibration]을 소모했다면 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If this Skill's Coin effects consumed [Vibration] on target, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
651. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 거기 멈추도록!
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].name ; dataList[id=1030903].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: I Command Thee, Halt!
   PL:
652. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수를 10 소모하여 코인 위력 +2
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 6+ [Vibration], Clash Power +1\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL:
653. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 643 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 10 이상이면, 대상의 [Vibration]을 10 소모하여 [TimeSuspend] 2 부여\n- 자신이 [TimeRentalTwoPersonality] 상태면, 대상의 [Vibration]을 소모하지 않음
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration], [TimeSuspend], [TimeRentalTwoPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [TimeSuspend] = 시간 유예 / Time Moratorium; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time
   EN: [OnSucceedAttack] If target has 10+ [Vibration], consume 10 [Vibration] on target and inflict 2 [TimeSuspend]\n- If this unit is in a [TimeRentalTwoPersonality] state, this effect does not consume the target's [Vibration]
   PL:
655. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 속도가 자신보다 낮다면, [VibrationChainPersonality]로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationChainPersonality], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] If target's Speed is slower than this unit's, trigger [Switch_Vibration] into [VibrationChainPersonality]
   PL:
656. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] <style="highlight">6 당 합 위력 +1 (최대 2)</style>\n<style="highlight">[WhenUse] 대상이 [Binding] 상태면, 합 위력 +1</style>\n[WhenUse] 자신의 [Vibration] 횟수를 10 소모하여 코인 위력 +2
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [WhenUse] <style="highlight">Clash Power +1 for every 6 [Vibration] on target (max 2)</style>\n<style="highlight">[WhenUse] If target has [Binding], gain Clash Power +1</style>\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL:
657. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 3 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 3 [Vibration]</style>
   PL:
658. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 10 이상이면, 대상의 [Vibration]을 10 소모하여 [TimeSuspend] 2 부여\n- 자신이 [TimeRentalTwoPersonality] 상태면, 대상의 [Vibration]을 소모하지 않음<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [TimeSuspend], [TimeRentalTwoPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [TimeSuspend] = 시간 유예 / Time Moratorium; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time
   EN: [OnSucceedAttack] If target has 10+ [Vibration], consume 10 [Vibration] on target and inflict 2 [TimeSuspend]\n- If this unit is in a [TimeRentalTwoPersonality] state, this effect does not consume the target's [Vibration]<style="highlight"></style>
   PL:
659. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
660. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 대상의 속도가 자신보다 낮다면, [VibrationChainPersonality]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationChainPersonality], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] If target's Speed is slower than this unit's, trigger [Switch_Vibration] into [VibrationChainPersonality]<style="highlight"></style>
   PL:
661. [Obrona (ulepszenia 1,4) — nazwa] 시간을 끌어와보도록 하지
   źródło: Skills_personality-03.json :: dataList[id=1030904].levelList[level=1].name ; dataList[id=1030904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: I Shall Summon the Time
   PL:
662. [Obrona (ulepszenie 1) — opis] [StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 4 얻음 (턴 당 1회)\n[WhenUse] 이번 턴 동안 적에게 피격 시, 다음 턴에 대상에게 [Vibration] 2 부여 (턴 당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1030904].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [TimeRentalTwoPersonality], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 4 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WhenUse] For this turn: when hit by an enemy, inflict 2 [Vibration] on target next turn (2 times per turn)
   PL:
663. [Obrona (ulepszenie 4) — opis] [StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 4 얻음 (턴 당 1회)\n[WhenUse] 이번 턴 동안 적에게 피격 시, 다음 턴에 대상에게 [Vibration] <style="highlight">3</style> 부여 (턴 당 <style="highlight">6</style>회)
   źródło: Skills_personality-03.json :: dataList[id=1030904].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [TimeRentalTwoPersonality], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 4 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WhenUse] For this turn: when hit by an enemy, inflict <style="highlight">3</style> [Vibration] on target next turn (<style="highlight">6 times</style> per turn)
   PL:
664. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 황금 시간 - 받아내기
   źródło: Passives.json :: dataList[id=1030901].name
   limit: do 40 znaków
   EN: Golden Time - Extracting
   PL:
665. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 턴 종료 시 체력이 10% ~ 20% 사이로 남았을 때, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투 당 1회)\n\n[TimeRentalTwoPersonality]가 해제될 경우, 다음 턴에 보유 중인 스킬 슬롯 중 하나의 [Aggro] 8 증가
   źródło: Passives.json :: dataList[id=1030901].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [TimeRentalTwoPersonality], [Aggro]
   znaczenie tagów: [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [Aggro] = 도발치 / Aggro
   EN: Turn End: If this unit's HP is between 10% ~ 20%, instantly heal 80% of this unit's max HP, and recover from Stagger. (once per Encounter)\n\nWhen this unit loses [TimeRentalTwoPersonality], gain +8 [Aggro] to one of this unit's Skill Slots next turn
   PL:
666. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] T사식 물리왜곡장
   źródło: Passives.json :: dataList[id=1030921].name
   limit: do 50 znaków
   EN: T Corp. Physics Distortion Field
   PL:
667. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 속도가 가장 느린 아군 1명이 [Vibration]이 부여된 적에게 피해를 받을 때, 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1030921].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When 1 ally with the slowest Speed takes damage from enemies that have [Vibration], take -10% damage
   PL:
668. [Kwestia głosowa [get_10309_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=get_10309_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Kwestia głosowa [get_10309_1] (Identity Acquisition)] 아~ 실례하겠네. 본인은 T사 3등급 직원으로 시간 징수를 맡고 있는 몸일세. 왜 왔는지는, 알고 있겠지?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=get_10309_1].dlg
   limit: do 210 znaków
   EN: Ahem~ Pray, pardon mine intrusion! I am a T Corp. Class 3 Employee of the Time Collections Agency! Thou must already be aware of our reason for visit, indeed?
   PL:
670. [Kwestia głosowa [lobby_morning_10309_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=lobby_morning_10309_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Kwestia głosowa [lobby_morning_10309_1] (Morning Greeting)] 좋은 아침일세. 아, 그대는 벌써 점심일지도 모르겠군. 느긋하게 아침을 즐기지 못한다는 건 다소 슬픈 일이지… 이해하네.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=lobby_morning_10309_1].dlg
   limit: do 210 znaków
   EN: Good morrow. Ah, mayhap 'tis already time to prepare for a luncheon for thee? It grieveth me to see a slow, unhurried breakfast denied... I understand thy pain.
   PL:
672. [Kwestia głosowa [lobby_noon_10309_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=lobby_noon_10309_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Kwestia głosowa [lobby_noon_10309_1] (Afternoon Greeting)] T사의 주요 복지 중 가장 좋다고 여기는 것은! 바로 점심시간 동안 주어지는 TT4 프로토콜이 적용된 수면캡슐일세!\n후후… T사 표준 시간의 30분 밖에 지나지 않았지만, 6시간은 느긋하게 잘 수 있게 만들어주지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=lobby_noon_10309_1].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The best of the already wonderful list of employee benefits here at T Corp is, verily, the TT4 Protocol-activated sleeping pod!\nHeh heh... The device permits me to enjoy a lengthy six-hour slumber over lunch, though only thirty minutes may have passed in the T Corp. Daily Standard Time!
   PL:
674. [Kwestia głosowa [lobby_night_10309_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=lobby_night_10309_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Kwestia głosowa [lobby_night_10309_1] (Evening Greeting)] 음… 밤이 다가오는군. 퇴근 전에 이런 느릿하고 꾸릿꾸릿한 일몰을 지켜보는 것도 제법 운치있지 않은가?\n퇴근을 하고 나면 순식간에 새까매지는 건 조금 슬픈 일이지만…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=lobby_night_10309_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, thus approacheth the night. 'Tis quite mesmerizing, is it not? To watch as the beige sun creeps ever-closer to the horizon ere we depart from work...\nThough I admit 'tis a shame that, once we clock out of work, the beauty soon gives way to utter darkness.
   PL:
676. [Kwestia głosowa [smalltalk_10309_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Kwestia głosowa [smalltalk_10309_1] (Chatter #1)] 시간세를 체납하는 사람은 의외로 꽤 많네. 허가되지 않은 방식으로 시간을 얻어서 쓰다가 적발된다던가 하는 사례는 흔할 정도고.\n물론, 우리 징수직 담당자들이 붙으면 이자까지 전부 되돌려받으니 걱정은 없네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are many who fail to pay their dues in Time Tax, not to mention those who are caught 'finding' time in unauthorized manners.\nForsooth, we Collectors make sure to retrieve every debt that we are owed, with interest, so there is naught for thee to worry!
   PL:
678. [Kwestia głosowa [smalltalk_10309_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Kwestia głosowa [smalltalk_10309_2] (Chatter #2)] 이 시계는 T사에 입사하게 되면 지급받는 것일세! 신분증명용으로도 대체할 수 있지.\n하지만 무엇보다 중요한 건! 이 뒤에 보이는 조그마한 태엽을 감으면…! 업무용 시간을 제공받는다는 것이지!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_2].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. Employment also ensures that thou shalt be bestowed with this watch-and-identification!\nPay heed to this little clockwork knob! Once I rotate this... I shall be bestowed with extra time to complete my missions!
   PL:
680. [Kwestia głosowa [smalltalk_10309_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Kwestia głosowa [smalltalk_10309_3] (Chatter #3)] 둥지에서, 그것도 날개의 직장인으로서 살아간다는 건 영광스럽고 행복한 일이지! 도시가 올바른 시간의 흐름을 가질 수 있게 조력할 수 있다니, 날개의 깃털로서도 최고의 보람이 아니겠는가!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_3].dlg
   limit: do 270 znaków
   EN: To be allowed residence within a Nest, as a feather of a Wing no less, is quite the glory! I cannot rightly ask for any other work as honorable as assisting a Wing to ensure the just flow of time in the City!
   PL:
682. [Kwestia głosowa [smalltalk_10309_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Kwestia głosowa [smalltalk_10309_4] (Post-Uptie Chat 1)] 시간이라는 건 끈적한 유체와도 같지. 시간을 징수할 때마다 쭉쭉 빨려들어오는 것을 보면, 특히 그렇게 느껴지네.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_4].dlg
   limit: do 210 znaków
   EN: The nature of 'time' is like a body of viscous fluid, indeed. 'Twas my impression upon collecting time; it very much resembled a stream or fluid as I drew it!
   PL:
684. [Kwestia głosowa [smalltalk_10309_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Kwestia głosowa [smalltalk_10309_5] (Post-Uptie Chat 2)] 아… 이 기계태엽들 말인가. 현장업무를 수행할 때 입는 외골격이네. 성공적인 시간의 회수를 하려면, 징수직의 안전도 보장되어야 하지 않겠나?
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=smalltalk_10309_5].dlg
   limit: do 270 znaków
   EN: Ah, thou wouldst like to know more of the clockwork machines I wear? 'Tis mine armor, an 'exoskeleton' for field missions. The safety of a collector must be guaranteed for a successful retrieval of time, no?
   PL:
686. [Kwestia głosowa [neglect_10309_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=neglect_10309_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Kwestia głosowa [neglect_10309_1] (Idle)] 아~ 신경쓰지 말게나! 그대가 본인을 방치하더라도, 본인 정도 되는 직원에게는 그리 길지 않은 시간일 뿐이니. 일 보게나!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=neglect_10309_1].dlg
   limit: do 220 znaków
   EN: Ah~ worry not thyself to keep me entertained! 'Tis only a brief moment for an employee of my Class. Go do whatever business it is that thou must see to, mind me not!
   PL:
688. [Kwestia głosowa [gacksung_10309_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=gacksung_10309_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Kwestia głosowa [gacksung_10309_1] (Uptying)] 시간 징수 집행. 혹시나 그대의 시간이 잘못 빨려들어갈 수 있으니, 거리에 주의하게나.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=gacksung_10309_1].dlg
   limit: do 120 znaków
   EN: Commencing Time Collections. Watch thy distance, lest thine own time be siphoned.
   PL:
690. [Kwestia głosowa [formation_10309_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=formation_10309_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Kwestia głosowa [formation_10309_1] (Deployment)] 시간체납자인가! 시계 챙기고 징수곡괭이 챙기고!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=formation_10309_1].dlg
   limit: do 120 znaków
   EN: A time defaulter, is it?! Get thine watches and collection pickaxes!
   PL:
692. [Kwestia głosowa [battleentry_10309_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battleentry_10309_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Kwestia głosowa [battleentry_10309_1] (Stage Entry)] 징수하겠네.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battleentry_10309_1].dlg
   limit: do 120 znaków
   EN: Commencing Collections, now.
   PL:
694. [Kwestia głosowa [battle_select_10309_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_select_10309_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Kwestia głosowa [battle_select_10309_1] (Viewed in Battle)] 천천히 말하시게나! 시간은 많네… 라고 하기에는 조금 그렇고 어느 정도 있네.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_select_10309_1].dlg
   limit: do 140 znaków
   EN: No need to be hasty in thy speech! For I have all the ti— for I have a moderate sum of time in the world.
   PL:
696. [Kwestia głosowa [battle_endcommand_10309_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_endcommand_10309_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Kwestia głosowa [battle_endcommand_10309_1] (Commencing Attack)] 해보겠네!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_endcommand_10309_1].dlg
   limit: do 120 znaków
   EN: It shall be done!
   PL:
698. [Kwestia głosowa [battle_enemy_break_10309_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_enemy_break_10309_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Kwestia głosowa [battle_enemy_break_10309_1] (Enemy Stagger)] 아직 징수할 내역이 남았으니 죽지는 마시게!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_enemy_break_10309_1].dlg
   limit: do 120 znaków
   EN: There is aught else to collect from thee! Breathe not thy final breath!
   PL:
700. [Kwestia głosowa [battle_break_10309_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_break_10309_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Kwestia głosowa [battle_break_10309_1] (Staggered)] 읏…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_break_10309_1].dlg
   limit: do 120 znaków
   EN: Agh...!
   PL:
702. [Kwestia głosowa [battle_kill_10309_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_kill_10309_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Kwestia głosowa [battle_kill_10309_1] (Enemy Killed)] 이런… 대상 사망. 징수 진행 불가.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_kill_10309_1].dlg
   limit: do 120 znaków
   EN: Fie... target deceased. Collection status: inaccessible.
   PL:
704. [Kwestia głosowa [battle_dead_10309_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_dead_10309_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Kwestia głosowa [battle_dead_10309_1] (Death)] 아직 회수해야 할 시간이 많이 남았거늘…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_dead_10309_1].dlg
   limit: do 120 znaków
   EN: There is yet much time that must be collected...
   PL:
706. [Kwestia głosowa [choice_success_p_10309_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=choice_success_p_10309_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Kwestia głosowa [choice_success_p_10309_2] (Check Passed)] 이번 업무도 여유있게 해냈지!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=choice_success_p_10309_2].dlg
   limit: do 120 znaków
   EN: Another quest, handily completed!
   PL:
708. [Kwestia głosowa [choice_fail_n_10309_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=choice_fail_n_10309_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Kwestia głosowa [choice_fail_n_10309_1] (Check Failed)] 으으, 시간을 잘못 써버렸네…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=choice_fail_n_10309_1].dlg
   limit: do 120 znaków
   EN: Aah... 'twas not the wisest use of my time...
   PL:
710. [Kwestia głosowa [battle_clear_10309_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_clear_10309_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Kwestia głosowa [battle_clear_10309_1] (Victory Cry)] 평범한 징수절차였을 뿐이네! 빠짐없이 시간을 회수했으니, 이제 돌아가보지.
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_clear_10309_1].dlg
   limit: do 120 znaków
   EN: Mm, 'twas naught exceptional. Now that the necessary time has been collected, let us return.
   PL:
712. [Kwestia głosowa [battle_clear_ex_10309_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_clear_ex_10309_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Kwestia głosowa [battle_clear_ex_10309_1] (Extra Conditions Fulfilled)] 이런, 회수해야 할 시간 보다 많이 징수해버렸네… 흠, 하지만 체납자가 생명을 다했으니, 남은 시간을 T사 시간 금고로 환수하는게 옳은 일이라는 생각도 드는군!
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_clear_ex_10309_1].dlg
   limit: do 280 znaków
   EN: Fie, I have collected more time than we were owed... Hm, yet... now that the defaulter has unfortunately perished, perchance it would be most just to return all of their remaining time to the T Corp. Time Vault, indeed!
   PL:
714. [Kwestia głosowa [battle_defeat_10309_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_defeat_10309_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Kwestia głosowa [battle_defeat_10309_1] (Defeat Wail)] 시간 회수율이 기준치 이하라니… 나는 시간을 잘못 썼고, 실패한 몸이 되었군…
   źródło: PersonalityVoiceDlg/Voice_Donquixote_Tcorp_10309.json :: dataList[id=battle_defeat_10309_1].dlg
   limit: do 180 znaków
   EN: My time collections rate is beneath the baseline...? Ah, thus I am become failure, a fool who knows not how to make the best of her time...
   PL:

## [000] The Manager of La Manchaland — Don Quixote — 라만차랜드 실장
- ID Tożsamości: `10310` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 63 · szybkość: 4–6 / 4–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed

716. [Karta Tożsamości — tytuł] 라만차랜드\n실장
   źródło: Personalities.json :: dataList[id=10310].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Manager\nof La Manchaland
   PL:
717. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10310].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10310].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Karta Tożsamości — opis] 돈키호테의 열번째 인격
   źródło: Personalities.json :: dataList[id=10310].desc
   limit: do 120 znaków
   EN: Don Quixote’s 10th Identity
   PL:
720. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 참는 것은 끝이다
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=1].name ; dataList[id=1031001].levelList[level=2].name ; dataList[id=1031001].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Enough is Enough
   PL:
721. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 5 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 5 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]
   PL:
722. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
723. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 5 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면 코인 위력 +1</style>
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=2].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 5 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL:
724. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
725. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 5 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 5 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>
   PL:
726. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 원하는대로 펼쳐라
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].name ; dataList[id=1031002].levelList[level=2].name ; dataList[id=1031002].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Let All Blossom Free
   PL:
728. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[BeforeAttack] [BloodArmorPersonalityFirst] 10 이상이면, 공격 가중치 +1
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[BeforeAttack] At 10+ [BloodArmorPersonalityFirst], Atk Weight +1
   PL:
729. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] 대상의 [Laceration]당 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +2.5% damage for every [Laceration] on target (max 25%)
   PL:
731. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] 자신의 [BloodDinner_Accumulation] 100당 피해량 +5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Deal +5% damage for every 100 [BloodDinner_Accumulation] by self (max 25%)
   PL:
732. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1</style>\n[BeforeAttack] [BloodArmorPersonalityFirst] <style="highlight">10 당</style> 공격 가중치 1 증가 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=2].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[BeforeAttack] <style="highlight">Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] on self (max 2)</style>
   PL:
733. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] 자신의 [BloodDinner_Accumulation] 100당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Deal +<style="highlight">10</style>% damage for every 100 [BloodDinner_Accumulation] by self (max <style="highlight">50</style>%)
   PL:
734. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n[BeforeAttack] [BloodArmorPersonalityFirst] 10 당 공격 가중치 1 증가 (최대 2)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[BeforeAttack] Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] on self (max 2)
   PL:
735. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] 자신의 [BloodDinner_Accumulation] 100당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">75</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Deal +<style="highlight">15</style>% damage for every 100 [BloodDinner_Accumulation] by self (max <style="highlight">75</style>%)
   PL:
736. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 꿰뚫겠습니다
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=3].name ; dataList[id=1031003].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: I Shall Impale
   PL:
737. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 10 이상이면, 코인 위력 +1\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n자신의 [BloodDinner_Accumulation] 100 당 피해량 +10% (최대 50%)\n[EndSkill] 대상이 사망한 경우 [BloodDinner] 30 증가. [BloodArmorPersonalityFirst] 10 얻음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=3].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner], [BloodDinner_Accumulation], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 10)\n[WhenUse] Clash Power +1 for every 10 [BloodArmorPersonalityFirst] (max 2)\n[WhenUse] If target has 10+ [Laceration], Coin Power +1\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] consumed\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\nDeal +5% damage for every [Laceration] on target (max 50%)\nDeal +10% damage for every 100 [BloodDinner_Accumulation] by self (max 50%)\n[EndSkill] If target is defeated, increase [BloodDinner] by 30; gain 10 [BloodArmorPersonalityFirst] (once per turn)
   PL:
738. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
739. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] <style="highlight">5 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n자신의 [BloodDinner_Accumulation] 100 당 피해량 +<style="highlight">20</style>% (최대 <style="highlight">100</style>%)\n[EndSkill] 대상이 사망한 경우 [BloodDinner] <style="highlight">60</style> 증가. [BloodArmorPersonalityFirst] 10 얻음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=4].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner], [BloodDinner_Accumulation], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 10)\n[WhenUse] Clash Power +1 for every 10 [BloodArmorPersonalityFirst] (max 2)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Laceration] on target (max 2)</style>\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] consumed\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\nDeal +5% damage for every [Laceration] on target (max 50%)\nDeal +<style="highlight">20</style>% damage for every 100 [BloodDinner_Accumulation] by self (max <style="highlight">100</style>%)\n[EndSkill] If target is defeated, increase [BloodDinner] by <style="highlight">60</style>; gain 10 [BloodArmorPersonalityFirst] (once per turn)
   PL:
740. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 아류 산초 경혈 6식 - 채찍
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].name ; dataList[id=1031005].levelList[level=2].name ; dataList[id=1031005].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 60 znaków
   EN: Variant Sancho Hardblood Arts 6 - Whip
   PL:
741. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] [Laceration] 20 얻음\n[WhenUse] [BloodArmorPersonalityFirst] 10 당 적중시 부여하는 [Laceration] +1 (최대 2). 공격 종료 시 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodArmorPersonalityFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 20)\n[WhenUse] Gain 20 [Laceration]\n[WhenUse] Inflict +1 more [Laceration] On Hit for every 10 [BloodArmorPersonalityFirst]. (max 2) Attack End: Consume 10 [BloodArmorPersonalityFirst]
   PL:
742. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031005].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031005].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
743. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1031005].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1031005].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1031005].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031005].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1031005].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1031005].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Laceration] 20 얻음\n[WhenUse] [BloodArmorPersonalityFirst] 10 당 적중시 부여하는 [Laceration] +1 (최대 2). 공격 종료 시 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BloodArmorPersonalityFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 20)\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain 20 [Laceration]\n[WhenUse] Inflict +1 more [Laceration] On Hit for every 10 [BloodArmorPersonalityFirst]. (max 2) Attack End: Consume 10 [BloodArmorPersonalityFirst]
   PL:
747. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] [Laceration] 20 얻음\n[WhenUse] [BloodArmorPersonalityFirst] 10당 적중시 부여하는 [Laceration] +1 (최대 2). 공격 종료 시 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BloodArmorPersonalityFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 20)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] Gain 20 [Laceration]\n[WhenUse] Inflict +1 more [Laceration] On Hit for every 10 [BloodArmorPersonalityFirst]. (max 2) Attack End: Consume 10 [BloodArmorPersonalityFirst]
   PL:
748. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Laceration]을 1회 발동 시킴. 대상의 [Laceration] 횟수 1 감소</style>
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Activate [Laceration] on target once (target loses 1 [Laceration] Count)</style>
   PL:
749. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 아류 산초 경혈 8식 - 갈라지도록
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].name ; dataList[id=1031006].levelList[level=2].name ; dataList[id=1031006].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 70 znaków
   EN: Variant Sancho Hardblood Arts 8 - Split Apart
   PL:
750. [Umiejętność 5 (×0) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1\n[BeforeAttack] [BloodArmorPersonalityFirst] 10 이상이면, 공격 가중치 +1\n[EndSkill] 공격 가중치가 증가했다면, [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BeforeAttack], [BloodArmorPersonalityFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[BeforeAttack] At 10+ [BloodArmorPersonalityFirst], Atk Weight +1\n[EndSkill] If this Skill had an increased Atk Weight, consume 10 [BloodArmorPersonalityFirst]
   PL:
751. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031006].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031006].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031006].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031006].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1031006].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031006].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] 대상의 [Laceration]당 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1031006].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1031006].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 730 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 3 — opis] [BloodDinner_Common_Accumulation] 100당 피해량 +5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner_Common_Accumulation]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared)
   EN: Deal +5% damage for every 100 [BloodDinner_Common_Accumulation] (max 25%)
   PL:
756. [Umiejętność 5 (×0) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[BeforeAttack] [BloodArmorPersonalityFirst] <style="highlight">10 당</style> 공격 가중치 증가 <style="highlight">(최대 2)</style>\n[EndSkill] 증가한 가중치당 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BeforeAttack], [BloodArmorPersonalityFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[BeforeAttack] <style="highlight">Gain Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] (max 2)</style>\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every Atk Weight gained
   PL:
757. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 3, efekt 3 — opis] [BloodDinner_Common_Accumulation] 100당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=2].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Common_Accumulation]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared)
   EN: Deal +<style="highlight">10</style>% damage for every 100 [BloodDinner_Common_Accumulation] (max <style="highlight">50</style>%)
   PL:
758. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 대상의 [Laceration] 6 당 코인 위력 +1 (최대 2)\n[BeforeAttack] [BloodArmorPersonalityFirst] 10당 공격 가중치 증가 (최대 2)\n[EndSkill] 증가한 가중치당 [BloodArmorPersonalityFirst] 10 소모<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BeforeAttack], [BloodArmorPersonalityFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)\n[BeforeAttack] Gain Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] (max 2)\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every Atk Weight gained<style="highlight"></style>
   PL:
759. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [BloodDinner_Common_Accumulation] 100당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">75</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Common_Accumulation]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared)
   EN: Deal +<style="highlight">15</style>% damage for every 100 [BloodDinner_Common_Accumulation] (max <style="highlight">75</style>%)
   PL:
760. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 산초류 경혈 오의 - 라 샹그레
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].name ; dataList[id=1031007].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 4 (+5)
   limit: do 60 znaków
   EN: Ascendant Sancho Hardblood Arts - La Sangre
   PL:
761. [Umiejętność 6 (×0) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 10 이상이면, 코인 위력 +1\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n[WhenUse] [BloodDinner_Common_Accumulation] 100당 피해량 +20% (최대 100%)\n[EndSkill] [BloodArmorPersonalityFirst] 10 당, [BloodArmorPersonalityFirst] 10 소모\n[EndSkill] 대상이 사망했으면 [BloodDinner] 50 증가. 이 스킬에서 소모한 [BloodArmorPersonalityFirst]을 절반 돌려 받음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [EndSkill], [BloodDinner]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 20)\n[WhenUse] Base Power +1 for every 10 [BloodArmorPersonalityFirst] on self (max 2)\n[WhenUse] If target has 10+ [Laceration], Coin Power +1\nDeal +5% damage for every [Laceration] on target (max 50%)\n[WhenUse] Deal +20% damage for every 100 [BloodDinner_Common_Accumulation] (max 100%)\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every 10 [BloodArmorPersonalityFirst]\n[EndSkill] If target is defeated, increase [BloodDinner] by 50. Regain half of [BloodArmorPersonalityFirst] consumed by this Skill (once per turn)
   PL:
762. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 4 증가
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +4 [Laceration] Count
   PL:
767. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [EndSkill] 대상이 사망했으면, 모든 적에게 [Laceration] 5 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1031007].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Laceration]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Laceration] = 출혈 / Bleed
   EN: [EndSkill] If target is defeated, inflict 5 [Laceration] and +1 [Laceration] Count against all enemies
   PL:
768. [Umiejętność 6 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당 기본 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 대상의 [Laceration] <style="highlight">5 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n[WhenUse] [BloodDinner_Common_Accumulation] 100당 피해량 +20% (최대 100%)\n[EndSkill] [BloodArmorPersonalityFirst] 10 당, [BloodArmorPersonalityFirst] 10 소모\n[EndSkill] 대상이 사망했으면 [BloodDinner] <style="highlight">100</style> 증가. 이 스킬에서 소모한 [BloodArmorPersonalityFirst]을 절반 돌려 받음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=4].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [EndSkill], [BloodDinner]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 20)\n[WhenUse] Base Power +1 for every 10 [BloodArmorPersonalityFirst] on self (max <style="highlight">3</style>)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Laceration] on target (max 2)</style>\nDeal +5% damage for every [Laceration] on target (max 50%)\n[WhenUse] Deal +20% damage for every 100 [BloodDinner_Common_Accumulation] (max 100%)\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every 10 [BloodArmorPersonalityFirst]\n[EndSkill] If target is defeated, increase [BloodDinner] by <style="highlight">100</style>. Regain half of [BloodArmorPersonalityFirst] consumed by this Skill (once per turn)
   PL:
769. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">8</style> 부여, 출혈 횟수 4 증가
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">8</style> [Laceration] and +4 [Laceration] Count
   PL:
770. [Obrona (ulepszenia 1,4) — nazwa] 웃음소리는 사그라들 것이다
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=1].name ; dataList[id=1031004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Laughters Shall Subside
   PL:
771. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] [BloodDinner]을 최대 50 소모하여 [BloodDinner] 10 당 [BloodArmorPersonalityFirst] 1얻음.\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n[StartBattle] [BloodDinner_Common_Accumulation] 50 당 체력이 가장 적은 아군 1명에게 [SwirlingBloodPersonality] 1 부여 (최대 10, 턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】
   EN: [DuelCounter]\n[StartBattle] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n[StartBattle] To 1 ally with the least HP: apply 1 [SwirlingBloodPersonality] for every 50 [BloodDinner_Common_Accumulation] (max 10, once per turn)
   PL:
772. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031004].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
773. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] [BloodDinner]을 최대 50 소모하여 [BloodDinner] 10 당 [BloodArmorPersonalityFirst] 1얻음.\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n[StartBattle] [BloodDinner_Common_Accumulation] 50 당 체력이 가장 적은 아군 1명에게 [SwirlingBloodPersonality] 1 부여 (최대 <style="highlight">15</style>, 턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】
   EN: [DuelCounter]\n[StartBattle] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n[StartBattle] To 1 ally with the least HP: apply 1 [SwirlingBloodPersonality] for every 50 [BloodDinner_Common_Accumulation] (max <style="highlight">15</style>, once per turn)
   PL:
774. [Obrona (ulepszenia 1,4) — nazwa] 아류 산초 경혈 15식 - 피날레 준비
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].name ; dataList[id=1031008].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 6 · monety: 2 (+5)
   limit: do 70 znaków
   EN: Variant Sancho Hardblood Arts 15 - Buildup to Finale
   PL:
775. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 체력이 가장 적은 아군 (3 + 가장 높은 공명 수 / 2)명에게 [BloodDinner_Common_Accumulation] 40 당 [SwirlingBloodPersonality]를 (1 + [BloodArmorPersonalityFirst]/15)만큼 부여하고, 보유한 [BloodArmorPersonalityFirst] 절반 소모. (아군 1명당 최대 1회 부여, 소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality], [BloodArmorPersonalityFirst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: [DuelCounter]\n[StartBattle] To (3 + (highest Reson. / 2)) allies with the least HP: apply (1 + ([BloodArmorPersonalityFirst] / 15)) [SwirlingBloodPersonality] for every 40 [BloodDinner_Common_Accumulation], then consume half of [BloodArmorPersonalityFirst] on self. (once per ally; rounded down)
   PL:
776. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031008].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Obrona (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1031008].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
778. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 체력이 가장 적은 아군 (3 + 가장 높은 공명 수 / 2)명에게 [BloodDinner_Common_Accumulation] 40 당 [SwirlingBloodPersonality]를 (1 + [BloodArmorPersonalityFirst]/<style="highlight">10</style>)만큼 부여하고, 보유한 [BloodArmorPersonalityFirst] 절반 소모. (아군 1명당 최대 1회 부여, 소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality], [BloodArmorPersonalityFirst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: [DuelCounter]\n[StartBattle] To (3 + (highest Reson. / 2)) allies with the least HP: apply (1 + ([BloodArmorPersonalityFirst] / <style="highlight">10</style>)) [SwirlingBloodPersonality] for every 40 [BloodDinner_Common_Accumulation], then consume half of [BloodArmorPersonalityFirst] on self. (once per ally; rounded down)
   PL:
779. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈찬
   źródło: Passives.json :: dataList[id=1031001].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL:
780. [Pasywka bojowa (od ulepszenia 1) — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 크게 드러난다.\n\n[BloodDinner]을 소모할 때, <라만차랜드[TabExplain]> 소속 중에서 자신과 같은 권속이 있으면, 자신이 먼저 [BloodDinner]을 소모함.\n\n'아류 산초 경혈[TabExplain] 6식 - 채찍'를 사용하는 동안 출혈 피해로 체력이 1 미만이 되지 않음.
   źródło: Passives.json :: dataList[id=1031001].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [TabExplain]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase Bloodfeast value by the amount of [Laceration] damage collectively received by every unit.\nWhen this unit enters the field, the sleeping blood drenching the battlefield will fill the surface.\n\nWhen consuming [BloodDinner], if there are <La Manchaland[TabExplain]> Kindreds of the same generation as this unit, this unit takes precedence.\n\nWhen using 'Variant Sancho Hardblood[TabExplain] Arts 6 - Whip', HP cannot drop below 1 due to Bleed damage.
   PL:
781. [Pasywka bojowa (od ulepszenia 1) — nazwa] 아류 산초 경혈식
   źródło: Passives.json :: dataList[id=1031002].name
   limit: do 50 znaków
   EN: Variant Sancho Hardblood Arts
   PL:
782. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시, [BloodArmorPersonalityFirst] 15 이상이고 다음의 인격이 전투에 참가 중이거나 사망했으면, 자신의 가장 왼쪽 슬롯의 스킬이 강화됨.\n- 라만차랜드[TabExplain] 신부 그레고르: 스킬 1 강화\n- 라만차랜드[TabExplain] 이발사 오티스: 스킬 2 강화\n- 자신: 스킬 3 강화\n- 라만차랜드[TabExplain] 공주 로쟈: 수비 스킬[TabExplain] 강화\n\n자신을 제외한 아군이 출혈 피해를 받거나 [BloodDinner]을 소모할 때, [BloodArmorPersonalityFirst] 2 얻음 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1031002].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [BloodArmorPersonalityFirst], [TabExplain], [BloodDinner], [Laceration]
   znaczenie tagów: [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: Turn Start: At 15+ [BloodArmorPersonalityFirst], if each following unit is either defeated or participating in the Encounter, empower this unit's leftmost Slot.\nThe Priest of La Manchaland[TabExplain] Gregor: Empower Skill 1\nThe Barber of La Manchaland[TabExplain] Outis: Empower Skill 2\nThis Unit: Empower Skill 3\nThe Princess of La Manchaland[TabExplain] Rodion: Empower Defense Skill[TabExplain]\n\nWhen other units among allies take [Laceration] damage or consume [BloodDinner], gain 2 [BloodArmorPersonalityFirst] on self (3 times per turn)
   PL:
783. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈족을 책임지게 된 자
   źródło: Passives.json :: dataList[id=1031003].name
   limit: do 40 znaków
   EN: Bearer of the Blood Kin
   PL:
784. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 동안 자신을 제외한 아군 중 <라만차랜드[TabExplain]> 소속이 사망한 경우\n- 자신의 기본 공격 스킬로 [BloodArmorPersonalityFirst]을 얻을 때, [BloodArmorPersonalityFirst]을 1 추가로 얻음\n- 자신을 제외한 아군 중 <라만차랜드[TabExplain]> 소속이 3명 이상 사망한 경우, 대신 [BloodArmorPersonalityFirst] 3을 추가로 얻고 턴 시작 시, [SadLamanchaland] 1 얻음
   źródło: Passives.json :: dataList[id=1031003].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [BloodArmorPersonalityFirst], [SadLamanchaland]
   znaczenie tagów: [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [SadLamanchaland] = 책임감 / Responsibility
   EN: In an Encounter, if another allied <La Manchaland[TabExplain]> unit is defeated:\n- Gain 1 more [BloodArmorPersonalityFirst] when gaining [BloodArmorPersonalityFirst] from this unit's Base Attack Skills\n- When 3+ other allied <La Manchaland[TabExplain]> units are defeated: gain 3 additional [BloodArmorPersonalityFirst]; at Turn Start, gain 1 [SadLamanchaland]
   PL:
785. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 혈갑
   źródło: Passives.json :: dataList[id=1031004].name
   limit: do 40 znaków
   EN: Armadura de Sangre
   PL:
786. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 자신의 공격 종료 시 적이 사망했다면, 대상의 최대 체력 10%만큼 [BloodDinner] 생성 (턴 당 최대 100, 집중 전투인 경우 부위로 판정)\n턴 종료 시 잃은 체력 15%당 다음 턴에 [AttackDmgUp] 1 얻음. (최대 3)\n전투 중 아군이 출혈 피해로 사망하려 할 때, 해당 턴동안 출혈 피해로는 사망하지 않음. (전투 당 인격 1명당 1회 발동)
   źródło: Passives.json :: dataList[id=1031004].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [AttackDmgUp], [Laceration]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [AttackDmgUp] = 피해량 증가 / Damage Up; [Laceration] = 출혈 / Bleed
   EN: Attack End: If the enemy is defeated, increase [BloodDinner] by 10% of the target's max HP (100 per turn; for Focused Encounters, if the Part is broken)\nGain 1 [AttackDmgUp] next turn for every 15% missing HP at Turn End (max 3)\nIf an ally is about to be defeated from [Laceration] damage, prevent them from being defeated from Bleed damage for the turn (once per Encounter for each Identity)
   PL:
787. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] ‘가족들이여 억눌러온 허기를 채워라’
   źródło: Passives.json :: dataList[id=1031021].name
   limit: do 60 znaków
   EN: ‘Feed your repressed hunger, my Family’
   PL:
788. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 전투 시작 시 체력이 가장 적은 아군이 잃은 체력 20%당 [AttackDmgUp] 1 얻음. (최대 3)\n- 대상 아군이 <혈귀>면, 효과를 대신하여 잃은 체력 15%당 [AttackDmgUp] 1 얻음. (최대 3)
   źródło: Passives.json :: dataList[id=1031021].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Combat Start: 1 ally with the least HP gains 1 [AttackDmgUp] for every 20% missing HP (max 3)\n- If the said ally is a <Bloodfiend>, gain 1 [AttackDmgUp] for every 15% missing HP instead (max 3)
   PL:
789. [Kwestia głosowa [get_10310_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=get_10310_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Kwestia głosowa [get_10310_1] (Identity Acquisition)] 가족의 관리는 차질이 없을 겁니다. …당신이 내팽개친 것을 돌보는 것이 저의 몫이었을테니.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=get_10310_1].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Family will be well-cared for.\n... After all, the onus always fell on me to provide for what you abandoned.
   PL:
791. [Kwestia głosowa [lobby_morning_10310_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=lobby_morning_10310_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Kwestia głosowa [lobby_morning_10310_1] (Morning Greeting)] 해가… 뜨는군. 곧 인간들이 잔뜩 찾아오겠지. 아무것도 모르는 얼굴로 웃으면서.\n가족들은 웃음거리가 되어 타들어가는 갈증에 목을 움켜쥐는데…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=lobby_morning_10310_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The sun rises... Humans will be arriving soon. Abound with smiles and laughter, their ignorance buried in happiness.\nAll the while the Family is reduced to laughingstocks and forced to endure this burning thirst, clutching their parched throats...
   PL:
793. [Kwestia głosowa [lobby_noon_10310_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=lobby_noon_10310_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Kwestia głosowa [lobby_noon_10310_1] (Afternoon Greeting)] 성문을 걸어 잠가보아야 또 부서져라 문을 두드리겠지. 그러면 어버이는 눈을 반짝이시며 어서 그 기사를 들이라 할 거고.\n후우… 매일 이 시간만 되면 머리부터 아파오는군.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=lobby_noon_10310_1].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't suppose locking the castle gates will do aught to deter the Knight from relentlessly knocking upon them. Father will command us to let the Knight in, with that familiar twinkle in his eyes, and...\nHaah... this hour alone has become a cause for headaches.
   PL:
795. [Kwestia głosowa [lobby_night_10310_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=lobby_night_10310_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Kwestia głosowa [lobby_night_10310_1] (Evening Greeting)] 꺼질 줄 모르는 고해소의 불빛. 재단실의 미싱소리. 퍼레이드 연습실의 땅울림.\n더는 두고 볼 수 없어. 굶주린 가족들이… 어버이의 꿈에 갇혀사는 건.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=lobby_night_10310_1].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The ever-lit lights of the confessional, the ceaseless sounds of the sewing machine from the tailor's room, the tired footsteps echoing from the Parade training hall... \nI can no longer abide by this charade as the family starves, suffering and gaoled in Father's dream.
   PL:
797. [Kwestia głosowa [smalltalk_10310_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Kwestia głosowa [smalltalk_10310_1] (Chatter #1)] 어버이께서는… 누구보다 강한 힘과 강인한 정신력을 지니셨어. …그렇기에 우리를 절대 이해하실 수 없는 거다. 우리가 얼마나 피에 절실한지. 우리가 어떻게 죽어가고 있는지.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_1].dlg
   limit: do 290 znaków
   EN: Father's strength and will are greater than those of anyone. ... That is precisely why he shall never discern the fathoms of our suffering and our yearning for blood. He will never understand how death encroaches upon us.
   PL:
799. [Kwestia głosowa [smalltalk_10310_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Kwestia głosowa [smalltalk_10310_2] (Chatter #2)] 권속을 만들지 않은 이유… 처음에는 혼자가 편해서. 그 다음에는 책임질 것이 늘어나는 게 싫어서.\n그리고 지금은… 헛된 꿈에 취한 어버이 대신, 내 동생의 자식들을 지키는 것만으로도 벅차니까.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_2].dlg
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I did not sire my own Kindreds because... I enjoyed solitude, at first. Then, my reasoning became that I did not wish for my responsibility to be expanded beyond what there was.\nAnd now... because I already have my hands full protecting my little sister's Children while Father has absconded from his responsibilities in favor of a futile dream.
   PL:
801. [Kwestia głosowa [smalltalk_10310_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Kwestia głosowa [smalltalk_10310_3] (Chatter #3)] 정의로운 해결사? 그런 건 없어. 하얀 달의 기사가 말했던 용기도, 자비도, 겸손도… 인간의 기준에 치우친 발상일 뿐.\n그들이 우리와 같은 갈망을 가졌다면, 그런 정의로움을 논할 수 있었을까?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_3].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'The righteous Fixer of justice'? It is only an illusion. Courage, clemency, and humility that the Knight of the White Moon preached of are all but concepts conjured from a human mind.\nLet us see if humans can continue to insist on such 'righteousness' were they plagued by the same yearning that ails us.
   PL:
803. [Kwestia głosowa [smalltalk_10310_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Kwestia głosowa [smalltalk_10310_4] (Post-Uptie Chat 1)] 결국 당신이 꾸었던 공존이라는 허울 좋은 꿈은… 가족을 울타리 밖으로 내팽개친 무책임한 어버이로 끝을 맺는군요.\n왜 우리의 고통은 안중에도 없었던 겁니까, 왜 우리는 항상 희생을 강요당해야만 했던 겁니까!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_4].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the end of the road paved by your gilded dream of coexistence lies the ruin of an irresponsible Father who's cast his Children from the sanctuary of their home.\nWhere was your concern for our suffering? Why—why was the burden of sacrifice always ours?!
   PL:
805. [Kwestia głosowa [smalltalk_10310_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Kwestia głosowa [smalltalk_10310_5] (Post-Uptie Chat 2)] 공존이 끝났으니, 만찬을 즐길 때가 왔다. 인간을 죽여 피로 온몸을 적시고, 억눌렸던 감정을 따라라.\n그리고… 심장에 박힌 말뚝과 짓눌린 혈향 앞에 돌아와 목놓아 외치는 거다. 앞으로 우리는, 혈귀답게 살겠노라고.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=smalltalk_10310_5].dlg
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coexistence is no more; let the hour of the banquet commence. Slaughter them, kill every human you see. Bathe in their blood and break the levees of your repressed emotions.\nWe shall then return to the stake that has impaled the heart, mantled in this stench of blood... and declare with our voices bridled no more. That we shall, henceforth, live as Bloodfiends should.
   PL:
807. [Kwestia głosowa [neglect_10310_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=neglect_10310_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Kwestia głosowa [neglect_10310_1] (Idle)] …좋은 생각이 났더라도, 입 밖으로 꺼내지 마. 허황된 생각을 들어주는 건 이제 지긋지긋하니까.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=neglect_10310_1].dlg
   limit: do 190 znaków
   EN: ... Hold your tongue; I will no longer tolerate any more ingenious ideas. I've wasted enough time entertaining those cloud-chasing ruminations.
   PL:
809. [Kwestia głosowa [gacksung_10310_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=gacksung_10310_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Kwestia głosowa [gacksung_10310_1] (Uptying)] 그 허황되고 유치한 꿈은 즐거우셨습니까. 이제 깨어날 시간입니다. 당신이 외면하고 떠넘겼던 모든 책임을 다하기 위해서.\n…원망하십시오, 어버이시여. 우리 역시 당신을 원망할 테니.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=gacksung_10310_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Was it sweet, your hollow, juvenile dream? It is about time you awakened from it. Take responsibility for those you had once abandoned in the hands of others.\nResent us, O Father. For we shall resent you in return.
   PL:
811. [Kwestia głosowa [formation_10310_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=formation_10310_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Kwestia głosowa [formation_10310_1] (Deployment)] 책임은 모두 내가 진다.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=formation_10310_1].dlg
   limit: do 120 znaków
   EN: I shall bear the responsibility for everything.
   PL:
813. [Kwestia głosowa [battleentry_10310_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battleentry_10310_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Kwestia głosowa [battleentry_10310_1] (Stage Entry)] 라만차랜드를 뒤엎는다.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battleentry_10310_1].dlg
   limit: do 120 znaków
   EN: Rebellion comes to La Manchaland.
   PL:
815. [Kwestia głosowa [battle_select_10310_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_select_10310_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Kwestia głosowa [battle_select_10310_1] (Viewed in Battle)] 나는… 어떤 말도 할 수 없어.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_select_10310_1].dlg
   limit: do 120 znaków
   EN: I... cannot speak a word.
   PL:
817. [Kwestia głosowa [battle_endcommand_10310_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_endcommand_10310_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Kwestia głosowa [battle_endcommand_10310_1] (Commencing Attack)] 가족을 위해…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_endcommand_10310_1].dlg
   limit: do 120 znaków
   EN: For the Family...
   PL:
819. [Kwestia głosowa [battle_enemy_break_10310_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_enemy_break_10310_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Kwestia głosowa [battle_enemy_break_10310_1] (Enemy Stagger)] 꿰뚫리고…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_enemy_break_10310_1].dlg
   limit: do 120 znaków
   EN: From this impalement...
   PL:
821. [Kwestia głosowa [battle_break_10310_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_break_10310_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Kwestia głosowa [battle_break_10310_1] (Staggered)] 별 것 아닌 상처다.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_break_10310_1].dlg
   limit: do 120 znaków
   EN: This is nothing.
   PL:
823. [Kwestia głosowa [battle_kill_10310_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_kill_10310_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Kwestia głosowa [battle_kill_10310_1] (Enemy Killed)] …쏟아내라.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_kill_10310_1].dlg
   limit: do 120 znaków
   EN: ... shall it cascade.
   PL:
825. [Kwestia głosowa [battle_dead_10310_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_dead_10310_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Kwestia głosowa [battle_dead_10310_1] (Death)] 신부… 네가 말했던 벌이… 이것인가.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_dead_10310_1].dlg
   limit: do 120 znaków
   EN: Is this... 'the retribution' you spoke of, Priest...?
   PL:
827. [Kwestia głosowa [choice_success_p_10310_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=choice_success_p_10310_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Kwestia głosowa [choice_success_p_10310_2] (Check Passed)] 지금은 성공했지만, 앞으로는 어떨지.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=choice_success_p_10310_2].dlg
   limit: do 120 znaków
   EN: We triumphed for now, yet I do not know what lies in our future.
   PL:
829. [Kwestia głosowa [choice_fail_n_10310_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=choice_fail_n_10310_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Kwestia głosowa [choice_fail_n_10310_1] (Check Failed)] …불가능한 것에 기대를 품었던 거다. 처음부터 안 될 일이었어.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=choice_fail_n_10310_1].dlg
   limit: do 120 znaków
   EN: ... Your mistake was putting your faith in an impossibility. It was destined for failure.
   PL:
831. [Kwestia głosowa [battle_clear_10310_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_clear_10310_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Kwestia głosowa [battle_clear_10310_1] (Victory Cry)] 고작 이 정도로 만족하려고, 패륜의 죄까지 저지른 게 아냐. 더 많은 가족들이 배불리 먹기 위해… 피의 흐름이 멈춰선 안 돼.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_clear_10310_1].dlg
   limit: do 170 znaków
   EN: I did not commit the sin of filial impiety for this meager outcome. Blood must continue to flow, to sate more of my family...
   PL:
833. [Kwestia głosowa [battle_clear_ex_10310_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_clear_ex_10310_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Kwestia głosowa [battle_clear_ex_10310_1] (Extra Conditions Fulfilled)] 오랜 목마름도, 어버이를 향한 죄책감도… 피를 마시는 순간에는 생각나지 않을 거다. 그러니, 가릴 것 없이 마음껏 마셔. 그게 우리가 이룰 수 있는 유일한 꿈이니까.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_clear_ex_10310_1].dlg
   limit: do 260 znaków
   EN: When the blood wets our throats, we shall be liberated from the deep thirst and the guilt toward our Father. So drink, drink with abandon, for that is the only dream this existence has permitted us.
   PL:
835. [Kwestia głosowa [battle_defeat_10310_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_defeat_10310_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Kwestia głosowa [battle_defeat_10310_1] (Defeat Wail)] …예상한 일이야. 어버이와 달리 우리는 약하니까.\n비록 지금은 이렇게 되돌아가지만, 더 많은 피가 흐른 뒤에는…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_Bloodfiend_10310.json :: dataList[id=battle_defeat_10310_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This was to be expected, for we do not possess the strength that our Father wields.\nThus we retreat for now, but should more blood spill...
   PL:

## [000] Cinq Assoc. East Section 3 — Don Quixote — 동부 섕크 협회 3과
- ID Tożsamości: `10311` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: — · HP bazowe: 82 · szybkość: 2–5 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise, Burn

837. [Karta Tożsamości — tytuł] 동부 섕크 협회\n3과
   źródło: Personalities.json :: dataList[id=10311].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nEast Section 3
   PL:
838. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10311].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10311].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Karta Tożsamości — opis] 돈키호테의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10311].desc
   limit: do 120 znaków
   EN: Don Quixote's 11th Identity
   PL:
841. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발경
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].name ; dataList[id=1031101].levelList[level=2].name ; dataList[id=1031101].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Fa Jin
   PL:
842. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL:
843. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]
   PL:
844. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 843 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 속도가 대상보다 <style="highlight">2</style> 이상 높으면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by <style="highlight">2</style> or more, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL:
846. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict 1 [Combustion]
   PL:
847. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL:
849. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL:
850. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +1 [Combustion] Count</style>
   PL:
852. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 초염장
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].name ; dataList[id=1031102].levelList[level=2].name ; dataList[id=1031102].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Virescent Flame Palm
   PL:
853. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WinDuel] Gain 3 [Breath]
   PL:
854. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +2 [Breath] Count
   PL:
855. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 843 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
857. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 6당 [DefenseDown] 1 부여 (최대 2, 턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 6 [Combustion] on target (max 2, once per turn)
   PL:
858. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 속도가 대상보다 <style="highlight">2</style> 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by <style="highlight">2</style> or more, Coin Power +1\n[WinDuel] Gain 3 [Breath]
   PL:
859. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[OnSucceedAttack]</style> Gain +2 [Breath] Count
   PL:
860. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL:
862. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 6당 [DefenseDown] 1 부여 (최대 <style="highlight">3</style>, 턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 6 [Combustion] on target (max <style="highlight">3</style>, once per turn)
   PL:
863. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WinDuel] [Breath] 3 얻음\n<style="highlight">- 대상의 [DianxueDonQuixote]만큼 추가로 [Breath] 횟수 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [Breath], [DianxueDonQuixote]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WinDuel] Gain 3 [Breath]\n<style="highlight">- Gain additional [Breath] Count equal to [DianxueDonQuixote] on target</style>
   PL:
864. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count<style="highlight"></style>
   PL:
865. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL:
866. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 6당 [DefenseDown] 1 부여 (최대 <style="highlight">5</style>, 턴당 1회)\n<style="highlight">- 대상의 [DianxueDonQuixote]만큼 [DefenseDown] 추가로 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Combustion], [DefenseDown], [DianxueDonQuixote]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 6 [Combustion] on target (max <style="highlight">5</style>, once per turn)\n<style="highlight">- Inflict additional [DefenseDown] equal to [DianxueDonQuixote] on target</style>
   PL:
867. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 한 수 부탁드리겠네
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].name ; dataList[id=1031103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 60 znaków
   EN: Prithee, let this be an enlightening bout
   PL:
868. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [DianxueDonQuixote] 1당 피해량 +10% (최대 30%)\n자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [DianxueDonQuixote]가 있으면 추가로 [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [DianxueDonQuixote], [WinDuel], [Breath]
   znaczenie tagów: [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: Deal +10% damage for every 1 [DianxueDonQuixote] on target (max 30%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WinDuel] Gain 5 [Breath]\n- If target has [DianxueDonQuixote], gain 3 additional [Breath]
   PL:
869. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
870. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 869 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 856 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +(자신의 [Breath] + 대상의 [Combustion])% (최대 30%)
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn
   EN: Deal +([Breath] on self + [Combustion] on target)% damage on Critical Hit (max 30%)
   PL:
873. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [DianxueDonQuixote] 1당 피해량 <style="highlight">+15%</style> (최대 <style="highlight">45%</style>)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [DianxueDonQuixote]가 있으면 추가로 [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DianxueDonQuixote], [WinDuel], [Breath]
   znaczenie tagów: [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: Deal <style="highlight">+15%</style> damage for every 1 [DianxueDonQuixote] on target (max <style="highlight">45%</style>)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WinDuel] Gain 5 [Breath]\n- If target has [DianxueDonQuixote], gain 3 additional [Breath]
   PL:
874. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 861 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +(자신의 [Breath] + 대상의 [Combustion])% (최대 <style="highlight">50%</style>)
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn
   EN: Deal +([Breath] on self + [Combustion] on target)% damage on Critical Hit (max <style="highlight">50%</style>)
   PL:
878. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상에게 [DianxueDonQuixote]가 있으면 [DefenseDown] 3 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DianxueDonQuixote], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttack] If target has [DianxueDonQuixote], inflict 3 [DefenseDown]</style>
   PL:
879. [Obrona (ulepszenia 1,4) — nazwa] 밥상머리 예절부터 배우시게!
   źródło: Skills_personality-03.json :: dataList[id=1031104].levelList[level=1].name ; dataList[id=1031104].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 70 znaków
   EN: Thou'rt in dire need of a lesson in table manners!
   PL:
880. [Obrona (ulepszenie 4) — opis] <style="highlight">자신의 속도가 공격자보다 높으면, 속도 차이 2당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031104].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain +1 Coin Power for every 2 Speed difference (max 2)</style>
   PL:
881. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath, posiadane 2× Pride) — nazwa] 초염옥구
   źródło: Passives.json :: dataList[id=1031101].name
   limit: do 40 znaków
   EN: Virescent Pyrojade
   PL:
882. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath, posiadane 2× Pride) — opis] 턴 종료 시 자신의 [Breath] 위력 5당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n기본 공격 스킬로 마지막에 적중한 대상(또는 부위)에게 다음 턴에 [DianxueDonQuixote] 부여 (턴당 1회)\n\n크리티컬 피해량 +(대상의 [Combustion] 위력)% (최대 15%)
   źródło: Passives.json :: dataList[id=1031101].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [DianxueDonQuixote], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [Combustion] = 화상 / Burn
   EN: Turn End: gain 1 [Agility] next turn for every 5 [Breath] Potency on self (max 2)\n\nAgainst the target(or the Part) a Base Attack Skill hit last, inflict [DianxueDonQuixote] next turn (once per turn)\n\nDeal +([Combustion] Potency on the target)% damage on Critical Hit (max 15%)
   PL:
883. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Wrath, posiadane 2× Pride) — nazwa] 초염옥구
   źródło: Passives.json :: dataList[id=1031111].name
   (powtórzenie elementu 881 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Wrath, posiadane 2× Pride) — opis] 턴 종료 시 자신의 [Breath] 위력 <style="highlight">3</style>당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n기본 공격 스킬로 마지막에 적중한 대상(또는 부위)에게 다음 턴에 [DianxueDonQuixote] 부여 (턴당 1회)\n\n크리티컬 피해량 +(대상의 [Combustion] 위력)% (최대 15%)\n<style="highlight">- 대상의 [DianxueDonQuixote] 1당 최댓값 5% 증가</style>
   źródło: Passives.json :: dataList[id=1031111].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Agility], [DianxueDonQuixote], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [Combustion] = 화상 / Burn
   EN: Turn End: gain 1 [Agility] next turn for every <style="highlight">3</style> [Breath] Potency on self (max 2)\n\nAgainst the target(or the Part) a Base Attack Skill hit last, inflict [DianxueDonQuixote] next turn (once per turn)\n\nDeal +([Combustion] Potency on the target)% damage on Critical Hit (max 15%)\n<style="highlight">- Increase max cap by 5% for every 1 [DianxueDonQuixote] on the target</style>
   PL:
885. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 경신법
   źródło: Passives.json :: dataList[id=1031121].name
   limit: do 40 znaków
   EN: Featherstride Technique
   PL:
886. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 속도가 가장 빠른 아군 1명이 [Combustion] 또는 특수 화상을 보유한 적에게 합 승리 시, 다음 턴에 [Agility] 1을 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1031121].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Agility]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Agility] = 신속 / Haste
   EN: 1 ally with the fastest Speed : On Clash Win against enemies with [Combustion] or 'Unique Burn', gain 1 [Agility] next turn (once per turn)
   PL:
887. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — nazwa] 경신법
   źródło: Passives.json :: dataList[id=1031131].name
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — opis] 속도가 가장 빠른 아군 1명이 [Combustion] 또는 특수 화상을 보유한 적에게 합 승리 시, 다음 턴에 [Agility] 1을 얻음 (턴당 1회)\n<style="highlight">- 대상의 [Combustion] 위력이 20 이상이면, 신속 1을 추가로 얻음</style>
   źródło: Passives.json :: dataList[id=1031131].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Agility]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Agility] = 신속 / Haste
   EN: 1 ally with the fastest Speed : On Clash Win against enemies with [Combustion] or 'Unique Burn', gain 1 [Agility] next turn (once per turn)\n<style="highlight">- If the target has 20+ [Combustion] Potency, gain 1 additional [Agility]</style>
   PL:
889. [Kwestia głosowa [get_10311_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=get_10311_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Kwestia głosowa [get_10311_1] (Identity Acquisition)] 음식이 좀 슴슴한가 했더니~\n이런 난장판이라는 조미료를 준비해 둘 줄은 본인이 미처 몰랐군!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=get_10311_1].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Aha, so this explaineth the slight blandness of thy banquet! To prepare such spicy condiments in the form of a brawl... Forsooth, 'twas most unexpected!
   PL:
891. [Kwestia głosowa [lobby_morning_10311_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=lobby_morning_10311_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Kwestia głosowa [lobby_morning_10311_1] (Morning Greeting)] 아침 내내 잠만 잤다면 섭섭할 뻔했지 뭔가! 어우! 거기서 의자를 던진다고?! 히야… 간만의 휴일에 어울리는 최고의 아침드롸마 아니겠는가?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=lobby_morning_10311_1].dlg
   limit: do 240 znaków
   EN: Slumbering through such an exciting morn would have been a most tragic affair! Hooie, to launch that chair from such a distance—'tis as dramatic as an episode of a soap opera in the morn!!
   PL:
893. [Kwestia głosowa [lobby_noon_10311_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=lobby_noon_10311_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Kwestia głosowa [lobby_noon_10311_1] (Afternoon Greeting)] 동부는 점심에도 그리 여유롭게 돌아가지 않는다네. 서부의 협회는 제법 긴 티-타임을 즐긴다고도 들었네만~\n흠, 그렇게 느긋하게만 보내면 거리를 활보하는 의뢰 대상을 놓치기 마련이지.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=lobby_noon_10311_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The eastern branch doth not spend the lunch idly on their behinds. I have heard tell that the western branch enjoyeth a rather lengthy tea-time, yet...\nHm, alas. 'Tis one way to lose potential clientele that may be roaming the streets at that very moment.
   PL:
895. [Kwestia głosowa [lobby_night_10311_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=lobby_night_10311_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Kwestia głosowa [lobby_night_10311_1] (Evening Greeting)] 아~ 우리 섕크 동부지부는 야근은 지양하는 주의라서 말일세! 보통 밤에 일어나는 일은 우리보다 적합한 협회가 있지 않겠는가?\n무릇 결투란 백주대낮에 구경꾼들로 인산인해를 이룬 곳에서 치름이 바르지!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=lobby_night_10311_1].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah~ Verily, the eastern branch of the Cinq Association doth hold late-night assignments in disdain! Prithee, might there not be worthier Associations to which thou couldst call for matters of the night?\nDuels, forsooth, ought to be carried out under the high-noon sun in the audience of countless spectators!
   PL:
897. [Kwestia głosowa [smalltalk_10311_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Kwestia głosowa [smalltalk_10311_1] (Chatter #1)] 그야, 저렇게 소란스러운 자들이 있으면 몸이 들썩거리기는 하지만… 우리도 의뢰로 밥을 벌어먹고 사는 해결사. 아무런 대가 없이 행동할 수는 없는 것 아니겠나.\n…그, 그대… 본인의 옛날이야기는 어찌…! 크흠, 그건 과거 협회에 입문한지 얼마 안 되어 철부지였을 때…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_1].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Troublemakers such as those cur make my blood run hot... yet we are but Fixers whose subsistence dependeth on our trade. Wouldst thou not say that, thus, we mustn't act without compensation?\nH-how doest thou know of mine olden foolishness...! Ahem, 'twas but the manifestation of mine inexperience as a newcomer to this Association...!
   PL:
899. [Kwestia głosowa [smalltalk_10311_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Kwestia głosowa [smalltalk_10311_2] (Chatter #2)] 크흠… 그리고! 이렇게 자리를 잡고 앉아 있으면 결국엔 우릴 알아보고 대리 결투를 의뢰하기 마련이지.\n그때 나서서 싸운다면 의뢰도 해결, 오만방자한 저 괴한들도 침묵! 일석이조 아니겠는가?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_2].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ahem... Aha! They shalt recognize me in no time, after I remain seated here awhile, and request me to duel in their stead.\n'Twould be like striking two birds with one pebble! I shall attain both the completion of a contract, and the silence of those raucous rascals!
   PL:
901. [Kwestia głosowa [smalltalk_10311_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Kwestia głosowa [smalltalk_10311_3] (Chatter #3)] 그나저나… 이 유포면, 훌륭하군! 면이 바삭바삭한 게… 음?! 이보시게! 그쪽 반찬이 여기까지 튀잖나! 싸울 거면 식사에 방해가 되지 않게 싸우시게!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_3].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ooh... this bowl of biangbiang noodles is... ah, what an utter excellence this is! The crunchi— ack?!\nHark! Thou hast cast specks of thy side dishes unto my plates! Keep thy violent parley out of my bowl, pah!
   PL:
903. [Kwestia głosowa [smalltalk_10311_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Kwestia głosowa [smalltalk_10311_4] (Post-Uptie Chat 1)] 그런 날붙이는 본인에게 그다지 위협이 되지 않네, 친구. 그 날이 이 몸을 베어버리기 전에 본인의 초염옥구가 전부 녹여버릴테니!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_4].dlg
   limit: do 170 znaków
   EN: Thy bladed instrument poseth little threat to me, amigo. Mine virescent pyrojade shall melt it to nothingness ere it doth me harm!
   PL:
905. [Kwestia głosowa [smalltalk_10311_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Kwestia głosowa [smalltalk_10311_5] (Post-Uptie Chat 2)] 객잔에서 난장을 부리면 쓰겠나. 누가 있는지 잘 관찰부터 하셨어야지, 친구. 이 넓은 식당 안에 하나쯤은… 보통 고수가 섞여 있기 마련 아니겠나?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=smalltalk_10311_5].dlg
   limit: do 290 znaków
   EN: 'Twas a mistake to stir trouble in a tavern afore observing its clientele, amigo. 'Tis a rather spacious establishment—thou should have imagined that there would be a hidden dragon lurking somewhere amongst the shadows, hm?
   PL:
907. [Kwestia głosowa [neglect_10311_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=neglect_10311_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Kwestia głosowa [neglect_10311_1] (Idle)] 오오, 살짝 바삭한 것이 절묘하군!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=neglect_10311_1].dlg
   limit: do 120 znaków
   EN: Ooh! Verily, the present yet subtle crunchiness of the noodles maketh quite the perfection!
   PL:
909. [Kwestia głosowa [gacksung_10311_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=gacksung_10311_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Kwestia głosowa [gacksung_10311_1] (Uptying)] 어이쿠, 이런. 미안하네. 저쪽 신사분께서 '긴급 대리 결투'를 의뢰하셔서 말일세. 본인, 살짝 실례 좀 하겠네!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=gacksung_10311_1].dlg
   limit: do 160 znaków
   EN: Oof, apologies to thee. The gentleman there hath requested an 'emergency duel proxy' contract. I shall return in no time!
   PL:
911. [Kwestia głosowa [formation_10311_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=formation_10311_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Kwestia głosowa [formation_10311_1] (Deployment)] 자아, 의뢰로군!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=formation_10311_1].dlg
   limit: do 120 znaków
   EN: Aha, a contract!
   PL:
913. [Kwestia głosowa [battleentry_10311_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battleentry_10311_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Kwestia głosowa [battleentry_10311_1] (Stage Entry)] 동부 섕크 3과, 돈키호테!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battleentry_10311_1].dlg
   limit: do 120 znaków
   EN: Thou mayest know me as Don Quixote, Fixer of the third Section of Cinq Association East!
   PL:
915. [Kwestia głosowa [battle_select_10311_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_select_10311_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Kwestia głosowa [battle_select_10311_1] (Viewed in Battle)] 급행이신가? 의뢰비는 좀 더 비싸다네!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_select_10311_1].dlg
   limit: do 120 znaków
   EN: 'Tis an emergency, hm? Do know that it shall cost thee a tad more!
   PL:
917. [Kwestia głosowa [battle_endcommand_10311_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_endcommand_10311_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Kwestia głosowa [battle_endcommand_10311_1] (Commencing Attack)] 초염옥구를 달궈볼까.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_endcommand_10311_1].dlg
   limit: do 120 znaków
   EN: The virescent pyrojade burneth.
   PL:
919. [Kwestia głosowa [battle_enemy_break_10311_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_enemy_break_10311_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Kwestia głosowa [battle_enemy_break_10311_1] (Enemy Stagger)] 이 결투!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_enemy_break_10311_1].dlg
   limit: do 120 znaków
   EN: This duel!
   PL:
921. [Kwestia głosowa [battle_break_10311_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_break_10311_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Kwestia głosowa [battle_break_10311_1] (Staggered)] 헛?!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_break_10311_1].dlg
   limit: do 120 znaków
   EN: Hup?!
   PL:
923. [Kwestia głosowa [battle_kill_10311_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_kill_10311_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Kwestia głosowa [battle_kill_10311_1] (Enemy Killed)] 본인의 승리일세!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_kill_10311_1].dlg
   limit: do 120 znaków
   EN: Endeth with my victory!
   PL:
925. [Kwestia głosowa [battle_dead_10311_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_dead_10311_1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Kwestia głosowa [battle_dead_10311_1] (Death)] 아하… 한 수… 배웠, 네.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_dead_10311_1].dlg
   limit: do 120 znaków
   EN: Ahaaa... 'twas... quite education...al...
   PL:
927. [Kwestia głosowa [choice_success_p_10311_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=choice_success_p_10311_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Kwestia głosowa [choice_success_p_10311_2] (Check Passed)] 음, 해결됐잖나?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=choice_success_p_10311_2].dlg
   limit: do 120 znaków
   EN: Mm, the conundrum hath been resolved, no?
   PL:
929. [Kwestia głosowa [choice_fail_n_10311_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=choice_fail_n_10311_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Kwestia głosowa [choice_fail_n_10311_1] (Check Failed)] 흐으음… 앗, 녹이면 안됐나?!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=choice_fail_n_10311_1].dlg
   limit: do 120 znaków
   EN: Hohh... Ack, should I not have melted that?!
   PL:
931. [Kwestia głosowa [battle_clear_10311_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_clear_10311_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Kwestia głosowa [battle_clear_10311_1] (Victory Cry)] 의뢰 내용이 좀 복잡했지만, 뭐… 본인이 해결 못할 일은 없지! 장애물은 전부 흩트려 없애는 편이니.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_clear_10311_1].dlg
   limit: do 180 znaków
   EN: Forsooth, this contract was a tad complicated, yet... No task shall remain undone before me, for all that standeth before me scattereth!
   PL:
933. [Kwestia głosowa [battle_clear_ex_10311_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_clear_ex_10311_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Kwestia głosowa [battle_clear_ex_10311_1] (Extra Conditions Fulfilled)] 돈이 더 들긴 해도 긴급으로 하길 잘했지 않은가? 후훗, 아? 아냐. 넣어두게. 정말 두 배로 받을 거라고 생각했는가? 그런 건~ 정의롭지 않지!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_clear_ex_10311_1].dlg
   limit: do 340 znaków
   EN: Was it not a decision most wise to employ mine emergency services, though more expensive it may have been? Heh heh... oh? Ah, nay. Close thy wallet; thou didst not truly believe that I would charge thee double, hm? To do so~ would be to stray from the way of justice!
   PL:
935. [Kwestia głosowa [battle_defeat_10311_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_defeat_10311_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Kwestia głosowa [battle_defeat_10311_1] (Defeat Wail)] 결투의 내용이 난해하긴 했어도… 지는 것을 상상한 적은 없네만… 이, 이러면 중간중간 훈련을 내빼고 거리를 돌아다닌 책임을 추궁당할 터…! 으윽, 어찌해야…?!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_CinqEast_10311.json :: dataList[id=battle_defeat_10311_1].dlg
   limit: do 290 znaków
   EN: Ne'er did I once imagine that I would be defeated, despite the complicatedness of this contract... F-fie... they are to discover that I have absconded from training in favor of roaming the streets...! Agh, what must I do...?!
   PL:

## [000] Lobotomy E.G.O:: In the Name of Love and Hate — Don Quixote — 로보토미 E.G.O:: 사랑과 증오의 이름으로
- ID Tożsamości: `10312` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9106 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Charge, Rupture, Sinking

937. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n사랑과 증오의 이름으로
   źródło: Personalities.json :: dataList[id=10312].title
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nIn the Name of\nLove and Hate
   PL:
938. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10312].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10312].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Karta Tożsamości — opis] 돈키호테의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10312].desc
   limit: do 120 znaków
   EN: Don Quixote's 12th Identity
   PL:
941. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 관리자 나리의 명에 따라 등장!
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].name ; dataList[id=1031201].levelList[level=2].name ; dataList[id=1031201].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 60 znaków
   EN: By Manager Esquire's Orders, I Am Here!
   PL:
942. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [WhenUse] Gain +2 [ThePowerOfLoveAndHate] Count
   PL:
943. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +2 [ThePowerOfLoveAndHate] Count
   PL:
944. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 코인 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: <style="highlight">[WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">3</style> [ThePowerOfLoveAndHate] Count
   PL:
946. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +2 [ThePowerOfLoveAndHate] Count<style="highlight"></style>
   PL:
947. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL:
948. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 2당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1\n<style="highlight">[WhenUse] Coin Power +1 for every 2 [ThePowerOfLoveAndHate] (max 2)</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count
   PL:
949. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [ThePowerOfLoveAndHate] Count
   PL:
950. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Burst]
   PL:
951. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 사랑으로! 욥!
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].name ; dataList[id=1031202].levelList[level=2].name ; dataList[id=1031202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: With Love! Hyah!
   PL:
952. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count
   PL:
953. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +3 [ThePowerOfLoveAndHate] Count
   PL:
954. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">자신의 [ThePowerOfLoveAndHate]당 피해량 +7.5% (최대 30%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 코인 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ThePowerOfLoveAndHate], [WhenUse]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Deal +7.5% damage for every [ThePowerOfLoveAndHate] on self (max 30%)\n[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count
   PL:
956. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ThePowerOfLoveAndHate] Count
   PL:
957. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] 다음 턴에 메인 타겟에게 [VillainMark] 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [VillainMark]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttackHead] Inflict [VillainMark] against the main target next turn</style>
   PL:
959. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 [ThePowerOfLoveAndHate]당 피해량 +<style="highlight">12.5</style>% (최대 <style="highlight">75</style>%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 코인 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ThePowerOfLoveAndHate], [WhenUse]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [WhenUse] = [사용시] / [On Use]
   EN: Deal +<style="highlight">12.5</style>% damage for every [ThePowerOfLoveAndHate] on self (max <style="highlight">75</style>%)\n[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1\n[WhenUse] Gain +<style="highlight">5</style> [ThePowerOfLoveAndHate] Count
   PL:
960. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 4 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +4 [ThePowerOfLoveAndHate] Count<style="highlight"></style>
   PL:
961. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL:
962. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]</style> 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VillainMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict [VillainMark] against the main target next turn
   PL:
963. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 아르카나 비트!! / 마이너 아르카나 슬레이브!!!
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].name ; dataList[id=1031203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: Arcana Beats!! / Minor Arcana Slave!!!
   PL:
964. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [ArcanaQueenOfHate]당, 피해량 +15% (최대 45%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, ([ThePowerOfLoveAndHate] X 20)%만큼 피해량이 증가 (최대 80%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5씩 소모하여, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 6 증가\n[EndSkill] [ArcanaQueenOfHate] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [ArcanaQueenOfHate], [WhenUse], [ThePowerOfLoveAndHate], [EndSkill]
   znaczenie tagów: [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +15% damage for every [ArcanaQueenOfHate] on self (max 45%)\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], deal +([ThePowerOfLoveAndHate] x 20)% damage (max 80%)\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], Base Power +1\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Coin Power (Coin Power +1 for every 5 Count consumed, max 2)\n[WhenUse] Gain +6 [ThePowerOfLoveAndHate] Count\n[EndSkill] Gain 1 [ArcanaQueenOfHate]
   PL:
965. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1031203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst]
   PL:
968. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1031203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 967 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [ArcanaQueenOfHate]당 피해량 +<style="highlight">30</style>% (최대 <style="highlight">90</style>%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, ([ThePowerOfLoveAndHate] X <style="highlight">25</style>)%만큼 피해량이 증가 <style="highlight">(최대 125%)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, 기본 위력 +<style="highlight">2</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5씩 소모하여, 코인 위력 +1 <style="highlight">(최대 4)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 6 증가\n[EndSkill] [ArcanaQueenOfHate] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArcanaQueenOfHate], [WhenUse], [ThePowerOfLoveAndHate], [EndSkill]
   znaczenie tagów: [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +<style="highlight">30</style>% damage for every [ArcanaQueenOfHate] on self (max <style="highlight">90</style>%)\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], deal +([ThePowerOfLoveAndHate] x <style="highlight">25</style>)% damage <style="highlight">(max 125%)</style>\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], Base Power +<style="highlight">2</style>\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Coin Power (Coin Power +1 for every 5 Count consumed, max <style="highlight">4</style>)\n[WhenUse] Gain +6 [ThePowerOfLoveAndHate] Count\n[EndSkill] Gain 1 [ArcanaQueenOfHate]
   PL:
971. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 악당은... 어디있어....?
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].name ; dataList[id=1031205].levelList[level=2].name ; dataList[id=1031205].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 12 · monety: 2 (−4)
   limit: do 50 znaków
   EN: Where are... the villains...?
   PL:
972. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 자신의 [HystericGauge]당 피해량 +3% (최대 9%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가\n[WhenUse] 정신력 5 감소
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal +3% damage for every [HystericGauge] on self (max 9%)\n[WhenUse] Gain +2 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 5 SP
   PL:
973. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
975. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 자신의 [HystericGauge]당 피해량 <style="highlight">+4% (최대 12%)</style>\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 기본 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가\n[WhenUse] 정신력 5 감소
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal <style="highlight">+4%</style> damage for every [HystericGauge] on self <style="highlight">(max 12%)</style>\n<style="highlight">[WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1</style>\n[WhenUse] Gain <style="highlight">+3</style> [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 5 SP
   PL:
976. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 946 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Sinking]
   PL:
978. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 자신의 [HystericGauge]당 피해량 <style="highlight">+5% (최대 15%)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 기본 위력 +1\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 2당, 기본 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가\n[WhenUse] 정신력 5 감소
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal <style="highlight">+5%</style> damage for every [HystericGauge] on self <style="highlight">(max 15%)</style>\n<style="highlight">[WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1</style>\n<style="highlight">[WhenUse] Base Power +1 for every 2 [ThePowerOfLoveAndHate] on self (max 2)</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 5 SP
   PL:
979. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Sinking]
   PL:
981. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 내 머릿속에서 나가줘...
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].name ; dataList[id=1031206].levelList[level=2].name ; dataList[id=1031206].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 15 · monety: 2 (−6)
   limit: do 40 znaków
   EN: Get out of my head...
   PL:
982. [Umiejętność 5 (×0) (ulepszenie 1) — opis] 자신의 [HystericGauge]가 있으면, 합 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가\n[WhenUse] 정신력 8 감소
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: If this unit has [HystericGauge], Clash Power +1\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 8 SP
   PL:
983. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 974 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Umiejętność 5 (×0) (ulepszenie 2) — opis] 자신의 [HystericGauge]가 있으면, <style="highlight">기본 위력 +1</style>\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 기본 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가\n[WhenUse] 정신력 8 감소
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: If this unit has [HystericGauge], <style="highlight">Base Power +1</style>\n<style="highlight">[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 8 SP
   PL:
986. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031206].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +3 [ThePowerOfLoveAndHate] Count<style="highlight"></style>
   PL:
987. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 977 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackTail] 다음 턴에 메인 타겟에게 [VillainMark] 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [VillainMark]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttackTail] Inflict [VillainMark] against the main target next turn</style>
   PL:
989. [Umiejętność 5 (×0) (ulepszenie 4) — opis] <style="highlight">자신의 [HystericGauge]당 기본 위력 +1(최대 2)\n- [HystericGauge]가 3이면, 공격 가중치 +1\n- 서브 타겟에게 가하는 피해량 -50%</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 기본 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">5</style> 증가\n[WhenUse] 정신력 8 감소
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: <style="highlight">Base Power +1 for every [HystericGauge] on self (max 2)\n- At 3 [HystericGauge], gain +1 Atk Weight\n- Deal -50% damage against sub-targets</style>\n[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1\n[WhenUse] Gain +<style="highlight">5</style> [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 8 SP
   PL:
990. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL:
991. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]</style> 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 962 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 리버스드 비트 / 리버스드 아르카나 슬레이브
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].name ; dataList[id=1031207].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 20 · monety: 3 (−6)
   limit: do 60 znaków
   EN: Reversed Beats / Reversed Arcana Slave
   PL:
993. [Umiejętność 6 (×0) (ulepszenie 3) — opis] 이 스킬로 서브 타겟에게 가하는 피해량 -50%\n\n[WhenUse] [HystericGauge]를 전부 소모하여, 합 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 8씩 소모하여, 합 위력 +1 (최대 2)\n자신의 [ThePowerOfLoveAndHate]당 피해량 +15%(최대 60%)\n[BeforeAttack] 자신의 [ArcanaQueenOfHate]를 전부 소모하여, 공격 가중치 +1\n[BeforeAttack] 공격 대상이 한 명(집중 전투일 경우, 부위로 판정)일 때, 공격 가중치가 2 이상이면 피해량 +20%\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -18)\n[EndBattle] 정신력이 -45가 아니고 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 2회복, 최대 50)\n[WhenUse] 정신력 10 감소
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate], [BeforeAttack], [ArcanaQueenOfHate], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: This Skill deals -50% damage against sub-targets\n\n[WhenUse] Consume all [HystericGauge] to gain Clash Power +1\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Clash Power (Clash Power +1 for every 8 Count consumed, max 2)\nDeal +15% damage for every [ThePowerOfLoveAndHate] on self (max 60%)\n[BeforeAttack] Consume all [ArcanaQueenOfHate] on self to gain +1 Atk Weight\n[BeforeAttack] If this Skill only has a single target(for Focused Encounters, a Part), but has 2+ Atk Weight, deal +20% damage\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -18)\n[EndBattle] If this unit isn't at -45 SP, and is at less than 0 SP, heal 10 SP. Heal more SP the further this unit's SP value is from 0 (2 SP healed for every missing SP, max 50 SP)\n[WhenUse] Lose 10 SP
   PL:
994. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]
   PL:
997. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 996 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Umiejętność 6 (×0) (ulepszenie 4) — opis] 이 스킬로 서브 타겟에게 가하는 피해량 -50%\n\n[WhenUse] [HystericGauge]를 전부 소모하여<style="highlight">, 소모한 수치당 합 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 <style="highlight">5씩</style> 소모하여, 합 위력 +1 <style="highlight">(최대 4)</style>\n자신의 [ThePowerOfLoveAndHate]당 피해량 +<style="highlight">30</style>%(최대 <style="highlight">150</style>%)\n[BeforeAttack] 자신의 [ArcanaQueenOfHate]를 전부 소모하여, <style="highlight">소모한 수치당 공격 가중치 +1 (최대 3)\n- 이 스킬로 소모한 [HystericGauge]가 3이면, 공격 가중치 +1</style>\n[BeforeAttack] 공격 대상이 한 명(집중 전투일 경우, 부위로 판정)일 때, <style="highlight">(공격 가중치 - 1)만큼 피해량이 증가 (수치당 20%, 최대 80%)</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -18)\n[EndBattle] 정신력이 -45가 아니고 정신력이 0 미만이면, 정신력 10회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 2회복, 최대 50)\n[WhenUse] 정신력 10 감소
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].desc
   limit: do 1130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate], [BeforeAttack], [ArcanaQueenOfHate], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: This Skill deals -50% damage against sub-targets\n\n[WhenUse] Consume all [HystericGauge]; <style="highlight">Clash Power +1 for every Stack consumed (max 3)</style>\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Clash Power (Clash Power +1 for every <style="highlight">5</style> Count consumed, max <style="highlight">4</style>)\nDeal +<style="highlight">30</style>% damage for every [ThePowerOfLoveAndHate] on self (max <style="highlight">150</style>%)\n[BeforeAttack] Consume all [ArcanaQueenOfHate] on self; <style="highlight">gain +1 Atk Weight for every Stack consumed (max 3)\n- If this Skill consumed 3 [HystericGauge], gain +1 Atk Weight</style>\n[BeforeAttack] If this Skill only has a single target(for Focused Encounters, a Part), <style="highlight">deal +(20 x (Atk Weight - 1))% damage (max 80%)</style>\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -18)\n[EndBattle] If this unit isn't at -45 SP, and is at less than 0 SP, heal 10 SP. Heal more SP the further this unit's SP value is from 0 (2 SP healed for every missing SP, max 50 SP)\n[WhenUse] Lose 10 SP
   PL:
1000. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
1001. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1000 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL:
1003. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1000 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1002 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Obrona (ulepszenia 1,4) — nazwa] 단기 영창
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=1].name ; dataList[id=1031204].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Rapid Chant
   PL:
1006. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 자신의 [HystericGauge]당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가 (턴 당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [CanDuelGuard]\n[WhenUse] Base Power +1 for every [HystericGauge] (max 2)\n[WhenUse] Gain +2 [ThePowerOfLoveAndHate] Count (2 times per turn)
   PL:
1007. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[WhenUse] 자신의 [HystericGauge]당, 기본 위력 +1 <style="highlight">(최대 3)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">4</style> 증가 (턴 당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [CanDuelGuard]\n[WhenUse] Base Power +1 for every [HystericGauge] <style="highlight">(max 3)</style>\n[WhenUse] Gain +<style="highlight">4</style> [ThePowerOfLoveAndHate] Count (2 times per turn)
   PL:
1009. [Pasywka bojowa (od ulepszenia 1) — nazwa] 사랑과 증오의 이름으로 - !E.G.O 장비 동기화율 초과주의!
   źródło: Passives.json :: dataList[id=1031202].name
   limit: do 100 znaków
   EN: In the Name of Love and Hate - !ALERT: E.G.O GEAR SYNC THRESHOLD EXCEEDED!
   PL:
1010. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [ThePowerOfLoveAndHate] 횟수 10을 소모할 때마다, [ThePowerOfLoveAndHate] 1 얻음\n\n스테이지 시작시 [HystericGauge]가 없다면, [HystericGauge] 효과를 얻음\n\n스테이지 시작시 [ThePowerOfLoveAndHate]가 없다면, [ThePowerOfLoveAndHate] 효과를 얻음\n\n턴 시작시\n- 정신력이 0 이상이면, [MagicalGirlAppear] 얻음, [NoVillain] 제거\n- 정신력이 0 미만이면, [NoVillain] 얻음, [MagicalGirlAppear] 제거\n\n자신의 기본 공격 스킬의 정신력 소모 효과에 의해서 정신력이 -40 미만으로 내려가지 않음
   źródło: Passives.json :: dataList[id=1031202].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [ThePowerOfLoveAndHate], [HystericGauge], [MagicalGirlAppear], [NoVillain]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [HystericGauge] = 히스테리 / Hysteria; [MagicalGirlAppear] = 마법소녀 등장! / Here Comes Magical Girl!; [NoVillain] = 역변-리버스드 / Regressive Transformation - Reversed
   EN: Gain 1 [ThePowerOfLoveAndHate] every time this unit consumes 10 cumulative [ThePowerOfLoveAndHate] Count in this Encounter\n\nEncounter Start: if this unit does not have [HystericGauge], gain [HystericGauge]\n\nEncounter Start: if this unit does not have [ThePowerOfLoveAndHate], gain [ThePowerOfLoveAndHate]\n\nTurn Start:\n- At 0 or higher SP, gain [MagicalGirlAppear] and lose [NoVillain]\n- At less than 0 SP, gain [NoVillain] and lose [MagicalGirlAppear]\n\nThis unit's SP cannot drop below -40 due to the SP loss effects from this unit's Base Attack Skills
   PL:
1011. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Envy) — nazwa] 사랑의 마법소녀 / 증오의 여왕
   źródło: Passives.json :: dataList[id=1031201].name
   limit: do 60 znaków
   EN: Magical Girl of Love / Queen of Hatred
   PL:
1012. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Envy) — opis] [ThePowerOfLoveAndHate]당, 피해량 +2% (최대 10%)
   źródło: Passives.json :: dataList[id=1031201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ThePowerOfLoveAndHate]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal +2% damage for every [ThePowerOfLoveAndHate] (max 10%)
   PL:
1013. [Pasywka bojowa (od ulepszenia 3, rezonans 4× Envy) — nazwa] 사랑의 마법소녀 / 증오의 여왕
   źródło: Passives.json :: dataList[id=1031211].name
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1014. [Pasywka bojowa (od ulepszenia 3, rezonans 4× Envy) — opis] [ThePowerOfLoveAndHate]당, 피해량 +2% (최대 10%)\n전투 시작 시, [ArcanaQueenOfHate] 1 얻음
   źródło: Passives.json :: dataList[id=1031211].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [ThePowerOfLoveAndHate], [ArcanaQueenOfHate]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana
   EN: Deal +2% damage for every [ThePowerOfLoveAndHate] (max 10%)\nCombat Start: gain 1 [ArcanaQueenOfHate]
   PL:
1015. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — nazwa] 매지컬 파워 차징 서포트
   źródło: Passives.json :: dataList[id=1031221].name
   limit: do 50 znaków
   EN: Magical Power Charging Support
   PL:
1016. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — opis] 기본 공격 스킬에서 [Charge] 횟수를 획득하는 아군 중 [Charge] 횟수가 가장 적은 1명이 [Charge] 횟수를 획득하는 기본 공격 스킬 사용 시, [Charge] 횟수 +2 (턴 당 2회 발동)\n- 정신력이 0 이상이면, 체력을 (대상의 [Charge] X 2)만큼 회복 (최대 10, 턴 당 최대 20 회복)\n- 정신력이 0 미만이면, 정신력을 대상의 [Charge]만큼 회복 (최대 5, 턴 당 최대 10 회복)
   źródło: Passives.json :: dataList[id=1031221].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: If, among allies that gain [Charge] Count using their Base Attack Skills, 1 ally that has the least [Charge] Count uses a Base Attack Skill that gains [Charge] Count, the said ally gains +2 [Charge] Count (2 times per turn)\n- At 0 or higher SP: heal ([Charge] on target x 2) HP (max 10; heals up to 20 per turn)\n- At less than 0 SP: heal ([Charge] on target) SP (max 5; heals up to 10 per turn)
   PL:
1017. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — podsumowanie] [Charge] 횟수 증가\n- 정신력에 따라, [Charge]에 비례하여 체력이나 정신력 회복
   źródło: Passives.json :: dataList[id=1031221].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] Count\n- Depending on this unit's SP, Heal HP or SP based on [Charge]
   PL:
1018. [Kwestia głosowa [get_10312_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=get_10312_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Kwestia głosowa [get_10312_1] (Identity Acquisition)] 보시게! 사랑과 평화를 수호한 자들의 이야기가 여기에 적혀있지… 후후, 바로 우리 마법소녀들 같지 않은가! <color=#ff6baa>오오…! 해결사란 건 이런 거구나?</color>
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=get_10312_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6baa>, </color>, \n
   EN: Behold! Herein are chronicled the tales of protectors of love and peace! Heh heh, verily, they are quite like us Magical Maidens!\n<color=#ff6baa>Oooh...! So that's what Fixers do, huh?</color>
   PL:
1020. [Kwestia głosowa [lobby_morning_10312_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=lobby_morning_10312_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Kwestia głosowa [lobby_morning_10312_1] (Morning Greeting)] 아~ 마법소녀에게 아침은 너무나 힘든 시간이라네. 정의롭지 못한 자들은 어째서 항상 늦은 밤만 좋아하는 것인지! 그래서 항상 수면 부족인 셈이지…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=lobby_morning_10312_1].dlg
   limit: do 260 znaków
   EN: Ahhh~ Such early hours of the morn are cause for struggle for Magical Maidens. How is it that the unjust have such predilection for the wee hours of the night? As such, we are always sleep-deprived...
   PL:
1022. [Kwestia głosowa [lobby_noon_10312_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=lobby_noon_10312_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Kwestia głosowa [lobby_noon_10312_1] (Afternoon Greeting)] 아이고, 이것 참! 이 친구의 영웅담을 듣고 있다보니 벌써 점심을 먹을 시간이 되어버렸지 뭔가?! 배가 고픈 줄도 몰랐네… <color=#ff6baa>저기, 저기! 이번에 말해줄 건 진짜 더 재밌는 거야. 내가 지난 번에 아르카나에게 기습을 받았을 때 인데… </color> 으음?! 어… 그, 점심은 결식! 결식하겠네!!!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=lobby_noon_10312_1].dlg
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6baa>, </color>, \n
   EN: Fie, fie! It appeareth that the time for mine luncheon hath arrived already! I hardly noticed the time pass by, for I was engrossed in tales of thine heroism!\n<color=#ff6baa>Hey, hold on! I've got an even more exciting story for you. It's about the time I was ambushed by Arcana...</color>\nHm?! That's, uh... v-verily, I shall forgo the midday meal to hear thy tale, then!!!
   PL:
1024. [Kwestia głosowa [lobby_night_10312_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=lobby_night_10312_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1025. [Kwestia głosowa [lobby_night_10312_1] (Evening Greeting)] 밤이 되었지만 퇴근할 수 없다네… 본인의 담당이자 친구인 마법소녀께서는 이제부터가 본격적인 정의 집행의 시작일테니까! 직원으로서 도와야하지 않겠는가? 흐아암… 우우, 피곤하긴 하네만.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=lobby_night_10312_1].dlg
   limit: do 330 znaków
   EN: The hour is late, yet my work continueth... for Lady Magical Girl, my responsibility and a dear friend, hath deigned to enact justice at this hour! Forsooth, as an employee, 'tis mine obligation to assist her. Yaaaawn... Nngh, yet I am quite weary still...
   PL:
1026. [Kwestia głosowa [smalltalk_10312_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Kwestia głosowa [smalltalk_10312_1] (Chatter #1)] 평화롭고 조용하다는 건 좋은 것이지 않은가? 이 곳은 심심하면 끔찍한 일이 펑펑 터지는 곳이다보니까… 음? 아, 최근에는 좀 느긋하게 시간이 지나갔던 것 같기도 하군. 아, 심심하신가? 그럴 땐 역시! 해결사 잡지 만한게 없지!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_1].dlg
   limit: do 440 znaków
   EN: Peace and quiet are good qualities to have, are they not? 'Tis a place in which absurd horrors occur with such prevalence, thus... Hm? Ah, verily. 'Tis true that we are having a brief pocket of leisure at this moment. Ah, dost thou, perchance, find thyself mired in boredom? Then I have a remedy for thee! Behold, another issue of Fixers Monthly!
   PL:
1028. [Kwestia głosowa [smalltalk_10312_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Kwestia głosowa [smalltalk_10312_2] (Chatter #2)] 사실… 크흠, 본인은 자네에게 많은 고마움을 느끼고 있다네. 자네를 관리하는 실적을 인정 받아 이 중앙 본부의 팀장으로 전환 발령을 받았다고 들었어서… 본인이 자네를 담당한 이후로 한 번도 탈출하지 않았다고 하던데, 흠… 설마 본인을 위해서 참으신겐가?!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_2].dlg
   limit: do 430 znaków
   EN: In truth, I... ahem. I have been feeling quite indebted to thee. I heard in passing that I owe mine transfer and promotion to a Captain of the Central Command Team to my performance in managing thee... Thou hast not once broken containment succeeding thine assignment to my care, indeed? Hmm... ah, didst thou suppress thyself for my sake?!
   PL:
1030. [Kwestia głosowa [smalltalk_10312_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Kwestia głosowa [smalltalk_10312_3] (Chatter #3)] 아니! 세상은 꼭 선과 악, 두 가지로만 구분되진 않는다네! 모두가 혼재된 선과 악을 지니고 있지. 그러니 악이 없으면 자네의 존재 이유가 없을 거라는, 그런 슬픈 말은… 하지 마시게.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_3].dlg
   limit: do 370 znaków
   EN: Nay! We live not in a binary world with a clear-cut demarcation of 'good' and 'evil'! We are all amalgamations that exist in precarious and complicated balance of both. Thus, I implore thee—harbor no such sad sentiments, for the existence of evil is not the sole measure of thine worth.
   PL:
1032. [Kwestia głosowa [smalltalk_10312_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1033. [Kwestia głosowa [smalltalk_10312_4] (Post-Uptie Chat 1)] 2단계 경보가 울린다는 건… 음! 그대가 출동해서 정의의 심판을 내릴 시간이라는 것이겠군! 자, 나도 그대가 선물한 이 머리핀과 E.G.O 장비로… 직접 이 혼돈을 정리하겠네!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_4].dlg
   limit: do 260 znaków
   EN: The Second Warning... hm! 'Tis evident! Now is the time for thee to deliver unto them the smiting of justice! Ho! With this hairpin and E.G.O Gear, thy most gracious gift... and do away with this chaos!
   PL:
1034. [Kwestia głosowa [smalltalk_10312_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Kwestia głosowa [smalltalk_10312_5] (Post-Uptie Chat 2)] 나의 목숨을 바치는 한이 있더라도… 이곳의 직원들과 도시의 사람들을 지켜내고야 말겠네! 자, 아르카나… 비트!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=smalltalk_10312_5].dlg
   limit: do 180 znaków
   EN: Even if my life be made forfeit... I shall protect the employees of this establishment and the people of the City! Ho! Arcana... Beats!
   PL:
1036. [Kwestia głosowa [neglect_10312_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=neglect_10312_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Kwestia głosowa [neglect_10312_1] (Idle)] 흐음… 오늘은 경보가 울리지 않으려나… 헛! 이 무슨 무서운 생각을… 아니, 아니! 별 일 안 일어나서 심심하다던가, 그런 생각을 하진 않았다네!!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=neglect_10312_1].dlg
   limit: do 230 znaków
   EN: Hmm... no warnings today, I must wonder... hup! Perish the thought... Nay, nay! I have definitely not harbored thoughts of boredom induced by the lack of eventful action, nay!!
   PL:
1038. [Kwestia głosowa [gacksung_10312_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=gacksung_10312_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1039. [Kwestia głosowa [gacksung_10312_1] (Uptying)] 자아, 진정들 하시게! 이 몸이 등장했으니! 환상체 탈출 제압, 격리실 관리, 정신이 나가버린 직원 제압, 무엇이든지 좋네! 본인이! 틀림 없이 도움이 될 테니 꼭 부르게!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=gacksung_10312_1].dlg
   limit: do 350 znaków
   EN: Hark, one and all! Cease thy panicking, for I am here! Cast upon me any task thou seest fit: Abnormality containment breach suppression, containment unit management, insane employee suppression, anything shall do! Prithee, do summon me, as I shall doubtless be of assistance!
   PL:
1040. [Kwestia głosowa [formation_10312_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=formation_10312_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Kwestia głosowa [formation_10312_1] (Deployment)] 맡겨두시게!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=formation_10312_1].dlg
   limit: do 120 znaków
   EN: Prithee, leave it in my care!
   PL:
1042. [Kwestia głosowa [battleentry_10312_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battleentry_10312_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Kwestia głosowa [battleentry_10312_1] (Stage Entry)] 사랑과 정의의 이름으로~ 지금 이 곳에 등장!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battleentry_10312_1].dlg
   limit: do 120 znaków
   EN: In the name of Love and Justice~ Here cometh Magical Maiden!
   PL:
1044. [Kwestia głosowa [battle_select_10312_1] — sytuacja] 전투 중 인격 선택 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_select_10312_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle 1
   PL:
1045. [Kwestia głosowa [battle_select_10312_1] (Viewed in Battle 1)] 헉! 또 도움이 필요한 곳이 생겼는가?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_select_10312_1].dlg
   limit: do 120 znaków
   EN: Gasp! Doth aught requireth mine assistance?
   PL:
1046. [Kwestia głosowa [battle_select_hysteric_10312_1] — sytuacja] 전투 중 인격 선택 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_select_hysteric_10312_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle 2
   PL:
1047. [Kwestia głosowa [battle_select_hysteric_10312_1] (Viewed in Battle 2)] 내 머릿속에서 나가…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_select_hysteric_10312_1].dlg
   limit: do 120 znaków
   EN: Get out of my head...
   PL:
1048. [Kwestia głosowa [battle_endcommand_10312_1] — sytuacja] 공격 시작 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_endcommand_10312_1].desc
   limit: do 120 znaków
   EN: Commencing Attack 1
   PL:
1049. [Kwestia głosowa [battle_endcommand_10312_1] (Commencing Attack 1)] 만만찮겠군, 본인이 하지!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_endcommand_10312_1].dlg
   limit: do 120 znaków
   EN: 'Tis evident this foe shall pose a challenge... allow me!
   PL:
1050. [Kwestia głosowa [battle_endcommand_hysteric_10312_1] — sytuacja] 공격 시작 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_endcommand_hysteric_10312_1].desc
   limit: do 120 znaków
   EN: Commencing Attack 2
   PL:
1051. [Kwestia głosowa [battle_endcommand_hysteric_10312_1] (Commencing Attack 2)] 내가 쓸모가 있으려면…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_endcommand_hysteric_10312_1].dlg
   limit: do 120 znaków
   EN: If I am to be of any use...
   PL:
1052. [Kwestia głosowa [battle_enemy_break_10312_1] — sytuacja] 적 흐트러질 시 대사 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_enemy_break_10312_1].desc
   limit: do 120 znaków
   EN: Enemy Staggered 1
   PL:
1053. [Kwestia głosowa [battle_enemy_break_10312_1] (Enemy Staggered 1)] 후후. 이 정도 쯤이야!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_enemy_break_10312_1].dlg
   limit: do 120 znaków
   EN: Heh heh, 'tis light work!
   PL:
1054. [Kwestia głosowa [battle_enemy_break_hysteric_10312_1] — sytuacja] 적 흐트러질 시 대사 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_enemy_break_hysteric_10312_1].desc
   limit: do 120 znaków
   EN: Enemy Staggered 2
   PL:
1055. [Kwestia głosowa [battle_enemy_break_hysteric_10312_1] (Enemy Staggered 2)] 쓰레기 같은 아르카나 놈들…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_enemy_break_hysteric_10312_1].dlg
   limit: do 120 znaków
   EN: Arcana scum...
   PL:
1056. [Kwestia głosowa [battle_break_10312_1] — sytuacja] 흐트러질 시 대사 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_break_10312_1].desc
   limit: do 120 znaków
   EN: Staggered 1
   PL:
1057. [Kwestia głosowa [battle_break_10312_1] (Staggered 1)] 큭, 이럴 순…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_break_10312_1].dlg
   limit: do 120 znaków
   EN: Ngh, this cannot be...
   PL:
1058. [Kwestia głosowa [battle_break_hysteric_10312_1] — sytuacja] 흐트러질 시 대사 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_break_hysteric_10312_1].desc
   limit: do 120 znaków
   EN: Staggered 2
   PL:
1059. [Kwestia głosowa [battle_break_hysteric_10312_1] (Staggered 2)] 대가를 치를 때인가…?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_break_hysteric_10312_1].dlg
   limit: do 120 znaków
   EN: Is it time to pay the price...?
   PL:
1060. [Kwestia głosowa [battle_kill_10312_1] — sytuacja] 적 처치 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_kill_10312_1].desc
   limit: do 120 znaków
   EN: On Kill 1
   PL:
1061. [Kwestia głosowa [battle_kill_10312_1] (On Kill 1)] 자, 악은 이렇게 정화되었네!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_kill_10312_1].dlg
   limit: do 120 znaków
   EN: Behold, for evil hath been cleansed thus!
   PL:
1062. [Kwestia głosowa [battle_kill_hysteric_10312_1] — sytuacja] 적 처치 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_kill_hysteric_10312_1].desc
   limit: do 120 znaków
   EN: On Kill 2
   PL:
1063. [Kwestia głosowa [battle_kill_hysteric_10312_1] (On Kill 2)] 하하… 이제 평화가… 찾아오면…?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_kill_hysteric_10312_1].dlg
   limit: do 120 znaków
   EN: Ha ha... now peace shall reign, and...?
   PL:
1064. [Kwestia głosowa [battle_dead_10312_1] — sytuacja] 본인 사망 1
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_dead_10312_1].desc
   limit: do 120 znaków
   EN: Death #1
   PL:
1065. [Kwestia głosowa [battle_dead_10312_1] (Death #1)] 끝… 까지. 본인은… 모두를… 지켜…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_dead_10312_1].dlg
   limit: do 120 znaków
   EN: I... swore I would... protect thee all... to the bitter...
   PL:
1066. [Kwestia głosowa [battle_dead_hysteric_10312_1] — sytuacja] 본인 사망 2
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_dead_hysteric_10312_1].desc
   limit: do 120 znaków
   EN: Death #2
   PL:
1067. [Kwestia głosowa [battle_dead_hysteric_10312_1] (Death #2)] 나도 그녀처럼… 결국 지켜내지 못한 거야…
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_dead_hysteric_10312_1].dlg
   limit: do 120 znaków
   EN: I failed to protect them... just like she failed...
   PL:
1068. [Kwestia głosowa [choice_success_p_10312_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=choice_success_p_10312_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1069. [Kwestia głosowa [choice_success_p_10312_2] (Check Passed)] 흠, 해냈네! 다음에도 꼭 본인에게 맡겨주게!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=choice_success_p_10312_2].dlg
   limit: do 120 znaków
   EN: Hm! Handily managed! Prithee, count on mine assistance next time as well!
   PL:
1070. [Kwestia głosowa [choice_fail_n_10312_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=choice_fail_n_10312_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1071. [Kwestia głosowa [choice_fail_n_10312_1] (Check Failed)] …실패했네. 이제, 본인이… 필요치 않아지는가?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=choice_fail_n_10312_1].dlg
   limit: do 120 znaków
   EN: ... I failed. Hast thou no need of me any longer?
   PL:
1072. [Kwestia głosowa [battle_clear_10312_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_clear_10312_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Kwestia głosowa [battle_clear_10312_1] (Victory Cry)] 후훗. 정의, 실현! 자… 이제 경보도 꺼졌으니, 얼른 그 친구에게 돌아가서 이번 제압의 하이롸~이트에 대해 떠들어볼까?
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_clear_10312_1].dlg
   limit: do 180 znaków
   EN: Heh heh, justice, served! Now... I must forthwith make haste and return to her to regale her with the haaaaai-lights of this suppression!
   PL:
1074. [Kwestia głosowa [battle_clear_ex_10312_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_clear_ex_10312_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1075. [Kwestia głosowa [battle_clear_ex_10312_1] (Extra Conditions Fulfilled)] 승리의 보람과 세상의 아름다움에 대해 들어본 적 있는가? 없어도 전혀 상관 없다네! 지금 우리가 보는 경치가… 바로 그런 것일테니.
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_clear_ex_10312_1].dlg
   limit: do 200 znaków
   EN: Dost thou know of the glory of victory and the beauty of the world therein? Nay? All good! For what we behold now, at this very moment... is just that.
   PL:
1076. [Kwestia głosowa [battle_defeat_10312_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_defeat_10312_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1077. [Kwestia głosowa [battle_defeat_10312_1] (Defeat Wail)] 결국… 이렇게 되는 것인가. 나도 똑같아. 제압을 성공하지 못한 나는 쓸모 없는… 으으, 내 머릿 속에서 나가… 이 목소리 좀 멈춰줘…!
   źródło: PersonalityVoiceDlg/Voice_DonQuixote_LEGOMagic_10312.json :: dataList[id=battle_defeat_10312_1].dlg
   limit: do 210 znaków
   EN: So... this is what it hath all come to. I'm just like them. I failed the suppression, I'm a useless— Nngh, get out of my head... The voices, make it stop...!
   PL:
