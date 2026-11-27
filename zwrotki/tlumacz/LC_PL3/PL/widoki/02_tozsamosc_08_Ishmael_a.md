# Grzesznik #08: Ishmael — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Ishmael** (이스마엘) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #08: Ishmael (이스마엘)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 이스마엘
   źródło: Characters.json :: dataList[id=8].name
   limit: do 40 znaków
   EN: Ishmael
   PL:
2. [Akta więźnia — nazwa] 이스마엘
   źródło: IntroduceCharacter.json :: dataList[id=이스마엘].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도\n모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을\n처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을\n내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며\n화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한\n물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼\n인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: IntroduceCharacter.json :: dataList[id=이스마엘].description
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You may be disheartened by the defective state of many of your Sinners,\nbut do not worry; this Sinner is one of the few who can carry out most missions without much complaint.\nShe is likely to make reasonable judgements, so it is a good idea to start conversations\nwhile looking her way if you're seeking sound advice.\nHowever, you mustn't forget: this Sinner has survived an absurd voyage in a far and wide body of water.\nHer patience may run deep, but once you take a wrong turn with her,\nit will be a difficult task to regain her trust.
   PL: Być może widok tylu Grzeszników z licznymi wadami odbiera panu nadzieję.\nSpokojnie. Ta Grzesznica należy do nielicznych, które wykonują zadania\nbez większego szemrania. Zwykle podejmuje rozsądne decyzje, dlatego gdy\npotrzebuje pan rady, dobrze jest zagaić, patrząc w jej stronę.\nProszę jednak nie zapominać: przeżyła niedorzeczną żeglugę po dalekiej\ni ogromnej wodzie, jej cierpliwość jest więc długa, ale gdy relacja\nraz zacznie się psuć, trudno ją będzie naprawić.

## [0] LCB Sinner — Ishmael — LCB 수감자
- ID Tożsamości: `10801` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 78 · szybkość: 5–6 / 5–7 / 5–8 / 5–8
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10801].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10801].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10801].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 이스마엘의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10801].desc
   limit: do 120 znaków
   EN: Ishmael’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 강타
   źródło: Skills.json :: dataList[id=1080101].levelList[level=1].name ; dataList[id=1080101].levelList[level=2].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Loggerhead
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 슬라이딩
   źródło: Skills.json :: dataList[id=1080102].levelList[level=1].name ; dataList[id=1080102].levelList[level=2].name ; dataList[id=1080102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 1 (+9)
   limit: do 40 znaków
   EN: Slide
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 수비 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1080102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict 1 Defense Power Down
   PL:
13. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 수비 위력 감소 3 부여
   źródło: Skills.json :: dataList[id=1080102].levelList[level=2].desc ; dataList[id=1080102].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict 3 Defense Power Down
   PL:
14. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1080102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
15. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 방어
   źródło: Skills.json :: dataList[id=1080103].levelList[level=3].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 8 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Shield Bash
   PL:
16. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발. 타격 취약 1 부여
   źródło: Skills.json :: dataList[id=1080103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; Inflict 1 Blunt Fragility
   PL:
17. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1080104].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL:
18. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Wrath) — nazwa] 발악
   źródło: Passives.json :: dataList[id=1080101].name
   limit: do 40 znaków
   EN: Last-ditch Struggle
   PL:
19. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Wrath) — opis] 합 진행 시 자신의 체력이 25% 미만이면 합 위력 +1
   źródło: Passives.json :: dataList[id=1080101].desc
   limit: do 120 znaków
   EN: At less than 25% HP, gain +1 clash Power in a clash.
   PL:
20. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — nazwa] 살아남고 말것이라는 마음
   źródło: Passives.json :: dataList[id=1080121].name
   limit: do 40 znaków
   EN: Determination to Survive
   PL:
21. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — opis] 현재 체력이 가장 낮은 아군 1명 체력이 50% 미만이면 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1080121].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP and less than 50% of Max HP gains +1 Clash Power in a clash.
   PL:
22. [Kwestia głosowa [get_10801_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=get_10801_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
23. [Kwestia głosowa [get_10801_1] (Identity Acquisition)] 저를, 이스마엘이라고 불러주세요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=get_10801_1].dlg
   limit: do 120 znaków
   EN: Call me Ishmael, if you please.
   PL:
24. [Kwestia głosowa [lobby_morning_10801_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=lobby_morning_10801_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
25. [Kwestia głosowa [lobby_morning_10801_1] (Morning Greeting)] 네, 오늘도 하루가 시작됐네요. 가보죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=lobby_morning_10801_1].dlg
   limit: do 120 znaków
   EN: Yeah, another day has begun. Let’s get sailing.
   PL:
26. [Kwestia głosowa [lobby_noon_10801_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=lobby_noon_10801_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
27. [Kwestia głosowa [lobby_noon_10801_1] (Afternoon Greeting)] 하루의 절반이 지났네요. 효율적으로 보내고 계시나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=lobby_noon_10801_1].dlg
   limit: do 120 znaków
   EN: We’re halfway through the day. Are you spending your time efficiently?
   PL:
28. [Kwestia głosowa [lobby_night_10801_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=lobby_night_10801_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
29. [Kwestia głosowa [lobby_night_10801_1] (Evening Greeting)] 하루를 마무리할 시간이네요. 마무리하고 얼른 쉬죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=lobby_night_10801_1].dlg
   limit: do 120 znaków
   EN: It’s time to wrap up the day. Let’s finish our remaining tasks and get some rest.
   PL:
30. [Kwestia głosowa [smalltalk_10801_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
31. [Kwestia głosowa [smalltalk_10801_1] (Chatter #1)] 그래도 관리자님이 계셔서 다행이라고 생각해요. 생각이 똑바로 박힌 인간이 한 사람이라도 더 있는 게 낫죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_1].dlg
   limit: do 160 znaków
   EN: I do think it’s fortunate that we have you on our side. Better to have two people who can think straight than just one.
   PL:
32. [Kwestia głosowa [smalltalk_10801_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
33. [Kwestia głosowa [smalltalk_10801_2] (Chatter #2)] 전 웬만한 명령은 수월하게 처리할 수 있어요. 단, 합리적이고 효율적인 판단이 있었다는 가정 하에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_2].dlg
   limit: do 160 znaków
   EN: I can take care of most orders without much difficulty, provided that they’re based on rational and efficient judgement.
   PL:
34. [Kwestia głosowa [smalltalk_10801_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
35. [Kwestia głosowa [smalltalk_10801_3] (Chatter #3)] 수준 차이가 천차만별인  수감자들을 알맞게 써먹어야 하는 것도 관리자님의 몫이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_3].dlg
   limit: do 120 znaków
   EN: I suppose it’s your job to use this motley ensemble of Sinners appropriately.
   PL:
36. [Kwestia głosowa [smalltalk_10801_4] — sytuacja] 대화 4
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_4].desc
   limit: do 120 znaków
   EN: Chatter #4
   PL:
37. [Kwestia głosowa [smalltalk_10801_4] (Chatter #4)] 알아두셔야 하는게, 제가 말씀드리는 건 모두 임무의 성공 여부를 위한 도움을 제시하는 거에요. 관리자님한테 악감정은 없다는 뜻이에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_4].dlg
   limit: do 220 znaków
   EN: Just to be clear, the remarks I say to you are meant to assist you to ensure the success of our mission. I’m not just saying them with any hard feelings towards you.
   PL:
38. [Kwestia głosowa [smalltalk_10801_5] — sytuacja] 대화 5
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_5].desc
   limit: do 120 znaków
   EN: Chatter #5
   PL:
39. [Kwestia głosowa [smalltalk_10801_5] (Chatter #5)] 제가 예전에 있었던 곳은, 아주 작은 실수 하나에도 모두의 목숨이 위태로워질 수 있는 공간이었어요. 제가 가끔 예민해지는 건 그 경험들에 의한 거에요. 아… 이해해 달라는 건 아니에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=smalltalk_10801_5].dlg
   limit: do 240 znaków
   EN: In my previous occupation, a tiny mistake could compromise all of our safety. My sensitive tendencies come from that experience. Oh… No, I’m not trying to ask for your understanding.
   PL:
40. [Kwestia głosowa [neglect_10801_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=neglect_10801_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
41. [Kwestia głosowa [neglect_10801_1] (Idle)] 관리자님? 에휴… 저도 이만 돌아갈게요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=neglect_10801_1].dlg
   limit: do 120 znaków
   EN: Manager? Sigh… I’ll be off then.
   PL:
42. [Kwestia głosowa [formation_10801_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=formation_10801_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
43. [Kwestia głosowa [formation_10801_1] (Deployment)] 네, 문제없어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=formation_10801_1].dlg
   limit: do 120 znaków
   EN: Sure, no problem.
   PL:
44. [Kwestia głosowa [battleentry_10801_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battleentry_10801_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
45. [Kwestia głosowa [battleentry_10801_1] (Stage Entry)] 명령에 따를게요. 효율적이라면.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battleentry_10801_1].dlg
   limit: do 120 znaków
   EN: I’ll follow your orders, as long as they’re efficient.
   PL:
46. [Kwestia głosowa [battle_select_10801_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_select_10801_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
47. [Kwestia głosowa [battle_select_10801_1] (Viewed in Battle)] 바쁘니까, 짧게 부탁드려요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_select_10801_1].dlg
   limit: do 120 znaków
   EN: I’m busy at the moment, so please keep it brief.
   PL:
48. [Kwestia głosowa [battle_endcommand_10801_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_endcommand_10801_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
49. [Kwestia głosowa [battle_endcommand_10801_1] (Commencing Attack)] 좋은 전략이네요. 가보죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_endcommand_10801_1].dlg
   limit: do 120 znaków
   EN: Sounds like a plan. Let’s go.
   PL:
50. [Kwestia głosowa [battle_enemy_break_10801_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_enemy_break_10801_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
51. [Kwestia głosowa [battle_enemy_break_10801_1] (Enemy Stagger)] 적을, 난파시켰습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_enemy_break_10801_1].dlg
   limit: do 120 znaków
   EN: The enemy has been stranded.
   PL:
52. [Kwestia głosowa [battle_break_10801_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_break_10801_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
53. [Kwestia głosowa [battle_break_10801_1] (Staggered)] 읏…!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_break_10801_1].dlg
   limit: do 120 znaków
   EN: Nghk…!
   PL:
54. [Kwestia głosowa [battle_kill_10801_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_kill_10801_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
55. [Kwestia głosowa [battle_kill_10801_1] (Enemy Killed)] 가라앉는군요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_kill_10801_1].dlg
   limit: do 120 znaków
   EN: Down they sink.
   PL:
56. [Kwestia głosowa [battle_allydead_10801_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_allydead_10801_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
57. [Kwestia głosowa [battle_allydead_10801_1] (Ally Death)] 고생하셔야겠네요, 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_allydead_10801_1].dlg
   limit: do 120 znaków
   EN: Looks like you’ve got work to do, Manager.
   PL:
58. [Kwestia głosowa [choice_success_p_10801_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=choice_success_p_10801_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
59. [Kwestia głosowa [choice_success_p_10801_1] (Check Passed)] 어떻게… 해내긴 했네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=choice_success_p_10801_1].dlg
   limit: do 120 znaków
   EN: Despite it all… I managed somehow.
   PL:
60. [Kwestia głosowa [choice_fail_n_10801_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=choice_fail_n_10801_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
61. [Kwestia głosowa [choice_fail_n_10801_1] (Check Failed)] 그러게 다른 사람을 쓰지 그랬어요. 제 탓하지나 마세요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=choice_fail_n_10801_1].dlg
   limit: do 120 znaków
   EN: You should’ve had someone else deal with it. Don’t blame me for this.
   PL:
62. [Kwestia głosowa [battle_clear_10801_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_clear_10801_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
63. [Kwestia głosowa [battle_clear_10801_1] (Victory Cry)] 이런 걸로 호들갑 떨지 않는 편이에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_clear_10801_1].dlg
   limit: do 120 znaków
   EN: I tend not to make a big deal out of such things.
   PL:
64. [Kwestia głosowa [battle_clear_ex_10801_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_clear_ex_10801_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
65. [Kwestia głosowa [battle_clear_ex_10801_1] (Extra Conditions Fulfilled)] 음… 솔직히, 이번엔 좀 잘한 것 같네요. 그렇죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_clear_ex_10801_1].dlg
   limit: do 120 znaków
   EN: Hmm… If I can be honest here, we did a pretty good job, right?
   PL:
66. [Kwestia głosowa [battle_defeat_10801_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_defeat_10801_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
67. [Kwestia głosowa [battle_defeat_10801_1] (Defeat Wail)] …아까 제 말 무시하고 그대로 달려 나간 사람 누구예요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LCB_10801.json :: dataList[id=battle_defeat_10801_1].dlg
   limit: do 120 znaków
   EN: …Who’s the one that ignored my words and bolted headfirst into the fray?
   PL:

## [000] R Corp. 4th Pack Reindeer — Ishmael — R사 제 4무리 순록팀
- ID Tożsamości: `10802` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Sinking

68. [Karta Tożsamości — tytuł] R사 제 4무리\n순록팀
   źródło: Personalities.json :: dataList[id=10802].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nReindeer
   PL:
69. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10802].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10802].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Karta Tożsamości — opis] 이스마엘의 두번째 인격
   źródło: Personalities.json :: dataList[id=10802].desc
   limit: do 120 znaków
   EN: Ishmael’s 2nd Identity
   PL:
72. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 정신 가격
   źródło: Skills.json :: dataList[id=1080201].levelList[level=1].name ; dataList[id=1080201].levelList[level=2].name ; dataList[id=1080201].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Mind Strike
   PL:
73. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]
   PL:
74. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
76. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL:
77. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count
   PL:
80. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL:
81. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 지져내기
   źródło: Skills.json :: dataList[id=1080202].levelList[level=1].name ; dataList[id=1080202].levelList[level=2].name ; dataList[id=1080202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Flaying Surge
   PL:
83. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 3 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +3 [Sinking] Count
   PL:
84. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 5 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Charge Count
   PL:
85. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 7 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +7 Charge Count
   PL:
86. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
87. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 정신 채찍
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].name ; dataList[id=1080203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 2 · monety: 4 (+6)
   limit: do 40 znaków
   EN: Mind Whip
   PL:
88. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 충전 횟수 전부 소모.\n전투 시작 시 충전 횟수가 10 미만이면 무작위 대상 일방 공격
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Spend all Charge Count\nIf at less than 10 Charge Count at Combat Start, target a random unit for an unopposed attack
   PL:
89. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 40%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 40% of damage dealt
   PL:
91. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30% of damage dealt
   PL:
93. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL:
95. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt
   PL:
97. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 충전 횟수 8 소모.\n전투 시작 시 충전 횟수가 8 미만이면 무작위 대상 일방 공격
   źródło: Skills.json :: dataList[id=1080203].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Spend 8 Charge Count\nIf at less than 8 Charge Count at Combat Start, target a random unit for an unopposed attack
   PL:
98. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1080204].levelList[level=1].name ; dataList[id=1080204].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
99. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain +1 Charge Count
   PL:
100. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 뇌파집속
   źródło: Passives.json :: dataList[id=1080201].name
   limit: do 40 znaków
   EN: Brainwave Focus
   PL:
101. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 전투 시작 시 정신력 -15.\n다음 턴 시작 시 공격 위력 증가를 (우울 공명 수/3)만큼 얻음
   źródło: Passives.json :: dataList[id=1080201].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the combat phase, lose 15 SP.\nGain (Gloom Res / 3) Attack Power Up next turn.
   PL:
102. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 집념
   źródło: Passives.json :: dataList[id=1080221].name
   limit: do 40 znaków
   EN: Tenacity
   PL:
103. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 정신력이 가장 낮은 아군 1명 타격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1080221].desc
   limit: do 120 znaków
   EN: 1 ally with the least SP deals +10% Blunt damage.
   PL:
104. [Kwestia głosowa [get_10802_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=get_10802_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Kwestia głosowa [get_10802_1] (Identity Acquisition)] 후, 복잡한 건 생략하죠. 제가 뭘 하면 되나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=get_10802_1].dlg
   limit: do 120 znaków
   EN: Huff, let’s skip the formalities. What do I need to do?
   PL:
106. [Kwestia głosowa [lobby_morning_10802_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=lobby_morning_10802_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Kwestia głosowa [lobby_morning_10802_1] (Morning Greeting)] 아침엔 주로 명상을 하는 편이에요. 최대한 정신을 비워놔야 하거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=lobby_morning_10802_1].dlg
   limit: do 120 znaków
   EN: I normally spend my morning in meditation. I have to cleanse my mind of distractions.
   PL:
108. [Kwestia głosowa [lobby_noon_10802_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=lobby_noon_10802_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Kwestia głosowa [lobby_noon_10802_1] (Afternoon Greeting)] 하아, 점심시간엔 다들 왜 이렇게 소란스러운 거죠? 조용히 밥만 먹으면 안 되는 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=lobby_noon_10802_1].dlg
   limit: do 120 znaków
   EN: Haah, why is everyone so noisy around noon? Can’t they have their meals quietly?
   PL:
110. [Kwestia głosowa [lobby_night_10802_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=lobby_night_10802_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Kwestia głosowa [lobby_night_10802_1] (Evening Greeting)] 후… 이제야 차분해질 수 있겠네요. 말 걸지 말아주세요. 좀 쉬고 싶거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=lobby_night_10802_1].dlg
   limit: do 120 znaków
   EN: Phew… I can finally have some peace and quiet. Please don’t talk to me. I need the rest.
   PL:
112. [Kwestia głosowa [smalltalk_10802_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Kwestia głosowa [smalltalk_10802_1] (Chatter #1)] 큭… 잠시만요. 머, 머리가 깨질 듯이… 아… 이제 나아졌어요. 요새 자주 이러네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_1].dlg
   limit: do 140 znaków
   EN: Knh… Give me a moment. My—my head, it’s splitting… Ahh… I’m better now. It’s been happening a lot recently.
   PL:
114. [Kwestia głosowa [smalltalk_10802_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Kwestia głosowa [smalltalk_10802_2] (Chatter #2)] 저는 항상 집중하고 있어야 해요. 그 말은 즉, 관리자님의 사사로운 대화에 맞춰줄 수 없다는 뜻이기도 하고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_2].dlg
   limit: do 150 znaków
   EN: I must remain focused at all times. In other words, I cannot afford to engage in unimportant chitchats with you.
   PL:
116. [Kwestia głosowa [smalltalk_10802_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Kwestia głosowa [smalltalk_10802_3] (Chatter #3)] 으… 혹시라도 제 뿔이 곧 부서질 듯 진동하고 있으면, 모두에게 대피 명령을 내려주세요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_3].dlg
   limit: do 120 znaków
   EN: Unh… If you see my antlers vibrating like they’re about to break, tell everyone to evacuate…
   PL:
118. [Kwestia głosowa [smalltalk_10802_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
119. [Kwestia głosowa [smalltalk_10802_4] (Post-Uptie Chat 1)] 관리자님, 그럴 리는 없겠지만… 혹시 제가 정신을 놓아버리게 되는… \n어느 날이 온다면… 그것도 시계로 해결이 될까요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_4].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Manager, hypothetically speaking… in the slightest chance that I lose my mind…\nIf that does occur… can your clock reverse that, too?
   PL:
120. [Kwestia głosowa [smalltalk_10802_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
121. [Kwestia głosowa [smalltalk_10802_5] (Post-Uptie Chat 2)] 정신을 항상 놓지 않게 버티고 있어야 한다는 건… 잘 때도 정신의 일면은 항상 깨어 있어야 한다는 거예요. \n숙면이란 게 어떤 느낌인지, 기억도 안 나네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=smalltalk_10802_5].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Keeping tight reins on my sanity… entails maintaining conscious control even in my sleep.\nI don’t remember what deep sleep feels like anymore.
   PL:
122. [Kwestia głosowa [neglect_10802_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=neglect_10802_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Kwestia głosowa [neglect_10802_1] (Idle)] 제가 제일 싫어하는 것 중 하나에요. 불러 놓고 먼저 사라지기.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=neglect_10802_1].dlg
   limit: do 120 znaków
   EN: You’re doing one of my least favorite things: calling me here only to leave me behind.
   PL:
124. [Kwestia głosowa [gacksung_10802_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=gacksung_10802_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
125. [Kwestia głosowa [gacksung_10802_1] (Uptying)] 윽… 하아, 힘이 강해진 것 같긴 한데… 두통도 더 심해진 것 같네요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=gacksung_10802_1].dlg
   limit: do 120 znaków
   EN: Hngh… Haah, I feel my power has grown more potent… but my headache’s gotten worse, too…
   PL:
126. [Kwestia głosowa [formation_10802_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=formation_10802_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Kwestia głosowa [formation_10802_1] (Deployment)] 크윽… 준비, 되었어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=formation_10802_1].dlg
   limit: do 120 znaków
   EN: Kngh… I’m—ready.
   PL:
128. [Kwestia głosowa [battleentry_10802_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battleentry_10802_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Kwestia głosowa [battleentry_10802_1] (Stage Entry)] 빨리 시작하시죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battleentry_10802_1].dlg
   limit: do 120 znaków
   EN: Let’s hurry up and get to it.
   PL:
130. [Kwestia głosowa [battle_select_10802_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_select_10802_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Kwestia głosowa [battle_select_10802_1] (Viewed in Battle)] 제정신이랍니다… 아직은.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_select_10802_1].dlg
   limit: do 120 znaków
   EN: I’m in my right mind… for now.
   PL:
132. [Kwestia głosowa [battle_endcommand_10802_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_endcommand_10802_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Kwestia głosowa [battle_endcommand_10802_1] (Commencing Attack)] 후… 전투에 임하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_endcommand_10802_1].dlg
   limit: do 120 znaków
   EN: Huff… Engaging in combat.
   PL:
134. [Kwestia głosowa [battle_enemy_break_10802_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_enemy_break_10802_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Kwestia głosowa [battle_enemy_break_10802_1] (Enemy Stagger)] 정신이 물러… 터졌군요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_enemy_break_10802_1].dlg
   limit: do 120 znaków
   EN: Your mind… is too easy to blow.
   PL:
136. [Kwestia głosowa [battle_break_10802_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_break_10802_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Kwestia głosowa [battle_break_10802_1] (Staggered)] 아!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_break_10802_1].dlg
   limit: do 120 znaków
   EN: Argh!
   PL:
138. [Kwestia głosowa [battle_kill_10802_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_kill_10802_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Kwestia głosowa [battle_kill_10802_1] (Enemy Killed)] 후… 소란이 줄었네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_kill_10802_1].dlg
   limit: do 120 znaków
   EN: Huff… The noise is reduced a little.
   PL:
140. [Kwestia głosowa [battle_allydead_10802_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_allydead_10802_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Kwestia głosowa [battle_allydead_10802_1] (Ally Death)] 으윽… 머리에… 소음이 너무 심해요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_allydead_10802_1].dlg
   limit: do 120 znaków
   EN: Urgh… My head… Too much noise…
   PL:
142. [Kwestia głosowa [choice_success_p_10802_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=choice_success_p_10802_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Kwestia głosowa [choice_success_p_10802_1] (Check Passed)] 완수… 했어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=choice_success_p_10802_1].dlg
   limit: do 120 znaków
   EN: Task… complete.
   PL:
144. [Kwestia głosowa [choice_fail_n_10802_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=choice_fail_n_10802_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Kwestia głosowa [choice_fail_n_10802_1] (Check Failed)] 죄송합니다. …윽, 머리가 깨지겠어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=choice_fail_n_10802_1].dlg
   limit: do 120 znaków
   EN: Apologies. …Nrh, my head is pounding.
   PL:
146. [Kwestia głosowa [battle_clear_10802_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_clear_10802_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Kwestia głosowa [battle_clear_10802_1] (Victory Cry)] 다행… 이네요… 제정신인 동안 끝나서.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_clear_10802_1].dlg
   limit: do 120 znaków
   EN: How… fortunate… We managed to end this while I was sane.
   PL:
148. [Kwestia głosowa [battle_clear_ex_10802_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_clear_ex_10802_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Kwestia głosowa [battle_clear_ex_10802_1] (Extra Conditions Fulfilled)] 윽… 전류가 너무 강하게 방출되었어요. 괴롭지만… 다행이에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_clear_ex_10802_1].dlg
   limit: do 120 znaków
   EN: Hngh… The electric discharge was too intense. It hurts, but… at least it’s over.
   PL:
150. [Kwestia głosowa [battle_defeat_10802_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_defeat_10802_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Kwestia głosowa [battle_defeat_10802_1] (Defeat Wail)] 큭… 머리가… 다른 사람들은 모두 정신 괜찮나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_RCorp4_10802.json :: dataList[id=battle_defeat_10802_1].dlg
   limit: do 120 znaków
   EN: Gah… My head… Are everyone else’s psyches alright?
   PL:

## [00] Shi Assoc. South Section 5 — Ishmael — 남부 시 협회 5과
- ID Tożsamości: `10803` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

152. [Karta Tożsamości — tytuł] 남부 시 협회\n5과
   źródło: Personalities.json :: dataList[id=10803].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nSouth Section 5
   PL:
153. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10803].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10803].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Karta Tożsamości — opis] 이스마엘의 세번째 인격
   źródło: Personalities.json :: dataList[id=10803].desc
   limit: do 120 znaków
   EN: Ishmael’s 3rd Identity
   PL:
156. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 비검
   źródło: Skills.json :: dataList[id=1080301].levelList[level=1].name ; dataList[id=1080301].levelList[level=2].name ; dataList[id=1080301].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flying Sword
   PL:
157. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1080301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
158. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 체력이 50%미만일 때 이 스킬로 얻는 호흡 +1
   źródło: Skills.json :: dataList[id=1080301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At less than 50% HP, this skill gives 1 additional [Breath]
   PL:
159. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1080301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
160. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 체력이 50%미만일 때 이 스킬로 얻는 호흡 +3
   źródło: Skills.json :: dataList[id=1080301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At less than 50% HP, this skill gives 3 additional [Breath]
   PL:
161. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 섬격
   źródło: Skills.json :: dataList[id=1080302].levelList[level=1].name ; dataList[id=1080302].levelList[level=2].name ; dataList[id=1080302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flashing Strike
   PL:
162. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL:
163. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 자신의 체력이 50%미만일 때, 스킬의 1, 2코인이 추가됨
   źródło: Skills.json :: dataList[id=1080302].levelList[level=2].desc ; dataList[id=1080302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At less than 50% HP, use Coin 1 and 2 an additional time
   PL:
165. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
166. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
168. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 숨고르기
   źródło: Skills.json :: dataList[id=1080303].levelList[level=3].name ; dataList[id=1080303].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 6 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Catch Breath
   PL:
170. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1080303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 체력이 25%미만일 때, 피해량의 100%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1080303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] At less than 25% HP, heal 100% of damage dealt
   PL:
172. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 호흡 횟수가 5 이상이면, 크리티컬 피해량 +50%
   źródło: Skills.json :: dataList[id=1080303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 5+ [Breath] Count, +50% Critical Damage
   PL:
173. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1080304].levelList[level=1].name ; dataList[id=1080304].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Counter
   PL:
174. [Obrona (ulepszenie 4) — opis] 자신의 호흡 횟수가 5 이상이면, 크리티컬 피해량 +50%
   źródło: Skills.json :: dataList[id=1080304].levelList[level=4].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
176. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — nazwa] 사선발악
   źródło: Passives.json :: dataList[id=1080301].name
   limit: do 40 znaków
   EN: Walking the Line of Death
   PL:
177. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — opis] 자신의 체력이 50%미만일 때 스킬 효과로 얻는 호흡 +1
   źródło: Passives.json :: dataList[id=1080301].desc
   limit: do 120 znaków
   EN: At less than 50% HP, gain 1 additional Poise from skills.
   PL:
178. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Envy) — nazwa] 투쟁
   źródło: Passives.json :: dataList[id=1080321].name
   limit: do 40 znaków
   EN: Strife
   PL:
179. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Envy) — opis] 현재 체력이 가장 낮은 아군 1명 반격 스킬의 최종 위력 +2
   źródło: Passives.json :: dataList[id=1080321].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP gains +2 counter skill final Power.
   PL:
180. [Kwestia głosowa [get_10803_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=get_10803_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [get_10803_1] (Identity Acquisition)] 누구보다 신속하게… 그들에게 침묵을 안겨드리죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=get_10803_1].dlg
   limit: do 120 znaków
   EN: With impeccable swiftness… I will render them silent.
   PL:
182. [Kwestia głosowa [lobby_morning_10803_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=lobby_morning_10803_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [lobby_morning_10803_1] (Morning Greeting)] 언제나 아침은 고요하죠. 의외로 행인이 없으니, 암살에도 적합한 시간대입니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=lobby_morning_10803_1].dlg
   limit: do 150 znaków
   EN: The morning is always quiet. It’s also a surprisingly viable time for assassination due to the lack of passersby.
   PL:
184. [Kwestia głosowa [lobby_noon_10803_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=lobby_noon_10803_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [lobby_noon_10803_1] (Afternoon Greeting)] 할 말 있으신가요? 기다려드릴 시간 정도는 있어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=lobby_noon_10803_1].dlg
   limit: do 120 znaków
   EN: Is there anything you want to say? I can afford a moment to hear it.
   PL:
186. [Kwestia głosowa [lobby_night_10803_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=lobby_night_10803_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [lobby_night_10803_1] (Evening Greeting)] 달빛이 흩어지네요… 이런 날에는 그림자에 숨어들기 좋죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=lobby_night_10803_1].dlg
   limit: do 120 znaków
   EN: The moonlight scatters… This is an opportune day for blending into the shade.
   PL:
188. [Kwestia głosowa [smalltalk_10803_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [smalltalk_10803_1] (Chatter #1)] 저는 언제나 지켜보고 있어요, 관리자님. 그저 저를 불러주기만 하세요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_1].dlg
   limit: do 120 znaków
   EN: I’m always watching, Manager. Just call when you need something.
   PL:
190. [Kwestia głosowa [smalltalk_10803_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [smalltalk_10803_2] (Chatter #2)] 다음 목표를 알려주세요. 신속하게 시작할게요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_2].dlg
   limit: do 120 znaków
   EN: Give me my next target. I’ll make quick work of them.
   PL:
192. [Kwestia głosowa [smalltalk_10803_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [smalltalk_10803_3] (Chatter #3)] 요새 히스클리프 씨가 심기를 거슬리게 하는데… 뭐, 결과는 나쁘지 않으니까요. 이 수첩이요? …아무것도 아니에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_3].dlg
   limit: do 190 znaków
   EN: Heathcliff has been irritating me lately… Though, I can’t deny that he brings serviceable results with him. This note? …It’s nothing to worry about.
   PL:
194. [Kwestia głosowa [smalltalk_10803_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [smalltalk_10803_4] (Post-Uptie Chat 1)] 제가 예전에 있었던 곳… 거기에 단테 씨가 있었더라면 결과가 조금은 달라졌을까요?\n 그 지옥조차도… 조금은 살만했을까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_4].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Where I used to be… would things have gone differently if you were there with us?\nCould that hell have been… somewhat bearable?
   PL:
196. [Kwestia głosowa [smalltalk_10803_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [smalltalk_10803_5] (Post-Uptie Chat 2)] 전 붉은 색이 좋아요. 색이 진해질수록 피는 멎지 않고 끝이 앞당겨지니까요. …\n그리고 단테씨의 머리 색과도 같잖아요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=smalltalk_10803_5].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I favor the color red. A deeper hue bespeaks an unstopping hemorrhage and briskly arriving demise.\n…Plus, it’s the color of your head, too.
   PL:
198. [Kwestia głosowa [neglect_10803_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=neglect_10803_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [neglect_10803_1] (Idle)] 관리자 님…? 제가 못 찾을 거라고 생각하시나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=neglect_10803_1].dlg
   limit: do 120 znaków
   EN: Executive Manager…? Do you really think you can hide from me?
   PL:
200. [Kwestia głosowa [gacksung_10803_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=gacksung_10803_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [gacksung_10803_1] (Uptying)] 보여드리죠. 더욱 깔끔하고 확실하게.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=gacksung_10803_1].dlg
   limit: do 120 znaków
   EN: I’ll repay the favor with my performance, now that it’s more reliable and efficient.
   PL:
202. [Kwestia głosowa [formation_10803_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=formation_10803_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [formation_10803_1] (Deployment)] 모두에게, 평등하게.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=formation_10803_1].dlg
   limit: do 120 znaków
   EN: An equal fate to all.
   PL:
204. [Kwestia głosowa [battleentry_10803_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battleentry_10803_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Kwestia głosowa [battleentry_10803_1] (Stage Entry)] 목표인가요? 손쉽죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battleentry_10803_1].dlg
   limit: do 120 znaków
   EN: Is that my target? Should be easy.
   PL:
206. [Kwestia głosowa [battle_select_10803_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_select_10803_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Kwestia głosowa [battle_select_10803_1] (Viewed in Battle)] 임무 중에 찾아오시면 안 되는데…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_select_10803_1].dlg
   limit: do 120 znaków
   EN: You aren’t supposed to visit me in the middle of a mission…
   PL:
208. [Kwestia głosowa [battle_endcommand_10803_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_endcommand_10803_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Kwestia głosowa [battle_endcommand_10803_1] (Commencing Attack)] 그 누구도 볼 수 없게.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_endcommand_10803_1].dlg
   limit: do 120 znaków
   EN: Unseen by any.
   PL:
210. [Kwestia głosowa [battle_enemy_break_10803_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_enemy_break_10803_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Kwestia głosowa [battle_enemy_break_10803_1] (Enemy Stagger)] 다음은 침묵을 안겨드리죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_enemy_break_10803_1].dlg
   limit: do 120 znaków
   EN: I’ll render you silent next.
   PL:
212. [Kwestia głosowa [battle_break_10803_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_break_10803_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Kwestia głosowa [battle_break_10803_1] (Staggered)] 아!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_break_10803_1].dlg
   limit: do 120 znaków
   EN: Ah!
   PL:
214. [Kwestia głosowa [battle_kill_10803_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_kill_10803_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Kwestia głosowa [battle_kill_10803_1] (Enemy Killed)] 완전한 침묵.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_kill_10803_1].dlg
   limit: do 120 znaków
   EN: Total silence.
   PL:
216. [Kwestia głosowa [battle_allydead_10803_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_allydead_10803_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Kwestia głosowa [battle_allydead_10803_1] (Ally Death)] 후… 잘 숨었더라면 괜찮았을 텐데.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_allydead_10803_1].dlg
   limit: do 120 znaków
   EN: Huff… You’d have been fine if you stayed hidden.
   PL:
218. [Kwestia głosowa [choice_success_p_10803_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=choice_success_p_10803_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Kwestia głosowa [choice_success_p_10803_1] (Check Passed)] 이 정도는 하급 임무 축에도 안 드네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=choice_success_p_10803_1].dlg
   limit: do 120 znaków
   EN: Wouldn’t even count as a low rank mission.
   PL:
220. [Kwestia głosowa [choice_fail_n_10803_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=choice_fail_n_10803_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Kwestia głosowa [choice_fail_n_10803_1] (Check Failed)] 이번 임무의 성공 확률은 고지 드렸던 것 같은데요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=choice_fail_n_10803_1].dlg
   limit: do 120 znaków
   EN: I’m sure I told you the likelihood of success for this mission…
   PL:
222. [Kwestia głosowa [battle_clear_10803_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_clear_10803_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Kwestia głosowa [battle_clear_10803_1] (Victory Cry)] 정해진 결말이죠. 다음 작전은 어떤 거죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_clear_10803_1].dlg
   limit: do 120 znaków
   EN: A predetermined conclusion. What’s my next mission?
   PL:
224. [Kwestia głosowa [battle_clear_ex_10803_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_clear_ex_10803_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Kwestia głosowa [battle_clear_ex_10803_1] (Extra Conditions Fulfilled)] 깔끔한 전투였어요. 적의 모든 급소를 파악했거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_clear_ex_10803_1].dlg
   limit: do 120 znaków
   EN: That was a smooth battle. I was able to see through all the enemy’s weaknesses.
   PL:
226. [Kwestia głosowa [battle_defeat_10803_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_defeat_10803_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Kwestia głosowa [battle_defeat_10803_1] (Defeat Wail)] 제가 지나치게 빨랐던 건가요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_ShiAsso5_10803.json :: dataList[id=battle_defeat_10803_1].dlg
   limit: do 120 znaków
   EN: Was I too fast for everyone else to follow?
   PL:

## [00] LCCB Assistant Manager — Ishmael — LCCB 대리
- ID Tożsamości: `10804` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 82 · szybkość: 1–5 / 1–5 / 2–6 / 2–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor, Rupture

228. [Karta Tożsamości — tytuł] LCCB\n대리
   źródło: Personalities.json :: dataList[id=10804].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCCB\nAssistant Manager
   PL:
229. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10804].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10804].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Karta Tożsamości — opis] 이스마엘의 네번째 인격
   źródło: Personalities.json :: dataList[id=10804].desc
   limit: do 120 znaków
   EN: Ishmael’s 4th Identity
   PL:
232. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 밀쳐내기
   źródło: Skills.json :: dataList[id=1080401].levelList[level=1].name ; dataList[id=1080401].levelList[level=2].name ; dataList[id=1080401].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Shove
   PL:
233. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1080401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze
   PL:
234. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills.json :: dataList[id=1080401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL:
235. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n대상의 [Vibration]이 8 이상이면, 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1080401].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\nIf target has 8+ [Vibration], Skill Power +2
   PL:
236. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 진동탄
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].name ; dataList[id=1080402].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Quake Rounds
   PL:
237. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Attack Power Down
   PL:
238. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 4 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 4 [Vibration]
   PL:
239. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 4 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Attack Power Down
   PL:
241. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 8 부여. 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 8 [Vibration]; Inflict +2 [Vibration] Count
   PL:
242. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 8 부여. 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080402].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 제압
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].name ; dataList[id=1080403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Suppress
   PL:
244. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
245. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 파열 4 부여. 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 4 Rupture; Inflict +2 Rupture Count
   PL:
246. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 파열 4 부여. 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 취약 5 부여.
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 5 Fragile
   PL:
248. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 진동 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1080403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 5+ [Vibration] Count, Coin Power +1
   PL:
249. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1080404].levelList[level=1].name ; dataList[id=1080404].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+8)
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n탄환이 0일 때, 도발치 추가 2 증가
   źródło: Skills.json :: dataList[id=1080404].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\nAt 0 Ammo, gain 2 more Aggro
   PL:
251. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — nazwa] 약점포착
   źródło: Passives.json :: dataList[id=1080401].name
   limit: do 40 znaków
   EN: Eye for Weakness
   PL:
252. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — opis] 합 승리 후 공격 적중 시마다 진동 1 부여
   źródło: Passives.json :: dataList[id=1080401].desc
   limit: do 120 znaków
   EN: Attacks inflict 1 Tremor in a won clash.
   PL:
253. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Glut.) — nazwa] 매뉴얼대로
   źródło: Passives.json :: dataList[id=1080421].name
   limit: do 40 znaków
   EN: By the Manual
   PL:
254. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Glut.) — opis] 속도가 가장 낮은 아군 1명 가드 스킬의 최종 위력 +2
   źródło: Passives.json :: dataList[id=1080421].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed gains +2 guard skill final Power.
   PL:
255. [Kwestia głosowa [get_10804_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=get_10804_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Kwestia głosowa [get_10804_1] (Identity Acquisition)] 본 측, 이스마엘. 제가 도와드릴 게 있나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=get_10804_1].dlg
   limit: do 120 znaków
   EN: Ishmael speaking. Is there anything I can help you with?
   PL:
257. [Kwestia głosowa [lobby_morning_10804_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=lobby_morning_10804_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Kwestia głosowa [lobby_morning_10804_1] (Morning Greeting)] 아, 아침… 체조 중이랍니다. 미리 몸을 풀어놓고 있어야 되거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=lobby_morning_10804_1].dlg
   limit: do 120 znaków
   EN: Ah, I was… doing my morning routine. I need to warm up my body for what’s to come.
   PL:
259. [Kwestia głosowa [lobby_noon_10804_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=lobby_noon_10804_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Kwestia głosowa [lobby_noon_10804_1] (Afternoon Greeting)] 밥은 항상 균형 잡힌 식단으로 먹어야 해요. 진정한 프로는 편식 따위 하진 않으니까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=lobby_noon_10804_1].dlg
   limit: do 120 znaków
   EN: I make sure to have a balanced diet at all times. True professionals are not picky eaters.
   PL:
261. [Kwestia głosowa [lobby_night_10804_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=lobby_night_10804_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Kwestia głosowa [lobby_night_10804_1] (Evening Greeting)] 문제없는 하루였나요, 관리자님? 저는 이제야 좀 쉴 것 같네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=lobby_night_10804_1].dlg
   limit: do 120 znaków
   EN: Did you have an untroubled day, Manager? It looks like I can finally rest.
   PL:
263. [Kwestia głosowa [smalltalk_10804_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Kwestia głosowa [smalltalk_10804_1] (Chatter #1)] 전 효율적인 작전 설계와 정찰 방법에 대해 누구보다 잘 알고 있답니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_1].dlg
   limit: do 120 znaków
   EN: I know better than anyone about efficient mission planning and reconnaissance.
   PL:
265. [Kwestia głosowa [smalltalk_10804_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Kwestia głosowa [smalltalk_10804_2] (Chatter #2)] 관리자님의 핵심 능력 중 하나는 팀의 에이스를 어떻게 잘 써먹느냐는 거겠죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_2].dlg
   limit: do 140 znaków
   EN: One of the key qualities a manager must possess is the ability to utilize the ace members of their team.
   PL:
267. [Kwestia głosowa [smalltalk_10804_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Kwestia głosowa [smalltalk_10804_3] (Chatter #3)] 작전이 내려오면, 누구누구처럼 무작정 돌진 하는 것만큼 최악의 행동은 없답니다. 모든 변수를 다 예상해야 해요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_3].dlg
   limit: do 190 znaków
   EN: When carrying out missions, there’s nothing worse than charging in without a thought—like a certain someone. You need to anticipate every variable.
   PL:
269. [Kwestia głosowa [smalltalk_10804_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Kwestia głosowa [smalltalk_10804_4] (Post-Uptie Chat 1)] 알아요, 제가 가끔은 강박적인 수준으로 사전 계획에 집착하고 있다는 거요. \n하지만 사소한 실수가 분열로, 그리고 전멸로 이어지는 건 다 아시겠죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_4].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I know—I know I can be obsessive about preplanning at times.\nIn my defense, however, you should be well aware that even a small mistake can lead to discordance and consequently a total wipeout.
   PL:
271. [Kwestia głosowa [smalltalk_10804_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Kwestia głosowa [smalltalk_10804_5] (Post-Uptie Chat 2)] 가끔… 관리자님의 능력을 보면 다행이다 싶다가도 뼛속까지 허무해지기도 해요. \n제대로 된 수습도 없이 죽어간 옛 대원들은...
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=smalltalk_10804_5].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Occasionally… your capabilities reassure me, Manager. But at the same time, it leaves me with this empty feeling.\nThinking about my old teammates—they couldn’t even be given a proper burial…
   PL:
273. [Kwestia głosowa [gacksung_10804_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=gacksung_10804_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Kwestia głosowa [gacksung_10804_1] (Uptying)] 승진이요? 네, 알고 있었답니다. …고맙다는 인사는 해야겠네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=gacksung_10804_1].dlg
   limit: do 120 znaków
   EN: A promotion? Yes, I was aware of it. …I do suppose I owe you some thanks.
   PL:
275. [Kwestia głosowa [neglect_10804_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=neglect_10804_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Kwestia głosowa [neglect_10804_1] (Idle)] 하… 또 다른 분들 뒤치다꺼리 하러 가신 건가요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=neglect_10804_1].dlg
   limit: do 120 znaków
   EN: Sigh… Have you gone off to clean up after the others again?
   PL:
277. [Kwestia głosowa [formation_10804_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=formation_10804_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Kwestia głosowa [formation_10804_1] (Deployment)] 작전호출, 입감.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=formation_10804_1].dlg
   limit: do 120 znaków
   EN: Mission confirmed, now on stand-by.
   PL:
279. [Kwestia głosowa [battleentry_10804_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battleentry_10804_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Kwestia głosowa [battleentry_10804_1] (Stage Entry)] 준비는 끝났습니다. 명령 대기.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battleentry_10804_1].dlg
   limit: do 120 znaków
   EN: Preparations are complete. Awaiting orders.
   PL:
281. [Kwestia głosowa [battle_select_10804_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_select_10804_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Kwestia głosowa [battle_select_10804_1] (Viewed in Battle)] …수신.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_select_10804_1].dlg
   limit: do 120 znaków
   EN: …Wilco.
   PL:
283. [Kwestia głosowa [battle_endcommand_10804_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_endcommand_10804_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Kwestia głosowa [battle_endcommand_10804_1] (Commencing Attack)] 교전 시작합니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_endcommand_10804_1].dlg
   limit: do 120 znaków
   EN: Engaging the target.
   PL:
285. [Kwestia głosowa [battle_enemy_break_10804_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_enemy_break_10804_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Kwestia głosowa [battle_enemy_break_10804_1] (Enemy Stagger)] 표적 무력화.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_enemy_break_10804_1].dlg
   limit: do 120 znaków
   EN: Target incapacitated.
   PL:
287. [Kwestia głosowa [battle_break_10804_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_break_10804_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Kwestia głosowa [battle_break_10804_1] (Staggered)] 앗!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_break_10804_1].dlg
   limit: do 120 znaków
   EN: Ah!
   PL:
289. [Kwestia głosowa [battle_kill_10804_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_kill_10804_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Kwestia głosowa [battle_kill_10804_1] (Enemy Killed)] 표적, 완전 무력화.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_kill_10804_1].dlg
   limit: do 120 znaków
   EN: Target neutralization confirmed.
   PL:
291. [Kwestia głosowa [battle_allydead_10804_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_allydead_10804_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Kwestia głosowa [battle_allydead_10804_1] (Ally Death)] …의무팀, 의무팀은 없어요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_allydead_10804_1].dlg
   limit: do 120 znaków
   EN: …Medic, don’t we have a medical team?
   PL:
293. [Kwestia głosowa [choice_success_p_10804_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=choice_success_p_10804_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Kwestia głosowa [choice_success_p_10804_1] (Check Passed)] 아, 상황 종료라고 알림.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=choice_success_p_10804_1].dlg
   limit: do 120 znaków
   EN: Ahem, reporting in that we’re all clear.
   PL:
295. [Kwestia głosowa [choice_fail_n_10804_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=choice_fail_n_10804_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Kwestia głosowa [choice_fail_n_10804_1] (Check Failed)] 실패… 라고 알림.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=choice_fail_n_10804_1].dlg
   limit: do 120 znaków
   EN: Mission status… failure.
   PL:
297. [Kwestia głosowa [battle_clear_10804_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_clear_10804_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Kwestia głosowa [battle_clear_10804_1] (Victory Cry)] 임무 완료. 절차대로 복귀하겠습니다. 교신 끝.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_clear_10804_1].dlg
   limit: do 120 znaków
   EN: Mission complete. Returning to base per procedure. Out.
   PL:
299. [Kwestia głosowa [battle_clear_ex_10804_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_clear_ex_10804_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Kwestia głosowa [battle_clear_ex_10804_1] (Extra Conditions Fulfilled)] 이 정도면 훈장감… 아, 정정! 임무 완료라고 알림. 교, 교신 끝!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_clear_ex_10804_1].dlg
   limit: do 130 znaków
   EN: This could earn me a medal… Ah, disregard this transmission! Mission complete. I-Ishmael, out!
   PL:
301. [Kwestia głosowa [battle_defeat_10804_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_defeat_10804_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Kwestia głosowa [battle_defeat_10804_1] (Defeat Wail)] 제 방식은 완벽했어요. 원인은 다른 곳에서 찾아보길 바란답니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Sode_10804.json :: dataList[id=battle_defeat_10804_1].dlg
   limit: do 130 znaków
   EN: My methodology was flawless. If you’re looking for a reason we failed, kindly search elsewhere.
   PL:

## [00] Lobotomy E.G.O::Sloshing — Ishmael — 로보토미 E.G.O:: 출렁임
- ID Tożsamości: `10805` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 90 · szybkość: 1–6 / 2–6 / 2–7 / 2–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor, Rupture

303. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n출렁임
   źródło: Personalities.json :: dataList[id=10805].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Sloshing
   PL:
304. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10805].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10805].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Karta Tożsamości — opis] 이스마엘의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10805].desc
   limit: do 120 znaków
   EN: Ishmael’s 5th Identity
   PL:
307. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 무거워...!
   źródło: Skills.json :: dataList[id=1080501].levelList[level=1].name ; dataList[id=1080501].levelList[level=2].name ; dataList[id=1080501].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: It's Heavy...!
   PL:
308. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1080501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL:
310. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1080501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 2, 파열 2 부여
   źródło: Skills.json :: dataList[id=1080501].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 2 [Vibration] and 2 Rupture
   PL:
312. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 울렁거려...!
   źródło: Skills.json :: dataList[id=1080502].levelList[level=1].name ; dataList[id=1080502].levelList[level=2].name ; dataList[id=1080502].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: It's Churning...!
   PL:
313. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL:
315. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
316. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
317. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 3, 파열 3 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 3 [Vibration] and 3 Rupture
   PL:
318. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 부식성 점액 타격
   źródło: Skills.json :: dataList[id=1080503].levelList[level=1].name ; dataList[id=1080503].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 1 (+16)
   limit: do 40 znaków
   EN: Corrosive Splash
   PL:
319. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 진동 횟수 4 감소. 파열 5 부여
   źródło: Skills.json :: dataList[id=1080503].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nAfter triggering [VibrationExplosion], reduce [Vibration] Count by 4. Inflict 5 Rupture
   PL:
320. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 5, 파열 5 부여
   źródło: Skills.json :: dataList[id=1080503].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 5 [Vibration] and 5 Rupture
   PL:
321. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1080504].levelList[level=1].name ; dataList[id=1080504].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가
   źródło: Skills.json :: dataList[id=1080504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn
   PL:
323. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Gloom) — nazwa] 차오르는 액체
   źródło: Passives.json :: dataList[id=1080501].name
   limit: do 40 znaków
   EN: Filling Fluid
   PL:
324. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Gloom) — opis] 공격 스킬로 대상의 체력에 피해를 주지 못한 경우, 다음 턴에 최대 체력의 5%만큼 보호막을 얻음 (최대 30)
   źródło: Passives.json :: dataList[id=1080501].desc
   limit: do 160 znaków
   EN: If this unit fails to deal HP damage using attack skills in a turn, gain a Shield equal to 5% of Max HP next turn. (Max 30)
   PL:
325. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 부식 점액
   źródło: Passives.json :: dataList[id=1080521].name
   limit: do 40 znaków
   EN: Corrosive Slime
   PL:
326. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 속도가 가장 빠른 아군 1명이 진동 폭발 발동 시 파열 2 부여
   źródło: Passives.json :: dataList[id=1080521].desc
   limit: do 120 znaków
   EN: When 1 ally with the fastest Speed triggers Tremor Burst, they inflict 2 Rupture.
   PL:
327. [Kwestia głosowa [get_10805_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=get_10805_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Kwestia głosowa [get_10805_1] (Identity Acquisition)] 하… 비웃지 마세요. 저도 좋아서 이딴 걸 입었겠어요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=get_10805_1].dlg
   limit: do 120 znaków
   EN: Haah... Please hold that laughter. Does it look like I wore this because I liked it?
   PL:
329. [Kwestia głosowa [lobby_morning_10805_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=lobby_morning_10805_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Kwestia głosowa [lobby_morning_10805_1] (Morning Greeting)] 아침부터 기분 더럽네… 아, 들으셨나요? 하지만… 사실이에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=lobby_morning_10805_1].dlg
   limit: do 130 znaków
   EN: It's morning, and I already feel like ass... Oh, sorry, did you hear that? But... it really is true.
   PL:
331. [Kwestia głosowa [lobby_noon_10805_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=lobby_noon_10805_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Kwestia głosowa [lobby_noon_10805_1] (Afternoon Greeting)] 그거 아시나요. 이 끈덕거리는거, 더럽게 맛이 없어요.\n어떻게 알았냐고요…? 점심 시간에 벗어두기 귀찮아서… 여기까지 하죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=lobby_noon_10805_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You know, this sticky thing tastes awful.\nHow do I know...? I couldn't be bothered to take it off during lunchtime, and... let's stop here.
   PL:
333. [Kwestia głosowa [lobby_night_10805_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=lobby_night_10805_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [lobby_night_10805_1] (Evening Greeting)] 장점이라… 이것 보세요. 야광 날개예요. 밤에 불을 켤 필요도 없죠. 유일한 장점이네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=lobby_night_10805_1].dlg
   limit: do 170 znaków
   EN: Upsides, you ask... Check this out. The wings glow. Don't have to turn on the lights at night. I guess that's the one upside it has.
   PL:
335. [Kwestia głosowa [smalltalk_10805_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [smalltalk_10805_1] (Chatter #1)] 이상하게… 기운은 축축 쳐지지만 생긴 거에 비해 무겁지는 않아요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_1].dlg
   limit: do 150 znaków
   EN: Weirdly enough... while it drags my mood down to the bottom of the barrel, it's not actually as heavy as it looks.
   PL:
337. [Kwestia głosowa [smalltalk_10805_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [smalltalk_10805_2] (Chatter #2)] 아핫! …저, 저리 가세요… 하, 이걸 입고 나서부터 자꾸 주정뱅이들 처럼 웃게 되네요. 짜증나.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_2].dlg
   limit: do 150 znaków
   EN: Ahah! ...L-Leave me alone, please... Haah, I keep laughing like drunkards ever since I put this on. It sucks.
   PL:
339. [Kwestia głosowa [smalltalk_10805_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [smalltalk_10805_3] (Chatter #3)] …날 수 없다니까, 몇 번을 묻는 건가요? 애초에, 이런 조그만 날개로… 하, 그만두죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_3].dlg
   limit: do 150 znaków
   EN: ...How many times do you have to ask? I can't fly. I mean, look how small these wings are, and... Haah, forget it.
   PL:
341. [Kwestia głosowa [smalltalk_10805_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [smalltalk_10805_4] (Post-Uptie Chat 1)] 음… 요정주 한 잔… 대체 왜 이런 말을 하게 되는 거죠? 관리자 님! 당신은 아시는 거죠?!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_4].dlg
   limit: do 140 znaków
   EN: Mmm... A glass of fairy wine... What makes me keep saying this stuff? Manager! You know the answer, right?!
   PL:
343. [Kwestia głosowa [smalltalk_10805_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [smalltalk_10805_5] (Post-Uptie Chat 2)] 왜 제가 이런걸 써야하는 지는 아직도 모르겠지만… 그래도, 쓰면 쓸수록 몸에 익기는 하네요.\n아뇨! 이 젤리 같은걸 말하는 게 아니라, 무기로 쓰는 걸 말하는 거예요!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=smalltalk_10805_5].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I still don't know why I have to use this thing... but, it does get more familiar as I keep using it.\nNo! I am NOT talking about this jelly-like thing, I specifically mean the weapon!
   PL:
345. [Kwestia głosowa [gacksung_10805_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=gacksung_10805_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [gacksung_10805_1] (Uptying)] 결국… 이딴 걸로 인정까지 받는 군요… 좋아해야 할지, 싫어해야 할지.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=gacksung_10805_1].dlg
   limit: do 120 znaków
   EN: Oh, joy... I get recognition for this nonsense... Not sure how I should feel about it.
   PL:
347. [Kwestia głosowa [neglect_10805_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=neglect_10805_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [neglect_10805_1] (Idle)] 하… 의자에 앉으면 묻어서 앉기도 싫네…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=neglect_10805_1].dlg
   limit: do 120 znaków
   EN: Haah... I don't even feel like sitting, this thing sticks to chairs if I try...
   PL:
349. [Kwestia głosowa [formation_10805_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=formation_10805_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [formation_10805_1] (Deployment)] 기술들을 해방하러 가죠. 안 익숙해서… 조금 느리지만.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=formation_10805_1].dlg
   limit: do 120 znaków
   EN: Let's go free some technology. I'm not too used to this, so... I might be a bit slow.
   PL:
351. [Kwestia głosowa [battleentry_10805_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battleentry_10805_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [battleentry_10805_1] (Stage Entry)] 으… 치덕거려.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battleentry_10805_1].dlg
   limit: do 120 znaków
   EN: Ugh... It's gooey.
   PL:
353. [Kwestia głosowa [battle_select_10805_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_select_10805_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [battle_select_10805_1] (Viewed in Battle)] 꿀꿀하니까, 용건만 간단히요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_select_10805_1].dlg
   limit: do 120 znaków
   EN: Not in the mood, please make it short.
   PL:
355. [Kwestia głosowa [battle_endcommand_10805_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_endcommand_10805_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [battle_endcommand_10805_1] (Commencing Attack)] 갑니다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_endcommand_10805_1].dlg
   limit: do 120 znaków
   EN: Here I go!
   PL:
357. [Kwestia głosowa [battle_enemy_break_10805_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_enemy_break_10805_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [battle_enemy_break_10805_1] (Enemy Stagger)] 한 잔!…아니, 한 방 먹혔지?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_enemy_break_10805_1].dlg
   limit: do 120 znaków
   EN: A toast! ...I mean, a clean hit, right?
   PL:
359. [Kwestia głosowa [battle_break_10805_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_break_10805_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_break_10805_1] (Staggered)] 우엑…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_break_10805_1].dlg
   limit: do 120 znaków
   EN: Bwegh...
   PL:
361. [Kwestia głosowa [battle_kill_10805_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_kill_10805_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [battle_kill_10805_1] (Enemy Killed)] 취해서 쓰러지는군.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_kill_10805_1].dlg
   limit: do 120 znaków
   EN: Knocked out by the booze.
   PL:
363. [Kwestia głosowa [battle_dead_10805_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_dead_10805_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [battle_dead_10805_1] (Ally Death)] 아… 이럴 때까지 끈적거리고… 말이야…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_dead_10805_1].dlg
   limit: do 120 znaków
   EN: Bah... You had to keep being sticky... to the bitter end...
   PL:
365. [Kwestia głosowa [choice_success_p_10805_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=choice_success_p_10805_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Kwestia głosowa [choice_success_p_10805_2] (Check Passed)] 끈덕지게 관찰한 결과죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=choice_success_p_10805_2].dlg
   limit: do 120 znaków
   EN: Observing with gluey tenacity paid off.
   PL:
367. [Kwestia głosowa [choice_fail_n_10805_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=choice_fail_n_10805_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Kwestia głosowa [choice_fail_n_10805_1] (Check Failed)] 으, 이게 걸리적 거려서 그런거예요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=choice_fail_n_10805_1].dlg
   limit: do 120 znaków
   EN: Ugh, it's this thing's fault for getting in the way.
   PL:
369. [Kwestia głosowa [battle_clear_10805_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_clear_10805_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Kwestia głosowa [battle_clear_10805_1] (Victory Cry)] 휴. 어떻게든 처리 했네요. …이걸로 기술해방에 좀 더 도움이 되었겠죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_clear_10805_1].dlg
   limit: do 120 znaków
   EN: Phew. That's dealt with somehow. ...This will help free more technologies, right?
   PL:
371. [Kwestia głosowa [battle_clear_ex_10805_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_clear_ex_10805_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Kwestia głosowa [battle_clear_ex_10805_1] (Extra Conditions Fulfilled)] 아핫! 해결한 김에, 요정주… 아, 또 헛소리를… 돌아가죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_clear_ex_10805_1].dlg
   limit: do 150 znaków
   EN: Ahah! Now that that's done, let's drink some fairy... Oh, there I go again with the twaddle... Let's get back.
   PL:
373. [Kwestia głosowa [battle_defeat_10805_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_defeat_10805_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Kwestia głosowa [battle_defeat_10805_1] (Defeat Wail)] 젠장… 우린 해방에 실패했군요. 뭐하나 되는게 없네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LEGO_10805.json :: dataList[id=battle_defeat_10805_1].dlg
   limit: do 120 znaków
   EN: Damn it... We've failed to liberate. Nothing is working out.
   PL:

## [000] Liu Assoc. South Section 4 — Ishmael — 남부 리우 협회 4과
- ID Tożsamości: `10806` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

375. [Karta Tożsamości — tytuł] 남부 리우 협회\n4과
   źródło: Personalities.json :: dataList[id=10806].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 4
   PL:
376. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10806].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10806].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Karta Tożsamości — opis] 이스마엘의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10806].desc
   limit: do 120 znaków
   EN: Ishmael’s 6th Identity
   PL:
379. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 단각
   źródło: Skills.json :: dataList[id=1080601].levelList[level=1].name ; dataList[id=1080601].levelList[level=2].name ; dataList[id=1080601].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Red Kick
   PL:
380. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL:
381. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion]이 3 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1080601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 3+ [Combustion], Coin Power +1
   PL:
383. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 화상 3당, 코인 위력 +1 (최대 2)
   źródło: Skills.json :: dataList[id=1080601].levelList[level=4].desc
   limit: do 120 znaków
   EN: Coin Power +1 for every 3 Burn on target (Max 2)
   PL:
384. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정면 돌파
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].name ; dataList[id=1080602].levelList[level=2].name ; dataList[id=1080602].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Frontal Assault
   PL:
385. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 화상 횟수 2 부여
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1080602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1080602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict 2 Burn Count
   PL:
388. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1080602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL:
389. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 화상 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills.json :: dataList[id=1080602].levelList[level=4].desc
   limit: do 120 znaków
   EN: Coin Power +1 for every 6 Burn on target (Max 2)
   PL:
390. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 이문정주
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].name ; dataList[id=1080603].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Inner Gate Elbow Strike
   PL:
391. [Umiejętność 3 (×1) (ulepszenie 1) — opis] 대상의 화상과 화상 횟수가 6 이상이면, 피해량 +30%
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has 6+ Burn and Burn Count, deal +30% damage
   PL:
392. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Burn Count
   PL:
395. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 4, efekt 1 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 다음 턴에 더하기 코인 강화 1을 얻음
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] If target is Staggered or defeated, gain 1 Plus Coin Boost next turn
   PL:
396. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 화상과 화상 횟수가 6 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1080603].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 6+ Burn and Burn Count, deal +50% damage
   PL:
397. [Obrona (ulepszenie 1) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1080604].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Burn Count
   PL:
399. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 격화
   źródło: Passives.json :: dataList[id=1080601].name
   limit: do 40 znaków
   EN: Intense Blaze
   PL:
400. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 대상의 화상 횟수 3 당 타격 피해량 +10% (최대 30%)
   źródło: Passives.json :: dataList[id=1080601].desc
   limit: do 120 znaków
   EN: Deal +10% Blunt damage for every 3 Burn Count on target. (Max 30%)
   PL:
401. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — nazwa] 격화
   źródło: Passives.json :: dataList[id=1080621].name
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — opis] 속도가 가장 느린 아군 1명이 공격 적중 시 대상의 화상 횟수 3 당 타격 피해량 +5% (최대 15%)
   źródło: Passives.json :: dataList[id=1080621].desc
   limit: do 130 znaków
   EN: 1 ally with the slowest Speed deals +5% Blunt damage for every 3 Burn Count on target. (Max 15%)
   PL:
403. [Kwestia głosowa [get_10806_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=get_10806_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Kwestia głosowa [get_10806_1] (Identity Acquisition)] 저를 부르셨나요? 앗 뜨… 네, 무슨 일이죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=get_10806_1].dlg
   limit: do 120 znaków
   EN: You called me? Ow, my tongue's burning... Right, how can I help?
   PL:
405. [Kwestia głosowa [lobby_morning_10806_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=lobby_morning_10806_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Kwestia głosowa [lobby_morning_10806_1] (Morning Greeting)] 아무리 몸쓰는 일이 많다곤 해도… 오전에는 저희도 서류작업이 꽤 있는 편이죠. 회의도 하고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=lobby_morning_10806_1].dlg
   limit: do 150 znaków
   EN: As often as we get physical... we still have paperwork to take care of in the morning. There are meetings, too.
   PL:
407. [Kwestia głosowa [lobby_noon_10806_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=lobby_noon_10806_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Kwestia głosowa [lobby_noon_10806_1] (Afternoon Greeting)] 자~ 밥 먹고 하죠, 이번에도 우육면 먹으러 갈 거면 안 따라 갈 거라고요? 아니, 그럼 주변에 거기 만한 데가 또 있나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=lobby_noon_10806_1].dlg
   limit: do 210 znaków
   EN: Alright~ Let's go eat something first. You aren't gonna follow along if it's beef noodles again? I mean, what other place around here serves meals that good?
   PL:
409. [Kwestia głosowa [lobby_night_10806_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=lobby_night_10806_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Kwestia głosowa [lobby_night_10806_1] (Evening Greeting)] 하… 밤 훈련 때는 선글라스라도 써야 할까봐요. 자꾸 불꽃이 올라오는 탓에 눈이 너무 아파요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=lobby_night_10806_1].dlg
   limit: do 140 znaków
   EN: Haah... Maybe I should wear sunglasses for night training. All the flickering flames are hard on my eyes.
   PL:
411. [Kwestia głosowa [smalltalk_10806_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Kwestia głosowa [smalltalk_10806_1] (Chatter #1)] 여기요? 네, 자주 오죠. 단골인걸요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_1].dlg
   limit: do 120 znaków
   EN: This venue? Sure, I go often. I'm a regular.
   PL:
413. [Kwestia głosowa [smalltalk_10806_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [smalltalk_10806_2] (Chatter #2)] 이 옷에 새겨진 자수는 월광석으로 만들어진 것이에요. 높은 과에 배정받을 때 마다 무늬가 늘어난다고 하더라고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_2].dlg
   limit: do 150 znaków
   EN: This clothing's embroidery was made with moonlight stones. I heard higher sections get more of these fancyworks.
   PL:
415. [Kwestia głosowa [smalltalk_10806_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [smalltalk_10806_3] (Chatter #3)] 분위기가 좋은 것 같다고요? 뭐… 그렇게 보일 수도 있겠네요. 저희야 워낙, 모여서 부대끼는 일이 잦으니까요.\n흥, 하지만 식사자리에는 잘 안 따라와 주는 걸요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_3].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We look like we get along fine? Well... I see how you get that impression. We gather up and rub shoulders with each other pretty much all the time, after all.\nHmph, and yet they won't join me to dine nearly as often.
   PL:
417. [Kwestia głosowa [smalltalk_10806_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [smalltalk_10806_4] (Post-Uptie Chat 1)] 리우 협회에서는 워낙 다양한 권법이나 무술을 배울 수 있는 기회가 있는데 저는 팔극권이 취향에 맞더라고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_4].dlg
   limit: do 160 znaków
   EN: Liu Association offers opportunities to learn all kinds of martial arts and techniques, Bajiquan was my personal favorite.
   PL:
419. [Kwestia głosowa [smalltalk_10806_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [smalltalk_10806_5] (Post-Uptie Chat 2)] 아… 날붙이에 어떻게 대응하냐고요? 훗, 이 자켓은 그런 것에 쉽게 뚫리지 않는답니다. 저보다 더 윗 과에 계신 분들의 원단은 더 한 것도 막을 걸요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=smalltalk_10806_5].dlg
   limit: do 250 znaków
   EN: Ah... You wanna know how we deal with sharp weapons? Heh, this jacket isn't easily penetrated by the likes of them. The fabric used by my coworkers in higher sections can stop even more, I think?
   PL:
421. [Kwestia głosowa [gacksung_10806_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=gacksung_10806_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [gacksung_10806_1] (Uptying)] …그렇군요. 더 호출이 잦아지겠네요. 뭐, 권법을 더 단련 해두죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=gacksung_10806_1].dlg
   limit: do 120 znaków
   EN: ...I see. I'll get busier, won't I. Well, I'll be training myself to prepare for it.
   PL:
423. [Kwestia głosowa [neglect_10806_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=neglect_10806_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [neglect_10806_1] (Idle)] 음… 다음에 먹을 메뉴나… 찾아볼까?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=neglect_10806_1].dlg
   limit: do 120 znaków
   EN: Hmm... Should I look up... what to eat next?
   PL:
425. [Kwestia głosowa [formation_10806_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=formation_10806_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [formation_10806_1] (Deployment)] 함께하죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=formation_10806_1].dlg
   limit: do 120 znaków
   EN: I'm with you.
   PL:
427. [Kwestia głosowa [battleentry_10806_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battleentry_10806_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [battleentry_10806_1] (Stage Entry)] 제가 앞에 서죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battleentry_10806_1].dlg
   limit: do 120 znaków
   EN: I'll take the front.
   PL:
429. [Kwestia głosowa [battle_select_10806_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_select_10806_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [battle_select_10806_1] (Viewed in Battle)] 가까이 오지 마세요. 다치십니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_select_10806_1].dlg
   limit: do 120 znaków
   EN: Keep your distance. You'll get yourself hurt.
   PL:
431. [Kwestia głosowa [battle_endcommand_10806_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_endcommand_10806_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [battle_endcommand_10806_1] (Commencing Attack)] 순식간에 끝내죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_endcommand_10806_1].dlg
   limit: do 120 znaków
   EN: I'll end this in a moment.
   PL:
433. [Kwestia głosowa [battle_enemy_break_10806_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_enemy_break_10806_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [battle_enemy_break_10806_1] (Enemy Stagger)] 한 놈…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_enemy_break_10806_1].dlg
   limit: do 120 znaków
   EN: That's one...
   PL:
435. [Kwestia głosowa [battle_break_10806_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_break_10806_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [battle_break_10806_1] (Staggered)] 크윽…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_break_10806_1].dlg
   limit: do 120 znaków
   EN: Kgh...
   PL:
437. [Kwestia głosowa [battle_kill_10806_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_kill_10806_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [battle_kill_10806_1] (Enemy Killed)] 보냈고!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_kill_10806_1].dlg
   limit: do 120 znaków
   EN: Down the gutter!
   PL:
439. [Kwestia głosowa [battle_dead_10806_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_dead_10806_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
440. [Kwestia głosowa [battle_dead_10806_1] (Death)] 아… 우육… 면… 먹고 싶… 네.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_dead_10806_1].dlg
   limit: do 120 znaków
   EN: Agh... I could... really use... a bowl of beef... noodles.
   PL:
441. [Kwestia głosowa [choice_success_p_10806_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=choice_success_p_10806_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [choice_success_p_10806_2] (Check Passed)] 이 정도는 쉽죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=choice_success_p_10806_2].dlg
   limit: do 120 znaków
   EN: This is no trouble at all.
   PL:
443. [Kwestia głosowa [choice_fail_n_10806_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=choice_fail_n_10806_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [choice_fail_n_10806_1] (Check Failed)] 쳇… 실패했습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=choice_fail_n_10806_1].dlg
   limit: do 120 znaków
   EN: Tch... I've failed.
   PL:
445. [Kwestia głosowa [battle_clear_10806_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_clear_10806_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [battle_clear_10806_1] (Victory Cry)] 이 정도면… 그럭저럭 나쁘지 않죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_clear_10806_1].dlg
   limit: do 120 znaków
   EN: This... wasn't too bad, don't you think?
   PL:
447. [Kwestia głosowa [battle_clear_ex_10806_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_clear_ex_10806_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [battle_clear_ex_10806_1] (Extra Conditions Fulfilled)] 후~ 깔끔하게 해결했네요. 가는 길에 우육면 드실래요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_clear_ex_10806_1].dlg
   limit: do 120 znaków
   EN: Whew~ That was a job well done. Wanna have some beef noodles on the way back?
   PL:
449. [Kwestia głosowa [battle_defeat_10806_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_defeat_10806_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [battle_defeat_10806_1] (Defeat Wail)] 좀 더… 단련과 경험의 시간이 필요한 것 같군요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_LiuAsso4_10806.json :: dataList[id=battle_defeat_10806_1].dlg
   limit: do 120 znaków
   EN: I'll need... more experience and training, it seems...
   PL:

## [000] Molar Boatworks Fixer — Ishmael — 어금니 보트 센터 해결사
- ID Tożsamości: `10807` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 70 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Sinking, Tremor

451. [Karta Tożsamości — tytuł] 어금니 보트 센터\n해결사
   źródło: Personalities.json :: dataList[id=10807].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molar Boatworks\nFixer
   PL:
452. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10807].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10807].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Karta Tożsamości — opis] 이스마엘의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10807].desc
   limit: do 120 znaków
   EN: Ishmael’s 7th Identity
   PL:
455. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 파쇄 준비
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=1].name ; dataList[id=1080701].levelList[level=2].name ; dataList[id=1080701].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Ready to Crush
   PL:
456. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Tremor Count
   PL:
457. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Sinking Count
   PL:
458. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=2].desc ; dataList[id=1080701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Tremor Count
   PL:
459. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL:
460. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 작렬
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].name ; dataList[id=1080702].levelList[level=2].name ; dataList[id=1080702].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Explosive Blast
   PL:
461. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Tremor Count
   PL:
462. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Sinking
   PL:
463. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Defense Level Down next turn
   PL:
464. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 자신의 진동 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].desc ; dataList[id=1080702].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 5+ Tremor Count, Coin Power +1
   PL:
465. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Tremor Count
   PL:
466. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1080702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Tremor Count
   PL:
467. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Defense Level Down next turn
   PL:
468. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 4 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Defense Level Down next turn
   PL:
469. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과격한 판단
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].name ; dataList[id=1080703].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Risky Judgement
   PL:
470. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 진동 횟수가 5 이상이면, 코인 위력 +1\n대상의 침잠이 6 이상이면, 피해량 +20%
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 5+ Tremor Count, Coin Power +1\nIf target has 6+ Sinking, deal +20% damage
   PL:
471. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 5 증가
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +5 Sinking Count
   PL:
472. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL:
473. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수 5를 소모하여 다음 턴에 취약 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1080703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 5 Tremor Count to inflict 1 Fragile next turn
   PL:
474. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수 5를 소모하여 다음 턴에 취약 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1080703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 5 Tremor Count to inflict 2 Fragile next turn
   PL:
476. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 진동 횟수가 5 당, 코인 위력 +1(최대 2)\n대상의 침잠이 6 이상이면, 피해량 +40%
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coin Power +1 for every 5 Tremor Count on self (Max 2)\nIf target has 6+ Sinking, deal +40% damage
   PL:
477. [Obrona (ulepszenie 1) — nazwa] 신속 보법
   źródło: Skills_personality-08.json :: dataList[id=1080704].levelList[level=1].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Nimble Steps
   PL:
478. [Obrona (ulepszenie 1) — opis] [WhenUse] 파열 보호 2를 얻음 (턴 당 최대 6)
   źródło: Skills_personality-08.json :: dataList[id=1080704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Rupture Protection (6 times per turn)
   PL:
479. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 크랲 파쇄
   źródło: Passives.json :: dataList[id=1080701].name
   limit: do 40 znaków
   EN: Crushin' Crabs
   PL:
480. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] [Vibration]이 있는 대상에게 공격 적중 시 침잠 횟수 1 증가
   źródło: Passives.json :: dataList[id=1080701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: On Hit against a target that has [Vibration], inflict +1 Sinking Count
   PL:
481. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 크랲 드라이버
   źródło: Passives.json :: dataList[id=1080721].name
   limit: do 40 znaków
   EN: Crab Driver
   PL:
482. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 최대 체력이 가장 낮은 아군이 공격 적중 시 앞면이 나온 경우, 코인 효과로 진동 횟수를 적에게 부여할 때 침잠 횟수 1 부여
   źródło: Passives.json :: dataList[id=1080721].desc
   limit: do 200 znaków
   EN: When an ally that has the lowest Max HP hits with Heads Coins, they inflict +1 Sinking Count when inflicting Tremor Count on their target with Coin effects.
   PL:
483. [Kwestia głosowa [get_10807_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=get_10807_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Kwestia głosowa [get_10807_1] (Identity Acquisition)] 하, 가까이 오지 마세요. 아직 잡아야 할 게들이 산더미니까. 그리고… 게 내장 묻을 수도 있어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=get_10807_1].dlg
   limit: do 140 znaków
   EN: Haah, keep your distance. I still have loads of crabs to hunt. Plus... you do NOT want crab guts on you.
   PL:
485. [Kwestia głosowa [lobby_morning_10807_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=lobby_morning_10807_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Kwestia głosowa [lobby_morning_10807_1] (Morning Greeting)] 아침에 일찍 일찍 움직여야죠. 저녁거리도 미리 잡아둬야하고, 술 마실 시간도 벌어야 하니까.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=lobby_morning_10807_1].dlg
   limit: do 120 znaków
   EN: Early bird gets the worm, you know. And the dinner. And the time for drinking.
   PL:
487. [Kwestia głosowa [lobby_noon_10807_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=lobby_noon_10807_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Kwestia głosowa [lobby_noon_10807_1] (Afternoon Greeting)] 후… 푹푹 찌네요. 정말. 그거 아세요? 여긴 한낮일 때 뻘에서 올라오는 습기랑 비린내가 장난 아니예요. 짜증만 한가득 난다니까요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=lobby_noon_10807_1].dlg
   limit: do 190 znaków
   EN: Phew... It's sweltering. Seriously. Wanna know what's more? Come midday, this place gets awful humid and begins to reek of fish. It's infuriating.
   PL:
489. [Kwestia głosowa [lobby_night_10807_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=lobby_night_10807_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Kwestia głosowa [lobby_night_10807_1] (Evening Greeting)] 해가 졌으니까, 슬슬 쉬어봐야죠. 마침…? 담궈놓았던 비장의 술이 완성되는 날이거든요! 후후.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=lobby_night_10807_1].dlg
   limit: do 180 znaków
   EN: Well, the sun's gone down, and it's about time I went home for the day. And guess what? Today I pop the cork off my secret wine! Hehe.
   PL:
491. [Kwestia głosowa [smalltalk_10807_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Kwestia głosowa [smalltalk_10807_1] (Chatter #1)] 날씨만 좀 선선해도 할 만할 것 같은데, 으…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_1].dlg
   limit: do 120 znaków
   EN: If only the weather was a bit cooler. Ugh...
   PL:
493. [Kwestia głosowa [smalltalk_10807_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Kwestia głosowa [smalltalk_10807_2] (Chatter #2)] 어어… 그 크<size=110%>랲</size> 드라이버 위험해요. 폐품으로 급조하고 덧댄 거라, 잘 모르고 사용하면 뼈가 부러질 수도 있다고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_2].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>
   EN: Hey... Be careful with that crab driver. It's got a makeshift mod with scraps, so it could break your bones if you're not careful.
   PL:
495. [Kwestia głosowa [smalltalk_10807_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Kwestia głosowa [smalltalk_10807_3] (Chatter #3)] 아, 지금 하고 있는거요? 잇, 이렇게 폐품은 크<size=110%>랲</size>게에게서 전부 떼어 전달해 줘야 하니까요… 그래야 폐품으로 새로운 부품을 만들고, 보트 센터도 운영하고. 요리하기에도 용이해질 테니까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_3].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>
   EN: Oh, what am I doing? Uh, we have to pull the scraps off the trash crabs first before processing them... That's how we make new stuff with the scrap, run the workshop, and cook us up dinner.
   PL:
497. [Kwestia głosowa [smalltalk_10807_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Kwestia głosowa [smalltalk_10807_4] (Post-Uptie Chat 1)] 그러고 보니… 그 커다란 놈이 우리 공방이 있는 곳까지 기어 올라온 적이 있었어요. 완전 밑바닥일 때부터 저희를 도와주셨던 분들을 전부 죽이고… 유유히 떠났죠.\n뭐, 그렇다고 특별한 악감정은 없어요. 그 큰 놈도 그렇고, 저도 그렇듯이. 생존을 위해 싸우는 것 뿐이죠. …그게 그놈인지도 모르겠고.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_4].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Now that I think about it... the big one once crawled all the way up to our workshop. It killed everyone that helped us get started and... just left.\nI don't harbor any hatred against it, though. The big guy, me, we're both just fighting to survive. ...I don't even know if it's the same one, either.
   PL:
499. [Kwestia głosowa [smalltalk_10807_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Kwestia głosowa [smalltalk_10807_5] (Post-Uptie Chat 2)] 흠~ 너무 빼지 말고, 가끔은 같이 마시죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=smalltalk_10807_5].dlg
   limit: do 120 znaków
   EN: Hmph~ Quit being a teetotaler and join us sometimes, huh?
   PL:
501. [Kwestia głosowa [gacksung_10807_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=gacksung_10807_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Kwestia głosowa [gacksung_10807_1] (Uptying)] 엇챠… 크<size=110%>랲</size> 드라이버를 좀 더 개조해 봤죠. 아무래도 역시 이걸로 그 큰 놈을 잡아봐야 겠어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=gacksung_10807_1].dlg
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>
   EN: Hup... I made a few modifications to the crab driver. I might try using this one to get the big guy.
   PL:
503. [Kwestia głosowa [neglect_10807_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=neglect_10807_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Kwestia głosowa [neglect_10807_1] (Idle)] 후우… 푹푹 찌는구만…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=neglect_10807_1].dlg
   limit: do 120 znaków
   EN: Whew... it's so hot out here...
   PL:
505. [Kwestia głosowa [formation_10807_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=formation_10807_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Kwestia głosowa [formation_10807_1] (Deployment)] 다들, 연장 챙기죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=formation_10807_1].dlg
   limit: do 120 znaków
   EN: Grab your tools, everyone.
   PL:
507. [Kwestia głosowa [battleentry_10807_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battleentry_10807_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Kwestia głosowa [battleentry_10807_1] (Stage Entry)] 잠수 준비 끝.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battleentry_10807_1].dlg
   limit: do 120 znaków
   EN: Ready to dive.
   PL:
509. [Kwestia głosowa [battle_select_10807_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_select_10807_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Kwestia głosowa [battle_select_10807_1] (Viewed in Battle)] 뭐죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_select_10807_1].dlg
   limit: do 120 znaków
   EN: What's up?
   PL:
511. [Kwestia głosowa [battle_endcommand_10807_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_endcommand_10807_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Kwestia głosowa [battle_endcommand_10807_1] (Commencing Attack)] 꽂아 터트려주지.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_endcommand_10807_1].dlg
   limit: do 120 znaków
   EN: I'll harpoon and crack you open.
   PL:
513. [Kwestia głosowa [battle_enemy_break_10807_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_enemy_break_10807_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Kwestia głosowa [battle_enemy_break_10807_1] (Enemy Stagger)] 얼얼하지, 정신 못 차릴 거야.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_enemy_break_10807_1].dlg
   limit: do 120 znaków
   EN: How's that? Painful, I'm sure.
   PL:
515. [Kwestia głosowa [battle_break_10807_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_break_10807_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Kwestia głosowa [battle_break_10807_1] (Staggered)] 어우…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_break_10807_1].dlg
   limit: do 120 znaków
   EN: Oww...
   PL:
517. [Kwestia głosowa [battle_kill_10807_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_kill_10807_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Kwestia głosowa [battle_kill_10807_1] (Enemy Killed)] 파쇄 완료.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_kill_10807_1].dlg
   limit: do 120 znaków
   EN: Crushed it.
   PL:
519. [Kwestia głosowa [battle_dead_10807_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_dead_10807_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Kwestia głosowa [battle_dead_10807_1] (Death)] 아… 하… 이렇게 끝나는… 건가?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_dead_10807_1].dlg
   limit: do 120 znaków
   EN: Ah... Haa... Is this... the end?
   PL:
521. [Kwestia głosowa [choice_success_p_10807_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=choice_success_p_10807_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Kwestia głosowa [choice_success_p_10807_2] (Check Passed)] 좋아, 잘 됐네!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=choice_success_p_10807_2].dlg
   limit: do 120 znaków
   EN: Nice, I did it!
   PL:
523. [Kwestia głosowa [choice_fail_n_10807_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=choice_fail_n_10807_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Kwestia głosowa [choice_fail_n_10807_1] (Check Failed)] 견적이 안 나오네, 이거…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=choice_fail_n_10807_1].dlg
   limit: do 120 znaków
   EN: Man, I'm not sure about this...
   PL:
525. [Kwestia głosowa [battle_clear_10807_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_clear_10807_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Kwestia głosowa [battle_clear_10807_1] (Victory Cry)] 얼른 돌아가서 씻고 쉬기나 하자고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_clear_10807_1].dlg
   limit: do 120 znaków
   EN: Come on, let's go home 'n clean and rest up.
   PL:
527. [Kwestia głosowa [battle_clear_ex_10807_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_clear_ex_10807_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Kwestia głosowa [battle_clear_ex_10807_1] (Extra Conditions Fulfilled)] 흠… 이 정도면 보수도 짭짤하겠는데. 다들 땅고기 외식이나 할까요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_clear_ex_10807_1].dlg
   limit: do 120 znaków
   EN: Hmm... This'll be pretty lucrative. How about we barbecue some land animal for once?
   PL:
529. [Kwestia głosowa [battle_defeat_10807_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_defeat_10807_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Kwestia głosowa [battle_defeat_10807_1] (Defeat Wail)] 에휴… 이러면 위약금 물어야 하는 거 아닌가?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ucorp_10807.json :: dataList[id=battle_defeat_10807_1].dlg
   limit: do 120 znaków
   EN: Sigh... Now I gotta pay the penalty fees, don't I?
   PL:

## [000] The Pequod Captain — Ishmael — 피쿼드호 선장
- ID Tożsamości: `10808` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 68 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Burn, Poise

531. [Karta Tożsamości — tytuł] 피쿼드호\n선장
   źródło: Personalities.json :: dataList[id=10808].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pequod\nCaptain
   PL:
532. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10808].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10808].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Karta Tożsamości — opis] 이스마엘의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10808].desc
   limit: do 120 znaków
   EN: Ishmael’s 8th Identity
   PL:
535. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 내 주위에 서라!
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=1].name ; dataList[id=1080801].levelList[level=2].name ; dataList[id=1080801].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: To Me!
   PL:
536. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 자신을 제외하고 최대 체력이 가장 높은 아군 1명의 가장 왼쪽 슬롯의 [Aggro]가 (가장 높은 공명 수) 만큼 증가 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Next turn, the leftmost Skill Slot of 1 other ally with the highest Max HP gains +(highest Reson.) [Aggro] (Once per turn)
   PL:
537. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL:
538. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 자신을 제외하고 최대 체력이 가장 높은 아군 1명의 가장 왼쪽 슬롯의 [Aggro]가 (가장 높은 공명 수) 만큼 증가 (턴 당 1회)\n- 가장 높은 완전 공명의 합이 4 이상이면, 효과 발동 시 다음 턴에 보호 1 부여 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Next turn, the leftmost Skill Slot of 1 other ally with the highest Max HP gains +(highest Reson.) [Aggro] (Once per turn)\n- At 4+ highest A-Reson., apply 1 Protection to the ally next turn when they gain Aggro (Once per turn)
   PL:
539. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
540. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 방어 레벨 증가 2 부여</style>\n[WhenUse] 다음 턴에 자신을 제외하고 최대 체력이 가장 높은 아군 1명의 가장 왼쪽 슬롯의 [Aggro]가 (가장 높은 공명 수) 만큼 증가 (턴 당 1회)\n- 가장 높은 완전 공명의 합이 4 이상이면, 효과 발동 시 다음 턴에 보호 1 부여 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [WhenUse], [Aggro]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">[StartBattle] Apply 2 Defense Level Up to 2 allies adjacent to this unit on the Dashboard</style>\n[WhenUse] Next turn, the leftmost Skill Slot of 1 other ally with the highest Max HP gains +(highest Reson.) [Aggro] (Once per turn)\n- At 4+ highest A-Reson., apply 1 Protection to the ally next turn when they gain Aggro (Once per turn)
   PL:
541. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 끝까지 추적한다!
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].name ; dataList[id=1080802].levelList[level=2].name ; dataList[id=1080802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Pursue Them to the End!
   PL:
542. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 가장 높은 공명의 공명 당 10% 확률로 조작 패널에서 자신의 우측에 위치한 아군에게 이번 턴에 [CoverAttack]을 명령함.
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [CoverAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CoverAttack] = 원호 공격 / Assist Attack
   EN: [WhenUse] Every Reson. of the highest Reson. adds 10% chance that this unit orders the ally on its immediate right(on the Dashboard) to use [CoverAttack] this turn.
   PL:
543. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
544. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Burn
   PL:
545. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 가장 높은 공명의 공명 당 15% 확률로 조작 패널에서 자신의 우측에 위치한 아군에게 이번 턴에 [CoverAttack]을 명령함.\n- 가장 높은 완전 공명의 합이 4 이상이면, 대상에게 피해량 증가 1 부여\n- 오만 완전 공명의 합이 4 이상이면, 오만 위력 증가 1 추가 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [CoverAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CoverAttack] = 원호 공격 / Assist Attack
   EN: [WhenUse] Every Reson. of the highest Reson. adds 15% chance that this unit orders the ally on its immediate right(on the Dashboard) to use [CoverAttack] this turn.\n- At 4+ highest A-Reson., apply 1 Damage Up to the ally\n- At 4+ Pride A-Reson., apply 1 additional Pride Power Up
   PL:
546. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
547. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1080802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 공격 레벨 증가 3 부여\n[WhenUse] 가장 높은 공명의 공명 당 20% 확률로 조작 패널에서 자신의 우측에 위치한 아군에게 이번 턴에 [CoverAttack]을 명령함.\n- 가장 높은 완전 공명의 합이 4 이상이면, 대상에게 피해량 증가 2 부여\n- 오만 완전 공명의 합이 4 이상이면, 오만 위력 증가 2 추가 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=4].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [CoverAttack]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [CoverAttack] = 원호 공격 / Assist Attack
   EN: [StartBattle] Apply 3 Offense Level Up to 2 allies adjacent to this unit on the Dashboard\n[WhenUse] Every Reson. of the highest Reson. adds 20% chance that this unit orders the ally on its immediate right(on the Dashboard) to use [CoverAttack] this turn.\n- At 4+ highest A-Reson., apply 2 Damage Up to the ally\n- At 4+ Pride A-Reson., apply 2 additional Pride Power Up
   PL:
549. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 집착의 작살
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].name ; dataList[id=1080803].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Harpoon of Obsession
   PL:
551. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 잃은 체력 1% 당 피해량 +0.2% (최대 20%)\n[EndSkill] 적이 흐트러짐 상태가 되거나 사망하면, 정신력이 가장 낮은 아군 1 + (가장 높은 완전 공명 수/2)명의 정신력 10 회복, 호흡 2 호흡 횟수 4 부여 (최대 2회. 최대 회복 인원 수: 4명)
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal more damage based on target's missing HP (+0.2% damage per 1% missing HP, max +20%)\n[EndSkill] If target is Staggered or defeated, (1+(highest A-Reson./2)) allies with the least SP heal 10 SP, gain 2 Poise, and +4 Poise Count. (2 times max. Max # of allies that can be healed: 4)
   PL:
552. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL:
553. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1080803].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 잃은 체력 1% 당 피해량 +0.3% (최대 30%)\n대상의 [Laceration] 5 당 코인 위력 +1 (최대 2)\n[EndSkill] 적이 흐트러짐 상태가 되거나 사망하면, 정신력이 가장 낮은 아군 1 + (가장 높은 완전 공명 수/2)명의 정신력 10 회복, 호흡 2 호흡 횟수 4 부여 (최대 4회. 최대 회복 인원 수: 4명)
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal more damage based on target's missing HP (+0.3% damage per 1% missing HP, max +30%)\nCoin Power +1 for every 5 [Laceration] on target (Max 2)\n[EndSkill] If target is Staggered or defeated, (1+(highest A-Reson./2)) allies with the least SP heal 10 SP, gain 2 Poise, and gain +4 Poise Count. (4 times max. Max # of allies that can be healed: 4)
   PL:
556. [Obrona (ulepszenia 1,4) — nazwa] 공포를 날려주지
   źródło: Skills_personality-08.json :: dataList[id=1080804].levelList[level=1].name ; dataList[id=1080804].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Do Not Fear
   PL:
557. [Obrona (ulepszenie 1) — opis] [WhenUse] 조작 패널에서 자신의 양 옆의 아군 정신력 3 회복 (최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1080804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 3 SP for 2 allies adjacent to this unit on the Dashboard (2 times max)
   PL:
558. [Obrona (ulepszenie 4) — opis] [WhenUse] 조작 패널에서 자신의 양 옆의 아군 정신력 5 회복 (최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1080804].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP for 2 allies adjacent to this unit on the Dashboard (2 times max)
   PL:
559. [Pasywka bojowa (od ulepszenia 1) — nazwa] 사냥 시간
   źródło: Passives.json :: dataList[id=1080802].name
   limit: do 40 znaków
   EN: Hour of the Hunt
   PL:
560. [Pasywka bojowa (od ulepszenia 1) — opis] 대상이 <호수의 존재>면 피해량 +10%
   źródło: Passives.json :: dataList[id=1080802].desc
   limit: do 120 znaków
   EN: If the target is a <Lake Entity>, deal +10% damage
   PL:
561. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 피쿼드호의 선장
   źródło: Passives.json :: dataList[id=1080801].name
   limit: do 40 znaków
   EN: Captain of the Pequod
   PL:
562. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 자신의 공격 종료 시 대상이 사망했으면,\n- 다음 턴에 [HeatedGasHarpoon] 상태가 됨.\n- 자신을 제외한 정신력이 가장 낮은 아군 1명의 정신력 7 회복.\n- 대상이 피쿼드호 소속이면, 정신력 5 추가 회복.
   źródło: Passives.json :: dataList[id=1080801].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [HeatedGasHarpoon]
   znaczenie tagów: [HeatedGasHarpoon] = 가열된 가스 작살 / Heated Gas Harpoon
   EN: Attack End: If the enemy is defeated after this unit's attack,\n- gain [HeatedGasHarpoon] next turn.\n- 1 other ally with the least SP heals 7 SP.\n- If the ally is from The Pequod, heal an additional 5 SP.
   PL:
563. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — nazwa] 피쿼드호의 선장
   źródło: Passives.json :: dataList[id=1080811].name
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — opis] 자신의 공격 종료 시 대상이 사망했으면,\n<style="highlight">- 호흡 4, 호흡 횟수 2를 얻고, 다음 턴에 [OverHeatedGasHarpoon] 상태가 됨.</style>\n- 자신을 제외한 정신력이 가장 낮은 아군 <style="highlight">2명의 정신력 7 회복, 호흡 4 부여.</style>\n- 대상이 피쿼드호 소속이면, 정신력 5 추가 회복, <style="highlight">턴 당 1회 다음 턴에 관통 위력 증가 1 부여.</style>
   źródło: Passives.json :: dataList[id=1080811].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OverHeatedGasHarpoon]
   znaczenie tagów: [OverHeatedGasHarpoon] = 과열된 가스 작살 / Overheated Gas Harpoon
   EN: - Attack End: If the enemy is defeated after this unit's attack,\n<style="highlight">- gain 4 Poise, +2 Poise Count. Then, gain [OverHeatedGasHarpoon] next turn.</style>\n<style="highlight">- 2 other allies with the least SP heal 7 SP and gain 4 Poise.</style>\n- If the allies are from The Pequod, heal an additional 5 SP. <style="highlight">Then, once per turn, apply 1 Pierce Power Up next turn.</style>
   PL:
565. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 선장의 명령
   źródło: Passives.json :: dataList[id=1080821].name
   limit: do 40 znaków
   EN: Captain's Orders
   PL:
566. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 정신력이 가장 높은 아군 1명이 자신의 공격 종료 시 대상이 사망했으면, 호흡 2 얻음 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1080821].desc
   limit: do 150 znaków
   EN: 1 ally with the highest SP gains 2 Poise when the target is defeated after that unit's attack (2 times per turn)
   PL:
567. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — nazwa] 선장의 명령
   źródło: Passives.json :: dataList[id=1080831].name
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — opis] 정신력이 가장 높은 아군 1명이 자신의 공격 종료 시 대상이 사망했으면, 호흡 2, <style="highlight">호흡 횟수 2</style> 얻음 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1080831].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Attack End: 1 ally with the highest SP gains 2 Poise and <style="highlight">+2 Poise Count</style> when the target is defeated after that unit's attack (2 times per turn)
   PL:
569. [Kwestia głosowa [get_10808_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=get_10808_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Kwestia głosowa [get_10808_1] (Identity Acquisition)] 승선을 환영한다, 신참. 튼튼한 몸뚱아리는 챙겨왔겠지!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=get_10808_1].dlg
   limit: do 120 znaków
   EN: Welcome aboard, greenhorn! You are able-bodied and ready for the voyage, I trust?
   PL:
571. [Kwestia głosowa [lobby_morning_10808_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=lobby_morning_10808_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Kwestia głosowa [lobby_morning_10808_1] (Morning Greeting)] 굼뜨게 움직이는 놈은 제일 먼저 돛대에 걸어둘 거다! 아침이라고 늑장부리지 마!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=lobby_morning_10808_1].dlg
   limit: do 180 znaków
   EN: Do not dilly-dally! If I see one slacker among you, I'll tie them to the mast myself! It's a morning, not a mourning; look alive, men!
   PL:
573. [Kwestia głosowa [lobby_noon_10808_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=lobby_noon_10808_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Kwestia głosowa [lobby_noon_10808_1] (Afternoon Greeting)] 인어 지느러미 육포는 입에 맞나? 맞아야 할걸. 당분간은 그것만 먹어야 할테니. 훗.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=lobby_noon_10808_1].dlg
   limit: do 180 znaków
   EN: How do you like the taste of that Mermaid fin jerky? You better enjoy it. It'll be our main source of sustenance for a good while. Heh.
   PL:
575. [Kwestia głosowa [lobby_night_10808_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=lobby_night_10808_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Kwestia głosowa [lobby_night_10808_1] (Evening Greeting)] 전부 자러 들어갔다고 방심하지 마라. 파도는 낮과 밤을 가리지 않으니… 눈 크게 뜨고 잘 지켜보라고.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=lobby_night_10808_1].dlg
   limit: do 200 znaków
   EN: The hour may be late, but do not let your guard down. The Waves can come crashing in at any moment—day or night. Keep your eyes wide open, am I clear?
   PL:
577. [Kwestia głosowa [smalltalk_10808_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Kwestia głosowa [smalltalk_10808_1] (Chatter #1)] 영문도 모를 것들이 우리를 덮친다고 한들, 두려워할 것 같은가? 마주하고 이빨을 드러내며 웃어라. 그것이 피쿼드호의 선원이다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_1].dlg
   limit: do 200 znaków
   EN: We do not fear the unfathomable horrors of the sea! Stand tall! Give them a toothy grin and a wild guffaw! That is what it means to be a crew of the Pequod!
   PL:
579. [Kwestia głosowa [smalltalk_10808_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Kwestia głosowa [smalltalk_10808_2] (Chatter #2)] 선장실은! 누구도 침범할 수 없다. 할 말이 있다면 항해사에게 해라. 호수의 파도가 무섭다고 징징대는 꼴을 보는 건 질색이니.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_2].dlg
   limit: do 240 znaków
   EN: None shall enter the Captain's quarters! If you have something to share—share it with the navigator. I grow tired of listening to fools whining, cowering at the Waves of the Great Lake.
   PL:
581. [Kwestia głosowa [smalltalk_10808_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [smalltalk_10808_3] (Chatter #3)] 고래는… 경이롭고도 신비한 괴물이다. 나와 함께 그것들을 잡아죽인다는 건, 인생의 큰 영광이지…\n하, 이 호수 위에서 나만큼 그것에 집착하는 자는 없을테니까!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_3].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Whales are... magnificent yet mysterious monsters. Consider it a great honor that you are allowed to hunt them beside me...\nHah, I daresay that my fervor for Whaling is unmatched!
   PL:
583. [Kwestia głosowa [smalltalk_10808_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [smalltalk_10808_4] (Post-Uptie Chat 1)] 작살잡이! 작살을 단단히 묶어라! 조타수는 우현으로 타각 최대! 노잡이!! 정신 차리고 저어라!!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_4].dlg
   limit: do 150 znaków
   EN: Harpooneers! Fasten your harpoons! Helmsmen, right hard rudder! OARSMEN!! Pull yourselves together and ROW!!!
   PL:
585. [Kwestia głosowa [smalltalk_10808_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [smalltalk_10808_5] (Post-Uptie Chat 2)] 총원, 그대로 들어! …때가 도래했다! 오늘 밤, 우리는 고대하던 그 고래를!\n…모든 것을 마르게 하는 새빨간 고래를… 잡는다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=smalltalk_10808_5].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All hands, heed my command! ... Our finest hour is upon us! Tonight, we hunt the Whale!\nTonight, we hunt the All-Withering Crimson Whale!
   PL:
587. [Kwestia głosowa [gacksung_10808_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=gacksung_10808_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [gacksung_10808_1] (Uptying)] 천둥이 몰아치기 시작하는군… 곧 우리가 손꼽아 기다리던 그 악의 고래의 사냥 시간이 찾아온다! 핫하!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=gacksung_10808_1].dlg
   limit: do 170 znaków
   EN: Thunder and lightning... Yes, the battle of our lifetimes will soon be upon us! We will hunt the Whale of all evils! Hahahahahaha!
   PL:
589. [Kwestia głosowa [neglect_10808_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=neglect_10808_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [neglect_10808_1] (Idle)] 후… 바람이 좋군. 가끔씩은 이런 폭풍 전 고요를 즐겨보는 것도 나쁘지 않지.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=neglect_10808_1].dlg
   limit: do 120 znaków
   EN: Haah... These are good winds. I enjoy this particular calm before the storm.
   PL:
591. [Kwestia głosowa [formation_10808_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=formation_10808_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [formation_10808_1] (Deployment)] 고래를 향해.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=formation_10808_1].dlg
   limit: do 120 znaków
   EN: Set course toward the Whale.
   PL:
593. [Kwestia głosowa [battleentry_10808_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battleentry_10808_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [battleentry_10808_1] (Stage Entry)] 가스 점화! 엔진 시동!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battleentry_10808_1].dlg
   limit: do 120 znaków
   EN: Light the gases and fire up the engines!
   PL:
595. [Kwestia głosowa [battle_select_10808_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_select_10808_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [battle_select_10808_1] (Viewed in Battle)] 입을 열 시간이 있나? 고래에 집중해!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_select_10808_1].dlg
   limit: do 120 znaków
   EN: Focus on the Whale if you have the time to flap your gums!
   PL:
597. [Kwestia głosowa [battle_endcommand_10808_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_endcommand_10808_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [battle_endcommand_10808_1] (Commencing Attack)] 총원, 돌격!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_endcommand_10808_1].dlg
   limit: do 120 znaków
   EN: All hands! CHARGE!
   PL:
599. [Kwestia głosowa [battle_enemy_break_10808_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_enemy_break_10808_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [battle_enemy_break_10808_1] (Enemy Stagger)] 기세가 수그러지는군! 반격의 기회다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_enemy_break_10808_1].dlg
   limit: do 120 znaków
   EN: Our foes cower! This is our opportunity to turn the tide!
   PL:
601. [Kwestia głosowa [battle_break_10808_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_break_10808_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [battle_break_10808_1] (Staggered)] 흣…! 전열을 지켜라! 내게 관심이 쏠렸으니, 너희가 공격할 기회는 더욱 많아진다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_break_10808_1].dlg
   limit: do 120 znaków
   EN: Hngh...! Hold your stations! The foe has its eyes on me—use this opportunity to strike them!
   PL:
603. [Kwestia głosowa [battle_kill_10808_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_kill_10808_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [battle_kill_10808_1] (Enemy Killed)] 잘했군! 한 놈도 남지 않을 때 까지 지금을 반복한다! 쉴 새는 없다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_kill_10808_1].dlg
   limit: do 150 znaków
   EN: Good! Do not stop until we have slaughtered every last one of them! We shall seek no respite until it is done!
   PL:
605. [Kwestia głosowa [battle_dead_10808_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_dead_10808_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [battle_dead_10808_1] (Death)] 나, 나는… 이스마엘이다! 나는… 여기서…!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_dead_10808_1].dlg
   limit: do 120 znaków
   EN: I-I am Captain Ishmael! I will not fall... here...!
   PL:
607. [Kwestia głosowa [choice_success_p_10808_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=choice_success_p_10808_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [choice_success_p_10808_2] (Check Passed)] 당연하지. 내 나침반이 틀린 적이 있었나?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=choice_success_p_10808_2].dlg
   limit: do 120 znaków
   EN: Of course. Has my compass ever led you astray?
   PL:
609. [Kwestia głosowa [choice_fail_n_10808_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=choice_fail_n_10808_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [choice_fail_n_10808_1] (Check Failed)] 젠장… 네 탓이군, 관리자!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=choice_fail_n_10808_1].dlg
   limit: do 120 znaków
   EN: Dammit... The fault lies with you, Manager!
   PL:
611. [Kwestia głosowa [battle_clear_10808_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_clear_10808_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [battle_clear_10808_1] (Victory Cry)] 어줍잖은 결과에 들뜨지 말도록! 우리가 사냥할 고래는 더욱 크고 사악하다!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_clear_10808_1].dlg
   limit: do 160 znaków
   EN: Hail not at this mediocre outcome! Set your sights beyond this puerile victory; our Whale is greater, more evil than this!
   PL:
613. [Kwestia głosowa [battle_clear_ex_10808_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_clear_ex_10808_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [battle_clear_ex_10808_1] (Extra Conditions Fulfilled)] 이번엔 성적이 좋았군… 하지만, 머나먼 고래에 닿기 위해서는 아직도 부족하다! 다시 가스 터빈을 점화한다! 그리고…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_clear_ex_10808_1].dlg
   limit: do 140 znaków
   EN: Not bad, not bad at all... But we are still yet to reach the Whale! Fire the gas turbines again, men! And—
   PL:
615. [Kwestia głosowa [battle_defeat_10808_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_defeat_10808_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [battle_defeat_10808_1] (Defeat Wail)] 이 무능한 놈들! 고작 이런 곳에서 쓰러지다니, 내가 네놈들에게 패배를 명령했더냐!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Ahab_10808.json :: dataList[id=battle_defeat_10808_1].dlg
   limit: do 140 znaków
   EN: You useless wretches! You dare fall to your knees here? I do not recall ordering any of you to be defeated!
   PL:

## [00] Edgar Family Butler — Ishmael — 에드가 가문 버틀러
- ID Tożsamości: `10809` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Poise, Sinking

617. [Karta Tożsamości — tytuł] 에드가 가문\n버틀러
   źródło: Personalities.json :: dataList[id=10809].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Edgar Family\nButler
   PL:
618. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10809].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10809].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Karta Tożsamości — opis] 이스마엘의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10809].desc
   limit: do 120 znaków
   EN: Ishmael’s 9th Identity
   PL:
621. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 빗겨쳐내기
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=1].name ; dataList[id=1080901].levelList[level=2].name ; dataList[id=1080901].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Sweeping Redirection
   PL:
622. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
623. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
624. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
625. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면 코인 위력 +1\n[WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL:
626. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Agility]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Agility] = 신속 / Haste
   EN: [CriticalOnSucceedAttack] Gain 1 [Agility] next turn
   PL:
627. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정리정돈
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].name ; dataList[id=1080902].levelList[level=2].name ; dataList[id=1080902].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Housekeeping
   PL:
628. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL:
630. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1080902].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL:
631. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080902].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL:
632. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] [Breath] 횟수 2 증가\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 2 [Breath]
   PL:
633. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면 코인 위력 +1\n[WhenUse] [Breath] 횟수 2 증가\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 2 [Breath]
   PL:
634. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Binding]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [Binding] next turn</style>
   PL:
635. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 동체 속박술
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].name ; dataList[id=1080903].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Restraining Technique
   PL:
637. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [Breath] 6 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 6 [Breath]
   PL:
638. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
639. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
642. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [SlashTakeDamageUp] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1080903].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp] next turn
   PL:
643. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면 코인 위력 +1\n[WhenUse] [Breath] 6 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain 6 [Breath]
   PL:
644. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
645. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-08.json :: dataList[id=1080904].levelList[level=1].name ; dataList[id=1080904].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 정신력 5 회복 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 5 SP (once per turn)
   PL:
647. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — nazwa] 묵은 먼지 털기
   źródło: Passives.json :: dataList[id=1080901].name
   limit: do 40 znaków
   EN: Deep Cleaning
   PL:
648. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — opis] 속도가 자신보다 느린 대상에게 크리티컬 적중 시 자신이 스킬로 부여하는 부정적인 효과의 위력이 1 추가 부여됨 (턴 당 최대 3회)
   źródło: Passives.json :: dataList[id=1080901].desc
   limit: do 220 znaków
   EN: If this unit Critically Hits against targets with Slower Speed than this unit's, inflict 1 additional Potency for negative effects using its Skills (3 times per turn)
   PL:
649. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 충실한 보조
   źródło: Passives.json :: dataList[id=1080921].name
   limit: do 40 znaków
   EN: Loyal Supporter
   PL:
650. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 속도가 가장 빠른 아군 1명이 [Sinking]이 있는 대상 공격 시 대상의 [Sinking] 1당 피해량 0.5% (최대 10%)
   źródło: Passives.json :: dataList[id=1080921].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally with the fastest Speed attacks a target that has [Sinking], deal +0.5% damage for every 1 [Sinking] on target (max 10%)
   PL:
651. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Gloom) — nazwa] 충실한 보조
   źródło: Passives.json :: dataList[id=1080931].name
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Gloom) — opis] 속도가 가장 빠른 아군 1명이 [Sinking]이 있는 대상 공격 시 대상의 [Sinking] 1당 피해량 1% (최대 20%)
   źródło: Passives.json :: dataList[id=1080931].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally with the fastest Speed attacks a target that has [Sinking], deal +1% damage for every 1 [Sinking] on target (max 20%)
   PL:
653. [Kwestia głosowa [get_10809_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=get_10809_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Kwestia głosowa [get_10809_1] (Identity Acquisition)] 이쪽에 아직 먼지가 남아있네요. 기관지가 안 좋으신 분이니 좀 더 철저히… 그냥, 제가 하죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=get_10809_1].dlg
   limit: do 140 znaków
   EN: Oh, there's some dust left here. Remember. Our Master has respiratory issues, so... No, I'll do it myself.
   PL:
655. [Kwestia głosowa [lobby_morning_10809_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=lobby_morning_10809_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Kwestia głosowa [lobby_morning_10809_1] (Morning Greeting)] 좋은 아침입니다, 주인님. 편안한 밤이 되셨나요. 오늘은 아침 식사 이후 일정이 잡혀있으십니다. 일정 중 고단하시지 않게, 식사는 잘 챙겨드시길 바랍니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=lobby_morning_10809_1].dlg
   limit: do 230 znaków
   EN: Good morning, Master. I hope you had a restful sleep. Remember, you have an appointment to attend to after breakfast. Make sure to partake in every meal to keep yourself energized.
   PL:
657. [Kwestia głosowa [lobby_noon_10809_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=lobby_noon_10809_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Kwestia głosowa [lobby_noon_10809_1] (Afternoon Greeting)] 말씀하신 대로, 점심에 찾아뵐 손님을 위해 정문 청소를 중점적으로 해보았습니다\n …아, 그 흙바닥의 붉은 얼룩은 간밤에 불청객이 있어 처리한 흔적이… 지금 처리해두죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=lobby_noon_10809_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As per your orders, we focused on cleaning the front gate in anticipation of the guests arriving for the luncheon.\nOh, that red stain on the gravel are just leftover marks from dealing with last night's uninvited gue— I'll take care of it right away.
   PL:
659. [Kwestia głosowa [lobby_night_10809_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=lobby_night_10809_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Kwestia głosowa [lobby_night_10809_1] (Evening Greeting)] 오늘의 야간 경비 업무는 제가 당번입니다. 문제가 생긴다면 신속하고 조용하게 처리해드릴 겁니다. 주인님께선 언제나 편안한 취침에 들 수 있도록.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=lobby_night_10809_1].dlg
   limit: do 250 znaków
   EN: I'm on the night watch duty tonight. I can assure you that any issues that may arise will be quickly and silently taken care of. I will try my utmost so that you may have a restful night, Master.
   PL:
661. [Kwestia głosowa [smalltalk_10809_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Kwestia głosowa [smalltalk_10809_1] (Chatter #1)] 음주는 지양하시는 편이 좋지 않을까요. 료슈님이 알게 되면 저택의 남은 술을 전부 몰수해버릴텐데요.\n…혹시 잠에 들 수 없으신 거라면, 식사 담당에게 따뜻한 요깃거리라도 귀띔해보겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_1].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Perhaps you could indulge less... in drinking. Should Lady Ryōshū find out about this, she'll confiscate every bottle of liquor in the manor.\nIf you're having trouble with going to sleep, I will give word to the kitchen staff to prepare a hearty late night snack.
   PL:
663. [Kwestia głosowa [smalltalk_10809_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Kwestia głosowa [smalltalk_10809_2] (Chatter #2)] 사냥의 날이 얼마 남지 않은 탓인지, 료슈님이 평소보다 훨씬 날카로워지신 것 같네요. 나이프와 포크는 몇 번이나 다시 닦았는지 제 얼굴이 다 비춰질 정도에요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_2].dlg
   limit: do 240 znaków
   EN: Lady Ryōshū's been on edge as of late... probably because the hunt is coming up so soon. I've polished my knives and forks so many times that I can practically use them like mirrors.
   PL:
665. [Kwestia głosowa [smalltalk_10809_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Kwestia głosowa [smalltalk_10809_3] (Chatter #3)] 조금 추우시더라도, 바람이 온순할 때 창문을 좀 열어두는 편이 좋습니다. 환기를 게을리 하지 않아야, 주인님의 몸이 호전되실 텐데요…\n괜찮으시다면, 잠시 응접실에 계시다가 오실 수 있나요. 제가 쌀쌀해지기 전의 환경으로 만들어 두겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_3].dlg
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I know it's pretty cold outside, but do keep your windows open when the winds aren't as wild. You need as much fresh air as you can get, Master. Your health won't ever improve otherwise.\n... If it is all right with you, would you mind spending a short while in the reception room? I will warm the room in your absence.
   PL:
667. [Kwestia głosowa [smalltalk_10809_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Kwestia głosowa [smalltalk_10809_4] (Post-Uptie Chat 1)] 눈 돌릴 틈도 주지 않겠습니다. 주인님의 땅에 들어선 불청객은, 먹기 좋게 썰린 스테이크처럼 조각조각을 낼 테니까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_4].dlg
   limit: do 220 znaków
   EN: They won't even have the time to look away. Any interloper who dares to tread our Master's land... I'll slice & dice them to pieces like a nice plate of steak bites.
   PL:
669. [Kwestia głosowa [smalltalk_10809_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Kwestia głosowa [smalltalk_10809_5] (Post-Uptie Chat 2)] 사냥을 위해 모인다고요… 네, 저도 반드시 참가하죠. 주인님의 호위와 사냥의 성공을 위해서… 그 폭풍우 치는 언덕에서 최선을 다해 임무를 수행하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=smalltalk_10809_5].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We're gathering for the hunt, huh... Of course, I'll join. For our Master's safety, for the success of the hunt...\nI will see my mission to the end through the wuthering storm.
   PL:
671. [Kwestia głosowa [gacksung_10809_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=gacksung_10809_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Kwestia głosowa [gacksung_10809_1] (Uptying)] 주인님의 집안에 고용된 버틀러가 유능하지 않을리가 없죠. 병약해지신 틈을 타 부당한 이득을 취하려는 놈들은, 제가 청소해드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=gacksung_10809_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I am a Butler in the employment of your household. What else could I possibly provide other than the utmost competence?\nI will clean up every fool who seeks to take advantage of your sickness.
   PL:
673. [Kwestia głosowa [neglect_10809_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=neglect_10809_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Kwestia głosowa [neglect_10809_1] (Idle)] …주인님? 거기에 계속 서 계시면 청소하기 어렵습니다. 잠시 이쪽으로…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=neglect_10809_1].dlg
   limit: do 190 znaków
   EN: ... Master? Would you please consider standing elsewhere? It's... difficult to clean the room with you standing in the middle. This way, please...
   PL:
675. [Kwestia głosowa [formation_10809_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=formation_10809_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Kwestia głosowa [formation_10809_1] (Deployment)] 청소시간이네요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=formation_10809_1].dlg
   limit: do 120 znaków
   EN: Housekeeping time.
   PL:
677. [Kwestia głosowa [battleentry_10809_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battleentry_10809_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Kwestia głosowa [battleentry_10809_1] (Stage Entry)] 버틀러 차원가방, 준비 완료했습니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battleentry_10809_1].dlg
   limit: do 120 znaków
   EN: Butler dimensional attache case at the ready.
   PL:
679. [Kwestia głosowa [battle_select_10809_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_select_10809_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Kwestia głosowa [battle_select_10809_1] (Viewed in Battle)] 네, 도와드릴 것이 있나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_select_10809_1].dlg
   limit: do 120 znaków
   EN: Yes? Is there anything I can help you with?
   PL:
681. [Kwestia głosowa [battle_endcommand_10809_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_endcommand_10809_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Kwestia głosowa [battle_endcommand_10809_1] (Commencing Attack)] 먼지를 떨어내죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_endcommand_10809_1].dlg
   limit: do 120 znaków
   EN: I'll dust them.
   PL:
683. [Kwestia głosowa [battle_enemy_break_10809_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_enemy_break_10809_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Kwestia głosowa [battle_enemy_break_10809_1] (Enemy Stagger)] 묵은 먼지도…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_enemy_break_10809_1].dlg
   limit: do 120 znaków
   EN: Even the old, crusty dirt...
   PL:
685. [Kwestia głosowa [battle_break_10809_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_break_10809_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Kwestia głosowa [battle_break_10809_1] (Staggered)] 핫…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_break_10809_1].dlg
   limit: do 120 znaków
   EN: Hah...!
   PL:
687. [Kwestia głosowa [battle_kill_10809_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_kill_10809_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Kwestia głosowa [battle_kill_10809_1] (Enemy Killed)] 결국은, 이렇게 떨어지죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_kill_10809_1].dlg
   limit: do 120 znaków
   EN: ... Gets dusted in the end.
   PL:
689. [Kwestia głosowa [battle_dead_10809_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_dead_10809_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Kwestia głosowa [battle_dead_10809_1] (Death)] 죄송… 합니다. 주인님… 제 본분을… 지키지…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_dead_10809_1].dlg
   limit: do 120 znaków
   EN: Apolo...gies... Master. I failed... my mission...
   PL:
691. [Kwestia głosowa [choice_success_p_10809_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=choice_success_p_10809_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Kwestia głosowa [choice_success_p_10809_2] (Check Passed)] 저는 유능한 버틀러니까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=choice_success_p_10809_2].dlg
   limit: do 120 znaków
   EN: But of course. I am a competent Butler.
   PL:
693. [Kwestia głosowa [choice_fail_n_10809_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=choice_fail_n_10809_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Kwestia głosowa [choice_fail_n_10809_1] (Check Failed)] 이, 이건… 죄송합니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=choice_fail_n_10809_1].dlg
   limit: do 120 znaków
   EN: T-this is... my apologies.
   PL:
695. [Kwestia głosowa [battle_clear_10809_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_clear_10809_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Kwestia głosowa [battle_clear_10809_1] (Victory Cry)] 조금 소란스러웠어도 나쁘지 않은 청소 결과네요. 료슈님이 만족하실지는 모르겠지만.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_clear_10809_1].dlg
   limit: do 170 znaków
   EN: We made a bit of a ruckus, but we put them all in the bin. Though I'm not sure if this will be to Lady Ryōshū's satisfaction.
   PL:
697. [Kwestia głosowa [battle_clear_ex_10809_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_clear_ex_10809_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Kwestia głosowa [battle_clear_ex_10809_1] (Extra Conditions Fulfilled)] 먼지 한 톨 남지 않은 완벽한 청소였어요. 주인님은 간 밤에 뭐가 다녀갔는지도 모르실테죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_clear_ex_10809_1].dlg
   limit: do 130 znaków
   EN: Didn't even leave a speck of dust behind. I'm sure Master won't even notice what happened overnight.
   PL:
699. [Kwestia głosowa [battle_defeat_10809_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_defeat_10809_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Kwestia głosowa [battle_defeat_10809_1] (Defeat Wail)] 료슈님께 또 한소리 듣겠네요. 어쩔 수 없죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Butler_10809.json :: dataList[id=battle_defeat_10809_1].dlg
   limit: do 120 znaków
   EN: Guess I'm due for another scolding from Lady Ryōshū. Well, what can I do?
   PL:

## [000] Zwei Assoc. West Section 3 — Ishmael — 서부 츠바이 협회 3과
- ID Tożsamości: `10810` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 93 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

701. [Karta Tożsamości — tytuł] 서부 츠바이 협회\n3과
   źródło: Personalities.json :: dataList[id=10810].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nWest Section 3
   PL:
702. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10810].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10810].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Karta Tożsamości — opis] 이스마엘의 열번째 인격
   źródło: Personalities.json :: dataList[id=10810].desc
   limit: do 120 znaków
   EN: Ishmael's 10th Identity
   PL:
705. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 츠바이 기사단 대검술
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].name ; dataList[id=1081001].levelList[level=2].name ; dataList[id=1081001].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 50 znaków
   EN: Zwei Knight's Greatsword Form
   PL:
706. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 2 증가\n[WhenUse] 자신의 [Vibration] 횟수 4 당, [DefenseUp] 1 얻음 (최대 2)
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 4 [Vibration] Count on self (max 2)
   PL:
707. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
708. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 1을 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 1 [DefenseUp] next turn
   PL:
709. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 1을 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 708 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] <style="highlight">3</style> 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">3</style> 당, [DefenseUp] 1 얻음 (최대 2)\n<style="highlight">[WhenUse] 자신의 [DefenseUp] 4 이상이면, 기본 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +<style="highlight">3</style> [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every <style="highlight">3</style> [Vibration] Count on self (max 2)\n<style="highlight">[WhenUse] At 4+ [DefenseUp], Base Power +1</style>
   PL:
712. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] <style="highlight">2</style>를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [DefenseUp] next turn
   PL:
713. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] <style="highlight">2</style>를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">2</style> 당 [DefenseUp] 1 얻음 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [DefenseUp] <style="highlight">4 당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every <style="highlight">2</style> [Vibration] Count on self (max <style="highlight">3</style>)\n[WhenUse] <style="highlight">Base Power +1 for every 4 [DefenseUp] (max 2)</style>
   PL:
715. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn<style="highlight"></style>
   PL:
716. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 못 지나갑니다.
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].name ; dataList[id=1081002].levelList[level=2].name ; dataList[id=1081002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Can't Let You Through.
   PL:
718. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 3)\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 3)\n[WinDuel] Gain +3 [Vibration] Count
   PL:
719. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
720. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 3을 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081002].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 3 [DefenseUp] next turn
   PL:
721. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (자신의 [Vibration] 횟수/2)만큼 [Vibration] 부여 (최대 2)
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] equal to (([Vibration] Count on self)/2) (max 2)
   PL:
722. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [DefenseUp]가 10 이상이면 대상에게 [Reduction] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1081002].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] At 10+ [DefenseUp], inflict 1 [Reduction]
   PL:
723. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">4</style>)\n<style="highlight">[WhenUse] 자신의 [DefenseUp]가 5 이상이면, 코인 위력 +1</style>\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">4</style>)\n<style="highlight">[WhenUse] At 5+ [DefenseUp], Coin Power +1</style>\n[WinDuel] Gain +3 [Vibration] Count
   PL:
724. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL:
725. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (자신의 [Vibration] 횟수/2)만큼 [Vibration] 부여 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] equal to (([Vibration] Count on self)/2) (max <style="highlight">3</style>)
   PL:
726. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] <style="highlight">5</style> 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">5</style>)\n[WhenUse] 자신의 [DefenseUp] <style="highlight">4</style> 이상이면, 코인 위력 +1\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +<style="highlight">5</style> [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">5</style>)\n[WhenUse] At <style="highlight">4</style>+ [DefenseUp], Coin Power +1\n[WinDuel] Gain +3 [Vibration] Count
   PL:
727. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Vibration]
   PL:
728. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] <style="highlight">4</style>를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain <style="highlight">4</style> [DefenseUp] next turn
   PL:
729. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (자신의 [Vibration] 횟수/2)만큼 [Vibration] 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] equal to (([Vibration] Count on self)/2) (max <style="highlight">4</style>)
   PL:
730. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [DefenseUp]가 <style="highlight">8</style> 이상이면 대상에게 [Reduction] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] At <style="highlight">8</style>+ [DefenseUp], inflict 1 [Reduction]
   PL:
731. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 수호
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].name ; dataList[id=1081003].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Ward
   PL:
732. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 3)\n[WhenUse] 자신에게 [DefensiveStance]가 있으면, 피해량 +50%\n[WhenUse] 자신의 [DefenseUp] 4 당 코인 위력 +1 (최대 2)\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 8 증가\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [DefenseUp], [DefensiveStance], [Aggro], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefensiveStance] = 방어 태세 / Defensive Stance; [Aggro] = 도발치 / Aggro; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 3)\n[WhenUse] If this unit is in [DefensiveStance], deal +50% damage\n[WhenUse] Coin Power +1 for every 4 [DefenseUp] on self (max 2)\n[WhenUse] Gain +8 [Aggro] to this Skill Slot next turn\n[WinDuel] Gain +3 [Vibration] Count
   PL:
733. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1081003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1081003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 전부 소모하여, 소모한 값만큼 [Vibration] 부여. (최대 10)\n- (초과한 [Vibration] x 1.5)%만큼 피해량이 증가 (최대 30%)
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume all [Vibration] Count on self, and inflict the value of the Count consumed as [Vibration] on target. (max 10)\n- Deal +(excess [Vibration] x 1.5)% damage (max 30%)
   PL:
736. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1081003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
737. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [DefensiveStance]면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1081003].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefensiveStance], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefensiveStance] = 방어 태세 / Defensive Stance; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit is in [DefensiveStance], trigger [VibrationExplosion]; then, reduce the target's [Vibration] Count by 1
   PL:
738. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">5</style>)\n[WhenUse] 자신에게 [DefensiveStance]가 있으면, 피해량 +<style="highlight">70</style>%\n[WhenUse] 자신의 [DefenseUp] 4 당 코인 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] <style="highlight">10</style> 증가\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [DefenseUp], [DefensiveStance], [Aggro], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefensiveStance] = 방어 태세 / Defensive Stance; [Aggro] = 도발치 / Aggro; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">5</style>)\n[WhenUse] If this unit is in [DefensiveStance], deal +<style="highlight">70</style>% damage\n[WhenUse] Coin Power +1 for every 4 [DefenseUp] on self (max <style="highlight">4</style>)\n[WhenUse] Gain +<style="highlight">10</style> [Aggro] to this Skill Slot next turn\n[WinDuel] Gain +3 [Vibration] Count
   PL:
739. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 전부 소모하여, 소모한 값만큼 [Vibration] 부여. (최대 <style="highlight">20</style>)\n- (초과한 [Vibration] x <style="highlight">5</style>)%만큼 피해량이 증가 (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume all [Vibration] Count on self, and inflict the value of the Count consumed as [Vibration] on target. (max <style="highlight">20</style>)\n- Deal +(excess [Vibration] x <style="highlight">5</style>)% damage (max <style="highlight">50</style>%)
   PL:
740. [Obrona (ulepszenia 1,4) — nazwa] 당신의 방패
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=1].name ; dataList[id=1081004].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Your Shield
   PL:
741. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [DefensiveStance] 2 얻음. (턴 당 1회)\n[WhenUse] 자신의 [Vibration] 횟수 10 증가 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [DefensiveStance], [WhenUse], [Vibration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [DefensiveStance] = 방어 태세 / Defensive Stance; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [CanDuelGuard]\n[StartBattle] Gain 2 [DefensiveStance]. (once per turn)\n[WhenUse] Gain +10 [Vibration] Count (once per turn)
   PL:
742. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081004].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
743. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] [DefensiveStance] 2 얻음. (턴 당 1회)\n[WhenUse] 자신의 [Vibration] 횟수 10 증가 (턴 당 1회)\n<style="highlight">[WinDuel] [VibrationExplosion]</style>
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [DefensiveStance], [WhenUse], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [DefensiveStance] = 방어 태세 / Defensive Stance; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [CanDuelGuard]\n[StartBattle] Gain 2 [DefensiveStance]. (once per turn)\n[WhenUse] Gain +10 [Vibration] Count (once per turn)\n<style="highlight">[WinDuel] Trigger [VibrationExplosion]</style>
   PL:
744. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 충격상쇄 그레이트소드
   źródło: Passives.json :: dataList[id=1081001].name
   limit: do 40 znaków
   EN: Shock-nullifying Greatsword
   PL:
745. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 전투 시작 시, 자신의 [Vibration] 횟수만큼 [DefenseUp]를 얻음 (최대 5)
   źródło: Passives.json :: dataList[id=1081001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration], [DefenseUp]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At Combat Start, gain [DefenseUp] equal to [Vibration] Count on self (max 5)
   PL:
746. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — nazwa] 충격상쇄 그레이트소드
   źródło: Passives.json :: dataList[id=1081011].name
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — opis] 전투 시작 시, 자신의 [Vibration] 횟수만큼 [DefenseUp]를 얻음 (최대 5)\n-[DefensiveStance]가 있으면 위 효과로 얻는 [DefenseUp]가 2배가 됨.
   źródło: Passives.json :: dataList[id=1081011].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [DefenseUp], [DefensiveStance]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefensiveStance] = 방어 태세 / Defensive Stance
   EN: At Combat Start, gain [DefenseUp] equal to [Vibration] Count on self (max 5)\n- If this unit is in [DefensiveStance], double the amount of [DefenseUp] gained from the above effect.
   PL:
748. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 긴급수호
   źródło: Passives.json :: dataList[id=1081021].name
   limit: do 40 znaków
   EN: Emergency Protection
   PL:
749. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 전투 시작 시 체력이 감소하여 이전 턴 시작과 체력 비율이 가장 차이가 많이 나는 인격에게 [DefenseUp] 2 부여
   źródło: Passives.json :: dataList[id=1081021].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At Combat Start, compare each Identity's current HP to their HP at the start of the previous turn. Then, apply 2 [DefenseUp] to the Identity that has the greatest disparity of HP values between turns.
   PL:
750. [Kwestia głosowa [get_10810_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=get_10810_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Kwestia głosowa [get_10810_1] (Identity Acquisition)] 떠들지 말고 줄 똑바로 맞춰 서세요. 아침 조회부터 한소리 듣는 건 질색이라서요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=get_10810_1].dlg
   limit: do 140 znaków
   EN: Zip it and get in line. I'd prefer it if we didn't have to sit through a scolding in the morning assembly.
   PL:
752. [Kwestia głosowa [lobby_morning_10810_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=lobby_morning_10810_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Kwestia głosowa [lobby_morning_10810_1] (Morning Greeting)] …아침 구보는 왜 선택 사항이 아닐까요?\n뛰는 건 상관 없지만, 그… 단체로 거리를 뛰는 건 좀 그렇더라고요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=lobby_morning_10810_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... Why aren't morning jogs optional?\nI don't mind the running, but... I don't like running in a group. Especially through the streets...
   PL:
754. [Kwestia głosowa [lobby_noon_10810_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=lobby_noon_10810_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Kwestia głosowa [lobby_noon_10810_1] (Afternoon Greeting)] 점심시간에 대검을 테이블이나 의자처럼 쓰는 거 꽤 괜찮은 아이디어 같지 않나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=lobby_noon_10810_1].dlg
   limit: do 130 znaków
   EN: Maybe we can use these greatswords as tables or chairs during lunch break. How's that for an idea?
   PL:
756. [Kwestia głosowa [lobby_night_10810_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=lobby_night_10810_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Kwestia głosowa [lobby_night_10810_1] (Evening Greeting)] 밤에도 지정 구역을 순찰하고는 있지만, 그래도 조심하세요.\n방패의 그늘도 밤에는 희미해지거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=lobby_night_10810_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Of course, we're always keeping up our patrols in each of our designated zones even during nighttime... but you should still be careful.\nEven the shield's shadow grows dim under the moonlight.
   PL:
758. [Kwestia głosowa [smalltalk_10810_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Kwestia głosowa [smalltalk_10810_1] (Chatter #1)] 세상에… 대검에 갑옷까지 입고 있으면 느릴 거라는 구시대적인 발상을 하는 사람이 아직도 있을 줄이야.\n이거, 생각보다 가벼워요. 공방에서 만든 장비인데 당연하지 않겠어요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wow... Do you seriously think this greatsword and a full suit of armor are heavy, unwieldy, and clunky? You know that misconception was debunked forever ago, right?\nThese things are lighter than they look. They're workshop-made, so it should be obvious.
   PL:
760. [Kwestia głosowa [smalltalk_10810_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Kwestia głosowa [smalltalk_10810_2] (Chatter #2)] 기사도라니… 그런 건 사고나 치고 돌아다니는 편력기사들에게 찾는 게 빠를 걸요.\n저희는 츠바이 협회 소속의 방패지, 동화 속의 기사님이 아니거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_2].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Chivalry, really...? Take that to one of those Knight-errant troublemakers.\nWe're just shields working for the Zwei Association, not noble knights from your fairy tales.
   PL:
762. [Kwestia głosowa [smalltalk_10810_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Kwestia głosowa [smalltalk_10810_3] (Chatter #3)] 고래잡이에 미쳐있던 배 위보다는 보람차고… 날개보다는 덜 지루하지만… 언제까지 여기 있을 수는 없겠죠.\n지키는 걸 천직으로 여기고 살기엔… 반드시 복수해야 할 사람이 한 명이 있어서요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_3].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is more fulfilling than that insanity that was Whaling, and more exciting than working for a Wing, but... I don't think I'll be here forever.\nI can't stand the irony of making my living by protecting people... when I live to get my revenge on that bastard.
   PL:
764. [Kwestia głosowa [smalltalk_10810_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Kwestia głosowa [smalltalk_10810_4] (Post-Uptie Chat 1)] 의뢰인 주변에 자연스레 녹아들어서 경호하는 건… 남부 협회가 잘하는 일이죠.\n저희는 이렇게 대검을 들고… 올테면 와보시지… 같은 느낌으로 옆에 서있는 게 전문이거든요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_4].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Low-key protection job, pretending like they're not even there... now that's how the southern branch does it. Our job is to stand imposingly next to our clients with these huge swords and intimidate any assailants before they even dare to attack.
   PL:
766. [Kwestia głosowa [smalltalk_10810_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Kwestia głosowa [smalltalk_10810_5] (Post-Uptie Chat 2)] 서부에서 스스로를 기사단이라고 자칭하는 사람들을 너무 믿지 마세요. M사의 월면기사단처럼 날개 소속이면 모를까, 보통은 해결사 사무소랑 크게 다르지 않거든요.\n괜한 로망을 가지고 접근했다가 피 보지 마시고… 보호의뢰는 받은 만큼 확실한 저희 츠바이에 의뢰하시죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=smalltalk_10810_5].dlg
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don't put too much faith in those 'Knight Orders' of the west unless they're part of a Wing like M Corp.'s Order of the Lunar Visage. Otherwise, they're no different from your usual Fixer Offices, so don't get your hopes up.\nIf you want a proper protection job, always hire experts like the Zwei and stay away from those amateurs.
   PL:
768. [Kwestia głosowa [gacksung_10810_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=gacksung_10810_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Kwestia głosowa [gacksung_10810_1] (Uptying)] 안심하세요. 제 뒤에 있는 한, 당신에게 화살 하나 닿지 못할 테니까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=gacksung_10810_1].dlg
   limit: do 140 znaków
   EN: Don't worry. Not even a single arrow will get through as long as I stand between you and your enemies.
   PL:
770. [Kwestia głosowa [neglect_10810_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=neglect_10810_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Kwestia głosowa [neglect_10810_1] (Idle)] 슬금슬금 어딜 가시는 건데요. 조회 빼먹으려는 거 아니죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=neglect_10810_1].dlg
   limit: do 120 znaków
   EN: Hey, where are you slinking off to? Not thinking of skipping the morning assembly, are you?
   PL:
772. [Kwestia głosowa [formation_10810_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=formation_10810_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Kwestia głosowa [formation_10810_1] (Deployment)] 지정 보호 구역에 소요 사태 확인.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=formation_10810_1].dlg
   limit: do 120 znaków
   EN: Disruption in the territory protection zone confirmed.
   PL:
774. [Kwestia głosowa [battleentry_10810_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battleentry_10810_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Kwestia głosowa [battleentry_10810_1] (Stage Entry)] 목표 위치로 돌격 중.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battleentry_10810_1].dlg
   limit: do 120 znaków
   EN: Advancing to the target location.
   PL:
776. [Kwestia głosowa [battle_select_10810_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_select_10810_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Kwestia głosowa [battle_select_10810_1] (Viewed in Battle)] 전투중이니까, 짧게 부탁드리죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_select_10810_1].dlg
   limit: do 120 znaków
   EN: We're mid-battle. Keep it short.
   PL:
778. [Kwestia głosowa [battle_endcommand_10810_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_endcommand_10810_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Kwestia głosowa [battle_endcommand_10810_1] (Commencing Attack)] 위험 인물 발견. 제압할게요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_endcommand_10810_1].dlg
   limit: do 120 znaków
   EN: Potentially dangerous individual identified. Moving in to suppress.
   PL:
780. [Kwestia głosowa [battle_enemy_break_10810_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_enemy_break_10810_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Kwestia głosowa [battle_enemy_break_10810_1] (Enemy Stagger)] 츠바이에 의뢰했다면…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_enemy_break_10810_1].dlg
   limit: do 120 znaków
   EN: Should've contracted the Zwei...
   PL:
782. [Kwestia głosowa [battle_break_10810_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_break_10810_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Kwestia głosowa [battle_break_10810_1] (Staggered)] 어, 어어…?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_break_10810_1].dlg
   limit: do 120 znaków
   EN: Wh— huh...?
   PL:
784. [Kwestia głosowa [battle_kill_10810_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_kill_10810_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Kwestia głosowa [battle_kill_10810_1] (Enemy Killed)] …대검에 머리가 쪼개지진 않았을텐데.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_kill_10810_1].dlg
   limit: do 120 znaków
   EN: ... or your head wouldn't have been crushed by my greatsword.
   PL:
786. [Kwestia głosowa [battle_dead_10810_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_dead_10810_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Kwestia głosowa [battle_dead_10810_1] (Death)] 당했네요… 빨리 지원 요청을…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_dead_10810_1].dlg
   limit: do 120 znaków
   EN: Dammit, they got us... We need to call for reinforcements...
   PL:
788. [Kwestia głosowa [choice_success_p_10810_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=choice_success_p_10810_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Kwestia głosowa [choice_success_p_10810_2] (Check Passed)] 흠흠. 의뢰비 인상에 대해서 대화를 나눠볼 만한 성과 아닌가요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=choice_success_p_10810_2].dlg
   limit: do 120 znaków
   EN: Ahem, ahem. I'd say our performance might just warrant a bonus for going above and beyond.
   PL:
790. [Kwestia głosowa [choice_fail_n_10810_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=choice_fail_n_10810_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Kwestia głosowa [choice_fail_n_10810_1] (Check Failed)] 제가 지켜야 할 대상은 아니었잖아요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=choice_fail_n_10810_1].dlg
   limit: do 120 znaków
   EN: Not my client anyway.
   PL:
792. [Kwestia głosowa [battle_clear_10810_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_clear_10810_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Kwestia głosowa [battle_clear_10810_1] (Victory Cry)] 주변 피해가 조금 있었네요. 이것도 다 실적에서 차감되겠지만… 그래도 사람은 지켰으니 다행이죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_clear_10810_1].dlg
   limit: do 180 znaków
   EN: We had some collateral damage... I guess it'll get deducted from the performance review. Hey, at least we managed to protect our client.
   PL:
794. [Kwestia głosowa [battle_clear_ex_10810_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_clear_ex_10810_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Kwestia głosowa [battle_clear_ex_10810_1] (Extra Conditions Fulfilled)] 인명 피해 없음. 기물 피해 경미… 완벽한데요? 소문이 퍼지면… 당분간 귀하신 분들의 영지 보호 의뢰가 끊이질 않겠어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_clear_ex_10810_1].dlg
   limit: do 250 znaków
   EN: No casualties, minimum collateral damage... that was perfect. Hey, if this story gets out, who knows? Maybe some important folks of the City might be hiring us for those dominion protection jobs.
   PL:
796. [Kwestia głosowa [battle_defeat_10810_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_defeat_10810_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Kwestia głosowa [battle_defeat_10810_1] (Defeat Wail)] 지역 보호 실패… 하아… 제 실수 때문에 츠바이의 명예가 땅에 떨어지겠네요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Zwei_10810.json :: dataList[id=battle_defeat_10810_1].dlg
   limit: do 130 znaków
   EN: Territory protection failed... Haah... looks like I'll be leaving a mark on the honor of the Zwei.
   PL:

## [000] Kurokumo Clan Captain — Ishmael — 흑운회 부조장
- ID Tożsamości: `10811` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 93 · szybkość: 3–4 / 3–5 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

798. [Karta Tożsamości — tytuł] 흑운회\n부조장
   źródło: Personalities.json :: dataList[id=10811].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nCaptain
   PL:
799. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10811].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10811].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Karta Tożsamości — opis] 이스마엘의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10811].desc
   limit: do 120 znaków
   EN: Ishmael's 11th Identity
   PL:
802. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 뒷처리
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].name ; dataList[id=1081101].levelList[level=2].name ; dataList[id=1081101].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Clean Up
   PL:
803. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
804. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
805. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]
   PL:
806. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>
   PL:
807. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL:
808. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL:
809. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1081101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]<style="highlight"></style>
   PL:
810. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 30%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\nDeal +10% damage for every type of negative effect on target (max 30%)</style>
   PL:
811. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 날카로운 칼날
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].name ; dataList[id=1081102].levelList[level=2].name ; dataList[id=1081102].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Sharpened Blade
   PL:
812. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] 자신을 제외하고 속도가 가장 빠른 아군 흑운회 소속 인격 2명에게 [AttackDmgUp] 1 부여 (턴 당 1회)\n- 자신 포함 흑운회 소속이 6명 이상이면 대신 5명에게 [AttackDmgUp] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] On 2 other allied Kurokumo Clan Identities with the fastest Speed: apply 1 [AttackDmgUp] (once per turn)\n- If there are 6+ Kurokumo Clan allies, including this unit, apply 2 [AttackDmgUp] to 5 allies instead
   PL:
813. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 804 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
815. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[StartBattle] 자신을 제외하고 속도가 가장 빠른 아군 흑운회 소속 인격 2명에게 [AttackDmgUp] <style="highlight">2</style> 부여 (턴 당 1회)\n- 자신 포함 흑운회 소속이 6명 이상이면 대신 5명에게 [AttackDmgUp] <style="highlight">3</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [AttackDmgUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[StartBattle] On 2 other allied Kurokumo Clan Identities with the fastest Speed: apply <style="highlight">2</style> [AttackDmgUp] (once per turn)\n- If there are 6+ Kurokumo Clan units, including this unit, apply <style="highlight">3</style> [AttackDmgUp] to 5 allies instead
   PL:
816. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 808 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp] (once per turn)</style>
   PL:
818. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL:
819. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [SlashResultUp] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: <style="highlight">[OnSucceedAttack] Gain 1 [SlashResultUp] next turn (once per turn)</style>
   PL:
820. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 50%)</style>\n[StartBattle] 자신을 제외하고 속도가 가장 빠른 아군 흑운회 소속 인격 2명에게 [AttackDmgUp] 2 부여 (턴 당 1회)\n- 자신 포함 흑운회 소속이 6명 이상이면 대신 5명에게 [AttackDmgUp] 4 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [AttackDmgUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\nDeal +10% damage for every type of negative effect on target (max 50%)</style>\n[StartBattle] On 2 other allied Kurokumo Clan Identities with the fastest Speed: apply 2 [AttackDmgUp] (once per turn)\n- If there are 6+ Kurokumo Clan units, including this unit, apply 4 [AttackDmgUp] to 5 allies instead
   PL:
821. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp] (once per turn)<style="highlight"></style>
   PL:
822. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">- 자신 포함 흑운회 소속이 6명 이상이면, 대신 [Vulnerable] 2 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: <style="highlight">- If there are 6+ Kurokumo Clan units, including this unit, inflict 2 [Vulnerable] instead</style>
   PL:
823. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashResultUp] 1 얻음 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: [OnSucceedAttack] Gain 1 [SlashResultUp] next turn (<style="highlight">2 times</style> per turn)
   PL:
824. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 먹칠
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].name ; dataList[id=1081103].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Ink Over
   PL:
825. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Coin Power +1
   PL:
826. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
828. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 3회 발동. 대상의 출혈 횟수 3 감소
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target 3 times; then, reduce their [Laceration] Count by 3
   PL:
829. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n[EnemyKill] 다음 턴에 [SlashResultUp] 2 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [EnemyKill], [SlashResultUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EnemyKill] = [적 처치 시] / [On Kill]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\n[EnemyKill] Gain 2 [SlashResultUp] next turn (once per turn)</style>
   PL:
830. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]<style="highlight"></style>
   PL:
832. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 100%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Deal +10% damage for every type of negative effect on target (max 100%)</style>
   PL:
833. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 3회 발동. 대상의 출혈 횟수 3 감소<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target 3 times; then, reduce their [Laceration] Count by 3<style="highlight"></style>
   PL:
834. [Obrona (ulepszenia 1,4) — nazwa] 흩어지는 검격
   źródło: Skills_personality-08.json :: dataList[id=1081104].levelList[level=1].name ; dataList[id=1081104].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Scattering Slash
   PL:
835. [Obrona (ulepszenie 1) — opis] [StartBattle] [Protection] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] Gain 1 [Protection] (once per turn)
   PL:
836. [Obrona (ulepszenie 4) — opis] [StartBattle] [Protection] 1 얻음 (턴 당 1회)\n<style="highlight">[StartBattle] 자신을 포함하여 속도가 가장 빠른 아군 흑운회 소속 인격 (2 + 최대 공명 수)명에게 [Endurance] 2 부여 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081104].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Protection], [Endurance]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: [StartBattle] Gain 1 [Protection] (once per turn)\n<style="highlight">[StartBattle] On (2 + highest Reson.) allied Kurokumo Clan Identities, including this unit, with the fastest Speed: apply 2 [Endurance] (once per turn)</style>
   PL:
837. [Pasywka bojowa (od ulepszenia 1) — nazwa] 임전
   źródło: Passives.json :: dataList[id=1081102].name
   limit: do 40 znaków
   EN: Battle Ready
   PL:
838. [Pasywka bojowa (od ulepszenia 1) — opis] 흑운회 소속 아군이 사망하면, 이번 전투 동안 [SlashResultUp] 1 얻음\n\n흑운회 소속 아군이 3명 이상 사망하면 이번 전투 동안 [EngageToBattle]을 얻음
   źródło: Passives.json :: dataList[id=1081102].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [SlashResultUp], [EngageToBattle]
   znaczenie tagów: [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [EngageToBattle] = 임전 / Battle Ready
   EN: When a Kurokumo Clan ally dies, gain 1 [SlashResultUp] for this Encounter\n\nWhen 3 or more Kurokumo Clan allies are defeated, gain [EngageToBattle] for this Encounter
   PL:
839. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 몰려드는 검은 구름
   źródło: Passives.json :: dataList[id=1081101].name
   limit: do 40 znaków
   EN: Gathering Dark Clouds
   PL:
840. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 전투 시작시 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면, [BlackCloudBlade] 1 얻음\n\n전투 시작시 조작 패널에서 자신의 양 옆의 흑운회 소속 인격에게 [BlackCloud] 1 부여
   źródło: Passives.json :: dataList[id=1081101].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [BlackCloudBlade], [BlackCloud]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade; [BlackCloud] = 검은 구름 / Dark Cloud
   EN: Combat Start: if there are 2+ allied Kurokumo Clan Identities in this Encounter, including this unit, gain 1 [BlackCloudBlade]\n\nCombat Start: apply 1 [BlackCloud] to Kurokumo Clan Identities adjacent to this unit on the Dashboard
   PL:
841. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 아군 흑운회 소속 인격에게 [BlackCloud] 부여
   źródło: Passives.json :: dataList[id=1081101].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BlackCloudBlade], [BlackCloud]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade; [BlackCloud] = 검은 구름 / Dark Cloud
   EN: Gain [BlackCloudBlade]; apply [BlackCloud] to allied Kurokumo Clan Identities
   PL:
842. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — nazwa] 몰려드는 검은 구름
   źródło: Passives.json :: dataList[id=1081111].name
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — opis] 전투 시작시 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면, [BlackCloudBlade] 1 얻음\n\n전투 시작시 조작 패널에서 자신의 양 옆의 흑운회 소속 인격에게 [BlackCloud] 1 부여\n<style="highlight">- 색욕 공명이 4 이상이면, 자신을 제외한 모든 흑운회 소속 아군에게 [BlackCloud] 1 부여</style>
   źródło: Passives.json :: dataList[id=1081111].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlackCloudBlade], [BlackCloud]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade; [BlackCloud] = 검은 구름 / Dark Cloud
   EN: Combat Start: if there are 2+ allied Kurokumo Clan Identities in this Encounter, including this unit, gain 1 [BlackCloudBlade]\n\nCombat Start: apply 1 [BlackCloud] to Kurokumo Clan Identities adjacent to this unit on the Dashboard\n<style="highlight">- At 4+ Lust Reson., apply 1 [BlackCloud] to all other Kurokumo Clan allies</style>
   PL:
844. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 아군 흑운회 소속 인격에게 [BlackCloud] 부여
   źródło: Passives.json :: dataList[id=1081111].summary
   (powtórzenie elementu 841 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 구름 공방 칼날
   źródło: Passives.json :: dataList[id=1081121].name
   limit: do 40 znaków
   EN: Cloud Workshop Blade
   PL:
846. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 속도가 가장 빠른 아군 1명이 적에게 스킬 효과, 코인 효과로 부여하는 [Laceration] 위력 또는 횟수 부여 값 +1
   źródło: Passives.json :: dataList[id=1081121].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally with the fastest Speed inflicts +1 more [Laceration] Potency or Count with Skill and Coin effects against enemies
   PL:
847. [Kwestia głosowa [get_10811_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=get_10811_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Kwestia głosowa [get_10811_1] (Identity Acquisition)] 용무가 있다면 조금 이따 오시지요.\n칼날을 정돈하는 시간을 방해받고 싶진 않으니.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=get_10811_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I would like to ask you to save business until later. I'd like to clean my blade in peace.
   PL:
849. [Kwestia głosowa [lobby_morning_10811_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=lobby_morning_10811_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Kwestia głosowa [lobby_morning_10811_1] (Morning Greeting)] 좋은 아침이네요. 오늘은 조직 회의도 있고, 엄지에게 상납 일정도 잡혀 있어서 바쁜 오전이 되겠지만…\n하, 급하게 앉은 자리라 그런가, 혼자서 일정까지 정하고 있으려니 머리가 지끈지끈하네요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=lobby_morning_10811_1].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Good morning. A bit busy, though... Today, we have the Syndicate gathering to attend and payments to make for the Thumb.\nHaah, my head's starting to hurt, having to deal with scheduling on top of my other responsibilities. I guess this is what I get for getting shoved into this position last minute.
   PL:
851. [Kwestia głosowa [lobby_noon_10811_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=lobby_noon_10811_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Kwestia głosowa [lobby_noon_10811_1] (Afternoon Greeting)] 아… 이전 부조장께선 부하들과 제법 점심 식사를 즐기시긴 했죠. 저는 생각이 조금 달라서 그러진 않지만요.\n아래 애들하고 부대끼는 것도 지치는 일이라…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=lobby_noon_10811_1].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah... yeah, the former Captain used to enjoy having lunches with the underlings from time to time. I don't, because I don't really agree with that philosophy.\nIt's exhausting that I have to deal with them at all.
   PL:
853. [Kwestia głosowa [lobby_night_10811_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=lobby_night_10811_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Kwestia głosowa [lobby_night_10811_1] (Evening Greeting)] 밤까지 나와 있지 말고 일 없으면 빨리 들어가서… 아, 미안하군요. 아랫놈들인 줄 알았네요.\n가뜩이나 바쁜 마당에 밖에서 술 먹고 사고 치면 골치 아파서요…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=lobby_night_10811_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If you've got nothing better to do, quit loitering out here and get your ass—oh. Apologies, I thought you were one of my underlings.\nWhen they get drunk and make a mess, it can be a real headache to deal with. Especially when I'm already swamped with work...
   PL:
855. [Kwestia głosowa [smalltalk_10811_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Kwestia głosowa [smalltalk_10811_1] (Chatter #1)] 흑운도… 이렇게 일찍 받게 될 줄은 사실 몰랐는데 말이죠. 부조장께서 갑자기 도서관이라는 곳에 끌려들어 갔다는 소식 이후론… 돌아오질 않으셔서.\n뭐, 부조장 자리를 오래 비워서 좋을 건 없으니 조장께서 급하셨던 것도 당연한 것일지도.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_1].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kokuuntō... I didn't think I'd receive it so soon. The last we heard of our former Captain was that she got dragged into some Library or something, and... she's been gone ever since. So...\nWell, I guess the Patriarch also realized that the Captain's seat shouldn't remain vacant for too long. Makes sense he was so anxious to fill it quick.
   PL:
857. [Kwestia głosowa [smalltalk_10811_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Kwestia głosowa [smalltalk_10811_2] (Chatter #2)] 조장… 지금은 잘려버린 손목 대신 붙이신 의수 때문도 있고, 연로하신 이유도 있어서 그렇지, 원래는 '동부십검'에 들어가는 어마어마한 분이셨죠.\n유쾌하신 분이긴 하지만 진지하게 임할 때는… 바라만 봐도 온 몸이 얼어붙는 기분이…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_2].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our Patriarch, he's... well, he's old now and had to replace one of his wrists with a prosthetic, but he used to be someone, you know? One of the Ten Blades of the East.\nHe's a pretty jolly old guy, but when he gets serious... I can feel the chill running down my spine just from looking at him.
   PL:
859. [Kwestia głosowa [smalltalk_10811_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Kwestia głosowa [smalltalk_10811_3] (Chatter #3)] 하아아… 좀이 다 쑤시네. 큰 건이 아니면 밖에 나가서 칼 쓸 일도 많지 않고. 아래 애들이 잘하고 다니는지도 신경 쓰이고.\n…옛날이 좋았는데, 깝죽거리는 놈들 혓바닥을 잘라버릴 때…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_3].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haaah… this is the pits. I don’t even get to draw my blade often unless it’s for something important, and I always have to babysit my underlings.\nI miss the good old times, cutting off the tongues of bastards who thought they were hot shit…
   PL:
861. [Kwestia głosowa [smalltalk_10811_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Kwestia głosowa [smalltalk_10811_4] (Post-Uptie Chat 1)] 고작 이 정도 끄나풀이나 족치려고 저까지 불러들인 건 아니었으면 좋겠군요. 길바닥에서 걸린 시비도 아니고, 조직끼리 목숨을 걸고 '결전'을 외쳤다면…\n당연히 당신들 윗대가리 쌍판은 봐야겠죠?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_4].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please tell me you didn't involve me in this mess just to deal with these small fries. This is no street brawl, know what I mean? This is a Syndicate Showdown. So...\n... you should understand that I can't let this go without seeing your boss's mug.
   PL:
863. [Kwestia głosowa [smalltalk_10811_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Kwestia głosowa [smalltalk_10811_5] (Post-Uptie Chat 2)] 이게 뒷골목의 규칙인 거랍니다. 혓바닥으로 해결되는 일은 이곳의 규칙이 아니니까요. …생각해 보니 괘씸하네. 당신 팔 한 짝도 가져가죠.\n…아, 이전 부조장 말투가 또 옮았네.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=smalltalk_10811_5].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You should get familiar with the rules of the Backstreets. And the rules don't take kindly to people trying to sweet-talk their way out of trouble. ...It’s rather infuriating now that I think about it. I'll be taking your arm as well.\n... Oh, huh. I guess the former Captain's habits are rubbing off on me.
   PL:
865. [Kwestia głosowa [gacksung_10811_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=gacksung_10811_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Kwestia głosowa [gacksung_10811_1] (Uptying)] 흑운회 삼십사대 부조장 이스마엘. …당신의 결전 신청, 받아들이죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=gacksung_10811_1].dlg
   limit: do 140 znaków
   EN: My name is Ishmael, thirty-fourth Captain of the Kurokumo Clan... And I accept your Showdown challenge.
   PL:
867. [Kwestia głosowa [neglect_10811_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=neglect_10811_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Kwestia głosowa [neglect_10811_1] (Idle)] 거슬리게 굴지 말고, 할 말 있으면 빨리하시죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=neglect_10811_1].dlg
   limit: do 120 znaków
   EN: Stop hesitating and say it straight. You're starting to get on my nerves.
   PL:
869. [Kwestia głosowa [formation_10811_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=formation_10811_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Kwestia głosowa [formation_10811_1] (Deployment)] 내가, 움직여야 하나?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=formation_10811_1].dlg
   limit: do 120 znaków
   EN: You want <i>me</i> to make a move?
   PL:
871. [Kwestia głosowa [battleentry_10811_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battleentry_10811_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Kwestia głosowa [battleentry_10811_1] (Stage Entry)] 잘됐네.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battleentry_10811_1].dlg
   limit: do 120 znaków
   EN: Nice.
   PL:
873. [Kwestia głosowa [battle_select_10811_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_select_10811_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Kwestia głosowa [battle_select_10811_1] (Viewed in Battle)] 할 말이 남았나요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_select_10811_1].dlg
   limit: do 120 znaków
   EN: Anything left to say?
   PL:
875. [Kwestia głosowa [battle_endcommand_10811_1] — sytuacja] 공격시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_endcommand_10811_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
876. [Kwestia głosowa [battle_endcommand_10811_1] (Commencing Attack)] 갑니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_endcommand_10811_1].dlg
   limit: do 120 znaków
   EN: Here I go.
   PL:
877. [Kwestia głosowa [battle_enemy_break_10811_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_enemy_break_10811_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Kwestia głosowa [battle_enemy_break_10811_1] (Enemy Stagger)] 저런, 베인 줄도 몰랐나.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_enemy_break_10811_1].dlg
   limit: do 120 znaków
   EN: My, didn't you know? You've been cut.
   PL:
879. [Kwestia głosowa [battle_break_10811_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_break_10811_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Kwestia głosowa [battle_break_10811_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_break_10811_1].dlg
   limit: do 120 znaków
   EN: Ngh...
   PL:
881. [Kwestia głosowa [battle_kill_10811_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_kill_10811_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Kwestia głosowa [battle_kill_10811_1] (Enemy Killed)] 이 정도로 나와 검을 맞대…?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_kill_10811_1].dlg
   limit: do 120 znaków
   EN: How are you keeping up with me this well...?
   PL:
883. [Kwestia głosowa [battle_dead_10811_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_dead_10811_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Kwestia głosowa [battle_dead_10811_1] (Death)] …컥. 삼십사대는… 여기까지… 였나.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_dead_10811_1].dlg
   limit: do 120 znaków
   EN: ... Kuh. So this... is where the thirty-fourth Captain falls...
   PL:
885. [Kwestia głosowa [choice_success_p_10811_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=choice_success_p_10811_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Kwestia głosowa [choice_success_p_10811_2] (Check Passed)] 하. 시킬 사람이 없어서…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=choice_success_p_10811_2].dlg
   limit: do 120 znaków
   EN: Hah. Are you running short on people to do these chores?
   PL:
887. [Kwestia głosowa [choice_fail_n_10811_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=choice_fail_n_10811_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Kwestia głosowa [choice_fail_n_10811_1] (Check Failed)] …뒷처리는 애들 시켰어야지.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=choice_fail_n_10811_1].dlg
   limit: do 120 znaków
   EN: ... These cleanups are underlings' jobs anyway.
   PL:
889. [Kwestia głosowa [battle_clear_10811_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_clear_10811_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Kwestia głosowa [battle_clear_10811_1] (Victory Cry)] 이만 가죠. 히스클리프, 이 너저분한 것들은 치우고 돌아오세요. 위에 알려야 하니까 저기 나뒹구는 대가리 세 개 정돈 모아오고.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_clear_10811_1].dlg
   limit: do 190 znaków
   EN: Let's go, Heathcliff. Clean up this mess, will you? And cut off their heads—about three would do. We'll need something to report back, after all.
   PL:
891. [Kwestia głosowa [battle_clear_ex_10811_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_clear_ex_10811_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Kwestia głosowa [battle_clear_ex_10811_1] (Extra Conditions Fulfilled)] 싱겁네요… 윗대가리가 죽었으니, 이제 당신들도 우리 조직 밑에서 구르게 되겠죠. …식구 취급을 해주진 않으니, 알아서 기세요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_clear_ex_10811_1].dlg
   limit: do 220 znaków
   EN: That was disappointing... Now that your leader's dead, looks like our Syndicate will be absorbing yours. ... You won't be a part of our family, though, so know your place.
   PL:
893. [Kwestia głosowa [battle_defeat_10811_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_defeat_10811_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Kwestia głosowa [battle_defeat_10811_1] (Defeat Wail)] …이 되도 않는 싸움을 먼저 벌인 놈은 누구죠. 제. 가. 밖에서 사고치지 말라고… 했을 텐데…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Kurokumo_10811.json :: dataList[id=battle_defeat_10811_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... Be honest. Which one of you idiots started this ridiculous fight?\nI <i>clearly</i> remember asking all of you not to get into any trouble...
   PL:

## [000] Family Hierarch Candidate — Ishmael — 가주 후보
- ID Tożsamości: `10812` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 70 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Rupture, Poise

895. [Karta Tożsamości — tytuł] 가주 후보
   źródło: Personalities.json :: dataList[id=10812].title
   limit: do 40 znaków
   EN: Family Hierarch Candidate
   PL:
896. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10812].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10812].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Karta Tożsamości — opis] 이스마엘의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10812].desc
   limit: do 120 znaków
   EN: Ishmael's 12th Identity
   PL:
899. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 적격
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].name ; dataList[id=1081201].levelList[level=2].name ; dataList[id=1081201].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Crimson Strike
   PL:
900. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n[WinDuel] [Breath] 1 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n[WinDuel] Gain 1 [Breath] and +1 [Breath] Count
   PL:
901. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
902. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
903. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1081201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [AttackUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalOnSucceedAttack] Gain 1 [AttackUp] next turn (once per turn)
   PL:
904. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n<style="highlight">[WhenUse] 대상의 [Burst] 3 이상이면, 코인 위력 +1</style>\n[WinDuel] [Breath] 2 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n<style="highlight">[WhenUse] If target has 3+ [Burst], Coin Power +1</style>\n[WinDuel] Gain 2 [Breath] and +1 [Breath] Count
   PL:
905. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Burst] <style="highlight">3당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] [Breath] <style="highlight">3</style> 얻음, 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n[WhenUse] <style="highlight">Coin Power +1 for every 3 [Burst] on target (max 2)</style>\n[WinDuel] Gain <style="highlight">3</style> [Breath] and +<style="highlight">2</style> [Breath] Count
   PL:
906. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [AttackUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalOnSucceedAttack] Gain 1 [AttackUp] next turn (<style="highlight">2 times</style> per turn)
   PL:
907. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 적봉
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].name ; dataList[id=1081202].levelList[level=2].name ; dataList[id=1081202].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 2 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Crimson Phoenix
   PL:
908. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].desc ; dataList[id=1081202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has 5+ types of negative effects, Coin Power +1
   PL:
909. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 901 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 901 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 [Breath] 얻음 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] equal to [Burst] on target (max 5)
   PL:
912. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 대상의 [Burst] 횟수만큼 [Breath] 횟수 증가 (최대 3)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1081202].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1081202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain [Breath] Count equal to [Burst] Count on target (max 3)
   PL:
913. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +(20 + 자신의 [Breath] + 대상의 [Burst])% (최대 50%)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(20 + [Breath] on self + [Burst] on target)% damage on Critical Hit (max 50%)
   PL:
914. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict 1 [DefenseDown] next turn
   PL:
915. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 914 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 2 — opis] [CriticalEnemyTargetKill] 다음 턴에 [AttackUp] 3 얻음 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=2].coinlist[#3].coindescs[#1].desc ; dataList[id=1081202].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKill], [AttackUp]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalEnemyTargetKill] Gain 3 [AttackUp] next turn (once per turn)
   PL:
917. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ types of negative effects, Coin Power +1\n<style="highlight">[WhenUse] If target has 4+ [Burst], Coin Power +1</style>
   PL:
918. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">2</style> [DefenseDown] next turn
   PL:
919. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 918 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 적춘
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].name ; dataList[id=1081203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 8 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Crimson Spring
   PL:
921. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeAttack] 메인 타겟의 부정적인 효과가 6개 이상이면 공격 가중치 +1\n[WhenUse] 메인 타겟의 부정적인 효과 3개당, 코인 위력+2 (최대 4)\n[WhenUse] 메인 타겟의 ([Burst] + [Burst] 횟수)의 합 7당, 코인 위력 +1 (최대 3)\n[WinDuel] [Breath] 4 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] If main target has 6+ types of negative effects, Atk Weight +1\n[WhenUse] Coin Power +2 for every 3 types of negative effect on the main target (max 4)\n[WhenUse] Coin Power +1 for every 7 ([Burst] + [Burst] Count) on the main target (max 3)\n[WinDuel] Gain 4 [Breath]
   PL:
922. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량 +(20 + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 40%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(20 + [Breath] on self + [Burst] on the main target)% damage (max 40%)
   PL:
924. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] 크리티컬 피해량 +(45 + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 65%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(45 + [Breath] on self + [Burst] on the main target)% damage on Critical Hit (max 65%)
   PL:
925. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] 자신의 [StartXichun]당 크리티컬 피해량 +5% (최대 30%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartXichun]
   znaczenie tagów: [StartXichun] = 시[始] / Launcher [始]
   EN: +5% Damage on Critical Hit for every [StartXichun] on self (max 30%)
   PL:
926. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL:
927. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 6 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain 2 [Breath] and +1 [Breath] Count
   PL:
928. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 7 — opis] [CriticalEnemyTargetKill] [Breath] 횟수 2 증가 (턴 당 3회)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKill], [Breath]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [Breath] = 호흡 / Poise
   EN: [CriticalEnemyTargetKill] Gain +2 [Breath] Count (3 times per turn)
   PL:
929. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeAttack] 메인 타겟의 부정적인 효과가 5개 이상이면, 공격 가중치 +1\n<style="highlight">[BeforeAttack] 자신의 [StartXichun]가 3 이상이면, 공격 가중치 +1</style>\n[WhenUse] 메인 타겟의 부정적인 효과 3개당, 코인 위력+2 (최대 <style="highlight">6</style>)\n[WhenUse] 메인 타겟의 ([Burst] + [Burst] 횟수)의 합 7당, 코인 위력 +1 (최대 <style="highlight">5</style>)\n[WinDuel] [Breath] 4 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [StartXichun], [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [StartXichun] = 시[始] / Launcher [始]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] If main target has 5+ types of negative effects, Atk Weight +1\n<style="highlight">[BeforeAttack] At 3+ [StartXichun], Atk Weight +1</style>\n[WhenUse] Coin Power +2 for every 3 types of negative effect on the main target (max <style="highlight">6</style>)\n[WhenUse] Coin Power +1 for every 7 ([Burst] + [Burst] Count) on the main target (max <style="highlight">5</style>)\n[WinDuel] Gain 4 [Breath]
   PL:
930. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 피해량 +(<style="highlight">50</style> + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 <style="highlight">75</style>%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(<style="highlight">50</style> + [Breath] on self + [Burst] on the main target)% damage (max <style="highlight">75</style>%)
   PL:
931. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] 크리티컬 피해량 +(<style="highlight">80</style> + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 <style="highlight">105</style>%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(<style="highlight">80</style> + [Breath] on self + [Burst] on the main target)% damage on Critical Hit (max <style="highlight">105</style>%)
   PL:
932. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] 자신의 [StartXichun]당 크리티컬 피해량 +5% (최대 30%)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [StartXichun]
   znaczenie tagów: [StartXichun] = 시[始] / Launcher [始]
   EN: +5% Damage on Critical Hit for every [StartXichun] on self (max 30%)<style="highlight"></style>
   PL:
933. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Burst] 5 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]<style="highlight"></style>
   PL:
934. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 6 — opis] <style="highlight">[CriticalOnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +1 [Burst] Count</style>
   PL:
935. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 7 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain 2 [Breath] and +1 [Breath] Count<style="highlight"></style>
   PL:
936. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 8 — opis] [CriticalEnemyTargetKill] [Breath] 횟수 2 증가 (턴 당 3회)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalEnemyTargetKill], [Breath]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [Breath] = 호흡 / Poise
   EN: [CriticalEnemyTargetKill] Gain +2 [Breath] Count (3 times per turn)<style="highlight"></style>
   PL:
937. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 적격 - 시[始]
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=1].name ; dataList[id=1081205].levelList[level=2].name ; dataList[id=1081205].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 2 · monety: 2 (+2)
   limit: do 50 znaków
   EN: Crimson Strike - Launcher [始]
   PL:
938. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 2 증가\n[BeforeAttack] 자신의 [WaitingXichun]를 전부 소모하여, (자신의 [WaitingXichun] X 2)만큼 가중치 증가 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Breath], [BeforeAttack], [WaitingXichun]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WaitingXichun] = 대[待] / Ready [待]
   EN: [CantDuel]\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count\n[BeforeAttack] Consume all [WaitingXichun] on self to gain +([WaitingXichun] on self x 2) Atk Weight (max 5)
   PL:
939. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081205].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
940. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [CantDuel]\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 2 증가\n<style="highlight">[WhenUse] 자신의 [WaitingXichun]가 3 이상이면, 코인 위력 +1</style>\n[BeforeAttack] 자신의 [WaitingXichun]를 전부 소모하여, (자신의 [WaitingXichun] X 2)만큼 가중치 증가 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [Breath], [WaitingXichun], [BeforeAttack]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WaitingXichun] = 대[待] / Ready [待]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantDuel]\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count\n<style="highlight">[WhenUse] At 3+ [WaitingXichun], Coin Power +1</style>\n[BeforeAttack] Consume all [WaitingXichun] on self to gain +([WaitingXichun] on self x 2) Atk Weight (max 5)
   PL:
941. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 2 증가\n[WhenUse] 자신의 [WaitingXichun]가 3 이상이면, 코인 위력 +<style="highlight">2</style>\n[BeforeAttack] 자신의 [WaitingXichun]를 전부 소모하여, (자신의 [WaitingXichun] X 2)만큼 가중치 증가 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [Breath], [WaitingXichun], [BeforeAttack]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WaitingXichun] = 대[待] / Ready [待]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantDuel]\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count\n[WhenUse] At 3+ [WaitingXichun], Coin Power +<style="highlight">2</style>\n[BeforeAttack] Consume all [WaitingXichun] on self to gain +([WaitingXichun] on self x 2) Atk Weight (max 5)
   PL:
942. [Obrona (ulepszenia 1,4) — nazwa] 수회
   źródło: Skills_personality-08.json :: dataList[id=1081204].levelList[level=1].name ; dataList[id=1081204].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Adept Evasion
   PL:
943. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신의 [StartXichun]가 3 이상이면, 턴 종료 시 [RetreatForCommon]함.\n- 퇴각 시 대기 순서 1번이 됨 (대기 인원의 대기 해제보다 우선적으로 복귀함)\n[OnSucceedEvade] [Breath] 2 얻음. (턴 당 최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1081204].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [StartXichun], [RetreatForCommon], [OnSucceedEvade], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [StartXichun] = 시[始] / Launcher [始]; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [StartBattle] At 3+ [StartXichun], perform a [RetreatForCommon] at Turn End.\n- Upon Retreat, move to the frontmost place in the Backup units' Deployment order (Returns first before the other Backup units Substitute in)\n[OnSucceedEvade] Gain 2 [Breath] (2 times per turn)
   PL:
944. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신의 [StartXichun]가 3 이상이면, 턴 종료 시 [RetreatForCommon]함.\n- 퇴각 시 대기 순서 1번이 됨 (대기 인원의 대기 해제보다 우선적으로 복귀함)\n<style="highlight">[WhenUse] [Breath] 횟수 1 증가 (턴 당 최대 2회)</style>\n[OnSucceedEvade] [Breath] 2 얻음. (턴 당 최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1081204].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [StartXichun], [RetreatForCommon], [WhenUse], [Breath], [OnSucceedEvade]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [StartXichun] = 시[始] / Launcher [始]; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [StartBattle] At 3+ [StartXichun], perform a [RetreatForCommon] at Turn End.\n- Upon Retreat, move to the frontmost place in the Backup units' Deployment order (Returns first before the other Backup units Substitute in)\n<style="highlight">[WhenUse] Gain +1 [Breath] Count (2 times per turn)</style>\n[OnSucceedEvade] Gain 2 [Breath] (2 times per turn)
   PL:
945. [Pasywka bojowa (od ulepszenia 1) — nazwa] 시동[始動]
   źródło: Passives.json :: dataList[id=1081202].name
   limit: do 40 znaków
   EN: Launching Maneuver [始動]
   PL:
946. [Pasywka bojowa (od ulepszenia 1) — opis] 전투에서 퇴각할 때, 아군에게 편성 순서 순으로 다음 턴에 공격 레벨 증가 1 부여\n- 부여 대상 수 : 자신의 [StartXichun] 수치\n- 부여 대상이 "가씨 가문"이면, 대신 다음 턴에 공격 레벨 증가 2 부여\n- 다음 턴에 복귀, 대기 해제되는 인격에게는 부여되지 않음\n\n대기 해제 또는 복귀로 등장한 턴에 자신이 [WaitingXichun]를 얻고, 전투 시작시 스킬 순서상 가장 먼저 '적격 - 시【始】'를 무작위 대상에게 사용함
   źródło: Passives.json :: dataList[id=1081202].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [StartXichun], [WaitingXichun]
   znaczenie tagów: [StartXichun] = 시[始] / Launcher [始]; [WaitingXichun] = 대[待] / Ready [待]
   EN: Upon Retreat: apply 1 Offense Level Up next turn to allies in their Deployment order\n- Number of affected allies = [StartXichun] Stack on self\n- If the affected ally is a "Jia Family" unit, apply 2 Offense Level Up next turn instead\n- Does not affect allies that either Return or Substitute next turn\n\nOn the turn this unit Substituted or Returned to the field, gain [WaitingXichun]; then, at Combat Start, as the very first Skill in the Skill order, use 'Crimson Strike - Launcher【始】' against a random target.
   PL:
947. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 대기 해제 혹은 복귀로 등장한 턴에 전투 시작시, 스킬 순서상 가장 먼저 "적격 - 시(始)"을 무작위 대상에게 사용함
   źródło: Passives.json :: dataList[id=1081202].summary
   limit: do 250 znaków
   EN: In the turn this unit entered the battle via Substitution or Return: at Combat Start, as the very first Skill in the Skill order, use 'Crimson Strike - Launcher (始)' against a random target
   PL:
948. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 파흡자환[破吸自桓]
   źródło: Passives.json :: dataList[id=1081201].name
   limit: do 50 znaków
   EN: Rupture-breathing Resolve [破吸自桓]
   PL:
949. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 자신의 공격 스킬로 대상 처치 시 대상의 [Burst]만큼 [Breath]을 얻음 (적 1명당 최대 3, 턴 당 최대 1회)\n- 위 효과로 [Breath]을 3까지 얻었다면, 대상의 [Burst] 횟수만큼 자신의 [Breath] 횟수 증가 (적 1명당 최대 2, 턴 당 최대 1회)\n\n합 진행 시 합을 진행하는 적보다 공격 레벨이 높으면, 합 위력 +1\n\n합 진행 시 합을 진행하는 적보다 공격 레벨이 높으면, 기본 공격 스킬로 부여하는 [Burst] 위력 또는 [Burst] 횟수 +1 (턴 당 2회 발동)
   źródło: Passives.json :: dataList[id=1081201].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: When killing the target with this unit's Attack Skills, gain [Breath] equal to [Burst] on target (3 per 1 enemy; once per turn)\n- If this unit gained 3 [Breath] with the above effect, gain [Breath] Count equal to [Burst] Count on target (2 per 1 enemy; once per turn)\n\nIn a Clash, if this unit's Offense Level is higher than the target's, Clash Power +1\n\nIn a Clash, if this unit's Offense Level is higher than the target's, inflict +1 more [Burst] Potency or [Burst] Count with this unit's Base Attack Skills (2 times per turn)
   PL:
950. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — podsumowanie] 합을 할 때, 공격 대상보다 공격 레벨이 높을 경우, 합 위력 +1\n기본 공격 스킬로 부여하는 [Burst] 위력 혹은 [Burst] 횟수 +1
   źródło: Passives.json :: dataList[id=1081201].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: In a Clash, if this unit's Offense Level is higher than the target's, Clash Power +1\nInflict +1 more [Burst] Potency and [Burst] Count with this unit's Base Attack Skills
   PL:
951. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — nazwa] 여환[餘桓]
   źródło: Passives.json :: dataList[id=1081221].name
   limit: do 40 znaków
   EN: Lingering Resolve [餘桓]
   PL:
952. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — opis] 전투 중 자신이 사망했으면, 자신 다음 턴에 대기해제 되는 인격(대기 편성 순서상 가장 빠른 인격)에게 전투 시작 시 [CheerUpXichun] 부여\n\n연속 전투에서 자신이 퇴각 혹은 대기 상태일 때, 아래의 효과 발동\n전투 시작 시 체력이 최대 체력의 50% 이하이고, 수비 스킬을 사용한 인격 중 편성 순서가 가장 빠른 인격이 턴 종료 시 피해로 인한 흐트러짐을 해제하고  [RetreatForCommon]함 (전투당 2회 발동)
   źródło: Passives.json :: dataList[id=1081221].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [CheerUpXichun], [RetreatForCommon]
   znaczenie tagów: [CheerUpXichun] = 원[援] / Assist [援]; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat
   EN: If this unit is defeated in an Encounter, apply [CheerUpXichun] to the subsequently Substituting Identity (the fastest Backup Unit in the Deployment Order) next turn\n\nIn Chain Battles, if this unit is a Backup unit or has Retreated, activate the following:\n- Combat Start: Among the Identities who 1) are at 50% HP or lower, and 2) used a Defense Skill, choose the Identity with the earliest Deployment order. At Turn End, that Identity recovers from Stagger due to damage and performs a [RetreatForCommon] (2 times per Encounter)
   PL:
953. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — podsumowanie] 전투 시작 시 체력이 50%이하이고 수비 스킬을 사용한 인격을 턴 종료 시, 퇴각 시킴
   źródło: Passives.json :: dataList[id=1081221].summary
   limit: do 150 znaków
   EN: Turn End: Retreat the Identity that, at Combat Start, has 50% or less HP and has used a Defense Skill this turn
   PL:
954. [Kwestia głosowa [get_10812_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=get_10812_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [Kwestia głosowa [get_10812_1] (Identity Acquisition)] 끝내 가을 버텨낼 꽃 없다더니, 어찌 된 일인지 홍원은 변한 게 하나도 없네요. 아, 길은 예전 같지 않으려나.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=get_10812_1].dlg
   limit: do 170 znaków
   EN: No flower ever endures the fall... or so they say. Hongyuan's certainly not changed one bit. Except for its roads, I suppose.
   PL:
956. [Kwestia głosowa [lobby_morning_10812_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=lobby_morning_10812_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Kwestia głosowa [lobby_morning_10812_1] (Morning Greeting)] 꽤 소란스러운 밤이었는데도, 햇빛 아래 멀쩡히 걸어 나오시다니… 운이 좋았나 보네요.\n하지만 조심하는 게 좋을걸요. 낮이 되었다고, 당신 목숨을 노리는 암수가 사라지는 건 아닐 테니.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=lobby_morning_10812_1].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: That was one crazy night... I'm almost surprised to see you in the sun this morning, unharmed. Must've gotten lucky.\nBut you better keep your guard up. Sunshine isn't much of a deterrent for assassins.
   PL:
958. [Kwestia głosowa [lobby_noon_10812_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=lobby_noon_10812_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Kwestia głosowa [lobby_noon_10812_1] (Afternoon Greeting)] 창고가 가득 차야 예절을 안다고, 식사에 돈을 아낄 필요는 없어요. 그런 푼돈보다 세가의 사기와 상태가 훨씬 중요하니까.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=lobby_noon_10812_1].dlg
   limit: do 210 znaków
   EN: Manners are learned when the storehouses are made abundant. Let's not waste any money on food, okay? The morale and health of my clan is more important than that.
   PL:
960. [Kwestia głosowa [lobby_night_10812_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=lobby_night_10812_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Kwestia głosowa [lobby_night_10812_1] (Evening Greeting)] 하아… 불빛 하나 없이 어두운 걸 보니, 오늘부터 발 뻗고 자긴 글렀네요. 야밤의 불청객이 몇이나 될런지.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=lobby_night_10812_1].dlg
   limit: do 200 znaków
   EN: Haah... pitch-black darkness, huh? We should probably say goodbye to proper sleep from here on out. Wonder how many uninvited 'guests' we'll get tonight.
   PL:
962. [Kwestia głosowa [smalltalk_10812_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Kwestia głosowa [smalltalk_10812_1] (Chatter #1)] 홍원의 가주 후보자, 가씨 가의 이스마엘. 단서를 찾아 홍원으로 돌아왔어요. 어… 뭔가 이상하지 않냐고요…?\n…이상할 게 뭐가 있어요. 저는 태어날 때부터 가씨 가문에서 살아왔으니, 가씨인게 당연하잖아요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_1].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I am Ishmael of the Jia family, candidate for the seat of Family Hierarch of Hongyuan. I have found my clue, and I have returned to Hongyuan. Uh... what... what do you mean, that's weird...?\n... Yeah, no. There isn't anything weird about that. Of course I'm a Jia, I was born and raised by the Jia family.
   PL:
964. [Kwestia głosowa [smalltalk_10812_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [Kwestia głosowa [smalltalk_10812_2] (Chatter #2)] 어중간한 결과물로는 눈에 들기 어렵겠지만, 레테의 강물이라면 분명 가모님도 주목하시겠죠.\n그 깊은 곳의 강에서 뭐라도 가져온 후보자는, 분명 제가 유일할 테니까요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_2].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: They won't even bat an eye at mediocre offerings, but... waters of river Lethe will be sure to get even the venerable Jia Mu's attention.\nPretty sure I'm the only candidate who's brought anything from a river in the deep place.
   PL:
966. [Kwestia głosowa [smalltalk_10812_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Kwestia głosowa [smalltalk_10812_3] (Chatter #3)] 가주가 되고 싶은 이유요? 그야 당연히… 음. 생각해 본 적… 없었네요. 어릴 적부터 집안 어른들이 바란 일이라서? 가씨 가문에서 태어나서?\n심사가 끝나기 전까진 찾고 싶네요. 가문과 상관없이 제가 정한, 가주가 되고 싶은 이유를.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_3].dlg
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: My motivation for wanting to become a Family Hierarch? Well that's... I... hm. I never gave it much thought, if I'm being honest. But it's what everyone and the family seniors want? Because I'm a Jia family child?\nWell, hopefully I'll find out by the time the Evaluation is over. My motivation, separate from that of the family.
   PL:
968. [Kwestia głosowa [smalltalk_10812_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Kwestia głosowa [smalltalk_10812_4] (Post-Uptie Chat 1)] 뒷골목에서 수상한 노랫소리가 들리는 걸 보니… 곧 돌아오시겠군요.\n그 불길한 걸음이 이쪽으로 향하지 않기를 바라지만… 후보자인 이상 언젠가 부딪힐 수밖에 없겠죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_4].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I've been hearing these strange songs from the Backstreets... I suppose it won't be long before he returns.\nI just hope I won't ever have to run into him, but... It's inevitable that we'd come to blows sooner or later.
   PL:
970. [Kwestia głosowa [smalltalk_10812_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [Kwestia głosowa [smalltalk_10812_5] (Post-Uptie Chat 2)] 가주 심사에서 흑수는 아주 강력한 패지만… 마땅한 뒷배경이 없는 처지라서요. 흑수의 재갈은 두 번밖에 못 쥐어봤어요.\n한 번은 ■■를 풀어주느라 재갈을 놓아줬고, 다른 한 번은… 후우… 다른 가문의 철부지 탓에 어이없게 잃었죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=smalltalk_10812_5].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heishou Packs will make for really, really powerful hands in the Family Hierarch Evaluation, but... I don't really have any sponsors, which means that I've only held their leash twice in my life.\nThe first time, I relinquished my leashes to free ■■ ■■■■. And the other time, well... I lost it thanks to some dumbass from a different family.
   PL:
972. [Kwestia głosowa [gacksung_10812_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=gacksung_10812_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [Kwestia głosowa [gacksung_10812_1] (Uptying)] 잔칫상에는 코빼기도 안 비치더니… 제 목 한 번 쳐보러 난향오(暖香坞)에 모이셨군요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=gacksung_10812_1].dlg
   limit: do 190 znaków
   EN: Didn't even have the courtesy of showing up to my banquet, but now you're here... at my Nuanxiangwu. Itching for a chance to cut off my head, huh?
   PL:
974. [Kwestia głosowa [neglect_10812_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=neglect_10812_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Kwestia głosowa [neglect_10812_1] (Idle)] …할 말이 있으면 어서 하세요. 답답하게 말없이 서있지 말고.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=neglect_10812_1].dlg
   limit: do 120 znaków
   EN: ... If you've got something to say, say it. Don't just stand there spacing out.
   PL:
976. [Kwestia głosowa [formation_10812_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=formation_10812_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Kwestia głosowa [formation_10812_1] (Deployment)] 음. 보는 눈은 있네요. 여기서 저만큼 유능한 인재는 흔치 않죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=formation_10812_1].dlg
   limit: do 120 znaków
   EN: Hm. Good eye. I'm a rare talent around here, you know?
   PL:
978. [Kwestia głosowa [battleentry_10812_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battleentry_10812_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Kwestia głosowa [battleentry_10812_1] (Stage Entry)] 후우… 준비한 대로만 하면…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battleentry_10812_1].dlg
   limit: do 120 znaków
   EN: Hooh... I just need to do exactly as I prepared...
   PL:
980. [Kwestia głosowa [battle_select_10812_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_select_10812_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Kwestia głosowa [battle_select_10812_1] (Viewed in Battle)] 불필요한 관심은 사양하죠. 저는 조용한 게 좋아서요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_select_10812_1].dlg
   limit: do 120 znaków
   EN: Please, I don't need any unnecessary fussing. I prefer the silence.
   PL:
982. [Kwestia głosowa [battle_endcommand_10812_1] — sytuacja] 공격시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_endcommand_10812_1].desc
   (powtórzenie elementu 875 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Kwestia głosowa [battle_endcommand_10812_1] (Commencing Attack)] 시간 끌 것 없이, 모조리 치워버리죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_endcommand_10812_1].dlg
   limit: do 120 znaków
   EN: Let's take them all out. No need to waste our time here.
   PL:
984. [Kwestia głosowa [battle_enemy_break_10812_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_enemy_break_10812_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Kwestia głosowa [battle_enemy_break_10812_1] (Enemy Stagger)] 흥. 허술하긴!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_enemy_break_10812_1].dlg
   limit: do 120 znaków
   EN: Hmph. You're open!
   PL:
986. [Kwestia głosowa [battle_break_10812_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_break_10812_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [Kwestia głosowa [battle_break_10812_1] (Staggered)] 큭! 무슨 술수를…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_break_10812_1].dlg
   limit: do 120 znaków
   EN: Agh! What the hell—
   PL:
988. [Kwestia głosowa [battle_kill_10812_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_kill_10812_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Kwestia głosowa [battle_kill_10812_1] (Enemy Killed)] 시도는 좋았어요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_kill_10812_1].dlg
   limit: do 120 znaków
   EN: Nice try.
   PL:
990. [Kwestia głosowa [battle_dead_10812_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_dead_10812_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [Kwestia głosowa [battle_dead_10812_1] (Death)] 봄 한 번… 짧기도 하지…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_dead_10812_1].dlg
   limit: do 120 znaków
   EN: What a... short-lived spring this is...
   PL:
992. [Kwestia głosowa [choice_success_p_10812_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=choice_success_p_10812_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Kwestia głosowa [choice_success_p_10812_2] (Check Passed)] 이런 것쯤이야, 주머니에서 물건 꺼내는 것보다 쉽죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=choice_success_p_10812_2].dlg
   limit: do 120 znaków
   EN: This is easier than pulling something from my pocket.
   PL:
994. [Kwestia głosowa [choice_fail_n_10812_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=choice_fail_n_10812_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Kwestia głosowa [choice_fail_n_10812_1] (Check Failed)] …잠시만요. 다시 해볼게요. 아니, 한 번만 다시 해본다니까요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=choice_fail_n_10812_1].dlg
   limit: do 120 znaków
   EN: ... Wait, let me try that again. Come on, I said let me try that again!
   PL:
996. [Kwestia głosowa [battle_clear_10812_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_clear_10812_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Kwestia głosowa [battle_clear_10812_1] (Victory Cry)] 고작 이 정도 승리에 기뻐할 생각이었다면, 가주 심사엔 참가하지도 않았겠죠.\n뭐… 기왕 이렇게 된 김에 조금만 더 도우시죠. 제가 가주가 된다면, 그 값은 몇 배로 치러드릴 테니.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_clear_10812_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I wouldn't have participated in the Family Hierarch Evaluation if I was someone who'd let this little victory get to my head.\nWell... why don't you help me out a little more? I'll double, triple, quintuple your rewards should I become the next Hierarch.
   PL:
998. [Kwestia głosowa [battle_clear_ex_10812_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_clear_ex_10812_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Kwestia głosowa [battle_clear_ex_10812_1] (Extra Conditions Fulfilled)] 허, 이렇게 쉽게 통과하리라곤 상상도 못 했는데… 세가들에게 은자를 풀어야겠어요. 이런 경사스러운 날에는 조금 풀어줘도 괜찮겠죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_clear_ex_10812_1].dlg
   limit: do 230 znaków
   EN: Huh, didn't think it'd be that easy. Guess I could afford to be a bit more generous with the bonuses for my clan today... Hey, this is what money's for. To celebrate good tidings.
   PL:
1000. [Kwestia głosowa [battle_defeat_10812_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_defeat_10812_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1001. [Kwestia głosowa [battle_defeat_10812_1] (Defeat Wail)] …손도 못 쓰고 당했다고…? 내… 세가가…? …후… 그, 아… 아니에요. 제 준비가… 부족했던 탓… 이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Xichun_10812.json :: dataList[id=battle_defeat_10812_1].dlg
   limit: do 210 znaków
   EN: ... My clan... destroyed...? They didn't... even stand a chance... Haah, it's... ngh, it's nothing. This is all my fault. I... should've been better prepared.
   PL:

## [000] Jeong's Office Rep — Ishmael — 정사무소 대표
- ID Tożsamości: `10813` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9107 · HP bazowe: 88 · szybkość: 2–6 / 2–6 / 3–7 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Sinking

1002. [Karta Tożsamości — tytuł] 정사무소\n대표
   źródło: Personalities.json :: dataList[id=10813].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Jeong's Office Rep
   PL:
1003. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10813].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10813].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Karta Tożsamości — opis] 이스마엘의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10813].desc
   limit: do 120 znaków
   EN: Ishmael's 13th Identity
   PL:
1006. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 츠루기리[鶴斬り]
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].name ; dataList[id=1081301].levelList[level=2].name ; dataList[id=1081301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Tsuru-giri [鶴斬り]
   PL:
1007. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Discard]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill
   PL:
1008. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL:
1009. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1010. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n<style="highlight">[WhenUse] If target has 6+ ([Vibration] + [Sinking]), Coin Power +1</style>
   PL:
1011. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count<style="highlight"></style>
   PL:
1012. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Sinking] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttackHead] Inflict +1 [Sinking] Count</style>
   PL:
1013. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL:
1014. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Vibration] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttackHead] Inflict +1 [Vibration] Count</style>
   PL:
1015. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Vibration] + [Sinking]) on target (max 2)</style>
   PL:
1016. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count<style="highlight"></style>
   PL:
1017. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL:
1018. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 억새 흘리기
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].name ; dataList[id=1081302].levelList[level=2].name ; dataList[id=1081302].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Susuki Misdirection
   PL:
1019. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].desc
   (powtórzenie elementu 1007 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1022. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].desc
   (powtórzenie elementu 1010 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL:
1024. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Sinking] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [Sinking]</style>
   PL:
1025. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL:
1026. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Vibration] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [Vibration]</style>
   PL:
1027. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].desc
   (powtórzenie elementu 1015 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]<style="highlight"></style>
   PL:
1029. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]<style="highlight"></style>
   PL:
1030. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 정신력 5 회복</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Heal 5 SP</style>
   PL:
1031. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 사쿠라센[桜閃]
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].name ; dataList[id=1081303].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Sakura-sen [桜閃]
   PL:
1032. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [HanafudaCombo] 위력 1당 피해량 +5%\n[WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n[WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [HanafudaCombo], [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: Deal +5% damage for every [HanafudaCombo] Potency on self\n[WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n[WhenUse] If target has 6+ ([Vibration] + [Sinking]), Coin Power +1
   PL:
1033. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
1034. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
1035. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL:
1036. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
1037. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
1038. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL:
1039. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [OnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]
   PL:
1040. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [HanafudaCombo] 위력 1당 피해량 <style="highlight">+10%</style>\n[WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 3)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HanafudaCombo], [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: Deal +<style="highlight">10</style>% damage for every [HanafudaCombo] Potency on self\n[WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Vibration] + [Sinking]), on target (max 3)</style>
   PL:
1041. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count<style="highlight"></style>
   PL:
1042. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL:
1043. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 1016 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL:
1045. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]<style="highlight"></style>
   PL:
1046. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 1017 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1047. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">대상이 [Switch_Vibration] 이나 [FusionVibration] 상태면, 이 코인 피해량 +48%</style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: <style="highlight"> If target is in either [Switch_Vibration] or [FusionVibration] states, this Coin deals +48% damage</style>
   PL:
1048. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [OnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]<style="highlight"></style>
   PL:
1049. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 코오쟌[光斬]
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].name ; dataList[id=1081305].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Kōzan [光斬]
   PL:
1050. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 미만이면, 스킬이 취소되고 다음 턴에 [Enhancement] 2 얻음\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 이상이면, 위력당 아래 효과 적용\n- 1당 이 스킬 피해량 +10%\n- 4 이상이면, 기본 위력 +1\n- 5면, 마지막 재사용 코인 적중시 [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 1 감소\n[EndSkillAll] 자신의 [HanafudaCombo] 소멸\n[EndSkillAll] 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회)\n[EndSkillAll] 사용하지 못한 코인 갯수만큼 다음 턴에 [HanafudaCombo] 위력 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [HanafudaCombo], [Enhancement], [VibrationExplosion], [Vibration], [EndSkillAll]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [HanafudaCombo] = 광【光】 / Bright【光】; [Enhancement] = 공격 위력 증가 / Attack Power Up; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n\n[WhenUse] At less than 3 [HanafudaCombo] Potency, cancel the Skill and gain 2 [Enhancement] next turn\n[WhenUse] At 3+ [HanafudaCombo] Potency, gain the following effects based on Potency:\n- Per 1 Potency: this Skill deals +10% damage\n- At 4+ Potency: Base Power +1\n- At 5 Potency: On Hit with the final Reuse Coin, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 1\n[EndSkillAll] Lose [HanafudaCombo] on self\n[EndSkillAll] Next turn, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills (once per turn)\n[EndSkillAll] Gain [HanafudaCombo] Potency next turn equal to the # of Coins that weren't used
   PL:
1051. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] 자신의 ([HanafudaCombo] 위력 - 1)만큼 이 코인 재사용 (최대 4회)
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [HanafudaCombo]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】
   EN: Reuse this Coin ([HanafudaCombo] Potency - 1) times (4 times max)
   PL:
1052. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1054. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 미만이면, 스킬이 취소되고 다음 턴에 [Enhancement] 2 얻음\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 이상이면, 위력당 아래 효과 적용\n- 1당 이 스킬 피해량 +10%\n- 4 이상이면, 기본 위력 +1\n- 5면, 마지막 재사용 코인 적중시 [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 1 감소\n[EndSkillAll] 자신의 [HanafudaCombo] 소멸\n[EndSkillAll] 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회)\n[EndSkillAll] 사용하지 못한 코인 갯수만큼 다음 턴에 [HanafudaCombo] 위력 얻음<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [HanafudaCombo], [Enhancement], [VibrationExplosion], [Vibration], [EndSkillAll]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [HanafudaCombo] = 광【光】 / Bright【光】; [Enhancement] = 공격 위력 증가 / Attack Power Up; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n\n[WhenUse] At less than 3 [HanafudaCombo] Potency, cancel the Skill and gain 2 [Enhancement] next turn\n[WhenUse] At 3+ [HanafudaCombo] Potency, gain the following effects based on Potency:\n- Per 1 Potency: this Skill deals +10% damage\n- At 4+ Potency: Base Power +1\n- At 5 Potency: On Hit with the final Reuse Coin, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 1\n[EndSkillAll] Lose [HanafudaCombo] on self\n[EndSkillAll] Next turn, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills (once per turn)\n[EndSkillAll] Gain [HanafudaCombo] Potency next turn equal to the # of Coins that weren't used<style="highlight"></style>
   PL:
1055. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] 자신의 ([HanafudaCombo] 위력 - 1)만큼 이 코인 재사용 (최대 4회)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [HanafudaCombo]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】
   EN: Reuse this Coin ([HanafudaCombo] Potency - 1) times (4 times max)<style="highlight"></style>
   PL:
1056. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 1013 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1057. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1058. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] <style="highlight">[OnSucceedAttackHead] [DefenseDown] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [DefenseDown]</style>
   PL:
1059. [Obrona (ulepszenia 1,4) — nazwa] 화투패 섞기
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].name ; dataList[id=1081304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Shuffle Hands - Floral Deck
   PL:
1060. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 [Discard] (턴당 1회)\n[StartBattle] 자신의 가장 왼쪽 슬롯에 장착했으면, 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회. 보유한 ‘짝패’와 동일한 ‘짝패’ 제외)
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [Discard]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [Discard] = 버림 / Discard
   EN: [DuelCounter]\n[StartBattle] [Discard] 2 Skills of the lowest rank in all of this unit's Skill Slots (once per turn)\n[StartBattle] If this Skill was equipped on this unit's leftmost Skill Slot, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills next turn. (once per turn; excluding the Suit already in this unit's Hand)
   PL:
1061. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1062. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 [Discard] (턴당 1회)\n[StartBattle] 자신의 가장 왼쪽 슬롯에 장착했으면, 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회. 보유한 ‘짝패’와 동일한 ‘짝패’ 제외)\n<style="highlight">[StartBattle] 50% 확률로 [HanafudaCombo] 위력 1 얻음 (턴당 1회)</style>\n<style="highlight">[WhenUse] 자신의 [HanafudaCombo] 위력 2당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=4].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [Discard], [HanafudaCombo], [WhenUse]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [Discard] = 버림 / Discard; [HanafudaCombo] = 광【光】 / Bright【光】; [WhenUse] = [사용시] / [On Use]
   EN: [DuelCounter]\n[StartBattle] [Discard] 2 Skills of the lowest rank in all of this unit's Skill Slots (once per turn)\n[StartBattle] If this Skill was equipped on this unit's leftmost Skill Slot, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills next turn. (once per turn; excluding the Suit already in this unit's Hand)\n<style="highlight">[StartBattle] 50% chance to gain 1 [HanafudaCombo] Potency (once per turn)</style>\n<style="highlight">[WhenUse] Coin Power +1 for every 2 [HanafudaCombo] Potency on self (max 2)</style>
   PL:
1064. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1065. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1025 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1066. [Pasywka bojowa (od ulepszenia 1) — nazwa] 코이코이[こいこい]
   źródło: Passives.json :: dataList[id=1081302].name
   limit: do 40 znaków
   EN: Koi-Koi [こいこい]
   PL:
1067. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작시 [HanafudaCombo]이 없으면, [HanafudaCombo] 위력 0, 횟수 3 얻음\n\n턴 시작시 ‘짝패’가 없으면, [HanafudaOne], [HanafudaTwo], [HanafudaThree] 중 자신의 가장 왼쪽 슬롯의 기본 공격 스킬에 대응되는 무작위 ‘짝패’ 얻음\n\n전투 시작시 자신의 가장 왼쪽 슬롯에 장착한 기본 공격 스킬 또는 E.G.O 스킬이 사용될 때 아래 효과 적용 (턴당 1회)\n- 다음 턴에 해당 스킬에 대응되는 ‘짝패’로 변경\n- '사쿠라센' 또는 E.G.O 스킬이면, [HanafudaCombo] 위력 1 얻음\n- 해당 스킬 속성이 ‘짝패’와 일치하면, 아래 효과 적용\n  · [HanafudaCombo] 위력 1 얻음\n  · 이전 턴과 연속으로 ‘짝패’가 일치했으면, [HanafudaCombo] 위력 1 얻음\n  · 해당 스킬 적중 시 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n  · 25% 확률로 해당 스킬 속성의 E.G.O 자원 1 얻음\n- 해당 스킬 종료 시 [HanafudaCombo] 위력이 5거나, 횟수가 0이면, '코오쟌' 발동
   źródło: Passives.json :: dataList[id=1081302].desc
   limit: do 1500 znaków
   tokeny: zachowaj dokładnie: \n, [HanafudaCombo], [HanafudaOne], [HanafudaTwo], [HanafudaThree], [VibrationExplosion], [Vibration]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】; [HanafudaOne] = 짝패 - 송학 / Hand - Pine Crane Suit; [HanafudaTwo] = 짝패 - 억새 / Hand - Susuki Grass Suit; [HanafudaThree] = 짝패 - 청벚꽃 / Hand - Blue Sakura Suit; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: Turn Start: if this unit does not have [HanafudaCombo], gain 0 [HanafudaCombo] Potency and 3 [HanafudaCombo] Count\n\nTurn Start: if this unit does not have a Suit in Hand, gain a random Suit([HanafudaOne], [HanafudaTwo], or [HanafudaThree]) that corresponds to a Base Attack Skill on this unit's leftmost Skill Slot\n\nCombat Start: when this unit uses a Base Attack Skill or an E.G.O Skill equipped on its leftmost Skill Slot, activate the following (once per turn):\n- Next turn, convert the Hand on self to the one corresponding to the used Skill's Affinity\n- If the Skill was either "Sakura-sen" or an E.G.O Skill, gain 1 [HanafudaCombo] Potency\n- If the Skill's Affinity matches the Affinity on the current Hand's description(thus "forming a Hand"), activate the following:\n  · Gain 1 [HanafudaCombo] Potency\n  · If this unit formed a Hand last turn and this turn in succession, gain 1 [HanafudaCombo] Potency\n  · On Hit with the said Skill: trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n  · 25% chance to gain 1 E.G.O Resource corresponding to the Skill's Affinity\n- At the Skill's Skill End: at 5 [HanafudaCombo] Potency, or at 0 [HanafudaCombo] Count, use "Kōzan"
   PL:
1068. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 짝패를 맞추면, [HanafudaCombo] 얻음. 진동 폭발.
   źródło: Passives.json :: dataList[id=1081302].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [HanafudaCombo]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】
   EN: When forming a Hand, gain [HanafudaCombo]. Trigger Tremor Burst.
   PL:
1069. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Gloom) — nazwa] 낱장치기
   źródło: Passives.json :: dataList[id=1081301].name
   limit: do 40 znaków
   EN: Stacking the Deck
   PL:
1070. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Gloom) — opis] 뒷면 적중 시 정신력 5 회복 (턴 당 1회)\n사기 저하 또는 패닉 상태인 적에게 가하는 피해량 +10%
   źródło: Passives.json :: dataList[id=1081301].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Tails Hit, heal 5 SP (once per turn)\nDeal +10% damage against targets in either Low Morale or Panic states
   PL:
1071. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Gloom) — podsumowanie] 정신력 회복\n사기 저하, 패닉 대상에게 가하는 피해량 증가
   źródło: Passives.json :: dataList[id=1081301].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heal SP\nDeal more damage against Low Morale or Panicked targets
   PL:
1072. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth, posiadane 3× Gloom) — nazwa] 중계
   źródło: Passives.json :: dataList[id=1081321].name
   limit: do 40 znaków
   EN: Relay
   PL:
1073. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth, posiadane 3× Gloom) — opis] 전투 시작시 정신력이 가장 낮은 아군 1명이 기본 공격 스킬로 앞면 적중시 해당 아군 정신력 5 회복 (턴당 2회, 정신력이 -40 이하인 아군 제외)
   źródło: Passives.json :: dataList[id=1081321].desc
   limit: do 200 znaków
   EN: Combat Start: when 1 ally that has the least SP uses a Base Attack Skill to Heads Hit, it heals 5 SP (2 times per turn; excluding allies at -40 or lower SP)
   PL:
1074. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth, posiadane 3× Gloom) — podsumowanie] 정신력 회복
   źródło: Passives.json :: dataList[id=1081321].summary
   limit: do 120 znaków
   EN: Heal SP
   PL:
1075. [Kwestia głosowa [get_10813_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=get_10813_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1076. [Kwestia głosowa [get_10813_1] (Identity Acquisition)] 사람은 꽃으로도 때리지 말라… 던가요. 허, 저희 집 꽃은 사람 패는데 이골이 나있는데 말이죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=get_10813_1].dlg
   limit: do 190 znaków
   EN: You know what they say—sometimes in life, you gotta stop and smell the flowers. Hah, too bad people we deal with often end up pushing daisies.
   PL:
1077. [Kwestia głosowa [lobby_morning_10813_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=lobby_morning_10813_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1078. [Kwestia głosowa [lobby_morning_10813_1] (Morning Greeting)] 도박장에 빌붙어서 돈버는 사람으로서 말하기는 좀 그런데… 저 사람들, 꼭두새벽부터 도박판에 앉아 있으면 판돈은 어디서 벌어오는 걸까요?\n…하긴 벌 곳이 없으니 여기서 일발역전이나 노리다가 저희한테 정리되는 거겠지만.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=lobby_morning_10813_1].dlg
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I know it's a strange question for someone working in this line of business to be asking, but... I wonder how they bankroll themselves? I'm talking about gamblers like those guys over there whose asses are parked in gambling dens all day, all night.\n... Well, I guess that explains why they spend most of their days chasing after that one life-changing win before people like us deal with them.
   PL:
1079. [Kwestia głosowa [lobby_noon_10813_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=lobby_noon_10813_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1080. [Kwestia głosowa [lobby_noon_10813_1] (Afternoon Greeting)] 저희는 화투패로 하는 거라면 전문으로 입회를 담당하고 있죠. 포커나 마작같이 다른 물건들을 사용하는 건 그쪽 전문가에게 의뢰하시고요.\n뭐, 못하는 건 아니지만… 중요한 판일수록 전문 입회인이 들어가는게 상식이니까요. 화투패로 딱지내기를 하더라도 말이예요.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=lobby_noon_10813_1].dlg
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Games played with any of those flower cards—Hwatu, Hanafuda—are our specialty. Find different specialists if you're looking for someone to observe games played with other stuff, like poker or mahjong.\nWell, I guess we <i>could</i> take your contract for those games too, but... it's common sense to have a specialist present for high-roller games. Even if you're just playing ddakji with these cards.
   PL:
1081. [Kwestia głosowa [lobby_night_10813_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=lobby_night_10813_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1082. [Kwestia głosowa [lobby_night_10813_1] (Evening Greeting)] 이 밤에 여긴 왜 자꾸 알짱거려요? 지금이 제일 민감한 시간이니까… 괜히 걸리적거리지 말고 안전한데로 가시죠.\n특히 저기… 눈동자에 초점이 없는 사람이랑, 손목 한쪽이 날아가서 버려진 사람 근처엔 가지도 마시고.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=lobby_night_10813_1].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hey, what are you doing loitering around here at night? Don't get yourself in trouble and go someplace safer—it's like a powder keg in here right now.\nAnd especially steer clear of those two over there, got that? Yeah, that guy with dead eyes, and that one over there who's just got a hand chopped off.
   PL:
1083. [Kwestia głosowa [smalltalk_10813_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1084. [Kwestia głosowa [smalltalk_10813_1] (Chatter #1)] 끗발이 자꾸 자기한테만 붙는 것 같으면 한번쯤 의심을 해야하는 건데요… 그 판의 호구가 누구일지.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_1].dlg
   limit: do 180 znaków
   EN: If you feel like you're on a lucky streak that's too good to be true... You might want to pause and see if you're the "sucker" in that game.
   PL:
1085. [Kwestia głosowa [smalltalk_10813_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1086. [Kwestia głosowa [smalltalk_10813_2] (Chatter #2)] 뭐, 어디에나 있잖아요. 승부가 갈렸는데도 난 인정 못 한다, 저 녀석이 반칙을 했다… 그런 시정잡배들. 저희 사무소는 그런 사람들이 말썽을 일으키지 않게 개입하는 일을 해요.\n따지자면 외우피 협회의 공증인거죠… 뭐, 그러니까 외우피 산하에 붙어 일하는 거지만.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_2].dlg
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Well, you know the type. People who accuse their opponents of cheating because they can't admit they lost... You know, sore losers. Our Office's job usually entails making sure they don't kick up a fuss.\nYeah, kinda like how Öufi oversees contracts... Which is why we're working under their umbrella, I suppose.
   PL:
1087. [Kwestia głosowa [smalltalk_10813_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1088. [Kwestia głosowa [smalltalk_10813_3] (Chatter #3)] 언젠가는… 저기 꼭대기에 있는 다이아몬드… 그중에서도 천외천들만 참가한다는 블루 다이아몬드 갬블의 입회에 들어가고 싶어요. 뭐, 돈을 더 벌고 싶다기 보단… 그것도 나쁘진 않은데.\n이쪽 업계에서는 그만큼 커리어를 인정받는 일도 없으니까요. 실력 없으면 부르지도 않으니.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_3].dlg
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One day, I'd like to oversee a Blue Diamond game that takes place way up on the top floor. You know, the Diamond games where only the highest of high-rollers get to participate. Sure, a good payday's nice, but... sometimes, it's not all about the money.\nIt's just that in this business, there's no better acknowledgment of my career than getting called to oversee a game that only employs the best of the best.
   PL:
1089. [Kwestia głosowa [smalltalk_10813_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_4].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1090. [Kwestia głosowa [smalltalk_10813_4] (Post-Uptie Chat 1)] 이럴 줄 알았죠. 금방 아수라장이 날 것 같더라니. 자, 거기! 딱 멈춰요. 지금부터 이 테이블에서 벗어나거나, 화투짝 건드리거나, 재채기라도 하면… 그대로 손목째로 썰어버릴테니까.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_4].dlg
   limit: do 280 znaków
   EN: Had a feeling this game wasn't going to waste any time turning into a shitshow. Alright, you! Stop right there. Anyone who tries to leave this table, touch a card, or so much as even sneeze... I'll chop off your hands.
   PL:
1091. [Kwestia głosowa [smalltalk_10813_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_5].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1092. [Kwestia głosowa [smalltalk_10813_5] (Post-Uptie Chat 2)] 낮장밤일, 밤일낮장. 지금 새벽이 된 지가 언젠데 아직도 그거로 시비죠? 잔 말 말고 당신이 졌으니까 돈 뱉어내시죠.\n뭐… 이번 입회 규칙에 의하면 창자를 뱉어내셔도 상관 없긴 한데. 도와드려요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=smalltalk_10813_5].dlg
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Low at Night, High at Day." For night games, the smallest draw goes first; for day games, the highest draw. We've been sitting through the daybreak the whole time, folks. Why are we still arguing about this? You lost, so quit arguing and cough it up.\nOh, by the way... according to the rules of this game as observed by us, you can also choose to cough up your entrails. Let me know if you need a hand.
   PL:
1093. [Kwestia głosowa [gacksung_10813_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=gacksung_10813_1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1094. [Kwestia głosowa [gacksung_10813_1] (Uptying)] 거기까지. 낙장불입입니다. 한 번 패를 냈으면… 아무리 개같은 상황이셔도, 물릴 순 없죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=gacksung_10813_1].dlg
   limit: do 150 znaków
   EN: Nope. The card's out in the open... there's no forfeiting once the die is cast. No matter how screwed you are.
   PL:
1095. [Kwestia głosowa [neglect_10813_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=neglect_10813_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1096. [Kwestia głosowa [neglect_10813_1] (Idle)] …휘유, 고코(五光)? 저걸 실화로 쳐서 뽑네.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=neglect_10813_1].dlg
   limit: do 120 znaków
   EN: ... *whistle* Gokō? Hard to believe that wasn't a sleight of hand.
   PL:
1097. [Kwestia głosowa [formation_10813_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=formation_10813_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1098. [Kwestia głosowa [formation_10813_1] (Deployment)] 가시죠. 화투패 입회 의뢰인가요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=formation_10813_1].dlg
   limit: do 120 znaków
   EN: Let's head out. Are we attending as observers to a Hwatu Card game for this contract?
   PL:
1099. [Kwestia głosowa [battleentry_10813_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battleentry_10813_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1100. [Kwestia głosowa [battleentry_10813_1] (Stage Entry)] 자, 판 돌아 갑니다.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battleentry_10813_1].dlg
   limit: do 120 znaków
   EN: Alright, bets on the table.
   PL:
1101. [Kwestia głosowa [battle_select_10813_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_select_10813_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1102. [Kwestia głosowa [battle_select_10813_1] (Viewed in Battle)] 이미 입회중입니다. 제게 말을 거는건 룰 위반이죠.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_select_10813_1].dlg
   limit: do 120 znaków
   EN: I'm already carrying out my duties as an observer. Chatting me up is a rule violation.
   PL:
1103. [Kwestia głosowa [battle_endcommand_10813_1] — sytuacja] 공격시작
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_endcommand_10813_1].desc
   (powtórzenie elementu 875 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1104. [Kwestia głosowa [battle_endcommand_10813_1] (Commencing Attack)] 당신, 짝패군요!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_endcommand_10813_1].dlg
   limit: do 120 znaków
   EN: Hey now, that makes a matching hand!
   PL:
1105. [Kwestia głosowa [battle_enemy_break_10813_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_enemy_break_10813_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1106. [Kwestia głosowa [battle_enemy_break_10813_1] (Enemy Stagger)] 좋아, 코이코이!
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_enemy_break_10813_1].dlg
   limit: do 120 znaków
   EN: Let's go! Koi-koi!
   PL:
1107. [Kwestia głosowa [battle_break_10813_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_break_10813_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1108. [Kwestia głosowa [battle_break_10813_1] (Staggered)] 이딴 개패가…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_break_10813_1].dlg
   limit: do 120 znaków
   EN: What a shitty hand...
   PL:
1109. [Kwestia głosowa [battle_kill_10813_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_kill_10813_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1110. [Kwestia głosowa [battle_kill_10813_1] (Enemy Killed)] 흥, 올인이었나요?
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_kill_10813_1].dlg
   limit: do 120 znaków
   EN: Hmph. You went all-in, didn't you?
   PL:
1111. [Kwestia głosowa [battle_dead_10813_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_dead_10813_1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1112. [Kwestia głosowa [battle_dead_10813_1] (Death)] 내가 구석에 몰릴 줄이야…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_dead_10813_1].dlg
   limit: do 120 znaków
   EN: Never thought I'd be cornered like this...
   PL:
1113. [Kwestia głosowa [choice_success_p_10813_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=choice_success_p_10813_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1114. [Kwestia głosowa [choice_success_p_10813_2] (Check Passed)] 흠, 장땡.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=choice_success_p_10813_2].dlg
   limit: do 120 znaków
   EN: Hmm. Jangttaeng.
   PL:
1115. [Kwestia głosowa [choice_fail_n_10813_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=choice_fail_n_10813_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1116. [Kwestia głosowa [choice_fail_n_10813_1] (Check Failed)] …망통이 뜨냐, 어떻게…
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=choice_fail_n_10813_1].dlg
   limit: do 120 znaków
   EN: ... Mangtong? Shit, that's the worst possible hand...
   PL:
1117. [Kwestia głosowa [battle_clear_10813_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_clear_10813_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1118. [Kwestia głosowa [battle_clear_10813_1] (Victory Cry)] 그러니까 재밌게 놀다 가시기나 하지, 왜 승질을 부려서 이 꼴을 내나요… 어휴, 이 돈은 이번 입회 규칙에 따라 처리해두겠습니다. 이럴 줄 알았으면 주인 없는 돈이 생겼을 때 입회인이 챙기는 비율 좀 늘려서 계약할 걸.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_clear_10813_1].dlg
   limit: do 390 znaków
   EN: Couldn't you have just enjoyed the game without losing your cool? Seriously, you only have yourself to blame for this mess... *sigh* These notes will be processed as per the game rules observed by our party. I should've raised the observer's cut for unclaimed cash in the contract... If only I'd known.
   PL:
1119. [Kwestia głosowa [battle_clear_ex_10813_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_clear_ex_10813_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1120. [Kwestia głosowa [battle_clear_ex_10813_1] (Extra Conditions Fulfilled)] 도박장 째로 의뢰를 냈다 싶더니… 이렇게나 밑장 빼는 놈들이 한 가득일 줄이야. 후… 한 달은 의뢰 없이 놀아도 되겠는데요? 사무소 노났네.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_clear_ex_10813_1].dlg
   limit: do 260 znaków
   EN: I see now why they hired us for the whole gambling den... This hole's full of cheating bottom dealers. Whew... we should be set for the next month even if we don't pick up a single contract. Hell yeah.
   PL:
1121. [Kwestia głosowa [battle_defeat_10813_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_defeat_10813_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1122. [Kwestia głosowa [battle_defeat_10813_1] (Defeat Wail)] 이 판은… 죽습니다. 이래가지곤 의뢰고 뭐고 제 몸 하나 건사하기도 어려워서… 하, 사무소에서 사람을 더 끌고 나와야겠네.
   źródło: PersonalityVoiceDlg/Voice_Ishmael_Hanafuda_10813.json :: dataList[id=battle_defeat_10813_1].dlg
   limit: do 200 znaków
   EN: I think I'll... fold this round. Can't finish the contract if I'm too dead to carry it out, right? Hah, I've got to get reinforcements from the office.
   PL:
