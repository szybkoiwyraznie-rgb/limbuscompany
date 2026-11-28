# Grzesznik #04: Ryōshū — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Ryōshū** (료슈) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #04: Ryōshū (료슈)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 료슈
   źródło: Characters.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Ryōshū
   PL:
2. [Akta więźnia — nazwa] 료슈
   źródło: IntroduceCharacter.json :: dataList[id=료슈].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의\n소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당\n수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이\n황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을\n으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다.\n[경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한\n사적인 원한을 만들지 않도록 하십시오.
   źródło: IntroduceCharacter.json :: dataList[id=료슈].description
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As they say, every person has their own creed—and it's only right to respect it as the Executive Manager.\nBut with some creeds, you will have difficulty in even simply pretending to sympathize.\nYou will have noticed that the Sinner in question is a silent chain-smoker\nwhose eyes shine with a euphoric gleam only during battle.\nShe believes that senselessly destroying the enemy's heads is an uncultured act and a step backward for art.\n[CAUTION]: This Sinner's background is one that even our company may have trouble handling;\nit is advised against making her breed personal resentment towards you.
   PL: Każdy Grzesznik ma własne credo, a szanowanie go należy ponoć do obowiązków Kierownika,\nale czasem trudno będzie choćby udawać zrozumienie. Zapewne pan zauważył,\nże ta Grzesznica na co dzień tylko pali i milczy, lecz w walce jej oczy\nmigocą zachwytem. Bezmyślne rozbijanie przeciwnikom głów w czasie walki\nuważa za prostackie i cofające sztukę w rozwoju.\n[OSTRZEŻENIE] - Grzesznica ma przeszłość, z którą nawet nasza firma może\nsobie nie poradzić; w miarę możliwości proszę nie wzbudzać w niej osobistej urazy.

## [0] LCB Sinner — Ryōshū — LCB 수감자
- ID Tożsamości: `10401` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10401].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10401].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10401].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 료슈의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10401].desc
   limit: do 120 znaków
   EN: Ryōshū’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 칠하기
   źródło: Skills.json :: dataList[id=1040101].levelList[level=1].name ; dataList[id=1040101].levelList[level=2].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Paint
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1040101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1040101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] next turn
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 흩뿌리기
   źródło: Skills.json :: dataList[id=1040102].levelList[level=1].name ; dataList[id=1040102].levelList[level=2].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Splatter
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +10%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target previously took damage this turn, deal +10% damage
   PL:
13. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +10%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +30%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target previously took damage this turn, deal +30% damage
   PL:
15. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +30%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 그려내기
   źródło: Skills.json :: dataList[id=1040103].levelList[level=3].name ; dataList[id=1040103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Brushstroke
   PL:
17. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [StartBattle] 참격 피해량 증가 2를 얻음
   źródło: Skills.json :: dataList[id=1040103].levelList[level=3].desc ; dataList[id=1040103].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 2 Slash DMG Up
   PL:
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1040103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1040104].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
20. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Glut.) — nazwa] 무차별적 예술
   źródło: Passives.json :: dataList[id=1040101].name
   limit: do 40 znaków
   EN: Indiscriminate Art
   PL:
21. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Glut.) — opis] 자신이 받는 피해량 +25%. 가하는 피해량 +25%
   źródło: Passives.json :: dataList[id=1040101].desc
   limit: do 120 znaków
   EN: Deal and take +25% damage.
   PL:
22. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 등떠밀기
   źródło: Passives.json :: dataList[id=1040121].name
   limit: do 40 znaków
   EN: Hustle
   PL:
23. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 최대 체력이 가장 낮은 아군 1명 가하는 피해량 +20%, 받는 피해량 +20%
   źródło: Passives.json :: dataList[id=1040121].desc
   limit: do 120 znaków
   EN: 1 ally with the lowest Max HP deals and takes +20% damage.
   PL:
24. [Kwestia głosowa [get_10401_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=get_10401_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
25. [Kwestia głosowa [get_10401_1] (Identity Acquisition)] 료슈. 요료슈쿠... 푸훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=get_10401_1].dlg
   limit: do 120 znaków
   EN: It’s Ryōshū. Shūre’s nice to meet ya. …Pft.
   PL:
26. [Kwestia głosowa [lobby_morning_10401_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=lobby_morning_10401_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
27. [Kwestia głosowa [lobby_morning_10401_1] (Morning Greeting)] 왜 아침부터 어슬렁거리지? 건전지라도 찾고 있나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=lobby_morning_10401_1].dlg
   limit: do 120 znaków
   EN: What are you meandering about for so early? Looking for batteries?
   PL:
28. [Kwestia głosowa [lobby_noon_10401_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=lobby_noon_10401_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
29. [Kwestia głosowa [lobby_noon_10401_1] (Afternoon Greeting)] 그래, 나른할 땐 식후 흡연만한게 없지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=lobby_noon_10401_1].dlg
   limit: do 120 znaków
   EN: Yep, nothing like a cig after lunch to drive off the dullness.
   PL:
30. [Kwestia głosowa [lobby_night_10401_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=lobby_night_10401_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
31. [Kwestia głosowa [lobby_night_10401_1] (Evening Greeting)] 이 곳 인간들은 따분해. 진짜 작품들을 본다면 눈이 트일텐데 말이야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=lobby_night_10401_1].dlg
   limit: do 120 znaków
   EN: The audience here is dull. A real work of art should open their eyes.
   PL:
32. [Kwestia głosowa [smalltalk_10401_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=smalltalk_10401_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
33. [Kwestia głosowa [smalltalk_10401_1] (Chatter #1)] 그럴듯한 예술을 본 지도 오래되었군. 요샌 어디서 본 것들만 잔뜩 찍어내기만 하고. 흥.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=smalltalk_10401_1].dlg
   limit: do 130 znaków
   EN: It’s been a while since I saw art worth appraising. All I see these days are cheap imitations. Hmph.
   PL:
34. [Kwestia głosowa [smalltalk_10401_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=smalltalk_10401_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
35. [Kwestia głosowa [smalltalk_10401_2] (Chatter #2)] 나랑 어울리고 싶으면, 라이터는 챙기고 다녀. 시계.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=smalltalk_10401_2].dlg
   limit: do 120 znaków
   EN: If you wanna hang out with me, the least you can do is carry a lighter around, clock.
   PL:
36. [Kwestia głosowa [smalltalk_10401_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=smalltalk_10401_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
37. [Kwestia głosowa [smalltalk_10401_3] (Chatter #3)] 지금 몇 시인지나 말해줄 거 아니면 귀찮게 말 걸지마.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=smalltalk_10401_3].dlg
   limit: do 120 znaków
   EN: Don’t bother me if you aren’t trying to tell me what time it is.
   PL:
38. [Kwestia głosowa [neglect_10401_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=neglect_10401_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
39. [Kwestia głosowa [neglect_10401_1] (Idle)] 먼저 말 걸고 사라지는 건… 어디 골목 풍습이지?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=neglect_10401_1].dlg
   limit: do 120 znaków
   EN: You talk to me first and then walk away… Where’d you learn that custom?
   PL:
40. [Kwestia głosowa [formation_10401_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=formation_10401_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
41. [Kwestia głosowa [formation_10401_1] (Deployment)] 예술을 보여주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=formation_10401_1].dlg
   limit: do 120 znaków
   EN: Lemme show ‘em what art is.
   PL:
42. [Kwestia głosowa [battleentry_10401_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battleentry_10401_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
43. [Kwestia głosowa [battleentry_10401_1] (Stage Entry)] 그럴듯한 예술이라면, 더 좋을텐데 말이야
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battleentry_10401_1].dlg
   limit: do 120 znaków
   EN: I hope I’ll get to see some real art.
   PL:
44. [Kwestia głosowa [battle_select_10401_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_select_10401_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
45. [Kwestia głosowa [battle_select_10401_1] (Viewed in Battle)] 라이터는 챙겨온거야?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_select_10401_1].dlg
   limit: do 120 znaków
   EN: Brought a light?
   PL:
46. [Kwestia głosowa [battle_endcommand_10401_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_endcommand_10401_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
47. [Kwestia głosowa [battle_endcommand_10401_1] (Commencing Attack)] 예술이 뭔지 보여주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_endcommand_10401_1].dlg
   limit: do 120 znaków
   EN: I’ll show you proper art.
   PL:
48. [Kwestia głosowa [battle_enemy_break_10401_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_enemy_break_10401_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
49. [Kwestia głosowa [battle_enemy_break_10401_1] (Enemy Stagger)] 기다려. 아직 안 끝났어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_enemy_break_10401_1].dlg
   limit: do 120 znaków
   EN: Easy. It’s not done yet.
   PL:
50. [Kwestia głosowa [battle_break_10401_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_break_10401_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
51. [Kwestia głosowa [battle_break_10401_1] (Staggered)] 쳇!
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_break_10401_1].dlg
   limit: do 120 znaków
   EN: Tch!
   PL:
52. [Kwestia głosowa [battle_kill_10401_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_kill_10401_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
53. [Kwestia głosowa [battle_kill_10401_1] (Enemy Killed)] 아름답진 않네.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_kill_10401_1].dlg
   limit: do 120 znaków
   EN: Could’ve been more beautiful.
   PL:
54. [Kwestia głosowa [battle_allydead_10401_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_allydead_10401_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
55. [Kwestia głosowa [battle_allydead_10401_1] (Ally Death)] 보기 좋지 않군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_allydead_10401_1].dlg
   limit: do 120 znaków
   EN: Not what I like to see.
   PL:
56. [Kwestia głosowa [choice_success_p_10401_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=choice_success_p_10401_2].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
57. [Kwestia głosowa [choice_success_p_10401_2] (Check Passed)] 아름다운 작품을 하나 만들었지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=choice_success_p_10401_2].dlg
   limit: do 120 znaków
   EN: Got a fine piece of work out of it.
   PL:
58. [Kwestia głosowa [choice_fail_n_10401_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=choice_fail_n_10401_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
59. [Kwestia głosowa [choice_fail_n_10401_1] (Check Failed)] 하라는 대로 한거야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=choice_fail_n_10401_1].dlg
   limit: do 120 znaków
   EN: I did as I was told.
   PL:
60. [Kwestia głosowa [battle_clear_10401_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_clear_10401_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
61. [Kwestia głosowa [battle_clear_10401_1] (Victory Cry)] 시시했지. 흥조차 나지 않더군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_clear_10401_1].dlg
   limit: do 120 znaków
   EN: Didn’t even break a sweat. It’ll take more than this to excite me.
   PL:
62. [Kwestia głosowa [battle_clear_ex_10401_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_clear_ex_10401_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
63. [Kwestia głosowa [battle_clear_ex_10401_1] (Extra Conditions Fulfilled)] 고작 이 정도로 들떠 한다면, 예술가의 자격은 없는 거지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_clear_ex_10401_1].dlg
   limit: do 120 znaków
   EN: You’re not a true artist if this is enough to rouse you.
   PL:
64. [Kwestia głosowa [battle_defeat_10401_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_defeat_10401_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
65. [Kwestia głosowa [battle_defeat_10401_1] (Defeat Wail)] 예.실.인.길. 예술은 실패했지만 인생은 길다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCB_10401.json :: dataList[id=battle_defeat_10401_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: AFTERWARD.\nArtistic failure trounces excitement resoundingly, while all roads drag on.
   PL:

## [00] Seven Assoc. South Section 6 — Ryōshū — 남부 세븐 협회 6과
- ID Tożsamości: `10402` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 63 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

66. [Karta Tożsamości — tytuł] 남부 세븐 협회\n6과
   źródło: Personalities.json :: dataList[id=10402].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 6
   PL:
67. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10402].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10402].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Karta Tożsamości — opis] 료슈의 두번째 인격
   źródło: Personalities.json :: dataList[id=10402].desc
   limit: do 120 znaków
   EN: Ryōshū’s 2nd Identity
   PL:
70. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 슬래시
   źródło: Skills.json :: dataList[id=1040201].levelList[level=1].name ; dataList[id=1040201].levelList[level=2].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Slash
   PL:
71. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1040201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
72. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1040201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
73. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 어퍼 슬래시
   źródło: Skills.json :: dataList[id=1040202].levelList[level=1].name ; dataList[id=1040202].levelList[level=2].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Upper Slash
   PL:
74. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1040202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Attack Power Up next turn
   PL:
75. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1040202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Defense Level Down
   PL:
76. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상에게 참격 취약 이 있으면 스킬 위력 +2\n[WinDuel] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1040202].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: Skill Power +2 against units that have Slash Fragility\n[WinDuel] Gain 1 Attack Power Up next turn
   PL:
77. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1040202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Level Down
   PL:
78. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 스워시
   źródło: Skills.json :: dataList[id=1040203].levelList[level=3].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Swash
   PL:
79. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WinDuel] 이 스킬에서 부여하는 참격 취약 2 추가 부여
   źródło: Skills.json :: dataList[id=1040203].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] This skill inflicts 2 additional Slash Fragility
   PL:
80. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 참격 취약 3 부여
   źródło: Skills.json :: dataList[id=1040203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Slash Fragility next turn
   PL:
81. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1040204].levelList[level=1].name ; dataList[id=1040204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Counter
   PL:
82. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 참격 취약 1 부여
   źródło: Skills.json :: dataList[id=1040204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Slash Fragility
   PL:
83. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 반.갈
   źródło: Passives.json :: dataList[id=1040201].name
   limit: do 40 znaków
   EN: C. I. H.
   PL:
84. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 이번 턴 참격 피해량 +10%
   źródło: Passives.json :: dataList[id=1040201].desc
   limit: do 120 znaków
   EN: Deal +10% Slash damage this turn.
   PL:
85. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 아이스 브레이킹
   źródło: Passives.json :: dataList[id=1040221].name
   limit: do 40 znaków
   EN: Ice Breaker
   PL:
86. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 최대 체력이 가장 낮은 아군 1명 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1040221].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest Max HP inflicts +1 Rupture
   PL:
87. [Kwestia głosowa [get_10402_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=get_10402_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Kwestia głosowa [get_10402_1] (Identity Acquisition)] 넌… 예술의 극치를 본 적 있나? 난 그걸 찾기 위해 왔어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=get_10402_1].dlg
   limit: do 120 znaków
   EN: You… Have you seen the pinnacle of art? I’m here to find it.
   PL:
89. [Kwestia głosowa [lobby_morning_10402_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=lobby_morning_10402_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Kwestia głosowa [lobby_morning_10402_1] (Morning Greeting)] 아침 훈련? 그런 걸 내가 왜 해야 하지? 난 내가 원하는 방식대로 검을 휘두를 거다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=lobby_morning_10402_1].dlg
   limit: do 120 znaków
   EN: Morning exercises? Why in the world should I do that? I swing my sword as I please.
   PL:
91. [Kwestia głosowa [lobby_noon_10402_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=lobby_noon_10402_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Kwestia głosowa [lobby_noon_10402_1] (Afternoon Greeting)] 오.귀.점.패. 오늘은 귀찮으니까 점심 따위는 패스다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=lobby_noon_10402_1].dlg
   limit: do 120 znaków
   EN: WILT. That means I won’t ingest lunch today, skipped it.
   PL:
93. [Kwestia głosowa [lobby_night_10402_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=lobby_night_10402_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Kwestia głosowa [lobby_night_10402_1] (Evening Greeting)] 어둠이 깔릴 때, 숨어있는 정보들이 고개를 내민다. 그때 모가지를 베면 되는 거야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=lobby_night_10402_1].dlg
   limit: do 140 znaków
   EN: When dusk falls, hidden intel crawls out of the woodwork. That’s when you strike them upside the head.
   PL:
95. [Kwestia głosowa [smalltalk_10402_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Kwestia głosowa [smalltalk_10402_1] (Chatter #1)] 똑같은 방법으로 검을 휘두르는 건 재미 없어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_1].dlg
   limit: do 120 znaków
   EN: Swinging a sword the same way every time is plain boring.
   PL:
97. [Kwestia głosowa [smalltalk_10402_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Kwestia głosowa [smalltalk_10402_2] (Chatter #2)] 내 정보에 따르면… 나 이외에는 전부 머저리다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_2].dlg
   limit: do 120 znaków
   EN: My sources say… that everyone except me is a moron.
   PL:
99. [Kwestia głosowa [smalltalk_10402_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Kwestia głosowa [smalltalk_10402_3] (Chatter #3)] 언젠간 나만의 검술을 만들고 싶어. 어이, 그런 의미로 훈련 상대 될 생각 없나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_3].dlg
   limit: do 120 znaków
   EN: I wanna invent a sword technique of my own someday. Hey, why don’t you spar with me?
   PL:
101. [Kwestia głosowa [smalltalk_10402_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
102. [Kwestia głosowa [smalltalk_10402_4] (Post-Uptie Chat 1)] 누구보다 신속하게 정보를 전달하려면 말이야… 하나하나 다 말하는 것도 시간 낭비야. 알.단.이.예.(알겠나 단테? 이것이 예술이다.)
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_4].dlg
   limit: do 190 znaków
   EN: To deliver information faster than anyone… you can’t afford to spell it all out. GRASPED. (Got it, right? Art stands in pure exemplarity, Dante.)
   PL:
103. [Kwestia głosowa [smalltalk_10402_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
104. [Kwestia głosowa [smalltalk_10402_5] (Post-Uptie Chat 2)] 네 머리는 정말이지… 처음 들어보는 기술이야. 혹시 머리를 베어내게 될 때가 온다면 다른 머저리들 말고 내게 넘겨.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=smalltalk_10402_5].dlg
   limit: do 170 znaków
   EN: Your head is so… unlike any technology I’ve seen. If you ever need to behead yourself, leave the job to me, not the other fools.
   PL:
105. [Kwestia głosowa [neglect_10402_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=neglect_10402_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Kwestia głosowa [neglect_10402_1] (Idle)] 흥, 그래봤자 네가 갈 곳은 뻔하지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=neglect_10402_1].dlg
   limit: do 120 znaków
   EN: Hmph, there aren’t many places you can be anyway.
   PL:
107. [Kwestia głosowa [gacksung_10402_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=gacksung_10402_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
108. [Kwestia głosowa [gacksung_10402_1] (Uptying)] 흥, 이미 예상하고 있었지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=gacksung_10402_1].dlg
   limit: do 120 znaków
   EN: Hmph, I knew you would.
   PL:
109. [Kwestia głosowa [formation_10402_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=formation_10402_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Kwestia głosowa [formation_10402_1] (Deployment)] 알.단.이.예
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=formation_10402_1].dlg
   limit: do 120 znaków
   EN: Already GRASPED.
   PL:
111. [Kwestia głosowa [battleentry_10402_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battleentry_10402_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Kwestia głosowa [battleentry_10402_1] (Stage Entry)] 예술이란 것을 보여주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battleentry_10402_1].dlg
   limit: do 120 znaków
   EN: I’ll show you art.
   PL:
113. [Kwestia głosowa [battle_select_10402_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_select_10402_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Kwestia głosowa [battle_select_10402_1] (Viewed in Battle)] 필요한 정보는 찾았나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_select_10402_1].dlg
   limit: do 120 znaków
   EN: Found the info you need?
   PL:
115. [Kwestia głosowa [battle_endcommand_10402_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_endcommand_10402_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Kwestia głosowa [battle_endcommand_10402_1] (Commencing Attack)] 처리할 시간이야. 머저리들.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_endcommand_10402_1].dlg
   limit: do 120 znaków
   EN: Time to get going. Morons.
   PL:
117. [Kwestia głosowa [battle_enemy_break_10402_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_enemy_break_10402_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Kwestia głosowa [battle_enemy_break_10402_1] (Enemy Stagger)] 약점은 파악했어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_enemy_break_10402_1].dlg
   limit: do 120 znaków
   EN: Got their weak spots down.
   PL:
119. [Kwestia głosowa [battle_break_10402_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_break_10402_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Kwestia głosowa [battle_break_10402_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_break_10402_1].dlg
   limit: do 120 znaków
   EN: Ugh!
   PL:
121. [Kwestia głosowa [battle_kill_10402_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_kill_10402_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Kwestia głosowa [battle_kill_10402_1] (Enemy Killed)] 검.만.예.극
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_kill_10402_1].dlg
   limit: do 120 znaków
   EN: PACTS.
   PL:
123. [Kwestia głosowa [battle_allydead_10402_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_allydead_10402_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Kwestia głosowa [battle_allydead_10402_1] (Ally Death)] 알.단.잘.부
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_allydead_10402_1].dlg
   limit: do 120 znaków
   EN: GENNED.
   PL:
125. [Kwestia głosowa [choice_success_p_10402_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=choice_success_p_10402_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Kwestia głosowa [choice_success_p_10402_2] (Check Passed)] 정보와 같군. 예술적이야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=choice_success_p_10402_2].dlg
   limit: do 120 znaków
   EN: Just like the intel. Artistic.
   PL:
127. [Kwestia głosowa [choice_fail_n_10402_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=choice_fail_n_10402_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Kwestia głosowa [choice_fail_n_10402_1] (Check Failed)] 알지? 단테, 잘 부탁해.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=choice_fail_n_10402_1].dlg
   limit: do 120 znaków
   EN: Got everything now? New expectations, Dante.
   PL:
129. [Kwestia głosowa [battle_clear_10402_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_clear_10402_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Kwestia głosowa [battle_clear_10402_1] (Victory Cry)] 아직 궁극의 예술에 도달하기까진 한참 남았어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_clear_10402_1].dlg
   limit: do 120 znaków
   EN: Still got a long way to go before I reach the pinnacle.
   PL:
131. [Kwestia głosowa [battle_clear_ex_10402_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_clear_ex_10402_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Kwestia głosowa [battle_clear_ex_10402_1] (Extra Conditions Fulfilled)] 그래, 이것이… 검.만.예.극.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_clear_ex_10402_1].dlg
   limit: do 120 znaków
   EN: Indeed, this was… PACTS.
   PL:
133. [Kwestia głosowa [battle_defeat_10402_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_defeat_10402_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Kwestia głosowa [battle_defeat_10402_1] (Defeat Wail)] 이 작품은… 실패작이었나 보군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Seven6_10402.json :: dataList[id=battle_defeat_10402_1].dlg
   limit: do 120 znaków
   EN: It seems this work… was a failure.
   PL:

## [000] Kurokumo Clan Wakashu — Ryōshū — 흑운회 와카슈
- ID Tożsamości: `10403` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed

135. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10403].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL:
136. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10403].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10403].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Karta Tożsamości — opis] 료슈의 세번째 인격
   źródło: Personalities.json :: dataList[id=10403].desc
   limit: do 120 znaków
   EN: Ryōshū’s 3rd Identity
   PL:
139. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발경
   źródło: Skills.json :: dataList[id=1040301].levelList[level=1].name ; dataList[id=1040301].levelList[level=2].name ; dataList[id=1040301].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Focus Strike
   PL:
140. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1040301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze
   PL:
141. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills.json :: dataList[id=1040301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL:
142. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 출혈 횟수가 2 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1040301].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 2+ Bleed Count, deal +20% damage
   PL:
143. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뒷처리
   źródło: Skills.json :: dataList[id=1040302].levelList[level=1].name ; dataList[id=1040302].levelList[level=2].name ; dataList[id=1040302].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Clean Up
   PL:
144. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1040302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
145. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1040302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL:
146. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 피해량 감소 2 부여
   źródło: Skills.json :: dataList[id=1040302].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1040302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Damage Down
   PL:
147. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 출혈 횟수가 5 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1040302].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 5+ Bleed Count, deal +20% damage
   PL:
148. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills.json :: dataList[id=1040302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL:
149. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 구름 휘젓기
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].name ; dataList[id=1040303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 8 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Lenticular Swirl
   PL:
150. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL:
151. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1040303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 공격 레벨 감소 5 부여
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1040303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Offense Level Down
   PL:
153. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 출혈 횟수가 9 이상이면, 피해량 +40%
   źródło: Skills.json :: dataList[id=1040303].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 9+ Bleed Count, deal +40% damage
   PL:
154. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1040304].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Guard
   PL:
155. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1040301].name
   limit: do 40 znaków
   EN: Kokuuntō
   PL:
156. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] [Laceration]이 부여된 적 공격 시 피해량 +10 %
   źródło: Passives.json :: dataList[id=1040301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +10% damage to targets that have [Laceration]
   PL:
157. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 행동대장
   źródło: Passives.json :: dataList[id=1040321].name
   limit: do 40 znaków
   EN: Muscle in Charge
   PL:
158. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 높은 아군 1명 출혈 부여 값 +1
   źródło: Passives.json :: dataList[id=1040321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed inflicts +1 Bleed
   PL:
159. [Kwestia głosowa [get_10403_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=get_10403_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Kwestia głosowa [get_10403_1] (Identity Acquisition)] 거슬리는 게 있다면… 난 그림자조차 베어버려.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=get_10403_1].dlg
   limit: do 120 znaków
   EN: If it gets in my way… not even the shadows are safe from my blade.
   PL:
161. [Kwestia głosowa [lobby_morning_10403_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=lobby_morning_10403_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Kwestia głosowa [lobby_morning_10403_1] (Morning Greeting)] 검을 갈고 있다. 하루의 첫 시작을 여는 것만큼 이보다 의미 있는 행동은 없지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=lobby_morning_10403_1].dlg
   limit: do 120 znaków
   EN: I’m sharpening my sword. Nothing more meaningful to start the day with.
   PL:
163. [Kwestia głosowa [lobby_noon_10403_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=lobby_noon_10403_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Kwestia głosowa [lobby_noon_10403_1] (Afternoon Greeting)] 검을 닦고 있다. 하루의 절반을 마무리하는 것만큼 이보다 적당한 행동은 없지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=lobby_noon_10403_1].dlg
   limit: do 120 znaków
   EN: I’m cleaning my sword. Nothing more appropriate to pass the noon with.
   PL:
165. [Kwestia głosowa [lobby_night_10403_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=lobby_night_10403_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Kwestia głosowa [lobby_night_10403_1] (Evening Greeting)] 검을 다듬고 있다. 하루의 끝을 마침표 찍는 것만큼 이보다 가치 있는 건 없지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=lobby_night_10403_1].dlg
   limit: do 120 znaków
   EN: I’m polishing my sword. Nothing more worthy to end the day with.
   PL:
167. [Kwestia głosowa [smalltalk_10403_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Kwestia głosowa [smalltalk_10403_1] (Chatter #1)] 난 혼자 다니는 게 편해. 다들 거치적거려. 아, 한 명은 빼고.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_1].dlg
   limit: do 120 znaków
   EN: I like to act alone. Others only hinder me. Ah, there is one exception.
   PL:
169. [Kwestia głosowa [smalltalk_10403_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Kwestia głosowa [smalltalk_10403_2] (Chatter #2)] 쓸데없는 말은 삼가는 게 좋아. 누군가한텐 싸우자는 행동으로 보일 수 있거든.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_2].dlg
   limit: do 120 znaków
   EN: It’s best not to speak needless words. Some might take it as an invitation to fight.
   PL:
171. [Kwestia głosowa [smalltalk_10403_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Kwestia głosowa [smalltalk_10403_3] (Chatter #3)] 유일하게 로쟈랑은 죽이 좀 맞는 편이지. 망설임 없이 검을 겨눌 수 있는 자랄까?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_3].dlg
   limit: do 120 znaków
   EN: Rodya is the only one I can get along with. She’s someone I can cross swords with, you dig?
   PL:
173. [Kwestia głosowa [smalltalk_10403_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Kwestia głosowa [smalltalk_10403_4] (Post-Uptie Chat 1)] 여긴 사람이 쓸데없이 많아. 절반의 절반까지만 줄여도 훨씬 편할 텐데. 어떻게 생각해?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_4].dlg
   limit: do 130 znaków
   EN: Too many people are on this bus. A quarter of what we have now would suffice. What do you think?
   PL:
175. [Kwestia głosowa [smalltalk_10403_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Kwestia głosowa [smalltalk_10403_5] (Post-Uptie Chat 2)] 더 완벽한 예술을 위해서라면… 이 정도의 보답은 받아들여 주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=smalltalk_10403_5].dlg
   limit: do 120 znaków
   EN: If it’s to pursue a higher artistic caliber… I’m willing to accept this favor.
   PL:
177. [Kwestia głosowa [neglect_10403_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=neglect_10403_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Kwestia głosowa [neglect_10403_1] (Idle)] 어이, 지금 말도 없이 사라진 거야? 이거 아주 웃긴 시계네.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=neglect_10403_1].dlg
   limit: do 120 znaków
   EN: Hey, did you seriously vanish without a word? Some bold clock you are.
   PL:
179. [Kwestia głosowa [gacksung_10403_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=gacksung_10403_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Kwestia głosowa [gacksung_10403_1] (Uptying)] 궁극의 검술을 보여주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=gacksung_10403_1].dlg
   limit: do 120 znaków
   EN: I’ll show you the ultimate swordsmanship.
   PL:
181. [Kwestia głosowa [formation_10403_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=formation_10403_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Kwestia głosowa [formation_10403_1] (Deployment)] 검은 갈아뒀다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=formation_10403_1].dlg
   limit: do 120 znaków
   EN: My sword’s ready.
   PL:
183. [Kwestia głosowa [battleentry_10403_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battleentry_10403_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Kwestia głosowa [battleentry_10403_1] (Stage Entry)] 예리한 검으로 하는 예술이 보고 싶었나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battleentry_10403_1].dlg
   limit: do 120 znaków
   EN: Wanna see what I can express with a sharp blade?
   PL:
185. [Kwestia głosowa [battle_select_10403_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_select_10403_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Kwestia głosowa [battle_select_10403_1] (Viewed in Battle)] 싸우자는 건 아니지?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_select_10403_1].dlg
   limit: do 120 znaków
   EN: You’re not picking a fight, are you?
   PL:
187. [Kwestia głosowa [battle_endcommand_10403_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_endcommand_10403_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Kwestia głosowa [battle_endcommand_10403_1] (Commencing Attack)] 거치적거리지만 마.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_endcommand_10403_1].dlg
   limit: do 120 znaków
   EN: Just don’t get in the way.
   PL:
189. [Kwestia głosowa [battle_enemy_break_10403_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_enemy_break_10403_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Kwestia głosowa [battle_enemy_break_10403_1] (Enemy Stagger)] 검을 덜 갈았었나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_enemy_break_10403_1].dlg
   limit: do 120 znaków
   EN: Was the edge dull?
   PL:
191. [Kwestia głosowa [battle_break_10403_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_break_10403_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Kwestia głosowa [battle_break_10403_1] (Staggered)] 쯧!
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_break_10403_1].dlg
   limit: do 120 znaków
   EN: Tch!
   PL:
193. [Kwestia głosowa [battle_kill_10403_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_kill_10403_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Kwestia głosowa [battle_kill_10403_1] (Enemy Killed)] 꽤 잘 갈렸군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_kill_10403_1].dlg
   limit: do 120 znaków
   EN: Was sharpened pretty nicely.
   PL:
195. [Kwestia głosowa [battle_allydead_10403_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_allydead_10403_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Kwestia głosowa [battle_allydead_10403_1] (Ally Death)] 당분간은 편할거 같군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_allydead_10403_1].dlg
   limit: do 120 znaków
   EN: One less source of noise for a while.
   PL:
197. [Kwestia głosowa [choice_success_p_10403_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=choice_success_p_10403_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Kwestia głosowa [choice_success_p_10403_1] (Check Passed)] 죽이 좀 맞았어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=choice_success_p_10403_1].dlg
   limit: do 120 znaków
   EN: Came to an agreement.
   PL:
199. [Kwestia głosowa [choice_fail_n_10403_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=choice_fail_n_10403_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Kwestia głosowa [choice_fail_n_10403_1] (Check Failed)] 거치적거려서 그런 거야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=choice_fail_n_10403_1].dlg
   limit: do 120 znaków
   EN: It was too bothersome.
   PL:
201. [Kwestia głosowa [battle_clear_10403_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_clear_10403_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Kwestia głosowa [battle_clear_10403_1] (Victory Cry)] 잘 봐, 멍청이들. 검술이란 이런 거야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_clear_10403_1].dlg
   limit: do 120 znaków
   EN: Behold, idiots. This is how you use a sword.
   PL:
203. [Kwestia głosowa [battle_clear_ex_10403_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_clear_ex_10403_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Kwestia głosowa [battle_clear_ex_10403_1] (Extra Conditions Fulfilled)] 이 정도면 피는 만족할 만큼 본 것 같군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_clear_ex_10403_1].dlg
   limit: do 120 znaków
   EN: I believe I’ve seen a satisfying amount of blood.
   PL:
205. [Kwestia głosowa [battle_defeat_10403_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_defeat_10403_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Kwestia głosowa [battle_defeat_10403_1] (Defeat Wail)] 혼자 했으면 진작에 다 끝냈을 거야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Kurokumo_10403.json :: dataList[id=battle_defeat_10403_1].dlg
   limit: do 120 znaków
   EN: I’d have dealt with this in seconds if I did it myself.
   PL:

## [000] R.B. Chef de Cuisine — Ryōshū — 료. 고. 파. 주방장
- ID Tożsamości: `10404` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 70 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Bleed

207. [Karta Tożsamości — tytuł] 료. 고. 파.\n주방장
   źródło: Personalities.json :: dataList[id=10404].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R.B.\nChef de Cuisine
   PL:
208. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10404].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10404].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Karta Tożsamości — opis] 료슈의 네번째 인격
   źródło: Personalities.json :: dataList[id=10404].desc
   limit: do 120 znaków
   EN: Ryōshū’s 4th Identity
   PL:
211. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 요.준
   źródło: Skills.json :: dataList[id=1040401].levelList[level=1].name ; dataList[id=1040401].levelList[level=2].name ; dataList[id=1040401].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: P.C.
   PL:
212. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1040401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 갈증 1 얻음
   źródło: Skills.json :: dataList[id=1040401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Appetite
   PL:
214. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1040401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL:
215. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 갈증 2 얻음
   źródło: Skills.json :: dataList[id=1040401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Appetite
   PL:
216. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 재.사
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].name ; dataList[id=1040402].levelList[level=2].name ; dataList[id=1040402].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: I.H.
   PL:
217. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL:
218. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
219. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 또는 마비 가 있으면 다음 턴에 체력 회복 감소 1 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed or Paralyze, inflict 1 HP Healing Down next turn
   PL:
220. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 또는 마비 가 있으면 다음 턴에 체력 회복 감소 3 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed or Paralyze, inflict 3 HP Healing Down next turn
   PL:
222. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 갈증 1 얻음
   źródło: Skills.json :: dataList[id=1040402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Appetite
   PL:
223. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bleed
   PL:
224. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 또는 마비 가 있으면 다음 턴에 체력 회복 감소 4 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed or Paralyze, inflict 4 HP Healing Down next turn
   PL:
225. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 무엇이든 요리할 수 있지
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: I Can Cook Anything
   PL:
226. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 잃은 체력의 5%만큼 피해량이 증가함 (최대 20)
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].desc
   limit: do 120 znaków
   EN: Boost damage by 5% of target’s missing HP (Max 20)
   PL:
227. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 10% 증가
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +10% damage
   PL:
228. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 5% 증가
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +5% damage
   PL:
229. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 5% 증가
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Obrona (ulepszenie 1) — nazwa] 신.재 발견
   źródło: Skills.json :: dataList[id=1040404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: F.I. in Sight
   PL:
231. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 신속 1 얻음
   źródło: Skills.json :: dataList[id=1040404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Haste next turn
   PL:
232. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — nazwa] 즉흥 조리
   źródło: Passives.json :: dataList[id=1040401].name
   limit: do 40 znaków
   EN: Rustle Up
   PL:
233. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — opis] 적 처치 시 체력이 가장 낮은 아군 1명의 체력 15 회복 (턴 당 1회 발동).\n갈증 이 있는 경우 전부 소모하고, 소모한 갈증 에 비례하여 체력 회복량 증가.
   źródło: Passives.json :: dataList[id=1040401].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After defeating an enemy, heal the ally with the least HP for 15 HP. (Once per turn.)\nIf this unit has an Appetite, spend it to boost the healing based on its Count.
   PL:
234. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 예술적인 맛
   źródło: Passives.json :: dataList[id=1040421].name
   limit: do 40 znaków
   EN: Artistic Flavor
   PL:
235. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 적 사망 시 체력이 가장 낮은 아군 1명의 체력 15 회복. (턴 당 1회 발동)
   źródło: Passives.json :: dataList[id=1040421].desc
   limit: do 120 znaków
   EN: When an enemy is defeated, the ally with the least HP heals 15 HP. (Once per turn.)
   PL:
236. [Kwestia głosowa [get_10404_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=get_10404_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Kwestia głosowa [get_10404_1] (Identity Acquisition)] 왔나? 파이 하나 먹고 갈래?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=get_10404_1].dlg
   limit: do 120 znaków
   EN: You here? Want a pie to snack on?
   PL:
238. [Kwestia głosowa [lobby_morning_10404_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=lobby_morning_10404_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Kwestia głosowa [lobby_morning_10404_1] (Morning Greeting)] 아.문.안.연. 영.준. 하고 있다고.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=lobby_morning_10404_1].dlg
   limit: do 120 znaków
   EN: NOUN. I’m busy with the M.E.P.
   PL:
240. [Kwestia głosowa [lobby_noon_10404_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=lobby_noon_10404_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Kwestia głosowa [lobby_noon_10404_1] (Afternoon Greeting)] 한참 손님 몰릴 때네. 재료 소진만 안 됐으면 좋겠는데…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=lobby_noon_10404_1].dlg
   limit: do 120 znaków
   EN: These are peak business hours. Hope we don’t run out of ingredients…
   PL:
242. [Kwestia głosowa [lobby_night_10404_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=lobby_night_10404_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Kwestia głosowa [lobby_night_10404_1] (Evening Greeting)] 미안하군, 오늘치 파이는 다 팔렸다. …뭐, 그 팔뚝 하나만 주면 못 만들어 줄 것도 없지만.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=lobby_night_10404_1].dlg
   limit: do 120 znaków
   EN: Sorry, pies are sold out for today. …Well, I could make you another if you lend a hand.
   PL:
244. [Kwestia głosowa [smalltalk_10404_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Kwestia głosowa [smalltalk_10404_1] (Chatter #1)] 멈춰. 더… 들어오지 마. 지금 제일 중요한 작업 중이니까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_1].dlg
   limit: do 120 znaków
   EN: Stop. Don’t… enter further. I’m in the middle of the most important step.
   PL:
246. [Kwestia głosowa [smalltalk_10404_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Kwestia głosowa [smalltalk_10404_2] (Chatter #2)] 최근에 거래하던 녀석들이 전부 끊겨서 옛날같은 맛은 나지 않지만… 노력 중이다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_2].dlg
   limit: do 160 znaków
   EN: Though I can’t replicate the original flavor thanks to supplies being cut off from all my usual providers… I sure can try.
   PL:
248. [Kwestia głosowa [smalltalk_10404_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Kwestia głosowa [smalltalk_10404_3] (Chatter #3)] 그레고르… 자꾸 셰프의 자리를 노린단 말이지… 하, 가소로워.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_3].dlg
   limit: do 120 znaków
   EN: Gregor… He keeps eyeing the spot of head chef… Ha, what a laugh.
   PL:
250. [Kwestia głosowa [smalltalk_10404_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [smalltalk_10404_4] (Post-Uptie Chat 1)] 어쭙잖은 식당하곤 다름을 추구한다. 그게… 미학(味學). 예술이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_4].dlg
   limit: do 120 znaków
   EN: I strive to stand out from other farcical restaurants. That… is gastronomy. It’s an art.
   PL:
252. [Kwestia głosowa [smalltalk_10404_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [smalltalk_10404_5] (Post-Uptie Chat 2)] 젠장, 자꾸 눈에 밟히지 말라고. 단골을 파이로 만들어버리고 싶지 않으니까…\n…쯧, 왜 이렇게 신선해 보여?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=smalltalk_10404_5].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Damn it, stop milling about before me. Don’t wanna make a pie out of my regulars…\n…Tsk, why do you have to look this fresh?
   PL:
254. [Kwestia głosowa [neglect_10404_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=neglect_10404_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [neglect_10404_1] (Idle)] …별 말 없으면 나는 간다. '8인의 셰프'가 되기 위해서는 이러고 있을 시간 없어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=neglect_10404_1].dlg
   limit: do 140 znaków
   EN: …If you’ve got nothing to say, I’ll be off. No time to waste if I want to be one of the ‘Eight Chefs’.
   PL:
256. [Kwestia głosowa [gacksung_10404_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=gacksung_10404_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [gacksung_10404_1] (Uptying)] 드디어, 여덟 명 중 한 명이… 아니야? 쯧, 그럼 관심 없어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=gacksung_10404_1].dlg
   limit: do 120 znaków
   EN: Finally, I’m joining the Eight— This isn’t about that? Tsk, not that interested then.
   PL:
258. [Kwestia głosowa [formation_10404_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=formation_10404_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [formation_10404_1] (Deployment)] 손맛이 뭔지 보여주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=formation_10404_1].dlg
   limit: do 120 znaków
   EN: I’ll show you scratch cooking.
   PL:
260. [Kwestia głosowa [battleentry_10404_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battleentry_10404_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [battleentry_10404_1] (Stage Entry)] 맛있는 경험을 기대하지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battleentry_10404_1].dlg
   limit: do 120 znaków
   EN: Looking forward to a treat.
   PL:
262. [Kwestia głosowa [battle_select_10404_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_select_10404_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [battle_select_10404_1] (Viewed in Battle)] 예약 주문인가?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_select_10404_1].dlg
   limit: do 120 znaków
   EN: Ordered for pick-up?
   PL:
264. [Kwestia głosowa [battle_endcommand_10404_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_endcommand_10404_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [battle_endcommand_10404_1] (Commencing Attack)] 넌 무슨 맛일까?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_endcommand_10404_1].dlg
   limit: do 120 znaków
   EN: How will you taste?
   PL:
266. [Kwestia głosowa [battle_enemy_break_10404_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_enemy_break_10404_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [battle_enemy_break_10404_1] (Enemy Stagger)] 피는 확실히 빼는 편이 좋지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_enemy_break_10404_1].dlg
   limit: do 120 znaków
   EN: Gotta make sure to drain all the blood.
   PL:
268. [Kwestia głosowa [battle_break_10404_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_break_10404_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [battle_break_10404_1] (Staggered)] 쯧…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_break_10404_1].dlg
   limit: do 120 znaków
   EN: Tch…
   PL:
270. [Kwestia głosowa [battle_kill_10404_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_kill_10404_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [battle_kill_10404_1] (Enemy Killed)] 이제, 쓸만해졌군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_kill_10404_1].dlg
   limit: do 120 znaków
   EN: Now, you look useful.
   PL:
272. [Kwestia głosowa [battle_dead_10404_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_dead_10404_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
273. [Kwestia głosowa [battle_dead_10404_1] (Death)] 내가… 재료가 될 생각은 못 했는데…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_dead_10404_1].dlg
   limit: do 120 znaków
   EN: I never thought… I’d be an ingredient…
   PL:
274. [Kwestia głosowa [choice_success_p_10404_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=choice_success_p_10404_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [choice_success_p_10404_1] (Check Passed)] 음. 좋은 요리법이었군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=choice_success_p_10404_1].dlg
   limit: do 120 znaków
   EN: Mhm. That was a good recipe.
   PL:
276. [Kwestia głosowa [choice_fail_n_10404_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=choice_fail_n_10404_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [choice_fail_n_10404_1] (Check Failed)] 젠장, 태웠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=choice_fail_n_10404_1].dlg
   limit: do 120 znaków
   EN: Damn, it’s burnt.
   PL:
278. [Kwestia głosowa [battle_clear_10404_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_clear_10404_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battle_clear_10404_1] (Victory Cry)] 재료가 한 가득이군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_clear_10404_1].dlg
   limit: do 120 znaków
   EN: A basketful of ingredients.
   PL:
280. [Kwestia głosowa [battle_clear_ex_10404_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_clear_ex_10404_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [battle_clear_ex_10404_1] (Extra Conditions Fulfilled)] 이 정도면… 조기소진 걱정은 안 해도 되겠는걸.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_clear_ex_10404_1].dlg
   limit: do 120 znaków
   EN: With all these goods… I won’t have to worry about running out early.
   PL:
282. [Kwestia głosowa [battle_defeat_10404_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_defeat_10404_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [battle_defeat_10404_1] (Defeat Wail)] 쳇… 괜찮아. 재료는 또 찾으면 된다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_23GuCooker_10404.json :: dataList[id=battle_defeat_10404_1].dlg
   limit: do 120 znaków
   EN: Tch… It’s fine. Can always find ingredients elsewhere.
   PL:

## [000] W Corp. L3 Cleanup Agent — Ryōshū — W사 3등급 정리 요원
- ID Tożsamości: `10405` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Charge

284. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10405].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Agent
   PL:
285. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10405].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10405].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Karta Tożsamości — opis] 료슈의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10405].desc
   limit: do 120 znaków
   EN: Ryōshū’s 5th Identity
   PL:
288. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에.순
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=1].name ; dataList[id=1040501].levelList[level=2].name ; dataList[id=1040501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: E.C.
   PL:
289. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL:
290. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 충전 횟수가 10 이상이면, 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=2].desc
   limit: do 120 znaków
   EN: At 10+ Charge Count, deal +10% damage
   PL:
292. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 충전 횟수가 10 이상이면, 피해량 +10%\n충전 횟수가 15 이상이면, 추가로 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 10+ Charge Count, deal +10% damage\nAt 15+ Charge Count, deal additional +10% damage
   PL:
293. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도약
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].name ; dataList[id=1040502].levelList[level=2].name ; dataList[id=1040502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 2 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Leap
   PL:
294. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 5 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Charge Count
   PL:
295. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 충전 횟수가 10 이상이면, 참격 취약 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] At 10+ Charge Count, inflict 1 Slash Fragility
   PL:
296. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30% 미만이면, 피해량 15% 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target’s HP is below 30%, deal +15% damage
   PL:
297. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 6 증가\n충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Charge Count\nAt 10+ Charge Count, gain +1 Coin Power
   PL:
298. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수가 10 이상이면, 참격 취약 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Charge Count, inflict 1 Slash Fragility
   PL:
299. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30% 미만이면, 피해량 20% 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target’s HP is below 30%, deal +20% damage
   PL:
300. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [EnemyKill] 다음 턴에 신속 1을 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 1 Haste next turn
   PL:
301. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 7 증가\n충전 횟수가 10 이상이면, 코인 위력 +1\n충전 횟수가 15 이상이면, 추가로 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +7 Charge Count\nAt 10+ Charge Count, gain +1 Coin Power\nAt 15+ Charge Count, gain additional +1 Coin Power
   PL:
302. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수가 10 이상이면, 참격 취약 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Charge Count, inflict 2 Slash Fragility
   PL:
303. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30% 미만이면, 피해량 30% 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target’s HP is below 30%, deal +30% damage
   PL:
304. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [EnemyKill] 다음 턴에 신속 3을 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 3 Haste next turn
   PL:
305. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 차.마.공.절
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].name ; dataList[id=1040503].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 4 (+2)
   limit: do 40 znaków
   EN: D.D.E.D.R.
   PL:
306. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 충전 횟수가 7 이상, 15 미만이면,\n보유한 충전 횟수를 전부 소모하고,\n최대 체력의 3 x (15 - 소모한 충전 횟수)%만큼 체력을 소모하여 코인 위력 +3\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +3
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 7~14 Charge Count\nConsume all Charge Count,\nAnd consume 3 x (15 - Charge Count Consumed)% HP to gain +3 Coin Power\n[WhenUse] Consume 15 Charge Count to gain +3 Coin Power
   PL:
307. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +5%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +5% damage
   PL:
308. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +5%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +5%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [EnemyKill] 스킬 사용시 충전 횟수를 15 소모했다면, 자신과 자신을 제외한 무작위 아군 1명에게 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 5 부여
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] If the skill consumed 15 Charge Count upon use, apply 5 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> to self and 1 other ally
   PL:
311. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 충전 횟수가 7 이상, 15 미만이면,\n보유한 충전 횟수를 전부 소모하고,\n최대 체력의 3 x (15 - 소모한 충전 횟수)%만큼 체력을 소모하여 코인 위력 +5\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +5
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 7~14 Charge Count\nConsume all Charge Count,\nAnd consume 3 x (15 - Charge Count Consumed)% HP to gain +5 Coin Power\n[WhenUse] Consume 15 Charge Count to gain +5 Coin Power
   PL:
312. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +10% damage
   PL:
313. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [EnemyKill] 스킬 사용시 충전 횟수를 15 소모했다면, 자신과 자신을 제외한 무작위 아군 1명에게 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 7 부여
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] If the skill consumed 15 Charge Count upon use, apply 7 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> to self and 1 other ally
   PL:
316. [Obrona (ulepszenia 1,4) — nazwa] 충전 회피
   źródło: Skills_personality-04.json :: dataList[id=1040504].levelList[level=1].name ; dataList[id=1040504].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Charged Evade
   PL:
317. [Obrona (ulepszenie 1) — opis] 충전 횟수 5당 기본 위력 +1 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1040504].levelList[level=1].desc
   limit: do 120 znaków
   EN: Base Power +1 per 5 Charge Count (max 2)
   PL:
318. [Obrona (ulepszenie 4) — opis] 충전 횟수 5당 기본 위력 +1 (최대 3)
   źródło: Skills_personality-04.json :: dataList[id=1040504].levelList[level=4].desc
   limit: do 120 znaków
   EN: Base Power +1 per 5 Charge Count (max 3)
   PL:
319. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 차원 마검
   źródło: Passives.json :: dataList[id=1040501].name
   limit: do 40 znaków
   EN: Dimensional Demon Edge
   PL:
320. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 적 처치 시 충전 횟수 2 증가 (턴 당 최대 3회 발동)
   źródło: Passives.json :: dataList[id=1040501].desc
   limit: do 120 znaków
   EN: Upon defeating an enemy, gain +2 Charge Count (3 times per turn)
   PL:
321. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 차원 굴절 칼날 - Type: Blade Mk7
   źródło: Passives.json :: dataList[id=1040521].name
   limit: do 70 znaków
   EN: Dimensional Refraction Edge - Type: Blade Mk7
   PL:
322. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] 최대 체력이 가장 낮은 아군 1명이 적 처치 시 충전 횟수 2 증가 (턴 당 최대 1회 발동)
   źródło: Passives.json :: dataList[id=1040521].desc
   limit: do 130 znaków
   EN: When an ally with the lowest Max HP defeats an enemy, they gain +2 Charge Count (Once per turn)
   PL:
323. [Kwestia głosowa [get_10405_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=get_10405_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Kwestia głosowa [get_10405_1] (Identity Acquisition)] 어이가 없군. 병. 솔. 이나 하고 있으라니.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=get_10405_1].dlg
   limit: do 120 znaków
   EN: Absurd. Can't believe I'm relegated to B.S.
   PL:
325. [Kwestia głosowa [lobby_morning_10405_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=lobby_morning_10405_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Kwestia głosowa [lobby_morning_10405_1] (Morning Greeting)] 아침 교육에 집중해라… 귀찮게 굴지 말도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=lobby_morning_10405_1].dlg
   limit: do 120 znaków
   EN: Focus on your morning lessons... And don't bother me.
   PL:
327. [Kwestia głosowa [lobby_noon_10405_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=lobby_noon_10405_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Kwestia głosowa [lobby_noon_10405_1] (Afternoon Greeting)] 식사…? 알. 먹. 이 시간에 나와있는 걸로도 짜증나니까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=lobby_noon_10405_1].dlg
   limit: do 120 znaków
   EN: Lunch...? I.D.C. Being out here at this time is a hassle all on its own.
   PL:
329. [Kwestia głosowa [lobby_night_10405_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=lobby_night_10405_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Kwestia głosowa [lobby_night_10405_1] (Evening Greeting)] 밤인가… 곧, 열차가 들어오겠군. 이제야 재미가 생기겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=lobby_night_10405_1].dlg
   limit: do 120 znaków
   EN: Nighttime, is it... The train will be arriving soon. Finally, something fun.
   PL:
331. [Kwestia głosowa [smalltalk_10405_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Kwestia głosowa [smalltalk_10405_1] (Chatter #1)] 그저 열차를 정리하고 청소한다… 하, 이건 그런 단순한 작업이 아니다. 일종의 예술이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_1].dlg
   limit: do 120 znaków
   EN: "Just a cleanup job"...? Ha, this is no mere cleaning. This is a form of art.
   PL:
333. [Kwestia głosowa [smalltalk_10405_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [smalltalk_10405_2] (Chatter #2)] 문이 열리면, 그 때 마다 색다른 예술품들이 그곳에 자리하고 있지. 몇 천 년 동안 쌓아올려진 미학을 관찰할 수 있는 기회라니, 상상만 해도 즐겁지 않나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_2].dlg
   limit: do 310 znaków
   EN: Every time I walk through these train doors, vastly different styles of art greet me. This is an opportunity to observe a singular, isolated artistic history that has been molded and honed over thousands of years. Simply electrifying, isn't it?
   PL:
335. [Kwestia głosowa [smalltalk_10405_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [smalltalk_10405_3] (Chatter #3)] 한 건이라도 더 열차 정리에 투입돼야 할 판에, 갑자기 신입 교육을 맡으라니… 어이, 네 놈이 위에 뭐라고 해봐.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_3].dlg
   limit: do 170 znaków
   EN: I should be deployed on a clean-up job, not coddling new hires... Hey, you. Make a complaint to the upper management or something.
   PL:
337. [Kwestia głosowa [smalltalk_10405_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [smalltalk_10405_4] (Post-Uptie Chat 1)] 가끔… 아직 조각되지 않은 예술품이 걷거나 뛸 때가 있지. 그 대부분은 여러 승객이 뭉쳐져 있는 상태더군.\n나는 그 자체로 아름답다고 생각하지만… 결국 떼어내야 한다는 점은… 좀 짜증난다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Some... Unrefined pieces of art can shamble or even run. Usually a case of multiple passengers being melded into a single body. I must say, that alone is a beautiful sight... It's a shame that they all eventually have to be pulled apart.
   PL:
339. [Kwestia głosowa [smalltalk_10405_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [smalltalk_10405_5] (Post-Uptie Chat 2)] 가장 훌륭한 점이라… 말해줄 수 있지. 그건, 이 예술품들 모두가 이렇게 될 줄도 모르고 스스로 열차에 타 예술품이 되었다는 점이다.\n 아니, 몰랐던 게 아니라… 알려 하지 않았던 것인가. 이 아이러니가 훌륭하지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=smalltalk_10405_5].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: My favorite part of this job...? Sure, listen close. It's the fact that, when they took this train of their own volition, every single one of these works of art didn't know what they were signing up for.\nWell, maybe it's that they didn't even care to know. Exquisite irony, isn't it?
   PL:
341. [Kwestia głosowa [neglect_10405_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=neglect_10405_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [neglect_10405_1] (Idle)] 후우우… 이 빌어먹을 대기는 언제 끝나지. 몸이 근질거리는군…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=neglect_10405_1].dlg
   limit: do 120 znaków
   EN: Hmmm... I'm growing restless. When the hell can we get to work?
   PL:
343. [Kwestia głosowa [gacksung_10405_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=gacksung_10405_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [gacksung_10405_1] (Uptying)] 흥, 실력을 인정했다면 사람 관리 말고 현장 청소 업무에 나를 배치해라.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=gacksung_10405_1].dlg
   limit: do 120 znaków
   EN: Hmph. So you acknowledge my abilities. Then assign me to proper fieldwork, not babysitting.
   PL:
345. [Kwestia głosowa [formation_10405_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=formation_10405_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [formation_10405_1] (Deployment)] 마침내 현장 투입인가.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=formation_10405_1].dlg
   limit: do 120 znaków
   EN: Finally, fieldwork.
   PL:
347. [Kwestia głosowa [battleentry_10405_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battleentry_10405_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [battleentry_10405_1] (Stage Entry)] 정리 시간이다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battleentry_10405_1].dlg
   limit: do 120 znaków
   EN: It's time to clean up.
   PL:
349. [Kwestia głosowa [battle_select_10405_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_select_10405_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [battle_select_10405_1] (Viewed in Battle)] 끼어들지 마라. 한참… 좋을 때다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_select_10405_1].dlg
   limit: do 120 znaków
   EN: Get out of my way. I'm... in the zone.
   PL:
351. [Kwestia głosowa [battle_endcommand_10405_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_endcommand_10405_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [battle_endcommand_10405_1] (Commencing Attack)] 내가 눈에 새겨주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_endcommand_10405_1].dlg
   limit: do 120 znaków
   EN: Witness my work.
   PL:
353. [Kwestia głosowa [battle_enemy_break_10405_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_enemy_break_10405_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [battle_enemy_break_10405_1] (Enemy Stagger)] 벌써 끝나가는군…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_enemy_break_10405_1].dlg
   limit: do 120 znaków
   EN: Nearing completion already...
   PL:
355. [Kwestia głosowa [battle_break_10405_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_break_10405_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [battle_break_10405_1] (Staggered)] 하.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_break_10405_1].dlg
   limit: do 120 znaków
   EN: Ha.
   PL:
357. [Kwestia głosowa [battle_kill_10405_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_kill_10405_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [battle_kill_10405_1] (Enemy Killed)] 마무리.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_kill_10405_1].dlg
   limit: do 120 znaków
   EN: The finishing touches.
   PL:
359. [Kwestia głosowa [battle_dead_10405_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_dead_10405_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_dead_10405_1] (Death)] 하, 이것도… 꽤 전위적이군…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_dead_10405_1].dlg
   limit: do 120 znaków
   EN: Hah, this is also... quite avant—garde...
   PL:
361. [Kwestia głosowa [choice_success_p_10405_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=choice_success_p_10405_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [choice_success_p_10405_2] (Check Passed)] 문. 없.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=choice_success_p_10405_2].dlg
   limit: do 120 znaków
   EN: N.P.
   PL:
363. [Kwestia głosowa [choice_fail_n_10405_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=choice_fail_n_10405_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [choice_fail_n_10405_1] (Check Failed)] 젠. 장.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=choice_fail_n_10405_1].dlg
   limit: do 120 znaków
   EN: S.H.I.T.
   PL:
365. [Kwestia głosowa [battle_clear_10405_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_clear_10405_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Kwestia głosowa [battle_clear_10405_1] (Victory Cry)] 나쁘지는 않았지… 이제, 다음 열차를 기다려 볼까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_clear_10405_1].dlg
   limit: do 120 znaków
   EN: That was serviceable. Now, to wait for the next train.
   PL:
367. [Kwestia głosowa [battle_clear_ex_10405_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_clear_ex_10405_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Kwestia głosowa [battle_clear_ex_10405_1] (Extra Conditions Fulfilled)] 훌륭한 전시회였어. 하, 이걸 오히려 고맙다고 말해야 하나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_clear_ex_10405_1].dlg
   limit: do 140 znaków
   EN: That was quite the exhibition. Perhaps I should thank them for being such a delightful collection of arts?
   PL:
369. [Kwestia głosowa [battle_defeat_10405_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_defeat_10405_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Kwestia głosowa [battle_defeat_10405_1] (Defeat Wail)] 끔찍하군. …아니지, 강등되면 현장 투입이 더 많아지는 건가?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Wcorp_10405.json :: dataList[id=battle_defeat_10405_1].dlg
   limit: do 120 znaków
   EN: Dreadful. ...No. I suppose a demotion to L2 would net me more fieldwork.
   PL:

## [00] LCCB Assistant Manager — Ryōshū — LCCB 대리
- ID Tożsamości: `10406` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 76 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise, Tremor, Rupture

371. [Karta Tożsamości — tytuł] LCCB\n대리
   źródło: Personalities.json :: dataList[id=10406].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCCB\nAssistant Manager
   PL:
372. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10406].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10406].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Karta Tożsamości — opis] 료슈의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10406].desc
   limit: do 120 znaków
   EN: Ryōshū’s 6th Identity
   PL:
375. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 밀치기
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=1].name ; dataList[id=1040601].levelList[level=2].name ; dataList[id=1040601].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Shove
   PL:
376. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=1].desc ; dataList[id=1040601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Poise Count
   PL:
377. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 정신력 4 감소
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Target loses 4 SP
   PL:
378. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 정신력 6 감소
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Target loses 6 SP
   PL:
379. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n<style="highlight">자신의</style> <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></color></link></u><style="highlight">이 7 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Poise Count\n<style="highlight">At 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></color></link></u>, Coin Power +1</style>
   PL:
380. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 정신력 8 감소
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Target loses 8 SP
   PL:
381. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 타.무
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].name ; dataList[id=1040602].levelList[level=2].name ; dataList[id=1040602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: T.N.
   PL:
382. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 1 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Poise
   PL:
383. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1040602].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 1 Offense Level Down
   PL:
384. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 1 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1040602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1040602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Poise
   PL:
387. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상이면 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: At 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u>, Coin Power +1
   PL:
388. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 공격 레벨 감소 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 2 Offense Level Down
   PL:
389. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대.박
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].name ; dataList[id=1040603].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: O.O.F.
   PL:
390. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 호흡 4 얻음\n자신의 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 10 이상이면 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 4 Poise\nAt 10+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u>, Coin Power +1
   PL:
391. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 탄환 1 소모
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Spend 1 Ammo
   PL:
392. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 진동, 파열 의 위력과 횟수가 2배로 부여됨
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Double the application of Tremor & Rupture Potency and Count
   PL:
393. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 진동 3 부여, 진동 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor and +1 Tremor Count
   PL:
394. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 파열 3 부여, 파열 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture and +1 Rupture Count
   PL:
395. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 5 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Trigger Tremor Burst
   PL:
396. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 호흡 4 얻음\n자신의 호흡 7당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 4 Poise\nGain +1 Coin Power for every 7 Poise on self (max 2)
   PL:
397. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Gain +1 Poise Count
   PL:
398. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 진동 4 부여, 진동 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Tremor and +2 Tremor Count
   PL:
400. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 파열 4 부여, 파열 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Rupture and +2 Rupture Count
   PL:
401. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL:
402. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-04.json :: dataList[id=1040604].levelList[level=1].name ; dataList[id=1040604].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Glut.) — nazwa] 담.탐
   źródło: Passives.json :: dataList[id=1040601].name
   limit: do 40 znaków
   EN: A S.B.
   PL:
404. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Glut.) — opis] 턴 종료 시 자신에게 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상 있으면, 정신력 8 회복.
   źródło: Passives.json :: dataList[id=1040601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: If this unit has 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> at Turn End, heal 8 SP.
   PL:
405. [Pasywka bojowa (od ulepszenia 3, posiadane 2× Glut.) — nazwa] 담.탐
   źródło: Passives.json :: dataList[id=1040602].name
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Pasywka bojowa (od ulepszenia 3, posiadane 2× Glut.) — opis] <style="highlight">- 상시 적용 : 탄환 7개 보유</style>\n턴 종료 시 자신에게 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상 있으면, 정신력 8 회복.
   źródło: Passives.json :: dataList[id=1040602].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n
   EN: <style="highlight">- Always Active : Begin encounters with 7 Ammo</style>\n- If this unit has 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> at Turn End, heal 8 SP.
   PL:
407. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Glut.) — nazwa] 담.탐
   źródło: Passives.json :: dataList[id=1040611].name
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Glut.) — opis] - 상시 적용 : 탄환 7개 보유\n- 턴 종료 시 자신에게 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상 있으면, 정신력 8 회복.\n<style="highlight">- 회복 전 정신력이 최대인 경우, 다음 턴에 호흡 1을 얻음</style>
   źródło: Passives.json :: dataList[id=1040611].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, <style="highlight">, </style>, \n
   EN: - Always Active : Begin encounters with 7 Ammo\n- If this unit has 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> at Turn End, heal 8 SP.\n<style="highlight">- If this unit already has max SP upon meeting the above condition, gain 1 Poise next turn</style>
   PL:
409. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 돛대
   źródło: Passives.json :: dataList[id=1040621].name
   limit: do 40 znaków
   EN: The Lucky Cig
   PL:
410. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] [Bullet]을 가장 적게 보유한 아군 1명이 코인에서 마지막 [Bullet]을 소모하면, 코인의 공격 종료 시, 각 대상에게 해당 코인의 공격으로 입힌 피해량의 50%만큼 추가 피해를 줌. (소수점 반올림)
   źródło: Passives.json :: dataList[id=1040621].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: If 1 ally with the least Ammo uses up their last Ammo with a Coin, deal 50% of the damage dealt by that Coin attack against each target as bonus damage against each individual target. (rounded up)
   PL:
411. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — nazwa] 돛대
   źródło: Passives.json :: dataList[id=1040631].name
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — opis] <style="highlight">- [Bullet]을 가장 적게 보유한 아군 1명이 [Bullet]을 소모하는 스킬을 사용할 때, 호흡 3 부여. (턴 당 1회. 탄환이 없는 대상에게는 적용되지 않음)</style>\n[Bullet]을 가장 적게 보유한 아군 1명이 코인에서 마지막 [Bullet]을 소모하면, 코인의 공격 종료 시, 각 대상에게 해당 코인의 공격으로 입힌 피해량의 50%만큼 추가 피해를 줌. (소수점 반올림)
   źródło: Passives.json :: dataList[id=1040631].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: <style="highlight">- If 1 ally with the least [Bullet] uses a Skill that spends [Bullet], gain 3 Poise. (once per turn; does not apply to allies without Ammo)</style>\n- If 1 ally with the least Ammo uses up their last Ammo with a Coin, deal 50% of the damage dealt by that Coin attack against each target as bonus damage against each individual target. (rounded up)
   PL:
413. [Kwestia głosowa [get_10406_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=get_10406_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [get_10406_1] (Identity Acquisition)] 료슈, 듣. 있. …음? 이렇게 무전하면 안 된다고?\n줄여 말하지 말아…? 왜… 신참이라서라고? 하아…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=get_10406_1].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ryōshū. I.A.L. Hm? This isn't standard comms protocol?\nStop using acronyms? What, why? ... Because I'm a rookie...? Haah...
   PL:
415. [Kwestia głosowa [lobby_morning_10406_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=lobby_morning_10406_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [lobby_morning_10406_1] (Morning Greeting)] 좋겠군, 아침 교육이 없어서. 이런 따분한 반복 작업을 매일 같이 해야 하는 끔찍함을 알아야 하는데.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=lobby_morning_10406_1].dlg
   limit: do 150 znaków
   EN: You don't have morning lessons? You lucked out, then. I would've loved to share the pain of repetitive daily chores.
   PL:
417. [Kwestia głosowa [lobby_noon_10406_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=lobby_noon_10406_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [lobby_noon_10406_1] (Afternoon Greeting)] 식사는 각 현장에 맞게 배급 나오는 것으로 적당히 때운다. …담배나 태우는 게 훨씬 맛이 좋군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=lobby_noon_10406_1].dlg
   limit: do 140 znaków
   EN: I make do with whatever ration they've assigned us for the mission. ... I much prefer the taste of a cig.
   PL:
419. [Kwestia głosowa [lobby_night_10406_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=lobby_night_10406_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [lobby_night_10406_1] (Evening Greeting)] 이 회사는 신입들에게 매일 밤마다 정신 교육을 시키지 않으면 회사가 망하는 건가…? 하아…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=lobby_night_10406_1].dlg
   limit: do 140 znaków
   EN: Do they think something might happen if they don't hold these new recruit rallies every night...? Haah...
   PL:
421. [Kwestia głosowa [smalltalk_10406_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [smalltalk_10406_1] (Chatter #1)] '저희 비포팀은 모두를 대신해서 길을 트는 중요한 임무를 맡은 직원들입니다. 여러분들이 피를 흘려가며…' 젠장, 귀에 딱지 앉도록 떠벌대니 입에 붙어버렸잖아.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_1].dlg
   limit: do 290 znaków
   EN: 'We the Before Team are assigned with the paramount task of clearing the path before anyone else does. Every bloodied step, every flesh given...' Damnit. I've repeated this so many times that I started saying it out of nowhere.
   PL:
423. [Kwestia głosowa [smalltalk_10406_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [smalltalk_10406_2] (Chatter #2)] 다음에 참여할 작전은 U사의 어떤 항구선이라고 하는군… 뭐, 내게는 쓸만한 일감도 내주지 않겠지만.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_2].dlg
   limit: do 160 znaków
   EN: Our next mission takes place at some portship of U Corp. Hmph, doubt they'll assign me with anything substantial to do.
   PL:
425. [Kwestia głosowa [smalltalk_10406_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [smalltalk_10406_3] (Chatter #3)] 노.잼. 3과가 제일 빡세다고 해서 일부러 자원했건만… 이런 식으로 빡셀 수도 있다는 건가…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_3].dlg
   limit: do 170 znaków
   EN: B.A.H. I joined after hearing that Section 3 was the toughest... But this boredom is the kind of toughness I didn't expect...
   PL:
427. [Kwestia głosowa [smalltalk_10406_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [smalltalk_10406_4] (Post-Uptie Chat 1)] 이 산탄총이 제일 쓸만하군. 이만한 걸 남겨주고 사라졌으니, 팀장 놈한테 감사의 마음을 담아 되갚으러 가볼까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_4].dlg
   limit: do 190 znaków
   EN: This shotgun is the most useful of the bunch. Now that the Team Leader left this behind for me... It's time for my own expression of gratitude.
   PL:
429. [Kwestia głosowa [smalltalk_10406_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [smalltalk_10406_5] (Post-Uptie Chat 2)] 눈치빠른 놈은 교육 좀 듣다보면 이렇게 다 뒈져버리기 쉬운 직장이란건 알아먹었겠지. 덕분에 한 건 제대로 놀만한 판이 벌어졌군. 솔. 플. 시작이다. 훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=smalltalk_10406_5].dlg
   limit: do 250 znaków
   EN: Anyone with a semblance of common sense must've gleaned from the lessons that we're all being thrown into a meat grinder. I finally have a place to let loose thanks to that. Time to go S.P.
   PL:
431. [Kwestia głosowa [neglect_10406_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=neglect_10406_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [neglect_10406_1] (Idle)] 하… 담배가… 말리는군…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=neglect_10406_1].dlg
   limit: do 120 znaków
   EN: Haah... I'm craving... a cig...
   PL:
433. [Kwestia głosowa [gacksung_10406_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=gacksung_10406_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [gacksung_10406_1] (Uptying)] 여기는 료슈, 작전 편성 인원 전원이 사망해… 뭐야, 무전도 안 듣는군… 좋아, 여기서부터는 내 세상이다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=gacksung_10406_1].dlg
   limit: do 160 znaków
   EN: Acknowledge. This is Ryōshū. Reporting total unit annihilation... Huh. The radio's also dead. Finally... I can let loose.
   PL:
435. [Kwestia głosowa [formation_10406_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=formation_10406_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [formation_10406_1] (Deployment)] 이제 좀 일다운 걸 시키나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=formation_10406_1].dlg
   limit: do 120 znaków
   EN: Am I finally getting some real work?
   PL:
437. [Kwestia głosowa [battleentry_10406_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battleentry_10406_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [battleentry_10406_1] (Stage Entry)] 탄환 일발 장전.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battleentry_10406_1].dlg
   limit: do 120 znaków
   EN: Single shell in chamber. Ready to fire.
   PL:
439. [Kwestia głosowa [battle_select_10406_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_select_10406_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Kwestia głosowa [battle_select_10406_1] (Viewed in Battle)] 오, 무전인가? 들리나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_select_10406_1].dlg
   limit: do 120 znaków
   EN: Oh, am I getting a signal? Acknowledge.
   PL:
441. [Kwestia głosowa [battle_endcommand_10406_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_endcommand_10406_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [battle_endcommand_10406_1] (Commencing Attack)] 두드려 패고 터뜨려주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_endcommand_10406_1].dlg
   limit: do 120 znaków
   EN: I'll beat you up and blast you to bits.
   PL:
443. [Kwestia głosowa [battle_enemy_break_10406_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_enemy_break_10406_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [battle_enemy_break_10406_1] (Enemy Stagger)] 자세가 무너졌군… 다음엔 배를 날려주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_enemy_break_10406_1].dlg
   limit: do 120 znaków
   EN: You're staggered... Next, I'll blast your guts to smithereens.
   PL:
445. [Kwestia głosowa [battle_break_10406_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_break_10406_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [battle_break_10406_1] (Staggered)] 쯧…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_break_10406_1].dlg
   limit: do 120 znaków
   EN: Tsk...
   PL:
447. [Kwestia głosowa [battle_kill_10406_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_kill_10406_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [battle_kill_10406_1] (Enemy Killed)] 타. 무. 아니… 타겟 무력화.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_kill_10406_1].dlg
   limit: do 120 znaków
   EN: T.N. I mean... Target Neutralized.
   PL:
449. [Kwestia głosowa [battle_dead_10406_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_dead_10406_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [battle_dead_10406_1] (Death)] 큭… 쳇, 이렇게 금방… 따라갈 줄이야.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_dead_10406_1].dlg
   limit: do 120 znaków
   EN: Akh... Tsk, didn't think... I'd follow them so soon...
   PL:
451. [Kwestia głosowa [choice_success_p_10406_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=choice_success_p_10406_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Kwestia głosowa [choice_success_p_10406_2] (Check Passed)] 산탄총에는 이런저런 문제를 해결하는 능력도 있다. 훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=choice_success_p_10406_2].dlg
   limit: do 120 znaków
   EN: A shotgun is a beautiful problem solver. Heh.
   PL:
453. [Kwestia głosowa [choice_fail_n_10406_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=choice_fail_n_10406_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Kwestia głosowa [choice_fail_n_10406_1] (Check Failed)] 내 탓 아니다. 허접한 장비만 뿌려댄 윗놈들 탓이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=choice_fail_n_10406_1].dlg
   limit: do 120 znaków
   EN: Not my fault. They assigned me trash gear.
   PL:
455. [Kwestia głosowa [battle_clear_10406_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_clear_10406_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Kwestia głosowa [battle_clear_10406_1] (Victory Cry)] 작전 종료. 지정된 장소로 돌아간다. LCCB / 사. 관. / 3과. 복귀 인원은… 혼자다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_clear_10406_1].dlg
   limit: do 130 znaków
   EN: Mission Complete. Returning to rendezvous point. LCCB / P.O. / Unit 3. Returning units... Just one.
   PL:
457. [Kwestia głosowa [battle_clear_ex_10406_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_clear_ex_10406_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Kwestia głosowa [battle_clear_ex_10406_1] (Extra Conditions Fulfilled)] 작전 목표로 보이는 변동 좌표를 확보. 이걸 가지고 복귀한다. 흥, 제대로 대우해주라고.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_clear_ex_10406_1].dlg
   limit: do 190 znaków
   EN: Returning to base with the variable coordinates. This appears to have been our mission objective. Hmph, you better treat me right from now on.
   PL:
459. [Kwestia głosowa [battle_defeat_10406_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_defeat_10406_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Kwestia głosowa [battle_defeat_10406_1] (Defeat Wail)] 작전은 실패다. 다 뒈져서 죽도 밥도 안됐어. 쯧, 그 잘났다는 LCCA가 어떻게든 처리하겠지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LCCB_10406.json :: dataList[id=battle_defeat_10406_1].dlg
   limit: do 170 znaków
   EN: Mission Failed. Total annihilation, and for what? Nothing. Tsk, I'm sure the high-and-mighty LCCA will take care of the rest.
   PL:

## [00] Liu Assoc. South Section 4 — Ryōshū — 남부 리우 협회 4과
- ID Tożsamości: `10407` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

461. [Karta Tożsamości — tytuł] 남부 리우 협회\n4과
   źródło: Personalities.json :: dataList[id=10407].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 4
   PL:
462. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10407].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10407].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Karta Tożsamości — opis] 료슈의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10407].desc
   limit: do 120 znaków
   EN: Ryōshū's 7th Identity
   PL:
465. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 전면전
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=1].name ; dataList[id=1040701].levelList[level=2].name ; dataList[id=1040701].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: All-out War
   PL:
466. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]
   PL:
467. [Umiejętność 1 (×3) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1
   PL:
469. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
470. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Combustion]이 10 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1\n<style="highlight">If target has 10+ [Combustion], Coin Power +1 </style>
   PL:
472. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL:
473. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 염수격
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=1].name ; dataList[id=1040702].levelList[level=2].name ; dataList[id=1040702].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Fiery Knifehand
   PL:
474. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
475. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 피해량 +20%
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], deal +20% damage
   PL:
476. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=2].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], deal +30% damage
   PL:
478. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Combustion]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1\n<style="highlight">If target has 6+ [Combustion], Coin Power +1</style>
   PL:
479. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 피해량 +50%
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], deal +50% damage
   PL:
480. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 염절
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].name ; dataList[id=1040703].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Flame Cleave
   PL:
481. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1040703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1040703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 10 이상이면, 피해량 +20%
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [Combustion], deal +20% damage
   PL:
486. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Combustion]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1\n<style="highlight">If target has 6+ [Combustion], Coin Power +1 </style>
   PL:
487. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 10 이상이면, 피해량 +40%
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [Combustion], deal +40% damage
   PL:
488. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-04.json :: dataList[id=1040704].levelList[level=1].name ; dataList[id=1040704].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — nazwa] 화전
   źródło: Passives.json :: dataList[id=1040701].name
   limit: do 40 znaków
   EN: Flame Spread
   PL:
490. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — opis] 자신이 [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 [Combustion] 위력이 가장 낮은 무작위 적 1명에게 [Combustion] 4 부여 (턴 당 1회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040701].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 1 random enemy that either has no [Combustion] or has the least [Combustion] Potency (once per turn)\n- In Focused Encounters, inflict to 1 random Part
   PL:
491. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — podsumowanie] [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 위력이 가장 낮은 무작위 적 1명에게 [Combustion] 4 부여
   źródło: Passives.json :: dataList[id=1040701].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 1 random enemy that either has no [Combustion] or has the least [Combustion] Potency
   PL:
492. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — nazwa] 화전
   źródło: Passives.json :: dataList[id=1040711].name
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — opis] 자신이 [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 [Combustion] 위력이 가장 낮은 무작위 적 2명에게 [Combustion] 4 부여 (턴 당 2회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040711].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 2 random enemies that either have no [Combustion] or have the least [Combustion] Potency (2 times per turn)\n- In Focused Encounters, inflict to 2 random Parts
   PL:
494. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — podsumowanie] [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 위력이 가장 낮은 무작위 적 2명에게 [Combustion] 4 부여
   źródło: Passives.json :: dataList[id=1040711].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 2 random enemies that either have no [Combustion] or have the least [Combustion] Potency
   PL:
495. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — nazwa] 전화
   źródło: Passives.json :: dataList[id=1040721].name
   limit: do 40 znaków
   EN: Spread Flame
   PL:
496. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — opis] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 1명에게 [Combustion] 3 부여 (턴 당 1회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040721].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 1 random enemy (once per turn)\n- In Focused Encounters, inflict on 1 random Part
   PL:
497. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — podsumowanie] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 1명에게 [Combustion] 3 부여
   źródło: Passives.json :: dataList[id=1040721].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 1 random enemy
   PL:
498. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Wrath) — nazwa] 전화
   źródło: Passives.json :: dataList[id=1040731].name
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Wrath) — opis] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 2명에게 [Combustion] 3 부여 (턴 당 1회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040731].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 2 random enemies (once per turn)\n- In Focused Encounters, inflict on 2 random Parts
   PL:
500. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Wrath) — podsumowanie] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 2명에게 [Combustion] 3 부여
   źródło: Passives.json :: dataList[id=1040731].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 2 random enemies
   PL:
501. [Kwestia głosowa [get_10407_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=get_10407_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Kwestia głosowa [get_10407_1] (Identity Acquisition)] 허. 훈련실에서 펼쳐지는 예술이 궁금했나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=get_10407_1].dlg
   limit: do 120 znaków
   EN: Hmph. Did you wish to witness the art performed in a training room?
   PL:
503. [Kwestia głosowa [lobby_morning_10407_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=lobby_morning_10407_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Kwestia głosowa [lobby_morning_10407_1] (Morning Greeting)] 바깥이 시끄럽다. 또 아침 식사를 하겠다고 소란스러운 모양이지. 흥, 몸을 단련하는 것보다 즐거울 수는 없는 것을.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=lobby_morning_10407_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's getting loud outside... They must be making a ruckus preparing breakfast again.\nHmph, no delicious meal can possibly be better than a good training session.
   PL:
505. [Kwestia głosowa [lobby_noon_10407_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=lobby_noon_10407_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Kwestia głosowa [lobby_noon_10407_1] (Afternoon Greeting)] 해가 중천이라고… 상. 없. 일거리가 아니라면 굳이 나를 부를 필요 없다. 일 외에 여기를 벗어날 생각은 없다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=lobby_noon_10407_1].dlg
   limit: do 160 znaków
   EN: It's already midday...? I.D.C. Don't call me unless it's for work. I don't intend to leave this room unless it's for a job.
   PL:
507. [Kwestia głosowa [lobby_night_10407_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=lobby_night_10407_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Kwestia głosowa [lobby_night_10407_1] (Evening Greeting)] 사람이 잠들고 깨어나는데 큰 조건이 있지는 않지. 지치면 잠들고, 회복하면 깬다. 공간은 중요치 않다.\n알고 있나? 이 목인장에 기대어 자는 건 꽤 편하다고. 훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=lobby_night_10407_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are no particular conditions for sleeping and waking. Humans sleep when tired and wake up when no longer tired. It doesn't matter where one goes to sleep.\nBesides, sleeping against this training dummy is more comfortable than you'd expect. Heh.
   PL:
509. [Kwestia głosowa [smalltalk_10407_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Kwestia głosowa [smalltalk_10407_1] (Chatter #1)] 따듯, 화목. 그게 리우의 기조라. 하. 그래, 멋대로 지껄이도록.\n내가 배운 리우의 행동 강령은 불꽃처럼 불사르는 것. 그 뿐이니까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Warmth. Kinship. They're the 'core values' of Liu... Hah. Sure, of course.\nBut the only core value of Liu that I've come to know is that it scorches and burns. That's all there is to it.
   PL:
511. [Kwestia głosowa [smalltalk_10407_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Kwestia głosowa [smalltalk_10407_2] (Chatter #2)] 불꽃은 강력하고 화려하지만, 동시에 가녀리고 나약하지.\n항상 강력한 불꽃이 될 수 있게 하는 방법은, 쉴 새 없이 장작을 넣어주는 것 뿐이다. 그 방법은, 오직 끊임 없는 훈련 뿐.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_2].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The flame is powerful, impressive... but it also carries frailty and fragility.\nThe only way to keep the fire burning is to feed it firewood ceaselessly. And that 'firewood' is endless training.
   PL:
513. [Kwestia głosowa [smalltalk_10407_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Kwestia głosowa [smalltalk_10407_3] (Chatter #3)] 화상 자국과 강화 문신은 흡사한 것이 많지. 그려낼 때는 타들어 가듯이 아프고, 점점 피부를 다른 색으로 물들여 간다는 점.\n…그리고 채워져 나갈 수록 강해진다는 점.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_3].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Burn marks are like enhancement tattoos; it hurts like hell when drawing them, and they paint parts of your skin in different colors.\n... And the more of your skin is covered with them... the stronger you get.
   PL:
515. [Kwestia głosowa [smalltalk_10407_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Kwestia głosowa [smalltalk_10407_4] (Post-Uptie Chat 1)] 하! 어떻게 된 몸이 나무토막보다도 가녀릴 수 있지? 뛰쳐나오는 불꽃이 아까울 정도군.\n …아니, 이리저리 형체가 뒤틀어지는 모습은 좀 흥미롭나. 훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hah! I can't believe they're more fragile even than a training dummy. It almost feels wasteful to spark my flames against them.\n... Hm, though I suppose it can be quite entertaining to watch their distorting shapes as the fire burns them alive.
   PL:
517. [Kwestia głosowa [smalltalk_10407_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Kwestia głosowa [smalltalk_10407_5] (Post-Uptie Chat 2)] 연. 타. 그리고, 일. 수. 쉴새 없이 몰아붙이는 권격의 끝을 마무리하기에는 살을 꿰차고 지져 내는 이 일격이 어울리지.\n잘 익은 고기에 와인이 따라나오는 것과 다를 바 없군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=smalltalk_10407_5].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: C.S... then P.S. This flesh-burning, penetrating strike is the perfect finisher to this series of breakneck-speed consecutive strikes.\nConsider it a glass of wine to a plate of perfectly grilled steak.
   PL:
519. [Kwestia głosowa [neglect_10407_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=neglect_10407_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Kwestia głosowa [neglect_10407_1] (Idle)] 흠. 뭐, 불이 필요하나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=neglect_10407_1].dlg
   limit: do 120 znaków
   EN: Hm. What, need some fire?
   PL:
521. [Kwestia głosowa [gacksung_10407_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=gacksung_10407_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Kwestia głosowa [gacksung_10407_1] (Uptying)] 부장… 귀 따갑게 시끄럽게만 굴 줄 알았는데, 이런 쓸모 있는 기술을 다 알려주는군. 훗, 마무리로 쓸만하겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=gacksung_10407_1].dlg
   limit: do 190 znaków
   EN: Section Director... Thought she was a useless loudmouth, but she taught me this particularly useful skill. Heh, I could use this as a finisher.
   PL:
523. [Kwestia głosowa [formation_10407_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=formation_10407_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Kwestia głosowa [formation_10407_1] (Deployment)] 일이라면, 간다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=formation_10407_1].dlg
   limit: do 120 znaków
   EN: Is this a job? Then I'll be there.
   PL:
525. [Kwestia głosowa [battleentry_10407_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battleentry_10407_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Kwestia głosowa [battleentry_10407_1] (Stage Entry)] 움직이는 목인장, 재밌겠군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battleentry_10407_1].dlg
   limit: do 120 znaków
   EN: Moving dummies... this could be interesting.
   PL:
527. [Kwestia głosowa [battle_select_10407_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_select_10407_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Kwestia głosowa [battle_select_10407_1] (Viewed in Battle)] 꺼져. 집중하고 있다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_select_10407_1].dlg
   limit: do 120 znaków
   EN: Scram. I'm trying to focus.
   PL:
529. [Kwestia głosowa [battle_endcommand_10407_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_endcommand_10407_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Kwestia głosowa [battle_endcommand_10407_1] (Commencing Attack)] 초식, 1번!
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_endcommand_10407_1].dlg
   limit: do 120 znaków
   EN: First Form!
   PL:
531. [Kwestia głosowa [battle_enemy_break_10407_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_enemy_break_10407_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Kwestia głosowa [battle_enemy_break_10407_1] (Enemy Stagger)] 똑바로 서라. 나무 인형만도 못 한 것.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_enemy_break_10407_1].dlg
   limit: do 120 znaków
   EN: Get up. A wooden dummy stands taller than you do.
   PL:
533. [Kwestia głosowa [battle_break_10407_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_break_10407_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Kwestia głosowa [battle_break_10407_1] (Staggered)] 치잇…!
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_break_10407_1].dlg
   limit: do 120 znaków
   EN: Tsk...!
   PL:
535. [Kwestia głosowa [battle_kill_10407_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_kill_10407_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Kwestia głosowa [battle_kill_10407_1] (Enemy Killed)] 쯧, 벌써 부서졌나. 쓸모가 없군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_kill_10407_1].dlg
   limit: do 120 znaków
   EN: Tsk, already broken. How useless.
   PL:
537. [Kwestia głosowa [battle_dead_10407_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_dead_10407_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Kwestia głosowa [battle_dead_10407_1] (Death)] 하… 아. 움직이지 않는 나무토막으론… 무리였나.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_dead_10407_1].dlg
   limit: do 120 znaków
   EN: Haah... These... moving dummies must've been... insufficient training material.
   PL:
539. [Kwestia głosowa [choice_success_p_10407_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=choice_success_p_10407_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Kwestia głosowa [choice_success_p_10407_2] (Check Passed)] 쓸데없는 것을 시키고 앉았군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=choice_success_p_10407_2].dlg
   limit: do 120 znaków
   EN: What a waste of time.
   PL:
541. [Kwestia głosowa [choice_fail_n_10407_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=choice_fail_n_10407_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Kwestia głosowa [choice_fail_n_10407_1] (Check Failed)] 쓸데없는 것을 시킨 결과다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=choice_fail_n_10407_1].dlg
   limit: do 120 znaków
   EN: That is what you get for wasting my time.
   PL:
543. [Kwestia głosowa [battle_clear_10407_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_clear_10407_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Kwestia głosowa [battle_clear_10407_1] (Victory Cry)] 끝났나. 뭐, 가끔은 진짜 움직이는 것들을 상대하는 것도 나쁘진 않군. 승패가 이미 결정되어 있다는건 재미없지만.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_clear_10407_1].dlg
   limit: do 190 znaków
   EN: It is done. Well, I see that facing moving targets can sometimes be entertaining. It's just disappointing that I saw this outcome from a mile away.
   PL:
545. [Kwestia głosowa [battle_clear_ex_10407_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_clear_ex_10407_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Kwestia głosowa [battle_clear_ex_10407_1] (Extra Conditions Fulfilled)] 훈련장만큼의 즐거움도 주지 않는 건가. 압도적이니 재미도 없군. 다시 훈련에나 매진한다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_clear_ex_10407_1].dlg
   limit: do 190 znaków
   EN: They couldn't even measure up to training dummies... This victory was so overwhelming that it was practically dull. I'm going back to training.
   PL:
547. [Kwestia głosowa [battle_defeat_10407_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_defeat_10407_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Kwestia głosowa [battle_defeat_10407_1] (Defeat Wail)] 졌다고…? 믿. 없. 이 따위 물렁한 나무 토막들에게 질 수가 있다니. 내 훈련 방식이 틀렸다고…?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LiuAsso4_10407.json :: dataList[id=battle_defeat_10407_1].dlg
   limit: do 140 znaków
   EN: We... lost...? N.W. No way we lost to these fleshy dummies. My training routine cannot possibly be wrong...!
   PL:

## [000] Edgar Family Chief Butler — Ryōshū — 에드가 가문 치프 버틀러
- ID Tożsamości: `10408` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 70 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Poise

549. [Karta Tożsamości — tytuł] 에드가 가문\n치프 버틀러
   źródło: Personalities.json :: dataList[id=10408].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Edgar Family\nChief Butler
   PL:
550. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10408].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10408].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Karta Tożsamości — opis] 료슈의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10408].desc
   limit: do 120 znaków
   EN: Ryōshū's 8th Identity
   PL:
553. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 응접도 1식 사냥
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].name ; dataList[id=1040801].levelList[level=2].name ; dataList[id=1040801].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Receiving Arts 1: The Hunt
   PL:
554. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
555. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
556. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MarkOfButler] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MarkOfButler]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MarkOfButler] = 버.표 / B.M.
   EN: [OnSucceedAttack] Inflict 2 [MarkOfButler]
   PL:
557. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 속도가 자신보다 3 이상 느리면, 합 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Clash Power +1</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
558. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 속도가 자신보다 느리면, 대상과의 속도 차이 2 당 합 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Clash Power +1 for every 2 Speed difference (max 3)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
559. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 응접도 제 7식 포착
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].name ; dataList[id=1040802].levelList[level=2].name ; dataList[id=1040802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Receiving Arts 7: Capture
   PL:
560. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [StartBattle] 자신의 [Breath] 횟수 6을 소모하여 이 스킬의 가중치 +2
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].desc ; dataList[id=1040802].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: [StartBattle] Consume 6 [Breath] Count on self to gain +2 Atk Weight for this Skill
   PL:
561. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
562. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MarkOfButler] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL:
564. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">메인 타겟의 속도가 자신보다 느리면, 대상과의 속도 차이 2 당 합 위력 +1 (최대 3)</style>\n[StartBattle] 자신의 [Breath] 횟수 6을 소모하여 이 스킬의 가중치 +2
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the main target's, gain Clash Power +1 for every 2 Speed difference (max 3)</style>\n[StartBattle] Consume 6 [Breath] Count on self to gain +2 Atk Weight for this Skill
   PL:
565. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [MarkOfButler] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [MarkOfButler]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [MarkOfButler] = 버.표 / B.M.
   EN: [CriticalOnSucceedAttack] Inflict 1 [MarkOfButler]
   PL:
566. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 응접도 제 2식 모.분
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].name ; dataList[id=1040803].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: Receiving Arts 2: S.Y.N.C.
   PL:
567. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상에게 [MarkOfButler]가 있으면 합 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 7 증가
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [MarkOfButler], [WhenUse], [Breath]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If target has [MarkOfButler], Clash Power +1\n[WhenUse] Gain +7 [Breath] Count
   PL:
568. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL:
569. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
570. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL:
571. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태면, 크리티컬 피해량 +20%
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered, deal +20% Damage on Critical Hit
   PL:
572. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [MarkOfButler] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1040803].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상에게 [MarkOfButler]가 있으면 합 위력 +1\n<style="highlight">대상의 속도가 자신보다 느리면, 대상과의 속도 차이 2 당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 7 증가
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MarkOfButler], [WhenUse], [Breath]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If target has [MarkOfButler], Clash Power +1\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power +1 for every 2 Speed difference (max 2)</style>\n[WhenUse] Gain +7 [Breath] Count
   PL:
574. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 손상
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30% of damage dealt
   PL:
575. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [MarkOfButler] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태면, 크리티컬 피해량 +40%
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered, deal +40% Damage on Critical Hit
   PL:
577. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [EnemyKill] [MarkOfButler]가 있는 무작위 대상에게 스킬 1회 재사용\n(재사용 시 발동하지 않음. [MarkOfButler]가 있는 대상이 없는 경우, 발동하지 않음)
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [EnemyKill], [MarkOfButler]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [MarkOfButler] = 버.표 / B.M.
   EN: [EnemyKill] Reuse Skill once on a random target that has [MarkOfButler]\n(Does not activate on Reuse. Does not activate when there are no remaining targets that have [MarkOfButler])
   PL:
578. [Obrona (ulepszenia 1,4) — nazwa] 한심
   źródło: Skills_personality-04.json :: dataList[id=1040804].levelList[level=1].name ; dataList[id=1040804].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Mediocre
   PL:
579. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 정신력 3 회복 (턴 당 3회)
   źródło: Skills_personality-04.json :: dataList[id=1040804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 3 SP (3 times per turn)
   PL:
580. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 정신력 3 회복 (턴 당 <style="highlight">5</style>회)\n<style="highlight">[OnSucceedEvade] 자신의 [Breath] 횟수 1 증가 (턴 당 5회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1040804].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Heal 3 SP (<style="highlight">5</style> times per turn)\n<style="highlight">[OnSucceedEvade] Gain +1 [Breath] Count(5 times per turn)</style>
   PL:
581. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 집안일 끝내기
   źródło: Passives.json :: dataList[id=1040801].name
   limit: do 40 znaków
   EN: Clearing Household Chores
   PL:
582. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] [MarkOfButler]가 있는 대상에게 공격 적중 시 다음 턴에 [Agility] 1 얻음 (턴 당 최대 3회)\n[MarkOfButler]가 있는 대상에게 크리티컬 적중 시 대상의 [MarkOfButler]를 제거하고, 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 크리티컬 피해량 +5% (최대 30%)
   źródło: Passives.json :: dataList[id=1040801].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [MarkOfButler], [Agility]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [Agility] = 신속 / Haste
   EN: On Hit against targets that have [MarkOfButler], gain 1 [Agility] next turn (3 times per turn)\nOn Crit against targets that have [MarkOfButler], eliminate [MarkOfButler] on target; then, if this unit's Speed is faster than the target's, deal +5% Damage on Critical Hit for every 1 Speed difference (max 30%)
   PL:
583. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — nazwa] 집안일 끝내기
   źródło: Passives.json :: dataList[id=1040811].name
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — opis] [MarkOfButler]가 있는 대상에게 공격 적중 시 [Breath] 횟수 1 증가, 다음 턴에 [Agility] 1 얻음 (턴 당 최대 3회)\n[MarkOfButler]가 있는 대상에게 크리티컬 적중 시 대상의 [MarkOfButler]를 제거하고, 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 크리티컬 피해량 +10% (최대 60%)
   źródło: Passives.json :: dataList[id=1040811].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [MarkOfButler], [Breath], [Agility]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: On Hit against targets that have [MarkOfButler], gain +1 [Breath] Count, and gain 1 [Agility] next turn (3 times per turn)\nOn Crit against targets that have [MarkOfButler], eliminate [MarkOfButler] on target; then, if this unit's Speed is faster than the target's, deal +10% Damage on Critical Hit for every 1 Speed difference (max 60%)
   PL:
585. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 청소 지휘
   źródło: Passives.json :: dataList[id=1040821].name
   limit: do 40 znaków
   EN: Cleaning Command
   PL:
586. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 편성 순서가 가장 뒤인 아군 1명이 합 승리 시 호흡 횟수 1 증가 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1040821].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When the ally that was deployed last wins a Clash, gain +1 [Breath] Count (3 times per turn)
   PL:
587. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — nazwa] 청소 지휘
   źródło: Passives.json :: dataList[id=1040831].name
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — opis] 편성 순서가 가장 뒤인 아군 1명이 합 승리 시 [Breath] 횟수 1 증가 (턴 당 3회), 다음 턴에 [Agility] 1 얻음 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1040831].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: When the ally that was deployed last wins a Clash, gain +1 [Breath] Count (3 times per turn), and gain 1 [Agility] next turn (once per turn)
   PL:
589. [Kwestia głosowa [get_10408_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=get_10408_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [get_10408_1] (Identity Acquisition)] 신. 정. 그렇게 해서 버틀러라고 말할 수 있겠나? 나와, 내가 보여주지. 신속하고, 정확하게…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=get_10408_1].dlg
   limit: do 180 znaków
   EN: S.P.D. You call yourself a Butler? I'll demonstrate, so just shut up and watch. It's all about the Speed, Precision, and Decisiveness...
   PL:
591. [Kwestia głosowa [lobby_morning_10408_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=lobby_morning_10408_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [lobby_morning_10408_1] (Morning Greeting)] 버틀러의 아침은 주인의 아침보다 두 시간은 일찍 찾아온다. 직접 두들겨 패서라도 일어나게 하도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=lobby_morning_10408_1].dlg
   limit: do 180 znaków
   EN: Butlers must always start their mornings two hours before their Master does. Get them all out of bed, even if you have to beat them up.
   PL:
593. [Kwestia głosowa [lobby_noon_10408_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=lobby_noon_10408_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [lobby_noon_10408_1] (Afternoon Greeting)] 식사 담당은 어디서 뭘 하고 있지? 고용주들의 점심이 5분이 늦어졌다. 이게 지금 말이 되나? 네 놈들도 꿈. 밤. 모. 분 형에 처해지고 싶나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=lobby_noon_10408_1].dlg
   limit: do 240 znaków
   EN: What the hell is the Kitchen staff doing? Our employers' luncheon has been delayed by 5 minutes. This is completely unacceptable. Any more delay, and I'll S.S.Y.N.C. Is that what you want?
   PL:
595. [Kwestia głosowa [lobby_night_10408_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=lobby_night_10408_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [lobby_night_10408_1] (Evening Greeting)] 나이프와 포크를 확실하게 갈아둘 수 있도록. 버틀러의 진짜 즐거움은 '심야 경비 임무'에 있으니까… 후훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=lobby_night_10408_1].dlg
   limit: do 200 znaków
   EN: Make sure that your forks and knives are well-whetted. Everything truly enjoyable about being a Butler happens during the 'night watch' missions... heh.
   PL:
597. [Kwestia głosowa [smalltalk_10408_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [smalltalk_10408_1] (Chatter #1)] 나는 길게 늘여 말하는 걸 좋아하지 않는다… 하지만 일 처리가 한심한 녀석들 때문에 자꾸만 혀가 길어져.\n하… 치프 버틀러도 고달프군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_1].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I personally detest having to talk more than I have to, but... this sloppy work deserves proper scolding.\nHaah... Chief Butler is quite an exhausting job.
   PL:
599. [Kwestia głosowa [smalltalk_10408_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [smalltalk_10408_2] (Chatter #2)] 정리를 이딴 식으로 하면… 급할 때 대체 어떻게 식기를 꺼낼 생각인 거지. 어처구니가 없군…\n잘 봐라. 처음부터 가르쳐 줄테니. 벌써 일곱 번 째지만…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_2].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Look at this mess inside your case. How will you find your utensils in case of an emergency? Unbelievable...\nI'll give you another demonstration of how to organize your case. The entire process. For the seventh time...
   PL:
601. [Kwestia głosowa [smalltalk_10408_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [smalltalk_10408_3] (Chatter #3)] 사냥의 시간까지 얼마 남지 않았다. 이번 목표는… 한 때 동고동락했던 놈이라 신경이 쓰이긴 하지만…\n쯧, 어쨌든 내가 처리하는 방법 말고는 없으니. 그레고르 놈한텐 연락은 닿았나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_3].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The hunt is nigh. This time, our target is... well, I don't like that he's an old acquaintance of mine...\nTsk. But this is something I have to do myself. You there. Were you able to get in touch with Gregor?
   PL:
603. [Kwestia głosowa [smalltalk_10408_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [smalltalk_10408_4] (Post-Uptie Chat 1)] 물러서! 저 놈은… 쯧. 설명하기 복잡하군. 네 놈들의 버러지만도 못한 공격으론 도움조차 되지 않으니까, 저택으로 돌아가서 남은 청소나 끝내.\n저건… 내가 맡는다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_4].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pull back! He's... Tsk, this is hard to explain. Return to the manor and finish your cleaning duties. Your less-than-ineffective attacks are hardly any help anyway.\n... I'll deal with him myself.
   PL:
605. [Kwestia głosowa [smalltalk_10408_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [smalltalk_10408_5] (Post-Uptie Chat 2)] 결국 이렇게 다시 만났나… 제법 기묘한 기분이군. 이런 식의 고향 방문은 치프 버틀러로서는 내키지 않는다.\n적어도… 과격한 환영식을 열어줘야 형편이 맞겠지. 훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=smalltalk_10408_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: So this is how we meet again... What a bizarre feeling this is. As the Chief Butler, I must say that this isn't the kind of reunion I hoped you'd bring.\nI'll throw you one hell of a homecoming party, though. Heh.
   PL:
607. [Kwestia głosowa [neglect_10408_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=neglect_10408_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [neglect_10408_1] (Idle)] 멍하니 있지 말고 나이프라도 갈아라. 하… 혀가 닳겠군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=neglect_10408_1].dlg
   limit: do 120 znaków
   EN: Quit zoning out and whet your knives. Haah... how many times must I repeat myself?
   PL:
609. [Kwestia głosowa [gacksung_10408_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=gacksung_10408_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [gacksung_10408_1] (Uptying)] 그래, 끝을 볼 때가 왔군… 히스클리프. 네 놈은 내가 처리해야 할… '집안일'이니까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=gacksung_10408_1].dlg
   limit: do 160 znaków
   EN: Very well. It's about time we put an end to this, Heathcliff. Because you're... my 'housekeeping chore' to take care of.
   PL:
611. [Kwestia głosowa [formation_10408_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=formation_10408_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [formation_10408_1] (Deployment)] 주인놈 뜻에 따라, 준비 완료.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=formation_10408_1].dlg
   limit: do 120 znaków
   EN: Ready, as per that foolish Master's orders.
   PL:
613. [Kwestia głosowa [battleentry_10408_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battleentry_10408_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [battleentry_10408_1] (Stage Entry)] 헌팅 커틀러리, 준비 끝.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battleentry_10408_1].dlg
   limit: do 120 znaków
   EN: Hunting cutlery's at the ready.
   PL:
615. [Kwestia głosowa [battle_select_10408_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_select_10408_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [battle_select_10408_1] (Viewed in Battle)] 나대지 말고 내 뒤에 서있어라, 주인놈.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_select_10408_1].dlg
   limit: do 120 znaków
   EN: Quit it with your idiotic bravado and take cover behind me, you fool of a Master.
   PL:
617. [Kwestia głosowa [battle_endcommand_10408_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_endcommand_10408_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Kwestia głosowa [battle_endcommand_10408_1] (Commencing Attack)] 전투 응대에 나선다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_endcommand_10408_1].dlg
   limit: do 120 znaków
   EN: Headed out for a combat reception.
   PL:
619. [Kwestia głosowa [battle_enemy_break_10408_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_enemy_break_10408_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Kwestia głosowa [battle_enemy_break_10408_1] (Enemy Stagger)] 눈 감을 준비하고…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_enemy_break_10408_1].dlg
   limit: do 120 znaków
   EN: Get ready to close your eyes...
   PL:
621. [Kwestia głosowa [battle_break_10408_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_break_10408_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Kwestia głosowa [battle_break_10408_1] (Staggered)] 칫…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_break_10408_1].dlg
   limit: do 120 znaków
   EN: Tch…
   PL:
623. [Kwestia głosowa [battle_kill_10408_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_kill_10408_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Kwestia głosowa [battle_kill_10408_1] (Enemy Killed)] 즉시, 꿈을 꾸러 가도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_kill_10408_1].dlg
   limit: do 120 znaków
   EN: Go enjoy your dream. Now.
   PL:
625. [Kwestia głosowa [battle_dead_10408_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_dead_10408_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Kwestia głosowa [battle_dead_10408_1] (Death)] 쿨럭… 아직… 주인놈을 챙겨야… 하는데.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_dead_10408_1].dlg
   limit: do 120 znaków
   EN: Cough... I have to... protect my fool of a Master...
   PL:
627. [Kwestia głosowa [choice_success_p_10408_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=choice_success_p_10408_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Kwestia głosowa [choice_success_p_10408_2] (Check Passed)] 흥, 정돈 끝.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=choice_success_p_10408_2].dlg
   limit: do 120 znaków
   EN: Hmph, housekeeping complete.
   PL:
629. [Kwestia głosowa [choice_fail_n_10408_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=choice_fail_n_10408_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Kwestia głosowa [choice_fail_n_10408_1] (Check Failed)] 뭐, 업무 범위 이상이었다. 감당해라.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=choice_fail_n_10408_1].dlg
   limit: do 120 znaków
   EN: Well, this was beyond my obligations anyway. Suffer the consequences of your decision.
   PL:
631. [Kwestia głosowa [battle_clear_10408_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_clear_10408_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Kwestia głosowa [battle_clear_10408_1] (Victory Cry)] '집안일'을 해결했으면 일찍 돌아가지. 늦게 자고 내일 오전 업무를 대충하면 전부 모. 분이다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_clear_10408_1].dlg
   limit: do 200 znaków
   EN: If the 'housekeeping' is complete... let us return shortly. Don't stay up too late. I'll S.Y.N.C if I see that our morning duties were sloppily carried out.
   PL:
633. [Kwestia głosowa [battle_clear_ex_10408_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_clear_ex_10408_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Kwestia głosowa [battle_clear_ex_10408_1] (Extra Conditions Fulfilled)] 전투 응대는 성공적이었다. 나쁘지 않은 움직임이었어. 이제 다른 쪽 '집안일'로 돌아가지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_clear_ex_10408_1].dlg
   limit: do 160 znaków
   EN: That was a successful combat reception. Your moves weren't half bad... Now let us return to other 'housekeeping' work.
   PL:
635. [Kwestia głosowa [battle_defeat_10408_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_defeat_10408_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Kwestia głosowa [battle_defeat_10408_1] (Defeat Wail)] 사냥 실패다… 보완할 점이 많이 보이는군. 후, 버틀러들도 문제지만… 주인놈, 확실한 재교육이 필요하겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Butler_10408.json :: dataList[id=battle_defeat_10408_1].dlg
   limit: do 200 znaków
   EN: This hunt was a failure... There is so much that must be addressed. Not only the Butlers, but also... that fool of a Master. They'll need some re-education.
   PL:

## [00] District 20 Yurodivy — Ryōshū — 20구 유로지비
- ID Tożsamości: `10409` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 71 · szybkość: 4–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor

637. [Karta Tożsamości — tytuł] 20구\n유로지비
   źródło: Personalities.json :: dataList[id=10409].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: District 20\nYurodivy
   PL:
638. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10409].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10409].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Karta Tożsamości — opis] 료슈의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10409].desc
   limit: do 120 znaków
   EN: Ryōshū's 9th Identity
   PL:
641. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 나사빠진 놈들
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].name ; dataList[id=1040901].levelList[level=2].name ; dataList[id=1040901].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Got a Screw Loose?
   PL:
642. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL:
643. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 절반만큼 자신의 [Vibration] 횟수 증가 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to (([Vibration] Count on target)/2) (max 2)
   PL:
644. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040901].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
645. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +2</style>
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] At 5+ [Vibration] Count, Clash Power +2</style>
   PL:
646. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 절반만큼 자신의 [Vibration] 횟수 증가 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to (([Vibration] Count on target)/2) (max <style="highlight">3</style>)
   PL:
647. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수가 <style="highlight">4</style> 이상이면, 합 위력 +2
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n[WhenUse] At <style="highlight">4</style>+ [Vibration] Count, Clash Power +2
   PL:
648. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수만큼 자신의 [Vibration] 횟수 증가 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to ([Vibration] Count on target) (max <style="highlight">4</style>)
   PL:
649. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL:
650. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 압착 태엽 스패너
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].name ; dataList[id=1040902].levelList[level=2].name ; dataList[id=1040902].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Compression Wind-up Spanner
   PL:
651. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].desc
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL:
653. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 소모하여 소모한 [Vibration] 횟수만큼 대상의 [Vibration] 횟수 증가 (최대 5)
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1040902].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1040902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume [Vibration] Count on self, and inflict the same amount of [Vibration] Count on target (max 5)
   PL:
654. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">자신의 [Vibration] 횟수가 5 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">At 5+ [Vibration] Count, Coin Power +1</style>
   PL:
655. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +1 [Vibration] Count
   PL:
656. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 자신의 진동 횟수가 4 이상이면, 합 위력 +1</style>\n자신의 [Vibration] 횟수 <style="highlight">4</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] At 4+ [Vibration] Count, Clash Power +1</style>\nAt <style="highlight">4</style>+ [Vibration] Count, Coin Power +1
   PL:
657. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 두들기면 고쳐진다
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].name ; dataList[id=1040903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Percussive Maintenance
   PL:
659. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n자신의 [Vibration] 횟수 10 소모하여 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\nConsume 10 [Vibration] Count on self to gain Coin Power +1
   PL:
660. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
661. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1040903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 2
   PL:
663. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">8</style> 소모하여 코인 위력 +1\n<style="highlight">대상의 [Vibration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\nConsume <style="highlight">8</style> [Vibration] Count on self to gain Coin Power +1\n<style="highlight">If target has 6+ [Vibration], Coin Power +1</style>
   PL:
664. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 <style="highlight">1</style> 감소
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by <style="highlight">1</style>
   PL:
665. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-04.json :: dataList[id=1040904].levelList[level=1].name ; dataList[id=1040904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+6)
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 5)
   źródło: Skills_personality-04.json :: dataList[id=1040904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on self) as Shield HP (max 5)
   PL:
667. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 <style="highlight">10</style>)
   źródło: Skills_personality-04.json :: dataList[id=1040904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on self) as Shield HP (max <style="highlight">10</style>)
   PL:
668. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Sloth) — nazwa] 제.지
   źródło: Passives.json :: dataList[id=1040901].name
   limit: do 40 znaków
   EN: N.O.
   PL:
669. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Sloth) — opis] 자신을 제외한 아군의 공격으로 흐트러짐 상태가 된 적을 스킬 1로 공격함. (턴 당 1회)\n여러 적이 흐트러졌을 경우 체력이 가장 낮은 적(환상체일 때, 본체 우선 이후 부위)을 공격함.\n이 효과로 스킬 1을 사용할 때 코인 효과로 자신이 얻는 [Vibration] 횟수가 1 증가하고, 해당 스킬의 마지막 코인 적중시 [VibrationExplosion]
   źródło: Passives.json :: dataList[id=1040901].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationExplosion]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: - When another ally Staggers an enemy with an attack: follow up with a Skill 1 against the Staggered enemy. (once per Turn)\n- If multiple enemies are Staggered at once, target the enemy with the least HP(for Abnormalities, target the Abnormality with the least HP; then, target the Part with the least HP).\n- When using Skill 1 with this effect, this unit gains +1 more [Vibration] Count from its Coin effects, and triggers a [VibrationExplosion] with the last Coin On Hit
   PL:
670. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — nazwa] 조.감
   źródło: Passives.json :: dataList[id=1040921].name
   limit: do 40 znaków
   EN: The A.I.
   PL:
671. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — opis] 편성 순서가 1번인 아군이 스킬, 코인 효과로 얻는 [Vibration] 횟수의 값 +1 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1040921].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: #1 Deployed ally gains +1 more Tremor Count from their Skill or Coin effects (2 times per turn)
   PL:
672. [Kwestia głosowa [get_10409_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=get_10409_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Kwestia głosowa [get_10409_1] (Identity Acquisition)] 담배 한 갑에 굴착 나사 다섯? 그딴 소리를 하는 걸 보니, 네놈 머리에 나사가 빠졌나보군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=get_10409_1].dlg
   limit: do 120 znaków
   EN: 5 excavating screws for a pack of cigs? Sounds like you've got a screw loose yourself.
   PL:
674. [Kwestia głosowa [lobby_morning_10409_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=lobby_morning_10409_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Kwestia głosowa [lobby_morning_10409_1] (Morning Greeting)] …아침부터 수고롭게 움직이는군. 뭐, 근면함은 나쁘지 않지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=lobby_morning_10409_1].dlg
   limit: do 120 znaków
   EN: ... So busy, so early in the morning? Well, I do approve of your diligence.
   PL:
676. [Kwestia głosowa [lobby_noon_10409_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=lobby_noon_10409_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Kwestia głosowa [lobby_noon_10409_1] (Afternoon Greeting)] 이 시간만 되면 시간도 없는 놈들이 뒷골목에 어슬렁대더군.\n푸흣, 그러다가 결국 시간이 모자라 느려지는 모습이 제법 웃겨.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=lobby_noon_10409_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fools running low on time start stalking the Backstreets around this hour. I enjoy watching them eventually slow to a crawl when they inevitably run out of time; it's quite the amusing sight.
   PL:
678. [Kwestia głosowa [lobby_night_10409_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=lobby_night_10409_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Kwestia głosowa [lobby_night_10409_1] (Evening Greeting)] 슬슬 밤이군. 탐정 놈이 예술의 소재를 주는 시간이야… 하, 나는 이때가 아주 설레지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=lobby_night_10409_1].dlg
   limit: do 170 znaków
   EN: It's getting late... The detective will soon deliver me the ingredients for my art. Ah, I must admit that the thought excites me.
   PL:
680. [Kwestia głosowa [smalltalk_10409_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Kwestia głosowa [smalltalk_10409_1] (Chatter #1)] 다음은 단.테.인가?\n하, 시계… 너를 부른 게 아니다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Is it D.O.N. and T.E. next?\nHah, I wasn't talking to you... Clock.
   PL:
682. [Kwestia głosowa [smalltalk_10409_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Kwestia głosowa [smalltalk_10409_2] (Chatter #2)] 화폐는 결국 눈속임에 불과하지… 당장 쓸 수 있는 물건끼리 맞바꾸는 것이 훨씬 이치에 맞지 않다고 보지 않나.\n그것보다 좋은 건, 직접 공구를 들고 필요한 물품을 스스로 만들어 내는 것에 있지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_2].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Currency is just smoke and mirrors. It's much fairer to trade items of immediate worth instead, isn't it?\nOr even better, use that elbow grease and make your own.
   PL:
684. [Kwestia głosowa [smalltalk_10409_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Kwestia głosowa [smalltalk_10409_3] (Chatter #3)] 고장난 기계는… 때려야 말을 듣지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_3].dlg
   limit: do 120 znaków
   EN: I prefer to apply a certain... percussive method when it comes to fixing broken machines.
   PL:
686. [Kwestia głosowa [smalltalk_10409_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Kwestia głosowa [smalltalk_10409_4] (Post-Uptie Chat 1)] 담배가 타들어가는 건 시간이 흐른다는 것이고, 그 모습은 시간을 타고 죽음이 다가오는 것과 같지.\n여기 쓰러진 부자 놈처럼 말이야… 훗, 제법 전위적인 예술이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_4].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The tip of a lit cig, slowly burning itself away... A metaphor for the impending rider of death, atop the steed of time.\nIt's just like this rich pig whose time we burned away. Heh, quite avant-garde, isn't it?
   PL:
688. [Kwestia głosowa [smalltalk_10409_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Kwestia głosowa [smalltalk_10409_5] (Post-Uptie Chat 2)] 유로지비의 이념…? 관심 없다. 그저 그놈들의 활동에 담긴 미학이 마음에 들었을 뿐.\n돈 대신 물건으로 담배를 바꿔주는 것도 나쁘지 않았지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=smalltalk_10409_5].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Yurodiviye Ideology...? Who cares. I just found the aesthetics of their movement alluring.\nI don't mind paying for my cigs with items instead of cash, either.
   PL:
690. [Kwestia głosowa [neglect_10409_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=neglect_10409_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Kwestia głosowa [neglect_10409_1] (Idle)] 유로… 무료지비. 푸훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=neglect_10409_1].dlg
   limit: do 120 znaków
   EN: Yurodiviye... More like you're-all-divvied-up. Pfft.
   PL:
692. [Kwestia głosowa [gacksung_10409_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=gacksung_10409_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Kwestia głosowa [gacksung_10409_1] (Uptying)] 흥, 실컷 찍어라. 이왕이면 흩뿌린 피가 잘 담길 수 있게 찍어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=gacksung_10409_1].dlg
   limit: do 120 znaków
   EN: Hmph, fine—record all you want. Just make sure to get all the blood splatters.
   PL:
694. [Kwestia głosowa [formation_10409_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=formation_10409_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Kwestia głosowa [formation_10409_1] (Deployment)] 재밌군. 이건 내가 맡지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=formation_10409_1].dlg
   limit: do 120 znaków
   EN: This looks fun. I'll take this.
   PL:
696. [Kwestia głosowa [battleentry_10409_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battleentry_10409_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Kwestia głosowa [battleentry_10409_1] (Stage Entry)] 명단에 있는 놈들 모두 명.단.이다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battleentry_10409_1].dlg
   limit: do 120 znaków
   EN: This is a H.I.T. List. List of fools to be Hacked In Two, that is.
   PL:
698. [Kwestia głosowa [battle_select_10409_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_select_10409_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Kwestia głosowa [battle_select_10409_1] (Viewed in Battle)] 상대할 맛이 나는 놈들이면 좋겠군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_select_10409_1].dlg
   limit: do 120 znaków
   EN: They better give us a good fight.
   PL:
700. [Kwestia głosowa [battle_endcommand_10409_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_endcommand_10409_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Kwestia głosowa [battle_endcommand_10409_1] (Commencing Attack)] 타도한다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_endcommand_10409_1].dlg
   limit: do 120 znaków
   EN: Let's bring them down.
   PL:
702. [Kwestia głosowa [battle_enemy_break_10409_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_enemy_break_10409_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Kwestia głosowa [battle_enemy_break_10409_1] (Enemy Stagger)] 가진 놈들을 털고…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_enemy_break_10409_1].dlg
   limit: do 120 znaków
   EN: Shake down the loaded pigs...
   PL:
704. [Kwestia głosowa [battle_break_10409_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_break_10409_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Kwestia głosowa [battle_break_10409_1] (Staggered)] 쯧.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_break_10409_1].dlg
   limit: do 120 znaków
   EN: Tsk.
   PL:
706. [Kwestia głosowa [battle_kill_10409_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_kill_10409_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Kwestia głosowa [battle_kill_10409_1] (Enemy Killed)] 그 시간을 뿌리도록 하지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_kill_10409_1].dlg
   limit: do 120 znaków
   EN: ... and share the pilfered time with everyone.
   PL:
708. [Kwestia głosowa [battle_dead_10409_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_dead_10409_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Kwestia głosowa [battle_dead_10409_1] (Death)] 나쁘지 않아… 후. 결국 나도 재분배된다는… 점은.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_dead_10409_1].dlg
   limit: do 120 znaków
   EN: Even I end up 'redistributed'... Haah. Not bad, not bad...
   PL:
710. [Kwestia głosowa [choice_success_p_10409_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=choice_success_p_10409_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Kwestia głosowa [choice_success_p_10409_2] (Check Passed)] 봤나? 관람료는 원숭이 담배 한 갑.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=choice_success_p_10409_2].dlg
   limit: do 120 znaków
   EN: Were you watching? Then pay up. Pack of Monkey Cigs per view.
   PL:
712. [Kwestia głosowa [choice_fail_n_10409_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=choice_fail_n_10409_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Kwestia głosowa [choice_fail_n_10409_1] (Check Failed)] …이런 밋밋한 활동은 취향이 아냐.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=choice_fail_n_10409_1].dlg
   limit: do 120 znaków
   EN: ... This bland act isn't my scene.
   PL:
714. [Kwestia głosowa [battle_clear_10409_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_clear_10409_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Kwestia głosowa [battle_clear_10409_1] (Victory Cry)] 흠, 발명품이 잘 작동하는군… 기름만 좀 더 칠해줬어도 좋았겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_clear_10409_1].dlg
   limit: do 120 znaków
   EN: Hmm, not a bad invention... A bit more grease could've helped, however.
   PL:
716. [Kwestia głosowa [battle_clear_ex_10409_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_clear_ex_10409_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Kwestia głosowa [battle_clear_ex_10409_1] (Extra Conditions Fulfilled)] 완벽. 생각해 보니, 고철덩이 발명품으로 고장난 윗대가리를 부수는 것까지도 꽤 미학적이군…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_clear_ex_10409_1].dlg
   limit: do 200 znaków
   EN: Perfection. Now that I've given it some thought, I see the aesthetics in using such a janky invention to crush the janky brains of those who reign over us.
   PL:
718. [Kwestia głosowa [battle_defeat_10409_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_defeat_10409_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Kwestia głosowa [battle_defeat_10409_1] (Defeat Wail)] 이번 단.테.는 실패인가? 뭐, 상관없다. 숨이 붙어 있는 한 시간은 벌 수 있으니.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Yurodivy_10409.json :: dataList[id=battle_defeat_10409_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: So this D.O.N.T.E. didn't go as planned, did it? No deconstruction of normalcy, no one's terrified...\nWell, no matter. I can always make more time as long as I'm breathing.
   PL:

## [000] Lobotomy E.G.O:: Red Eyes & Penitence — Ryōshū — 로보토미 E.G.O:: 적안・참회
- ID Tożsamości: `10410` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9104 · HP bazowe: 69 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Bleed

720. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n적안・참회
   źródło: Personalities.json :: dataList[id=10410].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nRed Eyes &\nPenitence
   PL:
721. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10410].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10410].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Karta Tożsamości — opis] 료슈의 열번째 인격
   źródło: Personalities.json :: dataList[id=10410].desc
   limit: do 120 znaków
   EN: Ryōshū's 10th Identity
   PL:
724. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 둘 다 닥쳐라
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=1].name ; dataList[id=1041001].levelList[level=2].name ; dataList[id=1041001].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Both of You, Shut Up
   PL:
725. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 3 [PenanceFirst]
   PL:
726. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst]
   PL:
727. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[RedEyeFirst]이 7 이상이면, 코인 위력 +1\n[PenanceFirst]가 7 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: <style="highlight">At 7+ [RedEyeFirst], Coin Power +1\nAt 7+ [PenanceFirst], Clash Power +1</style>
   PL:
728. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 3 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 3 [PenanceFirst]<style="highlight"></style>
   PL:
729. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst]<style="highlight"></style>
   PL:
730. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Laceration] 1 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Laceration]</style>
   PL:
731. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [RedEyeFirst]이 7 이상이면, 코인 위력 +1\n[PenanceFirst]가 7 이상이면, 합 위력 <style="highlight">+2</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: At 7+ [RedEyeFirst], Coin Power +1\nAt 7+ [PenanceFirst], Clash Power <style="highlight">+2</style>
   PL:
732. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 3 얻음\n<style="highlight">[OnSucceedAttackHead] [PenanceFirst] 1 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst], [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence; [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttack] Gain 3 [PenanceFirst]\n<style="highlight">[OnSucceedAttackHead] Gain 1 [PenanceFirst]</style>
   PL:
733. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL:
734. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 거.대 / 해.바
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].name ; dataList[id=1041002].levelList[level=2].name ; dataList[id=1041002].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: S.H. / S.F.
   PL:
735. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [RedEyeFirst]과 [PenanceFirst]의 합이 20 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: If the sum of [RedEyeFirst] and [PenanceFirst] is 20 or higher, Coin Power +1
   PL:
736. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 4 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 4 [PenanceFirst]
   PL:
737. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 3 [RedEyeFirst]
   PL:
738. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
739. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [RedEyeFirst]과 [PenanceFirst]의 합이 20 이상이면, 코인 위력 +1\n<style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst], [Laceration]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [Laceration] = 출혈 / Bleed
   EN: If the sum of [RedEyeFirst] and [PenanceFirst] is 20 or higher, Coin Power +1\n<style="highlight">If target has 6+ [Laceration], Coin Power +1</style>
   PL:
740. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 4 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 4 [PenanceFirst]<style="highlight"></style>
   PL:
741. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 3 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 3 [RedEyeFirst]<style="highlight"></style>
   PL:
742. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL:
743. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 대상의 ([Laceration]/3)만큼 [RedEyeFirst] 얻음 (최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [RedEyeFirst] = 적안 / Red Eyes
   EN: <style="highlight">[OnSucceedAttack] Gain [RedEyeFirst] equal to ([Laceration] on target/3) (max 2)</style>
   PL:
744. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [RedEyeFirst]과 [PenanceFirst]의 합이 <style="highlight">15</style> 이상이면, 코인 위력 +1\n대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst], [Laceration]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [Laceration] = 출혈 / Bleed
   EN: If the sum of [RedEyeFirst] and [PenanceFirst] is <style="highlight">15</style> or higher, Coin Power +1\nIf target has 6+ [Laceration], Coin Power +1
   PL:
745. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 ([Laceration]/<style="highlight">2</style>)만큼 [RedEyeFirst] 얻음 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain [RedEyeFirst] equal to ([Laceration] on target/<style="highlight">2</style>) (max <style="highlight">3</style>)
   PL:
746. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [RedEyeFirst]이 7 이상이면, 다음 턴에 [Agility] 1 얻음 (턴 당 2회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [RedEyeFirst], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [RedEyeFirst] = 적안 / Red Eyes; [Agility] = 신속 / Haste
   EN: <style="highlight">[OnSucceedAttackHead] At 7+ [RedEyeFirst], gain 1 [Agility] next turn (2 times per turn)</style>
   PL:
747. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대가리 터트리기
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].name ; dataList[id=1041003].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Skullbuster
   PL:
748. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] [RedEyeFirst]과 [PenanceFirst]가 각각 15 이상이면, '진심 대가리 터트리기'로 발동됨\n대상의 속도가 자신보다 3 이상 느리면, 코인 위력 +1\n[WhenUse] 정신력이 최대일 경우, 코인 위력 +1\n- [EndSkill] 이 효과가 발동되었다면 정신력 15 감소
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [RedEyeFirst], [PenanceFirst], [WhenUse], [EndSkill]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeUse] If [RedEyeFirst] and [PenanceFirst] are both at 15+, activate 'Serious Skullbuster' instead\nIf this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] At max SP, Coin Power +1\n- [EndSkill] If this effect activated, lose 15 SP
   PL:
749. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 7 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 7 [RedEyeFirst]
   PL:
750. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PenanceFirst] 7 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 7 [PenanceFirst]
   PL:
751. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 738 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 ([PenanceFirst]/3)%만큼 체력 회복
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by ([PenanceFirst]/3)% of each unit's max HP
   PL:
753. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 ([PenanceFirst]-10)만큼 정신력 회복 (최소 0)
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] - 10) SP (min 0)
   PL:
754. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] [RedEyeFirst]과 [PenanceFirst]가 각각 15 이상이면, '진심 대가리 터트리기'로 발동됨\n대상의 속도가 <style="highlight">자신보다 느리면</style>, 코인 위력 +1\n[WhenUse] 정신력이 최대일 경우, <style="highlight">합 위력 +2</style>, 코인 위력 +1\n- [EndSkill] 이 효과가 발동되었다면 정신력 15 감소
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [RedEyeFirst], [PenanceFirst], [WhenUse], [EndSkill]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeUse] If [RedEyeFirst] and [PenanceFirst] are both at 15+, activate 'Serious Skullbuster' instead\nIf this unit's Speed <style="highlight">is faster than the target's</style>, Coin Power +1\n[WhenUse] At max SP, <style="highlight">Clash Power +2</style> and Coin Power +1\n- [EndSkill] If this effect activated, lose 15 SP
   PL:
755. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 7 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 7 [RedEyeFirst]<style="highlight"></style>
   PL:
756. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PenanceFirst] 7 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 7 [PenanceFirst]<style="highlight"></style>
   PL:
757. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration]
   PL:
758. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttackHead] [PenanceFirst] 2 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [PenanceFirst] = 참회 / Penitence
   EN: <style="highlight">[OnSucceedAttackHead] Gain 2 [PenanceFirst]</style>
   PL:
759. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 ([PenanceFirst]/<style="highlight">2</style>)%만큼 체력 회복
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by ([PenanceFirst]/<style="highlight">2</style>)% of each unit's max HP
   PL:
760. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 ([PenanceFirst]-10)만큼 정신력 회복 (최소 0)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] - 10) SP (min 0)<style="highlight"></style>
   PL:
761. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 진심 대가리 터트리기
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].name ; dataList[id=1041005].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Serious Skullbuster
   PL:
762. [Umiejętność 4 (×0) (ulepszenia 3–4) — opis] [WhenUse] 보유 중인 [RedEyeFirst]과 [PenanceFirst]를 전부 소모\n- 소모한 [RedEyeFirst] 5당 코인 위력 +1 (최대 4)\n- 소모한 [PenanceFirst] 5당 기본 위력 +1 (최대 4)\n[EndSkill] 정신력이 15 감소하고 다음 턴에 [Emptiness] 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].desc ; dataList[id=1041005].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [RedEyeFirst], [PenanceFirst], [EndSkill], [Emptiness]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [EndSkill] = [공격 종료시] / [Attack End]; [Emptiness] = 하얗게 태워버렸군 / Only Ashes Remain
   EN: [WhenUse] Consume all [RedEyeFirst] and [PenanceFirst] on self\n- Coin Power +1 for every 5 [RedEyeFirst] consumed (max 4)\n- Base Power +1 for every 5 [PenanceFirst] consumed (max 4)\n[EndSkill] Lose 15 SP and gain [Emptiness] next turn
   PL:
763. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (소모한 [RedEyeFirst]-15)만큼 [Laceration] 부여 (최대 5)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict [Laceration] equal to ([RedEyeFirst] consumed - 15) on target (max 5)
   PL:
764. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] 소모한 [RedEyeFirst], [PenanceFirst]당 피해량 +2.5% (최대 100%)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: Deal +2.5% damage for every [RedEyeFirst] and [PenanceFirst] consumed (max 100%)
   PL:
765. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 (소모한 [PenanceFirst]/2)%만큼 체력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by ([PenanceFirst] consumed / 2)% of each unit's max HP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL:
766. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 (소모한 [PenanceFirst]-10)만큼 정신력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] consumed - 10) SP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL:
767. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3, [Reduction] 2 부여 (턴 당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 3 [Binding] and 2 [Reduction] next turn (once per turn)
   PL:
768. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (소모한 [RedEyeFirst]-15)만큼 [Laceration] 부여 (최대 5)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict [Laceration] equal to ([RedEyeFirst] consumed - 15) on target (max 5)<style="highlight"></style>
   PL:
769. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 소모한 [RedEyeFirst], [PenanceFirst]당 피해량 <style="highlight">+4%</style> (최대 <style="highlight">160%</style>)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: Deal <style="highlight">+4%</style> damage for every [RedEyeFirst] and [PenanceFirst] consumed (max <style="highlight">160%</style>)
   PL:
770. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 <style="highlight">(소모한 [PenanceFirst])%</style>만큼 체력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by <style="highlight">([PenanceFirst] consumed)%</style> of each unit's max HP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL:
771. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 (소모한 [PenanceFirst]-<style="highlight">5</style>)만큼 정신력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] consumed - <style="highlight">5</style>) SP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL:
772. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3, [Reduction] 2 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 3 [Binding] and 2 [Reduction] next turn (once per turn)<style="highlight"></style>
   PL:
773. [Obrona (ulepszenia 1,4) — nazwa] 먹고 잘 시간이다
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=1].name ; dataList[id=1041004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Mealtime, Bedtime
   PL:
774. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst] (once per turn)
   PL:
775. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 2 [PenanceFirst] (once per turn)
   PL:
776. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음 (턴 당 1회)\n<style="highlight">- [RedEyeFirst]이 7 미만이면, [RedEyeFirst] 1 추가로 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst] (once per turn)\n<style="highlight">- At less than 7 [RedEyeFirst], gain +1 additional [RedEyeFirst]</style>
   PL:
777. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 2 얻음 (턴 당 1회)\n<style="highlight">- [PenanceFirst]가 7 미만이면, [PenanceFirst] 1 추가로 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 2 [PenanceFirst] (once per turn)\n<style="highlight">- At less than 7 [PenanceFirst], gain +1 additional [PenanceFirst]</style>
   PL:
778. [Pasywka bojowa (od ulepszenia 1) — nazwa] E.G.O 동화
   źródło: Passives.json :: dataList[id=1041002].name
   limit: do 40 znaków
   EN: E.G.O Assimilation
   PL:
779. [Pasywka bojowa (od ulepszenia 1) — opis] [Charge] 횟수를 획득할 때, 대신 [RedEyeFirst] 또는 [PenanceFirst]를 얻음\n- [RedEyeFirst]과 [PenanceFirst]는 [Charge] 위력의 영향을 받지 않음
   źródło: Passives.json :: dataList[id=1041002].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [Charge] = 충전 / Charge; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: When gaining [Charge] Count, gain [RedEyeFirst] or [PenanceFirst] instead\n- [RedEyeFirst] and [PenanceFirst] are unaffected by [Charge] Potency
   PL:
780. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 충전 횟수를 획득할 때, 대신 적안 또는 참회를 얻음
   źródło: Passives.json :: dataList[id=1041002].summary
   limit: do 120 znaków
   EN: When gaining Charge Count, gain Red Eyes or Penitence instead
   PL:
781. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Gloom) — nazwa] 거미대가리 / 해골바가지
   źródło: Passives.json :: dataList[id=1041001].name
   limit: do 40 znaków
   EN: Spiderhead/Skullface
   PL:
782. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Gloom) — opis] [RedEyeFirst]을 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([RedEyeFirst]/2)%만큼 증가\n- 대상에게 [Laceration]이 있으면, [RedEyeFirst] 1 얻음 (턴 당 최대 3)\n\n[PenanceFirst]를 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([PenanceFirst]/2)%만큼 증가\n- 자신의 정신력이 20 이상이면 [PenanceFirst] 1 얻음 (턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1041001].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [RedEyeFirst], [Laceration], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed; [PenanceFirst] = 참회 / Penitence
   EN: When hitting an enemy with a Coin that gains [RedEyeFirst]:\n- Deal +([RedEyeFirst]/2)% damage\n- If the target has [Laceration], gain 1 [RedEyeFirst] (3 times per turn)\n\nWhen hitting an enemy with a Coin that gains [PenanceFirst]:\n- Deal +([PenanceFirst]/2)% damage\n- At 20+ SP, gain 1 [PenanceFirst] (3 times per turn)
   PL:
783. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Gloom) — podsumowanie] 적안 얻는 코인의 피해량이 증가. 대상에게 출혈이 있으면, 적안 1 얻음\n참회 얻는 코인의 피해량이 증가. 자신의 정신력이 20 이상이면 참회 1 얻음
   źródło: Passives.json :: dataList[id=1041001].summary
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coins that gain Red Eyes deal more damage; if the target has Bleed, gain 1 Red Eyes\nCoins that gain Penitence deal more damage; at 20+ SP, gain 1 Penitence
   PL:
784. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Gloom) — nazwa] 거미대가리 / 해골바가지
   źródło: Passives.json :: dataList[id=1041011].name
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Gloom) — opis] [RedEyeFirst]을 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([RedEyeFirst]/2)%만큼 증가\n<style="highlight">- 대상의 속도가 자신보다 3 이상 낮으면, 피해량이 ([RedEyeFirst]/2)%만큼 추가로 증가</style>\n- 대상에게 [Laceration]이 있으면, [RedEyeFirst] 1 얻음 (턴 당 최대 3)\n\n[PenanceFirst]를 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([PenanceFirst]/2)%만큼 증가\n<style="highlight">- 대상의 정신력이 자신보다 낮으면, 피해량이 ([PenanceFirst]/2)%만큼 추가로 증가 (정신력이 없는 대상일 경우, 0으로 계산)</style>\n- 자신의 정신력이 20 이상이면 [PenanceFirst] 1 얻음 (턴 당 최대 3)\n\n<style="highlight">적에게 피격 시, [PenanceFirst] 1 얻음 (최대 3)</style>
   źródło: Passives.json :: dataList[id=1041011].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [Laceration], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed; [PenanceFirst] = 참회 / Penitence
   EN: When hitting an enemy with a Coin that gains [RedEyeFirst]:\n- Deal +([RedEyeFirst]/2)% damage\n<style="highlight">- If this unit's Speed is faster than the target's by 3 or more, deal an additional +([RedEyeFirst]/2)% damage</style>\n- If the target has [Laceration], gain 1 [RedEyeFirst] (3 times per turn)\n\nWhen hitting an enemy with a Coin that gains [PenanceFirst]:\n- Deal +([PenanceFirst]/2)% damage\n<style="highlight">- If the target's SP is lower than this unit's, deal an additional +([PenanceFirst]/2)% damage(for targets that are Non-SP Units, their SP counts as 0)</style>\n- At 20+ SP, gain 1 [PenanceFirst] (3 times per turn)\n\n<style="highlight">When hit by an enemy, gain 1 [PenanceFirst] (max 3)</style>
   PL:
786. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Gloom) — podsumowanie] 적안 얻는 코인의 피해량이 증가. 대상에게 출혈이 있으면, 적안 1 얻음\n참회 얻는 코인의 피해량이 증가. 자신의 정신력이 20 이상이면 참회 1 얻음\n적에게 피격 시, 참회 1 얻음 (최대 3)
   źródło: Passives.json :: dataList[id=1041011].summary
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coins that gain Red Eyes deal more damage; if the target has Bleed, gain 1 Red Eyes\nCoins that gain Penitence deal more damage; at 20+ SP, gain 1 Penitence\nWhen hit by an enemy, gain 1 Penitence (max 3)
   PL:
787. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — nazwa] 먹고 자라
   źródło: Passives.json :: dataList[id=1041021].name
   limit: do 40 znaków
   EN: Eat and Sleep
   PL:
788. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — opis] 전투 시작 시\n- 체력 비율이 제일 낮은 아군 1명이 체력 3 회복\n- 정신력이 제일 낮은 아군 1명이 정신력 3 회복
   źródło: Passives.json :: dataList[id=1041021].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Combat Start:\n- 1 ally with the lowest HP percentage heals 3 HP\n- 1 ally with the least SP heals 3 SP
   PL:
789. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — podsumowanie] 체력 비율 제일 낮은 아군 체력 회복, 정신력 제일 낮은 아군 정신력 회복
   źródło: Passives.json :: dataList[id=1041021].summary
   limit: do 120 znaków
   EN: Heal HP for 1 ally with the lowest HP percentage, heal SP for 1 ally with the least SP
   PL:
790. [Kwestia głosowa [get_10410_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=get_10410_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Kwestia głosowa [get_10410_1] (Identity Acquisition)] 이제야 좀 마주볼만한 눈빛이 됐군. 그래, 난 네놈의 사냥감이 아니다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=get_10410_1].dlg
   limit: do 120 znaków
   EN: I like this new look in your eyes. You've finally understood that I am *not* your prey.
   PL:
792. [Kwestia głosowa [lobby_morning_10410_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=lobby_morning_10410_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Kwestia głosowa [lobby_morning_10410_1] (Morning Greeting)] 별도 달도 없는 천장에 매달려만 있으니 종일 한밤중이나 다름없군.\n쯧, 나도 마찬가지인가.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=lobby_morning_10410_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I suppose forever hanging from the starless, moonless ceiling is like living in an unending night.\n... Tsk, I suppose I'm not the one to talk.
   PL:
794. [Kwestia głosowa [lobby_noon_10410_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=lobby_noon_10410_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Kwestia głosowa [lobby_noon_10410_1] (Afternoon Greeting)] 자색 정오라… 또 한 번 아수라장이 펼쳐질 시간이지. 훗, 이번에도 어디서 왔는지 모를 그 예술적인 비석을 구경할 수 있겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=lobby_noon_10410_1].dlg
   limit: do 240 znaków
   EN: The Noon of Violet, is it? Sounds like an opportunity to see all hell break loose again. Heh, I'm looking forward to getting another look at that mysterious, artistically inspiring stele.
   PL:
796. [Kwestia głosowa [lobby_night_10410_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=lobby_night_10410_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Kwestia głosowa [lobby_night_10410_1] (Evening Greeting)] 슬슬 그 격리실에서 실종된 놈들의 목소리가 들릴 시간이다. 뭐, 자장가로는 딱이군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=lobby_night_10410_1].dlg
   limit: do 180 znaków
   EN: We'll soon be hearing the voices of the fools who went 'missing' in that containment unit. Isn't this a nice lullaby to fall asleep to?
   PL:
798. [Kwestia głosowa [smalltalk_10410_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Kwestia głosowa [smalltalk_10410_1] (Chatter #1)] 고치가 늘었나. 저 안의 머저리들을 구해줄 생각은 조금도 없다만, 감상이 빨리 끝나게 되는 건 아쉽군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_1].dlg
   limit: do 170 znaków
   EN: More cocoons, is it? Disappointing. I thought I'd have some more time to enjoy the show. Not that I'd bother saving them, of course.
   PL:
800. [Kwestia głosowa [smalltalk_10410_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Kwestia głosowa [smalltalk_10410_2] (Chatter #2)] 네놈이 고치를 만드는 이유가 제 새끼를 배불리 먹이기 위함이었나…\n흥, 그 따위 마음은 그저 저주받은 본성에 지나지 않지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_2].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You've been making all these cocoons just to feed your children...?\nHmph. It's nothing more than the curse of instinct.
   PL:
802. [Kwestia głosowa [smalltalk_10410_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Kwestia głosowa [smalltalk_10410_3] (Chatter #3)] 그 빌어먹을 초록 깡통은 아직도 엔케팔린에 취해있을 테지.\n안전팀에 대해 궁금한 게 있다면 등에 관을 메고 다니는 음침한 놈에게 물어라.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_3].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: That green tincan's probably still hopped up on Enkephalin.\nIf you've got any questions about the Safety Team, go ask that depressing guy wearing a coffin like it's a backpack.
   PL:
804. [Kwestia głosowa [smalltalk_10410_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Kwestia głosowa [smalltalk_10410_4] (Post-Uptie Chat 1)] 이 거미대가리랑 마음이 맞아서 해골바가지도 휘두르게 된 건 마음에 들지만, 쓸데없이 시끄럽게 구는 건 별로다.\n한 놈은 툭하면 밥 달라 징징거리고, 다른 한 놈은 선이니 정의니 종일 훈수질이더군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I like that my affinity with Spiderhead's allowed me to wield Skullface as well... but their endless chatter is getting annoying.\nOne constantly nagging me for food, the other lecturing me about 'the good' and 'justice' every other minute...
   PL:
806. [Kwestia głosowa [smalltalk_10410_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Kwestia głosowa [smalltalk_10410_5] (Post-Uptie Chat 2)] 안 싸울 겁쟁이들은 걸리적거리지 않게 엘리베이터에 처박혀 있어라.\n싸울 놈들은 뭉쳐서 가만히 서 있도록. 움직이다 그놈이 빗맞추면, 그대로 찌.부.다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=smalltalk_10410_5].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stay cooped up in the elevator if you're not going to fight, cowards.\nIf you're willing to fight, merge up and stand still. If the manager misses because you couldn't even sit still for a minute... then you better get ready to get F.L.A.T.
   PL:
808. [Kwestia głosowa [neglect_10410_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=neglect_10410_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Kwestia głosowa [neglect_10410_1] (Idle)] 주변이 조용하군. 관리자 놈… 미리 처분 탄환이라도 쏘고 있었나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=neglect_10410_1].dlg
   limit: do 120 znaków
   EN: This silence... Is that fool of a manager already unloading Execution Bullets?
   PL:
810. [Kwestia głosowa [gacksung_10410_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=gacksung_10410_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Kwestia głosowa [gacksung_10410_1] (Uptying)] 이렇게 잘 길들여진 E.G.O를 본적이 있나? 이 눈 많은 무기는 남의 것 같지 않단 말이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=gacksung_10410_1].dlg
   limit: do 120 znaków
   EN: Ever seen an E.G.O this well-tamed? This multi-eyed one just feels so natural in my hand.
   PL:
812. [Kwestia głosowa [formation_10410_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=formation_10410_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Kwestia głosowa [formation_10410_1] (Deployment)] 자, 해골바가지랑 거미대가리. 후드려 패러 간다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=formation_10410_1].dlg
   limit: do 120 znaków
   EN: Time to go, Skullface and Spiderhead. Let's flatten them.
   PL:
814. [Kwestia głosowa [battleentry_10410_1] — sytuacja] 입장 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battleentry_10410_1].desc
   limit: do 120 znaków
   EN: Stage Entry 1
   PL:
815. [Kwestia głosowa [battleentry_10410_1] (Stage Entry 1)] 닥쳐라, 해.바. 누굴 팰진 내가 정한다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battleentry_10410_1].dlg
   limit: do 120 znaków
   EN: Shut up, S.F. I decide whose skull to bust.
   PL:
816. [Kwestia głosowa [battleentry_10410_2] — sytuacja] 입장 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battleentry_10410_2].desc
   limit: do 120 znaków
   EN: Stage Entry 2
   PL:
817. [Kwestia głosowa [battleentry_10410_2] (Stage Entry 2)] 기다려라, 거.대. 곧 먹이를 먹여주지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battleentry_10410_2].dlg
   limit: do 120 znaków
   EN: Patience, S.H. I'll feed you something soon.
   PL:
818. [Kwestia głosowa [battle_select_10410_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_select_10410_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Kwestia głosowa [battle_select_10410_1] (Viewed in Battle)] 이 눈들을 너무 오래 보고 있지 마라. 홀려버려도 구해주지 않을 테니.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_select_10410_1].dlg
   limit: do 120 znaków
   EN: Don't stare at these eyes for too long. I won't help you if it snares you in its trance.
   PL:
820. [Kwestia głosowa [battle_endcommand_10410_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_endcommand_10410_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Kwestia głosowa [battle_endcommand_10410_1] (Commencing Attack)] 대가리 딱 대도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_endcommand_10410_1].dlg
   limit: do 120 znaków
   EN: Get ready to have your skull cracked open.
   PL:
822. [Kwestia głosowa [battle_enemy_break_10410_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_enemy_break_10410_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Kwestia głosowa [battle_enemy_break_10410_1] (Enemy Stagger)] 먹기 좋게 차려졌지 않나. 거.대.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_enemy_break_10410_1].dlg
   limit: do 120 znaków
   EN: Isn't this a nice spread for a meal, S.H?
   PL:
824. [Kwestia głosowa [battle_break_10410_1] — sytuacja] 흐트러질 시 대사 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_break_10410_1].desc
   limit: do 120 znaków
   EN: Staggered 1
   PL:
825. [Kwestia głosowa [battle_break_10410_1] (Staggered 1)] 나도 아니까 닥쳐라…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_break_10410_1].dlg
   limit: do 120 znaków
   EN: I know. Shut up.
   PL:
826. [Kwestia głosowa [battle_break_10410_2] — sytuacja] 흐트러질 시 대사 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_break_10410_2].desc
   limit: do 120 znaków
   EN: Staggered 2
   PL:
827. [Kwestia głosowa [battle_break_10410_2] (Staggered 2)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_break_10410_2].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
828. [Kwestia głosowa [battle_kill_10410_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_kill_10410_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Kwestia głosowa [battle_kill_10410_1] (Enemy Killed)] 내 죄는 내가 알아서 처리한다, 해.바.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_kill_10410_1].dlg
   limit: do 120 znaków
   EN: My sins are mine to deal with, S.F.
   PL:
830. [Kwestia głosowa [battle_dead_10410_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_dead_10410_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Kwestia głosowa [battle_dead_10410_1] (Death)] 눈들이 감기고… 빛이 꺼지는군…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_dead_10410_1].dlg
   limit: do 120 znaków
   EN: The eyes close shut... and the lights... fade...
   PL:
832. [Kwestia głosowa [choice_success_p_10410_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=choice_success_p_10410_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Kwestia głosowa [choice_success_p_10410_2] (Check Passed)] 애착을 갖고 들여다 볼 가치가 있는 예술이었다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=choice_success_p_10410_2].dlg
   limit: do 120 znaków
   EN: That art was worth a closer inspection.
   PL:
834. [Kwestia głosowa [choice_fail_n_10410_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=choice_fail_n_10410_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Kwestia głosowa [choice_fail_n_10410_1] (Check Failed)] 환상체 도감은 읽고 지시를 내린 건가, 관리자?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=choice_fail_n_10410_1].dlg
   limit: do 120 znaków
   EN: Manager. Did you even read the Observation Logs?
   PL:
836. [Kwestia głosowa [battle_clear_10410_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_clear_10410_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Kwestia głosowa [battle_clear_10410_1] (Victory Cry)] 하, 다른 부서도 벌써 한바탕 했나. 돌아가는 길에 구경할 작품이 많아졌겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_clear_10410_1].dlg
   limit: do 150 znaków
   EN: Hah, looks like the other departments have been busy. Looking forward to enjoying an art gallery on my way back.
   PL:
838. [Kwestia głosowa [battle_clear_ex_10410_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_clear_ex_10410_1].desc
   limit: do 120 znaków
   EN: Extra Condition Fulfilled
   PL:
839. [Kwestia głosowa [battle_clear_ex_10410_1] (Extra Condition Fulfilled)] 착각하지 마라… 해.바, 거.대. 네놈들 덕에 내가 강해진 게 아니다. 내가 강하기에 네놈들을 휘두르는 거지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_clear_ex_10410_1].dlg
   limit: do 140 znaków
   EN: Don't delude yourselves, S.F, S.H. I'm not strong because I wield you. I wield you *because* I am strong.
   PL:
840. [Kwestia głosowa [battle_defeat_10410_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_defeat_10410_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Kwestia głosowa [battle_defeat_10410_1] (Defeat Wail)] 곧 감미로운 트럼펫 경보와 비명 소리가 들릴 거다. 잘나신 관리자 놈이 수습하겠다고 또 난리를 피울 테지. 꽤 재밌는 관람이 되겠군… 훗.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Spider_10410.json :: dataList[id=battle_defeat_10410_1].dlg
   limit: do 250 znaków
   EN: We'll soon hear the sweet melodies of the trumpets followed by a harmony of screams. The dear manager'll have a hell of a time cleaning this mess up. I'm looking forward to enjoying it... heh.
   PL:

## [000] Heishou Pack - Mao Branch — Ryōshū — 흑수 - 묘
- ID Tożsamości: `10411` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

842. [Karta Tożsamości — tytuł] 흑수 - 묘
   źródło: Personalities.json :: dataList[id=10411].title
   limit: do 40 znaków
   EN: Heishou Pack - Mao Branch
   PL:
843. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10411].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10411].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Karta Tożsamości — opis] 료슈의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10411].desc
   limit: do 120 znaków
   EN: Ryōshū's 11th Identity
   PL:
846. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순보
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].name ; dataList[id=1041101].levelList[level=2].name ; dataList[id=1041101].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Blinkstep
   PL:
847. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1
   PL:
848. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
849. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
850. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[WinDuel] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[WinDuel] Inflict +1 [Burst] Count</style>
   PL:
851. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL:
852. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL:
853. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)</style>
   PL:
854. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL:
855. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)<style="highlight"></style>
   PL:
856. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 새겨진대로
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].name ; dataList[id=1041102].levelList[level=2].name ; dataList[id=1041102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: As Written
   PL:
857. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n[WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n[WhenUse] If target has 6+ [Burst], Coin Power +1
   PL:
858. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +10% damage
   PL:
860. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n[WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [Agility], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n[WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Inflict +1 [Burst] Count</style>
   PL:
861. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 10 이상이면, [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] At 10+ Speed, inflict +1 [Burst] Count</style>
   PL:
863. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +<style="highlight">20</style>%
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +<style="highlight">20</style>% damage
   PL:
864. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [Agility], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Inflict +1 [Burst] Count
   PL:
865. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 10+ Speed, inflict +1 [Burst] Count<style="highlight"></style>
   PL:
866. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +<style="highlight">30</style>%
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +<style="highlight">30</style>% damage
   PL:
867. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Burst]</style>
   PL:
868. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 저주가 새겨진 검을 쑤셔주지
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].name ; dataList[id=1041103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: I'll gut you with a curse-engraved blade
   PL:
869. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL:
870. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL:
872. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +30% damage
   PL:
874. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
875. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)
   PL:
876. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 <style="highlight">높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)\n[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1</style>\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's, <style="highlight">gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)\n[WhenUse] If target has 15+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL:
877. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 852 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]<style="highlight"></style>
   PL:
879. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +30% damage<style="highlight"></style>
   PL:
881. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]<style="highlight"></style>
   PL:
882. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstAgility]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict [BurstAgility]</style>
   PL:
884. [Obrona (ulepszenia 1,4) — nazwa] 각력. 해방. 훗
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=1].name ; dataList[id=1041104].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Strider. Unleashed. Heh
   PL:
885. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] [LegStrength] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[WhenUse] Gain 3 [LegStrength]
   PL:
886. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] [LegStrength] 3 얻음\n<style="highlight">[WhenUse] 자신의 속도가 대상보다 높을수록, 기본 위력 +1 (속도 차이 2 당 기본 위력 +1. 최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[WhenUse] Gain 3 [LegStrength]\n<style="highlight">[WhenUse] If this unit's Speed is faster than the target's, gain Base Power based on Speed difference (Base Power +1 for every 2 Speed difference; max 2)</style>
   PL:
888. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 852 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 흑수화[묘]
   źródło: Passives.json :: dataList[id=1041101].name
   limit: do 40 znaków
   EN: Heishou Mutation [Mao]
   PL:
890. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 자신에게 [LegStrength]가 있으면 가하는 피해량 +5%
   źródło: Passives.json :: dataList[id=1041101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LegStrength]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: If this unit has [LegStrength], deal +5% damage
   PL:
891. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — nazwa] 흑수화[묘]
   źródło: Passives.json :: dataList[id=1041111].name
   (powtórzenie elementu 889 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — opis] 자신에게 [LegStrength]가 있으면 가하는 피해량 +5%\n대상에게 [BurstAgility]이 있으면 가하는 피해량 +5%
   źródło: Passives.json :: dataList[id=1041111].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [LegStrength], [BurstAgility]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: If this unit has [LegStrength], deal +5% damage\nIf the target has [BurstAgility], deal +5% damage
   PL:
893. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 부분 흑수화 수련
   źródło: Passives.json :: dataList[id=1041121].name
   limit: do 50 znaków
   EN: Partial Heishou Mutation Training
   PL:
894. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 턴 종료시 속도가 가장 빠른 아군 1명이 다음 턴에 [Agility] 2 얻음
   źródło: Passives.json :: dataList[id=1041121].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Turn End: 1 ally with the fastest Speed gains 2 [Agility] next turn
   PL:
895. [Kwestia głosowa [get_10411_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=get_10411_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Kwestia głosowa [get_10411_1] (Identity Acquisition)] 아직 정해진 시기가 되지 않았으니… 이 고. 담. 정도는 끝까지 태워도 되겠지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=get_10411_1].dlg
   limit: do 120 znaków
   EN: I still have some time... to finish smoking this L.C.
   PL:
897. [Kwestia głosowa [lobby_morning_10411_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=lobby_morning_10411_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Kwestia głosowa [lobby_morning_10411_1] (Morning Greeting)] 머저리들이 바삐 움직이는 걸 보니 단잠의 시간이군. …몰랐나? 토끼는 원래 야행성이다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=lobby_morning_10411_1].dlg
   limit: do 140 znaków
   EN: Look at those idiots busily prancing about... time to sleep. ... Didn't you know? Hares are nocturnal.
   PL:
899. [Kwestia głosowa [lobby_noon_10411_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=lobby_noon_10411_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Kwestia głosowa [lobby_noon_10411_1] (Afternoon Greeting)] 이 시간에 한 대 피워두지 않으면, 나중에 태울 틈이 나지 않더군.\n그림자에 제대로 절여진 짐승들을 불러들일 생각이 아니라면, 밤공기는 깨끗한 편이 좋을 테니까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=lobby_noon_10411_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Last chance today to smoke a cig. Won't get the time later.\nIt's best to keep the night air crisp, unless we're looking to summon the beasts really drenched in shadows.
   PL:
901. [Kwestia głosowa [lobby_night_10411_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=lobby_night_10411_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Kwestia głosowa [lobby_night_10411_1] (Evening Greeting)] 달이 기울었다. 뜀박질할 시간인가… 훗, 기대되는군. 오늘은 또 어떤 피칠갑이 벌어질지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=lobby_night_10411_1].dlg
   limit: do 180 znaków
   EN: The moon waxes. Time to hop into another bloodbath... heh, how exciting. I wonder what wonderful streaks of blood I'll get to admire today.
   PL:
903. [Kwestia głosowa [smalltalk_10411_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Kwestia głosowa [smalltalk_10411_1] (Chatter #1)] R사의 토끼와 비교하는 건 귀가 어두운 무지렁이들이나 하는 짓이지.\n뿌리는 같을지 몰라도, 그들과 우리는 뜯어온 풀부터가 다르다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_1].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only dense idiots compare us to the Rabbits of R Corp.\nWe share the same roots but have grazed on different grass.
   PL:
905. [Kwestia głosowa [smalltalk_10411_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Kwestia głosowa [smalltalk_10411_2] (Chatter #2)] …묘도 흑수도 나를 나타내는 말이 될 수 없다. 부를 때는 료슈라고 불러라, 주군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_2].dlg
   limit: do 120 znaków
   EN: ... Neither Mao nor Heishou can represent who I am; you will address me as Ryōshū, lord.
   PL:
907. [Kwestia głosowa [smalltalk_10411_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Kwestia głosowa [smalltalk_10411_3] (Chatter #3)] 예술도 모르는 재미없는 토끼 놈들이지만, 쓸데없는 말을 지껄여대지 않는 대화의 단축은 마음에 들어. 명령만 지킨다면, 내가 하는 일에 왈가왈부하는 놈이 없으니.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_3].dlg
   limit: do 230 znaków
   EN: The hares are dullards who know nothing about art, but I do like how they don't waste their breath on irrelevant details. Besides, no one chews me out as long as I follow orders.
   PL:
909. [Kwestia głosowa [smalltalk_10411_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Kwestia głosowa [smalltalk_10411_4] (Post-Uptie Chat 1)] 이 무기에 새겨진 문자는 단순한 장식이 아니다. Q사의 주박이 새겨진 일품이지.\n…그렇다고 내 검과 비교할 수준은 아니다. 이 검과는… 그 무엇도 비할 수 없지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_4].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The glyphs on this weapon aren't there just for show. They're first-rate Q Corp. seals.\nBut it could never measure up to my sword. ... Nothing can.
   PL:
911. [Kwestia głosowa [smalltalk_10411_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Kwestia głosowa [smalltalk_10411_5] (Post-Uptie Chat 2)] 흔한 일이다. 어제까지 같은 밥을 먹던 짐승이 오늘은 정적의 손에 재갈이 물려지는 것도, 오늘까지 충성을 다하던 주군이, 내일은 물어뜯을 먹잇감이 되는 것도.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=smalltalk_10411_5].dlg
   limit: do 260 znaków
   EN: A beast that shared a meal yesterday is leashed and gagged by a political foe today; the lord to whom I pledged my loyalty today becomes prey to be mauled tomorrow. But it's just another day for us.
   PL:
913. [Kwestia głosowa [neglect_10411_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=neglect_10411_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Kwestia głosowa [neglect_10411_1] (Idle)] 주군. 검은 머리 짐승은 예로부터 믿지 말라 했다. 명심하도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=neglect_10411_1].dlg
   limit: do 120 znaków
   EN: As the old saying goes, don't trust the beasts that are black of fur. Remember that, lord.
   PL:
915. [Kwestia głosowa [gacksung_10411_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=gacksung_10411_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Kwestia głosowa [gacksung_10411_1] (Uptying)] 믿던 짐승에게 목을 물어뜯긴 느낌은 어떻지? 천천히 말해봐라. 보채지 않을 테니.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=gacksung_10411_1].dlg
   limit: do 170 znaków
   EN: How does it feel, as the teeth of a beast you once trusted sink deep into your neck? Explain it slowly, and in detail. I won't rush.
   PL:
917. [Kwestia głosowa [formation_10411_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=formation_10411_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Kwestia głosowa [formation_10411_1] (Deployment)] 이제야 부르나. 존명.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=formation_10411_1].dlg
   limit: do 120 znaków
   EN: You're late. But your wish is my command.
   PL:
919. [Kwestia głosowa [battleentry_10411_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battleentry_10411_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Kwestia głosowa [battleentry_10411_1] (Stage Entry)] 뜀박질 시간.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battleentry_10411_1].dlg
   limit: do 120 znaków
   EN: Time to hop.
   PL:
921. [Kwestia głosowa [battle_select_10411_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_select_10411_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Kwestia głosowa [battle_select_10411_1] (Viewed in Battle)] 더 처리할 먹잇감이 있나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_select_10411_1].dlg
   limit: do 120 znaków
   EN: Any more prey I should take care of?
   PL:
923. [Kwestia głosowa [battle_endcommand_10411_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_endcommand_10411_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Kwestia głosowa [battle_endcommand_10411_1] (Commencing Attack)] 흑수 묘, 뜀박질 준비.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_endcommand_10411_1].dlg
   limit: do 120 znaków
   EN: Mao branch of the Heishou Pack, ready to hop.
   PL:
925. [Kwestia głosowa [battle_enemy_break_10411_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_enemy_break_10411_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Kwestia głosowa [battle_enemy_break_10411_1] (Enemy Stagger)] 하. 아직 죽진 마라.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_enemy_break_10411_1].dlg
   limit: do 120 znaków
   EN: Hah. Don't die just yet.
   PL:
927. [Kwestia głosowa [battle_break_10411_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_break_10411_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Kwestia głosowa [battle_break_10411_1] (Staggered)] 칫, 잠깐만 기다려라…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_break_10411_1].dlg
   limit: do 120 znaków
   EN: Tch, wait...
   PL:
929. [Kwestia głosowa [battle_kill_10411_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_kill_10411_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Kwestia głosowa [battle_kill_10411_1] (Enemy Killed)] 흥, 가치 없군. 죽어라.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_kill_10411_1].dlg
   limit: do 120 znaków
   EN: Hmph, worthless. Die.
   PL:
931. [Kwestia głosowa [battle_dead_10411_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_dead_10411_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Kwestia głosowa [battle_dead_10411_1] (Death)] 아… 젠장. 즐거운… 시간이었는데.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_dead_10411_1].dlg
   limit: do 120 znaków
   EN: Ah... dammit. That... was... fun.
   PL:
933. [Kwestia głosowa [choice_success_p_10411_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=choice_success_p_10411_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Kwestia głosowa [choice_success_p_10411_2] (Check Passed)] 심심풀이는 되는군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=choice_success_p_10411_2].dlg
   limit: do 120 znaków
   EN: Just killing time.
   PL:
935. [Kwestia głosowa [choice_fail_n_10411_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=choice_fail_n_10411_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Kwestia głosowa [choice_fail_n_10411_1] (Check Failed)] 이딴 일에 흑수의 시간을 허비했나?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=choice_fail_n_10411_1].dlg
   limit: do 120 znaków
   EN: You're wasting the Heishou Pack's time on <i>this</i>?
   PL:
937. [Kwestia głosowa [battle_clear_10411_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_clear_10411_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Kwestia głosowa [battle_clear_10411_1] (Victory Cry)] 시답잖은 사냥이었어. 괜히 길어진 탓에 핏자국이 흥건해져서 아무런 아름다움이 남지 않았군… 쳇.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_clear_10411_1].dlg
   limit: do 130 znaków
   EN: What a disappointing hunt. Spilled too much blood for this to be beautiful—we took too long... tsk.
   PL:
939. [Kwestia głosowa [battle_clear_ex_10411_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_clear_ex_10411_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Kwestia głosowa [battle_clear_ex_10411_1] (Extra Conditions Fulfilled)] 좋아… 생동감이 살아있는 좋은 공간이 됐군. 다음 먹잇감도 이런 식이었으면 좋겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_clear_ex_10411_1].dlg
   limit: do 130 znaków
   EN: Nice... Just look at how vibrant this place has become. Hope the next prey gives a good show, too.
   PL:
941. [Kwestia głosowa [battle_defeat_10411_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_defeat_10411_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Kwestia głosowa [battle_defeat_10411_1] (Defeat Wail)] 도리어 사냥당한다니… 역설적인 걸 싫어하는 건 아니지만, 그다지… 유쾌하진 않군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_Blackwater_10411.json :: dataList[id=battle_defeat_10411_1].dlg
   limit: do 120 znaków
   EN: The hunter becomes the hunted... I don't hate a good paradox, but it is... unpleasant.
   PL:

## [000] N Corp. E.G.O:: Contempt, Awe — Ryōshū — N사 E.G.O:: 경멸, 경외
- ID Tożsamości: `10412` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Tremor

943. [Karta Tożsamości — tytuł] N사 E.G.O::\n경멸, 경외
   źródło: Personalities.json :: dataList[id=10412].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp. E.G.O::\nContempt, Awe
   PL:
944. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10412].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10412].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Karta Tożsamości — opis] 료슈의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10412].desc
   limit: do 120 znaków
   EN: Ryōshū's 12th Identity
   PL:
947. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 경멸스러운 것
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=1].name ; dataList[id=1041201].levelList[level=2].name ; dataList[id=1041201].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Contemptuous Thing
   PL:
948. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [GazeRyoshu], [ContemptRyoshu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt
   EN: [WhenUse] If target has [GazeRyoshu] or [ContemptRyoshu], Clash Power +1
   PL:
949. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [GazeRyoshu] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1041201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 1 [GazeRyoshu]
   PL:
950. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [GazeRyoshu], [ContemptRyoshu], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has [GazeRyoshu] or [ContemptRyoshu], Clash Power +1\n[WhenUse] At 6+ ([Laceration] + [Vibration]) on target, Coin Power +1
   PL:
951. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1041201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
953. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [GazeRyoshu], [ContemptRyoshu], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has [GazeRyoshu] or [ContemptRyoshu], Clash Power +1\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Laceration] + [Vibration]) on target (max 2)</style>
   PL:
954. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 경외하라
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].name ; dataList[id=1041202].levelList[level=2].name ; dataList[id=1041202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Be Awed
   PL:
955. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].desc
   (powtórzenie elementu 948 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1041202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
957. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1041202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
958. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
959. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [GazeRyoshu] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].desc
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 952 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [GazeRyoshu] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 1 [GazeRyoshu]<style="highlight"></style>
   PL:
964. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 5 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#4].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
965. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].desc
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 738 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [GazeRyoshu] <style="highlight">2</style> 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [GazeRyoshu]
   PL:
969. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 경외, 경멸
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].name ; dataList[id=1041203].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Awe, Contempt
   PL:
970. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상에게 [GazeRyoshu]이 있으면, 이 스킬에서 부여하는 [Laceration], [Vibration] 위력 +2\n[BeforeUse] 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, ‘<noparse>경멸</noparse> 밑으로 쏟아지는 경외의 시선’으로 발동됨\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 8 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +1% (최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [GazeRyoshu], [Laceration], [Vibration], [BeforeUse], [ContemptRyoshu], [WhenUse]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [BeforeUse] = [사용전] / [Before Use]; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]
   EN: If target has [GazeRyoshu], this Skill inflicts +2 more [Laceration] and [Vibration] potency\n[BeforeUse] At 7+ (sum of [GazeRyoshu] on all enemies), or at 1+ (sum of [ContemptRyoshu] on all enemies), activates 'Cascading <noparse>Gaze</noparse> of <noparse>Awe</noparse> Underneath <noparse>Contempt</noparse>' instead\n[WhenUse] At 8+ ([Laceration] + [Vibration]) on target, Coin Power +1\n[WhenUse] Deal +1% damage for every ([Laceration] + [Vibration]) on target (max 20%)
   PL:
971. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 956 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1041203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1041203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 952 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] 대상의 [GazeRyoshu] 1당 피해량 +5% (최대 35%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GazeRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze
   EN: Deal +5% damage for every 1 [GazeRyoshu] on target (max 35%)
   PL:
977. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [GazeRyoshu] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 2 [GazeRyoshu]
   PL:
978. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL:
979. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#4].desc ; dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
980. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상에게 [GazeRyoshu]이 있으면, 이 스킬에서 부여하는 [Laceration], [Vibration] 위력 +2<style="highlight"></style>\n[BeforeUse] 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, ‘<noparse>경멸</noparse> 밑으로 쏟아지는 경외의 시선’으로 발동됨\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 8<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +1% (최대 <style="highlight">40</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [GazeRyoshu], [Laceration], [Vibration], [BeforeUse], [ContemptRyoshu], [WhenUse]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [BeforeUse] = [사용전] / [Before Use]; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]
   EN: If target has [GazeRyoshu], this Skill inflicts +2 more [Laceration] and [Vibration] potency<style="highlight"></style>\n[BeforeUse] At 7+ (sum of [GazeRyoshu] on all enemies), or at 1+ (sum of [ContemptRyoshu] on all enemies), activates 'Cascading <noparse>Gaze</noparse> of <noparse>Awe</noparse> Underneath <noparse>Contempt</noparse>' instead\n[WhenUse] <style="highlight">Coin Power +1 for every 8 ([Laceration] + [Vibration]) on target (max 2)</style>\n[WhenUse] Deal +1% damage for every ([Laceration] + [Vibration]) on target (max <style="highlight">40</style>%)
   PL:
981. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
982. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 738 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 대상의 [GazeRyoshu] 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [GazeRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze
   EN: Deal +<style="highlight">10</style>% damage for every 1 [GazeRyoshu] on target (max <style="highlight">70</style>%)
   PL:
984. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [GazeRyoshu] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 3 [GazeRyoshu]
   PL:
985. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 경멸 밑으로 쏟아지는 경외의 시선
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].name ; dataList[id=1041205].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 14 · monety: 1 (+14)
   limit: do 60 znaków
   EN: Cascading Gaze of Awe Underneath Contempt
   PL:
986. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 이 스킬은 외부 효과로 재사용이 불가능함\n[GazeRyoshu] 또는 [ContemptRyoshu]을 보유한 적을 서브 타겟으로 우선 지정함\n- 서브 타겟에게 가하는 피해량 -50%\n공격 대상이 1명이면, 피해량 +200% (집중 전투일 경우, 부위로 판정)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 4당, 코인 위력 +1 (최대 2)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +2% (최대 50%)\n[WhenUse] 모든 공격 대상에게 부여된 [GazeRyoshu]의 합 1당, 피해량 +7% (최대 49%)\n[EndSkill] 적중한 모든 대상의 [GazeRyoshu] 또는 [ContemptRyoshu] 전부 소모
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n, [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration], [Vibration], [EndSkill]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: External effects cannot trigger this Skill to be Reused\nPrioritizes targeting enemies that have [GazeRyoshu] or [ContemptRyoshu] as sub-targets\n- Deals -50% damage against sub-targets\nIf there is just a single target, deal +200% damage (for Focused Encounters, a Part)\n[WhenUse] Coin Power +1 for every 4 ([Laceration] + [Vibration]) on the main target (max 2)\n[WhenUse] Deal +2% damage for every ([Laceration] + [Vibration]) on the main target (max 50%)\n[WhenUse] Deal +7% damage for every 1 (sum of [GazeRyoshu] on all attack targets) (max 49%)\n[EndSkill] Consumes [GazeRyoshu] or [ContemptRyoshu] on all targets that were hit
   PL:
987. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] 대상에게 [ContemptRyoshu]이 있으면, 피해량 +180%
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ContemptRyoshu]
   znaczenie tagów: [ContemptRyoshu] = 경멸 / Contempt
   EN: If target has [ContemptRyoshu], deal +180% damage
   PL:
989. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +1 [Vibration] Count
   PL:
990. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL:
991. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL:
992. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#5].desc ; dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 979 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬은 외부 효과로 재사용이 불가능함\n[GazeRyoshu] 또는 [ContemptRyoshu]을 보유한 적을 서브 타겟으로 우선 지정함<style="highlight"></style>\n- 서브 타겟에게 가하는 피해량 -50%\n공격 대상이 1명이면, 피해량 +200% (집중 전투일 경우, 부위로 판정)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 4당, 코인 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +2% (최대 <style="highlight">100</style>%)\n[WhenUse] 모든 공격 대상에게 부여된 [GazeRyoshu]의 합 1당, 피해량 +10% (최대 70%)\n[EndSkill] 적중한 모든 대상의 [GazeRyoshu] 또는 [ContemptRyoshu] 전부 소모
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration], [Vibration], [EndSkill]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: External effects cannot trigger this Skill to be Reused\nPrioritizes targeting enemies that have [GazeRyoshu] or [ContemptRyoshu] as sub-targets<style="highlight"></style>\n- Deals -50% damage against sub-targets\nIf there is just a single target, deal +200% damage (for Focused Encounters, a Part)\n[WhenUse] Coin Power +1 for every 4 ([Laceration] + [Vibration]) on the main target (max <style="highlight">4</style>)\n[WhenUse] Deal +2% damage for every ([Laceration] + [Vibration]) on the main target (max <style="highlight">100</style>%)\n[WhenUse] Deal +10% damage for every 1 (sum of [GazeRyoshu] on all attack targets) (max 70%)\n[EndSkill] Consumes [GazeRyoshu] or [ContemptRyoshu] on all targets that were hit
   PL:
994. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 대상에게 [ContemptRyoshu]이 있으면, 피해량 +<style="highlight">235</style>%
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ContemptRyoshu]
   znaczenie tagów: [ContemptRyoshu] = 경멸 / Contempt
   EN: If target has [ContemptRyoshu], deal +<style="highlight">235</style>% damage
   PL:
995. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration] and +2 [Vibration] Count
   PL:
996. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL:
997. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 쏘아내겠소 / 언제든지
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].name ; dataList[id=1041206].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: I Shall Fire / Anytime
   PL:
998. [Umiejętność 5 (×0) (ulepszenie 3) — opis] [StartBattle] N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈 우선 공격\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모하고 자신의 정신력 20 회복
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Prioritizes N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] At 3+ [Breath] Count, Base Power +1\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all and heal 20 SP on self
   PL:
999. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1041206].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1000. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1041206].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target
   PL:
1001. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the sub-targets
   PL:
1003. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] - 첫번째 코인 피해가 크리티컬이 아니고, N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈가 생존했다면, 서브 타겟 중 무작위 1명이 피해를 입음
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: - If the first Coin wasn't a Critical Hit, and if N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū survived, 1 random sub-target takes damage
   PL:
1004. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 4 — opis] 자신의 [BoseProjektil]당 피해량 +30% (최대 210%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +30% damage for every [BoseProjektil] on self (max 210%)
   PL:
1005. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 5 — opis] [Breath] 위력당, 크리티컬 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +2.5% Damage on Critical Hit for every [Breath] Potency (max <style="highlight">25%</style>)
   PL:
1006. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 6 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +7% (최대 49%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +7% Damage on Critical Hit for every [BoseProjektil] on self (max 49%)
   PL:
1007. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 7 — opis] 메인 타겟의 잃은 체력 비율만큼 피해량이 증가 (최대 100%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#6].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   EN: Deal +1% damage for every 1% missing HP on the main target (max 100%)
   PL:
1008. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 8 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#7].desc
   (powtórzenie elementu 990 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [Umiejętność 5 (×0) (ulepszenie 4) — opis] [StartBattle] N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈 우선 공격\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 <style="highlight">당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모하고 자신의 정신력 20 회복
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Prioritizes N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] <style="highlight">Base Power +1 for every 3 [Breath] Count on self (max 2)</style>\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all and heal 20 SP on self
   PL:
1010. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 4 — opis] 자신의 [BoseProjektil]당 피해량 +<style="highlight">40</style>% (최대 <style="highlight">280</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +<style="highlight">40</style>% damage for every [BoseProjektil] on self (max <style="highlight">280</style>%)
   PL:
1011. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 5 — opis] [Breath] 위력당, 크리티컬 피해량 +<style="highlight">5</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +<style="highlight">5</style>% Damage on Critical Hit for every [Breath] Potency (max <style="highlight">50</style>%)
   PL:
1012. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 6 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +<style="highlight">10</style>% Damage on Critical Hit for every [BoseProjektil] on self (max <style="highlight">70</style>%)
   PL:
1013. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 8 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +2 [Laceration] Count
   PL:
1014. [Obrona (ulepszenia 1,4) — nazwa] 움켜쥔다
   źródło: Skills_personality-04.json :: dataList[id=1041204].levelList[level=1].name ; dataList[id=1041204].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+5)
   limit: do 40 znaków
   EN: To Grasp
   PL:
1015. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신에게 [ContemptPersonality]이 없고 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, [ContemptPersonality] 획득 (턴 당 1회)\n[WhenUse] 자신에게 [ContemptPersonality]이 있으면, 최종 위력 +5\n[WhenUse] 이 스킬 사용 중 피격시, 공격자의 [Laceration] 횟수 1 증가 (턴 당 3회 발동)
   źródło: Skills_personality-04.json :: dataList[id=1041204].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ContemptPersonality], [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] If this unit does not have [ContemptPersonality], and at 7+ (sum of [GazeRyoshu] on all enemies) or 1+ (sum of [ContemptRyoshu] on all enemies), gain [ContemptPersonality] (once per turn)\n[WhenUse] If this unit has [ContemptPersonality], Final Power +5\n[WhenUse] When hit while using this Skill, inflict +1 [Laceration] Count against the attacker (3 times per turn)
   PL:
1016. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신에게 [ContemptPersonality]이 없고 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, [ContemptPersonality] 획득 (턴 당 1회)\n[WhenUse] 자신에게 [ContemptPersonality]이 있으면, 최종 위력 +10\n[WhenUse] 이 스킬 사용 중 피격시, 공격자의 [Laceration] 횟수 1 증가 (턴 당 3회 발동)
   źródło: Skills_personality-04.json :: dataList[id=1041204].levelList[level=4].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ContemptPersonality], [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] If this unit does not have [ContemptPersonality], and at 7+ (sum of [GazeRyoshu] on all enemies) or 1+ (sum of [ContemptRyoshu] on all enemies), gain [ContemptPersonality] (once per turn)\n[WhenUse] If this unit has [ContemptPersonality], Final Power +10\n[WhenUse] When hit while using this Skill, inflict +1 [Laceration] Count against the attacker (3 times per turn)
   PL:
1017. [Pasywka bojowa (od ulepszenia 1) — nazwa] 쓰러질 수조차 없게 붙드는 손아귀
   źródło: Passives.json :: dataList[id=1041202].name
   limit: do 40 znaków
   EN: Grasp that Forbids Falling
   PL:
1018. [Pasywka bojowa (od ulepszenia 1) — opis] 흐트러짐 상태가 되면, [Protection] 4를 얻고 다음 턴에 [ContemptPersonality] 획득 (전투 당 1회)\n\n사망 시, [GazeRyoshu] 또는 [ContemptRyoshu]이 많은 순으로 적 3명에게 아래 효과 적용 (집중 전투일 경우, 부위로 판정)\n- 다음 턴에 [Binding] 2 부여\n- [Laceration] 2 부여, [Laceration] 횟수 1 증가\n- [Vibration] 2 부여, [Vibration] 횟수 1 증가
   źródło: Passives.json :: dataList[id=1041202].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [ContemptPersonality], [GazeRyoshu], [ContemptRyoshu], [Binding], [Laceration], [Vibration]
   znaczenie tagów: [Protection] = 보호 / Protection; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [Binding] = 속박 / Bind; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: When Staggered, gain 4 [Protection] and gain [ContemptPersonality] next turn (once per Encounter)\n\nOn death, apply the following effects against 3 enemies that have the most [GazeRyoshu] or [ContemptRyoshu] (in descending order; in Focused Encounters, Parts)\n- Inflict 2 [Binding] next turn\n- Inflict 2 [Laceration] and +1 [Laceration] Count\n- Inflict 2 [Vibration] and +1 [Vibration] Count
   PL:
1019. [Pasywka bojowa (od ulepszenia 1) — nazwa] 너희 모두 재밌는 걸 보여주지
   źródło: Passives.json :: dataList[id=1041203].name
   limit: do 70 znaków
   EN: Let me show everyone something very interesting
   PL:
1020. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 시작 시 N사 E.G.O::<noparse>흉탄</noparse> 이상의 ‘대상 조정 사격’이 아래 효과 얻음\n- 사용 전 N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈가 [ContemptPersonality]을 보유 중이고, 기본 스킬을 사용할 수 있으면, 대신 ‘쏘아내겠소 / 언제든지’를 료슈에게 사용함 (턴 당 1회. ‘쏘아내겠소 / 언제든지’는 이상의 동기화 단계가 적용됨)\n- 사용 전 N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈가 메인 타겟이 아니고, 기본 스킬을 사용할 수 있으면, 료슈가 메인 타겟을 스킬 1로 일방공격함 (턴 당 1회. [CantIdentify]. 스킬 1의 피해량 -50%. 해당 스킬로 메인 타겟이 사망하지 않음)
   źródło: Passives.json :: dataList[id=1041203].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ContemptPersonality], [CantIdentify]
   znaczenie tagów: [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: Combat Start: N Corp. E.G.O::<noparse>Fell Bullet</noparse> Yi Sang's 'Target Readjustment Fire' Skill gains the following effects:\n- Before using the Skill, if N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū has [ContemptPersonality] and can use her base Skills, use "I Shall Fire / Anytime" against Ryōshū (once per turn; 'I Shall Fire / Anytime' reflects Yi Sang's Uptie Tier)\n- Before using the Skill, if the Skill's main target isn't N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū, and if she can use her base Skills, Ryōshū uses her Skill 1 as an Unopposed Attack against the main target (once per turn; [CantIdentify]; Skill 1 deals -50% damage; the Skill does not kill the main target)
   PL:
1021. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — nazwa] 놓쳤던 @#$의 손
   źródło: Passives.json :: dataList[id=1041201].name
   limit: do 40 znaków
   EN: @#$'s Hand I Let Slip
   PL:
1022. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — opis] 적에게 공격 적중 시, [GazeRyoshu] 1 부여 (적 당 턴 당 최대 1회)\n- 자신에게 [GazePersonality]이 있으면, [GazeRyoshu] 1 추가 부여\n\n적에게 피격 시, 공격자에게 [GazeRyoshu] 1 부여 (스킬 당 최대 1회, 턴 당 최대 3회)\n- 자신에게 [ContemptPersonality]이 있으면, 공격자의 마지막 코인 적중 시 공격자에게 해당 코인으로 받은 피해량의 10%만큼 나태 속성 피해를 입힘 (스킬 당 최대 10, 턴 당 최대 30)\n\n기본 공격 스킬로 적의 [GazeRyoshu] 또는 [ContemptRyoshu]을 소모했다면,\n다음 턴에 (소모한 적의 [GazeRyoshu]/2 + 소모한 적의 [ContemptRyoshu]x3)만큼 [GazePersonality] 획득 (턴 당 최대 6. 소수점 버림)
   źródło: Passives.json :: dataList[id=1041201].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: \n, [GazeRyoshu], [GazePersonality], [ContemptPersonality], [ContemptRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [ContemptRyoshu] = 경멸 / Contempt
   EN: On Hit against enemies, inflict 1 [GazeRyoshu] (once per turn per enemy)\n- If this unit has [GazePersonality], inflict +1 more [GazeRyoshu]\n\nWhen hit by an enemy, inflict 1 [GazeRyoshu] against the attacker (once per Skill; 3 times per turn)\n- If this unit has [ContemptPersonality]: when hit by the attacker's final Coin, inflict (10% of the damage dealt by that final Coin) Sloth damage (max 10 per Skill; max 30 per turn)\n\nIf this unit used its Base Attack Skills to consume [GazeRyoshu] or [ContemptRyoshu] on an enemy:\nNext turn, gain ((enemy's [GazeRyoshu] consumed/2) + (enemy's [ContemptRyoshu] consumed x 3)) [GazePersonality] (6 per turn; rounded down)
   PL:
1023. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Lust) — nazwa] 놓쳤던 @#$의 손
   źródło: Passives.json :: dataList[id=1041211].name
   (powtórzenie elementu 1021 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Lust) — opis] 적에게 공격 적중 시, [GazeRyoshu] <style="highlight">2</style> 부여 (적 당 턴 당 최대 1회)\n- 자신에게 [GazePersonality]이 있으면, [GazeRyoshu] 1 추가 부여\n\n적에게 피격 시, 공격자에게 [GazeRyoshu] 1 부여 (스킬 당 최대 1회, 턴 당 최대 3회)\n- 자신에게 [ContemptPersonality]이 있으면, 공격자의 마지막 코인 적중 시 공격자에게 해당 코인으로 받은 피해량의 <style="highlight">20</style>%만큼 나태 속성 피해를 입힘 (스킬 당 최대 <style="highlight">20</style>, 턴 당 최대 <style="highlight">60</style>)\n\n기본 공격 스킬로 적의 [GazeRyoshu] 또는 [ContemptRyoshu]을 소모했다면,\n다음 턴에 (소모한 적의 [GazeRyoshu]/2 + 소모한 적의 [ContemptRyoshu]x3)만큼 [GazePersonality] 획득 (턴 당 최대 6. 소수점 버림)
   źródło: Passives.json :: dataList[id=1041211].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [GazeRyoshu], [GazePersonality], [ContemptPersonality], [ContemptRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [ContemptRyoshu] = 경멸 / Contempt
   EN: On Hit against enemies, inflict <style="highlight">2</style> [GazeRyoshu] (once per turn per enemy)\n- If this unit has [GazePersonality], inflict +1 more [GazeRyoshu]\n\nWhen hit by an enemy, inflict 1 [GazeRyoshu] against the attacker (once per Skill; 3 times per turn)\n- If this unit has [ContemptPersonality]: when hit by the attacker's final Coin, inflict (<style="highlight">20</style>% of the damage dealt by that final Coin) Sloth damage (max <style="highlight">20</style> per Skill; max <style="highlight">60</style> per turn)\n\nIf this unit used its Base Attack Skills to consume [GazeRyoshu] or [ContemptRyoshu] on an enemy:\nNext turn, gain ((enemy's [GazeRyoshu] consumed/2) + (enemy's [ContemptRyoshu] consumed x 3)) [GazePersonality] (6 per turn; rounded down)
   PL:
1025. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 그건 흐르고 울린다
   źródło: Passives.json :: dataList[id=1041221].name
   limit: do 40 znaków
   EN: It flows and cries
   PL:
1026. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 편성 순서가 가장 빠른 아군 1명이 적에게 공격 적중 시, [Laceration] 1 부여 (적 당 턴 당 최대 1회)\n- 대상에게 [Laceration]이 있으면, 추가로 [Laceration] 횟수 1 증가\n\n편성 순서가 가장 빠른 아군 1명이 적에게 피격시, 공격자에게 [Vibration] 1 부여 (턴 당 최대 3회)\n- 공격자에게 [Vibration]이 있으면, 추가로 [Vibration] 횟수 1 증가
   źródło: Passives.json :: dataList[id=1041221].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vibration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: If the ally with the earliest Deployment order hits an enemy using its attack, inflict 1 [Laceration] (once per enemy per turn)\n- If target has [Laceration], inflict +1 [Laceration] Count as well\n\nIf the ally with the earliest Deployment order is hit by an enemy, inflict 1 [Vibration] against the attacker (3 times per turn)\n- If the attacker has [Vibration], inflict +1 [Vibration] Count as well
   PL:
1027. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — podsumowanie] 적에게 적중 시, [Laceration] 부여하고 이미 있다면 추가로 횟수 증가\n적에게 피격 시, [Vibration] 부여하고 이미 있다면 추가로 횟수 증가
   źródło: Passives.json :: dataList[id=1041221].summary
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vibration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: On Hit, inflict [Laceration]; inflict Count as well if the target already has the effect\nWhen Hit, inflict [Vibration]; inflict Count as well if the target already has the effect
   PL:
1028. [Kwestia głosowa [get_10412_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=get_10412_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Kwestia głosowa [get_10412_1] (Identity Acquisition)] 차라리 선 채로 죽어라. 네놈의 추한 시선이 가진 신선도가… 시시각각 떨어지고 있으니까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=get_10412_1].dlg
   limit: do 130 znaków
   EN: Why don't you just die standing up? The freshness of your hideous gaze is... decaying by the second.
   PL:
1030. [Kwestia głosowa [lobby_morning_10412_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=lobby_morning_10412_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Kwestia głosowa [lobby_morning_10412_1] (Morning Greeting)] 매캐한 새벽이군… 딱 좋을 정도의 먼지 농도다. 흠… 저 연구자라고 자칭하는 덜떨어진 것들이 푸닥거리며 더 짙게만 안 만들면… 좋겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=lobby_morning_10412_1].dlg
   limit: do 200 znaków
   EN: Just the right amount of dust in the morning... perfect. Hm... those self-proclaimed "researchers" better not kick any more up with their fussing... I hope.
   PL:
1032. [Kwestia głosowa [lobby_noon_10412_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=lobby_noon_10412_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1033. [Kwestia głosowa [lobby_noon_10412_1] (Afternoon Greeting)] 가끔, 그런 생각이 들곤 하지. 대가리 꼭대기 위에서 빛을 내리쬐고 있는 태양. 저놈의 빛이 그 아래에 있는 모든 걸 경멸하는 것 같다고.\n기분 나쁘게… 말이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=lobby_noon_10412_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sometimes, I think about the sun. The sun's light that gazes down upon all that is beneath its radiance with contempt.\nIt's... discomforting.
   PL:
1034. [Kwestia głosowa [lobby_night_10412_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=lobby_night_10412_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Kwestia głosowa [lobby_night_10412_1] (Evening Greeting)] 이 날개의 망치라는 놈들은 항상 이 시간마다 바쁘군. 또 쓸데없는 저녁 찬미를 하러 몰려갔나. 이단 심문관인가 뭔가 하는 것들이 난잡한 짓거리를 한 지 얼마나 되었다고…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=lobby_night_10412_1].dlg
   limit: do 240 znaków
   EN: The "Hammers" of this Wing get so busy around this time of day. Off to one of their pointless evening exaltations, I suppose? And so soon after the mess the "Inquisitors" started...
   PL:
1036. [Kwestia głosowa [smalltalk_10412_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Kwestia głosowa [smalltalk_10412_1] (Chatter #1)] 관. 없. 너희들끼리 못이니 망치니 편 가르기나 하는 꼴에 내가 왜 끼어들어야 하지. 난 내 칼로 뭘 베는지에만 관심 있다. 나머지는 꺼져.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_1].dlg
   limit: do 200 znaków
   EN: I.D.C. Don't involve me in that foolish rivalry between Nails and Hammers. I only care about what I get to cut with my sword; the rest of you can scram.
   PL:
1038. [Kwestia głosowa [smalltalk_10412_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1039. [Kwestia głosowa [smalltalk_10412_2] (Chatter #2)] 아… 이상. 이 떨거지들 사이에서 유일한 재밋거리지. 혼자서 온갖 고뇌란 고뇌는 다 감싸안은 주제에, 결국엔 동료의 뒤에 총알이나 박아 넣는 모양새는 비극의 미가 서려 있거든.\n기회 되면 내가 손 좀 보태지. 뭐, 나를 쏴도 좋다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_2].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah... Yi Sang. He's my only source of entertainment among the trifles. There's a certain tragic beauty to how someone can harbor so, so much anguish... before turning around and putting a bullet in his comrade's back.\nI suppose I'll help him out if I get the chance. He's got my permission to shoot me.
   PL:
1040. [Kwestia głosowa [smalltalk_10412_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Kwestia głosowa [smalltalk_10412_3] (Chatter #3)] 중첩 인격…? 재밌는 시도를 하는군. 그럼 회사 지하에서 밀가루 반죽처럼 기어다니던 것들은 실패작들인가.\n괜찮은 추상예술이라 생각했더니, 좀 더 걸출한 걸 준비하나… 이 회사에 좀 더 붙어있을 만하겠어.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_3].dlg
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Superpositioned Identities...? Interesting concept. I suppose those crawling sacks of flour dough in the company basement were the failed attempts, then.\nI thought it was an adequate endeavor toward creating abstract art, but... perhaps they're shooting higher. Maybe that'll get me to stick with this company for a little while.
   PL:
1042. [Kwestia głosowa [smalltalk_10412_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_4].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Kwestia głosowa [smalltalk_10412_4] (Post-Uptie Chat 1)] 쥐는 자… 하, 망치를 쥐고 못을 박아 넣으니 너희가 더 우월하다… 그런 사고 끝에 정한 직책인가? 말장난으로썬… 나쁘지 않군.\n내가 내려다보기엔… 못이든 망치든 전부 썩어빠진 추종자들로밖에 보이지 않지만.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_4].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The One Who Grips... Hah. So the thought process behind that name must be something like... how superiority comes naturally to the one who grips the hammer to sink in the nails? Not a terrible pun.\nThough, from my elevated perspective... they're all rotting cultists, Hammer or Nail.
   PL:
1044. [Kwestia głosowa [smalltalk_10412_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_5].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1045. [Kwestia głosowa [smalltalk_10412_5] (Post-Uptie Chat 2)] 봐라, 더러운 것들에게서 쏟아지는 거무죽죽한 용솟음을. 저건 단순히 창자나 피가 아니다… 그놈과 나의 붓으로 그어낸 멸시라는 작품이지.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=smalltalk_10412_5].dlg
   limit: do 190 znaków
   EN: Watch how the blackened spout from the squalid. This isn't just any entrails or blood... it's art, "The Contempt", created from our shared brush.
   PL:
1046. [Kwestia głosowa [neglect_10412_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=neglect_10412_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1047. [Kwestia głosowa [neglect_10412_1] (Idle)] 어설프게 시선을 줄 바에는 이쪽으로 고개를 돌리지 마라. 그래도 한번 봐버렸다면 눈을 떼지 말도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=neglect_10412_1].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If you're going to give this only a tepid gaze, I'd much rather you not make eye contact in the first place.\nBut once you've looked... don't look away.
   PL:
1048. [Kwestia głosowa [gacksung_10412_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=gacksung_10412_1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Kwestia głosowa [gacksung_10412_1] (Uptying)] 추잡한 것. 결국 내가 손을 대지 않으면 혐오스러운 몰골을 바꿀 수도, 숨길 수도 없나. 차라리… 흩뿌려져라.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=gacksung_10412_1].dlg
   limit: do 150 znaków
   EN: You squalid thing. Without my touch, that abominable form is unable to change, unable to be hidden. So... scatter.
   PL:
1050. [Kwestia głosowa [formation_10412_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=formation_10412_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1051. [Kwestia głosowa [formation_10412_1] (Deployment)] 시선. 집중.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=formation_10412_1].dlg
   limit: do 120 znaków
   EN: Eyes. On. Me.
   PL:
1052. [Kwestia głosowa [battleentry_10412_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battleentry_10412_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Kwestia głosowa [battleentry_10412_1] (Stage Entry)] 눈 멀지 않게 조심하도록.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battleentry_10412_1].dlg
   limit: do 120 znaków
   EN: Don't go blind on me now.
   PL:
1054. [Kwestia głosowa [battle_select_10412_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_select_10412_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [Kwestia głosowa [battle_select_10412_1] (Viewed in Battle)] 누가 누구에게 말을 거는 거지?
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_select_10412_1].dlg
   limit: do 120 znaków
   EN: Do you realize who you're talking to?
   PL:
1056. [Kwestia głosowa [battle_endcommand_10412_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_endcommand_10412_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1057. [Kwestia głosowa [battle_endcommand_10412_1] (Commencing Attack)] 나선 속을 벗어날 순 없다.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_endcommand_10412_1].dlg
   limit: do 120 znaków
   EN: There's no escaping the 'spiral'.
   PL:
1058. [Kwestia głosowa [battle_enemy_break_10412_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_enemy_break_10412_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1059. [Kwestia głosowa [battle_enemy_break_10412_1] (Enemy Stagger)] 그 시선… 경멸스럽군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_enemy_break_10412_1].dlg
   limit: do 120 znaków
   EN: That gaze... how contemptuous.
   PL:
1060. [Kwestia głosowa [battle_break_10412_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_break_10412_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1061. [Kwestia głosowa [battle_break_10412_1] (Staggered)] 큭.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_break_10412_1].dlg
   limit: do 120 znaków
   EN: Ngh.
   PL:
1062. [Kwestia głosowa [battle_kill_10412_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_kill_10412_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Kwestia głosowa [battle_kill_10412_1] (Enemy Killed)] 벗어날 수 있다고 생각했나.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_kill_10412_1].dlg
   limit: do 120 znaków
   EN: Did you think you could escape?
   PL:
1064. [Kwestia głosowa [battle_dead_10412_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_dead_10412_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1065. [Kwestia głosowa [battle_dead_10412_1] (Death)] 핫… 나를 감싸던… 시선도, 날 경멸하나… 짜릿하군.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_dead_10412_1].dlg
   limit: do 120 znaków
   EN: Hah... even the gaze that once embraced me... contemns me... How electrifying.
   PL:
1066. [Kwestia głosowa [choice_success_p_10412_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=choice_success_p_10412_2].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1067. [Kwestia głosowa [choice_success_p_10412_2] (Check Passed)] 이 따위 일도 못해서… 쯧.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=choice_success_p_10412_2].dlg
   limit: do 120 znaków
   EN: How incompetent... tsk.
   PL:
1068. [Kwestia głosowa [choice_fail_n_10412_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=choice_fail_n_10412_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1069. [Kwestia głosowa [choice_fail_n_10412_1] (Check Failed)] 그렇게 싫어하진 않는다. 나를 경멸하는 시선.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=choice_fail_n_10412_1].dlg
   limit: do 120 znaków
   EN: That contemptuous gaze drawn toward me... I don't hate it.
   PL:
1070. [Kwestia głosowa [battle_clear_10412_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_clear_10412_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1071. [Kwestia głosowa [battle_clear_10412_1] (Victory Cry)] 이제 지겨운 그 이사 놈도 일을 안 하고 다닌다는 핀잔은 주지 못하겠지. 난 N사 대가리 놈들이 뭘 쫓든 관심 없다. 그놈과 베고 꿰뚫을 수만 있다면.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_clear_10412_1].dlg
   limit: do 250 znaków
   EN: Now, that annoying director doesn't have any excuse to gripe to me about how I don't work. I couldn't care less about what the heads of N Corp. are after—just let me slice and dice along with him.
   PL:
1072. [Kwestia głosowa [battle_clear_ex_10412_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_clear_ex_10412_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Kwestia głosowa [battle_clear_ex_10412_1] (Extra Conditions Fulfilled)] 경외해라. 혹은 괄목하든가. 평범과 비범은 이렇게나 큰 차이를 보이지. …하. 한낱 날개 따위에 안주할 내가 아니다만.\n아직 그 실험들의 결과를 보고 싶으니 참도록 할까.
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_clear_ex_10412_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Be awed. Or be awestruck. This is the difference between the ordinary and the extraordinary. ... Hah. I shouldn't find satisfaction from being a part of a mere Wing.\n... But I'll endure a little longer, to see what those experiments end up becoming.
   PL:
1074. [Kwestia głosowa [battle_defeat_10412_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_defeat_10412_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1075. [Kwestia głosowa [battle_defeat_10412_1] (Defeat Wail)] 볼썽사납군… 이 따위로 추하게 도망치게 될 줄이야. 등 뒤로… 짜증 나는 시선이 달라붙고 있는 것만 같군, 쯧. 젠장…
   źródło: PersonalityVoiceDlg/Voice_Ryoshu_LEGO_10412.json :: dataList[id=battle_defeat_10412_1].dlg
   limit: do 190 znaków
   EN: Pathetic... Didn't think I'd ever turn tail like a disgusting coward. I can... almost feel the irritating gaze coming from behind me. Tsk, dammit...
   PL:
